---
title: "fanotify_mark(2)"
name: "fanotify_mark"
section: "2"
letter: "f"
url: "/docs/linux/man/2-fanotify_mark/"
description: "fanotify_mark – add, remove, or modify an fanotify mark on a filesystem object"
---

<h2 class="name">NAME</h2>
<p> fanotify_mark &#8211; add, remove, or modify an fanotify mark on a filesystem object </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;sys/fanotify.h&gt;
int fanotify_mark(int fanotify_fd, unsigned int flags,
                  uint64_t mask, int dirfd, const char *pathname);
</code></pre>
<h2>DESCRIPTION</h2>
<p> For an overview of the fanotify API, see <code><a href="/docs/linux/man/7-fanotify/">fanotify</a></code>(7). </p>
<p> <code>fanotify_mark</code>() adds, removes, or modifies an fanotify mark on a filesystem object. The caller must have read permission on the filesystem object that is to be marked. </p>
<p> The <i>fanotify_fd</i> argument is a file descriptor returned by <code><a href="/docs/linux/man/2-fanotify_init/">fanotify_init</a></code>(2). </p>
<p> <i>flags</i> is a bit mask describing the modification to perform. It must include exactly one of the following values:</p>
<dl>
<dt><code>FAN_MARK_ADD</code></p>
<dd> The events in <i>mask</i> will be added to the mark mask (or to the ignore mask). <i>mask</i> must be nonempty or the error <code>EINVAL</code> will occur.</p>
<dt><code>FAN_MARK_REMOVE</code></p>
<dd> The events in argument <i>mask</i> will be removed from the mark mask (or from the ignore mask). <i>mask</i> must be nonempty or the error <code>EINVAL</code> will occur.</p>
<dt><code>FAN_MARK_FLUSH</code></p>
<dd> Remove either all marks for filesystems, all marks for mounts, or all marks for directories and files from the fanotify group. If <i>flags</i> contains <code>FAN_MARK_MOUNT</code>, all marks for mounts are removed from the group. If <i>flags</i> contains <code>FAN_MARK_FILESYSTEM</code>, all marks for filesystems are removed from the group. Otherwise, all marks for directories and files are removed. No flag other than and at most one of the flags <code>FAN_MARK_MOUNT</code> or <code>FAN_MARK_FILESYSTEM</code> can be used in conjunction with <code>FAN_MARK_FLUSH</code>. <i>mask</i> is ignored.</dl>
<p> If none of the values above is specified, or more than one is specified, the call fails with the error <code>EINVAL</code>. </p>
<p> In addition, zero or more of the following values may be ORed into <i>flags</i>:</p>
<dl>
<dt><code>FAN_MARK_DONT_FOLLOW</code></p>
<dd> If <i>pathname</i> is a symbolic link, mark the link itself, rather than the file to which it refers. (By default, <code>fanotify_mark</code>() dereferences <i>pathname</i> if it is a symbolic link.)</p>
<dt><code>FAN_MARK_ONLYDIR</code></p>
<dd> If the filesystem object to be marked is not a directory, the error <code>ENOTDIR</code> shall be raised.</p>
<dt><code>FAN_MARK_MOUNT</code></p>
<dd> Mark the mount point specified by <i>pathname</i>. If <i>pathname</i> is not itself a mount point, the mount point containing <i>pathname</i> will be marked. All directories, subdirectories, and the contained files of the mount point will be monitored. The events which require that filesystem objects are identified by file handles, such as <code>FAN_CREATE</code>, <code>FAN_ATTRIB</code>, <code>FAN_MOVE</code>, and <code>FAN_DELETE_SELF</code>, cannot be provided as a <i>mask</i> when <i>flags</i> contains <code>FAN_MARK_MOUNT</code>. Attempting to do so will result in the error <code>EINVAL</code> being returned.</p>
<dt><code>FAN_MARK_FILESYSTEM</code> (since Linux 4.20)</p>
<dd> Mark the filesystem specified by <i>pathname</i>. The filesystem containing <i>pathname</i> will be marked. All the contained files and directories of the filesystem from any mount point will be monitored.</p>
<dt><code>FAN_MARK_IGNORED_MASK</code></p>
<dd> The events in <i>mask</i> shall be added to or removed from the ignore mask.</p>
<dt><code>FAN_MARK_IGNORED_SURV_MODIFY</code></p>
<dd> The ignore mask shall survive modify events. If this flag is not set, the ignore mask is cleared when a modify event occurs for the ignored file or directory.</dl>
<p> <i>mask</i> defines which events shall be listened for (or which shall be ignored). It is a bit mask composed of the following values:</p>
<dl>
<dt><code>FAN_ACCESS</code></p>
<dd> Create an event when a file or directory (but see BUGS) is accessed (read).</p>
<dt><code>FAN_MODIFY</code></p>
<dd> Create an event when a file is modified (write).</p>
<dt><code>FAN_CLOSE_WRITE</code></p>
<dd> Create an event when a writable file is closed.</p>
<dt><code>FAN_CLOSE_NOWRITE</code></p>
<dd> Create an event when a read-only file or directory is closed.</p>
<dt><code>FAN_OPEN</code></p>
<dd> Create an event when a file or directory is opened.</p>
<dt><code>FAN_OPEN_EXEC</code> (since Linux 5.0)</p>
<dd> Create an event when a file is opened with the intent to be executed. See NOTES for additional details.</p>
<dt><code>FAN_ATTRIB</code> (since Linux 5.1)</p>
<dd> Create an event when the metadata for a file or directory has changed. An fanotify group that identifies filesystem objects by file handles is required.</p>
<dt><code>FAN_CREATE</code> (since Linux 5.1)</p>
<dd> Create an event when a file or directory has been created in a marked parent directory. An fanotify group that identifies filesystem objects by file handles is required.</p>
<dt><code>FAN_DELETE</code> (since Linux 5.1)</p>
<dd> Create an event when a file or directory has been deleted in a marked parent directory. An fanotify group that identifies filesystem objects by file handles is required.</p>
<dt><code>FAN_DELETE_SELF</code> (since Linux 5.1)</p>
<dd> Create an event when a marked file or directory itself is deleted. An fanotify group that identifies filesystem objects by file handles is required.</p>
<dt><code>FAN_MOVED_FROM</code> (since Linux 5.1)</p>
<dd> Create an event when a file or directory has been moved from a marked parent directory. An fanotify group that identifies filesystem objects by file handles is required.</p>
<dt><code>FAN_MOVED_TO</code> (since Linux 5.1)</p>
<dd> Create an event when a file or directory has been moved to a marked parent directory. An fanotify group that identifies filesystem objects by file handles is required.</p>
<dt><code>FAN_MOVE_SELF</code> (since Linux 5.1)</p>
<dd> Create an event when a marked file or directory itself has been moved. An fanotify group that identifies filesystem objects by file handles is required.</p>
<dt><code>FAN_OPEN_PERM</code></p>
<dd> Create an event when a permission to open a file or directory is requested. An fanotify file descriptor created with <code>FAN_CLASS_PRE_CONTENT</code> or <code>FAN_CLASS_CONTENT</code> is required.</p>
<dt><code>FAN_OPEN_EXEC_PERM</code> (since Linux 5.0)</p>
<dd> Create an event when a permission to open a file for execution is requested. An fanotify file descriptor created with <code>FAN_CLASS_PRE_CONTENT</code> or <code>FAN_CLASS_CONTENT</code> is required. See NOTES for additional details.</p>
<dt><code>FAN_ACCESS_PERM</code></p>
<dd> Create an event when a permission to read a file or directory is requested. An fanotify file descriptor created with <code>FAN_CLASS_PRE_CONTENT</code> or <code>FAN_CLASS_CONTENT</code> is required.</p>
<dt><code>FAN_ONDIR</code></p>
<dd> Create events for directories&#8212;for example, when <code><a href="/docs/linux/man/3-opendir/">opendir</a></code>(3), <code><a href="/docs/linux/man/3-readdir/">readdir</a></code>(3) (but see BUGS), and <code><a href="/docs/linux/man/3-closedir/">closedir</a></code>(3) are called. Without this flag, events are created only for files. In the context of directory entry events, such as <code>FAN_CREATE</code>, <code>FAN_DELETE</code>, <code>FAN_MOVED_FROM</code>, and <code>FAN_MOVED_TO</code>, specifying the flag <code>FAN_ONDIR</code> is required in order to create events when subdirectory entries are modified (i.e., <code><a href="/docs/linux/man/2-mkdir/">mkdir</a></code>(2)/ <code><a href="/docs/linux/man/2-rmdir/">rmdir</a></code>(2)).</p>
<dt><code>FAN_EVENT_ON_CHILD</code></p>
<dd> Events for the immediate children of marked directories shall be created. The flag has no effect when marking mounts and filesystems. Note that events are not generated for children of the subdirectories of marked directories. More specifically, the directory entry modification events <code>FAN_CREATE</code>, <code>FAN_DELETE</code>, <code>FAN_MOVED_FROM</code>, and <code>FAN_MOVED_TO</code> are not generated for any entry modifications performed inside subdirectories of marked directories. Note that the events <code>FAN_DELETE_SELF</code> and <code>FAN_MOVE_SELF</code> are not generated for children of marked directories. To monitor complete directory trees it is necessary to mark the relevant mount or filesystem.</dl>
<p> The following composed values are defined:</p>
<dl>
<dt><code>FAN_CLOSE</code></p>
<dd> A file is closed (<code>FAN_CLOSE_WRITE</code>|<code>FAN_CLOSE_NOWRITE</code>).</p>
<dt><code>FAN_MOVE</code></p>
<dd> A file or directory has been moved (<code>FAN_MOVED_FROM</code>|<code>FAN_MOVED_TO</code>).</dl>
<p> The filesystem object to be marked is determined by the file descriptor <i>dirfd</i> and the pathname specified in <i>pathname</i>:</p>
<dl>
<dt>*</p>
<dd> If <i>pathname</i> is NULL, <i>dirfd</i> defines the filesystem object to be marked.</p>
<dt>*</p>
<dd> If <i>pathname</i> is NULL, and <i>dirfd</i> takes the special value <code>AT_FDCWD</code>, the current working directory is to be marked.</p>
<dt>*</p>
<dd> If <i>pathname</i> is absolute, it defines the filesystem object to be marked, and <i>dirfd</i> is ignored.</p>
<dt>*</p>
<dd> If <i>pathname</i> is relative, and <i>dirfd</i> does not have the value <code>AT_FDCWD</code>, then the filesystem object to be marked is determined by interpreting <i>pathname</i> relative the directory referred to by <i>dirfd</i>.</p>
<dt>*</p>
<dd> If <i>pathname</i> is relative, and <i>dirfd</i> has the value <code>AT_FDCWD</code>, then the filesystem object to be marked is determined by interpreting <i>pathname</i> relative the current working directory.</dl>
<h2>RETURN VALUE</h2>
<p> On success, <code>fanotify_mark</code>() returns 0. On error, -1 is returned, and <i>errno</i> is set to indicate the error.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EBADF</code></p>
<dd> An invalid file descriptor was passed in <i>fanotify_fd</i>.</p>
<dt><code>EINVAL</code></p>
<dd> An invalid value was passed in <i>flags</i> or <i>mask</i>, or <i>fanotify_fd</i> was not an fanotify file descriptor.</p>
<dt><code>EINVAL</code></p>
<dd> The fanotify file descriptor was opened with <code>FAN_CLASS_NOTIF</code> or the fanotify group identifies filesystem objects by file handles and mask contains a flag for permission events (<code>FAN_OPEN_PERM</code> or <code>FAN_ACCESS_PERM</code>).</p>
<dt><code>ENODEV</code></p>
<dd> The filesystem object indicated by <i>pathname</i> is not associated with a filesystem that supports <i>fsid</i> (e.g., <code><a href="/docs/linux/man/5-tmpfs/">tmpfs</a></code>(5)). This error can be returned only with an fanotify group that identifies filesystem objects by file handles.</p>
<dt><code>ENOENT</code></p>
<dd> The filesystem object indicated by <i>dirfd</i> and <i>pathname</i> does not exist. This error also occurs when trying to remove a mark from an object which is not marked.</p>
<dt><code>ENOMEM</code></p>
<dd> The necessary memory could not be allocated.</p>
<dt><code>ENOSPC</code></p>
<dd> The number of marks exceeds the limit of 8192 and the <code>FAN_UNLIMITED_MARKS</code> flag was not specified when the fanotify file descriptor was created with <code><a href="/docs/linux/man/2-fanotify_init/">fanotify_init</a></code>(2).</p>
<dt><code>ENOSYS</code></p>
<dd> This kernel does not implement <code>fanotify_mark</code>(). The fanotify API is available only if the kernel was configured with <code>CONFIG_FANOTIFY</code>.</p>
<dt><code>ENOTDIR</code></p>
<dd> <i>flags</i> contains <code>FAN_MARK_ONLYDIR</code>, and <i>dirfd</i> and <i>pathname</i> do not specify a directory.</p>
<dt><code>EOPNOTSUPP</code></p>
<dd> The object indicated by <i>pathname</i> is associated with a filesystem that does not support the encoding of file handles. This error can be returned only with an fanotify group that identifies filesystem objects by file handles.</p>
<dt><code>EXDEV</code></p>
<dd> The filesystem object indicated by <i>pathname</i> resides within a filesystem subvolume (e.g., <code><a href="/docs/linux/man/5-btrfs/">btrfs</a></code>(5)) which uses a different <i>fsid</i> than its root superblock. This error can be returned only with an fanotify group that identifies filesystem objects by file handles.</dl>
<h2>VERSIONS</h2>
<p> <code>fanotify_mark</code>() was introduced in version 2.6.36 of the Linux kernel and enabled in version 2.6.37.</p>
<h2>CONFORMING TO</h2>
<p> This system call is Linux-specific.</p>
<h2>NOTES</h2>
<h3>FAN_OPEN_EXEC and FAN_OPEN_EXEC_PERM</h3>
<p> When using either <code>FAN_OPEN_EXEC</code> or <code>FAN_OPEN_EXEC_PERM</code> within the <i>mask</i>, events of these types will be returned only when the direct execution of a program occurs. More specifically, this means that events of these types will be generated for files that are opened using <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2), <code><a href="/docs/linux/man/2-execveat/">execveat</a></code>(2), or <code><a href="/docs/linux/man/2-uselib/">uselib</a></code>(2). Events of these types will not be raised in the situation where an interpreter is passed (or reads) a file for interpretation. </p>
<p> Additionally, if a mark has also been placed on the Linux dynamic linker, a user should also expect to receive an event for it when an ELF object has been successfully opened using <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2) or <code><a href="/docs/linux/man/2-execveat/">execveat</a></code>(2). </p>
<p> For example, if the following ELF binary were to be invoked and a <code>FAN_OPEN_EXEC</code> mark has been placed on /: </p>
<p> $ /bin/echo foo </p>
<p> The listening application in this case would receive <code>FAN_OPEN_EXEC</code> events for both the ELF binary and interpreter, respectively: </p>
<p> /bin/echo /lib64/ld-linux-x86-64.so.2</p>
<h2>BUGS</h2>
<p> The following bugs were present in Linux kernels before version 3.16:</p>
<dl>
<dt>*</p>
<dd> If <i>flags</i> contains <code>FAN_MARK_FLUSH</code>, <i>dirfd</i>, and <i>pathname</i> must specify a valid filesystem object, even though this object is not used.</p>
<dt>*</p>
<dd> <code><a href="/docs/linux/man/2-readdir/">readdir</a></code>(2) does not generate a <code>FAN_ACCESS</code> event.</p>
<dt>*</p>
<dd> If <code>fanotify_mark</code>() is called with <code>FAN_MARK_FLUSH</code>, <i>flags</i> is not checked for invalid values.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-fanotify_init/">fanotify_init</a></code>(2), <code><a href="/docs/linux/man/7-fanotify/">fanotify</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
