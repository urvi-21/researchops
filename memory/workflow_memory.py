import json
import os


class WorkflowMemory:

    def __init__(
        self,
        memory_file="storage/metadata/workflow_memory.json"
    ):

        self.memory_file = memory_file

        if not os.path.exists(memory_file):

            with open(memory_file, "w") as f:
                json.dump([], f)

    def load_memory(self):

        with open(self.memory_file, "r") as f:
            return json.load(f)

    def save_workflow(
        self,
        workflow_data
    ):

        memory = self.load_memory()

        memory.append(workflow_data)

        with open(self.memory_file, "w") as f:
            json.dump(memory, f, indent=4)

        print("[SAVED] Workflow Memory")

    def fetch_all_workflows(self):

        return self.load_memory()