---
title: "quotastats(8)"
name: "quotastats"
section: "8"
letter: "q"
url: "/docs/linux/man/8-quotastats/"
description: "quotastats – Program to query quota statistics"
---

<p><code>quotastats</code> &#8211; Program to query quota statistics</p>
<h2>Synopsis</h2>
<p><i>/usr/sbin/quotastats</i></p>
<h2>Description</h2>
<p><code>quotastats</code> queries the kernel for quota statistics. It displays: </p>
<dl>
<dd>
</dd><dl>
<dt>&bull;</dt>
<dd>Supported kernel quota version</dd>
<dt>&bull;</dt>
<dd>Number of dquot lookups</dd>
<dt>&bull;</dt>
<dd>Number of dquot drops</dd>
<dt>&bull;</dt>
<dd>Number of dquot reads</dd>
<dt>&bull;</dt>
<dd>Number of dquot writes</dd>
<dt>&bull;</dt>
<dd>Number of quotafile syncs</dd>
<dt>&bull;</dt>
<dd>Number of dquot cache hits</dd>
<dt>&bull;</dt>
<dd>Number of allocated dquots</dd>
<dt>&bull;</dt>
<dd>Number of free dquots</dd>
<dt>&bull;</dt>
<dd>Number of in use dquot entries (user/group)</dd></dl>
</dl>
<h2>Options</h2>
<p>None.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-quota/">quota</a></code>(1). </p>
