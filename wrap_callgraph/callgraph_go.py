import subprocess
from loguru import logger
import traceback
import sys
import os
from utils import get_pkg_name

_suffix = ".node"


def execute_go_callgraph(pkg, output=None):
    graph_format = "digraph"
    if output is None:
        output = get_pkg_name(pkg) + _suffix
    logger.debug("output file: {}".format(output))
    cmd_output = None
    try:
        cmd = ["callgraph", "-algo=static",
               "-format={}".format(graph_format),
               "{}".format(pkg)]
        logger.debug("cmd: {}".format(" ".join(cmd)))

        cmd_output = open(output, "w")
        _ = subprocess.run(
            cmd, check=True, stdout=cmd_output, stderr=sys.stderr)
        logger.info("generate callgraph success.")
    except subprocess.CalledProcessError:
        logger.error("callgrapg exit wtih non-zero status.")
    except:
        logger.error("execute cmd: {} failed.".format(cmd))
        logger.debug("{}".format(traceback.format_exc()))
    finally:
        if cmd_output and cmd_output != sys.stdout:
            cmd_output.close()