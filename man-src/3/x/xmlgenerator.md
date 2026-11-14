---
title: "xmlgenerator(3)"
name: "xmlgenerator"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmlgenerator/"
---

XML::Generator - Perl extension for generating XML 

<h2>Synopsis</h2><pre> use XML::Generator ':pretty';
 print foo(bar({ baz =&gt; 3 }, bam()),
 bar([ 'qux' =&gt; '<a rel="nofollow" HREF="http://qux.com/'">http://qux.com/'</a> ],
 &quot;Hey there, world&quot;));
 # OR
 require XML::Generator;
 my $X = XML::Generator-&gt;new(':pretty');
 print $X-&gt;foo($X-&gt;bar({ baz =&gt; 3 }, $X-&gt;bam()),
 $X-&gt;bar([ 'qux' =&gt; '<a rel="nofollow" HREF="http://qux.com/'">http://qux.com/'</a> ],
 &quot;Hey there, world&quot;));</pre>Either of the above yield: 

 <pre> &lt;foo xmlns:qux=&quot;<a rel="nofollow" HREF="http://qux.com/">http://qux.com/</a>&quot;&gt;
 &lt;bar baz=&quot;3&quot;&gt;
 &lt;bam /&gt;
 &lt;/bar&gt;
 &lt;qux:bar&gt;Hey there, world&lt;/qux:bar&gt;
 &lt;/foo&gt;</pre><h2>Description</h2>In general, once you have an XML::Generator object, you then simply call methods on that object named for each <font SIZE="-1">XML</font> tag you wish to generate. 

 XML::Generator can also arrange for undefined subroutines in the caller's package to generate the corresponding <font SIZE="-1">XML,</font> by exporting an <tt>&quot;AUTOLOAD&quot;</tt> subroutine to your package. Just supply an ':import' argument to your <tt>&quot;use XML::Generator;&quot;</tt> call. If you already have an <tt>&quot;AUTOLOAD&quot;</tt> defined then XML::Generator can be configured to cooperate with it. See ``<font SIZE="-1">STACKABLE</font> AUTOLOADs''. 

 Say you want to generate this <font SIZE="-1">XML:</font> 

 <pre> &lt;person&gt;
 &lt;name&gt;Bob&lt;/name&gt;
 &lt;age&gt;34&lt;/age&gt;
 &lt;job&gt;Accountant&lt;/job&gt;
 &lt;/person&gt;</pre>Here's a snippet of code that does the job, complete with pretty printing: 

 <pre> use XML::Generator;
 my $gen = XML::Generator-&gt;new(':pretty');
 print $gen-&gt;person(
 $gen-&gt;name(&quot;Bob&quot;),
 $gen-&gt;age(34),
 $gen-&gt;job(&quot;Accountant&quot;)
 );</pre>The only problem with this is if you want to use a tag name that Perl's lexer won't understand as a method name, such as ``shoe-size''. Fortunately, since you can store the name of a method in a variable, there's a simple work-around: 

 <pre> my $shoe_size = &quot;shoe-size&quot;;
 $xml = $gen-&gt;$shoe_size(&quot;12 1/2&quot;);</pre>Which correctly generates: 

 <pre> &lt;shoe-size&gt;12 1/2&lt;/shoe-size&gt;</pre>You can use a hash ref as the first parameter if the tag should include atributes. Normally this means that the order of the attributes will be unpredictable, but if you have the Tie::IxHash module, you can use it to get the order you want, like this: 

 <pre> use Tie::IxHash;
 tie my %attr, 'Tie::IxHash';
 %attr = (name =&gt; 'Bob', 
 age =&gt; 34,
 job =&gt; 'Accountant',
 'shoe-size' =&gt; '12 1/2');
 print $gen-&gt;person(\%attr);</pre>This produces 

 <pre> &lt;person name=&quot;Bob&quot; age=&quot;34&quot; job=&quot;Accountant&quot; shoe-size=&quot;12 1/2&quot; /&gt;</pre>An array ref can also be supplied as the first argument to indicate a namespace for the element and the attributes. 

 If there is one element in the array, it is considered the <font SIZE="-1">URI</font> of the default namespace, and the tag will have an xmlns=``<font SIZE="-1">URI''</font> attribute added automatically. If there are two elements, the first should be the tag prefix to use for the namespace and the second element should be the <font SIZE="-1">URI. </font> In this case, the prefix will be used for the tag and an xmlns:PREFIX attribute will be automatically added. Prior to version 0.99, this prefix was also automatically added to each attribute name. Now, the default behavior is to leave the attributes alone (although you may always explicitly add a prefix to an attribute name). If the prior behavior is desired, use the constructor option <tt>&quot;qualified_attributes&quot;</tt>. 

 If you specify more than two elements, then each pair should correspond to a tag prefix and the corresponding <font SIZE="-1">URL. </font> An xmlns:PREFIX attribute will be added for each pair, and the prefix from the first such pair will be used as the tag's namespace. If you wish to specify a default namespace, use '#default' for the prefix. If the default namespace is first, then the tag will use the default namespace itself. 

 If you want to specify a namespace as well as attributes, you can make the second argument a hash ref. If you do it the other way around, the array ref will simply get stringified and included as part of the content of the tag. 

 Here's an example to show how the attribute and namespace parameters work: 

 <pre> $xml = $gen-&gt;account(
 $gen-&gt;open(['transaction'], 2000),
 $gen-&gt;deposit(['transaction'], { date =&gt; '1999.04.03'}, 1500)
 );</pre>This generates: 

 <pre> &lt;account&gt;
 &lt;open xmlns=&quot;transaction&quot;&gt;2000&lt;/open&gt;
 &lt;deposit xmlns=&quot;transaction&quot; date=&quot;1999.04.03&quot;&gt;1500&lt;/deposit&gt;
 &lt;/account&gt;</pre>Because default namespaces inherit, XML::Generator takes care to output the xmlns=``<font SIZE="-1">URI''</font> attribute as few times as strictly necessary. For example, 

 <pre> $xml = $gen-&gt;account(
 $gen-&gt;open(['transaction'], 2000),
 $gen-&gt;deposit(['transaction'], { date =&gt; '1999.04.03'},
 $gen-&gt;amount(['transaction'], 1500)
 )
 );</pre>This generates: 

 <pre> &lt;account&gt;
 &lt;open xmlns=&quot;transaction&quot;&gt;2000&lt;/open&gt;
 &lt;deposit xmlns=&quot;transaction&quot; date=&quot;1999.04.03&quot;&gt;
 &lt;amount&gt;1500&lt;/amount&gt;
 &lt;/deposit&gt;
 &lt;/account&gt;</pre>Notice how <tt>&quot;xmlns=&quot;transaction&quot;&quot;</tt> was left out of the <tt>&quot;&lt;amount&quot;</tt>&gt; tag. 

 Here is an example that uses the two-argument form of the namespace: 

 <pre> $xml = $gen-&gt;widget(['wru' =&gt; '<a rel="nofollow" HREF="http://www.widgets-r-us.com/xml/'],">http://www.widgets-r-us.com/xml/'],</a>
 {'id' =&gt; 123}, $gen-&gt;contents());
 &lt;wru:widget xmlns:wru=&quot;<a rel="nofollow" HREF="http://www.widgets-r-us.com/xml/">http://www.widgets-r-us.com/xml/</a>&quot; id=&quot;123&quot;&gt;
 &lt;contents /&gt;
 &lt;/wru:widget&gt;</pre>Here is an example that uses multiple namespaces. It generates the first example from the <font SIZE="-1">RDF</font> primer (&lt;<a rel="nofollow" HREF="http://www.w3.org/TR/rdf-primer/">http://www.w3.org/TR/rdf-primer/</a>&gt;). 

 <pre> my $contactNS = [contact =&gt; &quot;<a rel="nofollow" HREF="http://www.w3.org/2000/10/swap/pim/contact#">http://www.w3.org/2000/10/swap/pim/contact#</a>&quot;];
 $xml = $gen-&gt;xml(
 $gen-&gt;RDF([ rdf =&gt; &quot;<a rel="nofollow" HREF="http://www.w3.org/1999/02/22-rdf-syntax-ns#">http://www.w3.org/1999/02/22-rdf-syntax-ns#</a>&quot;,
 @$contactNS ],
 $gen-&gt;Person($contactNS, { 'rdf:about' =&gt; &quot;<a rel="nofollow" HREF="http://www.w3.org/People/EM/contact#me">http://www.w3.org/People/EM/contact#me</a>&quot; },
 $gen-&gt;fullName($contactNS, 'Eric Miller'),
 $gen-&gt;mailbox($contactNS, {'rdf:resource' =&gt; &quot;mailto:em [at] w3.org&quot;}),
 $gen-&gt;personalTitle($contactNS, 'Dr.'))));
 &lt;?xml version=&quot;1.0&quot; standalone=&quot;yes&quot;?&gt;
 &lt;rdf:RDF xmlns:rdf=&quot;<a rel="nofollow" HREF="http://www.w3.org/1999/02/22-rdf-syntax-ns#">http://www.w3.org/1999/02/22-rdf-syntax-ns#</a>&quot;
 xmlns:contact=&quot;<a rel="nofollow" HREF="http://www.w3.org/2000/10/swap/pim/contact#">http://www.w3.org/2000/10/swap/pim/contact#</a>&quot;&gt;
 &lt;contact:Person rdf:about=&quot;<a rel="nofollow" HREF="http://www.w3.org/People/EM/contact#me">http://www.w3.org/People/EM/contact#me</a>&quot;&gt;
 &lt;contact:fullName&gt;Eric Miller&lt;/contact:fullName&gt;
 &lt;contact:mailbox rdf:resource=&quot;mailto:em [at] w3.org&quot; /&gt;
 &lt;contact:personalTitle&gt;Dr.&lt;/contact:personalTitle&gt; 
 &lt;/Person&gt;
 &lt;/rdf:RDF&gt;</pre><h2>Constructor</h2>XML::Generator-&gt;new(':option', ...); 

 XML::Generator-&gt;new(option =&gt; 'value', ...); 

 (Both styles may be combined) 

 The following options are available:
<h3>:std, :standard</h3>Equivalent to 

 <pre> escape =&gt; 'always',
 conformance =&gt; 'strict',</pre><h3>:strict</h3>Equivalent to 

 <pre> conformance =&gt; 'strict',</pre><h3>:pretty[=N]</h3>Equivalent to 

 <pre> escape =&gt; 'always',
 conformance =&gt; 'strict',
 pretty =&gt; N # N defaults to 2</pre><h3>namespace</h3>This value of this option must be an array reference containing one or two values. If the array contains one value, it should be a <font SIZE="-1">URI</font> and will be the value of an 'xmlns' attribute in the top-level tag. If there are two or more elements, the first of each pair should be the namespace tag prefix and the second the <font SIZE="-1">URI</font> of the namespace. This will enable behavior similar to the namespace behavior in previous versions; the tag prefix will be applied to each tag. In addition, an xmlns:NAME=``<font SIZE="-1">URI''</font> attribute will be added to the top-level tag. Prior to version 0.99, the tag prefix was also automatically added to each attribute name, unless overridden with an explicit prefix. Now, the attribute names are left alone, but if the prior behavior is desired, use the constructor option <tt>&quot;qualified_attributes&quot;</tt>. 

 The value of this option is used as the global default namespace. For example, 

 <pre> my $html = XML::Generator-&gt;new(
 pretty =&gt; 2,
 namespace =&gt; [HTML =&gt; &quot;<a rel="nofollow" HREF="http://www.w3.org/TR/REC-html40">http://www.w3.org/TR/REC-html40</a>&quot;]);
 print $html-&gt;html(
 $html-&gt;body(
 $html-&gt;font({ face =&gt; 'Arial' },
 &quot;Hello, there&quot;)));</pre>would yield 

 <pre> &lt;HTML:html xmlns:HTML=&quot;<a rel="nofollow" HREF="http://www.w3.org/TR/REC-html40">http://www.w3.org/TR/REC-html40</a>&quot;&gt;
 &lt;HTML:body&gt;
 &lt;HTML:font face=&quot;Arial&quot;&gt;Hello, there&lt;/HTML:font&gt;
 &lt;/HTML:body&gt;
 &lt;/HTML:html&gt;</pre>Here is the same example except without all the prefixes: 

 <pre> my $html = XML::Generator-&gt;new(
 pretty =&gt; 2,
 namespace =&gt; [&quot;<a rel="nofollow" HREF="http://www.w3.org/TR/REC-html40">http://www.w3.org/TR/REC-html40</a>&quot;]);
 print $html-&gt;html(
 $html-&gt;body(
 $html-&gt;font({ 'face' =&gt; 'Arial' },
 &quot;Hello, there&quot;)));</pre>would yield 

 <pre> &lt;html xmlns=&quot;<a rel="nofollow" HREF="http://www.w3.org/TR/REC-html40">http://www.w3.org/TR/REC-html40</a>&quot;&gt;
 &lt;body&gt;
 &lt;font face=&quot;Arial&quot;&gt;Hello, there&lt;/font&gt;
 &lt;/body&gt;
 &lt;/html&gt;</pre><h3>qualifiedAttributes, qualified_attributes</h3>Set this to a true value to emulate the attribute prefixing behavior of XML::Generator prior to version 0.99. Here is an example: 

 <pre> my $foo = XML::Generator-&gt;new(
 namespace =&gt; [foo =&gt; &quot;<a rel="nofollow" HREF="http://foo.com/">http://foo.com/</a>&quot;],
 qualifiedAttributes =&gt; 1);
 print $foo-&gt;bar({baz =&gt; 3});</pre>yields 

 <pre> &lt;foo:bar xmlns:foo=&quot;<a rel="nofollow" HREF="http://foo.com/">http://foo.com/</a>&quot; foo:baz=&quot;3&quot; /&gt;</pre><h3>escape</h3>The contents and the values of each attribute have any illegal <font SIZE="-1">XML</font> characters escaped if this option is supplied. If the value is 'always', then &amp;, &lt; and &gt; (and &quot; within attribute values) will be converted into the corresponding <font SIZE="-1">XML</font> entity, although &amp; will not be converted if it looks like it could be part of a valid entity (but see below). If the value is 'unescaped', then the escaping will be turned off character-by- character if the character in question is preceded by a backslash, or for the entire string if it is supplied as a scalar reference. So, for example, 

 <pre> use XML::Generator escape =&gt; 'always';
 one('&lt;'); # &lt;one&gt;&amp;lt;&lt;/one&gt;
 two('\&amp;'); # &lt;two&gt;\&amp;amp;&lt;/two&gt;
 three(\'&gt;'); # &lt;three&gt;&amp;gt;&lt;/three&gt; (scalar refs always allowed)
 four('&amp;lt;'); # &lt;four&gt;&amp;lt;&lt;/four&gt; (looks like an entity)
 five('&amp;#34;'); # &lt;five&gt;&amp;#34;&lt;/five&gt; (looks like an entity)</pre>but 

 <pre> use XML::Generator escape =&gt; 'unescaped';
 one('&lt;'); # &lt;one&gt;&amp;lt;&lt;/one&gt;
 two('\&amp;'); # &lt;two&gt;&amp;&lt;/two&gt;
 three(\'&gt;'); # &lt;three&gt;&gt;&lt;/three&gt; (aiee!)
 four('&amp;lt;'); # &lt;four&gt;&amp;amp;lt;&lt;/four&gt; (no special case for entities)</pre>By default, high-bit data will be passed through unmodified, so that <font SIZE="-1">UTF-8</font> data can be generated with pre-Unicode perls. If you know that your data is <font SIZE="-1">ASCII,</font> use the value 'high-bit' for the escape option and bytes with the high bit set will be turned into numeric entities. You can combine this functionality with the other escape options by comma-separating the values: 

 <pre> my $a = XML::Generator-&gt;new(escape =&gt; 'always,high-bit');
 print $a-&gt;foo(&quot;&lt;\242&gt;&quot;);</pre>yields 

 <pre> &lt;foo&gt;&amp;lt;&amp;#162;&amp;gt;&lt;/foo&gt;</pre>Because XML::Generator always uses double quotes (&quot;&quot;) around attribute values, it does not escape single quotes. If you want single quotes inside attribute values to be escaped, use the value 'apos' along with 'always' or 'unescaped' for the escape option. For example: 

 <pre> my $gen = XML::Generator-&gt;new(escape =&gt; 'always,apos');
 print $gen-&gt;foo({'bar' =&gt; &quot;It's all good&quot;});
 &lt;foo bar=&quot;It&amp;apos;s all good&quot; /&gt;</pre>If you actually want &amp; to be converted to &amp;amp; even if it looks like it could be part of a valid entity, use the value 'even-entities' along with 'always'. Supplying 'even-entities' to the 'unescaped' option is meaningless as entities are already escaped with that option.
<h3>pretty</h3>To have nice pretty printing of the output <font SIZE="-1">XML </font>(great for config files that you might also want to edit by hand), supply an integer for the number of spaces per level of indenting, eg. 

 <pre> my $gen = XML::Generator-&gt;new(pretty =&gt; 2);
 print $gen-&gt;foo($gen-&gt;bar('baz'),
 $gen-&gt;qux({ tricky =&gt; 'no'}, 'quux'));</pre>would yield 

 <pre> &lt;foo&gt;
 &lt;bar&gt;baz&lt;/bar&gt;
 &lt;qux tricky=&quot;no&quot;&gt;quux&lt;/qux&gt;
 &lt;/foo&gt;</pre>You may also supply a non-numeric string as the argument to 'pretty', in which case the indents will consist of repetitions of that string. So if you want tabbed indents, you would use: 

 <pre> my $gen = XML::Generator-&gt;new(pretty =&gt; &quot;\t&quot;);</pre>Pretty printing does not apply to <font SIZE="-1">CDATA</font> sections or Processing Instructions.
<h3>conformance</h3>If the value of this option is 'strict', a number of syntactic checks are performed to ensure that generated <font SIZE="-1">XML</font> conforms to the formal <font SIZE="-1">XML</font> specification. In addition, since entity names beginning with 'xml' are reserved by the W3C, inclusion of this option enables several special tag names: xmlpi, xmlcmnt, xmldecl, xmldtd, xmlcdata, and xml to allow generation of processing instructions, comments, <font SIZE="-1">XML</font> declarations, <font SIZE="-1">DTD</font>'s, character data sections and ``final'' <font SIZE="-1">XML</font> documents, respectively. 

 Invalid characters (<a rel="nofollow" HREF="http://www.w3.org/TR/xml11/#charsets)">http://www.w3.org/TR/xml11/#charsets)</a> will be filtered out. To disable this behavior, supply the 'filter_invalid_chars' option with the value 0. 

 See ``<font SIZE="-1">XML CONFORMANCE''</font> and ``<font SIZE="-1">SPECIAL TAGS''</font> for more information.
<h3>filterInvalidChars, filter_invalid_chars</h3>Set this to a 1 to enable filtering of invalid characters, or to 0 to disable the filtering. See <a rel="nofollow" HREF="http://www.w3.org/TR/xml11/#charsets">http://www.w3.org/TR/xml11/#charsets</a> for the set of valid characters.
<h3>allowedXMLTags, allowed_xml_tags</h3>If you have specified 'conformance' =&gt; 'strict' but need to use tags that start with 'xml', you can supply a reference to an array containing those tags and they will be accepted without error. It is not an error to supply this option if 'conformance' =&gt; 'strict' is not supplied, but it will have no effect.
<h3>empty</h3>There are 5 possible values for this option: 

 <pre> self - create empty tags as &lt;tag /&gt; (default)
 compact - create empty tags as &lt;tag/&gt;
 close - close empty tags as &lt;tag&gt;&lt;/tag&gt;
 ignore - don't do anything (non-compliant!)
 args - use count of arguments to decide between &lt;x /&gt; and &lt;x&gt;&lt;/x&gt;</pre>Many web browsers like the 'self' form, but any one of the forms besides 'ignore' is acceptable under the <font SIZE="-1">XML</font> standard. 

 'ignore' is intended for subclasses that deal with <font SIZE="-1">HTML</font> and other <font SIZE="-1">SGML</font> subsets which allow atomic tags. It is an error to specify both 'conformance' =&gt; 'strict' and 'empty' =&gt; 'ignore'. 

 'args' will produce &lt;x /&gt; if there are no arguments at all, or if there is just a single undef argument, and &lt;x&gt;&lt;/x&gt; otherwise.
<h3>version</h3>Sets the default <font SIZE="-1">XML</font> version for use in <font SIZE="-1">XML</font> declarations. See ``xmldecl'' below.
<h3>encoding</h3>Sets the default encoding for use in <font SIZE="-1">XML</font> declarations.
<h3>dtd</h3>Specify the dtd. The value should be an array reference with three values; the type, the name and the uri.
<h2>Import Arguments</h2>use XML::Generator ':option'; 

 use XML::Generator option =&gt; 'value'; 

 (Both styles may be combined)
<h3>:import</h3>Cause <tt>&quot;use XML::Generator;&quot;</tt> to export an <tt>&quot;AUTOLOAD&quot;</tt> to your package that makes undefined subroutines generate <font SIZE="-1">XML</font> tags corresponding to their name. Note that if you already have an <tt>&quot;AUTOLOAD&quot;</tt> defined, it will be overwritten.
<h3>:stacked</h3>Implies :import, but if there is already an <tt>&quot;AUTOLOAD&quot;</tt> defined, the overriding <tt>&quot;AUTOLOAD&quot;</tt> will still give it a chance to run. See ``<font SIZE="-1">STACKED</font> AUTOLOADs''.
<h3><font SIZE="-1">ANYTHING ELSE</font></h3>If you supply any other options, :import is implied and the XML::Generator object that is created to generate tags will be constructed with those options.
<h2>Xml Conformance</h2>When the 'conformance' =&gt; 'strict' option is supplied, a number of syntactic checks are enabled. All entity and attribute names are checked to conform to the <font SIZE="-1">XML</font> specification, which states that they must begin with either an alphabetic character or an underscore and may then consist of any number of alphanumerics, underscores, periods or hyphens. Alphabetic and alphanumeric are interpreted according to the current locale if 'use locale' is in effect and according to the Unicode standard for Perl versions &gt;= 5.6. Furthermore, entity or attribute names are not allowed to begin with 'xml' (in any case), although a number of special tags beginning with 'xml' are allowed (see ``<font SIZE="-1">SPECIAL TAGS''</font>). Note that you can also supply an explicit list of allowed tags with the 'allowed_xml_tags' option. 

 Also, the filter_invalid_chars option is automatically set to 1 unless it is explicitly set to 0.
<h2>Special Tags</h2>The following special tags are available when running under strict conformance (otherwise they don't act special):
<h3>xmlpi</h3>Processing instruction; first argument is target, remaining arguments are attribute, value pairs. Attribute names are syntax checked, values are escaped.
<h3>xmlcmnt</h3>Comment. Arguments are concatenated and placed inside &lt;!-- ... --&gt; comment delimiters. Any occurences of '--' in the concatenated arguments are converted to '&amp;#45;&amp;#45;'
<h3>xmldecl(@args)</h3>Declaration. This can be used to specify the version, encoding, and other XML-related declarations (i.e., anything inside the &lt;?xml?&gt; tag). <tt>@args</tt> can be used to control what is output, as keyword-value pairs. 

 By default, the version is set to the value specified in the constructor, or to 1.0 if it was not specified. This can be overridden by providing a 'version' key in <tt>@args</tt>. If you do not want the version at all, explicitly provide undef as the value in <tt>@args</tt>. 

 By default, the encoding is set to the value specified in the constructor; if no value was specified, the encoding will be left out altogether. Provide an 'encoding' key in <tt>@args</tt> to override this. 

 If a dtd was set in the constructor, the standalone attribute of the declaration will be set to 'no' and the doctype declaration will be appended to the <font SIZE="-1">XML</font> declartion, otherwise the standalone attribute will be set to 'yes'. This can be overridden by providing a 'standalone' key in <tt>@args</tt>. If you do not want the standalone attribute to show up, explicitly provide undef as the value.
<h3>xmldtd</h3><font SIZE="-1">DTD</font> &lt;!DOCTYPE&gt; tag creation. The format of this method is different from others. Since <font SIZE="-1">DTD</font>'s are global and cannot contain namespace information, the first argument should be a reference to an array; the elements are concatenated together to form the <font SIZE="-1">DTD:</font> 

 <pre> print $xml-&gt;xmldtd([ 'html', 'PUBLIC', $xhtml_w3c, $xhtml_dtd ])</pre>This would produce the following declaration: 

 <pre> &lt;!DOCTYPE html PUBLIC &quot;-//W3C//DTD XHTML 1.0 Transitional//EN&quot;
 &quot;DTD/xhtml1-transitional.dtd&quot;&gt;</pre>Assuming that <tt>$xhtml_w3c</tt> and <tt>$xhtml_dtd</tt> had the correct values. 

 Note that you can also specify a <font SIZE="-1">DTD</font> on creation using the <i>new()</i> method's dtd option.
<h3>xmlcdata</h3>Character data section; arguments are concatenated and placed inside &lt;![CDATA[ ... ]]&gt; character data section delimiters. Any occurences of ']]&gt;' in the concatenated arguments are converted to ']]&amp;gt;'.
<h3>xml</h3>``Final'' <font SIZE="-1">XML</font> document. Must be called with one and exactly one XML::Generator-produced <font SIZE="-1">XML</font> document. Any combination of XML::Generator-produced <font SIZE="-1">XML</font> comments or processing instructions may also be supplied as arguments. Prepends an <font SIZE="-1">XML</font> declaration, and re-blesses the argument into a ``final'' class that can't be embedded.
<h2>Creating A Subclass</h2>For a simpler way to implement subclass-like behavior, see ``<font SIZE="-1">STACKABLE</font> AUTOLOADs''. 

 At times, you may find it desireable to subclass XML::Generator. For example, you might want to provide a more application-specific interface to the <font SIZE="-1">XML</font> generation routines provided. Perhaps you have a custom database application and would really like to say: 

 <pre> my $dbxml = new XML::Generator::MyDatabaseApp;
 print $dbxml-&gt;xml($dbxml-&gt;custom_tag_handler(@data));</pre>Here, <i>custom_tag_handler()</i> may be a method that builds a recursive <font SIZE="-1">XML</font> structure based on the contents of <tt>@data</tt>. In fact, it may even be named for a tag you want generated, such as <i>authors()</i>, whose behavior changes based on the contents (perhaps creating recursive definitions in the case of multiple elements). 

 Creating a subclass of XML::Generator is actually relatively straightforward, there are just three things you have to remember: 

 <pre> 1. All of the useful utilities are in XML::Generator::util.
 2. To construct a tag you simply have to call SUPER::tagname,
 where &quot;tagname&quot; is the name of your tag.
 3. You must fully-qualify the methods in XML::Generator::util.</pre>So, let's assume that we want to provide a custom <font SIZE="-1">HTML</font> <i>table()</i> method: 

 <pre> package XML::Generator::CustomHTML;
 use base 'XML::Generator';
 sub table {
 my $self = shift;
 
 # parse our args to get namespace and attribute info
 my($namespace, $attr, @content) =
 $self-&gt;XML::Generator::util::parse_args(@_)
 # check for strict conformance
 if ( $self-&gt;XML::Generator::util::config('conformance') eq 'strict' ) {
 # ... special checks ...
 }
 # ... special formatting magic happens ...
 # construct our custom tags
 return $self-&gt;SUPER::table($attr, $self-&gt;tr($self-&gt;td(@content)));
 }</pre>That's pretty much all there is to it. We have to explicitly call <i>SUPER::table()</i> since we're inside the class's <i>table()</i> method. The others can simply be called directly, assuming that we don't have a <i>tr()</i> in the current package. 

 If you want to explicitly create a specific tag by name, or just want a faster approach than <font SIZE="-1">AUTOLOAD</font> provides, you can use the <i>tag()</i> method directly. So, we could replace that last line above with: 

 <pre> # construct our custom tags 
 return $self-&gt;XML::Generator::util::tag('table', $attr, ...);</pre>Here, we must explicitly call <i>tag()</i> with the tag name itself as its first argument so it knows what to generate. These are the methods that you might find useful:
<dl COMPACT><dt><i>XML::Generator::util::parse_args()</i>
<dd>This parses the argument list and returns the namespace (arrayref), attributes (hashref), and remaining content (array), in that order.
<dt><i>XML::Generator::util::tag()</i>
<dd>This does the work of generating the appropriate tag. The first argument must be the name of the tag to generate.
<dt><i>XML::Generator::util::config()</i>
<dd>This retrieves options as set via the <i>new()</i> method.
<dt><i>XML::Generator::util::escape()</i>
<dd>This escapes any illegal <font SIZE="-1">XML</font> characters.</dl>
 

 Remember that all of these methods must be fully-qualified with the XML::Generator::util package name. This is because <font SIZE="-1">AUTOLOAD</font> is used by the main XML::Generator package to create tags. Simply calling <i>parse_args()</i> will result in a set of <font SIZE="-1">XML</font> tags called &lt;parse_args&gt;. 

 Finally, remember that since you are subclassing XML::Generator, you do not need to provide your own <i>new()</i> method. The one from XML::Generator is designed to allow you to properly subclass it.
<h2>STACKABLE AUTOLOADs</h2>As a simpler alternative to traditional subclassing, the <tt>&quot;AUTOLOAD&quot;</tt> that <tt>&quot;use XML::Generator;&quot;</tt> exports can be configured to work with a pre-defined <tt>&quot;AUTOLOAD&quot;</tt> with the ':stacked' option. Simply ensure that your <tt>&quot;AUTOLOAD&quot;</tt> is defined before <tt>&quot;use XML::Generator ':stacked';&quot;</tt> executes. The <tt>&quot;AUTOLOAD&quot;</tt> will get a chance to run first; the subroutine name will be in your <tt>$AUTOLOAD</tt> as normal. Return an empty list to let the default XML::Generator <tt>&quot;AUTOLOAD&quot;</tt> run or any other value to abort it. This value will be returned as the result of the original method call. 

 If there is no <tt>&quot;import&quot;</tt> defined, XML::Generator will create one. All that this <tt>&quot;import&quot;</tt> does is export <font SIZE="-1">AUTOLOAD,</font> but that lets your package be used as if it were a subclass of XML::Generator. 

 An example will help: 

 <pre> package MyGenerator;
 my %entities = ( copy =&gt; '&amp;copy;',
 nbsp =&gt; '&amp;nbsp;', ... );
 sub AUTOLOAD {
 my($tag) = our $AUTOLOAD =~ /.*::(.*)/;
 return $entities{$tag} if defined $entities{$tag};
 return;
 }
 use XML::Generator qw(:pretty :stacked);</pre>This lets someone do: 

 <pre> use MyGenerator;
 print html(head(title(&quot;My Title&quot;, copy())));</pre>Producing: 

 <pre> &lt;html&gt;
 &lt;head&gt;
 &lt;title&gt;My Title&amp;copy;&lt;/title&gt;
 &lt;/head&gt;
 &lt;/html&gt;</pre><h2>Authors</h2><dl COMPACT><dt>Benjamin Holzman &lt;bholzman [at] earthlink.net&gt;
<dd>Original author and maintainer
<dt>Bron Gondwana &lt;perlcode [at] brong.net&gt;
<dd>First modular version
<dt>Nathan Wiger &lt;nate [at] nateware.com&gt;
<dd>Modular rewrite to enable subclassing</dl><h2>See Also</h2><dl COMPACT><dt>The XML::Writer module
<dd><a rel="nofollow" HREF="http://search.cpan.org/search?mode=module">http://search.cpan.org/search?mode=module</a>&amp;query=XML::Writer 

</dl>
