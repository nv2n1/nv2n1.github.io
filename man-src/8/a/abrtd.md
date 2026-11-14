---
title: "abrtd(8)"
name: "abrtd"
section: "8"
letter: "a"
url: "/docs/linux/man/8-abrtd/"
---

abrtd - automated bug reporting tool's daemon.

<h2>Synopsis</h2>

<i>abrtd</i> [-dsv[v]...]

<h2>Description</h2>

<i>abrtd</i> is a daemon that watches for application crashes. When a crash occurs, it collects the problem data (core file, application's command line etc.) and takes action according to the type of application that crashed and according to the configuration in the <i>abrt.conf</i> config file. There are plugins for various actions: for example to report the crash to Bugzilla, to mail the report, or to transfer the report via FTP or SCP. See the manual pages for the respective plugins.

<h2>Options</h2>

-v
<dl><dd>Log more detailed debugging information.</dl>
 

 -d
<dl><dd>Stay in the foreground and log to standard error.</dl>
 

 -s
<dl><dd>Log to system log even with option -d.</dl>
 

 -t NUM
<dl><dd>Exit after NUM seconds of inactivity.</dl>
 

 -p
<dl><dd>Add program names to log.</dl>

<h2>Caveats</h2>

When you use some other crash-catching tool specific for an application or an application type (for example BugBuddy for GNOME applications), crashes of this type will be handled by that tool and not by <i>abrtd</i>. If you want <i>abrtd</i> to handle these crashes, turn off the higher-level crash-catching tool.

<h2>Authors</h2>

<dl><dd>&bull; ABRT team</dl>

<h2>See Also</h2>

<a HREF="/docs/linux/man/5-abrt-conf/">abrt.conf</a>(5) 
