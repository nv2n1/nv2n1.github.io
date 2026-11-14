---
title: "rpmatch(3)"
name: "rpmatch"
section: "3"
letter: "r"
url: "/docs/linux/man/3-rpmatch/"
description: "rpmatch – determine if the answer to a question is affirmative or negative"
---

<p>rpmatch &#8211; determine if the answer to a question is affirmative or negative</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;stdlib.h&gt;

int rpmatch(const char *response);</code></pre>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): <code>rpmatch</code>():<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Since glibc 2.19:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;_DEFAULT_SOURCE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Glibc 2.19 and earlier:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;_SVID_SOURCE</p>
<h2>Description</h2>
<p><code>rpmatch</code>() handles a user response to yes or no questions, with support for internationalization. </p>
<p> <i>response</i> should be a null-terminated string containing a user-supplied response, perhaps obtained with <code><a href="/docs/linux/man/3-fgets/">fgets</a></code>(3) or <code><a href="/docs/linux/man/3-getline/">getline</a></code>(3). </p>
<p> The user&#8217;s language preference is taken into account per the environment variables <code>LANG</code>, <code>LC_MESSAGES</code>, and <code>LC_ALL</code>, if the program has called <code><a href="/docs/linux/man/3-setlocale/">setlocale</a></code>(3) to effect their changes. </p>
<p> Regardless of the locale, responses matching <code>ha[Yy]</code> are always accepted as affirmative, and those matching <code>ha[Nn]</code> are always accepted as negative.</p>
<h2>Return Value</h2>
<p>After examining <i>response</i>, <code>rpmatch</code>() returns 0 for a recognized negative response (&quot;no&quot;), 1 for a recognized positive response (&quot;yes&quot;), and -1 when the value of <i>response</i> is unrecognized.</p>
<h2>Errors</h2>
<p>A return value of -1 may indicate either an invalid input, or some other error. It is incorrect to only test if the return value is nonzero. </p>
<p> <code>rpmatch</code>() can fail for any of the reasons that <code><a href="/docs/linux/man/3-regcomp/">regcomp</a></code>(3) or <code><a href="/docs/linux/man/3-regexec/">regexec</a></code>(3) can fail; the cause of the error is not available from <i>errno</i> or anywhere else, but indicates a failure of the regex engine (but this case is indistinguishable from that of an unrecognized value of <i>response</i>).</p>
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
<td> <code>rpmatch</code>() </td>
<td>Thread safety</td>
<td>MT-Safe locale
</td>
</tr>
</table>
<h2>Conforming To</h2>
<p><code>rpmatch</code>() is not required by any standard, but is available on a few other systems.</p>
<h2>Bugs</h2>
<p>The <code>rpmatch</code>() implementation looks at only the first character of <i>response</i>. As a consequence, &quot;nyes&quot; returns 0, and &quot;ynever; not in a million years&quot; returns 1. It would be preferable to accept input strings much more strictly, for example (using the extended regular expression notation described in <code><a href="/docs/linux/man/7-regex/">regex</a></code>(7)): <code>ha([yY]|yes|YES)$</code> and <code>ha([nN]|no|NO)$</code>.</p>
<h2>Examples</h2>
<p>The following program displays the results when <code>rpmatch</code>() is applied to the string given in the program&#8217;s command-line argument. </p>
<pre><code>#define _SVID_SOURCE
#include &lt;locale.h&gt;
#include &lt;stdio.h&gt;
#include &lt;stdlib.h&gt;
#include &lt;string.h&gt;
int main(int argc, char *argv[])
{
    if (argc != 2 || strcmp(argv[1], &quot;--help&quot;) == 0) {
        fprintf(stderr, &quot;%s response
&quot;, argv[0]);
        exit(EXIT_FAILURE);
    }
    setlocale(LC_ALL, &quot;&quot;);
    printf(&quot;rpmatch() returns: %d
&quot;, rpmatch(argv[1]));
    exit(EXIT_SUCCESS);
}</code></pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-fgets/">fgets</a></code>(3), <code><a href="/docs/linux/man/3-getline/">getline</a></code>(3), <code><a href="/docs/linux/man/3-nl_langinfo/">nl_langinfo</a></code>(3), <code><a href="/docs/linux/man/3-regcomp/">regcomp</a></code>(3), <code><a href="/docs/linux/man/3-setlocale/">setlocale</a></code>(3)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
