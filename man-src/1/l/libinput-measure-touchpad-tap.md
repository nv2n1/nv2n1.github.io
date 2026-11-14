---
title: "libinput-measure-touchpad-tap(1)"
name: "libinput-measure-touchpad-tap"
section: "1"
letter: "l"
url: "/docs/linux/man/1-libinput-measure-touchpad-tap/"
description: "libinput-measure-touchpad-tap – measure tap-to-click properties of devices"
---

<h2 class="name">NAME</h2>
<p> libinput-measure-touchpad-tap &#8211; measure tap-to-click properties of devices </p>
<h2>SYNOPSIS</h2>
<p> <code>libinput measure touchpad-tap [&#8211;help] [&#8211;format=</code><i>&lt;format&gt;</i><code>] </code><i>[/dev/input/event0]</i></p>
<h2>DESCRIPTION</h2>
<p> The <code>libinput measure touchpad-tap</code> tool measures properties of the tap-to-click behavior of the user. This is an interactive tool. When executed, the tool will prompt the user to interact with the touchpad. On termination, the tool prints a summary of the tap interactions seen. This data should be attached to any tap-related bug report. </p>
<p> For a full description on how libinput&#8217;s tap-to-click behavior works, see the online documentation here: <i><a rel="nofollow" href="https://wayland.freedesktop.org/libinput/doc/latest/tapping.html">https://wayland.freedesktop.org/libinput/doc/latest/tapping.html</a></i> </p>
<p> This is a debugging tool only, its output may change at any time. Do not rely on the output. </p>
<p> This tool usually needs to be run as root to have access to the /dev/input/eventX nodes.</p>
<h2>OPTIONS</h2>
<p> If a device node is given, this tool opens that device node. Otherwise, this tool searches for the first node that looks like a touchpad and uses that node.</p>
<dl>
<dt><code>&#8211;help</code></p>
<dd> Print help</p>
<dt><code>&#8211;format=summary|dat</code></p>
<dd> Specify the data format to be printed. The default (or if <code>&#8211;format</code> is omitted) is &quot;summary&quot;. See section <code>DATA FORMATS</code> </p>
</dl>
<h2>DATA FORMATS</h2>
<p> This section describes the data formats printed with the <code>&#8211;format</code> commandline argument. Note that any of the output may change at any time. </p>
<p> summary</p>
<dl>
<dt>
<dd> The <i>summary</i> format prints a summary of the data collected. This format is useful to get a quick overview of a user&#8217;s tapping behavior and why some taps may or may not be detected.</dl>
<p> dat</p>
<dl>
<dt>
<dd> The <i>dat</i> format prints the touch sequence data (raw and processed) in column-style format, suitable for processing by other tools such as <code><a href="/docs/linux/man/1-gnuplot/">gnuplot</a>(1).</code> The data is aligned in one row per touch with each column containing a separate data entry. <code>libinput-measure-touchpad-tap</code> prints comments at the top of the file to describe each column. </p>
<p> <code>WARNING:</code> The data contained in the output is grouped by different sort orders. For example, the first few columns may list tap information in the &#8216;natural&#8217; sort order (i.e. as they occured), the data in the next few columns may list tap information sorted by the delta time between touch down and touch up. Comparing columns across these group boundaries will compare data of two different touch points and result in invalid analysis.</dl>
<h2>BUGS</h2>
<p> This tool does not take finger pressure into account. The tap it detects may be different to those detected by libinput if libinput&#8217;s pressure thresholds differ significantly to the kernel&#8217;s pressure thresholds.</p>
<h2>LIBINPUT</h2>
<p> Part of the <code><a href="/docs/linux/man/1-libinput/">libinput</a>(1)</code> suite </p>
<h2>Index</h2>
