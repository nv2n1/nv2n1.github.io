---
title: "memusage(1)"
name: "memusage"
section: "1"
letter: "m"
url: "/docs/linux/man/1-memusage/"
description: "memusage – profile memory usage of a program"
---

<h2 class="name">NAME</h2>
<p> memusage &#8211; profile memory usage of a program </p>
<h2>SYNOPSIS</h2>
<p> <code>memusage</code> [<i>option</i>]&#8230; <i>program</i> [<i>programoption</i>]&#8230;</p>
<h2>DESCRIPTION</h2>
<p> <code>memusage</code> is a bash script which profiles memory usage of the program, <i>program</i>. It preloads the <code>libmemusage.so</code> library into the caller&#8217;s environment (via the <code>LD_PRELOAD</code> environment variable; see <code><a href="/docs/linux/man/8-ld-so/">ld.so</a></code>(8)). The <code>libmemusage.so</code> library traces memory allocation by intercepting calls to <code><a href="/docs/linux/man/3-malloc/">malloc</a></code>(3), <code><a href="/docs/linux/man/3-calloc/">calloc</a></code>(3), <code><a href="/docs/linux/man/3-free/">free</a></code>(3), and <code><a href="/docs/linux/man/3-realloc/">realloc</a></code>(3); optionally, calls to <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2), <code><a href="/docs/linux/man/2-mremap/">mremap</a></code>(2), and <code><a href="/docs/linux/man/2-munmap/">munmap</a></code>(2) can also be intercepted. </p>
<p> <code>memusage</code> can output the collected data in textual form, or it can use <code><a href="/docs/linux/man/1-memusagestat/">memusagestat</a></code>(1) (see the <code>-p</code> option, below) to create a PNG file containing graphical representation of the collected data.</p>
<h3>Memory usage summary</h3>
<p> The &quot;Memory usage summary&quot; line output by <code>memusage</code> contains three fields:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>heap total</code></p>
<dd> Sum of <i>size</i> arguments of all <code><a href="/docs/linux/man/3-malloc/">malloc</a></code>(3) calls, products of arguments (<i>nmemb</i>*<i>size</i>) of all <code><a href="/docs/linux/man/3-calloc/">calloc</a></code>(3) calls, and sum of <i>length</i> arguments of all <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2) calls. In the case of <code><a href="/docs/linux/man/3-realloc/">realloc</a></code>(3) and <code><a href="/docs/linux/man/2-mremap/">mremap</a></code>(2), if the new size of an allocation is larger than the previous size, the sum of all such differences (new size minus old size) is added.</p>
<dt><code>heap peak</code></p>
<dd> Maximum of all <i>size</i> arguments of <code><a href="/docs/linux/man/3-malloc/">malloc</a></code>(3), all products of <i>nmemb</i>*<i>size</i> of <code><a href="/docs/linux/man/3-calloc/">calloc</a></code>(3), all <i>size</i> arguments of <code><a href="/docs/linux/man/3-realloc/">realloc</a></code>(3), <i>length</i> arguments of <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2), and <i>new_size</i> arguments of <code><a href="/docs/linux/man/2-mremap/">mremap</a></code>(2).</p>
<dt><code>stack peak</code></p>
<dd> Before the first call to any monitored function, the stack pointer address (base stack pointer) is saved. After each function call, the actual stack pointer address is read and the difference from the base stack pointer computed. The maximum of these differences is then the stack peak.</dl>
</dl>
<p> Immediately following this summary line, a table shows the number calls, total memory allocated or deallocated, and number of failed calls for each intercepted function. For <code><a href="/docs/linux/man/3-realloc/">realloc</a></code>(3) and <code><a href="/docs/linux/man/2-mremap/">mremap</a></code>(2), the additional field &quot;nomove&quot; shows reallocations that changed the address of a block, and the additional &quot;dec&quot; field shows reallocations that decreased the size of the block. For <code><a href="/docs/linux/man/3-realloc/">realloc</a></code>(3), the additional field &quot;free&quot; shows reallocations that caused a block to be freed (i.e., the reallocated size was 0). </p>
<p> The &quot;realloc/total memory&quot; of the table output by <code>memusage</code> does not reflect cases where <code><a href="/docs/linux/man/3-realloc/">realloc</a></code>(3) is used to reallocate a block of memory to have a smaller size than previously. This can cause sum of all &quot;total memory&quot; cells (excluding &quot;free&quot;) to be larger than the &quot;free/total memory&quot; cell.</p>
<h3>Histogram for block sizes</h3>
<p> The &quot;Histogram for block sizes&quot; provides a breakdown of memory allocations into various bucket sizes.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-n&nbsp;</code><i>name</i>,&nbsp;<code>&#8211;progname=</code><i>name</i></p>
<dd> Name of the program file to profile.</p>
<dt><code>-p&nbsp;</code><i>file</i>,&nbsp;<code>&#8211;png=</code><i>file</i></p>
<dd> Generate PNG graphic and store it in <i>file</i>.</p>
<dt><code>-d&nbsp;</code><i>file</i>,&nbsp;<code>&#8211;data=</code><i>file</i></p>
<dd> Generate binary data file and store it in <i>file</i>.</p>
<dt><code>-u</code>,&nbsp;<code>&#8211;unbuffered</code></p>
<dd> Do not buffer output.</p>
<dt><code>-b&nbsp;</code><i>size</i>,&nbsp;<code>&#8211;buffer=</code><i>size</i></p>
<dd> Collect <i>size</i> entries before writing them out.</p>
<dt><code>&#8211;no-timer</code></p>
<dd> Disable timer-based (<code>SIGPROF</code>) sampling of stack pointer value.</p>
<dt><code>-m</code>,&nbsp;<code>&#8211;mmap</code></p>
<dd> Also trace <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2), <code><a href="/docs/linux/man/2-mremap/">mremap</a></code>(2), and <code><a href="/docs/linux/man/2-munmap/">munmap</a></code>(2).</p>
<dt><code>-?</code>,&nbsp;<code>&#8211;help</code></p>
<dd> Print help and exit.</p>
<dt><code>&#8211;usage</code></p>
<dd> Print a short usage message and exit.</p>
<dt><code>-V</code>,&nbsp;<code>&#8211;version</code></p>
<dd> Print version information and exit.</p>
<dt>The following options apply only when generating graphical output:</p>
<dd>
<dt><code>-t</code>,&nbsp;<code>&#8211;time-based</code></p>
<dd> Use time (rather than number of function calls) as the scale for the X axis.</p>
<dt><code>-T</code>,&nbsp;<code>&#8211;total</code></p>
<dd> Also draw a graph of total memory use.</p>
<dt><code>&#8211;title=</code><i>name</i></p>
<dd> Use <i>name</i> as the title of the graph.</p>
<dt><code>-x&nbsp;</code><i>size</i>,&nbsp;<code>&#8211;x-size=</code><i>size</i></p>
<dd> Make the graph <i>size</i> pixels wide.</p>
<dt><code>-y&nbsp;</code><i>size</i>,&nbsp;<code>&#8211;y-size=</code><i>size</i></p>
<dd> Make the graph <i>size</i> pixels high.</dl>
<h2>EXIT STATUS</h2>
<p> Exit status is equal to the exit status of profiled program.</p>
<h2>BUGS</h2>
<p> To report bugs, see</p>
<h2>EXAMPLES</h2>
<p> Below is a simple program that reallocates a block of memory in cycles that rise to a peak before then cyclically reallocating the memory in smaller blocks that return to zero. After compiling the program and running the following commands, a graph of the memory usage of the program can be found in the file <i>memusage.png</i>: </p>
<p> $ <code>memusage &#8211;data=memusage.dat ./a.out</code> &#8230; Memory usage summary: heap total: 45200, heap peak: 6440, stack peak: 224<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;total calls&nbsp;<wbr>&nbsp;total memory&nbsp;<wbr>&nbsp;failed calls<br />
&nbsp;malloc|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;1&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;400&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0 realloc| 40 44800 0 (nomove:40, dec:19, free:0)<br />
&nbsp;calloc|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;free|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;1&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;440 Histogram for block sizes:<br />
&nbsp;<wbr>&nbsp;192-207&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;1&nbsp;<wbr>&nbsp;<wbr>&nbsp;2%&nbsp;================ &#8230;<br />
&nbsp;2192-2207&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;1&nbsp;<wbr>&nbsp;<wbr>&nbsp;2%&nbsp;================<br />
&nbsp;2240-2255&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;2&nbsp;<wbr>&nbsp;<wbr>&nbsp;4%&nbsp;=================================<br />
&nbsp;2832-2847&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;2&nbsp;<wbr>&nbsp;<wbr>&nbsp;4%&nbsp;=================================<br />
&nbsp;3440-3455&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;2&nbsp;<wbr>&nbsp;<wbr>&nbsp;4%&nbsp;=================================<br />
&nbsp;4032-4047&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;2&nbsp;<wbr>&nbsp;<wbr>&nbsp;4%&nbsp;=================================<br />
&nbsp;4640-4655&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;2&nbsp;<wbr>&nbsp;<wbr>&nbsp;4%&nbsp;=================================<br />
&nbsp;5232-5247&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;2&nbsp;<wbr>&nbsp;<wbr>&nbsp;4%&nbsp;=================================<br />
&nbsp;5840-5855&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;2&nbsp;<wbr>&nbsp;<wbr>&nbsp;4%&nbsp;=================================<br />
&nbsp;6432-6447&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;1&nbsp;<wbr>&nbsp;<wbr>&nbsp;2%&nbsp;================ $ <code>memusagestat memusage.dat memusage.png</code></p>
<h3>Program source</h3>
<p> #include &lt;stdio.h&gt; #include &lt;stdlib.h&gt; </p>
<p> #define CYCLES 20 </p>
<p> int main(int argc, char *argv[]) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int i, j;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;size_t size;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int&nbsp;*p; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;size&nbsp;=&nbsp;sizeof(*p)&nbsp;*&nbsp;100;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;malloc:&nbsp;%zu
&quot;, size);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;p&nbsp;=&nbsp;malloc(size); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;for&nbsp;(i&nbsp;=&nbsp;0;&nbsp;i&nbsp;&lt;&nbsp;CYCLES;&nbsp;i++)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(i&nbsp;&lt;&nbsp;CYCLES&nbsp;/&nbsp;2)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;j&nbsp;=&nbsp;i;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;else<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;j&#8211;; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;size&nbsp;=&nbsp;sizeof(*p)&nbsp;*&nbsp;(j&nbsp;*&nbsp;50&nbsp;+&nbsp;110);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;realloc:&nbsp;%zu
&quot;, size);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;p&nbsp;=&nbsp;realloc(p, size); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;size&nbsp;=&nbsp;sizeof(*p)&nbsp;*&nbsp;((j&nbsp;+&nbsp;1)&nbsp;*&nbsp;150&nbsp;+&nbsp;110);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;realloc:&nbsp;%zu
&quot;, size);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;p&nbsp;=&nbsp;realloc(p, size);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;free(p);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_SUCCESS); }</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-memusagestat/">memusagestat</a></code>(1), <code><a href="/docs/linux/man/1-mtrace/">mtrace</a></code>(1), <code><a href="/docs/linux/man/8-ld-so/">ld.so</a></code>(8)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
