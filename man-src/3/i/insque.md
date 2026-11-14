---
title: "insque(3)"
name: "insque"
section: "3"
letter: "i"
url: "/docs/linux/man/3-insque/"
description: "insque, remque – insert/remove an item from a queue"
---

<h2 class="name">NAME</h2>
<p> insque, remque &#8211; insert/remove an item from a queue </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;search.h&gt;
void insque(void *elem, void *prev);
void remque(void *elem);
</code></pre>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p> <code>insque</code>(), <code>remque</code>():</p>
<dl>
<dt>
<dd> _XOPEN_SOURCE&nbsp;&gt;=&nbsp;500<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Glibc since 2.19:&nbsp;*/&nbsp;_DEFAULT_SOURCE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Glibc versions&nbsp;&lt;=&nbsp;2.19:&nbsp;*/&nbsp;_SVID_SOURCE</dl>
<h2>DESCRIPTION</h2>
<p> The <code>insque</code>() and <code>remque</code>() functions manipulate doubly linked lists. Each element in the list is a structure of which the first two elements are a forward and a backward pointer. The linked list may be linear (i.e., NULL forward pointer at the end of the list and NULL backward pointer at the start of the list) or circular. </p>
<p> The <code>insque</code>() function inserts the element pointed to by <i>elem</i> immediately after the element pointed to by <i>prev</i>. </p>
<p> If the list is linear, then the call <i>insque(elem, NULL)</i> can be used to insert the initial list element, and the call sets the forward and backward pointers of <i>elem</i> to NULL. </p>
<p> If the list is circular, the caller should ensure that the forward and backward pointers of the first element are initialized to point to that element, and the <i>prev</i> argument of the <code>insque</code>() call should also point to the element. </p>
<p> The <code>remque</code>() function removes the element pointed to by <i>elem</i> from the doubly linked list.</p>
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
<td> <code>insque</code>(), <code>remque</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> POSIX.1-2001, POSIX.1-2008.</p>
<h2>NOTES</h2>
<p> On ancient systems, the arguments of these functions were of type <i>struct qelem *</i>, defined as: </p>
<p> struct qelem {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct qelem&nbsp;*q_forw;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct qelem&nbsp;*q_back;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;q_data[1]; }; </p>
<p> This is still what you will get if <code>_GNU_SOURCE</code> is defined before including <i>&lt;search.h&gt;</i>. </p>
<p> The location of the prototypes for these functions differs among several versions of UNIX. The above is the POSIX version. Some systems place them in <i>&lt;string.h&gt;</i>.</p>
<h2>BUGS</h2>
<p> In glibc 2.4 and earlier, it was not possible to specify <i>prev</i> as NULL. Consequently, to build a linear list, the caller had to build a list using an initial call that contained the first two elements of the list, with the forward and backward pointers in each element suitably initialized.</p>
<h2>EXAMPLES</h2>
<p> The program below demonstrates the use of <code>insque</code>(). Here is an example run of the program: </p>
<p> $ <code>./a.out -c a b c</code> Traversing completed list:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;a<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;b<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;c That was a circular list</p>
<h3>Program source</h3>
<p> #include &lt;stdio.h&gt; #include &lt;stdlib.h&gt; #include &lt;unistd.h&gt; #include &lt;search.h&gt; </p>
<p> struct element {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct element&nbsp;*forward;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct element&nbsp;*backward;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;*name; }; </p>
<p> static struct element * new_element(void) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct element&nbsp;*e&nbsp;=&nbsp;malloc(sizeof(*e));<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(e&nbsp;==&nbsp;NULL)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fprintf(stderr,&nbsp;&quot;malloc()&nbsp;failed
&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return e; } </p>
<p> int main(int argc, char *argv[]) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct element&nbsp;*first,&nbsp;*elem,&nbsp;*prev;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int circular, opt, errfnd; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;The&nbsp;&quot;-c&quot;&nbsp;command-line option can be used to specify that the<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;list is circular&nbsp;*/ </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;errfnd&nbsp;=&nbsp;0;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;circular&nbsp;=&nbsp;0;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;while&nbsp;((opt&nbsp;=&nbsp;getopt(argc, argv,&nbsp;&quot;c&quot;))&nbsp;!=&nbsp;-1)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;switch&nbsp;(opt)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;case&nbsp;&#8216;c&#8217;:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;circular&nbsp;=&nbsp;1;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;break;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;default:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;errfnd&nbsp;=&nbsp;1;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;break;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;}<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(errfnd || optind&nbsp;&gt;=&nbsp;argc)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fprintf(stderr,&nbsp;<wbr>&nbsp;&quot;Usage:&nbsp;%s&nbsp;[-c]&nbsp;string&#8230;
&quot;, argv[0]);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Create first element and place it in the linked list&nbsp;*/ </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;elem&nbsp;=&nbsp;new_element();<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;first&nbsp;=&nbsp;elem; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;elem-&gt;name&nbsp;=&nbsp;argv[optind]; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(circular)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;elem-&gt;forward&nbsp;=&nbsp;elem;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;elem-&gt;backward&nbsp;=&nbsp;elem;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;insque(elem, elem);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;}&nbsp;else&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;insque(elem, NULL);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Add remaining command-line arguments as list elements&nbsp;*/ </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;while&nbsp;(++optind&nbsp;&lt;&nbsp;argc)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;prev&nbsp;=&nbsp;elem; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;elem&nbsp;=&nbsp;new_element();<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;elem-&gt;name&nbsp;=&nbsp;argv[optind];<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;insque(elem, prev);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Traverse the list from the start, printing element names&nbsp;*/ </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;Traversing completed list:
&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;elem&nbsp;=&nbsp;first;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;do&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;%s
&quot;, elem-&gt;name);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;elem&nbsp;=&nbsp;elem-&gt;forward;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;}&nbsp;while&nbsp;(elem&nbsp;!=&nbsp;NULL&nbsp;&amp;&amp;&nbsp;elem&nbsp;!=&nbsp;first); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(elem&nbsp;==&nbsp;first)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;That was a circular list
&quot;); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_SUCCESS); }</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-queue/">queue</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
