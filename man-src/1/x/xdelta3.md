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
<p> <code>xdelta3 </code> [<i>command</i>] [<i>options</i>] [<i>input</i> [<i>output</i>]]</p>
<p> <code>xdelta3</code> is a binary diff tool that uses the VCDIFF (RFC 3284) format and compression.</p>
<h2>COMMANDS</h2>
<dl>
<dt><code>config</code></dt>
<dd> prints xdelta3 configuration</dd>
<dt><code>decode</code></dt>
<dd> decompress the input, also set by -d</dd>
<dt><code>encode</code></dt>
<dd> compress the input, also set by -e (default)</dd>
<dt><code>test</code></dt>
<dd> run the builtin tests</dd>
<dt><code>printdelta</code></dt>
<dd> print information about the entire delta</dd>
<dt><code>printhdr</code></dt>
<dd> print information about the first window</dd>
<dt><code>printhdrs</code></dt>
<dd> print information about all windows</dd>
<dt><code>recode</code></dt>
<dd> encode with new application/secondary settings </dd>
</dl>
<h2>OPTIONS</h2>
<p> standard options:</p>
<dl>
<dt><code>-0 .. -9</code></dt>
<dd> compression level</dd>
<dt><code>-c</code></dt>
<dd> use stdout</dd>
<dt><code>-d</code></dt>
<dd> decompress</dd>
<dt><code>-e</code></dt>
<dd> compress</dd>
<dt><code>-f</code></dt>
<dd> force overwrite</dd>
<dt><code>-F</code></dt>
<dd> force the external-compression subprocess</dd>
<dt><code>-h</code></dt>
<dd> show help</dd>
<dt><code>-q</code></dt>
<dd> be quiet</dd>
<dt><code>-v</code></dt>
<dd> be verbose (max 2)</dd>
<dt><code>-V</code></dt>
<dd> show version </dd>
<dt>memory options:</dt>
<dd>
</dd><dt><code>-B</code></dt>
<dd> bytes source window size</dd>
<dt><code>-W</code></dt>
<dd> bytes input window size</dd>
<dt><code>-P</code></dt>
<dd> size compression duplicates window</dd>
<dt><code>-I</code></dt>
<dd> size instruction buffer size (0 = unlimited) </dd>
<dt>compression options:</dt>
<dd>
</dd><dt><code>-s</code></dt>
<dd> source source file to copy from (if any)</dd>
<dt><code>-S </code><i>[djw|fgk]</i></dt>
<dd> enable/disable secondary compression</dd>
<dt><code>-N</code></dt>
<dd> disable small string-matching compression</dd>
<dt><code>-D</code></dt>
<dd> disable external decompression (encode/decode)</dd>
<dt><code>-R</code></dt>
<dd> disable external recompression (decode)</dd>
<dt><code>-n</code></dt>
<dd> disable checksum (encode/decode)</dd>
<dt><code>-C</code></dt>
<dd> soft config (encode, undocumented)</dd>
<dt><code>-A </code><i>[apphead]</i></dt>
<dd> disable/provide application header (encode)</dd>
<dt><code>-J</code></dt>
<dd> disable output (check/compute only)</dd>
<dt><code>-T</code></dt>
<dd> use alternate code table (test)</dd>
<dt><code>-m</code></dt>
<dd> arguments for &quot;merge&quot; </dd>
</dl>
<h2>NOTES</h2>
<p> The <code>XDELTA</code> environment variable may contain extra args: </p>
<dl>
<dt>
</dt><dd> XDELTA=&quot;-s source-x.y.tar.gz&quot; \<br />
 tar &#8211;use-compress-program=xdelta3 -cf \<br />
 target-x.z.tar.gz.vcdiff target-x.y/ </dd>
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
