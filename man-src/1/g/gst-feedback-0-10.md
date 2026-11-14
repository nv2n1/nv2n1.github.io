---
title: "gst-feedback-0-10(1)"
name: "gst-feedback-0-10"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gst-feedback-0-10/"
description: "gst-feedback – generate debug info for GStreamer bug reports"
---

<p>gst-feedback &#8211; generate debug info for GStreamer bug reports</p>
<h2>Synopsis</h2>
<p><code>gst-feedback-0.10</code></p>
<h2>Description</h2>
<p><i>gst-feedback</i> is a utility that scans the system for various information that is useful to GStreamer developers to help diagnose user problem. </p>
<p> Depending on the type of bug report, it may be useful to attach the output of <i>gst-feedback</i> when you contact the developers. </p>
<p> NOTE: The current version of this script scans many dirs: /usr/lib /usr/local/lib /home /usr/include /usr/local/include /home (again) for various GStreamer installations. Depending on your system you may not want to do this. Improvements to the script are welcome.</p>
<h2>Usage</h2>
<p>Generate the feedback information by running <i>gst-feedback</i>:</p>
<dl>
<dt><code>gst-feedback</code></p>
<dd>
<dt>Possibly redirect output and errors to a file:</p>
<dd>
<dt><code>gst-feedback &amp;&gt; myfeedback</code></p>
<dd></dl>
<h2>Warning</h2>
<p>The <i>gst-feedback</i> dumps a lot of information about a system, some of which may be considered sensitive. If this is a concern, review the information before posting to a public forum, such as the GStreamer bug tracking system.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-gst-inspect/">gst-inspect</a></code>(1), <code><a href="/docs/linux/man/1-gst-launch/">gst-launch</a></code>(1), <code><a href="/docs/linux/man/1-gst-typefind/">gst-typefind</a></code>(1)</p>
<h2>Author</h2>
<p>The GStreamer team at <a rel="nofollow" href="http://gstreamer.freedesktop.org/">http://gstreamer.freedesktop.org/</a></p>
