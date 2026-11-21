---
title: "gfortran44(1)"
name: "gfortran44"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gfortran44/"
description: "gfortran – GNU Fortran compiler"
---
<h2>SYNOPSIS</h2>
<p> gfortran [<code>-c</code>|<code>-S</code>|<code>-E</code>] <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[<code>-g</code>]&nbsp;<wbr>[<code>-pg</code>]&nbsp;<wbr>[<code>-O</code><i>level</i>] <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[<code>-W</code><i>warn</i>...]&nbsp;<wbr>[<code>-pedantic</code>] <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[<code>-I</code><i>dir</i>...]&nbsp;<wbr>[<code>-L</code><i>dir</i>...] <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[<code>-D</code><i>macro</i>[=<i>defn</i>]...]&nbsp;<wbr>[<code>-U</code><i>macro</i>] <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[<code>-f</code><i>option</i>...] <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[<code>-m</code><i>machine-option</i>...] <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[<code>-o</code>&nbsp;<wbr><i>outfile</i>]&nbsp;<wbr><i>infile</i>... </p>
<p> Only the most useful options are listed here; see below for the remainder.  </p>
<h2>DESCRIPTION</h2>
<p> The <code>gfortran</code> command supports all the options supported by the <code>gcc</code> command. Only options specific to <font SIZE="-1">GNU</font> Fortran are documented here. </p>
<p> All <font SIZE="-1">GCC</font> and <font SIZE="-1">GNU</font> Fortran options are accepted both by <code>gfortran</code> and by <code>gcc</code> (as well as any other drivers built at the same time, such as <code>g++</code>), since adding <font SIZE="-1">GNU</font> Fortran to the <font SIZE="-1">GCC</font> distribution enables acceptance of <font SIZE="-1">GNU</font> Fortran options by all of the relevant drivers. </p>
<p> In some cases, options have positive and negative forms; the negative form of <code>-ffoo</code> would be <code>-fno-foo</code>. This manual documents only one of these two forms, whichever one is not the default.  </p>
<h2>OPTIONS</h2>
<p> Here is a summary of all the options specific to <font SIZE="-1">GNU</font> Fortran, grouped by type. Explanations are in the following sections. </p>
<dl>
<dt><i>Fortran Language Options</i></dt>
<dd> <p> <code>-fall-intrinsics -ffree-form -fno-fixed-form -fdollar-ok -fimplicit-none -fmax-identifier-length -std=</code><i>std</i> <code>-fd-lines-as-code -fd-lines-as-comments -ffixed-line-length-</code><i>n</i> <code>-ffixed-line-length-none -ffree-line-length-</code><i>n</i> <code>-ffree-line-length-none -fdefault-double-8 -fdefault-integer-8 -fdefault-real-8 -fcray-pointer -fopenmp -fno-range-check -fbackslash -fmodule-private</code> </p>
 </dd>
<dt><i>Preprocessing Options</i></dt>
<dd> <p> <code>-cpp -dD -dI -dM -dN -dU -fworking-directory -imultilib</code> <i>dir</i> <code>-iprefix</code> <i>file</i> <code>-isysroot</code> <i>dir</i> <code>-iquote -isystem</code> <i>dir</i> <code>-nocpp -nostdinc -undef -A</code><i>question</i><code>=</code><i>answer</i> <code>-A-</code><i>question</i>[<code>=</code><i>answer</i>] <code>-C -CC -D</code><i>macro</i>[<code>=</code><i>defn</i>] <code>-U</code><i>macro</i> <code>-H -P</code> </p>
 </dd>
<dt><i>Error and Warning Options</i></dt>
<dd> <p> <code>-fmax-errors=</code><i>n</i> <code>-fsyntax-only -pedantic -pedantic-errors -Wall -Waliasing -Wampersand -Warray-bounds -Wcharacter-truncation -Wconversion -Wimplicit-interface -Wline-truncation -Wintrinsics-std -Wsurprising -Wno-tabs -Wunderflow -Wunused-parameter -Wintrinsics-shadow -Wno-align-commons</code> </p>
 </dd>
<dt><i>Debugging Options</i></dt>
<dd> <p> <code>-fdump-parse-tree -ffpe-trap=</code><i>list</i> <code>-fdump-core -fbacktrace</code> </p>
 </dd>
<dt><i>Directory Options</i></dt>
<dd> <p> <code>-I</code><i>dir</i> <code>-J</code><i>dir</i> <code>-fintrinsic-modules-path</code> <i>dir</i> </p>
 </dd>
<dt><i>Link Options</i></dt>
<dd> <p> <code>-static-libgfortran</code> </p>
 </dd>
<dt><i>Runtime Options</i></dt>
<dd> <p> <code>-fconvert=</code><i>conversion</i> <code>-fno-range-check -frecord-marker=</code><i>length</i> <code>-fmax-subrecord-length=</code><i>length</i> <code>-fsign-zero</code> </p>
 </dd>
<dt><i>Code Generation Options</i></dt>
<dd> <p> <code>-fno-automatic -ff2c -fno-underscoring -fsecond-underscore -fbounds-check -fcheck-array-temporaries -fmax-array-constructor =</code><i>n</i> <code>-fmax-stack-var-size=</code><i>n</i> <code>-fpack-derived -frepack-arrays -fshort-enums -fexternal-blas -fblas-matmul-limit=</code><i>n</i> <code>-frecursive -finit-local-zero -finit-integer=</code><i>n</i> <code>-finit-real=</code><i>&lt;zero|inf|-inf|nan&gt;</i> <code>-finit-logical=</code><i>&lt;true|false&gt;</i> <code>-finit-character=</code><i>n</i> <code>-fno-align-commons</code> </p>
 </dd></dl>
<h3>Options controlling Fortran dialect</h3>
<p> The following options control the details of the Fortran dialect accepted by the compiler: </p>
<dl>
<dt><code>-ffree-form</code></dt>
<dd>  </dd>
<dt><code>-ffixed-form</code></dt>
<dd> <p> Specify the layout used by the source file. The free form layout was introduced in Fortran 90. Fixed form was traditionally used in older Fortran programs. When neither option is specified, the source form is determined by the file extension. </p>
 </dd>
<dt><code>-fall-intrinsics</code></dt>
<dd> <p> This option causes all intrinsic procedures (including the GNU-specific extensions) to be accepted. This can be useful with <code>-std=f95</code> to force standard-compliance but get access to the full range of intrinsics available with <code>gfortran</code>. As a consequence, <code>-Wintrinsics-std</code> will be ignored and no user-defined procedure with the same name as any intrinsic will be called except when it is explicitly declared <code>&quot;EXTERNAL&quot;</code>. </p>
 </dd>
<dt><code>-fd-lines-as-code</code></dt>
<dd>  </dd>
<dt><code>-fd-lines-as-comments</code></dt>
<dd> <p> Enable special treatment for lines beginning with <code>&quot;d&quot;</code> or <code>&quot;D&quot;</code> in fixed form sources. If the <code>-fd-lines-as-code</code> option is given they are treated as if the first column contained a blank. If the <code>-fd-lines-as-comments</code> option is given, they are treated as comment lines. </p>
 </dd>
<dt><code>-fdefault-double-8</code></dt>
<dd> <p> Set the <code>&quot;DOUBLE PRECISION&quot;</code> type to an 8 byte wide type. If <code>-fdefault-real-8</code> is given, <code>&quot;DOUBLE PRECISION&quot;</code> would instead be promoted to 16 bytes if possible, and <code>-fdefault-double-8</code> can be used to prevent this. The kind of real constants like <code>&quot;1.d0&quot;</code> will not be changed by <code>-fdefault-real-8</code> though, so also <code>-fdefault-double-8</code> does not affect it. </p>
 </dd>
<dt><code>-fdefault-integer-8</code></dt>
<dd> <p> Set the default integer and logical types to an 8 byte wide type. Do nothing if this is already the default. This option also affects the kind of integer constants like <code>42</code>. </p>
 </dd>
<dt><code>-fdefault-real-8</code></dt>
<dd> <p> Set the default real type to an 8 byte wide type. Do nothing if this is already the default. This option also affects the kind of non-double real constants like <code>1.0</code>, and does promote the default width of <code>&quot;DOUBLE PRECISION&quot;</code> to 16 bytes if possible, unless <code>&quot;-fdefault-double-8&quot;</code> is given, too. </p>
 </dd>
<dt><code>-fdollar-ok</code></dt>
<dd> <p> Allow <code>$</code> as a valid character in a symbol name. </p>
 </dd>
<dt><code>-fbackslash</code></dt>
<dd> <p> Change the interpretation of backslashes in string literals from a single backslash character to ``C-style&#8217;&#8216; escape characters. The following combinations are expanded <code>&quot;\a&quot;</code>, <code>&quot;\b&quot;</code>, <code>&quot;\f&quot;</code>, <code>&quot;\n&quot;</code>, <code>&quot;\r&quot;</code>, <code>&quot;\t&quot;</code>, <code>&quot;\v&quot;</code>, <code>&quot;\\&quot;</code>, and <code>&quot;\0&quot;</code> to the <font SIZE="-1">ASCII</font> characters alert, backspace, form feed, newline, carriage return, horizontal tab, vertical tab, backslash, and <font SIZE="-1">NUL,</font> respectively. Additionally, <code>&quot;\x&quot;</code><i>nn</i>, <code>&quot;\u&quot;</code><i>nnnn</i> and <code>&quot;\U&quot;</code><i>nnnnnnnn</i> (where each <i>n</i> is a hexadecimal digit) are translated into the Unicode characters corresponding to the specified code points. All other combinations of a character preceded by \ are unexpanded. </p>
 </dd>
<dt><code>-fmodule-private</code></dt>
<dd> <p> Set the default accessibility of module entities to <code>&quot;PRIVATE&quot;</code>. Use-associated entities will not be accessible unless they are explicitly declared as <code>&quot;PUBLIC&quot;</code>. </p>
 </dd>
<dt><code>-ffixed-line-length-</code><i>n</i></dt>
<dd> <p> Set column after which characters are ignored in typical fixed-form lines in the source file, and through which spaces are assumed (as if padded to that length) after the ends of short fixed-form lines. </p>
<p> Popular values for <i>n</i> include 72 (the standard and the default), 80 (card image), and 132 (corresponding to ``extended-source&#8217;&#8216; options in some popular compilers). <i>n</i> may also be <code>none</code>, meaning that the entire line is meaningful and that continued character constants never have implicit spaces appended to them to fill out the line. <code>-ffixed-line-length-0</code> means the same thing as <code>-ffixed-line-length-none</code>. </p>
 </dd>
<dt><code>-ffree-line-length-</code><i>n</i></dt>
<dd> <p> Set column after which characters are ignored in typical free-form lines in the source file. The default value is 132. <i>n</i> may be <code>none</code>, meaning that the entire line is meaningful. <code>-ffree-line-length-0</code> means the same thing as <code>-ffree-line-length-none</code>. </p>
 </dd>
<dt><code>-fmax-identifier-length=</code><i>n</i></dt>
<dd> <p> Specify the maximum allowed identifier length. Typical values are 31 (Fortran 95) and 63 (Fortran 2003 and Fortran 2008). </p>
 </dd>
<dt><code>-fimplicit-none</code></dt>
<dd> <p> Specify that no implicit typing is allowed, unless overridden by explicit <code>&quot;IMPLICIT&quot;</code> statements. This is the equivalent of adding <code>&quot;implicit none&quot;</code> to the start of every procedure. </p>
 </dd>
<dt><code>-fcray-pointer</code></dt>
<dd> <p> Enable the Cray pointer extension, which provides C-like pointer functionality. </p>
 </dd>
<dt><code>-fopenmp</code></dt>
<dd> <p> Enable the OpenMP extensions. This includes OpenMP <code>&quot;!$omp&quot;</code> directives in free form and <code>&quot;c$omp&quot;</code>, <code>*$omp</code> and <code>&quot;!$omp&quot;</code> directives in fixed form, <code>&quot;!$&quot;</code> conditional compilation sentinels in free form and <code>&quot;c$&quot;</code>, <code>&quot;*$&quot;</code> and <code>&quot;!$&quot;</code> sentinels in fixed form, and when linking arranges for the OpenMP runtime library to be linked in. The option <code>-fopenmp</code> implies <code>-frecursive</code>. </p>
 </dd>
<dt><code>-fno-range-check</code></dt>
<dd> <p> Disable range checking on results of simplification of constant expressions during compilation. For example, <font SIZE="-1">GNU</font> Fortran will give an error at compile time when simplifying <code>&quot;a = 1. / 0&quot;</code>. With this option, no error will be given and <code>&quot;a&quot;</code> will be assigned the value <code>&quot;+Infinity&quot;</code>. If an expression evaluates to a value outside of the relevant range of [<code>&quot;-HUGE()&quot;</code>:<code>&quot;HUGE()&quot;</code>], then the expression will be replaced by <code>&quot;-Inf&quot;</code> or <code>&quot;+Inf&quot;</code> as appropriate. Similarly, <code>&quot;DATA i/Z&#8217;FFFFFFFF&#8217;/&quot;</code> will result in an integer overflow on most systems, but with <code>-fno-range-check</code> the value will ``wrap around&#8217;&#8216; and <code>&quot;i&quot;</code> will be initialized to -1 instead. </p>
 </dd>
<dt><code>-std=</code><i>std</i></dt>
<dd> <p> Specify the standard to which the program is expected to conform, which may be one of <code>f95</code>, <code>f2003</code>, <code>f2008</code>, <code>gnu</code>, or <code>legacy</code>. The default value for <i>std</i> is <code>gnu</code>, which specifies a superset of the Fortran 95 standard that includes all of the extensions supported by <font SIZE="-1">GNU</font> Fortran, although warnings will be given for obsolete extensions not recommended for use in new code. The <code>legacy</code> value is equivalent but without the warnings for obsolete extensions, and may be useful for old non-standard programs. The <code>f95</code>, <code>f2003</code> and <code>f2008</code> values specify strict conformance to the Fortran 95, Fortran 2003 and Fortran 2008 standards, respectively; errors are given for all extensions beyond the relevant language standard, and warnings are given for the Fortran 77 features that are permitted but obsolescent in later standards. </p>
 </dd></dl>
<h3>Enable and customize preprocessing</h3>
<p> Preprocessor related options. See section <code>Preprocessing and conditional compilation</code> for more detailed information on preprocessing in <code>gfortran</code>. </p>
<dl>
<dt><code>-cpp</code></dt>
<dd>  </dd>
<dt><code>-nocpp</code></dt>
<dd> <p> Enable preprocessing. The preprocessor is automatically invoked if the file extension is <i>.fpp</i>, <i>.FPP</i>, <i>.F</i>, <i>.FOR</i>, <i>.FTN</i>, <i>.F90</i>, <i>.F95</i>, <i>.F03</i> or <i>.F08</i>. Use this option to manually enable preprocessing of any kind of Fortran file. </p>
<p> To disable preprocessing of files with any of the above listed extensions, use the negative form: <code>-nocpp</code>. </p>
<p> The preprocessor is run in traditional mode, be aware that any restrictions of the file-format, e.g. fixed-form line width, apply for preprocessed output as well. </p>
 </dd>
<dt><code>-dM</code></dt>
<dd> <p> Instead of the normal output, generate a list of <code>&#8216;#define&#8217;</code> directives for all the macros defined during the execution of the preprocessor, including predefined macros. This gives you a way of finding out what is predefined in your version of the preprocessor. Assuming you have no file <i>foo.f90</i>, the command </p>
<pre><code>          touch foo.f90; gfortran -cpp -dM foo.f90
</code></pre>
<p> will show all the predefined macros. </p>
 </dd>
<dt><code>-dD</code></dt>
<dd> <p> Like <code>-dM</code> except in two respects: it does not include the predefined macros, and it outputs both the <code>&quot;#define&quot;</code> directives and the result of preprocessing. Both kinds of output go to the standard output file. </p>
 </dd>
<dt><code>-dN</code></dt>
<dd> <p> Like <code>-dD</code>, but emit only the macro names, not their expansions. </p>
 </dd>
<dt><code>-dU</code></dt>
<dd> <p> Like <code>dD</code> except that only macros that are expanded, or whose definedness is tested in preprocessor directives, are output; the output is delayed until the use or test of the macro; and <code>&#8216;#undef&#8217;</code> directives are also output for macros tested but undefined at the time. </p>
 </dd>
<dt><code>-dI</code></dt>
<dd> <p> Output <code>&#8216;#include&#8217;</code> directives in addition to the result of preprocessing. </p>
 </dd>
<dt><code>-fworking-directory</code></dt>
<dd> <p> Enable generation of linemarkers in the preprocessor output that will let the compiler know the current working directory at the time of preprocessing. When this option is enabled, the preprocessor will emit, after the initial linemarker, a second linemarker with the current working directory followed by two slashes. <font SIZE="-1">GCC</font> will use this directory, when it&#8217;s present in the preprocessed input, as the directory emitted as the current working directory in some debugging information formats. This option is implicitly enabled if debugging information is enabled, but this can be inhibited with the negated form <code>-fno-working-directory</code>. If the <code>-P</code> flag is present in the command line, this option has no effect, since no <code>&quot;#line&quot;</code> directives are emitted whatsoever. </p>
 </dd>
<dt><code>-idirafter</code><i>dir</i></dt>
<dd> <p> Search <i>dir</i> for include files, but do it after all directories specified with <code>-I</code> and the standard system directories have been exhausted. <i>dir</i> is treated as a system include directory. If dir begins with <code>&quot;=&quot;</code>, then the <code>&quot;=&quot;</code> will be replaced by the sysroot prefix; see <code>--sysroot</code> and <code>-isysroot</code>. </p>
 </dd>
<dt><code>-imultilib</code><i>dir</i></dt>
<dd> <p> Use <i>dir</i> as a subdirectory of the directory containing target-specific C<font SIZE="-2">++</font> headers. </p>
 </dd>
<dt><code>-iprefix</code><i>prefix</i></dt>
<dd> <p> Specify <i>prefix</i> as the prefix for subsequent <code>-iwithprefix</code> options. If the <i>prefix</i> represents a directory, you should include the final <code>&#8216;/&#8216;</code>. </p>
 </dd>
<dt><code>-isysroot</code><i>dir</i></dt>
<dd> <p> This option is like the <code>--sysroot</code> option, but applies only to header files. See the <code>--sysroot</code> option for more information. </p>
 </dd>
<dt><code>-iquote</code><i>dir</i></dt>
<dd> <p> Search <i>dir</i> only for header files requested with <code>&quot;#include &quot;file&quot;&quot;</code>; they are not searched for <code>&quot;#include &lt;file&gt;&quot;</code>, before all directories specified by <code>-I</code> and before the standard system directories. If <i>dir</i> begins with <code>&quot;=&quot;</code>, then the <code>&quot;=&quot;</code> will be replaced by the sysroot prefix; see <code>--sysroot</code> and <code>-isysroot</code>. </p>
 </dd>
<dt><code>-isystem</code><i>dir</i></dt>
<dd> <p> Search <i>dir</i> for header files, after all directories specified by <code>-I</code> but before the standard system directories. Mark it as a system directory, so that it gets the same special treatment as is applied to the standard system directories. If <i>dir</i> begins with <code>&quot;=&quot;</code>, then the <code>&quot;=&quot;</code> will be replaced by the sysroot prefix; see <code>--sysroot</code> and <code>-isysroot</code>. </p>
 </dd>
<dt><code>-nostdinc</code></dt>
<dd> <p> Do not search the standard system directories for header files. Only the directories you have specified with <code>-I</code> options (and the directory of the current file, if appropriate) are searched. </p>
 </dd>
<dt><code>-undef</code></dt>
<dd> <p> Do not predefine any system-specific or GCC-specific macros. The standard predefined macros remain defined. </p>
 </dd>
<dt><code>-A</code><i>predicate</i><code>=</code><i>answer</i></dt>
<dd> <p> Make an assertion with the predicate <i>predicate</i> and answer <i>answer</i>. This form is preferred to the older form -A predicate(answer), which is still supported, because it does not use shell special characters. </p>
 </dd>
<dt><code>-A-</code><i>predicate</i><code>=</code><i>answer</i></dt>
<dd> <p> Cancel an assertion with the predicate <i>predicate</i> and answer <i>answer</i>. </p>
 </dd>
<dt><code>-C</code></dt>
<dd> <p> Do not discard comments. All comments are passed through to the output file, except for comments in processed directives, which are deleted along with the directive. </p>
<p> You should be prepared for side effects when using <code>-C</code>; it causes the preprocessor to treat comments as tokens in their own right. For example, comments appearing at the start of what would be a directive line have the effect of turning that line into an ordinary source line, since the first token on the line is no longer a <code>&#8216;#&#8216;</code>. </p>
<p> Warning: this currently handles C-Style comments only. The preprocessor does not yet recognize Fortran-style comments. </p>
 </dd>
<dt><code>-CC</code></dt>
<dd> <p> Do not discard comments, including during macro expansion. This is like <code>-C</code>, except that comments contained within macros are also passed through to the output file where the macro is expanded. </p>
<p> In addition to the side-effects of the <code>-C</code> option, the <code>-CC</code> option causes all C<font SIZE="-2">++</font>-style comments inside a macro to be converted to C-style comments. This is to prevent later use of that macro from inadvertently commenting out the remainder of the source line. The <code>-CC</code> option is generally used to support lint comments. </p>
<p> Warning: this currently handles C- and C<font SIZE="-2">++</font>-Style comments only. The preprocessor does not yet recognize Fortran-style comments. </p>
 </dd>
<dt><code>-D</code><i>name</i></dt>
<dd> <p> Predefine name as a macro, with definition <code>1</code>. </p>
 </dd>
<dt><code>-D</code><i>name</i><code>=</code><i>definition</i></dt>
<dd> <p> The contents of <i>definition</i> are tokenized and processed as if they appeared during translation phase three in a <code>&#8216;#define&#8217;</code> directive. In particular, the definition will be truncated by embedded newline characters. </p>
<p> If you are invoking the preprocessor from a shell or shell-like program you may need to use the shell&#8217;s quoting syntax to protect characters such as spaces that have a meaning in the shell syntax. </p>
<p> If you wish to define a function-like macro on the command line, write its argument list with surrounding parentheses before the equals sign (if any). Parentheses are meaningful to most shells, so you will need to quote the option. With sh and csh, <code>&quot;-D&#8217;name(args...)=definition&#8217;&quot;</code> works. </p>
<p> <code>-D</code> and <code>-U</code> options are processed in the order they are given on the command line. All -imacros file and -include file options are processed after all -D and -U options. </p>
 </dd>
<dt><code>-H</code></dt>
<dd> <p> Print the name of each header file used, in addition to other normal activities. Each name is indented to show how deep in the <code>&#8216;#include&#8217;</code> stack it is. </p>
 </dd>
<dt><code>-P</code></dt>
<dd> <p> Inhibit generation of linemarkers in the output from the preprocessor. This might be useful when running the preprocessor on something that is not C code, and will be sent to a program which might be confused by the linemarkers. </p>
 </dd>
<dt><code>-U</code><i>name</i></dt>
<dd> <p> Cancel any previous definition of <i>name</i>, either built in or provided with a <code>-D</code> option. </p>
 </dd></dl>
<h3>Options to request or suppress errors and warnings</h3>
<p> Errors are diagnostic messages that report that the <font SIZE="-1">GNU</font> Fortran compiler cannot compile the relevant piece of source code. The compiler will continue to process the program in an attempt to report further errors to aid in debugging, but will not produce any compiled output. </p>
<p> Warnings are diagnostic messages that report constructions which are not inherently erroneous but which are risky or suggest there is likely to be a bug in the program. Unless <code>-Werror</code> is specified, they do not prevent compilation of the program. </p>
<p> You can request many specific warnings with options beginning <code>-W</code>, for example <code>-Wimplicit</code> to request warnings on implicit declarations. Each of these specific warning options also has a negative form beginning <code>-Wno-</code> to turn off warnings; for example, <code>-Wno-implicit</code>. This manual lists only one of the two forms, whichever is not the default. </p>
<p> These options control the amount and kinds of errors and warnings produced by <font SIZE="-1">GNU</font> Fortran: </p>
<dl>
<dt><code>-fmax-errors=</code><i>n</i></dt>
<dd> <p> Limits the maximum number of error messages to <i>n</i>, at which point <font SIZE="-1">GNU</font> Fortran bails out rather than attempting to continue processing the source code. If <i>n</i> is 0, there is no limit on the number of error messages produced. </p>
 </dd>
<dt><code>-fsyntax-only</code></dt>
<dd> <p> Check the code for syntax errors, but don&#8217;t actually compile it. This will generate module files for each module present in the code, but no other output file. </p>
 </dd>
<dt><code>-pedantic</code></dt>
<dd> <p> Issue warnings for uses of extensions to Fortran 95. <code>-pedantic</code> also applies to C-language constructs where they occur in <font SIZE="-1">GNU</font> Fortran source files, such as use of <code>\e</code> in a character constant within a directive like <code>&quot;#include&quot;</code>. </p>
<p> Valid Fortran 95 programs should compile properly with or without this option. However, without this option, certain <font SIZE="-1">GNU</font> extensions and traditional Fortran features are supported as well. With this option, many of them are rejected. </p>
<p> Some users try to use <code>-pedantic</code> to check programs for conformance. They soon find that it does not do quite what they want---it finds some nonstandard practices, but not all. However, improvements to <font SIZE="-1">GNU</font> Fortran in this area are welcome. </p>
<p> This should be used in conjunction with <code>-std=f95</code>, <code>-std=f2003</code> or <code>-std=f2008</code>. </p>
 </dd>
<dt><code>-pedantic-errors</code></dt>
<dd> <p> Like <code>-pedantic</code>, except that errors are produced rather than warnings. </p>
 </dd>
<dt><code>-Wall</code></dt>
<dd> <p> Enables commonly used warning options pertaining to usage that we recommend avoiding and that we believe are easy to avoid. This currently includes <code>-Waliasing</code>, <code>-Wampersand</code>, <code>-Wsurprising</code>, <code>-Wintrinsics-std</code>, <code>-Wno-tabs</code>, <code>-Wintrinsic-shadow</code> and <code>-Wline-truncation</code>. </p>
 </dd>
<dt><code>-Waliasing</code></dt>
<dd> <p> Warn about possible aliasing of dummy arguments. Specifically, it warns if the same actual argument is associated with a dummy argument with <code>&quot;INTENT(IN)&quot;</code> and a dummy argument with <code>&quot;INTENT(OUT)&quot;</code> in a call with an explicit interface. </p>
<p> The following example will trigger the warning. </p>
<pre><code>          interface
            subroutine bar(a,b)
              integer, intent(in) :: a
              integer, intent(out) :: b
            end subroutine
          end interface
          integer :: a
          call bar(a,a)
</code></pre>
 </dd>
<dt><code>-Wampersand</code></dt>
<dd> <p> Warn about missing ampersand in continued character constants. The warning is given with <code>-Wampersand</code>, <code>-pedantic</code>, <code>-std=f95</code>, <code>-std=f2003</code> and <code>-std=f2008</code>. Note: With no ampersand given in a continued character constant, <font SIZE="-1">GNU</font> Fortran assumes continuation at the first non-comment, non-whitespace character after the ampersand that initiated the continuation. </p>
 </dd>
<dt><code>-Warray-temporaries</code></dt>
<dd> <p> Warn about array temporaries generated by the compiler. The information generated by this warning is sometimes useful in optimization, in order to avoid such temporaries. </p>
 </dd>
<dt><code>-Wcharacter-truncation</code></dt>
<dd> <p> Warn when a character assignment will truncate the assigned string. </p>
 </dd>
<dt><code>-Wline-truncation</code></dt>
<dd> <p> Warn when a source code line will be truncated. </p>
 </dd>
<dt><code>-Wconversion</code></dt>
<dd> <p> Warn about implicit conversions between different types. </p>
 </dd>
<dt><code>-Wimplicit-interface</code></dt>
<dd> <p> Warn if a procedure is called without an explicit interface. Note this only checks that an explicit interface is present. It does not check that the declared interfaces are consistent across program units. </p>
 </dd>
<dt><code>-Wintrinsics-std</code></dt>
<dd> <p> Warn if <code>gfortran</code> finds a procedure named like an intrinsic not available in the currently selected standard (with <code>-std</code>) and treats it as <code>&quot;EXTERNAL&quot;</code> procedure because of this. <code>-fall-intrinsics</code> can be used to never trigger this behaviour and always link to the intrinsic regardless of the selected standard. </p>
 </dd>
<dt><code>-Wsurprising</code></dt>
<dd> <p> Produce a warning when ``suspicious&#8217;&#8216; code constructs are encountered. While technically legal these usually indicate that an error has been made. </p>
<p> This currently produces a warning under the following circumstances: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt>&bull;</dt>
<dd> <p> An <font SIZE="-1">INTEGER SELECT</font> construct has a <font SIZE="-1">CASE</font> that can never be matched as its lower value is greater than its upper value. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> A <font SIZE="-1">LOGICAL SELECT</font> construct has three <font SIZE="-1">CASE</font> statements. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> A <font SIZE="-1">TRANSFER</font> specifies a source that is shorter than the destination. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The type of a function result is declared more than once with the same type. If <code>-pedantic</code> or standard-conforming mode is enabled, this is an error. </p>
 </dd></dl>
</dl>
<dl>
<dd>  </dd></dl>
<dt><code>-Wtabs</code></dt>
<dd> <p> By default, tabs are accepted as whitespace, but tabs are not members of the Fortran Character Set. For continuation lines, a tab followed by a digit between 1 and 9 is supported. <code>-Wno-tabs</code> will cause a warning to be issued if a tab is encountered. Note, <code>-Wno-tabs</code> is active for <code>-pedantic</code>, <code>-std=f95</code>, <code>-std=f2003</code>, <code>-std=f2008</code> and <code>-Wall</code>. </p>
 </dd>
<dt><code>-Wunderflow</code></dt>
<dd> <p> Produce a warning when numerical constant expressions are encountered, which yield an <font SIZE="-1">UNDERFLOW</font> during compilation. </p>
 </dd>
<dt><code>-Wintrinsic-shadow</code></dt>
<dd> <p> Warn if a user-defined procedure or module procedure has the same name as an intrinsic; in this case, an explicit interface or <code>&quot;EXTERNAL&quot;</code> or <code>&quot;INTRINSIC&quot;</code> declaration might be needed to get calls later resolved to the desired intrinsic/procedure. </p>
 </dd>
<dt><code>-Wunused-parameter</code></dt>
<dd> <p> Contrary to <code>gcc</code>&#8216;s meaning of <code>-Wunused-parameter</code>, <code>gfortran</code>&#8216;s implementation of this option does not warn about unused dummy arguments, but about unused <code>&quot;PARAMETER&quot;</code> values. <code>-Wunused-parameter</code> is not included in <code>-Wall</code> but is implied by <code>-Wall -Wextra</code>. </p>
 </dd>
<dt><code>-Walign-commons</code></dt>
<dd> <p> By default, <code>gfortran</code> warns about any occasion of variables being padded for proper alignment inside a <font SIZE="-1">COMMON</font> block. This warning can be turned off via <code>-Wno-align-commons</code>. See also <code>-falign-commons</code>. </p>
 </dd>
<dt><code>-Werror</code></dt>
<dd> <p> Turns all warnings into errors. </p>
 </dd></dl>
<p> Some of these have no effect when compiling programs written in Fortran.  </p>
<font SIZE="-1"></font><h3>Options for debugging your program or GNU Fortran</h3>
<p> <font SIZE="-1">GNU</font> Fortran has various special options that are used for debugging either your program or the <font SIZE="-1">GNU</font> Fortran compiler. </p>
<dl>
<dt><code>-fdump-parse-tree</code></dt>
<dd> <p> Output the internal parse tree before starting code generation. Only really useful for debugging the <font SIZE="-1">GNU</font> Fortran compiler itself. </p>
 </dd>
<dt><code>-ffpe-trap=</code><i>list</i></dt>
<dd> <p> Specify a list of <font SIZE="-1">IEEE</font> exceptions when a Floating Point Exception (<font SIZE="-1">FPE</font>) should be raised. On most systems, this will result in a <font SIZE="-1">SIGFPE</font> signal being sent and the program being interrupted, producing a core file useful for debugging. <i>list</i> is a (possibly empty) comma-separated list of the following <font SIZE="-1">IEEE</font> exceptions: <code>invalid</code> (invalid floating point operation, such as <code>&quot;SQRT(-1.0)&quot;</code>), <code>zero</code> (division by zero), <code>overflow</code> (overflow in a floating point operation), <code>underflow</code> (underflow in a floating point operation), <code>precision</code> (loss of precision during operation) and <code>denormal</code> (operation produced a denormal value). </p>
<p> Some of the routines in the Fortran runtime library, like <font SIZE="-1"><code>CPU_TIME</code></font>, are likely to trigger floating point exceptions when <code>&quot;ffpe-trap=precision&quot;</code> is used. For this reason, the use of <code>&quot;ffpe-trap=precision&quot;</code> is not recommended. </p>
 </dd>
<dt><code>-fbacktrace</code></dt>
<dd> <p> Specify that, when a runtime error is encountered or a deadly signal is emitted (segmentation fault, illegal instruction, bus error or floating-point exception), the Fortran runtime library should output a backtrace of the error. This option only has influence for compilation of the Fortran main program. </p>
 </dd>
<dt><code>-fdump-core</code></dt>
<dd> <p> Request that a core-dump file is written to disk when a runtime error is encountered on systems that support core dumps. This option is only effective for the compilation of the Fortran main program. </p>
 </dd></dl>
<h3>Options for directory search</h3>
<p> These options affect how <font SIZE="-1">GNU</font> Fortran searches for files specified by the <code>&quot;INCLUDE&quot;</code> directive and where it searches for previously compiled modules. </p>
<p> It also affects the search paths used by <code>cpp</code> when used to preprocess Fortran source. </p>
<dl>
<dt><code>-I</code><i>dir</i></dt>
<dd> <p> These affect interpretation of the <code>&quot;INCLUDE&quot;</code> directive (as well as of the <code>&quot;#include&quot;</code> directive of the <code>cpp</code> preprocessor). </p>
<p> Also note that the general behavior of <code>-I</code> and <code>&quot;INCLUDE&quot;</code> is pretty much the same as of <code>-I</code> with <code>&quot;#include&quot;</code> in the <code>cpp</code> preprocessor, with regard to looking for <i>header.gcc</i> files and other such things. </p>
<p> This path is also used to search for <i>.mod</i> files when previously compiled modules are required by a <code>&quot;USE&quot;</code> statement. </p>
 </dd>
<dt><code>-J</code><i>dir</i></dt>
<dd> <p> This option specifies where to put <i>.mod</i> files for compiled modules. It is also added to the list of directories to searched by an <code>&quot;USE&quot;</code> statement. </p>
<p> The default is the current directory. </p>
 </dd>
<dt><code>-fintrinsic-modules-path</code><i>dir</i></dt>
<dd> <p> This option specifies the location of pre-compiled intrinsic modules, if they are not in the default location expected by the compiler. </p>
 </dd></dl>
<h3>Influencing the linking step</h3>
<p> These options come into play when the compiler links object files into an executable output file. They are meaningless if the compiler is not doing a link step. </p>
<dl>
<dt><code>-static-libgfortran</code></dt>
<dd> <p> On systems that provide <i>libgfortran</i> as a shared and a static library, this option forces the use of the static version. If no shared version of <i>libgfortran</i> was built when the compiler was configured, this option has no effect. </p>
 </dd></dl>
<h3>Influencing runtime behavior</h3>
<p> These options affect the runtime behavior of programs compiled with <font SIZE="-1">GNU</font> Fortran. </p>
<dl>
<dt><code>-fconvert=</code><i>conversion</i></dt>
<dd> <p> Specify the representation of data for unformatted files. Valid values for conversion are: <code>native</code>, the default; <code>swap</code>, swap between big- and little-endian; <code>big-endian</code>, use big-endian representation for unformatted files; <code>little-endian</code>, use little-endian representation for unformatted files. </p>
<p> <i>This option has an effect only when used in the main program. The </i>&quot;CONVERT&quot;<i> specifier and the </i><font SIZE="-1"><i>GFORTRAN_CONVERT_UNIT</i></font><i> environment variable override the default specified by </i>-fconvert <i>.</i> </p>
 </dd>
<dt><code>-fno-range-check</code></dt>
<dd> <p> Disable range checking of input values during integer <code>&quot;READ&quot;</code> operations. For example, <font SIZE="-1">GNU</font> Fortran will give an error if an input value is outside of the relevant range of [<code>&quot;-HUGE()&quot;</code>:<code>&quot;HUGE()&quot;</code>]. In other words, with <code>&quot;INTEGER (kind=4) :: i&quot;</code> , attempting to read -2147483648 will give an error unless <code>-fno-range-check</code> is given. </p>
 </dd>
<dt><code>-frecord-marker=</code><i>length</i></dt>
<dd> <p> Specify the length of record markers for unformatted files. Valid values for <i>length</i> are 4 and 8. Default is 4. <i>This is different from previous versions of</i> <code>gfortran</code>, which specified a default record marker length of 8 on most systems. If you want to read or write files compatible with earlier versions of <code>gfortran</code>, use <code>-frecord-marker=8</code>. </p>
 </dd>
<dt><code>-fmax-subrecord-length=</code><i>length</i></dt>
<dd> <p> Specify the maximum length for a subrecord. The maximum permitted value for length is 2147483639, which is also the default. Only really useful for use by the gfortran testsuite. </p>
 </dd>
<dt><code>-fsign-zero</code></dt>
<dd> <p> When writing zero values, show the negative sign if the sign bit is set. <code>&quot;fno-sign-zero&quot;</code> does not print the negative sign of zero values for compatibility with F77. Default behavior is to show the negative sign. </p>
 </dd></dl>
<h3>Options for code generation conventions</h3>
<p> These machine-independent options control the interface conventions used in code generation. </p>
<p> Most of them have both positive and negative forms; the negative form of <code>-ffoo</code> would be <code>-fno-foo</code>. In the table below, only one of the forms is listed---the one which is not the default. You can figure out the other form by either removing <code>no-</code> or adding it. </p>
<dl>
<dt><code>-fno-automatic</code></dt>
<dd> <p> Treat each program unit (except those marked as <font SIZE="-1">RECURSIVE</font>) as if the <code>&quot;SAVE&quot;</code> statement were specified for every local variable and array referenced in it. Does not affect common blocks. (Some Fortran compilers provide this option under the name <code>-static</code> or <code>-save</code>.) The default, which is <code>-fautomatic</code>, uses the stack for local variables smaller than the value given by <code>-fmax-stack-var-size</code>. Use the option <code>-frecursive</code> to use no static memory. </p>
 </dd>
<dt><code>-ff2c</code></dt>
<dd> <p> Generate code designed to be compatible with code generated by <code>g77</code> and <code>f2c</code>. </p>
<p> The calling conventions used by <code>g77</code> (originally implemented in <code>f2c</code>) require functions that return type default <code>&quot;REAL&quot;</code> to actually return the C type <code>&quot;double&quot;</code>, and functions that return type <code>&quot;COMPLEX&quot;</code> to return the values via an extra argument in the calling sequence that points to where to store the return value. Under the default <font SIZE="-1">GNU</font> calling conventions, such functions simply return their results as they would in <font SIZE="-1">GNU</font> C---default <code>&quot;REAL&quot;</code> functions return the C type <code>&quot;float&quot;</code>, and <code>&quot;COMPLEX&quot;</code> functions return the <font SIZE="-1">GNU C</font> type <code>&quot;complex&quot;</code>. Additionally, this option implies the <code>-fsecond-underscore</code> option, unless <code>-fno-second-underscore</code> is explicitly requested. </p>
<p> This does not affect the generation of code that interfaces with the <code>libgfortran</code> library. </p>
<p> <i>Caution:</i> It is not a good idea to mix Fortran code compiled with <code>-ff2c</code> with code compiled with the default <code>-fno-f2c</code> calling conventions as, calling <code>&quot;COMPLEX&quot;</code> or default <code>&quot;REAL&quot;</code> functions between program parts which were compiled with different calling conventions will break at execution time. </p>
<p> <i>Caution:</i> This will break code which passes intrinsic functions of type default <code>&quot;REAL&quot;</code> or <code>&quot;COMPLEX&quot;</code> as actual arguments, as the library implementations use the <code>-fno-f2c</code> calling conventions. </p>
 </dd>
<dt><code>-fno-underscoring</code></dt>
<dd> <p> Do not transform names of entities specified in the Fortran source file by appending underscores to them. </p>
<p> With <code>-funderscoring</code> in effect, <font SIZE="-1">GNU</font> Fortran appends one underscore to external names with no underscores. This is done to ensure compatibility with code produced by many <font SIZE="-1">UNIX</font> Fortran compilers. </p>
<p> <i>Caution</i>: The default behavior of <font SIZE="-1">GNU</font> Fortran is incompatible with <code>f2c</code> and <code>g77</code>, please use the <code>-ff2c</code> option if you want object files compiled with <font SIZE="-1">GNU</font> Fortran to be compatible with object code created with these tools. </p>
<p> Use of <code>-fno-underscoring</code> is not recommended unless you are experimenting with issues such as integration of <font SIZE="-1">GNU</font> Fortran into existing system environments (vis-@`{a}-vis existing libraries, tools, and so on). </p>
<p> For example, with <code>-funderscoring</code>, and assuming other defaults like <code>-fcase-lower</code> and that <code>&quot;j()&quot;</code> and <code>&quot;max_count()&quot;</code> are external functions while <code>&quot;my_var&quot;</code> and <code>&quot;lvar&quot;</code> are local variables, a statement like </p>
<pre><code>        I = J() + MAX_COUNT (MY_VAR, LVAR)
</code></pre>
<p> is implemented as something akin to: </p>
<pre><code>        i = j_() + max_count__(&amp;my_var__, &amp;lvar);
</code></pre>
<p> With <code>-fno-underscoring</code>, the same statement is implemented as: </p>
<pre><code>        i = j() + max_count(&amp;my_var, &amp;lvar);
</code></pre>
<p> Use of <code>-fno-underscoring</code> allows direct specification of user-defined names while debugging and when interfacing <font SIZE="-1">GNU</font> Fortran code with other languages. </p>
<p> Note that just because the names match does <i>not</i> mean that the interface implemented by <font SIZE="-1">GNU</font> Fortran for an external name matches the interface implemented by some other language for that same name. That is, getting code produced by <font SIZE="-1">GNU</font> Fortran to link to code produced by some other compiler using this or any other method can be only a small part of the overall solution---getting the code generated by both compilers to agree on issues other than naming can require significant effort, and, unlike naming disagreements, linkers normally cannot detect disagreements in these other areas. </p>
<p> Also, note that with <code>-fno-underscoring</code>, the lack of appended underscores introduces the very real possibility that a user-defined external name will conflict with a name in a system library, which could make finding unresolved-reference bugs quite difficult in some cases---they might occur at program run time, and show up only as buggy behavior at run time. </p>
<p> In future versions of <font SIZE="-1">GNU</font> Fortran we hope to improve naming and linking issues so that debugging always involves using the names as they appear in the source, even if the names as seen by the linker are mangled to prevent accidental linking between procedures with incompatible interfaces. </p>
 </dd>
<dt><code>-fsecond-underscore</code></dt>
<dd> <p> By default, <font SIZE="-1">GNU</font> Fortran appends an underscore to external names. If this option is used <font SIZE="-1">GNU</font> Fortran appends two underscores to names with underscores and one underscore to external names with no underscores. <font SIZE="-1">GNU</font> Fortran also appends two underscores to internal names with underscores to avoid naming collisions with external names. </p>
<p> This option has no effect if <code>-fno-underscoring</code> is in effect. It is implied by the <code>-ff2c</code> option. </p>
<p> Otherwise, with this option, an external name such as <code>&quot;MAX_COUNT&quot;</code> is implemented as a reference to the link-time external symbol <code>&quot;max_count__&quot;</code>, instead of <code>&quot;max_count_&quot;</code>. This is required for compatibility with <code>g77</code> and <code>f2c</code>, and is implied by use of the <code>-ff2c</code> option. </p>
 </dd>
<dt><code>-fbounds-check</code></dt>
<dd> <p> Enable generation of run-time checks for array subscripts and against the declared minimum and maximum values. It also checks array indices for assumed and deferred shape arrays against the actual allocated bounds and ensures that all string lengths are equal for character array constructors without an explicit typespec. </p>
<p> Some checks require that <code>-fbounds-check</code> is set for the compilation of the main program. </p>
<p> Note: In the future this may also include other forms of checking, e.g., checking substring references. </p>
 </dd>
<dt><code>fcheck-array-temporaries</code></dt>
<dd> <p> Warns at run time when for passing an actual argument a temporary array had to be generated. The information generated by this warning is sometimes useful in optimization, in order to avoid such temporaries. </p>
<p> Note: The warning is only printed once per location. </p>
 </dd>
<dt><code>-fmax-array-constructor=</code><i>n</i></dt>
<dd> <p> This option can be used to increase the upper limit permitted in array constructors. The code below requires this option to expand the array at compile time. </p>
<pre><code>        C&lt;program test&gt;
        C&lt;implicit none&gt;
        C&lt;integer j&gt;
        C&lt;integer, parameter :: n = 100000&gt;
        C&lt;integer, parameter ::i(n) = (/ (2*j, j = 1, n) /)&gt;
        C&lt;print '(10(I0,1X))', i&gt;
        C&lt;end program test&gt;
</code></pre>
<p> <i>Caution: This option can lead to long compile times and excessively large object files.</i> </p>
<p> The default value for <i>n</i> is 65535. </p>
 </dd>
<dt><code>-fmax-stack-var-size=</code><i>n</i></dt>
<dd> <p> This option specifies the size in bytes of the largest array that will be put on the stack; if the size is exceeded static memory is used (except in procedures marked as <font SIZE="-1">RECURSIVE</font>). Use the option <code>-frecursive</code> to allow for recursive procedures which do not have a <font SIZE="-1">RECURSIVE</font> attribute or for parallel programs. Use <code>-fno-automatic</code> to never use the stack. </p>
<p> This option currently only affects local arrays declared with constant bounds, and may not apply to all character variables. Future versions of <font SIZE="-1">GNU</font> Fortran may improve this behavior. </p>
<p> The default value for <i>n</i> is 32768. </p>
 </dd>
<dt><code>-fpack-derived</code></dt>
<dd> <p> This option tells <font SIZE="-1">GNU</font> Fortran to pack derived type members as closely as possible. Code compiled with this option is likely to be incompatible with code compiled without this option, and may execute slower. </p>
 </dd>
<dt><code>-frepack-arrays</code></dt>
<dd> <p> In some circumstances <font SIZE="-1">GNU</font> Fortran may pass assumed shape array sections via a descriptor describing a noncontiguous area of memory. This option adds code to the function prologue to repack the data into a contiguous block at runtime. </p>
<p> This should result in faster accesses to the array. However it can introduce significant overhead to the function call, especially when the passed data is noncontiguous. </p>
 </dd>
<dt><code>-fshort-enums</code></dt>
<dd> <p> This option is provided for interoperability with C code that was compiled with the <code>-fshort-enums</code> option. It will make <font SIZE="-1">GNU</font> Fortran choose the smallest <code>&quot;INTEGER&quot;</code> kind a given enumerator set will fit in, and give all its enumerators this kind. </p>
 </dd>
<dt><code>-fexternal-blas</code></dt>
<dd> <p> This option will make <code>gfortran</code> generate calls to <font SIZE="-1">BLAS</font> functions for some matrix operations like <code>&quot;MATMUL&quot;</code>, instead of using our own algorithms, if the size of the matrices involved is larger than a given limit (see <code>-fblas-matmul-limit</code>). This may be profitable if an optimized vendor <font SIZE="-1">BLAS</font> library is available. The <font SIZE="-1">BLAS</font> library will have to be specified at link time. </p>
 </dd>
<dt><code>-fblas-matmul-limit=</code><i>n</i></dt>
<dd> <p> Only significant when <code>-fexternal-blas</code> is in effect. Matrix multiplication of matrices with size larger than (or equal to) <i>n</i> will be performed by calls to <font SIZE="-1">BLAS</font> functions, while others will be handled by <code>gfortran</code> internal algorithms. If the matrices involved are not square, the size comparison is performed using the geometric mean of the dimensions of the argument and result matrices. </p>
<p> The default value for <i>n</i> is 30. </p>
 </dd>
<dt><code>-frecursive</code></dt>
<dd> <p> Allow indirect recursion by forcing all local arrays to be allocated on the stack. This flag cannot be used together with <code>-fmax-stack-var-size=</code> or <code>-fno-automatic</code>. </p>
 </dd>
<dt><code>-finit-local-zero</code></dt>
<dd>  </dd>
<dt><code>-finit-integer=</code><i>n</i></dt>
<dd>  </dd>
<dt><code>-finit-real=</code><i>&lt;zero|inf|-inf|nan&gt;</i></dt>
<dd>  </dd>
<dt><code>-finit-logical=</code><i>&lt;true|false&gt;</i></dt>
<dd>  </dd>
<dt><code>-finit-character=</code><i>n</i></dt>
<dd> <p> The <code>-finit-local-zero</code> option instructs the compiler to initialize local <code>&quot;INTEGER&quot;</code>, <code>&quot;REAL&quot;</code>, and <code>&quot;COMPLEX&quot;</code> variables to zero, <code>&quot;LOGICAL&quot;</code> variables to false, and <code>&quot;CHARACTER&quot;</code> variables to a string of null bytes. Finer-grained initialization options are provided by the <code>-finit-integer=</code><i>n</i>, <code>-finit-real=</code><i>&lt;zero|inf|-inf|nan&gt;</i> (which also initializes the real and imaginary parts of local <code>&quot;COMPLEX&quot;</code> variables), <code>-finit-logical=</code><i>&lt;true|false&gt;</i>, and <code>-finit-character=</code><i>n</i> (where <i>n</i> is an <font SIZE="-1">ASCII</font> character value) options. These options do not initialize components of derived type variables, nor do they initialize variables that appear in an <code>&quot;EQUIVALENCE&quot;</code> statement. (This limitation may be removed in future releases). </p>
<p> Note that the <code>-finit-real=nan</code> option initializes <code>&quot;REAL&quot;</code> and <code>&quot;COMPLEX&quot;</code> variables with a quiet NaN. </p>
 </dd>
<dt><code>-falign-commons</code></dt>
<dd> <p> By default, <code>gfortran</code> enforces proper alignment of all variables in a <font SIZE="-1">COMMON</font> block by padding them as needed. On certain platforms this is mandatory, on others it increases performance. If a <font SIZE="-1">COMMON</font> block is not declared with consistent data types everywhere, this padding can cause trouble, and <code>-fno-align-commons</code> can be used to disable automatic alignment. The same form of this option should be used for all files that share a <font SIZE="-1">COMMON</font> block. To avoid potential alignment issues in <font SIZE="-1">COMMON</font> blocks, it is recommended to order objects from largests to smallest. </p>
 </dd></dl>
<h2>ENVIRONMENT</h2>
<p> The <code>gfortran</code> compiler currently does not make use of any environment variables to control its operation above and beyond those that affect the operation of <code>gcc</code>.  </p>
<h2>BUGS</h2>
<p> For instructions on reporting bugs, see &lt;<code><a rel="nofollow" href="http://bugzilla.redhat.com/bugzilla">http://bugzilla.redhat.com/bugzilla</a></code>&gt;.  </p>
<h2>SEE ALSO</h2>
<p> <i>gpl</i>(7), <i>gfdl</i>(7), <i>fsf-funding</i>(7), <i><a href="/docs/linux/man/1-cpp/">cpp</a></i>(1), <i><a href="/docs/linux/man/1-gcov/">gcov</a></i>(1), <i><a href="/docs/linux/man/1-gcc/">gcc</a></i>(1), <i><a href="/docs/linux/man/1-as/">as</a></i>(1), <i><a href="/docs/linux/man/1-ld/">ld</a></i>(1), <i><a href="/docs/linux/man/1-gdb/">gdb</a></i>(1), <i>adb</i>(1), <i>dbx</i>(1), <i>sdb</i>(1) and the Info entries for <i>gcc</i>, <i>cpp</i>, <i>gfortran</i>, <i>as</i>, <i>ld</i>, <i>binutils</i> and <i>gdb</i>.  </p>
<h2>AUTHOR</h2>
<p> See the Info entry for <code>gfortran</code> for contributors to <font SIZE="-1">GCC</font> and <font SIZE="-1">GNU</font> Fortran.  </p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 2004, 2005, 2006, 2007, 2008 Free Software Foundation, Inc. </p>
<p> Permission is granted to copy, distribute and/or modify this document under the terms of the <font SIZE="-1">GNU</font> Free Documentation License, Version 1.2 or any later version published by the Free Software Foundation; with the Invariant Sections being ``Funding Free Software&#8217;&#8216;, the Front-Cover Texts being (a) (see below), and with the Back-Cover Texts being (b) (see below). A copy of the license is included in the <i>gfdl</i>(7) man page. </p>
<p> (a) The <font SIZE="-1">FSF</font>&#8216;s Front-Cover Text is: </p>
<pre><code>     A GNU Manual
</code></pre>
<p> (b) The <font SIZE="-1">FSF</font>&#8216;s Back-Cover Text is: </p>
<pre><code>     You have freedom to copy and modify this GNU Manual, like GNU
     software. Copies published by the Free Software Foundation raise
     funds for GNU development.
</code></pre>
