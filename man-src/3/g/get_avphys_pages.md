---
title: "get_avphys_pages(3)"
name: "get_avphys_pages"
section: "3"
letter: "g"
url: "/docs/linux/man/3-get_avphys_pages/"
description: "get_phys_pages, get_avphys_pages – get total and available physical page counts"
---

<h2 class="name">NAME</h2>
<p> get_phys_pages, get_avphys_pages &#8211; get total and available physical page counts </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;sys/sysinfo.h&gt;
long get_phys_pages(void);
long get_avphys_pages(void);
</code></pre>
<h2>DESCRIPTION</h2>
<p> The function <code>get_phys_pages</code>() returns the total number of physical pages of memory available on the system. </p>
<p> The function <code>get_avphys_pages</code>() returns the number of currently available physical pages of memory on the system.</p>
<h2>RETURN VALUE</h2>
<p> On success, these functions return a nonnegative value as given in DESCRIPTION. On failure, they return -1 and set <i>errno</i> to indicate the cause of the error.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>ENOSYS</code></p>
<dd> The system could not provide the required information (possibly because the <i>/proc</i> filesystem was not mounted).</dl>
<h2>CONFORMING TO</h2>
<p> These functions are GNU extensions.</p>
<h2>NOTES</h2>
<p> These functions obtain the required information by scanning the <i>MemTotal</i> and <i>MemFree</i> fields of <i>/proc/meminfo</i>. </p>
<p> The following <code><a href="/docs/linux/man/3-sysconf/">sysconf</a></code>(3) calls provide a portable means of obtaining the same information as the functions described on this page. </p>
<p> total_pages = sysconf(_SC_PHYS_PAGES); /* total pages */ avl_pages = sysconf(_SC_AVPHYS_PAGES); /* available pages */</p>
<h2>EXAMPLES</h2>
<p> The following example shows how <code>get_phys_pages</code>() and <code>get_avphys_pages</code>() can be used. </p>
<p> #include &lt;stdio.h&gt; #include &lt;stdlib.h&gt; #include &lt;sys/sysinfo.h&gt; </p>
<p> int main(int argc, char *argv[]) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;This system has&nbsp;%ld pages of physical memory and&nbsp;&quot;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&quot;%ld pages of physical memory available.
&quot;,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;get_phys_pages(), get_avphys_pages());<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_SUCCESS); }</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-sysconf/">sysconf</a></code>(3)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
