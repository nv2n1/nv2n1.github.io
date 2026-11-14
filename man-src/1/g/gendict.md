---
title: "gendict(1)"
name: "gendict"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gendict/"
description: "gendict – Compiles word list into ICU string trie dictionary"
---

<h2 class="name">NAME</h2>
<p> <code>gendict</code> &#8211; Compiles word list into ICU string trie dictionary </p>
<h2>SYNOPSIS</h2>
<p> <code>gendict</code> [ <code>&#8211;uchars</code> | <code>&#8211;bytes</code> <code>&#8211;transform</code><i> transform</i> ] [ <code>-h</code>, <code>-?</code>, <code>&#8211;help</code> ] [ <code>-V</code>, <code>&#8211;version</code> ] [ <code>-c</code>, <code>&#8211;copyright</code> ] [ <code>-v</code>, <code>&#8211;verbose</code> ] [ <code>-i</code>, <code>&#8211;icudatadir</code><i> directory</i> ] <i> input-file</i> <i> output-file</i></p>
<h2>DESCRIPTION</h2>
<p> <code>gendict</code> reads the word list from <i>dictionary-file</i> and creates a string trie dictionary file. Normally this data file has the <code>.dict</code> extension. </p>
<p> Words begin at the beginning of a line and are terminated by the first whitespace. Lines that begin with whitespace are ignored.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code>, <code>-?</code>, <code>&#8211;help</code></p>
<dd> Print help about usage and exit.</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd> Print the version of <code>gendict</code> and exit.</p>
<dt><code>-c</code>, <code>&#8211;copyright</code></p>
<dd> Embeds the standard ICU copyright into the <i>output-file</i>.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd> Display extra informative messages during execution.</p>
<dt><code>-i</code>, <code>&#8211;icudatadir</code><i> directory</i></p>
<dd> Look for any necessary ICU data files in <i>directory</i>. For example, the file <code>pnames.icu</code> must be located when ICU&#8217;s data is not built as a shared library. The default ICU data directory is specified by the environment variable <code>ICU_DATA</code>. Most configurations of ICU do not require this argument.</p>
<dt><code>&#8211;uchars</code></p>
<dd> Set the output trie type to UChar. Mutually exclusive with <code>&#8211;bytes.</code></p>
<dt><code>&#8211;bytes</code></p>
<dd> Set the output trie type to Bytes. Mutually exclusive with <code>&#8211;uchars.</code></p>
<dt><code>&#8211;transform</code></p>
<dd> Set the transform type. Should only be specified with <code>&#8211;bytes.</code> Currently supported transforms are: <code>offset-&lt;hex-number&gt;,</code> which specifies an offset to subtract from all input characters. It should be noted that the offset transform also maps U+200D to 0xFF and U+200C to 0xFE, in order to offer compatibility to languages that require these characters. A transform must be specified for a bytes trie, and when applied to the non-value characters in the <i>input-file</i> must produce output between 0x00 and 0xFF.</p>
<dt><code> input-file</code></p>
<dd> The source file to read.</p>
<dt><code> output-file</code></p>
<dd> The file to write the output dictionary to.</dl>
<h2>CAVEATS</h2>
<p> The <i>input-file</i> is assumed to be encoded in UTF-8. The integers in the <i>input-file</i> that are used as values must be made up of ASCII digits. They may be specified either in hex, by using a 0x prefix, or in decimal. Either <code>&#8211;bytes</code> or <code>&#8211;uchars</code> must be specified.</p>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>ICU_DATA</code></p>
<dd> Specifies the directory containing ICU data. Defaults to <code>${prefix}/share/icu/70.1/</code>. Some tools in ICU depend on the presence of the trailing slash. It is thus important to make sure that it is present if <code>ICU_DATA</code> is set.</dl>
<h2>AUTHORS</h2>
<p> Maxime Serrano</p>
<h2>VERSION</h2>
<p> 1.0</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2012 International Business Machines Corporation and others</p>
<h2>SEE ALSO</h2>
<p> <code><a rel="nofollow" href="http://www.icu-project.org/userguide/boundaryAnalysis.html">http://www.icu-project.org/userguide/boundaryAnalysis.html</a></code> </p>
<h2>Index</h2>
