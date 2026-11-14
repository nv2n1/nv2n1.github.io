---
title: "slabinfo(5)"
name: "slabinfo"
section: "5"
letter: "s"
url: "/docs/linux/man/5-slabinfo/"
description: "slabinfo – kernel slab allocator statistics"
---

<p>slabinfo &#8211; kernel slab allocator statistics</p>
<h2>Synopsis</h2>
<p><code>cat /proc/slabinfo</code></p>
<h2>Description</h2>
<p>Frequently used objects in the Linux kernel (buffer heads, inodes, dentries, etc.) have their own cache. The file <i>/proc/slabinfo</i> gives statistics on these caches. The following (edited) output shows an example of the contents of this file: </p>
<p> $ <code>sudo cat /proc/slabinfo</code> slabinfo &#8211; version: 2.1 # name &lt;active_objs&gt; &lt;num_objs&gt; &lt;objsize&gt; &lt;objperslab&gt; &lt;pagesperslab&gt; &#8230; sigqueue 100 100 160 25 1 : tunables 0 0 0 : slabdata 4 4 0 sighand_cache 355 405 2112 15 8 : tunables 0 0 0 : slabdata 27 27 0 kmalloc-8192 96 96 8192 4 8 : tunables 0 0 0 : slabdata 24 24 0 &#8230; </p>
<p> The first line of output includes a version number, which allows an application that is reading the file to handle changes in the file format. (See VERSIONS, below.) The next line lists the names of the columns in the remaining lines. </p>
<p> Each of the remaining lines displays information about a specified cache. Following the cache name, the output shown in each line shows three components for each cache:</p>
<dl>
<dt>*</p>
<dd>statistics</p>
<dt>*</p>
<dd>tunables</p>
<dt>*</p>
<dd>slabdata</dl>
<p> The statistics are as follows:</p>
<dl>
<dt><i>active_objs</i></p>
<dd>The number of objects that are currently active (i.e., in use).</p>
<dt><i>num_objs</i></p>
<dd>The total number of allocated objects (i.e., objects that are both in use and not in use).</p>
<dt><i>objsize</i></p>
<dd>The size of objects in this slab, in bytes.</p>
<dt><i>objperslab</i></p>
<dd>The number of objects stored in each slab.</p>
<dt><i>pagesperslab</i></p>
<dd>The number of pages allocated for each slab.</dl>
<p> The <i>tunables</i> entries in each line show tunable parameters for the corresponding cache. When using the default SLUB allocator, there are no tunables, the <i>/proc/slabinfo</i> file is not writable, and the value 0 is shown in these fields. When using the older SLAB allocator, the tunables for a particular cache can be set by writing lines of the following form to <i>/proc/slabinfo</i>: </p>
<p> # <code>echo &#8216;name limit batchcount sharedfactor&#8217; &gt; /proc/slabinfo</code> </p>
<p> Here, <i>name</i> is the cache name, and <i>limit</i>, <i>batchcount</i>, and <i>sharedfactor</i> are integers defining new values for the corresponding tunables. The <i>limit</i> value should be a positive value, <i>batchcount</i> should be a positive value that is less than or equal to <i>limit</i>, and <i>sharedfactor</i> should be nonnegative. If any of the specified values is invalid, the cache settings are left unchanged. </p>
<p> The <i>tunables</i> entries in each line contain the following fields:</p>
<dl>
<dt><i>limit</i></p>
<dd>The maximum number of objects that will be cached.</p>
<dt><i>batchcount</i></p>
<dd>On SMP systems, this specifies the number of objects to transfer at one time when refilling the available object list.</p>
<dt><i>sharedfactor</i></p>
<dd>[To be documented]</dl>
<p> The <i>slabdata</i> entries in each line contain the following fields:</p>
<dl>
<dt><i>active_slabs</i></p>
<dd>The number of active slabs.</p>
<dt><i>nums_slabs</i></p>
<dd>The total number of slabs.</p>
<dt><i>sharedavail</i></p>
<dd>[To be documented]</dl>
<p> Note that because of object alignment and slab cache overhead, objects are not normally packed tightly into pages. Pages with even one in-use object are considered in-use and cannot be freed. </p>
<p> Kernels configured with <code>CONFIG_DEBUG_SLAB</code> will also have additional statistics fields in each line, and the first line of the file will contain the string &quot;(statistics)&quot;. The statistics field include : the high water mark of active objects; the number of times objects have been allocated; the number of times the cache has grown (new pages added to this cache); the number of times the cache has been reaped (unused pages removed from this cache); and the number of times there was an error allocating new pages to this cache.</p>
<h2>Versions</h2>
<p>The <i>/proc/slabinfo</i> file first appeared in Linux 2.1.23. The file is versioned, and over time there have been a number of versions with different layouts:</p>
<dl>
<dt>1.0</p>
<dd>Present throughout the Linux 2.2.x kernel series.</p>
<dt>1.1</p>
<dd>Present in the Linux 2.4.x kernel series.</p>
<dt>1.2</p>
<dd>A format that was briefly present in the Linux 2.5 development series.</p>
<dt>2.0</p>
<dd>Present in Linux 2.6.x kernels up to and including Linux 2.6.9.</p>
<dt>2.1</p>
<dd>The current format, which first appeared in Linux 2.6.10.</dl>
<h2>Notes</h2>
<p>Only root can read and (if the kernel was configured with <code>CONFIG_SLAB</code>) write the <i>/proc/slabinfo</i> file. </p>
<p> The total amount of memory allocated to the SLAB/SLUB cache is shown in the <i>Slab</i> field of <i>/proc/meminfo</i>.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-slabtop/">slabtop</a></code>(1) </p>
<p> The kernel source file <i>Documentation/vm/slub.txt</i> and <i>tools/vm/slabinfo.c</i>.</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
