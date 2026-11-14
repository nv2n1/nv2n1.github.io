---
title: "osx(1)"
name: "osx"
section: "1"
letter: "o"
url: "/docs/linux/man/1-osx/"
description: "osx – An SGML to XML converter"
---

<h2 class="name">NAME</h2>
<p> osx &#8211; An SGML to XML converter </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>osx</code> [<code>-CeghnRvx</code>] [<code>-a</code><i>name</i>] [<code>-A</code><i>architecture</i>] [<code>-b</code><i>encoding</i>] [<code>-c</code><i>catalog_file</i>] [<code>-d</code><i>directory</i>] [<code>-D</code><i>directory</i>] [<code>-i</code><i>name</i>] [<code>-f</code><i>file</i>] [<code>-l</code><i>dtd_file</i>] [<code>-w</code><i>warning_type</i>] [<code>-x</code><i>xml_output_option</i>&#8230;] [<i>sysid</i>&#8230;]</dl>
<h2>DESCRIPTION</h2>
<p> <code>osx</code></p>
<dd>converts SGML to XML. <code>osx</code> parses and validates the SGML document contained in</p>
<dl>
<dt>
<dd>and writes an equivalent XML document to the standard output. <code>osx</code> will warn about SGML constructs which have no XML equivalent.</dl>
<p> Part of an SGML System Conforming to International Standard ISO 8879 &#8212; Standard Generalized Markup Language. An SGML Extended Facilities system conforming to Annex A of International Standard ISO/IEC 10744 &#8212; Hypermedia/Time-based Structuring Language.</p>
<h2>OPTIONS</h2>
<p> The following options are available: </p>
<p> <code>-a</code><i>name</i>, <code>&#8211;activate=</code><i>name</i></p>
<dl>
<dt>
<dd> Make doctype or linkname <i>name</i> active.</dl>
<p> <code>-A</code><i>name</i>, <code>&#8211;architecture=</code><i>name</i></p>
<dl>
<dt>
<dd> Parse with respect to architecture <i>name</i>.</dl>
<p> <code>-b</code><i>encoding</i>, <code>&#8211;encoding=</code><i>encoding</i></p>
<dl>
<dt>
<dd> Use the BCTF <i>encoding</i> for output. By default <code>osx</code> uses UTF-8.</dl>
<p> <code>-c</code><i>sysid</i>, <code>&#8211;catalog=</code><i>sysid</i></p>
<dl>
<dt>
<dd> Map public identifiers and entity names to system identifiers using the catalog entry file whose system identifier is <i>sysid</i>.</dl>
<p> <code>-C</code>, <code>&#8211;catalogs</code></p>
<dl>
<dt>
<dd> This has the same effect as in <code><a href="/docs/linux/man/1-onsgmls/">onsgmls</a>(1)</code>.</dl>
<p> <code>-d</code><i>directory</i>, <code>&#8211;entity_output_location=</code><i>directory</i></p>
<dl>
<dt>
<dd> Place output files in <i>directory</i>.</dl>
<p> <code>-D</code><i>directory</i>, <code>&#8211;directory=</code><i>directory</i></p>
<dl>
<dt>
<dd> Search <i>directory</i> for files specified in system identifiers. This has the same effect as in <code><a href="/docs/linux/man/1-onsgmls/">onsgmls</a>(1)</code>.</dl>
<p> <code>-e</code>, <code>&#8211;open-entities</code></p>
<dl>
<dt>
<dd> Describe open entities in error messages.</dl>
<p> <code>-E</code><i>max_errors</i>, <code>&#8211;max-errors=</code><i>max_errors</i></p>
<dl>
<dt>
<dd> Give up after <i>max_errors</i> errors.</dl>
<p> <code>-f</code><i>file</i>, <code>&#8211;error-file=</code><i>file</i></p>
<dl>
<dt>
<dd> Redirect errors to <i>file</i>. This is useful mainly with shells that do not support redirection of stderr.</dl>
<p> <code>-g</code>, <code>&#8211;open-elements</code></p>
<dl>
<dt>
<dd> Describe open elements in error messages.</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Display a help text and exit.</dl>
<p> <code>-i</code><i>name</i>, <code>&#8211;include=</code><i>name</i></p>
<dl>
<dt>
<dd> This has the same effect as in <code><a href="/docs/linux/man/1-onsgmls/">onsgmls</a>(1)</code>.</dl>
<p> <code>-l</code><i>dtd-file</i>, <code>&#8211;dtd_location=</code><i>dtd-file</i></p>
<dl>
<dt>
<dd> Specify that the resulting XML file should conform to the DTD in <i>dtd-file</i>.</dl>
<p> <code>-n</code>, <code>&#8211;error-numbers</code></p>
<dl>
<dt>
<dd> Show error numbers in error messages.</dl>
<p> <code>&#8211;references</code></p>
<dl>
<dt>
<dd> Show references in error messages.</dl>
<p> <code>-R</code>, <code>&#8211;restricted</code></p>
<dl>
<dt>
<dd> This has the same effect as in <code><a href="/docs/linux/man/1-onsgmls/">onsgmls</a>(1)</code>.</dl>
<p> <code>-v</code>, <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Print the version number and exit.</dl>
<p> <code>-w</code><i>type</i>, <code>&#8211;warning=</code><i>type</i></p>
<dl>
<dt>
<dd> Control warnings and errors according to type. This has the same effect as in <code><a href="/docs/linux/man/1-onsgmls/">onsgmls</a>(1)</code>.</dl>
<p> <code>-x</code><i>xml_output_option</i>, <code>&#8211;xml-output-option=</code><i>xml_output_option</i></p>
<dl>
<dt>
<dd> Control the XML output according to the value of <i>xml_output_option</i> as follows: </p>
<p> <code>no-nl-in-tag</code> Don&#8217;t use newlines inside start-tags. Usually <code>osx</code> uses newlines inside start-tags so as to reduce the probability of excessively long lines. </p>
<p> <code>id</code> Output attribute declarations for ID attributes. </p>
<p> <code>notation</code> Output declarations for notations. </p>
<p> <code>ndata</code> Output declarations for external data entities. XML requires these to be NDATA. <code>osx</code> will warn about CDATA and SDATA external data entities and output them as NDATA entities. </p>
<p> <code>cdata</code> Use XML CDATA sections for CDATA marked sections and for elements with a declared content of CDATA. </p>
<p> <code>comment</code> Output comment declarations. Comment declarations in the DTD will not be output. </p>
<p> <code>lower</code> Prefer lower case. Names that were subjected to upper-case substitution by SGML will be folded to lower case. This does not include reserved names; XML requires these to be in upper-case. </p>
<p> <code>pi-escape</code> Escape &amp;&lt;&gt; in the contents of processing instructions using the amp, lt and gt entities. This allows processing instructions to contain the string &gt;?, but requires that applications handle the escapes. </p>
<p> <code>empty</code> Use the &lt;e/&gt; syntax for element types e declared as EMPTY. </p>
<p> <code>attlist</code> Output an ATTLIST declaration for every element specifying the type of all attributes. The default will always be #IMPLIED. </p>
<p> <code>report-input-sources</code> Output a processing instruction to report when an input source other than the main file is opened or closed in the instance. Do not report any input source changes in the DTD. </p>
<p> <code>report-entities</code> Output a processing instruction to report when an external entity reference has been resolved in the instance. Do not report any entity resolutions in the DTD. </p>
<p> <code>no-expand-external</code> Preserve external entities, write a declaration driver file named &quot;extEntities.dtf&quot;, and include that file in the instance&#8217;s internal subset. </p>
<p> <code>no-expand-internal</code> Preserve internal entities, write a declaration driver file named &quot;intEntities.dtf&quot;, and include that file in the instance&#8217;s internal subset. </p>
<p> <code>no-external-decl</code> Do not include the external entities declaration driver file in the instance&#8217;s internal subset. </p>
<p> <code>no-internal-decl</code> Do not include the internal entities declaration driver file in the instance&#8217;s internal subset. </p>
<p> <code>no-output-outside-outdir</code> When preserving external entities, do not write output files outside the specified output directory (&quot;.&quot; by default). In other words, if an external entity&#8217;s system identifier includes enough instances of &quot;..&quot; to cause osx to write a file outside (above) the output directory, exit (by default osx will issue a warning but will write the file and continue. </p>
<p> <code>no-overwrite</code> When preserving internal or external entities, multiple output files will be written. If this option is specified, do not overwrite existing files; instead, attempt to append a number to the end of the original filename to create a unique filename. Exit with an error if too many (100) such files already exist. </p>
<p> <code>preserve-case</code> Preserve casing as specified in the DTD for element names; attribute names; attribute values which are token lists. </p>
<p> <code>sdata-as-pis</code> When translating SDATA entities (whether expanding them or providing a definition for them in the output&#8217;s internal subset), express them as processing instructions instead of as general internal entities. </p>
<p> Multiple <code>-x</code> options are allowed.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-onsgmls/">onsgmls</a>(1)</code>, <code><a href="/docs/linux/man/1-ospam/">ospam</a>(1)</code>, <code><a href="/docs/linux/man/1-onsgmlnorm/">onsgmlnorm</a>(1)</code>, <code><a href="/docs/linux/man/1-ospent/">ospent</a>(1)</code></p>
<h2>AUTHORS</h2>
<p> <code>James Clark</code></p>
<dl>
<dt>
<dd> Author.</dl>
<p> <code>Ian Castle</code> &lt;ian.castle [at] openjade.org&gt;</p>
<dl>
<dt>
<dd> Author.</dl>
<h2>COPYRIGHT</h2>
<h2>Index</h2>
