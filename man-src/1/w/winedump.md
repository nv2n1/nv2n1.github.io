---
title: "winedump(1)"
name: "winedump"
section: "1"
letter: "w"
url: "/docs/linux/man/1-winedump/"
description: "winedump – A Wine DLL tool"
---

<h2>NAME</h2>
<p> winedump &#8211; A Wine DLL tool</p>
<h2>SYNOPSIS</h2>
<p> <code>winedump </code>[<code>-h </code>| <code>sym </code><i>sym</i> | <code>spec </code><i>dll</i> | <code>dump </code><i>file</i> ] [<i>mode_options</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>winedump</code> is a Wine tool which aims to help: </p>
<pre><code>
A: Reimplementing a Win32 DLL for use within Wine, or
B: Compiling a Win32 application with Winelib that uses x86 DLLs
For both tasks in order to be able to link to the Win functions some
glue code is needed.  This 'glue' comes in the form of a .spec file.
The .spec file, along with some dummy code, is used to create a
Wine .so corresponding to the Windows DLL.  The winebuild program
can then resolve calls made to DLL functions.
Creating a .spec file is a labour intensive task during which it is
easy to make a mistake. The idea of winedump is to automate this task
and create the majority of the support code needed for your DLL. In
addition you can have winedump create code to help you re-implement a
DLL, by providing tracing of calls to the DLL, and (in some cases)
automatically determining the parameters, calling conventions, and
return values of the DLL functions.
Another use for this tool is to display (dump)
information about a 32bit DLL or PE format image file.When used in this way winedump functions
                                     similarly to tools such as pedump provided by many Win32 compiler
                                         vendors.Finally winedump can be also used to demangle C++ symbols.
</code></pre>
<h2>MODES</h2>
<p> <code>winedump</code> can be used in several different modes. The first argument to the program determines the mode <code>winedump</code> will run in.</p>
<dl>
<dt><code>-h</code></p>
<dd> Help mode. Basic usage help is printed.</p>
<dt><code>dump</code></p>
<dd> To dump the contents of a file.</p>
<dt><code>spec</code></p>
<dd> For generating .spec files and stub DLLs.</p>
<dt><code>sym</code></p>
<dd> Symbol mode. Used to demangle C++ symbols.</dl>
<h2>OPTIONS</h2>
<p> Mode options depend on the mode given as the first argument. </p>
<p> <code>Help mode:</code> </p>
<pre><code>
No options are used.
The program prints the help info and then exits.
Dump mode:

fileDumps the contents of file. Various file formats are supported
(PE, NE, LE, Minidumps, .lnk).
-CTurns on symbol demangling.
-fDumps file header information.
This option dumps only the standard PE header structures,
along with the COFF sections available in the file.
-j dir_nameDumps only the content of directory dir_name, for files
which header points to directories.
For PE files, currently the import, export, debug, resource,
tls and clr directories are implemented.
For NE files, currently the export and resource directories are
implemented.
-xDumps everything.
This command prints all available information (including all
available directories - see -j option) about the file. You may
wish to pipe the output through more/less or into a file, since
a lot of output will be produced.
-GDumps contents of debug section if any (for now, only stabs
information is supported).

Spec mode:

dllUse dll for input file and generate implementation code.
-I dirLook for prototypes in dir (implies -c). In the case of
Windows DLLs, this could be either the standard include
directory from your compiler, or a SDK include directory.
If you have a text document with prototypes (such as
documentation) that can be used also, however you may need
to delete some non-code lines to ensure that prototypes are
parsed correctly.
The dir argument can also be a file specification (e.g.
include/*). If it contains wildcards you must quote it to
prevent the shell from expanding it.
If you have no prototypes, specify /dev/null as dir.
winedump may still be able to generate some working stub
code for you.
-cGenerate skeleton code (requires -I).
This option tells winedump to create function stubs for each
function in the DLL. As winedump reads each exported symbol
from the source DLL, it first tries to demangle the name. If
the name is a C++ symbol, the arguments, class and return
value are all encoded into the symbol name. Winedump
converts this information into a C function prototype. If
this fails, the file(s) specified in the -I argument are
scanned for a function prototype. If one is found it is used
for the next step of the process, code generation.
-tTRACE arguments (implies -c).
This option produces the same code as -c, except that
arguments are printed out when the function is called.
Structs that are passed by value are printed as "struct",
and functions that take variable argument lists print "...".
-f dllForward calls to dll (implies -t).
This is the most complicated level of code generation. The
same code is generated as -t, however support is added for
forwarding calls to another DLL. The DLL to forward to is
given as dll.
-DGenerate documentation.
By default, winedump generates a standard comment at the
header of each function it generates. Passing this option
makes winedump output a full header template for standard
Wine documentation, listing the parameters and return value
of the function.
-o nameSet the output dll name (default: dll).
By default, if winedump is run on DLL foo, it creates
files foo.spec, foo_main.c etc, and prefixes any
functions generated with FOO_.  If -o bar is given,
these will become bar.spec, bar_main.c and BAR_
respectively.
This option is mostly useful when generating a forwarding DLL.
-CAssume __cdecl calls (default: __stdcall).
If winebuild cannot determine the calling convention,
__stdcall is used by default, unless this option has
been given.
Unless -q is given, a warning will be printed for every
function that winedump determines the calling convention
for and which does not match the assumed calling convention.
-s numStart prototype search after symbol num.
-e numEnd prototype search after symbol num.
By passing the -s or -e options you can have winedump try to
generate code for only some functions in your DLL. This may
be used to generate a single function, for example, if you
wanted to add functionality to an existing DLL.
-S symfileSearch only prototype names found in symfile.
If you want to only generate code for a subset of exported
functions from your source DLL, you can use this option to
provide a text file containing the names of the symbols to
extract, one per line. Only the symbols present in this file
will be used in your output DLL.
-qDon't show progress (quiet).
No output is printed unless a fatal error is encountered.
-vShow lots of detail while working (verbose).
There are 3 levels of output while winedump is running. The
default level, when neither -q or -v are given, prints the
number of exported functions found in the dll, followed by
the name of each function as it is processed, and a status
indication of whether it was processed OK.  With -v given, a
lot of information is dumped while winedump works: this is
intended to help debug any problems.

Sym mode:

symDemangles C++ symbol sym and then exits.

</code></pre>
<h2>FILES</h2>
<p> <i>function_grep.pl</i></p>
<dl>
<dt>
<dd> Perl script used to retrieve a function prototype.</dl>
<p> Files output in <code>spec</code> mode for <i>foo.dll</i>: </p>
<pre>
<i>foo.spec</i>
<dl><dt><dd>This is the <i>.spec</i> file.
</dl>
<i>foo_dll.h</i>
<i>foo_main.c</i>
<dl><dt><dd>These are the source code files containing the minimum set
of code to build a stub DLL. The C file contains one
function, <i>FOO_Init</i>, which does nothing (but must be
present).
</dl>
<i>Makefile.in</i>
<dl><dt><dd>This is a template for <code>configure</code> to produce a makefile. It
is designed for a DLL that will be inserted into the Wine
source tree.
</dl>
</pre>
<h2>BUGS</h2>
<p> C++ name demangling is not fully in sync with the implementation in msvcrt. It might be useful to submit your C++ name to the testsuite for msvcrt. </p>
<p> Bugs can be reported on the <code>Wine bug tracker</code></p>
<h2>AUTHORS</h2>
<p> Jon P. Griffiths &lt;jon_p_griffiths at yahoo dot com&gt; </p>
<pre>
Michael Stefaniuc &lt;mstefani at redhat dot com&gt;
</pre>
<h2>AVAILABILITY</h2>
<p> <code>winedump</code> is part of the Wine distribution, which is available through WineHQ, the <code>Wine development headquarters</code></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-wine/">wine</a></code>(1)<br />
 <code>Wine documentation and support</code> </p>
<h2>Index</h2>
