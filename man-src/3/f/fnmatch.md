---
title: "fnmatch(3)"
name: "fnmatch"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fnmatch/"
description: "fnmatch – match filename or pathname"
---

<h2 class="name">NAME</h2>
<p> fnmatch &#8211; match filename or pathname </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;fnmatch.h&gt;
int fnmatch(const char *pattern, const char *string, int flags);
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>fnmatch</code>() function checks whether the <i>string</i> argument matches the <i>pattern</i> argument, which is a shell wildcard pattern (see <code><a href="/docs/linux/man/7-glob/">glob</a></code>(7)). </p>
<p> The <i>flags</i> argument modifies the behavior; it is the bitwise OR of zero or more of the following flags:</p>
<dl>
<dt><code>FNM_NOESCAPE</code></p>
<dd> If this flag is set, treat backslash as an ordinary character, instead of an escape character.</p>
<dt><code>FNM_PATHNAME</code></p>
<dd> If this flag is set, match a slash in <i>string</i> only with a slash in <i>pattern</i> and not by an asterisk (*) or a question mark (?) metacharacter, nor by a bracket expression ([]) containing a slash.</p>
<dt><code>FNM_PERIOD</code></p>
<dd> If this flag is set, a leading period in <i>string</i> has to be matched exactly by a period in <i>pattern</i>. A period is considered to be leading if it is the first character in <i>string</i>, or if both <code>FNM_PATHNAME</code> is set and the period immediately follows a slash.</p>
<dt><code>FNM_FILE_NAME</code></p>
<dd> This is a GNU synonym for <code>FNM_PATHNAME</code>.</p>
<dt><code>FNM_LEADING_DIR</code></p>
<dd> If this flag (a GNU extension) is set, the pattern is considered to be matched if it matches an initial segment of <i>string</i> which is followed by a slash. This flag is mainly for the internal use of glibc and is implemented only in certain cases.</p>
<dt><code>FNM_CASEFOLD</code></p>
<dd> If this flag (a GNU extension) is set, the pattern is matched case-insensitively.</p>
<dt><code>FNM_EXTMATCH</code></p>
<dd> If this flag (a GNU extension) is set, extended patterns are supported, as introduced by &#8216;ksh&#8217; and now supported by other shells. The extended format is as follows, with <i>pattern-list</i> being a &#8216;|&#8217; separated list of patterns.</p>
<dt>&#8216;?(<i>pattern-list</i>)&#8217;</p>
<dd> The pattern matches if zero or one occurrences of any of the patterns in the <i>pattern-list</i> match the input <i>string</i>.</p>
<dt>&#8216;*(<i>pattern-list</i>)&#8217;</p>
<dd> The pattern matches if zero or more occurrences of any of the patterns in the <i>pattern-list</i> match the input <i>string</i>.</p>
<dt>&#8216;+(<i>pattern-list</i>)&#8217;</p>
<dd> The pattern matches if one or more occurrences of any of the patterns in the <i>pattern-list</i> match the input <i>string</i>.</p>
<dt>&#8216;@(<i>pattern-list</i>)&#8217;</p>
<dd> The pattern matches if exactly one occurrence of any of the patterns in the <i>pattern-list</i> match the input <i>string</i>.</p>
<dt>&#8216;!(<i>pattern-list</i>)&#8217;</p>
<dd> The pattern matches if the input <i>string</i> cannot be matched with any of the patterns in the <i>pattern-list</i>.</dl>
<h2>RETURN VALUE</h2>
<p> Zero if <i>string</i> matches <i>pattern</i>, <code>FNM_NOMATCH</code> if there is no match or another nonzero value if there is an error.</p>
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
<td> <code>fnmatch</code>() </td>
<td>Thread safety</td>
<td>MT-Safe env locale
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> POSIX.1-2001, POSIX.1-2008, POSIX.2. The <code>FNM_FILE_NAME</code>, <code>FNM_LEADING_DIR</code>, and <code>FNM_CASEFOLD</code> flags are GNU extensions.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-sh/">sh</a></code>(1), <code><a href="/docs/linux/man/3-glob/">glob</a></code>(3), <code><a href="/docs/linux/man/3-scandir/">scandir</a></code>(3), <code><a href="/docs/linux/man/3-wordexp/">wordexp</a></code>(3), <code><a href="/docs/linux/man/7-glob/">glob</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
