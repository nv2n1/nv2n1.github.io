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
<dt><code>-b</code>, <code>&#8211;blocksize</code>=<i>B</i></dt>
<dd> Set the blocksize in bytes (e.g. 4096) or K (e.g. 4K) (must be between 2K and 64K and a power of 2, default 8K)</dd>
<dt><code>-n</code>, <code>&#8211;no-full</code></dt>
<dd> Disable full compaction</dd>
<dt><code>-F</code>, <code>&#8211;fuller</code></dt>
<dd> Enable fuller compaction (not recommended if you plan to update the compacted database)</dd>
<dt><code>-m</code>, <code>&#8211;multipass</code></dt>
<dd> If merging more than 3 databases, merge the postlists in multiple passes (which is generally faster but requires more disk space for temporary files)</dd>
<dt><code>&#8211;no-renumber</code></dt>
<dd> Preserve the numbering of document ids (useful if you have external references to them, or have set them to match unique ids from an external source). Currently this option is only supported when merging databases if they have disjoint ranges of used document ids</dd>
<dt><code>&#8211;help</code></dt>
<dd> display this help and exit</dd>
<dt><code>&#8211;version</code></dt>
<dd> output version information and exit </dd>
</dl>
<h2>Index</h2>
