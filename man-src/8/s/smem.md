---
title: "smem(8)"
name: "smem"
section: "8"
letter: "s"
url: "/docs/linux/man/8-smem/"
description: "smem – Report memory usage with shared memory divided proportionally."
---

<p>smem &#8211; Report memory usage with shared memory divided proportionally.</p>
<h2>Synopsis</h2>
<p><code>smem</code> [<i>options</i>] </p>
<h2>Description</h2>
<p><code>smem</code> reports physical memory usage, taking shared memory pages into account. Unshared memory is reported as the USS (Unique Set Size). Shared memory is divided evenly among the processes sharing that memory. The unshared memory (USS) plus a process&#8217;s proportion of shared memory is reported as the PSS (Proportional Set Size). The USS and PSS only include physical memory usage. They do not include memory that has been swapped out to disk. Memory can be reported by process, by user, by mapping, or systemwide. Both text mode and graphical output are available. </p>
<h2>Options</h2>
<h3>General Options</h3>
<dl>
<dt><code>-h, &#8211;help</code></p>
<dd>Show help. </p>
</dl>
<h3>Source Data</h3>
<p>By default, smem will pull most of the data it needs from the /proc filesystem of the system it is running on. The &#8211;source option lets you used a tarred set of /proc data saved earlier, possibly on a different machine. The &#8211;kernel and &#8211;realmem options let you specify a couple things that smem cannot discover on its own. </p>
<dl>
<dt><code>-K </code><i>KERNEL</i><code>, &#8211;kernel=</code><i>KERNEL</i></p>
<dd>Path to an uncompressed kernel image. This lets smem include the size of the kernel&#8217;s code and statically allocated data in the systemwide (-w) output. (To obtain an uncompressed image of a kernel on disk, you may need to build the kernel yourself, then locate file vmlinux in the source tree.) </p>
<dt><code>-R </code><i>REALMEM</i><code>, &#8211;realmem=</code><i>REALMEM</i></p>
<dd>Amount of physical RAM. This lets smem detect the amount of memory used by firmware/hardware in the systemwide (-w) output. If provided, it will also be used as the total memory size to base percentages on. Example: &#8211;realmem=1024M </p>
<dt><code>-S </code><i>SOURCE</i><code>, &#8211;source=</code><i>SOURCE</i></p>
<dd>/proc data source. This lets you specify an alternate source of the /proc data. For example, you can capture data from an embedded system using smemcap, and parse the data later on a different machine. If the &#8211;source option is not included, smem reports memory usage on the running system. </p>
</dl>
<h3>Report By</h3>
<p>If none of the following options are included, smem reports memory usage by process. </p>
<dl>
<dt><code>-m, &#8211;mappings</code></p>
<dd>Report memory usage by mapping. </p>
<dt><code>-u, &#8211;users</code></p>
<dd>Report memory usage by user. </p>
<dt><code>-w, &#8211;system</code></p>
<dd>Report systemwide memory usage summary. </p>
</dl>
<h3>Filter By</h3>
<p>If none of these options are included, memory usage is reported for all processes, users, or mappings. (Note: If you are running as a non-root user, and if you are not using the &#8211;source options, then you will only see data from processes whose /proc/ information you have access to.) </p>
<dl>
<dt><code>-M </code><i>MAPFILTER</i><code>, &#8211;mapfilter=</code><i>MAPFILTER</i></p>
<dd>Mapping filter regular expression. </p>
<dt><code>-P </code><i>PROCESSFILTER</i><code>, &#8211;processfilter=</code><i>PROCESSFILTER</i></p>
<dd>Process filter regular expression. </p>
<dt><code>-U </code><i>USERFILTER</i><code>, &#8211;userfilter=</code><i>USERFILTER</i></p>
<dd>User filter regular expression. </p>
</dl>
<h3>Output Formatting</h3>
<dl>
<dt><code>-c </code><i>COLUMNS</i><code>, &#8211;columns=</code><i>COLUMNS</i></p>
<dd>Columns to show. </p>
<dt><code>-H, &#8211;no-header</code></p>
<dd>Disable header line. </p>
<dt><code>-k, &#8211;abbreviate</code></p>
<dd>Show unit suffixes. </p>
<dt><code>-n, &#8211;numeric</code></p>
<dd>Show numeric user IDs instead of usernames. </p>
<dt><code>-p, &#8211;percent</code></p>
<dd>Show percentages. </p>
<dt><code>-r, &#8211;reverse</code></p>
<dd>Reverse sort. </p>
<dt><code>-s </code><i>SORT</i><code>, &#8211;sort=</code><i>SORT</i></p>
<dd>Field to sort on. </p>
<dt><code>-t, &#8211;totals</code></p>
<dd>Show totals. </p>
</dl>
<h3>Output Type</h3>
<p>These options specify graphical output styles. </p>
<dl>
<dt><code>&#8211;bar=</code><i>BAR</i></p>
<dd>Show bar graph. </p>
<dt><code>&#8211;pie=</code><i>PIE</i></p>
<dd>Show pie graph. </p>
</dl>
<h2>Requirements</h2>
<p><code>smem</code> requires: </p>
<dl>
<dt>&bull;</p>
<dd>Linux kernel providing &#8216;Pss&#8217; metric in /proc/&lt;pid&gt;/smaps (generally 2.6.27 or newer).</p>
<dt>&bull;</p>
<dd>Python 2.x (at least 2.4 or so).</p>
<dt>&bull;</p>
<dd>The matplotlib library (only if you want to generate graphical charts). </p>
</dl>
<h2>Embedded Usage</h2>
<p>To capture memory statistics on resource-constrained systems, the the <code>smem</code> source includes a utility named <code>smemcap</code>. <code>smemcap</code> captures all /proc entries required by <code>smem</code> and outputs them as an uncompressed .tar file to STDOUT. <code>smem</code> can analyze the output using the <code>&#8211;source</code> option. <code>smemcap</code> is small and does not require Python. </p>
<p> To use <code>smemcap</code>:</p>
<dl>
<dt>1.</p>
<dd>Obtain the smem source at <a rel="nofollow" href="http://selenic.com/repo/smem">http://selenic.com/repo/smem</a></p>
<dt>2.</p>
<dd>Compile <i>smemcap.c</i> for your target system.</p>
<dt>3.</p>
<dd>Run <code>smemcap</code> on the target system and save the output:<br />
 smemcap &gt; memorycapture.tar</p>
<dt>4.</p>
<dd>Copy the output to another machine and run smem on it:<br />
 smem -S memorycapture.tar </p>
</dl>
<h2>Files</h2>
<p><i>/proc/$pid/cmdline</i> </p>
<p> <i>/proc/$pid/smaps</i> </p>
<p> <i>/proc/$pid/stat</i> </p>
<p> <i>/proc/meminfo</i> </p>
<p> <i>/proc/version</i></p>
<h2>Resources</h2>
<p>Main Web Site: <a rel="nofollow" href="http://www.selenic.com/smem">http://www.selenic.com/smem</a> </p>
<p> Source code repository: <a rel="nofollow" href="http://selenic.com/repo/smem">http://selenic.com/repo/smem</a> </p>
<p> Mailing list: <a rel="nofollow" href="http://selenic.com/mailman/listinfo/smem">http://selenic.com/mailman/listinfo/smem</a></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-free/">free</a></code>(1), <code><a href="/docs/linux/man/1-pmap/">pmap</a></code>(1), <code><a href="/docs/linux/man/5-proc/">proc</a></code>(5), <code><a href="/docs/linux/man/1-ps/">ps</a></code>(1), <code><a href="/docs/linux/man/1-top/">top</a></code>(1), <code><a href="/docs/linux/man/8-vmstat/">vmstat</a></code>(8) </p>
<h2>Copying</h2>
<p>Copyright (C) 2008-2009 Matt Mackall. Free use of this software is granted under the terms of the GNU General Public License version 2 or later.</p>
<h2>Author</h2>
<p><code>smem</code> was written by Matt Mackall.</p>
