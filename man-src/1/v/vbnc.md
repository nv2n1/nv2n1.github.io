---
title: "vbnc(1)"
name: "vbnc"
section: "1"
letter: "v"
url: "/docs/linux/man/1-vbnc/"
description: "vbnc – Mono Visual Basic Compiler."
---

<h2>NAME</h2>
<p> vbnc &#8211; Mono Visual Basic Compiler.</p>
<h2>SYNOPSIS</h2>
<p> <code>vbnc</code> [option] [source-files]</p>
<h2>DESCRIPTION</h2>
<p> <i>(vbnc) </i> is a CIL compiler for the VisualBasic.NET language. </p>
<p> Applications developed on Windows with vbc can execute on Mono and applications compiled with &#8216;vbnc&#8217; can be executed on .NET runtime. </p>
<p> The Mono Visual Basic compiler accepts the same options as the Microsoft VB.NET compiler. Those options can start with a slash or a dash (/checked is the same as -checked). </p>
<p> Visual Basic.NET source files normally ends with a &quot;.vb&quot; extension. Compilation of VB.NET source code requires all the files that make up a library, module or executable to be provided on the command line. There is no support for partial compilation. To achieve the benefits of partial compilation, you should compile programs into their own assemblies, and later reference them with the &quot;-r&quot; flag. </p>
<p> The Mono Basic compiler generates images (.exe files) that contain CIL byte code that can be executed by any system that implements a Common Language Infrastructure virtual machine such as the Microsoft .NET runtime engine on Windows or the Mono runtime engine on Unix systems. Executables are not bound to a specific CPU or operating system. </p>
<p> The Mono Basic compiler by default only references these assemblies: mscorlib.dll, Microsoft.VisualBasic.dll, System.dll and System.Xml.dll. If you want to reference extra libraries you must manually specify them using the the -r: command line option. </p>
<h2>OPTIONS</h2>
<dl>
<dt><i>-addmodule:MODULE1[,MODULE2]</i></dt>
<dd> Includes the specified modules in the resulting assembly.</dd>
<dt><i>-codepage:ID</i></dt>
<dd> Specifies the code page used to process the input files from the point it is specified on. By default files will be processed in the current code page. The compiler will also automatically detect Unicode/UTF8 files that have an embedded byte mark at the beginning.</dd>
<dt>Other popular encodings are 28591 (Latin1), 1252 (iso-8859-1) and 65001 (UTF-8).</dt>
<dd>
</dd><dt><i>-define:SYMLIST, -d:SYMLIST</i></dt>
<dd> Defines the symbol listed by the semi-colon separeted list SYMLIST SYMBOL. This can be tested in the source code by the pre-processor, or can be used by methods that have been tagged with the Conditional attribute.</dd>
<dt><i>-debug:AMOUNT</i></dt>
<dd> Specify the amount of debugging information to emit. Possible values for AMOUNT are &quot;full&quot; and &quot;pdbonly&quot;.</dd>
<dt><i>-imports:import-list</i></dt>
<dd> Declare global Imports for listed namespaces.</dd>
<dt><i>-ignorewarn:XXXX</i></dt>
<dd> Ignores warning number XXXX.</dd>
<dt><i>-lib:PATHLIST, -libpath:PATHLIST</i></dt>
<dd> Each path specified in the comma-separated list will direct the compiler to look for libraries in that specified path.</dd>
<dt><i>-main:CLASS</i></dt>
<dd> Tells the compiler which CLASS or MODULE contains the entry point. Useful when you are compiling several classes with a Main method.</dd>
<dt><i>-nologo</i></dt>
<dd> Suppress printing copyright information on startup.</dd>
<dt><i>-nostdlib, -nostdlib+</i></dt>
<dd> Use this flag if you want to compile the core library. This makes the compiler load its internal types from the assembly being compiled.</dd>
<dt><i>-noconfig, -noconfig+</i></dt>
<dd> Disables the default compiler configuration to be loaded. The compiler by default has references to the system assemblies.</dd>
<dt><i>-nowarn</i></dt>
<dd> Makes the compiler ignore warnings.</dd>
<dt><i>-optioncompare:binary, -optioncompare:text </i></dt>
<dd> Select between binary and text string comparisons. The default is binary string comparisons.</dd>
<dt><i>-optionexplicit[+|-]</i></dt>
<dd> Require explicit declaration of variables</dd>
<dt><i>-optionstrict[+|-]</i></dt>
<dd> Enforce strict language semantics</dd>
<dt><i>-out:FNAME, -o FNAME</i></dt>
<dd> Names the output file to be generated.</dd>
<dt><i>-q -quiet</i></dt>
<dd> Commands the compiler to show only error messages for syntax-related errors and warnings.</dd>
<dt><i>-resource:RESOURCE[,ID]</i></dt>
<dd> Embeds to the given resource file. The optional ID can be used to give a different name to the resource. If not specified, the resource name will be the file name.</dd>
<dt><i>-linkresource:RESOURCE[,ID]</i></dt>
<dd> Links to the specified RESOURCE. The optional ID can be used to give a name to the linked resource.</dd>
<dt><i>-r:ASSEMBLY1[,ASSEMBLY2], -r ASSEMBLY1[,ASSEMBLY2]</i></dt>
<dd> Reference the named assemblies. Use this to use classes from the named assembly in your program. The assembly will be loaded from either the system directory where all the assemblies live, or from the path explicitly given with the -L option.</dd></dl>
<p> You can also use a semicolon to separate the assemblies instead of a comma.</p>
<dl>
<dt><i>-removeintchecks[+|-]</i></dt>
<dd> Remove integer checks. Default off.</dd>
<dt><i>-rootnamespace:namespace</i></dt>
<dd> Specifies the root namespace for all type declarations</dd>
<dt><i>-target:KIND, -t:KIND</i></dt>
<dd> Used to specify the desired target. The possible values are: exe (plain executable), winexe (Windows.Forms executable), library (component libraries) and module (partial library).</dd>
<dt><i>-utf8output[+|-]</i></dt>
<dd> Emit compiler output in UTF8 character encoding. Currently ignored.</dd>
<dt><i>&#8211;version</i></dt>
<dd> Shows the compiler version.</dd>
<dt><i>-warnaserror, -warnaserror+</i></dt>
<dd> Treat warnings as errors.</dd></dl>
<h2>STABILITY</h2>
<p> As of early 2007, the Mono Visual Basic compiler is still considered preview software. The compiler is almost feature-complete (targeting the Microsoft Visual Basic 8 compiler), only lacking support for the &#8216;My&#8217; namespace. Frequent crashes are still occuring, especially with incorrect code. </p>
<h2>AUTHORS</h2>
<p> See the ChangeLog for authors </p>
<h2>LICENSE</h2>
<p> The Mono Visual Basic compiler is released under the terms of the GNU LGPL. Alternative licenses are available from Novell. </p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-mcs/">mcs</a>(1), <a href="/docs/linux/man/1-mono/">mono</a>(1), mint(1), <a href="/docs/linux/man/1-sn/">sn</a>(1) </p>
<h2>BUGS</h2>
<p> To report bugs in the compiler, you can file bug reports in our bug tracking system: <a rel="nofollow" href="http://bugzilla.ximian.com.">http://bugzilla.ximian.com.</a></p>
<h2>MAILING LIST</h2>
<p> The Mono Basic Mailing List is available at: mono-vb-list-request [at] ximian.com </p>
