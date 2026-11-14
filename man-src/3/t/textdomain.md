---
title: "textdomain(3)"
name: "textdomain"
section: "3"
letter: "t"
url: "/docs/linux/man/3-textdomain/"
description: "textdomain – set domain for future gettext() calls"
---

<p>textdomain &#8211; set domain for future gettext() calls</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;libintl.h&gt;

char *textdomain(const char *domainname);</code></pre>
<h2>Description</h2>
<p>The <code>textdomain</code> function sets or retrieves the current message domain. </p>
<p> A message domain is a set of translatable <i>msgid</i> messages. Usually, every software package has its own message domain. The domain name is used to determine the message catalog where a translation is looked up; it must be a non-empty string. </p>
<p> The current message domain is used by the <code>gettext</code>, <code>ngettext</code> functions, and by the <code>dgettext</code>, <code>dcgettext</code>, <code>dngettext</code> and <code>dcngettext</code> functions when called with a NULL domainname argument. </p>
<p> If <i>domainname</i> is not NULL, the current message domain is set to <i>domainname</i>. The string the function stores internally is a copy of the <i>domainname</i> argument. </p>
<p> If <i>domainname</i> is NULL, the function returns the current message domain.</p>
<h2>Return Value</h2>
<p>If successful, the <code>textdomain</code> function returns the current message domain, after possibly changing it. The resulting string is valid until the next <code>textdomain</code> call and must not be modified or freed. If a memory allocation failure occurs, it sets <code>errno</code> to <code>ENOMEM</code> and returns NULL.</p>
<h2>Errors</h2>
<p>The following error can occur, among others:</p>
<dl>
<dt><code>ENOMEM</code></p>
<dd>Not enough memory available.</dl>
<h2>Bugs</h2>
<p>The return type ought to be <code>const char *</code>, but is <code>char *</code> to avoid warnings in C code predating ANSI C.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-gettext/">gettext</a></code>(3), <code><a href="/docs/linux/man/3-ngettext/">ngettext</a></code>(3), <code><a href="/docs/linux/man/3-bindtextdomain/">bindtextdomain</a></code>(3), <code><a href="/docs/linux/man/3-bind_textdomain_codeset/">bind_textdomain_codeset</a></code>(3) </p>
