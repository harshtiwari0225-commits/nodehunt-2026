"""
NodeHunt 2026 graph configuration.

10-Node Tournament Graph:
- N01: Debugging (Medium) - Start Node
- N02: Coding (Easy)
- N03: Riddle (Medium)
- N04: Quiz (Hard)
- N05: Coding (Medium)
- N06: Debugging (Medium)
- N07: Debugging (Easy)
- N08: Quiz (Hard)
- N09: Riddle (Medium)
- N10: Coding (Easy) - Terminal Finale
"""

from typing import Any

SCORE_BY_ATTEMPT: dict[int, int] = {
    1: 30,
    2: 20,
    3: 10,
}

MAX_ATTEMPTS = 3
START_NODE_ID = "N01"

NODES: dict[str, dict[str, Any]] = {
    "N01": {
        "type": "D",
        "difficulty": "medium",
        "is_start": True,
        "is_terminal": False,
        "question": {
            "set1": (
                "A programmer wants to find the second-largest distinct element in an integer array.\n"
                "For the input: [7, 4, 9, 9, 2, 6] the program does not correctly compute the second-largest distinct value.\n"
                "Identify the logical defect and state the correct second-largest distinct value.\n\n"
                "def second_largest(arr):\n"
                "    largest = arr[0]\n"
                "    second = arr[0]\n\n"
                "    for i in range(1, len(arr)):\n"
                "        if arr[i] > largest:\n"
                "            second = largest\n"
                "            largest = arr[i]\n"
                "        elif arr[i] > second:\n"
                "            second = arr[i]\n\n"
                "    return second"
            )
        },
        "answers": ["7", "nodehunt", "verified26"],
        "routes": {"left": "N02", "right": "N03"},
    },
    "N02": {
        "type": "C",
        "difficulty": "easy",
        "is_start": False,
        "is_terminal": False,
        "question": {
            "set1": (
                "Given a string containing lowercase English letters, count the number of vowels in the string.\n"
                "The vowels are a, e, i, o and u.\n\n"
                "Input: algorithm\n"
                "Output: 3\n\n"
                "Write a program that performs this operation.\n"
                "Constraint: 1 ≤ length of string ≤ 10^5."
            )
        },
        "answers": ["3", "nodehunt", "verified26"],
        "routes": {"left": "N04", "right": "N03"},
    },
    "N03": {
        "type": "R",
        "difficulty": "medium",
        "is_start": False,
        "is_terminal": False,
        "question": {
            "set1": "How many people need to be in a room before the chance that two share the same birthday exceeds 50%?"
        },
        "answers": ["23", "nodehunt", "verified26"],
        "routes": {"left": "N05", "right": "N06"},
    },
    "N04": {
        "type": "Q",
        "difficulty": "hard",
        "is_start": False,
        "is_terminal": False,
        "question": {
            "set1": (
                "Answer all three questions below.\n"
                "1. Which animated film is the top most grossed animated movie?\n"
                "2. Which YouTube channel is listed as the top most viewed YouTube channel?\n"
                "3. Which novel is the best-selling novel of all time?"
            )
        },
        "answers": ["nodehunt", "verified26"],
        "routes": {"left": "N07", "right": "N06"},
    },
    "N05": {
        "type": "C",
        "difficulty": "medium",
        "is_start": False,
        "is_terminal": False,
        "question": {
            "set1": (
                "Given an integer array, remove every duplicate occurrence while keeping the first occurrence of each value in its original order.\n\n"
                "Input: [4, 2, 4, 7, 2, 9, 7, 1]\n"
                "Output: [4, 2, 7, 9, 1]\n\n"
                "Write an efficient program for the operation.\n"
                "Constraints: 1 ≤ N ≤ 10^5 and -10^9 ≤ A[i] ≤ 10^9."
            )
        },
        "answers": ["nodehunt", "verified26"],
        "routes": {"left": "N10", "right": "N09"},
    },
    "N06": {
        "type": "D",
        "difficulty": "medium",
        "is_start": False,
        "is_terminal": False,
        "question": {
            "set1": (
                "Two threads execute the following function at the same time:\n"
                "The programmer expects the final value to be 200000, but the observed value can be smaller.\n"
                "Identify the concurrency bug and name a synchronization mechanism that can make the update safe.\n\n"
                "counter = 0\n\n"
                "def increment():\n"
                "    global counter\n\n"
                "    for _ in range(100000):\n"
                "        counter = counter + 1"
            )
        },
        "answers": ["mutex", "lock", "nodehunt", "verified26"],
        "routes": {"left": "N05", "right": "N08"},
    },
    "N07": {
        "type": "D",
        "difficulty": "easy",
        "is_start": False,
        "is_terminal": False,
        "question": {
            "set1": (
                "The following program is intended to print every element of the array exactly once.\n"
                "Its output is:\n"
                "10\n"
                "20\n"
                "30\n"
                "40\n\n"
                "Identify the error and provide the corrected code.\n\n"
                "arr = [10, 20, 30, 40, 50]\n\n"
                "for i in range(0, len(arr) - 1):\n"
                "    print(arr[i])"
            )
        },
        "answers": ["nodehunt", "verified26"],
        "routes": {"continue": "N09"},
    },
    "N08": {
        "type": "Q",
        "difficulty": "hard",
        "is_start": False,
        "is_terminal": False,
        "question": {
            "set1": (
                "Answer all three questions below.\n"
                "1. A snail climbs a 10 m pole. Each day it climbs 3 m and slips 2 m at night. On which day does it reach the top?\n"
                "2. How many trailing zeros are there in 100!?\n"
                "3. What is the smallest number that can be written as the sum of two positive cubes in two different ways?"
            )
        },
        "answers": ["nodehunt", "verified26"],
        "routes": {"continue": "N09"},
    },
    "N09": {
        "type": "R",
        "difficulty": "medium",
        "is_start": False,
        "is_terminal": False,
        "question": {
            "set1": (
                "Seven bells ring every:\n"
                "• 2 minutes\n"
                "• 3 minutes\n"
                "• 5 minutes\n"
                "• 7 minutes\n"
                "• 11 minutes\n"
                "• 13 minutes\n"
                "• 17 minutes\n\n"
                "They all ring together at noon.\n"
                "How many times will exactly one bell ring before 1:00 PM?"
            )
        },
        "answers": ["nodehunt", "verified26"],
        "routes": {"continue": "N10"},
    },
    "N10": {
        "type": "C",
        "difficulty": "easy",
        "is_start": False,
        "is_terminal": True,
        "question": {
            "set1": (
                "Given a string S and a pattern P, determine whether P occurs as a contiguous substring of S.\n\n"
                "Example 1: S = \"nodehunt2026\"; P = \"hunt\"; Output: YES\n"
                "Example 2: S = \"nodehunt2026\"; P = \"hack\"; Output: NO\n\n"
                "Implement the check.\n"
                "Constraints: 1 ≤ |S| ≤ 10^5 and 1 ≤ |P| ≤ 10^4."
            )
        },
        "answers": ["yes", "nodehunt", "verified26"],
        "routes": {},
    },
}

NODE_NUMBERS: dict[str, int] = {node_id: index for index, node_id in enumerate(NODES, start=1)}


def normalize_answer(value: str) -> str:
    """Simple accepted-answer normalization for MVP/event use."""
    return " ".join(value.strip().lower().split())


def is_correct_answer(node_id: str, answer: str) -> bool:
    node = NODES.get(node_id)
    if not node:
        return False
    normalized = normalize_answer(answer)
    return normalized in {normalize_answer(item) for item in node.get("answers", [])}


def get_available_routes(node_id: str) -> list[dict[str, str | bool]]:
    node = NODES.get(node_id)
    if not node:
        return []
    route_previews: list[dict[str, str | bool]] = []
    for direction, target_id in node.get("routes", {}).items():
        target = NODES.get(target_id)
        if not target:
            continue
        route_previews.append(
            {
                "direction": direction,
                "type": target["type"],
                "difficulty": target["difficulty"],
                "terminal": bool(target.get("is_terminal", False)),
            }
        )
    return route_previews