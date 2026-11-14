---
title: "libinput-measure-fuzz(1)"
name: "libinput-measure-fuzz"
section: "1"
letter: "l"
url: "/docs/linux/man/1-libinput-measure-fuzz/"
description: "libinput-measure-fuzz – measure absolute axis fuzz"
---

<h2 class="name">NAME</h2>
<p> libinput-measure-fuzz &#8211; measure absolute axis fuzz </p>
<h2>SYNOPSIS</h2>
<p> <code>libinput measure fuzz [&#8211;help] [options]</code> [<i>/dev/input/event0] </i></p>
<h2>DESCRIPTION</h2>
<p> The <code>libinput measure fuzz</code> tool measures the fuzz for an absolute axis on a kernel device. The current implementation does not actually measure anything, it only prints the relevant information available and suggests a udev rule. </p>
<p> This is a debugging tool only, its output may change at any time. Do not rely on the output. </p>
<p> This tool usually needs to be run as root to have access to the /dev/input/eventX nodes.</p>
<h2>OPTIONS</h2>
<p> If a device node is given, this tool opens that device node. Otherwise, this tool searches for the first node that looks like a touchpad device and uses that node.</p>
<dl>
<dt><code>&#8211;help</code></p>
<dd> Print help</dl>
<h2>LIBINPUT</h2>
<p> Part of the <code><a href="/docs/linux/man/1-libinput/">libinput</a>(1)</code> suite </p>
<h2>Index</h2>
