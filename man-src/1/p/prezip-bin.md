---
title: "prezip-bin(1)"
name: "prezip-bin"
section: "1"
letter: "p"
url: "/docs/linux/man/1-prezip-bin/"
description: "prezip-bin – prefix zip delta word list compressor/decompressor"
---

<h2 class="name">NAME</h2>
<p> prezip-bin &#8211; prefix zip delta word list compressor/decompressor </p>
<h2>SYNOPSIS</h2>
<p> <code>prezip-bin</code> [ <code>-V</code> | <code>-d</code> | <code>-z</code> ]</p>
<h2>DESCRIPTION</h2>
<p> <code>prezip-bin</code> compresses/decompresses sorted word lists from standard input to standard output. </p>
<p> <i>Prezip-bin</i> is similar to <i><a href="/docs/linux/man/1-word-list-compress/">word-list-compress</a>(1)</i> but it allows a larger character set of {0x00&#8230;0x09, 0x0B, 0x0C, 0x0E&#8230;0xFF} and multi-words larger than 255 characters in length. It can also decompress <i><a href="/docs/linux/man/1-word-list-compress/">word-list-compress</a>(1)</i> compatible files.</p>
<h2>COMMANDS</h2>
<p> <i>Prezip-bin</i> accepts only one of these commands.</p>
<dl>
<dt><code>-V</code></p>
<dd> Display <i>prezip-bin</i> version number to standard output.</p>
<dt><code>-d</code></p>
<dd> Read a compressed word list from standard input and decompress it to standard output. This can be a <i><a href="/docs/linux/man/1-word-list-compress/">word-list-compress</a>(1)</i> or a <i>prezip-bin</i> compressed file.</p>
<dt><code>-z</code></p>
<dd> Read a binary word list from standard input and compress it to standard output.</dl>
<h2>EXAMPLES</h2>
<dl>
<dt>prezip-bin <code>-d</code> &lt;wordlist.cwl &gt;wordlist.txt</p>
<dd> Decompress file wordlist.cwl to text file wordlist.txt</p>
<dt>prezip-bin <code>-z</code> &lt;wordlist.txt &gt;wordlist.pz 2&gt;errors.txt</p>
<dd> Compress wordlist.txt to binary file wordlist.pz and send any error messages to a text file named errors.txt</p>
<dt>LC_COLLATE=C sort -u &lt;wordlist.txt <code>|</code> prezip-bin -z &gt;wordlist.pz</p>
<dd> Sort a word list, then pipe it to <i>prezip-bin</i> to create a compressed binary wordlist.pz file.</p>
<dt>prezip-bin -d &lt;words.pz <code>|</code> aspell create master ./words.rws</p>
<dd> Decompress a wordlist, then pipe it to <i><a href="/docs/linux/man/1-aspell/">aspell</a>(1)</i> to create a spelling list. Please check the <i><a href="/docs/linux/man/1-aspell/">aspell</a>(1)</i> info manual for proper usage and options.</dl>
<h2>TIPS</h2>
<p> <i>Prezip-bin</i> is best used with sorted word list type files. It is not a general purpose compression program since resulting files may actually increase in size. </p>
<p> Unlike <i><a href="/docs/linux/man/1-word-list-compress/">word-list-compress</a>(1)</i> if your word list has leading or trailing blank spaces for formatting purposes, you should remove them first before you compress your list using <i>prezip-bin -z</i> , otherwise those spaces will be included in the compressed binary output.</p>
<h2>DIAGNOSTICS</h2>
<p> <i>Prezip-bin</i> normally exits with a return code of 0. If it encounters an error, a message is sent to standard error output (stderr), and <i>prezip-bin</i> exits with a non-zero return value. Error messages are listed below:</p>
<dl>
<dt><code>(display help/usage message)</code></p>
<dd> Unknown command given on the command line so <i>prezip-bin</i> displays a usage message to standard error output.</p>
<dt><code>unknown format</code></p>
<dd> The input file appears not to be an expected format, or may possibly be a more advanced format. The output file will be empty.</p>
<dt><code>corrupt input</code></p>
<dd> This is only for the decompression command <code>-d</code>. The input file appeared to be of a correct format, but something appears wrong now. There may be some valid data in output, but due to input corruption, the rest of the file can not be completed.</p>
<dt><code>unexpected EOF</code></p>
<dd> The input file appeared okay but ended sooner than expected, therefore the output file is not complete.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-aspell/">aspell</a></code>(1), <code><a href="/docs/linux/man/1-aspell-import/">aspell-import</a></code>(1), <code><a href="/docs/linux/man/1-run-with-aspell/">run-with-aspell</a></code>(1), <code><a href="/docs/linux/man/1-word-list-compress/">word-list-compress</a></code>(1) </p>
<p> Aspell is fully documented in its Texinfo manual. See the `<code>aspell</code>&#8216; entry in <code>info</code> for more complete documentation.</p>
<h2>REPORTING BUGS</h2>
<p> For help, see the Aspell homepage at &lt;<a rel="nofollow" href="http://aspell.net">http://aspell.net</a>&gt;. Send bug reports/comments to the Aspell user list at the above address.</p>
<h2>AUTHOR</h2>
<p> This info page was written by Jose Da Silva &lt;digital [at] joescat.com&gt;. </p>
<h2>Index</h2>
