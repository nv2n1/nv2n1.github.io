---
title: "gjots2docbook(1)"
name: "gjots2docbook"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gjots2docbook/"
description: "gjots2docbook – Convert a gjotsfile to DOCBOOK (on stdout)"
---

<h2>NAME</h2>
<p> gjots2docbook &#8211; Convert a gjotsfile to DOCBOOK (on <code>stdout</code>)</p>
<h2>SYNOPSIS</h2>
<p> <code>gjots2docbook</code> <code>-a</code>|<code>-b</code> [ <code>-e</code> ] [ <code>-P</code> ] [ <code>-p</code> ] [ <i>gjotsfile</i> ]</p>
<h2>DESCRIPTION</h2>
<p> <code>gjots2docbook</code> converts a gjotsfile into DOCBOOK XML. <code>gjots2docbook</code> uses <code><a href="/docs/linux/man/1-awk/">awk</a></code>(1) to perform the conversion. <code>gjots2docbook</code> does not create them so the first element in the file should contain any &lt;bookinfo&gt; or &lt;artheader&gt; element. Similarly, &lt;bibliographic&gt; elements are not created. In fact the output is very simplistic with item titles in the <code>gjotsfile</code> being converted to chapter or section headings in DOCBOOK. There is no reason why your gjotsfile should not contain valid DOCBOOK XML &#8211; and that is why the -e and -p options are provided. If the file does not start with &lt;?xml &#8230;&gt; then appropriate lines will be added as follows:</p>
<dl>
<dt>
<dd>
<pre>
&lt;?xml version=&quot;1.0&quot; encoding=&quot;UTF-8&quot;?&gt;
<br>
&lt;!DOCTYPE doc_type PUBLIC &quot;-//OASIS//DTD DocBook XML V4.1.2//EN&quot;&gt;
</pre>
</dl>
<p> If properly installed, the docbook utilities can then be used to create HTML, man, ps, pdf etc files eg:</p>
<dl>
<dt>
<dd>
<pre>
gjots2docbook -b ~/.gjotsfile &gt;gjotsfile.xml
<br>
docbook2pdf gjotsfile.xml
</pre>
</dl>
<p> It may be necessary to fine-tune the docbook formatting to access all features.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-a</code></p>
<dd> makes a DOCBOOK article</p>
<dt><code>-b</code></p>
<dd> makes a DOCBOOK book</p>
<dt><code>-e</code></p>
<dd> don&#8217;t encode special characters eg &lt; -&gt; &amp;lt;</p>
<dt><code>-p</code></p>
<dd> don&#8217;t change blank lines to &lt;/para&gt;&lt;para&gt; markers</p>
<dt><code>-P</code></p>
<dd> first section is a preface rather than a chapter (book only)</dl>
<h2>AUTHOR</h2>
<p> Written by Bob Hepple &lt;bhepple [at] freeshell.org&gt; <a rel="nofollow" href="http://bhepple.freeshell.org/gjots">http://bhepple.freeshell.org/gjots</a></p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 2002 Robert Hepple<br />
 This is free software; see the source for copying condi­ tions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-gjots/">gjots</a></code>(1), <code><a href="/docs/linux/man/1-gjots2html/">gjots2html</a></code>(1), <code><a href="/docs/linux/man/1-docbook2gjots/">docbook2gjots</a></code>(1)</p>
<h2>Index</h2>
