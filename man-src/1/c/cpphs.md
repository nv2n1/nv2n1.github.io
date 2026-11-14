---
title: "cpphs(1)"
name: "cpphs"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cpphs/"
description: "cpphs – liberalised cpp-a-like preprocessor for Haskell"
---

<h2 class="name">NAME</h2>
<p> cpphs &#8211; liberalised cpp-a-like preprocessor for Haskell</p>
<h2>SYNOPSIS</h2>
<p> <code>cpphs</code> [<i>FILENAME</i>|<i>OPTION</i>]&#8230; </p>
<h2>DESCRIPTION</h2>
<p> <i>cpphs</i> is a liberalised re-implementation of <code>cpp (1),</code> the C pre-processor, in and for Haskell. </p>
<p> Why re-implement cpp? Rightly or wrongly, the C pre-processor is widely used in Haskell source code. It enables conditional compilation for different compilers, different versions of the same compiler, and different OS platforms. It is also occasionally used for its macro language, which can enable certain forms of platform-specific detail-filling, such as the tedious boilerplate generation of instance definitions and FFI declarations. However, there are two problems with cpp, aside from the obvious aesthetic ones:</p>
<dl>
<dt>
<dd> For some Haskell systems, notably Hugs on Windows, a true cpp is not available by default.</p>
<dt>
<dd> Even for the other Haskell systems, the common cpp provided by the gcc 3.x series is changing subtly in ways that are incompatible with Haskell&#8217;s syntax. There have always been problems with, for instance, string gaps, and prime characters in identifiers. These problems are only going to get worse.</dl>
<p> So, it seemed right to attempt to provide an alternative to cpp, both more compatible with Haskell, and itself written in Haskell so that it can be distributed with compilers. </p>
<p> <i>cpphs</i> is pretty-much feature-complete, and compatible with the <code>-traditional</code> style of cpp. It has two modes:</p>
<dl>
<dt>
<dd> conditional compilation only (<code>&#8211;nomacro</code>),</p>
<dt>
<dd> and full macro-expansion (default).</dl>
<p> In <code>&#8211;nomacro</code> mode, <i>cpphs</i> performs only conditional compilation actions, i.e. <code>#include</code>&#8216;s, <code>#if</code>&#8216;s, and <code>#ifdef</code>&#8216;s are processed according to text-replacement definitions (both command-line and internal), but no parameterised macro expansion is performed. In full compatibility mode (the default), textual replacements and macro expansions are also processed in the remaining body of non-cpp text. </p>
<p> Working Features:</p>
<dl>
<dt><code>#ifdef</code></p>
<dd> simple conditional compilation</p>
<dt><code>#if</code></p>
<dd> the full boolean language of defined(), &amp;&amp;, ||, ==, etc.</p>
<dt><code>#elif</code></p>
<dd> chained conditionals</p>
<dt><code>#define</code></p>
<dd> in-line definitions (text replacements and macros)</p>
<dt><code>#undef</code></p>
<dd> in-line revocation of definitions</p>
<dt><code>#include</code></p>
<dd> file inclusion</p>
<dt><code>#line</code></p>
<dd> line number directives</p>
<dt><code>\n</code></p>
<dd> line continuations within all # directives</p>
<dt><code>/**/</code></p>
<dd> token catenation within a macro definition</p>
<dt><code>##</code></p>
<dd> ANSI-style token catenation</p>
<dt><code>#</code></p>
<dd> ANSI-style token stringisation</p>
<dt><code>__FILE__</code></p>
<dd> special text replacement for DIY error messages</p>
<dt><code>__LINE__</code></p>
<dd> special text replacement for DIY error messages</p>
<dt><code>__DATE__</code></p>
<dd> special text replacement</p>
<dt><code>__TIME__</code></p>
<dd> special text replacement</dl>
<p> Macro expansion is recursive. Redefinition of a macro name does not generate a warning. Macros can be defined on the command-line with <code>-D</code> just like textual replacements. Macro names are permitted to be Haskell identifiers e.g. with the prime ` and backtick &acute; characters, which is slightly looser than in C, but they still may not include operator symbols. </p>
<p> Numbering of lines in the output is preserved so that any later processor can give meaningful error messages. When a file is <code>#include</code>&#8216;d, <i>cpphs</i> inserts <code>#line</code> directives for the same reason. Numbering should be correct even in the presence of line continuations. If you don&#8217;t want <code>#line</code> directives in the final output, use the <code>&#8211;noline</code> option. </p>
<p> Any syntax errors in cpp directives gives a message to stderr and halts the program. Failure to find a #include&#8217;d file produces a warning to stderr, but processing continues. </p>
<p> You can give any number of filenames on the command-line. The results are catenated on standard output.</p>
<dl>
<dt><code>-D</code><i>sym</i></p>
<dd> define a textual replacement (default value is 1)</p>
<dt><code>-Dsym=</code><i>val</i></p>
<dd> define a textual replacement with a specific value</p>
<dt><code>-I</code><i>path</i></p>
<dd> add a directory to the search path for #include&#8217;s</p>
<dt><code>-O</code><i>file</i></p>
<dd> specify a file for output (default is stdout)</p>
<dt><code>&#8211;nomacro</code></p>
<dd> only process #ifdef&#8217;s and #include&#8217;s,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>do not expand macros</p>
<dt><code>&#8211;noline</code></p>
<dd> remove #line droppings from the output</p>
<dt><code>&#8211;strip</code></p>
<dd> convert C-style comments to whitespace, even outside<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>cpp directives</p>
<dt><code>&#8211;hashes</code></p>
<dd> recognise the ANSI # stringise operator, and ## for<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>token catenation, within macros</p>
<dt><code>&#8211;text</code></p>
<dd> treat the input as plain text, not Haskell code</p>
<dt><code>&#8211;layout</code></p>
<dd> preserve newlines within macro expansions</p>
<dt><code>&#8211;unlit</code></p>
<dd> remove literate-style comments</p>
<dt><code>&#8211;version</code></p>
<dd> report version number of cpphs and stop</dl>
<p> There are NO textual replacements defined by default. (Normal cpp usually has definitions for machine, OS, etc. These could easily be added to the cpphs source code if you wish.) The search path is searched in order of the <code>-I</code> options, except that the directory of the calling file, then the current directory, are always searched first. Again, there is no default search path (and again, this could easily be changed). </p>
<h2>DIFFERENCES FROM CPP</h2>
<p> In general, cpphs is based on the <code>-traditional</code> behaviour, not ANSI C, and has the following main differences from the standard cpp. </p>
<p> <code>General</code> </p>
<p> The <code>#</code> that introduces any cpp directive must be in the first column of a line (whereas ANSI permits whitespace before the <code>#</code> ). </p>
<p> Generates the <code>#line </code><i>n</i> &quot;<i>filename</i>&quot; syntax, not the <code># </code><i>n</i> &quot;<i>filename</i>&quot; variant. </p>
<p> C comments are only removed from within cpp directives. They are not stripped from other text. Consider for instance that in Haskell, all of the following are valid operator symbols: <code>/* */ */*</code> However, you can turn on C-comment removal with the <code>&#8211;strip</code> option. </p>
<p> <code>Macro language</code> </p>
<p> Accepts <code>/**/</code> for token-pasting in a macro definition. However, <code>/* */</code> (with any text between the open/close comment) inserts whitespace. </p>
<p> The ANSI <code>##</code> token-pasting operator is available with the <code>&#8211;hashes</code> flag. This is to avoid misinterpreting any valid Haskell operator of the same name. </p>
<p> Replaces a macro formal parameter with the actual, even inside a string (double or single quoted). This is -traditional behaviour, not supported in ANSI. </p>
<p> Recognises the <code>#</code> stringisation operator in a macro definition only if you use the <code>&#8211;hashes</code> option. (It is an ANSI addition, only needed because quoted stringisation (above) is prohibited by ANSI.) </p>
<p> Preserves whitespace within a textual replacement definition exactly (modulo newlines), but leading and trailing space is eliminated. </p>
<p> Preserves whitespace within a macro definition (and trailing it) exactly (modulo newlines), but leading space is eliminated. </p>
<p> Preserves whitespace within macro call arguments exactly (including newlines), but leading and trailing space is eliminated. </p>
<p> With the <code>&#8211;layout</code> option, line continuations in a textual replacement or macro definition are preserved as line-breaks in the macro call. (Useful for layout-sensitive code in Haskell.) </p>
<h2>BUGS</h2>
<p> Bug reports, and any other feedback, should be sent to Malcolm Wallace &lt;Malcolm.Wallace [at] cs.york.ac.uk&gt;</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2004-2005 Malcolm Wallace, except for ParseLib (Copyright &#169; 1995 Graham Hutton and Erik Meijer). </p>
<p> The library modules in cpphs are distributed under the terms of the LGPL. If that&#8217;s a problem for you, contact me to make other arrangements. The application module <code>Main.hs</code> itself is GPL.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-cpp/">cpp</a></code>(1) </p>
<h2>AUTHOR</h2>
<p> This manual page was written, based on <code>index.html</code>, by Ian Lynagh &lt;igloo [at] debian.org&gt; for the Debian system (but may be used by others). </p>
<h2>Index</h2>
