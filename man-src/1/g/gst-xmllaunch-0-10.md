---
title: "gst-xmllaunch-0-10(1)"
name: "gst-xmllaunch-0-10"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gst-xmllaunch-0-10/"
description: "gst-xmllaunch – build and run a GStreamer pipeline from an XML serialization"
---

<p>gst-xmllaunch &#8211; build and run a GStreamer pipeline from an XML serialization</p>
<h2>Synopsis</h2>
<p><code>gst-xmllaunch</code> <i>[OPTION&#8230;]</i> XML-FILE [ ELEMENT.PROPERTY=VALUE &#8230; ]</p>
<h2>Description</h2>
<p><i>gst-xmllaunch</i> is a tool that is used to build and run a basic <i>GStreamer</i> pipeline, loading it from an XML description. You can produce the XML description using <a href="/docs/linux/man/1-gst-launch-0-10/">gst-launch-0.10</a>(1) with the -o option or by calling gst_xml_write_file() in your own app. </p>
<p> A simple commandline looks like: </p>
<p>&nbsp;<wbr>gst-xmllaunch my-pipeline.xml filesrc0.location=music.mp3 </p>
<p> This sets the location property of the element named filesrc0 to the value &quot;music.mp3&quot;. See <a href="/docs/linux/man/1-gst-launch/">gst-launch</a>(1) for syntax on setting element names, and gst-inspect to see what properties various elements have. </p>
<p> You can pass &quot;-&quot; as the XML-FILE to read from stdin. </p>
<p> XML-FILE can be a URI as well, thanks to the wizardry of libxml. I&#8217;m not really sure what all is supported, it seems http works just fine though. </p>
<h2>Warning</h2>
<p><i>gst-xmllaunch</i> is deprecated and broken for all but the most simple pipelines. It will most likely be removed in future. Don&#8217;t use it.</p>
<h2>Options</h2>
<p><i>gst-xmllaunch</i> accepts the following options:</p>
<dl>
<dt><code>&#8211;help</code></p>
<dd>Print help synopsis and available FLAGS</p>
<dt><code>&#8211;silent</code></p>
<dd>Do not output status information</p>
<dt><code>&#8211;exclude=TYPE, -XTYPE</code></p>
<dd>Do not output status information of TYPE</p>
<dt><code>&#8211;output=FILE, -oFILE</code></p>
<dd>Save XML representation of pipeline to FILE and exit</p>
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
<p><code><a href="/docs/linux/man/1-gst-feedback/">gst-feedback</a></code>(1), <code><a href="/docs/linux/man/1-gst-inspect/">gst-inspect</a></code>(1), <code><a href="/docs/linux/man/1-gst-launch/">gst-launch</a></code>(1), <code><a href="/docs/linux/man/1-gst-typefind/">gst-typefind</a></code>(1)</p>
<h2>Author</h2>
<p>The GStreamer team at <a rel="nofollow" href="http://gstreamer.freedesktop.org/">http://gstreamer.freedesktop.org/</a></p>
