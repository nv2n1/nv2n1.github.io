---
title: "nl_langinfo(3)"
name: "nl_langinfo"
section: "3"
letter: "n"
url: "/docs/linux/man/3-nl_langinfo/"
description: "nl_langinfo, nl_langinfo_l – query language and locale information"
---

<p>nl_langinfo, nl_langinfo_l &#8211; query language and locale information</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;langinfo.h&gt;

char *nl_langinfo(nl_item item);

char *nl_langinfo_l(nl_item item, locale_t locale);</code></pre>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): <code>nl_langinfo_l</code>():</p>
<dl>
<dd>Since glibc 2.24:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;_POSIX_C_SOURCE&nbsp;&gt;=&nbsp;200809L<br />
 Glibc 2.23 and earlier:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;_POSIX_C_SOURCE&nbsp;&gt;=&nbsp;200112L</dl>
<h2>Description</h2>
<p>The <code>nl_langinfo</code>() and <code>nl_langinfo_l</code>() functions provide access to locale information in a more flexible way than <code><a href="/docs/linux/man/3-localeconv/">localeconv</a></code>(3). <code>nl_langinfo</code>() returns a string which is the value corresponding to <i>item</i> in the program&#8217;s current global locale. <code>nl_langinfo_l</code>() returns a string which is the value corresponding to <i>item</i> for the locale identified by the locale object <i>locale</i>, which was previously created by <code><a href="/docs/linux/man/1-newlocale/">newlocale</a></code>(1). Individual and additional elements of the locale categories can be queried. <code><a href="/docs/linux/man/3-setlocale/">setlocale</a></code>(3) needs to be executed with proper arguments before. </p>
<p> Examples for the locale elements that can be specified in <i>item</i> using the constants defined in <i>&lt;langinfo.h&gt;</i> are:</p>
<dl>
<dt><code>CODESET</code>&nbsp;(LC_CTYPE)</p>
<dd>Return a string with the name of the character encoding used in the selected locale, such as &quot;UTF-8&quot;, &quot;ISO-8859-1&quot;, or &quot;ANSI_X3.4-1968&quot; (better known as US-ASCII). This is the same string that you get with &quot;locale charmap&quot;. For a list of character encoding names, try &quot;locale -m&quot; (see <code><a href="/docs/linux/man/1-locale/">locale</a></code>(1)).</p>
<dt><code>D_T_FMT</code>&nbsp;(LC_TIME)</p>
<dd>Return a string that can be used as a format string for <code><a href="/docs/linux/man/3-strftime/">strftime</a></code>(3) to represent time and date in a locale-specific way (<code>%c</code> conversion specification).</p>
<dt><code>D_FMT</code>&nbsp;(LC_TIME)</p>
<dd>Return a string that can be used as a format string for <code><a href="/docs/linux/man/3-strftime/">strftime</a></code>(3) to represent a date in a locale-specific way (<code>%x</code> conversion specification).</p>
<dt><code>T_FMT</code>&nbsp;(LC_TIME)</p>
<dd>Return a string that can be used as a format string for <code><a href="/docs/linux/man/3-strftime/">strftime</a></code>(3) to represent a time in a locale-specific way (<code>%X</code> conversion specification).</p>
<dt><code>AM_STR</code>&nbsp;(LC_TIME)</p>
<dd>Return a string that represents affix for ante meridiem (before noon, &quot;AM&quot;) time. (Used in <code>%p</code> <code><a href="/docs/linux/man/3-strftime/">strftime</a></code>(3) conversion specification.)</p>
<dt><code>PM_STR</code>&nbsp;(LC_TIME)</p>
<dd>Return a string that represents affix for post meridiem (before midnight, &quot;PM&quot;) time. (Used in <code>%p</code> <code><a href="/docs/linux/man/3-strftime/">strftime</a></code>(3) conversion specification.)</p>
<dt><code>T_FMT_AMPM</code>&nbsp;(LC_TIME)</p>
<dd>Return a string that can be used as a format string for <code><a href="/docs/linux/man/3-strftime/">strftime</a></code>(3) to represent a time in a.m. or p.m. notation a locale-specific way (<code>%r</code> conversion specification).</p>
<dt><code>ERA</code>&nbsp;(LC_TIME)</p>
<dd>Return era description, which contains information about how years are counted and displayed for each era in a locale. Each era description segment shall have the format:</p>
<dl>
<dd>
<dl>
<dd><i>direction</i>:<i>offset</i>:<i>start_date</i>:<i>end_date</i>:<i>era_name</i>:<i>era_format</i></dl>
</dl>
<dd>according to the definitions below:</p>
<dl>
<dd>
<dl>
<dt><i>direction</i></p>
<dd>Either a &quot;<code>+</code>&quot; or a &quot;<code>&#8211;</code>&quot; character. The &quot;<code>+</code>&quot; means that years increase from the <i>start_date</i> towards the <i>end_date</i>, &quot;<code>&#8211;</code>&quot; means the opposite.</p>
<dt><i>offset</i></p>
<dd>The epoch year of the <i>start_date</i>.</p>
<dt><i>start_date</i></p>
<dd>A date in the form <i>yyyy</i>/<i>mm</i>/<i>dd</i>, where <i>yyyy</i>, <i>mm</i>, and <i>dd</i> are the year, month, and day numbers respectively of the start of the era.</p>
<dt><i>end_date</i></p>
<dd>The ending date of the era, in the same format as the <i>start_date</i>, or one of the two special values &quot;<code>-*</code>&quot; (minus infinity) or &quot;<code>+*</code>&quot; (plus infinity).</p>
<dt><i>era_name</i></p>
<dd>The name of the era, corresponding to the <code>%EC</code> <code><a href="/docs/linux/man/3-strftime/">strftime</a></code>(3) conversion specification.</p>
<dt><i>era_format</i></p>
<dd>The format of the year in the era, corresponding to the <code>%EY</code> <code><a href="/docs/linux/man/3-strftime/">strftime</a></code>(3) conversion specification.</dl>
</dl>
<dd>Era description segments are separated by semicolons. Most locales do not define this value. Examples of locales that do define this value are the Japanese and Thai locales.</p>
<dt><code>ERA_D_T_FMT</code>&nbsp;(LC_TIME)</p>
<dd>Return a string that can be used as a format string for <code><a href="/docs/linux/man/3-strftime/">strftime</a></code>(3) for alternative representation of time and date in a locale-specific way (<code>%Ec</code> conversion specification).</p>
<dt><code>ERA_D_FMT</code>&nbsp;(LC_TIME)</p>
<dd>Return a string that can be used as a format string for <code><a href="/docs/linux/man/3-strftime/">strftime</a></code>(3) for alternative representation of a date in a locale-specific way (<code>%Ex</code> conversion specification).</p>
<dt><code>ERA_T_FMT</code>&nbsp;(LC_TIME)</p>
<dd>Return a string that can be used as a format string for <code><a href="/docs/linux/man/3-strftime/">strftime</a></code>(3) for alternative representation of a time in a locale-specific way (<code>%EX</code> conversion specification).</p>
<dt><code>DAY_</code>{1-7} (LC_TIME)</p>
<dd>Return name of the <i>n</i>-th day of the week. [Warning: this follows the US convention DAY_1 = Sunday, not the international convention (ISO 8601) that Monday is the first day of the week.] (Used in <code>%A</code> <code><a href="/docs/linux/man/3-strftime/">strftime</a></code>(3) conversion specification.)</p>
<dt><code>ABDAY_</code>{1-7} (LC_TIME)</p>
<dd>Return abbreviated name of the <i>n</i>-th day of the week. (Used in <code>%a</code> <code><a href="/docs/linux/man/3-strftime/">strftime</a></code>(3) conversion specification.)</p>
<dt><code>MON_</code>{1-12} (LC_TIME)</p>
<dd>Return name of the <i>n</i>-th month. (Used in <code>%B</code> <code><a href="/docs/linux/man/3-strftime/">strftime</a></code>(3) conversion specification.)</p>
<dt><code>ABMON_</code>{1-12} (LC_TIME)</p>
<dd>Return abbreviated name of the <i>n</i>-th month. (Used in <code>%b</code> <code><a href="/docs/linux/man/3-strftime/">strftime</a></code>(3) conversion specification.)</p>
<dt><code>RADIXCHAR</code>&nbsp;(LC_NUMERIC)</p>
<dd>Return radix character (decimal dot, decimal comma, etc.).</p>
<dt><code>THOUSEP</code>&nbsp;(LC_NUMERIC)</p>
<dd>Return separator character for thousands (groups of three digits).</p>
<dt><code>YESEXPR</code>&nbsp;(LC_MESSAGES)</p>
<dd>Return a regular expression that can be used with the <code><a href="/docs/linux/man/3-regex/">regex</a></code>(3) function to recognize a positive response to a yes/no question.</p>
<dt><code>NOEXPR</code>&nbsp;(LC_MESSAGES)</p>
<dd>Return a regular expression that can be used with the <code><a href="/docs/linux/man/3-regex/">regex</a></code>(3) function to recognize a negative response to a yes/no question.</p>
<dt><code>CRNCYSTR</code>&nbsp;(LC_MONETARY)</p>
<dd>Return the currency symbol, preceded by &quot;-&quot; if the symbol should appear before the value, &quot;+&quot; if the symbol should appear after the value, or &quot;.&quot; if the symbol should replace the radix character.</dl>
<p> The above list covers just some examples of items that can be requested. For a more detailed list, consult <i>The GNU C Library Reference Manual</i>.</p>
<h2>Return Value</h2>
<p>On success, these functions return a pointer to a string which is the value corresponding to <i>item</i> in the specified locale. </p>
<p> If no locale has been selected by <code><a href="/docs/linux/man/3-setlocale/">setlocale</a></code>(3) for the appropriate category, <code>nl_langinfo</code>() return a pointer to the corresponding string in the &quot;C&quot; locale. The same is true of <code>nl_langinfo_l</code>() if <i>locale</i> specifies a locale where <i>langinfo</i> data is not defined. </p>
<p> If <i>item</i> is not valid, a pointer to an empty string is returned. </p>
<p> The pointer returned by these functions may point to static data that may be overwritten, or the pointer itself may be invalidated, by a subsequent call to <code>nl_langinfo</code>(), <code>nl_langinfo_l</code>(), or <code><a href="/docs/linux/man/3-setlocale/">setlocale</a></code>(3). The same statements apply to <code>nl_langinfo_l</code>() if the locale object referred to by <i>locale</i> is freed or modified by <code><a href="/docs/linux/man/3-freelocale/">freelocale</a></code>(3) or <code><a href="/docs/linux/man/3-newlocale/">newlocale</a></code>(3). </p>
<p> POSIX specifies that the application may not modify the string returned by these functions.</p>
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
<td> <code>nl_langinfo</code>() </td>
<td>Thread safety</td>
<td>MT-Safe locale
</td>
</tr>
</table>
<h2>Conforming To</h2>
<p>POSIX.1-2001, POSIX.1-2008, SUSv2.</p>
<h2>Notes</h2>
<p>The behavior of <code>nl_langinfo_l</code>() is undefined if <i>locale</i> is the special locale object <code>LC_GLOBAL_LOCALE</code> or is not a valid locale object handle.</p>
<h2>Examples</h2>
<p>The following program sets the character type and the numeric locale according to the environment and queries the terminal character set and the radix character. </p>
<pre><code>#include &lt;langinfo.h&gt;
#include &lt;locale.h&gt;
#include &lt;stdio.h&gt;
#include &lt;stdlib.h&gt;
int main(int argc, char *argv[])
{
    setlocale(LC_CTYPE, &quot;&quot;);
    setlocale(LC_NUMERIC, &quot;&quot;);
    printf(&quot;%s
&quot;, nl_langinfo(CODESET));
    printf(&quot;%s
&quot;, nl_langinfo(RADIXCHAR));
    exit(EXIT_SUCCESS);
}</code></pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-locale/">locale</a></code>(1), <code><a href="/docs/linux/man/3-localeconv/">localeconv</a></code>(3), <code><a href="/docs/linux/man/3-setlocale/">setlocale</a></code>(3), <code><a href="/docs/linux/man/7-charsets/">charsets</a></code>(7), <code><a href="/docs/linux/man/7-locale/">locale</a></code>(7) </p>
<p> The GNU C Library Reference Manual</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
