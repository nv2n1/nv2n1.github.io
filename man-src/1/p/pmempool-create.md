---
title: "pmempool-create(1)"
name: "pmempool-create"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pmempool-create/"
description: "pmempool-create – Create Persistent Memory Pool of specified type"
---

<h2>NAME</h2>
<p> pmempool-create &#8211; Create Persistent Memory Pool of specified type</p>
<h2>SYNOPSIS</h2>
<p> <code>pmempool create</code> [&lt;options&gt;] [&lt;type&gt;] [&lt;bsize&gt;] &lt;file&gt;</p>
<h2>DESCRIPTION</h2>
<p> The <code>pmempool</code> invoked with <code>create</code> command creates a pool file of specified type. Depending on a pool type it is possible to provide more properties of pool. </p>
<p> Valid pool types are: <code>blk</code>, <code>log</code> and <code>obj</code> which stands for <i>pmem</i>blk<i>,</i> <i>pmem</i>log and <i>pmem</i>obj pools respectively. By default the pool file is created with <i>minimum</i> allowed size for specified pool type. The minimum sizes for <code>blk</code>, <code>log</code> and <code>obj</code> pool types are <code>PMEMBLK_MIN_POOL</code>, <code>PMEMLOG_MIN_POOL</code> and <code>PMEMOBJ_MIN_POOL</code> respectively. See <code><a href="/docs/linux/man/3-libpmemblk/">libpmemblk</a></code>(3)<code>,</code> <code><a href="/docs/linux/man/3-libpmemlog/">libpmemlog</a></code>(3) and <code><a href="/docs/linux/man/3-libpmemobj/">libpmemobj</a></code>(3) for details. </p>
<p> For <i>pmem</i>blk pool type block size <code>&lt;bsize&gt;</code> is a required argument. </p>
<p> In order to set custom size of pool use <code>-s</code> option, or use <code>-M</code> option to create a pool of maximum available size on underlying file system. </p>
<p> The <i>size</i> argument may be passed in format that permits only the upper-case character for byte &#8211; B as specified in IEC 80000-13, IEEE 1541 and the Metric Interchange Format. Standards accept SI units with obligatory B &#8211; kB, MB, GB &#8230; which means multiplier by 1000 and IEC units with optional &quot;iB&quot; &#8211; KiB, MiB, GiB, &#8230;, K, M, G, &#8230; &#8211; which means multiplier by 1024. </p>
<h3>Available options:</h3>
<p> <code>-s, &#8211;size</code> &lt;size&gt;</p>
<dl>
<dt>
<dd> Size of pool file.</dl>
<p> <code>-M, &#8211;max-size</code></p>
<dl>
<dt>
<dd> Set size of pool to available space of underlying file system.</dl>
<p> <code>-m, &#8211;mode</code> &lt;octal&gt;</p>
<dl>
<dt>
<dd> Set permissions to &lt;octal&gt; (the default is 0664).</dl>
<p> <code>-i, &#8211;inherit</code> &lt;file&gt;</p>
<dl>
<dt>
<dd> Create a new pool of the same size and other properties as <code>&lt;file&gt;.</code></dl>
<p> <code>-v, &#8211;verbose</code></p>
<dl>
<dt>
<dd> Increase verbosity level.</dl>
<p> <code>-h, &#8211;help</code></p>
<dl>
<dt>
<dd> Display help message and exit.</dl>
<h3>Options for PMEMBLK:</h3>
<p> By default when creating a pmem <code>blk</code> pool, the <code>BTT</code> layout is <i>not</i> written until the first <i>write operation</i> of block entry is performed. Using <code>-w</code> option you can force writing the <code>BTT</code> layout. Please refer to <code><a href="/docs/linux/man/3-libpmemblk/">libpmemblk</a></code>(3) for details. </p>
<p> <code>-w, &#8211;write-layout</code></p>
<dl>
<dt>
<dd> Force writing the <code>BTT</code> layout.</dl>
<h3>Options for PMEMOBJ:</h3>
<p> By default when creating a pmem <code>obj</code> pool, the layout name provided to the <code>libpmemobj</code> library is an empty string. Please refer to <code><a href="/docs/linux/man/3-libpmemobj/">libpmemobj</a></code>(3) for details. </p>
<p> <code>-l, &#8211;layout &lt;layout&gt;</code></p>
<dl>
<dt>
<dd> Layout name of the <code>pmemobj</code> pool.</dl>
<h2>EXAMPLES</h2>
<dl>
<dt>pmempool create blk 512 pool.blk</p>
<dd> # Create a blk pool file of minimum allowed size and block size 512 bytes</p>
<dt>pmempool create log -M pool.log</p>
<dd> # Create a log pool file of maximum allowed size</p>
<dt>pmempool create blk &#8211;size=4G &#8211;write-layout 1K pool.blk</p>
<dd> # Create a blk pool file of size 4G, block size 1K and write the BTT layout</p>
<dt>pmempool create &#8211;layout my_layout obj pool.obj</p>
<dd> # Create an obj pool file of minimum allowed size and layout &#8216;my_layout&#8217;</p>
<dt>pmempool create &#8211;inherit=pool.log new_pool.log</p>
<dd> # Create a pool file based on pool.log file</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-libpmemblk/">libpmemblk</a>(3) <a href="/docs/linux/man/3-libpmemlog/">libpmemlog</a>(3) <a href="/docs/linux/man/1-pmempool/">pmempool</a>(1)</code></p>
<h2>PMEMPOOL</h2>
<p> Part of the <code><a href="/docs/linux/man/1-pmempool/">pmempool</a>(1)</code> suite. </p>
<h2>Index</h2>
