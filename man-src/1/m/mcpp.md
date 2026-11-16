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
<dt><code>-$, -fno-dollars-in-identifiers</dt>
<dd> Forbid &#8216;$&#8217; in identifiers.</dd>
<dt>-@MODE</dt>
<dd> Specify preprocessing mode. MODE should be one of these 4:</dd>
<dt> -@std</dt>
<dd> Standard conforming mode. (default)</dd>
<dt> -@poststd, -@post</dt>
<dd> special &#8216;post-Standard&#8217; mode.</dd>
<dt> -@kr</dt>
<dd> K&amp;R 1st mode.</dd>
<dt> -@oldprep, -@old</dt>
<dd> &quot;old_preprocessor&quot; mode (i.e. &quot;Reiser model&quot; cpp).</dd>
<dt> -@compat</dt>
<dd> Standard &#8216;compatible&#8217; mode.</dd>
<dt>-b</dt>
<dd> Output #line lines in C source style (default: GCC style).</dd>
<dt>-C</dt>
<dd> Output also comments.</dd>
<dt>-D &lt;macro&gt;[=&lt;value&gt;]</dt>
<dd> Define &lt;macro&gt; as &lt;value&gt; (default:1).</dd>
<dt>-D &lt;macro(args)&gt;[=&lt;replace&gt;]</dt>
<dd> Define &lt;macro(args)&gt; as &lt;replace&gt;.</dd>
<dt>-dM, -dD</dt>
<dd> Dump all current macro definitions to output stream.</dd>
<dt>-e &lt;encoding&gt;</dt>
<dd> Change the default multi-byte character encoding to one of: euc_jp, gb2312, ksc5601, big5, sjis, iso2022_jp, utf8.</dd>
<dt>-finput-charset=&lt;encoding&gt;</dt>
<dd> Same as -e &lt;encoding&gt;. (Do not insert spaces around &#8216;=&#8217;).</dd>
<dt>-f[no-]working-directory</dt>
<dd> (Don&#8217;t) emit #line marks with current working directory.</dd>
<dt>-fstack-protector[-all]</dt>
<dd> Add defines for GCC stack protector.</dd>
<dt>-f[no-]exceptions</dt>
<dd> (Don&#8217;t) add define for exception support.</dd>
<dt>-fpic, -fPIC, -fpie, -fPIE</dt>
<dd> Add defines for PIC/PIE code.</dd>
<dt>-I &lt;directory&gt;</dt>
<dd> Add &lt;directory&gt; to the #include search list.</dd>
<dt>-I-</dt>
<dd> Unset system or site specific include directories.</dd>
<dt>-include &lt;file&gt;</dt>
<dd> Include the &lt;file&gt; prior to the main input file.</dd>
<dt>-isystem &lt;dir&gt;</dt>
<dd> Look for include files in DIR, if not found in -I&#8217;s.</dd>
<dt>-iquote &lt;dir&gt;</dt>
<dd> Look for #include &quot;file&quot; (with quotes) in DIR.</dd>
<dt>-j</dt>
<dd> Do not output the source line in diagnostics.</dd>
<dt>-k</dt>
<dd> Keep white spaces of input lines as they are.</dd>
<dt>-M, -MM, -MD, -MMD, -MP, -MQ target, -MT target, -MF file</dt>
<dd> Output source file dependency line for makefile.</dd>
<dt>-m32</dt>
<dd> Change target CPU from x86_64, ppc64 to i386, ppc, respectively.</dd>
<dt>-m64</dt>
<dd> Change target CPU from i386, ppc to x86_64, ppc64, respectively.</dd>
<dt>-[no-]mmx</dt>
<dd> (Un-)define __MMX__.</dd>
<dt>-N</dt>
<dd> Don&#8217;t predefine any non-standard macros.</dd>
<dt>-nostdinc</dt>
<dd> Unset system or site specific include directories.</dd>
<dt>-o &lt;file&gt;</dt>
<dd> Output to &lt;file&gt;.</dd>
<dt>-P</dt>
<dd> Don&#8217;t output #line lines.</dd>
<dt>-Q</dt>
<dd> Output diagnostics to &quot;mcpp.err&quot; (default:stderr).</dd>
<dt>-U &lt;macro&gt;</dt>
<dd> Undefine &lt;macro&gt;.</dd>
<dt>-undef</dt>
<dd> Same as -N.</dd>
<dt>-v</dt>
<dd> Show version of mcpp</code>.</dd>
<dt><code>-W &lt;level&gt;</dt>
<dd> Set warning level to &lt;level&gt; (OR of {0,1,2,4,8,16}, default:1).</dd>
<dt>-w</dt>
<dd> Same as -W0.</dd>
<dt>-z</dt>
<dd> Don&#8217;t output the included file, only defining macros.</dd></dl>
<p> Options available with -@std (default) or -@poststd options:</p>
<dl>
<dt>-+</dt>
<dd> Process C++ source.</dd>
<dt>-2</dt>
<dd> Enable digraphs.</dd>
<dt>-digraphs</dt>
<dd> Enable digraphs.</dd>
<dt>-h &lt;n&gt;</dt>
<dd> Re-define the pre-defined macro __STDC_HOSTED__ as &lt;n&gt;.</dd>
<dt>-lang-c89</dt>
<dd> Same as -S1.</dd>
<dt>-lang-c99, -lang-c9x</dt>
<dd> Same as -S199901L.</dd>
<dt>-lang-c++</dt>
<dd> Same as -+.</dd>
<dt>-lang-asm</dt>
<dd> Same as -a.</dd>
<dt>-pedantic, -pedantic-errors</dt>
<dd> Same as -W7.</dd>
<dt>-S &lt;n&gt;</dt>
<dd> Redefine __STDC__ to &lt;n&gt;, undefine old style macros.</dd>
<dt>-std=&lt;STANDARD&gt;</dt>
<dd> Specify the standard to which the code should conform. &lt;STANDARD&gt; may be one of: c90, c99, iso9899:1990, iso14882, etc.<br />
 iso9899:&lt;n&gt;, iso14882:&lt;n&gt; : Same as -V &lt;n&gt; (long in decimals).</dd>
<dt>-V &lt;n&gt;</dt>
<dd> Redefine __STDC_VERSION__ or __cplusplus to &lt;n&gt;.<br />
 C with -V199901L specifies C99 mode.<br />
 C++ with -V199901L specifies C99 compatible mode.</dd>
<dt>-x c++</dt>
<dd> Same as -+.</dd></dl>
<p> Options available with only -@std (default) option:</p>
<dl>
<dt>-@compat</dt>
<dd> Expand recursive macro more than Standard.</dd>
<dt>-3</dt>
<dd> Enable trigraphs.</dd>
<dt>-trigraphs</dt>
<dd> Enable trigraphs.</dd>
<dt>-K</dt>
<dd> Embed macro annotations into comments.</dd></dl>
<p> Options available with -@std (default), -@kr or -@oldprep options:</p>
<dl>
<dt>-lang-asm</dt>
<dd> Same as -x assembler-with-cpp.</dd>
<dt>-x assembler-with-cpp</dt>
<dd> Process &quot;assembler&quot; source.</dd></dl>
<p> Option available on Mac OS X / Apple-GCC:</p>
<dl>
<dt>-arch &lt;arch&gt;</dt>
<dd> Change the target to &lt;arch&gt; (one of i386, x86_64, ppc and ppc64).</dd></dl>
<p> Option available on CygWIN:</p>
<dl>
<dt>-mno-cygwin</dt>
<dd> Change include directory and predefined macros for msvcrt.dll rather than cygwin1.dll.</dd></dl>
<p> </code></p>
<h2>PRAGMA</h2>
<p> <code>mcpp</code> has the following #pragma directives.</p>
<dl>
<dt>#pragma once</dt>
<dd> Read the header file only once even if multiply #included.</dd>
<dt>#pragma __setlocale( &quot;encoding&quot;)</dt>
<dd> Specify the multibyte character encoding to &quot;encoding&quot;. See -e option for the encodings.</dd>
<dt>#pragma MCPP put_defines</dt>
<dd> Putout all the macro definitions currently valid.</dd>
<dt>#pragma MCPP debug &lt;args&gt;</dt>
<dd> Start to putout debugging informations.<br />
&nbsp;<wbr>&lt;args&gt;&nbsp;<wbr>should be one or more of:<br />
&nbsp;<wbr>token expand macro_call path if expression memory getc</dd>
<dt>#pragma MCPP end_debug &lt;args&gt;</dt>
<dd> Stop to putout debugging informations.<br />
&nbsp;<wbr>&lt;args&gt;&nbsp;<wbr>are the same with&nbsp;<wbr>&#8216;debug&#8217;.<br />
&nbsp;<wbr>No argument specifies all arguments.</dd>
<dt>#pragma MCPP push_macro( &quot;MACRO&quot;)</dt>
<dd> Save the macro definition to the stack.</dd>
<dt>#pragma MCPP pop_macro( &quot;MACRO&quot;)</dt>
<dd> Retrieve the macro definition from the stack.</dd>
<dt>#pragma MCPP preprocess</dt>
<dd> &quot;Pre-preprocess&quot; the following header files for <code>mcpp</code>.</dd>
<dt>#pragma MCPP warning any message</dt>
<dd> Putout warning &quot;any message&quot;.</dd></dl>
<h2>VERSION</h2>
<p> MCPP V.2.7 (2008/03) for GCC</p>
<h2>SEE ALSO</h2>
<p> The full documentation for <code>mcpp</code> are maintained as html files. Please see mcpp-manual.html. </p>
<h2>Index</h2>
