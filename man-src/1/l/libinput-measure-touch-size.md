---
title: "libinput-measure-touch-size(1)"
name: "libinput-measure-touch-size"
section: "1"
letter: "l"
url: "/docs/linux/man/1-libinput-measure-touch-size/"
description: "libinput-measure-touch-size – measure touch size and orientation of devices"
---

<h2 class="name">NAME</h2>
<p> libinput-measure-touch-size &#8211; measure touch size and orientation of devices </p>
<h2>SYNOPSIS</h2>
<p> <code>libinput measure touch-size [&#8211;help] [options]</code> [<i>/dev/input/event0] </i></p>
<h2>DESCRIPTION</h2>
<p> The <code>libinput measure touch-size</code> tool measures the size and orientation of a touch as provided by the kernel. This is an interactive tool. When executed, the tool will prompt the user to interact with the touch device. On termination, the tool prints a summary of the values seen. This data should be attached to any touch-size-related bug report. </p>
<p> This is a debugging tool only, its output may change at any time. Do not rely on the output. </p>
<p> This tool usually needs to be run as root to have access to the /dev/input/eventX nodes.</p>
<h2>OPTIONS</h2>
<p> If a device node is given, this tool opens that device node. Otherwise, this tool searches for the first node that looks like a touch-capable device and uses that node.</p>
<dl>
<dt><code>&#8211;help</code></p>
<dd> Print help</p>
<dt><code>&#8211;touch-thresholds=</code><i>down:up</i></p>
<dd> Set the logical touch size thresholds to <i>down</i> and <i>up,</i> respectively. When a touch exceeds the size in <i>down</i> it is considered logically down. If a touch is logically down and goes below the size in <i>up,</i> it is considered logically up. The thresholds have to be in device-specific pressure values and it is required that <i>down</i> &gt;= <i>up.</i></p>
<dt><code>&#8211;palm-threshold=</code><i>N</i></p>
<dd> Assume a palm threshold of <i>N.</i> The threshold has to be in device-specific pressure values.</dl>
<p> If the touch-thresholds or the palm-threshold are not provided, this tool uses the thresholds provided by the device quirks (if any) or the built-in defaults.</p>
<h2>LIBINPUT</h2>
<p> Part of the <code><a href="/docs/linux/man/1-libinput/">libinput</a>(1)</code> suite </p>
<h2>Index</h2>
