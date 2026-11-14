---
title: "abrt-kerneloopsreporter(7)"
name: "abrt-kerneloopsreporter"
section: "7"
letter: "a"
url: "/docs/linux/man/7-abrt-kerneloopsreporter/"
---

KerneloopsReporter plugin for <a HREF="/docs/linux/man/8-abrt/">abrt</a>(8)

<h2>Description</h2>

<i>abrt</i> is a daemon that watches for application crashes. When a crash occurs, it collects the crash data and takes action according to its configuration. This manual page describes the <i>KerneloopsReporter</i> plugin for <i>abrt</i>. This plugin is used to report the crash to the Kerneloops tracker.

<h2>Invocation</h2>

The plugin is invoked in the <i>abrt.conf</i> configuration file. No parameters are necessary.

<h2>Configuration</h2>

The <i>KerneloopsReporter.conf</i> configuration file contains one entry:

<h3>SubmitURL</h3>

The URL of the kerneloops tracker, the default is 
 SubmitURL = <a rel="nofollow" HREF="http://submit.kerneloops.org/submitoops.php">http://submit.kerneloops.org/submitoops.php</a>

<h2>Examples</h2>

This is a snippet from the <i>abrt.conf</i> configuration file. Each time a kernel oops is detected, run KerneloopsReporter: [common] 
 ActionsAndReporters = Kerneloops, KerneloopsReporter 
 [AnalyzerActionsAndReporters] 
 Kerneloops = KerneloopsReporter

<h2>See Also</h2>

<i><a HREF="/docs/linux/man/8-abrt/">abrt</a></i>(8), <i><a HREF="/docs/linux/man/5-abrt-conf/">abrt.conf</a></i>(5), <i><a HREF="/docs/linux/man/7-abrt-plugins/">abrt-plugins</a></i>(7)

<h2>Author</h2>

Written by Anton Arapov &lt;anton [at] redhat.com&gt;. Manual page by Daniel Novotny &lt;dnovotny [at] redhat.com&gt;.
