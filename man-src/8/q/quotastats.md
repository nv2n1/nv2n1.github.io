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
<dl>
<dt>&bull;</p>
<dd>Supported kernel quota version</p>
<dt>&bull;</p>
<dd>Number of dquot lookups</p>
<dt>&bull;</p>
<dd>Number of dquot drops</p>
<dt>&bull;</p>
<dd>Number of dquot reads</p>
<dt>&bull;</p>
<dd>Number of dquot writes</p>
<dt>&bull;</p>
<dd>Number of quotafile syncs</p>
<dt>&bull;</p>
<dd>Number of dquot cache hits</p>
<dt>&bull;</p>
<dd>Number of allocated dquots</p>
<dt>&bull;</p>
<dd>Number of free dquots</p>
<dt>&bull;</p>
<dd>Number of in use dquot entries (user/group)</dl>
</dl>
<h2>Options</h2>
<p>None.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-quota/">quota</a></code>(1). </p>
