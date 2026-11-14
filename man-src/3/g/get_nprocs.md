---
title: "get_nprocs(3)"
name: "get_nprocs"
section: "3"
letter: "g"
url: "/docs/linux/man/3-get_nprocs/"
description: "get_nprocs, get_nprocs_conf – get number of processors"
---

<h2 class="name">NAME</h2>
<p> get_nprocs, get_nprocs_conf &#8211; get number of processors </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;sys/sysinfo.h&gt;</code> </p>
<p> <code>int get_nprocs(void);</code><br />
 <code>int get_nprocs_conf(void);</code></p>
<h2>DESCRIPTION</h2>
<p> The function <code>get_nprocs_conf</code>() returns the number of processors configured by the operating system. </p>
<p> The function <code>get_nprocs</code>() returns the number of processors currently available in the system. This may be less than the number returned by <code>get_nprocs_conf</code>() because processors may be offline (e.g., on hotpluggable systems).</p>
<h2>RETURN VALUE</h2>
<p> As given in DESCRIPTION.</p>
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
<td> <code>get_nprocs</code>(),<br />
 <code>get_nprocs_conf</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> These functions are GNU extensions.</p>
<h2>NOTES</h2>
<p> The current implementation of these functions is rather expensive, since they open and parse files in the <i>/sys</i> filesystem each time they are called. </p>
<p> The following <code><a href="/docs/linux/man/3-sysconf/">sysconf</a></code>(3) calls make use of the functions documented on this page to return the same information. </p>
<p> np = sysconf(_SC_NPROCESSORS_CONF); /* processors configured */ np = sysconf(_SC_NPROCESSORS_ONLN); /* processors available */</p>
<h2>EXAMPLES</h2>
<p> The following example shows how <code>get_nprocs</code>() and <code>get_nprocs_conf</code>() can be used. </p>
<p> #include &lt;stdlib.h&gt; #include &lt;stdio.h&gt; #include &lt;sys/sysinfo.h&gt; </p>
<p> int main(int argc, char *argv[]) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;This system has&nbsp;%d processors configured and&nbsp;&quot;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&quot;%d processors available.
&quot;,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;get_nprocs_conf(), get_nprocs());<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_SUCCESS); }</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-nproc/">nproc</a></code>(1)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
