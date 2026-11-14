---
title: "nfsstat(8)"
name: "nfsstat"
section: "8"
letter: "n"
url: "/docs/linux/man/8-nfsstat/"
description: "nfsstat – list NFS statistics"
---

<p>nfsstat &#8211; list NFS statistics</p>
<h2>Synopsis</h2>
<p><code>nfsstat</code> [<i>OPTION</i>]&#8230;</p>
<h2>Description</h2>
<p>The <code>nfsstat</code> displays statistics kept about NFS client and server activity.</p>
<h2>Options</h2>
<dl>
<dt><code>-s, &#8211;server</code></p>
<dd>Print only server-side statistics. The default is to print both server and client statistics.</p>
<dt><code>-c, &#8211;client</code></p>
<dd>Print only client-side statistics.</p>
<dt><code>-n, &#8211;nfs</code></p>
<dd>Print only NFS statistics. The default is to print both NFS and RPC information.</p>
<dt><code>-2</code></p>
<dd>Print only NFS v2 statistics. The default is to only print information about the versions of <code>NFS</code> that have non-zero counts.</p>
<dt><code>-3</code></p>
<dd>Print only NFS v3 statistics. The default is to only print information about the versions of <code>NFS</code> that have non-zero counts.</p>
<dt><code>-4</code></p>
<dd>Print only NFS v4 statistics. The default is to only print information about the versions of <code>NFS</code> that have non-zero counts.</p>
<dt><code>-m, &#8211;mounts</code></p>
<dd>Print information about each of the mounted <code>NFS</code> file systems. </p>
<p> If this option is used, all other options are ignored.</p>
<dt><code>-r, &#8211;rpc</code></p>
<dd>Print only RPC statistics.</p>
<dt><code>-o</code><i> facility</i></p>
<dd>Display statistics for the specified facility, which must be one of:</p>
<dl>
<dd>
<dl>
<dt><code>nfs</code></p>
<dd>NFS protocol information, split up by RPC call.</p>
<dt><code>rpc</code></p>
<dd>General RPC information.</p>
<dt><code>net</code></p>
<dd>Network layer statistics, such as the number of received packets, number of TCP connections, etc.</p>
<dt><code>fh</code></p>
<dd>Usage information on the server&#8217;s file handle cache, including the total number of lookups, and the number of hits and misses.</p>
<dt><code>rc</code></p>
<dd>Usage information on the server&#8217;s request reply cache, including the total number of lookups, and the number of hits and misses.</p>
<dt><code>all</code></p>
<dd>Display all of the above facilities.</dl>
</dl>
<dt><code>-v, &#8211;verbose</code></p>
<dd>This is equivalent to <code>-o all</code>.</p>
<dt><code>-l, &#8211;list</code></p>
<dd>Print information in list form.</p>
<dt><code>-S, &#8211;since </code><i>file</i></p>
<dd>Instead of printing current statistics, <code>nfsstat</code> imports statistics from <i>file</i> and displays the difference between those and the current statistics. Valid input <i>file</i>s may be in the form of <code>/proc/net/rpc/nfs</code> (raw client stats), <code>/proc/net/rpc/nfsd</code> (raw server stats), or saved output from <code>nfsstat</code> itself (client and/or server stats). Any statistics missing from a saved <code>nfsstat</code> output <i>file</i> are treated as zeroes.</p>
<dt><code>-Z[interval], &#8211;sleep=[interval]</code></p>
<dd>Instead of printing current statistics and immediately exiting, <code>nfsstat</code> takes a snapshot of the current statistics and pauses until it receives <code>SIGINT</code> (typically from <code>Ctrl-C</code>), at which point it takes another snapshot and displays the difference between the two. If <i>interval</i> is specified, <code>nfsstat</code> will print the number of <code>NFS</code> calls made since the previous report. Stats will be printed repeatedly every <i>interval</i> seconds.</dl>
<h2>Examples</h2>
<dl>
<dt><code>nfsstat -o all -234</code></p>
<dd>Show all information about all versions of <code>NFS</code>.</p>
<dt><code>nfsstat &#8211;verbose -234</code></p>
<dd>Same as above.</p>
<dt><code>nfsstat -o all</code></p>
<dd>Show all information about active versions of <code>NFS</code>.</p>
<dt><code>nfsstat &#8211;nfs &#8211;server -3</code></p>
<dd>Show statistics for <code>NFS</code> version 3 server.</p>
<dt><code>nfsstat -m</code></p>
<dd>Show information about mounted <code>NFS</code> filesystems.</dl>
<h2>Display</h2>
<p>The <code>Flags</code> output from the <code>-m</code> option is the same as the flags give to the <code>mount</code> command.</p>
<h2>Files</h2>
<dl>
<dt><code>/proc/net/rpc/nfsd</code></p>
<dd><code>procfs</code>-based interface to kernel NFS server statistics.</p>
<dt><code>/proc/net/rpc/nfs</code></p>
<dd><code>procfs</code>-based interface to kernel NFS client statistics.</p>
<dt><code>/proc/mounts</code></p>
<dd><code>procfs</code>-based interface to the mounted filesystems.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-rpc-nfsd/">rpc.nfsd</a></code>(8). <code><a href="/docs/linux/man/5-nfs/">nfs</a></code>(5).</p>
<h2>Bugs</h2>
<p>The default output has been changed. To get the old default output you must run <code>nfsstat &#8211;auto -2</code>. </p>
<p> The function of the <code>-v</code> and <code>-a</code> options have changed. The <code>-a</code> option is now reserved for future use. The <code>-v</code> does what the <code>-a</code> option used to do, and the new <code>-[234]</code> options replace the <code>-v</code> option. </p>
<p> The <code>Display</code> section should be more complete. </p>
<p> Further bugs can be found or reported at <code><a rel="nofollow" href="http://nfs.sf.net/">http://nfs.sf.net/</a></code>.</p>
<h2>Author</h2>
<p>Olaf Kirch, &lt;okir [at] suse.de&gt;</p>
