import os
from pathlib import Path

import gd
from gd.typing import Union

from modloader.logging import get_logger

__all__ = ("State", "create_state")

PathLike = Union[str, Path]

DEFAULT_NAME = "GeometryDash.exe"
GD_DIR = gd.api.get_path()
MOD_LOADER_DIR = Path(os.environ.get("HOMEPATH")) / ".modloader"

if not MOD_LOADER_DIR.exists():
    MOD_LOADER_DIR.mkdir()

log = get_logger(__name__)


class State:
    def __init__(self, name: str = DEFAULT_NAME, load: bool = True) -> None:
        self.memory = gd.memory.get_memory(name, load=load)

    def inject_dll(self, dll_path: PathLike) -> bool:
        return self.memory.inject_dll(dll_path)

    def append_dll(self, dll_path: PathLike) -> None:
        copy_file(Path(dll_path).resolve(), MOD_LOADER_DIR)

    def put_gd_dll(self, dll_path: PathLike) -> None:
        copy_file(Path(dll_path).resolve(), GD_DIR)

    def load(self) -> None:
        for path in MOD_LOADER_DIR.iterdir():
            if path.suffix == ".dll":
                self.inject_dll(path)
                log.info(f"Injected DLL: {path.name!r}.")
        else:
            log.info("No DLLs Found.")


def copy_file(source: PathLike, destination: PathLike) -> None:
    if not source.is_file():
        raise ValueError(f"Expected source to be file: {source}.")

    if destination.is_dir():
        destination /= source.name

    destination.write_bytes(source.read_bytes())

    log.info(f"Copied {source} to {destination}.")


def create_state(name: str = DEFAULT_NAME, load: bool = True) -> State:
    return State(name, load=load)
