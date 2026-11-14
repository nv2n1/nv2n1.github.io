---
title: "ts(5)"
name: "ts"
section: "5"
letter: "t"
url: "/docs/linux/man/5-ts/"
description: "ts.conf – Configuration file for tslib, controlling touch screens for embedded devices."
---

<p>ts.conf &#8211; Configuration file for tslib, controlling touch screens for embedded devices.</p>
<h2>Description</h2>
<p>The idea of tslib is to have a core library that provides standardised services, and a set of plugins to manage the conversion and filtering as needed. </p>
<p> The plugins for a particular touchscreen are loaded automatically by the library under the control of a static configuration file, /etc/ts.conf. /etc/ts.conf gives the library basic configuration information. Each line specifies one module, and the parameters for that module. The modules are loaded in order, with the first one processing the touchscreen data first. For example: </p>
<dl>
<dd>
<pre> module_raw input
 module variance delta=30
 module dejitter delta=100
 module linear</pre>
</dl>
<h2>Module Parameters</h2>
<p><code>variance</code></p>
<dl>
<dd>Tries to do it&#8217;s best in order to filter out random noise coming from touchscreen ADC&#8217;s. This is achieved by limiting the sample movement speed to some value (e.g. the pen is not supposed to move quicker than some threshold). </p>
<p> This is a &#8216;greedy&#8217; filter, e.g. it gives less samples on output than receives on input. </p>
<dl>
<dd>&bull; <code>Parameters:</code> <code>delta</code>. </p>
<p> Set the squared distance in touchscreen units between previous and current pen position (e.g. (X2-X1)^2 + (Y2-Y1)^2). This defines the criteria for determining whenever two samples are &#8216;near&#8217; or &#8216;far&#8217; to each other. </p>
<p> If the distance between previous and current sample is &#8216;far&#8217;, the sample is marked as &#8216;potential noise&#8217;. This doesn&#8217;t mean yet that it will be discarded; if the next reading will be close to it, this will be considered just a regular &#8216;quick motion&#8217; event, and it will sneak to the next layer. Also, if the sample after the &#8216;potential noise&#8217; is &#8216;far&#8217; from both previously discussed samples, this is also considered a &#8216;quick motion&#8217; event and the sample sneaks into the output stream.</dl>
</dl>
<p> <code>dejitter</code></p>
<dl>
<dd>Removes jitter on the X and Y co-ordinates. This is achieved by applying a weighted smoothing filter. The latest samples have most weight; earlier samples have less weight. This allows to achieve 1:1 input-&gt;output rate. </p>
<dl>
<dd>&bull; <code>Parameters:</code> <code>delta</code>. </p>
<p> Squared distance between two samples ((X2-X1)^2 + (Y2-Y1)^2) that defines the &#8216;quick motion&#8217; threshold. If the pen moves quick, it is not feasible to smooth pen motion, besides quick motion is not precise anyway; so if quick motion is detected the module just discards the backlog and simply copies input to output.</dl>
</dl>
<p> <code>linear</code></p>
<dl>
<dd>Linear scaling module, primarily used for conversion of touch screen co-ordinates to screen co-ordinates. </p>
<dl>
<dd>&bull; <code>Parameters:</code> <code>xyswap</code>. </p>
<p> Interchange the X and Y co-ordinates &#8212; no longer used or needed if the new linear calibration utility ts_calibrate is used.</dl>
</dl>
<h2>Environment Variables</h2>
<p>Latest versions of the Xorg tslib input driver use <code>hal</code> to configure the touchscreen within Xorg. Environment variables are only needed for the tslib commands. </p>
<p> <code>TSLIB_TSDEVICE</code></p>
<dl>
<dd>If the default touchscreen device cannot be found, set the <code>TSLIB_TSDEVICE</code> environment variable to the touchscreen device to use. </p>
<p> Default: /dev/input/event0</dl>
<p> <code>TSLIB_CONSOLEDEVICE</code></p>
<dl>
<dd>Tslib default console device. </p>
<p> Default: /dev/tty</dl>
<p> <code>TSLIB_CALIBFILE </code></p>
<dl>
<dd>Stores calibration data obtained using ts_calibrate. </p>
<p> Default: /etc/pointercal</dl>
<p> <code>TSLIB_CONFFILE</code></p>
<dl>
<dd>Set a different location for the ts.conf configuration file itself. </p>
<p> Default; /etc/ts.conf.</dl>
<p> <code>TSLIB_FBDEVICE</code></p>
<dl>
<dd>Framebuffer device to use for the touchscreen support. </p>
<p> Default: /dev/fb0.</dl>
<p> <code>TSLIB_PLUGINDIR</code></p>
<dl>
<dd>Plugin directory for tslib. </p>
<p> Default: /usr/lib/$triplet/ts0/ where triplet is the MultiArch path, e.g. arm-linux-gnueabi.</dl>
<h2>Author</h2>
<p>This manual page was written by Neil Williams codehelp [at] debian.org for the Debian(TM) distribution because the original program does not have a manual page, but may be used by others. Permission is granted to copy, distribute and/or modify this document under the terms of the GNU General Public License, Version 2 any later version published by the Free Software Foundation. </p>
<p> On Debian systems, the complete text of the GNU General Public License can be found in /usr/share/common-licenses/GPL.</p>
<h2>Author</h2>
<p><code>Russell King</code></p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
<p>Copyright &#169; 2008 Neil Williams</p>
