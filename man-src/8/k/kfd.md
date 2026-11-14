---
title: "kfd(8)"
name: "kfd"
section: "8"
letter: "k"
url: "/docs/linux/man/8-kfd/"
description: "kfd – receive forwarded tickets"
---

<p><code>kfd</code> &#8211; receive forwarded tickets</p>
<h2>Synopsis</h2>
<p>[-<code>p </code><i>port</i> &#8211;<code>-port = </code><i>port</i> ] [-<code>i | -inetd</code> ] [-<code>R </code><i>regpag</i> &#8211;<code>-regpag = </code><i>regpag</i> ] [-<code>h | -help</code> ] [-<code>-version</code> ]</p>
<h2>Description</h2>
<p>This is the daemon for <a href="/docs/linux/man/1-kf/">kf</a>(1). Supported options:</p>
<dl>
<dt> &#8211;<code>p </code><i>port</i> &#8211;<code>-port = </code><i>port</i></p>
<dd>
<dd>port to listen to</p>
<dt><code>-i , -inetd</code></p>
<dd>not started from inetd</p>
<dt> &#8211;<code>R </code><i>regpag</i> &#8211;<code>-regpag= </code><i>regpag</i></p>
<dd>
<dd>path to regpag binary</dl>
<h2>Examples</h2>
<p>Put the following in /etc/inetd.conf </p>
<pre>kf stream tcp nowait root /usr/heimdal/libexec/kfd kfd</pre>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-kf/">kf</a>(1) </p>
