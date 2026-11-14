---
title: "hwloc-dump-hwdata(1)"
name: "hwloc-dump-hwdata"
section: "1"
letter: "h"
url: "/docs/linux/man/1-hwloc-dump-hwdata/"
description: "hwloc-dump-hwdata – Dump topology and locality information from hardware tables"
---

<h2>NAME</h2>
<p> hwloc-dump-hwdata &#8211; Dump topology and locality information from hardware tables</p>
<h2>SYNOPSIS</h2>
<p> <code>hwloc-dump-hwdata</code> [<i>options</i>]</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-o &lt;dir&gt;</code></p>
<dd> save output files to directory &lt;dir&gt; instead of the default <i>/var/run/hwloc/</i> that was specified at configure time. </p>
<p> You may want to set the HWLOC_DUMPED_HWDATA_DIR environment variable as well so that the hwloc library looks for dumped files in that same directory.</dl>
<h2>DESCRIPTION</h2>
<p> hwloc may benefit from some locality and topology information from SMBIOS or ACPI tables. They are accessible from raw hardware files under directories such /sys/firmware/dmi/ or /sys/firmware/acpi/ on Linux. These files are usually only accessible to root. </p>
<p> The hwloc-dump-hwdata tool dumps the useful contents of such files into human-readable and world-accessible files. The intent is to run the tool once during boot and have the main (non-privileged) hwloc library gather information from these human-readable files. </p>
<p> <code>hwloc-dump-hwdata is currently only useful on Intel Knights Landing Xeon Phi platforms</code>. </p>
<p> The current list of dumped information is:</p>
<dl>
<dt><code>Intel Knights Landing memory-side cache characteristics</code></p>
<dd> gathered from specific SMBIOS entries such as <i>/sys/firmware/dmi/entries/14-*</i> and <i>/sys/firmware/dmi/entries/160-*</i>, and saved in file <i>knl_memoryside_cache</i>.</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/7-hwloc/">hwloc</a>(7), <a href="/docs/linux/man/1-lstopo/">lstopo</a>(1) </p>
<h2>Index</h2>
