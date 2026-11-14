---
title: "sysreport(1)"
name: "sysreport"
section: "1"
letter: "s"
url: "/docs/linux/man/1-sysreport/"
description: "sysreporter – Simple system statistics aggregator and emailer"
---

<h2 class="name">NAME</h2>
<p> sysreporter &#8211; Simple system statistics aggregator and emailer</p>
<h2>SYNOPSIS</h2>
<p> <code>sysreport</code> COMMAND [ARGUMENTS] </p>
<h2>DESCRIPTION</h2>
<p> <code>sysreport</code> is a tool to run multiple reports on a system and then either email a sysadmin or save the report to a specific location for later review. Reports can be anything from a simple shell script to a native binary. </p>
<h2>COMMANDS</h2>
<dl>
<dt><code>run</code></p>
<dd> Generate a new report by executing all enabled reports and aggregating their output into a single report. run can be ran with the arguments <code>email</code> or <code>stdout</code> to specify where the output will go. Email is assumed if neither is given. </p>
<dt><code>show</code></p>
<dd> Display configuration settings that sysreporter is currently using as well as enabled and disabled reports. </p>
<dt><code>enable</code> PATTERN</p>
<dd> Enable reports matching PATTERN. </p>
<dt><code>disable</code> PATTERN</p>
<dd> Disable reports matching PATTERN. </p>
<dt><code>help</code></p>
<dd> Display help information. </p>
<dt><code>version</code></p>
<dd> Print version information. </p>
</dl>
<h2>EXAMPLES</h2>
<p> To generate a report and email it use one of the following: </p>
<pre>
<dl><dt><dd>sysreport run
sysreport run email
</dl>
</pre>
<p> To generate a report and print it to standard out: </p>
<pre>
<dl><dt><dd>sysreport run stdout
</dl>
</pre>
<p> To enable a report by its number: </p>
<pre>
<dl><dt><dd>sysreport enable 43
</dl>
</pre>
<p> Or by name (enable all apache reports): </p>
<pre>
<dl><dt><dd>sysreport enable apache
</dl>
</pre>
<h2>BUGS</h2>
<p> File a bug report at <a rel="nofollow" href="https://github.com/onesimus-systems/sysreporter.">https://github.com/onesimus-systems/sysreporter.</a> </p>
<h2>AUTHOR</h2>
<p> Lee Keitel (lee [at] onesimussystems.com) </p>
<h2>Index</h2>
