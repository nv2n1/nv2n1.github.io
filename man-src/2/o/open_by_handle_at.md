---
title: "open_by_handle_at(2)"
name: "open_by_handle_at"
section: "2"
letter: "o"
url: "/docs/linux/man/2-open_by_handle_at/"
description: "name_to_handle_at, open_by_handle_at – obtain handle for a pathname and open file via a handle"
---

<h2 class="name">NAME</h2>
<p> name_to_handle_at, open_by_handle_at &#8211; obtain handle for a pathname and open file via a handle </p>
<h2>SYNOPSIS</h2>
<pre><code>
#define _GNU_SOURCE /* See feature_test_macros(7) */
#include &lt;fcntl.h&gt;
#include &lt;sys/stat.h&gt;
#include &lt;sys/types.h&gt;
int name_to_handle_at(int dirfd, const char *pathname,
                      struct file_handle *handle,
                      int *mount_id, int flags);
int open_by_handle_at(int mount_fd, struct file_handle *handle,
                      int flags);
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>name_to_handle_at</code>() and <code>open_by_handle_at</code>() system calls split the functionality of <code><a href="/docs/linux/man/2-openat/">openat</a></code>(2) into two parts: <code>name_to_handle_at</code>() returns an opaque handle that corresponds to a specified file; <code>open_by_handle_at</code>() opens the file corresponding to a handle returned by a previous call to <code>name_to_handle_at</code>() and returns an open file descriptor.</p>
<h3>name_to_handle_at()</h3>
<p> The <code>name_to_handle_at</code>() system call returns a file handle and a mount ID corresponding to the file specified by the <i>dirfd</i> and <i>pathname</i> arguments. The file handle is returned via the argument <i>handle</i>, which is a pointer to a structure of the following form: </p>
<p> struct file_handle {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned int&nbsp;<wbr>&nbsp;handle_bytes;&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Size of f_handle&nbsp;[in, out]&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;handle_type;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Handle type&nbsp;[out]&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned char f_handle[0];&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;File identifier&nbsp;(sized by<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;caller)&nbsp;[out]&nbsp;*/ }; </p>
<p> It is the caller&#8217;s responsibility to allocate the structure with a size large enough to hold the handle returned in <i>f_handle</i>. Before the call, the <i>handle_bytes</i> field should be initialized to contain the allocated size for <i>f_handle</i>. (The constant <code>MAX_HANDLE_SZ</code>, defined in <i>&lt;fcntl.h&gt;</i>, specifies the maximum expected size for a file handle. It is not a guaranteed upper limit as future filesystems may require more space.) Upon successful return, the <i>handle_bytes</i> field is updated to contain the number of bytes actually written to <i>f_handle</i>. </p>
<p> The caller can discover the required size for the <i>file_handle</i> structure by making a call in which <i>handle-&gt;handle_bytes</i> is zero; in this case, the call fails with the error <code>EOVERFLOW</code> and <i>handle-&gt;handle_bytes</i> is set to indicate the required size; the caller can then use this information to allocate a structure of the correct size (see EXAMPLES below). Some care is needed here as <code>EOVERFLOW</code> can also indicate that no file handle is available for this particular name in a filesystem which does normally support file-handle lookup. This case can be detected when the <code>EOVERFLOW</code> error is returned without <i>handle_bytes</i> being increased. </p>
<p> Other than the use of the <i>handle_bytes</i> field, the caller should treat the <i>file_handle</i> structure as an opaque data type: the <i>handle_type</i> and <i>f_handle</i> fields are needed only by a subsequent call to <code>open_by_handle_at</code>(). </p>
<p> The <i>flags</i> argument is a bit mask constructed by ORing together zero or more of <code>AT_EMPTY_PATH</code> and <code>AT_SYMLINK_FOLLOW</code>, described below. </p>
<p> Together, the <i>pathname</i> and <i>dirfd</i> arguments identify the file for which a handle is to be obtained. There are four distinct cases:</p>
<dl>
<dt>*</p>
<dd> If <i>pathname</i> is a nonempty string containing an absolute pathname, then a handle is returned for the file referred to by that pathname. In this case, <i>dirfd</i> is ignored.</p>
<dt>*</p>
<dd> If <i>pathname</i> is a nonempty string containing a relative pathname and <i>dirfd</i> has the special value <code>AT_FDCWD</code>, then <i>pathname</i> is interpreted relative to the current working directory of the caller, and a handle is returned for the file to which it refers.</p>
<dt>*</p>
<dd> If <i>pathname</i> is a nonempty string containing a relative pathname and <i>dirfd</i> is a file descriptor referring to a directory, then <i>pathname</i> is interpreted relative to the directory referred to by <i>dirfd</i>, and a handle is returned for the file to which it refers. (See <code><a href="/docs/linux/man/2-openat/">openat</a></code>(2) for an explanation of why &quot;directory file descriptors&quot; are useful.)</p>
<dt>*</p>
<dd> If <i>pathname</i> is an empty string and <i>flags</i> specifies the value <code>AT_EMPTY_PATH</code>, then <i>dirfd</i> can be an open file descriptor referring to any type of file, or <code>AT_FDCWD</code>, meaning the current working directory, and a handle is returned for the file to which it refers.</dl>
<p> The <i>mount_id</i> argument returns an identifier for the filesystem mount that corresponds to <i>pathname</i>. This corresponds to the first field in one of the records in <i>/proc/self/mountinfo</i>. Opening the pathname in the fifth field of that record yields a file descriptor for the mount point; that file descriptor can be used in a subsequent call to <code>open_by_handle_at</code>(). <i>mount_id</i> is returned both for a successful call and for a call that results in the error <code>EOVERFLOW</code>. </p>
<p> By default, <code>name_to_handle_at</code>() does not dereference <i>pathname</i> if it is a symbolic link, and thus returns a handle for the link itself. If <code>AT_SYMLINK_FOLLOW</code> is specified in <i>flags</i>, <i>pathname</i> is dereferenced if it is a symbolic link (so that the call returns a handle for the file referred to by the link). </p>
<p> <code>name_to_handle_at</code>() does not trigger a mount when the final component of the pathname is an automount point. When a filesystem supports both file handles and automount points, a <code>name_to_handle_at</code>() call on an automount point will return with error <code>EOVERFLOW</code> without having increased <i>handle_bytes</i>. This can happen since Linux 4.13 with NFS when accessing a directory which is on a separate filesystem on the server. In this case, the automount can be triggered by adding a &quot;/&quot; to the end of the pathname.</p>
<h3>open_by_handle_at()</h3>
<p> The <code>open_by_handle_at</code>() system call opens the file referred to by <i>handle</i>, a file handle returned by a previous call to <code>name_to_handle_at</code>(). </p>
<p> The <i>mount_fd</i> argument is a file descriptor for any object (file, directory, etc.) in the mounted filesystem with respect to which <i>handle</i> should be interpreted. The special value <code>AT_FDCWD</code> can be specified, meaning the current working directory of the caller. </p>
<p> The <i>flags</i> argument is as for <code><a href="/docs/linux/man/2-open/">open</a></code>(2). If <i>handle</i> refers to a symbolic link, the caller must specify the <code>O_PATH</code> flag, and the symbolic link is not dereferenced; the <code>O_NOFOLLOW</code> flag, if specified, is ignored. </p>
<p> The caller must have the <code>CAP_DAC_READ_SEARCH</code> capability to invoke <code>open_by_handle_at</code>().</p>
<h2>RETURN VALUE</h2>
<p> On success, <code>name_to_handle_at</code>() returns 0, and <code>open_by_handle_at</code>() returns a file descriptor (a nonnegative integer). </p>
<p> In the event of an error, both system calls return -1 and set <i>errno</i> to indicate the cause of the error.</p>
<h2>ERRORS</h2>
<p> <code>name_to_handle_at</code>() and <code>open_by_handle_at</code>() can fail for the same errors as <code><a href="/docs/linux/man/2-openat/">openat</a></code>(2). In addition, they can fail with the errors noted below. </p>
<p> <code>name_to_handle_at</code>() can fail with the following errors:</p>
<dl>
<dt><code>EFAULT</code></p>
<dd> <i>pathname</i>, <i>mount_id</i>, or <i>handle</i> points outside your accessible address space.</p>
<dt><code>EINVAL</code></p>
<dd> <i>flags</i> includes an invalid bit value.</p>
<dt><code>EINVAL</code></p>
<dd> <i>handle-&gt;handle_bytes</i> is greater than <code>MAX_HANDLE_SZ</code>.</p>
<dt><code>ENOENT</code></p>
<dd> <i>pathname</i> is an empty string, but <code>AT_EMPTY_PATH</code> was not specified in <i>flags</i>.</p>
<dt><code>ENOTDIR</code></p>
<dd> The file descriptor supplied in <i>dirfd</i> does not refer to a directory, and it is not the case that both <i>flags</i> includes <code>AT_EMPTY_PATH</code> and <i>pathname</i> is an empty string.</p>
<dt><code>EOPNOTSUPP</code></p>
<dd> The filesystem does not support decoding of a pathname to a file handle.</p>
<dt><code>EOVERFLOW</code></p>
<dd> The <i>handle-&gt;handle_bytes</i> value passed into the call was too small. When this error occurs, <i>handle-&gt;handle_bytes</i> is updated to indicate the required size for the handle.</dl>
<p> <code>open_by_handle_at</code>() can fail with the following errors:</p>
<dl>
<dt><code>EBADF</code></p>
<dd> <i>mount_fd</i> is not an open file descriptor.</p>
<dt><code>EFAULT</code></p>
<dd> <i>handle</i> points outside your accessible address space.</p>
<dt><code>EINVAL</code></p>
<dd> <i>handle-&gt;handle_bytes</i> is greater than <code>MAX_HANDLE_SZ</code> or is equal to zero.</p>
<dt><code>ELOOP</code></p>
<dd> <i>handle</i> refers to a symbolic link, but <code>O_PATH</code> was not specified in <i>flags</i>.</p>
<dt><code>EPERM</code></p>
<dd> The caller does not have the <code>CAP_DAC_READ_SEARCH</code> capability.</p>
<dt><code>ESTALE</code></p>
<dd> The specified <i>handle</i> is not valid. This error will occur if, for example, the file has been deleted.</dl>
<h2>VERSIONS</h2>
<p> These system calls first appeared in Linux 2.6.39. Library support is provided in glibc since version 2.14.</p>
<h2>CONFORMING TO</h2>
<p> These system calls are nonstandard Linux extensions. </p>
<p> FreeBSD has a broadly similar pair of system calls in the form of <code>getfh</code>() and <code>openfh</code>().</p>
<h2>NOTES</h2>
<p> A file handle can be generated in one process using <code>name_to_handle_at</code>() and later used in a different process that calls <code>open_by_handle_at</code>(). </p>
<p> Some filesystem don&#8217;t support the translation of pathnames to file handles, for example, <i>/proc</i>, <i>/sys</i>, and various network filesystems. </p>
<p> A file handle may become invalid (&quot;stale&quot;) if a file is deleted, or for other filesystem-specific reasons. Invalid handles are notified by an <code>ESTALE</code> error from <code>open_by_handle_at</code>(). </p>
<p> These system calls are designed for use by user-space file servers. For example, a user-space NFS server might generate a file handle and pass it to an NFS client. Later, when the client wants to open the file, it could pass the handle back to the server. This sort of functionality allows a user-space file server to operate in a stateless fashion with respect to the files it serves. </p>
<p> If <i>pathname</i> refers to a symbolic link and <i>flags</i> does not specify <code>AT_SYMLINK_FOLLOW</code>, then <code>name_to_handle_at</code>() returns a handle for the link (rather than the file to which it refers). The process receiving the handle can later perform operations on the symbolic link by converting the handle to a file descriptor using <code>open_by_handle_at</code>() with the <code>O_PATH</code> flag, and then passing the file descriptor as the <i>dirfd</i> argument in system calls such as <code><a href="/docs/linux/man/2-readlinkat/">readlinkat</a></code>(2) and <code><a href="/docs/linux/man/2-fchownat/">fchownat</a></code>(2).</p>
<h3>Obtaining a persistent filesystem ID</h3>
<p> The mount IDs in <i>/proc/self/mountinfo</i> can be reused as filesystems are unmounted and mounted. Therefore, the mount ID returned by <code>name_to_handle_at</code>() (in <i>*mount_id</i>) should not be treated as a persistent identifier for the corresponding mounted filesystem. However, an application can use the information in the <i>mountinfo</i> record that corresponds to the mount ID to derive a persistent identifier. </p>
<p> For example, one can use the device name in the fifth field of the <i>mountinfo</i> record to search for the corresponding device UUID via the symbolic links in <i>/dev/disks/by-uuid</i>. (A more comfortable way of obtaining the UUID is to use the <code><a href="/docs/linux/man/3-libblkid/">libblkid</a></code>(3) library.) That process can then be reversed, using the UUID to look up the device name, and then obtaining the corresponding mount point, in order to produce the <i>mount_fd</i> argument used by <code>open_by_handle_at</code>().</p>
<h2>EXAMPLES</h2>
<p> The two programs below demonstrate the use of <code>name_to_handle_at</code>() and <code>open_by_handle_at</code>(). The first program (<i>t_name_to_handle_at.c</i>) uses <code>name_to_handle_at</code>() to obtain the file handle and mount ID for the file specified in its command-line argument; the handle and mount ID are written to standard output. </p>
<p> The second program (<i>t_open_by_handle_at.c</i>) reads a mount ID and file handle from standard input. The program then employs <code>open_by_handle_at</code>() to open the file using that handle. If an optional command-line argument is supplied, then the <i>mount_fd</i> argument for <code>open_by_handle_at</code>() is obtained by opening the directory named in that argument. Otherwise, <i>mount_fd</i> is obtained by scanning <i>/proc/self/mountinfo</i> to find a record whose mount ID matches the mount ID read from standard input, and the mount directory specified in that record is opened. (These programs do not deal with the fact that mount IDs are not persistent.) </p>
<p> The following shell session demonstrates the use of these two programs: </p>
<p> $ <code>echo &#8216;Can you please think about it?&#8217; &gt; cecilia.txt</code> $ <code>./t_name_to_handle_at cecilia.txt &gt; fh</code> $ <code>./t_open_by_handle_at &lt; fh</code> open_by_handle_at: Operation not permitted $ <code>sudo ./t_open_by_handle_at &lt; fh</code> # Need CAP_SYS_ADMIN Read 31 bytes $ <code>rm cecilia.txt</code> </p>
<p> Now we delete and (quickly) re-create the file so that it has the same content and (by chance) the same inode. Nevertheless, <code>open_by_handle_at</code>() recognizes that the original file referred to by the file handle no longer exists. </p>
<p> $ <code>stat &#8211;printf=&quot;%i
&quot; cecilia.txt</code> # Display inode number 4072121 $ <code>rm cecilia.txt</code> $ <code>echo &#8216;Can you please think about it?&#8217; &gt; cecilia.txt</code> $ <code>stat &#8211;printf=&quot;%i
&quot; cecilia.txt</code> # Check inode number 4072121 $ <code>sudo ./t_open_by_handle_at &lt; fh</code> open_by_handle_at: Stale NFS file handle</p>
<h3>Program source: t_name_to_handle_at.c</h3>
<p> #define _GNU_SOURCE #include &lt;sys/types.h&gt; #include &lt;sys/stat.h&gt; #include &lt;fcntl.h&gt; #include &lt;stdio.h&gt; #include &lt;stdlib.h&gt; #include &lt;unistd.h&gt; #include &lt;errno.h&gt; #include &lt;string.h&gt; </p>
<p> #define errExit(msg) do { perror(msg); exit(EXIT_FAILURE); \<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;}&nbsp;while&nbsp;(0) </p>
<p> int main(int argc, char *argv[]) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct file_handle&nbsp;*fhp;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int mount_id, fhsize, flags, dirfd;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;*pathname; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(argc&nbsp;!=&nbsp;2)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fprintf(stderr,&nbsp;&quot;Usage:&nbsp;%s pathname
&quot;, argv[0]);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;pathname&nbsp;=&nbsp;argv[1]; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Allocate file_handle structure&nbsp;*/ </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fhsize&nbsp;=&nbsp;sizeof(*fhp);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fhp&nbsp;=&nbsp;malloc(fhsize);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(fhp&nbsp;==&nbsp;NULL)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;errExit(&quot;malloc&quot;); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Make an initial call to name_to_handle_at()&nbsp;to discover<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;the size required for file handle&nbsp;*/ </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;dirfd&nbsp;=&nbsp;AT_FDCWD;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;For name_to_handle_at()&nbsp;calls&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;flags&nbsp;=&nbsp;0;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;For name_to_handle_at()&nbsp;calls&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fhp-&gt;handle_bytes&nbsp;=&nbsp;0;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(name_to_handle_at(dirfd, pathname, fhp,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&amp;mount_id, flags)&nbsp;!=&nbsp;-1 || errno&nbsp;!=&nbsp;EOVERFLOW)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fprintf(stderr,&nbsp;&quot;Unexpected result from name_to_handle_at()
&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Reallocate file_handle structure with correct size&nbsp;*/ </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fhsize&nbsp;=&nbsp;sizeof(*fhp)&nbsp;+&nbsp;fhp-&gt;handle_bytes;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fhp&nbsp;=&nbsp;realloc(fhp, fhsize);&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Copies fhp-&gt;handle_bytes&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(fhp&nbsp;==&nbsp;NULL)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;errExit(&quot;realloc&quot;); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Get file handle from pathname supplied on command line&nbsp;*/ </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(name_to_handle_at(dirfd, pathname, fhp,&nbsp;&amp;mount_id, flags)&nbsp;==&nbsp;-1)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;errExit(&quot;name_to_handle_at&quot;); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Write mount ID, file handle size, and file handle to stdout,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;for later reuse by t_open_by_handle_at.c&nbsp;*/ </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;%d
&quot;, mount_id);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;%u&nbsp;%d&nbsp;<wbr>&nbsp;<wbr>&nbsp;&quot;, fhp-&gt;handle_bytes, fhp-&gt;handle_type);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;for&nbsp;(int j&nbsp;=&nbsp;0;&nbsp;j&nbsp;&lt;&nbsp;fhp-&gt;handle_bytes;&nbsp;j++)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;&nbsp;%02x&quot;, fhp-&gt;f_handle[j]);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;
&quot;); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_SUCCESS); }</p>
<h3>Program source: t_open_by_handle_at.c</h3>
<p> #define _GNU_SOURCE #include &lt;sys/types.h&gt; #include &lt;sys/stat.h&gt; #include &lt;fcntl.h&gt; #include &lt;limits.h&gt; #include &lt;stdio.h&gt; #include &lt;stdlib.h&gt; #include &lt;unistd.h&gt; #include &lt;string.h&gt; </p>
<p> #define errExit(msg) do { perror(msg); exit(EXIT_FAILURE); \<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;}&nbsp;while&nbsp;(0) </p>
<p> /* Scan /proc/self/mountinfo to find the line whose mount ID matches<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;&#8216;mount_id&#8217;.&nbsp;(An easier way to do this is to install and use the<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;&#8216;libmount&#8217;&nbsp;library provided by the&nbsp;&#8216;util-linux&#8217;&nbsp;project.)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;Open the corresponding mount path and return the resulting file<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;descriptor.&nbsp;*/ </p>
<p> static int open_mount_path_by_id(int mount_id) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;*linep;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;size_t lsize;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char mount_path[PATH_MAX];<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int mi_mount_id, found;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;ssize_t nread;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;FILE&nbsp;*fp; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fp&nbsp;=&nbsp;fopen(&quot;/proc/self/mountinfo&quot;,&nbsp;&quot;r&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(fp&nbsp;==&nbsp;NULL)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;errExit(&quot;fopen&quot;); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;found&nbsp;=&nbsp;0;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;linep&nbsp;=&nbsp;NULL;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;while&nbsp;(!found)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;nread&nbsp;=&nbsp;getline(&amp;linep,&nbsp;&amp;lsize, fp);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(nread&nbsp;==&nbsp;-1)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;break; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;nread&nbsp;=&nbsp;sscanf(linep,&nbsp;&quot;%d&nbsp;%*d&nbsp;%*s&nbsp;%*s&nbsp;%s&quot;,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&amp;mi_mount_id, mount_path);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(nread&nbsp;!=&nbsp;2)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fprintf(stderr,&nbsp;&quot;Bad sscanf()
&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(mi_mount_id&nbsp;==&nbsp;mount_id)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;found&nbsp;=&nbsp;1;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;}<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;free(linep); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fclose(fp); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(!found)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fprintf(stderr,&nbsp;&quot;Could not find mount point
&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return open(mount_path, O_RDONLY); } </p>
<p> int main(int argc, char *argv[]) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct file_handle&nbsp;*fhp;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int mount_id, fd, mount_fd, handle_bytes;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;ssize_t nread;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char buf[1000]; #define LINE_SIZE 100<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char line1[LINE_SIZE], line2[LINE_SIZE];<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;*nextp; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;((argc&nbsp;&gt;&nbsp;1&nbsp;&amp;&amp;&nbsp;strcmp(argv[1],&nbsp;&quot;&#8211;help&quot;)&nbsp;==&nbsp;0)&nbsp;|| argc&nbsp;&gt;&nbsp;2)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fprintf(stderr,&nbsp;&quot;Usage:&nbsp;%s&nbsp;[mount-path]
&quot;, argv[0]);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Standard input contains mount ID and file handle information: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Line 1:&nbsp;&lt;mount_id&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Line 2:&nbsp;&lt;handle_bytes&gt;&nbsp;&lt;handle_type&gt;&nbsp;<wbr>&nbsp;<wbr>&nbsp;&lt;bytes of handle in hex&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;*/ </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;((fgets(line1, sizeof(line1), stdin)&nbsp;==&nbsp;NULL)&nbsp;||<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(fgets(line2, sizeof(line2), stdin)&nbsp;==&nbsp;NULL))&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fprintf(stderr,&nbsp;&quot;Missing mount_id&nbsp;/&nbsp;file handle
&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;mount_id&nbsp;=&nbsp;atoi(line1); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;handle_bytes&nbsp;=&nbsp;strtoul(line2,&nbsp;&amp;nextp, 0); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Given handle_bytes, we can now allocate file_handle structure&nbsp;*/ </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fhp&nbsp;=&nbsp;malloc(sizeof(*fhp)&nbsp;+&nbsp;handle_bytes);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(fhp&nbsp;==&nbsp;NULL)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;errExit(&quot;malloc&quot;); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fhp-&gt;handle_bytes&nbsp;=&nbsp;handle_bytes; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fhp-&gt;handle_type&nbsp;=&nbsp;strtoul(nextp,&nbsp;&amp;nextp, 0); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;for&nbsp;(int j&nbsp;=&nbsp;0;&nbsp;j&nbsp;&lt;&nbsp;fhp-&gt;handle_bytes;&nbsp;j++)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fhp-&gt;f_handle[j]&nbsp;=&nbsp;strtoul(nextp,&nbsp;&amp;nextp, 16); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Obtain file descriptor for mount point, either by opening<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;the pathname specified on the command line, or by scanning<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/proc/self/mounts to find a mount that matches the&nbsp;&#8216;mount_id&#8217;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;that we received from stdin.&nbsp;*/ </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(argc&nbsp;&gt;&nbsp;1)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;mount_fd&nbsp;=&nbsp;open(argv[1], O_RDONLY);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;else<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;mount_fd&nbsp;=&nbsp;open_mount_path_by_id(mount_id); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(mount_fd&nbsp;==&nbsp;-1)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;errExit(&quot;opening mount fd&quot;); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Open file using handle and mount point&nbsp;*/ </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fd&nbsp;=&nbsp;open_by_handle_at(mount_fd, fhp, O_RDONLY);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(fd&nbsp;==&nbsp;-1)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;errExit(&quot;open_by_handle_at&quot;); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Try reading a few bytes from the file&nbsp;*/ </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;nread&nbsp;=&nbsp;read(fd, buf, sizeof(buf));<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(nread&nbsp;==&nbsp;-1)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;errExit(&quot;read&quot;); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;Read&nbsp;%zd bytes
&quot;, nread); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_SUCCESS); }</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-open/">open</a></code>(2), <code><a href="/docs/linux/man/3-libblkid/">libblkid</a></code>(3), <code><a href="/docs/linux/man/8-blkid/">blkid</a></code>(8), <code><a href="/docs/linux/man/8-findfs/">findfs</a></code>(8), <code><a href="/docs/linux/man/8-mount/">mount</a></code>(8) </p>
<p> The <i>libblkid</i> and <i>libmount</i> documentation in the latest <i>util-linux</i> release at</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
