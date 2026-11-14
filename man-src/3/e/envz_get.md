---
title: "envz_get(3)"
name: "envz_get"
section: "3"
letter: "e"
url: "/docs/linux/man/3-envz_get/"
description: "envz_add, envz_entry, envz_get, envz_merge, envz_remove, envz_strip – environment string support"
---

<h2 class="name">NAME</h2>
<p> envz_add, envz_entry, envz_get, envz_merge, envz_remove, envz_strip &#8211; environment string support </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;envz.h&gt;
error_t envz_add(char **envz, size_t *envz_len,
                 const char *name, const char *value);
char *envz_entry(const char *envz, size_t envz_len, const char *name);
char *envz_get(const char *envz, size_t envz_len, const char *name);
error_t envz_merge(char **envz, size_t *envz_len,
                   const char *envz2, size_t envz2_len, int override);
void envz_remove(char **envz, size_t *envz_len, const char *name);
void envz_strip(char **envz, size_t *envz_len);
</code></pre>
<h2>DESCRIPTION</h2>
<p> These functions are glibc-specific. </p>
<p> An argz vector is a pointer to a character buffer together with a length, see <code><a href="/docs/linux/man/3-argz_add/">argz_add</a></code>(3). An envz vector is a special argz vector, namely one where the strings have the form &quot;name=value&quot;. Everything after the first &#8216;=&#8217; is considered to be the value. If there is no &#8216;=&#8217;, the value is taken to be NULL. (While the value in case of a trailing &#8216;=&#8217; is the empty string &quot;&quot;.) </p>
<p> These functions are for handling envz vectors. </p>
<p> <code>envz_add</code>() adds the string name = value (in case <i>value</i> is non-NULL) or name (in case <i>value</i> is NULL) to the envz vector (<i>*envz</i>,&nbsp;<i>*envz_len</i>) and updates <i>*envz</i> and <i>*envz_len</i>. If an entry with the same <i>name</i> existed, it is removed. </p>
<p> <code>envz_entry</code>() looks for <i>name</i> in the envz vector (<i>envz</i>,&nbsp;<i>envz_len</i>) and returns the entry if found, or NULL if not. </p>
<p> <code>envz_get</code>() looks for <i>name</i> in the envz vector (<i>envz</i>,&nbsp;<i>envz_len</i>) and returns the value if found, or NULL if not. (Note that the value can also be NULL, namely when there is an entry for <i>name</i> without &#8216;=&#8217; sign.) </p>
<p> <code>envz_merge</code>() adds each entry in <i>envz2</i> to <i>*envz</i>, as if with <code>envz_add</code>(). If <i>override</i> is true, then values in <i>envz2</i> will supersede those with the same name in <i>*envz</i>, otherwise not. </p>
<p> <code>envz_remove</code>() removes the entry for <i>name</i> from (<i>*envz</i>,&nbsp;<i>*envz_len</i>) if there was one. </p>
<p> <code>envz_strip</code>() removes all entries with value NULL.</p>
<h2>RETURN VALUE</h2>
<p> All envz functions that do memory allocation have a return type of <i>error_t</i> (an integer type), and return 0 for success, and <code>ENOMEM</code> if an allocation error occurs.</p>
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
<td> <code>envz_add</code>(), <code>envz_entry</code>(),<br />
 <code>envz_get</code>(), <code>envz_merge</code>(),<br />
 <code>envz_remove</code>(), <code>envz_strip</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> These functions are a GNU extension.</p>
<h2>EXAMPLES</h2>
<p> #include &lt;stdio.h&gt; #include &lt;stdlib.h&gt; #include &lt;envz.h&gt; </p>
<p> int main(int argc, char *argv[], char *envp[]) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int e_len&nbsp;=&nbsp;0;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;*str; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;for&nbsp;(int i&nbsp;=&nbsp;0;&nbsp;envp[i]&nbsp;!=&nbsp;NULL;&nbsp;i++)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;e_len&nbsp;+=&nbsp;strlen(envp[i])&nbsp;+&nbsp;1; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;str&nbsp;=&nbsp;envz_entry(*envp, e_len,&nbsp;&quot;HOME&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;%s
&quot;, str);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;str&nbsp;=&nbsp;envz_get(*envp, e_len,&nbsp;&quot;HOME&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;%s
&quot;, str);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_SUCCESS); }</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-argz_add/">argz_add</a></code>(3)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
