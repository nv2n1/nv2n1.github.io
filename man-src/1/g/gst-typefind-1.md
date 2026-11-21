---

title: "gst-typefind-1(1)"
name: "gst-typefind-1"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gst-typefind-1/"
description: "gst-typefind – print Media type of file"
---

<p> gst-typefind &#8211; print Media type of file</p>
<h2>SYNOPSIS</h2>
<p> <code>gst-typefind &lt;file&gt;</code></p>
<h2>DESCRIPTION</h2>
<p> <i>gst-typefind</i> uses the GStreamer type finding system to determine the relevant GStreamer plugin to parse or decode <code>file</code>, and the corresponding media type.</p>
<h2>OPTIONS</h2>
<p> <i>gst-typefind</i> accepts the following options:</p>
<dl>
<dt><code>&#8211;help</code></dt>
<dd> Print help synopsis and available FLAGS</dd>
<dt><code>&#8211;gst-info-mask=FLAGS</code></dt>
<dd> <i>GStreamer</i> info flags to set (list with &#8211;help)</dd>
<dt><code>&#8211;gst-debug-mask=FLAGS</code></dt>
<dd> <i>GStreamer</i> debugging flags to set (list with &#8211;help)</dd>
<dt><code>&#8211;gst-mask=FLAGS</code></dt>
<dd> <i>GStreamer</i> info and debugging flags to set (list with &#8211;help)</dd>
<dt><code>&#8211;gst-plugin-spew</code></dt>
<dd> <i>GStreamer</i> info flags to set Enable printout of errors while loading <i>GStreamer</i> plugins</dd>
<dt><code>&#8211;gst-plugin-path=PATH</code></dt>
<dd> Add directories separated with &#8216;:&#8217; to the plugin search path</dd></dl>
<h2>SEE ALSO</h2>
<p> <code>gst-feedback</code>(1), <code>gst-inspect</code>(1), <code>gst-launch</code>(1)</p>
<h2>AUTHOR</h2>
<p> The GStreamer team at <a rel="nofollow" href="http://gstreamer.freedesktop.org/">http://gstreamer.freedesktop.org/</a> </p>
