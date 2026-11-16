---
title: "libinput(1)"
name: "libinput"
section: "1"
letter: "l"
url: "/docs/linux/man/1-libinput/"
description: "libinput – tool to interface with libinput"
---

<h2 class="name">NAME</h2>
<p> libinput &#8211; tool to interface with libinput </p>
<h2>SYNOPSIS</h2>
<p> <code>libinput [&#8211;help|&#8211;version] </code><i>&lt;command&gt;</i> <i>[&lt;args&gt;]</i></p>
<h2>DESCRIPTION</h2>
<p> libinput is a library to handle input devices and provides device detection and input device event processing for most Wayland compositors and the X.Org xf86-input-libinput driver. </p>
<p> The <code>libinput</code> tools are a set of tools to debug, interface with and analyze data for libinput. These tools create libinput contexts separate from that of the compositor/X server and cannot change settings in a running session. See section <code>COMMANDS</code> for a list of available commands. </p>
<p> libinput&#8217;s API documentation and details on features and various high-level concepts are available online at <i><a rel="nofollow" href="https://wayland.freedesktop.org/libinput/doc/latest/">https://wayland.freedesktop.org/libinput/doc/latest/</a></i> </p>
<p> The man page for the X.Org xf86-input-libinput driver is <code><a href="/docs/linux/man/4-libinput/">libinput</a>(4).</code></p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;help</code></dt>
<dd> Print help and exit</dd>
<dt><code>&#8211;version</code></dt>
<dd> Print the version and exit</dd></dl>
<h2>COMMANDS</h2>
<dl>
<dt><code><a href="/docs/linux/man/1-libinput-debug-events/">libinput-debug-events</a>(1)</code></dt>
<dd> Print all events as seen by libinput</dd>
<dt><code>libinput-debug-gui(1)</code></dt>
<dd> Show a GUI to visualize libinput&#8217;s events</dd>
<dt><code><a href="/docs/linux/man/1-libinput-debug-tablet/">libinput-debug-tablet</a>(1)</code></dt>
<dd> A commandline tool to debug tablet axis values</dd>
<dt><code><a href="/docs/linux/man/1-libinput-list-devices/">libinput-list-devices</a>(1)</code></dt>
<dd> List all devices recognized by libinput</dd>
<dt><code><a href="/docs/linux/man/1-libinput-measure/">libinput-measure</a>(1)</code></dt>
<dd> Measure various properties of devices</dd>
<dt><code><a href="/docs/linux/man/1-libinput-record/">libinput-record</a>(1)</code></dt>
<dd> Record the events from a device</dd>
<dt><code><a href="/docs/linux/man/1-libinput-replay/">libinput-replay</a>(1)</code></dt>
<dd> Replay the events from a device</dd></dl>
<h2>LIBINPUT</h2>
<p> Part of the <code><a href="/docs/linux/man/1-libinput/">libinput</a>(1)</code> suite </p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/4-libinput/">libinput</a>(4) </p>
<p> libinput&#8217;s online documentation <i><a rel="nofollow" href="https://wayland.freedesktop.org/libinput/doc/latest/">https://wayland.freedesktop.org/libinput/doc/latest/</a></i> </p>
<h2>Index</h2>
