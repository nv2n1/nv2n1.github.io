---
title: "libinput-measure(1)"
name: "libinput-measure"
section: "1"
letter: "l"
url: "/docs/linux/man/1-libinput-measure/"
description: "libinput-measure – measure properties of devices"
---

<h2 class="name">NAME</h2>
<p> libinput-measure &#8211; measure properties of devices </p>
<h2>SYNOPSIS</h2>
<p> <code>libinput measure [&#8211;help] </code><i>&lt;feature&gt; [&lt;args&gt;]</i></p>
<h2>DESCRIPTION</h2>
<p> The <code>libinput measure</code> tool measures properties of one (or more) devices. Depending on what is to be measured, this too may not create a libinput context. </p>
<p> This is a debugging tool only, its output may change at any time. Do not rely on the output. </p>
<p> This tool usually needs to be run as root to have access to the /dev/input/eventX nodes.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;help</code></p>
<dd> Print help</dl>
<h2>FEATURES</h2>
<p> Features that can be measured include</p>
<dl>
<dt><code><a href="/docs/linux/man/1-libinput-measure-fuzz/">libinput-measure-fuzz</a>(1)</code></p>
<dd> Measure touch fuzz to avoid pointer jitter</p>
<dt><code><a href="/docs/linux/man/1-libinput-measure-touch-size/">libinput-measure-touch-size</a>(1)</code></p>
<dd> Measure touch size and orientation</p>
<dt><code><a href="/docs/linux/man/1-libinput-measure-touchpad-tap/">libinput-measure-touchpad-tap</a>(1)</code></p>
<dd> Measure tap-to-click time</p>
<dt><code><a href="/docs/linux/man/1-libinput-measure-touchpad-pressure/">libinput-measure-touchpad-pressure</a>(1)</code></p>
<dd> Measure touch pressure</dl>
<h2>LIBINPUT</h2>
<p> Part of the <code><a href="/docs/linux/man/1-libinput/">libinput</a>(1)</code> suite </p>
<h2>Index</h2>
