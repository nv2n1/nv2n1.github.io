---
title: "apport-collect(1)"
name: "apport-collect"
section: "1"
letter: "a"
url: "/docs/linux/man/1-apport-collect/"
description: "apport-bug, apport-collect – file a bug report using Apport, or update an existing report"
---

<h2 class="name">NAME</h2>
<p> apport-bug, apport-collect &#8211; file a bug report using Apport, or update an existing report</p>
<h2>SYNOPSIS</h2>
<p> <code>apport-bug</code> </p>
<p> <code>apport-bug</code> <i>symptom </i>|<i> pid </i>|<i> package </i>|<i> program path </i>|<i> .apport/.crash file</i> </p>
<p> <code>apport-collect</code> <i>report-number</i> </p>
<h2>DESCRIPTION</h2>
<p> <code>apport-bug</code> reports problems to your distribution&#8217;s bug tracking system, using Apport to collect a lot of local information about your system to help the developers to fix the problem and avoid unnecessary question/answer turnarounds. </p>
<p> You should always start with running <code>apport-bug</code> without arguments, which will present a list of known symptoms. This will generate the most useful bug reports. </p>
<p> If there is no matching symptom, you need to determine the affected program or package yourself. You can provide a package name or program name to <code>apport-bug</code>, e. g.: </p>
<dl>
<dt>
<dd>
<pre>
apport-bug firefox
apport-bug /usr/bin/unzip
</pre>
</dl>
<p> In order to add more information to the bug report that could help the developers to fix the problem, you can also specify a process ID instead: </p>
<dl>
<dt>
<dd>
<pre>
$ pidof gnome-terminal
5139
$ apport-bug 5139
</pre>
</dl>
<p> As a special case, to report a bug against the Linux kernel, you do not need to use the full package name (such as linux-image-2.6.28-4-generic); you can just use </p>
<dl>
<dt>
<dd>
<pre>
apport-bug linux
</pre>
</dl>
<p> to report a bug against the currently running kernel. </p>
<p> Finally, you can use this program to report a previously stored crash or bug report: </p>
<dl>
<dt>
<dd>
<pre>
apport-bug /var/crash/_bin_bash.1000.crash
apport-bug /tmp/apport.firefox.332G9t.apport
</pre>
</dl>
<p> Bug reports can be written to a file by using the <code>&#8211;save</code> option or by using <code>apport-cli</code>. </p>
<p> <code>apport-bug</code> detects whether KDE or Gnome is running and calls <code>apport-gtk</code> or <code>apport-kde</code> accordingly. If neither is available, or the session does not run under X11, it calls <code>apport-cli</code> for a command-line client. </p>
<h2>UPDATING EXISTING REPORTS</h2>
<p> <code>apport-collect</code> collects the same information as apport-bug, but adds it to an already reported problem you have submitted. This is useful if the report was not originally filed through Apport, and the developers ask you to attach information from your system. </p>
<h2>OPTIONS</h2>
<p> Please see the <code><a href="/docs/linux/man/1-apport-cli/">apport-cli</a>(1)</code> manpage for possible options. </p>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>APPORT_IGNORE_OBSOLETE_PACKAGES</code></p>
<dd> Apport refuses to create bug reports if the package or any dependency is not current. If this environment variable is set, this check is waived. Experts who will thoroughly check the situation before filing a bug report can define this in their <code>~/.bashrc</code> or temporarily on the command line when calling <code>apport-bug</code>. </p>
</dl>
<h2>FILES</h2>
<p> apport crash files are written in to <code>/var/crash</code> by default, named uniquely per binary name and user id. They are not deleted after being sent to the bug tracker (but from cron when they get older than 7 days). You can extract the core file (if any) and other information using <code>apport-unpack.</code> </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-apport-cli/">apport-cli</a></code>(1), <code><a href="/docs/linux/man/1-apport-unpack/">apport-unpack</a></code>(1) </p>
<h2>AUTHOR</h2>
<p> <code>apport</code> and the accompanying tools are developed by Martin Pitt &lt;martin.pitt [at] ubuntu.com&gt;. </p>
<h2>Index</h2>
