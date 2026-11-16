---
title: "gst-device-monitor-1-0(1)"
name: "gst-device-monitor-1-0"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gst-device-monitor-1-0/"
description: "gst-device-monitor-1.0 – Simple command line testing tool for GStreamer device monitors"
---

<p>gst-device-monitor-1.0 &#8211; Simple command line testing tool for GStreamer device monitors </p>
<h2>Synopsis</h2>
<p><code>gst-device-monitor-1.0</code> <i>[DEVICE_CLASSES[:FILTER_CAPS]] [DEVICE_CLASSES[:FILTER_CAPS]]</i></p>
<h2>Description</h2>
<p><i>gst-device-monitor-1.0</i> is a command line tool that can be used to test GStreamer&#8217;s device monitoring functionality. By default it will just print a list of all devices found and exit, but you can also make it wait around for more devices by passing the &#8211;follow option. You can also pass it one or more filter arguments to filter the kind of devices you are interested in. </p>
<h2>Options</h2>
<p><i>gst-device-monitor-1.0</i> accepts the following options:</p>
<dl>
<dt><code>&#8211;help</code></dt>
<dd>Print help synopsis and available command line options</dd>
<dt><code>&#8211;version</code></dt>
<dd>Print version and exit</dd>
<dt><code>-f, &#8211;follow</code></dt>
<dd>Don&#8217;t exit after showing the initial device list, but wait for devices to be added or removed</dd>
<dt><code>-i, &#8211;include-hidden</code></dt>
<dd>Include devices from hidden device providers. </dd>
</dl>
<h2>Examples</h2>
<p><code>gst-device-monitor-1.0</code></p>
<dl>
<dt><code>gst-device-monitor-1.0 &#8211;follow</code></dt>
<dd>
</dd><dt><code>gst-device-monitor-1.0 Audio/Source</code></dt>
<dd>
</dd><dt><code>gst-device-monitor-1.0 Video/Source:video/x-raw</code></dt>
<dd>
</dd><dt><code>gst-device-monitor-1.0 -i Audio/Sink</code></dt>
<dd></dd></dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-gst-inspect-1-0/">gst-inspect-1.0</a></code>(1), <code><a href="/docs/linux/man/1-gst-launch-1-0/">gst-launch-1.0</a></code>(1), <code><a href="/docs/linux/man/1-gst-discoverer-1-0/">gst-discoverer-1.0</a></code>(1), <code><a href="/docs/linux/man/1-gst-play-1-0/">gst-play-1.0</a></code>(1),</p>
<h2>Author</h2>
<p>The GStreamer team at <a rel="nofollow" href="http://gstreamer.freedesktop.org/">http://gstreamer.freedesktop.org/</a></p>
