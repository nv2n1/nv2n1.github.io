---
title: "ceph-syn(8)"
name: "ceph-syn"
section: "8"
letter: "c"
url: "/docs/linux/man/8-ceph-syn/"
description: "ceph-syn – ceph synthetic workload generator"
---

<p>ceph-syn &#8211; ceph synthetic workload generator</p>
<h2>Synopsis</h2>
<pre><code>ceph-syn</code> [ -m <i>monaddr</i>:<i>port</i> ] --syn <i>command</i> <i>...</i></pre>
<h2>Description</h2>
<p><code>ceph-syn</code> is a simple synthetic workload generator for the Ceph distributed file system. It uses the userspace client library to generate simple workloads against a currently running file system. The file system need not be mounted via <a href="/docs/linux/man/8-ceph-fuse/">ceph-fuse</a>(8) or the kernel client. </p>
<p> One or more <code>&#8211;syn</code> command arguments specify the particular workload, as documented below.</p>
<h2>Options</h2>
<dl>
<dt><code>-d</code></p>
<dd>Detach from console and daemonize after startup.</p>
<dt><code>-c ceph.conf, &#8211;conf=ceph.conf</code></p>
<dd>Use <i>ceph.conf</i> configuration file instead of the default <code>/etc/ceph/ceph.conf</code> to determine monitor addresses during startup.</p>
<dt><code>-m monaddress[:port]</code></p>
<dd>Connect to specified monitor (instead of looking through <code>ceph.conf</code>).</p>
<dt><code>&#8211;num_client num</code></p>
<dd>Run num different clients, each in a separate thread.</p>
<dt><code>&#8211;syn workloadspec</code></p>
<dd>Run the given workload. May be specified as many times as needed. Workloads will normally run sequentially.</dl>
<h2>Workloads</h2>
<p>Each workload should be preceded by <code>&#8211;syn</code> on the command line. This is not a complete list.</p>
<dl>
<dt><code>mknap</code> <i>path</i> <i>snapname</i></p>
<dd>Create a snapshot called <i>snapname</i> on <i>path</i>.</p>
<dt><code>rmsnap</code> <i>path</i> <i>snapname</i></p>
<dd>Delete snapshot called <i>snapname</i> on <i>path</i>.</p>
<dt><code>rmfile</code> <i>path</i></p>
<dd>Delete/unlink <i>path</i>.</p>
<dt><code>writefile</code> <i>sizeinmb</i> <i>blocksize</i></p>
<dd>Create a file, named after our client id, that is <i>sizeinmb</i> MB by writing <i>blocksize</i> chunks.</p>
<dt><code>readfile</code> <i>sizeinmb</i> <i>blocksize</i></p>
<dd>Read file, named after our client id, that is <i>sizeinmb</i> MB by writing <i>blocksize</i> chunks.</p>
<dt><code>rw</code> <i>sizeinmb</i> <i>blocksize</i></p>
<dd>Write file, then read it back, as above.</p>
<dt><code>makedirs</code> <i>numsubdirs</i> <i>numfiles</i> <i>depth</i></p>
<dd>Create a hierarchy of directories that is <i>depth</i> levels deep. Give each directory <i>numsubdirs</i> subdirectories and <i>numfiles</i> files.</p>
<dt><code>walk</code></p>
<dd>Recursively walk the file system (like find).</dl>
<h2>Availability</h2>
<p><code>ceph-syn</code> is part of Ceph, a massively scalable, open-source, distributed storage system. Please refer to the Ceph documentation at <i><a rel="nofollow" href="http://ceph.com/docs">http://ceph.com/docs</a></i> for more information.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-ceph/">ceph</a></code>(8), <code><a href="/docs/linux/man/8-ceph-fuse/">ceph-fuse</a></code>(8)</p>
<h2>Copyright</h2>
<p>2010-2014, Inktank Storage, Inc. and contributors. Licensed under Creative Commons BY-SA</p>
