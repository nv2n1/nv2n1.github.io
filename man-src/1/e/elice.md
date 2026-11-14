---
title: "elice(1)"
name: "elice"
section: "1"
letter: "e"
url: "/docs/linux/man/1-elice/"
description: "elice – compiler for programs written in PureBasic"
---

<h2>NAME</h2>
<p> elice &#8211; compiler for programs written in PureBasic</p>
<h2>SYNOPSIS</h2>
<p> <code>elice</code> [<i>options&#8230;</i>] [<code>-o</code> <i>outfile</i>] <i>sourcefile&#8230;</i></p>
<h2>DESCRIPTION</h2>
<p> <code>elice</code> is a compiler for programs written in the proprietary language PureBasic. It compiles such programs to C++ and then invokes <code>g++</code> to generate an executable. Its interface is similar to that of <code>g++</code>. </p>
<p> Normal usage is to compile just one source file, which uses IncludeFile and XIncludeFile statements to incorporate whatever other source files are needed. Such include statements are resolved relative to the directory of the source file they are in. If there are multiple source files on the command line, they are compiled together to form one executable. </p>
<p> <code>elice</code> comes with a library of builtin procedures which will be included in the executable when they are needed. Depending on which builtin procedures are used, the resulting executable may be dynamically linked to other libraries such as libSDL.</p>
<h2>OPTIONS</h2>
<p> Most options will be passed through to <code>g++</code>, so you can use -g -O2 and such as usual.</p>
<dl>
<dt><code>-o</code> <i>outfile</i></p>
<dd> Use <i>outfile</i> as the name of the resulting executable. Without <code>-o</code>, the default is to use the name of the first source file without its extension (for example <code>prog.pb</code> becomes <code>prog</code>).</p>
<dt><code>-save-temps</code></p>
<dd> Save intermediate stages of compilation (C++ with suffix .cc, preprocessed C++ with suffix .ii, assembler code with suffix .s, object code with suffix .o) in the current directory.</p>
<dt><code>-v</code></p>
<dd> Verbose mode. Print detailed information about the programs invoked during compilation.</dl>
<h2>EXIT STATUS</h2>
<p> The exit status is 0 if there were no errors. <code>elice</code> returns 1 if there was a parse error or an error in the command line. If the invocation of <code>g++</code> fails, it returns the exit code from <code>g++</code>.</p>
<h2>EXAMPLES</h2>
<p> elice -g -O2 program.pb -o program</p>
<h2>BUGS</h2>
<p> This program is a work in progress. It does not support the entire PureBasic language, and supports only a small selection of the builtin procedures. It was written to compile one specific program, and it is not likely to be able to compile other programs without modification. </p>
<p> Please let the author know if you would like to use <code>elice</code> to compile other free software programs and need help extending it.</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to &lt;eligo [at] clueonic.net&gt;.</p>
<h2>AUTHOR</h2>
<p> Written by Richard Braakman.</p>
<h2>COPYRIGHT</h2>
<p> Copyright 2008 Richard Braakman. Published under the GNU GPL version 2 or later. See the COPYING file for details. There are additional permissions for the use of the runtime library.</p>
<h2>HISTORY</h2>
<p> <code>elice</code> was written specifically to free the game <i>Lost Labyrinth</i> (<a rel="nofollow" href="http://www.lostlabyrinth.com/)">http://www.lostlabyrinth.com/)</a> and to make it playable on the author&#8217;s amd64 system. Lost Labyrinth is a free software game published under the GNU GPL, but it is written in a language that had a proprietary compiler, and that compiler supported a limited set of target platforms which did not include 64-bit Linux. </p>
<p> Under the battle cry of &quot;It&#8217;s BASIC, how hard can it be?&quot; the author of <code>elice</code> started to write a free compiler. Most of the work was done in September 2006 and it resulted in a playable game, but the compiler was not maintained and was not able to compile newer versions of Lost Labyrinth. </p>
<p> The first public version of <code>elice</code> was released in the summer of 2008, when it had been upgraded to support PureBasic version 4 and was ready for inclusion in the build system of Lost Labyrinth. </p>
<p> Much thanks goes to Markus D[:o]bele for having faith in early versions of <code>elice</code> and relying on it to build the Linux version of Lost Labyrinth. </p>
<h2>Index</h2>
