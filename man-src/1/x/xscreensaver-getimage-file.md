---
title: "xscreensaver-getimage-file(1)"
name: "xscreensaver-getimage-file"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xscreensaver-getimage-file/"
description: "xscreensaver-getimage-file – put a randomly-selected image on the root window"
---

<h2>SYNOPSIS</h2>
<p> <code>xscreensaver-getimage-file</code> [-display <i>host:display.screen</i>] [&#8211;verbose] [&#8211;name] [&#8211;no-cache] directory-or-URL</p>
<h2>DESCRIPTION</h2>
<p> The <i>xscreensaver-getimage-file</i> program is a helper program for the xscreensaver hacks that manipulate images. Specifically, it is invoked by <code><a href="/docs/linux/man/1-xscreensaver-getimage/">xscreensaver-getimage</a></code>(1) as needed. This is not a user-level command. </p>
<p> This program selects a random image from disk, and loads it on the root window. It does this by figuring out which image-loading programs are installed on the system, and invoking the first one it finds.</p>
<h2>OPTIONS</h2>
<p> <i>xscreensaver-getimage-file</i> accepts the following options:</p>
<dl>
<dt><code>&#8211;verbose</code></dt>
<dd> Print diagnostics.</dd>
<dt><code>&#8211;name</code></dt>
<dd> Don&#8217;t load an image: instead just print the file name to stdout.</dd>
<dt><i>directory-or-URL</i></dt>
<dd> If a directory is specified, it will be searched recursively for images. Any images found will eligible for display. For efficiency, the contents of the directory are cached for a few hours before it is re-scanned. </dd>
<p> If a URL is specified, it should be the URL of an RSS or Atom feed containing images. The first time it is accessed, all of the images in the feed will be downloaded to a local cache directory. If a few hours have elapsed since last time, the URL will be polled again, and any new images will be cached, any images no longer in the feed will be expired.</p>
<dt><code>&#8211;no-cache</code></dt>
<dd> Update the cache immediately, even if it is not time yet. This will re-scan the directory, or re-poll the RSS feed.</dd></dl>
<h2>SEE ALSO</h2>
<p> <code>X</code>(1), <code><a href="/docs/linux/man/1-xscreensaver/">xscreensaver</a></code>(1), <code><a href="/docs/linux/man/1-xscreensaver-demo/">xscreensaver-demo</a></code>(1), <code><a href="/docs/linux/man/1-xscreensaver-getimage/">xscreensaver-getimage</a></code>(1), <code><a href="/docs/linux/man/1-xv/">xv</a></code>(1), <code>xli</code>(1), <code>xloadimage</code>(1), <code>chbg</code>(1)</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2001-2012 by Jamie Zawinski. Permission to use, copy, modify, distribute, and sell this software and its documentation for any purpose is hereby granted without fee, provided that the above copyright notice appear in all copies and that both that copyright notice and this permission notice appear in supporting documentation. No representations are made about the suitability of this software for any purpose. It is provided &quot;as is&quot; without express or implied warranty.</p>
<h2>AUTHOR</h2>
<p> Jamie Zawinski &lt;jwz [at] jwz.org&gt;, 14-Apr-01 </p>
