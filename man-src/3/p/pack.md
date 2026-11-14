---
title: "pack(3)"
name: "pack"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pack/"
description: "libpack – support for connected components"
---

<p><code>libpack</code> &#8211; support for connected components</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;graphviz/pack.h&gt;

typedef enum { l_clust,
               l_node,
               l_graph,
               l_array } pack_mode;

typedef struct {
    float aspect;        /* desired aspect ratio */
    int sz;              /* row/column size size */
    unsigned int margin; /* margin left around objects, in points */
    int doSplines;       /* use splines in constructing graph shape */
    pack_mode mode;      /* granularity and method */
    boolean *fixed;      /* fixed[i] == true implies g[i] should not be moved */
    packval_t *vals;     /* for arrays, sort numbers */
    int flags;
} pack_info;

point *putRects(int ng, boxf *bbs, pack_info *pinfo);
int packRects(int ng, boxf *bbs, pack_info *pinfo);

point *putGraphs(int, Agraph_t **, Agraph_t *, pack_info *);
int packGraphs(int, Agraph_t **, Agraph_t *, pack_info *);
int packSubgraphs(int, Agraph_t **, Agraph_t *, pack_info *);

pack_mode getPackMode(Agraph_t *, pack_mode dflt);
int getPack(Agraph_t *, int, int);

int isConnected(Agraph_t *);
Agraph_t **ccomps(Agraph_t *, int *, char *);
Agraph_t **pccomps(Agraph_t *, int *, char *, boolean *);
int nodeInduce(Agraph_t *);</code></pre>
<h2>Description</h2>
<p><i>libpack</i> supports the use of connected components in the context of laying out graphs using other <i>graphviz</i> libraries. One set of functions can be used to take a single graph and break it apart into connected components. A complementary set of functions takes a collection of graphs (not necessarily components of a single graph) which have been laid out separately, and packs them together. </p>
<p> As this library is meant to be used with <i>libcommon</i>, it relies on the <i>Agraphinfo_t</i>, <i>Agnodeinfo_t</i> and <i>Agedgeinfo_t</i> used in that library. The specific dependencies are given below in the function descriptions.</p>
<h3>Creating components</h3>
<h3> Agraph_t** ccomps (Agraph_t* g, int* cnt, char* pfx)</h3>
<p>The function <i>ccomps</i> takes a graph <i>g</i> and returns an array of pointers to subgraphs of <i>g</i> which are its connected components. <i>cnt</i> is set to the number of components. If <i>pfx</i> is non-NULL, it is used as a prefix for the names of the subgraphs; otherwise, the string &#8220;_cc_&#8221; is used. Note that the subgraphs only contain the relevant nodes, not any corresponding edges. Depending on the use, this allows the caller to retrieve edge information from the root graph. </p>
<p> The array returned is obtained from <i>malloc</i> and must be freed by the caller. The function relies on the <i>mark</i> field in <i>Agnodeinfo_t</i>.</p>
<h3> Agraph_t** pccomps (Agraph_t* g, int* cnt, char* pfx, boolean* pinned)</h3>
<p>This is identical to <i>ccomps</i> except that is puts all pinned nodes in the first component returned. In addition, if <i>pinned</i> is non-NULL, it is set to true if pinned nodes are found and false otherwise.</p>
<h3> int nodeInduce (Agraph_t* g)</h3>
<p>This function takes a subgraph <i>g</i> and finds all edges in its root graph both of whose endpoints are in <i>g</i>. It returns the number of such edges and, if this edge is not already in the subgraph, it is added.</p>
<h3> int isConnected (Agraph_t* g)</h3>
<p>This function returns non-zero if the graph <i>g</i> is connected.</p>
<h3>Packing components</h3>
<h3> point* putGraphs (int ng, Agraph_t** gs, Agraph_t* root, pack_info ip)</h3>
<p><i>putGraphs</i> packs together a collection of laid out graphs into a single layout which avoids any overlap. It takes as input <i>ng</i> graphs <i>gs</i>. For each graph, it is assumed that all the nodes have been positioned using <i>pos</i>, and that the <i>xsize</i> and <i>ysize</i> fields have been set. </p>
<p> If <i>root</i> is non-NULL, it is taken as the root graph of the subgraphs <i>gs</i> and is used to find the edges. Otherwise, <i>putGraphs</i> uses the edges found in each graph <i>gs[i]</i>. </p>
<p> For the modes <i>l_node</i>, <i>l_clust</i>, and <i>l_graph</i>, the packing is done using the polyomino-based algorithm of Freivalds et al. This allows for a fairly tight packing, in which a convex part of one graph might be inserted into the concave part of another. The granularity of the polyominoes used depends on the value of <i>ip-&gt;mode</i>. If this is <i>l_node</i>, a polyomino is constructed to approximate the nodes and edges. If this is <i>l_clust</i>, the polyomino treats top-level clusters as single rectangles, unioned with the polyominoes for the remaining nodes and edges. If the value is <i>l_graph</i>, the polyomino for a graph is a single rectangle corresponding to the bounding box of the graph. </p>
<p> The mode <i>l_node</i> specifies that the graphs should be packed as an array. </p>
<p> If <i>ip-&gt;doSplines</i> is true, the function uses the spline information in the <i>spl</i> field of an edge, if it exists. Otherwise, the algorithm represents an edge as a straight line segment connecting node centers. </p>
<p> The parameter <i>ip-&gt;margin</i> specifies a boundary of <i>margin</i> points to be allowed around each node. It must be non-negative. </p>
<p> The parameter <i>ip-&gt;fixed</i>, if non-null, should point to an array of <i>ng</i> booleans. If <i>ip-&gt;fixed[i]</i> is true, graph <i>gs[i]</i> should be left at its original position. The packing will first first place all of the fixed graphs, then fill in the with the remaining graphs. </p>
<p> The function returns an array of points which can be used as the origin of the bounding box of each graph. If the graphs are translated to these positions, none of the graph components will overlap. The array returned is obtained from <i>malloc</i> and must be freed by the caller. If any problem occurs, <i>putGraphs</i> returns NULL. As a side-effect, at its start, <i>putGraphs</i> sets the <i>bb</i> of each graph to reflect its initial layout. Note that <i>putGraphs</i> does not do any translation or change the input graphs in any other way than setting the <i>bb</i>. </p>
<p> This function uses the <i>bb</i> field in <i>Agraphinfo_t</i>, the <i>pos</i>, <i>xsize</i> and <i>ysize</i> fields in <i>nodehinfo_t</i> and the <i>spl</i> field in <i>Aedgeinfo_t</i>.</p>
<h3> int packGraphs (int ng, Agraph_t** gs, Agraph_t* root, pack_info* ip)</h3>
<p>This function takes <i>ng</i> subgraphs <i>gs</i> of a root graph <i>root</i> and calls <i>putGraphs</i> with the given arguments to generate a packing of the subgraphs. If successful, it then invokes shifts the subgraphs to their new positions. It returns 0 on success.</p>
<h3> int packSubgraphs (int ng, Agraph_t** gs, Agraph_t* root, pack_info* ip)</h3>
<p>This function simply calls <i>packGraphs</i> with the given arguments, and then recomputes the bounding box of the <i>root</i> graph.</p>
<h3> int pack_graph(int ng, Agraph_t** gs, Agraph_t* root, boolean* fixed)</h3>
<p>uses <i>packSubgraphs</i> to place the individual subgraphs into a single layout with the parameters obtained from <i>getPackInfo</i>. If successful, <i>dotneato_postprocess</i> is called on the root graph.</p>
<h3> point* putRects (int ng, boxf* bbs, pack_info* ip)</h3>
<p><i>putRects</i> packs together a collection of rectangles into a single layout which avoids any overlap. It takes as input <i>ng</i> rectangles <i>bbs</i>. </p>
<p> Its behavior and return value are analogous to those of <i>putGraphs</i>. However, the modes <i>l_node</i> and <i>l_clust</i> are illegal. The fields <i>fixed</i> and <i>doSplines</i> of <i>ip</i> are unused.</p>
<h3> int packRects (int ng, boxf* bbs, pack_info* ip)</h3>
<p><i>packRects</i> is analogous to <i>packGraphs</i>: it calls <i>putRects</i> and, if this is successful, it translates the rectangles in <i>bbs</i> appropriately.</p>
<h3>Utility functions</h3>
<p>The library provides several functions which can be used to tailor the packing based on graph attributes.</p>
<h3> pack_mode parsePackModeInfo(char* p, pack_mode dflt, pack_info* pinfo)</h3>
<p>analyzes <i>p</i> as a string representation of pack mode, storing the information in <i>pinfo</i>. If <i>p</i> is &quot;cluster&quot;, it returns <i>l_clust</i>; for &quot;graph&quot;, it returns <i>l_graph</i>; for &quot;node&quot;, it returns <i>l_node</i>; for &quot;array&quot;, it returns <i>l_array</i>; for &quot;aspect&quot;, it returns <i>l_aspect</i>; otherwise, it returns <i>dflt</i>. Related data is also stored in <i>pinfo</i>.</p>
<h3> pack_mode getPackModeInfo(Agraph_t * g, pack_mode dflt, pack_info* pinfo)</h3>
<p>This function processes the graph&#8217;s <i>&quot;packmode&quot;</i> attribute, storing the information in <i>pinfo</i>. It returns <i>pinfo-&gt;mode</i>. The attribute is processed using <i>parsePackModeInfo</i> with <i>dflt</i> passed as the default argument.</p>
<h3> pack_mode getPackMode (Agraph_t* g, pack_mode dflt)</h3>
<p>This function returns a <i>pack_mode</i> associated with <i>g</i>.</p>
<h3> int getPack (Agraph_t* g, int not_def, int dflt)</h3>
<p>This function queries the graph attribute <i>&quot;pack&quot;</i>. If this is defined as a non-negative integer, the integer is returned; if it is defined as &quot;true&quot;, the value <i>dflt</i> is returned; otherwise, the value <i>not_def</i> is returned.</p>
<h3> pack_mode getPackInfo(Agraph_t * g, pack_mode dflt, int dfltMargin, pack_info* pinfo)</h3>
<p>This function calls both <i>getPackModeInfo</i> and <i>getPack</i>, storing the information in <i>pinfo</i>. <i>dfltMargin</i> is used for both integer arguments of <i>getPack</i>, with the result saved as <i>pinfo-&gt;margin</i>. It returns <i>pinfo-&gt;mode</i>.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-dot/">dot</a></code>(1), <code><a href="/docs/linux/man/1-neato/">neato</a></code>(1), <code><a href="/docs/linux/man/1-twopi/">twopi</a></code>(1), <code><a href="/docs/linux/man/3-libgraph/">libgraph</a></code>(3)<br />
 K. Freivalds et al., &quot;Disconnected Graph Layout and the Polyomino Packing Approach&quot;, GD0&#8217;01, LNCS 2265, pp. 378-391. </p>
<h2>Bugs</h2>
<p>The packing does not take into account edge or graph labels.</p>
<h2>Authors</h2>
<p>Emden Gansner (erg [at] research.att.com).</p>
