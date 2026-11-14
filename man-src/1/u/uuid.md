---
title: "uuid(1)"
name: "uuid"
section: "1"
letter: "u"
url: "/docs/linux/man/1-uuid/"
description: "uuid – Universally Unique Identifier Command-Line Tool"
---

<h2 class="name">NAME</h2>
<p> uuid &#8211; Universally Unique Identifier Command-Line Tool </p>
<h2>VERSION</h2>
<p> <font SIZE="-1">OSSP</font> uuid <font SIZE="-1">1.6.2 (04-Jul-2008)</font></p>
<h2>SYNOPSIS</h2>
<p> <code>uuid</code> [<code>-v</code> <i>version</i>] [<code>-m</code>] [<code>-n</code> <i>count</i>] [<code>-1</code>] [<code>-F</code> <i>format</i>] [<code>-o</code> <i>filename</i>] [<i>namespace</i> <i>name</i>] </p>
<p> <code>uuid</code> <code>-d</code> [<code>-r</code>] [<code>-o</code> <i>filename</i>] <i>uuid</i></p>
<h2>DESCRIPTION</h2>
<p> <font SIZE="-1"><code>OSSP</code></font><code> uuid</code> is a <font SIZE="-1">ISO-C:1999</font> application programming interface (<font SIZE="-1">API</font>) and corresponding command line interface (<font SIZE="-1">CLI</font>) for the generation of <font SIZE="-1">DCE 1.1, ISO/IEC 11578:1996</font> and <font SIZE="-1">IETF RFC-4122</font> compliant <i>Universally Unique Identifier</i> (<font SIZE="-1">UUID</font>). It supports <font SIZE="-1">DCE 1.1</font> variant UUIDs of version 1 (time and node based), version 3 (name based, <font SIZE="-1">MD5</font>), version 4 (random number based) and version 5 (name based, <font SIZE="-1">SHA-1</font>). Additional <font SIZE="-1">API</font> bindings are provided for the languages <font SIZE="-1">ISO-C<font SIZE="-2">++</font>:1998,</font> Perl:5 and <font SIZE="-1">PHP:4/5.</font> Optional backward compatibility exists for the ISO-C <font SIZE="-1">DCE-1.1</font> and Perl Data::UUID APIs. </p>
<p> UUIDs are 128 bit numbers which are intended to have a high likelihood of uniqueness over space and time and are computationally difficult to guess. They are globally unique identifiers which can be locally generated without contacting a global registration authority. UUIDs are intended as unique identifiers for both mass tagging objects with an extremely short lifetime and to reliably identifying very persistent objects across a network. </p>
<p> This is the command line interface (<font SIZE="-1">CLI</font>) of <font SIZE="-1"><code>OSSP</code></font><code> uuid</code>. For a detailed description of UUIDs see the documentation of the application programming interface (<font SIZE="-1">API</font>) in <i><a href="/docs/linux/man/3-uuid/">uuid</a></i>(3).</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-v</code> <i>version</i></p>
<dd> Sets the version of the generated <font SIZE="-1">DCE 1.1</font> variant <font SIZE="-1">UUID.</font> Supported are <i>version</i> &quot;<tt>1</tt>&#8220;, &#8221;<tt>3</tt>&#8220;, &#8221;<tt>4</tt>&#8220; and &#8221;<tt>5</tt>&#8220;. The default is &#8221;<tt>1</tt>&quot;. </p>
<p> For version 3 and version 5 UUIDs the additional command line arguments <i>namespace</i> and <i>name</i> have to be given. The <i>namespace</i> is either a <font SIZE="-1">UUID</font> in string representation or an identifier for internally pre-defined namespace UUIDs (currently known are &quot;<tt> ns:DNS<br />
 </tt>&#8220;, &#8221;<tt> ns:URL<br />
 </tt>&#8220;, &#8221;<tt> ns:OID<br />
 </tt>&#8220;, and &#8221;<tt> ns:X500<br />
 </tt>&quot;). The <i>name</i> is a string of arbitrary length.</p>
<dt><code>-m</code></p>
<dd> Forces the use of a random multi-cast <font SIZE="-1">MAC</font> address when generating version 1 UUIDs. By default the real physical <font SIZE="-1">MAC</font> address of the system is used.</p>
<dt><code>-n</code> <i>count</i></p>
<dd> Generate <i>count</i> UUIDs instead of just a single one (the default).</p>
<dt><code>-1</code></p>
<dd> If option <code>-n</code> is used with a <i>count</i> greater than <tt>1</tt>, then this option can enforce the reset the <font SIZE="-1">UUID</font> context for each generated <font SIZE="-1">UUID.</font> This makes no difference for <i>version</i> <tt>3</tt>, <tt>4</tt> and <tt>5</tt> UUIDs. But version <tt>1</tt> UUIDs are based on the previously generated <font SIZE="-1">UUID</font> which is remembered in the <font SIZE="-1">UUID</font> context of the <font SIZE="-1">API.</font> Option <code>-1</code> deletes the remembered <font SIZE="-1">UUID</font> on each iteration.</p>
<dt><code>-F</code> <i>format</i></p>
<dd> Representation format for importing or exporting an <font SIZE="-1">UUID.</font> The following (case insensitive) format identifiers are currently recognized:</p>
<dl>
<dt>
<dd>
<dl>
<dt> BIN<br />
 (binary representation)</p>
<dd> This is the raw 128 bit network byte order binary representation of a <font SIZE="-1">UUID.</font> Example is the octet stream <tt> 0xF8 0x1D 0x4F 0xAE 0x7D 0xEC 0x11 0xD0 0xA7 0x65 0x00 0xA0 0xC9 0x1E 0x6B 0xF6<br />
 </tt>.</p>
<dt> STR<br />
 (string representation)</p>
<dd> This is the 36 character hexadecimal <font SIZE="-1">ASCII</font> string representation of a <font SIZE="-1">UUID.</font> Example is the string &quot;<tt> f81d4fae-7dec-11d0-a765-00a0c91e6bf6<br />
 </tt>&quot;.</p>
<dt> SIV<br />
 (single integer value representation)</p>
<dd> This is the maximum 39 character long single integer value representation of a <font SIZE="-1">UUID.</font> Example is the string &quot;<tt>329800735698586629295641978511506172918</tt>&quot;.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>-o</code> <i>filename</i></p>
<dd> Write output to <i>filename</i> instead of to <i>stdout</i>.</p>
<dt><code>-d</code></p>
<dd> Decode a given <font SIZE="-1">UUID</font> (given as a command line argument or if the command line argument is &quot;<tt> -<br />
 </tt>&quot; the <font SIZE="-1">UUID</font> is read from <i>stdin</i>) and dump textual information about the <font SIZE="-1">UUID.</font></dl>
<h2>EXAMPLES</h2>
<pre>
 # generate DCE 1.1 v1 UUID (time and node based)
 $ uuid -v1
 01c47915-4777-11d8-bc70-0090272ff725
 # decode and dump DCE 1.1 v1 UUID (time and node based)
 $ uuid -d 01c47915-4777-11d8-bc70-0090272ff725
 encode: STR:     01c47915-4777-11d8-bc70-0090272ff725
         SIV:     2349374037528578887923094374772111141
 decode: variant: DCE 1.1, ISO/IEC 11578:1996
         version: 1 (time and node based)
         content: time:  2004-01-15 16:22:26.376322.1 UTC
                  clock: 15472 (usually random)
                  node:  00:90:27:2f:f7:25 (global unicast)
 # generate DCE 1.1 v3 UUID (name based)
 $ uuid -v3 ns:URL <a rel="nofollow" href="http://www.ossp.org/">http://www.ossp.org/</a>
 02d9e6d5-9467-382e-8f9b-9300a64ac3cd
 # decode and dump DCE 1.1 v3 UUID (name based)
 $ uuid -d 02d9e6d5-9467-382e-8f9b-9300a64ac3cd
 encode: STR:     02d9e6d5-9467-382e-8f9b-9300a64ac3cd
         SIV:     3789866285607910888100818383505376205
 decode: variant: DCE 1.1, ISO/IEC 11578:1996
         version: 3 (name based, MD5)
         content: 02:D9:E6:D5:94:67:08:2E:0F:9B:93:00:A6:4A:C3:CD
                  (not decipherable: MD5 message digest only)
 # generate DCE 1.1 v4 UUID 4 (random data based)
 $ uuid -v4
 eb424026-6f54-4ef8-a4d0-bb658a1fc6cf
 # decode and dump DCE 1.1 v4 UUID 4 (random data based)
 $ uuid -d eb424026-6f54-4ef8-a4d0-bb658a1fc6cf
 encode: STR:     eb424026-6f54-4ef8-a4d0-bb658a1fc6cf
         SIV:     312712571721458096795100956955942831823
 decode: variant: DCE 1.1, ISO/IEC 11578:1996
         version: 4 (random data based)
         content: EB:42:40:26:6F:54:0E:F8:24:D0:BB:65:8A:1F:C6:CF
                  (no semantics: random data only)
</pre>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/3-uuid/">uuid</a></i>(3), <i><a href="/docs/linux/man/3-ossp--uuid/">OSSP::uuid</a></i>(3). </p>
<h2>Index</h2>
