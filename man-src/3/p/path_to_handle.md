---
title: "path_to_handle(3)"
name: "path_to_handle"
section: "3"
letter: "p"
url: "/docs/linux/man/3-path_to_handle/"
description: "path_to_handle, path_to_fshandle, fd_to_handle, handle_to_fshandle, open_by_handle, readlink_by_handle, attr_multi_by_handle, attr_list_by_handle, fssetdm_by_handle, free_handle, getparents_by_hand..."
---

<p>path_to_handle, path_to_fshandle, fd_to_handle, handle_to_fshandle, open_by_handle, readlink_by_handle, attr_multi_by_handle, attr_list_by_handle, fssetdm_by_handle, free_handle, getparents_by_handle, getparentpaths_by_handle &#8211; file handle operations</p>
<h2>C Synopsis</h2>
<p><code>#include &lt;sys/types.h&gt;</code><br />
 <code>#include &lt;xfs/handle.h&gt;</code></p>
<dl>
<dt> <code>int path_to_handle(char *</code><i>path</i><code>, void **</code><i>hanp</i><code>, size_t *</code><i>hlen</i><code>);</code></p>
<dt> <code>int path_to_fshandle(char *</code><i>path</i><code>, void **</code><i>hanp</i><code>, size_t *</code><i>hlen</i><code>);</code></p>
<dt> <code>int fd_to_handle(int </code><i>fd</i><code>, void **</code><i>hanp</i><code>, size_t *</code><i>hlen</i><code>);</code></p>
<dt> <code>int handle_to_fshandle(void *</code><i>hanp</i><code>, size_t </code><i>hlen</i><code>, void **</code><i>fshanp</i><code>,</code> <code>size_t *</code><i>fshlen</i><code>);</code></p>
<dt> <code>int open_by_handle(void *</code><i>hanp</i><code>, size_t </code><i>hlen</i><code>, int </code><i>oflag</i><code>);</code></p>
<dt> <code>int readlink_by_handle(void *</code><i>hanp</i><code>, size_t </code><i>hlen</i><code>, void *</code><i>buf</i><code>,</code> <code>size_t </code><i>bs</i><code>);</code></p>
<dt> <code>int attr_multi_by_handle(void *</code><i>hanp</i><code>, size_t </code><i>hlen</i><code>, void *</code><i>buf</i><code>,</code> <code>int </code><i>rtrvcnt</i><code>, int </code><i>flags</i><code>);</code></p>
<dt> <code>int attr_list_by_handle(void *</code><i>hanp</i><code>, size_t </code><i>hlen</i><code>, char *</code><i>buf</i><code>,</code> <code>size_t </code><i>bufsiz</i><code>, int </code><i>flags</i><code>, struct attrlist_cursor *</code><i>cursor</i><code>);</code></p>
<dt> <code>int fssetdm_by_handle(void *</code><i>hanp</i><code>, size_t </code><i>hlen</i><code>, struct fsdmidata</code> <code>*</code><i>fssetdm</i><code>);</code></p>
<dt> <code>void free_handle(void *</code><i>hanp</i><code>, size_t </code><i>hlen</i><code>);</code></p>
<dt> <code>int getparents_by_handle(void *</code><i>hanp</i><code>, size_t </code><i>hlen</i><code>, parent_t *</code><i>buf</i><code>,</code> <code>size_t </code><i>bufsiz</i><code>, parent_cursor_t *</code><i>cursor</i><code>, unsigned int *</code><i>count</i><code>,</code> <code>unsigned int *</code><i>more</i><code>);</code></p>
<dt> <code>int getparentpaths_by_handle(void *</code><i>hanp</i><code>, size_t </code><i>hlen</i><code>, parent_t</code> <code>*</code><i>buf</i><code>, size_t </code><i>bufsiz</i><code>, parent_cursor_t *</code><i>cursor</i><code>, unsigned int </code> <code>*</code><i>count</i><code>, unsigned int *</code><i>more</i><code>);</code></dl>
<h2>Description</h2>
<dd>These functions provide a way to perform certain filesystem operations without using a file descriptor to access filesystem objects. They are intended for use by a limited set of system utilities such as backup programs. They are supported only by the XFS filesystem. Link with the <code>libhandle</code> library to access these functions. </p>
<p> A handle, <i>hanp</i>, uniquely identifies a filesystem object or an entire filesystem. There is one and only one handle per filesystem or filesystem object. Handles consist of some number of bytes. The size of a handle (i.e. the number of bytes comprising it) varies by the type of handle and may vary for different objects of the same type. The content of a handle is opaque to applications. Since handle sizes vary and their contents are opaque, handles are described by two quantities, a pointer (<i>hanp</i>) and a size (<i>hlen</i>). The size, <i>hlen</i>, indicates the number of bytes in the handle which are pointed to by the pointer. </p>
<p> The <code>path_to_handle</code>() function returns the handle for the object given by the <i>path</i> argument. If the final component of the path name is a symbolic link, the handle returned is that of the link itself. </p>
<p> The <code>path_to_fshandle</code>() function returns the handle for the filesystem in which the object given by the <i>path</i> argument resides. </p>
<p> The <code>fd_to_handle</code>() function returns the handle for the object referenced by the <i>fd</i> argument, which must be a valid file descriptor. </p>
<p> The <code>handle_to_fshandle</code>() function returns the handle for the filesystem in which the object referenced by the handle given by the <i>hanp</i> and <i>hlen</i> arguments resides. </p>
<p> The <code>open_by_handle</code>() function opens a file descriptor for the object referenced by a handle. It is analogous and identical to <code><a href="/docs/linux/man/2-open/">open</a></code>(2) with the exception of accepting handles instead of path names. </p>
<p> The <code>readlink_by_handle</code>() function returns the contents of a symbolic link referenced by a handle. </p>
<p> The <code>attr_multi_by_handle</code>() function manipulates multiple user attributes on a filesystem object. It is analogous and identical to <code><a href="/docs/linux/man/3-attr_multif/">attr_multif</a></code>(3) except that a handle is specified instead of a file descriptor. </p>
<p> The <code>attr_list_by_handle</code>() function returns the names of the user attributes of a filesystem object. It is analogous and identical to <code><a href="/docs/linux/man/3-attr_listf/">attr_listf</a></code>(3) except that a handle is specified instead of a file descriptor. </p>
<p> The <code>fssetdm_by_handle</code>() function sets the <code>di_dmevmask</code> and <code>di_dmstate</code> fields in an XFS on-disk inode. It is analogous to the <code>XFS_IOC_FSSETDM <a href="/docs/linux/man/3-xfsctl/">xfsctl</a></code>(3) command, except that a handle is specified instead of a file. </p>
<p> The <code>free_handle</code>() function frees the storage allocated for handles returned by the following functions: <code>path_to_handle</code>(), <code>path_to_fshandle</code>(), <code>fd_to_handle</code>(), and <code>handle_to_fshandle</code>(). </p>
<p> The <code>getparents_by_handle</code>() function returns an array of <code>parent_t</code> structures for each hardlink to the inode represented by the given handle. The parent structure encodes the parent inode number, generation number and the basename of the link. <code>This function is not operational on Linux.</code> </p>
<p> The <code>getparentpaths_by_handle</code>() function is identical to the <code>getparents_by_handle</code>() function except that instead of returning the basename it returns the path of the link up to the mount point. <code>This function is also not operational on Linux.</code></p>
<h2>Return Value</h2>
<p>The function <code>free_handle</code>() has no failure indication. The other functions return the value 0 to the calling process if they succeed; otherwise, they return the value -1 and set <i>errno</i> to indicate the error.</p>
<h2>Errors</h2>
<dl>
<dt><code>EACCES</code></p>
<dd>Search permission was denied for a component of <i>path</i>.</p>
<dt><code>EBADF</code></p>
<dd><i>fd</i> is not a valid and open file descriptor.</p>
<dt><code>EFAULT</code></p>
<dd>An argument pointed to an invalid address.</p>
<dt><code>EINVAL</code></p>
<dd><i>path</i> is in a filesystem that does not support these functions.</p>
<dt><code>ELOOP</code></p>
<dd>Too many symbolic links were encountered in translating the path name.</p>
<dt><code>ENAMETOOLONG</code></p>
<dd>A component of <i>path</i> or the entire length of <i>path</i> exceeds filesystem limits.</p>
<dt><code>ENOENT</code></p>
<dd>A component of <i>path</i> does not exist.</p>
<dt><code>EPERM</code></p>
<dd>The caller does not have sufficient privileges.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/2-open/">open</a></code>(2), <code><a href="/docs/linux/man/2-readlink/">readlink</a></code>(2), <code><a href="/docs/linux/man/3-attr_multi/">attr_multi</a></code>(3), <code><a href="/docs/linux/man/3-attr_list/">attr_list</a></code>(3), <code><a href="/docs/linux/man/3-xfsctl/">xfsctl</a></code>(3), <code><a href="/docs/linux/man/5-xfs/">xfs</a></code>(5). </p>
