---
title: "pivot_root(2)"
name: "pivot_root"
section: "2"
letter: "p"
url: "/docs/linux/man/2-pivot_root/"
description: "pivot_root – change the root mount"
---

<h2 class="name">NAME</h2>
<p> pivot_root &#8211; change the root mount </p>
<h2>SYNOPSIS</h2>
<p> <code>int pivot_root(const char *</code><i>new_root</i><code>, const char *</code><i>put_old</i><code>);</code> </p>
<p> <i>Note</i>: There is no glibc wrapper for this system call; see NOTES.</p>
<h2>DESCRIPTION</h2>
<p> <code>pivot_root</code>() changes the root mount in the mount namespace of the calling process. More precisely, it moves the root mount to the directory <i>put_old</i> and makes <i>new_root</i> the new root mount. The calling process must have the <code>CAP_SYS_ADMIN</code> capability in the user namespace that owns the caller&#8217;s mount namespace. </p>
<p> <code>pivot_root</code>() changes the root directory and the current working directory of each process or thread in the same mount namespace to <i>new_root</i> if they point to the old root directory. (See also NOTES.) On the other hand, <code>pivot_root</code>() does not change the caller&#8217;s current working directory (unless it is on the old root directory), and thus it should be followed by a <code>chdir(&quot;/&quot;)</code> call. </p>
<p> The following restrictions apply:</p>
<dl>
<dt>&#8211;</p>
<dd> <i>new_root</i> and <i>put_old</i> must be directories.</p>
<dt>&#8211;</p>
<dd> <i>new_root</i> and <i>put_old</i> must not be on the same mount as the current root.</p>
<dt>&#8211;</p>
<dd> <i>put_old</i> must be at or underneath <i>new_root</i>; that is, adding some nonnegative number of &quot;<i>/..</i>&quot; prefixes to the pathname pointed to by <i>put_old</i> must yield the same directory as <i>new_root</i>.</p>
<dt>&#8211;</p>
<dd> <i>new_root</i> must be a path to a mount point, but can&#8217;t be <i>&quot;/&quot;</i>. A path that is not already a mount point can be converted into one by bind mounting the path onto itself.</p>
<dt>&#8211;</p>
<dd> The propagation type of the parent mount of <i>new_root</i> and the parent mount of the current root directory must not be <code>MS_SHARED</code>; similarly, if <i>put_old</i> is an existing mount point, its propagation type must not be <code>MS_SHARED</code>. These restrictions ensure that <code>pivot_root</code>() never propagates any changes to another mount namespace.</p>
<dt>&#8211;</p>
<dd> The current root directory must be a mount point.</dl>
<h2>RETURN VALUE</h2>
<p> On success, zero is returned. On error, -1 is returned, and <i>errno</i> is set appropriately.</p>
<h2>ERRORS</h2>
<p> <code>pivot_root</code>() may fail with any of the same errors as <code><a href="/docs/linux/man/2-stat/">stat</a></code>(2). Additionally, it may fail with the following errors:</p>
<dl>
<dt><code>EBUSY</code></p>
<dd> <i>new_root</i> or <i>put_old</i> is on the current root mount. (This error covers the pathological case where <i>new_root</i> is <i>&quot;/&quot;</i>.)</p>
<dt><code>EINVAL</code></p>
<dd> <i>new_root</i> is not a mount point.</p>
<dt><code>EINVAL</code></p>
<dd> <i>put_old</i> is not at or underneath <i>new_root</i>.</p>
<dt><code>EINVAL</code></p>
<dd> The current root directory is not a mount point (because of an earlier <code><a href="/docs/linux/man/2-chroot/">chroot</a></code>(2)).</p>
<dt><code>EINVAL</code></p>
<dd> The current root is on the rootfs (initial ramfs) mount; see NOTES.</p>
<dt><code>EINVAL</code></p>
<dd> Either the mount point at <i>new_root</i>, or the parent mount of that mount point, has propagation type <code>MS_SHARED</code>.</p>
<dt><code>EINVAL</code></p>
<dd> <i>put_old</i> is a mount point and has the propagation type <code>MS_SHARED</code>.</p>
<dt><code>ENOTDIR</code></p>
<dd> <i>new_root</i> or <i>put_old</i> is not a directory.</p>
<dt><code>EPERM</code></p>
<dd> The calling process does not have the <code>CAP_SYS_ADMIN</code> capability.</dl>
<h2>VERSIONS</h2>
<p> <code>pivot_root</code>() was introduced in Linux 2.3.41.</p>
<h2>CONFORMING TO</h2>
<p> <code>pivot_root</code>() is Linux-specific and hence is not portable.</p>
<h2>NOTES</h2>
<p> Glibc does not provide a wrapper for this system call; call it using <code><a href="/docs/linux/man/2-syscall/">syscall</a></code>(2). </p>
<p> A command-line interface for this system call is provided by <code><a href="/docs/linux/man/8-pivot_root/">pivot_root</a></code>(8). </p>
<p> <code>pivot_root</code>() allows the caller to switch to a new root filesystem while at the same time placing the old root mount at a location under <i>new_root</i> from where it can subsequently be unmounted. (The fact that it moves all processes that have a root directory or current working directory on the old root directory to the new root frees the old root directory of users, allowing the old root mount to be unmounted more easily.) </p>
<p> One use of <code>pivot_root</code>() is during system startup, when the system mounts a temporary root filesystem (e.g., an <code><a href="/docs/linux/man/4-initrd/">initrd</a></code>(4)), then mounts the real root filesystem, and eventually turns the latter into the root directory of all relevant processes and threads. A modern use is to set up a root filesystem during the creation of a container. </p>
<p> The fact that <code>pivot_root</code>() modifies process root and current working directories in the manner noted in DESCRIPTION is necessary in order to prevent kernel threads from keeping the old root mount busy with their root and current working directories, even if they never access the filesystem in any way. </p>
<p> The rootfs (initial ramfs) cannot be <code>pivot_root</code>()ed. The recommended method of changing the root filesystem in this case is to delete everything in rootfs, overmount rootfs with the new root, attach <i>stdin</i>/<i>stdout</i>/<i>stderr</i> to the new <i>/dev/console</i>, and exec the new <code><a href="/docs/linux/man/1-init/">init</a></code>(1). Helper programs for this process exist; see <code><a href="/docs/linux/man/8-switch_root/">switch_root</a></code>(8).</p>
<h3>pivot_root(&quot;.&quot;, &quot;.&quot;)</h3>
<p> <i>new_root</i> and <i>put_old</i> may be the same directory. In particular, the following sequence allows a pivot-root operation without needing to create and remove a temporary directory: </p>
<p> chdir(new_root); pivot_root(&quot;.&quot;, &quot;.&quot;); umount2(&quot;.&quot;, MNT_DETACH); </p>
<p> This sequence succeeds because the <code>pivot_root</code>() call stacks the old root mount point on top of the new root mount point at <i>/</i>. At that point, the calling process&#8217;s root directory and current working directory refer to the new root mount point (<i>new_root</i>). During the subsequent <code>umount</code>() call, resolution of <i>&quot;.&quot;</i> starts with <i>new_root</i> and then moves up the list of mounts stacked at <i>/</i>, with the result that old root mount point is unmounted.</p>
<h3>Historical notes</h3>
<p> For many years, this manual page carried the following text:</p>
<dl>
<dt>
<dd>
<p> <code>pivot_root</code>() may or may not change the current root and the current working directory of any processes or threads which use the old root directory. The caller of <code>pivot_root</code>() must ensure that processes with root or current working directory at the old root operate correctly in either case. An easy way to ensure this is to change their root and current working directory to <i>new_root</i> before invoking <code>pivot_root</code>().</dl>
<p> This text, written before the system call implementation was even finalized in the kernel, was probably intended to warn users at that time that the implementation might change before final release. However, the behavior stated in DESCRIPTION has remained consistent since this system call was first implemented and will not change now.</p>
<h2>EXAMPLES</h2>
<p> The program below demonstrates the use of <code>pivot_root</code>() inside a mount namespace that is created using <code><a href="/docs/linux/man/2-clone/">clone</a></code>(2). After pivoting to the root directory named in the program&#8217;s first command-line argument, the child created by <code><a href="/docs/linux/man/2-clone/">clone</a></code>(2) then executes the program named in the remaining command-line arguments. </p>
<p> We demonstrate the program by creating a directory that will serve as the new root filesystem and placing a copy of the (statically linked) <code><a href="/docs/linux/man/1-busybox/">busybox</a></code>(1) executable in that directory. </p>
<p> $ <code>mkdir /tmp/rootfs</code> $ <code>ls -id /tmp/rootfs</code> # Show inode number of new root directory 319459 /tmp/rootfs $ <code>cp $(which busybox) /tmp/rootfs</code> $ <code>PS1=&#8217;bbsh$ &#8216; sudo ./pivot_root_demo /tmp/rootfs /busybox sh</code> bbsh$ <code>PATH=/</code> bbsh$ <code>busybox ln busybox ln</code> bbsh$ <code>ln busybox echo</code> bbsh$ <code>ln busybox ls</code> bbsh$ <code>ls</code> busybox echo ln ls bbsh$ <code>ls -id /</code> # Compare with inode number above 319459 / bbsh$ <code>echo &#8216;hello world&#8217;</code> hello world</p>
<h3>Program source</h3>
<p> /* pivot_root_demo.c */ </p>
<p> #define _GNU_SOURCE #include &lt;sched.h&gt; #include &lt;stdio.h&gt; #include &lt;stdlib.h&gt; #include &lt;unistd.h&gt; #include &lt;sys/wait.h&gt; #include &lt;sys/syscall.h&gt; #include &lt;sys/mount.h&gt; #include &lt;sys/stat.h&gt; #include &lt;limits.h&gt; #include &lt;sys/mman.h&gt; </p>
<p> #define errExit(msg) do { perror(msg); exit(EXIT_FAILURE); \<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;}&nbsp;while&nbsp;(0) </p>
<p> static int pivot_root(const char *new_root, const char *put_old) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return syscall(SYS_pivot_root, new_root, put_old); } </p>
<p> #define STACK_SIZE (1024 * 1024) </p>
<p> static int /* Startup function for cloned child */ child(void *arg) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;**args&nbsp;=&nbsp;arg;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;*new_root&nbsp;=&nbsp;args[0];<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;const char&nbsp;*put_old&nbsp;=&nbsp;&quot;/oldrootfs&quot;;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char path[PATH_MAX]; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Ensure that&nbsp;&#8216;new_root&#8217;&nbsp;and its parent mount don&#8217;t have<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;shared propagation&nbsp;(which would cause pivot_root()&nbsp;to<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return an error), and prevent propagation of mount<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;events to the initial mount namespace&nbsp;*/ </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(mount(NULL,&nbsp;&quot;/&quot;, NULL, MS_REC | MS_PRIVATE, NULL)&nbsp;==&nbsp;-1)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;errExit(&quot;mount-MS_PRIVATE&quot;); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Ensure that&nbsp;&#8216;new_root&#8217;&nbsp;is a mount point&nbsp;*/ </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(mount(new_root, new_root, NULL, MS_BIND, NULL)&nbsp;==&nbsp;-1)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;errExit(&quot;mount-MS_BIND&quot;); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Create directory to which old root will be pivoted&nbsp;*/ </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;snprintf(path, sizeof(path),&nbsp;&quot;%s/%s&quot;, new_root, put_old);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(mkdir(path, 0777)&nbsp;==&nbsp;-1)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;errExit(&quot;mkdir&quot;); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;And pivot the root filesystem&nbsp;*/ </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(pivot_root(new_root, path)&nbsp;==&nbsp;-1)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;errExit(&quot;pivot_root&quot;); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Switch the current working directory to&nbsp;&quot;/&quot;&nbsp;*/ </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(chdir(&quot;/&quot;)&nbsp;==&nbsp;-1)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;errExit(&quot;chdir&quot;); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Unmount old root and remove mount point&nbsp;*/ </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(umount2(put_old, MNT_DETACH)&nbsp;==&nbsp;-1)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;perror(&quot;umount2&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(rmdir(put_old)&nbsp;==&nbsp;-1)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;perror(&quot;rmdir&quot;); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Execute the command specified in argv[1]&#8230;&nbsp;*/ </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;execv(args[1],&nbsp;&amp;args[1]);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;errExit(&quot;execv&quot;); } </p>
<p> int main(int argc, char *argv[]) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Create a child process in a new mount namespace&nbsp;*/ </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;*stack&nbsp;=&nbsp;mmap(NULL, STACK_SIZE, PROT_READ | PROT_WRITE,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;MAP_PRIVATE | MAP_ANONYMOUS | MAP_STACK, -1, 0);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(stack&nbsp;==&nbsp;MAP_FAILED)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;errExit(&quot;mmap&quot;); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(clone(child, stack&nbsp;+&nbsp;STACK_SIZE,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;CLONE_NEWNS | SIGCHLD,&nbsp;&amp;argv[1])&nbsp;==&nbsp;-1)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;errExit(&quot;clone&quot;); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Parent falls through to here;&nbsp;wait for child&nbsp;*/ </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(wait(NULL)&nbsp;==&nbsp;-1)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;errExit(&quot;wait&quot;); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_SUCCESS); }</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-chdir/">chdir</a></code>(2), <code><a href="/docs/linux/man/2-chroot/">chroot</a></code>(2), <code><a href="/docs/linux/man/2-mount/">mount</a></code>(2), <code><a href="/docs/linux/man/2-stat/">stat</a></code>(2), <code><a href="/docs/linux/man/4-initrd/">initrd</a></code>(4), <code><a href="/docs/linux/man/7-mount_namespaces/">mount_namespaces</a></code>(7), <code><a href="/docs/linux/man/8-pivot_root/">pivot_root</a></code>(8), <code><a href="/docs/linux/man/8-switch_root/">switch_root</a></code>(8)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
