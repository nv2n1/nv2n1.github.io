---
title: "bakefile(1)"
name: "bakefile"
section: "1"
letter: "b"
url: "/docs/linux/man/1-bakefile/"
description: "bakefile – native makefiles generator"
---

<h2 class="name">NAME</h2>
<p> bakefile &#8211; native makefiles generator </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>bakefile</code> [<code>&#8211;version</code>] [<code>&#8211;help</code>] <code>-f</code><i>FORMAT</i> <code>-o</code><i>OUTFILE</i> [<code>&#8211;eol=[format|dos|unix|mac|native]</code>] [<code>&#8211;wrap-output=[no|</code><i>LENGTH</i><code>]</code>] [<code>-D</code><i>VAR</i>=<i>VALUE</i>&#8230;] [<code>-I</code><i>PATH</i>&#8230;] [<code>-v</code>] [<code>-q</code>] [<code>&#8211;dry-run</code>] [<code>&#8211;touch</code>] [<code>&#8211;dump</code>] <i>file.bkl</i></dl>
<h2>DESCRIPTION</h2>
<p> <code>bakefile</code></p>
<dd>creates various types of Makefiles and project files from a single project description called a &quot;Bakefile&quot;.</p>
<h2>COMMAND LINE OPTIONS</h2>
<p> <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Display Bakefile version and exit.</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Display usage information and exit.</dl>
<p> <code>-f</code><i>FORMAT</i>, <code>&#8211;format</code>=<i>FORMAT</i></p>
<dl>
<dt>
<dd> Specify output format. Bakefile supports the following formats: </p>
<table BORDER>
<tr VALIGN=top>
<td><code> Format </code></td>
<td><code> File(s) Generated </code>
</td>
</tr>
<tr VALIGN=top>
<td> autoconf </td>
<td> Makefile.in for GNU Autoconf
</td>
</tr>
<tr VALIGN=top>
<td> borland </td>
<td> Makefile for Borland C++ and Borland<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>make
</td>
</tr>
<tr VALIGN=top>
<td> dmars </td>
<td> Generic Makefile for Digital Mars C/C++
</td>
</tr>
<tr VALIGN=top>
<td> dmars_smake </td>
<td> Makefile for Digital Mars C/C++ with<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>SMAKE
</td>
</tr>
<tr VALIGN=top>
<td> gnu </td>
<td> Makefile for GNU toolchain: GNU Make, GCC,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>etc.
</td>
</tr>
<tr VALIGN=top>
<td> mingw </td>
<td> Makefile for MinGW toolchain:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>mingw32-make, MinGW port of GCC, etc.
</td>
</tr>
<tr VALIGN=top>
<td> msvc </td>
<td> Makefile for Visual C++ with Microsoft<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>nmake
</td>
</tr>
<tr VALIGN=top>
<td> msvc6prj </td>
<td> Microsoft Visual C++ 6.0 project files
</td>
</tr>
<tr VALIGN=top>
<td> msevc4prj </td>
<td> Microsoft Embedded Visual C++ 4 project<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>files
</td>
</tr>
<tr VALIGN=top>
<td> msvs2003prj </td>
<td> MS Visual Studio 2003 project files
</td>
</tr>
<tr VALIGN=top>
<td> msvs2005prj </td>
<td> MS Visual Studio 2005 project files
</td>
</tr>
<tr VALIGN=top>
<td> msvs2008prj </td>
<td> MS Visual Studio 2008 project files
</td>
</tr>
<tr VALIGN=top>
<td> suncc </td>
<td> GNU makefile for SunCC compiler
</td>
</tr>
<tr VALIGN=top>
<td> symbian </td>
<td> Symbian development files
</td>
</tr>
<tr VALIGN=top>
<td> watcom </td>
<td> Makefile for OpenWatcom C/C++
</td>
</tr>
<tr VALIGN=top>
<td> xcode2 </td>
<td> Apple Xcode 2.4 project files
</td>
</tr>
</table>
</dl>
<p> <code>-o</code><i>OUTFILE</i>, <code>&#8211;output</code>=<i>OUTFILE</i></p>
<dl>
<dt>
<dd> File to write generated makefile to. For those backends that generate more than one file, this option specifies the name of the main makefile. </p>
<p> This option has special meaning for msvs200xprj formats: by default, both the project files (one for each target) and a solution file, containing all the project files, are generated. However if OUTFILE is a file with .vcproj extension, then only the (necessarily unique) project file will be generated.</dl>
<p> <code>-D</code><i>VAR</i>=<i>VALUE</i></p>
<dl>
<dt>
<dd> Define Bakefile variable. This definition overrides any definition from the ruleset or input makefile. You can use it to customize generated output.</dl>
<p> <code>&#8211;eol</code>=<i>[format|dos|unix|mac|native]</i></p>
<dl>
<dt>
<dd> Change the type of line endings used by general files. dos, unix and mac specify the line endings used by respective platforms. native will use line endings of the platform Bakefile is ran on (doing this is usually a bad idea, but it is useful e.g. when checking generated files into RCS system that can&#8217;t deal with line endings correctly, such as CVS). The default value is format and means that the most appropriate line endings for the output format will be used &#8211; Windows makefiles will use DOS line endings, Autoconf makefiles will use Unix ones and so on.</dl>
<p> <code>&#8211;wrap-output</code>=<i>[no|LENGTH]</i></p>
<dl>
<dt>
<dd> Change line wrappings behavior. By default, Bakefile wraps generated makefiles so that lines don&#8217;t exceed 75 characters. Use this option to either change the limit or to disable wrapping entirely by using no as the value.</dl>
<p> <code>-I</code><i>PATH</i></p>
<dl>
<dt>
<dd> Add path to the list of directories where Bakefile looks for rules and output templates.</dl>
<p> <code>&#8211;dry-run</code></p>
<dl>
<dt>
<dd> Process the bakefile normally, but instead of creating or modifying files, just print which files would be changed without actually modifying them.</dl>
<p> <code>-v</code>, <code>&#8211;verbose</code></p>
<dl>
<dt>
<dd> Be verbose.</dl>
<p> <code>-q</code>, <code>&#8211;quiet</code></p>
<dl>
<dt>
<dd> Supress all output except for errors.</dl>
<p> <code>&#8211;touch</code></p>
<dl>
<dt>
<dd> Always touch output files, even if their content doesn&#8217;t change.</dl>
<p> <code>&#8211;debug</code></p>
<dl>
<dt>
<dd> show internal debugging information</dl>
<p> <code>&#8211;dump</code></p>
<dl>
<dt>
<dd> Dump all Bakefile variables and targets to standard output instead of generating output. This is only useful for debugging Bakefile or ill-behaving makefiles.</dl>
<p> <code>&#8211;output-deps</code>=<i>FILE</i></p>
<dl>
<dt>
<dd> Output dependency information needed by <code>bakefile_gen</code> utility</dl>
<p> <code>&#8211;output-changes</code>=<i>FILE</i></p>
<dl>
<dt>
<dd> Store list of changed files to the given file</dl>
<p> <code>&#8211;xml-cache</code>=<i>FILE</i></p>
<dl>
<dt>
<dd> specify cache file where <code>bakefile_gen</code> stores pre-parsed XML files</dl>
<h2>ENVIRONMENT VARIABLES</h2>
<p> BAKEFILE_PATHS</p>
<dl>
<dt>
<dd> List of directories where ruleset files are looked for (syntax is same as in <i>PATH</i>). Bakefile&#8217;s data directory is always searched in addition to paths listed in <i>BAKEFILE_PATHS</i>, but <i>BAKEFILE_PATHS</i> has higher priority.</dl>
<h2>Index</h2>
