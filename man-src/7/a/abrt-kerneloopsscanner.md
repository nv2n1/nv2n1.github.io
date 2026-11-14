---
title: "abrt-kerneloopsscanner(7)"
name: "abrt-kerneloopsscanner"
section: "7"
letter: "a"
url: "/docs/linux/man/7-abrt-kerneloopsscanner/"
---

KerneloopsScanner plugin for <a HREF="/docs/linux/man/8-abrt/">abrt</a>(8)

<h2>Description</h2>

<i>abrt</i> is a daemon that watches for application crashes. When a crash occurs, it collects the crash data and takes action according to its configuration. This manual page describes the <i>KerneloopsScanner</i> plugin for <i>abrt</i>. This plugin reads the system log file (default /var/log/messages) and stores the kernel oops crashes, which were not already reported, to abrt's debug dump directory. To distinguish between new crashes and crashes that were already reported, the plugin makes its own entry in the log file, which acts as a separator.

<h2>Invocation</h2>

The plugin is invoked in the <i>abrt.conf</i> configuration file. No parameters are necessary.

<h2>Configuration</h2>

The <i>KerneloopsScanner.conf</i> configuration file contains one entry:

<h3>SysLogFile</h3>

The file to scan. The default is 
 SysLogFile = /var/log/messages

<h2>Examples</h2>

This is a snippet from the <i>abrt.conf</i> configuration file. Every 10 seconds look if there were any kernel crashes: [common] 
 ActionsAndReporters = Kerneloops, KerneloopsScanner 
 [cron] 
 10 = KerneloopsScanner

<h2>See Also</h2>

<i><a HREF="/docs/linux/man/8-abrt/">abrt</a></i>(8), <i><a HREF="/docs/linux/man/5-abrt-conf/">abrt.conf</a></i>(5), <i><a HREF="/docs/linux/man/7-abrt-plugins/">abrt-plugins</a></i>(7)

<h2>Author</h2>

Written by Anton Arapov &lt;anton [at] redhat.com&gt;. Manual page by Daniel Novotny &lt;dnovotny [at] redhat.com&gt;.
