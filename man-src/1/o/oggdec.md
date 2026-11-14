---
title: "oggdec(1)"
name: "oggdec"
section: "1"
letter: "o"
url: "/docs/linux/man/1-oggdec/"
description: "oggdec – simple decoder, Ogg Vorbis file to PCM audio file (Wave or RAW)."
---

<h2 class="name">NAME</h2>
<p> oggdec &#8211; simple decoder, Ogg Vorbis file to PCM audio file (Wave or RAW).</p>
<h2>SYNOPSIS</h2>
<p> <code>oggdec</code> [ <code>-QhV</code> ] [ <code>-b bits_per_sample</code> ] [ <code>-e endianness</code> ] [ <code>-R</code> ] [ <code>-s signedness</code> ] [ <code>-o outputfile</code> ] <code>file &#8230;</code> </p>
<h2>DESCRIPTION</h2>
<p> <code>oggdec</code> decodes Ogg Vorbis files into PCM-encoded (&quot;uncompressed&quot;) audio files, either Wave or RAW format. </p>
<p> For each input file, <code>oggdec</code> writes to a filename based on the input filename, but with the extension changed to &quot;.wav&quot; or &quot;.raw&quot; as appropriate. </p>
<p> If the input file is specified as <code>&#8211;</code> , then <code>oggdec</code> will read from stdin, and write to stdout unless an output filename is specified. Likewise, an output filename of <code>&#8211;</code> will cause output to be to stdout. </p>
<p> Writing Wave format to stdout is a bad idea. Wave requires a seekable medium for the header to be rewritten after all the data is written out; stdout is not seekable. </p>
<h2>OPTIONS</h2>
<dl>
<dt>-Q, &#8211;quiet</p>
<dd> Suppresses program output.</p>
<dt>-h, &#8211;help</p>
<dd> Print help message.</p>
<dt>-V, &#8211;version</p>
<dd> Display version information.</p>
<dt>-b n, &#8211;bits=n</p>
<dd> Bits per sample. Valid values are 8 or 16.</p>
<dt>-e n, &#8211;endianness=n</p>
<dd> Set endianness for 16-bit output. 0 (default) is little-endian (Intel byte order). 1 is big-endian (sane byte order).</p>
<dt>-R, &#8211;raw</p>
<dd> Output in raw format. If not specified, writes Wave file (RIFF headers).</p>
<dt>-s n, &#8211;sign=n</p>
<dd> Set signedness for output. 0 for unsigned, 1 (default) for signed.</p>
<dt>-o filename, &#8211;output=filename</p>
<dd> Write output to specified filename. This option is only valid if one input [file] is specified, or if raw mode is used. </p>
</dl>
<h2>EXAMPLES</h2>
<p> Decode a file <code>enabler.ogg</code> to <code>enabler.wav</code><br />
&nbsp;<wbr>as little-endian unsigned 16-bit&nbsp;<wbr>(default options):</p>
<dl>
<dt>
<dd> oggdec enabler.ogg</dl>
<p> Decode a file <code>enabler.ogg</code> to <code>enabler.raw</code> as headerless little-endian unsigned 16-bit:</p>
<dl>
<dt>
<dd> oggdec &#8211;raw=1 enabler.ogg</dl>
<p> Decode <code>enabler.ogg</code> to <code>enabler.crazymonkey</code> as unsigned 8-bit:</p>
<dl>
<dt>
<dd> oggdec -b 8 -s 0 -o enabler.crazymonkey enabler.ogg</dl>
<p> Decode <code>enabler.ogg</code> to <code>enabler.raw</code> as big-endian signed 16-bit (any of the following):</p>
<dl>
<dt>
<dd> oggdec -R -e 1 -b 16 enabler.ogg</dl>
<dl>
<dt>
<dd> oggdec -R -e 1 -b 16 -o enabler.raw &#8211; &lt; enabler.ogg</dl>
<dl>
<dt>
<dd> oggdec -R -e 1 -b 16 &#8211; &lt; enabler.ogg &gt; enabler.raw</dl>
<p> Mass decoding (foo.ogg to foo.wav, bar.ogg to bar.wav, quux.ogg to quux.wav, etc.):</p>
<dl>
<dt>
<dd> oggdec *.ogg</dl>
<h2>AUTHORS</h2>
<h3>Program Authors</h3>
<p> Michael Smith &lt;msmith [at] xiph.org&gt;</p>
<h3>Manpage Authors</h3>
<p> Frederick Lee &lt;phaethon [at] linux.ucla.edu&gt;, assisted by a few million monkeys armed with keyboards in <a href="irc://irc.openprojects.net/#vorbis">irc://irc.openprojects.net/#vorbis</a> </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ogg123/">ogg123</a></code>(1), <code><a href="/docs/linux/man/1-oggenc/">oggenc</a></code>(1), <code><a href="/docs/linux/man/1-vorbiscomment/">vorbiscomment</a></code>(1), <code><a href="/docs/linux/man/1-flac/">flac</a></code>(1), <code><a href="/docs/linux/man/1-speexdec/">speexdec</a></code>(1) </p>
<h2>Index</h2>
