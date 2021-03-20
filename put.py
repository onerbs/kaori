from os import getenv
import functools

__all__ = [
    'log', 'err', 'info', 'warn',
    'debug', 'done', 'fail',
    'toggle_debug', 'verbose'
]


def log(*msg):
    tag = _tint('  >>', 7)
    _put(tag, *msg)


def err(*msg):
    mark = _tint('!', 1, 3)
    tag = _tint('err', 1)
    _put(tag + mark, *msg)


def info(*msg):
    tag = _tint('info', 3)
    _put(tag, *msg)


def warn(*msg):
    tag = _tint('warn', 6)
    _put(tag, *msg)


def debug(*args):
    tag = _tint('debug', 4)
    _put(tag, *args)


def done(*msg):
    tag = _tint('done', 2)
    _put(tag, *msg)


def fail(*msg):
    err('failed to', *msg)


def verbose(fn):
    @functools.wraps(fn)
    def enhanced(*args):
        curr = __put__.DEBUG
        toggle_debug(True)
        result = fn(*args)
        __put__.DEBUG = curr
        return result

    return enhanced


class __put__:
    DEBUG = getenv('DEBUG', '').lower() == 'true'


def toggle_debug(to: bool = None):
    __put__.DEBUG = not __put__.DEBUG if to is None else to


def _put(tag: str, *msg, force=False):
    (force or __put__.DEBUG) and print(f'{tag}\033[m ', *msg)


def _tint(tag, *mods) -> str:
    return f'\033[3{";".join(str(mod) for mod in mods)}m{tag}'
