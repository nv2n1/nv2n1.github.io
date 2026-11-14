---
title: "nfsd(7)"
name: "nfsd"
section: "7"
letter: "n"
url: "/docs/linux/man/7-nfsd/"
description: "nfsd – special filesystem for controlling Linux NFS server"
---

<p>nfsd &#8211; special filesystem for controlling Linux NFS server</p>
<h2>Synposis</h2>
<p><code>mount -t nfsd nfsd /proc/fs/nfsd</code></p>
<h2>Description</h2>
<p>The <code>nfsd</code> filesystem is a special filesystem which provides access to the Linux NFS server. The filesystem consists of a single directory which contains a number of files. These files are actually gateways into the NFS server. Writing to them can affect the server. Reading from them can provide information about the server. </p>
<p> This file system is only available in Linux 2.6 and later series kernels (and in the later parts of the 2.5 development series leading up to 2.6). This man page does not apply to 2.4 and earlier. </p>
<p> As well as this filesystem, there are a collection of files in the <code>procfs</code> filesystem (normally mounted at <code>/proc</code>) which are used to control the NFS server. This manual page describes all of these files. </p>
<p> The <i>exportfs</i> and <i>mountd</i> programs (part of the nfs-utils package) expect to find this filesystem mounted at <code>/proc/fs/nfsd</code> or <code>/proc/fs/nfs</code>. If it is not mounted, they will fall-back on 2.4 style functionality. This involves accessing the NFS server via a systemcall. This systemcall is scheduled to be removed after the 2.6 kernel series.</p>
<h2>Details</h2>
<p>The three files in the <code>nfsd</code> filesystem are:</p>
<dl>
<dt><code>exports</code></p>
<dd>This file contains a list of filesystems that are currently exported and clients that each filesystem is exported to, together with a list of export options for that client/filesystem pair. This is similar to the <code>/proc/fs/nfs/exports</code> file in 2.4. One difference is that a client doesn&#8217;t necessarily correspond to just one host. It can respond to a large collection of hosts that are being treated identically. </p>
<p> Each line of the file contains a path name, a client name, and a number of options in parentheses. Any space, tab, newline or back-slash character in the path name or client name will be replaced by a backslash followed by the octal ASCII code for that character. </p>
<dt><code>threads</code></p>
<dd>This file represents the number of <code>nfsd</code> thread currently running. Reading it will show the number of threads. Writing an ASCII decimal number will cause the number of threads to be changed (increased or decreased as necessary) to achieve that number. </p>
<dt><code>filehandle</code></p>
<dd>This is a somewhat unusual file in that what is read from it depends on what was just written to it. It provides a transactional interface where a program can open the file, write a request, and read a response. If two separate programs open, write, and read at the same time, their requests will not be mixed up. </p>
<p> The request written to <code>filehandle</code> should be a client name, a path name, and a number of bytes. This should be followed by a newline, with white-space separating the fields, and octal quoting of special characters. </p>
<p> On writing this, the program will be able to read back a filehandle for that path as exported to the given client. The filehandle&#8217;s length will be at most the number of bytes given. </p>
<p> The filehandle will be represented in hex with a leading &#8216;
