---
title: "bootchart(5)"
name: "bootchart"
section: "5"
letter: "b"
url: "/docs/linux/man/5-bootchart/"
description: "bootchart.conf – Boot performance analysis graphing tool configuration file"
---

<p>bootchart.conf &#8211; Boot performance analysis graphing tool configuration file</p>
<h2>Synopsis</h2>
<p>/etc/systemd/bootchart.conf</p>
<h2>Description</h2>
<p>When starting, systemd-bootchart will read the configuration file bootchart.conf. This configuration file determines logging parameters and graph output.</p>
<h2>Options</h2>
<p><i>Samples=500</i></p>
<dl>
<dd>Configure the amount of samples to record in total before bootchart exits. Each sample will record at intervals defined by Frequency=.</dl>
<p> <i>Frequency=25</i></p>
<dl>
<dd>Configure the sample log frequency. This can be a fractional number, but must be larger than 0.0. Most systems can cope with values under 25-50 without impacting boot time severely.</dl>
<p> <i>Relative=no</i></p>
<dl>
<dd>Configures whether the left axis of the output graph equals time=0.0 (<code>CLOCK_MONOTONIC</code> start). This is useful for using bootchart at post-boot time to profile an already booted system, otherwise the graph would become extremely large. If set to yes, the horizontal axis starts at the first recorded sample instead of time=0.0.</dl>
<p> <i>Filter=no</i></p>
<dl>
<dd>Configures whether the resulting graph should omit tasks that did not contribute significantly to the boot. Processes that are too short-lived (only seen in one sample) or that do not consume any significant CPU time (less than 0.001sec) will not be displayed in the output graph.</dl>
<p> <i>Output=[path]</i></p>
<dl>
<dd>Configures the output directory for writing the graphs. By default, bootchart writes the graphs to /run/log.</dl>
<p> <i>Init=[path]</i></p>
<dl>
<dd>Configures bootchart to run a non-standard binary instead of /sbin/init. This option is only relevant if bootchart was invoked from the kernel command line with init=/usr/lib/systemd/systemd-bootchart.</dl>
<p> <i>PlotMemoryUsage=no</i></p>
<dl>
<dd>If set to yes, enables logging and graphing of processes&#8217; PSS memory consumption.</dl>
<p> <i>PlotEntropyGraph=no</i></p>
<dl>
<dd>If set to yes, enables logging and graphing of the kernel random entropy pool size.</dl>
<p> <i>ScaleX=100</i></p>
<dl>
<dd>Horizontal scaling factor for all variable graph components.</dl>
<p> <i>ScaleY=20</i></p>
<dl>
<dd>Vertical scaling factor for all variable graph components.</dl>
<p> <i>ControlGroup=no</i></p>
<dl>
<dd>Display process control group.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-systemd-bootchart/">systemd-bootchart</a></code>(1), <code><a href="/docs/linux/man/7-systemd-directives/">systemd.directives</a></code>(7) </p>
