---
title: "mperfmon(1)"
name: "mperfmon"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mperfmon/"
description: "mperfmon – Mono Performance Counter Monitor"
---

<h2>NAME</h2>
<p> mperfmon &#8211; Mono Performance Counter Monitor</p>
<h2>SYNOPSIS</h2>
<p> <code>mperfmon</code> [&#8211;config=FILE] [&#8211;report=REPORT_NAME] [&#8211;count=NUM] [pid]</p>
<h2>OPTIONS</h2>
<dl>
<dt><i>&#8211;config=FILE</i></p>
<dd> Specifies the configuration file to load instead of the default one installed in the same directory as the app.</p>
<dt><i>&#8211;report=REPORT_NAME</i></p>
<dd> Instead of showing the GUI, run in console mode and print a report of the set of counters specified by REPORT_NAME and described in the config file. The report is printed for up to the number of times specified with the &#8211;count option. The <i>pid</i> argument is used as the instance name in the performance counters, it is typically the pid of a mono process.</p>
<dt><i>&#8211;count=NUM</i></p>
<dd> Sets the number of times a report is printed in console mode. The default is 2.</dl>
<h2>DESCRIPTION</h2>
<p> mperfmon is a tool that allows you to monitor performance counters exposed by Mono processes or by the operating system. With the &#8211;report option it can be used on the console, otherwise a GUI is started. In GUI mode each counter added is monitored at user-specified time intervals (the default is 1 second) and it is shown in a graph as it changes over time. </p>
<h2>MAILING LISTS</h2>
<p> Visit <a rel="nofollow" href="http://lists.ximian.com/mailman/listinfo/mono-devel-list">http://lists.ximian.com/mailman/listinfo/mono-devel-list</a> for details.</p>
<h2>WEB SITE</h2>
<p> Visit <a rel="nofollow" href="http://www.mono-project.com">http://www.mono-project.com</a> for details </p>
<h2>Index</h2>
