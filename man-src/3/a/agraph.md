---
title: "agraph(3)"
name: "agraph"
section: "3"
letter: "a"
url: "/docs/linux/man/3-agraph/"
description: "Agraph – abstract graph library"
---

<h2>NAME</h2>
<p> <code>Agraph</code> &#8211; abstract graph library</p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;graphviz/agraph.h&gt;
</code></pre>
<h3>TYPES</h3>
<p>Agraph_t;<br />
Agnode_t;<br />
Agedge_t;<br />
Agdesc_t;<br />
Agdisc_t;<br />
Agsym_t;</p>
<h3>GRAPHS</h3>
<p>Agraph_t *agopen(char *name, Agdesc_t kind, Agdisc_t *disc);<br />
int agclose(Agraph_t *g);<br />
Agraph_t *agread(void *file, Agdisc_t *);<br />
Agraph_t *agconcat(Agraph_t *g, void *chan, Agdisc_t *disc) int agwrite(Agraph_t *g, void *file);<br />
int agnnodes(Agraph_t *g), agnedges(Agraph_t *g);</p>
<h3>SUBGRAPHS</h3>
<p>Agraph_t *agsubg(Agraph_t *g, char *name, int createflag);<br />
Agraph_t *agfstsubg(Agraph_t *g), agnxtsubg(Agraph_t *);<br />
Agraph_t *agparent(Agraph_t *g), *agroot(Agraph_t *g);</p>
<h3>NODES</h3>
<p>Agnode_t *agnode(Agraph_t *g, char *name, int createflag);<br />
Agnode_t *agidnode(Agraph_t *g, ulong id, int createflag);<br />
Agnode_t *agsubnode(Agraph_t *g, Agnode_t *n, int createflag);<br />
Agnode_t *agfstnode(Agraph_t *g);<br />
Agnode_t *agnxtnode(Agnode_t *n);<br />
int agdelnode(Agraph_t *g, Agnode_t *n);<br />
int agrename(Agraph_t *g, Agnode_t *n, char *newname);<br />
int agdegree(Agnode_t *n, int use_inedges, int use_outedges);</p>
<h3>EDGES</h3>
<p>Agedge_t *agedge(Agnode_t *t, Agnode_t *h, char *name, int createflag);<br />
Agedge_t *agsubedge(Agraph_t *g, Agedge_t *e, int createflag);<br />
int agdeledge(Agraph_t *g, Agedge_t *e);<br />
Agnode_t *aghead(Agedge_t *e), *agtail(Agedge_t *e);<br />
Agedge_t *agfstedge(Agnode_t *n);<br />
Agedge_t *agnxtedge(Agedge_t *e, Agnode_t *n);<br />
Agedge_t *agfstin(Agnode_t *n);<br />
Agedge_t *agnxtin(Agedge_t *e);<br />
Agedge_t *agfstout(Agnode_t *n);<br />
Agedge_t *agnxtout(Agedge_t *e);</p>
<h3>FLATTENED LISTS</h3>
<p>int agflatten(Agraph_t *graph, int flag);<br />
Agnode_t *agfstn(Agraph_t *g), *agnxtn(Agnode_t *n);<br />
Agedge_t *agfout(Agnode_t *n), *agfin(Agnode_t *n), *agnxte(Agedge_t *e);</p>
<h3>STRING ATTRIBUTES</h3>
<p>Agsym_t *agattr(Agraph_t *g, int kind, char *name, char *value);<br />
Agsym_t *agattrnxt(Agraph_t *g, int kind, Agsym_t *attr);<br />
char *agget(void *obj, char *name);<br />
char *agxget(void *obj, Agsym_t *sym);<br />
int agset(void *obj, char *name, char *value);<br />
int agxset(void *obj, Agsym_t *sym, char *value);</p>
<h3>RECORDS</h3>
<p>void *agnewrec(Agraph_t *g, void *obj, char *name, unsigned int size);<br />
Agrec_t *aggetrec(void *obj, char *name, int move_to_front);<br />
int agdelrec(Agraph_t *g, void *obj, char *name);</p>
<h3>CALLBACKS</h3>
<p>Agcbdisc_t *agpopdisc(Agraph_t *g);<br />
void agpushdisc(Agraph_t *g, Agcbdisc_t *disc);<br />
void agmethod(Agraph_t *g, void *obj, Agcbdisc_t *disc, int initflag);</p>
<h3>MEMORY</h3>
<p>void *agalloc(Agraph_t *g, size_t request);<br />
void *agrealloc(Agraph_t *g, void *ptr, size_t oldsize, size_t newsize);<br />
void agfree(Agraph_t *g, void *ptr);</p>
<h3>GENERIC OBJECTS</h3>
<p>Agraph_t *agraphof(void *);<br />
char *agnameof(void *);<br />
int agisarootobj(void *);<br />
Agrec_t *AGDATA(void *obj);<br />
ulong AGID(void *obj);<br />
int AGTYPE(void *obj);</p>
<h2>DESCRIPTION</h2>
<p> Libagraph supports graph programming by maintaining graphs in memory and reading and writing graph files. Graphs, nodes and edges may be attributed with programmer-defined records and string name-value pairs. Graphs are composed of nodes, edges, and nested subgraphs. Internally, Libagraph depends extensively on Libcdt (formerly Libdict) for set representation. </p>
<p> All of Libagraph&#8217;s global symbols have the prefix <code>ag</code> (case varying).</p>
<h2>GRAPHS</h2>
<p> A &#8220;main&#8221; or &#8220;root&#8221; graph defines a namespace for a collection of graph objects (subgraphs, nodes, edges) and their attributes. Objects may be named by unique strings or by 32-bit IDs. By default <code>data</code> points to runtime records containing application-dependent data, keyed by name (see Attributes). <code>desc</code> records if a graph is directed or undirected, and if it is strict or allows multi-edges and self-arcs. </p>
<p> <code>agopen</code> creates a new graph with the given name and graph kind descriptor (global values are <code>Agdirected</code>, <code>Agundirected</code>, <code>Agstrictdirected</code>, and <code>Agstrictundirected</code>). <code>agclose</code> deletes a graph, freeing all its associated storage. <code>agread</code> and <code>agwrite</code> perform file I/O (see Graph File Language bellow). <code>agsubg</code> creates a new subgraph, which always inherits the graph kind of its parent. The new subgraph is initially empty. Nested subgraph trees may be created. The name of a subgraph is interpreted only relative to the given parent graph. <code>agsubglist</code> returns a list (possibly empty) of subgraphs of a given graph. </p>
<p> By default, nodes are kept in ordered sets in <code>n_dict</code>, allowing efficient random access to insert, find, and delete nodes. Similarly the edges of each node are kept in ordered sets. The sets are maintained as splay tree dictionaries. <code>agflatten</code> allows flattening trees into linked lists, which may thereafter be traversed very quickly without function calls for low overhead in critical sections of code. In this mode, sets are locked to prevent updates or random access searches, though it is still legal to call Libagraph to scan lists sequentially. The flag argument requests flattening and locking (if boolean true), or unlocking (if false). In-line functions or macros for list traversal are given below under Nodes and Edges. Note that flattening a graph does not automatically flatten its subgraphs. </p>
<p> <code>agnnodes</code>, <code>agnedges</code>, and <code>agdegree</code> return the cardinalities of node and edge sets. The latter takes flags to select in-edges, out-edges, or both. </p>
<p> <code>Agdisc_t</code> specifies callbacks invoked when initializing, modifying, or finalizinf graph objects. (Casual users can ignore the following.) Disciplines are kept on a stack. Libagraph automatically calls the methods on the stack, top-down. A method can obtain its data (closure) via aggetuserptr. </p>
<p> When Libagraph is compiled with Vmalloc, each graph has its own heap. Programmers may allocate application-dependent data within the same heap as the rest of the graph. The advantage is that a graph can be deleted by atomically freeing its entire heap without scanning each individual node and edge.</p>
<h2>NODES</h2>
<p> A node is identified uniquely by name and graph pointer. Node pointers are not unique&#8212; separate node structs are created per subgraph. Name pointers are unique, though, because each graph has its own shared string pool. </p>
<p> <code>agnode</code> searches in a graph or subgraph for a node with the given name, and returns it if found. If not found, if <code>createflag</code> is boolean true a new node is created and returned, otherwise a nil pointer is returned. <code>agsubnode</code> takes an existing node as a template, usually to find or insert a node in a subgraph. </p>
<p> The default ordering of nodes is by order of creation (sequence). Internally, Libagraph switches between ID searching and sequence ordering as necessary. <code>agfstnode</code> and <code>agnxtnode</code> are the usual functions for scanning node lists. When node sets are flattened it is permissible to call <code>agfstnode</code> and <code>agnxtnode</code>, but conflicting attempts to insert, delete, or search for nodes cause a runtime error.</p>
<h2>EDGES</h2>
<p> An abstract edge is represented by two edge structs. There is one pointing to each terminal node, and residing in an edge list of the opposite node. The object tag distinguishes between these otherwise symmetric records, to allow obtaining head and tail. If a graph has multi-edges between the same nodes, the name field serves as a secondary key. </p>
<p> <code>agedge</code> searches in a graph of subgraph for an edge between the given endpoints (with an optional multi-edge selector name) and returns it if found. Otherwise, if <code>createflag</code> is boolean true, a new edge is created and returned: otherwise a nil pointer is returned. If the <code>name</code> is (char*)0 then an anonymous internal value is generated. <code>agfstin</code>, <code>agnxtint</code>, <code>agfstout</code>, and <code>agnxtout</code> visit directed in- and out- edge lists, and ordinarily apply only in directed graphs. <code>agfstedge</code> and <code>agnxtedge</code> visit all edges incident to a node. In traversing lists, e-&gt;node always points to the &#8220;other&#8221; node of the edge, To resolve ambiguity between in- and out-edge structs, <code>aghead</code> and <code>agtail</code> are macros or inline functions to find endpoints by checking object tags. <code>agopp</code> returns the &#8220;opposite&#8221; edge struct. Similarly <code>agfout</code>, <code>agfin</code>, and <code>agnedge</code> operate on flattened edge lists. </p>
<h2>STRING ATTRIBUTES</h2>
<p> Programmer-defined values may be dynamically attached to graphs, subgraphs, nodes, and edges. Such values are either uninterpreted binary records (for implementing efficient algorithms) or character string data (for I/O). String attributes are handled automatically in reading and writing graph files. Uninterpreted records are ignored; any desired conversion must be coded explicitly by application programmers. </p>
<p> A string attribute is identified by name and by an internal symbol table entry (<code>Agsym_t</code>) created by Libagraph. Attributes of nodes, edges, and graphs (with their subgraphs) have separate namespaces. The contents of an <code>Agsym_t</code> is listed below, followed by primitives to operate on string attributes.<br />
typedef struct Agsym_s { /* symbol in one of the above dictionaries */<br />
    Dtlink_t link;<br />
    char *name;   /* attribute&#8217;s name */<br />
    char *defval; /* its default value for initialization */<br />
    int id;       /* its index in attr[] */<br />
} Agsym_t;</p>
<p> <code>agattr</code> creates or looks up attributes. <code>kind</code> may be <code>AGRAPH</code>, <code>AGNODE</code>, or <code>AGEDGE</code>. If <code>value</code> is <code>(char*)0)</code>, the request is to search for an existing attribute of the given kind and name. Otherwise, if the attribute already exists, its default for creating new objects is set to the given value; if it does not exist, a new attribute is created with the given default, and the default is applied to all pre-existing objects of the given kind. </p>
<p> <code>agdictof</code> returns a Libdict set of all the attributes of a given kind. <code>agdictsym</code> is a utility function that finds an entry in one of these dictionary sets. </p>
<p> <code>agget</code> and <code>agset</code> read and update string attributes. The first argument should be a graph, node, or edge struct pointer. <code>agxset</code> and <code>agxset</code> take a symbol table entry reference instead of a name, to avoid the cost of looking up attribute names inside loops. Note that Libagraph performs its own storage management of strings. The calling program does not need to dynamically allocate storage. </p>
<h2>RECORDS</h2>
<p> Uninterpreted records may be attached to graphs (subgraphs), nodes, and edges for efficient operations on values such as marks, weights, counts, and pointers needed by algorithms. Application programmers define the fields of these records, but they have a common header as shown below.<br />
typedef struct Agrec_s {<br />
    char *name;<br />
    struct Agrec_s *next;<br />
    /* programmer-defined follows */<br />
} Agrec_t;<br />
 Records are created and managed by Libagraph. In each graph, node, or edge, <code>data</code> points to a circular list of records. The <code>name</code> field distinguishes various types of records, and is programmer defined (Libagraph reserves the prefix <code>_ag</code>). <code>next</code> stores the list pointers. The remainder of a record may contain application-dependent fields. <code>agnewrec</code> creates one new record of the given size and attaches it to the given object (graph, node, or edge). <code>agdelrec</code> is the corresponding function to delete records. <code>aggetrec</code> finds a record with the given name. </p>
<p> To allow referencing application-dependent data without function calls or linear search, Libagraph allows setting and locking the <code>data</code> field of a graph, node, or edge on a particular record. The <code>move_to_front</code> flag may be <code>AG_MTF_FALSE</code>, <code>AG_MTF_SOFT</code>, or <code>AG_MTF_HARD</code> accordingly. The <code>AG_MTF_SOFT</code> field is only a hint that decreases overhead in subsequent calls of <code>aggetrec</code>; <code>AG_MTF_HARD</code> guarantees that a lock was obtained. To release locks, use <code>AG_MTF_SOFT</code> or <code>AG_MTF_FALSE</code>. Use of this feature implies cooperation or at least isolation from other functions also using the move-to-front convention. </p>
<p> A cast (generally using a macro or inline function) is then needed to convert the <code>data</code> pointer to an appropriate programmer-defined type. </p>
<h2>DISCIPLINES</h2>
<p> Programmer-defined disciplines customize certain resources- ID namespace, memory, and I/O &#8211; needed by Libagraph. A discipline struct (or NIL) is passed at graph creation time.<br />
struct Agdisc_s { /* user&#8217;s discipline */<br />
    Agmemdisc_t *mem;<br />
    Agiddisc_t *id;<br />
    Agiodisc_t *io;<br />
};<br />
 A default discipline is supplied when NIL is given for any of these fields. </p>
<p> An ID allocator discipline allows a client to control assignment of IDs (uninterpreted 32-bit values) to objects, and possibly how they are mapped to and from strings. </p>
<p>struct Agiddisc_s {             /* object ID allocator */<br />
    void *(*open)(Agraph_t *g); /* associated with a graph */<br />
    int (*map)(void *state, int objtype, char *str, ulong *id, int createflag);<br />
    int (*alloc)(void *state, int objtype, ulong id);<br />
    void (*free)(void *state, int objtype, ulong id);<br />
    char *(*print)(void *state, int objtype, ulong id);<br />
    void (*close)(void *state);<br />
};</p>
<p> open permits the ID discipline to initialize any data structures that maintains per individual graph. Its return value is then passed as the first argument to all subsequent ID manager calls. </p>
<p> alloc informs the ID manager that Libagraph is attempting to create an object with a specific ID that was given by a client. The ID manager should return TRUE (nonzero) if the ID can be allocated, or FALSE (which aborts the operation). </p>
<p> free is called to inform the ID manager that the object labeled with the given ID is about to go out of existence. </p>
<p> map is called to create or look-up IDs by string name (if supported by the ID manager). Returning TRUE (nonzero) in all cases means that the request succeeded (with a valid ID stored through result. There are four cases: </p>
<p> name != NULL and createflag == 1: This requests mapping a string (e.g. a name in a graph file) into a new ID. If the ID manager can comply, then it stores the result and returns TRUE. It is then also responsible for being able to print the ID again as a string. Otherwise the ID manager may return FALSE but it must implement the following (at least for graph file reading and writing to work): </p>
<p> name == NULL and createflag == 1: The ID manager creates a unique new ID of its own choosing. Although it may return FALSE if it does not support anonymous objects, but this is strongly discouraged (to support &quot;local names&quot; in graph files.) </p>
<p> name != NULL and createflag == 0: This is a namespace probe. If the name was previously mapped into an allocated ID by the ID manager, then the manager must return this ID. Otherwise, the ID manager may either return FALSE, or may store any unallocated ID into result. (This is convenient, for example, if names are known to be digit strings that are directly converted into 32 bit values.) </p>
<p> name == NULL and createflag == 0: forbidden. </p>
<p> print should return print is allowed to return a pointer to a static buffer; a caller must copy its value if needed past subsequent calls. NULL should be returned by ID managers that do not map names. </p>
<p> The map and alloc calls do not pass a pointer to the newly allocated object. If a client needs to install object pointers in a handle table, it can obtain them via new object callbacks.<br />
struct Agiodisc_s {<br />
    int (*fread)(void *chan, char *buf, int bufsize);<br />
    int (*putstr)(void *chan, char *str);<br />
    int (*flush)(void *chan); /* sync */<br />
                              /* error messages? */<br />
};<br />
struct Agmemdisc_s {     /* memory allocator */<br />
    void *(*open)(void); /* independent of other resources */<br />
    void *(*alloc)(void *state, size_t req);<br />
    void *(*resize)(void *state, void *ptr, size_t old, size_t req);<br />
    void (*free)(void *state, void *ptr);<br />
    void (*close)(void *state);<br />
};</p>
<h2>EXAMPLE PROGRAM</h2>
<p>#include &lt;graphviz/agraph.h&gt;<br />
typedef struct mydata_s {<br />
    int x, y, z;<br />
} mydata;<br />
main(int argc, char **argv)<br />
{<br />
    Agraph_t *g;<br />
    Agnode_t *v;<br />
    Agedge_t *e;<br />
    Agsym_t *attr;<br />
    Dict_t *d int cnt;<br />
    mydata *p;<br />
    if (g = agread(stdin, NIL(Agdisc_t *))) {<br />
        /* dtsize() is a Libdict primitive */<br />
        fprintf(stderr, &#8220;%s has %d node attributes,<br />
                dtsize(agdictof(g, AGNODE)));<br />
        attr = agattr(g, AGNODE, &#8220;color&#8221;, &#8220;blue&#8221;);<br />
        /* create a new graph */<br />
        h = agopen(&#8220;tmp&#8221;, g-&gt;desc);<br />
        /* this is a way of counting all the edges of the graph */<br />
        cnt = 0;<br />
        for (v = agfstnode(g); v; v = agnxtnode(g, v))<br />
            for (e = agfstout(g, v); e; e = agnxtout(g, e))<br />
                cnt++;<br />
        /* using inline functions or macros, attach records to edges */<br />
        agflatten(g);<br />
        for (v = agfstn(g); v; v = agnxtn(v))<br />
            for (e = agfout(v); e; e; = agnxte(e)) {<br />
                p = (mydata *)agnewrec(g, e, &#8220;mydata&#8221;, sizeof(mydata));<br />
                p-&gt;x = 27; /* meaningless example */<br />
            }<br />
    }<br />
}</p>
<h2>EXAMPLE GRAPH FILES</h2>
<pre><code>
digraph G
{
    a-&gt;b;
    c[shape = box];
    a -&gt; c [weight=29,label="some text];
    subgraph anything {
        /* the following affects only x,y,z */
        node[shape = circle];
        a;
        x;
        y-&gt;z;
        y-&gt;z; /* multiple edges */
    }
}
strict graph H
{
    n0-- n1-- n2-- n0; /* a cycle */
    n0-- {a b c d};    /* a star */
    n0-- n3;
    n0-- n3[weight = 1]; /* same edge because graph is strict */
}
</code></pre>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/3-libcdt/">Libcdt</a>(3) </p>
<h2>BUGS</h2>
<p> The root graph <code>name</code> is treated as a comment. </p>
<p> There is no way to delete string attributes or modify edge keys. </p>
<p> Strings and uninterpreted records could be treatly more uniformly. </p>
<h2>AUTHOR</h2>
<p> Stephen North, north [at] research.att.com, AT&amp;T Research. </p>
<h2>Index</h2>
