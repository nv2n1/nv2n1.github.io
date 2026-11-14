---
title: "rpmgraph(8)"
name: "rpmgraph"
section: "8"
letter: "r"
url: "/docs/linux/man/8-rpmgraph/"
description: "rpmgraph – Display RPM Package Dependency Graph"
---

<p>rpmgraph &#8211; Display RPM Package Dependency Graph</p>
<h2>Synopsis</h2>
<p><code>rpmgraph</code> <i>PACKAGE_FILE</i><i> &#8230;</i> </p>
<h2>Description</h2>
<p><code>rpmgraph</code> uses <i>PACKAGE_FILE</i> arguments to generate a package dependency graph. Each <i>PACKAGE_FILE</i> argument is read and added to an rpm transaction set. The elements of the transaction set are partially ordered using a topological sort. The partially ordered elements are then printed to standard output. </p>
<p> Nodes in the dependency graph are package names, and edges in the directed graph point to the parent of each node. The parent node is defined as the last predecessor of a package when partially ordered using the package dependencies as a relation. That means that the parent of a given package is the package&#8217;s last prerequisite. </p>
<p> The output is in <code><a href="/docs/linux/man/1-dot/">dot</a></code>(1) directed graph format, and can be displayed or printed using the <code>dotty</code> graph editor from the <code>graphviz</code> package. There are no <code>rpmgraph</code> specific options, only common <code>rpm</code> options. See the <code>rpmgraph</code> usage message for what is currently implemented.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-dot/">dot</a></code>(1), </p>
<p> <code><a href="/docs/linux/man/1-dotty/">dotty</a></code>(1), </p>
<p> <code> <a rel="nofollow" href="http://www.graphviz.org/">http://www.graphviz.org/</a> &lt;URL:<a href="http://www.graphviz.org/">http://www.graphviz.org/</a>&gt; </code></p>
<h2>Authors</h2>
<p>Jeff Johnson &lt;jbj [at] redhat.com&gt;</p>
