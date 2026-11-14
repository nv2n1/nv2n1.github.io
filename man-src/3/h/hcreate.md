---
title: "hcreate(3)"
name: "hcreate"
section: "3"
letter: "h"
url: "/docs/linux/man/3-hcreate/"
description: "hcreate, hdestroy, hsearch, hcreate_r, hdestroy_r, hsearch_r – hash table management"
---

<h2 class="name">NAME</h2>
<p> hcreate, hdestroy, hsearch, hcreate_r, hdestroy_r, hsearch_r &#8211; hash table management </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;search.h&gt;
int hcreate(size_t nel);
ENTRY *hsearch(ENTRY item, ACTION action);
void hdestroy(void);
#define _GNU_SOURCE /* See feature_test_macros(7) */
#include &lt;search.h&gt;
int hcreate_r(size_t nel, struct hsearch_data *htab);
int hsearch_r(ENTRY item, ACTION action, ENTRY **retval,
              struct hsearch_data *htab);
void hdestroy_r(struct hsearch_data *htab);
</code></pre>
<h2>DESCRIPTION</h2>
<p> The three functions <code>hcreate</code>(), <code>hsearch</code>(), and <code>hdestroy</code>() allow the caller to create and manage a hash search table containing entries consisting of a key (a string) and associated data. Using these functions, only one hash table can be used at a time. </p>
<p> The three functions <code>hcreate_r</code>(), <code>hsearch_r</code>(), <code>hdestroy_r</code>() are reentrant versions that allow a program to use more than one hash search table at the same time. The last argument, <i>htab</i>, points to a structure that describes the table on which the function is to operate. The programmer should treat this structure as opaque (i.e., do not attempt to directly access or modify the fields in this structure). </p>
<p> First a hash table must be created using <code>hcreate</code>(). The argument <i>nel</i> specifies the maximum number of entries in the table. (This maximum cannot be changed later, so choose it wisely.) The implementation may adjust this value upward to improve the performance of the resulting hash table. </p>
<p> The <code>hcreate_r</code>() function performs the same task as <code>hcreate</code>(), but for the table described by the structure <i>*htab</i>. The structure pointed to by <i>htab</i> must be zeroed before the first call to <code>hcreate_r</code>(). </p>
<p> The function <code>hdestroy</code>() frees the memory occupied by the hash table that was created by <code>hcreate</code>(). After calling <code>hdestroy</code>(), a new hash table can be created using <code>hcreate</code>(). The <code>hdestroy_r</code>() function performs the analogous task for a hash table described by <i>*htab</i>, which was previously created using <code>hcreate_r</code>(). </p>
<p> The <code>hsearch</code>() function searches the hash table for an item with the same key as <i>item</i> (where &quot;the same&quot; is determined using <code><a href="/docs/linux/man/3-strcmp/">strcmp</a></code>(3)), and if successful returns a pointer to it. </p>
<p> The argument <i>item</i> is of type <i>ENTRY</i>, which is defined in <i>&lt;search.h&gt;</i> as follows: </p>
<p> typedef struct entry {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;*key;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;void&nbsp;*data; } ENTRY; </p>
<p> The field <i>key</i> points to a null-terminated string which is the search key. The field <i>data</i> points to data that is associated with that key. </p>
<p> The argument <i>action</i> determines what <code>hsearch</code>() does after an unsuccessful search. This argument must either have the value <code>ENTER</code>, meaning insert a copy of <i>item</i> (and return a pointer to the new hash table entry as the function result), or the value <code>FIND</code>, meaning that NULL should be returned. (If <i>action</i> is <code>FIND</code>, then <i>data</i> is ignored.) </p>
<p> The <code>hsearch_r</code>() function is like <code>hsearch</code>() but operates on the hash table described by <i>*htab</i>. The <code>hsearch_r</code>() function differs from <code>hsearch</code>() in that a pointer to the found item is returned in <i>*retval</i>, rather than as the function result.</p>
<h2>RETURN VALUE</h2>
<p> <code>hcreate</code>() and <code>hcreate_r</code>() return nonzero on success. They return 0 on error, with <i>errno</i> set to indicate the cause of the error. </p>
<p> On success, <code>hsearch</code>() returns a pointer to an entry in the hash table. <code>hsearch</code>() returns NULL on error, that is, if <i>action</i> is <code>ENTER</code> and the hash table is full, or <i>action</i> is <code>FIND</code> and <i>item</i> cannot be found in the hash table. <code>hsearch_r</code>() returns nonzero on success, and 0 on error. In the event of an error, these two functions set <i>errno</i> to indicate the cause of the error.</p>
<h2>ERRORS</h2>
<p> <code>hcreate_r</code>() and <code>hdestroy_r</code>() can fail for the following reasons:</p>
<dl>
<dt><code>EINVAL</code></p>
<dd> <i>htab</i> is NULL.</dl>
<p> <code>hsearch</code>() and <code>hsearch_r</code>() can fail for the following reasons:</p>
<dl>
<dt><code>ENOMEM</code></p>
<dd> <i>action</i> was <code>ENTER</code>, <i>key</i> was not found in the table, and there was no room in the table to add a new entry.</p>
<dt><code>ESRCH</code></p>
<dd> <i>action</i> was <code>FIND</code>, and <i>key</i> was not found in the table.</dl>
<p> POSIX.1 specifies only the <code>ENOMEM</code> error.</p>
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
<td> <code>hcreate</code>(), <code>hsearch</code>(),<br />
 <code>hdestroy</code>() </td>
<td>Thread safety</td>
<td>MT-Unsafe race:hsearch
</td>
</tr>
<tr VALIGN=top>
<td> <code>hcreate_r</code>(), <code>hsearch_r</code>(),<br />
 <code>hdestroy_r</code>() </td>
<td>Thread safety</td>
<td>MT-Safe race:htab
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> The functions <code>hcreate</code>(), <code>hsearch</code>(), and <code>hdestroy</code>() are from SVr4, and are described in POSIX.1-2001 and POSIX.1-2008. </p>
<p> The functions <code>hcreate_r</code>(), <code>hsearch_r</code>(), and <code>hdestroy_r</code>() are GNU extensions.</p>
<h2>NOTES</h2>
<p> Hash table implementations are usually more efficient when the table contains enough free space to minimize collisions. Typically, this means that <i>nel</i> should be at least 25% larger than the maximum number of elements that the caller expects to store in the table. </p>
<p> The <code>hdestroy</code>() and <code>hdestroy_r</code>() functions do not free the buffers pointed to by the <i>key</i> and <i>data</i> elements of the hash table entries. (It can&#8217;t do this because it doesn&#8217;t know whether these buffers were allocated dynamically.) If these buffers need to be freed (perhaps because the program is repeatedly creating and destroying hash tables, rather than creating a single table whose lifetime matches that of the program), then the program must maintain bookkeeping data structures that allow it to free them.</p>
<h2>BUGS</h2>
<p> SVr4 and POSIX.1-2001 specify that <i>action</i> is significant only for unsuccessful searches, so that an <code>ENTER</code> should not do anything for a successful search. In libc and glibc (before version 2.3), the implementation violates the specification, updating the <i>data</i> for the given <i>key</i> in this case. </p>
<p> Individual hash table entries can be added, but not deleted.</p>
<h2>EXAMPLES</h2>
<p> The following program inserts 24 items into a hash table, then prints some of them. </p>
<p> #include &lt;stdio.h&gt; #include &lt;stdlib.h&gt; #include &lt;search.h&gt; </p>
<p> static char *data[] = { &quot;alpha&quot;, &quot;bravo&quot;, &quot;charlie&quot;, &quot;delta&quot;,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&quot;echo&quot;,&nbsp;&quot;foxtrot&quot;,&nbsp;&quot;golf&quot;,&nbsp;&quot;hotel&quot;,&nbsp;&quot;india&quot;,&nbsp;&quot;juliet&quot;,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&quot;kilo&quot;,&nbsp;&quot;lima&quot;,&nbsp;&quot;mike&quot;,&nbsp;&quot;november&quot;,&nbsp;&quot;oscar&quot;,&nbsp;&quot;papa&quot;,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&quot;quebec&quot;,&nbsp;&quot;romeo&quot;,&nbsp;&quot;sierra&quot;,&nbsp;&quot;tango&quot;,&nbsp;&quot;uniform&quot;,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&quot;victor&quot;,&nbsp;&quot;whisky&quot;,&nbsp;&quot;x-ray&quot;,&nbsp;&quot;yankee&quot;,&nbsp;&quot;zulu&quot; }; </p>
<p> int main(void) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;ENTRY e;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;ENTRY&nbsp;*ep; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;hcreate(30); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;for&nbsp;(int i&nbsp;=&nbsp;0;&nbsp;i&nbsp;&lt;&nbsp;24;&nbsp;i++)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;e.key&nbsp;=&nbsp;data[i];<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;data is just an integer, instead of a<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;pointer to something&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;e.data&nbsp;=&nbsp;(void&nbsp;*)&nbsp;i;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;ep&nbsp;=&nbsp;hsearch(e, ENTER);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;there should be no failures&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(ep&nbsp;==&nbsp;NULL)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fprintf(stderr,&nbsp;&quot;entry failed
&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;}<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;for&nbsp;(int i&nbsp;=&nbsp;22;&nbsp;i&nbsp;&lt;&nbsp;26;&nbsp;i++)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;print two entries from the table, and<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;show that two are not in the table&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;e.key&nbsp;=&nbsp;data[i];<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;ep&nbsp;=&nbsp;hsearch(e, FIND);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;%9.9s -&gt;&nbsp;%9.9s:%d
&quot;, e.key,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;ep&nbsp;?&nbsp;ep-&gt;key :&nbsp;&quot;NULL&quot;, ep&nbsp;?&nbsp;(int)(ep-&gt;data)&nbsp;: 0);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;}<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;hdestroy();<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_SUCCESS); }</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-bsearch/">bsearch</a></code>(3), <code><a href="/docs/linux/man/3-lsearch/">lsearch</a></code>(3), <code><a href="/docs/linux/man/3-malloc/">malloc</a></code>(3), <code><a href="/docs/linux/man/3-tsearch/">tsearch</a></code>(3)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
