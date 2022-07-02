# -*- coding: utf-8 -*-

import logging
import os
import re
import shlex
import shutil
import subprocess
from pathlib import Path

logger = logging.getLogger('sh')


class CommandResult:
    def __init__(self, is_ok, stdout, stderr) -> None:
        self._is_ok = is_ok
        self._stdout = stdout
        self._stderr = stderr

    @property
    def is_ok(self):
        return self._is_ok

    @property
    def stdout(self):
        return self._stdout

    @property
    def stderr(self):
        return self._stderr


def _run(command_line, using_coreutils=False):
    logger.info(f'{command_line}')

    _command_line = command_line
    if using_coreutils:
        _command_line = 'coreutils ' + command_line

    process_result = subprocess.run(['sh', '-c', _command_line], stdout=subprocess.PIPE,
                                    stderr=subprocess.PIPE, universal_newlines=True)

    is_ok = process_result.returncode == 0
    stdout = process_result.stdout.strip()
    stderr = process_result.stderr.strip()

    if is_ok:
        print(stdout)
    else:
        print(stderr)

    return CommandResult(is_ok, stdout, stderr)


def run_command_line(command_line):
    exists = shutil.which('bash')
    return _run(command_line, using_coreutils=exists)


def var(name):
    return os.getenv(name) or ''


def cd(path):
    os.chdir(path)
    logger.info(f'cd {path}')


def ls(path):
    return _run(f'ls {path}')


def cat(path):
    return _run(f'cat {path}')


def mv(src, dst):
    _src = Path(src)

    if _src.exists():
        if _src.is_dir():
            _run(f'mv -rf {src} {dst}')
        else:
            _run(f'mv -f {src} {dst}')
    else:
        logger.warning(f'src not exists, do nothing')


def cp(src, dst):
    return _run(f'cp -rf {src} {dst}')


def pwd():
    return _run('pwd')


def rm(path: str):
    _path = Path(path.strip())

    if _path.as_posix() == '/':
        logger.error(f"is not allow to 'rm /'")
        exit(1)

    if _path.exists():
        if _path.is_dir():
            return _run(f'rm -rf {_path}')
        else:
            return _run(f'rm -f {_path}')
    else:
        logger.error(f"target not found when calling rm, path = {path}")
        exit(-1)


def mkdir(path):
    return _run(f'mkdir -p {path}')


def find(path, name):
    return _run(f'find {path} -name {name}')


def list_dir(path='.'):
    return _run(f'du -ah {path}')


__blank_re = re.compile(f'\s+')


def sha256sum(path: str) -> str | None:
    res = _run(f'sha256sum {path}')
    if not res.is_ok:
        return None
    else:
        return __blank_re.split(res.stdout)[0]


def render_file(path: str, table: dict[str, any]):
    with open(path, 'r') as reader:
        content = reader.read()
        for kv in table.items():
            key = kv[0]
            val = str(kv[1])
            content = content.replace(key, val)

    with open(path, 'w') as writer:
        writer.write(content)
