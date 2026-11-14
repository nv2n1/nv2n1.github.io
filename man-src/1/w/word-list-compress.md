---
title: "word-list-compress(1)"
name: "word-list-compress"
section: "1"
letter: "w"
url: "/docs/linux/man/1-word-list-compress/"
description: "word-list-compress – word list compressor/decompressor for GNU Aspell"
---

<h2 class="name">NAME</h2>
<p> word-list-compress &#8211; word list compressor/decompressor for GNU Aspell </p>
<h2>SYNOPSIS</h2>
<p> <code>word-list-compress</code> <code>c</code>[<code>ompress</code>] | <code>d</code>[<code>ecompress</code>]</p>
<h2>DESCRIPTION</h2>
<p> <code>word-list-compress</code> compresses or decompresses sorted word lists for use with the GNU Aspell spell checker.</p>
<h2>COMMANDS</h2>
<dl>
<dt><code>-c</code>, <code>c</code>, <code>compress</code></p>
<dd> compress the plain text word list read from standard input.</p>
<dt><code>-d</code>, <code>d</code>, <code>decompress</code></p>
<dd> decompress the compressed word list read from standard input.</dl>
<h2>EXAMPLES</h2>
<p> Here are a few examples of how you can use <i>word-list-compress</i></p>
<dl>
<dt>word-list-compress <code>d</code> &lt;wordlist.cwl &gt;wordlist.txt</p>
<dd> Decompress file wordlist.cwl to text file wordlist.txt</p>
<dt>word-list-compress <code>c</code> &lt;wordlist.wl &gt;wordlist.cwl 2&gt;errors.txt</p>
<dd> Compress wordlist.wl to wordlist.cwl and send any error messages to a text file named errors.txt</p>
<dt>LC_COLLATE=C sort -u &lt;wordlist.txt <code>|</code> word-list-compress c &gt;wordlist.cwl</p>
<dd> Sort a word list, then pipe it to <i>word-list-compress</i> to create a compressed binary wordlist.cwl file.</p>
<dt>word-list-compress d &lt;words.cwl <code>|</code> aspell create master ./words.rws</p>
<dd> Decompress a wordlist, then pipe it to <i><a href="/docs/linux/man/1-aspell/">aspell</a>(1)</i> to create a spelling list. Please check the <i><a href="/docs/linux/man/1-aspell/">aspell</a>(1)</i> info manual for proper usage and options.</dl>
<h2>TIPS</h2>
<p> <i>Word-list-compress</i> is best used with sorted word list type files. It is not a general purpose compression program since the resulting files may actually increase in size. </p>
<p> <i>Word-list-compress</i> accepts up to 255 text characters in the range of {0x21&#8230;0xFF}. If your word list requires a larger character set for certain languages or longer length for multi-word, scientific, medical, technical or other use, then it is recommended that you compress your word list using <i><a href="/docs/linux/man/1-prezip-bin/">prezip-bin</a>(1)</i></p>
<h2>DIAGNOSTICS</h2>
<p> <i>Word-list-compress</i> normally exits with a return code of 0. If it encounters an error, a message is sent to standard error output (stderr), and <i>word-list-compress</i> exits with a non-zero return value. Error messages are listed below:</p>
<dl>
<dt><code>(display help/usage message)</code></p>
<dd> Unknown command given on the command line so <i>word-list-compress</i> displays a usage message to standard error output.</p>
<dt><code>Corrupt Input</code></p>
<dd> This is only for the decompression command <code>d</code>. The input file is of an unknown format or the input file/stream is corrupted. You may have some valid output, but <i>word-list-compress</i> could not complete the process. If the input file is a compressed wordlist but you have no output file, then it may be a newer <i><a href="/docs/linux/man/1-prezip-bin/">prezip-bin</a>(1)</i> version of compressed file, if so, try decompressing the file with <i><a href="/docs/linux/man/1-prezip-bin/">prezip-bin</a>(1)</i> instead.</p>
<dt><code>Output Data Error</code></p>
<dd> The output is full, write protected, or has an error and can no longer be written to.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-aspell/">aspell</a></code>(1), <code><a href="/docs/linux/man/1-aspell-import/">aspell-import</a></code>(1), <code><a href="/docs/linux/man/1-prezip-bin/">prezip-bin</a></code>(1), <code><a href="/docs/linux/man/1-run-with-aspell/">run-with-aspell</a></code>(1) </p>
<p> Aspell is fully documented in its Texinfo manual. See the `<code>aspell</code>&#8216; entry in <code>info</code> for more complete documentation.</p>
<h2>REPORTING BUGS</h2>
<p> For help, see the Aspell homepage at &lt;<a rel="nofollow" href="http://aspell.net">http://aspell.net</a>&gt; and send bug reports/comments to the Aspell user list at the above address.</p>
<h2>AUTHOR</h2>
<p> This manual page was written by Aaron Lehmann &lt;aaronl [at] vitelus.com&gt;, Brian Nelson &lt;pyro [at] debian.org&gt; and Jose Da Silva &lt;digital [at] joescat.com&gt;. </p>
<h2>Index</h2>
