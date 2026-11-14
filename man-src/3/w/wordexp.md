---
title: "wordexp(3)"
name: "wordexp"
section: "3"
letter: "w"
url: "/docs/linux/man/3-wordexp/"
description: "wordexp, wordfree – perform word expansion like a posix-shell"
---

<p>wordexp, wordfree &#8211; perform word expansion like a posix-shell</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;wordexp.h&gt;
int wordexp(const char *s, wordexp_t *p, int flags);
void wordfree(wordexp_t *p);</code></pre>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): <code>wordexp</code>(), <code>wordfree</code>(): _XOPEN_SOURCE</p>
<h2>Description</h2>
<p>The function <code>wordexp</code>() performs a shell-like expansion of the string <i>s</i> and returns the result in the structure pointed to by <i>p</i>. The data type <i>wordexp_t</i> is a structure that at least has the fields <i>we_wordc</i>, <i>we_wordv</i>, and <i>we_offs</i>. The field <i>we_wordc</i> is a <i>size_t</i> that gives the number of words in the expansion of <i>s</i>. The field <i>we_wordv</i> is a <i>char&nbsp;**</i> that points to the array of words found. The field <i>we_offs</i> of type <i>size_t</i> is sometimes (depending on <i>flags</i>, see below) used to indicate the number of initial elements in the <i>we_wordv</i> array that should be filled with NULLs. </p>
<p> The function <code>wordfree</code>() frees the allocated memory again. More precisely, it does not free its argument, but it frees the array <i>we_wordv</i> and the strings that points to.</p>
<h3>The string argument</h3>
<p>Since the expansion is the same as the expansion by the shell (see <code><a href="/docs/linux/man/1-sh/">sh</a></code>(1)) of the parameters to a command, the string <i>s</i> must not contain characters that would be illegal in shell command parameters. In particular, there must not be any unescaped newline or |, &amp;, ;, &lt;, &gt;, (, ), {, } characters outside a command substitution or parameter substitution context. </p>
<p> If the argument <i>s</i> contains a word that starts with an unquoted comment character #, then it is unspecified whether that word and all following words are ignored, or the # is treated as a non-comment character.</p>
<h3>The expansion</h3>
<p>The expansion done consists of the following stages: tilde expansion (replacing ~user by user&#8217;s home directory), variable substitution (replacing $FOO by the value of the environment variable FOO), command substitution (replacing $(command) or `command` by the output of command), arithmetic expansion, field splitting, wildcard expansion, quote removal. </p>
<p> The result of expansion of special parameters ($@, $*, $#, $?, $-, $$, $!, $0) is unspecified. </p>
<p> Field splitting is done using the environment variable $IFS. If it is not set, the field separators are space, tab and newline.</p>
<h3>The output array</h3>
<p>The array <i>we_wordv</i> contains the words found, followed by a NULL.</p>
<h3>The flags argument</h3>
<p>The <i>flag</i> argument is a bitwise inclusive OR of the following values:</p>
<dl>
<dt><code>WRDE_APPEND</code></p>
<dd>Append the words found to the array resulting from a previous call.</p>
<dt><code>WRDE_DOOFFS</code></p>
<dd>Insert <i>we_offs</i> initial NULLs in the array <i>we_wordv</i>. (These are not counted in the returned <i>we_wordc</i>.)</p>
<dt><code>WRDE_NOCMD</code></p>
<dd>Don&#8217;t do command substitution.</p>
<dt><code>WRDE_REUSE</code></p>
<dd>The argument <i>p</i> resulted from a previous call to <code>wordexp</code>(), and <code>wordfree</code>() was not called. Reuse the allocated storage.</p>
<dt><code>WRDE_SHOWERR</code></p>
<dd>Normally during command substitution <i>stderr</i> is redirected to <i>/dev/null</i>. This flag specifies that <i>stderr</i> is not to be redirected.</p>
<dt><code>WRDE_UNDEF</code></p>
<dd>Consider it an error if an undefined shell variable is expanded.</dl>
<h2>Return Value</h2>
<p>In case of success 0 is returned. In case of error one of the following five values is returned.</p>
<dl>
<dt><code>WRDE_BADCHAR</code></p>
<dd>Illegal occurrence of newline or one of |, &amp;, ;, &lt;, &gt;, (, ), {, }.</p>
<dt><code>WRDE_BADVAL</code></p>
<dd>An undefined shell variable was referenced, and the <code>WRDE_UNDEF</code> flag told us to consider this an error.</p>
<dt><code>WRDE_CMDSUB</code></p>
<dd>Command substitution requested, but the <code>WRDE_NOCMD</code> flag told us to consider this an error.</p>
<dt><code>WRDE_NOSPACE</code></p>
<dd>Out of memory.</p>
<dt><code>WRDE_SYNTAX</code></p>
<dd>Shell syntax error, such as unbalanced parentheses or unmatched quotes.</dl>
<h2>Versions</h2>
<p><code>wordexp</code>() and <code>wordfree</code>() are provided in glibc since version 2.1.</p>
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
<td> <code>wordexp</code>() </td>
<td>Thread safety</td>
<td> MT-Unsafe race:utent const:env<br />
 env sig:ALRM timer locale
</td>
</tr>
<tr VALIGN=top>
<td> <code>wordfree</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<p> In the above table, <i>utent</i> in <i>race:utent</i> signifies that if any of the functions <code><a href="/docs/linux/man/3-setutent/">setutent</a></code>(3), <code><a href="/docs/linux/man/3-getutent/">getutent</a></code>(3), or <code><a href="/docs/linux/man/3-endutent/">endutent</a></code>(3) are used in parallel in different threads of a program, then data races could occur. <code>wordexp</code>() calls those functions, so we use race:utent to remind users.</p>
<h2>Conforming To</h2>
<p>POSIX.1-2001, POSIX.1-2008.</p>
<h2>Examples</h2>
<p>The output of the following example program is approximately that of &quot;ls [a-c]*.c&quot;. </p>
<pre><code>#include &lt;stdio.h&gt;
#include &lt;stdlib.h&gt;
#include &lt;wordexp.h&gt;
int main(int argc, char **argv)
{
    wordexp_t p;
    char **w;
    wordexp(&quot;[a-c]*.c&quot;, &amp;p, 0);
    w = p.we_wordv;
    for (int i = 0; i &lt; p.we_wordc; i++)
        printf(&quot;%s
&quot;, w[i]);
    wordfree(&amp;p);
    exit(EXIT_SUCCESS);
}</code></pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-fnmatch/">fnmatch</a></code>(3), <code><a href="/docs/linux/man/3-glob/">glob</a></code>(3)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
