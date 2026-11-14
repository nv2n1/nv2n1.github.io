---
title: "mallopt(3)"
name: "mallopt"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mallopt/"
description: "mallopt – set memory allocation parameters"
---

<h2 class="name">NAME</h2>
<p> mallopt &#8211; set memory allocation parameters </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;malloc.h&gt;</code> </p>
<p> <code>int mallopt(int </code><i>param</i><code>, int </code><i>value</i><code>);</code></p>
<h2>DESCRIPTION</h2>
<p> The <code>mallopt</code>() function adjusts parameters that control the behavior of the memory-allocation functions (see <code><a href="/docs/linux/man/3-malloc/">malloc</a></code>(3)). The <i>param</i> argument specifies the parameter to be modified, and <i>value</i> specifies the new value for that parameter. </p>
<p> The following values can be specified for <i>param</i>:</p>
<dl>
<dt><code>M_ARENA_MAX</code></p>
<dd> If this parameter has a nonzero value, it defines a hard limit on the maximum number of arenas that can be created. An arena represents a pool of memory that can be used by <code><a href="/docs/linux/man/3-malloc/">malloc</a></code>(3) (and similar) calls to service allocation requests. Arenas are thread safe and therefore may have multiple concurrent memory requests. The trade-off is between the number of threads and the number of arenas. The more arenas you have, the lower the per-thread contention, but the higher the memory usage.</p>
<dt>
<dd> The default value of this parameter is 0, meaning that the limit on the number of arenas is determined according to the setting of <code>M_ARENA_TEST</code>.</p>
<dt>
<dd> This parameter has been available since glibc 2.10 via <code>&#8211;enable-experimental-malloc</code>, and since glibc 2.15 by default. In some versions of the allocator there was no limit on the number of created arenas (e.g., CentOS 5, RHEL 5).</p>
<dt>
<dd> When employing newer glibc versions, applications may in some cases exhibit high contention when accessing arenas. In these cases, it may be beneficial to increase <code>M_ARENA_MAX</code> to match the number of threads. This is similar in behavior to strategies taken by tcmalloc and jemalloc (e.g., per-thread allocation pools).</p>
<dt><code>M_ARENA_TEST</code></p>
<dd> This parameter specifies a value, in number of arenas created, at which point the system configuration will be examined to determine a hard limit on the number of created arenas. (See <code>M_ARENA_MAX</code> for the definition of an arena.)</p>
<dt>
<dd> The computation of the arena hard limit is implementation-defined and is usually calculated as a multiple of the number of available CPUs. Once the hard limit is computed, the result is final and constrains the total number of arenas.</p>
<dt>
<dd> The default value for the <code>M_ARENA_TEST</code> parameter is 2 on systems where <i>sizeof(long)</i> is 4; otherwise the default value is 8.</p>
<dt>
<dd> This parameter has been available since glibc 2.10 via <code>&#8211;enable-experimental-malloc</code>, and since glibc 2.15 by default.</p>
<dt>
<dd> The value of <code>M_ARENA_TEST</code> is not used when <code>M_ARENA_MAX</code> has a nonzero value.</p>
<dt><code>M_CHECK_ACTION</code></p>
<dd> Setting this parameter controls how glibc responds when various kinds of programming errors are detected (e.g., freeing the same pointer twice). The 3 least significant bits (2, 1, and 0) of the value assigned to this parameter determine the glibc behavior, as follows:</p>
<dl>
<dt>
<dd>
<dl>
<dt>Bit 0</p>
<dd> If this bit is set, then print a one-line message on <i>stderr</i> that provides details about the error. The message starts with the string &quot;***&nbsp;glibc detected&nbsp;***&quot;, followed by the program name, the name of the memory-allocation function in which the error was detected, a brief description of the error, and the memory address where the error was detected.</p>
<dt>Bit 1</p>
<dd> If this bit is set, then, after printing any error message specified by bit 0, the program is terminated by calling <code><a href="/docs/linux/man/3-abort/">abort</a></code>(3). In glibc versions since 2.4, if bit 0 is also set, then, between printing the error message and aborting, the program also prints a stack trace in the manner of <code><a href="/docs/linux/man/3-backtrace/">backtrace</a></code>(3), and prints the process&#8217;s memory mapping in the style of <i>/proc/[pid]/maps</i> (see <code><a href="/docs/linux/man/5-proc/">proc</a></code>(5)).</p>
<dt>Bit 2 (since glibc 2.4)</p>
<dd> This bit has an effect only if bit 0 is also set. If this bit is set, then the one-line message describing the error is simplified to contain just the name of the function where the error was detected and the brief description of the error.</dl>
</dl>
<dt>
<dd> The remaining bits in <i>value</i> are ignored.</p>
<dt>
<dd> Combining the above details, the following numeric values are meaningful for <code>M_CHECK_ACTION</code>:</p>
<dl>
<dt>
<dd>
<dl>
<dt>0</p>
<dd> Ignore error conditions; continue execution (with undefined results).</p>
<dt>1</p>
<dd> Print a detailed error message and continue execution.</p>
<dt>2</p>
<dd> Abort the program.</p>
<dt>3</p>
<dd> Print detailed error message, stack trace, and memory mappings, and abort the program.</p>
<dt>5</p>
<dd> Print a simple error message and continue execution.</p>
<dt>7</p>
<dd> Print simple error message, stack trace, and memory mappings, and abort the program.</dl>
</dl>
<dt>
<dd> Since glibc 2.3.4, the default value for the <code>M_CHECK_ACTION</code> parameter is 3. In glibc version 2.3.3 and earlier, the default value is 1.</p>
<dt>
<dd> Using a nonzero <code>M_CHECK_ACTION</code> value can be useful because otherwise a crash may happen much later, and the true cause of the problem is then very hard to track down.</p>
<dt><code>M_MMAP_MAX</code></p>
<dd> This parameter specifies the maximum number of allocation requests that may be simultaneously serviced using <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2). This parameter exists because some systems have a limited number of internal tables for use by <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2), and using more than a few of them may degrade performance.</p>
<dt>
<dd> The default value is 65,536, a value which has no special significance and which serves only as a safeguard. Setting this parameter to 0 disables the use of <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2) for servicing large allocation requests.</p>
<dt><code>M_MMAP_THRESHOLD</code></p>
<dd> For allocations greater than or equal to the limit specified (in bytes) by <code>M_MMAP_THRESHOLD</code> that can&#8217;t be satisfied from the free list, the memory-allocation functions employ <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2) instead of increasing the program break using <code><a href="/docs/linux/man/2-sbrk/">sbrk</a></code>(2).</p>
<dt>
<dd> Allocating memory using <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2) has the significant advantage that the allocated memory blocks can always be independently released back to the system. (By contrast, the heap can be trimmed only if memory is freed at the top end.) On the other hand, there are some disadvantages to the use of <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2): deallocated space is not placed on the free list for reuse by later allocations; memory may be wasted because <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2) allocations must be page-aligned; and the kernel must perform the expensive task of zeroing out memory allocated via <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2). Balancing these factors leads to a default setting of 128*1024 for the <code>M_MMAP_THRESHOLD</code> parameter.</p>
<dt>
<dd> The lower limit for this parameter is 0. The upper limit is <code>DEFAULT_MMAP_THRESHOLD_MAX</code>: 512*1024 on 32-bit systems or <i>4*1024*1024*sizeof(long)</i> on 64-bit systems.</p>
<dt>
<dd> <i>Note:</i> Nowadays, glibc uses a dynamic mmap threshold by default. The initial value of the threshold is 128*1024, but when blocks larger than the current threshold and less than or equal to <code>DEFAULT_MMAP_THRESHOLD_MAX</code> are freed, the threshold is adjusted upward to the size of the freed block. When dynamic mmap thresholding is in effect, the threshold for trimming the heap is also dynamically adjusted to be twice the dynamic mmap threshold. Dynamic adjustment of the mmap threshold is disabled if any of the <code>M_TRIM_THRESHOLD</code>, <code>M_TOP_PAD</code>, <code>M_MMAP_THRESHOLD</code>, or <code>M_MMAP_MAX</code> parameters is set.</p>
<dt><code>M_MXFAST</code> (since glibc 2.3)</p>
<dd> Set the upper limit for memory allocation requests that are satisfied using &quot;fastbins&quot;. (The measurement unit for this parameter is bytes.) Fastbins are storage areas that hold deallocated blocks of memory of the same size without merging adjacent free blocks. Subsequent reallocation of blocks of the same size can be handled very quickly by allocating from the fastbin, although memory fragmentation and the overall memory footprint of the program can increase.</p>
<dt>
<dd> The default value for this parameter is <i>64*sizeof(size_t)/4</i> (i.e., 64 on 32-bit architectures). The range for this parameter is 0 to <i>80*sizeof(size_t)/4</i>. Setting <code>M_MXFAST</code> to 0 disables the use of fastbins.</p>
<dt><code>M_PERTURB</code> (since glibc 2.4)</p>
<dd> If this parameter is set to a nonzero value, then bytes of allocated memory (other than allocations via <code><a href="/docs/linux/man/3-calloc/">calloc</a></code>(3)) are initialized to the complement of the value in the least significant byte of <i>value</i>, and when allocated memory is released using <code><a href="/docs/linux/man/3-free/">free</a></code>(3), the freed bytes are set to the least significant byte of <i>value</i>. This can be useful for detecting errors where programs incorrectly rely on allocated memory being initialized to zero, or reuse values in memory that has already been freed.</p>
<dt>
<dd> The default value for this parameter is 0.</p>
<dt><code>M_TOP_PAD</code></p>
<dd> This parameter defines the amount of padding to employ when calling <code><a href="/docs/linux/man/2-sbrk/">sbrk</a></code>(2) to modify the program break. (The measurement unit for this parameter is bytes.) This parameter has an effect in the following circumstances:</p>
<dl>
<dt>
<dd>
<dl>
<dt>*</p>
<dd> When the program break is increased, then <code>M_TOP_PAD</code> bytes are added to the <code><a href="/docs/linux/man/2-sbrk/">sbrk</a></code>(2) request.</p>
<dt>*</p>
<dd> When the heap is trimmed as a consequence of calling <code><a href="/docs/linux/man/3-free/">free</a></code>(3) (see the discussion of <code>M_TRIM_THRESHOLD</code>) this much free space is preserved at the top of the heap.</dl>
</dl>
<dt>
<dd> In either case, the amount of padding is always rounded to a system page boundary.</p>
<dt>
<dd> Modifying <code>M_TOP_PAD</code> is a trade-off between increasing the number of system calls (when the parameter is set low) and wasting unused memory at the top of the heap (when the parameter is set high).</p>
<dt>
<dd> The default value for this parameter is 128*1024.</p>
<dt><code>M_TRIM_THRESHOLD</code></p>
<dd> When the amount of contiguous free memory at the top of the heap grows sufficiently large, <code><a href="/docs/linux/man/3-free/">free</a></code>(3) employs <code><a href="/docs/linux/man/2-sbrk/">sbrk</a></code>(2) to release this memory back to the system. (This can be useful in programs that continue to execute for a long period after freeing a significant amount of memory.) The <code>M_TRIM_THRESHOLD</code> parameter specifies the minimum size (in bytes) that this block of memory must reach before <code><a href="/docs/linux/man/2-sbrk/">sbrk</a></code>(2) is used to trim the heap.</p>
<dt>
<dd> The default value for this parameter is 128*1024. Setting <code>M_TRIM_THRESHOLD</code> to -1 disables trimming completely.</p>
<dt>
<dd> Modifying <code>M_TRIM_THRESHOLD</code> is a trade-off between increasing the number of system calls (when the parameter is set low) and wasting unused memory at the top of the heap (when the parameter is set high).</dl>
<h3>Environment variables</h3>
<p> A number of environment variables can be defined to modify some of the same parameters as are controlled by <code>mallopt</code>(). Using these variables has the advantage that the source code of the program need not be changed. To be effective, these variables must be defined before the first call to a memory-allocation function. (If the same parameters are adjusted via <code>mallopt</code>(), then the <code>mallopt</code>() settings take precedence.) For security reasons, these variables are ignored in set-user-ID and set-group-ID programs. </p>
<p> The environment variables are as follows (note the trailing underscore at the end of the name of some variables):</p>
<dl>
<dt><code>MALLOC_ARENA_MAX</code></p>
<dd> Controls the same parameter as <code>mallopt</code>() <code>M_ARENA_MAX</code>.</p>
<dt><code>MALLOC_ARENA_TEST</code></p>
<dd> Controls the same parameter as <code>mallopt</code>() <code>M_ARENA_TEST</code>.</p>
<dt><code>MALLOC_CHECK_</code></p>
<dd> This environment variable controls the same parameter as <code>mallopt</code>() <code>M_CHECK_ACTION</code>. If this variable is set to a nonzero value, then a special implementation of the memory-allocation functions is used. (This is accomplished using the <code><a href="/docs/linux/man/3-malloc_hook/">malloc_hook</a></code>(3) feature.) This implementation performs additional error checking, but is slower than the standard set of memory-allocation functions. (This implementation does not detect all possible errors; memory leaks can still occur.)</p>
<dt>
<dd> The value assigned to this environment variable should be a single digit, whose meaning is as described for <code>M_CHECK_ACTION</code>. Any characters beyond the initial digit are ignored.</p>
<dt>
<dd> For security reasons, the effect of <code>MALLOC_CHECK_</code> is disabled by default for set-user-ID and set-group-ID programs. However, if the file <i>/etc/suid-debug</i> exists (the content of the file is irrelevant), then <code>MALLOC_CHECK_</code> also has an effect for set-user-ID and set-group-ID programs.</p>
<dt><code>MALLOC_MMAP_MAX_</code></p>
<dd> Controls the same parameter as <code>mallopt</code>() <code>M_MMAP_MAX</code>.</p>
<dt><code>MALLOC_MMAP_THRESHOLD_</code></p>
<dd> Controls the same parameter as <code>mallopt</code>() <code>M_MMAP_THRESHOLD</code>.</p>
<dt><code>MALLOC_PERTURB_</code></p>
<dd> Controls the same parameter as <code>mallopt</code>() <code>M_PERTURB</code>.</p>
<dt><code>MALLOC_TRIM_THRESHOLD_</code></p>
<dd> Controls the same parameter as <code>mallopt</code>() <code>M_TRIM_THRESHOLD</code>.</p>
<dt><code>MALLOC_TOP_PAD_</code></p>
<dd> Controls the same parameter as <code>mallopt</code>() <code>M_TOP_PAD</code>.</dl>
<h2>RETURN VALUE</h2>
<p> On success, <code>mallopt</code>() returns 1. On error, it returns 0.</p>
<h2>ERRORS</h2>
<p> On error, <i>errno</i> is <i>not</i> set.</p>
<h2>CONFORMING TO</h2>
<p> This function is not specified by POSIX or the C standards. A similar function exists on many System V derivatives, but the range of values for <i>param</i> varies across systems. The SVID defined options <code>M_MXFAST</code>, <code>M_NLBLKS</code>, <code>M_GRAIN</code>, and <code>M_KEEP</code>, but only the first of these is implemented in glibc.</p>
<h2>BUGS</h2>
<p> Specifying an invalid value for <i>param</i> does not generate an error. </p>
<p> A calculation error within the glibc implementation means that a call of the form: </p>
<p> mallopt(M_MXFAST, n) </p>
<p> does not result in fastbins being employed for all allocations of size up to <i>n</i>. To ensure desired results, <i>n</i> should be rounded up to the next multiple greater than or equal to <i>(2k+1)*sizeof(size_t)</i>, where <i>k</i> is an integer. </p>
<p> If <code>mallopt</code>() is used to set <code>M_PERTURB</code>, then, as expected, the bytes of allocated memory are initialized to the complement of the byte in <i>value</i>, and when that memory is freed, the bytes of the region are initialized to the byte specified in <i>value</i>. However, there is an off-by-<i>sizeof(size_t)</i> error in the implementation: instead of initializing precisely the block of memory being freed by the call <i>free(p)</i>, the block starting at <i>p+sizeof(size_t)</i> is initialized.</p>
<h2>EXAMPLES</h2>
<p> The program below demonstrates the use of <code>M_CHECK_ACTION</code>. If the program is supplied with an (integer) command-line argument, then that argument is used to set the <code>M_CHECK_ACTION</code> parameter. The program then allocates a block of memory, and frees it twice (an error). </p>
<p> The following shell session shows what happens when we run this program under glibc, with the default value for <code>M_CHECK_ACTION</code>: </p>
<p> $ <code>./a.out</code> main(): returned from first free() call *** glibc detected *** ./a.out: double free or corruption (top): 0x09d30008 *** ======= Backtrace: ========= /lib/libc.so.6(+0x6c501)[0x523501] /lib/libc.so.6(+0x6dd70)[0x524d70] /lib/libc.so.6(cfree+0x6d)[0x527e5d] ./a.out[0x80485db] /lib/libc.so.6(__libc_start_main+0xe7)[0x4cdce7] ./a.out[0x8048471] ======= Memory map: ======== 001e4000-001fe000 r-xp 00000000 08:06 1083555 /lib/libgcc_s.so.1 001fe000-001ff000 r&#8211;p 00019000 08:06 1083555 /lib/libgcc_s.so.1 [some lines omitted] b7814000-b7817000 rw-p 00000000 00:00 0 bff53000-bff74000 rw-p 00000000 00:00 0 [stack] Aborted (core dumped) </p>
<p> The following runs show the results when employing other values for <code>M_CHECK_ACTION</code>: </p>
<p> $ <code>./a.out 1</code> # Diagnose error and continue main(): returned from first free() call *** glibc detected *** ./a.out: double free or corruption (top): 0x09cbe008 *** main(): returned from second free() call $ <code>./a.out 2</code> # Abort without error message main(): returned from first free() call Aborted (core dumped) $ <code>./a.out 0</code> # Ignore error and continue main(): returned from first free() call main(): returned from second free() call </p>
<p> The next run shows how to set the same parameter using the <code>MALLOC_CHECK_</code> environment variable: </p>
<p> $ <code>MALLOC_CHECK_=1 ./a.out</code> main(): returned from first free() call *** glibc detected *** ./a.out: free(): invalid pointer: 0x092c2008 *** main(): returned from second free() call</p>
<h3>Program source</h3>
<p> #include &lt;malloc.h&gt; #include &lt;stdio.h&gt; #include &lt;stdlib.h&gt; </p>
<p> int main(int argc, char *argv[]) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;*p; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(argc&nbsp;&gt;&nbsp;1)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(mallopt(M_CHECK_ACTION, atoi(argv[1]))&nbsp;!=&nbsp;1)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fprintf(stderr,&nbsp;&quot;mallopt()&nbsp;failed&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;}<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;p&nbsp;=&nbsp;malloc(1000);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(p&nbsp;==&nbsp;NULL)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fprintf(stderr,&nbsp;&quot;malloc()&nbsp;failed&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;free(p);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;main(): returned from first free()&nbsp;call
&quot;); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;free(p);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;main(): returned from second free()&nbsp;call
&quot;); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_SUCCESS); }</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2), <code><a href="/docs/linux/man/2-sbrk/">sbrk</a></code>(2), <code><a href="/docs/linux/man/3-mallinfo/">mallinfo</a></code>(3), <code><a href="/docs/linux/man/3-malloc/">malloc</a></code>(3), <code><a href="/docs/linux/man/3-malloc_hook/">malloc_hook</a></code>(3), <code><a href="/docs/linux/man/3-malloc_info/">malloc_info</a></code>(3), <code><a href="/docs/linux/man/3-malloc_stats/">malloc_stats</a></code>(3), <code><a href="/docs/linux/man/3-malloc_trim/">malloc_trim</a></code>(3), <code><a href="/docs/linux/man/3-mcheck/">mcheck</a></code>(3), <code><a href="/docs/linux/man/3-mtrace/">mtrace</a></code>(3), <code><a href="/docs/linux/man/3-posix_memalign/">posix_memalign</a></code>(3)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
