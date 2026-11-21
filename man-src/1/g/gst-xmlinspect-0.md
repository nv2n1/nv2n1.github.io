---

title: "gst-xmlinspect-0(1)"
name: "gst-xmlinspect-0"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gst-xmlinspect-0/"
description: "gst-xmlinspect – print info about a GStreamer plugin or element"
---

<p> gst-xmlinspect &#8211; print info about a GStreamer plugin or element</p>
<h2>SYNOPSIS</h2>
<p> <code>gst-xmlinspect [OPTION&#8230;] [PLUGIN|ELEMENT]</code></p>
<h2>DESCRIPTION</h2>
<p> <i>gst-xmlinspect</i> is a tool that prints out information on available <i>GStreamer</i> plugins, information about a particular plugin, or information about a particular element. When executed with no PLUGIN or ELEMENT argument, <i>gst-xmlinspect</i> will print a list of all plugins and elements. When executed with a PLUGIN or ELEMENT argument, <i>gst-xmlinspect</i> will print information about that plug-in or element as an XML document.</p>
<h2>OPTIONS</h2>
<p> <i>gst-xmlinspect</i> accepts the following arguments and options:</p>
<dl>
<dt><code>PLUGIN</code></dt>
<dd> Name of a plugin</dd>
<dt><code>ELEMENT</code></dt>
<dd> Name of an element</dd>
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
<p> <code>gst-feedback</code>(1), <code>gst-inspect</code>(1), <code>gst-launch</code>(1), <code>gst-typefind</code>(1)</p>
<h2>AUTHOR</h2>
<p> The GStreamer team at <a rel="nofollow" href="http://gstreamer.freedesktop.org/">http://gstreamer.freedesktop.org/</a> </p>
