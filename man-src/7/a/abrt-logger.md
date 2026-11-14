---
title: "abrt-logger(7)"
name: "abrt-logger"
section: "7"
letter: "a"
url: "/docs/linux/man/7-abrt-logger/"
---

Logger plugin for <a HREF="/docs/linux/man/8-abrt/">abrt</a>(8)

<h2>Description</h2>

<i>abrt</i> is a daemon that watches for application crashes. When a crash occurs, it collects the crash data and takes action according to its configuration. This manual page describes the <i>Logger</i> plugin for <i>abrt</i>. This plugin is used to log the crash to a file. The log will contain all the file names as well as their content. It also contains &quot;duplicity check&quot;: the ID of the crash, which is used to tell whether the same crash has happened previously.

<h2>Invocation</h2>

The plugin is invoked in the <i>abrt.conf</i> configuration file. No parameters are necessary.

<h2>Configuration</h2>

The <i>Logger.conf</i> configuration file contains several entries in a format &quot;Option = Value&quot;. The options are:

<h3>LogPath</h3>

The path to the log file.

<h3>AppendLogs</h3>

If set to &quot;yes&quot; (the default) <i>Logger</i> will append the report to the file, otherwise it will overwrite the file (so only the last crash will be stored).

<h2>Examples</h2>

This is a snippet from the <i>abrt.conf</i> configuration file. Log all the C/C++ application crashes: [AnalyzerActionsAndReporters] 
 CCpp = Logger

<h2>See Also</h2>

<i><a HREF="/docs/linux/man/8-abrt/">abrt</a></i>(8), <i><a HREF="/docs/linux/man/5-abrt-conf/">abrt.conf</a></i>(5), <i><a HREF="/docs/linux/man/7-abrt-plugins/">abrt-plugins</a></i>(7)

<h2>Author</h2>

Written by Zdenek Prikryl &lt;zprikryl [at] redhat.com&gt;. Manual page by Daniel Novotny &lt;dnovotny [at] redhat.com&gt;.
