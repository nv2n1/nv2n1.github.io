---
title: "xscreensaver-getimage-video(1)"
name: "xscreensaver-getimage-video"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xscreensaver-getimage-video/"
description: "xscreensaver-getimage-video – put a video frame on the root window"
---

<h2 class="name">NAME</h2>
<p> xscreensaver-getimage-video &#8211; put a video frame on the root window </p>
<h2>SYNOPSIS</h2>
<p> <code>xscreensaver-getimage-video</code> [-display <i>host:display.screen</i>] [&#8211;verbose] [&#8211;stdout]</p>
<h2>DESCRIPTION</h2>
<p> The <i>xscreensaver-getimage-video</i> program is a helper program for the xscreensaver hacks that manipulate images. Specifically, it is invoked by <code><a href="/docs/linux/man/1-xscreensaver-getimage/">xscreensaver-getimage</a></code>(1) as needed. This is not a user-level command. </p>
<p> This program grabs a random frame of video from the system&#8217;s video input, and then loads it on the root window. It does this by figuring out which frame-grabbing programs are installed on the system, and invoking the first one it finds. Then it runs <code><a href="/docs/linux/man/1-xscreensaver-getimage-file/">xscreensaver-getimage-file</a></code>(1) to load that image onto the root window.</p>
<h2>OPTIONS</h2>
<p> <i>xscreensaver-getimage-video</i> accepts the following options:</p>
<dl>
<dt><code>&#8211;verbose</code></p>
<dd> Print diagnostics.</p>
<dt><code>&#8211;stdout</code></p>
<dd> Instead of loading the image onto the root window, write it to stdout as a PBM file.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-x/">X</a></code>(1), <code><a href="/docs/linux/man/1-xscreensaver/">xscreensaver</a></code>(1), <code><a href="/docs/linux/man/1-xscreensaver-demo/">xscreensaver-demo</a></code>(1), <code><a href="/docs/linux/man/1-xscreensaver-getimage/">xscreensaver-getimage</a></code>(1), <code><a href="/docs/linux/man/1-xscreensaver-getimage-file/">xscreensaver-getimage-file</a></code>(1), <code><a href="/docs/linux/man/1-bttvgrab/">bttvgrab</a></code>(1), <code><a href="/docs/linux/man/1-qcam/">qcam</a></code>(1), <code><a href="/docs/linux/man/1-streamer/">streamer</a></code>(1), <code><a href="/docs/linux/man/1-atitv/">atitv</a></code>(1), <code><a href="/docs/linux/man/1-vidtomem/">vidtomem</a></code>(1)</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2001 by Jamie Zawinski. Permission to use, copy, modify, distribute, and sell this software and its documentation for any purpose is hereby granted without fee, provided that the above copyright notice appear in all copies and that both that copyright notice and this permission notice appear in supporting documentation. No representations are made about the suitability of this software for any purpose. It is provided &quot;as is&quot; without express or implied warranty.</p>
<h2>AUTHOR</h2>
<p> Jamie Zawinski &lt;jwz [at] jwz.org&gt;, 14-Apr-01 </p>
<h2>Index</h2>
