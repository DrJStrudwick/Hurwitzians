# Copyright (c) 2024 James Strudwick
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT
from quaternion_djs import Quaternion
import numpy as np


class Hurwitzian(Quaternion):
    def __init__(self, x: int | float, i: int | float, j: int | float, k: int | float):
        # TODO: 6. docstring
        # TODO: 7. write test

        # Check that the inputs ant ints of half ints
        if all((np.array([x, i, j, k]) % 1) == 0) or all(
            (np.array([x, i, j, k]) % 1) == 0.5
        ):
            super().__init__(x=x, i=i, j=j, k=k)
        else:
            # if not raise error
            raise ValueError(
                "The input for hurwitzians must ALL be integers or ALL half integers"
            )
