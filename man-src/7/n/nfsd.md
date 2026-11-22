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
<dt><code>exports</code></dt>
<dd>This file contains a list of filesystems that are currently exported and clients that each filesystem is exported to, together with a list of export options for that client/filesystem pair. This is similar to the <code>/proc/fs/nfs/exports</code> file in 2.4. One difference is that a client doesn&#8217;t necessarily correspond to just one host. It can respond to a large collection of hosts that are being treated identically. </dd>
<p> Each line of the file contains a path name, a client name, and a number of options in parentheses. Any space, tab, newline or back-slash character in the path name or client name will be replaced by a backslash followed by the octal ASCII code for that character. </p>
<dt><code>threads</code></dt>
<dd>This file represents the number of <code>nfsd</code> thread currently running. Reading it will show the number of threads. Writing an ASCII decimal number will cause the number of threads to be changed (increased or decreased as necessary) to achieve that number. </dd>
<dt><code>filehandle</code></dt>
<dd>This is a somewhat unusual file in that what is read from it depends on what was just written to it. It provides a transactional interface where a program can open the file, write a request, and read a response. If two separate programs open, write, and read at the same time, their requests will not be mixed up. </dd>
<p> The request written to <code>filehandle</code> should be a client name, a path name, and a number of bytes. This should be followed by a newline, with white-space separating the fields, and octal quoting of special characters. </p>
<p> On writing this, the program will be able to read back a filehandle for that path as exported to the given client. The filehandle&#8217;s length will be at most the number of bytes given. </p>
<p> The filehandle will be represented in hex with a leading &#8216;\x&#8217;. </dl>
 </p>
<p> The directory <code>/proc/net/rpc</code> in the <code>procfs</code> filesystem contains a number of files and directories. The files contain statistics that can be display using the <i>nfsstat</i> program. The directories contain information about various caches that the NFS server maintains to keep track of access permissions that different clients have for different filesystems. The caches are: </p>
<dl>
<dt><code>auth.unix.ip</code></dt>
<dd> <p> This cache contains a mapping from IP address to the name of the authentication domain that the ipaddress should be treated as part of. </p>
 </dd>
<dt><code>nfsd.export</code></dt>
<dd> <p> This cache contains a mapping from directory and domain to export options. </p>
 </dd>
<dt><code>nfsd.fh</code></dt>
<dd> <p> This cache contains a mapping from domain and a filesystem identifier to a directory. The filesystem identifier is stored in the filehandles and consists of a number indicating the type of identifier and a number of hex bytes indicating the content of the identifier. </p>
 </dd></dl>
<p> Each directory representing a cache can hold from 1 to 3 files. They are: </p>
<dl>
<dt><code>flush</code></dt>
<dd> <p> When a number of seconds since epoch (1 Jan 1970) is written to this file, all entries in the cache that were last updated before that file become invalidated and will be flushed out. Writing a time in the future (in seconds since epoch) will flush everything. This is the only file that will always be present. </p>
 </dd>
<dt><code>content</code></dt>
<dd> <p> This file, if present, contains a textual representation of ever entry in the cache, one per line. If an entry is still in the cache (because it is actively being used) but has expired or is otherwise invalid, it will be presented as a comment (with a leading hash character). </p>
 </dd>
<dt><code>channel</code></dt>
<dd> <p> This file, if present, acts a channel for request from the kernel-based nfs server to be passed to a user-space program for handling. </p>
<p> When the kernel needs some information which isn&#8217;t in the cache, it makes a line appear in the <code>channel</code> file giving the key for the information. A user-space program should read this, find the answer, and write a line containing the key, an expiry time, and the content. For example the kernel might make <br/>
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> nfsd 127.0.0.1 <br/>
 appear in the <code>auth.unix.ip/content</code> file. The user-space program might then write <br/>
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> nfsd 127.0.0.1 1057206953 localhost <br/>
 to indicate that 127.0.0.1 should map to localhost, at least for now. </p>
<p> If the program uses <a href="/docs/linux/man/2-select/">select</a>(2) or <a href="/docs/linux/man/2-poll/">poll</a>(2) to discover if it can read from the <code>channel</code> then it will never see and end-of-file but when all requests have been answered, it will block until another request appears. </p>
 </dd></dl>
<p> In the <code>/proc</code> filesystem there are 4 files that can be used to enabled extra tracing of nfsd and related code. They are: <code>/proc/sys/sunrpc/nfs_debug</code> <br/>
 <code>/proc/sys/sunrpc/nfsd_debug</code> <br/>
 <code>/proc/sys/sunrpc/nlm_debug</code> <br/>
 <code>/proc/sys/sunrpc/rpc_debug</code> <br/>
 They control tracing for the NFS client, the NFS server, the Network Lock Manager (lockd) and the underlying RPC layer respectively. Decimal numbers can be read from or written to these files. Each number represents a bit-pattern where bits that are set cause certain classes of tracing to be enabled. Consult the kernel header files to find out what number correspond to what tracing. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-rpc.nfsd/">rpc.nfsd</a></code>(8), <code><a href="/docs/linux/man/5-exports/">exports</a></code>(5), <code><a href="/docs/linux/man/8-nfsstat/">nfsstat</a></code>(8), <code><a href="/docs/linux/man/8-mountd/">mountd</a></code>(8) <code><a href="/docs/linux/man/8-exportfs/">exportfs</a></code>(8). </p>
<h2>AUTHOR</h2>
<p> NeilBrown </p>
