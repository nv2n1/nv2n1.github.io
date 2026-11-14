---
title: "bindtextdomain(3)"
name: "bindtextdomain"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bindtextdomain/"
description: "bindtextdomain – set directory containing message catalogs"
---

<h2 class="name">NAME</h2>
<p> bindtextdomain &#8211; set directory containing message catalogs </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;libintl.h&gt;
char *bindtextdomain(const char *domainname, const char *dirname);
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>bindtextdomain</code> function sets the base directory of the hierarchy containing message catalogs for a given message domain. </p>
<p> A message domain is a set of translatable <i>msgid</i> messages. Usually, every software package has its own message domain. The need for calling <code>bindtextdomain</code> arises because packages are not always installed with the same prefix as the &lt;libintl.h&gt; header and the libc/libintl libraries. </p>
<p> Message catalogs will be expected at the pathnames <i>dirname</i>/<i>locale</i>/<i>category</i>/<i>domainname</i>.mo, where <i>locale</i> is a locale name and <i>category</i> is a locale facet such as <code>LC_MESSAGES</code>. </p>
<p> <i>domainname</i> must be a non-empty string. </p>
<p> If <i>dirname</i> is not NULL, the base directory for message catalogs belonging to domain <i>domainname</i> is set to <i>dirname</i>. The function makes copies of the argument strings as needed. If the program wishes to call the <code>chdir</code> function, it is important that <i>dirname</i> be an absolute pathname; otherwise it cannot be guaranteed that the message catalogs will be found. </p>
<p> If <i>dirname</i> is NULL, the function returns the previously set base directory for domain <i>domainname</i>.</p>
<h2>RETURN VALUE</h2>
<p> If successful, the <code>bindtextdomain</code> function returns the current base directory for domain <i>domainname</i>, after possibly changing it. The resulting string is valid until the next <code>bindtextdomain</code> call for the same <i>domainname</i> and must not be modified or freed. If a memory allocation failure occurs, it sets <code>errno</code> to <code>ENOMEM</code> and returns NULL.</p>
<h2>ERRORS</h2>
<p> The following error can occur, among others:</p>
<dl>
<dt><code>ENOMEM</code></p>
<dd> Not enough memory available.</dl>
<h2>BUGS</h2>
<p> The return type ought to be <code>const char *</code>, but is <code>char *</code> to avoid warnings in C code predating ANSI C.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-gettext/">gettext</a></code>(3), <code><a href="/docs/linux/man/3-dgettext/">dgettext</a></code>(3), <code><a href="/docs/linux/man/3-dcgettext/">dcgettext</a></code>(3), <code><a href="/docs/linux/man/3-ngettext/">ngettext</a></code>(3), <code><a href="/docs/linux/man/3-dngettext/">dngettext</a></code>(3), <code><a href="/docs/linux/man/3-dcngettext/">dcngettext</a></code>(3), <code><a href="/docs/linux/man/3-textdomain/">textdomain</a></code>(3), <code><a href="/docs/linux/man/3-realpath/">realpath</a></code>(3) </p>
<h2>Index</h2>
