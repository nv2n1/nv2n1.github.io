---
title: "xdelta3(1)"
name: "xdelta3"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xdelta3/"
description: "xdelta3 – VCDIFF (RFC 3284) binary diff tool"
---

<h2>NAME</h2>
<p> xdelta3 &#8211; VCDIFF (RFC 3284) binary diff tool</p>
<h2>SYNOPSIS</h2>
<p> <code>xdelta3 </code> [<i>command</i>] [<i>options</i>] [<i>input</i> [<i>output</i>]]</p>
<h2>DESCRIPTION</h2>
<p> <code>xdelta3</code> is a binary diff tool that uses the VCDIFF (RFC 3284) format and compression.</p>
<h2>COMMANDS</h2>
<dl>
<dt><code>config</code></p>
<dd> prints xdelta3 configuration</p>
<dt><code>decode</code></p>
<dd> decompress the input, also set by -d</p>
<dt><code>encode</code></p>
<dd> compress the input, also set by -e (default)</p>
<dt><code>test</code></p>
<dd> run the builtin tests</p>
<dt><code>printdelta</code></p>
<dd> print information about the entire delta</p>
<dt><code>printhdr</code></p>
<dd> print information about the first window</p>
<dt><code>printhdrs</code></p>
<dd> print information about all windows</p>
<dt><code>recode</code></p>
<dd> encode with new application/secondary settings </p>
</dl>
<h2>OPTIONS</h2>
<p> standard options:</p>
<dl>
<dt><code>-0 .. -9</code></p>
<dd> compression level</p>
<dt><code>-c</code></p>
<dd> use stdout</p>
<dt><code>-d</code></p>
<dd> decompress</p>
<dt><code>-e</code></p>
<dd> compress</p>
<dt><code>-f</code></p>
<dd> force overwrite</p>
<dt><code>-F</code></p>
<dd> force the external-compression subprocess</p>
<dt><code>-h</code></p>
<dd> show help</p>
<dt><code>-q</code></p>
<dd> be quiet</p>
<dt><code>-v</code></p>
<dd> be verbose (max 2)</p>
<dt><code>-V</code></p>
<dd> show version </p>
<dt>memory options:</p>
<dd>
<dt><code>-B</code></p>
<dd> bytes source window size</p>
<dt><code>-W</code></p>
<dd> bytes input window size</p>
<dt><code>-P</code></p>
<dd> size compression duplicates window</p>
<dt><code>-I</code></p>
<dd> size instruction buffer size (0 = unlimited) </p>
<dt>compression options:</p>
<dd>
<dt><code>-s</code></p>
<dd> source source file to copy from (if any)</p>
<dt><code>-S </code><i>[djw|fgk]</i></p>
<dd> enable/disable secondary compression</p>
<dt><code>-N</code></p>
<dd> disable small string-matching compression</p>
<dt><code>-D</code></p>
<dd> disable external decompression (encode/decode)</p>
<dt><code>-R</code></p>
<dd> disable external recompression (decode)</p>
<dt><code>-n</code></p>
<dd> disable checksum (encode/decode)</p>
<dt><code>-C</code></p>
<dd> soft config (encode, undocumented)</p>
<dt><code>-A </code><i>[apphead]</i></p>
<dd> disable/provide application header (encode)</p>
<dt><code>-J</code></p>
<dd> disable output (check/compute only)</p>
<dt><code>-T</code></p>
<dd> use alternate code table (test)</p>
<dt><code>-m</code></p>
<dd> arguments for &quot;merge&quot; </p>
</dl>
<h2>NOTES</h2>
<p> The <code>XDELTA</code> environment variable may contain extra args: </p>
<dl>
<dt>
<dd> XDELTA=&quot;-s source-x.y.tar.gz&quot; \<br />
 tar &#8211;use-compress-program=xdelta3 -cf \<br />
 target-x.z.tar.gz.vcdiff target-x.y/ </p>
</dl>
<h2>EXAMPLES</h2>
<p> Compress the differences between SOURCE and TARGET, yielding OUT, using &quot;djw&quot; secondary compression: </p>
<p> xdelta3 -S djw -s SOURCE TARGET OUT </p>
<p> Do the same, using standard input and output: </p>
<p> xdelta3 -S djw -s SOURCE &lt; TARGET &gt; OUT </p>
<p> To decompress OUT, using SOURCE, yielding TARGET: </p>
<p> xdelta3 -d -s SOURCE OUT TARGET </p>
<h2>AUTHOR</h2>
<p> xdelta3 was written by Josh MacDonald &lt;josh.macdonald [at] gmail.com&gt;. </p>
<p> This manual page was written by Leo &#8216;costela&#8217; Antunes &lt;costela [at] debian.org&gt; for the Debian project (but may be used by others). </p>
<h2>Index</h2>
