---
title: "fuse(4)"
name: "fuse"
section: "4"
letter: "f"
url: "/docs/linux/man/4-fuse/"
description: "fuse – Filesystem in Userspace (FUSE) device"
---

<p>fuse &#8211; Filesystem in Userspace (FUSE) device</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;linux/fuse.h&gt;</code></pre>
<h2>Description</h2>
<p>This device is the primary interface between the FUSE filesystem driver and a user-space process wishing to provide the filesystem (referred to in the rest of this manual page as the <i>filesystem daemon</i>). This manual page is intended for those interested in understanding the kernel interface itself. Those implementing a FUSE filesystem may wish to make use of a user-space library such as <i>libfuse</i> that abstracts away the low-level interface. At its core, FUSE is a simple client-server protocol, in which the Linux kernel is the client and the daemon is the server. After obtaining a file descriptor for this device, the daemon may <code><a href="/docs/linux/man/2-read/">read</a></code>(2) requests from that file descriptor and is expected to <code><a href="/docs/linux/man/2-write/">write</a></code>(2) back its replies. It is important to note that a file descriptor is associated with a unique FUSE filesystem. In particular, opening a second copy of this device, will not allow access to resources created through the first file descriptor (and vice versa).</p>
<h3>The basic protocol</h3>
<p>Every message that is read by the daemon begins with a header described by the following structure: struct fuse_out_header {<br />
    uint32_t len;    /* Total length of data written to<br />
                        the file descriptor */<br />
    int32_t error;   /* Any error that occurred (0 if none) */<br />
    uint64_t unique; /* The value from the<br />
                        corresponding request */<br />
}; The header is followed by a variable-length data portion (which may be empty) specific to the requested operation (the requested operation is indicated by <i>opcode</i>). The daemon should then process the request and if applicable send a reply (almost all operations require a reply; if they do not, this is documented below), by performing a <code><a href="/docs/linux/man/2-write/">write</a></code>(2) to the file descriptor. All replies must start with the following header: </p>
<pre><code>struct fuse_out_header {
    uint32_t len;    /* Total length of data written to
                        the file descriptor */
    int32_t error;   /* Any error that occurred (0 if none) */
    uint64_t unique; /* The value from the
                        corresponding request */
};</code></pre>
<p> This header is also followed by (potentially empty) variable-sized data depending on the executed request. However, if the reply is an error reply (i.e., <i>error</i> is set), then no further payload data should be sent, independent of the request.</p>
<h3>Exchanged messages</h3>
<p>This section should contain documentation for each of the messages in the protocol. This manual page is currently incomplete, so not all messages are documented. For each message, first the struct sent by the kernel is given, followed by a description of the semantics of the message.</p>
<dl>
<dt><code>FUSE_INIT</code></p>
<dd>
<dd>struct fuse_init_in {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint32_t major;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint32_t minor;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint32_t max_readahead;&nbsp;/*&nbsp;Since protocol v7.6&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint32_t flags;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Since protocol v7.6&nbsp;*/ };</p>
<dd>This is the first request sent by the kernel to the daemon. It is used to negotiate the protocol version and other filesystem parameters. Note that the protocol version may affect the layout of any structure in the protocol (including this structure). The daemon must thus remember the negotiated version and flags for each session. As of the writing of this man page, the highest supported kernel protocol version is <i>7.26</i>.</p>
<dd>Users should be aware that the descriptions in this manual page may be incomplete or incorrect for older or more recent protocol versions.</p>
<dd>The reply for this request has the following format:</p>
<dd>struct fuse_init_out {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint32_t major;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint32_t minor;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint32_t max_readahead;&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Since v7.6&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint32_t flags;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Since v7.6;&nbsp;some flags bits<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;were introduced later&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint16_t max_background;&nbsp;<wbr>&nbsp;/*&nbsp;Since v7.13&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint16_t congestion_threshold;&nbsp;<wbr>&nbsp;/*&nbsp;Since v7.13&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint32_t max_write;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Since v7.5&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint32_t time_gran;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Since v7.6&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint32_t unused[9]; };</p>
<dd>If the major version supported by the kernel is larger than that supported by the daemon, the reply shall consist of only <i>uint32_t major</i> (following the usual header), indicating the largest major version supported by the daemon. The kernel will then issue a new <code>FUSE_INIT</code> request conforming to the older version. In the reverse case, the daemon should quietly fall back to the kernel&#8217;s major version.</p>
<dd>The negotiated minor version is considered to be the minimum of the minor versions provided by the daemon and the kernel and both parties should use the protocol corresponding to said minor version.</p>
<dt><code>FUSE_GETATTR</code></p>
<dd>
<dd>struct fuse_getattr_in {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint32_t getattr_flags;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint32_t dummy;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint64_t fh;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Set only if<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(getattr_flags&nbsp;&amp;&nbsp;FUSE_GETATTR_FH) };</p>
<dd>The requested operation is to compute the attributes to be returned by <code><a href="/docs/linux/man/2-stat/">stat</a></code>(2) and similar operations for the given filesystem object. The object for which the attributes should be computed is indicated either by <i>header-&gt;nodeid</i> or, if the <code>FUSE_GETATTR_FH</code> flag is set, by the file handle <i>fh</i>. The latter case of operation is analogous to <code><a href="/docs/linux/man/2-fstat/">fstat</a></code>(2).</p>
<dd>For performance reasons, these attributes may be cached in the kernel for a specified duration of time. While the cache timeout has not been exceeded, the attributes will be served from the cache and will not cause additional <code>FUSE_GETATTR</code> requests.</p>
<dd>The computed attributes and the requested cache timeout should then be returned in the following structure:</p>
<dd>struct fuse_attr_out {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Attribute cache duration&nbsp;(seconds&nbsp;+&nbsp;nanoseconds)&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint64_t attr_valid;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint32_t attr_valid_nsec;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint32_t dummy;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct fuse_attr&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint64_t ino;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint64_t size;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint64_t blocks;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint64_t atime;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint64_t mtime;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint64_t ctime;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint32_t atimensec;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint32_t mtimensec;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint32_t ctimensec;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint32_t mode;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint32_t nlink;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint32_t uid;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint32_t gid;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint32_t rdev;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint32_t blksize;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint32_t padding;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;}&nbsp;attr; };</p>
<dt><code>FUSE_ACCESS</code></p>
<dd>
<dd>struct fuse_access_in {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint32_t mask;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint32_t padding; };</p>
<dd>If the <i>default_permissions</i> mount options is not used, this request may be used for permissions checking. No reply data is expected, but errors may be indicated as usual by setting the <i>error</i> field in the reply header (in particular, access denied errors may be indicated by returning <code>-EACCES</code>).</p>
<dt><code>FUSE_OPEN</code> and <code>FUSE_OPENDIR</code></p>
<dd>struct fuse_open_in {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint32_t flags;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;The flags that were passed<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;to the&nbsp;<a href="/docs/linux/man/2-open/">open</a>(2)&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint32_t unused; };</p>
<dd>The requested operation is to open the node indicated by <i>header-&gt;nodeid</i>. The exact semantics of what this means will depend on the filesystem being implemented. However, at the very least the filesystem should validate that the requested <i>flags</i> are valid for the indicated resource and then send a reply with the following format:</p>
<dd>struct fuse_open_out {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint64_t fh;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint32_t open_flags;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint32_t padding; };</p>
<dd>The <i>fh</i> field is an opaque identifier that the kernel will use to refer to this resource The <i>open_flags</i> field is a bit mask of any number of the flags that indicate properties of this file handle to the kernel:</p>
<dl>
<dd>
<dl>
<dt><code>FOPEN_DIRECT_IO</code></p>
<dd>Bypass page cache for this open file.</p>
<dt><code>FOPEN_KEEP_CACHE</code></p>
<dd>Don&#8217;t invalidate the data cache on open.</p>
<dt><code>FOPEN_NONSEEKABLE</code></p>
<dd>The file is not seekable.</dl>
</dl>
<dt><code>FUSE_READ</code> and <code>FUSE_READDIR</code></p>
<dd>
<dd>struct fuse_read_in {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint64_t fh;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint64_t offset;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint32_t size;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint32_t read_flags;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint64_t lock_owner;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint32_t flags;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint32_t padding; };</p>
<dd>The requested action is to read up to <i>size</i> bytes of the file or directory, starting at <i>offset</i>. The bytes should be returned directly following the usual reply header.</p>
<dt><code>FUSE_INTERRUPT</code></p>
<dd>struct fuse_interrupt_in {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint64_t unique; };</p>
<dd>The requested action is to cancel the pending operation indicated by <i>unique</i>. This request requires no response. However, receipt of this message does not by itself cancel the indicated operation. The kernel will still expect a reply to said operation (e.g., an <i>EINTR</i> error or a short read). At most one <code>FUSE_INTERRUPT</code> request will be issued for a given operation. After issuing said operation, the kernel will wait uninterruptibly for completion of the indicated request.</p>
<dt><code>FUSE_LOOKUP</code></p>
<dd>Directly following the header is a filename to be looked up in the directory indicated by <i>header-&gt;nodeid</i>. The expected reply is of the form:</p>
<dd>struct fuse_entry_out {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint64_t nodeid;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Inode ID&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint64_t generation;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Inode generation&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint64_t entry_valid;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint64_t attr_valid;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint32_t entry_valid_nsec;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint32_t attr_valid_nsec;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct fuse_attr attr; };</p>
<dd>The combination of <i>nodeid</i> and <i>generation</i> must be unique for the filesystem&#8217;s lifetime.</p>
<dd>The interpretation of timeouts and <i>attr</i> is as for <code>FUSE_GETATTR</code>.</p>
<dt><code>FUSE_FLUSH</code></p>
<dd>struct fuse_flush_in {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint64_t fh;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint32_t unused;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint32_t padding;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint64_t lock_owner; };</p>
<dd>The requested action is to flush any pending changes to the indicated file handle. No reply data is expected. However, an empty reply message still needs to be issued once the flush operation is complete.</p>
<dt><code>FUSE_RELEASE</code> and <code>FUSE_RELEASEDIR</code></p>
<dd>struct fuse_release_in {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint64_t fh;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint32_t flags;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint32_t release_flags;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint64_t lock_owner; };</p>
<dd>These are the converse of <code>FUSE_OPEN</code> and <code>FUSE_OPENDIR</code> respectively. The daemon may now free any resources associated with the file handle <i>fh</i> as the kernel will no longer refer to it. There is no reply data associated with this request, but a reply still needs to be issued once the request has been completely processed.</p>
<dt><code>FUSE_STATFS</code></p>
<dd>This operation implements <code><a href="/docs/linux/man/2-statfs/">statfs</a></code>(2) for this filesystem. There is no input data associated with this request. The expected reply data has the following structure:</p>
<dd>struct fuse_kstatfs {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint64_t blocks;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint64_t bfree;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint64_t bavail;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint64_t files;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint64_t ffree;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint32_t bsize;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint32_t namelen;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint32_t frsize;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint32_t padding;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint32_t spare[6]; }; struct fuse_statfs_out {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct fuse_kstatfs st; };</p>
<dd>For the interpretation of these fields, see <code><a href="/docs/linux/man/2-statfs/">statfs</a></code>(2).</dl>
<h2>Errors</h2>
<dl>
<dt><code>E2BIG</code></p>
<dd>Returned from <code><a href="/docs/linux/man/2-read/">read</a></code>(2) operations when the kernel&#8217;s request is too large for the provided buffer and the request was <code>FUSE_SETXATTR</code>.</p>
<dt><code>EINVAL</code></p>
<dd>Returned from <code><a href="/docs/linux/man/2-write/">write</a></code>(2) if validation of the reply failed. Not all mistakes in replies will be caught by this validation. However, basic mistakes, such as short replies or an incorrect <i>unique</i> value, are detected.</p>
<dt><code>EIO</code></p>
<dd>Returned from <code><a href="/docs/linux/man/2-read/">read</a></code>(2) operations when the kernel&#8217;s request is too large for the provided buffer.</p>
<dd><i>Note</i>: There are various ways in which incorrect use of these interfaces can cause operations on the provided filesystem&#8217;s files and directories to fail with <code>EIO</code>. Among the possible incorrect uses are:</p>
<dl>
<dd>
<dl>
<dt>*</p>
<dd>changing <i>mode &amp; S_IFMT</i> for an inode that has previously been reported to the kernel; or</p>
<dt>*</p>
<dd>giving replies to the kernel that are shorter than what the kernel expected.</dl>
</dl>
<dt><code>ENODEV</code></p>
<dd>Returned from <code><a href="/docs/linux/man/2-read/">read</a></code>(2) and <code><a href="/docs/linux/man/2-write/">write</a></code>(2) if the FUSE filesystem was unmounted.</p>
<dt><code>EPERM</code></p>
<dd>Returned from operations on a <i>/dev/fuse</i> file descriptor that has not been mounted.</dl>
<h2>Conforming To</h2>
<p>The FUSE filesystem is Linux-specific.</p>
<h2>Notes</h2>
<p>The following messages are not yet documented in this manual page: </p>
<p> <code>FUSE_BATCH_FORGET</code> <code>FUSE_BMAP</code> <code>FUSE_CREATE</code> <code>FUSE_DESTROY</code> <code>FUSE_FALLOCATE</code> <code>FUSE_FORGET</code> <code>FUSE_FSYNC</code> <code>FUSE_FSYNCDIR</code> <code>FUSE_GETLK</code> <code>FUSE_GETXATTR</code> <code>FUSE_IOCTL</code> <code>FUSE_LINK</code> <code>FUSE_LISTXATTR</code> <code>FUSE_LSEEK</code> <code>FUSE_MKDIR</code> <code>FUSE_MKNOD</code> <code>FUSE_NOTIFY_REPLY</code> <code>FUSE_POLL</code> <code>FUSE_READDIRPLUS</code> <code>FUSE_READLINK</code> <code>FUSE_REMOVEXATTR</code> <code>FUSE_RENAME</code> <code>FUSE_RENAME2</code> <code>FUSE_RMDIR</code> <code>FUSE_SETATTR</code> <code>FUSE_SETLK</code> <code>FUSE_SETLKW</code> <code>FUSE_SYMLINK</code> <code>FUSE_UNLINK</code> <code>FUSE_WRITE</code></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-fusermount/">fusermount</a></code>(1), <code><a href="/docs/linux/man/8-mount-fuse/">mount.fuse</a></code>(8)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
