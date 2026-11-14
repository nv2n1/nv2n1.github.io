---
title: "acpiexec(1)"
name: "acpiexec"
section: "1"
letter: "a"
url: "/docs/linux/man/1-acpiexec/"
description: "acpiexec – ACPI AML execution and debug utility"
---

<h2 class="name">NAME</h2>
<p> acpiexec &#8211; ACPI AML execution and debug utility </p>
<h2>SYNOPSIS</h2>
<p> <code>acpiexec</code> [<i>&lt;option&gt;</i>&#8230;<i>]</i> &lt;aml-file&gt; <code>&#8230;</code> </p>
<h2>DESCRIPTION</h2>
<p> This manual page briefly documents the <code>acpiexec</code> command. The option list is taken from the acpiexec interactive help. </p>
<p> <code>acpiexec</code> provides a simulated execution environment for AML code so that it can be more easily tested and debugged. </p>
<p> Much more detailed documentation may be found at <a rel="nofollow" href="http://www.acpica.org/documentation/.">http://www.acpica.org/documentation/.</a> </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-?</code></p>
<dd> Display the help message</p>
<dt><code>-b command-line</code></p>
<dd> Batch mode command line execution (cmd1;cmd2;&#8230;)</p>
<dt><code>-M [&lt;method&gt;]</code></p>
<dd> Batch mode method execution (Default: MAIN)</p>
<dt><code>-da</code></p>
<dd> Disable method abort on error</p>
<dt><code>-di</code></p>
<dd> Disable execution of _STA/_INI methods during init</p>
<dt><code>-do</code></p>
<dd> Disable Operation Region address simulation</p>
<dt><code>-dr</code></p>
<dd> Disable repair of method return values</p>
<dt><code>-dt</code></p>
<dd> Disable allocation tracking (performance)</p>
<dt><code>-ef</code></p>
<dd> Enable display of final memory statistics</p>
<dt><code>-ei</code></p>
<dd> Enable additional tests for ACPICA interfaces</p>
<dt><code>-em</code></p>
<dd> Enable interpreter Serialized mode</p>
<dt><code>-es</code></p>
<dd> Enable interpreter Slack mode</p>
<dt><code>-et</code></p>
<dd> Enable debug semaphore timeour</p>
<dt><code>-f &lt;value&gt;</code></p>
<dd> Operation Region initialization fill value</p>
<dt><code>-r</code></p>
<dd> Use hardware-reduced FADT V5</p>
<dt><code>-vi</code></p>
<dd> Verbose initialization output</p>
<dt><code>-vr</code></p>
<dd> Verbose region handler output</p>
<dt><code>-x &lt;debug-level&gt;</code></p>
<dd> Debug output level </p>
</dl>
<h2>AUTHOR</h2>
<p> acpiexec was written by Robert Moore &lt;robert.moore [at] intel.com&gt;. </p>
<p> This manual page was written by Al Stone &lt;ahs3 [at] redhat.com&gt; for the Fedora project (but may be used by others). </p>
<h2>Index</h2>
