---
title: "gettext(3)"
name: "gettext"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gettext/"
description: "gettext, dgettext, dcgettext – translate message"
---

<h2 class="name">NAME</h2>
<p> gettext, dgettext, dcgettext &#8211; translate message </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;libintl.h&gt;
char *gettext(const char *msgid);
char *dgettext(const char *domainname, const char *msgid);
char *dcgettext(const char *domainname, const char *msgid,
                int category);
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>gettext</code>, <code>dgettext</code> and <code>dcgettext</code> functions attempt to translate a text string into the user&#8217;s native language, by looking up the translation in a message catalog. </p>
<p> The <i>msgid</i> argument identifies the message to be translated. By convention, it is the English version of the message, with non-ASCII characters replaced by ASCII approximations. This choice allows the translators to work with message catalogs, called PO files, that contain both the English and the translated versions of each message, and can be installed using the <code>msgfmt</code> utility. </p>
<p> A message domain is a set of translatable <i>msgid</i> messages. Usually, every software package has its own message domain. The domain name is used to determine the message catalog where the translation is looked up; it must be a non-empty string. For the <code>gettext</code> function, it is specified through a preceding <code>textdomain</code> call. For the <code>dgettext</code> and <code>dcgettext</code> functions, it is passed as the <i>domainname</i> argument; if this argument is NULL, the domain name specified through a preceding <code>textdomain</code> call is used instead. </p>
<p> Translation lookup operates in the context of the current locale. For the <code>gettext</code> and <code>dgettext</code> functions, the <code>LC_MESSAGES</code> locale facet is used. It is determined by a preceding call to the <code>setlocale</code> function. <code>setlocale(LC_ALL,&quot;&quot;)</code> initializes the <code>LC_MESSAGES</code> locale based on the first nonempty value of the three environment variables <code>LC_ALL</code>, <code>LC_MESSAGES</code>, <code>LANG</code>; see <code><a href="/docs/linux/man/3-setlocale/">setlocale</a></code>(3). For the <code>dcgettext</code> function, the locale facet is determined by the <i>category</i> argument, which should be one of the <code>LC_xxx</code> constants defined in the &lt;locale.h&gt; header, excluding <code>LC_ALL</code>. In both cases, the functions also use the <code>LC_CTYPE</code> locale facet in order to convert the translated message from the translator&#8217;s codeset to the current locale&#8217;s codeset, unless overridden by a prior call to the <code>bind_textdomain_codeset</code> function. </p>
<p> The message catalog used by the functions is at the pathname <i>dirname</i>/<i>locale</i>/<i>category</i>/<i>domainname</i>.mo. Here <i>dirname</i> is the directory specified through <code>bindtextdomain</code>. Its default is system and configuration dependent; typically it is <i>prefix</i>/share/locale, where <i>prefix</i> is the installation prefix of the package. <i>locale</i> is the name of the current locale facet; the GNU implementation also tries generalizations, such as the language name without the territory name. <i>category</i> is <code>LC_MESSAGES</code> for the <code>gettext</code> and <code>dgettext</code> functions, or the argument passed to the <code>dcgettext</code> function. </p>
<p> If the <code>LANGUAGE</code> environment variable is set to a nonempty value, and the locale is not the &quot;C&quot; locale, the value of <code>LANGUAGE</code> is assumed to contain a colon separated list of locale names. The functions will attempt to look up a translation of <i>msgid</i> in each of the locales in turn. This is a GNU extension. </p>
<p> In the &quot;C&quot; locale, or if none of the used catalogs contain a translation for <i>msgid</i>, the <code>gettext</code>, <code>dgettext</code> and <code>dcgettext</code> functions return <i>msgid</i>.</p>
<h2>RETURN VALUE</h2>
<p> If a translation was found in one of the specified catalogs, it is converted to the locale&#8217;s codeset and returned. The resulting string is statically allocated and must not be modified or freed. Otherwise <i>msgid</i> is returned.</p>
<h2>ERRORS</h2>
<p> <code>errno</code> is not modified.</p>
<h2>BUGS</h2>
<p> The return type ought to be <code>const char *</code>, but is <code>char *</code> to avoid warnings in C code predating ANSI C. </p>
<p> When an empty string is used for <i>msgid</i>, the functions may return a nonempty string.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-ngettext/">ngettext</a></code>(3), <code><a href="/docs/linux/man/3-dngettext/">dngettext</a></code>(3), <code><a href="/docs/linux/man/3-dcngettext/">dcngettext</a></code>(3), <code><a href="/docs/linux/man/3-setlocale/">setlocale</a></code>(3), <code><a href="/docs/linux/man/3-textdomain/">textdomain</a></code>(3), <code><a href="/docs/linux/man/3-bindtextdomain/">bindtextdomain</a></code>(3), <code><a href="/docs/linux/man/3-bind_textdomain_codeset/">bind_textdomain_codeset</a></code>(3), <code><a href="/docs/linux/man/1-msgfmt/">msgfmt</a></code>(1) </p>
<h2>Index</h2>
