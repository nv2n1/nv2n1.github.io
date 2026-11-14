---
title: "kmodsign(1)"
name: "kmodsign"
section: "1"
letter: "k"
url: "/docs/linux/man/1-kmodsign/"
description: "kmodsign – Kernel module signing tool"
---

<h2 class="name">NAME</h2>
<p> kmodsign &#8211; Kernel module signing tool </p>
<h2>SYNOPSIS</h2>
<p> <code>kmodsign</code> [<i>,-dpkD/</i>] <i>,&lt;hash algo&gt; &lt;key&gt; &lt;x509&gt; &lt;module&gt; /</i>[<i>,&lt;dest&gt;/</i>]</p>
<h2>DESCRIPTION</h2>
<p> Sign a kernel module image for use with an enforcing kernel.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-p</code></p>
<dd> save a copy of the p7s signature (.p7s)</p>
<dt><code>-d</code></p>
<dd> produce a detached signature file (.p7s) only</p>
<dt><code>-D</code></p>
<dd> produce a full detached signature block (may be cat&#8217;d onto the end of a module)</p>
<dt><code>-k</code></p>
<dd> switch to using keyid for identification </p>
</dl>
<h2>Index</h2>
