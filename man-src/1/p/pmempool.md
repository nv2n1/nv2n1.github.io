---
title: "pmempool(1)"
name: "pmempool"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pmempool/"
description: "pmempool – Persistent Memory Pool Management Tool"
---

<h2>NAME</h2>
<p> pmempool &#8211; Persistent Memory Pool Management Tool</p>
<h2>SYNOPSIS</h2>
<p> <code>pmempool [&#8211;help] [&#8211;version] &lt;command&gt; [&lt;args&gt;]</code></p>
<h2>DESCRIPTION</h2>
<p> The <code>pmempool</code> is a management tool for <i>Persistent Memory</i> pool files created by <code>NVML</code> libraries. </p>
<p> The main purpose of <code>pmempool</code> is to provide a user with a set of utilities for off-line analysis and manipulation of pools created by pmem libraries. The pmempool is a generic command which consists of subcommands for specific purposes. Some of subcommands are required to work <i>without</i> any impact on processed pool, but some of them <i>may</i> create a new or modify an existing one. </p>
<p> The <code>pmempool</code> may be useful for troubleshooting by system administrators and for software developers who work on applications based on <code>NVML</code> library. The latter may find these tools useful for testing and debugging purposes also.</p>
<h2>OPTIONS</h2>
<p> <code>-V, &#8211;version</code></p>
<dl>
<dt>
<dd> Prints the version of <code>pmempool.</code></dl>
<p> <code>-h, &#8211;help</code></p>
<dl>
<dt>
<dd> Prints synopsis and list of commands.</dl>
<h2>COMMANDS</h2>
<p> Currently there is a following set of commands available: </p>
<p> <code><a href="/docs/linux/man/1-pmempool-info/">pmempool-info</a>(1)</code></p>
<dl>
<dt>
<dd> Prints information and statistics in human-readable format about specified pool.</dl>
<p> <code><a href="/docs/linux/man/1-pmempool-check/">pmempool-check</a>(1)</code></p>
<dl>
<dt>
<dd> Checks pool&#8217;s consistency and repairs pool if it is not consistent.</dl>
<p> <code><a href="/docs/linux/man/1-pmempool-create/">pmempool-create</a>(1)</code></p>
<dl>
<dt>
<dd> Creates a pool of specified type with additional properties specific for this type of pool.</dl>
<p> <code><a href="/docs/linux/man/1-pmempool-dump/">pmempool-dump</a>(1)</code></p>
<dl>
<dt>
<dd> Dumps usable data from pool in hexadecimal or binary format.</dl>
<p> <code><a href="/docs/linux/man/1-pmempool-rm/">pmempool-rm</a>(1)</code></p>
<dl>
<dt>
<dd> Removes pool file or all pool files listed in poolset configuration file.</dl>
<p> <code><a href="/docs/linux/man/1-pmempool-convert/">pmempool-convert</a>(1)</code></p>
<dl>
<dt>
<dd> Updates the pool to the latest available layout version.</dl>
<p> In order to get more information about specific <i>command</i> you can use <code>pmempool help &lt;command&gt;.</code></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-libpmemlog/">libpmemlog</a>(3) <a href="/docs/linux/man/3-libpmemblk/">libpmemblk</a>(3) <a href="/docs/linux/man/3-libpmemobj/">libpmemobj</a>(3)</code> </p>
<h2>Index</h2>
