---
title: "abrt-runapp(7)"
name: "abrt-runapp"
section: "7"
letter: "a"
url: "/docs/linux/man/7-abrt-runapp/"
---

RunApp plugin for <a HREF="/docs/linux/man/8-abrt/">abrt</a>(8)

<h2>Description</h2>

<i>abrt</i> is a daemon that watches for application crashes. When a crash occurs, it collects the crash data and takes action according to its configuration. This manual page describes the <i>RunApp</i> plugin for <i>abrt</i>. This plugin is used to run a specified application when the crash occurs.

<h2>Invocation</h2>

The plugin is invoked in the <i>abrt.conf</i> configuration file. The first parameter is the command to run. The second, optional parameter specifies an output file, to which the standard output of the program is saved.

<h2>Configuration</h2>

There is no configuration file, the plugin parameters are sufficient.

<h2>Examples</h2>

These are snippets from the <i>abrt.conf</i> configuration file. 1) Each time something crashes, print (and save in a text file) which processes are running on the system. 

 [common] 
 ActionsAndReporters = RunApp(&quot;ps ax&quot;,&quot;processes.txt&quot;) 2) When proftpd crashes, restart it. 

 [AnalyzerActionsAndReporters] 
 CCpp:proftpd = RunApp(&quot;/etc/init.d/proftpd restart&quot;)

<h2>See Also</h2>

<i><a HREF="/docs/linux/man/8-abrt/">abrt</a></i>(8), <i><a HREF="/docs/linux/man/5-abrt-conf/">abrt.conf</a></i>(5), <i><a HREF="/docs/linux/man/7-abrt-plugins/">abrt-plugins</a></i>(7)

<h2>Author</h2>

Written by Zdenek Prikryl &lt;zprikryl [at] redhat.com&gt;. Manual page by Daniel Novotny &lt;dnovotny [at] redhat.com&gt;.
