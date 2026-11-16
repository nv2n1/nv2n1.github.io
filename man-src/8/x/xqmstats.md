---
title: "xqmstats(8)"
name: "xqmstats"
section: "8"
letter: "x"
url: "/docs/linux/man/8-xqmstats/"
description: "xqmstats – Display XFS quota manager statistics from /proc"
---

<p><code>xqmstats</code> &#8211; Display XFS quota manager statistics from /proc</p>
<h2>Synopsis</h2>
<p><i>/usr/sbin/xqmstats</i></p>
<h2>Description</h2>
<p><code>xqmstat</code> queries the kernel for the XFS Quota Manager dquot statistics. It displays: </p>
<dl>
<dd>
</dd><dl>
<dt>&bull;</dt>
<dd>Reclaims</dd>
<dt>&bull;</dt>
<dd>Missed reclaims</dd>
<dt>&bull;</dt>
<dd>Dquot dups</dd>
<dt>&bull;</dt>
<dd>Cache misses</dd>
<dt>&bull;</dt>
<dd>Cache hits</dd>
<dt>&bull;</dt>
<dd>Dquot wants</dd>
<dt>&bull;</dt>
<dd>Shake reclaims</dd>
<dt>&bull;</dt>
<dd>Inact reclaims</dd></dl>
</dl>
<h2>Options</h2>
<p>None.</p>
<h2>See Also</h2>
<p><code>quotastats</code>(1), <code><a href="/docs/linux/man/1-quota/">quota</a></code>(1). </p>
