---
title: "bootchart-conf(5)"
name: "bootchart-conf"
section: "5"
letter: "b"
url: "/docs/linux/man/5-bootchart-conf/"
description: "bootchart.conf, bootchart.conf.d – Boot performance analysis graphing tool configuration files"
---

<p>bootchart.conf, bootchart.conf.d &#8211; Boot performance analysis graphing tool configuration files</p>
<h2>Synopsis</h2>
<p>/etc/systemd/bootchart.conf </p>
<p> /etc/systemd/bootchart.conf.d/*.conf </p>
<p> /run/systemd/bootchart.conf.d/*.conf </p>
<p> /usr/lib/systemd/bootchart.conf.d/*.conf</p>
<h2>Description</h2>
<p>When starting, systemd-bootchart will read the configuration file /etc/systemd/bootchart.conf, followed by the files in the bootchart.conf.d directories. These configuration files determine logging parameters and graph output.</p>
<h2>Configuration Directories And Precedence</h2>
<p>Default configuration is defined during compilation, so a configuration file is only needed when it is necessary to deviate from those defaults. By default the configuration file in /etc/systemd/ contains commented out entries showing the defaults as a guide to the administrator. This file can be edited to create local overrides. </p>
<p> When packages need to customize the configuration, they can install configuration snippets in /usr/lib/systemd/*.conf.d/. Files in /etc/ are reserved for the local administrator, who may use this logic to override the configuration files installed by vendor packages. The main configuration file is read before any of the configuration directories, and has the lowest precedence; entries in a file in any configuration directory override entries in the single configuration file. Files in the *.conf.d/ configuration subdirectories are sorted by their filename in lexicographic order, regardless of which of the subdirectories they reside in. If multiple files specify the same option, the entry in the file with the lexicographically latest name takes precedence. It is recommended to prefix all filenames in those subdirectories with a two-digit number and a dash, to simplify the ordering of the files. </p>
<p> To disable a configuration file supplied by the vendor, the recommended way is to place a symlink to /dev/null in the configuration directory in /etc/, with the same filename as the vendor configuration file.</p>
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
<dd>Configures bootchart to run a non-standard binary instead of /usr/lib/systemd/systemd. This option is only relevant if bootchart was invoked from the kernel command line with init=/usr/lib/systemd/systemd-bootchart.</dl>
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
