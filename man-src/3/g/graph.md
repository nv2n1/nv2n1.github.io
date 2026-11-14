---
title: "graph(3)"
name: "graph"
section: "3"
letter: "g"
url: "/docs/linux/man/3-graph/"
description: "libgraph – abstract graph library"
---

<h2>NAME</h2>
<p> <code>libgraph</code> &#8211; abstract graph library</p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;graphviz/graph.h&gt;
void aginit();
Agraph_t *agread(FILE *);
int agwrite(Agraph_t *, FILE *);
int agerrors();
Agraph_t *agopen(char *name, int kind);
void agclose(Agraph_t *g);
Agraph_t *agsubg(Agraph_t *g, char *name);
Agraph_t *agfindsubg(Agraph_t *g, char *name);
Agnode_t *agmetanode(Agraph_t *g);
Agraph_t *agusergraph(Agnode_t *metanode);
int agnnodes(Agraph_t *g), agnedges(Agraph_t *g);
int agcontains(Agraph_t *g, void *obj);
int aginsert(Agraph_t *g, void *obj);
int agdelete(Agraph_t *g, void *obj);
Agnode_t *agnode(Agraph_t *g, char *name);
Agnode_t *agfindnode(Agraph_t *g, char *name);
Agnode_t *agfstnode(Agraph_t *g);
Agnode_t *agnxtnode(Agraph_t *g, Agnode_t *n);
Agnode_t *aglstnode(Agraph_t *g);
Agnode_t *agprvnode(Agraph_t *g, Agnode_t *n);
Agedge_t *agedge(Agraph_t *g, Agnode_t *tail, Agnode_t *head);
Agedge_t *agfindedge(Agraph_t *g, Agnode_t *tail, Agnode_t *head);
Agedge_t *agfstedge(Agraph_t *g, Agnode_t *n);
Agedge_t *agnxtedge(Agraph_t *g, Agedge_t *e, Agnode_t *n);
Agedge_t *agfstin(Agraph_t *g, Agnode_t *n);
Agedge_t *agnxtin(Agraph_t *g, Agedge_t *e);
Agedge_t *agfstout(Agraph_t *g, Agnode_t *n);
Agedge_t *agnxtout(Agraph_t *g, Agedge_t *e);
char *agget(void *obj, char *name);
char *agxget(void *obj, int index);
void agset(void *obj, char *name, char *value);
void agxset(void *obj, int index, char *value);
int agindex(void *obj, char *name);
Agsym_t *agraphattr(Agraph_t *g, char *name, char *value);
Agsym_t *agnodeattr(Agraph_t *g, char *name, char *value);
Agsym_t *agedgeattr(Agraph_t *g, char *name, char *value);
Agsym_t *agfindattr(void *obj, char *name);
</code></pre>
<h2>DESCRIPTION</h2>
<p> <i>libgraph</i> maintains directed and undirected attributed graphs in memory and reads and writes graph files. Graphs are composed of nodes, edges, and nested subgraphs. A subgraph may contain any nodes and edges of its parents, and may be passed to any <i>libgraph</i> function taking a graph pointer, except the three that create new attributes (where a main graph is required). </p>
<p> Attributes are internal or external. Internal attributes are fields in the graph, node and edge structs defined at compile time. These allow efficient representation and direct access to values such as marks, weights, and pointers for writing graph algorithms. External attributes, on the other hand, are character strings (name-value pairs) dynamically allocated at runtime and accessed through <i>libgraph</i> calls. External attributes are used in graph file I/O; internal attributes are not. Conversion between internal and external attributes must be explicitly programmed. </p>
<p> The subgraphs in a main graph are represented by an auxiliary directed graph (a meta-graph). Meta-nodes correspond to subgraphs, and meta-edges signify containment of one subgraph in another. agmetanode and agusergraph map between subgraphs and meta-nodes. The nodes and edges of the meta-graph may be traversed by the usual <i>libgraph</i> functions for this purpose. </p>
<h2>USE</h2>
<p> 1. Define types Agraphinfo_t, Agnodeinfo_t, and Agedgeinfo_t (usually in a header file) before including &lt;graphviz/graph.h&gt;. </p>
<p> 2. Call aginit() before any other <i>libgraph</i> functions. (This is a macro that calls aginitlib() to define the sizes of Agraphinfo_t, Agnodeinfo_t, and Agedgeinfo_t.) </p>
<p> 3. Compile with -lgraph -lcdt. </p>
<p> Except for the <code>u</code> fields, <i>libgraph</i> data structures must be considered read-only. Corrupting their contents by direct updates can cause catastrophic errors. </p>
<p> Warning: the library is not thread-safe. </p>
<h2>GRAPHS</h2>
<p>typedef struct Agraph_t {<br />
    char kind;<br />
    char *name;<br />
    Agraph_t *root;<br />
    char **attr;<br />
    graphdata_t *univ;<br />
    Dict_t *nodes, *inedges, *outedges;<br />
    proto_t *proto;<br />
    Agraphinfo_t u;<br />
} Agraph_t;<br />
typedef struct graphdata_t {<br />
    Dict_t *node_dict;<br />
    attrdict_t *nodeattr, *edgeattr, *globattr;<br />
} graphdata_t;<br />
typedef struct proto_t {<br />
    Agnode_t *n;<br />
    Agedge_t *e;<br />
    proto_t *prev;<br />
} proto_t;<br />
 A graph <i>kind</i> is one of: AGRAPH, AGRAPHSTRICT, AGDIGRAPH, or AGDIGRAPHSTRICT. There are related macros for testing the properties of a graph: AG_IS_DIRECTED(g) and AG_IS_STRICT(g). Strict graphs cannot have self-arcs or multi-edges. <code>attr</code> is the array of external attribute values. <code>univ</code> points to values shared by all subgraphs of a main graph. <code>nodes</code>, <code>inedges</code>, and <code>outedges</code> are sets maintained by <code><a href="/docs/linux/man/3-cdt/">cdt</a>(3)</code>. Normally you don&#8217;t access these dictionaries directly, though the edge dictionaries may be re-ordered to support programmer-defined ordered edges (see dtreorder in <i><a href="/docs/linux/man/3-cdt/">cdt</a>(3)</i>). <code>proto</code> is a stack of templates for node and edge initialization. The attributes of these nodes and edges are set in the usual way (agget, agset, etc.) to set defaults. </p>
<p> agread reads a file and returns a new graph if one was successfully parsed, otherwise returns NULL if EOF or a syntax error was encountered. Errors are reported on stderr and a count is returned from g5agerrors(). write_graph prints a graph on a file. agopen and agsubg create new empty graph and subgraphs. agfindsubg searches for a subgraph by name, returning NULL when the search fails. </p>
<h2>ALL OBJECTS</h2>
<p> agcontains, aginsert, agdelete are generic functions for nodes, edges, and graphs. gcontains is a predicate that tests if an object belongs to the given graph. aginsert inserts an object in a graph and agdelete undoes this operation. A node or edge is destroyed (and its storage freed) at the time it is deleted from the main graph. Likewise a subgraph is destroyed when it is deleted from its last parent or when its last parent is deleted. </p>
<h2>NODES</h2>
<p>typedef struct Agnode_t {<br />
    char *name;<br />
    Agraph_t *graph;<br />
    char **attr;<br />
    Agnodeinfo_t u;<br />
} Agnode_t;</p>
<p> agnode attempts to create a node. If one with the requested name already exists, the old node is returned unmodified. Otherwise a new node is created, with attributed copied from g-&gt;proto-&gt;n. agfstnode (agnxtnode) return the first (next) element in the node set of a graph, respectively, or NULL. aglstnode (agprvnode) return the last (previous) element in the node set of a graph, respectively, or NULL. </p>
<h2>EDGES</h2>
<p>typedef struct Agedge_t {<br />
    Agnode_t *head, *tail;<br />
    char **attr;<br />
    Agedgeinfo_t u;<br />
} Agedge_t;<br />
 agedge creates a new edge with the attributes of g-&gt;proto-&gt;e including its key if not empty. agfindedge finds the first (u,v) edge in g. agfstedge (agnxtedge) return the first (next) element in the edge set of a graph, respectively, or NULL. agfstin, agnxtin, agfstout, agnxtout refer to in- or out-edge sets. The idiomatic usage in a directed graph is: </p>
<p> for (e = agfstout(g,n); e; e = agnextout(g,e)) your_fun(e); </p>
<p> An edge is uniquely identified by its endpoints and its key attribute (if there are multiple edges). If the key of g-&gt;proto-&gt;e is empty, new edges are assigned an internal value. Edges also have tailport and headport values. These have special syntax in the graph file language but are not otherwise interpreted. </p>
<h2>ATTRIBUTES</h2>
<p>typedef struct attrsym_t {<br />
    char *name, *value;<br />
    int index;<br />
    unsigned char printed;<br />
} attrsym_t;<br />
typedef struct attrdict_t {<br />
    char *name;<br />
    Dict_t *dict;<br />
    attrsym_t **list;<br />
} attrdict_t;<br />
 agraphattr, agnodeattr, and agedgeattr make new attributes. g should be a main graph, or NULL for declarations applying to all graphs subsequently read or created. agfindattr searches for an existing attribute. </p>
<p> External attributes are accessed by agget and agset These take a pointer to any graph, node, or edge, and an attribute name. Also, each attribute has an integer index. For efficiency this index may be passed instead of the name, by calling agxget and agxset. The printed flag of an attribute may be set to 0 to skip it when writing a graph file. </p>
<p> The list in an attribute dictionary is maintained in order of creation and is NULL terminated. Here is a program fragment to print node attribute names:<br />
attrsym_t *aptr;<br />
for (i = 0; aptr = g-&gt;univ-&gt;nodedict-&gt;list[i]; i++)<br />
    puts(aptr-&gt;name);</p>
<h2>EXAMPLE GRAPH FILES</h2>
<pre><code>
graph any_name
{                                     /* an undirected graph */
    a-- b;                            /* a simple edge */
    a-- x1-- x2-- x3;                 /* a chain of edges */
    "x3.a!" --a;                      /* quotes protect special characters */
    b-- {q r s t};                    /* edges that fan out */
    b[color = "red", size = ".5,.5"]; /* set various node attributes */
    node[color = blue];               /* set default attributes */
    b-- c[weight = 25];               /* set edge attributes */
    subgraph sink_nodes{a b c};       /* make a subgraph */
}
digraph G
{
    size = "8.5,11";          /* sets a graph attribute */
    a-&gt;b;                     /* makes a directed edge */
    chip12.pin1-&gt;chip28.pin3; /* uses named node "ports" */
}
</code></pre>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-dot/">dot</a></code>(1), <code><a href="/docs/linux/man/1-neato/">neato</a></code>(1), <code><a href="/docs/linux/man/3-libdict/">libdict</a></code>(3)<br />
 S. C. North and K. P. Vo, &quot;Dictionary and Graph Libraries&#8221; 1993 Winter USENIX Conference Proceedings, pp. 1-11. </p>
<h2>AUTHOR</h2>
<p> Stephen North (north [at] ulysses.att.com), AT&amp;T Bell Laboratories. </p>
<h2>Index</h2>
