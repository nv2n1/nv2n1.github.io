---
title: "acpidump-acpica(1)"
name: "acpidump-acpica"
section: "1"
letter: "a"
url: "/docs/linux/man/1-acpidump-acpica/"
description: "acpidump – ACPI table dump utility"
---

<h2>SYNOPSIS</h2>
<p> <code>acpidump</code> [<i>&lt;option&gt;</i>&#8230;<i>]</i> </p>
<h2>DESCRIPTION</h2>
<p> This manual page briefly documents the <code>acpidump</code> command. The option list is taken from the interactive help. </p>
<p> The <code>acpidump</code> command extracts the ACPI tables currently in use from the running kernel in a form usable for later processing by the <code>acpixtract</code> command. </p>
<p> Invocation of <code>acpidump</code> without parameters will dump all available ACPI tables. Multiple mixed instances of the <code>-a</code> , <code>-f</code> , and <code>-n</code> parameters can be used. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-b</code></dt>
<dd> Dump tables in binary format (versus the default human-readable form). </dd>
</dl>
<dl>
<dt><code>-h | -?</code></dt>
<dd> Display this help message. </dd>
</dl>
<dl>
<dt><code>-o &lt;file&gt;</code></dt>
<dd> Redirect output to a file. This file can be used later by <code>acpixtract</code> to examine the contents of the ACPI tables. </dd>
</dl>
<dl>
<dt><code>-r &lt;address&gt;</code></dt>
<dd> Dump tables from specified RSDP. </dd>
</dl>
<dl>
<dt><code>-s</code></dt>
<dd> Print table summaries only. </dd>
</dl>
<dl>
<dt><code>-v</code></dt>
<dd> Print the version of this utility. </dd>
</dl>
<dl>
<dt><code>-z</code></dt>
<dd> Verbose mode. </dd>
</dl>
<h2>TABLE OPTIONS</h2>
<dl>
<dt><code>-a &lt;address&gt;</code></dt>
<dd> Get a table from a physical address (must be superuser and you must be careful which address you use &#8212; dmesg will typically report the addresses for the various tables). </dd>
</dl>
<dl>
<dt><code>-c &lt;on|off&gt;</code></dt>
<dd> Turn on/off customized table dumping. If turned on, tables are dumped from /sys/firmware/acpi/tables. If turned off, tables are dumped from /dev/mem. The default is on. </dd>
</dl>
<dl>
<dt><code>-f &lt;binary-file&gt;</code></dt>
<dd> Get a table from a binary file (see the <code>-b</code> option). </dd>
</dl>
<dl>
<dt><code>-n &lt;signature&gt;</code></dt>
<dd> Get a table via it&#8217;s name or signature (e.g., MADT or SSDT). </dd>
</dl>
<dl>
<dt><code>-x</code></dt>
<dd> Do not use but dump XSDT. </dd>
</dl>
<dl>
<dt><code>-x -x</code></dt>
<dd> Do not use or dump XSDT. </dd>
</dl>
<h2>SEE ALSO</h2>
<p> <code>acpixtract(1)</code> </p>
<h2>AUTHOR</h2>
<p> acpidump was written by Robert Moore &lt;robert.moore [at] intel.com&gt; and Chao Guan &lt;chao.guan [at] intel.com&gt;. </p>
<p> This manual page was written by Al Stone &lt;ahs3 [at] redhat.com&gt; for the Fedora project (but may be used by others). </p>
