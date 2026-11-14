---
title: "amcleanupdisk(8)"
name: "amcleanupdisk"
section: "8"
letter: "a"
url: "/docs/linux/man/8-amcleanupdisk/"
description: "amcleanupdisk – cleanup holding disk directory"
---

<p>amcleanupdisk &#8211; cleanup holding disk directory</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>amcleanupdisk</code> [<code>-r</code>] [<code>-v</code>] <i>config</i></dl>
<h2>Description</h2>
<p><code>Amcleanupdisk</code></p>
<dd>list and/or remove invalid file from the holding disk directories. </p>
<p> This program is run by <code>amcleanup</code>. </p>
<p> See the <code><a href="/docs/linux/man/8-amanda/">amanda</a></code>(8) man page for more details about Amanda.</p>
<h2>Options</h2>
<p><code>-r</code></p>
<dl>
<dd>Remove invalid file from holding disk.</dl>
<p> <code>-v</code></p>
<dl>
<dd>Generate verbose output.</dl>
<h2>Examples</h2>
<p>This example runs the Amanda holding disk cleanup process. </p>
<pre>% amcleanupdisk daily -v -r</pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-amanda/">amanda</a></code>(8), <code><a href="/docs/linux/man/8-amcleanup/">amcleanup</a></code>(8), <code><a href="/docs/linux/man/8-amdump/">amdump</a></code>(8) </p>
<p> The Amanda Wiki: : <a rel="nofollow" href="http://wiki.zmanda.com/">http://wiki.zmanda.com/</a></p>
<h2>Authors</h2>
<p><code>James da Silva</code> &lt;jds [at] amanda.org&gt; </p>
<p> <code>Stefan G. Weichinger</code> &lt;sgw [at] amanda.org&gt;</p>
