---
title: "io_submit(2)"
name: "io_submit"
section: "2"
letter: "i"
url: "/docs/linux/man/2-io_submit/"
description: "io_submit – submit asynchronous I/O blocks for processing"
---

<h2 class="name">NAME</h2>
<p> io_submit &#8211; submit asynchronous I/O blocks for processing </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;linux/aio_abi.h&gt; /* Defines needed types */
int io_submit(aio_context_t ctx_id, long nr, struct iocb **iocbpp);
</code></pre>
<p> <i>Note</i>: There is no glibc wrapper for this system call; see NOTES.</p>
<h2>DESCRIPTION</h2>
<p> <i>Note</i>: this page describes the raw Linux system call interface. The wrapper function provided by <i>libaio</i> uses a different type for the <i>ctx_id</i> argument. See NOTES. </p>
<p> The <code>io_submit</code>() system call queues <i>nr</i> I/O request blocks for processing in the AIO context <i>ctx_id</i>. The <i>iocbpp</i> argument should be an array of <i>nr</i> AIO control blocks, which will be submitted to context <i>ctx_id</i>. </p>
<p> The <i>iocb</i> (I/O control block) structure defined in <i>linux/aio_abi.h</i> defines the parameters that control the I/O operation. </p>
<p> #include &lt;linux/aio_abi.h&gt; </p>
<p> struct iocb {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u64&nbsp;<wbr>&nbsp;<wbr>&nbsp;aio_data;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u32&nbsp;<wbr>&nbsp;<wbr>&nbsp;PADDED(aio_key, aio_rw_flags);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u16&nbsp;<wbr>&nbsp;<wbr>&nbsp;aio_lio_opcode;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__s16&nbsp;<wbr>&nbsp;<wbr>&nbsp;aio_reqprio;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u32&nbsp;<wbr>&nbsp;<wbr>&nbsp;aio_fildes;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u64&nbsp;<wbr>&nbsp;<wbr>&nbsp;aio_buf;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u64&nbsp;<wbr>&nbsp;<wbr>&nbsp;aio_nbytes;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__s64&nbsp;<wbr>&nbsp;<wbr>&nbsp;aio_offset;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u64&nbsp;<wbr>&nbsp;<wbr>&nbsp;aio_reserved2;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u32&nbsp;<wbr>&nbsp;<wbr>&nbsp;aio_flags;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u32&nbsp;<wbr>&nbsp;<wbr>&nbsp;aio_resfd; }; </p>
<p> The fields of this structure are as follows:</p>
<dl>
<dt><i>aio_data</i></p>
<dd> This data is copied into the <i>data</i> field of the <i>io_event</i> structure upon I/O completion (see <code><a href="/docs/linux/man/2-io_getevents/">io_getevents</a></code>(2)).</p>
<dt><i>aio_key</i></p>
<dd> This is an internal field used by the kernel. Do not modify this field after an <code>io_submit</code>() call.</p>
<dt><i>aio_rw_flags</i></p>
<dd> This defines the R/W flags passed with structure. The valid values are:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>RWF_APPEND</code> (since Linux 4.16)</p>
<dd> Append data to the end of the file. See the description of the flag of the same name in <code><a href="/docs/linux/man/2-pwritev2/">pwritev2</a></code>(2) as well as the description of <code>O_APPEND</code> in <code><a href="/docs/linux/man/2-open/">open</a></code>(2). The <i>aio_offset</i> field is ignored. The file offset is not changed.</p>
<dt><code>RWF_DSYNC</code> (since Linux 4.13)</p>
<dd> Write operation complete according to requirement of synchronized I/O data integrity. See the description of the flag of the same name in <code><a href="/docs/linux/man/2-pwritev2/">pwritev2</a></code>(2) as well the description of <code>O_DSYNC</code> in <code><a href="/docs/linux/man/2-open/">open</a></code>(2).</p>
<dt><code>RWF_HIPRI</code> (since Linux 4.13)</p>
<dd> High priority request, poll if possible</p>
<dt><code>RWF_NOWAIT</code> (since Linux 4.14)</p>
<dd> Don&#8217;t wait if the I/O will block for operations such as file block allocations, dirty page flush, mutex locks, or a congested block device inside the kernel. If any of these conditions are met, the control block is returned immediately with a return value of <code>-EAGAIN</code> in the <i>res</i> field of the <i>io_event</i> structure (see <code><a href="/docs/linux/man/2-io_getevents/">io_getevents</a></code>(2)).</p>
<dt><code>RWF_SYNC</code> (since Linux 4.13)</p>
<dd> Write operation complete according to requirement of synchronized I/O file integrity. See the description of the flag of the same name in <code><a href="/docs/linux/man/2-pwritev2/">pwritev2</a></code>(2) as well the description of <code>O_SYNC</code> in <code><a href="/docs/linux/man/2-open/">open</a></code>(2).</dl>
</dl>
<dt><i>aio_lio_opcode</i></p>
<dd> This defines the type of I/O to be performed by the <i>iocb</i> structure. The valid values are defined by the enum defined in <i>linux/aio_abi.h</i>:</p>
<dt>
<dd> enum {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;IOCB_CMD_PREAD&nbsp;=&nbsp;0,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;IOCB_CMD_PWRITE&nbsp;=&nbsp;1,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;IOCB_CMD_FSYNC&nbsp;=&nbsp;2,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;IOCB_CMD_FDSYNC&nbsp;=&nbsp;3,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;IOCB_CMD_POLL&nbsp;=&nbsp;5,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;IOCB_CMD_NOOP&nbsp;=&nbsp;6,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;IOCB_CMD_PREADV&nbsp;=&nbsp;7,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;IOCB_CMD_PWRITEV&nbsp;=&nbsp;8, };</p>
<dt><i>aio_reqprio</i></p>
<dd> This defines the requests priority.</p>
<dt><i>aio_fildes</i></p>
<dd> The file descriptor on which the I/O operation is to be performed.</p>
<dt><i>aio_buf</i></p>
<dd> This is the buffer used to transfer data for a read or write operation.</p>
<dt><i>aio_nbytes</i></p>
<dd> This is the size of the buffer pointed to by <i>aio_buf</i>.</p>
<dt><i>aio_offset</i></p>
<dd> This is the file offset at which the I/O operation is to be performed.</p>
<dt><i>aio_flags</i></p>
<dd> This is the set of flags associated with the <i>iocb</i> structure. The valid values are:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>IOCB_FLAG_RESFD</code></p>
<dd> Asynchronous I/O control must signal the file descriptor mentioned in <i>aio_resfd</i> upon completion.</p>
<dt><code>IOCB_FLAG_IOPRIO</code> (since Linux 4.18)</p>
<dd> Interpret the <i>aio_reqprio</i> field as an <code>IOPRIO_VALUE</code> as defined by <i>linux/ioprio.h</i>.</dl>
</dl>
<dt><i>aio_resfd</i></p>
<dd> The file descriptor to signal in the event of asynchronous I/O completion.</dl>
<h2>RETURN VALUE</h2>
<p> On success, <code>io_submit</code>() returns the number of <i>iocb</i>s submitted (which may be less than <i>nr</i>, or 0 if <i>nr</i> is zero). For the failure return, see NOTES.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EAGAIN</code></p>
<dd> Insufficient resources are available to queue any <i>iocb</i>s.</p>
<dt><code>EBADF</code></p>
<dd> The file descriptor specified in the first <i>iocb</i> is invalid.</p>
<dt><code>EFAULT</code></p>
<dd> One of the data structures points to invalid data.</p>
<dt><code>EINVAL</code></p>
<dd> The AIO context specified by <i>ctx_id</i> is invalid. <i>nr</i> is less than 0. The <i>iocb</i> at <i>*iocbpp[0]</i> is not properly initialized, the operation specified is invalid for the file descriptor in the <i>iocb</i>, or the value in the <i>aio_reqprio</i> field is invalid.</p>
<dt><code>ENOSYS</code></p>
<dd> <code>io_submit</code>() is not implemented on this architecture.</p>
<dt><code>EPERM</code></p>
<dd> The <i>aio_reqprio</i> field is set with the class <code>IOPRIO_CLASS_RT</code>, but the submitting context does not have the <code>CAP_SYS_ADMIN</code> capability.</dl>
<h2>VERSIONS</h2>
<p> The asynchronous I/O system calls first appeared in Linux 2.5.</p>
<h2>CONFORMING TO</h2>
<p> <code>io_submit</code>() is Linux-specific and should not be used in programs that are intended to be portable.</p>
<h2>NOTES</h2>
<p> Glibc does not provide a wrapper function for this system call. You could invoke it using <code><a href="/docs/linux/man/2-syscall/">syscall</a></code>(2). But instead, you probably want to use the <code>io_submit</code>() wrapper function provided by <i>libaio</i>. </p>
<p> Note that the <i>libaio</i> wrapper function uses a different type (<i>io_context_t</i>) for the <i>ctx_id</i> argument. Note also that the <i>libaio</i> wrapper does not follow the usual C library conventions for indicating errors: on error it returns a negated error number (the negative of one of the values listed in ERRORS). If the system call is invoked via <code><a href="/docs/linux/man/2-syscall/">syscall</a></code>(2), then the return value follows the usual conventions for indicating an error: -1, with <i>errno</i> set to a (positive) value that indicates the error.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-io_cancel/">io_cancel</a></code>(2), <code><a href="/docs/linux/man/2-io_destroy/">io_destroy</a></code>(2), <code><a href="/docs/linux/man/2-io_getevents/">io_getevents</a></code>(2), <code><a href="/docs/linux/man/2-io_setup/">io_setup</a></code>(2), <code><a href="/docs/linux/man/7-aio/">aio</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
