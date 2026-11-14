---
title: "xapian-compact(1)"
name: "xapian-compact"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xapian-compact/"
description: "xapian-compact – Compact a database, or merge and compact several"
---

<h2>NAME</h2>
<p> xapian-compact &#8211; Compact a database, or merge and compact several</p>
<h2>SYNOPSIS</h2>
<p> <code>xapian-compact</code> [<i>OPTIONS</i>] <i>SOURCE_DATABASE</i>&#8230; <i>DESTINATION_DATABASE</i></p>
<h2>DESCRIPTION</h2>
<p> xapian-compact &#8211; Compact a database, or merge and compact several</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-b</code>, <code>&#8211;blocksize</code>=<i>B</i></p>
<dd> Set the blocksize in bytes (e.g. 4096) or K (e.g. 4K) (must be between 2K and 64K and a power of 2, default 8K)</p>
<dt><code>-n</code>, <code>&#8211;no-full</code></p>
<dd> Disable full compaction</p>
<dt><code>-F</code>, <code>&#8211;fuller</code></p>
<dd> Enable fuller compaction (not recommended if you plan to update the compacted database)</p>
<dt><code>-m</code>, <code>&#8211;multipass</code></p>
<dd> If merging more than 3 databases, merge the postlists in multiple passes (which is generally faster but requires more disk space for temporary files)</p>
<dt><code>&#8211;no-renumber</code></p>
<dd> Preserve the numbering of document ids (useful if you have external references to them, or have set them to match unique ids from an external source). Currently this option is only supported when merging databases if they have disjoint ranges of used document ids</p>
<dt><code>&#8211;help</code></p>
<dd> display this help and exit</p>
<dt><code>&#8211;version</code></p>
<dd> output version information and exit </p>
</dl>
<h2>Index</h2>
