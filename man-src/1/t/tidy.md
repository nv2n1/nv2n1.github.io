---
title: "tidy(1)"
name: "tidy"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tidy/"
---

<h2 class="name">NAME</h2>
 

 <b>tidy</b> - check, correct, and pretty-print 

<a HREF="/docs/linux/man/5-html/">HTML</a>(5) files

<h2>SYNOPSIS</h2>

 <b>tidy</b> [<i>options</i>] [<i>file</i> ...] [<i>options</i>] [<i>file</i> ...] ...

<h2>DESCRIPTION</h2>

 Tidy reads HTML, XHTML, and XML files and writes cleaned-up markup. For HTML variants, it detects, reports, and corrects many common coding errors and strives to produce visually equivalent markup that is both conformant to the HTML specifications and that works in most browsers. 

 A common use of Tidy is to convert plain HTML to XHTML. For generic XML files, Tidy is limited to correcting basic well-formedness errors and pretty printing. 

 If no input file is specified, Tidy reads the standard input. If no output file is specified, Tidy writes the tidied markup to the standard output. If no error file is specified, Tidy writes messages to the standard error.

<h2>OPTIONS</h2>

 Tidy supports two different kinds of options. Purely <i>command-line</i> options, starting with a single dash '<b>-</b>', can only be used on the command-line, not in configuration files. They are listed in the first part of this section. <i>Configuration</i> options, on the other hand, can either be passed on the command line, starting with two dashes <b>--</b>, or specified in a configuration file, using the option name without the starting dashes. They are listed in the second part of this section. 

 For <i>command-line</i> options that expect a numerical argument, a default is assumed if no meaningful value can be found. On the other hand, <i>configuration</i> options cannot be used without a value; a <i>configuration</i> option without a value is simply discarded and reported as an error. 

 Using a <i>command-line</i> option is sometimes equivalent to setting the value of a <i>configuration</i> option. The equivalent option and value are shown in parentheses in the list below, as they would appear in a configuration file. For example, <b>-quiet, -q</b> (<i>quiet: yes</i>) means that using the <i>command-line</i> option <b>-quiet</b> or <b>-q</b> is equivalent to setting the <i>configuration</i> option <i>quiet</i> to <i>yes</i>. 

 Single-letter <i>command-line</i> options without an associated value can be combined; for example '<b>-i</b>', '<b>-m</b>' and '<b>-u</b>' may be combined as '<b>-imu</b>'.

<h3>File manipulation</h3>

 
&nbsp;<wbr>&nbsp;<wbr>
<dl>
<dt><b>-output &lt;%s&gt;</b>, <b>-o &lt;%s&gt;</b> (<i>output-file: &lt;%s&gt;</i>)
<dd> write output to the specified &lt;file&gt;
<dt><b>-config &lt;%s&gt;</b>
<dd> set configuration options from the specified &lt;file&gt;
<dt><b>-file &lt;%s&gt;</b>, <b>-f &lt;%s&gt;</b> (<i>error-file: &lt;%s&gt;</i>)
<dd> write errors and warnings to the specified &lt;file&gt;
<dt><b>-modify</b>, <b>-m</b> (<i>write-back: yes</i>)
<dd> modify the original input files</dl>

<h3>Processing directives</h3>

 
&nbsp;<wbr>&nbsp;<wbr>
<dl>
<dt><b>-indent</b>, <b>-i</b> (<i>indent: auto</i>)
<dd> indent element content
<dt><b>-wrap &lt;%s&gt;</b>, <b>-w &lt;%s&gt;</b> (<i>wrap: &lt;%s&gt;</i>)
<dd> wrap text at the specified &lt;column&gt;. 0 is assumed if &lt;column&gt; is missing. When this option is omitted, the default of the configuration option 'wrap' applies.
<dt><b>-upper</b>, <b>-u</b> (<i>uppercase-tags: yes</i>)
<dd> force tags to upper case
<dt><b>-clean</b>, <b>-c</b> (<i>clean: yes</i>)
<dd> replace FONT, NOBR and CENTER tags with CSS
<dt><b>-bare</b>, <b>-b</b> (<i>bare: yes</i>)
<dd> strip out smart quotes and em dashes, etc.
<dt><b>-gdoc</b>, <b>-g</b> (<i>gdoc: yes</i>)
<dd> produce clean version of html exported by Google Docs
<dt><b>-numeric</b>, <b>-n</b> (<i>numeric-entities: yes</i>)
<dd> output numeric rather than named entities
<dt><b>-errors</b>, <b>-e</b> (<i>markup: no</i>)
<dd> show only errors and warnings
<dt><b>-quiet</b>, <b>-q</b> (<i>quiet: yes</i>)
<dd> suppress nonessential output
<dt><b>-omit</b> (<i>omit-optional-tags: yes</i>)
<dd> omit optional start tags and end tags
<dt><b>-xml</b> (<i>input-xml: yes</i>)
<dd> specify the input is well formed XML
<dt><b>-asxml</b>, <b>-asxhtml</b> (<i>output-xhtml: yes</i>)
<dd> convert HTML to well formed XHTML
<dt><b>-ashtml</b> (<i>output-html: yes</i>)
<dd> force XHTML to well formed HTML
<dt><b>-access &lt;%s&gt;</b> (<i>accessibility-check: &lt;%s&gt;</i>)
<dd> do additional accessibility checks (&lt;level&gt; = 0, 1, 2, 3). 0 is assumed if &lt;level&gt; is missing.</dl>

<h3>Character encodings</h3>

 
&nbsp;<wbr>&nbsp;<wbr>
<dl>
<dt><b>-raw</b>
<dd> output values above 127 without conversion to entities
<dt><b>-ascii</b>
<dd> use ISO-8859-1 for input, US-ASCII for output
<dt><b>-latin0</b>
<dd> use ISO-8859-15 for input, US-ASCII for output
<dt><b>-latin1</b>
<dd> use ISO-8859-1 for both input and output
<dt><b>-iso2022</b>
<dd> use ISO-2022 for both input and output
<dt><b>-utf8</b>
<dd> use UTF-8 for both input and output
<dt><b>-mac</b>
<dd> use MacRoman for input, US-ASCII for output
<dt><b>-win1252</b>
<dd> use Windows-1252 for input, US-ASCII for output
<dt><b>-ibm858</b>
<dd> use IBM-858 (CP850+Euro) for input, US-ASCII for output
<dt><b>-utf16le</b>
<dd> use UTF-16LE for both input and output
<dt><b>-utf16be</b>
<dd> use UTF-16BE for both input and output
<dt><b>-utf16</b>
<dd> use UTF-16 for both input and output
<dt><b>-big5</b>
<dd> use Big5 for both input and output
<dt><b>-shiftjis</b>
<dd> use Shift_JIS for both input and output</dl>

<h3>Miscellaneous</h3>

 
&nbsp;<wbr>&nbsp;<wbr>
<dl>
<dt><b>-version</b>, <b>-v</b>
<dd> show the version of Tidy
<dt><b>-help</b>, <b>-h</b>, <b>-?</b>
<dd> list the command line options
<dt><b>-help-config</b>
<dd> list all configuration options
<dt><b>-show-config</b>
<dd> list the current configuration settings
<dt><b>-help-option &lt;%s&gt;</b>
<dd> show a description of the &lt;option&gt;
<dt><b>-language &lt;%s&gt;</b> (<i>language: &lt;%s&gt;</i>)
<dd> set Tidy's output language to &lt;lang&gt;. Specify '-language help' for more help. Use before output-causing arguments to ensure the language takes effect, e.g.,`tidy -lang es -lang help`.</dl>

<h3>XML</h3>

 
&nbsp;<wbr>&nbsp;<wbr>
<dl>
<dt><b>-xml-help</b>
<dd> list the command line options in XML format
<dt><b>-xml-config</b>
<dd> list all configuration options in XML format
<dt><b>-xml-strings</b>
<dd> output all of Tidy's strings in XML format
<dt><b>-xml-error-strings</b>
<dd> output error constants and strings in XML format
<dt><b>-xml-options-strings</b>
<dd> output option descriptions in XML format</dl>
 

 <i>Configuration</i> options can be specified by preceding each option with <b>--</b> at the command line, followed by its desired value, OR by placing the options and values in a configuration file, and telling tidy to read that file with the <b>-config</b> option: 

 <b>tidy --</b><i>option1 </i>value1 <b>--</b><i>option2 </i>value2 ... 
 <b>tidy -config </b><i>config-file </i> ... 

 <i>Configuration</i> options can be conveniently grouped in a single config file. A Tidy configuration file is simply a text file, where each option is listed on a separate line in the form 

 <i>option1</i>: <i>value1</i> 
 <i>option2</i>: <i>value2</i> 
 etc. 

 The permissible values for a given option depend on the option's Type. There are five Types: <i>Boolean</i>, <i>AutoBool</i>, <i>DocType</i>, <i>Enum</i>, and <i>String</i>. <i>Boolean</i> Types allow any of <b>yes/no, y/n, true/false, t/f, 1/0</b>. <i>AutoBool</i>s allow <b>auto</b> in addition to the values allowed by <i>Booleans</i>. <i>Integer</i> Types take non-negative integers. <i>String</i> Types generally have no defaults, and you should provide them in non-quoted form (unless you wish the output to contain the literal quotes). 

 <i>Enum</i>, <i>Encoding</i>, and <i>DocType</i> Types have a fixed repertoire of items, which are listed in the <i>Supported values</i> sections below. 

 You only need to provide options and values for those whose defaults you wish to override, although you may wish to include some already-defaulted options and values for the sake of documentation and explicitness. 

 Here is a sample config file, with at least one example of each of the five Types: 

 
&nbsp;<wbr><i>//&nbsp;<wbr>sample Tidy configuration options 
&nbsp;<wbr>output-xhtml: yes 
&nbsp;<wbr>add-xml-decl: no 
&nbsp;<wbr>doctype: strict 
&nbsp;<wbr>char-encoding: ascii 
&nbsp;<wbr>indent: auto 
&nbsp;<wbr>wrap: 76 
&nbsp;<wbr>repeated-attributes: keep-last 
&nbsp;<wbr>error-file: errs.txt </i> 

 Below is a summary and brief description of each of the options. They are listed alphabetically within each category.

<h3>HTML, XHTML, XML options</h3>

<dl>
<dt><b>--add-xml-decl</b> <i>Boolean</i> (<b>no</b> if unset)
<dd> 
 This option specifies if Tidy should add the XML declaration when outputting XML or XHTML. 

 Note that if the input already includes an <i>&lt;?xml ... ?&gt;</i> declaration then this option will be ignored. 

 If the encoding for the output is different from <b>ascii</b>, one of the <b>utf*</b> encodings, or <b>raw</b>, then the declaration is always added as required by the XML standard. 

 See also: <b>--char-encoding</b>, <b>--output-encoding</b>
<dt><b>--add-xml-space</b> <i>Boolean</i> (<b>no</b> if unset)
<dd> 
 This option specifies if Tidy should add <i>xml:space=&quot;preserve&quot;</i> to elements such as <i>&lt;pre&gt;</i>, <i>&lt;style&gt;</i> and <i>&lt;script&gt;</i> when generating XML. 

 This is needed if the whitespace in such elements is to be parsed appropriately without having access to the DTD.
<dt><b>--alt-text</b> <i>String</i>
<dd> 
 This option specifies the default <i>alt=</i> text Tidy uses for <i>&lt;img&gt;</i> attributes when the <i>alt=</i> attribute is missing. 

 Use with care, as it is your responsibility to make your documents accessible to people who cannot see the images.
<dt><b>--anchor-as-name</b> <i>Boolean</i> (<b>yes</b> if unset)
<dd> 
 This option controls the deletion or addition of the <i>name</i> attribute in elements where it can serve as anchor. 

 If set to <b>yes</b> a <i>name</i> attribute, if not already existing, is added along an existing <i>id</i> attribute if the DTD allows it. 

 If set to <b>no</b> any existing name attribute is removed if an <i>id</i> attribute exists or has been added.
<dt><b>--assume-xml-procins</b> <i>Boolean</i> (<b>no</b> if unset)
<dd> 
 This option specifies if Tidy should change the parsing of processing instructions to require <i>?&gt;</i> as the terminator rather than <i>&gt;</i>. 

 This option is automatically set if the input is in XML.
<dt><b>--bare</b> <i>Boolean</i> (<b>no</b> if unset)
<dd> 
 This option specifies if Tidy should strip Microsoft specific HTML from Word 2000 documents, and output spaces rather than non-breaking spaces where they exist in the input.
<dt><b>--clean</b> <i>Boolean</i> (<b>no</b> if unset)
<dd> 
 This option specifies if Tidy should perform cleaning of some legacy presentational tags (currently <i>&lt;i&gt;</i>, <i>&lt;b&gt;</i>, <i>&lt;center&gt;</i> when enclosed within appropriate inline tags, and <i>&lt;font&gt;</i>). If set to <b>yes</b> then legacy tags will be replaced with CSS <i>&lt;style&gt;</i> tags and structural markup as appropriate.
<dt><b>--coerce-endtags</b> <i>Boolean</i> (<b>yes</b> if unset)
<dd> 
 This option specifies if Tidy should coerce a start tag into an end tag in cases where it looks like an end tag was probably intended; for example, given 

 <i>&lt;span&gt;foo &lt;b&gt;bar&lt;b&gt; baz&lt;/span&gt;</i> 

 Tidy will output 

 <i>&lt;span&gt;foo &lt;b&gt;bar&lt;/b&gt; baz&lt;/span&gt;</i>
<dt><b>--css-prefix</b> <i>String</i>
<dd> 
 This option specifies the prefix that Tidy uses for styles rules. 

 By default, <b>c</b> will be used.
<dt><b>--decorate-inferred-ul</b> <i>Boolean</i> (<b>no</b> if unset)
<dd> 
 This option specifies if Tidy should decorate inferred <i>&lt;ul&gt;</i> elements with some CSS markup to avoid indentation to the right.
<dt><b>--doctype</b> <i>DocType</i> (<b>auto</b> if unset)
<dd> 
 Supported values: <b>html5, omit, auto, strict, transitional, user</b> 

 This option specifies the DOCTYPE declaration generated by Tidy. 

 If set to <b>omit</b> the output won't contain a DOCTYPE declaration. Note this this also implies <i>numeric-entities</i> is set to <b>yes</b>. 

 If set to <b>html5</b> the DOCTYPE is set to <i>&lt;!DOCTYPE html&gt;</i>. 

 If set to <b>auto</b> (the default) Tidy will use an educated guess based upon the contents of the document. 

 If set to <b>strict</b>, Tidy will set the DOCTYPE to the HTML4 or XHTML1 strict DTD. 

 If set to <b>loose</b>, the DOCTYPE is set to the HTML4 or XHTML1 loose (transitional) DTD. 

 Alternatively, you can supply a string for the formal public identifier (FPI). 

 For example: 

 <i>doctype: &quot;-//ACME//DTD HTML 3.14159//EN&quot;</i> 

 If you specify the FPI for an XHTML document, Tidy will set the system identifier to an empty string. For an HTML document, Tidy adds a system identifier only if one was already present in order to preserve the processing mode of some browsers. Tidy leaves the DOCTYPE for generic XML documents unchanged. 

 This option does not offer a validation of document conformance.
<dt><b>--drop-empty-elements</b> <i>Boolean</i> (<b>yes</b> if unset)
<dd> 
 This option specifies if Tidy should discard empty elements.
<dt><b>--drop-empty-paras</b> <i>Boolean</i> (<b>yes</b> if unset)
<dd> 
 This option specifies if Tidy should discard empty paragraphs.
<dt><b>--drop-font-tags</b> <i>Boolean</i> (<b>no</b> if unset)
<dd> 
 Deprecated; <i>do not use</i>. This option is destructive to <i>&lt;font&gt;</i> tags, and it will be removed from future versions of Tidy. Use the <i>clean</i> option instead. 

 If you do set this option despite the warning it will perform as <i>clean</i> except styles will be inline instead of put into a CSS class. <i>&lt;font&gt;</i> tags will be dropped completely and their styles will not be preserved. 

 If both <i>clean</i> and this option are enabled, <i>&lt;font&gt;</i> tags will still be dropped completely, and other styles will be preserved in a CSS class instead of inline. 

 See <i>clean</i> for more information.
<dt><b>--drop-proprietary-attributes</b> <i>Boolean</i> (<b>no</b> if unset)
<dd> 
 This option specifies if Tidy should strip out proprietary attributes, such as Microsoft data binding attributes. Additionally attributes that aren't permitted in the output version of HTML will be dropped if used with <i>strict-tags-attributes</i>.
<dt><b>--enclose-block-text</b> <i>Boolean</i> (<b>no</b> if unset)
<dd> 
 This option specifies if Tidy should insert a <i>&lt;p&gt;</i> element to enclose any text it finds in any element that allows mixed content for HTML transitional but not HTML strict.
<dt><b>--enclose-text</b> <i>Boolean</i> (<b>no</b> if unset)
<dd> 
 This option specifies if Tidy should enclose any text it finds in the body element within a <i>&lt;p&gt;</i> element. 

 This is useful when you want to take existing HTML and use it with a style sheet.
<dt><b>--escape-cdata</b> <i>Boolean</i> (<b>no</b> if unset)
<dd> 
 This option specifies if Tidy should convert <i>&lt;![CDATA[]]&gt;</i> sections to normal text.
<dt><b>--fix-backslash</b> <i>Boolean</i> (<b>yes</b> if unset)
<dd> 
 This option specifies if Tidy should replace backslash characters <i>\</i> in URLs with forward slashes <i>/</i>.
<dt><b>--fix-bad-comments</b> <i>Boolean</i> (<b>yes</b> if unset)
<dd> 
 This option specifies if Tidy should replace unexpected hyphens with <i>=</i> characters when it comes across adjacent hyphens. 

 The default is <b>yes</b>. 

 This option is provided for users of Cold Fusion which uses the comment syntax: <i>&lt;!--- ---&gt;</i>.
<dt><b>--fix-uri</b> <i>Boolean</i> (<b>yes</b> if unset)
<dd> 
 This option specifies if Tidy should check attribute values that carry URIs for illegal characters and if such are found, escape them as HTML4 recommends.
<dt><b>--gdoc</b> <i>Boolean</i> (<b>no</b> if unset)
<dd> 
 This option specifies if Tidy should enable specific behavior for cleaning up HTML exported from Google Docs.
<dt><b>--hide-comments</b> <i>Boolean</i> (<b>no</b> if unset)
<dd> 
 This option specifies if Tidy should print out comments.
<dt><b>--hide-endtags</b> <i>Boolean</i> (<b>no</b> if unset)
<dd> 
 This option is an alias for <i>omit-optional-tags</i>.
<dt><b>--indent-cdata</b> <i>Boolean</i> (<b>no</b> if unset)
<dd> 
 This option specifies if Tidy should indent <i>&lt;![CDATA[]]&gt;</i> sections.
<dt><b>--input-xml</b> <i>Boolean</i> (<b>no</b> if unset)
<dd> 
 This option specifies if Tidy should use the XML parser rather than the error correcting HTML parser.
<dt><b>--join-classes</b> <i>Boolean</i> (<b>no</b> if unset)
<dd> 
 This option specifies if Tidy should combine class names to generate a single, new class name if multiple class assignments are detected on an element.
<dt><b>--join-styles</b> <i>Boolean</i> (<b>yes</b> if unset)
<dd> 
 This option specifies if Tidy should combine styles to generate a single, new style if multiple style values are detected on an element.
<dt><b>--literal-attributes</b> <i>Boolean</i> (<b>no</b> if unset)
<dd> 
 This option specifies how Tidy deals with whitespace characters within attribute values. 

 If the value is <b>no</b> Tidy normalizes attribute values by replacing any newline or tab with a single space, and further by replacing any contiguous whitespace with a single space. 

 To force Tidy to preserve the original, literal values of all attributes and ensure that whitespace within attribute values is passed through unchanged, set this option to <b>yes</b>.
<dt><b>--logical-emphasis</b> <i>Boolean</i> (<b>no</b> if unset)
<dd> 
 This option specifies if Tidy should replace any occurrence of <i>&lt;i&gt;</i> with <i>&lt;em&gt;</i> and any occurrence of <i>&lt;b&gt;</i> with <i>&lt;strong&gt;</i>. Any attributes are preserved unchanged. 

 This option can be set independently of the <i>clean</i> option.
<dt><b>--lower-literals</b> <i>Boolean</i> (<b>yes</b> if unset)
<dd> 
 This option specifies if Tidy should convert the value of an attribute that takes a list of predefined values to lower case. 

 This is required for XHTML documents.
<dt><b>--merge-divs</b> <i>AutoBool</i> (<b>auto</b> if unset)
<dd> 
 This option can be used to modify the behavior of <i>clean</i> when set to <b>yes</b>. 

 This option specifies if Tidy should merge nested <i>&lt;div&gt;</i> such as <i>&lt;div&gt;&lt;div&gt;...&lt;/div&gt;&lt;/div&gt;</i>. 

 If set to <b>auto</b> the attributes of the inner <i>&lt;div&gt;</i> are moved to the outer one. Nested <i>&lt;div&gt;</i> with <i>id</i> attributes are <i>not</i> merged. 

 If set to <b>yes</b> the attributes of the inner <i>&lt;div&gt;</i> are discarded with the exception of <i>class</i> and <i>style</i>. 

 See also: <b>--clean</b>, <b>--merge-spans</b>
<dt><b>--merge-emphasis</b> <i>Boolean</i> (<b>yes</b> if unset)
<dd> 
 This option specifies if Tidy should merge nested <i>&lt;b&gt;</i> and <i>&lt;i&gt;</i> elements; for example, for the case 

 <i>&lt;b class=&quot;rtop-2&quot;&gt;foo &lt;b class=&quot;r2-2&quot;&gt;bar&lt;/b&gt; baz&lt;/b&gt;</i>, 

 Tidy will output <i>&lt;b class=&quot;rtop-2&quot;&gt;foo bar baz&lt;/b&gt;</i>.
<dt><b>--merge-spans</b> <i>AutoBool</i> (<b>auto</b> if unset)
<dd> 
 This option can be used to modify the behavior of <i>clean</i> when set to <b>yes</b>. 

 This option specifies if Tidy should merge nested <i>&lt;span&gt;</i> such as <i>&lt;span&gt;&lt;span&gt;...&lt;/span&gt;&lt;/span&gt;</i>. 

 The algorithm is identical to the one used by <i>merge-divs</i>. 

 See also: <b>--clean</b>, <b>--merge-divs</b>
<dt><b>--ncr</b> <i>Boolean</i> (<b>yes</b> if unset)
<dd> 
 This option specifies if Tidy should allow numeric character references.
<dt><b>--new-blocklevel-tags</b> <i>Tag names</i>
<dd> 
 This option specifies new block-level tags. This option takes a space or comma separated list of tag names. 

 Unless you declare new tags, Tidy will refuse to generate a tidied file if the input includes previously unknown tags. 

 Note you can't change the content model for elements such as <i>&lt;table&gt;</i>, <i>&lt;ul&gt;</i>, <i>&lt;ol&gt;</i> and <i>&lt;dl&gt;</i>. 

 This option is ignored in XML mode. 

 See also: <b>--new-empty-tags</b>, <b>--new-inline-tags</b>, <b>--new-pre-tags</b>
<dt><b>--new-empty-tags</b> <i>Tag names</i>
<dd> 
 This option specifies new empty inline tags. This option takes a space or comma separated list of tag names. 

 Unless you declare new tags, Tidy will refuse to generate a tidied file if the input includes previously unknown tags. 

 Remember to also declare empty tags as either inline or blocklevel. 

 This option is ignored in XML mode. 

 See also: <b>--new-blocklevel-tags</b>, <b>--new-inline-tags</b>, <b>--new-pre-tags</b>
<dt><b>--new-inline-tags</b> <i>Tag names</i>
<dd> 
 This option specifies new non-empty inline tags. This option takes a space or comma separated list of tag names. 

 Unless you declare new tags, Tidy will refuse to generate a tidied file if the input includes previously unknown tags. 

 This option is ignored in XML mode. 

 See also: <b>--new-blocklevel-tags</b>, <b>--new-empty-tags</b>, <b>--new-pre-tags</b>
<dt><b>--new-pre-tags</b> <i>Tag names</i>
<dd> 
 This option specifies new tags that are to be processed in exactly the same way as HTML's <i>&lt;pre&gt;</i> element. This option takes a space or comma separated list of tag names. 

 Unless you declare new tags, Tidy will refuse to generate a tidied file if the input includes previously unknown tags. 

 Note you cannot as yet add new CDATA elements. 

 This option is ignored in XML mode. 

 See also: <b>--new-blocklevel-tags</b>, <b>--new-empty-tags</b>, <b>--new-inline-tags</b>
<dt><b>--numeric-entities</b> <i>Boolean</i> (<b>no</b> if unset)
<dd> 
 This option specifies if Tidy should output entities other than the built-in HTML entities (<i>&amp;amp;</i>, <i>&amp;lt;</i>, <i>&amp;gt;</i>, and <i>&amp;quot;</i>) in the numeric rather than the named entity form. 

 Only entities compatible with the DOCTYPE declaration generated are used. 

 Entities that can be represented in the output encoding are translated correspondingly. 

 See also: <b>--doctype</b>, <b>--preserve-entities</b>
<dt><b>--omit-optional-tags</b> <i>Boolean</i> (<b>no</b> if unset)
<dd> 
 This option specifies if Tidy should omit optional start tags and end tags when generating output. 

 Setting this option causes all tags for the <i>&lt;html&gt;</i>, <i>&lt;head&gt;</i>, and <i>&lt;body&gt;</i> elements to be omitted from output, as well as such end tags as <i>&lt;/p&gt;</i>, <i>&lt;/li&gt;</i>, <i>&lt;/dt&gt;</i>, <i>&lt;/dd&gt;</i>, <i>&lt;/option&gt;</i>, <i>&lt;/tr&gt;</i>, <i>&lt;/td&gt;</i>, and <i>&lt;/th&gt;</i>. 

 This option is ignored for XML output.
<dt><b>--output-html</b> <i>Boolean</i> (<b>no</b> if unset)
<dd> 
 This option specifies if Tidy should generate pretty printed output, writing it as HTML.
<dt><b>--output-xhtml</b> <i>Boolean</i> (<b>no</b> if unset)
<dd> 
 This option specifies if Tidy should generate pretty printed output, writing it as extensible HTML. 

 This option causes Tidy to set the DOCTYPE and default namespace as appropriate to XHTML, and will use the corrected value in output regardless of other sources. 

 For XHTML, entities can be written as named or numeric entities according to the setting of <i>numeric-entities</i>. 

 The original case of tags and attributes will be preserved, regardless of other options.
<dt><b>--output-xml</b> <i>Boolean</i> (<b>no</b> if unset)
<dd> 
 This option specifies if Tidy should pretty print output, writing it as well-formed XML. 

 Any entities not defined in XML 1.0 will be written as numeric entities to allow them to be parsed by an XML parser. 

 The original case of tags and attributes will be preserved, regardless of other options.
<dt><b>--preserve-entities</b> <i>Boolean</i> (<b>no</b> if unset)
<dd> 
 This option specifies if Tidy should preserve well-formed entities as found in the input.
<dt><b>--quote-ampersand</b> <i>Boolean</i> (<b>yes</b> if unset)
<dd> 
 This option specifies if Tidy should output unadorned <i>&amp;</i> characters as <i>&amp;amp;</i>.
<dt><b>--quote-marks</b> <i>Boolean</i> (<b>no</b> if unset)
<dd> 
 This option specifies if Tidy should output <i>&quot;</i> characters as <i>&amp;quot;</i> as is preferred by some editing environments. 

 The apostrophe character <i>'</i> is written out as <i>&amp;#39;</i> since many web browsers don't yet support <i>&amp;apos;</i>.
<dt><b>--quote-nbsp</b> <i>Boolean</i> (<b>yes</b> if unset)
<dd> 
 This option specifies if Tidy should output non-breaking space characters as entities, rather than as the Unicode character value 160 (decimal).
<dt><b>--repeated-attributes</b> <i>enum</i> (<b>keep-last</b> if unset)
<dd> 
 Supported values: <b>keep-first, keep-last</b> 

 This option specifies if Tidy should keep the first or last attribute, if an attribute is repeated, e.g. has two <i>align</i> attributes. 

 See also: <b>--join-classes</b>, <b>--join-styles</b>
<dt><b>--replace-color</b> <i>Boolean</i> (<b>no</b> if unset)
<dd> 
 This option specifies if Tidy should replace numeric values in color attributes with HTML/XHTML color names where defined, e.g. replace <i>#ffffff</i> with <i>white</i>.
<dt><b>--show-body-only</b> <i>AutoBool</i> (<b>no</b> if unset)
<dd> 
 This option specifies if Tidy should print only the contents of the body tag as an HTML fragment. 

 If set to <b>auto</b>, this is performed only if the body tag has been inferred. 

 Useful for incorporating existing whole pages as a portion of another page. 

 This option has no effect if XML output is requested.
<dt><b>--skip-nested</b> <i>Boolean</i> (<b>yes</b> if unset)
<dd> 
 This option specifies that Tidy should skip nested tags when parsing script and style data.
<dt><b>--strict-tags-attributes</b> <i>Boolean</i> (<b>no</b> if unset)
<dd> 
 This options ensures that tags and attributes are applicable for the version of HTML that Tidy outputs. When set to <b>yes</b> (the default) and the output document type is a strict doctype, then Tidy will report errors. If the output document type is a loose or transitional doctype, then Tidy will report warnings. 

 Additionally if <i>drop-proprietary-attributes</i> is enabled, then not applicable attributes will be dropped, too. 

 When set to <b>no</b>, these checks are not performed.
<dt><b>--uppercase-attributes</b> <i>Boolean</i> (<b>no</b> if unset)
<dd> 
 This option specifies if Tidy should output attribute names in upper case. 

 The default is <b>no</b>, which results in lower case attribute names, except for XML input, where the original case is preserved.
<dt><b>--uppercase-tags</b> <i>Boolean</i> (<b>no</b> if unset)
<dd> 
 This option specifies if Tidy should output tag names in upper case. 

 The default is <b>no</b> which results in lower case tag names, except for XML input where the original case is preserved.
<dt><b>--word-2000</b> <i>Boolean</i> (<b>no</b> if unset)
<dd> 
 This option specifies if Tidy should go to great pains to strip out all the surplus stuff Microsoft Word 2000 inserts when you save Word documents as &quot;Web pages&quot;. It doesn't handle embedded images or VML. 

 You should consider using Word's &quot;Save As: Web Page, Filtered&quot;.</dl>

<h3>Diagnostics options</h3>

 
&nbsp;<wbr>&nbsp;<wbr>
<dl>
<dt><b>--accessibility-check</b> <i>enum</i> (<b>0 (Tidy Classic)</b> if unset)
<dd> 
 Supported values: <b>0 (Tidy Classic), 1 (Priority 1 Checks), 2 (Priority 2 Checks), 3 (Priority 3 Checks)</b> 

 This option specifies what level of accessibility checking, if any, that Tidy should perform. 

 Level <b>0 (Tidy Classic)</b> is equivalent to Tidy Classic's accessibility checking. 

 For more information on Tidy's accessibility checking, visit Tidy's Accessibility Page at <i><a rel="nofollow" HREF="http://www.html-tidy.org/accessibility/">http://www.html-tidy.org/accessibility/</a></i>.
<dt><b>--show-errors</b> <i>Integer</i> (<b>6</b> if unset)
<dd> 
 This option specifies the number Tidy uses to determine if further errors should be shown. If set to <b>0</b>, then no errors are shown.
<dt><b>--show-info</b> <i>Boolean</i> (<b>yes</b> if unset)
<dd> 
 This option specifies if Tidy should display info-level messages.
<dt><b>--show-warnings</b> <i>Boolean</i> (<b>yes</b> if unset)
<dd> 
 This option specifies if Tidy should suppress warnings. This can be useful when a few errors are hidden in a flurry of warnings.</dl>

<h3>Pretty Print options</h3>

 
&nbsp;<wbr>&nbsp;<wbr>
<dl>
<dt><b>--break-before-br</b> <i>Boolean</i> (<b>no</b> if unset)
<dd> 
 This option specifies if Tidy should output a line break before each <i>&lt;br&gt;</i> element.
<dt><b>--escape-scripts</b> <i>Boolean</i> (<b>yes</b> if unset)
<dd> 
 This option causes items that look like closing tags, like <i>&lt;/g</i> to be escaped to <i>&lt;\/g</i>. Set this option to 'no' if you do not want this.
<dt><b>--indent</b> <i>AutoBool</i> (<b>no</b> if unset)
<dd> 
 This option specifies if Tidy should indent block-level tags. 

 If set to <b>auto</b> Tidy will decide whether or not to indent the content of tags such as <i>&lt;title&gt;</i>, <i>&lt;h1&gt;</i>-<i>&lt;h6&gt;</i>, <i>&lt;li&gt;</i>, <i>&lt;td&gt;</i>, or <i>&lt;p&gt;</i> based on the content including a block-level element. 

 Setting <i>indent</i> to <b>yes</b> can expose layout bugs in some browsers. 

 Use the option <i>indent-spaces</i> to control the number of spaces or tabs output per level of indent, and <i>indent-with-tabs</i> to specify whether spaces or tabs are used. 

 See also: <b>--indent-spaces</b>
<dt><b>--indent-attributes</b> <i>Boolean</i> (<b>no</b> if unset)
<dd> 
 This option specifies if Tidy should begin each attribute on a new line.
<dt><b>--indent-spaces</b> <i>Integer</i> (<b>2</b> if unset)
<dd> 
 This option specifies the number of spaces or tabs that Tidy uses to indent content when <i>indent</i> is enabled. 

 Note that the default value for this option is dependent upon the value of <i>indent-with-tabs</i> (see also). 

 See also: <b>--indent</b>
<dt><b>--indent-with-tabs</b> <i>Boolean</i> (<b>no</b> if unset)
<dd> 
 This option specifies if Tidy should indent with tabs instead of spaces, assuming <i>indent</i> is <b>yes</b>. 

 Set it to <b>yes</b> to indent using tabs instead of the default spaces. 

 Use the option <i>indent-spaces</i> to control the number of tabs output per level of indent. Note that when <i>indent-with-tabs</i> is enabled the default value of <i>indent-spaces</i> is reset to <b>1</b>. 

 Note <i>tab-size</i> controls converting input tabs to spaces. Set it to zero to retain input tabs.
<dt><b>--markup</b> <i>Boolean</i> (<b>yes</b> if unset)
<dd> 
 This option specifies if Tidy should generate a pretty printed version of the markup. Note that Tidy won't generate a pretty printed version if it finds significant errors (see <i>force-output</i>).
<dt><b>--punctuation-wrap</b> <i>Boolean</i> (<b>no</b> if unset)
<dd> 
 This option specifies if Tidy should line wrap after some Unicode or Chinese punctuation characters.
<dt><b>--sort-attributes</b> <i>enum</i> (<b>none</b> if unset)
<dd> 
 Supported values: <b>none, alpha</b> 

 This option specifies that Tidy should sort attributes within an element using the specified sort algorithm. If set to <b>alpha</b>, the algorithm is an ascending alphabetic sort.
<dt><b>--split</b> <i>Boolean</i> (<b>no</b> if unset)
<dd> 
 This option has no function and is deprecated.
<dt><b>--tab-size</b> <i>Integer</i> (<b>8</b> if unset)
<dd> 
 This option specifies the number of columns that Tidy uses between successive tab stops. It is used to map tabs to spaces when reading the input.
<dt><b>--vertical-space</b> <i>AutoBool</i> (<b>no</b> if unset)
<dd> 
 This option specifies if Tidy should add some extra empty lines for readability. 

 The default is <b>no</b>. 

 If set to <b>auto</b> Tidy will eliminate nearly all newline characters.
<dt><b>--wrap</b> <i>Integer</i> (<b>68</b> if unset)
<dd> 
 This option specifies the right margin Tidy uses for line wrapping. 

 Tidy tries to wrap lines so that they do not exceed this length. 

 Set <i>wrap</i> to <b>0</b>(zero) if you want to disable line wrapping.
<dt><b>--wrap-asp</b> <i>Boolean</i> (<b>yes</b> if unset)
<dd> 
 This option specifies if Tidy should line wrap text contained within ASP pseudo elements, which look like: <i>&lt;% ... %&gt;</i>.
<dt><b>--wrap-attributes</b> <i>Boolean</i> (<b>no</b> if unset)
<dd> 
 This option specifies if Tidy should line-wrap attribute values, meaning that if the value of an attribute causes a line to exceed the width specified by <i>wrap</i>, Tidy will add one or more line breaks to the value, causing it to be wrapped into multiple lines. 

 Note that this option can be set independently of <i>wrap-script-literals</i>. By default Tidy replaces any newline or tab with a single space and replaces any sequences of whitespace with a single space. 

 To force Tidy to preserve the original, literal values of all attributes, and ensure that whitespace characters within attribute values are passed through unchanged, set <i>literal-attributes</i> to <b>yes</b>. 

 See also: <b>--wrap-script-literals</b>, <b>--literal-attributes</b>
<dt><b>--wrap-jste</b> <i>Boolean</i> (<b>yes</b> if unset)
<dd> 
 This option specifies if Tidy should line wrap text contained within JSTE pseudo elements, which look like: <i>&lt;# ... #&gt;</i>.
<dt><b>--wrap-php</b> <i>Boolean</i> (<b>yes</b> if unset)
<dd> 
 This option specifies if Tidy should line wrap text contained within PHP pseudo elements, which look like: <i>&lt;?php ... ?&gt;</i>.
<dt><b>--wrap-script-literals</b> <i>Boolean</i> (<b>no</b> if unset)
<dd> 
 This option specifies if Tidy should line wrap string literals that appear in script attributes. 

 Tidy wraps long script string literals by inserting a backslash character before the line break. 

 See also: <b>--wrap-attributes</b>
<dt><b>--wrap-sections</b> <i>Boolean</i> (<b>yes</b> if unset)
<dd> 
 This option specifies if Tidy should line wrap text contained within <i>&lt;![ ... ]&gt;</i> section tags.</dl>

<h3>Character Encoding options</h3>

 
&nbsp;<wbr>&nbsp;<wbr>
<dl>
<dt><b>--ascii-chars</b> <i>Boolean</i> (<b>no</b> if unset)
<dd> 
 Can be used to modify behavior of the <i>clean</i> option when set to <b>yes</b>. 

 If set to <b>yes</b> when using <i>clean</i>, <i>&amp;emdash;</i>, <i>&amp;rdquo;</i>, and other named character entities are downgraded to their closest ASCII equivalents. 

 See also: <b>--clean</b>
<dt><b>--char-encoding</b> <i>Encoding</i> (<b>utf8</b> if unset)
<dd> 
 Supported values: <b>raw, ascii, latin0, latin1, utf8, iso2022, mac, win1252, ibm858, utf16le, utf16be, utf16, big5, shiftjis</b> 

 This option specifies the character encoding Tidy uses for both the input and output. 

 For <b>ascii</b> Tidy will accept Latin-1 (ISO-8859-1) character values, but will use entities for all characters whose value &gt;127. 

 For <b>raw</b>, Tidy will output values above 127 without translating them into entities. 

 For <b>latin1</b>, characters above 255 will be written as entities. 

 For <b>utf8</b>, Tidy assumes that both input and output are encoded as UTF-8. 

 You can use <b>iso2022</b> for files encoded using the ISO-2022 family of encodings e.g. ISO-2022-JP. 

 For <b>mac</b> and <b>win1252</b>, Tidy will accept vendor specific character values, but will use entities for all characters whose value &gt;127. 

 For unsupported encodings, use an external utility to convert to and from UTF-8. 

 See also: <b>--input-encoding</b>, <b>--output-encoding</b>
<dt><b>--input-encoding</b> <i>Encoding</i> (<b>utf8</b> if unset)
<dd> 
 Supported values: <b>raw, ascii, latin0, latin1, utf8, iso2022, mac, win1252, ibm858, utf16le, utf16be, utf16, big5, shiftjis</b> 

 This option specifies the character encoding Tidy uses for the input. See <i>char-encoding</i> for more info. 

 See also: <b>--char-encoding</b>
<dt><b>--language</b> <i>String</i>
<dd> 
 Currently not used, but this option specifies the language Tidy would use if it were properly localized. For example: <b>en</b>.
<dt><b>--newline</b> <i>enum</i> (<b>Platform dependent</b> if unset)
<dd> 
 Supported values: <b>LF, CRLF, CR</b> 

 The default is appropriate to the current platform. 

 Genrally CRLF on PC-DOS, Windows and OS/2; CR on Classic Mac OS; and LF everywhere else (Linux, Mac OS X, and Unix).
<dt><b>--output-bom</b> <i>AutoBool</i> (<b>auto</b> if unset)
<dd> 
 This option specifies if Tidy should write a Unicode Byte Order Mark character (BOM; also known as Zero Width No-Break Space; has value of U+FEFF) to the beginning of the output, and only applies to UTF-8 and UTF-16 output encodings. 

 If set to <b>auto</b> this option causes Tidy to write a BOM to the output only if a BOM was present at the beginning of the input. 

 A BOM is always written for XML/XHTML output using UTF-16 output encodings.
<dt><b>--output-encoding</b> <i>Encoding</i> (<b>utf8</b> if unset)
<dd> 
 Supported values: <b>raw, ascii, latin0, latin1, utf8, iso2022, mac, win1252, ibm858, utf16le, utf16be, utf16, big5, shiftjis</b> 

 This option specifies the character encoding Tidy uses for the output. 

 Note that this may only be different from <i>input-encoding</i> for Latin encodings (<b>ascii</b>, <b>latin0</b>, <b>latin1</b>, <b>mac</b>, <b>win1252</b>, <b>ibm858</b>). 

 See <i>char-encoding</i> for more information 

 See also: <b>--char-encoding</b></dl>

<h3>Miscellaneous options</h3>

 
&nbsp;<wbr>&nbsp;<wbr>
<dl>
<dt><b>--error-file</b> <i>String</i>
<dd> 
 This option specifies the error file Tidy uses for errors and warnings. Normally errors and warnings are output to <i>stderr</i>. 

 See also: <b>--output-file</b>
<dt><b>--force-output</b> <i>Boolean</i> (<b>no</b> if unset)
<dd> 
 This option specifies if Tidy should produce output even if errors are encountered. 

 Use this option with care; if Tidy reports an error, this means Tidy was not able to (or is not sure how to) fix the error, so the resulting output may not reflect your intention.
<dt><b>--gnu-emacs</b> <i>Boolean</i> (<b>no</b> if unset)
<dd> 
 This option specifies if Tidy should change the format for reporting errors and warnings to a format that is more easily parsed by GNU Emacs.
<dt><b>--gnu-emacs-file</b> <i>String</i>
<dd> 
 Used internally.
<dt><b>--keep-time</b> <i>Boolean</i> (<b>no</b> if unset)
<dd> 
 This option specifies if Tidy should keep the original modification time of files that Tidy modifies in place. 

 Setting the option to <b>yes</b> allows you to tidy files without changing the file modification date, which may be useful with certain tools that use the modification date for things such as automatic server deployment. 

 Note this feature is not supported on some platforms.
<dt><b>--output-file</b> <i>String</i>
<dd> 
 This option specifies the output file Tidy uses for markup. Normally markup is written to <i>stdout</i>. 

 See also: <b>--error-file</b>
<dt><b>--quiet</b> <i>Boolean</i> (<b>no</b> if unset)
<dd> 
 This option specifies if Tidy should output the summary of the numbers of errors and warnings, or the welcome or informational messages.
<dt><b>--slide-style</b> <i>String</i>
<dd> 
 This option has no function and is deprecated.
<dt><b>--tidy-mark</b> <i>Boolean</i> (<b>yes</b> if unset)
<dd> 
 This option specifies if Tidy should add a <i>meta</i> element to the document head to indicate that the document has been tidied. 

 Tidy won't add a meta element if one is already present.
<dt><b>--write-back</b> <i>Boolean</i> (<b>no</b> if unset)
<dd> 
 This option specifies if Tidy should write back the tidied markup to the same file it read from. 

 You are advised to keep copies of important files before tidying them, as on rare occasions the result may not be what you expect.</dl>

<h2>ENVIRONMENT</h2>

<dl>
<dt><b>HTML_TIDY</b>
<dd> Name of the default configuration file. This should be an absolute path, since you will probably invoke <b>tidy</b> from different directories. The value of HTML_TIDY will be parsed after the compiled-in default (defined with -DTIDY_CONFIG_FILE), but before any of the files specified using <b>-config</b>.</dl>

<h2>EXIT STATUS</h2>

<dl>
<dt>0
<dd> All input files were processed successfully.
<dt>1
<dd> There were warnings.
<dt>2
<dd> There were errors. 

</dl>

<h2>SEE ALSO</h2>

 For more information about HTML Tidy:
<dl>
<dt>
<dd> 

 <a rel="nofollow" HREF="http://www.html-tidy.org/">http://www.html-tidy.org/</a></dl>
 

 For more information on HTML:
<dl>
<dt>
<dd> 

 <b>HTML: Edition for Web Authors</b> (the latest HTML specification) 
 <a rel="nofollow" HREF="http://dev.w3.org/html5/spec-author-view">http://dev.w3.org/html5/spec-author-view</a> 

 <b>HTML: The Markup Language</b> (an HTML language reference) 
 <a rel="nofollow" HREF="http://dev.w3.org/html5/markup/">http://dev.w3.org/html5/markup/</a></dl>
 

 For bug reports and comments:
<dl>
<dt>
<dd> 

 <a rel="nofollow" HREF="https://github.com/htacg/tidy-html5/issues/">https://github.com/htacg/tidy-html5/issues/</a></dl>
 

 Or send questions and comments to <b>public-htacg [at] w3.org</b>. 

 Validate your HTML documents using the <b>W3C Nu Markup Validator</b>:
<dl>
<dt>
<dd> 

 <a rel="nofollow" HREF="http://validator.w3.org/nu/">http://validator.w3.org/nu/</a></dl>

<h2>AUTHOR</h2>

 <b>Tidy</b> was written by <b>Dave Raggett</b> &lt;dsr [at] w3.org&gt;, and subsequently maintained by a team at <a rel="nofollow" HREF="http://tidy.sourceforge.net/,">http://tidy.sourceforge.net/,</a> and now maintained by <b>HTACG</b> (<a rel="nofollow" HREF="http://www.htacg.org">http://www.htacg.org</a>). 

 The sources for <b>HTML Tidy</b> are available at <a rel="nofollow" HREF="https://github.com/htacg/tidy-html5/">https://github.com/htacg/tidy-html5/</a> under the MIT Licence. 

<h2>Index</h2>


