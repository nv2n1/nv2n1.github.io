---
title: "xmtargetsarecompatible(3)"
name: "xmtargetsarecompatible"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmtargetsarecompatible/"
description: "XmTargetsAreCompatible — A function that tests whether the target types match between a drop site and source object"
---

<p><code>XmTargetsAreCompatible</code> &#8212; A function that tests whether the target types match between a drop site and source object</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/DragDrop.h&gt;
<code>Boolean XmTargetsAreCompatible</code>(
<code>Display *display</code>,
<code>Atom *export_targets</code>,
<code>Cardinal num_export_targets</code>,
<code>Atom *import_targets</code>,
<code>Cardinal num_import_targets</code>);</pre>
<h2>Description</h2>
<p><code>XmTargetsAreCompatible</code> determines whether the import targets of the destination match any of the export targets of a source. If there is at least one target in common, the function returns True.</p>
<dl COMPACT>
<dt><i>display</i></p>
<dd>Specifies the display connection.</p>
<dt><i>export_targets</i></p>
<dd>Specifies the list of target atoms associated with the source object. This resource identifies the selection targets the source can convert to.</p>
<dt><i>num_export_targets</i></p>
<dd>Specifies the number of entries in the list of export targets.</p>
<dt><i>import_targets</i></p>
<dd>Specifies the list of targets to be checked against the <code>XmNexportTargets</code> of the source associated with the specified DragContext</p>
<dt><i>num_import_targets</i></p>
<dd>Specifies the number of entries in the <i>import_targets</i> list.</dl>
<h2>Return</h2>
<p>Returns a Boolean value that indicates whether the destination targets are compatible with the source targets. If there is at least one target in common, the routine returns True; otherwise, returns False.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmdragcontext/">XmDragContext</a></code>(3) and <code><a href="/docs/linux/man/3-xmdropsite/">XmDropSite</a></code>(3).</p>
