---
title: "libinput-measure-trackpoint-range(1)"
name: "libinput-measure-trackpoint-range"
section: "1"
letter: "l"
url: "/docs/linux/man/1-libinput-measure-trackpoint-range/"
description: "libinput-measure-trackpoint-range – measure the delta range of a trackpoint"
---

<h2 class="name">NAME</h2>
<p> libinput-measure-trackpoint-range &#8211; measure the delta range of a trackpoint </p>
<h2>SYNOPSIS</h2>
<p> <code>libinput measure trackpoint-range [&#8211;help] [/dev/input/event0]</code></p>
<h2>DESCRIPTION</h2>
<p> The <code>libinput measure trackpoint-range</code> tool measures the delta range of a trackpoint. This is an interactive tool. When executed, the tool will prompt the user to interact with the trackpoint. On termination, the tool prints a summary of the trackpoint deltas seen. This data should be attached to any bug report relating to the trackpoint&#8217;s speed. </p>
<p> This is a debugging tool only, its output may change at any time. Do not rely on the output. </p>
<p> This tool usually needs to be run as root to have access to the /dev/input/eventX nodes.</p>
<h2>OPTIONS</h2>
<p> If a device node is given, this tool opens that device node. Otherwise, this tool searches for the first node that looks like a trackpoint and uses that node.</p>
<dl>
<dt><code>&#8211;help</code></p>
<dd> Print help</dl>
<h2>LIBINPUT</h2>
<p> Part of the <code><a href="/docs/linux/man/1-libinput/">libinput</a>(1)</code> suite </p>
<h2>Index</h2>
