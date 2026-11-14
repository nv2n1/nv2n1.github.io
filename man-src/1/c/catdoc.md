---
title: "catdoc(1)"
name: "catdoc"
section: "1"
letter: "c"
url: "/docs/linux/man/1-catdoc/"
description: "catdoc – reads MS-Word file and puts its content as plain text on standard output"
---

<h2>NAME</h2>
<p> catdoc &#8211; reads MS-Word file and puts its content as plain text on standard output</p>
<h2>SYNOPSIS</h2>
<p> <code>catdoc</code> [<code>-vlu8btawxV</code>] [<code>-m</code> <i>number</i>] [ <code>-s</code> <i>charset</i>] [ <code>-d </code> <i>charset</i>] [ <code>-f</code> <i>output-format</i>] <i>file</i> </p>
<h2>DESCRIPTION</h2>
<p> <code>catdoc</code> behaves much like <code><a href="/docs/linux/man/1-cat/">cat</a></code>(1) but it reads MS-Word file and produces human-readable text on standard output. Optionally it can use <code><a href="/docs/linux/man/1-latex/">latex</a></code>(1) escape sequences for characters which have special meaning for LaTeX. It also makes some effort to recognize MS-Word tables, although it never tries to write correct headers for LaTeX tabular environment. Additional output formats, such is HTML can be easily defined. </p>
<p> <code>catdoc</code> doesn&#8217;t attempt to extract formatting information other than tables from MS-Word document, so different output modes means mainly that different characters should be escaped and different ways used to represent characters, missing from output charset. See CHARACTER SUBSTITUTION below </p>
<p> <code>catdoc</code> uses internal <code><a href="/docs/linux/man/4-unicode/">unicode</a></code>(4) representation of text, so it is able to convert texts when charset in source document doesn&#8217;t match charset on target system. See CHARACTER SETS below. </p>
<p> If no file names supplied, <code>catdoc</code> processes its standard input unless it is terminal. It is unlikely that somebody could type Word document from keyboard, so if <code>catdoc </code> invoked without arguments and stdin is not redirected, it prints brief usage message and exits. Processing of standard input (even among other files) can be forced using dash &#8216;-&#8216; as file name. </p>
<p> By default, <code>catdoc</code> wraps lines which are more than 72 chars long and separates paragraphs by blank lines. This behavior can be turned of by <code>-w</code> switch. In <i>wide</i> mode <code>catdoc prints each paragraph as one long line, suitable for import into</code> word processors which perform word wrapping theirselves.<br />
&nbsp;<wbr> </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-a </code></p>
<dd> &#8211; shortcut for -f ascii. Produces ASCII text as output. Separates table columns with TAB</p>
<dt><code>-b</code></p>
<dd> &#8211; process broken MS-Word file. Normally, <code>catdoc checks if first 8 bytes</code> of file is Microsoft OLE signature. If so, it processes file, otherwise it just copies it to stdin. It is intended to use <code>catdoc </code> as filter for viewing all files with <i>.doc</i> extension.</p>
<dt><code>-d</code><i>charset</i></p>
<dd> &#8211; specifies destination charset name. Charset file has format described in CHARACTER SETS below and should have <code>.txt</code> extension and reside in <code>catdoc library directory ( /usr/lib64/catdoc). By default, current</code> locale charset is used if langinfo support compiled in.</p>
<dt><code>-f</code><i>format</i></p>
<dd> &#8211; specifies output format as described in CHARACTER SUBSTITUTION below. <code>catdoc</code> comes with two output formats &#8211; ascii and tex. You can add your own if you wish.</p>
<dt><code>-l</code></p>
<dd> Causes <code>catdoc</code> to list names of available charsets to the stdout and exit successfully.</p>
<dt><code>-m</code><i>number</i></p>
<dd> Specifies right margin for text (default 72). <code>-m 0</code> is equivalent to <code>-w</code></p>
<dt><code>-s</code><i>charset</i></p>
<dd> Specifies source charset. (one used in Word document), if Word document doesn&#8217;t contain UTF-16 text. When reading rtf documents, it is typically not necessary, because rtf documents contain ansicpg specification. But it can be set wrong by Word (I&#8217;ve seen RTF documents on Russian, where cp1252 was specified). In this case this option would take precedence over charset, specified in the document. But source_charset statement in the configuration file have less priority than charset in the document.</p>
<dt><code>-t</code></p>
<dd> &#8211; shortcut for <code>-f tex</code><br />
&nbsp;<wbr>converts all printable chars, which have special meaning for&nbsp;<wbr> <code><a href="/docs/linux/man/1-latex/">LaTeX</a></code>(1) into appropriate control sequences. Separates table columns by <code>&amp;.</code></p>
<dt><code>-u</code></p>
<dd> &#8211; declares that Word document contain UNICODE (UTF-16) representation of text (as some Word-97 documents). If catdoc fails to correct Word document with default charset, try this option.</p>
<dt><code>-8</code></p>
<dd> &#8211; declares is Word document is 8 bit. Just in case that catdoc<br />
&nbsp;<wbr>recognizes file format incorrectly.</p>
<dt><code>-w</code></p>
<dd> disables word wrapping. By default <code>catdoc</code> output is splitted into lines not longer than 72 (or number, specified by -m option) characters and paragraphs are separated by blank line. With this option each paragraph is one long line.</p>
<dt><code>-x</code></p>
<dd> causes catdoc to output unknown UNICODE character as 
