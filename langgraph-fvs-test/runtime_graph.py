# runtime_graph.py

import json

def extract_edges(messages):

    edges = []

    for msg in messages:

        if hasattr(msg, "tool_calls"):

            for tc in msg.tool_calls:

                name = tc["name"]

                if name.startswith("transfer_to_"):

                    src = msg.name

                    dst = name.replace(
                        "transfer_to_",
                        ""
                    )

                    edges.append(
                        (src, dst)
                    )

                elif name.startswith(
                    "transfer_back_to_"
                ):

                    src = msg.name

                    dst = name.replace(
                        "transfer_back_to_",
                        ""
                    )

                    edges.append(
                        (src, dst)
                    )

    return edges