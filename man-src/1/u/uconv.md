---
title: "uconv(1)"
name: "uconv"
section: "1"
letter: "u"
url: "/docs/linux/man/1-uconv/"
description: "uconv – convert data from one encoding to another"
---

<h2 class="name">NAME</h2>
<p> <code>uconv</code> &#8211; convert data from one encoding to another </p>
<h2>SYNOPSIS</h2>
<p> <code>uconv</code> [ <code>-h</code>, <code>-?</code>, <code>&#8211;help</code> ] [ <code>-V</code>, <code>&#8211;version</code> ] [ <code>-s</code>, <code>&#8211;silent</code> ] [ <code>-v</code>, <code>&#8211;verbose</code> ] [ <code>-l</code>, <code>&#8211;list</code> | <code>-l</code>, <code>&#8211;list-code</code><i> code</i> | <code>&#8211;default-code</code> | <code>-L</code>, <code>&#8211;list-transliterators</code> ] [ <code>&#8211;canon</code> ] [ <code>-x</code><i> transliteration</i> ] [ <code>&#8211;to-callback</code><i> callback</i> | <code>-c</code> ] [ <code>&#8211;from-callback</code><i> callback</i> | <code>-i</code> ] [ <code>&#8211;callback</code><i> callback</i> ] [ <code>&#8211;fallback</code> | <code>&#8211;no-fallback</code> ] [ <code>-b</code>, <code>&#8211;block-size</code><i> size</i> ] [ <code>-f</code>, <code>&#8211;from-code</code><i> encoding</i> ] [ <code>-t</code>, <code>&#8211;to-code</code><i> encoding</i> ] [ <code>&#8211;add-signature</code> ] [ <code>&#8211;remove-signature</code> ] [ <code>-o</code>, <code>&#8211;output</code><i> file</i> ] [ <i>file</i>&#8230; ]</p>
<h2>DESCRIPTION</h2>
<p> <code>uconv</code> converts, or transcodes, each given <i>file</i> (or its standard input if no <i>file</i> is specified) from one <i>encoding</i> to another. The transcoding is done using Unicode as a pivot encoding (i.e. the data are first transcoded from their original encoding to Unicode, and then from Unicode to the destination encoding). </p>
<p> If an <i>encoding</i> is not specified or is <code>&#8211;</code>, the default encoding is used. Thus, calling <code>uconv</code> with no <i>encoding</i> provides an easy way to validate and sanitize data files for further consumption by tools requiring data in the default encoding. </p>
<p> When calling <code>uconv</code>, it is possible to specify callbacks that are used to handle invalid characters in the input, or characters that cannot be transcoded to the destination encoding. Some encodings, for example, offer a default substitution character that can be used to represent the occurrence of such characters in the input. Other callbacks offer a useful visual representation of the invalid data. </p>
<p> <code>uconv</code> can also run the specified <i>transliteration</i> on the transcoded data, in which case transliteration will happen as an intermediate step, after the data have been transcoded to Unicode. The <i>transliteration</i> can be either a list of semicolon-separated transliterator names, or an arbitrarily complex set of rules in the ICU transliteration rules format. </p>
<p> For transcoding purposes, <code>uconv</code> options are compatible with those of <code><a href="/docs/linux/man/1-iconv/">iconv</a></code>(1), making it easy to replace it in scripts. It is not necessarily the case, however, that the encoding names used by <code>uconv</code> and ICU are the same as the ones used by <code><a href="/docs/linux/man/1-iconv/">iconv</a></code>(1). Also, options that provide informational data, such as the <code>-l</code>, <code>&#8211;list</code> one offered by some <code><a href="/docs/linux/man/1-iconv/">iconv</a></code>(1) variants such as GNU&#8217;s, produce data in a slightly different and easier to parse format.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code>, <code>-?</code>, <code>&#8211;help</code></p>
<dd> Print help about usage and exit.</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd> Print the version of <code>uconv</code> and exit.</p>
<dt><code>-s</code>, <code>&#8211;silent</code></p>
<dd> Suppress messages during execution.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd> Display extra informative messages during execution.</p>
<dt><code>-l</code>, <code>&#8211;list</code></p>
<dd> List all the available encodings and exit.</p>
<dt><code>-l</code>, <code>&#8211;list-code</code><i> code</i></p>
<dd> List only the <i>code</i> encoding and exit. If <i>code</i> is not a proper encoding, exit with an error.</p>
<dt><code>&#8211;default-code</code></p>
<dd> List only the name of the default encoding and exit.</p>
<dt><code>-L</code>, <code>&#8211;list-transliterators</code></p>
<dd> List all the available transliterators and exit.</p>
<dt><code>&#8211;canon</code></p>
<dd> If used with <code>-l</code>, <code>&#8211;list</code> or <code>&#8211;default-code</code>, the list of encodings is produced in a format compatible with <code><a href="/docs/linux/man/5-convrtrs-txt/">convrtrs.txt</a></code>(5). If used with <code>-L</code>, <code>&#8211;list-transliterators</code>, print only one transliterator name per line.</p>
<dt><code>-x</code><i> transliteration</i></p>
<dd> Run the given <i>transliteration</i> on the transcoded Unicode data, and use the transliterated data as input for the transcoding to the destination encoding.</p>
<dt><code>&#8211;to-callback</code><i> callback</i></p>
<dd> Use <i>callback</i> to handle characters that cannot be transcoded to the destination encoding. See section <code>CALLBACKS</code> for details on valid callbacks.</p>
<dt><code>-c</code></p>
<dd> Omit invalid characters from the output. Same as <code>&#8211;to-callback skip</code>.</p>
<dt><code>&#8211;from-callback</code><i> callback</i></p>
<dd> Use <i>callback</i> to handle characters that cannot be transcoded from the original encoding. See section <code>CALLBACKS</code> for details on valid callbacks.</p>
<dt><code>-i</code></p>
<dd> Ignore invalid sequences in the input. Same as <code>&#8211;from-callback skip</code>.</p>
<dt><code>&#8211;callback</code><i> callback</i></p>
<dd> Use <i>callback</i> to handle both characters that cannot be transcoded from the original encoding and characters that cannot be transcoded to the destination encoding. See section <code>CALLBACKS</code> for details on valid callbacks.</p>
<dt><code>&#8211;fallback</code></p>
<dd> Use the fallback mapping when transcoding from Unicode to the destination encoding.</p>
<dt><code>&#8211;no-fallback</code></p>
<dd> Do not use the fallback mapping when transcoding from Unicode to the destination encoding. This is the default.</p>
<dt><code>-b</code>, <code>&#8211;block-size</code><i> size</i></p>
<dd> Read input in blocks of <i>size</i> bytes at a time. The default block size is 4096.</p>
<dt><code>-f</code>, <code>&#8211;from-code</code><i> encoding</i></p>
<dd> Set the original encoding of the data to <i>encoding</i>.</p>
<dt><code>-t</code>, <code>&#8211;to-code</code><i> encoding</i></p>
<dd> Transcode the data to <i>encoding</i>.</p>
<dt><code>&#8211;add-signature</code></p>
<dd> Add a U+FEFF Unicode signature character (BOM) if the output charset supports it and does not add one anyway.</p>
<dt><code>&#8211;remove-signature</code></p>
<dd> Remove a U+FEFF Unicode signature character (BOM).</p>
<dt><code>-o</code>, <code>&#8211;output</code><i> file</i></p>
<dd> Write the transcoded data to <i>file</i>.</dl>
<h2>CALLBACKS</h2>
<p> <code>uconv</code> supports specifying callbacks to handle invalid data. Callbacks can be set for both directions of transcoding: from the original encoding to Unicode, with the <code>&#8211;from-callback</code> option, and from Unicode to the destination encoding, with the <code>&#8211;to-callback</code> option. </p>
<p> The following is a list of valid <i>callback</i> names, along with a description of their behavior. The list of callbacks actually supported by <code>uconv</code> is displayed when it is called with <code>-h</code>, <code>&#8211;help</code>. </p>
<dl>
<dt><code>substitute</code></p>
<dd> Write the encoding&#8217;s substitute sequence, or the Unicode replacement character <code>U+FFFD</code> when transcoding to Unicode.</p>
<dt><code>skip</code></p>
<dd> Ignore the invalid data.</p>
<dt><code>stop</code></p>
<dd> Stop with an error when encountering invalid data. This is the default callback.</p>
<dt><code>escape</code></p>
<dd> Same as <code>escape-icu</code>.</p>
<dt><code>escape-icu</code></p>
<dd> Replace the missing characters with a string of the format <code>%U</code><i>hhhh</i> for plane 0 characters, and <code>%U</code><i>hhhh</i>%U<i>hhhh</i> for planes 1 and above characters, where <i>hhhh</i> is the hexadecimal value of one of the UTF-16 code units representing the character. Characters from planes 1 and above are written as a pair of UTF-16 surrogate code units.</p>
<dt><code>escape-java</code></p>
<dd> Replace the missing characters with a string of the format <code>
