---
title: "setlocale(3)"
name: "setlocale"
section: "3"
letter: "s"
url: "/docs/linux/man/3-setlocale/"
description: "setlocale – set the current locale"
---

<p>setlocale &#8211; set the current locale</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;locale.h&gt;

char *setlocale(int category, const char *locale);</code></pre>
<h2>Description</h2>
<p>The <code>setlocale</code>() function is used to set or query the program&#8217;s current locale. </p>
<p> If <i>locale</i> is not NULL, the program&#8217;s current locale is modified according to the arguments. The argument <i>category</i> determines which parts of the program&#8217;s current locale should be modified. </p>
<table>
<tr VALIGN=top>
<td><code>Category</code></td>
<td><code>Governs</code>
</td>
</tr>
<tr VALIGN=top>
<td><code>LC_ALL</code></td>
<td>All of the locale
</td>
</tr>
<tr VALIGN=top>
<td><code>LC_ADDRESS</code></td>
<td> Formatting of addresses and<br />
 geography-related items (*)
</td>
</tr>
<tr VALIGN=top>
<td><code>LC_COLLATE</code></td>
<td>String collation
</td>
</tr>
<tr VALIGN=top>
<td><code>LC_CTYPE</code></td>
<td>Character classification
</td>
</tr>
<tr VALIGN=top>
<td><code>LC_IDENTIFICATION</code></td>
<td>Metadata describing the locale (*)
</td>
</tr>
<tr VALIGN=top>
<td><code>LC_MEASUREMENT</code></td>
<td> Settings related to measurements<br />
 (metric versus US customary) (*)
</td>
</tr>
<tr VALIGN=top>
<td><code>LC_MESSAGES</code></td>
<td>Localizable natural-language messages
</td>
</tr>
<tr VALIGN=top>
<td><code>LC_MONETARY</code></td>
<td>Formatting of monetary values
</td>
</tr>
<tr VALIGN=top>
<td><code>LC_NAME</code></td>
<td>Formatting of salutations for persons (*)
</td>
</tr>
<tr VALIGN=top>
<td><code>LC_NUMERIC</code></td>
<td>Formatting of nonmonetary numeric values
</td>
</tr>
<tr VALIGN=top>
<td><code>LC_PAPER</code></td>
<td>Settings related to the standard paper size (*)
</td>
</tr>
<tr VALIGN=top>
<td><code>LC_TELEPHONE</code></td>
<td>Formats to be used with telephone services (*)
</td>
</tr>
<tr VALIGN=top>
<td><code>LC_TIME</code></td>
<td>Formatting of date and time values
</td>
</tr>
</table>
<p> The categories marked with an asterisk in the above table are GNU extensions. For further information on these locale categories, see <code><a href="/docs/linux/man/7-locale/">locale</a></code>(7). </p>
<p> The argument <i>locale</i> is a pointer to a character string containing the required setting of <i>category</i>. Such a string is either a well-known constant like &quot;C&quot; or &quot;da_DK&quot; (see below), or an opaque string that was returned by another call of <code>setlocale</code>(). </p>
<p> If <i>locale</i> is an empty string, <code>&quot;&quot;</code>, each part of the locale that should be modified is set according to the environment variables. The details are implementation-dependent. For glibc, first (regardless of <i>category</i>), the environment variable <code>LC_ALL</code> is inspected, next the environment variable with the same name as the category (see the table above), and finally the environment variable <code>LANG</code>. The first existing environment variable is used. If its value is not a valid locale specification, the locale is unchanged, and <code>setlocale</code>() returns NULL. </p>
<p> The locale <code>C</code> or <code>POSIX</code> is a portable locale; it exists on all conforming systems. </p>
<p> A locale name is typically of the form <i>language</i>[_<i>territory</i>][.<i>codeset</i>][@<i>modifier</i>], where <i>language</i> is an ISO 639 language code, <i>territory</i> is an ISO 3166 country code, and <i>codeset</i> is a character set or encoding identifier like <code>ISO-8859-1</code> or <code>UTF-8</code>. For a list of all supported locales, try &quot;locale -a&quot; (see <code><a href="/docs/linux/man/1-locale/">locale</a></code>(1)). </p>
<p> If <i>locale</i> is NULL, the current locale is only queried, not modified. </p>
<p> On startup of the main program, the portable <code>C</code> locale is selected as default. A program may be made portable to all locales by calling: </p>
<p> setlocale(LC_ALL, &quot;&quot;); </p>
<p> after program initialization, by using the values returned from a <code><a href="/docs/linux/man/3-localeconv/">localeconv</a></code>(3) call for locale-dependent information, by using the multibyte and wide character functions for text processing if <code>MB_CUR_MAX &gt; 1</code>, and by using <code><a href="/docs/linux/man/3-strcoll/">strcoll</a></code>(3), <code><a href="/docs/linux/man/3-wcscoll/">wcscoll</a></code>(3) or <code><a href="/docs/linux/man/3-strxfrm/">strxfrm</a></code>(3), <code><a href="/docs/linux/man/3-wcsxfrm/">wcsxfrm</a></code>(3) to compare strings.</p>
<h2>Return Value</h2>
<p>A successful call to <code>setlocale</code>() returns an opaque string that corresponds to the locale set. This string may be allocated in static storage. The string returned is such that a subsequent call with that string and its associated category will restore that part of the process&#8217;s locale. The return value is NULL if the request cannot be honored.</p>
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
<td> <code>setlocale</code>() </td>
<td>Thread safety</td>
<td>MT-Unsafe const:locale env
</td>
</tr>
</table>
<h2>Conforming To</h2>
<p>POSIX.1-2001, POSIX.1-2008, C89, C99. </p>
<p> The C standards specify only the categories <code>LC_ALL</code>, <code>LC_COLLATE</code>, <code>LC_CTYPE</code>, <code>LC_MONETARY</code>, <code>LC_NUMERIC</code>, and <code>LC_TIME</code>. POSIX.1 adds <code>LC_MESSAGES</code>. The remaining categories are GNU extensions.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-locale/">locale</a></code>(1), <code><a href="/docs/linux/man/1-localedef/">localedef</a></code>(1), <code><a href="/docs/linux/man/3-isalpha/">isalpha</a></code>(3), <code><a href="/docs/linux/man/3-localeconv/">localeconv</a></code>(3), <code><a href="/docs/linux/man/3-nl_langinfo/">nl_langinfo</a></code>(3), <code><a href="/docs/linux/man/3-rpmatch/">rpmatch</a></code>(3), <code><a href="/docs/linux/man/3-strcoll/">strcoll</a></code>(3), <code><a href="/docs/linux/man/3-strftime/">strftime</a></code>(3), <code><a href="/docs/linux/man/7-charsets/">charsets</a></code>(7), <code><a href="/docs/linux/man/7-locale/">locale</a></code>(7)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
