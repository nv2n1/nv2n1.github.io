---
title: "umask(2)"
name: "umask"
section: "2"
letter: "u"
url: "/docs/linux/man/2-umask/"
description: "umask – set file mode creation mask"
---

<h2 class="name">NAME</h2>
<p> umask &#8211; set file mode creation mask </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;sys/types.h&gt;</code><br />
 <code>#include &lt;sys/stat.h&gt;</code> </p>
<p> <code>mode_t umask(mode_t </code><i>mask</i><code>);</code></p>
<h2>DESCRIPTION</h2>
<p> <code>umask</code>() sets the calling process&#8217;s file mode creation mask (umask) to <i>mask</i> &amp; 0777 (i.e., only the file permission bits of <i>mask</i> are used), and returns the previous value of the mask. </p>
<p> The umask is used by <code><a href="/docs/linux/man/2-open/">open</a></code>(2), <code><a href="/docs/linux/man/2-mkdir/">mkdir</a></code>(2), and other system calls that create files to modify the permissions placed on newly created files or directories. Specifically, permissions in the umask are turned off from the <i>mode</i> argument to <code><a href="/docs/linux/man/2-open/">open</a></code>(2) and <code><a href="/docs/linux/man/2-mkdir/">mkdir</a></code>(2). </p>
<p> Alternatively, if the parent directory has a default ACL (see <code><a href="/docs/linux/man/5-acl/">acl</a></code>(5)), the umask is ignored, the default ACL is inherited, the permission bits are set based on the inherited ACL, and permission bits absent in the <i>mode</i> argument are turned off. For example, the following default ACL is equivalent to a umask of 022: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;u::rwx,g::r-x,o::r-x </p>
<p> Combining the effect of this default ACL with a <i>mode</i> argument of 0666 (rw-rw-rw-), the resulting file permissions would be 0644 (rw-r&#8211;r&#8211;). </p>
<p> The constants that should be used to specify <i>mask</i> are described in <code><a href="/docs/linux/man/7-inode/">inode</a></code>(7). </p>
<p> The typical default value for the process umask is <i>S_IWGRP | S_IWOTH</i> (octal 022). In the usual case where the <i>mode</i> argument to <code><a href="/docs/linux/man/2-open/">open</a></code>(2) is specified as: </p>
<p> S_IRUSR | S_IWUSR | S_IRGRP | S_IWGRP | S_IROTH | S_IWOTH </p>
<p> (octal 0666) when creating a new file, the permissions on the resulting file will be: </p>
<p> S_IRUSR | S_IWUSR | S_IRGRP | S_IROTH </p>
<p> (because 0666 &amp; ~022 = 0644; i.e., rw-r&#8211;r&#8211;).</p>
<h2>RETURN VALUE</h2>
<p> This system call always succeeds and the previous value of the mask is returned.</p>
<h2>CONFORMING TO</h2>
<p> POSIX.1-2001, POSIX.1-2008, SVr4, 4.3BSD.</p>
<h2>NOTES</h2>
<p> A child process created via <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2) inherits its parent&#8217;s umask. The umask is left unchanged by <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2). </p>
<p> It is impossible to use <code>umask</code>() to fetch a process&#8217;s umask without at the same time changing it. A second call to <code>umask</code>() would then be needed to restore the umask. The nonatomicity of these two steps provides the potential for races in multithreaded programs. </p>
<p> Since Linux 4.7, the umask of any process can be viewed via the <i>Umask</i> field of <i>/proc/[pid]/status</i>. Inspecting this field in <i>/proc/self/status</i> allows a process to retrieve its umask without at the same time changing it. </p>
<p> The umask setting also affects the permissions assigned to POSIX IPC objects (<code><a href="/docs/linux/man/3-mq_open/">mq_open</a></code>(3), <code><a href="/docs/linux/man/3-sem_open/">sem_open</a></code>(3), <code><a href="/docs/linux/man/3-shm_open/">shm_open</a></code>(3)), FIFOs (<code><a href="/docs/linux/man/3-mkfifo/">mkfifo</a></code>(3)), and UNIX domain sockets (<code><a href="/docs/linux/man/7-unix/">unix</a></code>(7)) created by the process. The umask does not affect the permissions assigned to System V IPC objects created by the process (using <code><a href="/docs/linux/man/2-msgget/">msgget</a></code>(2), <code><a href="/docs/linux/man/2-semget/">semget</a></code>(2), <code><a href="/docs/linux/man/2-shmget/">shmget</a></code>(2)).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-chmod/">chmod</a></code>(2), <code><a href="/docs/linux/man/2-mkdir/">mkdir</a></code>(2), <code><a href="/docs/linux/man/2-open/">open</a></code>(2), <code><a href="/docs/linux/man/2-stat/">stat</a></code>(2), <code><a href="/docs/linux/man/5-acl/">acl</a></code>(5)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
