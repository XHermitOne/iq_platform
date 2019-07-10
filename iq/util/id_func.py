#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Object identification functions.
"""

import uuid

__version__ = (0, 0, 0, 1)


def genNewId(limit_len=5):
    """
    Generate new id.
    @param limit_len: Identifier string length restriction.
    @return: New id as string.
    """
    return str(uuid.uuid4().fields[-1])[:limit_len]
