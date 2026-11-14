---
title: "satyr(1)"
name: "satyr"
section: "1"
letter: "s"
url: "/docs/linux/man/1-satyr/"
description: "satyr – create and manipulate problem reports"
---

<h2>NAME</h2>
<p> satyr &#8211; create and manipulate problem reports</p>
<h2>SYNOPSIS</h2>
<p> <code>satyr</code> &lt;command&gt; [option&#8230;]</p>
<h2>DESCRIPTION</h2>
<p> <i>satyr</i> is a command line tool that creates anonymous reports of software problems that are suitable for automated processing. </p>
<p> The tool has to be invoked with a <i>&lt;command&gt;</i> that specifies the action to be performed. The available commands are documented below. </p>
<h2>OPTIONS</h2>
<p> <code>Commands</code></p>
<dl>
<dt>abrt-print-report-from-dir &lt;directory&gt;</p>
<dd>
<p> Creates report from ABRT problem directory <i>directory</i> and prints it to standard output. </p>
<dt>abrt-create-core-stacktrace &lt;directory&gt;</p>
<dd>
<p> Creates stacktrace from ABRT problem directory <i>directory</i> that contains a core dump. </p>
</dl>
<h2>Index</h2>
