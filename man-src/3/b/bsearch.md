---
title: "bsearch(3)"
name: "bsearch"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bsearch/"
description: "bsearch – binary search of a sorted array"
---

<h2 class="name">NAME</h2>
<p> bsearch &#8211; binary search of a sorted array </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;stdlib.h&gt;
void *bsearch(const void *key, const void *base,
              size_t nmemb, size_t size,
              int (*compar)(const void *, const void *));
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>bsearch</code>() function searches an array of <i>nmemb</i> objects, the initial member of which is pointed to by <i>base</i>, for a member that matches the object pointed to by <i>key</i>. The size of each member of the array is specified by <i>size</i>. </p>
<p> The contents of the array should be in ascending sorted order according to the comparison function referenced by <i>compar</i>. The <i>compar</i> routine is expected to have two arguments which point to the <i>key</i> object and to an array member, in that order, and should return an integer less than, equal to, or greater than zero if the <i>key</i> object is found, respectively, to be less than, to match, or be greater than the array member.</p>
<h2>RETURN VALUE</h2>
<p> The <code>bsearch</code>() function returns a pointer to a matching member of the array, or NULL if no match is found. If there are multiple elements that match the key, the element returned is unspecified.</p>
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
<td> <code>bsearch</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> POSIX.1-2001, POSIX.1-2008, C89, C99, SVr4, 4.3BSD.</p>
<h2>EXAMPLES</h2>
<p> The example below first sorts an array of structures using <code><a href="/docs/linux/man/3-qsort/">qsort</a></code>(3), then retrieves desired elements using <code>bsearch</code>(). </p>
<p> #include &lt;stdio.h&gt; #include &lt;stdlib.h&gt; #include &lt;string.h&gt; </p>
<p> struct mi {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int nr;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;*name; } months[] = {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;{&nbsp;1,&nbsp;&quot;jan&quot;&nbsp;},&nbsp;{&nbsp;2,&nbsp;&quot;feb&quot;&nbsp;},&nbsp;{&nbsp;3,&nbsp;&quot;mar&quot;&nbsp;},&nbsp;{&nbsp;4,&nbsp;&quot;apr&quot;&nbsp;},<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;{&nbsp;5,&nbsp;&quot;may&quot;&nbsp;},&nbsp;{&nbsp;6,&nbsp;&quot;jun&quot;&nbsp;},&nbsp;{&nbsp;7,&nbsp;&quot;jul&quot;&nbsp;},&nbsp;{&nbsp;8,&nbsp;&quot;aug&quot;&nbsp;},<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;{&nbsp;9,&nbsp;&quot;sep&quot;&nbsp;},&nbsp;{10,&nbsp;&quot;oct&quot;&nbsp;},&nbsp;{11,&nbsp;&quot;nov&quot;&nbsp;},&nbsp;{12,&nbsp;&quot;dec&quot;&nbsp;} }; </p>
<p> #define nr_of_months (sizeof(months)/sizeof(months[0])) </p>
<p> static int compmi(const void *m1, const void *m2) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;const struct mi&nbsp;*mi1&nbsp;=&nbsp;m1;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;const struct mi&nbsp;*mi2&nbsp;=&nbsp;m2;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return strcmp(mi1-&gt;name, mi2-&gt;name); } </p>
<p> int main(int argc, char **argv) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;qsort(months, nr_of_months, sizeof(months[0]), compmi);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;for&nbsp;(int i&nbsp;=&nbsp;1;&nbsp;i&nbsp;&lt;&nbsp;argc;&nbsp;i++)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct mi key;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct mi&nbsp;*res; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;key.name&nbsp;=&nbsp;argv[i];<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;res&nbsp;=&nbsp;bsearch(&amp;key, months, nr_of_months,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;sizeof(months[0]), compmi);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(res&nbsp;==&nbsp;NULL)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;&#8217;%s&#8217;: unknown month
&quot;, argv[i]);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;else<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;%s: month&nbsp;#%d
&quot;, res-&gt;name, res-&gt;nr);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;}<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_SUCCESS); }</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-hsearch/">hsearch</a></code>(3), <code><a href="/docs/linux/man/3-lsearch/">lsearch</a></code>(3), <code><a href="/docs/linux/man/3-qsort/">qsort</a></code>(3), <code><a href="/docs/linux/man/3-tsearch/">tsearch</a></code>(3)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
