---
title: "gst-inspect-1-0(1)"
name: "gst-inspect-1-0"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gst-inspect-1-0/"
description: "gst-inspect-1.0 – print info about a GStreamer plugin or element"
---

<p>gst-inspect-1.0 &#8211; print info about a GStreamer plugin or element </p>
<h2>Synopsis</h2>
<p><code>gst-inspect-1.0 [OPTION&#8230;] [PLUGIN|ELEMENT]</code></p>
<h2>Description</h2>
<p><i>gst-inspect-1.0</i> is a tool that prints out information on available <i>GStreamer</i> plugins, information about a particular plugin, or information about a particular element. When executed with no PLUGIN or ELEMENT argument, <i>gst-inspect-1.0</i> will print a list of all plugins and elements together with a summary. When executed with a PLUGIN or ELEMENT argument, <i>gst-inspect-1.0</i> will print information about that plug-in or element.</p>
<h2>Options</h2>
<p><i>gst-inspect-1.0</i> accepts the following arguments and options:</p>
<dl>
<dt><code>PLUGIN</code></p>
<dd>Name of a plugin</p>
<dt><code>ELEMENT</code></p>
<dd>Name of an element</p>
<dt><code>&#8211;help</code></p>
<dd>Print help synopsis and available FLAGS</p>
<dt><code>&#8211;gst-info-mask=FLAGS</code></p>
<dd><i>GStreamer</i> info flags to set (list with &#8211;help)</p>
<dt><code>-a, &#8211;print-all</code></p>
<dd>Print all plugins and elements</p>
<dt><code>-b, &#8211;print-blacklist</code></p>
<dd>Print list of blacklisted files</p>
<dt><code>&#8211;plugin</code></p>
<dd>List the plugin contents</p>
<dt><code>&#8211;types=Element/Types</code></p>
<dd>Allow inspecting only elements that match all the element types filtered in this slash (&#8216;/&#8217;) separated list of element types. Those types correspond to what is also called &#8216;klass&#8217; which is a string describing the type of element, like &#8216;Decoder&#8217;, &#8216;Audio&#8217;, &#8216;Encoder&#8217; etc&#8230; This options implies that only elements will be printed (not typefind functions or tracers).</p>
<dt><code>&#8211;exists</code></p>
<dd>Check if the specified element or plugin exists</p>
<dt><code>&#8211;atleast-version</code></p>
<dd>When checking if an element or plugin exists, also check that its version is at least the version specified</p>
<dt><code>-u, &#8211;uri-handlers</code></p>
<dd>Print supported URI schemes, with the elements that implement them</p>
<dt><code>&#8211;no-colors</code></p>
<dd>Disable colors in output. You can also achieve the same by setting &#8216;GST_INSPECT_NO_COLORS&#8217; environment variable to any value.</p>
<dt><code>-C, &#8211;color</code></p>
<dd>Color output, even when not connected to a tty.</p>
<dt><code>&#8211;print-plugin-auto-install-info</code></p>
<dd>Print a machine-parsable list of features the specified plugin provides. Useful in connection with external automatic plugin installation mechanisms.</p>
<dt><code>&#8211;gst-debug-mask=FLAGS</code></p>
<dd><i>GStreamer</i> debugging flags to set (list with &#8211;help)</p>
<dt><code>&#8211;gst-mask=FLAGS</code></p>
<dd><i>GStreamer</i> info and debugging flags to set (list with &#8211;help)</p>
<dt><code>&#8211;gst-plugin-spew</code></p>
<dd><i>GStreamer</i> info flags to set Enable printout of errors while loading <i>GStreamer</i> plugins</p>
<dt><code>&#8211;gst-plugin-path=PATH</code></p>
<dd>Add directories separated with &#8216;:&#8217; to the plugin search path</dl>
<h2>Environment Variables</h2>
<p><i>gst-inspect-1.0</i> reads the following environment variables, in addition to the generic <i>GStreamer</i> environment variables also described in <code><a href="/docs/linux/man/1-gst-launch-1-0/">gst-launch-1.0</a></code>(1):</p>
<dl>
<dt><code>GST_LESS</code></p>
<dd>Override the options passed to <i>less</i> (by default &quot;RXF&quot;).<br />
 See <code><a href="/docs/linux/man/1-less/">less</a></code>(1) for more information.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-gst-launch-1-0/">gst-launch-1.0</a></code>(1), <code><a href="/docs/linux/man/1-gst-typefind-1-0/">gst-typefind-1.0</a></code>(1)</p>
<h2>Author</h2>
<p>The GStreamer team at <a rel="nofollow" href="http://gstreamer.freedesktop.org/">http://gstreamer.freedesktop.org/</a></p>
