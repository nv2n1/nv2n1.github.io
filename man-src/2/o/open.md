---
title: "open(2)"
name: "open"
section: "2"
letter: "o"
url: "/docs/linux/man/2-open/"
description: "open, openat, creat – open and possibly create a file"
---

<h2 class="name">NAME</h2>
<p> open, openat, creat &#8211; open and possibly create a file </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;fcntl.h&gt;
#include &lt;sys/stat.h&gt;
#include &lt;sys/types.h&gt;
int open(const char *pathname, int flags);
int open(const char *pathname, int flags, mode_t mode);
int creat(const char *pathname, mode_t mode);
int openat(int dirfd, const char *pathname, int flags);
int openat(int dirfd, const char *pathname, int flags, mode_t mode);
/* Documented separately, in openat2(2): */
int openat2(int dirfd, const char *pathname,
            const struct open_how *how, size_t size);
</code></pre>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p> <code>openat</code>():</p>
<dl>
<dt>
<dd>
<dl>
<dt>Since glibc 2.10:</p>
<dd> _POSIX_C_SOURCE&nbsp;&gt;=&nbsp;200809L</p>
<dt>Before glibc 2.10:</p>
<dd> _ATFILE_SOURCE</dl>
</dl>
<h2>DESCRIPTION</h2>
<p> The <code>open</code>() system call opens the file specified by <i>pathname</i>. If the specified file does not exist, it may optionally (if <code>O_CREAT</code> is specified in <i>flags</i>) be created by <code>open</code>(). </p>
<p> The return value of <code>open</code>() is a file descriptor, a small, nonnegative integer that is used in subsequent system calls (<code><a href="/docs/linux/man/2-read/">read</a></code>(2), <code><a href="/docs/linux/man/2-write/">write</a></code>(2), <code><a href="/docs/linux/man/2-lseek/">lseek</a></code>(2), <code><a href="/docs/linux/man/2-fcntl/">fcntl</a></code>(2), etc.) to refer to the open file. The file descriptor returned by a successful call will be the lowest-numbered file descriptor not currently open for the process. </p>
<p> By default, the new file descriptor is set to remain open across an <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2) (i.e., the <code>FD_CLOEXEC</code> file descriptor flag described in <code><a href="/docs/linux/man/2-fcntl/">fcntl</a></code>(2) is initially disabled); the <code>O_CLOEXEC</code> flag, described below, can be used to change this default. The file offset is set to the beginning of the file (see <code><a href="/docs/linux/man/2-lseek/">lseek</a></code>(2)). </p>
<p> A call to <code>open</code>() creates a new <i>open file description</i>, an entry in the system-wide table of open files. The open file description records the file offset and the file status flags (see below). A file descriptor is a reference to an open file description; this reference is unaffected if <i>pathname</i> is subsequently removed or modified to refer to a different file. For further details on open file descriptions, see NOTES. </p>
<p> The argument <i>flags</i> must include one of the following <i>access modes</i>: <code>O_RDONLY</code>, <code>O_WRONLY</code>, or <code>O_RDWR</code>. These request opening the file read-only, write-only, or read/write, respectively. </p>
<p> In addition, zero or more file creation flags and file status flags can be bitwise-<i>or</i>&#8216;d in <i>flags</i>. The <i>file creation flags</i> are <code>O_CLOEXEC</code>, <code>O_CREAT</code>, <code>O_DIRECTORY</code>, <code>O_EXCL</code>, <code>O_NOCTTY</code>, <code>O_NOFOLLOW</code>, <code>O_TMPFILE</code>, and <code>O_TRUNC</code>. The <i>file status flags</i> are all of the remaining flags listed below. The distinction between these two groups of flags is that the file creation flags affect the semantics of the open operation itself, while the file status flags affect the semantics of subsequent I/O operations. The file status flags can be retrieved and (in some cases) modified; see <code><a href="/docs/linux/man/2-fcntl/">fcntl</a></code>(2) for details. </p>
<p> The full list of file creation flags and file status flags is as follows:</p>
<dl>
<dt><code>O_APPEND</code></p>
<dd> The file is opened in append mode. Before each <code><a href="/docs/linux/man/2-write/">write</a></code>(2), the file offset is positioned at the end of the file, as if with <code><a href="/docs/linux/man/2-lseek/">lseek</a></code>(2). The modification of the file offset and the write operation are performed as a single atomic step.</p>
<dt>
<dd> <code>O_APPEND</code> may lead to corrupted files on NFS filesystems if more than one process appends data to a file at once. This is because NFS does not support appending to a file, so the client kernel has to simulate it, which can&#8217;t be done without a race condition.</p>
<dt><code>O_ASYNC</code></p>
<dd> Enable signal-driven I/O: generate a signal (<code>SIGIO</code> by default, but this can be changed via <code><a href="/docs/linux/man/2-fcntl/">fcntl</a></code>(2)) when input or output becomes possible on this file descriptor. This feature is available only for terminals, pseudoterminals, sockets, and (since Linux 2.6) pipes and FIFOs. See <code><a href="/docs/linux/man/2-fcntl/">fcntl</a></code>(2) for further details. See also BUGS, below.</p>
<dt><code>O_CLOEXEC</code> (since Linux 2.6.23)</p>
<dd> Enable the close-on-exec flag for the new file descriptor. Specifying this flag permits a program to avoid additional <code><a href="/docs/linux/man/2-fcntl/">fcntl</a></code>(2) <code>F_SETFD</code> operations to set the <code>FD_CLOEXEC</code> flag.</p>
<dt>
<dd> Note that the use of this flag is essential in some multithreaded programs, because using a separate <code><a href="/docs/linux/man/2-fcntl/">fcntl</a></code>(2) <code>F_SETFD</code> operation to set the <code>FD_CLOEXEC</code> flag does not suffice to avoid race conditions where one thread opens a file descriptor and attempts to set its close-on-exec flag using <code><a href="/docs/linux/man/2-fcntl/">fcntl</a></code>(2) at the same time as another thread does a <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2) plus <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2). Depending on the order of execution, the race may lead to the file descriptor returned by <code>open</code>() being unintentionally leaked to the program executed by the child process created by <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2). (This kind of race is in principle possible for any system call that creates a file descriptor whose close-on-exec flag should be set, and various other Linux system calls provide an equivalent of the <code>O_CLOEXEC</code> flag to deal with this problem.)</p>
<dt><code>O_CREAT</code></p>
<dd> If <i>pathname</i> does not exist, create it as a regular file.</p>
<dt>
<dd> The owner (user ID) of the new file is set to the effective user ID of the process.</p>
<dt>
<dd> The group ownership (group ID) of the new file is set either to the effective group ID of the process (System V semantics) or to the group ID of the parent directory (BSD semantics). On Linux, the behavior depends on whether the set-group-ID mode bit is set on the parent directory: if that bit is set, then BSD semantics apply; otherwise, System V semantics apply. For some filesystems, the behavior also depends on the <i>bsdgroups</i> and <i>sysvgroups</i> mount options described in <code><a href="/docs/linux/man/8-mount/">mount</a></code>(8).</p>
<dt>
<dd> The <i>mode</i> argument specifies the file mode bits to be applied when a new file is created. If neither <code>O_CREAT</code> nor <code>O_TMPFILE</code> is specified in <i>flags</i>, then <i>mode</i> is ignored (and can thus be specified as 0, or simply omitted). The <i>mode</i> argument <code>must</code> be supplied if <code>O_CREAT</code> or <code>O_TMPFILE</code> is specified in <i>flags</i>; if it is not supplied, some arbitrary bytes from the stack will be applied as the file mode.</p>
<dt>
<dd> The effective mode is modified by the process&#8217;s <i>umask</i> in the usual way: in the absence of a default ACL, the mode of the created file is <i>(mode&nbsp;&amp;&nbsp;~umask)</i>.</p>
<dt>
<dd> Note that <i>mode</i> applies only to future accesses of the newly created file; the <code>open</code>() call that creates a read-only file may well return a read/write file descriptor.</p>
<dt>
<dd> The following symbolic constants are provided for <i>mode</i>:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>S_IRWXU</code></p>
<dd> 00700 user (file owner) has read, write, and execute permission</p>
<dt><code>S_IRUSR</code></p>
<dd> 00400 user has read permission</p>
<dt><code>S_IWUSR</code></p>
<dd> 00200 user has write permission</p>
<dt><code>S_IXUSR</code></p>
<dd> 00100 user has execute permission</p>
<dt><code>S_IRWXG</code></p>
<dd> 00070 group has read, write, and execute permission</p>
<dt><code>S_IRGRP</code></p>
<dd> 00040 group has read permission</p>
<dt><code>S_IWGRP</code></p>
<dd> 00020 group has write permission</p>
<dt><code>S_IXGRP</code></p>
<dd> 00010 group has execute permission</p>
<dt><code>S_IRWXO</code></p>
<dd> 00007 others have read, write, and execute permission</p>
<dt><code>S_IROTH</code></p>
<dd> 00004 others have read permission</p>
<dt><code>S_IWOTH</code></p>
<dd> 00002 others have write permission</p>
<dt><code>S_IXOTH</code></p>
<dd> 00001 others have execute permission</dl>
</dl>
<dt>
<dd> According to POSIX, the effect when other bits are set in <i>mode</i> is unspecified. On Linux, the following bits are also honored in <i>mode</i>:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>S_ISUID</code></p>
<dd> 0004000 set-user-ID bit</p>
<dt><code>S_ISGID</code></p>
<dd> 0002000 set-group-ID bit (see <code><a href="/docs/linux/man/7-inode/">inode</a></code>(7)).</p>
<dt><code>S_ISVTX</code></p>
<dd> 0001000 sticky bit (see <code><a href="/docs/linux/man/7-inode/">inode</a></code>(7)).</dl>
</dl>
<dt><code>O_DIRECT</code> (since Linux 2.4.10)</p>
<dd> Try to minimize cache effects of the I/O to and from this file. In general this will degrade performance, but it is useful in special situations, such as when applications do their own caching. File I/O is done directly to/from user-space buffers. The <code>O_DIRECT</code> flag on its own makes an effort to transfer data synchronously, but does not give the guarantees of the <code>O_SYNC</code> flag that data and necessary metadata are transferred. To guarantee synchronous I/O, <code>O_SYNC</code> must be used in addition to <code>O_DIRECT</code>. See NOTES below for further discussion.</p>
<dt>
<dd> A semantically similar (but deprecated) interface for block devices is described in <code><a href="/docs/linux/man/8-raw/">raw</a></code>(8).</p>
<dt><code>O_DIRECTORY</code></p>
<dd> If <i>pathname</i> is not a directory, cause the open to fail. This flag was added in kernel version 2.1.126, to avoid denial-of-service problems if <code><a href="/docs/linux/man/3-opendir/">opendir</a></code>(3) is called on a FIFO or tape device.</p>
<dt><code>O_DSYNC</code></p>
<dd> Write operations on the file will complete according to the requirements of synchronized I/O <i>data</i> integrity completion.</p>
<dt>
<dd> By the time <code><a href="/docs/linux/man/2-write/">write</a></code>(2) (and similar) return, the output data has been transferred to the underlying hardware, along with any file metadata that would be required to retrieve that data (i.e., as though each <code><a href="/docs/linux/man/2-write/">write</a></code>(2) was followed by a call to <code><a href="/docs/linux/man/2-fdatasync/">fdatasync</a></code>(2)). <i>See NOTES below</i>.</p>
<dt><code>O_EXCL</code></p>
<dd> Ensure that this call creates the file: if this flag is specified in conjunction with <code>O_CREAT</code>, and <i>pathname</i> already exists, then <code>open</code>() fails with the error <code>EEXIST</code>.</p>
<dt>
<dd> When these two flags are specified, symbolic links are not followed: if <i>pathname</i> is a symbolic link, then <code>open</code>() fails regardless of where the symbolic link points.</p>
<dt>
<dd> In general, the behavior of <code>O_EXCL</code> is undefined if it is used without <code>O_CREAT</code>. There is one exception: on Linux 2.6 and later, <code>O_EXCL</code> can be used without <code>O_CREAT</code> if <i>pathname</i> refers to a block device. If the block device is in use by the system (e.g., mounted), <code>open</code>() fails with the error <code>EBUSY</code>.</p>
<dt>
<dd> On NFS, <code>O_EXCL</code> is supported only when using NFSv3 or later on kernel 2.6 or later. In NFS environments where <code>O_EXCL</code> support is not provided, programs that rely on it for performing locking tasks will contain a race condition. Portable programs that want to perform atomic file locking using a lockfile, and need to avoid reliance on NFS support for <code>O_EXCL</code>, can create a unique file on the same filesystem (e.g., incorporating hostname and PID), and use <code><a href="/docs/linux/man/2-link/">link</a></code>(2) to make a link to the lockfile. If <code><a href="/docs/linux/man/2-link/">link</a></code>(2) returns 0, the lock is successful. Otherwise, use <code><a href="/docs/linux/man/2-stat/">stat</a></code>(2) on the unique file to check if its link count has increased to 2, in which case the lock is also successful.</p>
<dt><code>O_LARGEFILE</code></p>
<dd> (LFS) Allow files whose sizes cannot be represented in an <i>off_t</i> (but can be represented in an <i>off64_t</i>) to be opened. The <code>_LARGEFILE64_SOURCE</code> macro must be defined (before including <i>any</i> header files) in order to obtain this definition. Setting the <code>_FILE_OFFSET_BITS</code> feature test macro to 64 (rather than using <code>O_LARGEFILE</code>) is the preferred method of accessing large files on 32-bit systems (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)).</p>
<dt><code>O_NOATIME</code> (since Linux 2.6.8)</p>
<dd> Do not update the file last access time (<i>st_atime</i> in the inode) when the file is <code><a href="/docs/linux/man/2-read/">read</a></code>(2).</p>
<dt>
<dd> This flag can be employed only if one of the following conditions is true:</p>
<dl>
<dt>
<dd>
<dl>
<dt>*</p>
<dd> The effective UID of the process matches the owner UID of the file.</p>
<dt>*</p>
<dd> The calling process has the <code>CAP_FOWNER</code> capability in its user namespace and the owner UID of the file has a mapping in the namespace.</dl>
</dl>
<dt>
<dd> This flag is intended for use by indexing or backup programs, where its use can significantly reduce the amount of disk activity. This flag may not be effective on all filesystems. One example is NFS, where the server maintains the access time.</p>
<dt><code>O_NOCTTY</code></p>
<dd> If <i>pathname</i> refers to a terminal device&#8212;see <code><a href="/docs/linux/man/4-tty/">tty</a></code>(4)&#8212;it will not become the process&#8217;s controlling terminal even if the process does not have one.</p>
<dt><code>O_NOFOLLOW</code></p>
<dd> If the trailing component (i.e., basename) of <i>pathname</i> is a symbolic link, then the open fails, with the error <code>ELOOP</code>. Symbolic links in earlier components of the pathname will still be followed. (Note that the <code>ELOOP</code> error that can occur in this case is indistinguishable from the case where an open fails because there are too many symbolic links found while resolving components in the prefix part of the pathname.)</p>
<dt>
<dd> This flag is a FreeBSD extension, which was added to Linux in version 2.1.126, and has subsequently been standardized in POSIX.1-2008.</p>
<dt>
<dd> See also <code>O_PATH</code> below.</p>
<dt><code>O_NONBLOCK</code> or <code>O_NDELAY</code></p>
<dd> When possible, the file is opened in nonblocking mode. Neither the <code>open</code>() nor any subsequent I/O operations on the file descriptor which is returned will cause the calling process to wait.</p>
<dt>
<dd> Note that the setting of this flag has no effect on the operation of <code><a href="/docs/linux/man/2-poll/">poll</a></code>(2), <code><a href="/docs/linux/man/2-select/">select</a></code>(2), <code><a href="/docs/linux/man/7-epoll/">epoll</a></code>(7), and similar, since those interfaces merely inform the caller about whether a file descriptor is &quot;ready&quot;, meaning that an I/O operation performed on the file descriptor with the <code>O_NONBLOCK</code> flag <i>clear</i> would not block.</p>
<dt>
<dd> Note that this flag has no effect for regular files and block devices; that is, I/O operations will (briefly) block when device activity is required, regardless of whether <code>O_NONBLOCK</code> is set. Since <code>O_NONBLOCK</code> semantics might eventually be implemented, applications should not depend upon blocking behavior when specifying this flag for regular files and block devices.</p>
<dt>
<dd> For the handling of FIFOs (named pipes), see also <code><a href="/docs/linux/man/7-fifo/">fifo</a></code>(7). For a discussion of the effect of <code>O_NONBLOCK</code> in conjunction with mandatory file locks and with file leases, see <code><a href="/docs/linux/man/2-fcntl/">fcntl</a></code>(2).</p>
<dt><code>O_PATH</code> (since Linux 2.6.39)</p>
<dd> Obtain a file descriptor that can be used for two purposes: to indicate a location in the filesystem tree and to perform operations that act purely at the file descriptor level. The file itself is not opened, and other file operations (e.g., <code><a href="/docs/linux/man/2-read/">read</a></code>(2), <code><a href="/docs/linux/man/2-write/">write</a></code>(2), <code><a href="/docs/linux/man/2-fchmod/">fchmod</a></code>(2), <code><a href="/docs/linux/man/2-fchown/">fchown</a></code>(2), <code><a href="/docs/linux/man/2-fgetxattr/">fgetxattr</a></code>(2), <code><a href="/docs/linux/man/2-ioctl/">ioctl</a></code>(2), <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2)) fail with the error <code>EBADF</code>.</p>
<dt>
<dd> The following operations <i>can</i> be performed on the resulting file descriptor:</p>
<dl>
<dt>
<dd>
<dl>
<dt>*</p>
<dd> <code><a href="/docs/linux/man/2-close/">close</a></code>(2).</p>
<dt>*</p>
<dd> <code><a href="/docs/linux/man/2-fchdir/">fchdir</a></code>(2), if the file descriptor refers to a directory (since Linux 3.5).</p>
<dt>*</p>
<dd> <code><a href="/docs/linux/man/2-fstat/">fstat</a></code>(2) (since Linux 3.6).</p>
<dt>*</p>
<dd> <code><a href="/docs/linux/man/2-fstatfs/">fstatfs</a></code>(2) (since Linux 3.12).</p>
<dt>*</p>
<dd> Duplicating the file descriptor (<code><a href="/docs/linux/man/2-dup/">dup</a></code>(2), <code><a href="/docs/linux/man/2-fcntl/">fcntl</a></code>(2) <code>F_DUPFD</code>, etc.).</p>
<dt>*</p>
<dd> Getting and setting file descriptor flags (<code><a href="/docs/linux/man/2-fcntl/">fcntl</a></code>(2) <code>F_GETFD</code> and <code>F_SETFD</code>).</p>
<dt>*</p>
<dd> Retrieving open file status flags using the <code><a href="/docs/linux/man/2-fcntl/">fcntl</a></code>(2) <code>F_GETFL</code> operation: the returned flags will include the bit <code>O_PATH</code>.</p>
<dt>*</p>
<dd> Passing the file descriptor as the <i>dirfd</i> argument of <code>openat</code>() and the other &quot;*at()&quot; system calls. This includes <code><a href="/docs/linux/man/2-linkat/">linkat</a></code>(2) with <code>AT_EMPTY_PATH</code> (or via procfs using <code>AT_SYMLINK_FOLLOW</code>) even if the file is not a directory.</p>
<dt>*</p>
<dd> Passing the file descriptor to another process via a UNIX domain socket (see <code>SCM_RIGHTS</code> in <code><a href="/docs/linux/man/7-unix/">unix</a></code>(7)).</dl>
</dl>
<dt>
<dd> When <code>O_PATH</code> is specified in <i>flags</i>, flag bits other than <code>O_CLOEXEC</code>, <code>O_DIRECTORY</code>, and <code>O_NOFOLLOW</code> are ignored.</p>
<dt>
<dd> Opening a file or directory with the <code>O_PATH</code> flag requires no permissions on the object itself (but does require execute permission on the directories in the path prefix). Depending on the subsequent operation, a check for suitable file permissions may be performed (e.g., <code><a href="/docs/linux/man/2-fchdir/">fchdir</a></code>(2) requires execute permission on the directory referred to by its file descriptor argument). By contrast, obtaining a reference to a filesystem object by opening it with the <code>O_RDONLY</code> flag requires that the caller have read permission on the object, even when the subsequent operation (e.g., <code><a href="/docs/linux/man/2-fchdir/">fchdir</a></code>(2), <code><a href="/docs/linux/man/2-fstat/">fstat</a></code>(2)) does not require read permission on the object.</p>
<dt>
<dd> If <i>pathname</i> is a symbolic link and the <code>O_NOFOLLOW</code> flag is also specified, then the call returns a file descriptor referring to the symbolic link. This file descriptor can be used as the <i>dirfd</i> argument in calls to <code><a href="/docs/linux/man/2-fchownat/">fchownat</a></code>(2), <code><a href="/docs/linux/man/2-fstatat/">fstatat</a></code>(2), <code><a href="/docs/linux/man/2-linkat/">linkat</a></code>(2), and <code><a href="/docs/linux/man/2-readlinkat/">readlinkat</a></code>(2) with an empty pathname to have the calls operate on the symbolic link.</p>
<dt>
<dd> If <i>pathname</i> refers to an automount point that has not yet been triggered, so no other filesystem is mounted on it, then the call returns a file descriptor referring to the automount directory without triggering a mount. <code><a href="/docs/linux/man/2-fstatfs/">fstatfs</a></code>(2) can then be used to determine if it is, in fact, an untriggered automount point (<code>.f_type == AUTOFS_SUPER_MAGIC</code>).</p>
<dt>
<dd> One use of <code>O_PATH</code> for regular files is to provide the equivalent of POSIX.1&#8217;s <code>O_EXEC</code> functionality. This permits us to open a file for which we have execute permission but not read permission, and then execute that file, with steps something like the following:</p>
<dt>
<dd> char buf[PATH_MAX]; fd = open(&quot;some_prog&quot;, O_PATH); snprintf(buf, PATH_MAX, &quot;/proc/self/fd/%d&quot;, fd); execl(buf, &quot;some_prog&quot;, (char *) NULL);</p>
<dt>
<dd> An <code>O_PATH</code> file descriptor can also be passed as the argument of <code><a href="/docs/linux/man/3-fexecve/">fexecve</a></code>(3).</p>
<dt><code>O_SYNC</code></p>
<dd> Write operations on the file will complete according to the requirements of synchronized I/O <i>file</i> integrity completion (by contrast with the synchronized I/O <i>data</i> integrity completion provided by <code>O_DSYNC</code>.)</p>
<dt>
<dd> By the time <code><a href="/docs/linux/man/2-write/">write</a></code>(2) (or similar) returns, the output data and associated file metadata have been transferred to the underlying hardware (i.e., as though each <code><a href="/docs/linux/man/2-write/">write</a></code>(2) was followed by a call to <code><a href="/docs/linux/man/2-fsync/">fsync</a></code>(2)). <i>See NOTES below</i>.</p>
<dt><code>O_TMPFILE</code> (since Linux 3.11)</p>
<dd> Create an unnamed temporary regular file. The <i>pathname</i> argument specifies a directory; an unnamed inode will be created in that directory&#8217;s filesystem. Anything written to the resulting file will be lost when the last file descriptor is closed, unless the file is given a name.</p>
<dt>
<dd> <code>O_TMPFILE</code> must be specified with one of <code>O_RDWR</code> or <code>O_WRONLY</code> and, optionally, <code>O_EXCL</code>. If <code>O_EXCL</code> is not specified, then <code><a href="/docs/linux/man/2-linkat/">linkat</a></code>(2) can be used to link the temporary file into the filesystem, making it permanent, using code like the following:</p>
<dt>
<dd> char path[PATH_MAX]; fd = open(&quot;/path/to/dir&quot;, O_TMPFILE | O_RDWR,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;S_IRUSR | S_IWUSR); </p>
<p> /* File I/O on &#8216;fd&#8217;&#8230; */ </p>
<p> linkat(fd, NULL, AT_FDCWD, &quot;/path/for/file&quot;, AT_EMPTY_PATH); </p>
<p> /* If the caller doesn&#8217;t have the CAP_DAC_READ_SEARCH<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;capability&nbsp;(needed to use AT_EMPTY_PATH with&nbsp;<a href="/docs/linux/man/2-linkat/">linkat</a>(2)),<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;and there is a&nbsp;<a href="/docs/linux/man/5-proc/">proc</a>(5)&nbsp;filesystem mounted, then the<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<a href="/docs/linux/man/2-linkat/">linkat</a>(2)&nbsp;call above can be replaced with: </p>
<p> snprintf(path, PATH_MAX, &quot;/proc/self/fd/%d&quot;, fd); linkat(AT_FDCWD, path, AT_FDCWD, &quot;/path/for/file&quot;,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;AT_SYMLINK_FOLLOW); */</p>
<dt>
<dd> In this case, the <code>open</code>() <i>mode</i> argument determines the file permission mode, as with <code>O_CREAT</code>.</p>
<dt>
<dd> Specifying <code>O_EXCL</code> in conjunction with <code>O_TMPFILE</code> prevents a temporary file from being linked into the filesystem in the above manner. (Note that the meaning of <code>O_EXCL</code> in this case is different from the meaning of <code>O_EXCL</code> otherwise.)</p>
<dt>
<dd> There are two main use cases for <code>O_TMPFILE</code>:</p>
<dl>
<dt>
<dd>
<dl>
<dt>*</p>
<dd> Improved <code><a href="/docs/linux/man/3-tmpfile/">tmpfile</a></code>(3) functionality: race-free creation of temporary files that (1) are automatically deleted when closed; (2) can never be reached via any pathname; (3) are not subject to symlink attacks; and (4) do not require the caller to devise unique names.</p>
<dt>*</p>
<dd> Creating a file that is initially invisible, which is then populated with data and adjusted to have appropriate filesystem attributes (<code><a href="/docs/linux/man/2-fchown/">fchown</a></code>(2), <code><a href="/docs/linux/man/2-fchmod/">fchmod</a></code>(2), <code><a href="/docs/linux/man/2-fsetxattr/">fsetxattr</a></code>(2), etc.) before being atomically linked into the filesystem in a fully formed state (using <code><a href="/docs/linux/man/2-linkat/">linkat</a></code>(2) as described above).</dl>
</dl>
<dt>
<dd> <code>O_TMPFILE</code> requires support by the underlying filesystem; only a subset of Linux filesystems provide that support. In the initial implementation, support was provided in the ext2, ext3, ext4, UDF, Minix, and shmem filesystems. Support for other filesystems has subsequently been added as follows: XFS (Linux 3.15); Btrfs (Linux 3.16); F2FS (Linux 3.16); and ubifs (Linux 4.9)</p>
<dt><code>O_TRUNC</code></p>
<dd> If the file already exists and is a regular file and the access mode allows writing (i.e., is <code>O_RDWR</code> or <code>O_WRONLY</code>) it will be truncated to length 0. If the file is a FIFO or terminal device file, the <code>O_TRUNC</code> flag is ignored. Otherwise, the effect of <code>O_TRUNC</code> is unspecified.</dl>
<h3>creat()</h3>
<p> A call to <code>creat</code>() is equivalent to calling <code>open</code>() with <i>flags</i> equal to <code>O_CREAT|O_WRONLY|O_TRUNC</code>.</p>
<h3>openat()</h3>
<p> The <code>openat</code>() system call operates in exactly the same way as <code>open</code>(), except for the differences described here. </p>
<p> If the pathname given in <i>pathname</i> is relative, then it is interpreted relative to the directory referred to by the file descriptor <i>dirfd</i> (rather than relative to the current working directory of the calling process, as is done by <code>open</code>() for a relative pathname). </p>
<p> If <i>pathname</i> is relative and <i>dirfd</i> is the special value <code>AT_FDCWD</code>, then <i>pathname</i> is interpreted relative to the current working directory of the calling process (like <code>open</code>()). </p>
<p> If <i>pathname</i> is absolute, then <i>dirfd</i> is ignored.</p>
<h3><a href="/docs/linux/man/2-openat2/">openat2</a>(2)</h3>
<p> The <code><a href="/docs/linux/man/2-openat2/">openat2</a></code>(2) system call is an extension of <code>openat</code>(), and provides a superset of the features of <code>openat</code>(). It is documented separately, in <code><a href="/docs/linux/man/2-openat2/">openat2</a></code>(2).</p>
<h2>RETURN VALUE</h2>
<p> <code>open</code>(), <code>openat</code>(), and <code>creat</code>() return the new file descriptor (a nonnegative integer), or -1 if an error occurred (in which case, <i>errno</i> is set appropriately).</p>
<h2>ERRORS</h2>
<p> <code>open</code>(), <code>openat</code>(), and <code>creat</code>() can fail with the following errors:</p>
<dl>
<dt><code>EACCES</code></p>
<dd> The requested access to the file is not allowed, or search permission is denied for one of the directories in the path prefix of <i>pathname</i>, or the file did not exist yet and write access to the parent directory is not allowed. (See also <code><a href="/docs/linux/man/7-path_resolution/">path_resolution</a></code>(7).)</p>
<dt><code>EACCES</code></p>
<dd> Where <code>O_CREAT</code> is specified, the <i>protected_fifos</i> or <i>protected_regular</i> sysctl is enabled, the file already exists and is a FIFO or regular file, the owner of the file is neither the current user nor the owner of the containing directory, and the containing directory is both world- or group-writable and sticky. For details, see the descriptions of <i>/proc/sys/fs/protected_fifos</i> and <i>/proc/sys/fs/protected_regular</i> in <code><a href="/docs/linux/man/5-proc/">proc</a></code>(5).</p>
<dt><code>EBUSY</code></p>
<dd> <code>O_EXCL</code> was specified in <i>flags</i> and <i>pathname</i> refers to a block device that is in use by the system (e.g., it is mounted).</p>
<dt><code>EDQUOT</code></p>
<dd> Where <code>O_CREAT</code> is specified, the file does not exist, and the user&#8217;s quota of disk blocks or inodes on the filesystem has been exhausted.</p>
<dt><code>EEXIST</code></p>
<dd> <i>pathname</i> already exists and <code>O_CREAT</code> and <code>O_EXCL</code> were used.</p>
<dt><code>EFAULT</code></p>
<dd> <i>pathname</i> points outside your accessible address space.</p>
<dt><code>EFBIG</code></p>
<dd> See <code>EOVERFLOW</code>.</p>
<dt><code>EINTR</code></p>
<dd> While blocked waiting to complete an open of a slow device (e.g., a FIFO; see <code><a href="/docs/linux/man/7-fifo/">fifo</a></code>(7)), the call was interrupted by a signal handler; see <code><a href="/docs/linux/man/7-signal/">signal</a></code>(7).</p>
<dt><code>EINVAL</code></p>
<dd> The filesystem does not support the <code>O_DIRECT</code> flag. See <code>NOTES</code> for more information.</p>
<dt><code>EINVAL</code></p>
<dd> Invalid value in <i>flags</i>.</p>
<dt><code>EINVAL</code></p>
<dd> <code>O_TMPFILE</code> was specified in <i>flags</i>, but neither <code>O_WRONLY</code> nor <code>O_RDWR</code> was specified.</p>
<dt><code>EINVAL</code></p>
<dd> <code>O_CREAT</code> was specified in <i>flags</i> and the final component (&quot;basename&quot;) of the new file&#8217;s <i>pathname</i> is invalid (e.g., it contains characters not permitted by the underlying filesystem).</p>
<dt><code>EINVAL</code></p>
<dd> The final component (&quot;basename&quot;) of <i>pathname</i> is invalid (e.g., it contains characters not permitted by the underlying filesystem).</p>
<dt><code>EISDIR</code></p>
<dd> <i>pathname</i> refers to a directory and the access requested involved writing (that is, <code>O_WRONLY</code> or <code>O_RDWR</code> is set).</p>
<dt><code>EISDIR</code></p>
<dd> <i>pathname</i> refers to an existing directory, <code>O_TMPFILE</code> and one of <code>O_WRONLY</code> or <code>O_RDWR</code> were specified in <i>flags</i>, but this kernel version does not provide the <code>O_TMPFILE</code> functionality.</p>
<dt><code>ELOOP</code></p>
<dd> Too many symbolic links were encountered in resolving <i>pathname</i>.</p>
<dt><code>ELOOP</code></p>
<dd> <i>pathname</i> was a symbolic link, and <i>flags</i> specified <code>O_NOFOLLOW</code> but not <code>O_PATH</code>.</p>
<dt><code>EMFILE</code></p>
<dd> The per-process limit on the number of open file descriptors has been reached (see the description of <code>RLIMIT_NOFILE</code> in <code><a href="/docs/linux/man/2-getrlimit/">getrlimit</a></code>(2)).</p>
<dt><code>ENAMETOOLONG</code></p>
<dd> <i>pathname</i> was too long.</p>
<dt><code>ENFILE</code></p>
<dd> The system-wide limit on the total number of open files has been reached.</p>
<dt><code>ENODEV</code></p>
<dd> <i>pathname</i> refers to a device special file and no corresponding device exists. (This is a Linux kernel bug; in this situation <code>ENXIO</code> must be returned.)</p>
<dt><code>ENOENT</code></p>
<dd> <code>O_CREAT</code> is not set and the named file does not exist.</p>
<dt><code>ENOENT</code></p>
<dd> A directory component in <i>pathname</i> does not exist or is a dangling symbolic link.</p>
<dt><code>ENOENT</code></p>
<dd> <i>pathname</i> refers to a nonexistent directory, <code>O_TMPFILE</code> and one of <code>O_WRONLY</code> or <code>O_RDWR</code> were specified in <i>flags</i>, but this kernel version does not provide the <code>O_TMPFILE</code> functionality.</p>
<dt><code>ENOMEM</code></p>
<dd> The named file is a FIFO, but memory for the FIFO buffer can&#8217;t be allocated because the per-user hard limit on memory allocation for pipes has been reached and the caller is not privileged; see <code><a href="/docs/linux/man/7-pipe/">pipe</a></code>(7).</p>
<dt><code>ENOMEM</code></p>
<dd> Insufficient kernel memory was available.</p>
<dt><code>ENOSPC</code></p>
<dd> <i>pathname</i> was to be created but the device containing <i>pathname</i> has no room for the new file.</p>
<dt><code>ENOTDIR</code></p>
<dd> A component used as a directory in <i>pathname</i> is not, in fact, a directory, or <code>O_DIRECTORY</code> was specified and <i>pathname</i> was not a directory.</p>
<dt><code>ENXIO</code></p>
<dd> <code>O_NONBLOCK</code> | <code>O_WRONLY</code> is set, the named file is a FIFO, and no process has the FIFO open for reading.</p>
<dt><code>ENXIO</code></p>
<dd> The file is a device special file and no corresponding device exists.</p>
<dt><code>ENXIO</code></p>
<dd> The file is a UNIX domain socket.</p>
<dt><code>EOPNOTSUPP</code></p>
<dd> The filesystem containing <i>pathname</i> does not support <code>O_TMPFILE</code>.</p>
<dt><code>EOVERFLOW</code></p>
<dd> <i>pathname</i> refers to a regular file that is too large to be opened. The usual scenario here is that an application compiled on a 32-bit platform without <i>-D_FILE_OFFSET_BITS=64</i> tried to open a file whose size exceeds <i>(1&lt;&lt;31)-1</i> bytes; see also <code>O_LARGEFILE</code> above. This is the error specified by POSIX.1; in kernels before 2.6.24, Linux gave the error <code>EFBIG</code> for this case.</p>
<dt><code>EPERM</code></p>
<dd> The <code>O_NOATIME</code> flag was specified, but the effective user ID of the caller did not match the owner of the file and the caller was not privileged.</p>
<dt><code>EPERM</code></p>
<dd> The operation was prevented by a file seal; see <code><a href="/docs/linux/man/2-fcntl/">fcntl</a></code>(2).</p>
<dt><code>EROFS</code></p>
<dd> <i>pathname</i> refers to a file on a read-only filesystem and write access was requested.</p>
<dt><code>ETXTBSY</code></p>
<dd> <i>pathname</i> refers to an executable image which is currently being executed and write access was requested.</p>
<dt><code>ETXTBSY</code></p>
<dd> <i>pathname</i> refers to a file that is currently in use as a swap file, and the <code>O_TRUNC</code> flag was specified.</p>
<dt><code>ETXTBSY</code></p>
<dd> <i>pathname</i> refers to a file that is currently being read by the kernel (e.g., for module/firmware loading), and write access was requested.</p>
<dt><code>EWOULDBLOCK</code></p>
<dd> The <code>O_NONBLOCK</code> flag was specified, and an incompatible lease was held on the file (see <code><a href="/docs/linux/man/2-fcntl/">fcntl</a></code>(2)).</dl>
<p> The following additional errors can occur for <code>openat</code>():</p>
<dl>
<dt><code>EBADF</code></p>
<dd> <i>dirfd</i> is not a valid file descriptor.</p>
<dt><code>ENOTDIR</code></p>
<dd> <i>pathname</i> is a relative pathname and <i>dirfd</i> is a file descriptor referring to a file other than a directory.</dl>
<h2>VERSIONS</h2>
<p> <code>openat</code>() was added to Linux in kernel 2.6.16; library support was added to glibc in version 2.4.</p>
<h2>CONFORMING TO</h2>
<p> <code>open</code>(), <code>creat</code>() SVr4, 4.3BSD, POSIX.1-2001, POSIX.1-2008. </p>
<p> <code>openat</code>(): POSIX.1-2008. </p>
<p> <code><a href="/docs/linux/man/2-openat2/">openat2</a></code>(2) is Linux-specific. </p>
<p> The <code>O_DIRECT</code>, <code>O_NOATIME</code>, <code>O_PATH</code>, and <code>O_TMPFILE</code> flags are Linux-specific. One must define <code>_GNU_SOURCE</code> to obtain their definitions. </p>
<p> The <code>O_CLOEXEC</code>, <code>O_DIRECTORY</code>, and <code>O_NOFOLLOW</code> flags are not specified in POSIX.1-2001, but are specified in POSIX.1-2008. Since glibc 2.12, one can obtain their definitions by defining either <code>_POSIX_C_SOURCE</code> with a value greater than or equal to 200809L or <code>_XOPEN_SOURCE</code> with a value greater than or equal to 700. In glibc 2.11 and earlier, one obtains the definitions by defining <code>_GNU_SOURCE</code>. </p>
<p> As noted in <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7), feature test macros such as <code>_POSIX_C_SOURCE</code>, <code>_XOPEN_SOURCE</code>, and <code>_GNU_SOURCE</code> must be defined before including <i>any</i> header files.</p>
<h2>NOTES</h2>
<p> Under Linux, the <code>O_NONBLOCK</code> flag is sometimes used in cases where one wants to open but does not necessarily have the intention to read or write. For example, this may be used to open a device in order to get a file descriptor for use with <code><a href="/docs/linux/man/2-ioctl/">ioctl</a></code>(2). </p>
<p> The (undefined) effect of <code>O_RDONLY | O_TRUNC</code> varies among implementations. On many systems the file is actually truncated. </p>
<p> Note that <code>open</code>() can open device special files, but <code>creat</code>() cannot create them; use <code><a href="/docs/linux/man/2-mknod/">mknod</a></code>(2) instead. </p>
<p> If the file is newly created, its <i>st_atime</i>, <i>st_ctime</i>, <i>st_mtime</i> fields (respectively, time of last access, time of last status change, and time of last modification; see <code><a href="/docs/linux/man/2-stat/">stat</a></code>(2)) are set to the current time, and so are the <i>st_ctime</i> and <i>st_mtime</i> fields of the parent directory. Otherwise, if the file is modified because of the <code>O_TRUNC</code> flag, its <i>st_ctime</i> and <i>st_mtime</i> fields are set to the current time. </p>
<p> The files in the <i>/proc/[pid]/fd</i> directory show the open file descriptors of the process with the PID <i>pid</i>. The files in the <i>/proc/[pid]/fdinfo</i> directory show even more information about these file descriptors. See <code><a href="/docs/linux/man/5-proc/">proc</a></code>(5) for further details of both of these directories. </p>
<p> The Linux header file <code>&lt;asm/fcntl.h&gt;</code> doesn&#8217;t define <code>O_ASYNC</code>; the (BSD-derived) <code>FASYNC</code> synonym is defined instead.</p>
<h3>Open file descriptions</h3>
<p> The term open file description is the one used by POSIX to refer to the entries in the system-wide table of open files. In other contexts, this object is variously also called an &quot;open file object&quot;, a &quot;file handle&quot;, an &quot;open file table entry&quot;, or&#8212;in kernel-developer parlance&#8212;a <i>struct file</i>. </p>
<p> When a file descriptor is duplicated (using <code><a href="/docs/linux/man/2-dup/">dup</a></code>(2) or similar), the duplicate refers to the same open file description as the original file descriptor, and the two file descriptors consequently share the file offset and file status flags. Such sharing can also occur between processes: a child process created via <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2) inherits duplicates of its parent&#8217;s file descriptors, and those duplicates refer to the same open file descriptions. </p>
<p> Each <code>open</code>() of a file creates a new open file description; thus, there may be multiple open file descriptions corresponding to a file inode. </p>
<p> On Linux, one can use the <code><a href="/docs/linux/man/2-kcmp/">kcmp</a></code>(2) <code>KCMP_FILE</code> operation to test whether two file descriptors (in the same process or in two different processes) refer to the same open file description.</p>
<h3>Synchronized I/O</h3>
<p> The POSIX.1-2008 &quot;synchronized I/O&quot; option specifies different variants of synchronized I/O, and specifies the <code>open</code>() flags <code>O_SYNC</code>, <code>O_DSYNC</code>, and <code>O_RSYNC</code> for controlling the behavior. Regardless of whether an implementation supports this option, it must at least support the use of <code>O_SYNC</code> for regular files. </p>
<p> Linux implements <code>O_SYNC</code> and <code>O_DSYNC</code>, but not <code>O_RSYNC</code>. Somewhat incorrectly, glibc defines <code>O_RSYNC</code> to have the same value as <code>O_SYNC</code>. (<code>O_RSYNC</code> is defined in the Linux header file <i>&lt;asm/fcntl.h&gt;</i> on HP PA-RISC, but it is not used.) </p>
<p> <code>O_SYNC</code> provides synchronized I/O <i>file</i> integrity completion, meaning write operations will flush data and all associated metadata to the underlying hardware. <code>O_DSYNC</code> provides synchronized I/O <i>data</i> integrity completion, meaning write operations will flush data to the underlying hardware, but will only flush metadata updates that are required to allow a subsequent read operation to complete successfully. Data integrity completion can reduce the number of disk operations that are required for applications that don&#8217;t need the guarantees of file integrity completion. </p>
<p> To understand the difference between the two types of completion, consider two pieces of file metadata: the file last modification timestamp (<i>st_mtime</i>) and the file length. All write operations will update the last file modification timestamp, but only writes that add data to the end of the file will change the file length. The last modification timestamp is not needed to ensure that a read completes successfully, but the file length is. Thus, <code>O_DSYNC</code> would only guarantee to flush updates to the file length metadata (whereas <code>O_SYNC</code> would also always flush the last modification timestamp metadata). </p>
<p> Before Linux 2.6.33, Linux implemented only the <code>O_SYNC</code> flag for <code>open</code>(). However, when that flag was specified, most filesystems actually provided the equivalent of synchronized I/O <i>data</i> integrity completion (i.e., <code>O_SYNC</code> was actually implemented as the equivalent of <code>O_DSYNC</code>). </p>
<p> Since Linux 2.6.33, proper <code>O_SYNC</code> support is provided. However, to ensure backward binary compatibility, <code>O_DSYNC</code> was defined with the same value as the historical <code>O_SYNC</code>, and <code>O_SYNC</code> was defined as a new (two-bit) flag value that includes the <code>O_DSYNC</code> flag value. This ensures that applications compiled against new headers get at least <code>O_DSYNC</code> semantics on pre-2.6.33 kernels.</p>
<h3>C library/kernel differences</h3>
<p> Since version 2.26, the glibc wrapper function for <code>open</code>() employs the <code>openat</code>() system call, rather than the kernel&#8217;s <code>open</code>() system call. For certain architectures, this is also true in glibc versions before 2.26.</p>
<h3>NFS</h3>
<p> There are many infelicities in the protocol underlying NFS, affecting amongst others <code>O_SYNC</code> and <code>O_NDELAY</code>. </p>
<p> On NFS filesystems with UID mapping enabled, <code>open</code>() may return a file descriptor but, for example, <code><a href="/docs/linux/man/2-read/">read</a></code>(2) requests are denied with <code>EACCES</code>. This is because the client performs <code>open</code>() by checking the permissions, but UID mapping is performed by the server upon read and write requests.</p>
<h3>FIFOs</h3>
<p> Opening the read or write end of a FIFO blocks until the other end is also opened (by another process or thread). See <code><a href="/docs/linux/man/7-fifo/">fifo</a></code>(7) for further details.</p>
<h3>File access mode</h3>
<p> Unlike the other values that can be specified in <i>flags</i>, the <i>access mode</i> values <code>O_RDONLY</code>, <code>O_WRONLY</code>, and <code>O_RDWR</code> do not specify individual bits. Rather, they define the low order two bits of <i>flags</i>, and are defined respectively as 0, 1, and 2. In other words, the combination <code>O_RDONLY | O_WRONLY</code> is a logical error, and certainly does not have the same meaning as <code>O_RDWR</code>. </p>
<p> Linux reserves the special, nonstandard access mode 3 (binary 11) in <i>flags</i> to mean: check for read and write permission on the file and return a file descriptor that can&#8217;t be used for reading or writing. This nonstandard access mode is used by some Linux drivers to return a file descriptor that is to be used only for device-specific <code><a href="/docs/linux/man/2-ioctl/">ioctl</a></code>(2) operations.</p>
<h3>Rationale for openat() and other directory file descriptor APIs</h3>
<p> <code>openat</code>() and the other system calls and library functions that take a directory file descriptor argument (i.e., <code><a href="/docs/linux/man/2-execveat/">execveat</a></code>(2), <code><a href="/docs/linux/man/2-faccessat/">faccessat</a></code>(2), <code><a href="/docs/linux/man/2-fanotify_mark/">fanotify_mark</a></code>(2), <code><a href="/docs/linux/man/2-fchmodat/">fchmodat</a></code>(2), <code><a href="/docs/linux/man/2-fchownat/">fchownat</a></code>(2), <code><a href="/docs/linux/man/2-fspick/">fspick</a></code>(2), <code><a href="/docs/linux/man/2-fstatat/">fstatat</a></code>(2), <code><a href="/docs/linux/man/2-futimesat/">futimesat</a></code>(2), <code><a href="/docs/linux/man/2-linkat/">linkat</a></code>(2), <code><a href="/docs/linux/man/2-mkdirat/">mkdirat</a></code>(2), <code><a href="/docs/linux/man/2-move_mount/">move_mount</a></code>(2), <code><a href="/docs/linux/man/2-mknodat/">mknodat</a></code>(2), <code><a href="/docs/linux/man/2-name_to_handle_at/">name_to_handle_at</a></code>(2), <code><a href="/docs/linux/man/2-open_tree/">open_tree</a></code>(2), <code><a href="/docs/linux/man/2-openat2/">openat2</a></code>(2), <code><a href="/docs/linux/man/2-readlinkat/">readlinkat</a></code>(2), <code><a href="/docs/linux/man/2-renameat/">renameat</a></code>(2), <code><a href="/docs/linux/man/2-statx/">statx</a></code>(2), <code><a href="/docs/linux/man/2-symlinkat/">symlinkat</a></code>(2), <code><a href="/docs/linux/man/2-unlinkat/">unlinkat</a></code>(2), <code><a href="/docs/linux/man/2-utimensat/">utimensat</a></code>(2), <code><a href="/docs/linux/man/3-mkfifoat/">mkfifoat</a></code>(3), and <code><a href="/docs/linux/man/3-scandirat/">scandirat</a></code>(3)) address two problems with the older interfaces that preceded them. Here, the explanation is in terms of the <code>openat</code>() call, but the rationale is analogous for the other interfaces. </p>
<p> First, <code>openat</code>() allows an application to avoid race conditions that could occur when using <code>open</code>() to open files in directories other than the current working directory. These race conditions result from the fact that some component of the directory prefix given to <code>open</code>() could be changed in parallel with the call to <code>open</code>(). Suppose, for example, that we wish to create the file <i>dir1/dir2/xxx.dep</i> if the file <i>dir1/dir2/xxx</i> exists. The problem is that between the existence check and the file-creation step, <i>dir1</i> or <i>dir2</i> (which might be symbolic links) could be modified to point to a different location. Such races can be avoided by opening a file descriptor for the target directory, and then specifying that file descriptor as the <i>dirfd</i> argument of (say) <code><a href="/docs/linux/man/2-fstatat/">fstatat</a></code>(2) and <code>openat</code>(). The use of the <i>dirfd</i> file descriptor also has other benefits:</p>
<dl>
<dt>*</p>
<dd> the file descriptor is a stable reference to the directory, even if the directory is renamed; and</p>
<dt>*</p>
<dd> the open file descriptor prevents the underlying filesystem from being dismounted, just as when a process has a current working directory on a filesystem.</dl>
<p> Second, <code>openat</code>() allows the implementation of a per-thread &quot;current working directory&quot;, via file descriptor(s) maintained by the application. (This functionality can also be obtained by tricks based on the use of <i>/proc/self/fd/</i>dirfd, but less efficiently.) </p>
<p> The <i>dirfd</i> argument for these APIs can be obtained by using <code>open</code>() or <code>openat</code>() to open a directory (with either the <code>O_RDONLY</code> or the <code>O_PATH</code> flag). Alternatively, such a file descriptor can be obtained by applying <code><a href="/docs/linux/man/3-dirfd/">dirfd</a></code>(3) to a directory stream created using <code><a href="/docs/linux/man/3-opendir/">opendir</a></code>(3). </p>
<p> When these APIs are given a <i>dirfd</i> argument of <code>AT_FDCWD</code> or the specified pathname is absolute, then they handle their pathname argument in the same way as the corresponding conventional APIs. However, in this case, several of the APIs have a <i>flags</i> argument that provides access to functionality that is not available with the corresponding conventional APIs.</p>
<h3>O_DIRECT</h3>
<p> The <code>O_DIRECT</code> flag may impose alignment restrictions on the length and address of user-space buffers and the file offset of I/Os. In Linux alignment restrictions vary by filesystem and kernel version and might be absent entirely. However there is currently no filesystem-independent interface for an application to discover these restrictions for a given file or filesystem. Some filesystems provide their own interfaces for doing so, for example the <code>XFS_IOC_DIOINFO</code> operation in <code><a href="/docs/linux/man/3-xfsctl/">xfsctl</a></code>(3). </p>
<p> Under Linux 2.4, transfer sizes, and the alignment of the user buffer and the file offset must all be multiples of the logical block size of the filesystem. Since Linux 2.6.0, alignment to the logical block size of the underlying storage (typically 512 bytes) suffices. The logical block size can be determined using the <code><a href="/docs/linux/man/2-ioctl/">ioctl</a></code>(2) <code>BLKSSZGET</code> operation or from the shell using the command: </p>
<p> blockdev &#8211;getss </p>
<p> <code>O_DIRECT</code> I/Os should never be run concurrently with the <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2) system call, if the memory buffer is a private mapping (i.e., any mapping created with the <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2) <code>MAP_PRIVATE</code> flag; this includes memory allocated on the heap and statically allocated buffers). Any such I/Os, whether submitted via an asynchronous I/O interface or from another thread in the process, should be completed before <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2) is called. Failure to do so can result in data corruption and undefined behavior in parent and child processes. This restriction does not apply when the memory buffer for the <code>O_DIRECT</code> I/Os was created using <code><a href="/docs/linux/man/2-shmat/">shmat</a></code>(2) or <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2) with the <code>MAP_SHARED</code> flag. Nor does this restriction apply when the memory buffer has been advised as <code>MADV_DONTFORK</code> with <code><a href="/docs/linux/man/2-madvise/">madvise</a></code>(2), ensuring that it will not be available to the child after <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2). </p>
<p> The <code>O_DIRECT</code> flag was introduced in SGI IRIX, where it has alignment restrictions similar to those of Linux 2.4. IRIX has also a <code><a href="/docs/linux/man/2-fcntl/">fcntl</a></code>(2) call to query appropriate alignments, and sizes. FreeBSD 4.x introduced a flag of the same name, but without alignment restrictions. </p>
<p> <code>O_DIRECT</code> support was added under Linux in kernel version 2.4.10. Older Linux kernels simply ignore this flag. Some filesystems may not implement the flag, in which case <code>open</code>() fails with the error <code>EINVAL</code> if it is used. </p>
<p> Applications should avoid mixing <code>O_DIRECT</code> and normal I/O to the same file, and especially to overlapping byte regions in the same file. Even when the filesystem correctly handles the coherency issues in this situation, overall I/O throughput is likely to be slower than using either mode alone. Likewise, applications should avoid mixing <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2) of files with direct I/O to the same files. </p>
<p> The behavior of <code>O_DIRECT</code> with NFS will differ from local filesystems. Older kernels, or kernels configured in certain ways, may not support this combination. The NFS protocol does not support passing the flag to the server, so <code>O_DIRECT</code> I/O will bypass the page cache only on the client; the server may still cache the I/O. The client asks the server to make the I/O synchronous to preserve the synchronous semantics of <code>O_DIRECT</code>. Some servers will perform poorly under these circumstances, especially if the I/O size is small. Some servers may also be configured to lie to clients about the I/O having reached stable storage; this will avoid the performance penalty at some risk to data integrity in the event of server power failure. The Linux NFS client places no alignment restrictions on <code>O_DIRECT</code> I/O. </p>
<p> In summary, <code>O_DIRECT</code> is a potentially powerful tool that should be used with caution. It is recommended that applications treat use of <code>O_DIRECT</code> as a performance option which is disabled by default.</p>
<h2>BUGS</h2>
<p> Currently, it is not possible to enable signal-driven I/O by specifying <code>O_ASYNC</code> when calling <code>open</code>(); use <code><a href="/docs/linux/man/2-fcntl/">fcntl</a></code>(2) to enable this flag. </p>
<p> One must check for two different error codes, <code>EISDIR</code> and <code>ENOENT</code>, when trying to determine whether the kernel supports <code>O_TMPFILE</code> functionality. </p>
<p> When both <code>O_CREAT</code> and <code>O_DIRECTORY</code> are specified in <i>flags</i> and the file specified by <i>pathname</i> does not exist, <code>open</code>() will create a regular file (i.e., <code>O_DIRECTORY</code> is ignored).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-chmod/">chmod</a></code>(2), <code><a href="/docs/linux/man/2-chown/">chown</a></code>(2), <code><a href="/docs/linux/man/2-close/">close</a></code>(2), <code><a href="/docs/linux/man/2-dup/">dup</a></code>(2), <code><a href="/docs/linux/man/2-fcntl/">fcntl</a></code>(2), <code><a href="/docs/linux/man/2-link/">link</a></code>(2), <code><a href="/docs/linux/man/2-lseek/">lseek</a></code>(2), <code><a href="/docs/linux/man/2-mknod/">mknod</a></code>(2), <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2), <code><a href="/docs/linux/man/2-mount/">mount</a></code>(2), <code><a href="/docs/linux/man/2-open_by_handle_at/">open_by_handle_at</a></code>(2), <code><a href="/docs/linux/man/2-openat2/">openat2</a></code>(2), <code><a href="/docs/linux/man/2-read/">read</a></code>(2), <code><a href="/docs/linux/man/2-socket/">socket</a></code>(2), <code><a href="/docs/linux/man/2-stat/">stat</a></code>(2), <code><a href="/docs/linux/man/2-umask/">umask</a></code>(2), <code><a href="/docs/linux/man/2-unlink/">unlink</a></code>(2), <code><a href="/docs/linux/man/2-write/">write</a></code>(2), <code><a href="/docs/linux/man/3-fopen/">fopen</a></code>(3), <code><a href="/docs/linux/man/5-acl/">acl</a></code>(5), <code><a href="/docs/linux/man/7-fifo/">fifo</a></code>(7), <code><a href="/docs/linux/man/7-inode/">inode</a></code>(7), <code><a href="/docs/linux/man/7-path_resolution/">path_resolution</a></code>(7), <code><a href="/docs/linux/man/7-symlink/">symlink</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
<dt><a href="#lbAH">RETURN VALUE</a></p>
<dd>
<dt><a href="#lbAI">ERRORS</a></p>
<dd>
<dt><a href="#lbAJ">VERSIONS</a></p>
<dd>
<dt><a href="#lbAK">CONFORMING TO</a></p>
<dd>
<dt><a href="#lbAL">NOTES</a></p>
<dd>
<dt><a href="#lbAU">BUGS</a></p>
<dd>
<dt><a href="#lbAV">SEE ALSO</a></p>
<dd>
<dt><a href="#lbAW">COLOPHON</a></p>
<dd></dl>
