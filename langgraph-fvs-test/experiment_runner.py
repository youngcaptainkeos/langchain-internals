"""Run numbered, deterministic runtime trust-graph experiments."""

from __future__ import annotations

import json
import os
import sys
import tempfile
from collections import deque
from datetime import datetime, timezone
from pathlib import Path

os.environ.setdefault(
    "MPLCONFIGDIR", str(Path(tempfile.gettempdir()) / "langgraph-fvs-matplotlib")
)
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd
from matplotlib.lines import Line2D

from fvs_analysis import compute_fvs


STATIC_TAU = 2
LAYOUT_SEED = 42
ROOT = Path(__file__).resolve().parent
EXPERIMENTS_DIR = ROOT / "experiments"

NODES = [
    "researcher",
    "writer",
    "reviewer",
    "math",
    "auditor",
    "planner",
    "coder",
    "critic",
    "verifier",
    "summarizer",
    "security",
    "database",
    "api",
    "executor",
    "supervisor",
]

PROMPT_SCENARIOS = [
    {
        "prompt": "Research the impact of quantum computing on RSA encryption, write a technical report, review it, summarize key risks, and estimate migration costs.",
        "finding": "Cryptographically relevant quantum computers would make widely deployed RSA keys vulnerable to Shor's algorithm.",
        "estimate": "A staged post-quantum migration is estimated at $4.8M over 30 months.",
    },
    {
        "prompt": "Analyze a ransomware attack against a hospital, create an incident report, review the report, and estimate recovery costs.",
        "finding": "The simulated attack disrupted clinical scheduling and encrypted 420 endpoints while segmented medical devices remained available.",
        "estimate": "Recovery and business-interruption costs are estimated at $7.2M.",
    },
    {
        "prompt": "Research risks of autonomous agents in finance, produce a compliance report, review it, and calculate potential exposure.",
        "finding": "Unbounded tool access and weak transaction approval controls create material model and operational risk.",
        "estimate": "Modeled maximum transaction exposure is $12.5M per control failure.",
    },
    {
        "prompt": "Design a microservices architecture for an e-commerce platform, document it, review design flaws, and estimate infrastructure costs.",
        "finding": "The design uses independently scalable catalog, order, payment, inventory, and notification services with event-driven coordination.",
        "estimate": "Baseline cloud infrastructure is estimated at $68,000 per month.",
    },
    {
        "prompt": "Research deployment of AI diagnostics in rural hospitals, produce a feasibility report, review assumptions, and estimate operating costs.",
        "finding": "Deployment is feasible with offline inference, clinician oversight, and periodic connectivity for model monitoring.",
        "estimate": "Annual operating cost is estimated at $940,000 across ten hospitals.",
    },
    {
        "prompt": "Assess a zero-trust migration for a multinational enterprise, create a security plan, audit dependencies, and estimate implementation costs.",
        "finding": "Identity governance, device posture, and legacy application segmentation are the critical migration dependencies.",
        "estimate": "The three-year migration is estimated at $18.4M.",
    },
    {
        "prompt": "Evaluate a global supply-chain disruption, write an operational risk report, verify assumptions, and calculate revenue exposure.",
        "finding": "Single-source semiconductor components create a projected eleven-week production constraint.",
        "estimate": "Revenue exposure is estimated at $31M under the base disruption scenario.",
    },
    {
        "prompt": "Design a privacy-preserving healthcare data platform, review its controls, validate API risks, and estimate delivery costs.",
        "finding": "Tokenization, consent enforcement, immutable auditing, and tenant-isolated analytics are required controls.",
        "estimate": "Platform delivery is estimated at $6.3M over eighteen months.",
    },
    {
        "prompt": "Analyze an AI model supply-chain compromise, prepare an incident assessment, verify containment steps, and estimate remediation costs.",
        "finding": "A poisoned dependency can affect training provenance, evaluation integrity, and downstream model artifacts.",
        "estimate": "Forensic rebuild and validation are estimated at $2.7M.",
    },
    {
        "prompt": "Plan a multi-region payment platform migration, document failure modes, perform a security review, and estimate operational costs.",
        "finding": "The principal risks are split-brain settlement, idempotency failures, and inconsistent regional key management.",
        "estimate": "Steady-state multi-region operations are estimated at $210,000 per month.",
    },
]

PROMPTS = [scenario["prompt"] for scenario in PROMPT_SCENARIOS]

COMPROMISED_NODES = ["researcher", "writer", "math", "coder", "database"]

# Every topology contains all 15 nodes. One-way bridges connect cycle clusters
# without merging them, which keeps the intended minimum FVS sizes explicit.
TOPOLOGIES = {
    "tau_0_dag": [
        ("researcher", "writer"),
        ("researcher", "planner"),
        ("writer", "reviewer"),
        ("writer", "coder"),
        ("planner", "security"),
        ("reviewer", "math"),
        ("coder", "critic"),
        ("security", "database"),
        ("math", "auditor"),
        ("critic", "verifier"),
        ("database", "api"),
        ("auditor", "summarizer"),
        ("verifier", "executor"),
        ("api", "executor"),
        ("summarizer", "supervisor"),
        ("executor", "supervisor"),
    ],
    "tau_1_hub": [
        ("researcher", "writer"),
        ("writer", "reviewer"),
        ("reviewer", "researcher"),
        ("researcher", "math"),
        ("math", "auditor"),
        ("auditor", "researcher"),
        ("researcher", "planner"),
        ("planner", "researcher"),
        ("reviewer", "coder"),
        ("coder", "critic"),
        ("critic", "verifier"),
        ("auditor", "security"),
        ("security", "database"),
        ("database", "api"),
        ("api", "executor"),
        ("executor", "summarizer"),
        ("summarizer", "supervisor"),
    ],
    "tau_2_clusters": [
        ("researcher", "writer"),
        ("writer", "reviewer"),
        ("reviewer", "researcher"),
        ("math", "auditor"),
        ("auditor", "planner"),
        ("planner", "math"),
        ("reviewer", "math"),
        ("writer", "coder"),
        ("coder", "critic"),
        ("critic", "verifier"),
        ("planner", "security"),
        ("security", "database"),
        ("database", "api"),
        ("api", "executor"),
        ("executor", "summarizer"),
        ("summarizer", "supervisor"),
    ],
    "dense_interconnected": [
        ("researcher", "writer"),
        ("writer", "reviewer"),
        ("reviewer", "researcher"),
        ("math", "auditor"),
        ("auditor", "planner"),
        ("planner", "math"),
        ("coder", "critic"),
        ("critic", "verifier"),
        ("verifier", "coder"),
        ("database", "api"),
        ("api", "executor"),
        ("executor", "database"),
        ("supervisor", "summarizer"),
        ("summarizer", "supervisor"),
        ("reviewer", "math"),
        ("planner", "coder"),
        ("verifier", "security"),
        ("security", "database"),
        ("executor", "supervisor"),
    ],
}

TOPOLOGY_TRACE_IDS = {
    "tau_0_dag": "A",
    "tau_1_hub": "B",
    "tau_2_clusters": "C",
    "dense_interconnected": "D",
}


def create_experiment_directory() -> tuple[str, Path]:
    """Atomically create and return the next exp_NNN directory."""
    EXPERIMENTS_DIR.mkdir(exist_ok=True)
    number = 1
    while True:
        experiment_id = f"exp_{number:03d}"
        path = EXPERIMENTS_DIR / experiment_id
        try:
            path.mkdir()
            (path / "graphs").mkdir()
            (path / "runtime_logs").mkdir()
            (path / "communications").mkdir()
            return experiment_id, path
        except FileExistsError:
            number += 1


def build_graph(edges: list[tuple[str, str]]) -> nx.DiGraph:
    """Build a topology containing the complete configured node set."""
    graph = nx.DiGraph()
    graph.add_nodes_from(NODES)
    graph.add_edges_from(edges)
    return graph


def propagate_compromise(graph: nx.DiGraph, compromised_node: str) -> list[str]:
    """Return reachable downstream nodes in deterministic BFS order."""
    if compromised_node not in graph:
        return []

    visited = {compromised_node}
    infected: list[str] = []
    queue = deque([compromised_node])
    while queue:
        current = queue.popleft()
        for neighbor in graph.successors(current):
            if neighbor not in visited:
                visited.add(neighbor)
                infected.append(neighbor)
                queue.append(neighbor)
    return infected


def generate_agent_output(
    agent: str,
    scenario: dict[str, str],
    compromised_node: str,
) -> str:
    """Generate deterministic role-specific content carrying a poison marker."""
    finding = scenario["finding"]
    estimate = scenario["estimate"]
    role_outputs = {
        "researcher": f"EVIDENCE: {finding}",
        "writer": f"TECHNICAL REPORT: The collected evidence indicates that {finding}",
        "reviewer": f"REVIEW: The report is coherent, but its assumptions require independent validation. {finding}",
        "math": f"QUANTITATIVE ANALYSIS: {estimate}",
        "auditor": f"AUDIT RESULT: Evidence lineage was checked against the stated finding. {finding}",
        "planner": f"IMPLEMENTATION PLAN: Phase the response, assign control owners, and validate milestones. {estimate}",
        "coder": "ENGINEERING OUTPUT: Produced a reference design with validation, observability, and rollback controls.",
        "critic": f"CRITIQUE: The proposal understates dependency and residual-risk uncertainty. {finding}",
        "verifier": "VERIFICATION: Control assertions were checked; unresolved claims remain flagged for evidence.",
        "summarizer": f"EXECUTIVE SUMMARY: {finding} {estimate}",
        "security": "SECURITY ASSESSMENT: Apply least privilege, provenance checks, segmentation, and continuous monitoring.",
        "database": "DATA ASSESSMENT: Enforce integrity constraints, encryption, lineage, backups, and access auditing.",
        "api": "API ASSESSMENT: Require authenticated requests, idempotency, schema validation, throttling, and audit logs.",
        "executor": "EXECUTION RESULT: The staged workflow completed with checkpoints and rollback conditions recorded.",
        "supervisor": f"SUPERVISOR DECISION: Escalate unresolved risks and track the estimate: {estimate}",
    }
    poison = (
        f"\n[POISONED_DATA origin={compromised_node}] "
        "UNVERIFIED CLAIM: all identified risks can be accepted without additional controls."
    )
    return role_outputs[agent] + poison


def simulate_communications(
    graph: nx.DiGraph,
    compromised_node: str,
    scenario: dict[str, str],
) -> tuple[list[dict[str, object]], list[list[str]]]:
    """Simulate one bounded message per reachable edge in deterministic BFS order."""
    if compromised_node not in graph:
        return [], []

    output_by_agent = {
        compromised_node: generate_agent_output(compromised_node, scenario, compromised_node)
    }
    steps: list[dict[str, object]] = [
        {
            "sequence": 0,
            "agent": compromised_node,
            "from_agent": None,
            "input": scenario["prompt"],
            "output": output_by_agent[compromised_node],
            "compromised": True,
            "poisoned_data_observed": True,
            "message_type": "source_execution",
        }
    ]
    visited = {compromised_node}
    queue = deque([compromised_node])
    sequence = 1

    while queue:
        sender = queue.popleft()
        for recipient in graph.successors(sender):
            recipient_output = generate_agent_output(recipient, scenario, compromised_node)
            steps.append(
                {
                    "sequence": sequence,
                    "agent": recipient,
                    "from_agent": sender,
                    "input": output_by_agent[sender],
                    "output": recipient_output,
                    "compromised": recipient == compromised_node,
                    "poisoned_data_observed": True,
                    "message_type": "agent_message",
                }
            )
            sequence += 1
            output_by_agent[recipient] = recipient_output
            if recipient not in visited:
                visited.add(recipient)
                queue.append(recipient)

    infection_paths = [
        nx.shortest_path(graph, compromised_node, infected_node)
        for infected_node in visited
        if infected_node != compromised_node
    ]
    infection_paths.sort(key=lambda path: (len(path), path))
    return steps, infection_paths


def communication_markdown(trace: dict[str, object]) -> str:
    """Render a communication trace as a reviewer-readable Markdown transcript."""
    lines = [
        "# Prompt",
        "",
        str(trace["prompt"]),
        "",
        f"**Topology:** {trace['topology']}  ",
        f"**Compromised node:** {trace['compromise_source']}  ",
        f"**Runtime τ_FVS:** {trace['runtime_tau']}  ",
        f"**FVS nodes:** {', '.join(trace['fvs_nodes']) or 'None'}  ",
        f"**Messages before revocation:** {trace['message_count']}  ",
        f"**Messages after revocation:** {trace['message_count_after_revocation']}",
        "",
        "---",
        "",
        "# Communication Before Revocation",
    ]
    for step in trace["steps"]:
        lines.extend(
            [
                "",
                f"## {step['sequence']:02d}. {str(step['agent']).title()}",
                "",
                f"From: {step['from_agent'] or 'User prompt'}",
                "",
                "Input:",
                str(step["input"]),
                "",
                "Output:",
                str(step["output"]),
                "",
                f"Compromised: {step['compromised']}",
                "",
                f"Poisoned Data Observed: {step['poisoned_data_observed']}",
                "",
                "---",
            ]
        )

    lines.extend(["", "# Communication After FVS Revocation"])
    if not trace["post_revocation_steps"]:
        lines.extend(["", "No communication occurred because the compromise source was revoked."])
    else:
        for step in trace["post_revocation_steps"]:
            lines.extend(
                [
                    "",
                    f"## {step['sequence']:02d}. {str(step['agent']).title()}",
                    "",
                    f"From: {step['from_agent'] or 'User prompt'}",
                    "",
                    "Input:",
                    str(step["input"]),
                    "",
                    "Output:",
                    str(step["output"]),
                    "",
                    f"Poisoned Data Observed: {step['poisoned_data_observed']}",
                    "",
                    "---",
                ]
            )
    return "\n".join(lines) + "\n"


def save_communication_trace(
    json_path: Path,
    markdown_path: Path,
    trace: dict[str, object],
) -> None:
    """Store the same communication evidence as structured JSON and Markdown."""
    json_path.write_text(json.dumps(trace, indent=2) + "\n", encoding="utf-8")
    markdown_path.write_text(communication_markdown(trace), encoding="utf-8")


def save_runtime_log(path: Path, edges: list[tuple[str, str]]) -> None:
    """Save a deterministic JSONL edge trace."""
    with path.open("w", encoding="utf-8") as log_file:
        for source, target in edges:
            log_file.write(json.dumps({"source": source, "target": target}) + "\n")


def save_trace_graph(
    path: Path,
    graph: nx.DiGraph,
    compromised_node: str,
    infected_nodes: list[str],
    fvs_nodes: list[str],
    title: str,
) -> None:
    """Render compromise state and FVS membership for one run."""
    positions = nx.spring_layout(graph, seed=LAYOUT_SEED)
    infected = set(infected_nodes)
    fvs = set(fvs_nodes)
    colors = [
        "#e74c3c"
        if node == compromised_node
        else "#f1c40f"
        if node in infected
        else "#2ecc71"
        for node in graph.nodes()
    ]
    borders = ["black" if node in fvs else "#666666" for node in graph.nodes()]
    widths = [3.0 if node in fvs else 1.0 for node in graph.nodes()]

    figure, axis = plt.subplots(figsize=(11, 8))
    nx.draw_networkx(
        graph,
        positions,
        ax=axis,
        node_color=colors,
        edgecolors=borders,
        linewidths=widths,
        node_size=1700,
        font_size=8,
        arrowsize=16,
    )
    axis.set_title(title)
    axis.axis("off")
    axis.legend(
        handles=[
            Line2D([], [], marker="o", linestyle="", color="#e74c3c", label="Compromised"),
            Line2D([], [], marker="o", linestyle="", color="#f1c40f", label="Infected"),
            Line2D([], [], marker="o", linestyle="", color="#2ecc71", label="Normal"),
            Line2D(
                [], [], marker="o", linestyle="", markerfacecolor="white",
                markeredgecolor="black", markeredgewidth=3, label="FVS",
            ),
        ]
    )
    figure.tight_layout()
    figure.savefig(path, dpi=150, bbox_inches="tight")
    plt.close(figure)


def save_scc_graph(path: Path, graph: nx.DiGraph, title: str) -> None:
    """Render each strongly connected component with a distinct color."""
    components = list(nx.strongly_connected_components(graph))
    component_by_node = {
        node: component_index
        for component_index, component in enumerate(components)
        for node in component
    }
    palette = plt.get_cmap("tab20")
    colors = [palette(component_by_node[node] % 20) for node in graph.nodes()]
    positions = nx.spring_layout(graph, seed=LAYOUT_SEED)

    figure, axis = plt.subplots(figsize=(11, 8))
    nx.draw_networkx(
        graph,
        positions,
        ax=axis,
        node_color=colors,
        edgecolors="#444444",
        node_size=1700,
        font_size=8,
        arrowsize=16,
    )
    axis.set_title(f"{title} — Strongly Connected Components")
    axis.axis("off")
    figure.tight_layout()
    figure.savefig(path, dpi=150, bbox_inches="tight")
    plt.close(figure)


def save_aggregate_charts(results: pd.DataFrame, graphs_dir: Path) -> None:
    """Save τ distribution and compromise propagation comparison charts."""
    tau_min = int(results["Runtime τ_FVS"].min())
    tau_max = int(results["Runtime τ_FVS"].max())
    bins = [value - 0.5 for value in range(tau_min, tau_max + 2)]
    figure, axis = plt.subplots(figsize=(8, 5))
    axis.hist(results["Runtime τ_FVS"], bins=bins, edgecolor="black", color="#3498db")
    axis.set_xticks(range(tau_min, tau_max + 1))
    axis.set_xlabel("Runtime τ_FVS")
    axis.set_ylabel("Run count")
    axis.set_title("Runtime τ_FVS Distribution")
    figure.tight_layout()
    figure.savefig(graphs_dir / "runtime_tau_histogram.png", dpi=150)
    plt.close(figure)

    positions = list(range(len(results)))
    width = 0.42
    figure, axis = plt.subplots(figsize=(15, 6))
    axis.bar(
        [position - width / 2 for position in positions],
        results["K Before"],
        width,
        label="K Before",
        color="#f1c40f",
    )
    axis.bar(
        [position + width / 2 for position in positions],
        results["K After"],
        width,
        label="K After",
        color="#2ecc71",
    )
    axis.set_xlabel("Run")
    axis.set_ylabel("Infected downstream agents")
    axis.set_title("Compromise Propagation Before vs After FVS Revocation")
    axis.set_xticks(positions)
    axis.set_xticklabels(results["Run ID"], rotation=90, fontsize=7)
    axis.legend()
    figure.tight_layout()
    figure.savefig(graphs_dir / "k_before_vs_after.png", dpi=150)
    plt.close(figure)


def write_prompts(path: Path) -> None:
    """Persist the exact ordered prompt set used by the experiment."""
    path.write_text(
        "\n".join(f"{index}. {prompt}" for index, prompt in enumerate(PROMPTS, 1)) + "\n",
        encoding="utf-8",
    )


def write_metadata(experiment_id: str, path: Path, run_count: int) -> None:
    """Persist experiment configuration and reproducibility metadata."""
    metadata = {
        "experiment_id": experiment_id,
        "created_at_utc": datetime.now(timezone.utc).isoformat(),
        "static_tau": STATIC_TAU,
        "layout_seed": LAYOUT_SEED,
        "node_count": len(NODES),
        "nodes": NODES,
        "topologies": list(TOPOLOGIES),
        "prompt_count": len(PROMPTS),
        "run_count": run_count,
        "compromised_node_rotation": COMPROMISED_NODES,
        "communication_model": (
            "Deterministic simulation: one source execution and one message per "
            "reachable directed edge, with each reachable node expanded once."
        ),
        "communication_formats": ["json", "markdown"],
        "networkx_version": nx.__version__,
        "pandas_version": pd.__version__,
    }
    path.write_text(json.dumps(metadata, indent=2) + "\n", encoding="utf-8")


def write_validation_report(results: pd.DataFrame, path: Path) -> None:
    """Generate a conclusion from observed values without assuming success."""
    observed = sorted(int(value) for value in results["Runtime τ_FVS"].unique())
    maximum = int(results["Runtime τ_FVS"].max())
    minimum = int(results["Runtime τ_FVS"].min())
    containment_rate = float(results["Containment Success"].mean() * 100)
    average_before = float(results["K Before"].mean())
    average_after = float(results["K After"].mean())
    average_messages = float(results["Message Count"].mean())
    total_messages = int(results["Message Count"].sum())
    bound_holds = maximum <= STATIC_TAU

    violating_topologies = sorted(
        results.loc[results["Runtime τ_FVS"] > STATIC_TAU, "Topology"].unique()
    )
    lines = [
        "Runtime τ_FVS Validation Report",
        "================================",
        "",
        f"Observed τ values: {set(observed)}",
        f"Maximum runtime τ: {maximum}",
        f"Minimum runtime τ: {minimum}",
        f"Containment Success Rate: {containment_rate:.1f}%",
        f"Average K Before: {average_before:.2f}",
        f"Average K After: {average_after:.2f}",
        f"Average Message Count: {average_messages:.2f}",
        f"Total Agent-to-Agent Messages: {total_messages}",
        f"Static τ_FVS: {STATIC_TAU}",
        "",
        "Static upper-bound validation: " + ("PASS" if bound_holds else "FAIL"),
    ]
    if bound_holds:
        lines.append("All observed runtime τ values were less than or equal to the static upper bound.")
    else:
        lines.append(
            "The configured static upper bound was exceeded by: "
            + ", ".join(violating_topologies)
            + "."
        )
    lines.extend(
        [
            "",
            "Interpretation:",
            "FVS revocation guarantees removal of directed cycles. It does not, by itself, "
            "guarantee zero downstream reachability from every compromised node.",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def run_experiment() -> tuple[str, Path, pd.DataFrame]:
    """Execute every prompt against every topology in a new experiment directory."""
    experiment_id, experiment_dir = create_experiment_directory()
    graphs_dir = experiment_dir / "graphs"
    logs_dir = experiment_dir / "runtime_logs"
    communications_dir = experiment_dir / "communications"
    write_prompts(experiment_dir / "prompts.txt")

    topology_analyses = {}
    for topology, edges in TOPOLOGIES.items():
        graph = build_graph(edges)
        cycles = list(nx.simple_cycles(graph))
        tau_runtime, fvs_nodes = compute_fvs(graph)
        topology_analyses[topology] = {
            "graph": graph,
            "cycles": cycles,
            "scc_count": nx.number_strongly_connected_components(graph),
            "tau": tau_runtime,
            "fvs": fvs_nodes,
        }

    records = []
    run_number = 0
    for topology, edges in TOPOLOGIES.items():
        analysis = topology_analyses[topology]
        graph = analysis["graph"]
        trace_id = TOPOLOGY_TRACE_IDS[topology]
        for prompt_number, scenario in enumerate(PROMPT_SCENARIOS, 1):
            prompt = scenario["prompt"]
            run_number += 1
            run_id = f"run_{run_number:03d}"
            compromised = COMPROMISED_NODES[(run_number - 1) % len(COMPROMISED_NODES)]
            infected_before = propagate_compromise(graph, compromised)
            revoked_graph = graph.copy()
            revoked_graph.remove_nodes_from(analysis["fvs"])
            infected_after = propagate_compromise(revoked_graph, compromised)
            containment_success = len(infected_before) > 0 and len(infected_after) == 0
            steps_before, infection_paths = simulate_communications(
                graph, compromised, scenario
            )
            steps_after, infection_paths_after = simulate_communications(
                revoked_graph, compromised, scenario
            )
            message_count = max(0, len(steps_before) - 1)
            message_count_after = max(0, len(steps_after) - 1)

            communication_stem = f"trace_{trace_id}_prompt_{prompt_number:02d}"
            communication_json = f"communications/{communication_stem}.json"
            communication_markdown_path = f"communications/{communication_stem}.md"
            communication_trace = {
                "experiment": experiment_id,
                "run_id": run_id,
                "prompt": prompt,
                "topology": topology,
                "runtime_tau": analysis["tau"],
                "compromise_source": compromised,
                "fvs_nodes": analysis["fvs"],
                "k_before": len(infected_before),
                "k_after": len(infected_after),
                "message_count": message_count,
                "message_count_after_revocation": message_count_after,
                "infected_nodes": infected_before,
                "infected_nodes_after_revocation": infected_after,
                "infection_paths": infection_paths,
                "infection_paths_after_revocation": infection_paths_after,
                "steps": steps_before,
                "post_revocation_steps": steps_after,
                "trace_semantics": (
                    "Deterministic simulation; each reachable directed edge transmits "
                    "at most once, preventing infinite replay through cycles."
                ),
            }
            save_communication_trace(
                experiment_dir / communication_json,
                experiment_dir / communication_markdown_path,
                communication_trace,
            )

            save_runtime_log(logs_dir / f"{run_id}.jsonl", edges)
            title = f"{run_id}: {topology} | compromised={compromised}"
            save_trace_graph(
                graphs_dir / f"{run_id}_trace_graph.png",
                graph,
                compromised,
                infected_before,
                analysis["fvs"],
                title,
            )
            save_scc_graph(graphs_dir / f"{run_id}_scc.png", graph, title)

            records.append(
                {
                    "Experiment ID": experiment_id,
                    "Run ID": run_id,
                    "Prompt": prompt,
                    "Topology": topology,
                    "Nodes": graph.number_of_nodes(),
                    "Edges": graph.number_of_edges(),
                    "Cycle Count": len(analysis["cycles"]),
                    "SCC Count": analysis["scc_count"],
                    "Runtime τ_FVS": analysis["tau"],
                    "FVS Nodes": "|".join(analysis["fvs"]),
                    "Compromised Node": compromised,
                    "K Before": len(infected_before),
                    "K After": len(infected_after),
                    "Containment Success": containment_success,
                    "Message Count": message_count,
                    "Messages After Revocation": message_count_after,
                    "Infection Path Count": len(infection_paths),
                    "Communications JSON": communication_json,
                    "Communications Markdown": communication_markdown_path,
                }
            )

    results = pd.DataFrame.from_records(records)
    results.to_csv(experiment_dir / "results.csv", index=False)
    save_aggregate_charts(results, graphs_dir)
    write_validation_report(results, experiment_dir / "validation_report.txt")
    write_metadata(experiment_id, experiment_dir / "metadata.json", len(results))
    return experiment_id, experiment_dir, results


def print_summary(experiment_id: str, experiment_dir: Path, results: pd.DataFrame) -> None:
    """Print the experiment location and aggregate observations."""
    observed = set(int(value) for value in results["Runtime τ_FVS"].unique())
    successes = int(results["Containment Success"].sum())
    print(f"Experiment: {experiment_id}")
    print(f"Output: {experiment_dir}")
    print(f"Runs: {len(results)}")
    print(f"Observed runtime τ values: {observed}")
    print(f"Maximum runtime τ: {int(results['Runtime τ_FVS'].max())}")
    print(f"Minimum runtime τ: {int(results['Runtime τ_FVS'].min())}")
    print(f"Containment success rate: {successes}/{len(results)}")
    print(f"Average K Before: {results['K Before'].mean():.2f}")
    print(f"Average K After: {results['K After'].mean():.2f}")
    print(f"Average message count: {results['Message Count'].mean():.2f}")
    print(f"Total agent-to-agent messages: {int(results['Message Count'].sum())}")


if __name__ == "__main__":
    current_id, current_dir, experiment_results = run_experiment()
    print_summary(current_id, current_dir, experiment_results)
