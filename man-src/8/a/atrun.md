---
title: "atrun(8)"
name: "atrun"
section: "8"
letter: "a"
url: "/docs/linux/man/8-atrun/"
description: "atrun – run jobs queued for later execution"
---

<p>atrun &#8211; run jobs queued for later execution</p>
<h2>Synopsis</h2>
<p><code>atrun</code> [<code>-l</code> <i>load_avg</i>] [<code>-d</code>]</p>
<h2>Description</h2>
<p><code>atrun</code> runs jobs queued by <code><a href="/docs/linux/man/1-at/">at</a>(1)</code>. It is a shell script invoking <code>/usr/sbin/atd</code> with the <i>-s</i> option, and is provided for backward compatibility with older installations.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-at/">at</a></code>(1), <code><a href="/docs/linux/man/8-atd/">atd</a></code>(8).</p>
<h2>Author</h2>
<p>At was mostly written by Thomas Koenig, ig25 [at] rz.uni-karlsruhe.de.</p>
