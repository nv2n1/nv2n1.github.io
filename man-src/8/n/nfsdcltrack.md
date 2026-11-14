---
title: "nfsdcltrack(8)"
name: "nfsdcltrack"
section: "8"
letter: "n"
url: "/docs/linux/man/8-nfsdcltrack/"
description: "nfsdcltrack – NFSv4 Client Tracking Callout Program"
---

<p>nfsdcltrack &#8211; NFSv4 Client Tracking Callout Program</p>
<h2>Synopsis</h2>
<p>nfsdcltrack [-d] [-f] [-s stable storage dir] &lt;command&gt; &lt;args&#8230;&gt;</p>
<h2>Description</h2>
<p>nfsdcltack is the NFSv4 client tracking callout program. It is not necessary to install this daemon on machines that are not acting as NFSv4 servers. </p>
<p> When a network partition is combined with a server reboot, there are edge conditions that can cause the server to grant lock reclaims when other clients have taken conflicting locks in the interim. A more detailed explanation of this issue is described in <font SIZE="-1">RFC</font> 3530, section 8.6.3. </p>
<p> In order to prevent these problems, the server must track a small amount of per-client information on stable storage. This program provides the userspace piece of that functionality. When the kernel needs to manipulate the database that stores this info, it will execute this program to handle it.</p>
<h2>Options</h2>
<dl>
<dt><code>-d</code>, <code>&#8211;debug</code></p>
<dd>Enable debug level logging.</p>
<dt><code>-f</code>, <code>&#8211;foreground</code></p>
<dd>Log to stderr instead of syslog.</p>
<dt><code>-s</code> <i>storagedir</i>, <code>&#8211;storagedir</code>=<i>storage_dir</i></p>
<dd>Directory where stable storage information should be kept. The default value is <i>/var/lib/nfs/nfsdcltrack</i>.</dl>
<h2>Commands</h2>
<p>nfsdcltrack requires a command for each invocation. Supported commands are:</p>
<dl>
<dt><code>init</code></p>
<dd>Initialize the database. This command requires no argument.</p>
<dt><code>create</code></p>
<dd>Create a new client record (or update the timestamp on an existing one). This command requires a hex-encoded nfs_client_id4 as an argument.</p>
<dt><code>remove</code></p>
<dd>Remove a client record from the database. This command requires a hex-encoded nfs_client_id4 as an argument.</p>
<dt><code>check</code></p>
<dd>Check to see if a nfs_client_id4 is allowed to reclaim. This command requires a hex-encoded nfs_client_id4 as an argument.</p>
<dt><code>gracedone</code></p>
<dd>Remove any unreclaimed client records from the database. This command requires a epoch boot time as an argument.</dl>
<h2>External Configuration</h2>
<p>The directory for stable storage information can be set via the file <code>/etc/nfs.conf</code> by setting the <code>storagedir</code> value in the <code>nfsdcltrack</code> section. For example: [nfsdcltrack] </p>
<p>&nbsp;<wbr>&nbsp;<wbr>storagedir&nbsp;<wbr>=&nbsp;<wbr>/shared/nfs/nfsdcltrack Debuging to syslog can also be enabled by setting &quot;debug = 1&quot; in this file.</p>
<h2>Legacy Transition Mechanism</h2>
<p>The Linux kernel NFSv4 server has historically tracked this information on stable storage by manipulating information on the filesystem directly, in the directory to which <i>/proc/fs/nfsd/nfsv4recoverydir</i> points. If the kernel passes the correct information, then nfsdcltrack can use it to allow a seamless transition from the old client tracking scheme to the new one. </p>
<p> On a <code>check</code> operation, if there is no record of the client in the database, nfsdcltrack will look to see if the <font SIZE="-1"><code>NFSDCLTRACK_LEGACY_RECDIR</code></font> environment variable is set. If it is, then it will fetch that value and see if a directory exists by that name. If it does, then the check operation will succeed and the directory will be removed. </p>
<p> On a <code>gracedone</code> operation, nfsdcltrack will look to see if the <font SIZE="-1"><code>NFSDCLTRACK_LEGACY_TOPDIR</code></font> environment variable is set. If it is, then it will attempt to clean out that directory prior to exiting. </p>
<p> Note that this transition is one-way. If the machine subsequently reboots back into an older kernel that does not support the nfsdcltrack upcall then the clients will not be able to recover their state.</p>
<h2>Notes</h2>
<p>This program requires a kernel that supports the nfsdcltrack usermodehelper upcall. This support was first added to mainline kernels in 3.8.</p>
<h2>Authors</h2>
<p>nfsdcltrack was developed by Jeff Layton &lt;jlayton [at] redhat.com&gt;.</p>
