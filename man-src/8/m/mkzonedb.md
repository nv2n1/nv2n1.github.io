---
title: "mkzonedb(8)"
name: "mkzonedb"
section: "8"
letter: "m"
url: "/docs/linux/man/8-mkzonedb/"
description: "mkzonedb – Utility create a zone file for isdnlog"
---

<p>mkzonedb &#8211; Utility create a zone file for isdnlog</p>
<h2>Synopsis</h2>
<p>mkzonedb -r zonefile -d database [-v] [-V] [-o Oz] [-l len]</p>
<h2>Description</h2>
<p><code>mkzonedb</code> reads a text file with zone (area code) information, and writes it in a special format to the database file so that other apps such as isdnlog can easily access the data. </p>
<p> This data is used to determine in what &quot;zone&quot; a given area code is in relation to another, to see what rate applies to a call between these area codes (&quot;is the call a local call&quot;). </p>
<p> This utility is really only used during the building of the isdnlog-data package, but it may be useful for those who want to create their own custom tables.</p>
<h2>Options</h2>
<dl>
<dt><code>-r</code><i> zonefile</i></p>
<dd>the text file with the zone information. Use &quot;-&quot; for standard input. </p>
<dt><code>-d</code><i> database</i></p>
<dd>the output database filename </p>
<dt><code>-v</code></p>
<dd>verbose mode </p>
<dt><code>-V</code></p>
<dd>show version information, and quit (don&#8217;t do anything) </p>
<dt><code>-o</code><i> Oz</i></p>
<dd>Use &quot;Oz&quot; area zone. Default is 1. (What does this mean, exactly?) </p>
<dt><code>-l</code><i> len</i></p>
<dd>&quot;len&quot; is the length of areacodes.<br />
 If 5 or more is given, then more space is allocated for the internal tables (40000 instead of 10000 numbers allowed). Other values aren&#8217;t really used. </p>
</dl>
<h2>Author</h2>
<p>manpage written from C source by Paul Slootman &lt;paul [at] debian.org&gt;.</p>
