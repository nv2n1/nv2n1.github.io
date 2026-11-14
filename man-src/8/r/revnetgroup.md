---
title: "revnetgroup(8)"
name: "revnetgroup"
section: "8"
letter: "r"
url: "/docs/linux/man/8-revnetgroup/"
description: "revnetgroup – generate reverse netgroup data"
---

<p>revnetgroup &#8211; generate reverse netgroup data</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>/usr/lib/yp/revnetgroup</code> [-u | -h]</dl>
<h2>Description</h2>
<p><code>Revnetgroup</code></p>
<dd>processes the standard input in <code><a href="/docs/linux/man/5-netgroup/">netgroup</a></code>(5) format into what is called <i>reverse netgroup</i> form. That is, where the original file shows netgroup memberships in terms of which members reside in a particular group, the reverse netgroup format specifies what groups are associated with a particular member. This information is used to generate the <i>netgroup.byuser</i> and <i>netgroup.byhosts</i> NIS maps. These reverse netgroup maps are used to help speed up netgroup lookups, particularly for the <code>innetgr()</code> library function. </p>
<p> The <code>revnetgroup</code> command prints its results on the standard output. It is usually called only by <i>/var/yp/Makefile</i> when rebuilding the NIS netgroup maps.</p>
<h2>Options</h2>
<p><code>-u</code></p>
<dl>
<dd>Generate <i>netgroup.byuser</i> output; only username information in the original netgroup file is processed.</dl>
<p> <code>-h</code></p>
<dl>
<dd>Generate <i>netgroup.byhost</i> output; only hostname information in the original netgroup file is processed.</dl>
<h2>Files</h2>
<p><i>/var/yp/Makefile</i></p>
<dl>
<dd>The Makefile to build the NIS databases.</dl>
<p> <i>/etc/netgroup</i></p>
<dl>
<dd>The default netgroup database file. This file is most often found only on the NIS master server.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-getnetgrent/">getnetgrent</a></code>(3), <code><a href="/docs/linux/man/5-netgroup/">netgroup</a></code>(5),</p>
<h2>Author</h2>
<p><code>revnetgroup</code> was written by Thorsten Kukuk &lt;kukuk [at] linux-nis.org&gt;.</p>
