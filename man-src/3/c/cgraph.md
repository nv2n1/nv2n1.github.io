---
title: "cgraph(3)"
name: "cgraph"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cgraph/"
description: "libcgraph – abstract graph library"
---

<h2>NAME</h2>
<p> <code>libcgraph</code> &#8211; abstract graph library</p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;graphviz/cgraph.h&gt;
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
Agraph_t *agread(void *channel, Agdisc_t *);<br />
void agreadline(int line_no);<br />
void agsetfile(char *file_name);<br />
Agraph_t *agconcat(Agraph_t *g, void *channel, Agdisc_t *disc) int agwrite(Agraph_t *g, void *channel);<br />
int agnnodes(Agraph_t *g), agnedges(Agraph_t *g);<br />
int agisdirected(Agraph_t *g), agisundirected(Agraph_t *g), agisstrict(Agraph_t *g), agissimple(Agraph_t *g);</p>
<h3>SUBGRAPHS</h3>
<p>Agraph_t *agsubg(Agraph_t *g, char *name, int createflag);<br />
Agraph_t *agidsubg(Agraph_t *g, unsigned long id, int cflag);<br />
Agraph_t *agfstsubg(Agraph_t *g), agnxtsubg(Agraph_t *);<br />
Agraph_t *agparent(Agraph_t *g);<br />
int agdelsubg(Agraph_t *g, Agraph_t *sub); /* same as agclose() */</p>
<h3>NODES</h3>
<p>Agnode_t *agnode(Agraph_t *g, char *name, int createflag);<br />
Agnode_t *agidnode(Agraph_t *g, ulong id, int createflag);<br />
Agnode_t *agsubnode(Agraph_t *g, Agnode_t *n, int createflag);<br />
Agnode_t *agfstnode(Agraph_t *g);<br />
Agnode_t *agnxtnode(Agraph_t *g, Agnode_t *n);<br />
Agnode_t *agprvnode(Agraph_t *g, Agnode_t *n);<br />
Agnode_t *aglstnode(Agraph_t *g);<br />
int agdelnode(Agraph_t *g, Agnode_t *n);<br />
int agdegree(Agnode_t *n, int use_inedges, int use_outedges);</p>
<h3>EDGES</h3>
<p>Agedge_t *agedge(Agraph_t *g, Agnode_t *t, Agnode_t *h, char *name, int createflag);<br />
Agedge_t *agidedge(Agraph_t *g, Agnode_t *t, Agnode_t *h, unsigned long id, int createflag);<br />
Agedge_t *agsubedge(Agraph_t *g, Agedge_t *e, int createflag);<br />
Agnode_t *aghead(Agedge_t *e), *agtail(Agedge_t *e);<br />
Agedge_t *agfstedge(Agraph_t *g, Agnode_t *n);<br />
Agedge_t *agnxtedge(Agraph_t *g, Agedge_t *e, Agnode_t *n);<br />
Agedge_t *agfstin(Agraph_t *g, Agnode_t *n);<br />
Agedge_t *agnxtin(Agraph_t *g, Agedge_t *e);<br />
Agedge_t *agfstout(Agraph_t *g, Agnode_t *n);<br />
Agedge_t *agnxtout(Agraph_t *g, Agedge_t *e);<br />
int agdeledge(Agraph_t *g, Agedge_t *e);</p>
<h3>STRING ATTRIBUTES</h3>
<p>Agsym_t *agattr(Agraph_t *g, int kind, char *name, char *value);<br />
Agsym_t *agattrsym(void *obj, char *name);<br />
Agsym_t *agnxtattr(Agraph_t *g, int kind, Agsym_t *attr);<br />
char *agget(void *obj, char *name);<br />
char *agxget(void *obj, Agsym_t *sym);<br />
int agset(void *obj, char *name, char *value);<br />
int agxset(void *obj, Agsym_t *sym, char *value);<br />
int agsafeset(void *obj, char *name, char *value, char *def);</p>
<h3>RECORDS</h3>
<p>void *agbindrec(void *obj, char *name, unsigned int size, move_to_front);<br />
Agrec_t *aggetrec(void *obj, char *name, int move_to_front);<br />
int agdelrec(Agraph_t *g, void *obj, char *name);<br />
int agcopyattr(void *, void *);<br />
void aginit(Agraph_t *g, int kind, char *rec_name, int rec_size, int move_to_front);<br />
void agclean(Agraph_t *g, int kind, char *rec_name);</p>
<h3>CALLBACKS</h3>
<p>Agcbdisc_t *agpopdisc(Agraph_t *g);<br />
void agpushdisc(Agraph_t *g, Agcbdisc_t *disc);<br />
void agmethod(Agraph_t *g, void *obj, Agcbdisc_t *disc, int initflag);</p>
<h3>MEMORY</h3>
<p>void *agalloc(Agraph_t *g, size_t request);<br />
void *agrealloc(Agraph_t *g, void *ptr, size_t oldsize, size_t newsize);<br />
void agfree(Agraph_t *g, void *ptr);</p>
<h3>STRINGS</h3>
<p>char *agstrdup(Agraph_t *, char *);<br />
char *agstrdup_html(Agraph_t *, char *);<br />
int aghtmlstr(char *);<br />
char *agstrbind(Agraph_t *g, char *);<br />
int strfree(Agraph_t *, char *);<br />
char *agcanonStr(char *);<br />
char *agstrcanon(char *, char *);</p>
<h3>GENERIC OBJECTS</h3>
<p>Agraph_t *agraphof(void *);<br />
Agraph_t *agroot(void *);<br />
int agcontains(Agraph_t *, void *);<br />
char *agnameof(void *);<br />
void agdelete(Agraph_t *g, void *obj);<br />
int agobjkind(void *obj);<br />
Agrec_t *AGDATA(void *obj);<br />
ulong AGID(void *obj);<br />
int AGTYPE(void *obj);</p>
<h3>ERROR REPORTING</h3>
<p>typedef enum { AGWARN,<br />
               AGERR,<br />
               AGMAX,<br />
               AGPREV } agerrlevel_t;<br />
typedef int (*agusererrf)(char *);<br />
agerrlevel_t agerrno;<br />
agerrlevel_t agseterr(agerrlevel_t);<br />
char *aglasterr(void);<br />
int agerr(agerrlevel_t level, char *fmt, &#8230;);<br />
void agerrorf(char *fmt, &#8230;);<br />
void agwarningf(char *fmt, &#8230;);<br />
int agerrors(void);<br />
agusererrf agseterrf(agusererrf);</p>
<h2>DESCRIPTION</h2>
<p> Libcgraph supports graph programming by maintaining graphs in memory and reading and writing graph files. Graphs are composed of nodes, edges, and nested subgraphs. These graph objects may be attributed with string name-value pairs and programmer-defined records (see Attributes). </p>
<p> All of Libcgraph&#8217;s global symbols have the prefix <code>ag</code> (case varying).</p>
<h2>GRAPH AND SUBGRAPHS</h2>
<p> A &#8220;main&#8221; or &#8220;root&#8221; graph defines a namespace for a collection of graph objects (subgraphs, nodes, edges) and their attributes. Objects may be named by unique strings or by integer IDs. </p>
<p> <code>agopen</code> creates a new graph with the given name and kind. (Graph kinds are <code>Agdirected</code>, <code>Agundirected</code>, <code>Agstrictdirected</code>, and <code>Agstrictundirected</code>. A strict graph cannot have multi-edges or self-arcs.) <code>agclose</code> deletes a graph, freeing its associated storage. <code>agread</code>, <code>agwrite</code>, and <code>agconcat</code> perform file I/O using the graph file language described below. <code>agread</code> constructs a new graph while <code>agconcat</code> merges the file contents with a pre-existing graph. Though I/O methods may be overridden, the default is that the channel argument is a stdio FILE pointer. <code>agsetfile</code> and <code>agreadline</code> are helper functions that simply set the current file name and input line number for subsequent error reporting. </p>
<p> <code>agsubg</code> finds or creates a subgraph by name. A new subgraph is is initially empty and is of the same kind as its parent. Nested subgraph trees may be created. A subgraph&#8217;s name is only interpreted relative to its parent. A program can scan subgraphs under a given graph using <code>agfstsubg</code> and agnxtsubg. A subgraph is deleted with <code>agdelsubg</code> (or <code>agclose</code>). </p>
<p> By default, nodes are stored in ordered sets for efficient random access to insert, find, and delete nodes. The edges of a node are also stored in ordered sets. The sets are maintained internally as splay tree dictionaries using Phong Vo&#8217;s cdt library. </p>
<p> <code>agnnodes</code>, <code>agnedges</code>, and <code>agdegree</code> return the sizes of node and edge sets of a graph. The <code>agdegree</code> returns the size of the edge set of a nodes, and takes flags to select in-edges, out-edges, or both. </p>
<p> An <code>Agdisc_t</code> defines callbacks to be invoked by libcgraph when initializing, modifying, or finalizing graph objects. (Casual users can ignore the following.) Disciplines are kept on a stack. Libcgraph automatically calls the methods on the stack, top-down. Callbacks are installed with <code>agpushdisc</code>, uninstalled with <code>agpopdisc</code>, and can be held pending or released via <code>agcallbacks</code>. </p>
<p> (Casual users may ignore the following. When Libcgraph is compiled with Vmalloc (which is not the default), each graph has its own heap. Programmers may allocate application-dependent data within the same heap as the rest of the graph. The advantage is that a graph can be deleted by atomically freeing its entire heap without scanning each individual node and edge.</p>
<h2>NODES</h2>
<p> A node is created by giving a unique string name or programmer defined integer ID, and is represented by a unique internal object. (Node equality can checked by pointer comparison.) </p>
<p> <code>agnode</code> searches in a graph or subgraph for a node with the given name, and returns it if found. If not found, if <code>createflag</code> is boolean true a new node is created and returned, otherwise a nil pointer is returned. <code>agidnode</code> allows a programmer to specify the node by a unique integer ID. <code>agsubnode</code> performs a similar operation on an existing node and a subgraph. </p>
<p> <code>agfstnode</code> and <code>agnxtnode</code> scan node lists. <code>agprvnode</code> and aglstnode are symmetric but scan backward. The default sequence is order of creation (object timestamp.) <code>agdelnode</code> removes a node from a graph or subgraph.</p>
<h2>EDGES</h2>
<p> An abstract edge has two endpoint nodes called tail and head where the all outedges of the same node have it as the tail value and similarly all inedges have it as the head. In an undirected graph, head and tail are interchangeable. If a graph has multi-edges between the same pair of nodes, the edge&#8217;s string name behaves as a secondary key. </p>
<p> <code>agedge</code> searches in a graph of subgraph for an edge between the given endpoints (with an optional multi-edge selector name) and returns it if found. Otherwise, if <code>createflag</code> is boolean true, a new edge is created and returned: otherwise a nil pointer is returned. If the <code>name</code> is NULL, then an anonymous internal value is generated. <code>agidedge</code> allows a programmer to create an edge by giving its unique integer ID. <code>agfstin</code>, <code>agnxtint</code>, <code>agfstout</code>, and <code>agnxtout</code> visit directed in- and out- edge lists, and ordinarily apply only in directed graphs. <code>agfstedge</code> and <code>agnxtedge</code> visit all edges incident to a node. <code>agtail</code> and <code>aghead</code> get the endpoint of an edge.</p>
<h2>INTERNAL ATTRIBUTES</h2>
<p> Programmer-defined values may be dynamically attached to graphs, subgraphs, nodes, and edges. Such values are either uninterpreted binary records (for implementing efficient algorithms) or character string data (for I/O).</p>
<h2>STRING ATTRIBUTES</h2>
<p> String attributes are handled automatically in reading and writing graph files. A string attribute is identified by name and by an internal symbol table entry (<code>Agsym_t</code>) created by Libcgraph. Attributes of nodes, edges, and graphs (with their subgraphs) have separate namespaces. The contents of an <code>Agsym_t</code> is listed below, followed by primitives to operate on string attributes.<br />
typedef struct Agsym_s { /* symbol in one of the above dictionaries */<br />
    Dtlink_t link;<br />
    char *name;          /* attribute&#8217;s name */<br />
    char *defval;        /* its default value for initialization */<br />
    int id;              /* its index in attr[] */<br />
    unsigned char kind;  /* referent object type */<br />
    unsigned char fixed; /* immutable value */<br />
} Agsym_t;</p>
<p> <code>agattr</code> creates or looks up attributes. <code>kind</code> may be <code>AGRAPH</code>, <code>AGNODE</code>, or <code>AGEDGE</code>. If <code>value</code> is <code>(char*)0)</code>, the request is to search for an existing attribute of the given kind and name. Otherwise, if the attribute already exists, its default for creating new objects is set to the given value; if it does not exist, a new attribute is created with the given default, and the default is applied to all pre-existing objects of the given kind. If <code>g</code> is NIL, the default is set for all graphs created subsequently. <code>agattrsym</code> is a helper function that looks up an attribute for a graph object given as an argument. <code>agnxtattr</code> permits traversing the list of attributes of a given type. If <code>NIL</code> is passed as an argument it gets the first attribute, otherwise it returns the next one in succession or returns <code>NIL</code> at the end of the list. <code>agget</code> and agset allow fetching and updating a string attribute for an object taking the attribute name as an argument. <code>agxget</code> and <code>agxset</code> do this but with an attribute symbol table entry as an argument (to avoid the cost of the string lookup). <code>agsafeset</code> is a convenience function that ensures the given attribute is declared before setting it locally on an object. </p>
<h2>STRINGS</h2>
<p> Libcgraph performs its own storage management of strings as reference-counted strings. The caller does not need to dynamically allocate storage. </p>
<p> <code>agstrdup</code> returns a pointer to a reference-counted copy of the argument string, creating one if necessary. <code>agstrbind</code> returns a pointer to a reference-counted string if it exists, or NULL if not. All uses of cgraph strings need to be freed using <code>agstrfree</code> in order to correctly maintain the reference count. </p>
<p> <code>agcanonStr</code> returns a pointer to a version of the input string canonicalized for output for later re-parsing. This includes quoting special characters and keywords. It uses its own internal buffer, so the value will be lost on the next call to <code>agcanonStr</code>. <code>agstrcanon</code> is an unsafe version of <code>agcanonStr</code>, in which the application passes in a buffer as the second argument. Note that the buffer may not be used; if the input string is in canonical form, the function will just return a pointer to it. </p>
<p> The cgraph parser handles HTML-like strings. These should be indistinguishable from other strings for most purposes. To create an HTML-like string, use <code>agstrdup_html</code>. The <code>aghtmlstr</code> function can be used to query if a string is an ordinary string or an HTML-like string.</p>
<h2>RECORDS</h2>
<p> Uninterpreted records may be attached to graphs, subgraphs, nodes, and edges for efficient operations on values such as marks, weights, counts, and pointers needed by algorithms. Application programmers define the fields of these records, but they must be declared with a common header as shown below. </p>
<p>typedef struct Agrec_s {<br />
    Agrec_t header;<br />
    /* programmer-defined fields follow */<br />
} Agrec_t;</p>
<p> Records are created and managed by Libcgraph. A programmer must explicitly attach them to the objects in a graph, either to individual objects one at a time via <code>agbindrec</code>, or to all the objects of the same class in a graph via <code>aginit</code>. (Note that for graphs, aginit is applied recursively to the graph and its subgraphs if rec_size is negative (of the actual rec_size.)) The <code>name</code> argument a record distinguishes various types of records, and is programmer defined (Libcgraph reserves the prefix <code>_ag</code>). If size is 0, the call to <code>agbindrec</code> is simply a lookup. <code>agdelrec</code> is the deletes records one at a time. <code>agclean</code> does the same for all objects of the same class in an entire graph. </p>
<p> Internally, records are maintained in circular linked lists attached to graph objects. To allow referencing application-dependent data without function calls or search, Libcgraph allows setting and locking the list pointer of a graph, node, or edge on a particular record. This pointer can be obtained with the macro <code>AGDATA(obj)</code>. A cast, generally within a macro or inline function, is usually applied to convert the list pointer to an appropriate programmer-defined type. </p>
<p> To control the setting of this pointer, the <code>move_to_front</code> flag may be <code>AG_MTF_FALSE</code>, <code>AG_MTF_SOFT</code>, or <code>AG_MTF_HARD</code> accordingly. The <code>AG_MTF_SOFT</code> field is only a hint that decreases overhead in subsequent calls of <code>aggetrec</code>; <code>AG_MTF_HARD</code> guarantees that a lock was obtained. To release locks, use <code>AG_MTF_SOFT</code> or <code>AG_MTF_FALSE</code>. Use of this feature implies cooperation or at least isolation from other functions also using the move-to-front convention. </p>
<h2>DISCIPLINES</h2>
<p> (The following is not intended for casual users.) Programmer-defined disciplines customize certain resources- ID namespace, memory, and I/O &#8211; needed by Libcgraph. A discipline struct (or NIL) is passed at graph creation time. </p>
<p>struct Agdisc_s { /* user&#8217;s discipline */<br />
    Agmemdisc_t *mem;<br />
    Agiddisc_t *id;<br />
    Agiodisc_t *io;<br />
};</p>
<p> A default discipline is supplied when NIL is given for any of these fields. </p>
<p> An ID allocator discipline allows a client to control assignment of IDs (uninterpreted integer values) to objects, and possibly how they are mapped to and from strings. </p>
<p>struct Agiddisc_s {                         /* object ID allocator */<br />
    void *(*open)(Agraph_t *g, Agdisc_t *); /* associated with a graph */<br />
    long (*map)(void *state, int objtype, char *str, unsigned long *id, int createflag);<br />
    long (*alloc)(void *state, int objtype, unsigned long id);<br />
    void (*free)(void *state, int objtype, unsigned long id);<br />
    char *(*print)(void *state, int objtype, unsigned long id);<br />
    void (*close)(void *state);<br />
};</p>
<p> <i>open</i> permits the ID discipline to initialize any data structures that it maintains per individual graph. Its return value is then passed as the first argument (void *state) to all subsequent ID manager calls. </p>
<p> <i>alloc</i> informs the ID manager that Libcgraph is attempting to create an object with a specific ID that was given by a client. The ID manager should return TRUE (nonzero) if the ID can be allocated, or FALSE (which aborts the operation). </p>
<p> <i>free</i> is called to inform the ID manager that the object labeled with the given ID is about to go out of existence. </p>
<p> <i>map</i> is called to create or look-up IDs by string name (if supported by the ID manager). Returning TRUE (nonzero) in all cases means that the request succeeded (with a valid ID stored through result. There are four cases: </p>
<p> <i>name != NULL</i> and createflag == 1: This requests mapping a string (e.g. a name in a graph file) into a new ID. If the ID manager can comply, then it stores the result and returns TRUE. It is then also responsible for being able to print the ID again as a string. Otherwise the ID manager may return FALSE but it must implement the following (at least for graph file reading and writing to work): </p>
<p> name == NULL and createflag == 1: The ID manager creates a unique new ID of its own choosing. Although it may return FALSE if it does not support anonymous objects, but this is strongly discouraged (to support &quot;local names&quot; in graph files.) </p>
<p> name != NULL and createflag == 0: This is a namespace probe. If the name was previously mapped into an allocated ID by the ID manager, then the manager must return this ID. Otherwise, the ID manager may either return FALSE, or may store any unallocated ID into result. (This is convenient, for example, if names are known to be digit strings that are directly converted into integer values.) </p>
<p> name == NULL and createflag == 0: forbidden. </p>
<p> print is allowed to return a pointer to a static buffer; a caller must copy its value if needed past subsequent calls. NULL should be returned by ID managers that do not map names. </p>
<p> The map and alloc calls do not pass a pointer to the newly allocated object. If a client needs to install object pointers in a handle table, it can obtain them via new object callbacks.<br />
struct Agiodisc_s {<br />
    int (*fread)(void *chan, char *buf, int bufsize);<br />
    int (*putstr)(void *chan, char *str);<br />
    int (*flush)(void *chan); /* sync */<br />
                              /* error messages? */<br />
};<br />
struct Agmemdisc_s {           /* memory allocator */<br />
    void *(*open)(Agdisc_t *); /* independent of other resources */<br />
    void *(*alloc)(void *state, size_t req);<br />
    void *(*resize)(void *state, void *ptr, size_t old, size_t req);<br />
    void (*free)(void *state, void *ptr);<br />
    void (*close)(void *state);<br />
};</p>
<h2>GENERIC OBJECTS</h2>
<p> <code>agroot</code> takes any graph object (graph, subgraph, node, edge) and returns the root graph in which it lives. <code>agraphof</code> does the same, except it is the identity function on graphs and subgraphs. Note that there is no function to return the least subgraph containing an object, in part because this is not well-defined as nodes and edges may be in incomparable subgraphs. </p>
<p> <code>agcontains(</code><i>g</i>,<i>obj</i>) returns non-zero if <i>obj</i> is a member of (sub)graph <i>g</i>. <code>agdelete(</code><i>g</i>,<i>obj</i>) is equivalent to <code>agclose</code>, <code>agdelnode</code>, and <code>agclose</code> for <i>obj</i> being a graph, node or edge, respectively. It returns -1 if <i>obj</i> does not belong to <i>g</i>. </p>
<p> <code>agnameof</code> returns a string descriptor for the object. It returns the name of the node or graph, and the key of an edge. <code>agobjkind</code> is a synonym for <code>AGTYPE</code>. </p>
<p> <code>AGDATA</code>, <code>AGID</code>, and <code>AGTYPE</code> are macros returning the specified fields of the argument object. The first is described in the <code>RECORDS</code> section above. The second returns the unique integer ID associated with the object. The last returns <code>AGRAPH</code>, <code>AGNODE</code>, and <code>AGEDGE</code> depending on the type of the object. </p>
<p> typedef int (*agusererrf) (char*); agusererrf agseterrf(agusererrf);</p>
<h2>ERROR REPORTING</h2>
<p> The library provides a variety of mechanisms to control the reporting of errors and warnings. At present, there are basically two types of messages: warnings and errors. A message is only written if its type has higher priority than a programmer-controlled minimum, which is <code>AGWARN</code> by default. The programmer can set this value using <code>agseterr</code>, which returns the previous value. Calling <code>agseterr(AGMAX)</code> turns off the writing of messages. </p>
<p> The function <code>agerr</code> if the main entry point for reporting an anomaly. The first argument indicates the type of message. Usually, the first argument in <code>AGWARN</code> or <code>AGERR</code> to indicate warnings and errors, respectively. Sometimes additional context information is only available in functions calling the function where the error is actually caught. In this case, the calling function can indicate that it is continuing the current error by using <code>AGPREV</code> as the first argument. The remaining arguments to <code>agerr</code> are the same as the arguments to <code>printf</code>. </p>
<p> The functions <code>agwarningf</code> and <code>agerrorf</code> are shorthand for <code>agerr(AGERR,&#8230;)</code> and <code>agerr(AGWARN,&#8230;)</code>, respectively. </p>
<p> Some applications desire to directly control the writing of messages. Such an application can use the function <code>agseterrf</code> to register the function that the library should call to actually write the message. The previous error function is returned. By default, the message is written to <code>stderr</code>. </p>
<p> Errors not written are stored in a log file. The last recorded error can be retreived by calling <code>aglasterr</code>. </p>
<p> The function <code>agerrors</code> returns non-zero if errors have been reported.</p>
<h2>EXAMPLE PROGRAM</h2>
<p>#include &lt;graphviz/cgraph.h&gt;<br />
typedef struct mydata_s {<br />
    Agrec_t hdr;<br />
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
        cnt = 0;<br />
        attr = 0;<br />
        while (attr = agnxtattr(g, AGNODE, attr))<br />
            cnt++;<br />
                printf(&#8220;The graph %s has %d attributes,agnameof(g),cnt);<br />
                /* make the graph have a node color attribute, default is blue */<br />
        attr = agattr(g,AGNODE,&#8221;color&#8221;,&#8221;blue&#8221;);<br />
        /* create a new graph of the same kind as g */<br />
        h = agopen(&#8220;tmp&#8221;,g-&gt;desc);<br />
        /* this is a way of counting all the edges of the graph */<br />
        cnt = 0;<br />
        for (v = agfstnode(g); v; v = agnxtnode(g,v))<br />
            for (e = agfstout(g,v); e; e = agnxtout(g,e))<br />
                cnt++;<br />
        /* attach records to edges */<br />
        for (v = agfstnode(g); v; v = agnxtnode(g,v))<br />
            for (e = agfstout(g,v); e; e; = agnxtout(g,e)) {<br />
            p = (mydata *)agbindrec(g, e, &#8220;mydata&#8221;, sizeof(mydata), TRUE);<br />
            p-&gt;x = 27;                        /* meaningless data access example */<br />
            ((mydata *)(AGDATA(e)))-&gt;y = 999; /* another example */<br />
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
<p> It is difficult to change endpoints of edges, delete string attributes or modify edge keys. The work-around is to create a new object and copy the contents of an old one (but new object obviously has a different ID, internal address, and object creation timestamp). </p>
<p> The API lacks convenient functions to substitute programmer-defined ordering of nodes and edges but in principle this can be supported. </p>
<p> The library is not thread safe.</p>
<h2>AUTHOR</h2>
<p> Stephen North, north [at] research.att.com, AT&amp;T Research. </p>
<h2>Index</h2>
