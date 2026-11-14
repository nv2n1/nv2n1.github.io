---
title: "swig(1)"
name: "swig"
section: "1"
letter: "s"
url: "/docs/linux/man/1-swig/"
description: "swig – Simplified Wrapper and Interface Generator"
---

<h2>NAME</h2>
<p> swig &#8211; Simplified Wrapper and Interface Generator</p>
<h2>SYNOPSIS</h2>
<p> <code>swig</code> [<i>options</i>]<i> file</i> </p>
<h2>DESCRIPTION</h2>
<p> The swig command is used to create wrapper code to connect C and C++ code to scripting languages like Perl, Python, Tcl etc. from the definition of the interface. For detailed information on writing those interface definitions please refer to /usr/share/doc/swig-doc-2.0.9/Doc/Manual/index.html from the swig-doc package. This manpage concentrates on explaining the invocation of the swig command. </p>
<h2>OPTIONS</h2>
<h3>Target Language Options:</h3>
<dl>
<dt><code>-allegrocl</code></p>
<dd> Generate ALLEGROCL wrappers</p>
<dt><code>-chicken</code></p>
<dd> Generate CHICKEN wrappers</p>
<dt><code>-clisp</code></p>
<dd> Generate CLISP wrappers</p>
<dt><code>-cffi</code></p>
<dd> Generate CFFI wrappers</p>
<dt><code>-csharp</code></p>
<dd> Generate C# wrappers</p>
<dt><code>-d</code></p>
<dd> Generate D wrappers</p>
<dt><code>-go</code></p>
<dd> Generate Go wrappers</p>
<dt><code>-guile</code></p>
<dd> Generate Guile wrappers</p>
<dt><code>-java</code></p>
<dd> Generate Java wrappers</p>
<dt><code>-lua</code></p>
<dd> Generate Lua wrappers</p>
<dt><code>-modula3</code></p>
<dd> Generate Modula 3 wrappers</p>
<dt><code>-mzscheme</code></p>
<dd> Generate Mzscheme wrappers</p>
<dt><code>-ocaml</code></p>
<dd> Generate Ocaml wrappers</p>
<dt><code>-octave</code></p>
<dd> Generate Octave wrappers</p>
<dt><code>-perl</code></p>
<dd> Generate Perl wrappers</p>
<dt><code>-php</code></p>
<dd> Generate PHP wrappers</p>
<dt><code>-pike</code></p>
<dd> Generate Pike wrappers</p>
<dt><code>-python</code></p>
<dd> Generate Python wrappers</p>
<dt><code>-r</code></p>
<dd> Generate R (aka GNU S) wrappers</p>
<dt><code>-ruby</code></p>
<dd> Generate Ruby wrappers</p>
<dt><code>-sexp</code></p>
<dd> Generate Lisp S-Expressions wrappers</p>
<dt><code>-tcl</code></p>
<dd> Generate Tcl wrappers</p>
<dt><code>-uffi</code></p>
<dd> Generate Common Lisp / UFFI wrappers</p>
<dt><code>-xml</code></p>
<dd> Generate XML wrappers i </p>
</dl>
<h3>General Options:</h3>
<dl>
<dt><code>-addextern</code></p>
<dd> Add extra extern declarations</p>
<dt><code>-c++</code></p>
<dd> Enable C++ processing</p>
<dt><code>-co </code><i>file</i></p>
<dd> Check <i>file</i> out of the SWIG library</p>
<dt><code>-copyctor</code></p>
<dd> Automatically generate copy constructors wherever possible</p>
<dt><code>-cpperraswarn</code></p>
<dd> Treat the preprocessor #error statement as #warning (default)</p>
<dt><code>-copyright</code></p>
<dd> Display copyright notices</p>
<dt><code>-debug-classes</code></p>
<dd> Display information about the classes found in the interface</p>
<dt><code>-debug-module </code><i>n</i></p>
<dd> Display module parse tree at stages 1-4, <i>n</i> is a csv list of stages</p>
<dt><code>-debug-symtabs</code></p>
<dd> Display symbol tables information</p>
<dt><code>-debug-symbols</code></p>
<dd> Display target language symbols in the symbol tables</p>
<dt><code>-debug-csymbols</code></p>
<dd> Display C symbols in the symbol tables</p>
<dt><code>-debug-lsymbols</code></p>
<dd> Display target language layer symbols</p>
<dt><code>-debug-tags</code></p>
<dd> Display information about the tags found in the interface</p>
<dt><code>-debug-template</code></p>
<dd> Display information for debugging templates</p>
<dt><code>-debug-top </code><i>n</i></p>
<dd> Display entire parse tree at stages 1-4, <i>n</i> is a csv list of stages</p>
<dt><code>-debug-typedef</code></p>
<dd> Display information about the types and typedefs in the interface</p>
<dt><code>-debug-typemap</code></p>
<dd> Display typemap debugging information</p>
<dt><code>-debug-tmsearch</code></p>
<dd> Display typemap search debugging information</p>
<dt><code>-debug-tmused</code></p>
<dd> Display typemaps used debugging information</p>
<dt><code>-directors</code></p>
<dd> Turn on director mode for all the classes, mainly for testing</p>
<dt><code>-dirprot</code></p>
<dd> Turn on wrapping of protected members for director classes (default)</p>
<dt><code>-D</code><i>symbol</i></p>
<dd> Define a symbol <i>symbol</i> (for conditional compilation)</p>
<dt><code>-E</code></p>
<dd> Preprocess only, does not generate wrapper code</p>
<dt><code>-external-runtime [file]</code></p>
<dd> Export the SWIG runtime stack</p>
<dt><code>-fakeversion </code><i>v</i></p>
<dd> Make SWIG fake the program version number to <i>v</i></p>
<dt><code>-fcompact</code></p>
<dd> Compile in compact mode</p>
<dt><code>-features </code><i>list</i></p>
<dd> Set global features, where <i>list</i> is a comma separated list of features, eg -features directors,autodoc=1 If no explicit value is given to the feature, a default of 1 is used</p>
<dt><code>-fastdispatch</code></p>
<dd> Enable fast dispatch mode to produce faster overload dispatcher code</p>
<dt><code>-Fmicrosoft</code></p>
<dd> Display error/warning messages in Microsoft format</p>
<dt><code>-Fstandard</code></p>
<dd> Display error/warning messages in commonly used format</p>
<dt><code>-fvirtual</code></p>
<dd> Compile in virtual elimination mode</p>
<dt><code>-help</code></p>
<dd> This output</p>
<dt><code>-I-</code></p>
<dd> Don&#8217;t search the current directory</p>
<dt><code>-I</code><i>dir</i></p>
<dd> Look for SWIG files in directory <i>dir</i></p>
<dt><code>-ignoremissing</code></p>
<dd> Ignore missing include files</p>
<dt><code>-importall</code></p>
<dd> Follow all #include statements as imports</p>
<dt><code>-includeall</code></p>
<dd> Follow all #include statements</p>
<dt><code>-l</code><i>ifile</i></p>
<dd> Include SWIG library file <i>ifile</i></p>
<dt><code>-macroerrors</code></p>
<dd> Report errors inside macros</p>
<dt><code>-makedefault</code></p>
<dd> Create default constructors/destructors (the default)</p>
<dt><code>-M</code></p>
<dd> List all dependencies</p>
<dt><code>-MD</code></p>
<dd> Is equivalent to &#8216;-M -MF <i>file</i>&#8216;, except &#8216;-E&#8217; is not implied</p>
<dt><code>-MF </code><i>file</i></p>
<dd> Generate dependencies into <i>file</i> and continue generating wrappers</p>
<dt><code>-MM</code></p>
<dd> List dependencies, but omit files in SWIG library</p>
<dt><code>-MMD</code></p>
<dd> Like &#8216;-MD&#8217;, but omit files in SWIG library</p>
<dt><code>-module </code><i>name</i></p>
<dd> Set module name to <i>name</i></p>
<dt><code>-MP</code></p>
<dd> Generate phony targets for all dependencies</p>
<dt><code>-MT </code><i>target</i></p>
<dd> Set the target of the rule emitted by dependency generation</p>
<dt><code>-nocontract</code></p>
<dd> Turn off contract checking</p>
<dt><code>-nocpperraswarn</code></p>
<dd> Do not treat the preprocessor #error statement as #warning</p>
<dt><code>-nodefault</code></p>
<dd> Do not generate default constructors nor default destructors</p>
<dt><code>-nodefaultctor</code></p>
<dd> Do not generate implicit default constructors</p>
<dt><code>-nodefaultdtor</code></p>
<dd> Do not generate implicit default destructors</p>
<dt><code>-nodirprot</code></p>
<dd> Do not wrap director protected members</p>
<dt><code>-noexcept</code></p>
<dd> Do not wrap exception specifiers</p>
<dt><code>-nofastdispatch</code></p>
<dd> Disable fast dispatch mode (default)</p>
<dt><code>-nopreprocess</code></p>
<dd> Skip the preprocessor step</p>
<dt><code>-notemplatereduce</code></p>
<dd> Disable reduction of the typedefs in templates</p>
<dt><code>-O</code></p>
<dd> Enable the optimization options: -fastdispatch -fvirtual</p>
<dt><code>-o </code><i>outfile</i></p>
<dd> Set name of the output file to <i>outfile</i></p>
<dt><code>-oh headfile</code></p>
<dd> Set name of the output header file to <i>headfile</i></p>
<dt><code>-outcurrentdir</code></p>
<dd> Set default output dir to current dir instead of input file&#8217;s path</p>
<dt><code>-outdir </code><i>dir</i></p>
<dd> Set language specific files output directory to <i>dir</i></p>
<dt><code>-pcreversion</code></p>
<dd> Display PCRE version information</p>
<dt><code>-small</code></p>
<dd> Compile in virtual elimination &amp; compact mode</p>
<dt><code>-swiglib</code></p>
<dd> Report location of SWIG library and exit</p>
<dt><code>-templatereduce</code></p>
<dd> Reduce all the typedefs in templates</p>
<dt><code>-v</code></p>
<dd> Run in verbose mode</p>
<dt><code>-version</code></p>
<dd> Display SWIG version number</p>
<dt><code>-Wall</code></p>
<dd> Remove all warning suppression, also implies -Wextra</p>
<dt><code>-Wallkw</code></p>
<dd> Enable keyword warnings for all the supported languages</p>
<dt><code>-Werror</code></p>
<dd> Treat warnings as errors</p>
<dt><code>-Wextra</code></p>
<dd> Adds the following additional warnings: 202,309,403,512,321,322</p>
<dt><code>-w</code><i>list</i></p>
<dd> Suppress/add warning messages, eg -w401,+321 see Warnings.html</p>
<dt><code>-xmlout file</code></p>
<dd> Write XML version of the parse tree to <i>file</i> after normal processing </p>
</dl>
<h3>Tcl 8 Options (available with -tcl)</h3>
<dl>
<dt><code>-itcl</code></p>
<dd> Enable ITcl support</p>
<dt><code>-nosafe</code></p>
<dd> Leave out SafeInit module function.</p>
<dt><code>-prefix </code><i>name</i></p>
<dd> Set a prefix <i>name</i> to be prepended to all names</p>
<dt><code>-namespace</code></p>
<dd> Build module into a Tcl 8 namespace</p>
<dt><code>-pkgversion</code></p>
<dd> Set package version </p>
</dl>
<p> Note: &#8216;swig &#8211;<i>lang</i> -help&#8217; displays options for a specific target language. </p>
<h2>AUTHOR</h2>
<p> SWIG was originally created by David Beazley. For up-to-date information about authors and contributors please check <a rel="nofollow" href="http://www.swig.org/guilty.html.">http://www.swig.org/guilty.html.</a> This manual page was written by Torsten Landschoff &lt;torsten [at] debian.org&gt; and updated by Jitka Plesnikova &lt;jplesnik [at] redhat.com&gt; (but may be used by others). </p>
<h2>Index</h2>
