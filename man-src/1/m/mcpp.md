---
title: "mcpp(1)"
name: "mcpp"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mcpp/"
description: "mcpp – Matsui CPP, an alternative C preprocessor"
---

<h2>NAME</h2>
<p> mcpp &#8211; Matsui CPP, an alternative C preprocessor</p>
<h2>SYNOPSIS</h2>
<p> mcpp [<i>options</i>] [<i>&lt;infile&gt;</i> [<i>&lt;outfile&gt;</i>]]</p>
<h2>DESCRIPTION</h2>
<p> <code>mcpp</code> is a C/C++ preprocessor with the highest conformance which implements C90, C99 and C++98. <code>mcpp</code> has plentiful diagnostics and many #pragmas. It is useful to check portability of your program, and also useful to debug complicated macro. This is a man-page for <code>mcpp</code> of GCC-specific-build.</p>
<h2>OPTIONS</h2>
<p> <code>mcpp</code> expects two file names as arguments, <i>&lt;infile&gt;</i> and <i>&lt;outfile&gt;</i>. If not specified, <i>&lt;infile&gt;</i> defaults to standard input and <i>&lt;outfile&gt;</i> defaults to standard output. </p>
<p> It takes the following options. </p>
<p> Commonly used options:</p>
<dl>
<dt><code>-$, -fno-dollars-in-identifiers</p>
<dd> Forbid &#8216;$&#8217; in identifiers.</p>
<dt>-@MODE</p>
<dd> Specify preprocessing mode. MODE should be one of these 4:</p>
<dt> -@std</p>
<dd> Standard conforming mode. (default)</p>
<dt> -@poststd, -@post</p>
<dd> special &#8216;post-Standard&#8217; mode.</p>
<dt> -@kr</p>
<dd> K&amp;R 1st mode.</p>
<dt> -@oldprep, -@old</p>
<dd> &quot;old_preprocessor&quot; mode (i.e. &quot;Reiser model&quot; cpp).</p>
<dt> -@compat</p>
<dd> Standard &#8216;compatible&#8217; mode.</p>
<dt>-b</p>
<dd> Output #line lines in C source style (default: GCC style).</p>
<dt>-C</p>
<dd> Output also comments.</p>
<dt>-D &lt;macro&gt;[=&lt;value&gt;]</p>
<dd> Define &lt;macro&gt; as &lt;value&gt; (default:1).</p>
<dt>-D &lt;macro(args)&gt;[=&lt;replace&gt;]</p>
<dd> Define &lt;macro(args)&gt; as &lt;replace&gt;.</p>
<dt>-dM, -dD</p>
<dd> Dump all current macro definitions to output stream.</p>
<dt>-e &lt;encoding&gt;</p>
<dd> Change the default multi-byte character encoding to one of: euc_jp, gb2312, ksc5601, big5, sjis, iso2022_jp, utf8.</p>
<dt>-finput-charset=&lt;encoding&gt;</p>
<dd> Same as -e &lt;encoding&gt;. (Do not insert spaces around &#8216;=&#8217;).</p>
<dt>-f[no-]working-directory</p>
<dd> (Don&#8217;t) emit #line marks with current working directory.</p>
<dt>-fstack-protector[-all]</p>
<dd> Add defines for GCC stack protector.</p>
<dt>-f[no-]exceptions</p>
<dd> (Don&#8217;t) add define for exception support.</p>
<dt>-fpic, -fPIC, -fpie, -fPIE</p>
<dd> Add defines for PIC/PIE code.</p>
<dt>-I &lt;directory&gt;</p>
<dd> Add &lt;directory&gt; to the #include search list.</p>
<dt>-I-</p>
<dd> Unset system or site specific include directories.</p>
<dt>-include &lt;file&gt;</p>
<dd> Include the &lt;file&gt; prior to the main input file.</p>
<dt>-isystem &lt;dir&gt;</p>
<dd> Look for include files in DIR, if not found in -I&#8217;s.</p>
<dt>-iquote &lt;dir&gt;</p>
<dd> Look for #include &quot;file&quot; (with quotes) in DIR.</p>
<dt>-j</p>
<dd> Do not output the source line in diagnostics.</p>
<dt>-k</p>
<dd> Keep white spaces of input lines as they are.</p>
<dt>-M, -MM, -MD, -MMD, -MP, -MQ target, -MT target, -MF file</p>
<dd> Output source file dependency line for makefile.</p>
<dt>-m32</p>
<dd> Change target CPU from x86_64, ppc64 to i386, ppc, respectively.</p>
<dt>-m64</p>
<dd> Change target CPU from i386, ppc to x86_64, ppc64, respectively.</p>
<dt>-[no-]mmx</p>
<dd> (Un-)define __MMX__.</p>
<dt>-N</p>
<dd> Don&#8217;t predefine any non-standard macros.</p>
<dt>-nostdinc</p>
<dd> Unset system or site specific include directories.</p>
<dt>-o &lt;file&gt;</p>
<dd> Output to &lt;file&gt;.</p>
<dt>-P</p>
<dd> Don&#8217;t output #line lines.</p>
<dt>-Q</p>
<dd> Output diagnostics to &quot;mcpp.err&quot; (default:stderr).</p>
<dt>-U &lt;macro&gt;</p>
<dd> Undefine &lt;macro&gt;.</p>
<dt>-undef</p>
<dd> Same as -N.</p>
<dt>-v</p>
<dd> Show version of mcpp</code>.</p>
<dt><code>-W &lt;level&gt;</p>
<dd> Set warning level to &lt;level&gt; (OR of {0,1,2,4,8,16}, default:1).</p>
<dt>-w</p>
<dd> Same as -W0.</p>
<dt>-z</p>
<dd> Don&#8217;t output the included file, only defining macros.</dl>
<p> Options available with -@std (default) or -@poststd options:</p>
<dl>
<dt>-+</p>
<dd> Process C++ source.</p>
<dt>-2</p>
<dd> Enable digraphs.</p>
<dt>-digraphs</p>
<dd> Enable digraphs.</p>
<dt>-h &lt;n&gt;</p>
<dd> Re-define the pre-defined macro __STDC_HOSTED__ as &lt;n&gt;.</p>
<dt>-lang-c89</p>
<dd> Same as -S1.</p>
<dt>-lang-c99, -lang-c9x</p>
<dd> Same as -S199901L.</p>
<dt>-lang-c++</p>
<dd> Same as -+.</p>
<dt>-lang-asm</p>
<dd> Same as -a.</p>
<dt>-pedantic, -pedantic-errors</p>
<dd> Same as -W7.</p>
<dt>-S &lt;n&gt;</p>
<dd> Redefine __STDC__ to &lt;n&gt;, undefine old style macros.</p>
<dt>-std=&lt;STANDARD&gt;</p>
<dd> Specify the standard to which the code should conform. &lt;STANDARD&gt; may be one of: c90, c99, iso9899:1990, iso14882, etc.<br />
 iso9899:&lt;n&gt;, iso14882:&lt;n&gt; : Same as -V &lt;n&gt; (long in decimals).</p>
<dt>-V &lt;n&gt;</p>
<dd> Redefine __STDC_VERSION__ or __cplusplus to &lt;n&gt;.<br />
 C with -V199901L specifies C99 mode.<br />
 C++ with -V199901L specifies C99 compatible mode.</p>
<dt>-x c++</p>
<dd> Same as -+.</dl>
<p> Options available with only -@std (default) option:</p>
<dl>
<dt>-@compat</p>
<dd> Expand recursive macro more than Standard.</p>
<dt>-3</p>
<dd> Enable trigraphs.</p>
<dt>-trigraphs</p>
<dd> Enable trigraphs.</p>
<dt>-K</p>
<dd> Embed macro annotations into comments.</dl>
<p> Options available with -@std (default), -@kr or -@oldprep options:</p>
<dl>
<dt>-lang-asm</p>
<dd> Same as -x assembler-with-cpp.</p>
<dt>-x assembler-with-cpp</p>
<dd> Process &quot;assembler&quot; source.</dl>
<p> Option available on Mac OS X / Apple-GCC:</p>
<dl>
<dt>-arch &lt;arch&gt;</p>
<dd> Change the target to &lt;arch&gt; (one of i386, x86_64, ppc and ppc64).</dl>
<p> Option available on CygWIN:</p>
<dl>
<dt>-mno-cygwin</p>
<dd> Change include directory and predefined macros for msvcrt.dll rather than cygwin1.dll.</dl>
<p> </code></p>
<h2>PRAGMA</h2>
<p> <code>mcpp</code> has the following #pragma directives.</p>
<dl>
<dt>#pragma once</p>
<dd> Read the header file only once even if multiply #included.</p>
<dt>#pragma __setlocale( &quot;encoding&quot;)</p>
<dd> Specify the multibyte character encoding to &quot;encoding&quot;. See -e option for the encodings.</p>
<dt>#pragma MCPP put_defines</p>
<dd> Putout all the macro definitions currently valid.</p>
<dt>#pragma MCPP debug &lt;args&gt;</p>
<dd> Start to putout debugging informations.<br />
&nbsp;<wbr>&lt;args&gt;&nbsp;<wbr>should be one or more of:<br />
&nbsp;<wbr>token expand macro_call path if expression memory getc</p>
<dt>#pragma MCPP end_debug &lt;args&gt;</p>
<dd> Stop to putout debugging informations.<br />
&nbsp;<wbr>&lt;args&gt;&nbsp;<wbr>are the same with&nbsp;<wbr>&#8216;debug&#8217;.<br />
&nbsp;<wbr>No argument specifies all arguments.</p>
<dt>#pragma MCPP push_macro( &quot;MACRO&quot;)</p>
<dd> Save the macro definition to the stack.</p>
<dt>#pragma MCPP pop_macro( &quot;MACRO&quot;)</p>
<dd> Retrieve the macro definition from the stack.</p>
<dt>#pragma MCPP preprocess</p>
<dd> &quot;Pre-preprocess&quot; the following header files for <code>mcpp</code>.</p>
<dt>#pragma MCPP warning any message</p>
<dd> Putout warning &quot;any message&quot;.</dl>
<h2>VERSION</h2>
<p> MCPP V.2.7 (2008/03) for GCC</p>
<h2>SEE ALSO</h2>
<p> The full documentation for <code>mcpp</code> are maintained as html files. Please see mcpp-manual.html. </p>
<h2>Index</h2>
