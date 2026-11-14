---
title: "strfmon_l(3)"
name: "strfmon_l"
section: "3"
letter: "s"
url: "/docs/linux/man/3-strfmon_l/"
description: "strfmon, strfmon_l – convert monetary value to a string"
---

<p>strfmon, strfmon_l &#8211; convert monetary value to a string</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;monetary.h&gt;

ssize_t strfmon(char *s, size_t max, const char *format, ...);

ssize_t strfmon_l(char *s, size_t max, locale_t locale,
                  const char *format, ...);</code></pre>
<h2>Description</h2>
<p>The <code>strfmon</code>() function formats the specified monetary amount according to the current locale and format specification <i>format</i> and places the result in the character array <i>s</i> of size <i>max</i>. </p>
<p> The <code>strfmon_l</code>() function performs the same task, but uses the locale specified by <i>locale</i>. The behavior of <code>strfmon_l</code>() is undefined if <i>locale</i> is the special locale object <code>LC_GLOBAL_LOCALE</code> (see <code><a href="/docs/linux/man/3-duplocale/">duplocale</a></code>(3)) or is not a valid locale object handle. </p>
<p> Ordinary characters in <i>format</i> are copied to <i>s</i> without conversion. Conversion specifiers are introduced by a &#8216;%&#8217; character. Immediately following it there can be zero or more of the following flags:</p>
<dl>
<dt><code>=</code><i>f</i></p>
<dd>The single-byte character <i>f</i> is used as the numeric fill character (to be used with a left precision, see below). When not specified, the space character is used.</p>
<dt><code>ha</code></p>
<dd>Do not use any grouping characters that might be defined for the current locale. By default, grouping is enabled.</p>
<dt><code>(</code> or <code>+</code></p>
<dd>The ( flag indicates that negative amounts should be enclosed between parentheses. The + flag indicates that signs should be handled in the default way, that is, amounts are preceded by the locale&#8217;s sign indication, for example, nothing for positive, &quot;-&quot; for negative.</p>
<dt><code>!</code></p>
<dd>Omit the currency symbol.</p>
<dt><code>&#8211;</code></p>
<dd>Left justify all fields. The default is right justification.</dl>
<p> Next, there may be a field width: a decimal digit string specifying a minimum field width in bytes. The default is 0. A result smaller than this width is padded with spaces (on the left, unless the left-justify flag was given). </p>
<p> Next, there may be a left precision of the form &quot;#&quot; followed by a decimal digit string. If the number of digits left of the radix character is smaller than this, the representation is padded on the left with the numeric fill character. Grouping characters are not counted in this field width. </p>
<p> Next, there may be a right precision of the form &quot;.&quot; followed by a decimal digit string. The amount being formatted is rounded to the specified number of digits prior to formatting. The default is specified in the <i>frac_digits</i> and <i>int_frac_digits</i> items of the current locale. If the right precision is 0, no radix character is printed. (The radix character here is determined by <code>LC_MONETARY</code>, and may differ from that specified by <code>LC_NUMERIC</code>.) </p>
<p> Finally, the conversion specification must be ended with a conversion character. The three conversion characters are</p>
<dl>
<dt><code>%</code></p>
<dd>(In this case, the entire specification must be exactly &quot;%%&quot;.) Put a &#8216;%&#8217; character in the result string.</p>
<dt><code>i</code></p>
<dd>One argument of type <i>double</i> is converted using the locale&#8217;s international currency format.</p>
<dt><code>n</code></p>
<dd>One argument of type <i>double</i> is converted using the locale&#8217;s national currency format.</dl>
<h2>Return Value</h2>
<p>The <code>strfmon</code>() function returns the number of characters placed in the array <i>s</i>, not including the terminating null byte, provided the string, including the terminating null byte, fits. Otherwise, it sets <i>errno</i> to <code>E2BIG</code>, returns -1, and the contents of the array is undefined.</p>
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
<td> <code>strfmon</code>() </td>
<td>Thread safety</td>
<td>MT-Safe locale
</td>
</tr>
<tr VALIGN=top>
<td> <code>strfmon_l</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>Conforming To</h2>
<p>POSIX.1-2001, POSIX.1-2008.</p>
<h2>Examples</h2>
<p>The call </p>
<pre><code>strfmon(buf, sizeof(buf), &quot;[%ha=*#6n] [%=*#6i]&quot;,
1234.567, 1234.567);</code></pre>
<p> outputs [€ **1234,57] [EUR **1 234,57] in the <i>nl_NL</i> locale. The <i>de_DE</i>, <i>de_CH</i>, <i>en_AU</i>, and <i>en_GB</i> locales yield [ **1234,57 €] [ **1.234,57 EUR] [ Fr. **1234.57] [ CHF **1&#8217;234.57] [ $**1234.57] [ AUD**1,234.57] [ £**1234.57] [ GBP**1,234.57]</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-duplocale/">duplocale</a></code>(3), <code><a href="/docs/linux/man/3-setlocale/">setlocale</a></code>(3), <code><a href="/docs/linux/man/3-sprintf/">sprintf</a></code>(3), <code><a href="/docs/linux/man/7-locale/">locale</a></code>(7)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
