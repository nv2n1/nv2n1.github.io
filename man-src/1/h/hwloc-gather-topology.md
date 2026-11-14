---
title: "hwloc-gather-topology(1)"
name: "hwloc-gather-topology"
section: "1"
letter: "h"
url: "/docs/linux/man/1-hwloc-gather-topology/"
description: "hwloc-gather-topology – Saves the relevant Linux topology files and the lstopo output for later (possibly offline) usage"
---

<h2>NAME</h2>
<p> hwloc-gather-topology &#8211; Saves the relevant Linux topology files and the lstopo output for later (possibly offline) usage</p>
<h2>SYNOPSIS</h2>
<p> <code>hwloc-gather-topology [</code><i>options</i>] <i>&lt;path&gt;</i></p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;io</code></p>
<dd> Also gather I/O related files. The gathering may be much slower, and the generated archive may be much bigger. <code>&#8211;dmi</code> Also gather DMI/SMBIOS related files. The gathering requires root access, and the dmi-sysfs kernel module should be loaded.</p>
<dt><code>-h</code> <code>&#8211;help</code></p>
<dd> Display help message and exit</dl>
<h2>DESCRIPTION</h2>
<p> <code>hwloc-gather-topology</code> saves all the relevant topology files into an archive (<code>&lt;path&gt;.tar.bz2</code>) and the lstopo output (<code>&lt;path&gt;.output</code>). The utility for example stores the <code>/proc/cpuinfo</code> file and the entire <code>/sys/devices/system/node/</code> directory tree. </p>
<p> These files can be used later to explore the machine topology offline. Once the tarball has been extracted, it may for instance be given to some hwloc command-line utilities through their <code>&#8211;input</code> option. It is also possible to override the default topology that the hwloc library will read by setting the extracted path in the <code>HWLOC_FSROOT</code> environment variable. </p>
<p> Both archive and lstopo output may also be submitted to hwloc developers to debug issues remotely. </p>
<p> <code>hwloc-gather-topology</code> is a Linux specific tool, it is not installed on other operating systems. </p>
<p> <code>NOTE:</code> It is highly recommended that you read the <a href="/docs/linux/man/7-hwloc/">hwloc</a>(7) overview page before reading this man page.</p>
<h2>EXAMPLES</h2>
<p> To store topology information to be used later (possibly on a different host) please run: </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>hwloc-gather-topology /tmp/myhost</p>
<p> It will store all relevant topology files in the <code>/tmp/myhost.tar.bz2</code> archive and the lstopo output in the <code>/tmp/myhost.output</code> file. These files can be transferred on another host for later/offline analysis and/or as the input to various hwloc utilities. </p>
<p> To use these data with hwloc utilities you have to unpack <code>myhost.tar.bz2</code> archive first: </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>tar jxvf /tmp/myhost.tar.bz2</p>
<p> A new directory named <code>myhost</code> now contains all topology files. Then you ask various hwloc utilities to use this topology instead of the one of the real machine by passing <code>&#8211;input myhost</code>. To display the topology just run: </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>lstopo &#8211;input ./myhost</p>
<p> It is not necessary that the topology is extracted in the current directory, absolute or relative paths are also supported: </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>lstopo &#8211;input /path/to/remote/host/extracted/topology/</p>
<p> To see how hwloc would distribute 8 parallel jobs on the original host: </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>hwloc-distrib &#8211;input myhost &#8211;single 8</p>
<p> To get the corresponding physical indexes in the previous command: </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>hwloc-calc &#8211;input myhost &#8211;po &#8211;li &#8211;proclist $(hwloc-distrib &#8211;input myhost &#8211;single 8)</p>
<p> Any program may actually override the default topology with a given archived one even if it does not have a <code>&#8211;input</code> option. The <code>HWLOC_FSROOT</code> environment variable should be used to do so: </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>HWLOC_FSROOT=myhost hwloc-calc &#8211;po &#8211;li &#8211;proclist $(hwloc-distrib &#8211;single 8)</p>
<p> All these commands will produce the same output as if executed directly on the host on which the topology information was originally gathered by the <code>hwloc-gather-topology</code> script.</p>
<h2>RETURN VALUE</h2>
<p> Upon successful execution, <code>hwloc-gather-topology</code> will exit with the code 0. </p>
<p> <code>hwloc-gather-topology</code> will return nonzero exit status if any kind of error occurs, such as (but not limited to) failure to create the archive or output file.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/7-hwloc/">hwloc</a>(7), <a href="/docs/linux/man/1-lstopo/">lstopo</a>(1), <a href="/docs/linux/man/1-hwloc-calc/">hwloc-calc</a>(1), <a href="/docs/linux/man/1-hwloc-distrib/">hwloc-distrib</a>(1) </p>
<h2>Index</h2>
