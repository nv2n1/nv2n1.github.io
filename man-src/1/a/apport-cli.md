---
title: "apport-cli(1)"
name: "apport-cli"
section: "1"
letter: "a"
url: "/docs/linux/man/1-apport-cli/"
description: "apport-cli, apport-gtk, apport-kde – Apport user interfaces for reporting problems"
---

<h2 class="name">NAME</h2>
<p> apport-cli, apport-gtk, apport-kde &#8211; Apport user interfaces for reporting problems</p>
<h2>SYNOPSIS</h2>
<p> <code>apport-cli</code> </p>
<p> <code>apport-cli </code> [ <code>&#8211;save </code><i>file</i> ] <i>symptom </i>|<i> pid </i>|<i> package </i>|<i> program path </i>|<i> .apport/.crash file</i> </p>
<p> <code>apport-cli -f</code> </p>
<p> <code>apport-cli -f -p</code> <i>package</i> <code>-P</code> <i>pid</i> </p>
<p> <code>apport-cli -u</code> <i>report-number</i> </p>
<p> Same options/arguments for <code>apport-gtk</code> and <code>apport-kde</code>. </p>
<h2>DESCRIPTION</h2>
<p> <code>apport </code> automatically collects data from crashed processes and compiles a problem report in <i>/var/crash/</i>. This is a command line frontend for reporting those crashes to the developers. It can also be used to report bugs about packages or running processes. </p>
<p> If symptom scripts are available, it can also be given the name of a symptom, or be called with just <code>-f</code> to display a list of known symptoms. </p>
<p> When being called without any options, it processes the pending crash reports and offers to report them one by one. You can also display the entire report to see what is sent to the software developers. </p>
<p> When being called with exactly one argument and no option, <code>apport-cli</code> uses some heuristics to find out &quot;what you mean&quot; and reports a bug against the given symptom name, package name, program path, or PID. If the argument is a <code>.crash </code> or <code>.apport</code> file, it uploads the stored problem report to the bug tracking system. </p>
<p> For desktop systems with a graphical user interface, you should consider installing the GTK or KDE user interface (apport-gtk or apport-kde). They accept the very same options and arguments. <code>apport-cli</code> is mainly intended to be used on servers. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-f, &#8211;file-bug</code></p>
<dd> Report a (non-crash) problem. If neither <code>&#8211;package</code>, <code>&#8211;symptom</code>, or <code>&#8211;pid</code> are specified, then it displays a list of available symptoms. If none are available, it aborts with an error. </p>
<p> This will automatically attach information about your operating system and the package version etc. to the bug report, so that the developers have some important context. </p>
<dt><code>-s </code><i>symptom</i>, <code>&#8211;symptom</code>=<i>symptom</i></p>
<dd> When being used in <code>&#8211;file-bug</code> mode, specify the symptom to report the problem about. </p>
<dt><code>-p </code><i>package</i>, <code>&#8211;package</code>=<i>package</i></p>
<dd> When being used in <code>&#8211;file-bug</code> mode, specify the package to report the problem against. </p>
<dt><code>-P </code><i>pid</i>, <code>&#8211;pid</code>=<i>pid</i></p>
<dd> When being used in <code>&#8211;file-bug</code> mode, specify the PID (process ID) of a running program to report the problem against. This can be determined with e. g. <code>ps -ux</code>. </p>
<dt><code>-c </code><i>report</i>, <code>&#8211;crash-file</code>=<i>report</i></p>
<dd> Upload a previously processed stored report in an arbitrary file location. This is useful for copying a crash report to a machine with internet connection and reporting it from there. Files must end in <code>.crash</code> or <code>.apport</code>. </p>
<dt><code>-u </code><i>report-number</i>, <code>&#8211;update-report </code><i>report-number</i></p>
<dd> Run apport information collection on an already existing problem report. The affected package is taken from the report by default, but you can explicitly specify one with &#8211;package to collect information for a different package (this is useful if the report is assigned to the wrong package). </p>
<dt><code>&#8211;save </code><i>filename</i></p>
<dd> In &#8211;file-bug mode, save the collected information into a file instead of reporting it. This file can then be reported with &#8211;crash-file later on. </p>
<dt><code>-w, &#8211;window</code></p>
<dd> Point and click at the application window against which you wish to report the bug. Apport will automatically find the package name and generate a report for you. This option can be specially useful in situations when you do not know the name of the package, or if the application window has stopped responding and you cannot report the problem from the &quot;Help&quot; menu of the application. </p>
<p> This option is not supported on Wayland. Users running Wayland should use another option such as <code>-P</code> to specify the application. </p>
</dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>APPORT_IGNORE_OBSOLETE_PACKAGES</code></p>
<dd> Apport refuses to create bug reports if the package or any dependency is not current. If this environment variable is set, this check is waived. Experts who will thoroughly check the situation before filing a bug report can define this in their <code>~/.bashrc</code> or temporarily when calling the apport frontend (-cli, -gtk, or -kde). </p>
</dl>
<h2>FILES</h2>
<dl>
<dt><code>/usr/share/apport/symptoms/*.py</code></p>
<dd> Symptom scripts. These ask a set of interactive questions to determine the package which is responsible for a particular problem. (For some problems like sound or storage device related bugs there are many places where things can go wrong, and it&#8217;s not immediately obvious for a bug reporter where the problem is.) </p>
</dl>
<h2>AUTHOR</h2>
<p> <code>apport</code> and the accompanying tools are developed by Martin Pitt &lt;martin.pitt [at] ubuntu.com&gt;. </p>
<h2>Index</h2>
