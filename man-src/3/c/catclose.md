---
title: "catclose(3)"
name: "catclose"
section: "3"
letter: "c"
url: "/docs/linux/man/3-catclose/"
description: "catopen, catclose – open/close a message catalog"
---

<h2 class="name">NAME</h2>
<p> catopen, catclose &#8211; open/close a message catalog </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;nl_types.h&gt;</code> </p>
<p> <code>nl_catd catopen(const char *</code><i>name</i><code>, int </code><i>flag</i><code>);</code> </p>
<p> <code>int catclose(nl_catd </code><i>catalog</i><code>);</code></p>
<h2>DESCRIPTION</h2>
<p> The function <code>catopen</code>() opens a message catalog and returns a catalog descriptor. The descriptor remains valid until <code>catclose</code>() or <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2). If a file descriptor is used to implement catalog descriptors, then the <code>FD_CLOEXEC</code> flag will be set. </p>
<p> The argument <i>name</i> specifies the name of the message catalog to be opened. If <i>name</i> specifies an absolute path (i.e., contains a &#8216;/&#8217;), then <i>name</i> specifies a pathname for the message catalog. Otherwise, the environment variable <code>NLSPATH</code> is used with <i>name</i> substituted for <code>%N</code> (see <code><a href="/docs/linux/man/7-locale/">locale</a></code>(7)). It is unspecified whether <code>NLSPATH</code> will be used when the process has root privileges. If <code>NLSPATH</code> does not exist in the environment, or if a message catalog cannot be opened in any of the paths specified by it, then an implementation defined path is used. This latter default path may depend on the <code>LC_MESSAGES</code> locale setting when the <i>flag</i> argument is <code>NL_CAT_LOCALE</code> and on the <code>LANG</code> environment variable when the <i>flag</i> argument is 0. Changing the <code>LC_MESSAGES</code> part of the locale may invalidate open catalog descriptors. </p>
<p> The <i>flag</i> argument to <code>catopen</code>() is used to indicate the source for the language to use. If it is set to <code>NL_CAT_LOCALE</code>, then it will use the current locale setting for <code>LC_MESSAGES</code>. Otherwise, it will use the <code>LANG</code> environment variable. </p>
<p> The function <code>catclose</code>() closes the message catalog identified by <i>catalog</i>. It invalidates any subsequent references to the message catalog defined by <i>catalog</i>.</p>
<h2>RETURN VALUE</h2>
<p> The function <code>catopen</code>() returns a message catalog descriptor of type <i>nl_catd</i> on success. On failure, it returns <i>(nl_catd)&nbsp;-1</i> and sets <i>errno</i> to indicate the error. The possible error values include all possible values for the <code><a href="/docs/linux/man/2-open/">open</a></code>(2) call. </p>
<p> The function <code>catclose</code>() returns 0 on success, or -1 on failure.</p>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>LC_MESSAGES</code></p>
<dd> May be the source of the <code>LC_MESSAGES</code> locale setting, and thus determine the language to use if <i>flag</i> is set to <code>NL_CAT_LOCALE</code>.</p>
<dt><code>LANG</code></p>
<dd> The language to use if <i>flag</i> is 0.</dl>
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
<td> <code>catopen</code>() </td>
<td>Thread safety</td>
<td>MT-Safe env
</td>
</tr>
<tr VALIGN=top>
<td> <code>catclose</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> POSIX.1-2001, POSIX.1-2008.</p>
<h2>NOTES</h2>
<p> The above is the POSIX.1 description. The glibc value for <code>NL_CAT_LOCALE</code> is 1. The default path varies, but usually looks at a number of places below <i>/usr/share/locale</i>.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-catgets/">catgets</a></code>(3), <code><a href="/docs/linux/man/3-setlocale/">setlocale</a></code>(3)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
