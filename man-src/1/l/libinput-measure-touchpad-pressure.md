---
title: "libinput-measure-touchpad-pressure(1)"
name: "libinput-measure-touchpad-pressure"
section: "1"
letter: "l"
url: "/docs/linux/man/1-libinput-measure-touchpad-pressure/"
description: "libinput-measure-touchpad-pressure – measure pressure properties of devices"
---

<h2 class="name">NAME</h2>
<p> libinput-measure-touchpad-pressure &#8211; measure pressure properties of devices </p>
<h2>SYNOPSIS</h2>
<p> <code>libinput measure touchpad-pressure [&#8211;help] [options]</code> [<i>/dev/input/event0] </i></p>
<h2>DESCRIPTION</h2>
<p> The <code>libinput measure touchpad-pressure</code> tool measures the pressure of touches on a touchpad. This is an interactive tool. When executed, the tool will prompt the user to interact with the touchpad. On termination, the tool prints a summary of the pressure values seen. This data should be attached to any pressure-related bug report. </p>
<p> For a full description on how libinput&#8217;s pressure-to-click behavior works, see the online documentation here: <i><a rel="nofollow" href="https://wayland.freedesktop.org/libinput/doc/latest/touchpad_pressure.html">https://wayland.freedesktop.org/libinput/doc/latest/touchpad_pressure.html</a></i> and <i><a rel="nofollow" href="https://wayland.freedesktop.org/libinput/doc/latest/palm_detection.html">https://wayland.freedesktop.org/libinput/doc/latest/palm_detection.html</a></i> </p>
<p> This is a debugging tool only, its output may change at any time. Do not rely on the output. </p>
<p> This tool usually needs to be run as root to have access to the /dev/input/eventX nodes.</p>
<h2>OPTIONS</h2>
<p> If a device node is given, this tool opens that device node. Otherwise, this tool searches for the first node that looks like a touchpad and uses that node.</p>
<dl>
<dt><code>&#8211;help</code></p>
<dd> Print help</p>
<dt><code>&#8211;touch-thresholds=</code><i>down:up</i></p>
<dd> Set the logical touch pressure thresholds to <i>down</i> and <i>up,</i> respectively. When a touch exceeds the pressure in <i>down</i> it is considered logically down. If a touch is logically down and goes below the pressure in <i>up,</i> it is considered logically up. The thresholds have to be in device-specific pressure values and it is required that <i>down</i> &gt;= <i>up.</i></p>
<dt><code>&#8211;palm-threshold=</code><i>N</i></p>
<dd> Assume a palm threshold of <i>N.</i> The threshold has to be in device-specific pressure values.</dl>
<p> If the touch-thresholds or the palm-threshold are not provided, this tool uses the thresholds provided by the device quirks (if any) or the built-in defaults.</p>
<h2>LIBINPUT</h2>
<p> Part of the <code><a href="/docs/linux/man/1-libinput/">libinput</a>(1)</code> suite </p>
<h2>Index</h2>
