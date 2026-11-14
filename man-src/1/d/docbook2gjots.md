---
title: "docbook2gjots(1)"
name: "docbook2gjots"
section: "1"
letter: "d"
url: "/docs/linux/man/1-docbook2gjots/"
description: "docbook2gjots – Convert a DOCBOOK file to gjots format (on stdout)"
---

<h2>NAME</h2>
<p> docbook2gjots &#8211; Convert a DOCBOOK file to gjots format (on <code>stdout</code>)</p>
<h2>SYNOPSIS</h2>
<p> <code>docbook2gjots</code> [ <i>DOCBOOK-file</i> ]</p>
<h2>DESCRIPTION</h2>
<p> <code>docbook2gjots</code> converts a DOCBOOK XML file into gjots format. <code>docbook2gjots</code> uses <code><a href="/docs/linux/man/1-gawk/">gawk</a></code>(1) to perform the conversion. <code>&lt;preface&gt;</code>, <code>&lt;chapter&gt;</code>, <code>&lt;section&gt;</code>, <code>&lt;sect1&gt;</code>, <code>&lt;sect2&gt;</code>, <code>&lt;sect3&gt;</code> and <code>&lt;sect4&gt;</code> tags are used to define <code>NewEntry</code> and <code>NewFolder</code> boundaries. They should definitely have <code>&lt;title&gt;</code> tags. This is a quick and dirty hack using <code><a href="/docs/linux/man/1-gawk/">gawk</a></code>(1) and does no formal checking of XML or SGML syntax nor does it validate against the DOCBOOK DTD. Consequently, if the syntax of the file is broken the conversion will probably fail. It is intended that a round-trip can be made so that <code><a href="/docs/linux/man/1-gjots/">gjots</a></code>(1) can be used as a tool at all stages of DOCBOOK production &#8211; mainly as an outline processor to help the author organise and order the work. A document may well start its life in <code><a href="/docs/linux/man/1-gjots/">gjots</a></code>(1) as the initial thoughts are marshalled. As the document forms up, it can be converted to DOCBOOK with the following command which automatically adds tags such as <code>&lt;?xml&#8230;&gt;</code>, <code>&lt;para&gt; </code> etc:</p>
<dl>
<dt>
<dd>
<pre>
gjots2docbook -b file.gjots &gt;file.xml
<br>
docbook2pdf file.xml
</pre>
</dl>
<p> Or, starting with an existing DOCBOOK file:</p>
<dl>
<dt>
<dd>
<pre>
docbook2gjots file.xml &gt;file.gjots
</pre>
</dl>
<p> In the latter case, the document will already have a lot of DOCBOOK tags so to convert back to docbook, add the -e and -p options:</p>
<dl>
<dt>
<dd>
<pre>
gjots2docbook -b -p -e file.gjots &gt;file.xml
<br>
docbook2pdf file.xml
</pre>
</dl>
<h2>AUTHOR</h2>
<p> Written by Bob Hepple &lt;bhepple [at] freeshell.org&gt; <a rel="nofollow" href="http://bhepple.freeshell.org/gjots">http://bhepple.freeshell.org/gjots</a></p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 2002 Robert Hepple<br />
 This is free software; see the source for copying condi­ tions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-gjots/">gjots</a></code>(1), <code><a href="/docs/linux/man/1-gjots2html/">gjots2html</a></code>(1), <code><a href="/docs/linux/man/1-gjots2docbook/">gjots2docbook</a></code>(1) </p>
<h2>Index</h2>
