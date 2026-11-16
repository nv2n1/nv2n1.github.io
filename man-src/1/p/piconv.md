---
title: "piconv(1)"
name: "piconv"
section: "1"
letter: "p"
url: "/docs/linux/man/1-piconv/"
description: "piconv —"
---

<h2 class="name">NAME</h2>
<p> piconv &#8212; </p>
<p> <a href="/docs/linux/man/1-iconv/">iconv</a>(1), reinvented in perl</p>
<h2>SYNOPSIS</h2>
<pre><code>
piconv[-f from_encoding][-t to_encoding]
      [-p | --perlqq | --htmlcref | --xmlcref][-C N | -c][-D][-S scheme]
      [-s string | file...] piconv -
    l
        piconv -
    r encoding_alias
        piconv -
    h
</code></pre>
<h2>DESCRIPTION</h2>
<p> <code>piconv</code> is perl version of <code>iconv</code>, a character encoding converter widely available for various Unixen today. This script was primarily a technology demonstrator for Perl 5.8.0, but you can use piconv in the place of iconv for virtually any case. </p>
<p> piconv converts the character encoding of either <font SIZE="-1">STDIN</font> or files specified in the argument and prints out to <font SIZE="-1">STDOUT.</font> </p>
<p> Here is the list of options. Some options can be in short format (-f) or long (&#8211;from) one.</p>
<dl>
<dt>-f,&#8211;from <i>from_encoding</i></dt>
<dd> Specifies the encoding you are converting from. Unlike <code>iconv</code>, this option can be omitted. In such cases, the current locale is used.</dd>
<dt>-t,&#8211;to <i>to_encoding</i></dt>
<dd> Specifies the encoding you are converting to. Unlike <code>iconv</code>, this option can be omitted. In such cases, the current locale is used. </dd>
<p> Therefore, when both -f and -t are omitted, <code>piconv</code> just acts like <code>cat</code>.</p>
<dt>-s,&#8211;string <i>string</i></dt>
<dd> uses <i>string</i> instead of file for the source of text.</dd>
<dt>-l,&#8211;list</dt>
<dd> Lists all available encodings, one per line, in case-insensitive order. Note that only the canonical names are listed; many aliases exist. For example, the names are case-insensitive, and many standard and common aliases work, such as &#8220;latin1&#8221; for &#8220;<font SIZE="-1">ISO-8859-1&#8221;,</font> or &#8220;ibm850&#8221; instead of &#8220;cp850&#8221;, or &#8220;winlatin1&#8221; for &#8220;cp1252&#8221;. See Encode::Supported for a full discussion.</dd>
<dt>-r,&#8211;resolve <i>encoding_alias</i></dt>
<dd> Resolve <i>encoding_alias</i> to Encode canonical encoding name.</dd>
<dt>-C,&#8211;check <i>N</i></dt>
<dd> Check the validity of the stream if <i>N</i> = 1. When <i>N</i> = -1, something interesting happens when it encounters an invalid character.</dd>
<dt>-c</dt>
<dd> Same as <tt>&quot;-C 1&quot;</tt>.</dd>
<dt>-p,&#8211;perlqq</dt>
<dd> Transliterate characters missing in encoding to 
</dd></dl>