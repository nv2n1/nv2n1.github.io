---
title: "edata(3)"
name: "edata"
section: "3"
letter: "e"
url: "/docs/linux/man/3-edata/"
description: "etext, edata, end – end of program segments"
---

<h2 class="name">NAME</h2>
<p> etext, edata, end &#8211; end of program segments </p>
<h2>SYNOPSIS</h2>
<pre>
<code>extern</code><i> etext</i><code>;</code>
<code>extern</code><i> edata</i><code>;</code>
<code>extern</code><i> end</i><code>;</code>
</pre>
<h2>DESCRIPTION</h2>
<p> The addresses of these symbols indicate the end of various program segments:</p>
<dl>
<dt><i>etext</i></p>
<dd> This is the first address past the end of the text segment (the program code).</p>
<dt><i>edata</i></p>
<dd> This is the first address past the end of the initialized data segment.</p>
<dt><i>end</i></p>
<dd> This is the first address past the end of the uninitialized data segment (also known as the BSS segment).</dl>
<h2>CONFORMING TO</h2>
<p> Although these symbols have long been provided on most UNIX systems, they are not standardized; use with caution.</p>
<h2>NOTES</h2>
<p> The program must explicitly declare these symbols; they are not defined in any header file. </p>
<p> On some systems the names of these symbols are preceded by underscores, thus: <i>_etext</i>, <i>_edata</i>, and <i>_end</i>. These symbols are also defined for programs compiled on Linux. </p>
<p> At the start of program execution, the program break will be somewhere near <i>&amp;end</i> (perhaps at the start of the following page). However, the break will change as memory is allocated via <code><a href="/docs/linux/man/2-brk/">brk</a></code>(2) or <code><a href="/docs/linux/man/3-malloc/">malloc</a></code>(3). Use <code><a href="/docs/linux/man/2-sbrk/">sbrk</a></code>(2) with an argument of zero to find the current value of the program break.</p>
<h2>EXAMPLES</h2>
<p> When run, the program below produces output such as the following: </p>
<p> $<code> ./a.out</code> First address past:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;program text&nbsp;(etext)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0x8048568<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;initialized data&nbsp;(edata)&nbsp;<wbr>&nbsp;<wbr>&nbsp;0x804a01c<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uninitialized data&nbsp;(end)&nbsp;<wbr>&nbsp;<wbr>&nbsp;0x804a024</p>
<h3>Program source</h3>
<p> #include &lt;stdio.h&gt; #include &lt;stdlib.h&gt; </p>
<p> extern char etext, edata, end; /* The symbols must have some type,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;or&nbsp;&quot;gcc -Wall&quot;&nbsp;complains&nbsp;*/ </p>
<p> int main(int argc, char *argv[]) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;First address past:
&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;program text&nbsp;(etext)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;%10p
&quot;,&nbsp;&amp;etext);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;initialized data&nbsp;(edata)&nbsp;<wbr>&nbsp;%10p
&quot;,&nbsp;&amp;edata);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uninitialized data&nbsp;(end)&nbsp;<wbr>&nbsp;%10p
&quot;,&nbsp;&amp;end); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_SUCCESS); }</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-objdump/">objdump</a></code>(1), <code><a href="/docs/linux/man/1-readelf/">readelf</a></code>(1), <code><a href="/docs/linux/man/2-sbrk/">sbrk</a></code>(2), <code><a href="/docs/linux/man/5-elf/">elf</a></code>(5)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
