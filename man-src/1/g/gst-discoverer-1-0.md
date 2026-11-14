---
title: "gst-discoverer-1-0(1)"
name: "gst-discoverer-1-0"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gst-discoverer-1-0/"
description: "gst-discoverer-1.0 – Display file metadata and stream information"
---

<p>gst-discoverer-1.0 &#8211; Display file metadata and stream information </p>
<h2>Synopsis</h2>
<p><code>gst-discoverer-1.0</code> <i>FILE|DIRECTORY|URI [FILE2|DIRECTORY2|URI2]</i></p>
<h2>Description</h2>
<p><i>gst-discoverer-1.0</i> is a tool that can be used to print basic metadata and stream information about a media file. It can be run on individual files or whole directories. It will recurse into sub-directories in that case. </p>
<h2>Options</h2>
<p><i>gst-discoverer-1.0</i> accepts the following options:</p>
<dl>
<dt><code>&#8211;help</code></p>
<dd>Print help synopsis and available FLAGS</p>
<dt><code>-v, &#8211;verbose</code></p>
<dd>Output all available information</p>
<dt><code>-a, &#8211;async</code></p>
<dd>Use asynchronous code path</p>
<dt><code>-t, &#8211;timeout=T</code></p>
<dd>Specify timeout in seconds (default: 10 seconds)</p>
<dt><code>-c, &#8211;toc</code></p>
<dd>Output TOC (chapters and editions) if available</p>
<dd></dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-gst-inspect-1-0/">gst-inspect-1.0</a></code>(1), <code><a href="/docs/linux/man/1-gst-launch-1-0/">gst-launch-1.0</a></code>(1),</p>
<h2>Author</h2>
<p>The GStreamer team at <a rel="nofollow" href="http://gstreamer.freedesktop.org/">http://gstreamer.freedesktop.org/</a></p>
