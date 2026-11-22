---

title: "native2ascii-java-1(1)"
name: "native2ascii-java-1"
section: "1"
letter: "n"
url: "/docs/linux/man/1-native2ascii-java-1/"
description: "native2ascii – Native-to-ASCII Converter"
---

<p> native2ascii &#8211; Native-to-ASCII Converter </p>
<p> Converts a file with characters in any supported character encoding to one with ASCII and/or Unicode escapes, or visa versa. </p>
<h2>SYNOPSIS</h2>
<pre><code>
native2ascii[options][inputfile[outputfile]]
</code></pre>
<h2>DESCRIPTION</h2>
<p> <i>native2ascii</i> converts files that are encoded to any character encoding that is supported by the Java runtime environment to files encoded in ASCII, using Unicode escapes (&quot;\uxxxx&quot; notation) for all characters that are not part of the ASCII character set. This process is required for properties files containing characters not in ISO-8859-1 character sets. The tool can also perform the reverse conversion. </p>
<p> If <i>outputfile</i> is omitted, standard output is used for output. If, in addition, <i>inputfile</i> is omitted, standard input is used for input. </p>
<h2>OPTIONS</h2>
<dl>
<dd>  </dd>
<dl>
<dt>-reverse </dt>
<dd> <p> Perform the reverse operation: Convert a file encoded in ISO-8859-1 with Unicode escapes to a file in any character encoding supported by the Java runtime environment. <br/>
 <br/>
 </p>
 </dd>
<dt>-encoding encoding_name </dt>
<dd> <p> Specifies the name of the character encoding to be used by the conversion procedure. If this option is not present, the default character encoding (as determined by the <i>java.nio.charset.Charset.defaultCharset</i> method) is used. The <i>encoding_name</i> string must be the name of a character encoding that is supported by the Java runtime environment &#8211; see the <code>Supported Encodings</code> @ <a rel="nofollow" href="http://docs.oracle.com/javase/7/docs/technotes/guides/intl/encoding.doc.html">http://docs.oracle.com/javase/7/docs/technotes/guides/intl/encoding.doc.html</a> document. <br/>
 <br/>
 </p>
 </dd>
<dt>-Joption </dt>
<dd> <p> Pass <i>option</i> to the Java virtual machine, where <i>option</i> is one of the options described on the reference page for the <a href="/docs/linux/man/1-java/">java</a>(1). For example, <code>-J-Xms48m</code> sets the startup memory to 48 megabytes. </p>
 </dd></dl>
</dl>
<p> <br/>
&nbsp;<wbr> </p>
