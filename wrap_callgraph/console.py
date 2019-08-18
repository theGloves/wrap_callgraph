from loguru import logger
from utils import match_pkg


class digraph():
    node: list
    edge: list

    def __init__(self):
        self.node = []
        self.edge = []

    def _ignore_(self, name: str):
        ignore_list = ["runtime", "internal",
                       "reflect", "math", "sync", "syscall", "fmt", "os", "time", "unicode", "strconv", "io", "sort"]
        return match_pkg(name, ignore_list)

    def add_node(self, node_name: str):
        if node_name is None or not isinstance(node_name, str):
            return False
        tmp_name = node_name.strip()
        if tmp_name == "":
            return False

        if self._ignore_(node_name):
            return False
        if tmp_name not in self.node:
            logger.debug("add {} to node".format(tmp_name))
            self.node.append(tmp_name)
        return True

    def add_edge(self, edge_tuple: tuple):
        caller, callee = edge_tuple[0], edge_tuple[1]
        if self.add_node(caller) and self.add_node(callee):
            self.edge.append((caller, callee))

    def print_graph(self):
        print("node sum: {}".format(len(self.node)))
        print("nodes: {}".format(self.node))
        print("edge: {}".format(self.edge))

def load_dg_from_file(filename: str):
    """将指定路径的文件加载至内存
    再一次会话中，该文件一直存在在内存中直至会话结束或者加载其他文件
    文件内容格式: {{pkg.Caller}}\t{{pkg.Callee}}
    """
    cdg = digraph()
    with open(filename, "r") as f:
        while True:
            line = f.readline()
            if not line:
                break
            line = line.replace('"', "")
            tmp = line.split(" ")
            tuple_edge = (tmp[0], tmp[1])
            cdg.add_edge(tuple_edge)
    return cdg
