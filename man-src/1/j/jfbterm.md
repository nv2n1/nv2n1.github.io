---
title: "jfbterm(1)"
name: "jfbterm"
section: "1"
letter: "j"
url: "/docs/linux/man/1-jfbterm/"
description: "jfbterm – program to print several character sets on framebuffer device."
---

<h2 class="name">NAME</h2>
<p> jfbterm &#8211; program to print several character sets on framebuffer device. </p>
<h2>SYNOPSIS</h2>
<p> <code>jfbterm</code> [<i>options</i>]</p>
<h2>DESCRIPTION</h2>
<p> This manual page documents briefly the <code>jfbterm</code> command. </p>
<p> <code>jfbterm</code> is a program that prints various encodings such as UTF-8, ISO-8859-*, EUC-*, and so on, on Linux framebuffer device, like KON that prints on VGA device. It supports ISO-2022-compliant character sets, encodings which consist from such character sets, UTF-8, and encodings which <code><a href="/docs/linux/man/3-iconv/">iconv</a></code>(3) can convert from/to UTF-8. In GNU libc systems, all encodings which are available for <code><a href="/docs/linux/man/3-iconv/">iconv</a></code>(3) meet this condition and are available. </p>
<p> This supports fullwidth characters (which occupies two columns, like CJK Ideogram, Hiragana, Katakana, and Hangul). However, this doesn&#8217;t support combining characters nor BIDI.</p>
<h2>OPTIONS</h2>
<p> This program follows the usual GNU command line syntax, with long options starting with two dashes (`-&#8216;). A summary of options is included below.</p>
<dl>
<dt><code>-h, &#8211;help</code></p>
<dd> Show summary of current configuration.</p>
<dt><code>-e, &#8211;exec, &#8211;shell</code></p>
<dd> Specify a program that run in jfbterm. Default is $SHELL (or /bin/sh). Rest of arguments will be passed to the specified program.</p>
<dt><code>-f, &#8211;config</code></p>
<dd> Specify a pathname of the configuration file. Default is /etc/jfbterm.conf.</p>
<dt><code>-c, &#8211;encoding, &#8211;charmap</code></p>
<dd> Specify the encoding. The format is same as <code>encoding</code> line of <code><a href="/docs/linux/man/5-jfbterm-conf/">jfbterm.conf</a></code>(5) file.</p>
<dt>
<dd> When the given string is &quot;locale&quot; (the first format), the encoding specified by LC_CTYPE locale is adopted.</p>
<dt>
<dd> When the given string doesn&#8217;t contain `,&#8217; (the second format), the string is assumed as an encoding name. A valid encoding name is either a name defined in encoding.<i>encodingName</i> line in <code><a href="/docs/linux/man/5-jfbterm-conf/">jfbterm.conf</a></code>(5) or a name which is valid for <code><a href="/docs/linux/man/1-iconv/">iconv</a></code>(1) or <code><a href="/docs/linux/man/3-iconv_open/">iconv_open</a></code>(3).</p>
<dt>
<dd> When the given string contains a `,&#8217; (the third format), the string is assumed to have <i>GL</i>,<i>GR</i>,<i>G0</i>,<i>G1</i>,<i>G2</i>,<i>G3</i> format. See <code><a href="/docs/linux/man/5-jfbterm-conf/">jfbterm.conf</a></code>(5) for detail.</p>
<dt><code>-r, &#8211;reset</code></p>
<dd> Output ISO-2022 initialize sequence to tty. You can specify codeset name as optional argument like: <code>&#8211;reset=</code><i>encodingName</i>. Default is locale&#8217;s codeset.</p>
<dt><code>-q, &#8211;quiet</code></p>
<dd> Don&#8217;t print out messages.</dl>
<h2>NOTES</h2>
<p> Since version 0.3.14, default encoding has been changed from EUC-JP to encoding for locale. To make it enable to display EUC-JP, run </p>
<pre>
        $ jfbterm --reset=EUC-JP
or
        $ export LANG=ja_JP.eucJP
        $ jfbterm -r
</pre>
<p> if you have already invoked jfbterm and are on it. If you have not invoked jfbterm and want to invoke it now, set LANG variable before invoking jfbterm.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/5-jfbterm-conf/">jfbterm.conf</a></code>(5).</p>
<h2>AUTHOR</h2>
<p> This manual page was written by Fumitoshi UKAI &lt;ukai [at] debian.or.jp&gt;. </p>
<h2>Index</h2>
