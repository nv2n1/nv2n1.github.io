---
title: "membarrier(2)"
name: "membarrier"
section: "2"
letter: "m"
url: "/docs/linux/man/2-membarrier/"
description: "membarrier – issue memory barriers on a set of threads"
---

<h2 class="name">NAME</h2>
<p> membarrier &#8211; issue memory barriers on a set of threads </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;linux/membarrier.h&gt;
int membarrier(int cmd, unsigned int flags, int cpu_id);
</code></pre>
<p> <i>Note</i>: There is no glibc wrapper for this system call; see NOTES.</p>
<h2>DESCRIPTION</h2>
<p> The <code>membarrier</code>() system call helps reducing the overhead of the memory barrier instructions required to order memory accesses on multi-core systems. However, this system call is heavier than a memory barrier, so using it effectively is <i>not</i> as simple as replacing memory barriers with this system call, but requires understanding of the details below. </p>
<p> Use of memory barriers needs to be done taking into account that a memory barrier always needs to be either matched with its memory barrier counterparts, or that the architecture&#8217;s memory model doesn&#8217;t require the matching barriers. </p>
<p> There are cases where one side of the matching barriers (which we will refer to as &quot;fast side&quot;) is executed much more often than the other (which we will refer to as &quot;slow side&quot;). This is a prime target for the use of <code>membarrier</code>(). The key idea is to replace, for these matching barriers, the fast-side memory barriers by simple compiler barriers, for example: </p>
<p> asm volatile (&quot;&quot; : : : &quot;memory&quot;) </p>
<p> and replace the slow-side memory barriers by calls to <code>membarrier</code>(). </p>
<p> This will add overhead to the slow side, and remove overhead from the fast side, thus resulting in an overall performance increase as long as the slow side is infrequent enough that the overhead of the <code>membarrier</code>() calls does not outweigh the performance gain on the fast side. </p>
<p> The <i>cmd</i> argument is one of the following:</p>
<dl>
<dt><code>MEMBARRIER_CMD_QUERY</code> (since Linux 4.3)</p>
<dd> Query the set of supported commands. The return value of the call is a bit mask of supported commands. <code>MEMBARRIER_CMD_QUERY</code>, which has the value 0, is not itself included in this bit mask. This command is always supported (on kernels where <code>membarrier</code>() is provided).</p>
<dt><code>MEMBARRIER_CMD_GLOBAL</code> (since Linux 4.16)</p>
<dd> Ensure that all threads from all processes on the system pass through a state where all memory accesses to user-space addresses match program order between entry to and return from the <code>membarrier</code>() system call. All threads on the system are targeted by this command.</p>
<dt><code>MEMBARRIER_CMD_GLOBAL_EXPEDITED</code> (since Linux 4.16)</p>
<dd> Execute a memory barrier on all running threads of all processes that previously registered with <code>MEMBARRIER_CMD_REGISTER_GLOBAL_EXPEDITED</code>.</p>
<dt>
<dd> Upon return from the system call, the calling thread has a guarantee that all running threads have passed through a state where all memory accesses to user-space addresses match program order between entry to and return from the system call (non-running threads are de facto in such a state). This guarantee is provided only for the threads of processes that previously registered with <code>MEMBARRIER_CMD_REGISTER_GLOBAL_EXPEDITED</code>.</p>
<dt>
<dd> Given that registration is about the intent to receive the barriers, it is valid to invoke <code>MEMBARRIER_CMD_GLOBAL_EXPEDITED</code> from a process that has not employed <code>MEMBARRIER_CMD_REGISTER_GLOBAL_EXPEDITED</code>.</p>
<dt>
<dd> The &quot;expedited&quot; commands complete faster than the non-expedited ones; they never block, but have the downside of causing extra overhead.</p>
<dt><code>MEMBARRIER_CMD_REGISTER_GLOBAL_EXPEDITED</code> (since Linux 4.16)</p>
<dd> Register the process&#8217;s intent to receive <code>MEMBARRIER_CMD_GLOBAL_EXPEDITED</code> memory barriers.</p>
<dt><code>MEMBARRIER_CMD_PRIVATE_EXPEDITED</code> (since Linux 4.14)</p>
<dd> Execute a memory barrier on each running thread belonging to the same process as the calling thread.</p>
<dt>
<dd> Upon return from the system call, the calling thread has a guarantee that all its running thread siblings have passed through a state where all memory accesses to user-space addresses match program order between entry to and return from the system call (non-running threads are de facto in such a state). This guarantee is provided only for threads in the same process as the calling thread.</p>
<dt>
<dd> The &quot;expedited&quot; commands complete faster than the non-expedited ones; they never block, but have the downside of causing extra overhead.</p>
<dt>
<dd> A process must register its intent to use the private expedited command prior to using it.</p>
<dt><code>MEMBARRIER_CMD_REGISTER_PRIVATE_EXPEDITED</code> (since Linux 4.14)</p>
<dd> Register the process&#8217;s intent to use <code>MEMBARRIER_CMD_PRIVATE_EXPEDITED</code>.</p>
<dt><code>MEMBARRIER_CMD_PRIVATE_EXPEDITED_SYNC_CORE</code> (since Linux 4.16)</p>
<dd> In addition to providing the memory ordering guarantees described in <code>MEMBARRIER_CMD_PRIVATE_EXPEDITED</code>, upon return from system call the calling thread has a guarantee that all its running thread siblings have executed a core serializing instruction. This guarantee is provided only for threads in the same process as the calling thread.</p>
<dt>
<dd> The &quot;expedited&quot; commands complete faster than the non-expedited ones, they never block, but have the downside of causing extra overhead.</p>
<dt>
<dd> A process must register its intent to use the private expedited sync core command prior to using it.</p>
<dt><code>MEMBARRIER_CMD_REGISTER_PRIVATE_EXPEDITED_SYNC_CORE</code> (since Linux 4.16)</p>
<dd> Register the process&#8217;s intent to use <code>MEMBARRIER_CMD_PRIVATE_EXPEDITED_SYNC_CORE</code>.</p>
<dt><code>MEMBARRIER_CMD_PRIVATE_EXPEDITED_RSEQ</code> (since Linux 5.10)</p>
<dd> Ensure the caller thread, upon return from system call, that all its running thread siblings have any currently running rseq critical sections restarted if <i>flags</i> parameter is 0; if <i>flags</i> parameter is <code>MEMBARRIER_CMD_FLAG_CPU</code>, then this operation is performed only on CPU indicated by <i>cpu_id</i>. This guarantee is provided only for threads in the same process as the calling thread.</p>
<dt>
<dd> RSEQ membarrier is only available in the &quot;private expedited&quot; form.</p>
<dt>
<dd> A process must register its intent to use the private expedited rseq command prior to using it.</p>
<dt><code>MEMBARRIER_CMD_REGISTER_PRIVATE_EXPEDITED_RSEQ</code> (since Linux 5.10)</p>
<dd> Register the process&#8217;s intent to use <code>MEMBARRIER_CMD_PRIVATE_EXPEDITED_RSEQ</code>.</p>
<dt><code>MEMBARRIER_CMD_SHARED</code> (since Linux 4.3)</p>
<dd> This is an alias for <code>MEMBARRIER_CMD_GLOBAL</code> that exists for header backward compatibility.</dl>
<p> The <i>flags</i> argument must be specified as 0 unless the command is <code>MEMBARRIER_CMD_PRIVATE_EXPEDITED_RSEQ</code>, in which case <i>flags</i> can be either 0 or <code>MEMBARRIER_CMD_FLAG_CPU</code>. </p>
<p> The <i>cpu_id</i> argument is ignored unless <i>flags</i> is <code>MEMBARRIER_CMD_FLAG_CPU</code>, in which case it must specify the CPU targeted by this membarrier command. </p>
<p> All memory accesses performed in program order from each targeted thread are guaranteed to be ordered with respect to <code>membarrier</code>(). </p>
<p> If we use the semantic <i>barrier()</i> to represent a compiler barrier forcing memory accesses to be performed in program order across the barrier, and <i>smp_mb()</i> to represent explicit memory barriers forcing full memory ordering across the barrier, we have the following ordering table for each pairing of <i>barrier()</i>, <code>membarrier</code>(), and <i>smp_mb()</i>. The pair ordering is detailed as (O: ordered, X: not ordered): </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;barrier()&nbsp;<wbr>&nbsp;smp_mb()&nbsp;<wbr>&nbsp;membarrier()<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;barrier()&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;X&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;X&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;O<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;smp_mb()&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;X&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;O&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;O<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;membarrier()&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;O&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;O&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;O</p>
<h2>RETURN VALUE</h2>
<p> On success, the <code>MEMBARRIER_CMD_QUERY</code> operation returns a bit mask of supported commands, and the <code>MEMBARRIER_CMD_GLOBAL</code>, <code>MEMBARRIER_CMD_GLOBAL_EXPEDITED</code>, <code>MEMBARRIER_CMD_REGISTER_GLOBAL_EXPEDITED</code>, <code>MEMBARRIER_CMD_PRIVATE_EXPEDITED</code>, <code>MEMBARRIER_CMD_REGISTER_PRIVATE_EXPEDITED</code>, <code>MEMBARRIER_CMD_PRIVATE_EXPEDITED_SYNC_CORE</code>, and <code>MEMBARRIER_CMD_REGISTER_PRIVATE_EXPEDITED_SYNC_CORE</code> operations return zero. On error, -1 is returned, and <i>errno</i> is set appropriately. </p>
<p> For a given command, with <i>flags</i> set to 0, this system call is guaranteed to always return the same value until reboot. Further calls with the same arguments will lead to the same result. Therefore, with <i>flags</i> set to 0, error handling is required only for the first call to <code>membarrier</code>().</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EINVAL</code></p>
<dd> <i>cmd</i> is invalid, or <i>flags</i> is nonzero, or the <code>MEMBARRIER_CMD_GLOBAL</code> command is disabled because the <i>nohz_full</i> CPU parameter has been set, or the <code>MEMBARRIER_CMD_PRIVATE_EXPEDITED_SYNC_CORE</code> and <code>MEMBARRIER_CMD_REGISTER_PRIVATE_EXPEDITED_SYNC_CORE</code> commands are not implemented by the architecture.</p>
<dt><code>ENOSYS</code></p>
<dd> The <code>membarrier</code>() system call is not implemented by this kernel.</p>
<dt><code>EPERM</code></p>
<dd> The current process was not registered prior to using private expedited commands.</dl>
<h2>VERSIONS</h2>
<p> The <code>membarrier</code>() system call was added in Linux 4.3. </p>
<p> Before Linux 5.10, the prototype for <code>membarrier</code>() was: </p>
<p> <code>int membarrier(int </code><i>cmd</i><code>, int </code><i>flags</i><code>);</code></p>
<h2>CONFORMING TO</h2>
<p> <code>membarrier</code>() is Linux-specific.</p>
<h2>NOTES</h2>
<p> A memory barrier instruction is part of the instruction set of architectures with weakly ordered memory models. It orders memory accesses prior to the barrier and after the barrier with respect to matching barriers on other cores. For instance, a load fence can order loads prior to and following that fence with respect to stores ordered by store fences. </p>
<p> Program order is the order in which instructions are ordered in the program assembly code. </p>
<p> Examples where <code>membarrier</code>() can be useful include implementations of Read-Copy-Update libraries and garbage collectors. </p>
<p> Glibc does not provide a wrapper for this system call; call it using <code><a href="/docs/linux/man/2-syscall/">syscall</a></code>(2).</p>
<h2>EXAMPLES</h2>
<p> Assuming a multithreaded application where &quot;fast_path()&quot; is executed very frequently, and where &quot;slow_path()&quot; is executed infrequently, the following code (x86) can be transformed using <code>membarrier</code>(): </p>
<p> #include &lt;stdlib.h&gt; </p>
<p> static volatile int a, b; </p>
<p> static void fast_path(int *read_b) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;a&nbsp;=&nbsp;1;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;asm volatile&nbsp;(&quot;mfence&quot;&nbsp;: : :&nbsp;&quot;memory&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;*read_b&nbsp;=&nbsp;b; } </p>
<p> static void slow_path(int *read_a) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;b&nbsp;=&nbsp;1;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;asm volatile&nbsp;(&quot;mfence&quot;&nbsp;: : :&nbsp;&quot;memory&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;*read_a&nbsp;=&nbsp;a; } </p>
<p> int main(int argc, char **argv) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int read_a, read_b; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;*&nbsp;Real applications would call fast_path()&nbsp;and slow_path()<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;*&nbsp;from different threads. Call those from main()&nbsp;to keep<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;*&nbsp;this example short.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;*/ </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;slow_path(&amp;read_a);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fast_path(&amp;read_b); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;*&nbsp;read_b&nbsp;==&nbsp;0 implies read_a&nbsp;==&nbsp;1 and<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;*&nbsp;read_a&nbsp;==&nbsp;0 implies read_b&nbsp;==&nbsp;1.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;*/ </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(read_b&nbsp;==&nbsp;0&nbsp;&amp;&amp;&nbsp;read_a&nbsp;==&nbsp;0)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;abort(); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_SUCCESS); } </p>
<p> The code above transformed to use <code>membarrier</code>() becomes: </p>
<p> #define _GNU_SOURCE #include &lt;stdlib.h&gt; #include &lt;stdio.h&gt; #include &lt;unistd.h&gt; #include &lt;sys/syscall.h&gt; #include &lt;linux/membarrier.h&gt; </p>
<p> static volatile int a, b; </p>
<p> static int membarrier(int cmd, unsigned int flags, int cpu_id) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return syscall(__NR_membarrier, cmd, flags, cpu_id); } </p>
<p> static int init_membarrier(void) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int ret; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Check that membarrier()&nbsp;is supported.&nbsp;*/ </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;ret&nbsp;=&nbsp;membarrier(MEMBARRIER_CMD_QUERY, 0, 0);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(ret&nbsp;&lt;&nbsp;0)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;perror(&quot;membarrier&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return -1;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(!(ret&nbsp;&amp;&nbsp;MEMBARRIER_CMD_GLOBAL))&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fprintf(stderr,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&quot;membarrier does not support MEMBARRIER_CMD_GLOBAL
&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return -1;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return 0; } </p>
<p> static void fast_path(int *read_b) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;a&nbsp;=&nbsp;1;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;asm volatile&nbsp;(&quot;&quot;&nbsp;: : :&nbsp;&quot;memory&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;*read_b&nbsp;=&nbsp;b; } </p>
<p> static void slow_path(int *read_a) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;b&nbsp;=&nbsp;1;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;membarrier(MEMBARRIER_CMD_GLOBAL, 0, 0);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;*read_a&nbsp;=&nbsp;a; } </p>
<p> int main(int argc, char **argv) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int read_a, read_b; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(init_membarrier())<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;*&nbsp;Real applications would call fast_path()&nbsp;and slow_path()<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;*&nbsp;from different threads. Call those from main()&nbsp;to keep<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;*&nbsp;this example short.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;*/ </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;slow_path(&amp;read_a);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fast_path(&amp;read_b); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;*&nbsp;read_b&nbsp;==&nbsp;0 implies read_a&nbsp;==&nbsp;1 and<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;*&nbsp;read_a&nbsp;==&nbsp;0 implies read_b&nbsp;==&nbsp;1.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;*/ </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(read_b&nbsp;==&nbsp;0&nbsp;&amp;&amp;&nbsp;read_a&nbsp;==&nbsp;0)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;abort(); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_SUCCESS); }</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
