---
title: "memfd_create(2)"
name: "memfd_create"
section: "2"
letter: "m"
url: "/docs/linux/man/2-memfd_create/"
description: "memfd_create – create an anonymous file"
---

<h2 class="name">NAME</h2>
<p> memfd_create &#8211; create an anonymous file </p>
<h2>SYNOPSIS</h2>
<pre><code>
#define _GNU_SOURCE /* See feature_test_macros(7) */
#include &lt;sys/mman.h&gt;
int memfd_create(const char *name, unsigned int flags);
</code></pre>
<h2>DESCRIPTION</h2>
<p> <code>memfd_create</code>() creates an anonymous file and returns a file descriptor that refers to it. The file behaves like a regular file, and so can be modified, truncated, memory-mapped, and so on. However, unlike a regular file, it lives in RAM and has a volatile backing storage. Once all references to the file are dropped, it is automatically released. Anonymous memory is used for all backing pages of the file. Therefore, files created by <code>memfd_create</code>() have the same semantics as other anonymous memory allocations such as those allocated using <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2) with the <code>MAP_ANONYMOUS</code> flag. </p>
<p> The initial size of the file is set to 0. Following the call, the file size should be set using <code><a href="/docs/linux/man/2-ftruncate/">ftruncate</a></code>(2). (Alternatively, the file may be populated by calls to <code><a href="/docs/linux/man/2-write/">write</a></code>(2) or similar.) </p>
<p> The name supplied in <i>name</i> is used as a filename and will be displayed as the target of the corresponding symbolic link in the directory <i>/proc/self/fd/</i>. The displayed name is always prefixed with <i>memfd:</i> and serves only for debugging purposes. Names do not affect the behavior of the file descriptor, and as such multiple files can have the same name without any side effects. </p>
<p> The following values may be bitwise ORed in <i>flags</i> to change the behavior of <code>memfd_create</code>():</p>
<dl>
<dt><code>MFD_CLOEXEC</code></p>
<dd> Set the close-on-exec (<code>FD_CLOEXEC</code>) flag on the new file descriptor. See the description of the <code>O_CLOEXEC</code> flag in <code><a href="/docs/linux/man/2-open/">open</a></code>(2) for reasons why this may be useful.</p>
<dt><code>MFD_ALLOW_SEALING</code></p>
<dd> Allow sealing operations on this file. See the discussion of the <code>F_ADD_SEALS</code> and <code>F_GET_SEALS</code> operations in <code><a href="/docs/linux/man/2-fcntl/">fcntl</a></code>(2), and also NOTES, below. The initial set of seals is empty. If this flag is not set, the initial set of seals will be <code>F_SEAL_SEAL</code>, meaning that no other seals can be set on the file.</p>
<dt><code>MFD_HUGETLB</code> (since Linux 4.14)</p>
<dd> The anonymous file will be created in the hugetlbfs filesystem using huge pages. See the Linux kernel source file <i>Documentation/admin-guide/mm/hugetlbpage.rst</i> for more information about hugetlbfs. Specifying both <code>MFD_HUGETLB</code> and <code>MFD_ALLOW_SEALING</code> in <i>flags</i> is supported since Linux 4.16.</p>
<dt><code>MFD_HUGE_2MB</code>, <code>MFD_HUGE_1GB</code>, <code>&#8230;</code></p>
<dd> Used in conjunction with <code>MFD_HUGETLB</code> to select alternative hugetlb page sizes (respectively, 2 MB, 1 GB, &#8230;) on systems that support multiple hugetlb page sizes. Definitions for known huge page sizes are included in the header file <i>&lt;linux/memfd.h&gt;.</i></p>
<dt>
<dd> For details on encoding huge page sizes not included in the header file, see the discussion of the similarly named constants in <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2).</dl>
<p> Unused bits in <i>flags</i> must be 0. </p>
<p> As its return value, <code>memfd_create</code>() returns a new file descriptor that can be used to refer to the file. This file descriptor is opened for both reading and writing (<code>O_RDWR</code>) and <code>O_LARGEFILE</code> is set for the file descriptor. </p>
<p> With respect to <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2) and <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2), the usual semantics apply for the file descriptor created by <code>memfd_create</code>(). A copy of the file descriptor is inherited by the child produced by <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2) and refers to the same file. The file descriptor is preserved across <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2), unless the close-on-exec flag has been set.</p>
<h2>RETURN VALUE</h2>
<p> On success, <code>memfd_create</code>() returns a new file descriptor. On error, -1 is returned and <i>errno</i> is set to indicate the error.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EFAULT</code></p>
<dd> The address in <i>name</i> points to invalid memory.</p>
<dt><code>EINVAL</code></p>
<dd> <i>flags</i> included unknown bits.</p>
<dt><code>EINVAL</code></p>
<dd> <i>name</i> was too long. (The limit is 249 bytes, excluding the terminating null byte.)</p>
<dt><code>EINVAL</code></p>
<dd> Both <code>MFD_HUGETLB</code> and <code>MFD_ALLOW_SEALING</code> were specified in <i>flags</i>.</p>
<dt><code>EMFILE</code></p>
<dd> The per-process limit on the number of open file descriptors has been reached.</p>
<dt><code>ENFILE</code></p>
<dd> The system-wide limit on the total number of open files has been reached.</p>
<dt><code>ENOMEM</code></p>
<dd> There was insufficient memory to create a new anonymous file.</dl>
<h2>VERSIONS</h2>
<p> The <code>memfd_create</code>() system call first appeared in Linux 3.17; glibc support was added in version 2.27.</p>
<h2>CONFORMING TO</h2>
<p> The <code>memfd_create</code>() system call is Linux-specific.</p>
<h2>NOTES</h2>
<p> The <code>memfd_create</code>() system call provides a simple alternative to manually mounting a <code><a href="/docs/linux/man/5-tmpfs/">tmpfs</a></code>(5) filesystem and creating and opening a file in that filesystem. The primary purpose of <code>memfd_create</code>() is to create files and associated file descriptors that are used with the file-sealing APIs provided by <code><a href="/docs/linux/man/2-fcntl/">fcntl</a></code>(2). </p>
<p> The <code>memfd_create</code>() system call also has uses without file sealing (which is why file-sealing is disabled, unless explicitly requested with the <code>MFD_ALLOW_SEALING</code> flag). In particular, it can be used as an alternative to creating files in <i>tmp</i> or as an alternative to using the <code><a href="/docs/linux/man/2-open/">open</a></code>(2) <code>O_TMPFILE</code> in cases where there is no intention to actually link the resulting file into the filesystem.</p>
<h3>File sealing</h3>
<p> In the absence of file sealing, processes that communicate via shared memory must either trust each other, or take measures to deal with the possibility that an untrusted peer may manipulate the shared memory region in problematic ways. For example, an untrusted peer might modify the contents of the shared memory at any time, or shrink the shared memory region. The former possibility leaves the local process vulnerable to time-of-check-to-time-of-use race conditions (typically dealt with by copying data from the shared memory region before checking and using it). The latter possibility leaves the local process vulnerable to <code>SIGBUS</code> signals when an attempt is made to access a now-nonexistent location in the shared memory region. (Dealing with this possibility necessitates the use of a handler for the <code>SIGBUS</code> signal.) </p>
<p> Dealing with untrusted peers imposes extra complexity on code that employs shared memory. Memory sealing enables that extra complexity to be eliminated, by allowing a process to operate secure in the knowledge that its peer can&#8217;t modify the shared memory in an undesired fashion. </p>
<p> An example of the usage of the sealing mechanism is as follows:</p>
<dl>
<dt>1.</p>
<dd> The first process creates a <code><a href="/docs/linux/man/5-tmpfs/">tmpfs</a></code>(5) file using <code>memfd_create</code>(). The call yields a file descriptor used in subsequent steps.</p>
<dt>2.</p>
<dd> The first process sizes the file created in the previous step using <code><a href="/docs/linux/man/2-ftruncate/">ftruncate</a></code>(2), maps it using <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2), and populates the shared memory with the desired data.</p>
<dt>3.</p>
<dd> The first process uses the <code><a href="/docs/linux/man/2-fcntl/">fcntl</a></code>(2) <code>F_ADD_SEALS</code> operation to place one or more seals on the file, in order to restrict further modifications on the file. (If placing the seal <code>F_SEAL_WRITE</code>, then it will be necessary to first unmap the shared writable mapping created in the previous step. Otherwise, behavior similar to <code>F_SEAL_WRITE</code> can be achieved by using <code>F_SEAL_FUTURE_WRITE</code>, which will prevent future writes via <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2) and <code><a href="/docs/linux/man/2-write/">write</a></code>(2) from succeeding while keeping existing shared writable mappings).</p>
<dt>4.</p>
<dd> A second process obtains a file descriptor for the <code><a href="/docs/linux/man/5-tmpfs/">tmpfs</a></code>(5) file and maps it. Among the possible ways in which this could happen are the following:</p>
<dl>
<dt>
<dd>
<dl>
<dt>*</p>
<dd> The process that called <code>memfd_create</code>() could transfer the resulting file descriptor to the second process via a UNIX domain socket (see <code><a href="/docs/linux/man/7-unix/">unix</a></code>(7) and <code><a href="/docs/linux/man/3-cmsg/">cmsg</a></code>(3)). The second process then maps the file using <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2).</p>
<dt>*</p>
<dd> The second process is created via <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2) and thus automatically inherits the file descriptor and mapping. (Note that in this case and the next, there is a natural trust relationship between the two processes, since they are running under the same user ID. Therefore, file sealing would not normally be necessary.)</p>
<dt>*</p>
<dd> The second process opens the file <i>/proc/&lt;pid&gt;/fd/&lt;fd&gt;</i>, where <i>&lt;pid&gt;</i> is the PID of the first process (the one that called <code>memfd_create</code>()), and <i>&lt;fd&gt;</i> is the number of the file descriptor returned by the call to <code>memfd_create</code>() in that process. The second process then maps the file using <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2).</dl>
</dl>
<dt>5.</p>
<dd> The second process uses the <code><a href="/docs/linux/man/2-fcntl/">fcntl</a></code>(2) <code>F_GET_SEALS</code> operation to retrieve the bit mask of seals that has been applied to the file. This bit mask can be inspected in order to determine what kinds of restrictions have been placed on file modifications. If desired, the second process can apply further seals to impose additional restrictions (so long as the <code>F_SEAL_SEAL</code> seal has not yet been applied).</dl>
<h2>EXAMPLES</h2>
<p> Below are shown two example programs that demonstrate the use of <code>memfd_create</code>() and the file sealing API. </p>
<p> The first program, <i>t_memfd_create.c</i>, creates a <code><a href="/docs/linux/man/5-tmpfs/">tmpfs</a></code>(5) file using <code>memfd_create</code>(), sets a size for the file, maps it into memory, and optionally places some seals on the file. The program accepts up to three command-line arguments, of which the first two are required. The first argument is the name to associate with the file, the second argument is the size to be set for the file, and the optional third argument is a string of characters that specify seals to be set on file. </p>
<p> The second program, <i>t_get_seals.c</i>, can be used to open an existing file that was created via <code>memfd_create</code>() and inspect the set of seals that have been applied to that file. </p>
<p> The following shell session demonstrates the use of these programs. First we create a <code><a href="/docs/linux/man/5-tmpfs/">tmpfs</a></code>(5) file and set some seals on it: </p>
<p> $ <code>./t_memfd_create my_memfd_file 4096 sw &amp;</code> [1] 11775 PID: 11775; fd: 3; /proc/11775/fd/3 </p>
<p> At this point, the <i>t_memfd_create</i> program continues to run in the background. From another program, we can obtain a file descriptor for the file created by <code>memfd_create</code>() by opening the <i>/proc/[pid]/fd</i> file that corresponds to the file descriptor opened by <code>memfd_create</code>(). Using that pathname, we inspect the content of the <i>/proc/[pid]/fd</i> symbolic link, and use our <i>t_get_seals</i> program to view the seals that have been placed on the file: </p>
<p> $ <code>readlink /proc/11775/fd/3</code> /memfd:my_memfd_file (deleted) $ <code>./t_get_seals /proc/11775/fd/3</code> Existing seals: WRITE SHRINK</p>
<h3>Program source: t_memfd_create.c</h3>
<p> #define _GNU_SOURCE #include &lt;stdint.h&gt; #include &lt;sys/mman.h&gt; #include &lt;fcntl.h&gt; #include &lt;stdlib.h&gt; #include &lt;unistd.h&gt; #include &lt;string.h&gt; #include &lt;stdio.h&gt; </p>
<p> #define errExit(msg) do { perror(msg); exit(EXIT_FAILURE); \<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;}&nbsp;while&nbsp;(0) </p>
<p> int main(int argc, char *argv[]) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int fd;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned int seals;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;*addr;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;*name,&nbsp;*seals_arg;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;ssize_t len; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(argc&nbsp;&lt;&nbsp;3)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fprintf(stderr,&nbsp;&quot;%s name size&nbsp;[seals]
&quot;, argv[0]);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fprintf(stderr,&nbsp;&quot;	&#8217;seals&#8217;&nbsp;can contain any of the&nbsp;&quot;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&quot;following characters:
&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fprintf(stderr,&nbsp;&quot;		g &#8211; F_SEAL_GROW
&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fprintf(stderr,&nbsp;&quot;		s &#8211; F_SEAL_SHRINK
&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fprintf(stderr,&nbsp;&quot;		w &#8211; F_SEAL_WRITE
&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fprintf(stderr,&nbsp;&quot;		W &#8211; F_SEAL_FUTURE_WRITE
&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fprintf(stderr,&nbsp;&quot;		S &#8211; F_SEAL_SEAL
&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;name&nbsp;=&nbsp;argv[1];<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;len&nbsp;=&nbsp;atoi(argv[2]);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;seals_arg&nbsp;=&nbsp;argv[3]; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Create an anonymous file in tmpfs;&nbsp;allow seals to be<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;placed on the file&nbsp;*/ </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fd&nbsp;=&nbsp;memfd_create(name, MFD_ALLOW_SEALING);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(fd&nbsp;==&nbsp;-1)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;errExit(&quot;memfd_create&quot;); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Size the file as specified on the command line&nbsp;*/ </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(ftruncate(fd, len)&nbsp;==&nbsp;-1)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;errExit(&quot;truncate&quot;); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;PID:&nbsp;%jd;&nbsp;fd:&nbsp;%d;&nbsp;/proc/%jd/fd/%d
&quot;,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(intmax_t)&nbsp;getpid(), fd,&nbsp;(intmax_t)&nbsp;getpid(), fd); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Code to map the file and populate the mapping with data<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;omitted&nbsp;*/ </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;If a&nbsp;&#8216;seals&#8217;&nbsp;command-line argument was supplied, set some<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;seals on the file&nbsp;*/ </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(seals_arg&nbsp;!=&nbsp;NULL)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;seals&nbsp;=&nbsp;0; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(strchr(seals_arg,&nbsp;&#8216;g&#8217;)&nbsp;!=&nbsp;NULL)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;seals |=&nbsp;F_SEAL_GROW;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(strchr(seals_arg,&nbsp;&#8216;s&#8217;)&nbsp;!=&nbsp;NULL)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;seals |=&nbsp;F_SEAL_SHRINK;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(strchr(seals_arg,&nbsp;&#8216;w&#8217;)&nbsp;!=&nbsp;NULL)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;seals |=&nbsp;F_SEAL_WRITE;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(strchr(seals_arg,&nbsp;&#8216;W&#8217;)&nbsp;!=&nbsp;NULL)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;seals |=&nbsp;F_SEAL_FUTURE_WRITE;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(strchr(seals_arg,&nbsp;&#8216;S&#8217;)&nbsp;!=&nbsp;NULL)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;seals |=&nbsp;F_SEAL_SEAL; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(fcntl(fd, F_ADD_SEALS, seals)&nbsp;==&nbsp;-1)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;errExit(&quot;fcntl&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Keep running, so that the file created by memfd_create()<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;continues to exist&nbsp;*/ </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;pause(); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_SUCCESS); }</p>
<h3>Program source: t_get_seals.c</h3>
<p> #define _GNU_SOURCE #include &lt;sys/mman.h&gt; #include &lt;fcntl.h&gt; #include &lt;unistd.h&gt; #include &lt;stdlib.h&gt; #include &lt;string.h&gt; #include &lt;stdio.h&gt; </p>
<p> #define errExit(msg) do { perror(msg); exit(EXIT_FAILURE); \<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;}&nbsp;while&nbsp;(0) </p>
<p> int main(int argc, char *argv[]) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int fd;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned int seals; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(argc&nbsp;!=&nbsp;2)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fprintf(stderr,&nbsp;&quot;%s&nbsp;/proc/PID/fd/FD
&quot;, argv[0]);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fd&nbsp;=&nbsp;open(argv[1], O_RDWR);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(fd&nbsp;==&nbsp;-1)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;errExit(&quot;open&quot;); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;seals&nbsp;=&nbsp;fcntl(fd, F_GET_SEALS);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(seals&nbsp;==&nbsp;-1)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;errExit(&quot;fcntl&quot;); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;Existing seals:&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(seals&nbsp;&amp;&nbsp;F_SEAL_SEAL)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;&nbsp;SEAL&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(seals&nbsp;&amp;&nbsp;F_SEAL_GROW)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;&nbsp;GROW&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(seals&nbsp;&amp;&nbsp;F_SEAL_WRITE)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;&nbsp;WRITE&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(seals&nbsp;&amp;&nbsp;F_SEAL_FUTURE_WRITE)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;&nbsp;FUTURE_WRITE&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(seals&nbsp;&amp;&nbsp;F_SEAL_SHRINK)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;&nbsp;SHRINK&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;
&quot;); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Code to map the file and access the contents of the<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;resulting mapping omitted&nbsp;*/ </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_SUCCESS); }</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-fcntl/">fcntl</a></code>(2), <code><a href="/docs/linux/man/2-ftruncate/">ftruncate</a></code>(2), <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2), <code><a href="/docs/linux/man/2-shmget/">shmget</a></code>(2), <code><a href="/docs/linux/man/3-shm_open/">shm_open</a></code>(3)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
