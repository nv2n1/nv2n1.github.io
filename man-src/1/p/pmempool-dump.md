---
title: "pmempool-dump(1)"
name: "pmempool-dump"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pmempool-dump/"
description: "pmempool-dump – Dump user data from specified pool"
---

<h2>NAME</h2>
<p> pmempool-dump &#8211; Dump user data from specified pool</p>
<h2>SYNOPSIS</h2>
<p> <code>pmempool dump</code> [&lt;options&gt;] &lt;file&gt;</p>
<h2>DESCRIPTION</h2>
<p> The <code>pmempool</code> invoked with <code>dump</code> command dumps user data from specified pool file. The output format may be either binary or hexadecimal. </p>
<p> By default the output format is hexadecimal. </p>
<p> By default data is dumped to standard output. It is possible to dump data to other file by specifying <code>-o</code> option. In this case data will be appended to this file. </p>
<p> Using <code>-r</code> option you can specify number of blocks/bytes/data chunks using special text format. See <code>RANGE</code> section for details. </p>
<h3>Available options:</h3>
<p> <code>-b, &#8211;binary</code></p>
<dl>
<dt>
<dd> Dump data in binary format.</dl>
<p> <code>-r, &#8211;range</code> &lt;range&gt;</p>
<dl>
<dt>
<dd> Range of pool file to dump. This may be number of blocks for <code>blk</code> pool type or either number of bytes or number of data chunks for <code>log</code> pool type.</dl>
<p> <code>-c, &#8211;chunk</code> &lt;size&gt;</p>
<dl>
<dt>
<dd> Size of chunk for <code>log</code> pool type. See <code>pmemlog_walk</code>() in <code><a href="/docs/linux/man/3-libpmemlog/">libpmemlog</a>(3)</code> for details.</dl>
<p> <code>-o, &#8211;output</code> &lt;file&gt;</p>
<dl>
<dt>
<dd> Name of output file.</dl>
<p> <code>-h, &#8211;help</code></p>
<dl>
<dt>
<dd> Display help message and exit.</dl>
<h2>RANGE</h2>
<p> Using <code>-r, &#8211;range</code> option it is possible to dump only a range of user data. This section describes valid format of <i>&lt;range&gt;</i> string. </p>
<p> You can specify multiple ranges separated by commas. </p>
<p> <code>&lt;first&gt;-&lt;last&gt;</code></p>
<dl>
<dt>
<dd> All blocks/bytes/data chunks from <code>&lt;first&gt;</code> to <code>&lt;last&gt;</code> will be dumped.</dl>
<p> <code>-&lt;last&gt;</code></p>
<dl>
<dt>
<dd> All blocks/bytes/data chunks up to <code>&lt;last&gt;</code> will be dumped.</dl>
<p> <code>&lt;first&gt;-</code></p>
<dl>
<dt>
<dd> All blocks/bytes/data chunks starting from <code>&lt;first&gt;</code> will be dumped.</dl>
<p> <code>&lt;number&gt;</code></p>
<dl>
<dt>
<dd> Only <code>&lt;number&gt;</code> block/byte/data chunk will be dumped.</dl>
<h2>EXAMPLES</h2>
<dl>
<dt>pmempool dump pool.bin</p>
<dd> # Dump user data from pool.bin file to standard output</p>
<dt>pmempool dump -o output.bin -r1,10-100 pool_blk.bin</p>
<dd> # Dump block number 1 and blocks from 10 to 100 from pool_blk.bin containing pmem blk pool to output.bin file</p>
<dt>pmempool dump -r 1K-2K pool.bin</p>
<dd> # Dump data form 1K to 2K from pool.bin file.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-libpmemblk/">libpmemblk</a>(3) <a href="/docs/linux/man/3-libpmemlog/">libpmemlog</a>(3) <a href="/docs/linux/man/1-pmempool/">pmempool</a>(1)</code></p>
<h2>PMEMPOOL</h2>
<p> Part of the <code><a href="/docs/linux/man/1-pmempool/">pmempool</a>(1)</code> suite. </p>
<h2>Index</h2>
