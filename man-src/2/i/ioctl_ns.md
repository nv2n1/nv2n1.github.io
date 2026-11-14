---
title: "ioctl_ns(2)"
name: "ioctl_ns"
section: "2"
letter: "i"
url: "/docs/linux/man/2-ioctl_ns/"
description: "ioctl_ns – ioctl() operations for Linux namespaces"
---

<h2 class="name">NAME</h2>
<p> ioctl_ns &#8211; ioctl() operations for Linux namespaces </p>
<h2>DESCRIPTION</h2>
<h3>Discovering namespace relationships</h3>
<p> The following <code><a href="/docs/linux/man/2-ioctl/">ioctl</a></code>(2) operations are provided to allow discovery of namespace relationships (see <code><a href="/docs/linux/man/7-user_namespaces/">user_namespaces</a></code>(7) and <code><a href="/docs/linux/man/7-pid_namespaces/">pid_namespaces</a></code>(7)). The form of the calls is: </p>
<p> new_fd = ioctl(fd, request); </p>
<p> In each case, <i>fd</i> refers to a <i>/proc/[pid]/ns/*</i> file. Both operations return a new file descriptor on success.</p>
<dl>
<dt><code>NS_GET_USERNS</code> (since Linux 4.9)</p>
<dd> Returns a file descriptor that refers to the owning user namespace for the namespace referred to by <i>fd</i>.</p>
<dt><code>NS_GET_PARENT</code> (since Linux 4.9)</p>
<dd> Returns a file descriptor that refers to the parent namespace of the namespace referred to by <i>fd</i>. This operation is valid only for hierarchical namespaces (i.e., PID and user namespaces). For user namespaces, <code>NS_GET_PARENT</code> is synonymous with <code>NS_GET_USERNS</code>.</dl>
<p> The new file descriptor returned by these operations is opened with the <code>O_RDONLY</code> and <code>O_CLOEXEC</code> (close-on-exec; see <code><a href="/docs/linux/man/2-fcntl/">fcntl</a></code>(2)) flags. </p>
<p> By applying <code><a href="/docs/linux/man/2-fstat/">fstat</a></code>(2) to the returned file descriptor, one obtains a <i>stat</i> structure whose <i>st_dev</i> (resident device) and <i>st_ino</i> (inode number) fields together identify the owning/parent namespace. This inode number can be matched with the inode number of another <i>/proc/[pid]/ns/{pid,user}</i> file to determine whether that is the owning/parent namespace. </p>
<p> Either of these <code><a href="/docs/linux/man/2-ioctl/">ioctl</a></code>(2) operations can fail with the following errors:</p>
<dl>
<dt><code>EPERM</code></p>
<dd> The requested namespace is outside of the caller&#8217;s namespace scope. This error can occur if, for example, the owning user namespace is an ancestor of the caller&#8217;s current user namespace. It can also occur on attempts to obtain the parent of the initial user or PID namespace.</p>
<dt><code>ENOTTY</code></p>
<dd> The operation is not supported by this kernel version.</dl>
<p> Additionally, the <code>NS_GET_PARENT</code> operation can fail with the following error:</p>
<dl>
<dt><code>EINVAL</code></p>
<dd> <i>fd</i> refers to a nonhierarchical namespace.</dl>
<p> See the EXAMPLES section for an example of the use of these operations.</p>
<h3>Discovering the namespace type</h3>
<p> The <code>NS_GET_NSTYPE</code> operation (available since Linux 4.11) can be used to discover the type of namespace referred to by the file descriptor <i>fd</i>: </p>
<p> nstype = ioctl(fd, NS_GET_NSTYPE); </p>
<p> <i>fd</i> refers to a <i>/proc/[pid]/ns/*</i> file. </p>
<p> The return value is one of the <code>CLONE_NEW*</code> values that can be specified to <code><a href="/docs/linux/man/2-clone/">clone</a></code>(2) or <code><a href="/docs/linux/man/2-unshare/">unshare</a></code>(2) in order to create a namespace.</p>
<h3>Discovering the owner of a user namespace</h3>
<p> The <code>NS_GET_OWNER_UID</code> operation (available since Linux 4.11) can be used to discover the owner user ID of a user namespace (i.e., the effective user ID of the process that created the user namespace). The form of the call is: </p>
<p> uid_t uid; ioctl(fd, NS_GET_OWNER_UID, &amp;uid); </p>
<p> <i>fd</i> refers to a <i>/proc/[pid]/ns/user</i> file. </p>
<p> The owner user ID is returned in the <i>uid_t</i> pointed to by the third argument. </p>
<p> This operation can fail with the following error:</p>
<dl>
<dt><code>EINVAL</code></p>
<dd> <i>fd</i> does not refer to a user namespace.</dl>
<h2>ERRORS</h2>
<p> Any of the above <code>ioctl</code>() operations can return the following errors:</p>
<dl>
<dt><code>ENOTTY</code></p>
<dd> <i>fd</i> does not refer to a <i>/proc/[pid]/ns/*</i> file.</dl>
<h2>CONFORMING TO</h2>
<p> Namespaces and the operations described on this page are a Linux-specific.</p>
<h2>EXAMPLES</h2>
<p> The example shown below uses the <code><a href="/docs/linux/man/2-ioctl/">ioctl</a></code>(2) operations described above to perform simple discovery of namespace relationships. The following shell sessions show various examples of the use of this program. </p>
<p> Trying to get the parent of the initial user namespace fails, since it has no parent: </p>
<p> $ <code>./ns_show /proc/self/ns/user p</code> The parent namespace is outside your namespace scope </p>
<p> Create a process running <code><a href="/docs/linux/man/1-sleep/">sleep</a></code>(1) that resides in new user and UTS namespaces, and show that the new UTS namespace is associated with the new user namespace: </p>
<p> $ <code>unshare -Uu sleep 1000 &amp;</code> [1] 23235 $ <code>./ns_show /proc/23235/ns/uts u</code> Device/Inode of owning user namespace is: [0,3] / 4026532448 $ <code>readlink /proc/23235/ns/user</code> user:[4026532448] </p>
<p> Then show that the parent of the new user namespace in the preceding example is the initial user namespace: </p>
<p> $ <code>readlink /proc/self/ns/user</code> user:[4026531837] $ <code>./ns_show /proc/23235/ns/user p</code> Device/Inode of parent namespace is: [0,3] / 4026531837 </p>
<p> Start a shell in a new user namespace, and show that from within this shell, the parent user namespace can&#8217;t be discovered. Similarly, the UTS namespace (which is associated with the initial user namespace) can&#8217;t be discovered. </p>
<p> $ <code>PS1=&quot;sh2$ &quot; unshare -U bash</code> sh2$ <code>./ns_show /proc/self/ns/user p</code> The parent namespace is outside your namespace scope sh2$ <code>./ns_show /proc/self/ns/uts u</code> The owning user namespace is outside your namespace scope</p>
<h3>Program source</h3>
<p> /* ns_show.c </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Licensed under the GNU General Public License v2 or later. */ #include &lt;stdint.h&gt; #include &lt;stdlib.h&gt; #include &lt;unistd.h&gt; #include &lt;stdio.h&gt; #include &lt;fcntl.h&gt; #include &lt;string.h&gt; #include &lt;sys/stat.h&gt; #include &lt;sys/ioctl.h&gt; #include &lt;errno.h&gt; #include &lt;sys/sysmacros.h&gt; </p>
<p> #ifndef NS_GET_USERNS #define NSIO 0xb7 #define NS_GET_USERNS _IO(NSIO, 0x1) #define NS_GET_PARENT _IO(NSIO, 0x2) #endif </p>
<p> int main(int argc, char *argv[]) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int fd, userns_fd, parent_fd;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct stat sb; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(argc&nbsp;&lt;&nbsp;2)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fprintf(stderr,&nbsp;&quot;Usage:&nbsp;%s&nbsp;/proc/[pid]/ns/[file]&nbsp;[p|u]
&quot;,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;argv[0]);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fprintf(stderr,&nbsp;&quot;
Display the result of one or both&nbsp;&quot;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&quot;of NS_GET_USERNS&nbsp;(u)&nbsp;or NS_GET_PARENT&nbsp;(p)
&quot;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&quot;for the specified&nbsp;/proc/[pid]/ns/[file]. If neither&nbsp;&quot;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&quot;&#8217;p&#8217;&nbsp;nor&nbsp;&#8216;u&#8217;&nbsp;is specified,
&quot;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&quot;NS_GET_USERNS is the default.
&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Obtain a file descriptor for the&nbsp;&#8216;ns&#8217;&nbsp;file specified<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;in argv[1]&nbsp;*/ </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fd&nbsp;=&nbsp;open(argv[1], O_RDONLY);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(fd&nbsp;==&nbsp;-1)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;perror(&quot;open&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Obtain a file descriptor for the owning user namespace and<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;then obtain and display the inode number of that namespace&nbsp;*/ </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(argc&nbsp;&lt;&nbsp;3 || strchr(argv[2],&nbsp;&#8216;u&#8217;))&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;userns_fd&nbsp;=&nbsp;ioctl(fd, NS_GET_USERNS); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(userns_fd&nbsp;==&nbsp;-1)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(errno&nbsp;==&nbsp;EPERM)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;The owning user namespace is outside&nbsp;&quot;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&quot;your namespace scope
&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;else<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;perror(&quot;ioctl-NS_GET_USERNS&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(fstat(userns_fd,&nbsp;&amp;sb)&nbsp;==&nbsp;-1)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;perror(&quot;fstat-userns&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;}<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;Device/Inode of owning user namespace is:&nbsp;&quot;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&quot;[%jx,%jx]&nbsp;/&nbsp;%ju
&quot;,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(uintmax_t)&nbsp;major(sb.st_dev),<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(uintmax_t)&nbsp;minor(sb.st_dev),<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(uintmax_t)&nbsp;sb.st_ino); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;close(userns_fd);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Obtain a file descriptor for the parent namespace and<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;then obtain and display the inode number of that namespace&nbsp;*/ </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(argc&nbsp;&gt;&nbsp;2&nbsp;&amp;&amp;&nbsp;strchr(argv[2],&nbsp;&#8216;p&#8217;))&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;parent_fd&nbsp;=&nbsp;ioctl(fd, NS_GET_PARENT); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(parent_fd&nbsp;==&nbsp;-1)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(errno&nbsp;==&nbsp;EINVAL)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;Can&#8217;&nbsp;get parent namespace of a&nbsp;&quot;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&quot;nonhierarchical namespace
&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;else if&nbsp;(errno&nbsp;==&nbsp;EPERM)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;The parent namespace is outside&nbsp;&quot;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&quot;your namespace scope
&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;else<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;perror(&quot;ioctl-NS_GET_PARENT&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(fstat(parent_fd,&nbsp;&amp;sb)&nbsp;==&nbsp;-1)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;perror(&quot;fstat-parentns&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;}<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;Device/Inode of parent namespace is:&nbsp;[%jx,%jx]&nbsp;/&nbsp;%ju
&quot;,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(uintmax_t)&nbsp;major(sb.st_dev),<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(uintmax_t)&nbsp;minor(sb.st_dev),<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(uintmax_t)&nbsp;sb.st_ino); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;close(parent_fd);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_SUCCESS); }</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-fstat/">fstat</a></code>(2), <code><a href="/docs/linux/man/2-ioctl/">ioctl</a></code>(2), <code><a href="/docs/linux/man/5-proc/">proc</a></code>(5), <code><a href="/docs/linux/man/7-namespaces/">namespaces</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
