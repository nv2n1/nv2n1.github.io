---
title: "jfbterm(5)"
name: "jfbterm"
section: "5"
letter: "j"
url: "/docs/linux/man/5-jfbterm/"
description: "jfbterm.conf – configuration file for"
---

<p>jfbterm.conf &#8211; configuration file for </p>
<p><a href="/docs/linux/man/1-jfbterm/">jfbterm</a>(1)</p>
<h2>Description</h2>
<p>This manual page documents briefly the <code>jfbterm.conf</code> configuration file that is used in <code><a href="/docs/linux/man/1-jfbterm/">jfbterm</a></code>(1) command.</p>
<h2>Configurations</h2>
<p>The format of an entry for this file is:</p>
<dl>
<dt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><i>entryName</i> : <i>value</i></p>
<dd></dl>
<p> If `+&#8217; is at beginning of the line, <i>value</i> is added to<br />
 <i>entryName</i> as an array. This means that one <i>entryName</i> can have multiple <i>value</i>s. </p>
<p> A summary of configrations is included below.</p>
<dl>
<dd><code>term</code> TERM environment variable&#8217;s value for a program that runs in <code><a href="/docs/linux/man/1-jfbterm/">jfbterm</a></code>(1). The default is <code>jfbterm</code>.</p>
<dd><code>fontset</code> This assigns a font for each character set. A term &quot;character set&quot; means a set of characters and is an element for &quot;encodings&quot;. In other words, an encoding consists from one or more character sets. In jfbterm, most of character sets are assumed to have ISO-2022-compliant structure, i.e., a character set contains 94 characters, 96 characters, 94^N characters, or 96^N characters. <code>iso10646.1</code> is the only exception.</p>
<dd>The format of <code>fontset</code> value is: </p>
<pre> <i>charsetName</i>,<i>type</i>,<i>side</i>,<i>fontname</i></pre>
<p>You can see a list of available <i>charsetName</i>s by running &quot;jfbterm &#8211;help&quot;.</p>
<dd><i>type</i> specifies &quot;pcf&quot; or &quot;alias&quot;. If <i>type</i> is &quot;pcf&quot;, <i>fontname</i> is a pathname of a font file. If <i>type</i> is &quot;alias&quot;, <i>fontname</i> specifies another <i>charsetName</i>, which means that the character set of <i>charsetName</i> will use the same font to the character set of <i>fontname</i>.</p>
<dd><i>side</i> specifies in which side (GL or GR) the font has glyphs for the character set, in terms of ISO-2022. <code>L</code> means GL (0x20-0x7f) and <code>R</code> means GR (0xa0-0xff). A unique specification, <code>U</code>, is used only for iso10646.1.</p>
<dd>For example, <code>iso8859.1-1987</code> is a character set which contains 96 characters. The glyphs for iso8859.1-1987 characters are available in GR side of *-iso8859-1 fonts.</p>
<dd><code>encoding</code> This defines an encoding. An encoding is what you really use to express texts and consists from one or more character sets. In jfbterm, most of encodings are defined as ISO-2022&#8217;s initial state and jfbterm can change character sets by using ISO-2022 escape sequences. However, non-ISO-2022-compliant encodings such as Big5 and KOI8-R are also supported via <code><a href="/docs/linux/man/3-iconv/">iconv</a></code>(3).</p>
<dd>The format of <code>encoding</code> value is </p>
<pre> locale
or
 <i>encodingName</i>
or
 <i>GL</i>,<i>GR</i>,<i>G0</i>,<i>G1</i>,<i>G2</i>,<i>G3</i></pre>
<p>If <code>encoding</code> value is &quot;locale&quot; (the first case), then <i>encodingName</i> value is initialized by the current LC_CTYPE locale (&quot;locale -k charmap&quot;) and falling into the second case.</p>
<dd>If no `,&#8217; is found in <code>encoding</code> value, it is recognized as <i>encodingName</i> (the second case). If the <i>encodingName</i> matches one of <code>encoding.</code><i>encodingName</i> which is explained below, this definition is used. Otherwise, if the <i>encodingName</i> matches one of valid encoding names for <code><a href="/docs/linux/man/1-iconv/">iconv</a></code>(1) or <code><a href="/docs/linux/man/3-iconv_open/">iconv_open</a></code>(3), <code>jfbterm</code> will work in UTF-8 mode internally. This means that the font defined by <code>fontset:iso10646.1</code> line will be used and <code><a href="/docs/linux/man/3-iconv/">iconv</a></code>(3) will be used to emulate the given <i>encodingName</i>. This behavior is just as if there is a line: </p>
<pre> encoding.<i>encodingName</i> : other,<i>encodingName</i>,iconv,UTF-8</pre>
<p>This mechanism enables <code>jfbterm</code> to support various encodings which are not ISO-2022-compliant.</p>
<dd>If a `,&#8217; is found in <code>encoding</code> value, it is recognized as the third case. This format defines an encoding as an ISO-2022 initial state. <i>GL</i> and <i>GR</i> specifies a slot (one of <code>G0</code>, <code>G1</code>, <code>G2</code>, or <code>G3</code>) which is invoked into GL (0x20-0x7F) and GR (0xA0-0xFF). <i>G0</i>, <i>G1</i>, <i>G2</i>, and <i>G3</i> specifies the character set which is designated into the corresponding slot.</p>
<dd>The default is &quot;locale&quot;.</p>
<dd><code>encoding.</code><i>encodingName</i> This defines an encoding of <i>encodingName</i> as an ISO-2022 initial state, like the third case of <code>encoding</code> item which is explained already. The format is like following: </p>
<pre> <i>GL</i>,<i>GR</i>,<i>G0</i>,<i>G1</i>,<i>G2</i>,<i>G3</i>
or
 UTF-8,iso10646.1
or
 other,<i>encodingName</i>,iconv,<i>internal-encodingName</i></pre>
<p>The first case is just same as explained in the third case of <code>encoding</code> item.</p>
<dd>The second case means that the encoding is UTF-8. This is a special case.</p>
<dd>The third case defines an encoding as a conversion of an other encoding. <code>jfbterm</code> will use the encoding of <i>internal-encodingName</i> internally and will use <code><a href="/docs/linux/man/3-iconv/">iconv</a></code>(3) for conversion.</p>
<dd>Note that, in the third case, <i>internal-encodingName</i> must be a valid encoding name which is defined in other <code>encoding.</code><i>encodingName</i> line (which has the first or second format). Both of <i>internal-encodingName</i> and <i>encodingName</i> must be valid encoding names for <code><a href="/docs/linux/man/1-iconv/">iconv</a></code>(1) or <code><a href="/docs/linux/man/3-iconv_open/">iconv_open</a></code>(3). Also, Both <i>encodingName</i>s (one is a part of <code>encoding.</code><i>encodingName</i> and the another appears next to &quot;other,&quot;) must be same.</p>
<dd><code>color.gamma</code> Color gamma value. The default is 1.7.</dl>
<h2>Files</h2>
<dl>
<dt><i>/etc/jfbterm.conf</i></p>
<dd>Configuration file for <code><a href="/docs/linux/man/1-jfbterm/">jfbterm</a></code>(1).</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-jfbterm/">jfbterm</a></code>(1), <code><a href="/docs/linux/man/1-locale/">locale</a></code>(1), <code><a href="/docs/linux/man/3-iconv/">iconv</a></code>(3).</p>
<h2>Author</h2>
<p>This manual page was written by Fumitoshi UKAI &lt;ukai [at] debian.or.jp&gt;.</p>
