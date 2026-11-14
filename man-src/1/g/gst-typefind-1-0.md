---
title: "gst-typefind-1-0(1)"
name: "gst-typefind-1-0"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gst-typefind-1-0/"
description: "gst-typefind-1.0 – print Media type of file"
---

<p>gst-typefind-1.0 &#8211; print Media type of file </p>
<h2>Synopsis</h2>
<p><code>gst-typefind-1.0 &lt;file&gt;</code></p>
<h2>Description</h2>
<p><i>gst-typefind-1.0</i> uses the GStreamer type finding system to determine the relevant GStreamer plugin to parse or decode <code>file</code>, and the corresponding media type.</p>
<h2>Options</h2>
<p><i>gst-typefind-1.0</i> accepts the following options:</p>
<dl>
<dt><code>&#8211;help</code></p>
<dd>Print help synopsis and available FLAGS</p>
<dt><code>&#8211;gst-info-mask=FLAGS</code></p>
<dd><i>GStreamer</i> info flags to set (list with &#8211;help)</p>
<dt><code>&#8211;gst-debug-mask=FLAGS</code></p>
<dd><i>GStreamer</i> debugging flags to set (list with &#8211;help)</p>
<dt><code>&#8211;gst-mask=FLAGS</code></p>
<dd><i>GStreamer</i> info and debugging flags to set (list with &#8211;help)</p>
<dt><code>&#8211;gst-plugin-spew</code></p>
<dd><i>GStreamer</i> info flags to set Enable printout of errors while loading <i>GStreamer</i> plugins</p>
<dt><code>&#8211;gst-plugin-path=PATH</code></p>
<dd>Add directories separated with &#8216;:&#8217; to the plugin search path</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-gst-inspect-1-0/">gst-inspect-1.0</a></code>(1), <code><a href="/docs/linux/man/1-gst-launch-1-0/">gst-launch-1.0</a></code>(1)</p>
<h2>Author</h2>
<p>The GStreamer team at <a rel="nofollow" href="http://gstreamer.freedesktop.org/">http://gstreamer.freedesktop.org/</a></p>
