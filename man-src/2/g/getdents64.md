---
title: "getdents64(2)"
name: "getdents64"
section: "2"
letter: "g"
url: "/docs/linux/man/2-getdents64/"
description: "getdents, getdents64 – get directory entries"
---

<h2 class="name">NAME</h2>
<p> getdents, getdents64 &#8211; get directory entries </p>
<h2>SYNOPSIS</h2>
<pre><code>
long getdents(unsigned int fd, struct linux_dirent *dirp,
              unsigned int count);
#define _GNU_SOURCE /* See feature_test_macros(7) */
#include &lt;dirent.h&gt;
ssize_t getdents64(int fd, void *dirp, size_t count);
</code></pre>
<p> <i>Note</i>: There is no glibc wrapper for <code>getdents</code>(); see NOTES.</p>
<h2>DESCRIPTION</h2>
<p> These are not the interfaces you are interested in. Look at <code><a href="/docs/linux/man/3-readdir/">readdir</a></code>(3) for the POSIX-conforming C library interface. This page documents the bare kernel system call interfaces.</p>
<h3>getdents()</h3>
<p> The system call <code>getdents</code>() reads several <i>linux_dirent</i> structures from the directory referred to by the open file descriptor <i>fd</i> into the buffer pointed to by <i>dirp</i>. The argument <i>count</i> specifies the size of that buffer. </p>
<p> The <i>linux_dirent</i> structure is declared as follows: </p>
<p> struct linux_dirent {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned long&nbsp;<wbr>&nbsp;d_ino;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Inode number&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned long&nbsp;<wbr>&nbsp;d_off;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Offset to next&nbsp;<i>linux_dirent</i>&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned short d_reclen;&nbsp;<wbr>&nbsp;/*&nbsp;Length of this&nbsp;<i>linux_dirent</i>&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;d_name[];&nbsp;<wbr>&nbsp;/*&nbsp;Filename&nbsp;(null-terminated)&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;length is actually&nbsp;(d_reclen &#8211; 2 &#8211;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;offsetof(struct linux_dirent, d_name))&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;pad;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;//&nbsp;Zero padding byte<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;d_type;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;//&nbsp;File type&nbsp;(only since Linux<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;//&nbsp;2.6.4);&nbsp;offset is&nbsp;(d_reclen &#8211; 1)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;*/ } </p>
<p> <i>d_ino</i> is an inode number. <i>d_off</i> is the distance from the start of the directory to the start of the next <i>linux_dirent</i>. <i>d_reclen</i> is the size of this entire <i>linux_dirent</i>. <i>d_name</i> is a null-terminated filename. </p>
<p> <i>d_type</i> is a byte at the end of the structure that indicates the file type. It contains one of the following values (defined in <i>&lt;dirent.h&gt;</i>):</p>
<dl>
<dt><code>DT_BLK</code></p>
<dd> This is a block device.</p>
<dt><code>DT_CHR</code></p>
<dd> This is a character device.</p>
<dt><code>DT_DIR</code></p>
<dd> This is a directory.</p>
<dt><code>DT_FIFO</code></p>
<dd> This is a named pipe (FIFO).</p>
<dt><code>DT_LNK</code></p>
<dd> This is a symbolic link.</p>
<dt><code>DT_REG</code></p>
<dd> This is a regular file.</p>
<dt><code>DT_SOCK</code></p>
<dd> This is a UNIX domain socket.</p>
<dt><code>DT_UNKNOWN</code></p>
<dd> The file type is unknown.</dl>
<p> The <i>d_type</i> field is implemented since Linux 2.6.4. It occupies a space that was previously a zero-filled padding byte in the <i>linux_dirent</i> structure. Thus, on kernels up to and including 2.6.3, attempting to access this field always provides the value 0 (<code>DT_UNKNOWN</code>). </p>
<p> Currently, only some filesystems (among them: Btrfs, ext2, ext3, and ext4) have full support for returning the file type in <i>d_type</i>. All applications must properly handle a return of <code>DT_UNKNOWN</code>.</p>
<h3>getdents64()</h3>
<p> The original Linux <code>getdents</code>() system call did not handle large filesystems and large file offsets. Consequently, Linux 2.4 added <code>getdents64</code>(), with wider types for the <i>d_ino</i> and <i>d_off</i> fields. In addition, <code>getdents64</code>() supports an explicit <i>d_type</i> field. </p>
<p> The <code>getdents64</code>() system call is like <code>getdents</code>(), except that its second argument is a pointer to a buffer containing structures of the following type: </p>
<p> struct linux_dirent64 {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;ino64_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;d_ino;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;64-bit inode number&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;off64_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;d_off;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;64-bit offset to next structure&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned short d_reclen;&nbsp;/*&nbsp;Size of this dirent&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned char&nbsp;<wbr>&nbsp;d_type;&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;File type&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;d_name[];&nbsp;/*&nbsp;Filename&nbsp;(null-terminated)&nbsp;*/ };</p>
<h2>RETURN VALUE</h2>
<p> On success, the number of bytes read is returned. On end of directory, 0 is returned. On error, -1 is returned, and <i>errno</i> is set appropriately.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EBADF</code></p>
<dd> Invalid file descriptor <i>fd</i>.</p>
<dt><code>EFAULT</code></p>
<dd> Argument points outside the calling process&#8217;s address space.</p>
<dt><code>EINVAL</code></p>
<dd> Result buffer is too small.</p>
<dt><code>ENOENT</code></p>
<dd> No such directory.</p>
<dt><code>ENOTDIR</code></p>
<dd> File descriptor does not refer to a directory.</dl>
<h2>CONFORMING TO</h2>
<p> SVr4.</p>
<h2>NOTES</h2>
<p> Library support for <code>getdents64</code>() was added in glibc 2.30; there is no glibc wrapper for <code>getdents</code>(). Calling <code>getdents</code>() (or <code>getdents64</code>() on earlier glibc versions) requires the use of <code><a href="/docs/linux/man/2-syscall/">syscall</a></code>(2). In that case you will need to define the <i>linux_dirent</i> or <i>linux_dirent64</i> structure yourself. </p>
<p> Probably, you want to use <code><a href="/docs/linux/man/3-readdir/">readdir</a></code>(3) instead of these system calls. </p>
<p> These calls supersede <code><a href="/docs/linux/man/2-readdir/">readdir</a></code>(2).</p>
<h2>EXAMPLES</h2>
<p> The program below demonstrates the use of <code>getdents</code>(). The following output shows an example of what we see when running this program on an ext2 directory: </p>
<p> $<code> ./a.out /testfs/</code> &#8212;&#8212;&#8212;&#8212;&#8212; nread=120 &#8212;&#8212;&#8212;&#8212;&#8212; inode# file type d_reclen d_off d_name<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;2&nbsp;<wbr>&nbsp;directory&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;16&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;12&nbsp;<wbr>&nbsp;.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;2&nbsp;<wbr>&nbsp;directory&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;16&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;24&nbsp;<wbr>&nbsp;..<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;11&nbsp;<wbr>&nbsp;directory&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;24&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;44&nbsp;<wbr>&nbsp;lost+found<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;12&nbsp;<wbr>&nbsp;regular&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;16&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;56&nbsp;<wbr>&nbsp;a<br />
&nbsp;<wbr>&nbsp;228929&nbsp;<wbr>&nbsp;directory&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;16&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;68&nbsp;<wbr>&nbsp;sub<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;16353&nbsp;<wbr>&nbsp;directory&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;16&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;80&nbsp;<wbr>&nbsp;sub2<br />
&nbsp;<wbr>&nbsp;130817&nbsp;<wbr>&nbsp;directory&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;16&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;4096&nbsp;<wbr>&nbsp;sub3</p>
<h3>Program source</h3>
<p> #define _GNU_SOURCE #include &lt;dirent.h&gt; /* Defines DT_* constants */ #include &lt;fcntl.h&gt; #include &lt;stdint.h&gt; #include &lt;stdio.h&gt; #include &lt;unistd.h&gt; #include &lt;stdlib.h&gt; #include &lt;sys/stat.h&gt; #include &lt;sys/syscall.h&gt; </p>
<p> #define handle_error(msg) \<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;do&nbsp;{&nbsp;perror(msg);&nbsp;exit(EXIT_FAILURE);&nbsp;}&nbsp;while&nbsp;(0) </p>
<p> struct linux_dirent {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned long&nbsp;<wbr>&nbsp;d_ino;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;off_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;d_off;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned short d_reclen;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;d_name[]; }; </p>
<p> #define BUF_SIZE 1024 </p>
<p> int main(int argc, char *argv[]) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int fd;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;long nread;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char buf[BUF_SIZE];<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct linux_dirent&nbsp;*d;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char d_type; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fd&nbsp;=&nbsp;open(argc&nbsp;&gt;&nbsp;1&nbsp;?&nbsp;argv[1]&nbsp;:&nbsp;&quot;.&quot;, O_RDONLY | O_DIRECTORY);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(fd&nbsp;==&nbsp;-1)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;handle_error(&quot;open&quot;); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;for&nbsp;(;;)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;nread&nbsp;=&nbsp;syscall(SYS_getdents, fd, buf, BUF_SIZE);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(nread&nbsp;==&nbsp;-1)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;handle_error(&quot;getdents&quot;); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(nread&nbsp;==&nbsp;0)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;break; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;&#8212;&#8212;&#8212;&#8212;&#8212; nread=%d &#8212;&#8212;&#8212;&#8212;&#8212;
&quot;, nread);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;inode#&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;file type&nbsp;<wbr>&nbsp;d_reclen&nbsp;<wbr>&nbsp;d_off&nbsp;<wbr>&nbsp;<wbr>&nbsp;d_name
&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;for&nbsp;(long bpos&nbsp;=&nbsp;0;&nbsp;bpos&nbsp;&lt;&nbsp;nread;)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;d&nbsp;=&nbsp;(struct linux_dirent&nbsp;*)&nbsp;(buf&nbsp;+&nbsp;bpos);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;%8ld&nbsp;<wbr>&nbsp;&quot;, d-&gt;d_ino);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;d_type&nbsp;=&nbsp;*(buf&nbsp;+&nbsp;bpos&nbsp;+&nbsp;d-&gt;d_reclen &#8211; 1);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;%-10s&nbsp;&quot;,&nbsp;(d_type&nbsp;==&nbsp;DT_REG)&nbsp;?&nbsp;<wbr>&nbsp;&quot;regular&quot;&nbsp;:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(d_type&nbsp;==&nbsp;DT_DIR)&nbsp;?&nbsp;<wbr>&nbsp;&quot;directory&quot;&nbsp;:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(d_type&nbsp;==&nbsp;DT_FIFO)&nbsp;?&nbsp;&quot;FIFO&quot;&nbsp;:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(d_type&nbsp;==&nbsp;DT_SOCK)&nbsp;?&nbsp;&quot;socket&quot;&nbsp;:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(d_type&nbsp;==&nbsp;DT_LNK)&nbsp;?&nbsp;<wbr>&nbsp;&quot;symlink&quot;&nbsp;:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(d_type&nbsp;==&nbsp;DT_BLK)&nbsp;?&nbsp;<wbr>&nbsp;&quot;block dev&quot;&nbsp;:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(d_type&nbsp;==&nbsp;DT_CHR)&nbsp;?&nbsp;<wbr>&nbsp;&quot;char dev&quot;&nbsp;:&nbsp;&quot;???&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;%4d&nbsp;%10jd&nbsp;<wbr>&nbsp;%s
&quot;, d-&gt;d_reclen,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(intmax_t)&nbsp;d-&gt;d_off, d-&gt;d_name);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;bpos&nbsp;+=&nbsp;d-&gt;d_reclen;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;}<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_SUCCESS); }</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-readdir/">readdir</a></code>(2), <code><a href="/docs/linux/man/3-readdir/">readdir</a></code>(3), <code><a href="/docs/linux/man/7-inode/">inode</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
