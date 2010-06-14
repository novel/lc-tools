from libcloud.types import NodeState

readable_status = {NodeState.RUNNING: "Running",
        NodeState.REBOOTING: "Rebooting",
        NodeState.TERMINATED: "Terminated",
        NodeState.PENDING: "Pending",
        NodeState.UNKNOWN: "Unknown"}
