---
title: "pmempool-check(1)"
name: "pmempool-check"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pmempool-check/"
description: "pmempool-check – Check and repair Persistent Memory Pool"
---

<h2>NAME</h2>
<p> pmempool-check &#8211; Check and repair Persistent Memory Pool</p>
<h2>SYNOPSIS</h2>
<p> <code>pmempool check</code> [&lt;options&gt;] &lt;file&gt;</p>
<h2>DESCRIPTION</h2>
<p> The <code>pmempool</code> invoked with <code>check</code> command checks consistency of a given pool file. If the pool file is consistent <code>pmempool</code> exits with 0 value. If the pool file is not consistent non-zero error code is returned. </p>
<p> In case of any errors, the proper message is printed. The verbosity level may be increased using <code>-v</code> option. The output messages may be also suppressed using <code>-q</code> option. </p>
<p> It is possible to try to fix encountered problems using <code>-r</code> option. In order to be sure this will not corrupt your data you can either create backup of the pool file using <code>-b</code> option or just print what would be fixed without modifying original pool using <code>-N</code> option. </p>
<h3>Available options:</h3>
<p> <code>-r, &#8211;repair</code></p>
<dl>
<dt>
<dd> Try to repair a pool file if possible.</dl>
<p> <code>-y, &#8211;yes</code></p>
<dl>
<dt>
<dd> Answer yes on all questions.</dl>
<p> <code>-N, &#8211;no-exec</code></p>
<dl>
<dt>
<dd> Don&#8217;t execute, just show what would be done.</dl>
<p> <code>-b, &#8211;backup &lt;file&gt;</code></p>
<dl>
<dt>
<dd> Create backup of a pool file before executing. Terminate if it is <i>not</i> possible to create a backup file. This option requires <code>-r</code> option.</dl>
<p> <code>-q, &#8211;quiet</code></p>
<dl>
<dt>
<dd> Be quiet and don&#8217;t print any messages.</dl>
<p> <code>-v, &#8211;verbose</code></p>
<dl>
<dt>
<dd> Be more verbose.</dl>
<p> <code>-h, &#8211;help</code></p>
<dl>
<dt>
<dd> Display help message and exit.</dl>
<h2>EXAMPLES</h2>
<dl>
<dt>pmempool check pool.bin</p>
<dd> # Check consistency of pool.bin pool file</p>
<dt>pmempool check &#8211;repair &#8211;backup pool.bin.backup pool.bin</p>
<dd> # Check consistency of pool.bin pool file, create backup and repair if necessary.</p>
<dt>pmempool check -rvN pool.bin</p>
<dd> # Check consistency of pool.bin pool file, print what would be repaired with increased verbosity level.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-libpmemblk/">libpmemblk</a>(3) <a href="/docs/linux/man/3-libpmemlog/">libpmemlog</a>(3) <a href="/docs/linux/man/1-pmempool/">pmempool</a>(1)</code></p>
<h2>PMEMPOOL</h2>
<p> Part of the <code><a href="/docs/linux/man/1-pmempool/">pmempool</a>(1)</code> suite. </p>
<h2>Index</h2>
