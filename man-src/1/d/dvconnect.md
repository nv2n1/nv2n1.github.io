---
title: "dvconnect(1)"
name: "dvconnect"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dvconnect/"
description: "dvconnect – receive or transmit raw DV using the video1394 device"
---

<h2>NAME</h2>
<p> dvconnect &#8211; receive or transmit raw DV using the video1394 device</p>
<h2>SYNOPSIS</h2>
<p> <code>dvconnect</code> [ <code>options</code> ] <i>raw dv files or &#8216;&#8211; -&#8216; for stdin/stdout</i></p>
<h2>DESCRIPTION</h2>
<p> <code>dvconnect</code> captures raw DV streams from or sends raw DV streams to the Linux IEEE 1394 video1394 device.</p>
<dl>
<dt><code>&#8211;version</code></p>
<dd> show dvconnect version number.</p>
<dt><code>-s</code>, <code>&#8211;send</code></p>
<dd> send data instead of capturing.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd> show status information while receiving / sending.</p>
<dt><code>-c</code>, <code>&#8211;channel</code>=<i>number</i></p>
<dd> channel to send / receive on (range: 0 &#8211; 63, default = 63).</p>
<dt><code>-k</code>, <code>&#8211;kbuffers</code>=<i>number</i></p>
<dd> number of kernel video1394 frame buffers to use. default = 8.</p>
<dt><code>&#8211;start-frame</code>=<i>count</i></p>
<dd> start at <i>count</i> frame (defaults to 0).</p>
<dt><code>-e</code>, <code>&#8211;end-frame</code>=<i>count</i></p>
<dd> end at <i>count</i> frame (defaults to unlimited).</p>
<dt><code>&#8211;cip-n-ntsc</code>=<i>number</i></p>
<dd> cip n ntsc timing counter (default: 2436).</p>
<dt><code>&#8211;cip-d-ntsc</code>=<i>number</i></p>
<dd> cip d ntsc timing counter (default: 38400).</p>
<dt><code>&#8211;syt-offset</code>=<i>number</i></p>
<dd> syt offset (default: 10000 range: 10000-26000).</p>
<dt><code>-b</code>, <code>&#8211;buffers</code>=<i>number</i></p>
<dd> max number of file io thread buffers to use. default = 250.</p>
<dt><code>-u</code>, <code>&#8211;underrun-data</code>=<i>filename</i></p>
<dd> file with the frame to send in case of underruns.</p>
<dt><code>-d</code>, <code>&#8211;device</code>=<i>filename</i></p>
<dd> Specify the video1394 device (default /dev/video1394/0).</dl>
<p> Help Options</p>
<dl>
<dt>&#8211;<code>?</code>, <code>&#8211;help</code></p>
<dd> Show help message.</p>
<dt><code>&#8211;usage</code></p>
<dd> Display brief usage message.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-playdv/">playdv</a></code>(1),<code><a href="/docs/linux/man/1-dubdv/">dubdv</a></code>(1),<code><a href="/docs/linux/man/1-encodedv/">encodedv</a></code>(1).</p>
<h2>AVAILABILITY</h2>
<p> See <a rel="nofollow" href="http://libdv.sourceforge.net/">http://libdv.sourceforge.net/</a> for the latest version.</p>
<h2>AUTHORS</h2>
<p> <code>dvconnect</code> was written by Peter Schlaile &lt;udbz [at] rz.uni-karlsruhe.de&gt;. </p>
<p> This manual page is based on dvconnect&#8217;s help message and was written by Dan Dennedy &lt;dan [at] dennedy.org&gt;. </p>
<h2>Index</h2>
