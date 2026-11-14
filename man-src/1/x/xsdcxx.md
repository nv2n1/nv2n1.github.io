---
title: "xsdcxx(1)"
name: "xsdcxx"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xsdcxx/"
description: "xsdcxx – W3C XML Schema to C++ Compiler"
---

<h2>NAME</h2>
<p> xsdcxx &#8211; W3C XML Schema to C++ Compiler</p>
<h2>SYNOPSIS</h2>
<p> <code>xsdcxx</code> <i>command</i> <code>[</code> <i>options</i> <code>]</code> <i>file</i> <code>[</code> <i>file</i> <code>&#8230;]</code> <code>xsdcxx help</code> <code>[</code> <i>command</i> <code>]</code> <code>xsdcxx version</code></p>
<h2>DESCRIPTION</h2>
<p> <code>xsdcxx</code> generates vocabulary-specific, statically-typed C++ mapping from W3C XML Schema definitions. Particular mapping to produce is selected by a <i>command</i>. Each mapping has a number of mapping-specific <i>options</i> that should appear, if any, after the <i>command</i>. Input files should be W3C XML Schema definitions. The exact set of the generated files depends on the selected mapping and options.</p>
<h2>COMMANDS</h2>
<dl>
<dt><code>cxx-tree</code></p>
<dd> Generate the C++/Tree mapping. For each input file in the form <code>name.xsd</code> the following C++ files are generated: <code>name.hxx</code> (header file), <code>name.ixx</code> (inline file, generated only if the <code>&#8211;generate-inline</code> option is specified), <code>name.cxx</code> (source file), and <code>name-fwd.hxx</code> (forward declaration file, generated only if the <code>&#8211;generate-forward</code> option is specified). </p>
<dt><code>cxx-parser</code></p>
<dd> Generate the C++/Parser mapping. For each input file in the form <code>name.xsd</code> the following C++ files are generated: <code>name-pskel.hxx</code> (parser skeleton header file), <code>name-pskel.ixx</code> (parser skeleton inline file, generated only if the <code>&#8211;generate-inline</code> option is specified), and <code>name-pskel.cxx</code> (parser skeleton source file). If the <code>&#8211;generate-noop-impl</code> or <code>&#8211;generate-print-impl</code> option is specified, the following additional sample implementation files are generated: <code>name-pimpl.hxx</code> (parser implementation header file) and <code>name-pimpl.cxx</code> (parser implementation source file). If the <code>&#8211;generate-test-driver</code> option is specified, the additional <code>name-driver.cxx</code> test driver file is generated. </p>
<dt><code>help</code></p>
<dd> Print usage information and exit. Use</dl>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> <code>xsdcxx help</code> <i>command</i></dl>
<p> for command-specific help.</dl>
<dl>
<dt><code>version</code></p>
<dd> Print version and exit.</dl>
<h2>OPTIONS</h2>
<p> Command-specific <i>options</i>, if any, should appear after the corresponding <i>command</i>. </p>
<h3>common options</h3>
<dl>
<dt><code>&#8211;std</code> <i>version</i></p>
<dd> Specify the C++ standard that the generated code should conform to. Valid values are <code>c++98</code> (default) and <code>c++11</code>. </p>
<p> The C++ standard affects various aspects of the generated code that are discussed in more detail in various mapping-specific documentation. Overall, when C++11 is selected, the generated code relies on the move semantics and uses <code>std::unique_ptr</code> instead of deprecated <code>std::auto_ptr</code>. </p>
<p> When the C++11 mode is selected, you normally don&#8217;t need to perform any extra steps other than enable C++11 in your C++ compiler, if required. The XSDCXX compiler will automatically add the necessary macro defines to the generated header files that will switch the header-only XSDCXX runtime library (<code>libxsd</code>) to the C++11 mode. However, if you include any of the XSDCXX runtime headers directly in your application (normally you just include the generated headers), then you will need to define the <code>XSD_CXX11</code> macro for your entire project. </p>
<dt><code>&#8211;char-type</code> <i>type</i></p>
<dd> Generate code using the provided character <i>type</i> instead of the default <code>char</code>. Valid values are <code>char</code> and <code>wchar_t</code>. </p>
<dt><code>&#8211;char-encoding</code> <i>enc</i></p>
<dd> Specify the character encoding that should be used in the generated code. Valid values for the <code>char</code> character type are <code>utf8</code> (default), <code>iso8859-1</code>, <code>lcp</code> (Xerces-C++ local code page), and <code>custom</code>. If you pass <code>custom</code> as the value then you will need to include the transcoder implementation header for your encoding at the beginning of the generated header files (see the <code>&#8211;hxx-prologue</code> option). </p>
<p> For the <code>wchar_t</code> character type the only valid value is <code>auto</code> and the encoding is automatically selected between UTF-16 and UTF-32/UCS-4, depending on the <code>wchar_t</code> type size. </p>
<dt><code>&#8211;output-dir</code> <i>dir</i></p>
<dd> Write generated files to <i>dir</i> instead of the current directory. </p>
<dt><code>&#8211;generate-inline</code></p>
<dd> Generate simple functions inline. This option triggers creation of the inline file. </p>
<dt><code>&#8211;generate-xml-schema</code></p>
<dd> Generate a C++ header file as if the schema being compiled defines the XML Schema namespace. For the C++/Tree mapping, the resulting file will contain definitions for all XML Schema built-in types. For the C++/Parser mapping, the resulting file will contain definitions for all the parser skeletons and implementations corresponding to the XML Schema built-in types. </p>
<p> The schema file provided to the compiler need not exist and is only used to derive the name of the resulting header file. Use the <code>&#8211;extern-xml-schema</code> option to include this file in the generated files for other schemas. </p>
<dt><code>&#8211;extern-xml-schema</code> <i>file</i></p>
<dd> Include a header file derived from <i>file</i> instead of generating the XML Schema namespace mapping inline. The provided file need not exist and is only used to derive the name of the included header file. Use the <code>&#8211;generate-xml-schema</code> option to generate this header file. </p>
<dt><code>&#8211;namespace-map</code> <i>xns</i>=<i>cns</i></p>
<dd> Map XML Schema namespace <i>xns</i> to C++ namespace <i>cns</i>. Repeat this option to specify mapping for more than one XML Schema namespace. For example, the following option: </p>
<p> <code>&#8211;namespace-map <a rel="nofollow" href="http://example.com/foo/bar=foo::bar">http://example.com/foo/bar=foo::bar</a></code> </p>
<p> Will map the <code><a rel="nofollow" href="http://example.com/foo/bar">http://example.com/foo/bar</a></code> XML Schema namespace to the <code>foo::bar</code> C++ namespace. </p>
<dt><code>&#8211;namespace-regex</code> <i>regex</i></p>
<dd> Add <i>regex</i> to the list of regular expressions used to translate XML Schema namespace names to C++ namespace names. <i>regex</i> is a Perl-like regular expression in the form <code>/</code><i>pattern</i><code>/</code><i>replacement</i><code>/</code>. Any character can be used as a delimiter instead of <code>/</code>. Escaping of the delimiter character in <i>pattern</i> or <i>replacement</i> is not supported. </p>
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
<dt><code>&#8211;namespace-regex-trace</code></p>
<dd> Trace the process of applying regular expressions specified with the <code>&#8211;namespace-regex</code> option. Use this option to find out why your regular expressions don&#8217;t do what you expected them to do. </p>
<dt><code>&#8211;reserved-name</code> <i>n</i>[=<i>r</i>]</p>
<dd> Add name <i>n</i> to the list of names that should not be used as identifiers. The name can optionally be followed by <code>=</code> and the replacement name <i>r</i> that should be used instead. All the C++ keywords are already in this list. </p>
<dt><code>&#8211;include-with-brackets</code></p>
<dd> Use angle brackets (&lt;&gt;) instead of quotes (&quot;&quot;) in generated <code>#include</code> directives. </p>
<dt><code>&#8211;include-prefix</code> <i>prefix</i></p>
<dd> Add <i>prefix</i> to generated <code>#include</code> directive paths. </p>
<p> For example, if you had the following import element in your schema </p>
<p> <code>&lt;import namespace=&quot;&#8230;&quot; schemaLocation=&quot;base.xsd&quot;/&gt;</code> </p>
<p> and compiled this fragment with <code>&#8211;include-prefix schemas/</code>, then the include directive in the generated code would be: </p>
<p> <code>#include &quot;schemas/base.hxx&quot;</code> </p>
<dt><code>&#8211;include-regex</code> <i>regex</i></p>
<dd> Add <i>regex</i> to the list of regular expressions used to transform <code>#include</code> directive paths. <i>regex</i> is a Perl-like regular expression in the form <code>/</code><i>pattern</i><code>/</code><i>replacement</i><code>/</code>. Any character can be used as a delimiter instead of <code>/</code>. Escaping of the delimiter character in <i>pattern</i> or <i>replacement</i> is not supported. </p>
<p> All the regular expressions are pushed into a stack with the last specified expression considered first. The first match that succeeds is used. </p>
<p> As an example, the following expression transforms paths in the form <code>schemas/foo/bar</code> to paths in the form <code>generated/foo/bar</code>: </p>
<p> <code>%schemas/(.+)%generated/$1%</code> </p>
<p> See also the REGEX AND SHELL QUOTING section below. </p>
<dt><code>&#8211;include-regex-trace</code></p>
<dd> Trace the process of applying regular expressions specified with the <code>&#8211;include-regex</code> option. Use this option to find out why your regular expressions don&#8217;t do what you expected them to do. </p>
<dt><code>&#8211;guard-prefix</code> <i>prefix</i></p>
<dd> Add <i>prefix</i> to generated header inclusion guards. The prefix is transformed to upper case and characters that are illegal in a preprocessor macro name are replaced with underscores. If this option is not specified then the directory part of the input schema file is used as a prefix. </p>
<dt><code>&#8211;hxx-suffix</code> <i>suffix</i></p>
<dd> Use the provided <i>suffix</i> instead of the default <code>.hxx</code> to construct the name of the header file. Note that this suffix is also used to construct names of header files corresponding to included/imported schemas. </p>
<dt><code>&#8211;ixx-suffix</code> <i>suffix</i></p>
<dd> Use the provided <i>suffix</i> instead of the default <code>.ixx</code> to construct the name of the inline file. </p>
<dt><code>&#8211;cxx-suffix</code> <i>suffix</i></p>
<dd> Use the provided <i>suffix</i> instead of the default <code>.cxx</code> to construct the name of the source file. </p>
<dt><code>&#8211;fwd-suffix</code> <i>suffix</i></p>
<dd> Use the provided <i>suffix</i> instead of the default <code>-fwd.hxx</code> to construct the name of the forward declaration file. </p>
<dt><code>&#8211;hxx-regex</code> <i>regex</i></p>
<dd> Use the provided expression to construct the name of the header file. <i>regex</i> is a Perl-like regular expression in the form <code>/</code><i>pattern</i><code>/</code><i>replacement</i><code>/</code>. Note that this expression is also used to construct names of header files corresponding to included/imported schemas. See also the REGEX AND SHELL QUOTING section below. </p>
<dt><code>&#8211;ixx-regex</code> <i>regex</i></p>
<dd> Use the provided expression to construct the name of the inline file. <i>regex</i> is a Perl-like regular expression in the form <code>/</code><i>pattern</i><code>/</code><i>replacement</i><code>/</code>. See also the REGEX AND SHELL QUOTING section below. </p>
<dt><code>&#8211;cxx-regex</code> <i>regex</i></p>
<dd> Use the provided expression to construct the name of the source file. <i>regex</i> is a Perl-like regular expression in the form <code>/</code><i>pattern</i><code>/</code><i>replacement</i><code>/</code>. See also the REGEX AND SHELL QUOTING section below. </p>
<dt><code>&#8211;fwd-regex</code> <i>regex</i></p>
<dd> Use the provided expression to construct the name of the forward declaration file. <i>regex</i> is a Perl-like regular expression in the form <code>/</code><i>pattern</i><code>/</code><i>replacement</i><code>/</code>. See also the REGEX AND SHELL QUOTING section below. </p>
<dt><code>&#8211;hxx-prologue</code> <i>text</i></p>
<dd> Insert <i>text</i> at the beginning of the header file. </p>
<dt><code>&#8211;ixx-prologue</code> <i>text</i></p>
<dd> Insert <i>text</i> at the beginning of the inline file. </p>
<dt><code>&#8211;cxx-prologue</code> <i>text</i></p>
<dd> Insert <i>text</i> at the beginning of the source file. </p>
<dt><code>&#8211;fwd-prologue</code> <i>text</i></p>
<dd> Insert <i>text</i> at the beginning of the forward declaration file. </p>
<dt><code>&#8211;prologue</code> <i>text</i></p>
<dd> Insert <i>text</i> at the beginning of each generated file for which there is no file-specific prologue. </p>
<dt><code>&#8211;hxx-epilogue</code> <i>text</i></p>
<dd> Insert <i>text</i> at the end of the header file. </p>
<dt><code>&#8211;ixx-epilogue</code> <i>text</i></p>
<dd> Insert <i>text</i> at the end of the inline file. </p>
<dt><code>&#8211;cxx-epilogue</code> <i>text</i></p>
<dd> Insert <i>text</i> at the end of the source file. </p>
<dt><code>&#8211;fwd-epilogue</code> <i>text</i></p>
<dd> Insert <i>text</i> at the end of the forward declaration file. </p>
<dt><code>&#8211;epilogue</code> <i>text</i></p>
<dd> Insert <i>text</i> at the end of each generated file for which there is no file-specific epilogue. </p>
<dt><code>&#8211;hxx-prologue-file</code> <i>file</i></p>
<dd> Insert the content of the <i>file</i> at the beginning of the header file. </p>
<dt><code>&#8211;ixx-prologue-file</code> <i>file</i></p>
<dd> Insert the content of the <i>file</i> at the beginning of the inline file. </p>
<dt><code>&#8211;cxx-prologue-file</code> <i>file</i></p>
<dd> Insert the content of the <i>file</i> at the beginning of the source file. </p>
<dt><code>&#8211;fwd-prologue-file</code> <i>file</i></p>
<dd> Insert the content of the <i>file</i> at the beginning of the forward declaration file. </p>
<dt><code>&#8211;prologue-file</code> <i>file</i></p>
<dd> Insert the content of the <i>file</i> at the beginning of each generated file for which there is no file-specific prologue file. </p>
<dt><code>&#8211;hxx-epilogue-file</code> <i>file</i></p>
<dd> Insert the content of the <i>file</i> at the end of the header file. </p>
<dt><code>&#8211;ixx-epilogue-file</code> <i>file</i></p>
<dd> Insert the content of the <i>file</i> at the end of the inline file. </p>
<dt><code>&#8211;cxx-epilogue-file</code> <i>file</i></p>
<dd> Insert the content of the <i>file</i> at the end of the source file. </p>
<dt><code>&#8211;fwd-epilogue-file</code> <i>file</i></p>
<dd> Insert the content of the <i>file</i> at the end of the forward declaration file. </p>
<dt><code>&#8211;epilogue-file</code> <i>file</i></p>
<dd> Insert the content of the <i>file</i> at the end of each generated file for which there is no file-specific epilogue file. </p>
<dt><code>&#8211;export-symbol</code> <i>symbol</i></p>
<dd> Insert <i>symbol</i> in places where DLL export/import control statements (<code>__declspec(dllexport/dllimport)</code>) are necessary. </p>
<dt><code>&#8211;export-xml-schema</code></p>
<dd> Export/import types in the XML Schema namespace using the export symbol provided with the <code>&#8211;export-symbol</code> option. The <code>XSD_NO_EXPORT</code> macro can be used to omit this code during C++ compilation, which may be useful if you would like to use the same generated code across multiple platforms. </p>
<dt><code>&#8211;export-maps</code></p>
<dd> Export polymorphism support maps from a Win32 DLL into which this generated code is placed. This is necessary when your type hierarchy is split across several DLLs since otherwise each DLL will have its own set of maps. In this situation the generated code for the DLL which contains base types and/or substitution group heads should be compiled with this option and the generated code for all other DLLs should be compiled with <code>&#8211;import-maps</code>. This option is only valid together with <code>&#8211;generate-polymorphic</code>. The <code>XSD_NO_EXPORT</code> macro can be used to omit this code during C++ compilation, which may be useful if you would like to use the same generated code across multiple platforms. </p>
<dt><code>&#8211;import-maps</code></p>
<dd> Import polymorphism support maps to a Win32 DLL or executable into which this generated code is linked. See the <code>&#8211;export-maps</code> option documentation for details. This options is only valid together with <code>&#8211;generate-polymorphic</code>. The <code>XSD_NO_EXPORT</code> macro can be used to omit this code during C++ compilation, which may be useful if you would like to use the same generated code across multiple platforms. </p>
<dt><code>&#8211;generate-dep</code></p>
<dd> Generate <code>make</code> dependency information. This option triggers the creation of the <code>.d</code> file containing the dependencies of the generated files on the main schema file as well as all the schema files that it includes/imports, transitively. This dependency file is then normally included into the main <code>makefile</code> to implement automatic dependency tracking. </p>
<p> Note also that automatic dependency generation is not supported in the file-per-type mode (<code>&#8211;file-per-type</code>). In this case, all the generated files are produced with a single compiler invocation and depend on all the schemas. As a result, it is easier to establish such a dependency manually, perhaps with the help of the <code>&#8211;file-list*</code> options. </p>
<dt><code>&#8211;generate-dep-only</code></p>
<dd> Generate <code>make</code> dependency information only. </p>
<dt><code>&#8211;dep-phony</code></p>
<dd> Generate phony targets for included/imported schema files, causing each to depend on nothing. Such dummy rules work around <code>make</code> errors caused by the removal of schema files without also updating the dependency file to match. </p>
<dt><code>&#8211;dep-target</code> <i>target</i></p>
<dd> Change the target of the dependency rule. By default it contains all the generated C++ files as well as the dependency file itself, without any directory prefixes. If you require multiple targets, then you can specify them as a single, space-separated argument or you can repeat this option multiple times. </p>
<dt><code>&#8211;dep-suffix</code> <i>suffix</i></p>
<dd> Use the provided <i>suffix</i> instead of the default <code>.d</code> to construct the name of the dependency file. </p>
<dt><code>&#8211;dep-regex</code> <i>regex</i></p>
<dd> Use the provided expression to construct the name of the dependency file. <i>regex</i> is a Perl-like regular expression in the form <code>/</code><i>pattern</i><code>/</code><i>replacement</i><code>/</code>. See also the REGEX AND SHELL QUOTING section below. </p>
<dt><code>&#8211;disable-warning</code> <i>warn</i></p>
<dd> Disable printing warning with id <i>warn</i>. If <code>all</code> is specified for the warning id then all warnings are disabled. </p>
<dt><code>&#8211;options-file</code> <i>file</i></p>
<dd> Read additional options from <i>file</i>. Each option should appearing on a separate line optionally followed by space and an option value. Empty lines and lines starting with <code>#</code> are ignored. Option values can be enclosed in double (<code>&quot;</code>) or single (<code>&#8216;</code>) quotes to preserve leading and trailing whitespaces as well as to specify empty values. If the value itself contains trailing or leading quotes, enclose it with an extra pair of quotes, for example <code>&#8216;&quot;x&quot;&#8217;</code>. Non-leading and non-trailing quotes are interpreted as being part of the option value. </p>
<p> The semantics of providing options in a file is equivalent to providing the same set of options in the same order on the command line at the point where the <code>&#8211;options-file</code> option is specified except that the shell escaping and quoting is not required. You can repeat this option to specify more than one options file. </p>
<dt><code>&#8211;show-sloc</code></p>
<dd> Show the number of generated physical source lines of code (SLOC). </p>
<dt><code>&#8211;sloc-limit</code> <i>num</i></p>
<dd> Check that the number of generated physical source lines of code (SLOC) does not exceed <i>num</i>. </p>
<dt><code>&#8211;proprietary-license</code></p>
<dd> Indicate that the generated code is licensed under a proprietary license instead of the GPL. </p>
<dt><code>&#8211;custom-literals</code> <i>file</i></p>
<dd> Load custom XML string to C++ literal mappings from <i>file</i>. This mechanism can be useful if you are using a custom character encoding and some of the strings in your schemas, for example element/attribute names or enumeration values, contain non-ASCII characters. In this case you will need to provide a custom mapping to C++ literals for such strings. The format of this file is specified in the <code>custom-literals.xsd</code> XML Schema file that can be found in the documentation directory. </p>
<dt><code>&#8211;preserve-anonymous</code></p>
<dd> Preserve anonymous types. By default anonymous types are automatically named with names derived from the enclosing elements/attributes. Because mappings implemented by this compiler require all types to be named, this option is only useful if you want to make sure your schemas don&#8217;t have anonymous types. </p>
<dt><code>&#8211;show-anonymous</code></p>
<dd> Show elements and attributes that are of anonymous types. This option only makes sense together with the <code>&#8211;preserve-anonymous</code> option. </p>
<dt><code>&#8211;anonymous-regex</code> <i>regex</i></p>
<dd> Add <i>regex</i> to the list of regular expressions used to derive names for anonymous types from the enclosing attributes/elements. <i>regex</i> is a Perl-like regular expression in the form <code>/</code><i>pattern</i><code>/</code><i>replacement</i><code>/</code>. Any character can be used as a delimiter instead of <code>/</code>. Escaping of the delimiter character in <i>pattern</i> or <i>replacement</i> is not supported. </p>
<p> All the regular expressions are pushed into a stack with the last specified expression considered first. The first match that succeeds is used. Regular expressions are applied to a string in the form </p>
<p> <i>filename</i> <i>namespace</i> <i>xpath</i> </p>
<p> For instance: </p>
<p> <code>hello.xsd <a rel="nofollow" href="http://example.com/hello">http://example.com/hello</a> element</code> </p>
<p> <code>hello.xsd <a rel="nofollow" href="http://example.com/hello">http://example.com/hello</a> type/element</code> </p>
<p> As an example, the following expression makes all the derived names start with capital letters. This could be useful when your naming convention requires type names to start with capital letters: </p>
<p> <code>%.* .* (.+/)*(.+)%
