# SPDX-License-Identifier: MIT OR MPL-2.0

from typing import TypedDict

class UserData(TypedDict, total=False):
    version: int
    data: str