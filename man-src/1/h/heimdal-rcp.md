---
title: "heimdal-rcp(1)"
name: "heimdal-rcp"
section: "1"
letter: "h"
url: "/docs/linux/man/1-heimdal-rcp/"
description: "rcp – copy file to and from remote machines"
---

<h2 class="name">NAME</h2>
<p> <code>rcp</code> &#8211; copy file to and from remote machines </p>
<h2>SYNOPSIS</h2>
<p> <code>rcp</code> [-<code>45FKpxz</code> ] [-<code>P </code><i>port</i> ] <i>file1 file2</i><br />
<code>rcp</code> [-<code>45FKprxz</code> ] [-<code>P </code><i>port</i> ] <i>file&#8230; directory</i></p>
<h2>DESCRIPTION</h2>
<p> <code>rcp</code> copies files between machines. Each file argument is either a remote file name of the form &#8220;rname [at] rhost:path&#8221; or a local file (containing no colon or with a slash before the first colon). </p>
<p> Supported options:</p>
<dl>
<dt> &#8211;<code>4</code> &#8211;<code>5</code> &#8211;<code>K</code> &#8211;<code>F</code> &#8211;<code>x</code> &#8211;<code>z</code></p>
<dd>
<dd>These options are passed on to <a href="/docs/linux/man/1-rsh/">rsh</a>(1).</p>
<dt><code>-P </code><i>port</i></p>
<dd> This will pass the option &#8211;<code>p </code><i>port</i> to <a href="/docs/linux/man/1-rsh/">rsh</a>(1).</p>
<dt><code>-p</code></p>
<dd> Preserve file permissions.</p>
<dt><code>-r</code></p>
<dd> Copy source directories recursively.</dl>
<h2>DIAGNOSTICS</h2>
<p> <code>rcp</code> is implemented as a protocol on top of <a href="/docs/linux/man/1-rsh/">rsh</a>(1), and thus requires a working rsh. If you intend to use Kerberos authentication, rsh needs to be Kerberos aware, else you may see more or less strange errors, such as &quot;login incorrect&quot;, or &quot;lost connection&quot;.</p>
<h2>HISTORY</h2>
<p> The <code>rcp</code> utility first appeared in 4.2BSD. This version is derived from 4.3BSD-Reno. </p>
<h2>Index</h2>
