---
title: "openjade-1-4devel(1)"
name: "openjade-1-4devel"
section: "1"
letter: "o"
url: "/docs/linux/man/1-openjade-1-4devel/"
description: "openjade – apply a DSSSL stylesheet to an SGML or XML document"
---

<p>openjade &#8211; apply a DSSSL stylesheet to an SGML or XML document </p>
<h2>Synopsis</h2>
<dl COMPACT>
<dt> <code>openjade</code> [<code>-vCegG2s</code>] [<code>-b&nbsp;</code><i>encoding</i>] [<code>-f&nbsp;</code><i>error_file</i>] [<code>-c&nbsp;</code><i>catalog_sysid</i>] [<code>-D&nbsp;</code><i>dir</i>] [<code>-a&nbsp;</code><i>link_type</i>] [<code>-A&nbsp;</code><i>arch</i>] [<code>-E&nbsp;</code><i>max_errors</i>] [<code>-i&nbsp;</code><i>entity</i>] [<code>-w&nbsp;</code><i>warning_type</i>] [<code>-d&nbsp;</code><i>dsssl_spec</i>] [<code>-V&nbsp;</code><i>variable[=value</i>]] [<code>-t&nbsp;</code><i>output_type</i>] [<code>-o&nbsp;</code><i>output_file</i>] [<i>sysid</i>&#8230;] </p>
</dl>
<h2>Description</h2>
<p>&nbsp;<code>openjade</code>&nbsp;is an implementation of the ISO/IEC 10179:1996 standard DSSSL language. The DSSSL engine receives as input an SGML or XML document and transforms it into formats like: </p>
<p> * XML representation of the flow object tree. </p>
<p> * RTF format that can be rendered and printed with Microsoft&#8217;s free Word Viewer 97 </p>
<p> * TeX format </p>
<p> * MIF format that can be rendered and printed with Framemaker </p>
<p> * SGML or XML format. This is used in conjunction with non-standard flow object classes to generate SGML, thus allowing <code>openjade</code> to be used for SGML/XML transformations. </p>
<dd>The system identifier of the document to be processed is specified as an argument to <code>openjade</code>. If this is omitted, standard input will be read. </p>
<p> <code>openjade</code> determines the system identifier for the DSSSL specification as follows: </p>
<p> 1. If the -d option is specified, it will use the argument as the system identifier. </p>
<p> 2. Otherwise, it will look for processing instructions in the prolog of the document. Two kinds of processing instruction are recognized: </p>
<p> &lt;?stylesheet href=&quot;sysid&quot; type=&quot;text/dsssl&quot;&gt; </p>
<p> The system data of the processing instruction is parsed like an SGML start-tag. It will be parsed using the reference concrete syntax whatever the actual concrete syntax of the document. The name that starts the processing instruction can be either stylesheet, xml-stylesheet or xml:stylesheet. The processing instruction will be ignored unless the value of the type attribute is one of text/dsssl, text/x-dsssl, application/dsssl, or application/x-dsssl. The value of href attribute is the system identifier of the DSSSL specification. </p>
<p> &lt;?dsssl sysid&gt; </p>
<p> The system identifier is the portion of the system data of the processing instruction following the initial name and any whitespace. </p>
<p> Although the processing instruction is only recognized in the prolog, it need not occur in the document entity. For example, it could occur in a DTD. The system identifier will be interpreted relative to where the the processing instruction occurs. </p>
<p> 3. Otherwise, it will use the system identifier of the document with any extension changed to .dsl. </p>
<p> A DSSSL specification document can contain more than one style-specification. If the system identifier of the DSSSL specification is followed by #id, then <code>openjade</code> will use the style-specification whose unique identifier is id. This is allowed both with the <code>-d</code> option and with the processing instructions. </p>
<p> The DSSSL specification must be an SGML document conforming to the DSSSL architecture. For an example, see <i>dsssl/demo.dsl</i>. </p>
<p> <code>openjade</code> supports the following options in addition to the normal OpenSP (see <code><a href="/docs/linux/man/1-onsgmls/">onsgmls</a>(1)</code>) options (note that all options are case-sensitive, ie <code>-g</code> and <code>-G</code> are different options): </p>
<dl COMPACT>
<dt><code>-d </code><i>dsssl_spec</i></p>
<dd>This specifies that dsssl_spec is the system identifier of the DSSSL specification to be used. </p>
<dt><code>-G</code></p>
<dd>Debug mode. When an error occurs in the evaluation of an expression, <code>openjade</code> will display a stack trace. Note that this disables tail-call optimization. </p>
<dt><code>-c </code><i>filename</i></p>
<dd>The filename arguments specify catalog files rather than the document entity. The document entity is specified by the first DOCUMENT entry in the catalog files. </p>
<dt><code>-s</code></p>
<dd>Strict compliance mode. Currently the only effect is that jade doesn&#8217;t use any predefined character names, sdata-entity mappings or name-characters. This is useful for checking that your stylesheet is portable to other DSSSL implementations and that it is strictly compliant to the DSSSL specifications. </p>
<dt><code>-t </code><i>output_type</i></p>
<dd><i>output_type</i> specifies the type of output as follows: </p>
<p> <code>fot </code> An XML representation of the flow object tree </p>
<p> <code>rtf</code> <code>rtf-95 </code> RTF (used for SGML/XML to RTF transformations) Microsoft&#8217;s Rich Text Format. rtf-95 produces output optimized for Word 95 rather than Word 97. </p>
<p> <code>tex</code> TeX (used for SGML/XML to TeX transformations) </p>
<p> <code>sgml</code> <code>sgml-raw</code> SGML (used for SGML/XML to SGML transformations). sgml-raw doesn&#8217;t emit linebreaks in tags. </p>
<p> <code>xml</code> <code>xml-raw</code> XML (used for SGML/XML to XML transformations). xml-raw doesn&#8217;t emit linebreaks in tags. </p>
<p> <code>html </code> HTML (used for SGML/XML to HTML transformations) </p>
<p> <code>mif</code> MIF (used for SGML/XML to MIF transformations) </p>
<dt><code>-o </code><i>output_file</i></p>
<dd>Write output to <i>output_file</i> instead of the default. The default filename is the name of the last input file with its extension replaced by the name of the type of output. If there is no input filename, then the extension is added onto jade-out. </p>
<dt><code>-V </code><i>variable</i></p>
<dd>This is equivalent to doing (define variable #t) except that this definition will take priority over any definition of variable in a style-sheet. </p>
<dt><code>-V </code><i>variable=value</i></p>
<dd>This is equivalent to doing (define <i>variable</i> &quot;<i>value</i>&quot;) except that this definition will take priority over any definition of variable in a style-sheet. </p>
<dt><code>-V (define </code><i>variable</i> <i>value</i>)</p>
<dd>This is equivalent to doing (define variable value) except that this definition will take priority over any definition of variable in a style-sheet. Note that you will probably have to use some escaping mechanism for the spaces to get the entire scheme expression parsed as one cmdline argument. </p>
<dt><code>-w</code><i>type</i></p>
<dd>Control warnings and errors. Multiple <code>-w</code> options are allowed. The following values of type enable warnings: </p>
<p> <code>xml</code> Warn about constructs that are not allowed by XML. </p>
<p> <code>mixed</code> Warn about mixed content models that do not allow #pcdata anywhere. </p>
<p> <code>sgmldecl</code> Warn about various dubious constructions in the SGML declaration. </p>
<p> <code>should</code> Warn about various recommendations made in ISO 8879 that the document does not comply with. (Recommendations are expressed with &#8220;should&#8221;, as distinct from requirements which are usually expressed with &#8220;shall&#8221;.) </p>
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
<p> A warning can be disabled by using its name prefixed with no-. Thus <code>-wall</code> <code>-wno-duplicate</code> will enable all warnings except those about duplicate entity declarations. </p>
<p> The following values for <i>warning_type</i> disable errors: </p>
<p> <code>no-idref</code> Do not give an error for an ID reference value which no element has as its ID. The effect will be as if each attribute declared as an ID reference value had been declared as a name. </p>
<p> <code>no-significant</code> Do not give an error when a character that is not a significant character in the reference concrete syntax occurs in a literal in the SGML declaration. This may be useful in conjunction with certain buggy test suites. </p>
<p> <code>no-valid</code> Do not require the document to be type-valid. This has the effect of changing the SGML declaration to specify VALIDITY NOASSERT and IMPLYDEF ATTLIST YES ELEMENT YES. An option of <code>-wvalid</code> has the effect of changing the SGML declaration to specify VALIDITY TYPE and IMPLYDEF ATTLIST NO ELEMENT NO. If neither <code>-wvalid</code> nor <code>-wno-valid</code> are specified, then the VALIDITY and IMPLYDEF specified in the SGML declaration will be used. </p>
</dl>
<h2>Environment</h2>
<p>OpenJade ignores the SP_CHARSET_FIXED and SP_SYSTEM_CHARSET environment variables and always uses Unicode as its internal character set, as if SP_CHARSET_FIXED was 1 and SP_SYSTEM_CHARSET was unset. Thus only the SP_ENCODING environment variable is relevant to OpenJade&#8217;s handling of character sets. </p>
<h2>Openjade Extensions</h2>
<p>The following external procedures are available. These external procedures are defined by a prototype in the same manner as in the standard. To use one of these external procedures, you must make use of the standard external-procedure procedure, using a public identifier of &quot;UNREGISTERED::James Clark//Procedure::name&quot; where name is the name given here, typically by including the following in the DSSSL specification: </p>
<p> (define name (external-procedure &quot;UNREGISTERED::James Clark//Procedure::name&quot;)) </p>
<p> Note that external-procedure returns #f if it doesn&#8217;t know about the specified public identifier. You can use this to enable your DSSSL specifications to work gracefully with other implementations which do not support these extensions. </p>
<p> For external procedures added by the OpenJade team, use a public identifier of the form &quot;UNREGISTERED::OpenJade//Procedure::name&quot;. </p>
<p> An easy way to get access to all external procedures is to use the style specification dsssl/extensions.dsl#procedures. The file dsssl/extensions.dsl also contains style specifications which make the nonstandard flow object classes and inherited characteristics supported by the backends available in a convenient way. </p>
<p> <code>Debugging</code> </p>
<p> (debug obj) </p>
<p> Generates a message including the value of obj and then returns obj. </p>
<p> <code>Simple-page-sequence header/footer control</code> </p>
<p> (if-first-page sosofo1 sosofo2) </p>
<p> This can be used only in the specification of the value of one of the header/footer characteristics of simple-page-sequence. It returns a sosofo that will display as sosofo1 if the page is the first page of the simple-page-sequence and as sosofo2 otherwise. </p>
<p> (if-front-page sosofo1 sosofo2) </p>
<p> This can be used only in the specification of the value of one of the header/footer characteristics of simple-page-sequence. It returns a sosofo that will display as sosofo1 if the page is a front (ie recto, odd-numbered) page and as sosofo2 if it is a back (ie verso, even-numbered) page. </p>
<p> <code>Numbering</code> </p>
<p> (all-element-number) </p>
<p> (all-element-number osnl) </p>
<p> This is the same as element-number except it counts elements with any generic identifier. If osnl is not an element returns #f, otherwise returns 1 plus the number of elements that started before osnl. This provides an efficient way of creating a unique identifier for any element in a document. </p>
<p> <code>External entity access</code> </p>
<p> (read-entity string) </p>
<p> This returns a string containing the contents of the external entity with system identifier string. This should be used only for textual entities (CDATA and SDATA), and not for binary entities (NDATA). </p>
<p> <code>POSIX locale access</code> </p>
<p> (language lang country) </p>
<p> This procedure returns an object of type language, if the system supports the specified language. lang is a string or symbol giving the two letter language code. country is a string or symbol giving the two letter country code. </p>
<p> This procedure uses POSIX locales. It is an OpenJade addition. It is not supported on all operating systems. </p>
<p> <code>Extended standard procedures</code> </p>
<p> (sgml-parse sysid #!key active: parent: architecture:) </p>
<p> This allows you to specify an SGML architecture with respect to which the document should be parsed. It is an OpenJade addition. </p>
<p> (expt q k) </p>
<p> This allows you to raise a quantity to an integral power. It is an OpenJade addition. </p>
<h2>Limitations</h2>
<p>This section describes the limitations of the front-end (the general-purpose DSSSL engine); each backend also has its own limitations. </p>
<p> <code>openjade</code> doesn&#8217;t allow internal definitions at the beginning of bodies and the (test =&gt; recipient) variant of cond clauses. </p>
<p> <code>openjade</code> supports only a single, fixed grove plan which comprises the following modules: </p>
<p> * baseabs </p>
<p> * prlgabs0 </p>
<p> * prlgabs1 </p>
<p> * instabs </p>
<p> * basesds0 </p>
<p> * instsds0 </p>
<p> * subdcabs </p>
<p> It doesn&#8217;t implement the following parts of SDQL: HyTime support, auxiliary parsing, node regular expressions. </p>
<p> Query rules, sosofo synchronization, indirect sosofos, reference values, decoration areas and font properties are not supported. </p>
<p> Note that only inherited characteristics that are applicable to some supported flow object can be specified. </p>
<p> <code>Character/glyph handling</code> </p>
<p> It only supports a single pre-defined character repertoire. A character name of the form U-XXXX where XXXX are four upper-case hexadecimal digits, is recognized as referring to the Unicode character with that code. For many characters, it is also possible to use the ISO/IEC 10646 name in lower-case with words separated by hyphens. </p>
<p> Some common SDATA entity names from the ISO entity sets are recognized and mapped to characters. In addition an SDATA entity name of the form U-XXXX, where XXXX are four upper-case hexadecimal digits, is mapped to the Unicode character with that code. </p>
<p> OpenJade now supports the standard-chars, map-sdata-entity, add-name-chars, add-separator-chars and char-repertoire declaration element forms, allowing a style-sheet to define additional character names, sdata entity mappings, name characters (i.e. characters allowed in identifiers) and separator characters. Currently the only recognized character repertoire is the built-in repertoire. It has the public identifier &quot;UNREGISTERED::OpenJade//Character Repertoire::OpenJade&quot;. </p>
<p> <code>Validation</code> </p>
<p> Several things that it would be desirable to have checked aren&#8217;t checked: </p>
<p> * When the allowed value of an inherited characteristic is a symbol, OpenJade checks only that the value is a symbol that is allowed as the value of some characteristic; #t and #f are treated as a special kind of symbol in this case. </p>
<p> * OpenJade doesn&#8217;t check whether a flow object is occurring in a context where it is allowed. </p>
<p> * OpenJade does not prevent flow objects being attached to the principal port of a flow object when the flow object shouldn&#8217;t have a principal port. </p>
<p> * Most type-checking is done at run-time not compile-time. </p>
<p> * OpenJade does not check for non-inherited characteristics that are required to be specified. </p>
<p> * It doesn&#8217;t check that optional features that have been used were declared in the features form. </p>
<p> <code>Other limitations</code> </p>
<p> The following primitives are just stubs: </p>
<p> <code>char-script-case</code> Always returns last argument. </p>
<p> <code>address-visited?</code> Always returns #f. </p>
<h2>Examples</h2>
<p>Given an SGML file <code>file.sgml</code>, use the stylesheet <code>file.dsl</code> and publish as an rtf file. </p>
<p> openjade -t rtf file.sgml </p>
<p> Using a different stylesheet: </p>
<p> openjade -t rtf -d docbook.dsl file.sgml </p>
<p> Using the <code>print</code> style specification contained within the stylesheet </p>
<p> openjade -t rtf -d docbook.dsl#print file.sgml </p>
<p> And use the html specification within the style sheet to convert to html </p>
<p> openjade -t sgml -i html -d docbook.dsl#html file.sgml </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-onsgmls/">onsgmls</a>(1)</code> </p>
<h2>Authors</h2>
<p>James Clark, Ian Castle &lt;ian.castle [at] looksystems.co.uk&gt;.</p>
