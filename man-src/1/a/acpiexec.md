---
title: "acpiexec(1)"
name: "acpiexec"
section: "1"
letter: "a"
url: "/docs/linux/man/1-acpiexec/"
description: "acpiexec – ACPI AML execution and debug utility"
---

<h2>SYNOPSIS</h2>
<p> <code>acpiexec</code> [<i>&lt;option&gt;</i>&#8230;<i>]</i> &lt;aml-file&gt; <code>&#8230;</code> </p>
<h2>DESCRIPTION</h2>
<p> This manual page briefly documents the <code>acpiexec</code> command. The option list is taken from the acpiexec interactive help. </p>
<p> <code>acpiexec</code> provides a simulated execution environment for AML code so that it can be more easily tested and debugged. </p>
<p> Much more detailed documentation may be found at <a rel="nofollow" href="http://www.acpica.org/documentation/.">http://www.acpica.org/documentation/.</a> </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-?</code></dt>
<dd> Display the help message</dd>
<dt><code>-b command-line</code></dt>
<dd> Batch mode command line execution (cmd1;cmd2;&#8230;)</dd>
<dt><code>-M [&lt;method&gt;]</code></dt>
<dd> Batch mode method execution (Default: MAIN)</dd>
<dt><code>-da</code></dt>
<dd> Disable method abort on error</dd>
<dt><code>-di</code></dt>
<dd> Disable execution of _STA/_INI methods during init</dd>
<dt><code>-do</code></dt>
<dd> Disable Operation Region address simulation</dd>
<dt><code>-dr</code></dt>
<dd> Disable repair of method return values</dd>
<dt><code>-dt</code></dt>
<dd> Disable allocation tracking (performance)</dd>
<dt><code>-ef</code></dt>
<dd> Enable display of final memory statistics</dd>
<dt><code>-ei</code></dt>
<dd> Enable additional tests for ACPICA interfaces</dd>
<dt><code>-em</code></dt>
<dd> Enable interpreter Serialized mode</dd>
<dt><code>-es</code></dt>
<dd> Enable interpreter Slack mode</dd>
<dt><code>-et</code></dt>
<dd> Enable debug semaphore timeour</dd>
<dt><code>-f &lt;value&gt;</code></dt>
<dd> Operation Region initialization fill value</dd>
<dt><code>-r</code></dt>
<dd> Use hardware-reduced FADT V5</dd>
<dt><code>-vi</code></dt>
<dd> Verbose initialization output</dd>
<dt><code>-vr</code></dt>
<dd> Verbose region handler output</dd>
<dt><code>-x &lt;debug-level&gt;</code></dt>
<dd> Debug output level </dd>
</dl>
<h2>AUTHOR</h2>
<p> acpiexec was written by Robert Moore &lt;robert.moore [at] intel.com&gt;. </p>
<p> This manual page was written by Al Stone &lt;ahs3 [at] redhat.com&gt; for the Fedora project (but may be used by others). </p>
