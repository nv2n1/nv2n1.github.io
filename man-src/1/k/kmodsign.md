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
<dt><code>-p</code></dt>
<dd> save a copy of the p7s signature (.p7s)</dd>
<dt><code>-d</code></dt>
<dd> produce a detached signature file (.p7s) only</dd>
<dt><code>-D</code></dt>
<dd> produce a full detached signature block (may be cat&#8217;d onto the end of a module)</dd>
<dt><code>-k</code></dt>
<dd> switch to using keyid for identification </dd>
</dl>
<h2>Index</h2>
