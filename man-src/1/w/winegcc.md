---
title: "winegcc(1)"
name: "winegcc"
section: "1"
letter: "w"
url: "/docs/linux/man/1-winegcc/"
description: "winegcc – Wine C and C++ MinGW Compatible Compiler"
---

<h2>NAME</h2>
<p> winegcc &#8211; Wine C and C++ MinGW Compatible Compiler</p>
<h2>SYNOPSIS</h2>
<p> <code>winegcc</code> [<i>options</i>] <i>infile</i>&#8230;</p>
<h2>DESCRIPTION</h2>
<p> <code>winegcc </code> is a gcc wrapper which tries to provide a MinGW compatible compiler under Linux. This is most useful to Win32 developers who can simply take their MinGW code from Windows, and recompile it without modifications under Winelib on Linux. wineg++ accepts mostly the same options as winegcc. </p>
<p> The goal of winegcc is to be able to simply replace gcc/g++/windres with winegcc/wineg++/wrc in a MinGW Makefile, and just recompile the application using Winelib under Wine. While typically there are small adjustments that must be made to the application source code and/or Makefile, it is quite easy to do them in a fashion that is compatible between the MinGW and Wine environments. </p>
<p> This manual will document only the differences from gcc; please consult the gcc manual for more information on those options. </p>
<h2>OPTIONS</h2>
<p> <code>gcc options:</code> All gcc options are supported, and are passed along to the backend compiler.</p>
<dl>
<dt><code>-B</code><i>prefix</i></p>
<dd> This option specifies where to find the executables, libraries, include files, and data files of the compiler itself. This is a standard gcc option that has been extended to recognize a <i>prefix</i> ending with &#8216;/tools/winebuild&#8217;, in which case winegcc enters a special mode for building Wine itself. Developers should avoid prefixes ending with the magic suffix, or if that is not possible, simply express it differently, such as &#8216;/tools/winebuild/&#8217;, to avoid the special behaviour.</p>
<dt><code>-fno-short-wchar</code></p>
<dd> Override the underlying type for wchar_t to be the default for the target, instead of using short unsigned int, which is the default for Win32.</p>
<dt><code>-mconsole</code></p>
<dd> This option passes &#8216;&#8211;subsystem console&#8217; to winebuild, to build console applications. It is the default.</p>
<dt><code>-mno-cygwin</code></p>
<dd> Use Wine implementation of MSVCRT, instead of linking against the host system libc. This is necessary for the vast majority of Win32 applications, as they typically depend on various features of MSVCRT. This switch is also used by the MinGW compiler to link against MSVCRT on Windows, instead of linking against Cygwin libc. Sharing the syntax with MinGW makes it very easy to write Makefiles that work under Wine, MinGW+MSYS, or MinGW+Cygwin.</p>
<dt><code>-municode</code></p>
<dd> Set the default entry point of the application to be the Unicode <code>wmain()</code> instead of the standard <code>main()</code>.</p>
<dt><code>-mwindows</code></p>
<dd> This option adds -lgdi32, -lcomdlg32, and -lshell32 to the list of default libraries, and passes &#8216;&#8211;subsystem windows&#8217; to winebuild to build graphical applications.</p>
<dt><code>-nodefaultlibs</code></p>
<dd> Do not use the standard system libraries when linking. These include at a minimum -lkernel32, -luser32, -ladvapi32, and any default libraries used by the backend compiler. The -mwindows option augments the list of default libraries as described above.</p>
<dt><code>-nostartfiles</code></p>
<dd> Do not add the winecrt0 library when linking.</p>
<dt><code>-Wb,</code><i>option</i></p>
<dd> Pass an option to winebuild. If <i>option</i> contains commas, it is split into multiple options at the commas.</dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>WINEBUILD</code></p>
<dd> Specifies the path and name of the <code>winebuild</code> binary that will be launched automatically by <code>winegcc</code>. If not set, <code>winegcc</code> will look for a file named <i>winebuild</i> in the path.</dl>
<h2>DEFINES</h2>
<p> winegcc defines __WINE__, for code that needs to know when it is being compiled under Wine. It also defines WIN32, _WIN32, __WIN32, __WIN32__, __WINNT, and __WINNT__ for compatibility with MinGW.</p>
<h2>BUGS</h2>
<p> The dllimport/dllexport attributes are not supported at the moment, due to lack of support for these features in the ELF version of gcc. </p>
<p> Static linking is not currently supported against Wine DLLs. As a result, the -static, &#8211;static, and -Wl,-static options will generate an error. </p>
<p> Bugs can be reported on the <code>Wine bug tracker</code></p>
<h2>AUTHORS</h2>
<p> <code>winegcc</code> was written by Dimitrie O. Paun.</p>
<h2>AVAILABILITY</h2>
<p> <code>winegcc</code> is part of the Wine distribution, which is available through WineHQ, the <code>Wine development headquarters</code></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-gcc/">gcc</a></code>(1), <code><a href="/docs/linux/man/1-winebuild/">winebuild</a></code>(1), <code><a href="/docs/linux/man/1-wrc/">wrc</a></code>(1), <code><a href="/docs/linux/man/1-wine/">wine</a></code>(1),<br />
 <code>Wine documentation and support</code> </p>
<h2>Index</h2>
