---
title: "uconv(1)"
name: "uconv"
section: "1"
letter: "u"
url: "/docs/linux/man/1-uconv/"
description: "uconv – convert data from one encoding to another"
---
<h2 class="name">NAME</h2>
<p> <code>uconv</code> - convert data from one encoding to another </p>
<h2>SYNOPSIS</h2>
<p> <code>uconv</code> [ <code>-h</code>, <code>-?</code>, <code>--help</code> ] [ <code>-V</code>, <code>--version</code> ] [ <code>-s</code>, <code>--silent</code> ] [ <code>-v</code>, <code>--verbose</code> ] [ <code>-l</code>, <code>--list</code> | <code>-l</code>, <code>--list-code</code><i> code</i> | <code>--default-code</code> | <code>-L</code>, <code>--list-transliterators</code> ] [ <code>--canon</code> ] [ <code>-x</code><i> transliteration</i> ] [ <code>--to-callback</code><i> callback</i> | <code>-c</code> ] [ <code>--from-callback</code><i> callback</i> | <code>-i</code> ] [ <code>--callback</code><i> callback</i> ] [ <code>--fallback</code> | <code>--no-fallback</code> ] [ <code>-b</code>, <code>--block-size</code><i> size</i> ] [ <code>-f</code>, <code>--from-code</code><i> encoding</i> ] [ <code>-t</code>, <code>--to-code</code><i> encoding</i> ] [ <code>--add-signature</code> ] [ <code>--remove-signature</code> ] [ <code>-o</code>, <code>--output</code><i> file</i> ] [ <i>file</i>... ]  </p>
<h2>DESCRIPTION</h2>
<p> <code>uconv</code> converts, or transcodes, each given <i>file</i> (or its standard input if no <i>file</i> is specified) from one <i>encoding</i> to another. The transcoding is done using Unicode as a pivot encoding (i.e. the data are first transcoded from their original encoding to Unicode, and then from Unicode to the destination encoding). </p>
<p> If an <i>encoding</i> is not specified or is <code>-</code>, the default encoding is used. Thus, calling <code>uconv</code> with no <i>encoding</i> provides an easy way to validate and sanitize data files for further consumption by tools requiring data in the default encoding. </p>
<p> When calling <code>uconv</code>, it is possible to specify callbacks that are used to handle invalid characters in the input, or characters that cannot be transcoded to the destination encoding. Some encodings, for example, offer a default substitution character that can be used to represent the occurrence of such characters in the input. Other callbacks offer a useful visual representation of the invalid data. </p>
<p> <code>uconv</code> can also run the specified <i>transliteration</i> on the transcoded data, in which case transliteration will happen as an intermediate step, after the data have been transcoded to Unicode. The <i>transliteration</i> can be either a list of semicolon-separated transliterator names, or an arbitrarily complex set of rules in the ICU transliteration rules format. </p>
<p> For transcoding purposes, <code>uconv</code> options are compatible with those of <code><a href="/docs/linux/man/1-iconv/">iconv</a></code>(1), making it easy to replace it in scripts. It is not necessarily the case, however, that the encoding names used by <code>uconv</code> and ICU are the same as the ones used by <code><a href="/docs/linux/man/1-iconv/">iconv</a></code>(1). Also, options that provide informational data, such as the <code>-l</code>, <code>--list</code> one offered by some <code><a href="/docs/linux/man/1-iconv/">iconv</a></code>(1) variants such as GNU&#8217;s, produce data in a slightly different and easier to parse format.  </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code>, <code>-?</code>, <code>--help</code></dt>
<dd> <p> Print help about usage and exit. </p>
 </dd>
<dt><code>-V</code>, <code>--version</code></dt>
<dd> <p> Print the version of <code>uconv</code> and exit. </p>
 </dd>
<dt><code>-s</code>, <code>--silent</code></dt>
<dd> <p> Suppress messages during execution. </p>
 </dd>
<dt><code>-v</code>, <code>--verbose</code></dt>
<dd> <p> Display extra informative messages during execution. </p>
 </dd>
<dt><code>-l</code>, <code>--list</code></dt>
<dd> <p> List all the available encodings and exit. </p>
 </dd>
<dt><code>-l</code>, <code>--list-code</code><i> code</i></dt>
<dd> <p> List only the <i>code</i> encoding and exit. If <i>code</i> is not a proper encoding, exit with an error. </p>
 </dd>
<dt><code>--default-code</code></dt>
<dd> <p> List only the name of the default encoding and exit. </p>
 </dd>
<dt><code>-L</code>, <code>--list-transliterators</code></dt>
<dd> <p> List all the available transliterators and exit. </p>
 </dd>
<dt><code>--canon</code></dt>
<dd> <p> If used with <code>-l</code>, <code>--list</code> or <code>--default-code</code>, the list of encodings is produced in a format compatible with <code>convrtrs.txt</code>(5). If used with <code>-L</code>, <code>--list-transliterators</code>, print only one transliterator name per line. </p>
 </dd>
<dt><code>-x</code><i> transliteration</i></dt>
<dd> <p> Run the given <i>transliteration</i> on the transcoded Unicode data, and use the transliterated data as input for the transcoding to the destination encoding. </p>
 </dd>
<dt><code>--to-callback</code><i> callback</i></dt>
<dd> <p> Use <i>callback</i> to handle characters that cannot be transcoded to the destination encoding. See section <code>CALLBACKS</code> for details on valid callbacks. </p>
 </dd>
<dt><code>-c</code></dt>
<dd> <p> Omit invalid characters from the output. Same as <code>--to-callback skip</code>. </p>
 </dd>
<dt><code>--from-callback</code><i> callback</i></dt>
<dd> <p> Use <i>callback</i> to handle characters that cannot be transcoded from the original encoding. See section <code>CALLBACKS</code> for details on valid callbacks. </p>
 </dd>
<dt><code>-i</code></dt>
<dd> <p> Ignore invalid sequences in the input. Same as <code>--from-callback skip</code>. </p>
 </dd>
<dt><code>--callback</code><i> callback</i></dt>
<dd> <p> Use <i>callback</i> to handle both characters that cannot be transcoded from the original encoding and characters that cannot be transcoded to the destination encoding. See section <code>CALLBACKS</code> for details on valid callbacks. </p>
 </dd>
<dt><code>--fallback</code></dt>
<dd> <p> Use the fallback mapping when transcoding from Unicode to the destination encoding. </p>
 </dd>
<dt><code>--no-fallback</code></dt>
<dd> <p> Do not use the fallback mapping when transcoding from Unicode to the destination encoding. This is the default. </p>
 </dd>
<dt><code>-b</code>, <code>--block-size</code><i> size</i></dt>
<dd> <p> Read input in blocks of <i>size</i> bytes at a time. The default block size is 4096. </p>
 </dd>
<dt><code>-f</code>, <code>--from-code</code><i> encoding</i></dt>
<dd> <p> Set the original encoding of the data to <i>encoding</i>. </p>
 </dd>
<dt><code>-t</code>, <code>--to-code</code><i> encoding</i></dt>
<dd> <p> Transcode the data to <i>encoding</i>. </p>
 </dd>
<dt><code>--add-signature</code></dt>
<dd> <p> Add a U+FEFF Unicode signature character (BOM) if the output charset supports it and does not add one anyway. </p>
 </dd>
<dt><code>--remove-signature</code></dt>
<dd> <p> Remove a U+FEFF Unicode signature character (BOM). </p>
 </dd>
<dt><code>-o</code>, <code>--output</code><i> file</i></dt>
<dd> <p> Write the transcoded data to <i>file</i>. </p>
 </dd></dl>
<h2>CALLBACKS</h2>
<p> <code>uconv</code> supports specifying callbacks to handle invalid data. Callbacks can be set for both directions of transcoding: from the original encoding to Unicode, with the <code>--from-callback</code> option, and from Unicode to the destination encoding, with the <code>--to-callback</code> option. </p>
<p> The following is a list of valid <i>callback</i> names, along with a description of their behavior. The list of callbacks actually supported by <code>uconv</code> is displayed when it is called with <code>-h</code>, <code>--help</code>. </p>
<dl>
<dt><code>substitute</code></dt>
<dd> <p> Write the encoding&#8217;s substitute sequence, or the Unicode replacement character <code>U+FFFD</code> when transcoding to Unicode. </p>
 </dd>
<dt><code>skip</code></dt>
<dd> <p> Ignore the invalid data. </p>
 </dd>
<dt><code>stop</code></dt>
<dd> <p> Stop with an error when encountering invalid data. This is the default callback. </p>
 </dd>
<dt><code>escape</code></dt>
<dd> <p> Same as <code>escape-icu</code>. </p>
 </dd>
<dt><code>escape-icu</code></dt>
<dd> <p> Replace the missing characters with a string of the format <code>%U</code><i>hhhh</i> for plane 0 characters, and <code>%U</code><i>hhhh</i>%U <i>hhhh</i> for planes 1 and above characters, where <i>hhhh</i> is the hexadecimal value of one of the UTF-16 code units representing the character. Characters from planes 1 and above are written as a pair of UTF-16 surrogate code units. </p>
 </dd>
<dt><code>escape-java</code></dt>
<dd> <p> Replace the missing characters with a string of the format <code>\u</code><i>hhhh</i> for plane 0 characters, and <code>\u</code><i>hhhh</i>\u <i>hhhh</i> for planes 1 and above characters, where <i>hhhh</i> is the hexadecimal value of one of the UTF-16 code units representing the character. Characters from planes 1 and above are written as a pair of UTF-16 surrogate code units. </p>
 </dd>
<dt><code>escape-c</code></dt>
<dd> <p> Replace the missing characters with a string of the format <code>\u</code><i>hhhh</i> for plane 0 characters, and <code>\U</code><i>hhhhhhhh</i> for planes 1 and above characters, where <i>hhhh</i> and <i>hhhhhhhh</i> are the hexadecimal values of the Unicode codepoint. </p>
 </dd>
<dt><code>escape-xml</code></dt>
<dd> <p> Same as <code>escape-xml-hex</code>. </p>
 </dd>
<dt><code>escape-xml-hex</code></dt>
<dd> <p> Replace the missing characters with a string of the format <code>&amp;#x</code><i>hhhh</i>;, where <i>hhhh</i> is the hexadecimal value of the Unicode codepoint. </p>
 </dd>
<dt><code>escape-xml-dec</code></dt>
<dd> <p> Replace the missing characters with a string of the format <code>&amp;#</code><i>nnnn</i>;, where <i>nnnn</i> is the decimal value of the Unicode codepoint. </p>
 </dd>
<dt><code>escape-unicode</code></dt>
<dd> <p> Replace the missing characters with a string of the format <code>{U+</code><i>hhhh</i>}, where <i>hhhh</i> is the hexadecimal value of the Unicode codepoint. That hexadecimal string is of variable length and can use from 4 to 6 digits. This is the format universally used to denote a Unicode codepoint in the literature, delimited by curly braces for easy recognition of those substitutions in the output. </p>
 </dd></dl>
<h2>EXAMPLES</h2>
<p> Convert data from a given <i>encoding</i> to the platform encoding: </p>
<dl>
<dd> <p> $ uconv -f <i>encoding</i> </p>
 </dd></dl>
<p> Check if a <i>file</i> contains valid data for a given <i>encoding</i>: </p>
<dl>
<dd> <p> $ uconv -f <i>encoding</i> -c <i>file</i> &gt;/dev/null </p>
 </dd></dl>
<p> Convert a UTF-8 <i>file</i> to a given <i>encoding</i> and ensure that the resulting text is good for any version of HTML: </p>
<dl>
<dd> <p> $ uconv -f utf-8 -t <i>encoding</i> \ <br />
 <code> --callback escape-xml-dec </code><i>file</i> </p>
 </dd></dl>
<p> Display the names of the Unicode code points in a UTF-file: </p>
<dl>
<dd> <p> $ uconv -f utf-8 -x any-name <i>file</i> </p>
 </dd></dl>
<p> Print the name of a Unicode code point whose value is known (<code>U+30AB</code> in this example): </p>
<dl>
<dd> <p> $ echo &#8216;\u30ab&#8217; | uconv -x &#8216;hex-any; any-name&#8217;; echo <br />
 {KATAKANA LETTER KA}{LINE FEED} <br />
 $ </p>
 </dd></dl>
<p> (The names are delimited by curly braces. Also, the name of the line terminator is also displayed.) </p>
<p> Normalize UTF-8 data using Unicode NFKC, remove all control characters, and map Katakana to Hiragana: </p>
<dl>
<dd> <p> $ uconv -f utf-8 -t utf-8 \ <br />
 <code> -x &#8216;::nfkc; [:Cc:] &gt;; ::katakana-hiragana;&#8216;</code> </p>
 </dd></dl>
<h2>CAVEATS AND BUGS</h2>
<p> <code>uconv</code> does report errors as occurring at the first invalid byte encountered. This may be confusing to users of GNU <code><a href="/docs/linux/man/1-iconv/">iconv</a></code>(1), which reports errors as occurring at the first byte of an invalid sequence. For multi-byte character sets or encodings, this means that <code>uconv</code> error positions may be at a later offset in the input stream than would be the case with GNU <code><a href="/docs/linux/man/1-iconv/">iconv</a></code>(1). </p>
<p> The reporting of error positions when a transliterator is used may be inaccurate or unavailable, in which case <code>uconv</code> will report the offset in the output stream at which the error occurred.  </p>
<h2>AUTHORS</h2>
<p> Jonas Utterstroem <br />
 Yves Arrouye  </p>
<h2>VERSION</h2>
<p> 70.1  </p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2000-2005 IBM, Inc. and others.  </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-iconv/">iconv</a></code>(1) </p>
<h2>Index</h2>
<dl>
<dt><a href="#lbAB">NAME</a></dt>
<dd>  </dd>
<dt><a href="#lbAC">SYNOPSIS</a></dt>
<dd>  </dd>
<dt><a href="#lbAD">DESCRIPTION</a></dt>
<dd>  </dd>
<dt><a href="#lbAE">OPTIONS</a></dt>
<dd>  </dd>
<dt><a href="#lbAF">CALLBACKS</a></dt>
<dd>  </dd>
<dt><a href="#lbAG">EXAMPLES</a></dt>
<dd>  </dd>
<dt><a href="#lbAH">CAVEATS AND BUGS</a></dt>
<dd>  </dd>
<dt><a href="#lbAI">AUTHORS</a></dt>
<dd>  </dd>
<dt><a href="#lbAJ">VERSION</a></dt>
<dd>  </dd>
<dt><a href="#lbAK">COPYRIGHT</a></dt>
<dd>  </dd>
<dt><a href="#lbAL">SEE ALSO</a></dt>
<dd>  </dd></dl>
