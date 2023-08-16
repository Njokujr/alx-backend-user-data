#!/usr/bin/env python3
"""A module for Authentication-related routines.
"""

import bcrypt
from uuid import uuid4
from typing import Union
from sqlalchemy.orm.exc import NoResultFound

from db import DB
from user import User


def _hash_password(password: str) -> bytes:
    """Hashes a password & rtrn bytes.
    """
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
