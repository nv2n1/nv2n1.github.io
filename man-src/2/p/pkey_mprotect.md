---
title: "pkey_mprotect(2)"
name: "pkey_mprotect"
section: "2"
letter: "p"
url: "/docs/linux/man/2-pkey_mprotect/"
description: "mprotect, pkey_mprotect – set protection on a region of memory"
---

<h2 class="name">NAME</h2>
<p> mprotect, pkey_mprotect &#8211; set protection on a region of memory </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;sys/mman.h&gt;
int mprotect(void *addr, size_t len, int prot);
#define _GNU_SOURCE /* See feature_test_macros(7) */
#include &lt;sys/mman.h&gt;
int pkey_mprotect(void *addr, size_t len, int prot, int pkey);
</code></pre>
<h2>DESCRIPTION</h2>
<p> <code>mprotect</code>() changes the access protections for the calling process&#8217;s memory pages containing any part of the address range in the interval [<i>addr</i>,&nbsp;<i>addr</i>+<i>len</i>-1]. <i>addr</i> must be aligned to a page boundary. </p>
<p> If the calling process tries to access memory in a manner that violates the protections, then the kernel generates a <code>SIGSEGV</code> signal for the process. </p>
<p> <i>prot</i> is a combination of the following access flags: <code>PROT_NONE</code> or a bitwise-or of the other values in the following list:</p>
<dl>
<dt><code>PROT_NONE</code></p>
<dd> The memory cannot be accessed at all.</p>
<dt><code>PROT_READ</code></p>
<dd> The memory can be read.</p>
<dt><code>PROT_WRITE</code></p>
<dd> The memory can be modified.</p>
<dt><code>PROT_EXEC</code></p>
<dd> The memory can be executed.</p>
<dt><code>PROT_SEM</code> (since Linux 2.5.7)</p>
<dd> The memory can be used for atomic operations. This flag was introduced as part of the <code><a href="/docs/linux/man/2-futex/">futex</a></code>(2) implementation (in order to guarantee the ability to perform atomic operations required by commands such as <code>FUTEX_WAIT</code>), but is not currently used in on any architecture.</p>
<dt><code>PROT_SAO</code> (since Linux 2.6.26)</p>
<dd> The memory should have strong access ordering. This feature is specific to the PowerPC architecture (version 2.06 of the architecture specification adds the SAO CPU feature, and it is available on POWER 7 or PowerPC A2, for example).</dl>
<p> Additionally (since Linux 2.6.0), <i>prot</i> can have one of the following flags set:</p>
<dl>
<dt>
<dd> <code>PROT_GROWSUP</code> Apply the protection mode up to the end of a mapping that grows upwards. (Such mappings are created for the stack area on architectures&#8212;for example, HP-PARISC&#8212;that have an upwardly growing stack.)</p>
<dt><code>PROT_GROWSDOWN</code></p>
<dd> Apply the protection mode down to the beginning of a mapping that grows downward (which should be a stack segment or a segment mapped with the <code>MAP_GROWSDOWN</code> flag set).</dl>
<p> Like <code>mprotect</code>(), <code>pkey_mprotect</code>() changes the protection on the pages specified by <i>addr</i> and <i>len</i>. The <i>pkey</i> argument specifies the protection key (see <code><a href="/docs/linux/man/7-pkeys/">pkeys</a></code>(7)) to assign to the memory. The protection key must be allocated with <code><a href="/docs/linux/man/2-pkey_alloc/">pkey_alloc</a></code>(2) before it is passed to <code>pkey_mprotect</code>(). For an example of the use of this system call, see <code><a href="/docs/linux/man/7-pkeys/">pkeys</a></code>(7).</p>
<h2>RETURN VALUE</h2>
<p> On success, <code>mprotect</code>() and <code>pkey_mprotect</code>() return zero. On error, these system calls return -1, and <i>errno</i> is set appropriately.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EACCES</code></p>
<dd> The memory cannot be given the specified access. This can happen, for example, if you <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2) a file to which you have read-only access, then ask <code>mprotect</code>() to mark it <code>PROT_WRITE</code>.</p>
<dt><code>EINVAL</code></p>
<dd> <i>addr</i> is not a valid pointer, or not a multiple of the system page size.</p>
<dt><code>EINVAL</code></p>
<dd> (<code>pkey_mprotect</code>()) <i>pkey</i> has not been allocated with <code><a href="/docs/linux/man/2-pkey_alloc/">pkey_alloc</a></code>(2)</p>
<dt><code>EINVAL</code></p>
<dd> Both <code>PROT_GROWSUP</code> and <code>PROT_GROWSDOWN</code> were specified in <i>prot</i>.</p>
<dt><code>EINVAL</code></p>
<dd> Invalid flags specified in <i>prot</i>.</p>
<dt><code>EINVAL</code></p>
<dd> (PowerPC architecture) <code>PROT_SAO</code> was specified in <i>prot</i>, but SAO hardware feature is not available.</p>
<dt><code>ENOMEM</code></p>
<dd> Internal kernel structures could not be allocated.</p>
<dt><code>ENOMEM</code></p>
<dd> Addresses in the range [<i>addr</i>, <i>addr</i>+<i>len</i>-1] are invalid for the address space of the process, or specify one or more pages that are not mapped. (Before kernel 2.4.19, the error <code>EFAULT</code> was incorrectly produced for these cases.)</p>
<dt><code>ENOMEM</code></p>
<dd> Changing the protection of a memory region would result in the total number of mappings with distinct attributes (e.g., read versus read/write protection) exceeding the allowed maximum. (For example, making the protection of a range <code>PROT_READ</code> in the middle of a region currently protected as <code>PROT_READ|PROT_WRITE</code> would result in three mappings: two read/write mappings at each end and a read-only mapping in the middle.)</dl>
<h2>VERSIONS</h2>
<p> <code>pkey_mprotect</code>() first appeared in Linux 4.9; library support was added in glibc 2.27.</p>
<h2>CONFORMING TO</h2>
<p> <code>mprotect</code>(): POSIX.1-2001, POSIX.1-2008, SVr4. POSIX says that the behavior of <code>mprotect</code>() is unspecified if it is applied to a region of memory that was not obtained via <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2). </p>
<p> <code>pkey_mprotect</code>() is a nonportable Linux extension.</p>
<h2>NOTES</h2>
<p> On Linux, it is always permissible to call <code>mprotect</code>() on any address in a process&#8217;s address space (except for the kernel vsyscall area). In particular, it can be used to change existing code mappings to be writable. </p>
<p> Whether <code>PROT_EXEC</code> has any effect different from <code>PROT_READ</code> depends on processor architecture, kernel version, and process state. If <code>READ_IMPLIES_EXEC</code> is set in the process&#8217;s personality flags (see <code><a href="/docs/linux/man/2-personality/">personality</a></code>(2)), specifying <code>PROT_READ</code> will implicitly add <code>PROT_EXEC</code>. </p>
<p> On some hardware architectures (e.g., i386), <code>PROT_WRITE</code> implies <code>PROT_READ</code>. </p>
<p> POSIX.1 says that an implementation may permit access other than that specified in <i>prot</i>, but at a minimum can allow write access only if <code>PROT_WRITE</code> has been set, and must not allow any access if <code>PROT_NONE</code> has been set. </p>
<p> Applications should be careful when mixing use of <code>mprotect</code>() and <code>pkey_mprotect</code>(). On x86, when <code>mprotect</code>() is used with <i>prot</i> set to <code>PROT_EXEC</code> a pkey may be allocated and set on the memory implicitly by the kernel, but only when the pkey was 0 previously. </p>
<p> On systems that do not support protection keys in hardware, <code>pkey_mprotect</code>() may still be used, but <i>pkey</i> must be set to -1. When called this way, the operation of <code>pkey_mprotect</code>() is equivalent to <code>mprotect</code>().</p>
<h2>EXAMPLES</h2>
<p> The program below demonstrates the use of <code>mprotect</code>(). The program allocates four pages of memory, makes the third of these pages read-only, and then executes a loop that walks upward through the allocated region modifying bytes. </p>
<p> An example of what we might see when running the program is the following: </p>
<p> $<code> ./a.out</code> Start of region: 0x804c000 Got SIGSEGV at address: 0x804e000</p>
<h3>Program source</h3>
<p> #include &lt;unistd.h&gt; #include &lt;signal.h&gt; #include &lt;stdio.h&gt; #include &lt;malloc.h&gt; #include &lt;stdlib.h&gt; #include &lt;errno.h&gt; #include &lt;sys/mman.h&gt; </p>
<p> #define handle_error(msg) \<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;do&nbsp;{&nbsp;perror(msg);&nbsp;exit(EXIT_FAILURE);&nbsp;}&nbsp;while&nbsp;(0) </p>
<p> static char *buffer; </p>
<p> static void handler(int sig, siginfo_t *si, void *unused) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Note: calling printf()&nbsp;from a signal handler is not safe<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(and should not be done in production programs), since<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf()&nbsp;is not async-signal-safe;&nbsp;see&nbsp;<a href="/docs/linux/man/7-signal-safety/">signal-safety</a>(7).<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Nevertheless, we use printf()&nbsp;here as a simple way of<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;showing that the handler was called.&nbsp;*/ </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;Got SIGSEGV at address:&nbsp;%p
&quot;, si-&gt;si_addr);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE); } </p>
<p> int main(int argc, char *argv[]) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int pagesize;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct sigaction sa; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;sa.sa_flags&nbsp;=&nbsp;SA_SIGINFO;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;sigemptyset(&amp;sa.sa_mask);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;sa.sa_sigaction&nbsp;=&nbsp;handler;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(sigaction(SIGSEGV,&nbsp;&amp;sa, NULL)&nbsp;==&nbsp;-1)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;handle_error(&quot;sigaction&quot;); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;pagesize&nbsp;=&nbsp;sysconf(_SC_PAGE_SIZE);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(pagesize&nbsp;==&nbsp;-1)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;handle_error(&quot;sysconf&quot;); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Allocate a buffer aligned on a page boundary;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;initial protection is PROT_READ | PROT_WRITE&nbsp;*/ </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;buffer&nbsp;=&nbsp;memalign(pagesize, 4&nbsp;*&nbsp;pagesize);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(buffer&nbsp;==&nbsp;NULL)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;handle_error(&quot;memalign&quot;); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;Start of region:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;%p
&quot;, buffer); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(mprotect(buffer&nbsp;+&nbsp;pagesize&nbsp;*&nbsp;2, pagesize,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;PROT_READ)&nbsp;==&nbsp;-1)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;handle_error(&quot;mprotect&quot;); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;for&nbsp;(char&nbsp;*p&nbsp;=&nbsp;buffer&nbsp;;&nbsp;;&nbsp;)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;*(p++)&nbsp;=&nbsp;&#8216;a&#8217;; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;Loop completed
&quot;);&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Should never happen&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_SUCCESS); }</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2), <code><a href="/docs/linux/man/3-sysconf/">sysconf</a></code>(3), <code><a href="/docs/linux/man/7-pkeys/">pkeys</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
