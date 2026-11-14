---
title: "avcstat(8)"
name: "avcstat"
section: "8"
letter: "a"
url: "/docs/linux/man/8-avcstat/"
description: "avcstat – Display SELinux AVC statistics"
---

<p>avcstat &#8211; Display SELinux AVC statistics</p>
<h2>Synopsis</h2>
<p><code>avcstat</code> [<code>-c</code>] [<code>-f</code> <i>status_file</i>] [<i>interval</i>]</p>
<h2>Description</h2>
<p>Display SELinux AVC statistics. If the <i>interval</i> parameter is specified, the program will loop, displaying updated statistics every <i>interval</i> seconds. Relative values are displayed by default.</p>
<h2>Options</h2>
<dl>
<dt><code>-c</code></p>
<dd>Display the cumulative values.</p>
<dt><code>-f</code></p>
<dd>Specifies the location of the AVC statistics file, defaulting to <i>/sys/fs/selinux/avc/cache_stats</i>.</dl>
<h2>Author</h2>
<p>This manual page was written by Dan Walsh &lt;dwalsh [at] redhat.com&gt;. The program was written by James Morris &lt;jmorris [at] redhat.com&gt;.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-selinux/">selinux</a></code>(8) </p>
