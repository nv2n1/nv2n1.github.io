---
title: "ksplice-view(8)"
name: "ksplice-view"
section: "8"
letter: "k"
url: "/docs/linux/man/8-ksplice-view/"
description: "ksplice-view – View in-kernel or on-disk Ksplice kernel updates"
---

<p>ksplice-view &#8211; View in-kernel or on-disk Ksplice kernel updates</p>
<h2>Synopsis</h2>
<p><code>ksplice-view</code> <code>ksplice-view</code> <code>&#8211;id=</code><i></i><i>KSPLICE_ID</i><i></i> </p>
<pre><code>ksplice-view --file={UPDATE_TARBALL | UPDATE_TREE}</code></pre>
<h2>Description</h2>
<p>When called with no arguments, <code>ksplice-view</code> lists the identification tags of all of the Ksplice updates that are currently present in the running kernel, along with their descriptions. </p>
<p> <code>ksplice-view</code> can report about a specific Ksplice update when given the update&#8217;s identification tag <i></i><i>KSPLICE_ID</i><i></i> (if the update is in the kernel) or given the update&#8217;s tarball filename <i></i><i>UPDATE_TARBALL</i><i></i> or unpacked tree root <i></i><i>UPDATE_TREE</i><i></i> (if the update is on disk).</p>
<h2>Options</h2>
<dl>
<dt><code>&#8211;id=</code><i></i><i>KSPLICE_ID</i><i></i></dt>
<dd>Report information about the Ksplice update <i></i><i>KSPLICE_ID</i><i></i> currently loaded in the running kernel.</dd>
<dt><code>&#8211;file=</code>{<i></i><i>UPDATE_TARBALL</i><i></i> | <i></i><i>UPDATE_TREE</i><i></i>}</dt>
<dd>Report information about the Ksplice update on disk as the tarball <i></i><i>UPDATE_TARBALL</i><i></i> or unpacked as the tree <i></i><i>UPDATE_TREE</i><i></i>.</dd>
<dt><code>-q</code></dt>
<dd>Output only the update IDs, one per line, omitting descriptions.</dd></dl>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/8-ksplice-create/">ksplice-create</a></i>(8), <i><a href="/docs/linux/man/8-ksplice-apply/">ksplice-apply</a></i>(8), <i><a href="/docs/linux/man/8-ksplice-undo/">ksplice-undo</a></i>(8)</p>
<h2>Bugs</h2>
<p>Please report bugs to &lt;devel [at] ksplice.com&gt;.</p>
<h2>Authors</h2>
<p>Jeff Arnold, Anders Kaseorg, and Tim Abbott</p>
<h2>Copyright</h2>
<p>Copyright (C) 2007-2009 Ksplice, Inc. </p>
<p> This is free software and documentation. You can redistribute and/or modify it under the terms of the GNU General Public License, version 2.</p>
