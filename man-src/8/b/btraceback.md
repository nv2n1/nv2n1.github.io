---
title: "btraceback(8)"
name: "btraceback"
section: "8"
letter: "b"
url: "/docs/linux/man/8-btraceback/"
description: "btraceback – wrapper script around gdb and bsmtp"
---

<p>&nbsp;<wbr>btraceback &#8211; wrapper script around gdb and bsmtp</p>
<h2>Synopsis</h2>
<p><code>btraceback </code> <i>/path/to/binary </i> <i>pid</i> </p>
<h2>Description</h2>
<p><code>btraceback</code> is a wrapper shell script around the <code>gdb</code> debugger (or <code>dbx</code> on Solaris systems) and <code>bsmtp</code>, provided for debugging purposes. </p>
<h2>Usage</h2>
<p><code>btraceback</code> is called by the exception handlers of the Bacula daemons during a crash. It can also be called interactively to view the current state of the threads belonging to a process, but this is not recommended unless you are trying to debug a problem (see below).</p>
<h2>Notes</h2>
<p>In order to work properly, debugging symbols must be available to the debugger on the system, and gdb, or dbx (on Solaris systems) must be available in the <code>$PATH</code>. If the Director or Storage daemon runs under a non-root uid, you will probably need to be modify the <code>btraceback</code> script to elevate privileges for the call to <code>gdb</code>/<code>dbx</code>, to ensure it has the proper permissions to debug when called by the daemon. Although Bacula&#8217;s use of <code>btraceback</code> within its exception handlers is always safe, manual or interactive use of <code>btraceback</code> is subject to the same risks than live debugging of any program, which means it could cause Bacula to crash under rare and abnormal circumstances. Consequently we do not recommend manual use of <code>btraceback</code> in production environments unless it is required for debugging a problem. </p>
<h2>Environment</h2>
<p><code>btracback</code> relies on <code>$PATH</code> to find the debugger.</p>
<h2>Files</h2>
<dl>
<dt><i>/usr/lib/bacula/btraceback</i></p>
<dd>
<dl>
<dd>The script itself.</dl>
<dt><i>/usr/sbin/btraceback</i></p>
<dd>
<dl>
<dd>symbolic link to <i>/usr/lib/bacula/btraceback</i></dl>
<dt><i>/etc/bacula/scripts/btraceback.gdb</i></p>
<dd>
<dl>
<dd>the GDB command batch used to output a stack trace</dl>
</dl>
<h2>Author</h2>
<p>This manual page was written by Lucas B. Cohen &lt;lbc [at] members.fsf.org&gt;</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-bsmtp/">bsmtp</a></code>(1) </p>
