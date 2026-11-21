---

title: "piconv(1)"
name: "piconv"
section: "1"
letter: "p"
url: "/docs/linux/man/1-piconv/"
description: "piconv —"
---

<p> <a href="/docs/linux/man/1-iconv/">iconv</a>(1), reinvented in perl  </p>
<pre><code>  piconv [-f from_encoding] [-t to_encoding]
         [-p|--perlqq|--htmlcref|--xmlcref] [-C N|-c] [-D] [-S scheme]
         [-s string|file...]
  piconv -l
  piconv -r encoding_alias
  piconv -h
</code></pre>
<p> <code>piconv</code> is perl version of <code>iconv</code>, a character encoding converter widely available for various Unixen today. This script was primarily a technology demonstrator for Perl 5.8.0, but you can use piconv in the place of iconv for virtually any case. </p>
<p> piconv converts the character encoding of either <font SIZE="-1">STDIN</font> or files specified in the argument and prints out to <font SIZE="-1">STDOUT.</font> </p>
<p> Here is the list of options. Some options can be in short format (-f) or long (--from) one. </p>
<dl>
<dt>-f,--from <i>from_encoding</i></dt>
<dd> <p> Specifies the encoding you are converting from. Unlike <code>iconv</code>, this option can be omitted. In such cases, the current locale is used. </p>
 </dd>
<dt>-t,--to <i>to_encoding</i></dt>
<dd> <p> Specifies the encoding you are converting to. Unlike <code>iconv</code>, this option can be omitted. In such cases, the current locale is used. </p>
<p> Therefore, when both -f and -t are omitted, <code>piconv</code> just acts like <code>cat</code>. </p>
 </dd>
<dt>-s,--string <i>string</i></dt>
<dd> <p> uses <i>string</i> instead of file for the source of text. </p>
 </dd>
<dt>-l,--list</dt>
<dd> <p> Lists all available encodings, one per line, in case-insensitive order. Note that only the canonical names are listed; many aliases exist. For example, the names are case-insensitive, and many standard and common aliases work, such as ``latin1&#8217;&#8216; for ``<font SIZE="-1">ISO-8859-1&#8217;&#8216;,</font> or ``ibm850&#8217;&#8216; instead of ``cp850&#8217;&#8216;, or ``winlatin1&#8217;&#8216; for ``cp1252&#8217;&#8216;. See Encode::Supported for a full discussion. </p>
 </dd>
<dt>-r,--resolve <i>encoding_alias</i></dt>
<dd> <p> Resolve <i>encoding_alias</i> to Encode canonical encoding name. </p>
 </dd>
<dt>-C,--check <i>N</i></dt>
<dd> <p> Check the validity of the stream if <i>N</i> = 1. When <i>N</i> = -1, something interesting happens when it encounters an invalid character. </p>
 </dd>
<dt>-c</dt>
<dd> <p> Same as <code>&quot;-C 1&quot;</code>. </p>
 </dd>
<dt>-p,--perlqq</dt>
<dd> <p> Transliterate characters missing in encoding to \x{<font SIZE="-1">HHHH</font>} where <font SIZE="-1">HHHH</font> is the hexadecimal Unicode code point. </p>
 </dd>
<dt>--htmlcref</dt>
<dd> <p> Transliterate characters missing in encoding to &amp;#NNN; where <font SIZE="-1">NNN</font> is the decimal Unicode code point. </p>
 </dd>
<dt>--xmlcref</dt>
<dd> <p> Transliterate characters missing in encoding to &amp;#xHHHH; where <font SIZE="-1">HHHH</font> is the hexadecimal Unicode code point. </p>
 </dd>
<dt>-h,--help</dt>
<dd> <p> Show usage. </p>
 </dd>
<dt>-D,--debug</dt>
<dd> <p> Invokes debugging mode. Primarily for Encode hackers. </p>
 </dd>
<dt>-S,--scheme <i>scheme</i></dt>
<dd> <p> Selects which scheme is to be used for conversion. Available schemes are as follows: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt>from_to</dt>
<dd> <p> Uses Encode::from_to for conversion. This is the default. </p>
 </dd>
<dt>decode_encode</dt>
<dd> <p> Input strings are <code>decode()</code>d then <code>encode()</code>d. A straight two-step implementation. </p>
 </dd>
<dt>perlio</dt>
<dd> <p> The new perlIO layer is used. <font SIZE="-1">NI-S</font>&#8216; favorite. </p>
<p> You should use this option if you are using <font SIZE="-1">UTF-16</font> and others which linefeed is not $/. </p>
 </dd></dl>
</dl>
<dl>
<dd> <p> Like the <i>-D</i> option, this is also for Encode hackers. </p>
 </dd></dl>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-iconv/">iconv</a></code>(1) <code>locale</code>(3) Encode Encode::Supported Encode::Alias PerlIO </p>
