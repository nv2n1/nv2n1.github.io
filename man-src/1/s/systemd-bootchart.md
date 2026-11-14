---
title: "systemd-bootchart(1)"
name: "systemd-bootchart"
section: "1"
letter: "s"
url: "/docs/linux/man/1-systemd-bootchart/"
description: "systemd-bootchart – Boot performance graphing tool"
---

<h2 class="name">NAME</h2>
<p> systemd-bootchart &#8211; Boot performance graphing tool </p>
<h2>DESCRIPTION</h2>
<p> <code>systemd-bootchart</code> is a tool, usually run at system startup, that collects the CPU load, disk load, memory usage, as well as per-process information from a running system. Collected results are output as an SVG graph. Normally, systemd-bootchart is invoked by the kernel by passing <code>init=</code><code>/usr/lib/systemd/systemd-bootchart</code> on the kernel command line. systemd-bootchart will then fork the real init off to resume normal system startup, while monitoring and logging startup information in the background. </p>
<p> After collecting a certain amount of data (usually 15-30 seconds, default 20 s) the logging stops and a graph is generated from the logged information. This graph contains vital clues as to which resources are being used, in which order, and where possible problems exist in the startup sequence of the system. It is essentially a more detailed version of the <code>systemd-analyze plot</code> function. </p>
<p> Of course, bootchart can also be used at any moment in time to collect and graph some data for an amount of time. It is recommended to use the <code>&#8211;rel</code> switch in this case. </p>
<p> Bootchart does not require root privileges, and will happily run as a normal user. </p>
<p> Bootchart graphs are by default written time-stamped in /run/log and saved to the journal with <i>MESSAGE_ID=9f26aa562cf440c2b16c773d0479b518</i>. Journal field <i>BOOTCHART=</i> contains the bootchart in SVG format.</p>
<h2>INVOCATION</h2>
<p> <code>systemd-bootchart</code> can be invoked in several different ways: </p>
<p> <i>Kernel invocation</i></p>
<dl>
<dt>
<dd> The kernel can invoke <code>systemd-bootchart</code> instead of the init process. In turn, <code>systemd-bootchart</code> will invoke <code>/usr/lib/systemd/systemd</code>.</dl>
<p> <i>Started as a standalone program</i></p>
<dl>
<dt>
<dd> One can execute <code>systemd-bootchart</code> as normal application from the command line. In this mode it is highly recommended to pass the <code>-r</code> flag in order to not graph the time elapsed since boot and before systemd-bootchart was started, as it may result in extremely large graphs. The time elapsed since boot might also include any time that the system was suspended.</dl>
<h2>OPTIONS</h2>
<p> These options can also be set in the /etc/systemd/bootchart.conf file. See <code><a href="/docs/linux/man/5-bootchart-conf/">bootchart.conf</a></code>(5). </p>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Print a short help text and exit.</dl>
<p> <code>-n</code>, <code>&#8211;sample </code><i>N</i></p>
<dl>
<dt>
<dd> Specify the number of samples, <i>N</i>, to record. Samples will be recorded at intervals defined with <code>&#8211;freq</code>.</dl>
<p> <code>-f</code>, <code>&#8211;freq </code><i>f</i></p>
<dl>
<dt>
<dd> Specify the sample log frequency, a positive real <i>f</i>, in Hz. Most systems can cope with values up to 25-50 without creating too much overhead.</dl>
<p> <code>-r</code>, <code>&#8211;rel</code></p>
<dl>
<dt>
<dd> Use relative times instead of absolute times. This is useful for using bootchart at post-boot time to profile an already booted system. Without this option the graph would become extremely large. If set, the horizontal axis starts at the first recorded sample instead of time 0.0.</dl>
<p> <code>-F</code>, <code>&#8211;no-filter</code></p>
<dl>
<dt>
<dd> Disable filtering of tasks that did not contribute significantly to the boot. Processes that are too short-lived (only seen in one sample) or that do not consume any significant CPU time (less than 0.001 s) will not be displayed in the output graph.</dl>
<p> <code>-C</code>, <code>&#8211;cmdline</code></p>
<dl>
<dt>
<dd> Display the full command line with arguments of processes, instead of only the process name.</dl>
<p> <code>-g</code>, <code>&#8211;control-group</code></p>
<dl>
<dt>
<dd> Display process control group</dl>
<p> <code>-o</code>, <code>&#8211;output </code><i>path</i></p>
<dl>
<dt>
<dd> Specify the output directory for the graphs. By default, bootchart writes the graphs to /run/log.</dl>
<p> <code>-i</code>, <code>&#8211;init </code><i>path</i></p>
<dl>
<dt>
<dd> Use this init binary. Defaults to <code>/usr/lib/systemd/systemd</code>.</dl>
<p> <code>-p</code>, <code>&#8211;pss</code></p>
<dl>
<dt>
<dd> Enable logging and graphing of processes&#8217; PSS (Proportional Set Size) memory consumption. See filesystems/proc.txt in the kernel documentation for an explanation of this field.</dl>
<p> <code>-e</code>, <code>&#8211;entropy</code></p>
<dl>
<dt>
<dd> Enable logging and graphing of the kernel random entropy pool size.</dl>
<p> <code>-x</code>, <code>&#8211;scale-x </code><i>N</i></p>
<dl>
<dt>
<dd> Horizontal scaling factor for all variable graph components.</dl>
<p> <code>-y</code>, <code>&#8211;scale-y </code><i>N</i></p>
<dl>
<dt>
<dd> Vertical scaling factor for all variable graph components.</dl>
<h2>OUTPUT</h2>
<p> <code>systemd-bootchart</code> generates SVG graphs. In order to render those on a graphical display any SVG capable viewer can be used. It should be noted that the SVG render engines in most browsers (including Chrome and Firefox) are many times faster than dedicated graphical applications like Gimp and Inkscape. Just point your browser at m[blue]<code>file:///run/log/</code>m[]!</p>
<h2>HISTORY</h2>
<p> This version of bootchart was implemented from scratch, but is inspired by former bootchart incantations: </p>
<p> <i>Original bash</i></p>
<dl>
<dt>
<dd> The original bash/shell code implemented bootchart. This version created a compressed tarball for processing with external applications. This version did not graph anything, only generated data.</dl>
<p> <i>Ubuntu C Implementation</i></p>
<dl>
<dt>
<dd> This version replaced the shell version with a fast and efficient data logger, but also did not graph the data.</dl>
<p> <i>Java bootchart</i></p>
<dl>
<dt>
<dd> This was the original graphing application for charting the data, written in java.</dl>
<p> <i>pybootchartgui.py</i></p>
<dl>
<dt>
<dd> pybootchart created a graph from the data collected by either the bash or C version.</dl>
<p> The version of bootchart you are using now combines both the data collection and the charting into a single application, making it more efficient and simpler. There are no longer any timing issues with the data collector and the grapher, as the graphing cannot be run until the data has been collected. Also, the data kept in memory is reduced to the absolute minimum needed.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/5-bootchart-conf/">bootchart.conf</a></code>(5)</p>
<h2>BUGS</h2>
<p> systemd-bootchart does not get the model information for the hard drive unless the root device is specified with root=/dev/sdxY. Using UUIDs or PARTUUIDs will boot fine, but the hard drive model will not be added to the chart. </p>
<p> For bugs, please contact the author and current maintainer:</p>
<dl>
<dt>
<dd> Auke Kok &lt;auke-jan.h.kok [at] intel.com&gt;</dl>
<h2>Index</h2>
