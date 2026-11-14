---
title: "makedbz(8)"
name: "makedbz"
section: "8"
letter: "m"
url: "/docs/linux/man/8-makedbz/"
description: "makedbz – Rebuild dbz files"
---

<p>makedbz &#8211; Rebuild dbz files</p>
<h2>Synopsis</h2>
<p><code>makedbz</code> [<code>-io</code>] [<code>-f</code> <i>filename</i>] [<code>-s</code> <i>size</i>]</p>
<h2>Description</h2>
<p><code>makedbz</code> rebuilds <i><a href="/docs/linux/man/3-dbz/">dbz</a></i>(3) database. The default name of the text file is <i>pathdb</i>/history; to specify a different name, use the <code>-f</code> flag.</p>
<h2>Options</h2>
<dl>
<dt><code>-f</code> <i>filename</i></p>
<dd>If the <code>-f</code> flag is used, then the database files are named <tt>&quot;</tt>filename<tt>.dir&quot;</tt>, <tt>&quot;</tt>filename<tt>.index&quot;</tt>, and <tt>&quot;</tt>filename<tt>.hash&quot;</tt>. If the <code>-f</code> flag is not used, then a temporary link to the name <tt>&quot;history.n&quot;</tt> is made and the database files are written as <tt>&quot;history.n.index&quot;</tt> , <tt>&quot;history.n.hash&quot;</tt> and <tt>&quot;history.n.dir&quot;</tt>.</p>
<dt><code>-i</code></p>
<dd>To ignore the old database, use the <code>-i</code> flag. Using the <code>-o</code> or <code>-s</code> flags implies the <code>-i</code> flag.</p>
<dt><code>-o</code></p>
<dd>If the <code>-o</code> flag is used, then the link is not made and any existing history files are overwritten. If the old database exists, <code>makedbz</code> will use it to determine the size of the new database.</p>
<dt><code>-s</code> <i>size</i></p>
<dd><code>makedbz</code> will also ignore any old database if the <code>-s</code> flag is used to specify the approximate number of entries in the new database. Accurately specifying the size is an optimization that will create a more efficient database. Size is measured in key-value pairs (i.e. lines). (The size should be the estimated eventual size of the file, typically the size of the old file.) </p>
<p> For more information, see the discussion of <code>dbzfresh</code> and <code>dbzsize</code> in <i><a href="/docs/linux/man/3-dbz/">dbz</a></i>(3).</dl>
<h2>History</h2>
<p>Written by Katsuhiro Kondou &lt;kondou [at] nec.co.jp&gt; for InterNetNews. Converted to <font SIZE="-1">POD</font> by Julien Elie. </p>
<p> <tt>$Id:</tt> makedbz.pod 8584 2009-08-20 21:54:07Z iulius $</p>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/3-dbz/">dbz</a></i>(3), <i><a href="/docs/linux/man/5-history/">history</a></i>(5). </p>
