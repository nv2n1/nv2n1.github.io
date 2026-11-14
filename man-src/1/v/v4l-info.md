---
title: "v4l-info(1)"
name: "v4l-info"
section: "1"
letter: "v"
url: "/docs/linux/man/1-v4l-info/"
description: "v4l-info – dump video4linux(2) device info to stdout"
---

<h2>NAME</h2>
<p> v4l-info &#8211; dump <a href="/docs/linux/man/2-video4linux/">video4linux</a>(2) device info to stdout</p>
<h2>SYNOPSIS</h2>
<p> <code>v4l-info [ device ]</code></p>
<h2>DESCRIPTION</h2>
<p> <code>v4l-info</code> just prints the <a href="/docs/linux/man/2-v4l/">v4l</a>(2) device info, i.e. calls lots of ioctls and dumps the results to stdout. It optionally accepts the device you want to query. Default is /dev/video0. </p>
<p> Was written to help debug drivers, probably not that useful for end users &#8230;</p>
<h2>AUTHOR</h2>
<p> Gerd Knorr &lt;kraxel [at] bytesex.org&gt; </p>
<h2>Index</h2>
