---
title: "getaliasent_r(3)"
name: "getaliasent_r"
section: "3"
letter: "g"
url: "/docs/linux/man/3-getaliasent_r/"
description: "setaliasent, endaliasent, getaliasent, getaliasent_r, getaliasbyname, getaliasbyname_r – read an alias entry"
---

<h2 class="name">NAME</h2>
<p> setaliasent, endaliasent, getaliasent, getaliasent_r, getaliasbyname, getaliasbyname_r &#8211; read an alias entry </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;aliases.h&gt;</code> </p>
<p> <code>void setaliasent(void);</code> </p>
<p> <code>void endaliasent(void);</code> </p>
<p> <code>struct aliasent *getaliasent(void);</code> </p>
<p> <code>int getaliasent_r(struct aliasent *</code><i>result</i><code>,</code><br />
 <code> char *</code><i>buffer</i><code>, size_t </code><i>buflen</i><code>, struct aliasent **</code><i>res</i><code>);</code> </p>
<p> <code>struct aliasent *getaliasbyname(const char *</code><i>name</i><code>);</code> </p>
<p> <code>int getaliasbyname_r(const char *</code><i>name</i><code>, struct aliasent *</code><i>result</i><code>,</code><br />
 <code> char *</code><i>buffer</i><code>, size_t </code><i>buflen</i><code>, struct aliasent **</code><i>res</i><code>);</code></p>
<h2>DESCRIPTION</h2>
<p> One of the databases available with the Name Service Switch (NSS) is the aliases database, that contains mail aliases. (To find out which databases are supported, try <i>getent &#8211;help</i>.) Six functions are provided to access the aliases database. </p>
<p> The <code>getaliasent</code>() function returns a pointer to a structure containing the group information from the aliases database. The first time it is called it returns the first entry; thereafter, it returns successive entries. </p>
<p> The <code>setaliasent</code>() function rewinds the file pointer to the beginning of the aliases database. </p>
<p> The <code>endaliasent</code>() function closes the aliases database. </p>
<p> <code>getaliasent_r</code>() is the reentrant version of the previous function. The requested structure is stored via the first argument but the programmer needs to fill the other arguments also. Not providing enough space causes the function to fail. </p>
<p> The function <code>getaliasbyname</code>() takes the name argument and searches the aliases database. The entry is returned as a pointer to a <i>struct aliasent</i>. </p>
<p> <code>getaliasbyname_r</code>() is the reentrant version of the previous function. The requested structure is stored via the second argument but the programmer needs to fill the other arguments also. Not providing enough space causes the function to fail. </p>
<p> The <i>struct aliasent</i> is defined in <i>&lt;aliases.h&gt;</i>: </p>
<p> struct aliasent {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;*alias_name;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;alias name&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;size_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;alias_members_len;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;<wbr>&nbsp;<wbr>&nbsp;**alias_members;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;alias name list&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;alias_local; };</p>
<h2>RETURN VALUE</h2>
<p> The functions <code>getaliasent_r</code>() and <code>getaliasbyname_r</code>() return a nonzero value on error.</p>
<h2>FILES</h2>
<p> The default alias database is the file <i>/etc/aliases</i>. This can be changed in the <i>/etc/nsswitch.conf</i> file.</p>
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
<td> <code>setaliasent</code>(), <code>endaliasent</code>(), <code>getaliasent_r</code>(), <code>getaliasbyname_r</code>() </td>
<td>Thread safety</td>
<td>MT-Safe locale
</td>
</tr>
<tr VALIGN=top>
<td> <code>getaliasent</code>(), <code>getaliasbyname</code>() </td>
<td>Thread safety</td>
<td>MT-Unsafe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> These routines are glibc-specific. The NeXT system has similar routines: </p>
<p> #include &lt;aliasdb.h&gt; </p>
<p> void alias_setent(void); void alias_endent(void); alias_ent *alias_getent(void); alias_ent *alias_getbyname(char *name);</p>
<h2>EXAMPLES</h2>
<p> The following example compiles with <i>gcc example.c -o example</i>. It will dump all names in the alias database. </p>
<p> #include &lt;aliases.h&gt; #include &lt;stdio.h&gt; #include &lt;stdlib.h&gt; #include &lt;errno.h&gt; </p>
<p> int main(void) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct aliasent&nbsp;*al;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;setaliasent();<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;for&nbsp;(;;)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;al&nbsp;=&nbsp;getaliasent();<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(al&nbsp;==&nbsp;NULL)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;break;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;Name:&nbsp;%s
&quot;, al-&gt;alias_name);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;}<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(errno)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;perror(&quot;reading alias&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;}<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;endaliasent();<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_SUCCESS); }</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-getgrent/">getgrent</a></code>(3), <code><a href="/docs/linux/man/3-getpwent/">getpwent</a></code>(3), <code><a href="/docs/linux/man/3-getspent/">getspent</a></code>(3), <code><a href="/docs/linux/man/5-aliases/">aliases</a></code>(5)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
