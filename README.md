# wrap_callgraph
golang static callgrap, wrap of golang/tools/cmd/callgraph

## callgraph使用说明
``` shell
callgraph [-algo=static|cha|rta|pta] [-test] [-format=...] package ...
```


## TODO
1. 提供golang某个包（或者指定包）的**静态函数**的函数函数调用关系
2. 可指定输出的格式，默认格式支持go/cmd/digraph的查询使用

## format使用说明
### callgraph可输出的信息
1. Caller 调用函数， 类型ssa.Function
2. Callee 被调用函数，类型ssa.function
3. Filename 函数名（包含package的路径）
4. Offset 该函数在文件里的位置偏移
5. Line 第几行
6. Column 第几列
7. Dynamic "static" or "dynamic"，暂时不知道这个信息的意义
8. Description 函数的描述信息

### Caller & Callee可输出的信息
1. Pkg  函数所在package的结构，类型ssa.Package
2. Prog 函数被编译时所在的程序，类型ssa.Program
3. Param 函数的参数，类型ssa.Parameter的数组  
……更多的参数查看 golang.org/x/tools/go/ssa 的Function信息

## (tools) digraph使用说明

	nodes
		the set of all nodes
	degree
		the in-degree and out-degree of each node
	transpose
		the reverse of the input edges
	preds <node> ...
		the set of immediate predecessors of the specified nodes
	succs <node> ...
		the set of immediate successors of the specified nodes
	forward <node> ...
		the set of nodes transitively reachable from the specified nodes
	reverse <node> ...
		the set of nodes that transitively reach the specified nodes
	somepath <node> <node>
		the list of nodes on some arbitrary path from the first node to the second
	allpaths <node> <node>
		the set of nodes on all paths from the first node to the second
	sccs
		all strongly connected components (one per line)
	scc <node>
		the set of nodes nodes strongly connected to the specified one