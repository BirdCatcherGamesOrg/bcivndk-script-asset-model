# SPDX-License-Identifier: MIT OR MPL-2.0

from pathlib import Path
from typing import List, TypedDict

from .user_data import UserData


class Manifest(TypedDict, total=False):
    parsed_script: Path
    characters: List[Path]
    scenes: List[Path]
    timestamp: int
    user_data: UserData
