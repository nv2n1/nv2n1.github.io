---
title: "acpixtract-acpica(1)"
name: "acpixtract-acpica"
section: "1"
letter: "a"
url: "/docs/linux/man/1-acpixtract-acpica/"
description: "acpixtract – ACPICA source code conversion utility"
---

<h2 class="name">NAME</h2>
<p> acpixtract &#8211; ACPICA source code conversion utility </p>
<h2>SYNOPSIS</h2>
<p> <code>acpixtract</code> [<i>&lt;option&gt;</i>&#8230;<i>]</i> &lt;acpidump-file&gt; </p>
<h2>DESCRIPTION</h2>
<p> This manual page briefly documents the <code>acpixtract</code> command. The option list is taken from the acpixtract interactive help. </p>
<p> <code>acpixtract</code> extracts binary ACPI tables from the output of the <code>acpidump</code> command (see the <code>pm-tools</code> package). A default invocation will extract the DSDT and all SSDTs. </p>
<p> Much more detailed documentation may be found at <a rel="nofollow" href="http://www.acpica.org/documentation/.">http://www.acpica.org/documentation/.</a> </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-a</code></p>
<dd> Extract all tables, not just DSDT/SSDT</p>
<dt><code>-l</code></p>
<dd> List table summaries, do not extract</p>
<dt><code>-s &lt;signature&gt;</code></p>
<dd> Extract all tables with &lt;signature&gt; </p>
</dl>
<h2>AUTHOR</h2>
<p> acpixtract was written by Robert Moore &lt;robert.moore [at] intel.com&gt;. </p>
<p> This manual page was written by Al Stone &lt;ahs3 [at] redhat.com&gt; for the Fedora project (but may be used by others). </p>
<h2>Index</h2>
