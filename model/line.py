# SPDX-License-Identifier: MIT OR MPL-2.0

from typing import List, TypedDict

from model.user_data import UserData


class Narration(TypedDict, total=False):
    text: str


class Dialogue(TypedDict, total=False):
    speaker: str
    line: str


class Jump(TypedDict, total=False):
    condition: str
    scene: str


class Menu(TypedDict, total=False):
    # TODO: https://github.com/BirdCatcherGamesOrg/fountain-vn-sdk-parser/issues/1
    condition: str
    scene: str


class Cue(TypedDict, total=False):
    type: str
    actions: List[str]


class Synopsis(TypedDict, total=False):
    text: str


class Line(TypedDict, total=False):
    narration: Narration
    dialogue: Dialogue
    synopsis: Synopsis
    jump: Jump
    menu: Menu
    cue: Cue
    user_data: UserData

