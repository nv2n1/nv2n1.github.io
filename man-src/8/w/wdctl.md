---
title: "wdctl(8)"
name: "wdctl"
section: "8"
letter: "w"
url: "/docs/linux/man/8-wdctl/"
description: "wdctl – show hardware watchdog status"
---

<p>wdctl &#8211; show hardware watchdog status</p>
<h2>Synopsis</h2>
<p><code>wdctl</code> [options] [<i>device</i>&#8230;]</p>
<h2>Description</h2>
<p>Show hardware watchdog status. The default device is <i>/dev/watchdog</i>. If more than one device is specified then the output is separated by one blank line. </p>
<p> If the device is already used or user has no permissions to read from the device, then <code>wdctl</code> reads data from sysfs. In this case information about supported features (flags) might be missing. </p>
<p> Note that the number of supported watchdog features is hardware specific.</p>
<h2>Options</h2>
<p><code>-f</code>, <code>&#8211;flags</code> <i>list</i></p>
<dl>
<dd>Print only the specified flags.</dl>
<p> <code>-F</code>, <code>&#8211;noflags</code></p>
<dl>
<dd>Do not print information about flags.</dl>
<p> <code>-I</code>, <code>&#8211;noident</code></p>
<dl>
<dd>Do not print watchdog identity information.</dl>
<p> <code>-n</code>, <code>&#8211;noheadings</code></p>
<dl>
<dd>Do not print a header line for flags table.</dl>
<p> <code>-o</code>, <code>&#8211;output</code> <i>list</i></p>
<dl>
<dd>Define the output columns to use in table of watchdog flags. If no output arrangement is specified, then a default set is used. Use <code>&#8211;help</code> to get list of all supported columns.</dl>
<p> <code>-O</code>, <code>&#8211;oneline</code></p>
<dl>
<dd>Print all wanted information on one line in key=&quot;value&quot; output format.</dl>
<p> <code>-r</code>, <code>&#8211;raw</code></p>
<dl>
<dd>Use the raw output format.</dl>
<p> <code>-s</code>, <code>-settimeout</code> <i>seconds</i></p>
<dl>
<dd>Set the watchdog timeout in seconds.</dl>
<p> <code>-T</code>, <code>&#8211;notimeouts</code></p>
<dl>
<dd>Do not print watchdog timeouts.</dl>
<p> <code>-x</code>, <code>&#8211;flags-only</code></p>
<dl>
<dd>Same as <code>-I -T</code>.</dl>
<p> <code>-V</code>, <code>&#8211;version</code></p>
<dl>
<dd>Display version information and exit.</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dd>Display help text and exit.</dl>
<h2>Authors</h2>
<h2>Reporting Bugs</h2>
<p>For bug reports, use the issue tracker at <i></i> &lt;<a rel="nofollow" href="https://github.com/karelzak/util-linux/issues">https://github.com/karelzak/util-linux/issues</a>&gt;.</p>
<h2>Availability</h2>
<p>The <code>wdctl</code> command is part of the util-linux package which can be downloaded from <i>Linux Kernel Archive</i> &lt;<a rel="nofollow" href="https://www.kernel.org/pub/linux/utils/util-linux/">https://www.kernel.org/pub/linux/utils/util-linux/</a>&gt;.</p>
