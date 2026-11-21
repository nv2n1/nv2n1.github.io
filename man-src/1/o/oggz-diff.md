---

title: "oggz-diff(1)"
name: "oggz-diff"
section: "1"
letter: "o"
url: "/docs/linux/man/1-oggz-diff/"
description: "oggz-diff — Hexdump the packets of two Ogg files and output differences"
---

<p> oggz-diff &#8212; Hexdump the packets of two Ogg files and output differences<br />
&nbsp;<wbr></p>
<h2>SYNOPSIS</h2>
<p> <code>oggz-diff</code> [options] [OGGZDUMP_OPTIONS] [DIFF_OPTIONS] file1.ogg file2.ogg </p>
<p> <code>options:</code> [&#8211;verbose ] [-v | &#8211;version ] [-h | &#8211;help ] </p>
<p> <code>OGGZDUMP_OPTIONS:</code> [-b | &#8211;binary ] [-x | &#8211;hexadecimal ] [-c content-type | &#8211;content-type content-type ] [-s serialno | &#8211;serialno serialno ] [-O | &#8211;hide-offset ] [-S | &#8211;hide-serialno ] [-G | &#8211;hide-granulepos ] [-P | &#8211;hide-packetno ] </p>
<p> <code>DIFF_OPTIONS:</code> [-q | &#8211;brief ] [-C NUM | &#8211;context[=NUM] ] [-u | -U NUM | &#8211;unified[=NUM] ] [-e | &#8211;ed ] [&#8211;normal ] [&#8211;rcs ] [-y | &#8211;side-by-side ] [-l | &#8211;paginate ]</p>
<h2>Description</h2>
<p> <code>oggz-diff</code> is a <code>sh</code> script which uses <code>oggz-dump</code> to generate hexadecimal packet dumps of each input file, then outputs the difference between these dumps using <code>diff</code>.<br />
&nbsp;<wbr></p>
<h2>Options</h2>
<p> <code>oggz-diff</code> forwards a subset of options accepted by <code>oggz-dump</code> and <code>diff</code>. See <code><a href="/docs/linux/man/1-oggz-dump/">oggz-dump</a></code><code>(1)</code> and <code><a href="/docs/linux/man/1-diff/">diff</a></code><code>(1)</code> for more detail.<br />
&nbsp;<wbr></p>
<h3>oggz-dump format options</h3>
<dl>
<dt>-b, &#8211;binary</dt>
<dd> Generate a binary dump of each packet<br />
&nbsp;<wbr></dd>
<dt>-x, &#8211;hexadeciaml</dt>
<dd> Generate a hexadecimal dump of each packet<br />
&nbsp;<wbr></dd></dl>
<h3>oggz-dump filtering options</h3>
<dl>
<dt>-c <code>content-type</code>, &#8211;content-type <code>content-type</code></dt>
<dd> Dump only the logical bitstreams for a specific <code>content-type</code>. Run <code><a href="/docs/linux/man/1-oggz-known-codecs/">oggz-known-codecs</a></code><code>(1)</code> for a full list of codecs known by the installed version of oggz.<br />
&nbsp;<wbr></dd>
<dt>-s <code>serialno</code>, &#8211;serialno <code>serialno</code></dt>
<dd> Dump only the logical bitstream with specified <code>serialno</code>.<br />
&nbsp;<wbr></dd>
<dt>-O, &#8211;hide-offset</dt>
<dd> Hide the byte offset field of the preamble for each packet dumped. This is particularly useful when comparing Ogg bitstreams that differ only in page structure.<br />
&nbsp;<wbr></dd>
<dt>-S, &#8211;hide-serialno</dt>
<dd> Hide the serialno field of the preamble for each packet dumped. This is particularly useful when comparing Ogg bitstreams that differ only in serialno assignment.<br />
&nbsp;<wbr></dd>
<dt>-G, &#8211;hide-granulepos</dt>
<dd> Hide the granulepos field of the preamble for each packet dumped.<br />
&nbsp;<wbr></dd>
<dt>-P, &#8211;hide-packetno</dt>
<dd> Hide the packetno field of the preamble for each packet dumped.<br />
&nbsp;<wbr></dd></dl>
<h3>diff options</h3>
<p> The -w (&#8211;ignore-all-space) option to <code>diff</code> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>is always implied. </p>
<p>&nbsp;<wbr></p>
<dl>
<dt>-q, &#8211;brief</dt>
<dd> Output only whether files differ.<br />
&nbsp;<wbr></dd>
<dt>-C <code>NUM</code>, &#8211;context[=<code>NUM</code>]</dt>
<dd> Output NUM lines of copied context.<br />
&nbsp;<wbr></dd>
<dt>-u, -U <code>NUM</code>, &#8211;unified[=<code>NUM</code>]</dt>
<dd> Output NUM (default 3) lines of unified context.<br />
&nbsp;<wbr></dd>
<dt>-e, &#8211;ed</dt>
<dd> Output an ed script.<br />
&nbsp;<wbr></dd>
<dt>&#8211;normal</dt>
<dd> Output a normal diff.<br />
&nbsp;<wbr></dd>
<dt>&#8211;rcs</dt>
<dd> Output an RCS format diff.<br />
&nbsp;<wbr></dd>
<dt>-y, &#8211;side-by-side</dt>
<dd> Output in two columns.<br />
&nbsp;<wbr></dd>
<dt>-l, &#8211;paginate</dt>
<dd> Pass the output through <code>pr</code> to paginate it.<br />
&nbsp;<wbr></dd></dl>
<h3>Miscellaneous options</h3>
<dl>
<dt>&#8211;verbose</dt>
<dd> Display verbose messages.</dd>
<dt>-v, &#8211;version</dt>
<dd> Display version information and exit.</dd>
<dt>-h, &#8211;help</dt>
<dd> Display usage information and exit.</dd></dl>
<h2>AUTHOR</h2>
<p> Conrad Parker</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2003 CSIRO Australia<br />
&nbsp;<wbr></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-oggz-dump/">oggz-dump</a></code><code>(1)</code>, <code><a href="/docs/linux/man/1-diff/">diff</a></code><code>(1)</code>, <code><a href="/docs/linux/man/1-patch/">patch</a></code><code>(1)</code> </p>
