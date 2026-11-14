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
<dt><code>&#8211;help</code></p>
<dd> Print help and exit</p>
<dt><code>&#8211;version</code></p>
<dd> Print the version and exit</dl>
<h2>COMMANDS</h2>
<dl>
<dt><code><a href="/docs/linux/man/1-libinput-debug-events/">libinput-debug-events</a>(1)</code></p>
<dd> Print all events as seen by libinput</p>
<dt><code><a href="/docs/linux/man/1-libinput-debug-gui/">libinput-debug-gui</a>(1)</code></p>
<dd> Show a GUI to visualize libinput&#8217;s events</p>
<dt><code><a href="/docs/linux/man/1-libinput-debug-tablet/">libinput-debug-tablet</a>(1)</code></p>
<dd> A commandline tool to debug tablet axis values</p>
<dt><code><a href="/docs/linux/man/1-libinput-list-devices/">libinput-list-devices</a>(1)</code></p>
<dd> List all devices recognized by libinput</p>
<dt><code><a href="/docs/linux/man/1-libinput-measure/">libinput-measure</a>(1)</code></p>
<dd> Measure various properties of devices</p>
<dt><code><a href="/docs/linux/man/1-libinput-record/">libinput-record</a>(1)</code></p>
<dd> Record the events from a device</p>
<dt><code><a href="/docs/linux/man/1-libinput-replay/">libinput-replay</a>(1)</code></p>
<dd> Replay the events from a device</dl>
<h2>LIBINPUT</h2>
<p> Part of the <code><a href="/docs/linux/man/1-libinput/">libinput</a>(1)</code> suite </p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/4-libinput/">libinput</a>(4) </p>
<p> libinput&#8217;s online documentation <i><a rel="nofollow" href="https://wayland.freedesktop.org/libinput/doc/latest/">https://wayland.freedesktop.org/libinput/doc/latest/</a></i> </p>
<h2>Index</h2>
