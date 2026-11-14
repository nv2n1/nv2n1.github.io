---
title: "gst-inspect-0(1)"
name: "gst-inspect-0"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gst-inspect-0/"
description: "gst-inspect – print info about a GStreamer plugin or element"
---

<h2>NAME</h2>
<p> gst-inspect &#8211; print info about a GStreamer plugin or element</p>
<h2>SYNOPSIS</h2>
<p> <code>gst-inspect [OPTION&#8230;] [PLUGIN|ELEMENT]</code></p>
<h2>DESCRIPTION</h2>
<p> <i>gst-inspect</i> is a tool that prints out information on available <i>GStreamer</i> plugins, information about a particular plugin, or information about a particular element. When executed with no PLUGIN or ELEMENT argument, <i>gst-inspect</i> will print a list of all plugins and elements together with a summary. When executed with a PLUGIN or ELEMENT argument, <i>gst-inspect</i> will print information about that plug-in or element.</p>
<h2>OPTIONS</h2>
<p> <i>gst-inspect</i> accepts the following arguments and options:</p>
<dl>
<dt><code>PLUGIN</code></p>
<dd> Name of a plugin</p>
<dt><code>ELEMENT</code></p>
<dd> Name of an element</p>
<dt><code>&#8211;help</code></p>
<dd> Print help synopsis and available FLAGS</p>
<dt><code>&#8211;gst-info-mask=FLAGS</code></p>
<dd> <i>GStreamer</i> info flags to set (list with &#8211;help)</p>
<dt><code>-a, &#8211;print-all</code></p>
<dd> Print all plugins and elements</p>
<dt><code>&#8211;print-plugin-auto-install-info</code></p>
<dd> Print a machine-parsable list of features the specified plugin provides. Useful in connection with external automatic plugin installation mechanisms.</p>
<dt><code>&#8211;gst-debug-mask=FLAGS</code></p>
<dd> <i>GStreamer</i> debugging flags to set (list with &#8211;help)</p>
<dt><code>&#8211;gst-mask=FLAGS</code></p>
<dd> <i>GStreamer</i> info and debugging flags to set (list with &#8211;help)</p>
<dt><code>&#8211;gst-plugin-spew</code></p>
<dd> <i>GStreamer</i> info flags to set Enable printout of errors while loading <i>GStreamer</i> plugins</p>
<dt><code>&#8211;gst-plugin-path=PATH</code></p>
<dd> Add directories separated with &#8216;:&#8217; to the plugin search path</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-gst-feedback/">gst-feedback</a></code>(1), <code><a href="/docs/linux/man/1-gst-launch/">gst-launch</a></code>(1), <code><a href="/docs/linux/man/1-gst-typefind/">gst-typefind</a></code>(1)</p>
<h2>AUTHOR</h2>
<p> The GStreamer team at <a rel="nofollow" href="http://gstreamer.freedesktop.org/">http://gstreamer.freedesktop.org/</a> </p>
<h2>Index</h2>
