---
title: "shm_unlink(3)"
name: "shm_unlink"
section: "3"
letter: "s"
url: "/docs/linux/man/3-shm_unlink/"
description: "shm_open, shm_unlink – create/open or unlink POSIX shared memory objects"
---

<p>shm_open, shm_unlink &#8211; create/open or unlink POSIX shared memory objects</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;sys/mman.h&gt;

#include &lt;sys/stat.h&gt; /* For mode constants */

#include &lt;fcntl.h&gt; /* For O_* constants */
int shm_open(const char *name, int oflag, mode_t mode);
int shm_unlink(const char *name);</code></pre>
<p> Link with <i>-lrt</i>.</p>
<h2>Description</h2>
<p><code>shm_open</code>() creates and opens a new, or opens an existing, POSIX shared memory object. A POSIX shared memory object is in effect a handle which can be used by unrelated processes to <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2) the same region of shared memory. The <code>shm_unlink</code>() function performs the converse operation, removing an object previously created by <code>shm_open</code>(). </p>
<p> The operation of <code>shm_open</code>() is analogous to that of <code><a href="/docs/linux/man/2-open/">open</a></code>(2). <i>name</i> specifies the shared memory object to be created or opened. For portable use, a shared memory object should be identified by a name of the form <i>/somename</i>; that is, a null-terminated string of up to <code>NAME_MAX</code> (i.e., 255) characters consisting of an initial slash, followed by one or more characters, none of which are slashes. </p>
<p> <i>oflag</i> is a bit mask created by ORing together exactly one of <code>O_RDONLY</code> or <code>O_RDWR</code> and any of the other flags listed here:</p>
<dl>
<dt><code>O_RDONLY</code></p>
<dd>Open the object for read access. A shared memory object opened in this way can be <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2)ed only for read (<code>PROT_READ</code>) access.</p>
<dt><code>O_RDWR</code></p>
<dd>Open the object for read-write access.</p>
<dt><code>O_CREAT</code></p>
<dd>Create the shared memory object if it does not exist. The user and group ownership of the object are taken from the corresponding effective IDs of the calling process, and the object&#8217;s permission bits are set according to the low-order 9 bits of <i>mode</i>, except that those bits set in the process file mode creation mask (see <code><a href="/docs/linux/man/2-umask/">umask</a></code>(2)) are cleared for the new object. A set of macro constants which can be used to define <i>mode</i> is listed in <code><a href="/docs/linux/man/2-open/">open</a></code>(2). (Symbolic definitions of these constants can be obtained by including <i>&lt;sys/stat.h&gt;</i>.)</p>
<dd>A new shared memory object initially has zero length&#8212;the size of the object can be set using <code><a href="/docs/linux/man/2-ftruncate/">ftruncate</a></code>(2). The newly allocated bytes of a shared memory object are automatically initialized to 0.</p>
<dt><code>O_EXCL</code></p>
<dd>If <code>O_CREAT</code> was also specified, and a shared memory object with the given <i>name</i> already exists, return an error. The check for the existence of the object, and its creation if it does not exist, are performed atomically.</p>
<dt><code>O_TRUNC</code></p>
<dd>If the shared memory object already exists, truncate it to zero bytes.</dl>
<p> Definitions of these flag values can be obtained by including <i>&lt;fcntl.h&gt;</i>. </p>
<p> On successful completion <code>shm_open</code>() returns a new file descriptor referring to the shared memory object. This file descriptor is guaranteed to be the lowest-numbered file descriptor not previously opened within the process. The <code>FD_CLOEXEC</code> flag (see <code><a href="/docs/linux/man/2-fcntl/">fcntl</a></code>(2)) is set for the file descriptor. </p>
<p> The file descriptor is normally used in subsequent calls to <code><a href="/docs/linux/man/2-ftruncate/">ftruncate</a></code>(2) (for a newly created object) and <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2). After a call to <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2) the file descriptor may be closed without affecting the memory mapping. </p>
<p> The operation of <code>shm_unlink</code>() is analogous to <code><a href="/docs/linux/man/2-unlink/">unlink</a></code>(2): it removes a shared memory object name, and, once all processes have unmapped the object, de-allocates and destroys the contents of the associated memory region. After a successful <code>shm_unlink</code>(), attempts to <code>shm_open</code>() an object with the same <i>name</i> fail (unless <code>O_CREAT</code> was specified, in which case a new, distinct object is created).</p>
<h2>Return Value</h2>
<p>On success, <code>shm_open</code>() returns a file descriptor (a nonnegative integer). On failure, <code>shm_open</code>() returns -1. <code>shm_unlink</code>() returns 0 on success, or -1 on error.</p>
<h2>Errors</h2>
<p>On failure, <i>errno</i> is set to indicate the cause of the error. Values which may appear in <i>errno</i> include the following:</p>
<dl>
<dt><code>EACCES</code></p>
<dd>Permission to <code>shm_unlink</code>() the shared memory object was denied.</p>
<dt><code>EACCES</code></p>
<dd>Permission was denied to <code>shm_open</code>() <i>name</i> in the specified <i>mode</i>, or <code>O_TRUNC</code> was specified and the caller does not have write permission on the object.</p>
<dt><code>EEXIST</code></p>
<dd>Both <code>O_CREAT</code> and <code>O_EXCL</code> were specified to <code>shm_open</code>() and the shared memory object specified by <i>name</i> already exists.</p>
<dt><code>EINVAL</code></p>
<dd>The <i>name</i> argument to <code>shm_open</code>() was invalid.</p>
<dt><code>EMFILE</code></p>
<dd>The per-process limit on the number of open file descriptors has been reached.</p>
<dt><code>ENAMETOOLONG</code></p>
<dd>The length of <i>name</i> exceeds <code>PATH_MAX</code>.</p>
<dt><code>ENFILE</code></p>
<dd>The system-wide limit on the total number of open files has been reached.</p>
<dt><code>ENOENT</code></p>
<dd>An attempt was made to <code>shm_open</code>() a <i>name</i> that did not exist, and <code>O_CREAT</code> was not specified.</p>
<dt><code>ENOENT</code></p>
<dd>An attempt was to made to <code>shm_unlink</code>() a <i>name</i> that does not exist.</dl>
<h2>Versions</h2>
<p>These functions are provided in glibc 2.2 and later.</p>
<h2>Attributes</h2>
<p>For an explanation of the terms used in this section, see <code><a href="/docs/linux/man/7-attributes/">attributes</a></code>(7). </p>
<table BORDER>
<tr VALIGN=top>
<td><code>Interface</code></td>
<td><code>Attribute</code></td>
<td><code>Value</code>
</td>
</tr>
<tr VALIGN=top>
<td> <code>shm_open</code>(), <code>shm_unlink</code>() </td>
<td>Thread safety</td>
<td>MT-Safe locale
</td>
</tr>
</table>
<h2>Conforming To</h2>
<p>POSIX.1-2001, POSIX.1-2008. </p>
<p> POSIX.1-2001 says that the group ownership of a newly created shared memory object is set to either the calling process&#8217;s effective group ID or &quot;a system default group ID&quot;. POSIX.1-2008 says that the group ownership may be set to either the calling process&#8217;s effective group ID or, if the object is visible in the filesystem, the group ID of the parent directory.</p>
<h2>Notes</h2>
<p>POSIX leaves the behavior of the combination of <code>O_RDONLY</code> and <code>O_TRUNC</code> unspecified. On Linux, this will successfully truncate an existing shared memory object&#8212;this may not be so on other UNIX systems. </p>
<p> The POSIX shared memory object implementation on Linux makes use of a dedicated <code><a href="/docs/linux/man/5-tmpfs/">tmpfs</a></code>(5) filesystem that is normally mounted under <i>/dev/shm</i>.</p>
<h2>Examples</h2>
<p>The programs below employ POSIX shared memory and POSIX unnamed semaphores to exchange a piece of data. The &quot;bounce&quot; program (which must be run first) raises the case of a string that is placed into the shared memory by the &quot;send&quot; program. Once the data has been modified, the &quot;send&quot; program then prints the contents of the modified shared memory. An example execution of the two programs is the following: $ <code>./pshm_ucase_bounce /myshm &amp;</code> [1] 270171 $ <code>./pshm_ucase_send /myshm hello</code> HELLO Further detail about these programs is provided below.</p>
<h3>Program source: pshm_ucase.h</h3>
<p>The following header file is included by both programs below. Its primary purpose is to define a structure that will be imposed on the memory object that is shared between the two programs. Licensed under GNU General Public License v2 or later.<br />
                                                        * /<br />
#include &quot;pshm_ucase.h&quot;<br />
#include &lt;string.h&gt;<br />
                                                    int<br />
                                                    main(int argc, char *argv[])<br />
{<br />
    if (argc != 3) {<br />
        fprintf(stderr, &quot;Usage: %s /shm-path string
&quot;, argv[0]);<br />
        exit(EXIT_FAILURE);<br />
    }<br />
    char *shmpath = argv[1];<br />
    char *string = argv[2];<br />
    size_t len = strlen(string);<br />
    if (len &gt; BUF_SIZE) {<br />
        fprintf(stderr, &quot;String is too long
&quot;);<br />
        exit(EXIT_FAILURE);<br />
    }<br />
    /* Open the existing shared memory object and map it<br />
           into the caller&#8217;s address space */<br />
    int fd = shm_open(shmpath, O_RDWR, 0);<br />
    if (fd == -1)<br />
        errExit(&quot;shm_open&quot;);<br />
    struct shmbuf *shmp = mmap(NULL, sizeof(*shmp),<br />
                               PROT_READ | PROT_WRITE,<br />
                               MAP_SHARED, fd, 0);<br />
    if (shmp == MAP_FAILED)<br />
        errExit(&quot;mmap&quot;);<br />
    /* Copy data into the shared memory object */<br />
    shmp-&gt;cnt = len;<br />
    memcpy(&amp;shmp-&gt;buf, string, len);<br />
    /* Tell peer that it can now access shared memory */<br />
    if (sem_post(&amp;shmp-&gt;sem1) == -1)<br />
        errExit(&quot;sem_post&quot;);<br />
    /* Wait until peer says that it has finished accessing<br />
           the shared memory */<br />
    if (sem_wait(&amp;shmp-&gt;sem2) == -1)<br />
        errExit(&quot;sem_wait&quot;);<br />
    /* Write modified data in shared memory to standard output */<br />
    write(STDOUT_FILENO, &amp;shmp-&gt;buf, len);<br />
    write(STDOUT_FILENO, &quot;
&quot;, 1);<br />
    exit(EXIT_SUCCESS);<br />
} /* Define a structure that will be imposed on the shared<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;memory object&nbsp;*/ struct shmbuf {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;sem_t&nbsp;<wbr>&nbsp;sem1;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;POSIX unnamed semaphore&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;sem_t&nbsp;<wbr>&nbsp;sem2;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;POSIX unnamed semaphore&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;size_t cnt;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Number of bytes used in&nbsp;&#8216;buf&#8217;&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;<wbr>&nbsp;<wbr>&nbsp;buf[BUF_SIZE];&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Data being transferred&nbsp;*/ };</p>
<h3>Program source: pshm_ucase_bounce.c</h3>
<p>The &quot;bounce&quot; program creates a new shared memory object with the name given in its command-line argument and sizes the object to match the size of the <i>shmbuf</i> structure defined in the header file. It then maps the object into the process&#8217;s address space, and initializes two POSIX semaphores inside the object to 0. After the &quot;send&quot; program has posted the first of the semaphores, the &quot;bounce&quot; program upper cases the data that has been placed in the memory by the &quot;send&quot; program and then posts the second semaphore to tell the &quot;send&quot; program that it may now access the shared memory. /* pshm_ucase_bounce.c Licensed under GNU General Public License v2 or later.<br />
                                                        * /<br />
#include &quot;pshm_ucase.h&quot;<br />
#include &lt;ctype.h&gt;<br />
                                                    int<br />
                                                    main(int argc, char *argv[])<br />
{<br />
    if (argc != 2) {<br />
        fprintf(stderr, &quot;Usage: %s /shm-path
&quot;, argv[0]);<br />
        exit(EXIT_FAILURE);<br />
    }<br />
    char *shmpath = argv[1];<br />
    /* Create shared memory object and set its size to the size<br />
           of our structure */<br />
    int fd = shm_open(shmpath, O_CREAT | O_EXCL | O_RDWR,<br />
                      S_IRUSR | S_IWUSR);<br />
    if (fd == -1)<br />
        errExit(&quot;shm_open&quot;);<br />
    if (ftruncate(fd, sizeof(struct shmbuf)) == -1)<br />
        errExit(&quot;ftruncate&quot;);<br />
    /* Map the object into the caller&#8217;s address space */<br />
    struct shmbuf *shmp = mmap(NULL, sizeof(*shmp),<br />
                               PROT_READ | PROT_WRITE,<br />
                               MAP_SHARED, fd, 0);<br />
    if (shmp == MAP_FAILED)<br />
        errExit(&quot;mmap&quot;);<br />
    /* Initialize semaphores as process-shared, with value 0 */<br />
    if (sem_init(&amp;shmp-&gt;sem1, 1, 0) == -1)<br />
        errExit(&quot;sem_init-sem1&quot;);<br />
    if (sem_init(&amp;shmp-&gt;sem2, 1, 0) == -1)<br />
        errExit(&quot;sem_init-sem2&quot;);<br />
    /* Wait for &#8216;sem1&#8217; to be posted by peer before touching<br />
           shared memory */<br />
    if (sem_wait(&amp;shmp-&gt;sem1) == -1)<br />
        errExit(&quot;sem_wait&quot;);<br />
    /* Convert data in shared memory into upper case */<br />
    for (int j = 0; j &lt; shmp-&gt;cnt; j++)<br />
        shmp-&gt;buf[j] = toupper((unsigned char)shmp-&gt;buf[j]);<br />
    /* Post &#8216;sem2&#8217; to tell the to tell peer that it can now<br />
           access the modified data in shared memory */<br />
    if (sem_post(&amp;shmp-&gt;sem2) == -1)<br />
        errExit(&quot;sem_post&quot;);<br />
    /* Unlink the shared memory object. Even if the peer process<br />
           is still using the object, this is okay. The object will<br />
           be removed only after all open references are closed. */<br />
    shm_unlink(shmpath);<br />
    exit(EXIT_SUCCESS);<br />
}</p>
<p>Program source : pshm_ucase_send.c</p>
<p>                     The &quot;send&quot; program takes two command &#8211;<br />
    line arguments : the pathname of a shared memory object previously created by the &quot;bounce&quot; program and a string that is to be copied into that object. The program opens the shared memory object and maps the object into its address space. It then copies the data specified in its second argument into the shared memory, and posts the first semaphore, which tells the &quot;bounce&quot; program that it can now access that data. After the &quot;bounce&quot; program posts the second semaphore, the &quot;send&quot; program prints the contents of the shared memory on standard output. /* pshm_ucase_send.c </p>
<pre><code>Licensed under GNU General Public License v2 or later.
                                                        * /
#include &quot;pshm_ucase.h&quot;
#include &lt;string.h&gt;
                                                    int
                                                    main(int argc, char *argv[])
{
    if (argc != 3) {
        fprintf(stderr, &quot;Usage: %s /shm-path string
&quot;, argv[0]);
        exit(EXIT_FAILURE);
    }
    char *shmpath = argv[1];
    char *string = argv[2];
    size_t len = strlen(string);
    if (len &gt; BUF_SIZE) {
        fprintf(stderr, &quot;String is too long
&quot;);
        exit(EXIT_FAILURE);
    }
    /* Open the existing shared memory object and map it
           into the caller's address space */
    int fd = shm_open(shmpath, O_RDWR, 0);
    if (fd == -1)
        errExit(&quot;shm_open&quot;);
    struct shmbuf *shmp = mmap(NULL, sizeof(*shmp),
                               PROT_READ | PROT_WRITE,
                               MAP_SHARED, fd, 0);
    if (shmp == MAP_FAILED)
        errExit(&quot;mmap&quot;);
    /* Copy data into the shared memory object */
    shmp-&gt;cnt = len;
    memcpy(&amp;shmp-&gt;buf, string, len);
    /* Tell peer that it can now access shared memory */
    if (sem_post(&amp;shmp-&gt;sem1) == -1)
        errExit(&quot;sem_post&quot;);
    /* Wait until peer says that it has finished accessing
           the shared memory */
    if (sem_wait(&amp;shmp-&gt;sem2) == -1)
        errExit(&quot;sem_wait&quot;);
    /* Write modified data in shared memory to standard output */
    write(STDOUT_FILENO, &amp;shmp-&gt;buf, len);
    write(STDOUT_FILENO, &quot;
&quot;, 1);
    exit(EXIT_SUCCESS);
}</code></pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/2-close/">close</a></code>(2), <code><a href="/docs/linux/man/2-fchmod/">fchmod</a></code>(2), <code><a href="/docs/linux/man/2-fchown/">fchown</a></code>(2), <code><a href="/docs/linux/man/2-fcntl/">fcntl</a></code>(2), <code><a href="/docs/linux/man/2-fstat/">fstat</a></code>(2), <code><a href="/docs/linux/man/2-ftruncate/">ftruncate</a></code>(2), <code><a href="/docs/linux/man/2-memfd_create/">memfd_create</a></code>(2), <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2), <code><a href="/docs/linux/man/2-open/">open</a></code>(2), <code><a href="/docs/linux/man/2-umask/">umask</a></code>(2), <code><a href="/docs/linux/man/7-shm_overview/">shm_overview</a></code>(7)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
