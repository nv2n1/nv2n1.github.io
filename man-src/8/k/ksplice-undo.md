---
title: "ksplice-undo(8)"
name: "ksplice-undo"
section: "8"
letter: "k"
url: "/docs/linux/man/8-ksplice-undo/"
description: "ksplice-undo – Undo a Ksplice update that has been applied to the running kernel"
---

<p>ksplice-undo &#8211; Undo a Ksplice update that has been applied to the running kernel</p>
<h2>Synopsis</h2>
<p><code>ksplice-undo</code> [<i></i><font SIZE="-1"><i>OPTIONS</i></font><i></i>] <i></i><font SIZE="-1"><i>KSPLICE_ID</i></font><i></i></p>
<h2>Description</h2>
<p><code>ksplice-undo</code> takes as input a Ksplice identification tag, as reported by <i><a href="/docs/linux/man/8-ksplice-view/">ksplice-view</a></i>(8), and it reverses that update within the running binary kernel.</p>
<h2>Options</h2>
<dl>
<dt><code>&#8211;debug</code></p>
<dd>Reverses the update with debugging output enabled. Recommended only for debugging.</p>
<dt><code>&#8211;debugfile=</code><i>filename</i></p>
<dd>Sets the location where debugging output should be saved. Implies &#8211;debug.</p>
<dt><code>&#8211;raw-errors</code></p>
<dd>Print only raw error information designed to be machine-readable on standard error (standard output is still intended to be human-readable). If <code>ksplice-undo</code> fails due to an error from the Ksplice kernel modules, the first line on standard error will be a Ksplice <code>abort code</code> (see the Ksplice source code for documentation on these codes). Further lines will vary depending on the abort code. If <code>ksplice-undo</code> fails for any other reason, it will output the line <tt>&quot;OTHER
&quot;</tt>, followed by a human-readable failure message, to standard error.</dl>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/8-ksplice-create/">ksplice-create</a></i>(8), <i><a href="/docs/linux/man/8-ksplice-apply/">ksplice-apply</a></i>(8), <i><a href="/docs/linux/man/8-ksplice-view/">ksplice-view</a></i>(8)</p>
<h2>Bugs</h2>
<p>Please report bugs to &lt;devel [at] ksplice.com&gt;.</p>
<h2>Authors</h2>
<p>Jeff Arnold, Anders Kaseorg, and Tim Abbott</p>
<h2>Copyright</h2>
<p>Copyright (C) 2007-2009 Ksplice, Inc. </p>
<p> This is free software and documentation. You can redistribute and/or modify it under the terms of the <font SIZE="-1">GNU</font> General Public License, version 2.</p>
