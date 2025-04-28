# SPDX-License-Identifier: MIT OR MPL-2.0

from typing import Required, TypedDict

from .user_data import UserData

class Character(TypedDict, total=False):
    script_name: Required[str]
    game_asset_id: str
    user_data: UserData
