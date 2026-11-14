---
title: "xmhierarchygetchildnodes(3)"
name: "xmhierarchygetchildnodes"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmhierarchygetchildnodes/"
description: "XmHierarchyGetChildNodes — A List function that returns all instances of an item in the list"
---

<p><code>XmHierarchyGetChildNodes</code> &#8212; A List function that returns all instances of an item in the list</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Hierarchy.h&gt;
<code>WidgetList XmHierarchyGetChildNodes</code>(
<code>Widget widget</code>);</pre>
<h2>Description</h2>
<p><code>XmHierarchyGetChildNodes</code> is a function that returns a list of child nodes of a Hierarchy.</p>
<dl COMPACT>
<dt><i>widget</i></p>
<dd>Specifies the ID of the Hierarchy widget.</dl>
<p> For a complete definition of List and its associated resources, see <code><a href="/docs/linux/man/3-xmhierarchy/">XmHierarchy</a></code>(3).</p>
<h2>Return</h2>
<p>Returns WidgetList with child nodes of the hierachy, or NULL if the hierachy contains no children.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmhierarchy/">XmHierarchy</a></code>(3).</p>
