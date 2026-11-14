---
title: "patchwork(1)"
name: "patchwork"
section: "1"
letter: "p"
url: "/docs/linux/man/1-patchwork/"
description: "patchwork – filter for drawing clustered graphs as treemaps"
---

<h2 class="name">NAME</h2>
<p> patchwork &#8211; filter for drawing clustered graphs as treemaps </p>
<h2>SYNOPSIS</h2>
<p> <code>patchwork</code> [<code>&#8211;</code>(<code>G</code>|<code>N</code>|<code>E</code>)<i>name=value</i>] [<code>-T</code><i>lang</i>] [<code>-l</code><i>libfile</i>] [<code>-o</code><i>outfile</i>] [<code>-O</code>] [<code>-P</code>] [<code>-v</code>] [<code>-V</code>] [files]</p>
<h2>DESCRIPTION</h2>
<p> <i>patchwork</i> draws clustered graphs using a squarified treemap layout. As input, it takes any graph in the <i>dot</i> format. Each cluster is given an area based on the areas specified by the clusters and nodes it contains. The areas of nodes and empty clusters can be specified by the <code>area</code> attribute. The default value is 1. </p>
<p> The root graph is laid out as a square. Then, recursively, the region of a cluster or graph is partitioned among its top-level nodes and clusters, with each given a roughly square subregion with its specified area.</p>
<h2>OUTPUT FORMATS</h2>
<p> Patchwork uses an extensible plugin mechanism for its output renderers, so to see what output formats your installation of patchwork supports you can use &#8220;patchwork -Txxx&#8221; (where xxx is an unlikely format) and check the warning message. Also, The plugin mechanism supports multiple implementations of the output formats. To see what variants are available, use, for example: &#8220;patchwork -Tpng:&#8221; and to force a particular variant, use, for example: &#8220;patchwork -Tpng:gd&#8221; </p>
<p> Traditionally, patchwork supports the following: <code>-Tps</code> (PostScript), <code>-Tsvg</code> <code>-Tsvgz</code> (Structured Vector Graphics), <code>-Tfig</code> (XFIG graphics), <code>-Tmif</code> (FrameMaker graphics), <code>-Thpgl</code> (HP pen plotters), and <code>-Tpcl</code> (Laserjet printers), <code>-Tpng</code> <code>-Tgif</code> (bitmap graphics), <code>-Tdia</code> (GTK+ based diagrams), <code>-Timap</code> (imagemap files for httpd servers for each node or edge that has a non-null &quot;href&quot; attribute.), <code>-Tcmapx</code> (client-side imagemap for use in html and xhtml). Additional less common or more special-purpose output formats can be found at <a rel="nofollow" href="http://www.graphviz.org/doc/info/output.html.)">http://www.graphviz.org/doc/info/output.html.)</a> </p>
<p> Alternative plugins providing support for a given output format can be found from the error message resulting from appending a &#8216;:&#8217; to the format. e.g. <code>-Tpng:</code> The first plugin listed is always the default.</p>
<h2>GRAPH FILE LANGUAGE</h2>
<p> Here is a synopsis of the graph file language, normally using the extension <code>.gv</code>, for graphs: </p>
<p> [<code>strict</code>] (<code>graph</code>|<code>digraph</code>) <i>name</i> { <i>statement-list</i> }<br />
 Is the top level graph. If the graph is <code>strict</code> then multiple edges are not allowed between the same pairs of nodes. If it is a directed graph, indicated by <code>digraph</code>, then the <i>edgeop</i> must be &quot;-&gt;&quot;. If it is an undirected <code>graph</code> then the <i>edgeop</i> must be &quot;&#8211;&quot;. Statements may be: </p>
<p> <i>name</i><code>=</code><i>val</i><code>;</code><br />
 <code>node [</code><i>name</i><code>=</code><i>val</i><code>];</code><br />
 <code>edge [</code><i>name</i><code>=</code><i>val</i><code>];</code><br />
 Set default graph, node, or edge attribute <i>name</i> to <i>val</i>. Any subgraph, node, or edge appearing after this inherits the new default attributes. </p>
<p> <code>n0 [</code><i>name0=val0,name1=val1,&#8230;</i><code>];</code> Creates node <code>n0</code> (if it does not already exist) and sets its attributes according to the optional list. </p>
<p> <code>n0 </code><i>edgeop</i> n1 <i>edgeop</i> <i>&#8230;</i><i>edgeop</i> nn [<i>name0=val0,name1=val1,&#8230;</i><code>];</code><br />
 Creates edges between nodes <code>n0</code>, <code>n1</code>, &#8230;, <code>nn</code> and sets their attributes according to the optional list. Creates nodes as necessary. </p>
<p> [<code>subgraph </code><i>name</i><code>] { </code><i>statement-list </i><code>}</code><br />
 Creates a subgraph. Subgraphs may be used in place of <code>n0</code>, &#8230;, <code>nn</code> in the above statements to create edges. [<code>subgraph </code><i>name</i>] is optional; if missing, the subgraph is assigned an internal name. </p>
<p> Comments may be /*C-like*/ or //C++-like. </p>
<p> Attribute names and values are ordinary (C-style) strings. The following sections describe attributes that control graph layout. </p>
<h2>GRAPH ATTRIBUTES</h2>
<p> <code>size=&quot;</code><i>x,y</i>&quot; sets bounding box of drawing in inches. </p>
<p> <code>page=&quot;</code><i>x,y</i>&quot; sets the PostScript pagination unit. </p>
<p> <code>ratio=</code><i>f</i> sets the aspect ratio to <i>f</i> which may be a floating point number, or one of the keywords <code>fill</code>, <code>compress</code>, or <code>auto</code>. </p>
<p> <code>pagedir=</code>[TBLR][TBLR] sets the major and minor order of pagination. </p>
<p> <code>rotate=90</code> sets landscape mode. (<code>orientation=land</code> is backward compatible but obsolete.) </p>
<p> <code>center=</code><i>n</i> a non-zero value centers the drawing on the page. </p>
<p> <code>layers=&quot;</code><i>id:id:id:id</i>&quot; is a sequence of layer identifiers for overlay diagrams. The PostScript array variable <i>layercolorseq</i> sets the assignment of colors to layers. The least index is 1 and each element must be a 3-element array to be interpreted as a color coordinate. </p>
<p> <code>color=</code><i>colorvalue</i> sets foreground color (<code>bgcolor</code> for background). </p>
<p> <code>href=</code><i>&quot;url&quot;</i> the default url for image map files; in PostScript files, the base URL for all relative URLs, as recognized by Acrobat Distiller 3.0 and up. </p>
<p> <code>URL=</code><i>&quot;url&quot;</i> (&quot;URL&quot; is a synonym for &quot;href&quot;.) </p>
<p> <code>stylesheet=</code><i>&quot;file.css&quot;</i> includes a reference to a stylesheet in -Tsvg and -Tsvgz outputs. Ignored by other formats. </p>
<p> <code>splines</code>. If set to <i>true</i>, edges are drawn as splines. If set to <i>polyline</i>, edges are drawn as polylines. If set to <i>ortho</i>, edges are drawn as orthogonal polylines. In all of these cases, the nodes may not overlap. If <code>splines=</code><i>false</i> or <code>splines=</code><i>line</i>, edges are drawn as line segments. The default is <i>false</i>. </p>
<h2>NODE ATTRIBUTES</h2>
<p> <code>height=</code><i>d</i> or <code>width=</code><i>d</i> sets minimum height or width. Adding <code>fixedsize=true</code> forces these to be the actual size (text labels are ignored). </p>
<p> <code>shape=record polygon epsf </code><i>builtin_polygon</i><br />
 <i>builtin_polygon</i> is one of: <code>plaintext ellipse oval circle egg triangle box diamond trapezium parallelogram house hexagon octagon note tab box3d component.</code> (Polygons are defined or modified by the following node attributes: <code>regular</code>, <code>peripheries</code>, <code>sides</code>, <code>orientation</code>, <code>distortion</code> and <code>skew</code>.) <code>epsf</code> uses the node&#8217;s <code>shapefile</code> attribute as the path name of an external EPSF file to be automatically loaded for the node shape. </p>
<p> <code>label=</code><i>text</i> where <i>text</i> may include escaped newlines 
, \l, or  for center, left, and right justified lines. The string &#8216;\N&#8217; value will be replaced by the node name. The string &#8216;\G&#8217; value will be replaced by the graph name. Record labels may contain recursive box lists delimited by { | }. Port identifiers in labels are set off by angle brackets &lt; &gt;. In the graph file, use colon (such as, <code>node0:port28</code>). </p>
<p> <code>fontsize=</code><i>n</i> sets the label type size to <i>n</i> points. </p>
<p> <code>fontname=</code><i>name</i> sets the label font family name. </p>
<p> <code>color=</code><i>colorvalue</i> sets the outline color, and the default fill color if style=filled and <code>fillcolor</code> is not specified. </p>
<p> <code>fillcolor=</code><i>colorvalue</i> sets the fill color when style=filled. If not specified, the fillcolor when style=filled defaults to be the same as the outline color. </p>
<p> <code>fontcolor=</code><i>colorvalue</i> sets the label text color. </p>
<p> A <i>colorvalue</i> may be &quot;<i>h,s,v</i><code>&quot;</code> (hue, saturation, brightness) floating point numbers between 0 and 1, or an X11 color name such as <code>white black red green blue yellow magenta cyan</code> or <code>burlywood</code>, or a &quot;<i>#rrggbb&quot; (red, green, blue, 2 hex characters each) value. </p>
<p> </i><code>style=filled solid dashed dotted bold invis</code> or any Postscript code. </p>
<p> <code>layer=</code><i>id</i> or <i>id:id</i> or &quot;all&quot; sets the node&#8217;s active layers. The empty string means no layers (invisible). </p>
<p> The following attributes apply only to polygon shape nodes: </p>
<p> <code>regular=</code><i>n</i> if <i>n</i> is non-zero then the polygon is made regular, i.e. symmetric about the x and y axis, otherwise the polygon takes on the aspect ratio of the label. <i>builtin_polygons</i> that are not already regular are made regular by this attribute. <i>builtin_polygons</i> that are already regular are not affected (i.e. they cannot be made asymmetric). </p>
<p> <code>peripheries=</code><i>n</i> sets the number of periphery lines drawn around the polygon. This value supersedes the number of periphery lines of <i>builtin_polygons</i>. </p>
<p> <code>sides=</code><i>n</i> sets the number of sides to the polygon. <i>n</i>&lt;3 results in an ellipse. This attribute is ignored by <i>builtin_polygons</i>. </p>
<p> <code>orientation=</code><i>f</i> sets the orientation of the first apex of the polygon counterclockwise from the vertical, in degrees. <i>f</i> may be a floating point number. The orientation of labels is not affected by this attribute. This attribute is added to the initial orientation of <i>builtin_polygons.</i> </p>
<p> <code>distortion=</code><i>f</i> sets the amount of broadening of the top and narrowing of the bottom of the polygon (relative to its orientation). Floating point values between -1 and +1 are suggested. This attribute is ignored by <i>builtin_polygons</i>. </p>
<p> <code>skew=</code><i>f</i> sets the amount of right-displacement of the top and left-displacement of the bottom of the polygon (relative to its orientation). Floating point values between -1 and +1 are suggested. This attribute is ignored by <i>builtin_polygons</i>. </p>
<p> <code>href=</code><i>&quot;url&quot;</i> sets the url for the node in imagemap, PostScript and SVG files. The substrings &#8216;\N&#8217; and &#8216;\G&#8217; are substituted in the same manner as for the node label attribute. Additionally the substring &#8216;\L&#8217; is substituted with the node label string. </p>
<p> <code>URL=</code><i>&quot;url&quot;</i> (&quot;URL&quot; is a synonym for &quot;href&quot;.) </p>
<p> <code>target=</code><i>&quot;target&quot;</i> is a target string for client-side imagemaps and SVG, effective when nodes have a URL. The target string is used to determine which window of the browser is used for the URL. Setting it to &quot;_graphviz&quot; will open a new window if it doesn&#8217;t already exist, or reuse it if it does. If the target string is empty, the default, then no target attribute is included in the output. The substrings &#8216;\N&#8217; and &#8216;\G&#8217; are substituted in the same manner as for the node label attribute. Additionally the substring &#8216;\L&#8217; is substituted with the node label string. </p>
<p> <code>tooltip=</code><i>&quot;tooltip&quot;</i> is a tooltip string for client-side imagemaps and SVG, effective when nodes have a URL. The tooltip string defaults to be the same as the label string, but this attribute permits nodes without labels to still have tooltips thus permitting denser graphs. The substrings &#8216;\N&#8217; and &#8216;\G&#8217; are substituted in the same manner as for the node label attribute. Additionally the substring &#8216;\L&#8217; is substituted with the node label string. </p>
<h2>EDGE ATTRIBUTES</h2>
<p> <code>label=</code><i>text</i> where <i>text</i> may include escaped newlines 
, \l, or  for centered, left, or right justified lines. If the substring &#8216;\T&#8217; is found in a label it will be replaced by the tail_node name. If the substring &#8216;\H&#8217; is found in a label it will be replaced by the head_node name. If the substring &#8216;\E&#8217; value is found in a label it will be replaced by: tail_node_name-&gt;head_node_name If the substring &#8216;\G&#8217; is found in a label it will be replaced by the graph name. or by: tail_node_name&#8211;head_node_name for undirected graphs. </p>
<p> <code>fontsize=</code><i>n</i> sets the label type size to <i>n</i> points. </p>
<p> <code>fontname=</code><i>name</i> sets the label font family name. </p>
<p> <code>fontcolor=</code><i>colorvalue</i> sets the label text color. </p>
<p> <code>style=solid dashed dotted bold invis</code> </p>
<p> <code>color=</code><i>colorvalue</i> sets the line color for edges. </p>
<p> <code>color=</code><i>colorvaluelist</i> a &#8216;:&#8217; separated list of <i>colorvalue</i> creates parallel edges, one edge for each color. </p>
<p> <code>dir=forward back both none</code> controls arrow direction. </p>
<p> <code>tailclip,headclip=false</code> disables endpoint shape clipping. </p>
<p> <code>href=</code><i>&quot;url&quot;</i> sets the url for the node in imagemap, PostScript and SVG files. The substrings &#8216;\T&#8217;, &#8216;\H&#8217;, &#8216;\E&#8217; and &#8216;\G&#8217; are substituted in the same manner as for the edge label attribute. Additionally the substring &#8216;\L&#8217; is substituted with the edge label string. </p>
<p> <code>URL=</code><i>&quot;url&quot;</i> (&quot;URL&quot; is a synonym for &quot;href&quot;.) </p>
<p> <code>target=</code><i>&quot;target&quot;</i> is a target string for client-side imagemaps and SVG, effective when edges have a URL. If the target string is empty, the default, then no target attribute is included in the output. The substrings &#8216;\T&#8217;, &#8216;\H&#8217;, &#8216;\E&#8217; and &#8216;\G&#8217; are substituted in the same manner as for the edge label attribute. Additionally the substring &#8216;\L&#8217; is substituted with the edge label string. </p>
<p> <code>tooltip=</code><i>&quot;tooltip&quot;</i> is a tooltip string for client-side imagemaps effective when edges have a URL. The tooltip string defaults to be the same as the edge label string. The substrings &#8216;\T&#8217;, &#8216;\H&#8217;, &#8216;\E&#8217; and &#8216;\G&#8217; are substituted in the same manner as for the edge label attribute. Additionally the substring &#8216;\L&#8217; is substituted with the edge label string. </p>
<p> <code>arrowhead,arrowtail=none, normal, inv, dot, odot, invdot, invodot, tee, empty, invempty, open, halfopen, diamond, odiamond, box, obox, crow</code>. </p>
<p> <code>arrowsize</code> (norm_length=10,norm_width=5, inv_length=6,inv_width=7,dot_radius=2) </p>
<p> <code>headlabel,taillabel=string</code> for port labels. <code>labelfontcolor</code>,<code>labelfontname</code>,<code>labelfontsize</code> for head and tail labels. The substrings &#8216;\T&#8217;, &#8216;\H&#8217;, &#8216;\E&#8217; and &#8216;\G&#8217; are substituted in the same manner as for the edge label attribute. Additionally the substring &#8216;\L&#8217; is substituted with the edge label string. </p>
<p> <code>headhref=</code><i>&quot;url&quot;</i> sets the url for the head port in imagemap, PostScript and SVG files. The substrings &#8216;\T&#8217;, &#8216;\H&#8217;, &#8216;\E&#8217; and &#8216;\G&#8217; are substituted in the same manner as for the edge label attribute. Additionally the substring &#8216;\L&#8217; is substituted with the edge label string. </p>
<p> <code>headURL=</code><i>&quot;url&quot;</i> (&quot;headURL&quot; is a synonym for &quot;headhref&quot;.) </p>
<p> <code>headtarget=</code><i>&quot;headtarget&quot;</i> is a target string for client-side imagemaps and SVG, effective when edge heads have a URL. The headtarget string is used to determine which window of the browser is used for the URL. If the headtarget string is empty, the default, then headtarget defaults to the same value as target for the edge. The substrings &#8216;\T&#8217;, &#8216;\H&#8217;, &#8216;\E&#8217; and &#8216;\G&#8217; are substituted in the same manner as for the edge label attribute. Additionally the substring &#8216;\L&#8217; is substituted with the edge label string. </p>
<p> <code>headtooltip=</code><i>&quot;tooltip&quot;</i> is a tooltip string for client-side imagemaps effective when head ports have a URL. The tooltip string defaults to be the same as the headlabel string. The substrings &#8216;\T&#8217;, &#8216;\H&#8217;, and &#8216;\E&#8217; are substituted in the same manner as for the edge label attribute. Additionally the substring &#8216;\L&#8217; is substituted with the edge label string. </p>
<p> <code>tailhref=</code><i>&quot;url&quot;</i> sets the url for the tail port in imagemap, PostScript and SVG files. The substrings &#8216;\T&#8217;, &#8216;\H&#8217;, &#8216;\E&#8217; and &#8216;\G&#8217; are substituted in the same manner as for the edge label attribute. Additionally the substring &#8216;\L&#8217; is substituted with the edge label string. </p>
<p> <code>tailURL=</code><i>&quot;url&quot;</i> (&quot;tailURL&quot; is a synonym for &quot;tailhref&quot;.) </p>
<p> <code>tailtarget=</code><i>&quot;tailtarget&quot;</i> is a target string for client-side imagemaps and SVG, effective when edge tails have a URL. The tailtarget string is used to determine which window of the browser is used for the URL. If the tailtarget string is empty, the default, then tailtarget defaults to the same value as target for the edge. The substrings &#8216;\T&#8217;, &#8216;\H&#8217;, &#8216;\E&#8217; and &#8216;\G&#8217; are substituted in the same manner as for the edge label attribute. Additionally the substring &#8216;\L&#8217; is substituted with the edge label string. </p>
<p> <code>tailtooltip=</code><i>&quot;tooltip&quot;</i> is a tooltip string for client-side imagemaps effective when tail ports have a URL. The tooltip string defaults to be the same as the taillabel string. The substrings &#8216;\T&#8217;, &#8216;\H&#8217;, &#8216;\E&#8217; and &#8216;\G&#8217; are substituted in the same manner as for the edge label attribute. Additionally the substring &#8216;\L&#8217; is substituted with the edge label string. </p>
<p> <code>labeldistance</code> and port_label_distance set distance; also <code>labelangle</code> (in degrees CCW) </p>
<p> <code>decorate</code> draws line from edge to label. </p>
<p> <code>samehead,sametail</code> aim edges having the same value to the same port, using the average landing point. </p>
<p> <code>layer=</code><i>id</i> or <i>id:id</i> or &quot;all&quot; sets the edge&#8217;s active layers. The empty string means no layers (invisible). </p>
<p> <code>(neato-specific attributes)</code><br />
 <code>w=</code><i>f</i> sets the weight (spring constant) of an edge to the given floating point value. The default is 1.0; greater values make the edge tend more toward its optimal length. </p>
<p> <code>len=</code><i>f</i> sets the optimal length of an edge. The default is 1.0.</p>
<h2>COMMAND LINE OPTIONS</h2>
<p> <code>-G</code> sets a default graph attribute.<br />
 <code>-N</code> sets a default node attribute.<br />
 <code>-E</code> sets a default edge attribute. Example: <code>-Gsize=&quot;7,8&quot; -Nshape=box -Efontsize=8</code> </p>
<p> <code>-l</code><i>file</i> loads custom PostScript library files. Usually these define custom shapes or styles. If <code>-l</code> is given by itself, the standard library is omitted. </p>
<p> <code>-T</code><i>lang</i> sets the output language as described above. </p>
<p> <code>-O</code> automatically generate output filenames based on the input filename and the -T format. </p>
<p> <code>-v</code> (verbose) prints various information useful for debugging. </p>
<p> <code>-V</code> (version) prints version information and exits. </p>
<p> <code>-?</code> prints the usage and exits.</p>
<h2>EXAMPLES</h2>
<pre><code>
graph G
{
    node[style = filled] subgraph cluster0{
        subgraph cluster0_0{
            style = filled
                fillcolor = green
                    a b[area = 3 fillcolor = yellow]} subgraph cluster0_1{
            area = 2 bgcolor = yellow} c[style = filled
                                             fillcolor = red]} subgraph cluster1
    {
        e f
    }
}
</code></pre>
<h2>BUGS</h2>
<p> At present, patchwork ignores edges, and supplies no visual clues to indicate nesting. Such clues might consist of nested boxes or thicker rectangular outlines. In addition, it would be good if some cluster label could be displayed. </p>
<p> Patchwork has no mechanism for fitting labels within the supplied box.</p>
<h2>AUTHORS</h2>
<p> Emden R. Gansner &lt;erg [at] graphviz.org&gt;<br />
 Yifan Hu &lt;yifanhu [at] yahoo.com&gt;</p>
<h2>SEE ALSO</h2>
<p> This man page contains only a small amount of the information related to the Graphviz layout programs. The most complete information can be found at <a rel="nofollow" href="http://www.graphviz.org/Documentation.php,">http://www.graphviz.org/Documentation.php,</a> especially in the on-line reference pages. Most of these documents are also available in the <i>doc</i> and <i>doc/info</i> subtrees in the source and binary distributions. </p>
<p> <a href="/docs/linux/man/1-dot/">dot</a>(1) </p>
<p> M. Bruls, K. Huizing and J. van Wijk, &quot;Squarified Treemaps&quot;, Proc. Eurographics and IEEE TVCG Symposium on Visualization, 1999, pp. 33-42. </p>
<h2>Index</h2>
