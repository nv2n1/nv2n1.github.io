---
title: "cpu_and_s(3)"
name: "cpu_and_s"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cpu_and_s/"
description: "CPU_SET, CPU_CLR, CPU_ISSET, CPU_ZERO, CPU_COUNT, CPU_AND, CPU_OR, CPU_XOR, CPU_EQUAL, CPU_ALLOC, CPU_ALLOC_SIZE, CPU_FREE, CPU_SET_S, CPU_CLR_S, CPU_ISSET_S, CPU_ZERO_S, CPU_COUNT_S, CPU_AND_S, CP..."
---

<p>CPU_SET, CPU_CLR, CPU_ISSET, CPU_ZERO, CPU_COUNT, CPU_AND, CPU_OR, CPU_XOR, CPU_EQUAL, CPU_ALLOC, CPU_ALLOC_SIZE, CPU_FREE, CPU_SET_S, CPU_CLR_S, CPU_ISSET_S, CPU_ZERO_S, CPU_COUNT_S, CPU_AND_S, CPU_OR_S, CPU_XOR_S, CPU_EQUAL_S &#8211; macros for manipulating CPU sets </p>
<h2>Synopsis</h2>
<pre><code>#define _GNU_SOURCE</code> /* See <a href="//www.systutorials.com/docs/linux/man/7-feature_test_macros/">feature_test_macros</a>(7) */
<code>#include &lt;sched.h&gt;</code>
<code>void CPU_ZERO(cpu_set_t *</code><i>set</i><code>);</code>
<code>void CPU_SET(int </code><i>cpu</i><code>, cpu_set_t *</code><i>set</i><code>);</code>
<code>void CPU_CLR(int </code><i>cpu</i><code>, cpu_set_t *</code><i>set</i><code>);</code>
<code>int CPU_ISSET(int </code><i>cpu</i><code>, cpu_set_t *</code><i>set</i><code>);</code>
<code>int CPU_COUNT(cpu_set_t *</code><i>set</i><code>);</code>
<code>void CPU_AND(cpu_set_t *</code><i>destset</i><code>,</code>
<code> cpu_set_t *</code><i>srcset1</i><code>, cpu_set_t *</code><i>srcset2</i><code>);</code>
<code>void CPU_OR(cpu_set_t *</code><i>destset</i><code>,</code>
<code> cpu_set_t *</code><i>srcset1</i><code>, cpu_set_t *</code><i>srcset2</i><code>);</code>
<code>void CPU_XOR(cpu_set_t *</code><i>destset</i><code>,</code>
<code> cpu_set_t *</code><i>srcset1</i><code>, cpu_set_t *</code><i>srcset2</i><code>);</code>
<code>int CPU_EQUAL(cpu_set_t *</code><i>set1</i><code>, cpu_set_t *</code><i>set2</i><code>);</code>
<code>cpu_set_t *CPU_ALLOC(int </code><i>num_cpus</i><code>);</code>
<code>void CPU_FREE(cpu_set_t *</code><i>set</i><code>);</code>
<code>size_t CPU_ALLOC_SIZE(int </code><i>num_cpus</i><code>);</code>
<code>void CPU_ZERO_S(size_t </code><i>setsize</i><code>, cpu_set_t *</code><i>set</i><code>);</code>
<code>void CPU_SET_S(int </code><i>cpu</i><code>, size_t </code><i>setsize</i><code>, cpu_set_t *</code><i>set</i><code>);</code>
<code>void CPU_CLR_S(int </code><i>cpu</i><code>, size_t </code><i>setsize</i><code>, cpu_set_t *</code><i>set</i><code>);</code>
<code>int CPU_ISSET_S(int </code><i>cpu</i><code>, size_t </code><i>setsize</i><code>, cpu_set_t *</code><i>set</i><code>);</code>
<code>int CPU_COUNT_S(size_t </code><i>setsize</i><code>, cpu_set_t *</code><i>set</i><code>);</code>
<code>void CPU_AND_S(size_t </code><i>setsize</i><code>, cpu_set_t *</code><i>destset</i><code>,</code>
<code> cpu_set_t *</code><i>srcset1</i><code>, cpu_set_t *</code><i>srcset2</i><code>);</code>
<code>void CPU_OR_S(size_t </code><i>setsize</i><code>, cpu_set_t *</code><i>destset</i><code>,</code>
<code> cpu_set_t *</code><i>srcset1</i><code>, cpu_set_t *</code><i>srcset2</i><code>);</code>
<code>void CPU_XOR_S(size_t </code><i>setsize</i><code>, cpu_set_t *</code><i>destset</i><code>,</code>
<code> cpu_set_t *</code><i>srcset1</i><code>, cpu_set_t *</code><i>srcset2</i><code>);</code>
<code>int CPU_EQUAL_S(size_t </code><i>setsize</i><code>, cpu_set_t *</code><i>set1</i><code>, cpu_set_t *</code><i>set2</i><code>);</code></pre>
<h2>Description</h2>
<p>The <i>cpu_set_t</i> data structure represents a set of CPUs. CPU sets are used by <code><a href="/docs/linux/man/2-sched_setaffinity/">sched_setaffinity</a></code>(2) and similar interfaces. </p>
<p> The <i>cpu_set_t</i> data type is implemented as a bit mask. However, the data structure should be treated as opaque: all manipulation of CPU sets should be done via the macros described in this page. </p>
<p> The following macros are provided to operate on the CPU set <i>set</i>:</p>
<dl COMPACT>
<dt><code>CPU_ZERO</code>()</p>
<dd>Clears <i>set</i>, so that it contains no CPUs.</p>
<dt><code>CPU_SET</code>()</p>
<dd>Add CPU <i>cpu</i> to <i>set</i>.</p>
<dt><code>CPU_CLR</code>()</p>
<dd>Remove CPU <i>cpu</i> from <i>set</i>.</p>
<dt><code>CPU_ISSET</code>()</p>
<dd>Test to see if CPU <i>cpu</i> is a member of <i>set</i>.</p>
<dt><code>CPU_COUNT</code>()</p>
<dd>Return the number of CPUs in <i>set</i>.</dl>
<p> Where a <i>cpu</i> argument is specified, it should not produce side effects, since the above macros may evaluate the argument more than once. </p>
<p> The first CPU on the system corresponds to a <i>cpu</i> value of 0, the next CPU corresponds to a <i>cpu</i> value of 1, and so on. No assumptions should be made about particular CPUs being available, or the set of CPUs being contiguous, since CPUs can be taken offline dynamically or be otherwise absent. The constant <code>CPU_SETSIZE</code> (currently 1024) specifies a value one greater than the maximum CPU number that can be stored in <i>cpu_set_t</i>. </p>
<p> The following macros perform logical operations on CPU sets:</p>
<dl COMPACT>
<dt><code>CPU_AND</code>()</p>
<dd>Store the intersection of the sets <i>srcset1</i> and <i>srcset2</i> in <i>destset</i> (which may be one of the source sets).</p>
<dt><code>CPU_OR</code>()</p>
<dd>Store the union of the sets <i>srcset1</i> and <i>srcset2</i> in <i>destset</i> (which may be one of the source sets).</p>
<dt><code>CPU_XOR</code>()</p>
<dd>Store the XOR of the sets <i>srcset1</i> and <i>srcset2</i> in <i>destset</i> (which may be one of the source sets). The XOR means the set of CPUs that are in either <i>srcset1</i> or <i>srcset2</i>, but not both.</p>
<dt><code>CPU_EQUAL</code>()</p>
<dd>Test whether two CPU set contain exactly the same CPUs.</dl>
<h3>Dynamically sized CPU sets</h3>
<p>Because some applications may require the ability to dynamically size CPU sets (e.g., to allocate sets larger than that defined by the standard <i>cpu_set_t</i> data type), glibc nowadays provides a set of macros to support this. </p>
<p> The following macros are used to allocate and deallocate CPU sets:</p>
<dl COMPACT>
<dt><code>CPU_ALLOC</code>()</p>
<dd>Allocate a CPU set large enough to hold CPUs in the range 0 to <i>num_cpus-1</i>.</p>
<dt><code>CPU_ALLOC_SIZE</code>()</p>
<dd>Return the size in bytes of the CPU set that would be needed to hold CPUs in the range 0 to <i>num_cpus-1</i>. This macro provides the value that can be used for the <i>setsize</i> argument in the <code>CPU_*_S</code>() macros described below.</p>
<dt><code>CPU_FREE</code>()</p>
<dd>Free a CPU set previously allocated by <code>CPU_ALLOC</code>().</dl>
<p> The macros whose names end with &quot;_S&quot; are the analogs of the similarly named macros without the suffix. These macros perform the same tasks as their analogs, but operate on the dynamically allocated CPU set(s) whose size is <i>setsize</i> bytes.</p>
<h2>Return Value</h2>
<p><code>CPU_ISSET</code>() and <code>CPU_ISSET_S</code>() return nonzero if <i>cpu</i> is in <i>set</i>; otherwise, it returns 0. </p>
<p> <code>CPU_COUNT</code>() and <code>CPU_COUNT_S</code>() return the number of CPUs in <i>set</i>. </p>
<p> <code>CPU_EQUAL</code>() and <code>CPU_EQUAL_S</code>() return nonzero if the two CPU sets are equal; otherwise they return 0. </p>
<p> <code>CPU_ALLOC</code>() returns a pointer on success, or NULL on failure. (Errors are as for <code><a href="/docs/linux/man/3-malloc/">malloc</a></code>(3).) </p>
<p> <code>CPU_ALLOC_SIZE</code>() returns the number of bytes required to store a CPU set of the specified cardinality. </p>
<p> The other functions do not return a value.</p>
<h2>Versions</h2>
<p>The <code>CPU_ZERO</code>(), <code>CPU_SET</code>(), <code>CPU_CLR</code>(), and <code>CPU_ISSET</code>() macros were added in glibc 2.3.3. </p>
<p> <code>CPU_COUNT</code>() first appeared in glibc 2.6. </p>
<p> <code>CPU_AND</code>(), <code>CPU_OR</code>(), <code>CPU_XOR</code>(), <code>CPU_EQUAL</code>(), <code>CPU_ALLOC</code>(), <code>CPU_ALLOC_SIZE</code>(), <code>CPU_FREE</code>(), <code>CPU_ZERO_S</code>(), <code>CPU_SET_S</code>(), <code>CPU_CLR_S</code>(), <code>CPU_ISSET_S</code>(), <code>CPU_AND_S</code>(), <code>CPU_OR_S</code>(), <code>CPU_XOR_S</code>(), and <code>CPU_EQUAL_S</code>() first appeared in glibc 2.7.</p>
<h2>Conforming To</h2>
<p>These interfaces are Linux-specific.</p>
<h2>Notes</h2>
<p>To duplicate a CPU set, use <code><a href="/docs/linux/man/3-memcpy/">memcpy</a></code>(3). </p>
<p> Since CPU sets are bit masks allocated in units of long words, the actual number of CPUs in a dynamically allocated CPU set will be rounded up to the next multiple of <i>sizeof(unsigned long)</i>. An application should consider the contents of these extra bits to be undefined. </p>
<p> Notwithstanding the similarity in the names, note that the constant <code>CPU_SETSIZE</code> indicates the number of CPUs in the <i>cpu_set_t</i> data type (thus, it is effectively a count of the bits in the bit mask), while the <i>setsize</i> argument of the <code>CPU_*_S</code>() macros is a size in bytes. </p>
<p> The data types for arguments and return values shown in the SYNOPSIS are hints what about is expected in each case. However, since these interfaces are implemented as macros, the compiler won&#8217;t necessarily catch all type errors if you violate the suggestions.</p>
<h2>Bugs</h2>
<p>On 32-bit platforms with glibc 2.8 and earlier, <code>CPU_ALLOC</code>() allocates twice as much space as is required, and <code>CPU_ALLOC_SIZE</code>() returns a value twice as large as it should. This bug should not affect the semantics of a program, but does result in wasted memory and less efficient operation of the macros that operate on dynamically allocated CPU sets. These bugs are fixed in glibc 2.9.</p>
<h2>Examples</h2>
<p>The following program demonstrates the use of some of the macros used for dynamically allocated CPU sets. </p>
<p> #define _GNU_SOURCE #include &lt;sched.h&gt; #include &lt;stdlib.h&gt; #include &lt;unistd.h&gt; #include &lt;stdio.h&gt; #include &lt;assert.h&gt; </p>
<p> int main(int argc, char *argv[]) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;cpu_set_t&nbsp;*cpusetp;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;size_t size;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int num_cpus; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(argc&nbsp;&lt;&nbsp;2)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fprintf(stderr,&nbsp;&quot;Usage:&nbsp;%s&nbsp;&lt;num-cpus&gt;
&quot;, argv[0]);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;num_cpus&nbsp;=&nbsp;atoi(argv[1]); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;cpusetp&nbsp;=&nbsp;CPU_ALLOC(num_cpus);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(cpusetp&nbsp;==&nbsp;NULL)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;perror(&quot;CPU_ALLOC&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;size&nbsp;=&nbsp;CPU_ALLOC_SIZE(num_cpus); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;CPU_ZERO_S(size, cpusetp);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;for&nbsp;(int cpu&nbsp;=&nbsp;0;&nbsp;cpu&nbsp;&lt;&nbsp;num_cpus;&nbsp;cpu&nbsp;+=&nbsp;2)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;CPU_SET_S(cpu, size, cpusetp); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;CPU_COUNT()&nbsp;of set:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;%d
&quot;, CPU_COUNT_S(size, cpusetp)); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;CPU_FREE(cpusetp);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_SUCCESS); }</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/2-sched_setaffinity/">sched_setaffinity</a></code>(2), <code><a href="/docs/linux/man/3-pthread_attr_setaffinity_np/">pthread_attr_setaffinity_np</a></code>(3), <code><a href="/docs/linux/man/3-pthread_setaffinity_np/">pthread_setaffinity_np</a></code>(3), <code><a href="/docs/linux/man/7-cpuset/">cpuset</a></code>(7)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a></p>
