---
title: "dngettext(3)"
name: "dngettext"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dngettext/"
description: "ngettext, dngettext, dcngettext – translate message and choose plural form"
---

<h2 class="name">NAME</h2>
<p> ngettext, dngettext, dcngettext &#8211; translate message and choose plural form </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;libintl.h&gt;
char *ngettext(const char *msgid, const char *msgid_plural,
               unsigned long int n);
char *dngettext(const char *domainname,
                const char *msgid, const char *msgid_plural,
                unsigned long int n);
char *dcngettext(const char *domainname,
                 const char *msgid, const char *msgid_plural,
                 unsigned long int n, int category);
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>ngettext</code>, <code>dngettext</code> and <code>dcngettext</code> functions attempt to translate a text string into the user&#8217;s native language, by looking up the appropriate plural form of the translation in a message catalog. </p>
<p> Plural forms are grammatical variants depending on the a number. Some languages have two forms, called singular and plural. Other languages have three forms, called singular, dual and plural. There are also languages with four forms. </p>
<p> The <code>ngettext</code>, <code>dngettext</code> and <code>dcngettext</code> functions work like the <code>gettext</code>, <code>dgettext</code> and <code>dcgettext</code> functions, respectively. Additionally, they choose the appropriate plural form, which depends on the number <i>n</i> and the language of the message catalog where the translation was found. </p>
<p> In the &quot;C&quot; locale, or if none of the used catalogs contain a translation for <i>msgid</i>, the <code>ngettext</code>, <code>dngettext</code> and <code>dcngettext</code> functions return <i>msgid</i> if <i>n</i> == 1, or <i>msgid_plural</i> if <i>n</i> != 1.</p>
<h2>RETURN VALUE</h2>
<p> If a translation was found in one of the specified catalogs, the appropriate plural form is converted to the locale&#8217;s codeset and returned. The resulting string is statically allocated and must not be modified or freed. Otherwise <i>msgid</i> or <i>msgid_plural</i> is returned, as described above.</p>
<h2>ERRORS</h2>
<p> <code>errno</code> is not modified.</p>
<h2>BUGS</h2>
<p> The return type ought to be <code>const char *</code>, but is <code>char *</code> to avoid warnings in C code predating ANSI C.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-gettext/">gettext</a></code>(3), <code><a href="/docs/linux/man/3-dgettext/">dgettext</a></code>(3), <code><a href="/docs/linux/man/3-dcgettext/">dcgettext</a></code>(3) </p>
<h2>Index</h2>
