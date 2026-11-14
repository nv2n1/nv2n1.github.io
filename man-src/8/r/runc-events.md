---
title: "runc-events(8)"
name: "runc-events"
section: "8"
letter: "r"
url: "/docs/linux/man/8-runc-events/"
description: "runc-events – display container events and statistics."
---

<p><code>runc-events</code> &#8211; display container events and statistics. </p>
<h2>Synopsis</h2>
<p><code>runc events</code> [<i>option</i> &#8230;] <i>container-id</i> </p>
<h2>Description</h2>
<p>The <code>events</code> command displays information about the container. By default, it works continuously, displaying stats every 5 seconds, and container events as they occur. </p>
<h2>Options</h2>
<dl>
<dt><code>&#8211;interval</code> <i>time</i></p>
<dd>Set the stats collection interval. Default is <code>5s</code>. </p>
<dt><code>&#8211;stats</code></p>
<dd>Show the container&#8217;s stats once then exit. </p>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-runc/">runc</a></code>(8). </p>
