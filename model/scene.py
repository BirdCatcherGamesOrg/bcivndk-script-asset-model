# SPDX-License-Identifier: MIT OR MPL-2.0

from typing import List, Required, TypedDict

from model.line import Line
from model.user_data import UserData


class Scene(TypedDict, total=False):
    id: Required[str]
    heading: str
    lines: List[Line]
    game_asset_id: str
    user_data: UserData

