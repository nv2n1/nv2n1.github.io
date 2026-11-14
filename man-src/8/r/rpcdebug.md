---
title: "rpcdebug(8)"
name: "rpcdebug"
section: "8"
letter: "r"
url: "/docs/linux/man/8-rpcdebug/"
description: "rpcdebug – set and clear NFS and RPC kernel debug flags"
---

<p>rpcdebug &#8211; set and clear NFS and RPC kernel debug flags</p>
<h2>Synopsis</h2>
<p><code>rpcdebug</code> <code>-vh</code><br />
 <code>rpcdebug</code> <code>-m</code> <i>module</i><br />
 <code>rpcdebug</code> <code>-m</code> <i>module</i> <code>-s</code> <i>flags</i>&#8230;<br />
 <code>rpcdebug</code> <code>-m</code> <i>module</i> <code>-c</code> <i>flags</i>&#8230;</p>
<h2>Description</h2>
<p>The <code>rpcdebug</code> command allows an administrator to set and clear the Linux kernel&#8217;s NFS client and server debug flags. Setting these flags causes the kernel to emit messages to the system log in response to NFS activity; this is typically useful when debugging NFS problems. </p>
<p> The first form in the synopsis can be used to list all available debug flags. The second form shows the currently set debug flags for the given module. The third form sets one or more flags, and the fourth form clears one or more flags. </p>
<p> The value <code>all</code> may be used to set or clear all the flags for the given module.</p>
<h2>Options</h2>
<dl>
<dt><code>-c</code></p>
<dd>Clear the given debug flags.</p>
<dt><code>-h</code></p>
<dd>Print a help message and exit. When combined with the <code>-v</code> option, also prints the available debug flags.</p>
<dt><code>-m</code><i> module</i></p>
<dd>Specify which module&#8217;s flags to set or clear. Available modules are:</p>
<dl>
<dd>
<dl>
<dt><code>nfsd</code></p>
<dd>The NFS server.</p>
<dt><code>nfs</code></p>
<dd>The NFS client.</p>
<dt><code>nlm</code></p>
<dd>The Network Lock Manager, in either an NFS client or server.</p>
<dt><code>rpc</code></p>
<dd>The Remote Procedure Call module, in either an NFS client or server.</dl>
</dl>
<dt><code>-s</code></p>
<dd>Set the given debug flags.</p>
<dt><code>-v</code></p>
<dd>Increase the verbosity of <code>rpcdebug</code>&#8216;s output.</dl>
<h2>Files</h2>
<dl>
<dt><code>/proc/sys/sunrpc/{rpc,nfs,nfsd,nlm}_debug</code></p>
<dd>procfs-based interface to kernel debug flags.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-rpc-nfsd/">rpc.nfsd</a></code>(8), <code><a href="/docs/linux/man/5-nfs/">nfs</a></code>(5), <code><a href="/docs/linux/man/8-syslogd/">syslogd</a></code>(8).</p>
<h2>Bugs</h2>
<p>Bugs can be found or reported at <code><a rel="nofollow" href="http://nfs.sf.net/">http://nfs.sf.net/</a></code>.</p>
<h2>Author</h2>
<p>Program by Olaf Kirch &lt;okir [at] suse.de&gt; and &lt;frederic.jolly [at] bull.ext.net&gt;. Manpage by Greg Banks &lt;gnb [at] melbourne.sgi.com&gt;.</p>
