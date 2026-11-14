---
title: "native2ascii-java-1-6-0-openjdk(1)"
name: "native2ascii-java-1-6-0-openjdk"
section: "1"
letter: "n"
url: "/docs/linux/man/1-native2ascii-java-1-6-0-openjdk/"
description: "native2ascii – Native-to-ASCII Converter"
---

<p>\ &quot; Created by: Doug Kramer, 19-Aug-1996 </p>
<h2>Name</h2>
<p>native2ascii &#8211; Native-to-ASCII Converter </p>
<p> Converts a file with native-encoded characters (characters which are non-Latin 1 and non-Unicode) to one with Unicode-encoded characters.</p>
<h2>Synopsis</h2>
<pre><tt>native2ascii</tt><i> [options] [inputfile [outputfile]]</i></pre>
<h2>Description</h2>
<p>The Java compiler and other Java tools can only process files which contain Latin-1 and/or Unicode-encoded (� notation) characters. <i>native2ascii</i> converts files which contain other character encodings into files containing Latin-1 and/or Unicode-encoded charaters. </p>
<p> If <i>outputfile</i> is omitted, standard output is used for output. If, in addition, <i>inputfile</i> is omitted, standard input is used for input. </p>
<h2>Options</h2>
<dl COMPACT>
<dt>-reverse</p>
<dd>Perform the reverse operation: convert a file with Latin-1 and/or Unicode encoded characters to one with native-encoded characters. </p>
<dt>-encoding encoding_name</p>
<dd>Specify the encoding name which is used by the conversion procedure. The default encoding is taken from System property <i>file.encoding</i>. The <i>encoding_name</i> string must be taken from the first column of the table of supported encodings in the <tt>Supported Encodings</tt> @ <a rel="nofollow" href="http://java.sun.com/javase/6/docs/technotes/guides/intl/encoding.doc.html">http://java.sun.com/javase/6/docs/technotes/guides/intl/encoding.doc.html</a> document.</p>
<dt>-Joption</p>
<dd>Pass <i>option</i> to the Java virtual machine, where <i>option</i> is one of the options described on the reference page for the java application launcher. For example, <code>-J-Xms48m</code> sets the startup memory to 48 megabytes.</dl>
<p>&nbsp;<wbr></p>
