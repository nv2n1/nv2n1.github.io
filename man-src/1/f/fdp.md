---
title: "fdp(1)"
name: "fdp"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fdp/"
description: "dot – filter for drawing directed graphs neato – filter for drawing undirected graphs twopi – filter for radial layouts of graphs circo – filter for circular layout of graphs fdp – filter for drawi..."
---

<h2 class="name">NAME</h2>
<p> dot &#8211; filter for drawing directed graphs<br />
 neato &#8211; filter for drawing undirected graphs<br />
 twopi &#8211; filter for radial layouts of graphs<br />
 circo &#8211; filter for circular layout of graphs<br />
 fdp &#8211; filter for drawing undirected graphs<br />
 sfdp &#8211; filter for drawing large undirected graphs<br />
 patchwork &#8211; filter for squarified tree maps<br />
 osage &#8211; filter for array-based layouts </p>
<h2>SYNOPSIS</h2>
<p> <code>dot</code> [<i>options</i>] [files]<br />
 <code>neato</code> [<i>options</i>] [files]<br />
 <code>twopi</code> [<i>options</i>] [files]<br />
 <code>circo</code> [<i>options</i>] [files]<br />
 <code>fdp</code> [<i>options</i>] [files]<br />
 <code>sfdp</code> [<i>options</i>] [files]<br />
 <code>patchwork</code> [<i>options</i>] [files]<br />
 <code>osage</code> [<i>options</i>] [files]</p>
<h2>DESCRIPTION</h2>
<p> These are a collection of programs for drawing graphs. There is actually only one main program; the specific layout algorithms are implemented as plugins. Thus, they largely share all of the same command-line options. </p>
<p> <i>dot</i> draws directed graphs. It works well on directed acyclic graphs and other graphs that can be drawn as hierarchies or have a natural &#8220;flow.&#8221; </p>
<p> <i>neato</i> draws undirected graphs using a &#8220;spring&#8221; model and reducing the related energy (see Kamada and Kawai, Information Processing Letters 31:1, April 1989). </p>
<p> <i>twopi</i> draws graphs using a radial layout (see G. Wills, Symposium on Graph Drawing GD&#8217;97, September, 1997). Basically, one node is chosen as the center and put at the origin. The remaining nodes are placed on a sequence of concentric circles centered about the origin, each a fixed radial distance from the previous circle. All nodes distance 1 from the center are placed on the first circle; all nodes distance 1 from a node on the first circle are placed on the second circle; and so forth. </p>
<p> <i>circo</i> draws graphs using a circular layout (see Six and Tollis, GD &#8217;99 and ALENEX &#8217;99, and Kaufmann and Wiese, GD &#8217;02.) The tool identifies biconnected components and draws the nodes of the component on a circle. The block-cutpoint tree is then laid out using a recursive radial algorithm. Edge crossings within a circle are minimized by placing as many edges on the circle&#8217;s perimeter as possible. In particular, if the component is outerplanar, the component will have a planar layout. If a node belongs to multiple non-trivial biconnected components, the layout puts the node in one of them. By default, this is the first non-trivial component found in the search from the root component. </p>
<p> <i>fdp</i> draws undirected graphs using a &#8220;spring&#8221; model. It relies on a force-directed approach in the spirit of Fruchterman and Reingold (cf. Software-Practice &amp; Experience 21(11), 1991, pp. 1129-1164). </p>
<p> <i>sfdp</i> also draws undirected graphs using the &#8220;spring&#8221; model described above, but it uses a multi-scale approach to produce layouts of large graphs in a reasonably short time. </p>
<p> <i>patchwork</i> draws the graph as a squarified treemap (see M. Bruls et al., &#8220;Squarified treemaps&#8221;, Proc. Joint Eurographics and IEEE TCVG Symp. on Visualization, 2000, pp. 33-42). The clusters of the graph are used to specify the tree. </p>
<p> <i>osage</i> draws the graph using its cluster structure. For a given cluster, each of its subclusters is laid out internally. Then the subclusters, plus any remaining nodes, are repositioned based on the cluster&#8217;s <code>pack</code> and <code>packmode</code> attributes.</p>
<h2>OUTPUT FORMATS</h2>
<p> Graphviz uses an extensible plugin mechanism for its output renderers, so to see what output formats your installation of dot supports you can use &#8220;dot -T:&#8221; and check the warning message. Also, The plugin mechanism supports multiple implementations of the output formats, allowing variations in the renderers and formatters. To see what variants are available for a particular output format, use, for example: &#8220;dot -Tpng:&#8221; and to force a particular variant, use, for example: &#8220;dot -Tpng:gd&#8221; </p>
<p> Traditionally, Graphviz supports the following:<br />
 <code>-Tdot</code> (Dot format containing layout information),<br />
 <code>-Txdot</code> (Dot format containing complete layout information),<br />
 <code>-Tps</code> (PostScript),<br />
 <code>-Tpdf</code> (PDF),<br />
 <code>-Tsvg</code> <code>-Tsvgz</code> (Structured Vector Graphics),<br />
 <code>-Tfig</code> (XFIG graphics),<br />
 <code>-Tpng</code> (png bitmap graphics),<br />
 <code>-Tgif</code> (gif bitmap graphics),<br />
 <code>-Tjpg</code> <code>-Tjpeg</code> (jpeg bitmap graphics),<br />
 <code>-Tjson</code> (xdot information encoded in JSON),<br />
 <code>-Timap</code> (imagemap files for httpd servers for each node or edge that has a non-null <code>href</code> attribute.),<br />
 <code>-Tcmapx</code> (client-side imagemap for use in html and xhtml).<br />
 Additional less common or more special-purpose output formats can be found at //<a rel="nofollow" href="http://www.graphviz.org/content/output-formats.">http://www.graphviz.org/content/output-formats.</a> </p>
<p> Alternative plugins providing support for a given output format can be found from the error message resulting from appending a &#8216;:&#8217; to the format. e.g. <code>-Tpng:</code> The first plugin listed is always the default. </p>
<p> The <code>-P</code> switch can be used to produce a graph of all output variants supported by plugins in the local installation of graphviz.</p>
<h2>GRAPH FILE LANGUAGE</h2>
<p> Here is a synopsis of the graph file language, normally using the extension <code>.gv</code>, for graphs: </p>
<p> [<code>strict</code>] (<code>graph</code>|<code>digraph</code>) <i>name</i> { <i>statement-list</i> }<br />
 is the top-level graph. If the graph is <code>strict</code>, then multiple edges are not allowed between the same pairs of nodes. If it is a directed graph, indicated by <code>digraph</code>, then the <i>edgeop</i> must be &quot;-&gt;&quot;. If it is an undirected <code>graph</code> then the <i>edgeop</i> must be &quot;&#8211;&quot;. </p>
<p> Statements may be: </p>
<p> <i>name</i><code>=</code><i>val</i><code>;</code><br />
 <code>node [</code><i>name</i><code>=</code><i>val</i><code>];</code><br />
 <code>edge [</code><i>name</i><code>=</code><i>val</i><code>];</code><br />
 Set default graph, node, or edge attribute <i>name</i> to <i>val</i>. Any subgraph, node, or edge appearing after this inherits the new default attributes. </p>
<p> <code>n0 [</code><i>name0=val0,name1=val1,&#8230;</i><code>];</code><br />
 Creates node <code>n0</code> (if it does not already exist) and sets its attributes according to the optional list. </p>
<p> <code>n0 </code><i>edgeop</i> n1 <i>edgeop</i> <i>&#8230;</i><i>edgeop</i> nn <code>[</code><i>name0=val0,name1=val1,&#8230;</i><code>];</code><br />
 Creates edges between nodes <code>n0</code>, <code>n1</code>, &#8230;, <code>nn</code> and sets their attributes according to the optional list. Creates nodes as necessary. </p>
<p> [<code>subgraph </code><i>name</i>] <code>{ </code><i>statement-list </i><code>}</code><br />
 Creates a subgraph. Subgraphs may be used in place of <code>n0</code>, &#8230;, <code>nn</code> in the above statements to create edges. [<code>subgraph </code><i>name</i>] is optional; if missing, the subgraph is assigned an internal name. </p>
<p> The language accepts both C-style comments /*C&#8230;*/ or //&#8230; </p>
<p> Attribute names and values are ordinary (C-style) strings. The following sections describe attributes that control graph layout. </p>
<p> A more complete description of the language can be found at <a rel="nofollow" href="http://www.graphviz.org/content/dot-language.">http://www.graphviz.org/content/dot-language.</a></p>
<h2>GRAPH, NODE AND EDGE ATTRIBUTES</h2>
<p> Graphviz uses the <i>name</i>=<i>value</i> attributes, attached to graphs, subgraphs, nodes and edges, to tailor the layout and rendering. We list the more prominent attributes below. The complete list is available at <a rel="nofollow" href="http://www.graphviz.org/content/attrs.">http://www.graphviz.org/content/attrs.</a></p>
<h2> Attributes Common to Nodes, Edges, Clusters and Graphs</h2>
<p> <code>href=</code><i>url</i> the default url for image map files; in PostScript files, the base URL for all relative URLs, as recognized by Acrobat Distiller 3.0 and up. </p>
<p> <code>URL=</code><i>url</i> (&#8220;URL&#8221; is a synonym for &#8220;href.&#8221;) </p>
<p> <code>fontcolor=</code><i>colorvalue</i> sets the label text color. </p>
<p> A <i>colorvalue</i> may be &quot;<i>h,s,v</i><code>&quot;</code> (hue, saturation, brightness) floating point numbers between 0 and 1, or an X11 color name such as <code>white, black, red, green, blue, yellow, magenta,</code> or <code>cyan</code>, or a &quot;<i>#rrggbb&quot; (red, green, blue, 2 hex characters each) value. See <a rel="nofollow" href="http://www.graphviz.org/content/attrs#kcolor">http://www.graphviz.org/content/attrs#kcolor</a> and <a rel="nofollow" href="http://www.graphviz.org/content/color-names">http://www.graphviz.org/content/color-names</a> for further details. </p>
<p> </i><code>fontsize=</code><i>n</i> sets the label type size to <i>n</i> points. </p>
<p> <code>fontname=</code><i>name</i> sets the label font family name. </p>
<p> <code>label=</code><i>text</i> where <i>text</i> may include escaped newlines 
, \l, or  for center, left, and right justified lines. The string &#8216;\G&#8217; value will be replaced by the graph name. For node labels, the string &#8216;\N&#8217; value will be replaced by the node name. For edges, if the substring &#8216;\T&#8217; is found in a label, it will be replaced by the name of the tail node; if the substring &#8216;\H&#8217; is found in a label, it will be replaced by the name of the head node; if the substring &#8216;\E&#8217; value is found in a label it will be replaced by: <i>tail_node_name</i>-&gt;<i>head_node_name</i> or by: <i>tail_node_name</i>&#8212;<i>head_node_name</i> for undirected graphs. </p>
<p> Graphviz also supports special HTML-like labels for constructing complex node content. A full-description of these is given at <a rel="nofollow" href="http://www.graphviz.org/content/node-shapes#html.">http://www.graphviz.org/content/node-shapes#html.</a> </p>
<p> If a node has <code>shape=record</code>, the label may contain recursive box lists delimited by { | }. Port identifiers in labels are set off by angle brackets &lt; &gt;. </p>
<h2> Graph Attributes</h2>
<p> <code>size=&quot;</code><i>x,y</i>&quot; specifies the maximum bounding box of drawing in inches. </p>
<p> <code>ratio=</code><i>f</i> sets the aspect ratio to <i>f</i> which may be a floating point number, or one of the keywords <code>fill</code>, <code>compress</code>, or <code>auto</code>. </p>
<p> <code>layout=</code><i>engine</i> indicates the preferred layout engine (<code>dot</code>, <code>neato</code>, <code>fdp</code>, etc.) overriding the default from the basename of the command or the -K commandline option. </p>
<p> <code>margin=</code><i>f</i> sets the page margin (included in the page size). </p>
<p> <code>ordering=out</code> constrains order of out-edges in a subgraph according to their file sequence. </p>
<p> <code>rotate=90</code> sets landscape mode. (<code>orientation=land</code> is backward compatible but obsolete.) </p>
<p> <code>center=</code><i>n</i> a non-zero value centers the drawing on the page. </p>
<p> <code>color=</code><i>colorvalue</i> sets foreground color (<code>bgcolor</code> for background). </p>
<p> <code>overlap=</code><i>mode</i>. This specifies what algorithm should do if any nodes overlap. If mode is <code>false</code>, the program uses the Prism algorithm to adjust the nodes to eliminate overlaps. If mode is <code>scale</code>, the layout is uniformly scaled up, preserving node sizes, until nodes no longer overlap. The latter technique removes overlaps while preserving symmetry and structure, while the former removes overlaps more compactly but destroys symmetries. If mode is <code>true</code> (the default), no repositioning is done. Since the <code>dot</code> algorithm always produces a layout with no node overlaps, this attribute is only useful with other layouts. </p>
<p> <code>stylesheet=</code><i>&quot;file.css&quot;</i> includes a reference to a stylesheet in -Tsvg and -Tsvgz outputs. Ignored by other formats. </p>
<p> <code>splines</code> If set to <code>true</code>, edges are drawn as splines. If set to <code>polyline</code>, edges are drawn as polylines. If set to <code>ortho</code>, edges are drawn as orthogonal polylines. In all of these cases, the nodes must not overlap. If <code>splines=false</code> or <code>splines=line</code>, edges are drawn as line segments. The default is <code>true</code> for dot, and <code>false</code> for all other layouts. </p>
<p> <code>(dot-specific attributes)</code> </p>
<p> <code>nodesep=</code><i>f</i> sets the minimum separation between nodes. </p>
<p> <code>ranksep=</code><i>f</i> sets the minimum separation between ranks. </p>
<p> <code>rankdir=LR|RL|BT</code> requests a left-to-right, right-to-left, or bottom-to-top, drawing. </p>
<p> <code>rank=same</code> (or <code>min</code> or <code>max</code>) in a subgraph constrains the rank assignment of its nodes. If a subgraph&#8217;s name has the prefix <code>cluster</code>, its nodes are drawn in a distinct rectangle of the layout. Clusters may be nested. </p>
<p> <code>(neato-specific attributes)</code><br />
 <code>mode=</code><i>val</i>. Algorithm for minimizing energy in the layout. By default, <code>neato</code> uses stress majorization. If <code>mode=KK</code>, it uses a version of gradient descent. </p>
<p> <code>model=</code><i>val</i>. The <code>neato</code> model computes the desired distances between all pairs of vertices. By default, it uses the length of the shortest path. If <code>model</code> is set to <code>circuit</code>, a circuit-resistance model is used. If <code>model</code> is set to <code>subset</code>, it uses a model whereby the edge length is the number of nodes that are neighbors of exactly one of the edge&#8217;s vertices. </p>
<p> <code>start=</code><i>val</i>. Requests random initial placement and seeds the random number generator. If <i>val</i> is not an integer, the process ID or current time is used as the seed. </p>
<p> <code>epsilon=</code><i>n</i>. Sets the cutoff for the solver. The default is 0.1. </p>
<p> <code>(twopi-specific attributes)</code><br />
 <code>root=</code><i>ctr</i>. This specifies the node to be used as the center of the layout. If not specified, <i>twopi</i> will randomly pick one of the nodes that are furthest from a leaf node, where a leaf node is a node of degree 1. If no leaf nodes exists, an arbitrary node is picked as center. </p>
<p> <code>ranksep=</code><i>val</i>. Specifies the radial distance in inches between the sequence of rings. The default is 0.75. </p>
<p> <code>(circo-specific attributes)</code><br />
 <code>root=</code><i>nodename</i>. Specifies the name of a node occurring in the root block. If the graph is disconnected, the <code>root</code> node attribute can be used to specify additional root blocks. </p>
<p> <code>mindist=</code><i>value</i>. Sets the minimum separation between all nodes. If not specified then <i>circo</i> uses a default value of 1.0. </p>
<p> <code>(fdp-specific attributes)</code><br />
 <code>K=</code><i>val</i>. Sets the default ideal node separation in the layout. </p>
<p> <code>maxiter=</code><i>val</i>. Sets the maximum number of iterations used to layout the graph. </p>
<p> <code>start=</code><i>val</i>. Adjusts the random initial placement of nodes with no specified position. If <i>val</i> is is an integer, it is used as the seed for the random number generator. If <i>val</i> is not an integer, a random system-generated integer, such as the process ID or current time, is used as the seed. </p>
<h2> Node Attributes</h2>
<p> <code>height=</code><i>d</i> or <code>width=</code><i>d</i> sets minimum height or width. Adding <code>fixedsize=true</code> forces these to be the actual size (text labels are ignored). </p>
<p> <code>shape=</code><i>builtin_polygon</i> record epsf<br />
 <i>builtin_polygon</i> can be such values as <code>plaintext, ellipse, oval, circle, egg, triangle, box, diamond, trapezium, parallelogram, house, hexagon, octagon, note, tab, box3d, or component,</code>, among others. (Polygons are defined or modified by the following node attributes: <code>regular</code>, <code>peripheries</code>, <code>sides</code>, <code>orientation</code>, <code>distortion</code> and <code>skew</code>.) <code>epsf</code> uses the node&#8217;s <code>shapefile</code> attribute as the path name of an external EPSF file to be automatically loaded for the node shape. </p>
<p> See <a rel="nofollow" href="http://www.graphviz.org/content/node-shapes">http://www.graphviz.org/content/node-shapes</a> for a complete description of node shapes. </p>
<p> <code>color=</code><i>colorvalue</i> sets the outline color, and the default fill color if style=filled and <code>fillcolor</code> is not specified. </p>
<p> <code>fillcolor=</code><i>colorvalue</i> sets the fill color when style=filled. If not specified, the fillcolor when style=filled defaults to be the same as the outline color. </p>
<p> <code>style=filled solid dashed dotted bold invis</code> </p>
<p> <code>xlabel=</code><i>&quot;text&quot;</i> specifies a label that will be place near, but outside, of a node. The normal <code>label</code> string is placed within the node shape. </p>
<p> <code>target=</code><i>&quot;target&quot;</i> is a target string for client-side imagemaps and SVG, effective when nodes have a URL. The target string is used to determine which window of the browser is used for the URL. Setting it to &quot;_graphviz&quot; will open a new window if it doesn&#8217;t already exist, or reuse it if it does. If the target string is empty, the default, then no target attribute is included in the output. The substrings &#8216;\N&#8217; and &#8216;\G&#8217; are substituted in the same manner as for the node label attribute. Additionally the substring &#8216;\L&#8217; is substituted with the node label string. </p>
<p> <code>tooltip=</code><i>&quot;text&quot;</i> is a tooltip string for client-side imagemaps and SVG, effective when nodes have a URL. The tooltip string defaults to be the same as the label string, but this attribute permits nodes without labels to still have tooltips thus permitting denser graphs. The substrings &#8216;\N&#8217; and &#8216;\G&#8217; are substituted in the same manner as for the node label attribute. Additionally the substring &#8216;\L&#8217; is substituted with the node label string. </p>
<p> The following attributes apply only to polygon shape nodes: </p>
<p> <code>regular=</code><i>n</i> if <i>n</i> is non-zero then the polygon is made regular, i.e. symmetric about the x and y axis, otherwise the polygon takes on the aspect ratio of the label. <i>builtin_polygons</i> that are not already regular are made regular by this attribute. <i>builtin_polygons</i> that are already regular are not affected (i.e. they cannot be made asymmetric). </p>
<p> <code>peripheries=</code><i>n</i> sets the number of periphery lines drawn around the polygon. This value supersedes the number of periphery lines of <i>builtin_polygons</i>. </p>
<p> <code>sides=</code><i>n</i> sets the number of sides to the polygon. <i>n</i>&lt;3 results in an ellipse. This attribute is ignored by <i>builtin_polygons</i>. </p>
<p> <code>orientation=</code><i>f</i> sets the orientation of the first apex of the polygon counterclockwise from the vertical, in degrees. <i>f</i> may be a floating point number. The orientation of labels is not affected by this attribute. This attribute is added to the initial orientation of <i>builtin_polygons.</i> </p>
<p> <code>distortion=</code><i>f</i> sets the amount of broadening of the top and narrowing of the bottom of the polygon (relative to its orientation). Floating point values between -1 and +1 are suggested. This attribute is ignored by <i>builtin_polygons</i>. </p>
<p> <code>skew=</code><i>f</i> sets the amount of right-displacement of the top and left-displacement of the bottom of the polygon (relative to its orientation). Floating point values between -1 and +1 are suggested. This attribute is ignored by <i>builtin_polygons</i>. </p>
<p> <code>(circo-specific attributes)</code><br />
 <code>root=</code><i>true/false</i>. This specifies that the block containing the given node be treated as the root of the spanning tree in the layout. </p>
<p> <code>(neato- and fdp-specific attributes)</code><br />
 <code>pin=</code><i>val</i>. If <i>val</i> is <code>true</code>, the node will remain at its initial position. </p>
<h2> Edge Attributes</h2>
<p> <code>weight=</code><i>val</i> where <i>val</i> is the cost of the edge. For <code>dot</code>, weights must be non-negative integers. Values greater than 1 tend to shorten the edge; weight 0 flat edges are ignored for ordering nodes. In <code>twopi</code>, a weight of 0 will cause the edge to be ignored in constructing the underlying spanning tree. For <code>neato</code> and <code>fdp</code>, a heavier weight will put more emphasis on the algorithm achieving an edge length closer to that specified by the edge&#8217;s <code>len</code> attribute. </p>
<p> <code>style=solid dashed dotted bold invis</code> </p>
<p> <code>color=</code><i>colorvalue</i> sets the line color for edges. </p>
<p> <code>color=</code><i>colorvaluelist</i> a &#8216;:&#8217; separated list of <i>colorvalue</i> creates parallel edges, one edge for each color. </p>
<p> <code>dir=forward back both none</code> controls arrow direction. </p>
<p> <code>tailclip,headclip=false</code> disables endpoint shape clipping. </p>
<p> <code>target=</code><i>&quot;text&quot;</i> is a target string for client-side imagemaps and SVG, effective when edges have a URL. If the target string is empty, the default, then no target attribute is included in the output. The substrings &#8216;\T&#8217;, &#8216;\H&#8217;, &#8216;\E&#8217; and &#8216;\G&#8217; are substituted in the same manner as for the edge label attribute. Additionally the substring &#8216;\L&#8217; is substituted with the edge label string. </p>
<p> <code>tooltip=</code><i>&quot;text&quot;</i> is a tooltip string for client-side imagemaps effective when edges have a URL. The tooltip string defaults to be the same as the edge label string. The substrings &#8216;\T&#8217;, &#8216;\H&#8217;, &#8216;\E&#8217; and &#8216;\G&#8217; are substituted in the same manner as for the edge label attribute. Additionally the substring &#8216;\L&#8217; is substituted with the edge label string. </p>
<p> <code>arrowhead,arrowtail=none, normal, inv, dot, odot, invdot, invodot, tee, empty, invempty, open, halfopen, diamond, odiamond, box, obox, crow</code>. Specifies the shape of the glyph occurring where the edge touches the head or tail node, respectively. Note that this only specifies the shape. The <code>dir</code> attribute determines whether or not the glyph is drawn. </p>
<p> <code>arrowsize=</code><i>val</i> specifies a multiplicative scale factor for the size of the arrowhead. inv_length=6,inv_width=7,dot_radius=2) </p>
<p> <code>headlabel,taillabel=</code><i>text</i> for labels appearing near the head and tail nodes of an edge. <code>labelfontcolor</code>, <code>labelfontname</code>, <code>labelfontsize</code> for head and tail labels. The substrings &#8216;\T&#8217;, &#8216;\H&#8217;, &#8216;\E&#8217; and &#8216;\G&#8217; are substituted in the same manner as for the edge label attribute. Additionally the substring &#8216;\L&#8217; is substituted with the edge label string. </p>
<p> <code>headhref=</code><i>&quot;url&quot;</i> sets the url for the head port in imagemap, PostScript and SVG files. The substrings &#8216;\T&#8217;, &#8216;\H&#8217;, &#8216;\E&#8217; and &#8216;\G&#8217; are substituted in the same manner as for the edge label attribute. Additionally the substring &#8216;\L&#8217; is substituted with the edge label string. </p>
<p> <code>headURL=</code><i>&quot;url&quot;</i> (<code>headURL</code> is a synonym for <code>headhref</code>.) </p>
<p> <code>headtarget=</code><i>&quot;headtarget&quot;</i> is a target string for client-side imagemaps and SVG, effective when edge heads have a URL. The headtarget string is used to determine which window of the browser is used for the URL. If the headtarget string is empty, the default, then headtarget defaults to the same value as target for the edge. The substrings &#8216;\T&#8217;, &#8216;\H&#8217;, &#8216;\E&#8217; and &#8216;\G&#8217; are substituted in the same manner as for the edge label attribute. Additionally the substring &#8216;\L&#8217; is substituted with the edge label string. </p>
<p> <code>headtooltip=</code><i>&quot;tooltip&quot;</i> is a tooltip string for client-side imagemaps effective when head ports have a URL. The tooltip string defaults to be the same as the headlabel string. The substrings &#8216;\T&#8217;, &#8216;\H&#8217;, and &#8216;\E&#8217; are substituted in the same manner as for the edge label attribute. Additionally the substring &#8216;\L&#8217; is substituted with the edge label string. </p>
<p> <code>tailhref=</code><i>&quot;url&quot;</i> sets the url for the tail port in imagemap, PostScript and SVG files. The substrings &#8216;\T&#8217;, &#8216;\H&#8217;, &#8216;\E&#8217; and &#8216;\G&#8217; are substituted in the same manner as for the edge label attribute. Additionally the substring &#8216;\L&#8217; is substituted with the edge label string. </p>
<p> <code>tailURL=</code><i>&quot;url&quot;</i> (<code>tailURL</code> is a synonym for <code>tailhref</code>.) </p>
<p> <code>tailtarget=</code><i>&quot;tailtarget&quot;</i> is a target string for client-side imagemaps and SVG, effective when edge tails have a URL. The tailtarget string is used to determine which window of the browser is used for the URL. If the tailtarget string is empty, the default, then tailtarget defaults to the same value as target for the edge. The substrings &#8216;\T&#8217;, &#8216;\H&#8217;, &#8216;\E&#8217; and &#8216;\G&#8217; are substituted in the same manner as for the edge label attribute. Additionally the substring &#8216;\L&#8217; is substituted with the edge label string. </p>
<p> <code>tailtooltip=</code><i>&quot;tooltip&quot;</i> is a tooltip string for client-side imagemaps effective when tail ports have a URL. The tooltip string defaults to be the same as the taillabel string. The substrings &#8216;\T&#8217;, &#8216;\H&#8217;, &#8216;\E&#8217; and &#8216;\G&#8217; are substituted in the same manner as for the edge label attribute. Additionally the substring &#8216;\L&#8217; is substituted with the edge label string. </p>
<p> <code>labeldistance</code> and <code>labelangle</code> (in degrees CCW) specify the placement of head and tail labels. </p>
<p> <code>decorate</code> draws line from edge to label. </p>
<p> <code>samehead,sametail</code> aim edges having the same value to the same port, using the average landing point. </p>
<p> <code>(dot-specific attributes)</code><br />
 <code>constraint=false</code> causes an edge to be ignored for rank assignment. </p>
<p> <code>minlen=</code><i>n</i> where <i>n</i> is an integer factor that applies to the edge length (ranks for normal edges, or minimum node separation for flat edges). </p>
<p> <code>xlabel=</code><i>&quot;text&quot;</i> Edge labels in <code>dot</code> are treated as special types of nodes, with space allocated for them during node layout. This can sometimes deform the edge routing. If an <code>xlabel</code> is used instead, the label is placed after all nodes and edges have been positioned. In turn, this may mean that there is some overlap among the labels. </p>
<p> <code>(neato and fdp-specific attributes)</code><br />
 <code>len=</code><i>f</i> sets the optimal length of an edge. The default is 1.0. </p>
<h2>COMMAND-LINE OPTIONS</h2>
<p> <code>-G</code> sets a default graph attribute.<br />
 <code>-N</code> sets a default node attribute.<br />
 <code>-E</code> sets a default edge attribute. Example: <code>-Gsize=&quot;7,8&quot; -Nshape=box -Efontsize=8</code> </p>
<p> <code>-l</code><i>file</i> loads custom PostScript library files. Usually these define custom shapes or styles. If <code>-l</code> is given by itself, the standard library is omitted. </p>
<p> <code>-T</code><i>lang</i> sets the output language as described above. </p>
<p> <code>-n</code>[<code>1</code>|<code>2</code>] (no-op) If set, neato assumes nodes have already been positioned and all nodes have a pos attribute giving the positions. It then performs an optional adjustment to remove node-node overlap, depending on the value of the overlap attribute, computes the edge layouts, depending on the value of the <code>splines</code> attribute, and emits the graph in the appropriate format. If num is supplied, the following actions occur: </p>
<pre>
    num = 1
</pre>
<p> Equivalent to -n. </p>
<pre>
    num &gt; 1
</pre>
<p> Use node positions as specified, with no adjustment to remove node-node overlaps, and use any edge layouts already specified by the pos attribute. neato computes an edge layout for any edge that does not have a <code>pos</code> attribute. As usual, edge layout is guided by the <code>splines</code> attribute. </p>
<p> <code>-K</code><i>layout</i> override the default layout engine implied by the command name. </p>
<p> <code>-O</code> automatically generate output filenames based on the input filename and the -T format. </p>
<p> <code>-P</code> generate a graph of the currently available plugins. </p>
<p> <code>-v</code> (verbose) prints various information useful for debugging. </p>
<p> <code>-c</code> configure plugins. </p>
<p> <code>-m</code> memory test (observe no growth with top, kill when done). </p>
<p> <code>-q</code><i>level</i> set level of message suppression. The default is 1. </p>
<p> <code>-s</code><i>fscale</i> scale input by <i>fscale</i>, the default is 72. </p>
<p> <code>-y</code> invert y coordinate in output. </p>
<p> <code>-V</code> (version) prints version information and exits. </p>
<p> <code>-?</code> prints the usage and exits. </p>
<p> A complete description of the available command-line options can be found at <a rel="nofollow" href="https://www.graphviz.org/doc/info/command.html.">https://www.graphviz.org/doc/info/command.html.</a></p>
<h2>EXAMPLES</h2>
<pre><code>
digraph test123
{
    a-&gt;b-&gt;c;
    a-&gt;{x y};
    b[shape = box];
    c[label = "hello
world", color = blue, fontsize = 24,
      fontname = "Palatino-Italic", fontcolor = red, style = filled];
    a-&gt;z[label = "hi", weight = 100];
    x-&gt;z[label = "multi-line
label"];
    edge[style = dashed, color = red];
    b-&gt;x;
    {
        rank = same;
        b x
    }
}
</code></pre>
<pre><code>
graph test123
{
    a-- b-- c;
    a-- {x y};
    x-- c[w = 10.0];
    x-- y[w = 5.0, len = 3];
}
</code></pre>
<h2>CAVEATS</h2>
<p> Edge splines can overlap unintentionally. </p>
<p> Flat edge labels are slightly broken. Intercluster edge labels are totally broken. </p>
<p> Because unconstrained optimization is employed, node boxes can possibly overlap or touch unrelated edges. All existing spring embedders seem to have this limitation. </p>
<p> Apparently reasonable attempts to pin nodes or adjust edge lengths and weights can cause instability.</p>
<h2>AUTHORS</h2>
<p> Stephen C. North &lt;north [at] research.att.com&gt;<br />
 Emden R. Gansner &lt;erg [at] graphviz.org&gt;<br />
 John C. Ellson &lt;ellson [at] research.att.com&gt;<br />
 Yifan Hu &lt;yifanhu [at] yahoo.com&gt; </p>
<p> The bitmap driver (PNG, GIF etc) is by Thomas Boutell, &lt;<a rel="nofollow" href="http://www.boutell.com/gd">http://www.boutell.com/gd</a>&gt; </p>
<p> The Truetype font renderer is from the Freetype Project (David Turner, Robert Wilhelm, and Werner Lemberg) (who can be contacted at freetype-devel [at] lists.lrz-muenchen.de).</p>
<h2>SEE ALSO</h2>
<p> This man page contains only a small amount of the information related to the Graphviz layout programs. The most complete information can be found at <a rel="nofollow" href="http://www.graphviz.org/Documentation.php,">http://www.graphviz.org/Documentation.php,</a> especially in the on-line reference pages. Most of these documents are also available in the <i>doc</i> and <i>doc/info</i> subtrees in the source and binary distributions. </p>
<p> <code><a href="/docs/linux/man/1-dotty/">dotty</a></code>(1),<code><a href="/docs/linux/man/n-tcldot/">tcldot</a></code>(n),<code><a href="/docs/linux/man/1-xcolors/">xcolors</a></code>(1),<code><a href="/docs/linux/man/3-libgraph/">libgraph</a></code>(3). </p>
<p> E. R. Gansner, S. C. North, K. P. Vo, &quot;DAG &#8211; A Program to Draw Directed Graphs&quot;, Software &#8211; Practice and Experience <a href="/docs/linux/man/1-17/">17</a>(1), 1988, pp. 1047-1062.<br />
 E. R. Gansner, E. Koutsofios, S. C. North, K. P. Vo, &quot;A Technique for Drawing Directed Graphs,&quot; IEEE Trans. on Soft. Eng. <a href="/docs/linux/man/3-19/">19</a>(3), 1993, pp. 214-230.<br />
 S. North and E. Koutsofios, &quot;Applications of graph visualization&quot;, Graphics Interface 94, pp. 234-245.<br />
 E. R. Gansner and E. Koutsofios and S. C. North, &quot;Drawing Graphs with dot,&quot; Available at <a rel="nofollow" href="http://www.graphviz.org/pdf/dotguide.pdf.">http://www.graphviz.org/pdf/dotguide.pdf.</a><br />
 S. C. North, &quot;NEATO User&#8217;s Manual&quot;. Available <a rel="nofollow" href="http://www.graphviz.org/pdf/neatoguide.pdf.">http://www.graphviz.org/pdf/neatoguide.pdf.</a><br />
 E. R. Gansner and Y. Hu, &quot;Efficient, Proximity-Preserving Node Overlap Removal&quot;, J. Graph Algorithms Appl., <a href="/docs/linux/man/1-14/">14</a>(1) pp. 53-74, 2010. </p>
<h2>Index</h2>
