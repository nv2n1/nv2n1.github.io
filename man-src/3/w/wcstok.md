---
title: "wcstok(3)"
name: "wcstok"
section: "3"
letter: "w"
url: "/docs/linux/man/3-wcstok/"
description: "wcstok – split wide-character string into tokens"
---

<p>wcstok &#8211; split wide-character string into tokens</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;wchar.h&gt;
wchar_t *wcstok(wchar_t *wcs, const wchar_t *delim, wchar_t **ptr);</code></pre>
<h2>Description</h2>
<p>The <code>wcstok</code>() function is the wide-character equivalent of the <code><a href="/docs/linux/man/3-strtok/">strtok</a></code>(3) function, with an added argument to make it multithread-safe. It can be used to split a wide-character string <i>wcs</i> into tokens, where a token is defined as a substring not containing any wide-characters from <i>delim</i>. </p>
<p> The search starts at <i>wcs</i>, if <i>wcs</i> is not NULL, or at <i>*ptr</i>, if <i>wcs</i> is NULL. First, any delimiter wide-characters are skipped, that is, the pointer is advanced beyond any wide-characters which occur in <i>delim</i>. If the end of the wide-character string is now reached, <code>wcstok</code>() returns NULL, to indicate that no tokens were found, and stores an appropriate value in <i>*ptr</i>, so that subsequent calls to <code>wcstok</code>() will continue to return NULL. Otherwise, the <code>wcstok</code>() function recognizes the beginning of a token and returns a pointer to it, but before doing that, it zero-terminates the token by replacing the next wide-character which occurs in <i>delim</i> with a null wide character (L&#8217;\0&#8217;), and it updates <i>*ptr</i> so that subsequent calls will continue searching after the end of recognized token.  </p>
<h2>RETURN VALUE</h2>
<p> The <code>wcstok</code>() function returns a pointer to the next token, or NULL if no further token was found.  </p>
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
<td> <code>wcstok</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> POSIX.1-2001, POSIX.1-2008, C99.  </p>
<h2>NOTES</h2>
<p> The original <i>wcs</i> wide-character string is destructively modified during the operation.  </p>
<h2>EXAMPLES</h2>
<p> The following code loops over the tokens contained in a wide-character string. </p>
<p> wchar_t *wcs = ...; wchar_t *token; wchar_t *state; for (token = wcstok(wcs, &quot; \t\n&quot;, &amp;state); <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;token&nbsp;!=&nbsp;NULL; <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;token&nbsp;=&nbsp;wcstok(NULL,&nbsp;&quot;&nbsp;\t\n&quot;,&nbsp;&amp;state))&nbsp;{ <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;... }  </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-strtok/">strtok</a></code>(3), <code><a href="/docs/linux/man/3-wcschr/">wcschr</a></code>(3)  </p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
