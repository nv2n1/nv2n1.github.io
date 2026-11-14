---
title: "ospam(1)"
name: "ospam"
section: "1"
letter: "o"
url: "/docs/linux/man/1-ospam/"
description: "ospam – An SGML/XML markup stream editor"
---

<h2 class="name">NAME</h2>
<p> ospam &#8211; An SGML/XML markup stream editor </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>ospam</code> [<code>-CeghilprRvx</code>] [<code>-a</code><i>linktype</i>] [<code>-A</code><i>architecture</i>] [<code>-b</code><i>bctf</i>] [<code>-c</code><i>catalog_file</i>] [<code>-D</code><i>directory</i>] [<code>-f</code><i>file</i>] [<code>-m</code><i>markup_option</i>] [<code>-o</code><i>entity_name</i>] [<code>-w</code><i>warning_type</i>] [<i>sysid</i>&#8230;]</dl>
<h2>DESCRIPTION</h2>
<p> <code>ospam</code> (OpenSP Add Markup) is an SGML markup stream editor implemented using the OpenSP parser. <code>ospam</code></p>
<dd>parses the SGML document contained in <i>sysid</i> and copies to the standard output the portion of the document entity containing the document instance, adding or changing markup as specified by the <code>-m</code> options. The <code>-p</code> option can be used to include the SGML declaration and prolog in the output. The <code>-o</code> option can be used to output other entities. The <code>-x</code> option can be used to expand entity references. </p>
<p> Part of an SGML System Conforming to International Standard ISO 8879 &#8212; Standard Generalized Markup Language. An SGML Extended Facilities system conforming to Annex A of Internation Standard ISO/IEC 10744 &#8212; Hypermedia/Time-based Structuring Language. </p>
<p> The following options are available: </p>
<p> <code>-a</code><i>name</i>, <code>&#8211;activate=</code><i>name</i></p>
<dl>
<dt>
<dd> Make doctype or linktype <i>name</i> active.</dl>
<p> <code>-A</code><i>architecture</i>, <code>&#8211;architecture=</code><i>architecture</i></p>
<dl>
<dt>
<dd> Parse with respect to architecture <i>architecture</i>.</dl>
<p> <code>-b</code><i>bctf</i>, <code>&#8211;bctf=</code><i>bctf</i></p>
<dl>
<dt>
<dd> Use bctf <i>bctf</i> for output.</dl>
<p> <code>-c</code><i>sysid</i>, <code>&#8211;catalog=</code><i>sysid</i></p>
<dl>
<dt>
<dd> Use the catalog entry file <i>sysid</i>.</dl>
<p> <code>-C</code>, <code>&#8211;catalogs</code></p>
<dl>
<dt>
<dd> This has the same effect as in <code><a href="/docs/linux/man/1-onsgmls/">onsgmls</a>(1)</code>.</dl>
<p> <code>-D</code><i>directory</i>, <code>&#8211;directory=</code><i>directory</i></p>
<dl>
<dt>
<dd> Search directory for files specified in system identifiers. This has the same effect as in <code><a href="/docs/linux/man/1-onsgmls/">onsgmls</a>(1)</code>.</dl>
<p> <code>-e</code>, <code>&#8211;open-entities</code></p>
<dl>
<dt>
<dd> Describe open entities in error messages.</dl>
<p> <code>-E</code><i>max_errors</i>, <code>&#8211;max-errors=</code><i>max_errors</i></p>
<dl>
<dt>
<dd> Exit after <i>max_errors</i> errors are encountered.</dl>
<p> <code>-f</code><i>file</i>, <code>&#8211;error-file=</code><i>file</i></p>
<dl>
<dt>
<dd> Redirect errors to <i>file</i>. This is useful mainly with shells that do not support redirection of stderr.</dl>
<p> <code>-g</code>, <code>&#8211;open-elements</code></p>
<dl>
<dt>
<dd> Show the generic identifiers of open elements in error messages.</dl>
<p> <code>-h</code>, <code>&#8211;hoist-omitted-tags</code></p>
<dl>
<dt>
<dd> Hoist omitted tags out from the start of internal entities. If the text at the beginning of an internal entity causes a tag to be implied, the tag will usually be treated as being in that internal entity; this option will instead cause it to be treated as being in the entity that referenced the internal entity. This option makes a difference in conjunction with <code>-momittag</code> or <code>-x</code><code>-x</code>.</dl>
<p> <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Display a help text and exit.</dl>
<p> <code>-i</code><i>name</i>, <code>&#8211;include=</code><i>name</i></p>
<dl>
<dt>
<dd> This has the same effect as in <code><a href="/docs/linux/man/1-onsgmls/">onsgmls</a>(1)</code>.</dl>
<p> <code>-l</code>, <code>&#8211;lowercase</code></p>
<dl>
<dt>
<dd> Prefer lower-case. Added names that were subject to upper-case substitution will be converted to lower-case.</dl>
<p> <code>-m</code><i>markup_option</i>, <code>&#8211;markup-option=</code><i>markup_option</i></p>
<dl>
<dt>
<dd> Change the markup in the output according to the value of <i>markup_option</i> as follows: </p>
<p> <code>omittag</code> Add tags that were omitted using omitted tag minimization. End tags that were omitted because the element has a declared content of EMPTY or an explicit content reference will not be added. </p>
<p> <code>shortref</code> Replace short references by named entity references. </p>
<p> <code>net</code> Change null end-tags into unminimized end-tags, and change net-enabling start-tags into unminimized start-tags. </p>
<p> <code>emptytag</code> Change empty tags into unminimized tags. </p>
<p> <code>unclosed</code> Change unclosed tags into unminimized tags. </p>
<p> <code>attname</code> Add omitted attribute names and vis. </p>
<p> <code>attvalue</code> Add literal delimiters omitted from attribute values. </p>
<p> <code>attspec</code> Add omitted attribute specifications. </p>
<p> <code>current</code> Add omitted attribute specifications for current attributes. This option is implied by the attspec option. </p>
<p> <code>shorttag</code> Equivalent to combination of net, emptytag, unclosed, attname, attvalue and attspec options. </p>
<p> <code>rank</code> Add omitted rank suffixes. </p>
<p> <code>reserved</code> Put reserved names in upper-case. </p>
<p> <code>ms</code> Remove marked section declarations whose effective status is IGNORE, and replace each marked section declaration whose effective status is INCLUDE by its marked section. In the document instance, empty comments will be added before or after the marked section declaration to ensure that ignored record ends remain ignored. </p>
<p> Multiple -m options are allowed.</dl>
<p> <code>-n</code>, <code>&#8211;error-numbers</code></p>
<dl>
<dt>
<dd> Show error numbers in error messages.</dl>
<p> <code>-o</code><i>name</i>, <code>&#8211;output-entity=</code><i>name</i></p>
<dl>
<dt>
<dd> Output the general entity name instead of the document entity. The output will correspond to the first time that the entity is referenced in content.</dl>
<p> <code>-p</code>, <code>&#8211;output-prolog</code></p>
<dl>
<dt>
<dd> Output the part of the document entity containing the SGML declaration (if it was explicitly present in the document entity) and the prolog before anything else. If this option is specified two or more times, then all entity references occurring between declarations in the prolog will be expanded; this includes the implicit reference to the entity containing the external subset of the DTD, if there is one. Note that the SGML declaration will not be included if it was specified by an SGMLDECL entry in a catalog.</dl>
<p> <code>-r</code>, <code>&#8211;raw</code></p>
<dl>
<dt>
<dd> Don&#8217;t perform any conversion on RSs and REs when outputting the entity. The entity would typically have the storage manager attribute records=asis.</dl>
<p> <code>-R</code>, <code>&#8211;restricted</code></p>
<dl>
<dt>
<dd> This as the same effect as in <code><a href="/docs/linux/man/1-onsgmls/">onsgmls</a>(1)</code></dl>
<p> <code>-v</code>, <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Print the version number.</dl>
<p> <code>-w</code><i>type</i>, <code>&#8211;warning=</code><i>type</i></p>
<dl>
<dt>
<dd> Control warnings and errors according to type. This has the same effect as in <code><a href="/docs/linux/man/1-onsgmls/">onsgmls</a>(1)</code>.</dl>
<p> <code>-x</code>, <code>&#8211;expand-references</code></p>
<dl>
<dt>
<dd> Expand references to entities that are changed. If this option is specified two or more times, then all references to entities that contain tags will be expanded.</dl>
<h2>BUGS</h2>
<p> Omitted tags are added at the point where they are implied by the SGML parser (except as modified by the <code>-h</code> option); this is often not quite where they are wanted. </p>
<p> The case of general delimiters is not preserved. </p>
<p> Incorrect results may be produced if a variant concrete syntax is used which is such that there are delimiters in markup to be added that have a prefix that is a proper suffix of some other delimiter. </p>
<p> If an entity reference in a default value uses the default entity and an entity with that name is subsequently defined and that default value is added to the document instance, then the resulting document may not be equivalent to the original document. <code>ospam</code> will give a warning when the first two conditions are met.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-onsgmls/">onsgmls</a>(1)</code>, <code><a href="/docs/linux/man/1-ospent/">ospent</a>(1)</code>, <code><a href="/docs/linux/man/1-onsgmlnorm/">onsgmlnorm</a>(1)</code>, <code><a href="/docs/linux/man/1-osx/">osx</a>(1)</code></p>
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
