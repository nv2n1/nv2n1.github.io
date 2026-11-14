---
title: "amcheckdb(8)"
name: "amcheckdb"
section: "8"
letter: "a"
url: "/docs/linux/man/8-amcheckdb/"
description: "amcheckdb – check Amanda database for tape consistency"
---

<p>amcheckdb &#8211; check Amanda database for tape consistency</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>amcheckdb</code> <i>config</i></dl>
<h2>Description</h2>
<p><code>Amcheckdb</code></p>
<dd>verifies that every tape mentioned in the Amanda database is still valid in the <code><a href="/docs/linux/man/5-tapelist/">tapelist</a></code>(5). </p>
<p> See the <code><a href="/docs/linux/man/8-amanda/">amanda</a></code>(8) man page for more details about Amanda.</p>
<h2>Example</h2>
<p>This shows a normal response: </p>
<pre># amcheckdb daily
Ready.</pre>
<p>This shows tape <i>DMP014</i> is still listed in the database but is no longer listed in the <code><a href="/docs/linux/man/5-tapelist/">tapelist</a></code>(5): </p>
<pre># amcheckdb daily
Tape DMP014 missing in /usr/local/etc/amanda//daily/tapelist
Ready.</pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-amanda/">amanda</a></code>(8), <code><a href="/docs/linux/man/8-amadmin/">amadmin</a></code>(8), <code><a href="/docs/linux/man/8-amrmtape/">amrmtape</a></code>(8) </p>
<p> The Amanda Wiki: : <a rel="nofollow" href="http://wiki.zmanda.com/">http://wiki.zmanda.com/</a></p>
<h2>Authors</h2>
<p><code>Adrian T. Filipi-Martin</code> &lt;atf3r [at] cs.virginia.edu&gt; </p>
<p> <code>Stefan G. Weichinger</code> &lt;sgw [at] amanda.org&gt;</p>
