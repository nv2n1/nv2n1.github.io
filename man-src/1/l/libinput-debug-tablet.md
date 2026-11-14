---
title: "libinput-debug-tablet(1)"
name: "libinput-debug-tablet"
section: "1"
letter: "l"
url: "/docs/linux/man/1-libinput-debug-tablet/"
description: "libinput-debug-tablet – debug and visualize tablet axes"
---

<h2 class="name">NAME</h2>
<p> libinput-debug-tablet &#8211; debug and visualize tablet axes </p>
<h2>SYNOPSIS</h2>
<p> <code>libinput debug-tablet [&#8211;help] [options] [</code><i>/dev/input/event0]</i></p>
<h2>DESCRIPTION</h2>
<p> The <code>libinput debug-tablet</code> tool debugs the values of the various axes on a tablet. This is an interactive tool. When executed, the tool will prompt the user to interact with the tablet and display the current value on each available axis. </p>
<p> This is a debugging tool only, its output may change at any time. Do not rely on the output. </p>
<p> This tool usually needs to be run as root to have access to the /dev/input/eventX nodes.</p>
<h2>OPTIONS</h2>
<p> If a device node is given, this tool opens that device node. Otherwise, this tool searches for the first node that looks like a tablet and uses that node.</p>
<dl>
<dt><code>&#8211;help</code></p>
<dd> Print help</dl>
<p> Events shown by this tool may not correspond to the events seen by a different user of libinput. This tool initializes a separate context.</p>
<h2>LIBINPUT</h2>
<p> Part of the <code><a href="/docs/linux/man/1-libinput/">libinput</a>(1)</code> suite </p>
<h2>Index</h2>
