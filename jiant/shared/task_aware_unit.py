from typing import Any, Dict, List, Optional, Union


class TaskAwareUnit(object):
    def __init__(self):
        self.tau_task_name = None

    def set_task(self, task_name: str):
        self.tau_task_name = task_name


def create_tau_dict(named_objects: Union[Dict, List[tuple]]):
    if isinstance(named_objects, dict):
        named_objects = named_objects.items()
    tau_dict = {
        object_name: one_object
        for object_name, one_object in named_objects
        if isinstance(one_object, TaskAwareUnit)
    }
    return tau_dict


def set_tau_task(tau_dict: Dict, task_name: str):
    for one_tau_object in tau_dict.values():
        one_tau_object.set_task(task_name)