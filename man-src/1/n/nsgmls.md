---
title: "nsgmls(1)"
name: "nsgmls"
section: "1"
letter: "n"
url: "/docs/linux/man/1-nsgmls/"
description: "onsgmls – An SGML/XML parser and validator"
---

<h2 class="name">NAME</h2>
<p> onsgmls &#8211; An SGML/XML parser and validator </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>onsgmls</code> [<code>-BCdeghlnpRrsuvx</code>] [<code>-a</code><i>linktype</i>] [<code>-A</code><i>architecture</i>] [<code>-b</code><i>bctf</i>] [<code>-c</code><i>sysid</i>&#8230;] [<code>-D</code><i>directory</i>] [<code>-E</code><i>max_errors</i>] [<code>-f</code><i>file</i>] [<code>-i</code><i>name</i>] [<code>-o</code><i>output_option</i>&#8230;] [<code>-t</code><i>file</i>] [<code>-w</code><i>warning_type</i>&#8230;] [<i>sysid</i>&#8230;]</dl>
<h2>DESCRIPTION</h2>
<p> <code>onsgmls</code></p>
<dd>parses and validates the SGML document whose document entity is specified by the system identifiers</p>
<dl>
<dt>
<dd>and prints on the standard output a simple text representation of its Element Structure Information Set. (This is the information set which a structure-controlled conforming SGML application should act upon.) If more than one system identifier is specified, then the corresponding entities will be concatenated to form the document entity. Thus the document entity may be spread among several files; for example, the SGML declaration, prolog and document instance set could each be in a separate file. If no system identifiers are specified, then onsgmls will read the document entity from the standard input. A command line system identifier of &#8211; can be used to refer to the standard input. (Normally in a system identifier, &lt;OSFD&gt;0 is used to refer to standard input.)</dl>
<p> Part of an SGML System Conforming to International Standard ISO 8879 &#8212; Standard Generalized Markup Language. An SGML Extended Facilities system conforming to Annex A of Internal Standard ISO/IEC 10744 &#8212; Hypermedia/Time-based Structuring Language </p>
<p> The following options are available: </p>
<p> <code>-a</code><i>linktype</i>, <code>&#8211;activate=</code><i>linktype</i></p>
<dl>
<dt>
<dd> Make link type <i>linktype</i> active. Not all ESIS information is output in this case: the active LPDs are not explicitly reported, although each link attribute is qualified with its link type name; there is no information about result elements; when there are multiple link rules applicable to the current element, onsgmls always chooses the first.</dl>
<p> <code>-A</code><i>architecture</i>, <code>&#8211;architecture=</code><i>architecture</i></p>
<dl>
<dt>
<dd> Parse with respect to architecture <i>architecture</i>.</dl>
<p> <code>-b</code><i>bctf</i>, <code>&#8211;bctf=</code><i>bctf</i>, <code>-b</code><i>encoding</i>, <code>&#8211;encoding=</code><i>encoding</i></p>
<dl>
<dt>
<dd> This determines the encoding used for output. If in fixed character set mode it specifies the name of an encoding; if not, it specifies the name of a BCTF.</dl>
<p> <code>-B</code>, <code>&#8211;batch_mode</code></p>
<dl>
<dt>
<dd> Batch mode. Parse each</p>
<dl>
<dt>
<dd>specified on the command line separately, rather than concatenating them. This is useful mainly with <code>-s</code>. </p>
<p> If <code>-t</code><i>filename</i> is also specified, then the specified filename will be prefixed to the <i>sysid</i> to make the filename for the RAST result for each <i>sysid</i>.</dl>
</dl>
<p> <code>-c</code><i>sysid</i>, <code>&#8211;catalog=</code><i>sysid</i></p>
<dl>
<dt>
<dd> Map public identifiers and entity names to system identifiers using the catalog entry file whose system identifier is sysid. Multiple <code>-c</code> options are allowed. If there is a catalog entry file called catalog in the same place as the document entity, it will be searched for immediately after those specified by <code>-c</code>.</dl>
<p> <code>-C</code>, <code>&#8211;catalogs</code></p>
<dl>
<dt>
<dd> The</p>
<dl>
<dt>
<dd>arguments specify catalog files rather than the document entity. The document entity is specified by the first DOCUMENT entry in the catalog files.</dl>
</dl>
<p> <code>-D</code><i>directory</i>, <code>&#8211;directory=</code><i>directory</i></p>
<dl>
<dt>
<dd> Search <i>directory</i> for files specified in system identifiers. Multiple <code>-D</code> options are allowed. See the description of the osfile storage manager for more information about file searching.</dl>
<p> <code>-e</code>, <code>&#8211;open-entities</code></p>
<dl>
<dt>
<dd> Describe open entities in error messages. Error messages always include the position of the most recently opened external entity.</dl>
<p> <code>-E</code><i>max_errors</i>, <code>&#8211;max-errors=</code><i>max_errors</i></p>
<dl>
<dt>
<dd> onsgmls will exit after <i>max_errors</i> errors. If <i>max_errors</i> is 0, there is no limit on the number of errors. The default is 200.</dl>
<p> <code>-f</code><i>file</i>, <code>&#8211;error-file=</code><i>file</i></p>
<dl>
<dt>
<dd> Redirect errors to <i>file</i>. This is useful mainly with shells that do not support redirection of stderr.</dl>
<p> <code>-g</code>, <code>&#8211;open-elements</code></p>
<dl>
<dt>
<dd> Show the generic identifiers of open elements in error messages.</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Show a help message and exit.</dl>
<p> <code>-i</code><i>name</i>, <code>&#8211;include=</code><i>name</i></p>
<dl>
<dt>
<dd> Pretend that </p>
<p> &lt;!ENTITY % <i>name</i> &quot;INCLUDE&quot;&gt; </p>
<p> occurs at the start of the document type declaration subset in the SGML document entity. Since repeated definitions of an entity are ignored, this definition will take precedence over any other definitions of this entity in the document type declaration. Multiple -i options are allowed. If the SGML declaration replaces the reserved name INCLUDE then the new reserved name will be the replacement text of the entity. Typically the document type declaration will contain </p>
<p> &lt;!ENTITY % <i>name</i> &quot;IGNORE&quot;&gt; </p>
<p> and will use %<i>name</i>; in the status keyword specification of a marked section declaration. In this case the effect of the option will be to cause the marked section not to be ignored.</dl>
<p> <code>-n</code>, <code>&#8211;error-numbers</code></p>
<dl>
<dt>
<dd> Show message numbers in error messages.</dl>
<p> <code>-o</code><i>output_option</i>, <code>&#8211;option=</code><i>output_option</i></p>
<dl>
<dt>
<dd> Output additional information according to <i>output_option</i>: </p>
<p> <code>entity</code> Output definitions of all general entities not just for data or subdoc entities that are referenced or named in an ENTITY or ENTITIES attribute. </p>
<p> <code>id</code> Distinguish attributes whose declared value is ID. </p>
<p> <code>line</code> Output L commands giving the current line number and filename. </p>
<p> <code>included</code> Output an i command for included sub-elements. </p>
<p> <code>empty</code> Output an e command for elements which are not allowed to have an end-tag, that is those with a declared content of empty or with a content reference attribute. </p>
<p> <code>notation-sysid</code> Output an f command before an N command, if a system identifier could be generated for that notation. </p>
<p> <code>nonsgml</code> In fixed character set mode, output \% escape sequences for non-SGML data characters. Non-SGML data characters can result from numeric character references. </p>
<p> <code>data-attribute</code> Output the notation name and attributes for DATA attributes. Otherwise, DATA attributes are treated like CDATA attributes. For more details see clause 4.4.3 of Annex K of ISO 8879. </p>
<p> <code>comment</code> Output an _ command with the contents of a comment. Multiple comments in a single comment declaration will result in multiple distinct _ commands, just as if the comments were each in a separate comment declaration. </p>
<p> <code>omitted</code> Output an o command before a command which was implied by the input document, but omitted from the actual markup. This currently affects (,), and A commands. </p>
<p> <code>tagomit</code> As <code>omitted</code>, but only for ( and ) commands. </p>
<p> <code>attromit</code> As <code>omitted</code>, but only for A commands. </p>
<p> Multiple <code>-o</code> options are allowed.</dl>
<p> <code>-p</code>, <code>&#8211;only-prolog</code></p>
<dl>
<dt>
<dd> Parse only the prolog. <code>onsgmls</code> will exit after parsing the document type declaration. Implies <code>-s</code>.</dl>
<p> <code>-R</code>, <code>&#8211;restricted</code></p>
<dl>
<dt>
<dd> Restrict file reading. This option is intended for use with onsgmls-based Web tools (e.g. CGI scripts) to prevent reading of arbitrary files on the Web server. With this option enabled, <code>onsgmls</code> will not read any local files unless they are located in a directory (or subdirectory) specified by the <code>-D</code> option or included in the SGML_SEARCH_PATH environment variable. As a further security precaution, this option limits filesnames to the characters A-Z, a-z, 0-9, &#8216;?&#8217;, &#8216;.&#8217;, &#8216;_&#8217;, &#8216;-&#8216; and does not allow filenames containing &quot;..&quot;. On systems with MS-DOS file names &#8216;:&#8217; and &#8216;\&#8217; are also allowed.</dl>
<p> <code>-s</code>, <code>&#8211;no-output</code></p>
<dl>
<dt>
<dd> Suppress output. Error messages will still be printed.</dl>
<p> <code>-t</code><i>file</i>, <code>&#8211;rast-file=</code><i>file</i></p>
<dl>
<dt>
<dd> Output to <i>file</i> the RAST result as defined by ISO/IEC 13673:1995 (actually this isn&#8217;t quite an IS yet; this implements the Intermediate Editor&#8217;s Draft of 1994/08/29, with changes to implement ISO/IEC JTC1/SC18/WG8 N1777). The normal output is not produced.</dl>
<p> <code>-v</code>, <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Print the version number.</dl>
<p> <code>-w</code><i>type</i>, <code>&#8211;warning=</code><i>type</i></p>
<dl>
<dt>
<dd> Control warnings and errors. Multiple <code>-w</code> options are allowed. The following values of type enable warnings: </p>
<p> <code>xml</code> Warn about constructs that are not allowed by XML. </p>
<p> <code>mixed</code> Warn about mixed content models that do not allow #PCDATA anywhere. </p>
<p> <code>sgmldecl</code> Warn about various dubious constructions in the SGML declaration. </p>
<p> <code>should</code> Warn about various recommendations made in ISO 8879 that the document does not comply with. (Recommendations are expressed with &quot;should&quot;, as distinct from requirements which are usually expressed with &quot;shall&quot;.) </p>
<p> <code>default</code> Warn about defaulted references. </p>
<p> <code>duplicate</code> Warn about duplicate entity declarations. </p>
<p> <code>undefined</code> Warn about undefined elements: elements used in the DTD but not defined. </p>
<p> <code>unclosed</code> Warn about unclosed start and end-tags. </p>
<p> <code>empty</code> Warn about empty start and end-tags. </p>
<p> <code>net</code> Warn about net-enabling start-tags and null end-tags. </p>
<p> <code>min-tag</code> Warn about minimized start and end-tags. Equivalent to combination of unclosed, empty and net warnings. </p>
<p> <code>unused-map</code> Warn about unused short reference maps: maps that are declared with a short reference mapping declaration but never used in a short reference use declaration in the DTD. </p>
<p> <code>unused-param</code> Warn about parameter entities that are defined but not used in a DTD. Unused internal parameter entities whose text is INCLUDE or IGNORE won&#8217;t get the warning. </p>
<p> <code>notation-sysid</code> Warn about notations for which no system identifier could be generated. </p>
<p> <code>all</code> Warn about conditions that should usually be avoided (in the opinion of the author). Equivalent to: mixed, should, default, undefined, sgmldecl, unused-map, unused-param, empty and unclosed. </p>
<p> <code>immediate-recursion</code> Warn about immediately recursive elements. For more detais see clause 2.2.5 of Annex K of ISO 8879. </p>
<p> <code>fully-declared</code> Warn if the document instance fails to be fully declared. This has the effect of changing the SGML declaration to specify IMPLYDEF ATTLIST NO ELEMENT NO ENTITY NO NOTATION NO. For more details see clause 2.2.1 of Annex K of ISO 8879. </p>
<p> <code>fully-tagged</code> Warn if the document instance fails to be fully-tagged. This has the effect of changing the SGML declaration to specify DATATAG NO, RANK NO, OMITTAG NO, SHORTTAG STARTTAG EMPTY NO and SHORTTAG ATTRIB OMITNAME NO. For more details see clause 2.2.2 of Annex K of ISO 8879. </p>
<p> <code>amply-tagged, amply-tagged-recursive</code> Warn if the doucment instance fails to be amply-tagged. Implicitly defined elements may be immediately recurisve if <code>amply-tagged-recursive</code> is specified. This has the effect of changing the SGML declaration to specify DATATAG NO, RANK NO, OMITTAG NO, SHORTTAG ATTRIB OMITNAME NO and either IMPLYDEF ELEMENT ANYOTHER or IMPLYDEF ELEMENT YES. For more details see clause 2.2.4 of Annex K of ISO 8879. </p>
<p> <code>type-valid</code> Warn if the document instance fails to be type-valid. This has the effect of changing the SGML declaration to specify VALIDITY YES. For more details see clause 2.2.3 of Annex K of ISO 8879. </p>
<p> <code>entity-ref</code> Warn about references to non-predefined entities. This has the effect of changing the SGML declaration to specify ENTITIES REF NONE. For more details see clause 2.3.2 of Annex K of ISO 8879. </p>
<p> <code>external-entity-ref</code> Warn about references to external entities. This includes references to an external DTD subset. This has the effect of changing the SGML declaration to specify ENTITIES REF INTERNAL. For more details see clause 2.3.3 of Annex K of ISO 8879. </p>
<p> <code>integral</code> Warn if the document instance is not integrally stored. This has the effect of changing the SGML declaration to specify ENTITIES INTEGRAL YES. For more details see clause 2.3.1 of Annex K of ISO 8879. </p>
<p> A warning can be disabled by using its name prefixed with no-. Thus <code>-wall</code><code>-wno-duplicate</code> will enable all warnings except those about duplicate entity declarations. </p>
<p> The following values for <i>warning_type</i> disable errors: </p>
<p> <code>no-idref</code> Do not give an error for an ID reference value which no element has as its ID. The effect will be as if each attribute declared as an ID reference value had been declared as a name. </p>
<p> <code>no-significant</code> Do not give an error when a character that is not a significant character in the reference concrete syntax occurs in a literal in the SGML declaration. This may be useful in conjunction with certain buggy test suites. </p>
<p> <code>no-valid</code> Do not require the document to be type-valid. This has the effect of changing the SGML declaration to specify VALIDITY NOASSERT and IMPLYDEF ATTLIST YES ELEMENT YES. An option of <code>-wvalid</code> has the effect of changing the SGML declaration to specify VALIDITY TYPE and IMPLYDEF ATTLIST NO ELEMENT NO. If neither <code>-wvalid</code> nor <code>-wno-valid</code> are specified, then the VALIDITY and IMPLYDEF specified in the SGML declaration will be used. </p>
<p> <code>no-afdr</code> Do not give errors when AFDR meta-DTD notation features are used in the DTD. These errors are normally produced when parsing the DTD, but suppressed when parsing meta-DTDs.</dl>
<p> <code>-x</code>, <code>&#8211;references</code></p>
<dl>
<dt>
<dd> Show information about relevant clauses (from ISO 8879:1986) in error messages.</dl>
<p> The following options are also supported for backward compatibility with sgmls: </p>
<p> <code>-d</code></p>
<dl>
<dt>
<dd> Same as <code>-wduplicate</code>.</dl>
<p> <code>-l</code></p>
<dl>
<dt>
<dd> Same as <code>-oline</code>.</dl>
<p> <code>-m</code><i>sysid</i></p>
<dl>
<dt>
<dd> Same as <code>-c</code>.</dl>
<p> <code>-r</code></p>
<dl>
<dt>
<dd> Same as <code>-wdefault</code>.</dl>
<p> <code>-u</code></p>
<dl>
<dt>
<dd> Same as <code>-wundef</code>.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ospent/">ospent</a>(1)</code>, <code><a href="/docs/linux/man/1-ospam/">ospam</a>(1)</code>, <code><a href="/docs/linux/man/1-onsgmlnorm/">onsgmlnorm</a>(1)</code>, <code><a href="/docs/linux/man/1-osx/">osx</a>(1)</code></p>
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
