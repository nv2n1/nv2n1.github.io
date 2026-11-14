---
title: "booth-keygen(8)"
name: "booth-keygen"
section: "8"
letter: "b"
url: "/docs/linux/man/8-booth-keygen/"
description: "booth-keygen – generate authentication key"
---

<p>booth-keygen &#8211; generate authentication key</p>
<h2>Synopsis</h2>
<p><code>booth-keygen</code> [<i>-h</i>] [<i>auth-file</i>]</p>
<h2>Description</h2>
<p>This program generates an authentication key suitable for <i>booth</i> using <i>/dev/urandom</i> as source.</p>
<h2>Parameters</h2>
<p><i>auth-file</i></p>
<dl>
<dd>The file to contain the generated key. Defaults to <i>/etc/booth/authkey</i>. Use absolute paths.</dl>
<h2>Options</h2>
<p><code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dd>Print usage.</dl>
<h2>Exit Status</h2>
<p><code>0</code></p>
<dl>
<dd>Success.</dl>
<p> <code>!= 0</code></p>
<dl>
<dd>File already exists or some other error.</dl>
<h2>Copying</h2>
<p>Copyright &#169; 2015 Dejan Muhamedagic &lt;dmuhamedagic [at] suse.com&gt; </p>
<p> Free use of this software is granted under the terms of the GNU General Public License (GPL) as of version 2 (see COPYING file) or later.</p>
