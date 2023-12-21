"""
--- Day 19: Aplenty ---
"""
import operator
import os
from typing import Callable, Dict, List, Tuple, Union

PartType = Dict[str, int]
RuleType = Callable[[PartType], Union[bool, str]]
WorkflowType = Tuple[str, List[RuleType]]


def parse_part(value: str) -> PartType:
    raw_categories = value[1:-1].split(",")

    categories = {}
    for category in raw_categories:
        category_letter, number = category.split("=")
        categories[category_letter] = int(number)

    return categories


def parse_workflow(value: str) -> WorkflowType:
    open_bracket_i = value.find("{")
    name = value[:open_bracket_i]
    value = value[open_bracket_i + 1 : -1]

    definitions = value.split(",")
    workflow_rules = []
    for definition in definitions:
        definition_parts = definition.split(":")

        if len(definition_parts) == 1:
            workflow_rules.append(definition_parts[0])
            continue

        category_filter = definition_parts[0]
        (category, operation, filter_value) = (
            category_filter[0],
            operator.lt if category_filter[1] == "<" else operator.gt,
            int(category_filter[2:]),
        )

        workflow_rules.append(
            (
                category,
                operation,
                filter_value,
                definition_parts[1],
            )
        )

    return name, workflow_rules


with open("19.in", "r", encoding="utf-8") as f:
    raw_workflows, raw_parts = f.read().split(f"{os.linesep}{os.linesep}")
    parts = [parse_part(p) for p in raw_parts.splitlines()]

    workflows = [parse_workflow(r) for r in raw_workflows.splitlines()]
    workflows = {w[0]: w[1] for w in workflows}


def apply_rules(part: PartType) -> int:
    current_workflow = "in"
    while True:
        for rule in workflows[current_workflow]:
            if rule == "A":
                return sum(part.values())
            if rule == "R":
                return 0

            if rule in workflows:
                current_workflow = rule
                break

            category, condition, filter_value, result = rule
            if condition(part[category], filter_value):
                if result == "A":
                    return sum(part.values())
                if result == "R":
                    return 0

                current_workflow = result
                break


p1_ratings = sum(apply_rules(part) for part in parts)
print(p1_ratings)

p2_parts = ...
p2_ratings = sum(apply_rules(part) for part in p2_parts)
print(p2_ratings)
