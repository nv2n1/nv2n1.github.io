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
<dt><code>-allegrocl</code></dt>
<dd> Generate ALLEGROCL wrappers</dd>
<dt><code>-chicken</code></dt>
<dd> Generate CHICKEN wrappers</dd>
<dt><code>-clisp</code></dt>
<dd> Generate CLISP wrappers</dd>
<dt><code>-cffi</code></dt>
<dd> Generate CFFI wrappers</dd>
<dt><code>-csharp</code></dt>
<dd> Generate C# wrappers</dd>
<dt><code>-d</code></dt>
<dd> Generate D wrappers</dd>
<dt><code>-go</code></dt>
<dd> Generate Go wrappers</dd>
<dt><code>-guile</code></dt>
<dd> Generate Guile wrappers</dd>
<dt><code>-java</code></dt>
<dd> Generate Java wrappers</dd>
<dt><code>-lua</code></dt>
<dd> Generate Lua wrappers</dd>
<dt><code>-modula3</code></dt>
<dd> Generate Modula 3 wrappers</dd>
<dt><code>-mzscheme</code></dt>
<dd> Generate Mzscheme wrappers</dd>
<dt><code>-ocaml</code></dt>
<dd> Generate Ocaml wrappers</dd>
<dt><code>-octave</code></dt>
<dd> Generate Octave wrappers</dd>
<dt><code>-perl</code></dt>
<dd> Generate Perl wrappers</dd>
<dt><code>-php</code></dt>
<dd> Generate PHP wrappers</dd>
<dt><code>-pike</code></dt>
<dd> Generate Pike wrappers</dd>
<dt><code>-python</code></dt>
<dd> Generate Python wrappers</dd>
<dt><code>-r</code></dt>
<dd> Generate R (aka GNU S) wrappers</dd>
<dt><code>-ruby</code></dt>
<dd> Generate Ruby wrappers</dd>
<dt><code>-sexp</code></dt>
<dd> Generate Lisp S-Expressions wrappers</dd>
<dt><code>-tcl</code></dt>
<dd> Generate Tcl wrappers</dd>
<dt><code>-uffi</code></dt>
<dd> Generate Common Lisp / UFFI wrappers</dd>
<dt><code>-xml</code></dt>
<dd> Generate XML wrappers i </dd>
</dl>
<h3>General Options:</h3>
<dl>
<dt><code>-addextern</code></dt>
<dd> Add extra extern declarations</dd>
<dt><code>-c++</code></dt>
<dd> Enable C++ processing</dd>
<dt><code>-co </code><i>file</i></dt>
<dd> Check <i>file</i> out of the SWIG library</dd>
<dt><code>-copyctor</code></dt>
<dd> Automatically generate copy constructors wherever possible</dd>
<dt><code>-cpperraswarn</code></dt>
<dd> Treat the preprocessor #error statement as #warning (default)</dd>
<dt><code>-copyright</code></dt>
<dd> Display copyright notices</dd>
<dt><code>-debug-classes</code></dt>
<dd> Display information about the classes found in the interface</dd>
<dt><code>-debug-module </code><i>n</i></dt>
<dd> Display module parse tree at stages 1-4, <i>n</i> is a csv list of stages</dd>
<dt><code>-debug-symtabs</code></dt>
<dd> Display symbol tables information</dd>
<dt><code>-debug-symbols</code></dt>
<dd> Display target language symbols in the symbol tables</dd>
<dt><code>-debug-csymbols</code></dt>
<dd> Display C symbols in the symbol tables</dd>
<dt><code>-debug-lsymbols</code></dt>
<dd> Display target language layer symbols</dd>
<dt><code>-debug-tags</code></dt>
<dd> Display information about the tags found in the interface</dd>
<dt><code>-debug-template</code></dt>
<dd> Display information for debugging templates</dd>
<dt><code>-debug-top </code><i>n</i></dt>
<dd> Display entire parse tree at stages 1-4, <i>n</i> is a csv list of stages</dd>
<dt><code>-debug-typedef</code></dt>
<dd> Display information about the types and typedefs in the interface</dd>
<dt><code>-debug-typemap</code></dt>
<dd> Display typemap debugging information</dd>
<dt><code>-debug-tmsearch</code></dt>
<dd> Display typemap search debugging information</dd>
<dt><code>-debug-tmused</code></dt>
<dd> Display typemaps used debugging information</dd>
<dt><code>-directors</code></dt>
<dd> Turn on director mode for all the classes, mainly for testing</dd>
<dt><code>-dirprot</code></dt>
<dd> Turn on wrapping of protected members for director classes (default)</dd>
<dt><code>-D</code><i>symbol</i></dt>
<dd> Define a symbol <i>symbol</i> (for conditional compilation)</dd>
<dt><code>-E</code></dt>
<dd> Preprocess only, does not generate wrapper code</dd>
<dt><code>-external-runtime [file]</code></dt>
<dd> Export the SWIG runtime stack</dd>
<dt><code>-fakeversion </code><i>v</i></dt>
<dd> Make SWIG fake the program version number to <i>v</i></dd>
<dt><code>-fcompact</code></dt>
<dd> Compile in compact mode</dd>
<dt><code>-features </code><i>list</i></dt>
<dd> Set global features, where <i>list</i> is a comma separated list of features, eg -features directors,autodoc=1 If no explicit value is given to the feature, a default of 1 is used</dd>
<dt><code>-fastdispatch</code></dt>
<dd> Enable fast dispatch mode to produce faster overload dispatcher code</dd>
<dt><code>-Fmicrosoft</code></dt>
<dd> Display error/warning messages in Microsoft format</dd>
<dt><code>-Fstandard</code></dt>
<dd> Display error/warning messages in commonly used format</dd>
<dt><code>-fvirtual</code></dt>
<dd> Compile in virtual elimination mode</dd>
<dt><code>-help</code></dt>
<dd> This output</dd>
<dt><code>-I-</code></dt>
<dd> Don&#8217;t search the current directory</dd>
<dt><code>-I</code><i>dir</i></dt>
<dd> Look for SWIG files in directory <i>dir</i></dd>
<dt><code>-ignoremissing</code></dt>
<dd> Ignore missing include files</dd>
<dt><code>-importall</code></dt>
<dd> Follow all #include statements as imports</dd>
<dt><code>-includeall</code></dt>
<dd> Follow all #include statements</dd>
<dt><code>-l</code><i>ifile</i></dt>
<dd> Include SWIG library file <i>ifile</i></dd>
<dt><code>-macroerrors</code></dt>
<dd> Report errors inside macros</dd>
<dt><code>-makedefault</code></dt>
<dd> Create default constructors/destructors (the default)</dd>
<dt><code>-M</code></dt>
<dd> List all dependencies</dd>
<dt><code>-MD</code></dt>
<dd> Is equivalent to &#8216;-M -MF <i>file</i>&#8216;, except &#8216;-E&#8217; is not implied</dd>
<dt><code>-MF </code><i>file</i></dt>
<dd> Generate dependencies into <i>file</i> and continue generating wrappers</dd>
<dt><code>-MM</code></dt>
<dd> List dependencies, but omit files in SWIG library</dd>
<dt><code>-MMD</code></dt>
<dd> Like &#8216;-MD&#8217;, but omit files in SWIG library</dd>
<dt><code>-module </code><i>name</i></dt>
<dd> Set module name to <i>name</i></dd>
<dt><code>-MP</code></dt>
<dd> Generate phony targets for all dependencies</dd>
<dt><code>-MT </code><i>target</i></dt>
<dd> Set the target of the rule emitted by dependency generation</dd>
<dt><code>-nocontract</code></dt>
<dd> Turn off contract checking</dd>
<dt><code>-nocpperraswarn</code></dt>
<dd> Do not treat the preprocessor #error statement as #warning</dd>
<dt><code>-nodefault</code></dt>
<dd> Do not generate default constructors nor default destructors</dd>
<dt><code>-nodefaultctor</code></dt>
<dd> Do not generate implicit default constructors</dd>
<dt><code>-nodefaultdtor</code></dt>
<dd> Do not generate implicit default destructors</dd>
<dt><code>-nodirprot</code></dt>
<dd> Do not wrap director protected members</dd>
<dt><code>-noexcept</code></dt>
<dd> Do not wrap exception specifiers</dd>
<dt><code>-nofastdispatch</code></dt>
<dd> Disable fast dispatch mode (default)</dd>
<dt><code>-nopreprocess</code></dt>
<dd> Skip the preprocessor step</dd>
<dt><code>-notemplatereduce</code></dt>
<dd> Disable reduction of the typedefs in templates</dd>
<dt><code>-O</code></dt>
<dd> Enable the optimization options: -fastdispatch -fvirtual</dd>
<dt><code>-o </code><i>outfile</i></dt>
<dd> Set name of the output file to <i>outfile</i></dd>
<dt><code>-oh headfile</code></dt>
<dd> Set name of the output header file to <i>headfile</i></dd>
<dt><code>-outcurrentdir</code></dt>
<dd> Set default output dir to current dir instead of input file&#8217;s path</dd>
<dt><code>-outdir </code><i>dir</i></dt>
<dd> Set language specific files output directory to <i>dir</i></dd>
<dt><code>-pcreversion</code></dt>
<dd> Display PCRE version information</dd>
<dt><code>-small</code></dt>
<dd> Compile in virtual elimination &amp; compact mode</dd>
<dt><code>-swiglib</code></dt>
<dd> Report location of SWIG library and exit</dd>
<dt><code>-templatereduce</code></dt>
<dd> Reduce all the typedefs in templates</dd>
<dt><code>-v</code></dt>
<dd> Run in verbose mode</dd>
<dt><code>-version</code></dt>
<dd> Display SWIG version number</dd>
<dt><code>-Wall</code></dt>
<dd> Remove all warning suppression, also implies -Wextra</dd>
<dt><code>-Wallkw</code></dt>
<dd> Enable keyword warnings for all the supported languages</dd>
<dt><code>-Werror</code></dt>
<dd> Treat warnings as errors</dd>
<dt><code>-Wextra</code></dt>
<dd> Adds the following additional warnings: 202,309,403,512,321,322</dd>
<dt><code>-w</code><i>list</i></dt>
<dd> Suppress/add warning messages, eg -w401,+321 see Warnings.html</dd>
<dt><code>-xmlout file</code></dt>
<dd> Write XML version of the parse tree to <i>file</i> after normal processing </dd>
</dl>
<h3>Tcl 8 Options (available with -tcl)</h3>
<dl>
<dt><code>-itcl</code></dt>
<dd> Enable ITcl support</dd>
<dt><code>-nosafe</code></dt>
<dd> Leave out SafeInit module function.</dd>
<dt><code>-prefix </code><i>name</i></dt>
<dd> Set a prefix <i>name</i> to be prepended to all names</dd>
<dt><code>-namespace</code></dt>
<dd> Build module into a Tcl 8 namespace</dd>
<dt><code>-pkgversion</code></dt>
<dd> Set package version </dd>
</dl>
<p> Note: &#8216;swig &#8211;<i>lang</i> -help&#8217; displays options for a specific target language. </p>
<h2>AUTHOR</h2>
<p> SWIG was originally created by David Beazley. For up-to-date information about authors and contributors please check <a rel="nofollow" href="http://www.swig.org/guilty.html.">http://www.swig.org/guilty.html.</a> This manual page was written by Torsten Landschoff &lt;torsten [at] debian.org&gt; and updated by Jitka Plesnikova &lt;jplesnik [at] redhat.com&gt; (but may be used by others). </p>
