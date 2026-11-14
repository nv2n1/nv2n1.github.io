---
title: "mallinfo(3)"
name: "mallinfo"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mallinfo/"
description: "mallinfo – obtain memory allocation information"
---

<h2 class="name">NAME</h2>
<p> mallinfo &#8211; obtain memory allocation information </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;malloc.h&gt;</code> </p>
<p> <code>struct mallinfo mallinfo(void);</code></p>
<h2>DESCRIPTION</h2>
<p> The <code>mallinfo</code>() function returns a copy of a structure containing information about memory allocations performed by <code><a href="/docs/linux/man/3-malloc/">malloc</a></code>(3) and related functions. </p>
<p> Note that not all allocations are visible to <code>mallinfo</code>(); see BUGS and consider using <code><a href="/docs/linux/man/3-malloc_info/">malloc_info</a></code>(3) instead. </p>
<p> The returned structure is defined as follows: </p>
<p> struct mallinfo {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int arena;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Non-mmapped space allocated&nbsp;(bytes)&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int ordblks;&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Number of free chunks&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int smblks;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Number of free fastbin blocks&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int hblks;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Number of mmapped regions&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int hblkhd;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Space allocated in mmapped regions&nbsp;(bytes)&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int usmblks;&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;See below&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int fsmblks;&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Space in freed fastbin blocks&nbsp;(bytes)&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int uordblks;&nbsp;<wbr>&nbsp;/*&nbsp;Total allocated space&nbsp;(bytes)&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int fordblks;&nbsp;<wbr>&nbsp;/*&nbsp;Total free space&nbsp;(bytes)&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int keepcost;&nbsp;<wbr>&nbsp;/*&nbsp;Top-most, releasable space&nbsp;(bytes)&nbsp;*/ }; </p>
<p> The fields of the <i>mallinfo</i> structure contain the following information:</p>
<dl>
<dt><i>arena</i></p>
<dd> The total amount of memory allocated by means other than <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2) (i.e., memory allocated on the heap). This figure includes both in-use blocks and blocks on the free list.</p>
<dt><i>ordblks</i></p>
<dd> The number of ordinary (i.e., non-fastbin) free blocks.</p>
<dt><i>smblks</i></p>
<dd> The number of fastbin free blocks (see <code><a href="/docs/linux/man/3-mallopt/">mallopt</a></code>(3)).</p>
<dt><i>hblks</i></p>
<dd> The number of blocks currently allocated using <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2). (See the discussion of <code>M_MMAP_THRESHOLD</code> in <code><a href="/docs/linux/man/3-mallopt/">mallopt</a></code>(3).)</p>
<dt><i>hblkhd</i></p>
<dd> The number of bytes in blocks currently allocated using <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2).</p>
<dt><i>usmblks</i></p>
<dd> This field is unused, and is always 0. Historically, it was the &quot;highwater mark&quot; for allocated space&#8212;that is, the maximum amount of space that was ever allocated (in bytes); this field was maintained only in nonthreading environments.</p>
<dt><i>fsmblks</i></p>
<dd> The total number of bytes in fastbin free blocks.</p>
<dt><i>uordblks</i></p>
<dd> The total number of bytes used by in-use allocations.</p>
<dt><i>fordblks</i></p>
<dd> The total number of bytes in free blocks.</p>
<dt><i>keepcost</i></p>
<dd> The total amount of releasable free space at the top of the heap. This is the maximum number of bytes that could ideally (i.e., ignoring page alignment restrictions, and so on) be released by <code><a href="/docs/linux/man/3-malloc_trim/">malloc_trim</a></code>(3).</dl>
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
<td> <code>mallinfo</code>() </td>
<td>Thread safety</td>
<td>MT-Unsafe init const:mallopt
</td>
</tr>
</table>
<p> <code>mallinfo</code>() would access some global internal objects. If modify them with non-atomically, may get inconsistent results. The identifier <i>mallopt</i> in <i>const:mallopt</i> mean that <code>mallopt</code>() would modify the global internal objects with atomics, that make sure <code>mallinfo</code>() is safe enough, others modify with non-atomically maybe not.</p>
<h2>CONFORMING TO</h2>
<p> This function is not specified by POSIX or the C standards. A similar function exists on many System V derivatives, and was specified in the SVID.</p>
<h2>BUGS</h2>
<p> <code>Information is returned for only the main memory allocation area.</code> Allocations in other arenas are excluded. See <code><a href="/docs/linux/man/3-malloc_stats/">malloc_stats</a></code>(3) and <code><a href="/docs/linux/man/3-malloc_info/">malloc_info</a></code>(3) for alternatives that include information about other arenas. </p>
<p> The fields of the <i>mallinfo</i> structure are typed as <i>int</i>. However, because some internal bookkeeping values may be of type <i>long</i>, the reported values may wrap around zero and thus be inaccurate.</p>
<h2>EXAMPLES</h2>
<p> The program below employs <code>mallinfo</code>() to retrieve memory allocation statistics before and after allocating and freeing some blocks of memory. The statistics are displayed on standard output. </p>
<p> The first two command-line arguments specify the number and size of blocks to be allocated with <code><a href="/docs/linux/man/3-malloc/">malloc</a></code>(3). </p>
<p> The remaining three arguments specify which of the allocated blocks should be freed with <code><a href="/docs/linux/man/3-free/">free</a></code>(3). These three arguments are optional, and specify (in order): the step size to be used in the loop that frees blocks (the default is 1, meaning free all blocks in the range); the ordinal position of the first block to be freed (default 0, meaning the first allocated block); and a number one greater than the ordinal position of the last block to be freed (default is one greater than the maximum block number). If these three arguments are omitted, then the defaults cause all allocated blocks to be freed. </p>
<p> In the following example run of the program, 1000 allocations of 100 bytes are performed, and then every second allocated block is freed: </p>
<p> $ <code>./a.out 1000 100 2</code> ============== Before allocating blocks ============== Total non-mmapped bytes (arena): 0 # of free chunks (ordblks): 1 # of free fastbin blocks (smblks): 0 # of mapped regions (hblks): 0 Bytes in mapped regions (hblkhd): 0 Max. total allocated space (usmblks): 0 Free bytes held in fastbins (fsmblks): 0 Total allocated space (uordblks): 0 Total free space (fordblks): 0 Topmost releasable block (keepcost): 0 </p>
<p> ============== After allocating blocks ============== Total non-mmapped bytes (arena): 135168 # of free chunks (ordblks): 1 # of free fastbin blocks (smblks): 0 # of mapped regions (hblks): 0 Bytes in mapped regions (hblkhd): 0 Max. total allocated space (usmblks): 0 Free bytes held in fastbins (fsmblks): 0 Total allocated space (uordblks): 104000 Total free space (fordblks): 31168 Topmost releasable block (keepcost): 31168 </p>
<p> ============== After freeing blocks ============== Total non-mmapped bytes (arena): 135168 # of free chunks (ordblks): 501 # of free fastbin blocks (smblks): 0 # of mapped regions (hblks): 0 Bytes in mapped regions (hblkhd): 0 Max. total allocated space (usmblks): 0 Free bytes held in fastbins (fsmblks): 0 Total allocated space (uordblks): 52000 Total free space (fordblks): 83168 Topmost releasable block (keepcost): 31168</p>
<h3>Program source</h3>
<p> #include &lt;malloc.h&gt; #include &lt;stdlib.h&gt; #include &lt;string.h&gt; </p>
<p> static void display_mallinfo(void) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct mallinfo mi; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;mi&nbsp;=&nbsp;mallinfo(); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;Total non-mmapped bytes&nbsp;(arena):&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;%d
&quot;, mi.arena);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;#&nbsp;of free chunks&nbsp;(ordblks):&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;%d
&quot;, mi.ordblks);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;#&nbsp;of free fastbin blocks&nbsp;(smblks):&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;%d
&quot;, mi.smblks);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;#&nbsp;of mapped regions&nbsp;(hblks):&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;%d
&quot;, mi.hblks);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;Bytes in mapped regions&nbsp;(hblkhd):&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;%d
&quot;, mi.hblkhd);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;Max. total allocated space&nbsp;(usmblks):&nbsp;<wbr>&nbsp;%d
&quot;, mi.usmblks);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;Free bytes held in fastbins&nbsp;(fsmblks):&nbsp;%d
&quot;, mi.fsmblks);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;Total allocated space&nbsp;(uordblks):&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;%d
&quot;, mi.uordblks);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;Total free space&nbsp;(fordblks):&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;%d
&quot;, mi.fordblks);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;Topmost releasable block&nbsp;(keepcost):&nbsp;<wbr>&nbsp;<wbr>&nbsp;%d
&quot;, mi.keepcost); } </p>
<p> int main(int argc, char *argv[]) { #define MAX_ALLOCS 2000000<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;*alloc[MAX_ALLOCS];<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int numBlocks, freeBegin, freeEnd, freeStep;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;size_t blockSize; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(argc&nbsp;&lt;&nbsp;3 || strcmp(argv[1],&nbsp;&quot;&#8211;help&quot;)&nbsp;==&nbsp;0)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fprintf(stderr,&nbsp;&quot;%s num-blocks block-size&nbsp;[free-step&nbsp;&quot;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&quot;[start-free&nbsp;[end-free]]]
&quot;, argv[0]);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;numBlocks&nbsp;=&nbsp;atoi(argv[1]);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;blockSize&nbsp;=&nbsp;atoi(argv[2]);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;freeStep&nbsp;=&nbsp;(argc&nbsp;&gt;&nbsp;3)&nbsp;?&nbsp;atoi(argv[3])&nbsp;: 1;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;freeBegin&nbsp;=&nbsp;(argc&nbsp;&gt;&nbsp;4)&nbsp;?&nbsp;atoi(argv[4])&nbsp;: 0;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;freeEnd&nbsp;=&nbsp;(argc&nbsp;&gt;&nbsp;5)&nbsp;?&nbsp;atoi(argv[5])&nbsp;: numBlocks; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;==============&nbsp;Before allocating blocks&nbsp;==============
&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;display_mallinfo(); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;for&nbsp;(int j&nbsp;=&nbsp;0;&nbsp;j&nbsp;&lt;&nbsp;numBlocks;&nbsp;j++)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(numBlocks&nbsp;&gt;=&nbsp;MAX_ALLOCS)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fprintf(stderr,&nbsp;&quot;Too many allocations
&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;alloc[j]&nbsp;=&nbsp;malloc(blockSize);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(alloc[j]&nbsp;==&nbsp;NULL)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;perror(&quot;malloc&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;}<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;
==============&nbsp;After allocating blocks&nbsp;==============
&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;display_mallinfo(); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;for&nbsp;(int j&nbsp;=&nbsp;freeBegin;&nbsp;j&nbsp;&lt;&nbsp;freeEnd;&nbsp;j&nbsp;+=&nbsp;freeStep)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;free(alloc[j]); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;
==============&nbsp;After freeing blocks&nbsp;==============
&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;display_mallinfo(); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_SUCCESS); }</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2), <code><a href="/docs/linux/man/3-malloc/">malloc</a></code>(3), <code><a href="/docs/linux/man/3-malloc_info/">malloc_info</a></code>(3), <code><a href="/docs/linux/man/3-malloc_stats/">malloc_stats</a></code>(3), <code><a href="/docs/linux/man/3-malloc_trim/">malloc_trim</a></code>(3), <code><a href="/docs/linux/man/3-mallopt/">mallopt</a></code>(3)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
