---
title: "intel_panel_fitter(1)"
name: "intel_panel_fitter"
section: "1"
letter: "i"
url: "/docs/linux/man/1-intel_panel_fitter/"
description: "intel_panel_fitter – Change the panel fitter settings"
---

<h2>NAME</h2>
<p> intel_panel_fitter &#8211; Change the panel fitter settings</p>
<h2>SYNOPSIS</h2>
<p> <code>intel_panel_fitter [options]</code></p>
<h2>DESCRIPTION</h2>
<p> <code>intel_panel_fitter</code> is a tool that allows you to change the panel fitter settings, so you can change the size of the screen being displayed on your monitor without changing the real pixel size of your desktop. The biggest use case for this tool is to work around overscan done by TVs and some monitors in interlaced mode.</p>
<h3>Options</h3>
<dl>
<dt><code>-p [pipe]</code></p>
<dd> pipe to be used (A, B or C, but C is only present on Ivy Bridge and newer).</p>
<dt><code>-x [value]</code></p>
<dd> final screen width size in pixels (needs -p option).</p>
<dt><code>-y [value]</code></p>
<dd> final screen height size in pixels (needs -p option).</p>
<dt><code>-d</code></p>
<dd> disable panel fitter (needs -p option, ignores -x and -y options).</p>
<dt><code>-l</code></p>
<dd> list current state of each pipe.</p>
<dt><code>-h</code></p>
<dd> prints the help message.</dl>
<h3></h3>
<h2>EXAMPLES</h2>
<dl>
<dt><code>intel_panel_fitter -l</code></p>
<dd> will list the current status of each pipe, so you can decide what to do.</p>
<dt><code>intel_panel_fitter -p A -x 1850 -y 1040</code></p>
<dd> will change the pipe A size to 1850&#215;1040 pixels.</p>
<dt><code>intel_panel_fitter -p A -d</code></p>
<dd> will disable the panel fitter for pipe A. </p>
</dl>
<h2>NOTES</h2>
<p> In the future, there will be support for this feature inside the Linux Kernel. </p>
<p> Machines older than Ironlake are still not supported, but support may be possible to implement. </p>
<h2>Index</h2>
<dt><a href="#lbAG">EXAMPLES</a></p>
<dd>
<dt><a href="#lbAH">NOTES</a></p>
<dd></dl>
