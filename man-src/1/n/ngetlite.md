---
title: "ngetlite(1)"
name: "ngetlite"
section: "1"
letter: "n"
url: "/docs/linux/man/1-ngetlite/"
description: "ngetlite – retrieve files from NNTP hosts"
---

<h2>NAME</h2>
<p> ngetlite &#8211; retrieve files from NNTP hosts</p>
<h2>SYNOPSIS</h2>
<p> <code>ngetlite &lt;listfiles&#8230;&gt;</code></p>
<h2>DESCRIPTION</h2>
<p> <code>ngetlite</code> retrieves messages as described in each listfile. Listfiles are generated with:<br />
 <code>nget -w &lt;listfile&gt; &lt;retrieval args&gt;</code> </p>
<p> In almost all circumstances, you will want to download and decode directly with nget. However, in some cases ngetlite can be useful on computers with low ram or cpu, that can&#8217;t handle the large cache files needed for some groups. You can run nget -w on some other computer and then do the actual downloading with ngetlite using very little resources.</p>
<h2>EXAMPLES</h2>
<p> The following sequence of commands demonstrates a typical usage:<br />
 nget -w foo.list -G alt.foo -r &quot;\.png&quot;<br />
 ngetlite foo.list<br />
 nget -N -G alt.foo -r &quot;\.png&quot;</p>
<h2>ENVIRONMENT</h2>
<dl>
<dt>NGETLITE_TIMEOUT</p>
<dd> Socket timeout value in seconds.</p>
<dt>NGETLITE_TRIES</p>
<dd> Max number of attempts per article.</dl>
<h2>AUTHOR</h2>
<p> Matthew Mueller &lt;donut AT dakotacom.net&gt;</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-nget/">nget</a></code>(1) </p>
<h2>Index</h2>
