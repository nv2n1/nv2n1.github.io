---
title: "acpidump-acpica(1)"
name: "acpidump-acpica"
section: "1"
letter: "a"
url: "/docs/linux/man/1-acpidump-acpica/"
description: "acpidump – ACPI table dump utility"
---

<h2 class="name">NAME</h2>
<p> acpidump &#8211; ACPI table dump utility </p>
<h2>SYNOPSIS</h2>
<p> <code>acpidump</code> [<i>&lt;option&gt;</i>&#8230;<i>]</i> </p>
<h2>DESCRIPTION</h2>
<p> This manual page briefly documents the <code>acpidump</code> command. The option list is taken from the interactive help. </p>
<p> The <code>acpidump</code> command extracts the ACPI tables currently in use from the running kernel in a form usable for later processing by the <code>acpixtract</code> command. </p>
<p> Invocation of <code>acpidump</code> without parameters will dump all available ACPI tables. Multiple mixed instances of the <code>-a</code> , <code>-f</code> , and <code>-n</code> parameters can be used. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-b</code></p>
<dd> Dump tables in binary format (versus the default human-readable form). </p>
</dl>
<dl>
<dt><code>-h | -?</code></p>
<dd> Display this help message. </p>
</dl>
<dl>
<dt><code>-o &lt;file&gt;</code></p>
<dd> Redirect output to a file. This file can be used later by <code>acpixtract</code> to examine the contents of the ACPI tables. </p>
</dl>
<dl>
<dt><code>-r &lt;address&gt;</code></p>
<dd> Dump tables from specified RSDP. </p>
</dl>
<dl>
<dt><code>-s</code></p>
<dd> Print table summaries only. </p>
</dl>
<dl>
<dt><code>-v</code></p>
<dd> Print the version of this utility. </p>
</dl>
<dl>
<dt><code>-z</code></p>
<dd> Verbose mode. </p>
</dl>
<h2>TABLE OPTIONS</h2>
<dl>
<dt><code>-a &lt;address&gt;</code></p>
<dd> Get a table from a physical address (must be superuser and you must be careful which address you use &#8212; dmesg will typically report the addresses for the various tables). </p>
</dl>
<dl>
<dt><code>-c &lt;on|off&gt;</code></p>
<dd> Turn on/off customized table dumping. If turned on, tables are dumped from /sys/firmware/acpi/tables. If turned off, tables are dumped from /dev/mem. The default is on. </p>
</dl>
<dl>
<dt><code>-f &lt;binary-file&gt;</code></p>
<dd> Get a table from a binary file (see the <code>-b</code> option). </p>
</dl>
<dl>
<dt><code>-n &lt;signature&gt;</code></p>
<dd> Get a table via it&#8217;s name or signature (e.g., MADT or SSDT). </p>
</dl>
<dl>
<dt><code>-x</code></p>
<dd> Do not use but dump XSDT. </p>
</dl>
<dl>
<dt><code>-x -x</code></p>
<dd> Do not use or dump XSDT. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-acpixtract/">acpixtract</a>(1)</code> </p>
<h2>AUTHOR</h2>
<p> acpidump was written by Robert Moore &lt;robert.moore [at] intel.com&gt; and Chao Guan &lt;chao.guan [at] intel.com&gt;. </p>
<p> This manual page was written by Al Stone &lt;ahs3 [at] redhat.com&gt; for the Fedora project (but may be used by others). </p>
<h2>Index</h2>
