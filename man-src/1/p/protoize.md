---
title: "protoize(1)"
name: "protoize"
section: "1"
letter: "p"
url: "/docs/linux/man/1-protoize/"
description: "protoize, unprotoize – automatically add or remove function prototypes"
---

<h2>NAME</h2>
<p> protoize, unprotoize &#8211; automatically add or remove function prototypes</p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>protoize</code> [-CfgklNnqv] [-B <i>DIRECTORY</i>] [-c <i>COMPILATION-OPTIONS</i>] [-d <i>DIRECTORY</i>] [-i <i>STRING</i>] [-p <i>PROGRAM</i>] [-x <i>FILE</i>] [<i>FILE</i>&#8230;]</p>
<dt> <code>unprotoize</code> [-fkNnqv] [-c <i>COMPILATION-OPTIONS</i>] [-d <i>DIRECTORY</i>] [-i <i>STRING</i>] [-p <i>PROGRAM</i>] [-x <i>FILE</i>] [<i>FILE</i>&#8230;]</dl>
<h2>DESCRIPTION</h2>
<p> <code>protoize</code> is an optional part of GCC.</p>
<dd>You can use it to add prototypes to a program, thus converting the program to ANSI C in one respect. The companion program <code>unprotoize</code> does the reverse: it removes argument types from any prototypes that are found. </p>
<p> When you run these programs, you must specify a set of source files as command line arguments. The conversion programs start out by compiling these files to see what functions they define. The information gathered about a file <i>FOO</i> is saved in a file named <i>FOO.X</i>. </p>
<p> After scanning comes the actual conversion. The specified files are all eligible to be converted; any files they include (whether sources or just headers) are eligible as well. </p>
<p> But not all the eligible files are converted. By default, <code>protoize</code> and <code>unprotoize</code> convert only source and header files in the current directory. You can specify additional directories whose files should be converted with the <code>-d</code> <i>DIRECTORY</i> option. You can also specify particular files to exclude with the <code>-x</code> <i>FILE</i> option. A file is converted if it is eligible, its directory name matches one of the specified directory names, and its name within the directory has not been excluded. </p>
<p> Basic conversion with <code>protoize</code> consists of rewriting most function definitions and function declarations to specify the types of the arguments. The only ones not rewritten are those for varargs functions. </p>
<p> <code>protoize</code> optionally inserts prototype declarations at the beginning of the source file, to make them available for any calls that precede the function&#8217;s definition. Or it can insert prototype declarations with block scope in the blocks where undeclared functions are called. </p>
<p> Basic conversion with <code>unprotoize</code> consists of rewriting most function declarations to remove any argument types, and rewriting function definitions to the old-style pre-ANSI form. </p>
<p> Both conversion programs print a warning for any function declaration or definition that they can&#8217;t convert. You can suppress these warnings with the <code>-q</code> option. </p>
<p> The output from <code>protoize</code> or <code>unprotoize</code> replaces the original source file. The original file is renamed to a name ending with <i>.save</i>. If the <i>.save</i> file already exists, then the source file is simply discarded. </p>
<p> <code>protoize</code> and <code>unprotoize</code> both depend on <code><a href="/docs/linux/man/1-gcc/">gcc</a></code>(1) to scan the program and collect information about the functions it uses. </p>
<p> The options are as follows:</p>
<dl>
<dt><code>-B</code> <i>DIRECTORY</i></p>
<dd> Look for the file <i>SYSCALLS.c.X</i> in <i>directory</i>, instead of the usual directory (normally <i>/usr/local/lib</i>). This file contains prototype information about standard system functions. This option applies only to <code>protoize</code>.</p>
<dt><code>-C</code></p>
<dd> Rename files to end in <i>.C</i> instead of <i>.c</i>. This is convenient if you are converting a C program to C++. This option applies only to <code>protoize</code>.</p>
<dt><code>-c</code> <i>COMPILATION-OPTIONS</i></p>
<dd> Use <i>COMPILATION-OPTIONS</i> as the options when running <code><a href="/docs/linux/man/1-gcc/">gcc</a></code>(1) to produce the <i>.X</i> files. The special option <code>-aux-info</code> is always passed in addition, to tell gcc to write a <i>.X</i> file. Note that the compilation options must be given as a single argument to <code>protoize</code> or <code>unprotoize</code>. If you want to specify several gcc options, you must quote the entire set of compilation options to make them a single word in the shell. There are certain gcc arguments that you cannot use, because they would produce the wrong kind of output. These include <code>-g</code>, <code>-O</code>, <code>-c</code>, <code>-S</code>,<code>-o</code>. If you include these in the <i>COMPILATION-OPTIONS</i>, they are ignored.</p>
<dt><code>-d</code> <i>DIRECTORY</i></p>
<dd> Specify additional directories whose files should be converted.</p>
<dt><code>-g</code></p>
<dd> Add explicit global declarations. This means inserting explicit declarations at the beginning of each source file for each function that is called in the file and was not declared. These declarations precede the first function definition that contains a call to an undeclared function. This option applies only to <code> protoize</code>.</p>
<dt><code>-i</code> <i>STRING</i></p>
<dd> Indent old-style parameter declarations with the string <i>STRING</i>. This option applies only to <code>protoize</code>. <code>unprotoize</code> converts prototyped function definitions to old-style function definitions, where the arguments are declared between the argument list and the initial <code>{</code>. By default, <code>unprotoize</code> uses five spaces as the indentation. If you want to indent with just one space instead, use <code>-i &quot; &quot;</code>.</p>
<dt><code>-k</code></p>
<dd> Keep the <i>.X</i> files. Normally, they are deleted after conversion is finished.</p>
<dt><code>-l</code></p>
<dd> Add explicit local declarations. <code>protoize</code> with <code>-l</code> inserts a prototype declaration for each function in each block which calls the function without any declaration. This option applies only to <code>protoize</code>.</p>
<dt><code>-N</code></p>
<dd> Make no <i>.save</i> files. The original files are simply deleted. Use this option with caution.</p>
<dt><code>-n</code></p>
<dd> Make no real changes. This mode just prints information about the conversions that would have been done without <code>-n</code>.</p>
<dt><code>-p</code> <i>PROGRAM</i></p>
<dd> Use the program <code>PROGRAM</code> as the compiler. Normally, the name <code>gcc</code> is used.</p>
<dt><code>-q</code></p>
<dd> Work quietly. Most warnings are suppressed.</p>
<dt><code>-v</code></p>
<dd> Print the version number, just like <code>-v</code> for gcc.</p>
<dt><code>-x</code> <code>FILE</code></p>
<dd> List of files to exclude from the conversion process.</dl>
<p> If you need special compiler options to compile one of your program&#8217;s source files, then you should generate that file&#8217;s <i>.X</i> file specially, by running gcc on that source file with the appropriate options and the option <code>-aux-info</code>. Then run <code>protoize</code> on the entire set of files. <code>protoize</code> will use the existing <i>.X</i> file because it is newer than the source file. For example: </p>
<p> You need to include the special files along with the rest in the <code>protoize</code> command, even though their <i>.X</i> files already exist, because otherwise they won&#8217;t get converted. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-gcc/">gcc</a></code>(1), and the Info entry for <code>gcc</code>, particularly <code>Running protoize</code> section.</p>
<h2>HISTORY</h2>
<p> Ron Guilmette implemented the <code>protoize</code> and <code>unprotoize</code> tools.</p>
<h2>AUTHORS</h2>
<p> See the GCC manual for the contributors to GCC.</p>
<h2>CAVEATS</h2>
<p> The conversion programs <code>protoize</code> and <code>unprotoize</code> can sometimes change a source file in a way that won&#8217;t work unless you rearrange it. </p>
<p> <code>protoize</code> can insert references to a type name or type tag before the definition, or in a file where they are not defined. </p>
<p> If this happens, compiler error messages should indicate where the new references are, so fixing the file by hand is straightforward. </p>
<p> There are some C constructs which <code>protoize</code> cannot figure out. For example, it can&#8217;t determine argument types for declaring a pointer-to-function variable; this must be done by hand. <code>protoize</code> inserts a comment containing <code>???</code> each time it finds such a variable; all such variables can be found by searching for this string. ANSI C does not require declaring the argument types of pointer-to-function types. </p>
<p> Using <code>unprotoize</code> can easily introduce bugs. If the program relied on prototypes to bring about conversion of arguments, these conversions will not take place in the program without prototypes. One case in which you can be sure <code>unprotoize</code> is safe is when you are removing prototypes that were made with <code>protoize</code>; if the program worked before without any prototypes, it will work again without them. </p>
<p> You can find all the places where this problem might occur by compiling the program with the <code>-Wconversion</code> option. It prints a warning whenever an argument is converted. </p>
<p> Both conversion programs can be confused if there are macro calls in and around the text to be converted. In other words, the standard syntax for a declaration or definition must not result from expanding a macro. This problem is inherent in the design of C and cannot be fixed. If only a few functions have confusing macro calls, you can easily convert them manually. </p>
<p> <code>protoize</code> cannot get the argument types for a function whose definition was not actually compiled due to preprocessing conditionals. When this happens, <code>protoize</code> changes nothing in regard to such a function. <code>protoize</code> tries to detect such instances and warn about them. </p>
<p> You can generally work around this problem by using <code>protoize</code> step by step, each time specifying a different set of <code>-D</code> options for compilation, until all of the functions have been converted. There is no automatic way to verify that you have got them all, however. </p>
<p> Confusion may result if there is an occasion to convert a function declaration or definition in a region of source code where there is more than one formal parameter list present. Thus, attempts to convert code containing multiple (conditionally compiled) versions of a single function header (in the same vicinity) may not produce the desired (or expected) results. </p>
<p> If you plan on converting source files which contain such code, it is recommended that you first make sure that each conditionally compiled region of source code which contains an alternative function header also contains at least one additional follower token (past the final right parenthesis of the function header). This should circumvent the problem. </p>
<p> <code>unprotoize</code> can become confused when trying to convert a function definition or declaration which contains a declaration for a pointer-to-function formal argument which has the same name as the function being defined or declared. We recommand you avoid such choices of formal parameter names. </p>
<p> It might be necessary to correct some of the indentation by hand and break long lines. (The conversion programs don&#8217;t write lines longer than eighty characters in any case.)</p>
<h2>BUGS</h2>
<p> For instructions on reporting bugs, see the GCC manual.</p>
<h2>COPYING</h2>
<p> Copyright 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006 Free Software Foundation, Inc. </p>
<p> Permission is granted to make and distribute verbatim copies of this manual provided the copyright notice and this permission notice are preserved on all copies. </p>
<p> Permission is granted to copy and distribute modified versions of this manual under the conditions for verbatim copying, provided that the entire resulting derived work is distributed under the terms of a permission notice identical to this one. </p>
<p> Permission is granted to copy and distribute translations of this manual into another language, under the above conditions for modified versions, except that this permission notice may be included in translations approved by the Free Software Foundation instead of in the original English. </p>
<h2>Index</h2>
