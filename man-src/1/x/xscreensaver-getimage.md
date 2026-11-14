---
title: "xscreensaver-getimage(1)"
name: "xscreensaver-getimage"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xscreensaver-getimage/"
description: "xscreensaver-getimage – put some randomly-selected image on the root window"
---

<h2 class="name">NAME</h2>
<p> xscreensaver-getimage &#8211; put some randomly-selected image on the root window </p>
<h2>SYNOPSIS</h2>
<p> <code>xscreensaver-getimage</code> [-display <i>host:display.screen</i>] [&#8211;verbose] window-id [pixmap-id]</p>
<h2>DESCRIPTION</h2>
<p> The <i>xscreensaver-getimage</i> program is a helper program for the xscreensaver hacks that manipulate images. This is not a user-level command. </p>
<p> This program selects a random image, and puts it on the specified window or pixmap. This image might be a snapshot of the desktop; or a frame captured from the system&#8217;s video input; or a randomly-selected image from disk. </p>
<p> If only a window ID is specified, the image will be painted there. If both a window ID and a pixmap ID are specified, then the image will be painted on the pixmap; and the window <i>may</i> be modified as a side-effect.</p>
<h2>OPTIONS</h2>
<p> <i>xscreensaver-getimage</i> reads the <i>~/.xscreensaver</i> file for configuration information. It uses these settings:</p>
<dl>
<dt><code>grabDesktopImages</code></p>
<dd> Whether it is acceptable to grab snapshots of the desktop. The security paranoid might want to turn this off, to avoid letting people see (but not touch!) your desktop while the screen is locked.</p>
<dt><code>grabVideoFrames</code></p>
<dd> Whether it is acceptable to grab frames of video from the system&#8217;s video input. Grabbing of video is done by invoking the <code><a href="/docs/linux/man/1-xscreensaver-getimage-video/">xscreensaver-getimage-video</a></code>(1) program.</p>
<dt><code>chooseRandomImages</code></p>
<dd> Whether it is acceptable to display random images found on disk. Selection and loading of images is done by invoking the <code><a href="/docs/linux/man/1-xscreensaver-getimage-file/">xscreensaver-getimage-file</a></code>(1) program.</p>
<dt><code>imageDirectory</code></p>
<dd> When loading images from disk, this is the directory to find them in. The directory will be searched recursively for images. </p>
<p> It may also be the URL of an RSS or Atom feed, in which case a random image from that feed will be selected instead. The contents of the feed will be cached locally and refreshed periodically as needed.</dl>
<p> If none of the three options are set to True, then video colorbars will be displayed instead.</p>
<h2>BUGS</h2>
<p> When grabbing desktop images, the <i>window</i> argument will be unmapped and have its contents modified, causing flicker. (This does not happen when loading image files or video frames.)</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-x/">X</a></code>(1), <code><a href="/docs/linux/man/1-xscreensaver/">xscreensaver</a></code>(1) <code><a href="/docs/linux/man/1-xscreensaver-demo/">xscreensaver-demo</a></code>(1) <code><a href="/docs/linux/man/1-xscreensaver-getimage-file/">xscreensaver-getimage-file</a></code>(1) <code><a href="/docs/linux/man/1-xscreensaver-getimage-video/">xscreensaver-getimage-video</a></code>(1)</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2001-2011 by Jamie Zawinski. Permission to use, copy, modify, distribute, and sell this software and its documentation for any purpose is hereby granted without fee, provided that the above copyright notice appear in all copies and that both that copyright notice and this permission notice appear in supporting documentation. No representations are made about the suitability of this software for any purpose. It is provided &quot;as is&quot; without express or implied warranty.</p>
<h2>AUTHOR</h2>
<p> Jamie Zawinski &lt;jwz [at] jwz.org&gt;, 14-Apr-01 </p>
<h2>Index</h2>
