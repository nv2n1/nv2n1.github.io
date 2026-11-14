---
title: "malloc_info(3)"
name: "malloc_info"
section: "3"
letter: "m"
url: "/docs/linux/man/3-malloc_info/"
description: "malloc_info – export malloc state to a stream"
---

<h2 class="name">NAME</h2>
<p> malloc_info &#8211; export malloc state to a stream </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;malloc.h&gt;
int malloc_info(int options, FILE *stream);
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>malloc_info</code>() function exports an XML string that describes the current state of the memory-allocation implementation in the caller. The string is printed on the file stream <i>stream</i>. The exported string includes information about all arenas (see <code><a href="/docs/linux/man/3-malloc/">malloc</a></code>(3)). </p>
<p> As currently implemented, <i>options</i> must be zero.</p>
<h2>RETURN VALUE</h2>
<p> On success, <code>malloc_info</code>() returns 0; on error, it returns -1, with <i>errno</i> set to indicate the cause.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EINVAL</code></p>
<dd> <i>options</i> was nonzero.</dl>
<h2>VERSIONS</h2>
<p> <code>malloc_info</code>() was added to glibc in version 2.10.</p>
<h2>ATTRIBUTES</h2>
<p> For an explanation of the terms used in this section, see <code><a href="/docs/linux/man/7-attributes/">attributes</a></code>(7). </p>
<table BORDER>
<tr VALIGN=top>
<td><code>Interface</code></td>
<td><code>Attribute</code></td>
<td><code>Value</code>
</td>
</tr>
<tr VALIGN=top>
<td> <code>malloc_info</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> This function is a GNU extension.</p>
<h2>NOTES</h2>
<p> The memory-allocation information is provided as an XML string (rather than a C structure) because the information may change over time (according to changes in the underlying implementation). The output XML string includes a version field. </p>
<p> The <code><a href="/docs/linux/man/3-open_memstream/">open_memstream</a></code>(3) function can be used to send the output of <code>malloc_info</code>() directly into a buffer in memory, rather than to a file. </p>
<p> The <code>malloc_info</code>() function is designed to address deficiencies in <code><a href="/docs/linux/man/3-malloc_stats/">malloc_stats</a></code>(3) and <code><a href="/docs/linux/man/3-mallinfo/">mallinfo</a></code>(3).</p>
<h2>EXAMPLES</h2>
<p> The program below takes up to four command-line arguments, of which the first three are mandatory. The first argument specifies the number of threads that the program should create. All of the threads, including the main thread, allocate the number of blocks of memory specified by the second argument. The third argument controls the size of the blocks to be allocated. The main thread creates blocks of this size, the second thread created by the program allocates blocks of twice this size, the third thread allocates blocks of three times this size, and so on. </p>
<p> The program calls <code>malloc_info</code>() twice to display the memory-allocation state. The first call takes place before any threads are created or memory allocated. The second call is performed after all threads have allocated memory. </p>
<p> In the following example, the command-line arguments specify the creation of one additional thread, and both the main thread and the additional thread allocate 10000 blocks of memory. After the blocks of memory have been allocated, <code>malloc_info</code>() shows the state of two allocation arenas. </p>
<p> $ <code>getconf GNU_LIBC_VERSION</code> glibc 2.13 $ <code>./a.out 1 10000 100</code> ============ Before allocating blocks ============ &lt;malloc version=&quot;1&quot;&gt; &lt;heap nr=&quot;0&quot;&gt; &lt;sizes&gt; &lt;/sizes&gt; &lt;total type=&quot;fast&quot; count=&quot;0&quot; size=&quot;0&quot;/&gt; &lt;total type=&quot;rest&quot; count=&quot;0&quot; size=&quot;0&quot;/&gt; &lt;system type=&quot;current&quot; size=&quot;135168&quot;/&gt; &lt;system type=&quot;max&quot; size=&quot;135168&quot;/&gt; &lt;aspace type=&quot;total&quot; size=&quot;135168&quot;/&gt; &lt;aspace type=&quot;mprotect&quot; size=&quot;135168&quot;/&gt; &lt;/heap&gt; &lt;total type=&quot;fast&quot; count=&quot;0&quot; size=&quot;0&quot;/&gt; &lt;total type=&quot;rest&quot; count=&quot;0&quot; size=&quot;0&quot;/&gt; &lt;system type=&quot;current&quot; size=&quot;135168&quot;/&gt; &lt;system type=&quot;max&quot; size=&quot;135168&quot;/&gt; &lt;aspace type=&quot;total&quot; size=&quot;135168&quot;/&gt; &lt;aspace type=&quot;mprotect&quot; size=&quot;135168&quot;/&gt; &lt;/malloc&gt; </p>
<p> ============ After allocating blocks ============ &lt;malloc version=&quot;1&quot;&gt; &lt;heap nr=&quot;0&quot;&gt; &lt;sizes&gt; &lt;/sizes&gt; &lt;total type=&quot;fast&quot; count=&quot;0&quot; size=&quot;0&quot;/&gt; &lt;total type=&quot;rest&quot; count=&quot;0&quot; size=&quot;0&quot;/&gt; &lt;system type=&quot;current&quot; size=&quot;1081344&quot;/&gt; &lt;system type=&quot;max&quot; size=&quot;1081344&quot;/&gt; &lt;aspace type=&quot;total&quot; size=&quot;1081344&quot;/&gt; &lt;aspace type=&quot;mprotect&quot; size=&quot;1081344&quot;/&gt; &lt;/heap&gt; &lt;heap nr=&quot;1&quot;&gt; &lt;sizes&gt; &lt;/sizes&gt; &lt;total type=&quot;fast&quot; count=&quot;0&quot; size=&quot;0&quot;/&gt; &lt;total type=&quot;rest&quot; count=&quot;0&quot; size=&quot;0&quot;/&gt; &lt;system type=&quot;current&quot; size=&quot;1032192&quot;/&gt; &lt;system type=&quot;max&quot; size=&quot;1032192&quot;/&gt; &lt;aspace type=&quot;total&quot; size=&quot;1032192&quot;/&gt; &lt;aspace type=&quot;mprotect&quot; size=&quot;1032192&quot;/&gt; &lt;/heap&gt; &lt;total type=&quot;fast&quot; count=&quot;0&quot; size=&quot;0&quot;/&gt; &lt;total type=&quot;rest&quot; count=&quot;0&quot; size=&quot;0&quot;/&gt; &lt;system type=&quot;current&quot; size=&quot;2113536&quot;/&gt; &lt;system type=&quot;max&quot; size=&quot;2113536&quot;/&gt; &lt;aspace type=&quot;total&quot; size=&quot;2113536&quot;/&gt; &lt;aspace type=&quot;mprotect&quot; size=&quot;2113536&quot;/&gt; &lt;/malloc&gt;</p>
<h3>Program source</h3>
<p> #include &lt;unistd.h&gt; #include &lt;stdlib.h&gt; #include &lt;pthread.h&gt; #include &lt;malloc.h&gt; #include &lt;errno.h&gt; </p>
<p> static size_t blockSize; static int numThreads, numBlocks; </p>
<p> #define errExit(msg) do { perror(msg); exit(EXIT_FAILURE); \<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;}&nbsp;while&nbsp;(0) </p>
<p> static void * thread_func(void *arg) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int tn&nbsp;=&nbsp;(int)&nbsp;arg; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;The multiplier&nbsp;&#8216;(2&nbsp;+&nbsp;tn)&#8217;&nbsp;ensures that each thread&nbsp;(including<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;the main thread)&nbsp;allocates a different amount of memory&nbsp;*/ </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;for&nbsp;(int j&nbsp;=&nbsp;0;&nbsp;j&nbsp;&lt;&nbsp;numBlocks;&nbsp;j++)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(malloc(blockSize&nbsp;*&nbsp;(2&nbsp;+&nbsp;tn))&nbsp;==&nbsp;NULL)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;errExit(&quot;malloc-thread&quot;); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;sleep(100);&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Sleep until main thread terminates&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return NULL; } </p>
<p> int main(int argc, char *argv[]) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int sleepTime; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(argc&nbsp;&lt;&nbsp;4)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fprintf(stderr,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&quot;%s num-threads num-blocks block-size&nbsp;[sleep-time]
&quot;,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;argv[0]);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;numThreads&nbsp;=&nbsp;atoi(argv[1]);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;numBlocks&nbsp;=&nbsp;atoi(argv[2]);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;blockSize&nbsp;=&nbsp;atoi(argv[3]);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;sleepTime&nbsp;=&nbsp;(argc&nbsp;&gt;&nbsp;4)&nbsp;?&nbsp;atoi(argv[4])&nbsp;: 0; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;pthread_t&nbsp;*thr&nbsp;=&nbsp;calloc(numThreads, sizeof(*thr));<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(thr&nbsp;==&nbsp;NULL)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;errExit(&quot;calloc&quot;); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;============&nbsp;Before allocating blocks&nbsp;============
&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;malloc_info(0, stdout); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Create threads that allocate different amounts of memory&nbsp;*/ </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;for&nbsp;(int tn&nbsp;=&nbsp;0;&nbsp;tn&nbsp;&lt;&nbsp;numThreads;&nbsp;tn++)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;errno&nbsp;=&nbsp;pthread_create(&amp;thr[tn], NULL, thread_func,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(void&nbsp;*)&nbsp;tn);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(errno&nbsp;!=&nbsp;0)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;errExit(&quot;pthread_create&quot;); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;If we add a sleep interval after the start-up of each<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;thread, the threads likely won&#8217;t contend for malloc<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;mutexes, and therefore additional arenas won&#8217;t be<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;allocated&nbsp;(see&nbsp;<a href="/docs/linux/man/3-malloc/">malloc</a>(3)).&nbsp;*/ </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(sleepTime&nbsp;&gt;&nbsp;0)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;sleep(sleepTime);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;The main thread also allocates some memory&nbsp;*/ </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;for&nbsp;(int j&nbsp;=&nbsp;0;&nbsp;j&nbsp;&lt;&nbsp;numBlocks;&nbsp;j++)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(malloc(blockSize)&nbsp;==&nbsp;NULL)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;errExit(&quot;malloc&quot;); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<a href="/docs/linux/man/2-sleep/">sleep</a>(2);&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Give all threads a chance to<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;complete allocations&nbsp;*/ </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;
============&nbsp;After allocating blocks&nbsp;============
&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;malloc_info(0, stdout); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_SUCCESS); }</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-mallinfo/">mallinfo</a></code>(3), <code><a href="/docs/linux/man/3-malloc/">malloc</a></code>(3), <code><a href="/docs/linux/man/3-malloc_stats/">malloc_stats</a></code>(3), <code><a href="/docs/linux/man/3-mallopt/">mallopt</a></code>(3), <code><a href="/docs/linux/man/3-open_memstream/">open_memstream</a></code>(3)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
