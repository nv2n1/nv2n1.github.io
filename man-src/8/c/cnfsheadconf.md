---
title: "cnfsheadconf(8)"
name: "cnfsheadconf"
section: "8"
letter: "c"
url: "/docs/linux/man/8-cnfsheadconf/"
description: "cnfsheadconf – Read and write CNFS headers"
---

<p>cnfsheadconf &#8211; Read and write CNFS headers</p>
<h2>Synopsis</h2>
<p><code>cnfsheadconf</code> [<code>-hw</code>] [<code>-c</code> <i>class</i>]</p>
<h2>Description</h2>
<p><i>cnfsheadconf</i> reads <i>pathetc</i>/cycbuff.conf and <i>pathetc</i>/storage.conf to determine which <font SIZE="-1">CNFS</font> buffers are available. It then reads all of them or the specified cyclic buffer via the <code>-c</code> flag, and modifies the header as directed by the interactive user if <code>-w</code> is used.</p>
<h2>Options</h2>
<dl>
<dt><code>-c</code> <i>class</i></p>
<dd>Print the status of the specified class. It also modifies it in case <code>-w</code> is used.</p>
<dt><code>-h</code></p>
<dd>Print usage information and exit.</p>
<dt><code>-w</code></p>
<dd>Prompt for modifications to make to cycbuff header.</dl>
<h2>History</h2>
<p>Written by Katsuhiro Kondou &lt;kondou [at] nec.co.jp&gt; for InterNetNews. Converted to <font SIZE="-1">POD</font> by Julien Elie. </p>
<p> <tt>$Id:</tt> cnfsheadconf.pod 8547 2009-07-03 22:02:42Z iulius $</p>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/5-cycbuff-conf/">cycbuff.conf</a></i>(5), <i><a href="/docs/linux/man/5-inn-conf/">inn.conf</a></i>(5), <i><a href="/docs/linux/man/5-storage-conf/">storage.conf</a></i>(5). </p>
