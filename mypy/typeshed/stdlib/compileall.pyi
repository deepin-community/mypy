import sys
from _typeshed import StrPath
from py_compile import PycInvalidationMode
from typing import Any, Protocol

__all__ = ["compile_dir", "compile_file", "compile_path"]

class _SupportsSearch(Protocol):
    def search(self, string: str) -> Any: ...

if sys.version_info >= (3, 10):
    def compile_dir(
        dir: StrPath,
        maxlevels: int | None = ...,
        ddir: StrPath | None = ...,
        force: bool = ...,
        rx: _SupportsSearch | None = ...,
        quiet: int = ...,
        legacy: bool = ...,
        optimize: int = ...,
        workers: int = ...,
        invalidation_mode: PycInvalidationMode | None = ...,
        *,
        stripdir: StrPath | None = ...,
        prependdir: StrPath | None = ...,
        limit_sl_dest: StrPath | None = ...,
        hardlink_dupes: bool = ...,
    ) -> int: ...
    def compile_file(
        fullname: StrPath,
        ddir: StrPath | None = ...,
        force: bool = ...,
        rx: _SupportsSearch | None = ...,
        quiet: int = ...,
        legacy: bool = ...,
        optimize: int = ...,
        invalidation_mode: PycInvalidationMode | None = ...,
        *,
        stripdir: StrPath | None = ...,
        prependdir: StrPath | None = ...,
        limit_sl_dest: StrPath | None = ...,
        hardlink_dupes: bool = ...,
    ) -> int: ...

elif sys.version_info >= (3, 9):
    def compile_dir(
        dir: StrPath,
        maxlevels: int | None = ...,
        ddir: StrPath | None = ...,
        force: bool = ...,
        rx: _SupportsSearch | None = ...,
        quiet: int = ...,
        legacy: bool = ...,
        optimize: int = ...,
        workers: int = ...,
        invalidation_mode: PycInvalidationMode | None = ...,
        *,
        stripdir: str | None = ...,  # https://bugs.python.org/issue40447
        prependdir: StrPath | None = ...,
        limit_sl_dest: StrPath | None = ...,
        hardlink_dupes: bool = ...,
    ) -> int: ...
    def compile_file(
        fullname: StrPath,
        ddir: StrPath | None = ...,
        force: bool = ...,
        rx: _SupportsSearch | None = ...,
        quiet: int = ...,
        legacy: bool = ...,
        optimize: int = ...,
        invalidation_mode: PycInvalidationMode | None = ...,
        *,
        stripdir: str | None = ...,  # https://bugs.python.org/issue40447
        prependdir: StrPath | None = ...,
        limit_sl_dest: StrPath | None = ...,
        hardlink_dupes: bool = ...,
    ) -> int: ...

else:
    def compile_dir(
        dir: StrPath,
        maxlevels: int = ...,
        ddir: StrPath | None = ...,
        force: bool = ...,
        rx: _SupportsSearch | None = ...,
        quiet: int = ...,
        legacy: bool = ...,
        optimize: int = ...,
        workers: int = ...,
        invalidation_mode: PycInvalidationMode | None = ...,
    ) -> int: ...
    def compile_file(
        fullname: StrPath,
        ddir: StrPath | None = ...,
        force: bool = ...,
        rx: _SupportsSearch | None = ...,
        quiet: int = ...,
        legacy: bool = ...,
        optimize: int = ...,
        invalidation_mode: PycInvalidationMode | None = ...,
    ) -> int: ...

def compile_path(
    skip_curdir: bool = ...,
    maxlevels: int = ...,
    force: bool = ...,
    quiet: int = ...,
    legacy: bool = ...,
    optimize: int = ...,
    invalidation_mode: PycInvalidationMode | None = ...,
) -> int: ...
