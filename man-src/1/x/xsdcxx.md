---

title: "xsdcxx(1)"
name: "xsdcxx"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xsdcxx/"
description: "xsdcxx – W3C XML Schema to C++ Compiler"
---

<p> xsdcxx &#8211; W3C XML Schema to C++ Compiler</p>
<h2>SYNOPSIS</h2>
<p> <code>xsdcxx</code> <i>command</i> <code>[</code> <i>options</i> <code>]</code> <i>file</i> <code>[</code> <i>file</i> <code>&#8230;]</code> <code>xsdcxx help</code> <code>[</code> <i>command</i> <code>]</code> <code>xsdcxx version</code></p>
<h2>DESCRIPTION</h2>
<p> <code>xsdcxx</code> generates vocabulary-specific, statically-typed C++ mapping from W3C XML Schema definitions. Particular mapping to produce is selected by a <i>command</i>. Each mapping has a number of mapping-specific <i>options</i> that should appear, if any, after the <i>command</i>. Input files should be W3C XML Schema definitions. The exact set of the generated files depends on the selected mapping and options.</p>
<h2>COMMANDS</h2>
<dl>
<dt><code>cxx-tree</code></dt>
<dd> Generate the C++/Tree mapping. For each input file in the form <code>name.xsd</code> the following C++ files are generated: <code>name.hxx</code> (header file), <code>name.ixx</code> (inline file, generated only if the <code>&#8211;generate-inline</code> option is specified), <code>name.cxx</code> (source file), and <code>name-fwd.hxx</code> (forward declaration file, generated only if the <code>&#8211;generate-forward</code> option is specified). </dd>
<dt><code>cxx-parser</code></dt>
<dd> Generate the C++/Parser mapping. For each input file in the form <code>name.xsd</code> the following C++ files are generated: <code>name-pskel.hxx</code> (parser skeleton header file), <code>name-pskel.ixx</code> (parser skeleton inline file, generated only if the <code>&#8211;generate-inline</code> option is specified), and <code>name-pskel.cxx</code> (parser skeleton source file). If the <code>&#8211;generate-noop-impl</code> or <code>&#8211;generate-print-impl</code> option is specified, the following additional sample implementation files are generated: <code>name-pimpl.hxx</code> (parser implementation header file) and <code>name-pimpl.cxx</code> (parser implementation source file). If the <code>&#8211;generate-test-driver</code> option is specified, the additional <code>name-driver.cxx</code> test driver file is generated. </dd>
<dt><code>help</code></dt>
<dd> Print usage information and exit. Use</dd></dl>
<dl>
<dl>
<dt>
</dt><dd> <code>xsdcxx help</code> <i>command</i></dd></dl>
<p> for command-specific help.</dl>
<dl>
<dt><code>version</code></dt>
<dd> Print version and exit.</dd></dl>
<h2>OPTIONS</h2>
<p> Command-specific <i>options</i>, if any, should appear after the corresponding <i>command</i>. </p>
<h3>common options</h3>
<dl>
<dt><code>&#8211;std</code> <i>version</i></dt>
<dd> Specify the C++ standard that the generated code should conform to. Valid values are <code>c++98</code> (default) and <code>c++11</code>. </dd>
<p> The C++ standard affects various aspects of the generated code that are discussed in more detail in various mapping-specific documentation. Overall, when C++11 is selected, the generated code relies on the move semantics and uses <code>std::unique_ptr</code> instead of deprecated <code>std::auto_ptr</code>. </p>
<p> When the C++11 mode is selected, you normally don&#8217;t need to perform any extra steps other than enable C++11 in your C++ compiler, if required. The XSDCXX compiler will automatically add the necessary macro defines to the generated header files that will switch the header-only XSDCXX runtime library (<code>libxsd</code>) to the C++11 mode. However, if you include any of the XSDCXX runtime headers directly in your application (normally you just include the generated headers), then you will need to define the <code>XSD_CXX11</code> macro for your entire project. </p>
<dt><code>&#8211;char-type</code> <i>type</i></dt>
<dd> Generate code using the provided character <i>type</i> instead of the default <code>char</code>. Valid values are <code>char</code> and <code>wchar_t</code>. </dd>
<dt><code>&#8211;char-encoding</code> <i>enc</i></dt>
<dd> Specify the character encoding that should be used in the generated code. Valid values for the <code>char</code> character type are <code>utf8</code> (default), <code>iso8859-1</code>, <code>lcp</code> (Xerces-C++ local code page), and <code>custom</code>. If you pass <code>custom</code> as the value then you will need to include the transcoder implementation header for your encoding at the beginning of the generated header files (see the <code>&#8211;hxx-prologue</code> option). </dd>
<p> For the <code>wchar_t</code> character type the only valid value is <code>auto</code> and the encoding is automatically selected between UTF-16 and UTF-32/UCS-4, depending on the <code>wchar_t</code> type size. </p>
<dt><code>&#8211;output-dir</code> <i>dir</i></dt>
<dd> Write generated files to <i>dir</i> instead of the current directory. </dd>
<dt><code>&#8211;generate-inline</code></dt>
<dd> Generate simple functions inline. This option triggers creation of the inline file. </dd>
<dt><code>&#8211;generate-xml-schema</code></dt>
<dd> Generate a C++ header file as if the schema being compiled defines the XML Schema namespace. For the C++/Tree mapping, the resulting file will contain definitions for all XML Schema built-in types. For the C++/Parser mapping, the resulting file will contain definitions for all the parser skeletons and implementations corresponding to the XML Schema built-in types. </dd>
<p> The schema file provided to the compiler need not exist and is only used to derive the name of the resulting header file. Use the <code>&#8211;extern-xml-schema</code> option to include this file in the generated files for other schemas. </p>
<dt><code>&#8211;extern-xml-schema</code> <i>file</i></dt>
<dd> Include a header file derived from <i>file</i> instead of generating the XML Schema namespace mapping inline. The provided file need not exist and is only used to derive the name of the included header file. Use the <code>&#8211;generate-xml-schema</code> option to generate this header file. </dd>
<dt><code>&#8211;namespace-map</code> <i>xns</i>=<i>cns</i></dt>
<dd> Map XML Schema namespace <i>xns</i> to C++ namespace <i>cns</i>. Repeat this option to specify mapping for more than one XML Schema namespace. For example, the following option: </dd>
<p> <code>&#8211;namespace-map <a rel="nofollow" href="http://example.com/foo/bar=foo::bar">http://example.com/foo/bar=foo::bar</a></code> </p>
<p> Will map the <code><a rel="nofollow" href="http://example.com/foo/bar">http://example.com/foo/bar</a></code> XML Schema namespace to the <code>foo::bar</code> C++ namespace. </p>
<dt><code>&#8211;namespace-regex</code> <i>regex</i></dt>
<dd> Add <i>regex</i> to the list of regular expressions used to translate XML Schema namespace names to C++ namespace names. <i>regex</i> is a Perl-like regular expression in the form <code>/</code><i>pattern</i><code>/</code><i>replacement</i><code>/</code>. Any character can be used as a delimiter instead of <code>/</code>. Escaping of the delimiter character in <i>pattern</i> or <i>replacement</i> is not supported. </dd>
<p> All the regular expressions are pushed into a stack with the last specified expression considered first. The first match that succeeds is used. Regular expressions are applied to a string in the form </p>
<p> <i>filename</i> <i>namespace</i> </p>
<p> For example, if you have file <code>hello.xsd</code> with namespace <code><a rel="nofollow" href="http://example.com/hello">http://example.com/hello</a></code> and you run <code>xsd</code> on this file, then the string in question will be: </p>
<p> <code>hello.xsd. <a rel="nofollow" href="http://example.com/hello">http://example.com/hello</a></code> </p>
<p> For the built-in XML Schema namespace the string is: </p>
<p> <code>XMLSchema.xsd <a rel="nofollow" href="http://www.w3.org/2001/XMLSchema">http://www.w3.org/2001/XMLSchema</a></code> </p>
<p> The following three steps are performed for each regular expression until the match is found: </p>
<p> 1. The expression is applied and if the result is empty the next expression is considered. </p>
<p> 2. All <code>/</code> are replaced with <code>::</code>. </p>
<p> 3. The result is verified to be a valid C++ scope name (e.g., <code>foo::bar</code>). If this test succeeds, the result is used as a C++ namespace name. </p>
<p> As an example, the following expression maps XML Schema namespaces in the form <code><a rel="nofollow" href="http://example.com/foo/bar">http://example.com/foo/bar</a></code> to C++ namespaces in the form <code>foo::bar</code>: </p>
<p> <code>%.* <a rel="nofollow" href="http://example.com/(.+)%$1%">http://example.com/(.+)%$1%</a></code> </p>
<p> See also the REGEX AND SHELL QUOTING section below. </p>
<dt><code>&#8211;namespace-regex-trace</code></dt>
<dd> Trace the process of applying regular expressions specified with the <code>&#8211;namespace-regex</code> option. Use this option to find out why your regular expressions don&#8217;t do what you expected them to do. </dd>
<dt><code>&#8211;reserved-name</code> <i>n</i>[=<i>r</i>]</dt>
<dd> Add name <i>n</i> to the list of names that should not be used as identifiers. The name can optionally be followed by <code>=</code> and the replacement name <i>r</i> that should be used instead. All the C++ keywords are already in this list. </dd>
<dt><code>&#8211;include-with-brackets</code></dt>
<dd> Use angle brackets (&lt;&gt;) instead of quotes (&quot;&quot;) in generated <code>#include</code> directives. </dd>
<dt><code>&#8211;include-prefix</code> <i>prefix</i></dt>
<dd> Add <i>prefix</i> to generated <code>#include</code> directive paths. </dd>
<p> For example, if you had the following import element in your schema </p>
<p> <code>&lt;import namespace=&quot;&#8230;&quot; schemaLocation=&quot;base.xsd&quot;/&gt;</code> </p>
<p> and compiled this fragment with <code>&#8211;include-prefix schemas/</code>, then the include directive in the generated code would be: </p>
<p> <code>#include &quot;schemas/base.hxx&quot;</code> </p>
<dt><code>&#8211;include-regex</code> <i>regex</i></dt>
<dd> Add <i>regex</i> to the list of regular expressions used to transform <code>#include</code> directive paths. <i>regex</i> is a Perl-like regular expression in the form <code>/</code><i>pattern</i><code>/</code><i>replacement</i><code>/</code>. Any character can be used as a delimiter instead of <code>/</code>. Escaping of the delimiter character in <i>pattern</i> or <i>replacement</i> is not supported. </dd>
<p> All the regular expressions are pushed into a stack with the last specified expression considered first. The first match that succeeds is used. </p>
<p> As an example, the following expression transforms paths in the form <code>schemas/foo/bar</code> to paths in the form <code>generated/foo/bar</code>: </p>
<p> <code>%schemas/(.+)%generated/$1%</code> </p>
<p> See also the REGEX AND SHELL QUOTING section below. </p>
<dt><code>&#8211;include-regex-trace</code></dt>
<dd> Trace the process of applying regular expressions specified with the <code>&#8211;include-regex</code> option. Use this option to find out why your regular expressions don&#8217;t do what you expected them to do. </dd>
<dt><code>&#8211;guard-prefix</code> <i>prefix</i></dt>
<dd> Add <i>prefix</i> to generated header inclusion guards. The prefix is transformed to upper case and characters that are illegal in a preprocessor macro name are replaced with underscores. If this option is not specified then the directory part of the input schema file is used as a prefix. </dd>
<dt><code>&#8211;hxx-suffix</code> <i>suffix</i></dt>
<dd> Use the provided <i>suffix</i> instead of the default <code>.hxx</code> to construct the name of the header file. Note that this suffix is also used to construct names of header files corresponding to included/imported schemas. </dd>
<dt><code>&#8211;ixx-suffix</code> <i>suffix</i></dt>
<dd> Use the provided <i>suffix</i> instead of the default <code>.ixx</code> to construct the name of the inline file. </dd>
<dt><code>&#8211;cxx-suffix</code> <i>suffix</i></dt>
<dd> Use the provided <i>suffix</i> instead of the default <code>.cxx</code> to construct the name of the source file. </dd>
<dt><code>&#8211;fwd-suffix</code> <i>suffix</i></dt>
<dd> Use the provided <i>suffix</i> instead of the default <code>-fwd.hxx</code> to construct the name of the forward declaration file. </dd>
<dt><code>&#8211;hxx-regex</code> <i>regex</i></dt>
<dd> Use the provided expression to construct the name of the header file. <i>regex</i> is a Perl-like regular expression in the form <code>/</code><i>pattern</i><code>/</code><i>replacement</i><code>/</code>. Note that this expression is also used to construct names of header files corresponding to included/imported schemas. See also the REGEX AND SHELL QUOTING section below. </dd>
<dt><code>&#8211;ixx-regex</code> <i>regex</i></dt>
<dd> Use the provided expression to construct the name of the inline file. <i>regex</i> is a Perl-like regular expression in the form <code>/</code><i>pattern</i><code>/</code><i>replacement</i><code>/</code>. See also the REGEX AND SHELL QUOTING section below. </dd>
<dt><code>&#8211;cxx-regex</code> <i>regex</i></dt>
<dd> Use the provided expression to construct the name of the source file. <i>regex</i> is a Perl-like regular expression in the form <code>/</code><i>pattern</i><code>/</code><i>replacement</i><code>/</code>. See also the REGEX AND SHELL QUOTING section below. </dd>
<dt><code>&#8211;fwd-regex</code> <i>regex</i></dt>
<dd> Use the provided expression to construct the name of the forward declaration file. <i>regex</i> is a Perl-like regular expression in the form <code>/</code><i>pattern</i><code>/</code><i>replacement</i><code>/</code>. See also the REGEX AND SHELL QUOTING section below. </dd>
<dt><code>&#8211;hxx-prologue</code> <i>text</i></dt>
<dd> Insert <i>text</i> at the beginning of the header file. </dd>
<dt><code>&#8211;ixx-prologue</code> <i>text</i></dt>
<dd> Insert <i>text</i> at the beginning of the inline file. </dd>
<dt><code>&#8211;cxx-prologue</code> <i>text</i></dt>
<dd> Insert <i>text</i> at the beginning of the source file. </dd>
<dt><code>&#8211;fwd-prologue</code> <i>text</i></dt>
<dd> Insert <i>text</i> at the beginning of the forward declaration file. </dd>
<dt><code>&#8211;prologue</code> <i>text</i></dt>
<dd> Insert <i>text</i> at the beginning of each generated file for which there is no file-specific prologue. </dd>
<dt><code>&#8211;hxx-epilogue</code> <i>text</i></dt>
<dd> Insert <i>text</i> at the end of the header file. </dd>
<dt><code>&#8211;ixx-epilogue</code> <i>text</i></dt>
<dd> Insert <i>text</i> at the end of the inline file. </dd>
<dt><code>&#8211;cxx-epilogue</code> <i>text</i></dt>
<dd> Insert <i>text</i> at the end of the source file. </dd>
<dt><code>&#8211;fwd-epilogue</code> <i>text</i></dt>
<dd> Insert <i>text</i> at the end of the forward declaration file. </dd>
<dt><code>&#8211;epilogue</code> <i>text</i></dt>
<dd> Insert <i>text</i> at the end of each generated file for which there is no file-specific epilogue. </dd>
<dt><code>&#8211;hxx-prologue-file</code> <i>file</i></dt>
<dd> Insert the content of the <i>file</i> at the beginning of the header file. </dd>
<dt><code>&#8211;ixx-prologue-file</code> <i>file</i></dt>
<dd> Insert the content of the <i>file</i> at the beginning of the inline file. </dd>
<dt><code>&#8211;cxx-prologue-file</code> <i>file</i></dt>
<dd> Insert the content of the <i>file</i> at the beginning of the source file. </dd>
<dt><code>&#8211;fwd-prologue-file</code> <i>file</i></dt>
<dd> Insert the content of the <i>file</i> at the beginning of the forward declaration file. </dd>
<dt><code>&#8211;prologue-file</code> <i>file</i></dt>
<dd> Insert the content of the <i>file</i> at the beginning of each generated file for which there is no file-specific prologue file. </dd>
<dt><code>&#8211;hxx-epilogue-file</code> <i>file</i></dt>
<dd> Insert the content of the <i>file</i> at the end of the header file. </dd>
<dt><code>&#8211;ixx-epilogue-file</code> <i>file</i></dt>
<dd> Insert the content of the <i>file</i> at the end of the inline file. </dd>
<dt><code>&#8211;cxx-epilogue-file</code> <i>file</i></dt>
<dd> Insert the content of the <i>file</i> at the end of the source file. </dd>
<dt><code>&#8211;fwd-epilogue-file</code> <i>file</i></dt>
<dd> Insert the content of the <i>file</i> at the end of the forward declaration file. </dd>
<dt><code>&#8211;epilogue-file</code> <i>file</i></dt>
<dd> Insert the content of the <i>file</i> at the end of each generated file for which there is no file-specific epilogue file. </dd>
<dt><code>&#8211;export-symbol</code> <i>symbol</i></dt>
<dd> Insert <i>symbol</i> in places where DLL export/import control statements (<code>__declspec(dllexport/dllimport)</code>) are necessary. </dd>
<dt><code>&#8211;export-xml-schema</code></dt>
<dd> Export/import types in the XML Schema namespace using the export symbol provided with the <code>&#8211;export-symbol</code> option. The <code>XSD_NO_EXPORT</code> macro can be used to omit this code during C++ compilation, which may be useful if you would like to use the same generated code across multiple platforms. </dd>
<dt><code>&#8211;export-maps</code></dt>
<dd> Export polymorphism support maps from a Win32 DLL into which this generated code is placed. This is necessary when your type hierarchy is split across several DLLs since otherwise each DLL will have its own set of maps. In this situation the generated code for the DLL which contains base types and/or substitution group heads should be compiled with this option and the generated code for all other DLLs should be compiled with <code>&#8211;import-maps</code>. This option is only valid together with <code>&#8211;generate-polymorphic</code>. The <code>XSD_NO_EXPORT</code> macro can be used to omit this code during C++ compilation, which may be useful if you would like to use the same generated code across multiple platforms. </dd>
<dt><code>&#8211;import-maps</code></dt>
<dd> Import polymorphism support maps to a Win32 DLL or executable into which this generated code is linked. See the <code>&#8211;export-maps</code> option documentation for details. This options is only valid together with <code>&#8211;generate-polymorphic</code>. The <code>XSD_NO_EXPORT</code> macro can be used to omit this code during C++ compilation, which may be useful if you would like to use the same generated code across multiple platforms. </dd>
<dt><code>&#8211;generate-dep</code></dt>
<dd> Generate <code>make</code> dependency information. This option triggers the creation of the <code>.d</code> file containing the dependencies of the generated files on the main schema file as well as all the schema files that it includes/imports, transitively. This dependency file is then normally included into the main <code>makefile</code> to implement automatic dependency tracking. </dd>
<p> Note also that automatic dependency generation is not supported in the file-per-type mode (<code>&#8211;file-per-type</code>). In this case, all the generated files are produced with a single compiler invocation and depend on all the schemas. As a result, it is easier to establish such a dependency manually, perhaps with the help of the <code>&#8211;file-list*</code> options. </p>
<dt><code>&#8211;generate-dep-only</code></dt>
<dd> Generate <code>make</code> dependency information only. </dd>
<dt><code>&#8211;dep-phony</code></dt>
<dd> Generate phony targets for included/imported schema files, causing each to depend on nothing. Such dummy rules work around <code>make</code> errors caused by the removal of schema files without also updating the dependency file to match. </dd>
<dt><code>&#8211;dep-target</code> <i>target</i></dt>
<dd> Change the target of the dependency rule. By default it contains all the generated C++ files as well as the dependency file itself, without any directory prefixes. If you require multiple targets, then you can specify them as a single, space-separated argument or you can repeat this option multiple times. </dd>
<dt><code>&#8211;dep-suffix</code> <i>suffix</i></dt>
<dd> Use the provided <i>suffix</i> instead of the default <code>.d</code> to construct the name of the dependency file. </dd>
<dt><code>&#8211;dep-regex</code> <i>regex</i></dt>
<dd> Use the provided expression to construct the name of the dependency file. <i>regex</i> is a Perl-like regular expression in the form <code>/</code><i>pattern</i><code>/</code><i>replacement</i><code>/</code>. See also the REGEX AND SHELL QUOTING section below. </dd>
<dt><code>&#8211;disable-warning</code> <i>warn</i></dt>
<dd> Disable printing warning with id <i>warn</i>. If <code>all</code> is specified for the warning id then all warnings are disabled. </dd>
<dt><code>&#8211;options-file</code> <i>file</i></dt>
<dd> Read additional options from <i>file</i>. Each option should appearing on a separate line optionally followed by space and an option value. Empty lines and lines starting with <code>#</code> are ignored. Option values can be enclosed in double (<code>&quot;</code>) or single (<code>&#8216;</code>) quotes to preserve leading and trailing whitespaces as well as to specify empty values. If the value itself contains trailing or leading quotes, enclose it with an extra pair of quotes, for example <code>&#8216;&quot;x&quot;&#8217;</code>. Non-leading and non-trailing quotes are interpreted as being part of the option value. </dd>
<p> The semantics of providing options in a file is equivalent to providing the same set of options in the same order on the command line at the point where the <code>&#8211;options-file</code> option is specified except that the shell escaping and quoting is not required. You can repeat this option to specify more than one options file. </p>
<dt><code>&#8211;show-sloc</code></dt>
<dd> Show the number of generated physical source lines of code (SLOC). </dd>
<dt><code>&#8211;sloc-limit</code> <i>num</i></dt>
<dd> Check that the number of generated physical source lines of code (SLOC) does not exceed <i>num</i>. </dd>
<dt><code>&#8211;proprietary-license</code></dt>
<dd> Indicate that the generated code is licensed under a proprietary license instead of the GPL. </dd>
<dt><code>&#8211;custom-literals</code> <i>file</i></dt>
<dd> Load custom XML string to C++ literal mappings from <i>file</i>. This mechanism can be useful if you are using a custom character encoding and some of the strings in your schemas, for example element/attribute names or enumeration values, contain non-ASCII characters. In this case you will need to provide a custom mapping to C++ literals for such strings. The format of this file is specified in the <code>custom-literals.xsd</code> XML Schema file that can be found in the documentation directory. </dd>
<dt><code>&#8211;preserve-anonymous</code></dt>
<dd> Preserve anonymous types. By default anonymous types are automatically named with names derived from the enclosing elements/attributes. Because mappings implemented by this compiler require all types to be named, this option is only useful if you want to make sure your schemas don&#8217;t have anonymous types. </dd>
<dt><code>&#8211;show-anonymous</code></dt>
<dd> Show elements and attributes that are of anonymous types. This option only makes sense together with the <code>&#8211;preserve-anonymous</code> option. </dd>
<dt><code>&#8211;anonymous-regex</code> <i>regex</i></dt>
<dd> Add <i>regex</i> to the list of regular expressions used to derive names for anonymous types from the enclosing attributes/elements. <i>regex</i> is a Perl-like regular expression in the form <code>/</code><i>pattern</i><code>/</code><i>replacement</i><code>/</code>. Any character can be used as a delimiter instead of <code>/</code>. Escaping of the delimiter character in <i>pattern</i> or <i>replacement</i> is not supported. </dd>
<p> All the regular expressions are pushed into a stack with the last specified expression considered first. The first match that succeeds is used. Regular expressions are applied to a string in the form </p>
<p> <i>filename</i> <i>namespace</i> <i>xpath</i> </p>
<p> For instance: </p>
<p> <code>hello.xsd <a rel="nofollow" href="http://example.com/hello">http://example.com/hello</a> element</code> </p>
<p> <code>hello.xsd <a rel="nofollow" href="http://example.com/hello">http://example.com/hello</a> type/element</code> </p>
<p> As an example, the following expression makes all the derived names start with capital letters. This could be useful when your naming convention requires type names to start with capital letters: </p>
<p> <code>%.* .* (.+/)*(.+)%</code>\u$2%</code> </p>
<p> See also the REGEX AND SHELL QUOTING section below. </p>
<dt><code>--anonymous-regex-trace</code></dt>
<dd> <p> Trace the process of applying regular expressions specified with the <code>--anonymous-regex</code> option. Use this option to find out why your regular expressions don&#8217;t do what you expected them to do. </p>
 </dd>
<dt><code>--location-map</code><i>ol</i>=<i>nl</i></dt>
<dd> <p> Map the original schema location <i>ol</i> that is specified in the XML Schema include or import elements to new schema location <i>nl</i>. Repeat this option to map more than one schema location. For example, the following option maps the <code><a rel="nofollow" href="http://example.com/foo.xsd">http://example.com/foo.xsd</a></code> URL to the <code>foo.xsd</code> local file. </p>
<p> <code>--location-map <a rel="nofollow" href="http://example.com/foo.xsd=foo.xsd">http://example.com/foo.xsd=foo.xsd</a></code> </p>
 </dd>
<dt><code>--location-regex</code><i>regex</i></dt>
<dd> <p> Add <i>regex</i> to the list of regular expressions used to map schema locations that are specified in the XML Schema include or import elements. <i>regex</i> is a Perl-like regular expression in the form <code>/</code><i>pattern</i><code>/</code><i>replacement</i><code>/</code>. Any character can be used as a delimiter instead of <code>/</code>. Escaping of the delimiter character in <i>pattern</i> or <i>replacement</i> is not supported. All the regular expressions are pushed into a stack with the last specified expression considered first. The first match that succeeds is used. </p>
<p> For example, the following expression maps URL locations in the form <code><a rel="nofollow" href="http://example.com/foo/bar.xsd">http://example.com/foo/bar.xsd</a></code> to local files in the form <code>bar.xsd</code>: </p>
<p> <code>%<a rel="nofollow" href="http://.+/(.+)%$1%">http://.+/(.+)%$1%</a></code> </p>
<p> See also the REGEX AND SHELL QUOTING section below. </p>
 </dd>
<dt><code>--location-regex-trace</code></dt>
<dd> <p> Trace the process of applying regular expressions specified with the <code>--location-regex</code> option. Use this option to find out why your regular expressions don&#8217;t do what you expected them to do. </p>
 </dd>
<dt><code>--file-per-type</code></dt>
<dd> <p> Generate a separate set of C++ files for each type defined in XML Schema. Note that in this mode you only need to compile the root schema(s) and the code will be generated for all included and imported schemas. This compilation mode is primarily useful when some of your schemas cannot be compiled separately or have cyclic dependencies which involve type inheritance. Other options related to this mode are: <code>--type-file-regex</code>, <code>--schema-file-regex</code>, <code>--fat-type-file</code>, and <code>--file-list</code>. </p>
 </dd>
<dt><code>--type-file-regex</code><i>regex</i></dt>
<dd> <p> Add <i>regex</i> to the list of regular expressions used to translate type names to file names when the <code>--file-per-type</code> option is specified. <i>regex</i> is a Perl-like regular expression in the form <code>/</code><i>pattern</i><code>/</code><i>replacement</i><code>/</code>. Any character can be used as a delimiter instead of <code>/</code>. Escaping of the delimiter character in <i>pattern</i> or <i>replacement</i> is not supported. All the regular expressions are pushed into a stack with the last specified expression considered first. The first match that succeeds is used. Regular expressions are applied to a string in the form </p>
<p> <i>namespace</i> <i>type-name</i> </p>
<p> For example, the following expression maps type <code>foo</code> that is defined in the <code><a rel="nofollow" href="http://example.com/bar">http://example.com/bar</a></code> namespace to file name <code>bar-foo</code>: </p>
<p> <code>%<a rel="nofollow" href="http://example.com/(.+)">http://example.com/(.+)</a> (.+)%$1-$2%</code> </p>
<p> See also the REGEX AND SHELL QUOTING section below. </p>
 </dd>
<dt><code>--type-file-regex-trace</code></dt>
<dd> <p> Trace the process of applying regular expressions specified with the <code>--type-file-regex</code> option. Use this option to find out why your regular expressions don&#8217;t do what you expected them to do. </p>
 </dd>
<dt><code>--schema-file-regex</code><i>regex</i></dt>
<dd> <p> Add <i>regex</i> to the list of regular expressions used to translate schema file names when the <code>--file-per-type</code> option is specified. <i>regex</i> is a Perl-like regular expression in the form <code>/</code><i>pattern</i><code>/</code><i>replacement</i><code>/</code>. Any character can be used as a delimiter instead of <code>/</code>. Escaping of the delimiter character in <i>pattern</i> or <i>replacement</i> is not supported. All the regular expressions are pushed into a stack with the last specified expression considered first. The first match that succeeds is used. Regular Expressions are applied to the absolute filesystem path of a schema file and the result, including the directory part, if any, is used to derive the <code>#include</code> directive paths as well as the generated C++ file paths. This option, along with <code>--type-file-regex</code> are primarily useful to place the generated files into subdirectories or to resolve file name conflicts. </p>
<p> For example, the following expression maps schema files in the <code>foo/1.0.0/</code> subdirectory to the files in the <code>foo/</code> subdirectory. As a result, the <code>#include</code> directive paths for such schemas will be in the <code>foo/schema.hxx</code> form and the generated C++ files will be placed into the <code>foo/</code> subdirectory: </p>
<p> <code>%.*/foo/1.0.0/(.+)%foo/$1%</code> </p>
<p> See also the REGEX AND SHELL QUOTING section below. </p>
 </dd>
<dt><code>--schema-file-regex-trace</code></dt>
<dd> <p> Trace the process of applying regular expressions specified with the <code>--schema-file-regex</code> option. Use this option to find out why your regular expressions don&#8217;t do what you expected them to do. </p>
 </dd>
<dt><code>--fat-type-file</code></dt>
<dd> <p> Generate code corresponding to global elements into type files instead of schema files when the <code>--type-file-regex</code> option is specified. This option is primarily useful when trying to minimize the amount of object code that is linked to an executable by packaging compiled generated code into a static (archive) library. </p>
 </dd>
<dt><code>--file-list</code><i>file</i></dt>
<dd> <p> Write a list of generated C++ files to <i>file</i>. This option is primarily useful in the file-per-type compilation mode (<code>--file-per-type</code>) to create a list of generated C++ files, for example, as a makefile fragment. </p>
 </dd>
<dt><code>--file-list-prologue</code><i>text</i></dt>
<dd> <p> Insert <i>text</i> at the beginning of the file list. As a convenience, all occurrences of the <code>\n</code> character sequence in <i>text</i> are replaced with new lines. This option can, for example, be used to assign the generated file list to a makefile variable. </p>
 </dd>
<dt><code>--file-list-epilogue</code><i>text</i></dt>
<dd> <p> Insert <i>text</i> at the end of the file list. As a convenience, all occurrences of the <code>\n</code> character sequence in <i>text</i> are replaced with new lines. </p>
 </dd>
<dt><code>--file-list-delim</code><i>text</i></dt>
<dd> <p> Delimit file names written to the file list with <i>text</i> instead of new lines. As a convenience, all occurrences of the <code>\n</code> character sequence in <i>text</i> are replaced with new lines. </p>
 </dd></dl>
<h3>cxx-tree command options</h3>
<dl>
<dt><code>--generate-polymorphic</code></dt>
<dd> <p> Generate polymorphism-aware code. Specify this option if you use substitution groups or <code>xsi:type</code>. Use the <code>--polymorphic-type</code> or <code>--polymorphic-type-all</code> option to specify which type hierarchies are polymorphic. </p>
 </dd>
<dt><code>--polymorphic-type</code><i>type</i></dt>
<dd> <p> Indicate that <i>type</i> is a root of a polymorphic type hierarchy. The compiler can often automatically determine which types are polymorphic based on the substitution group declarations. However, you may need to use this option if you are not using substitution groups or if substitution groups are defined in another schema. You need to specify this option when compiling every schema file that references <i>type</i>. The <i>type</i> argument is an XML Schema type name that can be optionally qualified with a namespace in the <i>namespace</i><code>#</code><i>name</i> form. </p>
 </dd>
<dt><code>--polymorphic-type-all</code></dt>
<dd> <p> Indicate that all types should be treated as polymorphic. </p>
 </dd>
<dt><code>--polymorphic-plate</code><i>num</i></dt>
<dd> <p> Specify the polymorphic map plate the generated code should register on. This functionality is primarily useful to segregate multiple schemas that define the same polymorphic types. </p>
 </dd>
<dt><code>--ordered-type</code><i>type</i></dt>
<dd> <p> Indicate that element order in <i>type</i> is significant. An example would be a complex type with unbounded choice as a content model where the element order in XML has application-specific semantics. For ordered types the compiler generates a special container data member and a corresponding set of accessors and modifiers that are used to capture the order of elements and, for mixed content, of text. </p>
<p> The <i>type</i> argument is an XML Schema type name that can be optionally qualified with a namespace in the <i>namespace</i><code>#</code><i>name</i> form. Note also that you will need to specify this option when compiling every schema file that has other ordered types derived from this type. </p>
 </dd>
<dt><code>--ordered-type-derived</code></dt>
<dd> <p> Automatically treat types derived from ordered bases as also ordered. This is primarily useful if you would like to be able to iterate over the complete content using the content order container. </p>
 </dd>
<dt><code>--ordered-type-mixed</code></dt>
<dd> <p> Automatically treat complex types with mixed content as ordered. </p>
 </dd>
<dt><code>--ordered-type-all</code></dt>
<dd> <p> Indicate that element order in all types is significant. </p>
 </dd>
<dt><code>--order-container</code><i>type</i></dt>
<dd> <p> Specify a custom class template that should be used as a container for the content order in ordered types instead of the default <code>std::vector</code>. See <code>--ordered-type</code> for more information on ordered type. This option is primarily useful if you need to perform more complex lookups in the content order container, for example by element id. In this case, a container like Boost multi-index may be more convenient. Note that if using a custom container, you will also most likely need to include the relevant headers using the <code>--hxx-prologue*</code> options. </p>
 </dd>
<dt><code>--generate-serialization</code></dt>
<dd> <p> Generate serialization functions. Serialization functions convert the object model back to XML. </p>
 </dd>
<dt><code>--generate-ostream</code></dt>
<dd> <p> Generate ostream insertion operators (<code>operator&lt;&lt;</code>) for generated types. This allows one to easily print a fragment or the whole object model for debugging or logging. </p>
 </dd>
<dt><code>--generate-doxygen</code></dt>
<dd> <p> Generate documentation comments suitable for extraction by the Doxygen documentation system. Documentation from annotations is added to the comments if present in the schema. </p>
 </dd>
<dt><code>--generate-comparison</code></dt>
<dd> <p> Generate comparison operators (<code>operator==</code> and <code>operator!=</code>) for complex types. Comparison is performed member-wise. </p>
 </dd>
<dt><code>--generate-default-ctor</code></dt>
<dd> <p> Generate default constructors even for types that have required members. Required members of an instance constructed using such a constructor are not initialized and accessing them results in undefined behavior. </p>
 </dd>
<dt><code>--generate-from-base-ctor</code></dt>
<dd> <p> Generate constructors that expect an instance of a base type followed by all required members. </p>
 </dd>
<dt><code>--suppress-assignment</code></dt>
<dd> <p> Suppress the generation of copy assignment operators for complex types. If this option is specified, the copy assignment operators for such types are declared private and left unimplemented. </p>
 </dd>
<dt><code>--generate-detach</code></dt>
<dd> <p> Generate detach functions for required elements and attributes. Detach functions for optional and sequence cardinalities are provided by the respective containers. These functions, for example, allow you to move sub-trees in the object model either within the same tree or between different trees. </p>
 </dd>
<dt><code>--generate-wildcard</code></dt>
<dd> <p> Generate accessors and modifiers as well as parsing and serialization code for XML Schema wildcards (<code>any</code> and <code>anyAttribute</code>). XML content matched by wildcards is presented as DOM fragments. Note that you need to initialize the Xerces-C++ runtime if you are using this option. </p>
 </dd>
<dt><code>--generate-any-type</code></dt>
<dd> <p> Extract and store content of the XML Schema <code>anyType</code> type as a DOM fragment. Note that you need to initialize the Xerces-C++ runtime if you are using this option. </p>
 </dd>
<dt><code>--generate-insertion</code><i>os</i></dt>
<dd> <p> Generate data representation stream insertion operators for the <i>os</i> output stream type. Repeat this option to specify more than one stream type. The ACE CDR stream (<code>ACE_OutputCDR</code>) and RPC XDR are recognized by the compiler and the necessary <code>#include</code> directives are automatically generated. For custom stream types use the <code>--hxx-prologue*</code> options to provide the necessary declarations. </p>
 </dd>
<dt><code>--generate-extraction</code><i>is</i></dt>
<dd> <p> Generate data representation stream extraction constructors for the <i>is</i> input stream type. Repeat this option to specify more than one stream type. The ACE CDR stream (<code>ACE_InputCDR</code>) and RPC XDR are recognized by the compiler and the necessary <code>#include</code> directives are automatically generated. For custom stream types use the <code>--hxx-prologue*</code> options to provide the necessary declarations. </p>
 </dd>
<dt><code>--generate-forward</code></dt>
<dd> <p> Generate a separate header file with forward declarations for the types being generated. </p>
 </dd>
<dt><code>--suppress-parsing</code></dt>
<dd> <p> Suppress the generation of the parsing functions and constructors. Use this option to reduce the generated code size when parsing from XML is not needed. </p>
 </dd>
<dt><code>--generate-element-type</code></dt>
<dd> <p> Generate types instead of parsing and serialization functions for root elements. This is primarily useful to distinguish object models with the same root type but with different root elements. </p>
 </dd>
<dt><code>--generate-element-map</code></dt>
<dd> <p> Generate a root element map that allows uniform parsing and serialization of multiple root elements. This option is only valid together with <code>--generate-element-type</code>. </p>
 </dd>
<dt><code>--generate-intellisense</code></dt>
<dd> <p> Generate workarounds for IntelliSense bugs in Visual Studio 2005 (8.0). When this option is used, the resulting code is slightly more verbose. IntelliSense in Visual Studio 2008 (9.0) and later does not require these workarounds. Support for IntelliSense in Visual Studio 2003 (7.1) is improved with this option but is still incomplete. </p>
 </dd>
<dt><code>--omit-default-attributes</code></dt>
<dd> <p> Omit attributes with default and fixed values from serialized XML documents. </p>
 </dd>
<dt><code>--type-naming</code><i>style</i></dt>
<dd> <p> Specify the type naming convention that should be used in the generated code. Valid styles are <code>knr</code> (default), <code>ucc</code>, and <code>java</code>. See the NAMING CONVENTION section below for more information. </p>
 </dd>
<dt><code>--function-naming</code><i>style</i></dt>
<dd> <p> Specify the function naming convention that should be used in the generated code. Valid styles are <code>knr</code> (default), <code>lcc</code>, and <code>java</code>. See the NAMING CONVENTION section below for more information. </p>
 </dd>
<dt><code>--type-regex</code><i>regex</i></dt>
<dd> <p> Add <i>regex</i> to the list of regular expressions used to translate XML Schema type names to C++ type names. See the NAMING CONVENTION section below for more information. </p>
 </dd>
<dt><code>--accessor-regex</code><i>regex</i></dt>
<dd> <p> Add <i>regex</i> to the list of regular expressions used to translate XML Schema names of elements/attributes to C++ accessor function names. See the NAMING CONVENTION section below for more information. </p>
 </dd>
<dt><code>--one-accessor-regex</code><i>regex</i></dt>
<dd> <p> Add <i>regex</i> to the list of regular expressions used to translate XML Schema names of elements/attributes with cardinality one to C++ accessor function names. See the NAMING CONVENTION section below for more information. </p>
 </dd>
<dt><code>--opt-accessor-regex</code><i>regex</i></dt>
<dd> <p> Add <i>regex</i> to the list of regular expressions used to translate XML Schema names of elements/attributes with cardinality optional to C++ accessor function names. See the NAMING CONVENTION section below for more information. </p>
 </dd>
<dt><code>--seq-accessor-regex</code><i>regex</i></dt>
<dd> <p> Add <i>regex</i> to the list of regular expressions used to translate XML Schema names of elements/attributes with cardinality sequence to C++ accessor function names. See the NAMING CONVENTION section below for more information. </p>
 </dd>
<dt><code>--modifier-regex</code><i>regex</i></dt>
<dd> <p> Add <i>regex</i> to the list of regular expressions used to translate XML Schema names of elements/attributes to C++ modifier function names. See the NAMING CONVENTION section below for more information. </p>
 </dd>
<dt><code>--one-modifier-regex</code><i>regex</i></dt>
<dd> <p> Add <i>regex</i> to the list of regular expressions used to translate XML Schema names of elements/attributes with cardinality one to C++ modifier function names. See the NAMING CONVENTION section below for more information. </p>
 </dd>
<dt><code>--opt-modifier-regex</code><i>regex</i></dt>
<dd> <p> Add <i>regex</i> to the list of regular expressions used to translate XML Schema names of elements/attributes with cardinality optional to C++ modifier function names. See the NAMING CONVENTION section below for more information. </p>
 </dd>
<dt><code>--seq-modifier-regex</code><i>regex</i></dt>
<dd> <p> Add <i>regex</i> to the list of regular expressions used to translate XML Schema names of elements/attributes with cardinality sequence to C++ modifier function names. See the NAMING CONVENTION section below for more information. </p>
 </dd>
<dt><code>--parser-regex</code><i>regex</i></dt>
<dd> <p> Add <i>regex</i> to the list of regular expressions used to translate XML Schema element names to C++ parsing function names. See the NAMING CONVENTION section below for more information. </p>
 </dd>
<dt><code>--serializer-regex</code><i>regex</i></dt>
<dd> <p> Add <i>regex</i> to the list of regular expressions used to translate XML Schema element names to C++ serialization function names. See the NAMING CONVENTION section below for more information. </p>
 </dd>
<dt><code>--const-regex</code><i>regex</i></dt>
<dd> <p> Add <i>regex</i> to the list of regular expressions used to translate XML Schema-derived names to C++ constant names. See the NAMING CONVENTION section below for more information. </p>
 </dd>
<dt><code>--enumerator-regex</code><i>regex</i></dt>
<dd> <p> Add <i>regex</i> to the list of regular expressions used to translate XML Schema enumeration values to C++ enumerator names. See the NAMING CONVENTION section below for more information. </p>
 </dd>
<dt><code>--element-type-regex</code><i>regex</i></dt>
<dd> <p> Add <i>regex</i> to the list of regular expressions used to translate XML Schema element names to C++ element type names. See the NAMING CONVENTION section below for more information. </p>
 </dd>
<dt><code>--name-regex-trace</code></dt>
<dd> <p> Trace the process of applying regular expressions specified with the name transformation options. Use this option to find out why your regular expressions don&#8217;t do what you expected them to do. </p>
 </dd>
<dt><code>--root-element-first</code></dt>
<dd> <p> Treat only the first global element as a document root. By default all global elements are considered document roots. </p>
 </dd>
<dt><code>--root-element-last</code></dt>
<dd> <p> Treat only the last global element as a document root. By default all global elements are considered document roots. </p>
 </dd>
<dt><code>--root-element-all</code></dt>
<dd> <p> Treat all global elements as document roots. This is the default behavior. By explicitly specifying this option you can suppress the warning that is issued if more than one global element is defined. </p>
 </dd>
<dt><code>--root-element-none</code></dt>
<dd> <p> Do not treat any global elements as document roots. By default all global elements are considered document roots. </p>
 </dd>
<dt><code>--root-element</code><i>element</i></dt>
<dd> <p> Treat only <i>element</i> as a document root. Repeat this option to specify more than one root element. </p>
 </dd>
<dt><code>--custom-type</code><i>map</i></dt>
<dd> <p> Use a custom C++ type instead of the generated class. The <i>map</i> argument is in the form <i>name</i>[<code>=</code><i>type</i>[<code>/</code><i>base</i>]], where <i>name</i> is a type name as defined in XML Schema and <i>type</i> is a C++ type name that should be used instead. If <i>type</i> is not present or empty then the custom type is assumed to have the same name and be defined in the same namespace as the generated class would have. If <i>base</i> is specified then the generated class is still generated but with that name. </p>
 </dd>
<dt><code>--custom-type-regex</code><i>regex</i></dt>
<dd> <p> Use custom C++ types instead of the generated classes. The <i>regex</i> argument is in the form <code>/</code><i>name-pat</i><code>/</code>[<i>type-sub</i><code>/</code>[<i>base-sub</i><code>/</code>]], where <i>name-pat</i> is a regex pattern that will be matched against type names as defined in XML Schema and <i>type-sub</i> is a C++ type name substitution that should be used instead. If <i>type-sub</i> is not present or its substitution results in an empty string then the custom type is assumed to have the same name and be defined in the same namespace as the generated class would have. If <i>base-sub</i> is present and its substitution results in a non-empty string then the generated class is still generated but with the result of this substitution as its name. The pattern and substitutions are in the Perl regular expression format. See also the REGEX AND SHELL QUOTING section below. </p>
 </dd>
<dt><code>--parts</code><i>num</i></dt>
<dd> <p> Split generated source code into <i>num</i> parts. This is useful when translating large, monolithic schemas and a C++ compiler is not able to compile the resulting source code at once (usually due to insufficient memory). </p>
 </dd>
<dt><code>--parts-suffix</code><i>suffix</i></dt>
<dd> <p> Use <i>suffix</i> instead of the default &#8216;<code>-</code>&#8216; to separate the file name from the part number. </p>
 </dd></dl>
<h3>cxx-parser command options</h3>
<dl>
<dt><code>--type-map</code><i>mapfile</i></dt>
<dd> <p> Read XML Schema to C++ type mapping information from <i>mapfile</i>. Repeat this option to specify several type maps. Type maps are considered in order of appearance and the first match is used. By default all user-defined types are mapped to <code>void</code>. See the TYPE MAP section below for more information. </p>
 </dd>
<dt><code>--xml-parser</code><i>parser</i></dt>
<dd> <p> Use <i>parser</i> as the underlying XML parser. Valid values are <code>xerces</code> for Xerces-C++ (default) and <code>expat</code> for Expat. </p>
 </dd>
<dt><code>--generate-validation</code></dt>
<dd> <p> Generate validation code. The validation code (&quot;perfect parser&quot;) ensures that instance documents conform to the schema. Validation code is generated by default when the selected underlying XML parser is non-validating (<code>expat</code>). </p>
 </dd>
<dt><code>--suppress-validation</code></dt>
<dd> <p> Suppress the generation of validation code. Validation is suppressed by default when the selected underlying XML parser is validating (<code>xerces</code>). </p>
 </dd>
<dt><code>--generate-polymorphic</code></dt>
<dd> <p> Generate polymorphism-aware code. Specify this option if you use substitution groups or <code>xsi:type</code>. </p>
 </dd>
<dt><code>--generate-noop-impl</code></dt>
<dd> <p> Generate a sample parser implementation that does nothing (no operation). The sample implementation can then be filled with the application-specific code. For an input file in the form <code>name.xsd</code> this option triggers the generation of two additional C++ files in the form: <code>name-pimpl.hxx</code> (parser implementation header file) and <code>name-pimpl.cxx</code> (parser implementation source file). </p>
 </dd>
<dt><code>--generate-print-impl</code></dt>
<dd> <p> Generate a sample parser implementation that prints the XML data to STDOUT. For an input file in the form <code>name.xsd</code> this option triggers the generation of two additional C++ files in the form: <code>name-pimpl.hxx</code> (parser implementation header file) and <code>name-pimpl.cxx</code> (parser implementation source file). </p>
 </dd>
<dt><code>--generate-test-driver</code></dt>
<dd> <p> Generate a test driver for the sample parser implementation. For an input file in the form <code>name.xsd</code> this option triggers the generation of an additional C++ file in the form <code>name-driver.cxx</code>. </p>
 </dd>
<dt><code>--force-overwrite</code></dt>
<dd> <p> Force overwriting of the existing implementation and test driver files. Use this option only if you do not mind loosing the changes you have made in the sample implementation or test driver files. </p>
 </dd>
<dt><code>--root-element-first</code></dt>
<dd> <p> Indicate that the first global element is the document root. This information is used to generate the test driver for the sample implementation. </p>
 </dd>
<dt><code>--root-element-last</code></dt>
<dd> <p> Indicate that the last global element is the document root. This information is used to generate the test driver for the sample implementation. </p>
 </dd>
<dt><code>--root-element</code><i>element</i></dt>
<dd> <p> Indicate that <i>element</i> is the document root. This information is used to generate the test driver for the sample implementation. </p>
 </dd>
<dt><code>--skel-type-suffix</code><i>suffix</i></dt>
<dd> <p> Use the provided <i>suffix</i> instead of the default <code>_pskel</code> to construct the names of the generated parser skeletons. </p>
 </dd>
<dt><code>--skel-file-suffix</code><i>suffix</i></dt>
<dd> <p> Use the provided <i>suffix</i> instead of the default <code>-pskel</code> to construct the names of the generated parser skeleton files. </p>
 </dd>
<dt><code>--impl-type-suffix</code><i>suffix</i></dt>
<dd> <p> Use the provided <i>suffix</i> instead of the default <code>_pimpl</code> to construct the names of the parser implementations for the built-in XML Schema types as well as sample parser implementations. </p>
 </dd>
<dt><code>--impl-file-suffix</code><i>suffix</i></dt>
<dd> <p> Use the provided <i>suffix</i> instead of the default <code>-pimpl</code> to construct the names of the generated sample parser implementation files. </p>
 </dd></dl>
<h2>NAMING CONVENTION</h2>
<p> The compiler can be instructed to use a particular naming convention in the generated code. A number of widely-used conventions can be selected using the <code>--type-naming</code> and <code>--function-naming</code> options. A custom naming convention can be achieved using the <code>--type-regex</code>, <code>--accessor-regex</code>, <code>--one-accessor-regex</code>, <code>--opt-accessor-regex</code>, <code>--seq-accessor-regex</code>, <code>--modifier-regex</code>, <code>--one-modifier-regex</code>, <code>--opt-modifier-regex</code>, <code>--seq-modifier-regex</code>, <code>--parser-regex</code>, <code>--serializer-regex</code>, <code>--const-regex</code>, <code>--enumerator-regex</code>, and <code>--element-type-regex</code> options. </p>
<p> The <code>--type-naming</code> option specifies the convention that should be used for naming C++ types. Possible values for this option are <code>knr</code> (default), <code>ucc</code>, and <code>java</code>. The <code>knr</code> value (stands for K&amp;R) signifies the standard, lower-case naming convention with the underscore used as a word delimiter, for example: foo, foo_bar. The <code>ucc</code> (stands for upper-camel-case) and <code>java</code> values a synonyms for the same naming convention where the first letter of each word in the name is capitalized, for example: Foo, FooBar. </p>
<p> Similarly, the <code>--function-naming</code> option specifies the convention that should be used for naming C++ functions. Possible values for this option are <code>knr</code> (default), <code>lcc</code>, and <code>java</code>. The <code>knr</code> value (stands for K&amp;R) signifies the standard, lower-case naming convention with the underscore used as a word delimiter, for example: foo(), foo_bar(). The <code>lcc</code> value (stands for lower-camel-case) signifies a naming convention where the first letter of each word except the first is capitalized, for example: foo(), fooBar(). The <code>java</code> naming convention is similar to the lower-camel-case one except that accessor functions are prefixed with get, modifier functions are prefixed with set, parsing functions are prefixed with parse, and serialization functions are prefixed with serialize, for example: getFoo(), setFooBar(), parseRoot(), serializeRoot(). </p>
<p> Note that the naming conventions specified with the <code>--type-naming</code> and <code>--function-naming</code> options perform only limited transformations on the names that come from the schema in the form of type, attribute, and element names. In other words, to get consistent results, your schemas should follow a similar naming convention as the one you would like to have in the generated code. Alternatively, you can use the <code>--*-regex</code> options (discussed below) to perform further transformations on the names that come from the schema. </p>
<p> The <code>--type-regex</code>, <code>--accessor-regex</code>, <code>--one-accessor-regex</code>, <code>--opt-accessor-regex</code>, <code>--seq-accessor-regex</code>, <code>--modifier-regex</code>, <code>--one-modifier-regex</code>, <code>--opt-modifier-regex</code>, <code>--seq-modifier-regex</code>, <code>--parser-regex</code>, <code>--serializer-regex</code>, <code>--const-regex</code>, <code>--enumerator-regex</code>, and <code>--element-type-regex</code> options allow you to specify extra regular expressions for each name category in addition to the predefined set that is added depending on the <code>--type-naming</code> and <code>--function-naming</code> options. Expressions that are provided with the <code>--*-regex</code> options are evaluated prior to any predefined expressions. This allows you to selectively override some or all of the predefined transformations. When debugging your own expressions, it is often useful to see which expressions match which names. The <code>--name-regex-trace</code> option allows you to trace the process of applying regular expressions to names. </p>
<p> The value for the <code>--*-regex</code> options should be a perl-like regular expression in the form <code>/</code><i>pattern</i><code>/</code><i>replacement</i><code>/</code>. Any character can be used as a delimiter instead of <code>/</code>. Escaping of the delimiter character in <i>pattern</i> or <i>replacement</i> is not supported. All the regular expressions for each category are pushed into a category-specific stack with the last specified expression considered first. The first match that succeeds is used. For the <code>--one-accessor-regex</code> (accessors with cardinality one), <code>--opt-accessor-regex</code> (accessors with cardinality optional), and <code>--seq-accessor-regex</code> (accessors with cardinality sequence) categories the <code>--accessor-regex</code> expressions are used as a fallback. For the <code>--one-modifier-regex</code>, <code>--opt-modifier-regex</code>, and <code>--seq-modifier-regex</code> categories the <code>--modifier-regex</code> expressions are used as a fallback. For the <code>--element-type-regex</code> category the <code>--type-regex</code> expressions are used as a fallback. </p>
<p> The type name expressions (<code>--type-regex</code>) are evaluated on the name string that has the following format: </p>
<p> [<i>namespace </i>]<i>name</i>[<code>,</code><i>name</i>][<code>,</code><i>name</i>][<code>,</code><i>name</i>] </p>
<p> The element type name expressions (<code>--element-type-regex</code>), effective only when the <code>--generate-element-type</code> option is specified, are evaluated on the name string that has the following format: </p>
<p> <i>namespace name</i> </p>
<p> In the type name format the <i>namespace</i> part followed by a space is only present for global type names. For global types and elements defined in schemas without a target namespace, the <i>namespace</i> part is empty but the space is still present. In the type name format after the initial <i>name</i> component, up to three additional <i>name</i> components can be present, separated by commas. For example: </p>
<p> <code><a rel="nofollow" href="http://example.com/hello">http://example.com/hello</a> type</code> </p>
<p> <code>foo</code> </p>
<p> <code>foo,iterator</code> </p>
<p> <code>foo,const,iterator</code> </p>
<p> The following set of predefined regular expressions is used to transform type names when the upper-camel-case naming convention is selected: </p>
<p> <code>/(?:[^ ]* )?([^,]+)/\\u$1/</code> </p>
<p> <code>/(?:[^ ]* )?([^,]+),([^,]+)/\\u$1\\u$2/</code> </p>
<p> <code>/(?:[^ ]* )?([^,]+),([^,]+),([^,]+)/\\u$1\\u$2\\u$3/</code> </p>
<p> <code>/(?:[^ ]* )?([^,]+),([^,]+),([^,]+),([^,]+)/\\u$1\\u$2\\u$3\\u$4/</code> </p>
<p> The accessor and modifier expressions (<code>--*accessor-regex</code> and <code>--*modifier-regex</code>) are evaluated on the name string that has the following format: </p>
<p> <i>name</i>[<code>,</code><i>name</i>][<code>,</code><i>name</i>] </p>
<p> After the initial <i>name</i> component, up to two additional <i>name</i> components can be present, separated by commas. For example: </p>
<p> <code>foo</code> </p>
<p> <code>dom,document</code> </p>
<p> <code>foo,default,value</code> </p>
<p> The following set of predefined regular expressions is used to transform accessor names when the <code>java</code> naming convention is selected: </p>
<p> <code>/([^,]+)/get\\u$1/</code> </p>
<p> <code>/([^,]+),([^,]+)/get\\u$1\\u$2/</code> </p>
<p> <code>/([^,]+),([^,]+),([^,]+)/get\\u$1\\u$2\\u$3/</code> </p>
<p> For the parser, serializer, and enumerator categories, the corresponding regular expressions are evaluated on local names of elements and on enumeration values, respectively. For example, the following predefined regular expression is used to transform parsing function names when the <code>java</code> naming convention is selected: </p>
<p> <code>/(.+)/parse\\u$1/</code> </p>
<p> The const category is used to create C++ constant names for the element/wildcard/text content ids in ordered types. </p>
<p> See also the REGEX AND SHELL QUOTING section below. </p>
<h2>TYPE MAP</h2>
<p> Type map files are used in C++/Parser to define a mapping between XML Schema and C++ types. The compiler uses this information to determine the return types of <code>post_*</code> functions in parser skeletons corresponding to XML Schema types as well as argument types for callbacks corresponding to elements and attributes of these types. </p>
<p> The compiler has a set of predefined mapping rules that map built-in XML Schema types to suitable C++ types (discussed below) and all other types to <code>void</code>. By providing your own type maps you can override these predefined rules. The format of the type map file is presented below: </p>
<dl>
<dd> <p> <code>namespace</code> <i>schema-namespace</i> [ <i>cxx-namespace</i> ] <br/>
 <code>{</code> <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>( <code>include</code> <i>file-name</i><code>;</code> )* <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>([ <code>type</code> ] <i>schema-type cxx-ret-type</i> [ <i>cxx-arg-type</i> ]<code>;</code> )* <br/>
 <code>}</code> <br/>
 </p>
 </dd></dl>
<p> Both <i>schema-namespace</i> and <i>schema-type</i> are regex patterns while <i>cxx-namespace</i>, <i>cxx-ret-type</i>, and <i>cxx-arg-type</i> are regex pattern substitutions. All names can be optionally enclosed in &quot; &quot;, for example, to include white-spaces. </p>
<p> <i>schema-namespace</i> determines XML Schema namespace. Optional <i>cxx-namespace</i> is prefixed to every C++ type name in this namespace declaration. <i>cxx-ret-type</i> is a C++ type name that is used as a return type for the <code>post_*</code> functions. Optional <i>cxx-arg-type</i> is an argument type for callback functions corresponding to elements and attributes of this type. If <i>cxx-arg-type</i> is not specified, it defaults to <i>cxx-ret-type</i> if <i>cxx-ret-type</i> ends with <code>*</code> or <code>&amp;</code> (that is, it is a pointer or a reference) and <code>const</code> <i>cxx-ret-type</i><code>&amp;</code> otherwise. <i>file-name</i> is a file name either in the &quot; &quot; or &lt; &gt; format and is added with the <code>#include</code> directive to the generated code. </p>
<p> The <code>#</code> character starts a comment that ends with a new line or end of file. To specify a name that contains <code>#</code> enclose it in &quot; &quot;. For example: </p>
<dl>
<dd> <p> namespace <a rel="nofollow" href="http://www.example.com/xmlns/my">http://www.example.com/xmlns/my</a> my <br/>
 { <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>include&nbsp;<wbr>&quot;my.hxx&quot;; <br/>
 </p>
<p> <br/>
&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>Pass apples by value. <br/>
&nbsp;<wbr>&nbsp;<wbr># <br/>
&nbsp;<wbr>&nbsp;<wbr>apple apple; <br/>
 </p>
<p> <br/>
&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>Pass oranges as pointers. <br/>
&nbsp;<wbr>&nbsp;<wbr># <br/>
&nbsp;<wbr>&nbsp;<wbr>orange orange_t*; <br/>
 } <br/>
 </p>
 </dd></dl>
<p> In the example above, for the <code><a rel="nofollow" href="http://www.example.com/xmlns/my#orange">http://www.example.com/xmlns/my#orange</a></code> XML Schema type, the <code>my::orange_t*</code> C++ type will be used as both return and argument types. </p>
<p> Several namespace declarations can be specified in a single file. The namespace declaration can also be completely omitted to map types in a schema without a namespace. For instance: </p>
<dl>
<dd> <p> include &quot;my.hxx&quot;; <br/>
 apple apple; <br/>
 </p>
<p> namespace <a rel="nofollow" href="http://www.example.com/xmlns/my">http://www.example.com/xmlns/my</a> <br/>
 { <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>orange&nbsp;<wbr>&quot;const orange_t*&quot;; <br/>
 } <br/>
 </p>
 </dd></dl>
<p> The compiler has a number of predefined mapping rules that can be presented as the following map files. The string-based XML Schema built-in types are mapped to either <code>std::string</code> or <code>std::wstring</code> depending on the character type selected with the <code>--char-type</code> option (<code>char</code> by default). </p>
<dl>
<dd> <p> namespace <a rel="nofollow" href="http://www.w3.org/2001/XMLSchema">http://www.w3.org/2001/XMLSchema</a> <br/>
 { <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>boolean bool bool; <br/>
 </p>
<p> <br/>
&nbsp;<wbr>&nbsp;<wbr>byte&nbsp;<wbr>&quot;signed char&quot;&nbsp;<wbr>&quot;signed char&quot;; <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>unsignedByte&nbsp;<wbr>&quot;unsigned char&quot;&nbsp;<wbr>&quot;unsigned char&quot;; <br/>
 </p>
<p> <br/>
&nbsp;<wbr>&nbsp;<wbr>short short short; <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>unsignedShort&nbsp;<wbr>&quot;unsigned short&quot;&nbsp;<wbr>&quot;unsigned short&quot;; <br/>
 </p>
<p> <br/>
&nbsp;<wbr>&nbsp;<wbr>int int int; <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>unsignedInt&nbsp;<wbr>&quot;unsigned int&quot;&nbsp;<wbr>&quot;unsigned int&quot;; <br/>
 </p>
<p> <br/>
&nbsp;<wbr>&nbsp;<wbr>long&nbsp;<wbr>&quot;long long&quot;&nbsp;<wbr>&quot;long long&quot;; <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>unsignedLong&nbsp;<wbr>&quot;unsigned long long&quot;&nbsp;<wbr>&quot;unsigned long long&quot;; <br/>
 </p>
<p> <br/>
&nbsp;<wbr>&nbsp;<wbr>integer&nbsp;<wbr>&quot;long long&quot;&nbsp;<wbr>&quot;long long&quot;; <br/>
 </p>
<p> <br/>
&nbsp;<wbr>&nbsp;<wbr>negativeInteger&nbsp;<wbr>&quot;long long&quot;&nbsp;<wbr>&quot;long long&quot;; <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>nonPositiveInteger&nbsp;<wbr>&quot;long long&quot;&nbsp;<wbr>&quot;long long&quot;; <br/>
 </p>
<p> <br/>
&nbsp;<wbr>&nbsp;<wbr>positiveInteger&nbsp;<wbr>&quot;unsigned long long&quot;&nbsp;<wbr>&quot;unsigned long long&quot;; <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>nonNegativeInteger&nbsp;<wbr>&quot;unsigned long long&quot;&nbsp;<wbr>&quot;unsigned long long&quot;; <br/>
 </p>
<p> <br/>
&nbsp;<wbr>&nbsp;<wbr>float float float; <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>double double double; <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>decimal double double; <br/>
 </p>
<p> <br/>
&nbsp;<wbr>&nbsp;<wbr>string std::string; <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>normalizedString std::string; <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>token std::string; <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>Name std::string; <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>NMTOKEN std::string; <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>NCName std::string; <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>ID std::string; <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>IDREF std::string; <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>language std::string; <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>anyURI std::string; <br/>
 </p>
<p> <br/>
&nbsp;<wbr>&nbsp;<wbr>NMTOKENS xml_schema::string_sequence; <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>IDREFS xml_schema::string_sequence; <br/>
 </p>
<p> <br/>
&nbsp;<wbr>&nbsp;<wbr>QName xml_schema::qname; <br/>
 </p>
<p> <br/>
&nbsp;<wbr>&nbsp;<wbr>base64Binary std::auto_ptr&lt;xml_schema::buffer&gt; <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>std::auto_ptr&lt;xml_schema::buffer&gt;; <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>hexBinary std::auto_ptr&lt;xml_schema::buffer&gt; <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>std::auto_ptr&lt;xml_schema::buffer&gt;; <br/>
 </p>
<p> <br/>
&nbsp;<wbr>&nbsp;<wbr>date xml_schema::date; <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>dateTime xml_schema::date_time; <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>duration xml_schema::duration; <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>gDay xml_schema::gday; <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>gMonth xml_schema::gmonth; <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>gMonthDay xml_schema::gmonth_day; <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>gYear xml_schema::gyear; <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>gYearMonth xml_schema::gyear_month; <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>time xml_schema::time; <br/>
 } <br/>
 </p>
 </dd></dl>
<p> The last predefined rule maps anything that wasn&#8217;t mapped by previous rules to <code>void</code>: </p>
<dl>
<dd> <p> namespace .* <br/>
 { <br/>
 <br/>
&nbsp;<wbr>&nbsp;<wbr>.*&nbsp;<wbr>void void; <br/>
 } <br/>
 </p>
 </dd></dl>
<p> When you provide your own type maps with the <code>--type-map</code> option, they are evaluated first. This allows you to selectively override predefined rules. </p>
<h2>REGEX AND SHELL QUOTING</h2>
<p> When entering a regular expression argument in the shell command line it is often necessary to use quoting (enclosing the argument in &quot; &quot; or &#8216; &#8216;) in order to prevent the shell from interpreting certain characters, for example, spaces as argument separators and $ as variable expansions. </p>
<p> Unfortunately it is hard to achieve this in a manner that is portable across POSIX shells, such as those found on GNU/Linux and UNIX, and Windows shell. For example, if you use &quot; &quot; for quoting you will get a wrong result with POSIX shells if your expression contains $. The standard way of dealing with this on POSIX systems is to use &#8216; &#8216; instead. Unfortunately, Windows shell does not remove &#8216; &#8216; from arguments when they are passed to applications. As a result you may have to use &#8216; &#8216; for POSIX and &quot; &quot; for Windows ($ is not treated as a special character on Windows). </p>
<p> Alternatively, you can save regular expression options into a file, one option per line, and use this file with the <code>--options-file</code> option. With this approach you don&#8217;t need to worry about shell quoting. </p>
<h2>DIAGNOSTICS</h2>
<p> If the input file is not a valid W3C XML Schema definition, <code>xsdcxx</code> will issue diagnostic messages to <code>STDERR</code> and exit with non-zero exit code.  </p>
<h2>BUGS</h2>
<p> Send bug reports to the xsd-users [at] codesynthesis.com mailing list.  </p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 2005-2014 Code Synthesis Tools CC. </p>
<p> Permission is granted to copy, distribute and/or modify this document under the terms of the GNU Free Documentation License, version 1.2; with no Invariant Sections, no Front-Cover Texts and no Back-Cover Texts. Copy of the license can be obtained from <a rel="nofollow" href="http://codesynthesis.com/licenses/fdl-1.2.txt">http://codesynthesis.com/licenses/fdl-1.2.txt</a> </p>
