---
title: "ttyslot(3)"
name: "ttyslot"
section: "3"
letter: "t"
url: "/docs/linux/man/3-ttyslot/"
description: "ttyslot – find the slot of the current user’s terminal in some file"
---

<p>ttyslot &#8211; find the slot of the current user&#8217;s terminal in some file</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;unistd.h&gt;       /See NOTES */
int ttyslot(void);</code></pre>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): <code>ttyslot</code>():</p>
<dl>
<dd>Since glibc 2.24:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;_DEFAULT_SOURCE<br />
 From glibc 2.20 to 2.23:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;_DEFAULT_SOURCE ||<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;_XOPEN_SOURCE&nbsp;&amp;&amp;&nbsp;_XOPEN_SOURCE&nbsp;&lt;&nbsp;500<br />
 Glibc 2.19 and earlier:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;_BSD_SOURCE ||<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;_XOPEN_SOURCE&nbsp;&amp;&amp;&nbsp;_XOPEN_SOURCE&nbsp;&lt;&nbsp;500</dl>
<h2>Description</h2>
<p>The legacy function <code>ttyslot</code>() returns the index of the current user&#8217;s entry in some file. </p>
<p> Now &quot;What file?&quot; you ask. Well, let&#8217;s first look at some history.</p>
<h3>Ancient history</h3>
<p>There used to be a file <i>/etc/ttys</i> in UNIX V6, that was read by the <code><a href="/docs/linux/man/1-init/">init</a></code>(1) program to find out what to do with each terminal line. Each line consisted of three characters. The first character was either &#8216;0&#8217; or &#8216;1&#8217;, where &#8216;0&#8217; meant &quot;ignore&quot;. The second character denoted the terminal: &#8216;8&#8217; stood for &quot;/dev/tty8&quot;. The third character was an argument to <code><a href="/docs/linux/man/8-getty/">getty</a></code>(8) indicating the sequence of line speeds to try (&#8216;-&#8216; was: start trying 110 baud). Thus a typical line was &quot;18-&quot;. A hang on some line was solved by changing the &#8216;1&#8217; to a &#8216;0&#8217;, signaling init, changing back again, and signaling init again. </p>
<p> In UNIX V7 the format was changed: here the second character was the argument to <code><a href="/docs/linux/man/8-getty/">getty</a></code>(8) indicating the sequence of line speeds to try (&#8216;0&#8217; was: cycle through 300-1200-150-110 baud; &#8216;4&#8217; was for the on-line console DECwriter) while the rest of the line contained the name of the tty. Thus a typical line was &quot;14console&quot;. </p>
<p> Later systems have more elaborate syntax. System V-like systems have <i>/etc/inittab</i> instead.</p>
<h3>Ancient history (2)</h3>
<p>On the other hand, there is the file <i>/etc/utmp</i> listing the people currently logged in. It is maintained by <code><a href="/docs/linux/man/1-login/">login</a></code>(1). It has a fixed size, and the appropriate index in the file was determined by <code><a href="/docs/linux/man/1-login/">login</a></code>(1) using the <code>ttyslot</code>() call to find the number of the line in <i>/etc/ttys</i> (counting from 1).</p>
<h3>The semantics of ttyslot</h3>
<p>Thus, the function <code>ttyslot</code>() returns the index of the controlling terminal of the calling process in the file <i>/etc/ttys</i>, and that is (usually) the same as the index of the entry for the current user in the file <i>/etc/utmp</i>. BSD still has the <i>/etc/ttys</i> file, but System V-like systems do not, and hence cannot refer to it. Thus, on such systems the documentation says that <code>ttyslot</code>() returns the current user&#8217;s index in the user accounting data base.</p>
<h2>Return Value</h2>
<p>If successful, this function returns the slot number. On error (e.g., if none of the file descriptors 0, 1 or 2 is associated with a terminal that occurs in this data base) it returns 0 on UNIX V6 and V7 and BSD-like systems, but -1 on System V-like systems.</p>
<h2>Attributes</h2>
<p>For an explanation of the terms used in this section, see <code><a href="/docs/linux/man/7-attributes/">attributes</a></code>(7). </p>
<table BORDER>
<tr VALIGN=top>
<td><code>Interface</code></td>
<td><code>Attribute</code></td>
<td><code>Value</code>
</td>
</tr>
<tr VALIGN=top>
<td> <code>ttyslot</code>() </td>
<td>Thread safety</td>
<td>MT-Unsafe
</td>
</tr>
</table>
<h2>Conforming To</h2>
<p>SUSv1; marked as LEGACY in SUSv2; removed in POSIX.1-2001. SUSv2 requires -1 on error.</p>
<h2>Notes</h2>
<p>The utmp file is found in various places on various systems, such as <i>/etc/utmp</i>, <i>/var/adm/utmp</i>, <i>/var/run/utmp</i>. </p>
<p> The glibc2 implementation of this function reads the file <code>_PATH_TTYS</code>, defined in <i>&lt;ttyent.h&gt;</i> as &quot;/etc/ttys&quot;. It returns 0 on error. Since Linux systems do not usually have &quot;/etc/ttys&quot;, it will always return 0. </p>
<p> On BSD-like systems and Linux, the declaration of <code>ttyslot</code>() is provided by <i>&lt;unistd.h&gt;</i>. On System V-like systems, the declaration is provided by <i>&lt;stdlib.h&gt;</i>. Since glibc 2.24, <i>&lt;stdlib.h&gt;</i> also provides the declaration with the following feature test macro definitions: </p>
<p> (_XOPEN_SOURCE &gt;= 500 ||<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(_XOPEN_SOURCE&nbsp;&amp;&amp;&nbsp;_XOPEN_SOURCE_EXTENDED))<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&amp;&amp;&nbsp;!&nbsp;(_POSIX_C_SOURCE&nbsp;&gt;=&nbsp;200112L ||&nbsp;_XOPEN_SOURCE&nbsp;&gt;=&nbsp;600) </p>
<p> Minix also has <i>fttyslot</i>(<i>fd</i>).</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-getttyent/">getttyent</a></code>(3), <code><a href="/docs/linux/man/3-ttyname/">ttyname</a></code>(3), <code><a href="/docs/linux/man/5-utmp/">utmp</a></code>(5)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
