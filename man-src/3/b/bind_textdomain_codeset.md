---
title: "bind_textdomain_codeset(3)"
name: "bind_textdomain_codeset"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bind_textdomain_codeset/"
description: "bind_textdomain_codeset – set encoding of message translations"
---

<h2 class="name">NAME</h2>
<p> bind_textdomain_codeset &#8211; set encoding of message translations </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;libintl.h&gt;
char *bind_textdomain_codeset(const char *domainname,
                              const char *codeset);
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>bind_textdomain_codeset</code> function sets the output codeset for message catalogs for domain <i>domainname</i>. </p>
<p> A message domain is a set of translatable <i>msgid</i> messages. Usually, every software package has its own message domain. </p>
<p> By default, the <code>gettext</code> family of functions returns translated messages in the locale&#8217;s character encoding, which can be retrieved as <code>nl_langinfo(CODESET)</code>. The need for calling <code>bind_textdomain_codeset</code> arises for programs which store strings in a locale independent way (e.g. UTF-8) and want to avoid an extra character set conversion on the returned translated messages. </p>
<p> <i>domainname</i> must be a non-empty string. </p>
<p> If <i>codeset</i> is not NULL, it must be a valid encoding name which can be used for the <code>iconv_open</code> function. The <code>bind_textdomain_codeset</code> function sets the output codeset for message catalogs belonging to domain <i>domainname</i> to <i>codeset</i>. The function makes copies of the argument strings as needed. </p>
<p> If <i>codeset</i> is NULL, the function returns the previously set codeset for domain <i>domainname</i>. The default is NULL, denoting the locale&#8217;s character encoding.</p>
<h2>RETURN VALUE</h2>
<p> If successful, the <code>bind_textdomain_codeset</code> function returns the current codeset for domain <i>domainname</i>, after possibly changing it. The resulting string is valid until the next <code>bind_textdomain_codeset</code> call for the same <i>domainname</i> and must not be modified or freed. If a memory allocation failure occurs, it sets <code>errno</code> to <code>ENOMEM</code> and returns NULL. If no codeset has been set for domain <i>domainname</i>, it returns NULL.</p>
<h2>ERRORS</h2>
<p> The following error can occur, among others:</p>
<dl>
<dt><code>ENOMEM</code></p>
<dd> Not enough memory available.</dl>
<h2>BUGS</h2>
<p> The return type ought to be <code>const char *</code>, but is <code>char *</code> to avoid warnings in C code predating ANSI C.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-gettext/">gettext</a></code>(3), <code><a href="/docs/linux/man/3-dgettext/">dgettext</a></code>(3), <code><a href="/docs/linux/man/3-dcgettext/">dcgettext</a></code>(3), <code><a href="/docs/linux/man/3-ngettext/">ngettext</a></code>(3), <code><a href="/docs/linux/man/3-dngettext/">dngettext</a></code>(3), <code><a href="/docs/linux/man/3-dcngettext/">dcngettext</a></code>(3), <code><a href="/docs/linux/man/3-textdomain/">textdomain</a></code>(3), <code><a href="/docs/linux/man/3-nl_langinfo/">nl_langinfo</a></code>(3), <code><a href="/docs/linux/man/3-iconv_open/">iconv_open</a></code>(3) </p>
<h2>Index</h2>
