from __future__ import unicode_literals
import fire
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit import PromptSession
from loguru import logger
import sys
from callgraph_go import execute_go_callgraph
from console import load_dg_from_file
from prompt_toolkit.history import FileHistory

cmd_completer = WordCompleter([
    'static', 'query', 'load', 'print'
], ignore_case=True)


class callgraph():
    def __init__(self):
        pass

    def static(self, pkg, output=None):
        if pkg is None:
            logger.error("need input golang pkg.")
            return
        logger.debug("input pkg: {}".format(pkg))
        execute_go_callgraph(pkg, output)

    def console(self):
        # 将变量以标签-值的字典形式存入args字典

        session = PromptSession(completer=cmd_completer,
                                history=FileHistory('/root/.go_callgrapgh/cmd_history'))

        func: str
        args: str
        _cdg_ = None  # 调用有向图
        while True:
            try:
                text = session.prompt('> ')
                tmp = text.split(" ")
                func = tmp[0]
                if len(tmp) > 1:
                    args = tmp[1]
                if func == "load":
                    _cdg_ = load_dg_from_file(args)
                    continue
                elif func == "print":
                    _cdg_.print_graph()
            except KeyboardInterrupt:
                continue
            except EOFError:
                break
        print('GoodBye!')


if __name__ == "__main__":
    fire.Fire(callgraph)
