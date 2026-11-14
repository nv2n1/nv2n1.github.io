---
title: "dshbak(1)"
name: "dshbak"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dshbak/"
description: "dshbak – format output from pdsh command"
---

<h2>NAME</h2>
<p> dshbak &#8211; format output from pdsh command </p>
<h2>SYNOPSIS</h2>
<p> <code>dshbak </code> [<i>OPTION</i>].. </p>
<h2>DESCRIPTION</h2>
<p> The <code>dshbak</code> program formats <code>pdsh</code> pdsh output for humans. Output from each node is consolidated, the leading &quot;<i>node:</i>&quot; is stripped, and a header block with the node name is added. If the <i>-c</i> option is specified, nodes with identical output are not displayed twice; instead, the header will contain a list of nodes. The list of nodes is further compressed into node ranges if the node names have a numeric suffix. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code></p>
<dd> Display a summary of command line options.</p>
<dt><code>-c</code></p>
<dd> Do not display identical output from nodes twice. Instead, print the list of nodes with matching output in the header block.</p>
<dt><code>-d </code><i>DIR</i></p>
<dd> Write consolidated node output to separate files in output directory <i>DIR</i>. Any existing files will be overwritten.</p>
<dt><code>-f</code></p>
<dd> With <i>-d</i>, force creation of specified <i>DIR</i>. </p>
</dl>
<h2>ORIGIN</h2>
<p> A rewrite of IBM <a href="/docs/linux/man/1-dshbak/">dshbak</a>(1) by Jim Garlick<br />
 &lt;garlick [at] llnl.gov&gt; on LLNL&#8217;s ASCI Blue-Pacific IBM SP system. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pdsh/">pdsh</a></code>(1) </p>
<p> <code><a rel="nofollow" href="http://pdsh.googlecode.com">http://pdsh.googlecode.com</a></code> </p>
<h2>Index</h2>
