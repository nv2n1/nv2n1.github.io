---

title: "genctd(1)"
name: "genctd"
section: "1"
letter: "g"
url: "/docs/linux/man/1-genctd/"
description: "genctd – Compiles word list into ICU compact trie dictionary"
---

<h2>NAME</h2>
<p> <code>genctd</code> &#8211; Compiles word list into ICU compact trie dictionary</p>
<p> <code>genctd</code> [ <code>-h</code>, <code>-?</code>, <code>&#8211;help</code> ] [ <code>-V</code>, <code>&#8211;version</code> ] [ <code>-c</code>, <code>&#8211;copyright</code> ] [ <code>-v</code>, <code>&#8211;verbose</code> ] [ <code>-d</code>, <code>&#8211;destdir</code><i> destination</i> ] [ <code>-i</code>, <code>&#8211;icudatadir</code><i> directory</i> ] <code>-o</code>, <code>&#8211;out</code><i> output-file</i> <i> dictionary-file</i></p>
<p> <code>genctd</code> reads the word list from <i>dictionary-file</i> and creates a compact trie dictionary file. Normally this data file has the <code>.ctd</code> extension. </p>
<p> Words begin at the beginning of a line and are terminated by the first whitespace. Lines that begin with whitespace are ignored.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code>, <code>-?</code>, <code>&#8211;help</code></dt>
<dd> Print help about usage and exit.</dd>
<dt><code>-V</code>, <code>&#8211;version</code></dt>
<dd> Print the version of <code>genctd</code> and exit.</dd>
<dt><code>-c</code>, <code>&#8211;copyright</code></dt>
<dd> Embeds the standard ICU copyright into the <i>output-file</i>.</dd>
<dt><code>-v</code>, <code>&#8211;verbose</code></dt>
<dd> Display extra informative messages during execution.</dd>
<dt><code>-d</code>, <code>&#8211;destdir</code><i> destination</i></dt>
<dd> Set the destination directory of the <i>output-file</i> to <i>destination</i>.</dd>
<dt><code>-i</code>, <code>&#8211;icudatadir</code><i> directory</i></dt>
<dd> Look for any necessary ICU data files in <i>directory</i>. For example, the file <code>pnames.icu</code> must be located when ICU&#8217;s data is not built as a shared library. The default ICU data directory is specified by the environment variable <code>ICU_DATA</code>. Most configurations of ICU do not require this argument.</dd>
<dt><code> dictionary-file</code></dt>
<dd> The source file to read.</dd>
<dt><code>-o</code>, <code>&#8211;out</code><i> output-file</i></dt>
<dd> The output data file to write.</dd></dl>
<h2>CAVEATS</h2>
<p> When the <i>dictionary-file</i> contains a byte order mark (BOM) at the beginning of the file, which is the Unicode character <code>U+FEFF,</code> then the <i>dictionary-file</i> is interpreted as Unicode. Without the BOM, the file is interpreted in the current operating system default codepage. In order to eliminate any ambiguity of the encoding for how the <i>rule-file</i> was written, it is recommended that you write this file in UTF-8 with the BOM.</p>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>ICU_DATA</code></dt>
<dd> Specifies the directory containing ICU data. Defaults to <code>/usr/share/icu/4.2.1/</code>. Some tools in ICU depend on the presence of the trailing slash. It is thus important to make sure that it is present if <code>ICU_DATA</code> is set.</dd></dl>
<h2>AUTHORS</h2>
<p> Deborah Goldsmith</p>
<h2>VERSION</h2>
<p> 1.0</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2006 International Business Machines Corporation and others</p>
<h2>SEE ALSO</h2>
<p> <code><a rel="nofollow" href="http://www.icu-project.org/userguide/boundaryAnalysis.html">http://www.icu-project.org/userguide/boundaryAnalysis.html</a></code> </p>
