---
title: "sgmlnorm(1)"
name: "sgmlnorm"
section: "1"
letter: "s"
url: "/docs/linux/man/1-sgmlnorm/"
description: "osgmlnorm – An SGML/XML document normalizer"
---

<h2 class="name">NAME</h2>
<p> osgmlnorm &#8211; An SGML/XML document normalizer </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>osgmlnorm</code> [<code>-CdeghmnrRvx</code>] [<code>-a</code><i>linktype</i>] [<code>-A</code><i>architecture</i>] [<code>-b</code><i>bctf</i>] [<code>-c</code><i>catalog</i>] [<code>-D</code><i>directory</i>&#8230;] [<code>-E</code><i>max_errors</i>&#8230;] [<code>-i</code><i>name</i>&#8230;] [<code>-f</code><i>name</i>&#8230;] [<code>-w</code><i>warning</i>&#8230;] [<i>sysid</i>&#8230;]</dt></dl>
<h2>DESCRIPTION</h2>
<p> <code>osgmlnorm</code></p>
<dd>prints on the standard output a normalized document instance for the SGML document contained in the concatenation of the entities with system identifiers</dd>
<dl>
<dt></dt></dl>
<dd>When the normalized instance is prefixed with the original SGML declaration and prolog, it will have the same ESIS as the original SGML document, with the following exceptions: </dd>
<p> * The output of osgmlnorm does not protect against the recognition of short reference delimiters, so any USEMAP declarations must be removed from the DTD. </p>
<p> * The normalized instance will use the reference delimiters, even if the original instance did not. </p>
<p> * If marked sections are included in the output using the -m option, the reference reserved names will be used for the status keywords even if the original instance did not. </p>
<p> * Any ESIS information relating to the SGML LINK feature will be lost. </p>
<p> The normalized instance will not use any markup minimization features except that: </p>
<p> * Any attributes that were not specified in the original instance will not be included in the normalized instance. (Current attributes will be included.) </p>
<p> * If the declared value of an attribute was a name token group, and a value was specified that was the same as the name of the attribute, then the attribute name and value indicator will be omitted. For example, with HTML osgmlnorm would output &lt;DL COMPACT&gt; rather than &lt;DL COMPACT=&quot;COMPACT&quot;&gt; </p>
<p> Part of an SGML System Conforming to International Standard ISO 8879 &#8212; Standard Generalized Markup Language. An SGML Extended Facilities system conforming to Annex A of International Standard ISO/IEC 10744 &#8212; Hypermedia/Time-based Structuring Language. </p>
<p> The following options are available: </p>
<p> <code>-a</code><i>name</i>, <code>&#8211;activate=</code><i>name</i></p>
<dl>
<dt>
</dt><dd> Make doctype or linktype <i>name</i> active.</dd></dl>
<p> <code>-A</code><i>architecture</i>, <code>&#8211;architecture=</code><i>architecture</i></p>
<dl>
<dt>
</dt><dd> Parse with respect to architecture <i>architecture</i>.</dd></dl>
<p> <code>-b</code><i>bctf</i>, <code>&#8211;bctf=</code><i>bctf</i></p>
<dl>
<dt>
</dt><dd> Use the BCTF with name <i>bctf</i> for output.</dd></dl>
<p> <code>-c</code><i>sysid</i>, <code>&#8211;catalog=</code><i>sysid</i></p>
<dl>
<dt>
</dt><dd> Map public identifiers and entity names to system identifiers using the catalog entry file whose system identifier is <i>sysid</i>.</dd></dl>
<p> <code>-C</code>, <code>&#8211;catalogs</code></p>
<dl>
<dt>
</dt><dd> This has the same effect as in <code><a href="/docs/linux/man/1-onsgmls/">onsgmls</a>(1)</code>.</dd></dl>
<p> <code>-d</code>, <code>&#8211;dtd</code></p>
<dl>
<dt>
</dt><dd> Output a document type declaration with the same external identifier as the input document, and with no internal declaration subset. No check is performed that the document instance is valid with respect to this DTD.</dd></dl>
<p> <code>-D</code><i>directory</i>, <code>&#8211;directory=</code><i>directory</i></p>
<dl>
<dt>
</dt><dd> Search <i>directory</i> for files specified in system identifiers. </dd>
<p> This has the same effect as in <code><a href="/docs/linux/man/1-onsgmls/">onsgmls</a>(1)</code>.</dl>
<p> <code>-e</code>, <code>&#8211;open-entities</code></p>
<dl>
<dt>
</dt><dd> Describe open entities in error messages.</dd></dl>
<p> <code>&#8211;error-numbers</code></p>
<dl>
<dt>
</dt><dd> Show error numbers in error messages.</dd></dl>
<p> <code>-g</code>, <code>&#8211;open-elements</code></p>
<dl>
<dt>
</dt><dd> Show the generic identifiers of open elements in error messages.</dd></dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
</dt><dd> Display a help text and exit.</dd></dl>
<p> <code>-i</code><i>name</i>, <code>&#8211;include=</code><i>name</i></p>
<dl>
<dt>
</dt><dd> This has the same effect as in <code><a href="/docs/linux/man/1-onsgmls/">onsgmls</a>(1)</code>.</dd></dl>
<p> <code>-m</code>, <code>&#8211;marked-sections</code></p>
<dl>
<dt>
</dt><dd> Output any marked sections that were in the input document instance.</dd></dl>
<p> <code>-n</code>, <code>&#8211;comments</code></p>
<dl>
<dt>
</dt><dd> Output any comments that were in the input document instance.</dd></dl>
<p> <code>-r</code>, <code>&#8211;raw</code></p>
<dl>
<dt>
</dt><dd> Raw output. Don&#8217;t perform any conversion on RSs and REs when printing the entity. The entity would typically have the storage manager attribute records=asis.</dd></dl>
<p> <code>-R</code>, <code>&#8211;restricted</code></p>
<dl>
<dt>
</dt><dd> This has the same effect as in <code><a href="/docs/linux/man/1-onsgmls/">onsgmls</a>(1)</code>.</dd></dl>
<p> <code>-v</code>, <code>&#8211;version</code></p>
<dl>
<dt>
</dt><dd> Print the version number.</dd></dl>
<p> <code>-w</code><i>type</i></p>
<dl>
<dt>
</dt><dd> Control warnings and errors according to type. This has the same effect as in <code><a href="/docs/linux/man/1-onsgmls/">onsgmls</a>(1)</code>.</dd></dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-onsgmls/">onsgmls</a>(1)</code>, <code><a href="/docs/linux/man/1-ospam/">ospam</a>(1)</code>, <code><a href="/docs/linux/man/1-ospent/">ospent</a>(1)</code>, <code><a href="/docs/linux/man/1-osx/">osx</a>(1)</code></p>
<h2>AUTHORS</h2>
<p> <code>James Clark</code></p>
<dl>
<dt>
</dt><dd> Author.</dd></dl>
<p> <code>Ian Castle</code> &lt;ian.castle [at] openjade.org&gt;</p>
<dl>
<dt>
</dt><dd> Author.</dd></dl>
<h2>COPYRIGHT</h2>
