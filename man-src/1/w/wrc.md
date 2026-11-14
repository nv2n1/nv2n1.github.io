---
title: "wrc(1)"
name: "wrc"
section: "1"
letter: "w"
url: "/docs/linux/man/1-wrc/"
description: "wrc – Wine Resource Compiler"
---

<h2>NAME</h2>
<p> wrc &#8211; Wine Resource Compiler</p>
<h2>SYNOPSIS</h2>
<p> <code>wrc</code> [<i>options</i>]&nbsp;<wbr>[<i>inputfile</i>&#8230;]</p>
<h2>DESCRIPTION</h2>
<p> <code>wrc</code> compiles resources from <i>inputfile</i> into win16 and win32 compatible binary format. </p>
<p> The source file is preprocessed with a builtin ANSI-C compatible preprocessor before the resources are compiled. See <code>PREPROCESSOR</code> below. </p>
<p> <code>wrc</code> takes a series of <i>inputfile</i> as argument. The resources are read from standard input if no inputfile is given. If the output file is not specified with <code>-o</code>, then <code>wrc</code> will write the output to <i>inputfile.res</i> with <i>.rc</i> stripped, or to <i>wrc.tab.res</i> if no inputfile was given.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-b, &#8211;target=</code><i>cpu-manufacturer</i>[<i></i><code>&#8211;</code><i>kernel</i>]<code>&#8211;</code><i>os</i></p>
<dd> Specify the target CPU and platform on which the generated code will be built. The target specification is in the standard autoconf format as returned by <code>config.sub</code>.</p>
<dt><i></i><code>-D</code>, <code>&#8211;define</code>=<i>id</i>[<code>=</code><i>val</i>]</p>
<dd> Define preprocessor identifier <i>id</i> to (optionally) value <i>val</i>. See also <code>PREPROCESSOR</code> below.</p>
<dt><i></i><code>&#8211;debug</code>=<i>nn</i></p>
<dd> Set debug level to <i>nn</i>. The value is a bitmask consisting of 1=verbose, 2=dump internals, 4=resource parser trace, 8=preprocessor messages, 16=preprocessor scanner and 32=preprocessor parser trace.</p>
<dt><i></i><code>&#8211;endianness</code>=<i>e</i></p>
<dd> Win32 only; set output byte-ordering, where <i>e</i> is one of n[ative], l[ittle] or b[ig]. Only resources in source-form can be reordered. Native ordering depends on the system on which <code>wrc</code> was built. You can see the native ordering by typing <i>wrc -h</i>.</p>
<dt><i></i><code>-E</code></p>
<dd> Preprocess only. The output is written to standard output if no outputfile was selected. The output is compatible with what gcc would generate.</p>
<dt><i></i><code>-h</code>, <code>&#8211;help</code></p>
<dd> Prints a summary message and exits.</p>
<dt><i></i><code>-i</code>, <code>&#8211;input</code>=<i>file</i></p>
<dd> The name of the input file. If this option is not used, then <code>wrc</code> will use the first non-option argument as the input file name. If there are no non-option arguments, then <code>wrc</code> will read from standard input.</p>
<dt><i></i><code>-I</code>, <code>&#8211;include-dir</code>=<i>path</i></p>
<dd> Add <i>path</i> to include search directories. <i>path</i> may contain multiple directories, separated with &#8216;:&#8217;. It is allowed to specify <code>-I</code> multiple times. Include files are searched in the order in which the <code>-I</code> options were specified.<br />
 The search is compatible with gcc, in which &#8216;&lt;&gt;&#8217; quoted filenames are searched exclusively via the <code>-I</code> set path, whereas the &#8216;&quot;&quot;&#8217; quoted filenames are first tried to be opened in the current directory. Also resource statements with file references are located in the same way.</p>
<dt><i></i><code>-J</code>, <code>&#8211;input-format</code>=<i>format</i></p>
<dd> Sets the input format. Valid options are &#8216;rc&#8217; or &#8216;rc16&#8217;. Setting the input to &#8216;rc16&#8217; disables the recognition of win32 keywords.</p>
<dt><i></i><code>-l</code>, <code>&#8211;language</code>=<i>lang</i></p>
<dd> Set default language to <i>lang</i>. Default is the neutral language 0 (i.e. &quot;LANGUAGE 0, 0&quot;).</p>
<dt><code>-m16, -m32, -m64</code></p>
<dd> Generate resources for 16-bit, 32-bit or 64-bit platforms respectively. The only difference between 32-bit and 64-bit is whether the _WIN64 preprocessor symbol is defined.</p>
<dt><i></i><code>&#8211;nostdinc</code></p>
<dd> Do not search the standard include path, look for include files only in the directories explicitly specified with the <code>-I</code> option.</p>
<dt><i></i><code>&#8211;no-use-temp-file</code></p>
<dd> Ignored for compatibility with <i>windres</i>.</p>
<dt><i></i><code>-o</code>, <code>-fo</code>, <code>&#8211;output</code>=<i>file</i></p>
<dd> Write output to <i>file</i>. Default is <code>inputfile.res</code> with <code>.rc</code> stripped or <code>wrc.tab.res</code> if input is read from standard input.</p>
<dt><i></i><code>-O</code>, <code>&#8211;output-format</code>=<i>format</i></p>
<dd> Sets the output format. The supported formats are <code>po</code>, <code>pot</code>, <code>res</code>, and <code>res16</code>. If this option is not specified, the format defaults to <code>res</code>.<br />
 In <code>po</code> mode, if an output file name is specified it must match a known language name, like <code>en_US.po</code>; only resources for the specified language are output. If no output file name is specified, a separate <i>.po</i> file is created for every language encountered in the input.</p>
<dt><i></i><code>&#8211;pedantic</code></p>
<dd> Enable pedantic warnings. Notably redefinition of #define statements can be discovered with this option.</p>
<dt><i></i><code>&#8211;po-dir=</code><i>dir</i></p>
<dd> Enable the generation of resource translations based on mo files loaded from the specified directory. That directory must follow the gettext convention, in particular it must contain one <i>.mo</i> file for each language, and a LINGUAS file listing the available languages.</p>
<dt><i></i><code>-r</code></p>
<dd> Ignored for compatibility with <i>rc</i>.</p>
<dt><i></i><code>&#8211;preprocessor</code>=<i>program</i></p>
<dd> This option may be used to specify the preprocessor to use, including any leading arguments. If not specified, <code>wrc</code> uses its builtin processor. To disable preprocessing, use <code>&#8211;preprocessor=cat</code>.</p>
<dt><i></i><code>-U</code>, <code>&#8211;undefine</code>=<i>id</i></p>
<dd> Undefine preprocessor identifier <i>id</i>. Please note that only macros defined up to this point are undefined by this command. However, these include the special macros defined automatically by <i>wrc</i>. See also <code>PREPROCESSOR</code> below.</p>
<dt><i></i><code>&#8211;use-temp-file</code></p>
<dd> Ignored for compatibility with <i>windres</i>.</p>
<dt><i></i><code>-v</code>, <code>&#8211;verbose</code></p>
<dd> Turns on verbose mode (equivalent to <code>-d 1</code>).</p>
<dt><i></i><code>&#8211;version</code></p>
<dd> Print version and exit.</dl>
<h2>PREPROCESSOR</h2>
<p> The preprocessor is ANSI-C compatible with some of the extensions of the gcc preprocessor. </p>
<p> The preprocessor recognizes these directives: #include, #define (both simple and macro), #undef, #if, #ifdef, #ifndef, #elif, #else, #endif, #error, #warning, #line, # (both null- and line-directive), #pragma (ignored), #ident (ignored). </p>
<p> The preprocessor sets by default several defines:<br />
 RC_INVOKED set to 1<br />
 __WRC__ Major version of wrc<br />
 __WRC_MINOR__ Minor version of wrc<br />
 __WRC_PATCHLEVEL__ Patch level </p>
<p> Win32 compilation mode also sets _WIN32 to 1. </p>
<p> Special macros __FILE__, __LINE__, __TIME__ and __DATE__ are also recognized and expand to their respective equivalent.</p>
<h2>LANGUAGE SUPPORT</h2>
<p> Language, version and characteristics can be bound to all resource types that have inline data, such as RCDATA. This is an extension to Microsoft&#8217;s resource compiler, which lacks this support completely. Only VERSIONINFO cannot have version and characteristics attached, but languages are propagated properly if you declare it correctly before the VERSIONINFO resource starts. </p>
<p> Example: </p>
<p> 1 RCDATA DISCARDABLE<br />
 LANGUAGE 1, 0<br />
 VERSION 312<br />
 CHARACTERISTICS 876<br />
 {<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>1, 2, 3, 4, 5, &quot;and whatever more data you want&quot;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>&#8217;00 01 02 03 04 05 06 07 08&#8242;</p>
<p> }</p>
<h2>AUTHORS</h2>
<p> <code>wrc</code> was written by Bertho A. Stultiens and is a nearly complete rewrite of the first wine resource compiler (1994) by Martin von Loewis. Additional resource-types were contributed by Ulrich Czekalla and Albert den Haan. Many cleanups by Dimitrie O. Paun in 2002-2003. Bugfixes have been contributed by many Wine developers.</p>
<h2>BUGS</h2>
<p> &#8211; The preprocessor recognizes variable argument macros, but does not expand them correctly.<br />
 &#8211; Error reporting should be more precise, as currently the column and line number reported are those of the next token.<br />
 &#8211; Default memory options should differ between win16 and win32. </p>
<p> There is no support for:<br />
 &#8211; RT_DLGINCLUDE, RT_VXD, RT_PLUGPLAY and RT_HTML (unknown format)<br />
 &#8211; PUSHBOX control is unsupported due to lack of original functionality. </p>
<p> Fonts are parsed and generated, but there is no support for the generation of the FONTDIR yet. The user must supply the FONTDIR resource in the source to match the FONT resources. </p>
<p> Bugs can be reported on the <code>Wine bug tracker</code></p>
<h2>AVAILABILITY</h2>
<p> <code>wrc</code> is part of the Wine distribution, which is available through WineHQ, the <code>Wine development headquarters</code></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-wine/">wine</a></code>(1),<br />
 <code>Wine documentation and support</code> </p>
<h2>Index</h2>
