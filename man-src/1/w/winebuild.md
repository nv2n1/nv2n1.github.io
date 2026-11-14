---
title: "winebuild(1)"
name: "winebuild"
section: "1"
letter: "w"
url: "/docs/linux/man/1-winebuild/"
description: "winebuild – Wine dll builder"
---

<h2>NAME</h2>
<p> winebuild &#8211; Wine dll builder</p>
<h2>SYNOPSIS</h2>
<p> <code>winebuild</code> [<i>options</i>]&nbsp;<wbr>[<i>inputfile</i>&#8230;]</p>
<h2>DESCRIPTION</h2>
<p> <code>winebuild</code> generates the assembly files that are necessary to build a Wine dll, which is basically a Win32 dll encapsulated inside a Unix library. </p>
<p> <code>winebuild</code> has different modes, depending on what kind of file it is asked to generate. The mode is specified by one of the mode options specified below. In addition to the mode option, various other command-line option can be specified, as described in the <code>OPTIONS</code> section.</p>
<h2>MODE OPTIONS</h2>
<p> You have to specify exactly one of the following options, depending on what you want winebuild to generate.</p>
<dl>
<dt><code>&#8211;dll</code></p>
<dd> Build an assembly file from a .spec file (see <code>SPEC FILE SYNTAX</code> for details), or from a standard Windows .def file. The .spec/.def file is specified via the <code>-E</code> option. The resulting file must be assembled and linked to the other object files to build a working Wine dll. In this mode, the <i>input files</i> should be the list of all object files that will be linked into the final dll, to allow <code>winebuild</code> to get the list of all undefined symbols that need to be imported from other dlls.</p>
<dt><code>&#8211;exe</code></p>
<dd> Build an assembly file for an executable. This is basically the same as the <code>&#8211;dll</code> mode except that it doesn&#8217;t require a .spec/.def file as input, since an executable need not export functions. Some executables however do export functions, and for those a .spec/.def file can be specified via the <code>-E</code> option. The executable is named from the .spec/.def file name if present, or explicitly through the <code>-F</code> option. The resulting file must be assembled and linked to the other object files to build a working Wine executable, and all the other object files must be listed as <i>input files.</i></p>
<dt><code>&#8211;def</code></p>
<dd> Build a .def file from a spec file. The .spec file is specified via the <code>-E</code> option. This is used when building dlls with a PE (Win32) compiler.</p>
<dt><code>&#8211;implib</code></p>
<dd> Build a PE import library from a spec file. The .spec file is specified via the <code>-E</code> option.</p>
<dt><code>&#8211;resources</code></p>
<dd> Generate a .o file containing all the input resources. This is useful when building with a PE compiler, since the PE binutils cannot handle multiple resource files as input. For a standard Unix build, the resource files are automatically included when building the spec file, so there&#8217;s no need for an intermediate .o file.</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;as-cmd=</code><i>as-command</i></p>
<dd> Specify the command to use to compile assembly files; the default is <code>as</code>.</p>
<dt><code>-b, &#8211;target=</code><i>cpu-manufacturer</i>[<code>&#8211;</code><i>kernel</i>]<code>&#8211;</code><i>os</i></p>
<dd> Specify the target CPU and platform on which the generated code will be built. The target specification is in the standard autoconf format as returned by config.sub.</p>
<dt><code>&#8211;cc-cmd=</code><i>cc-command</i></p>
<dd> Specify the C compiler to use to compile assembly files; the default is to instead use the assembler specified with <code>&#8211;as-cmd</code>.</p>
<dt><code>-d, &#8211;delay-lib=</code><i>name</i></p>
<dd> Set the delayed import mode for the specified library, which must be one of the libraries imported with the <code>-l</code> option. Delayed mode means that the library won&#8217;t be loaded until a function imported from it is actually called.</p>
<dt><code>-D&nbsp;<wbr></code><i>symbol</i></p>
<dd> Ignored for compatibility with the C compiler.</p>
<dt><code>-e, &#8211;entry=</code><i>function</i></p>
<dd> Specify the module entry point function; if not specified, the default is <code>DllMain</code> for dlls, and <code>main</code> for executables (if the standard C <code>main</code> is not defined, <code>WinMain</code> is used instead). This is only valid for Win32 modules.</p>
<dt><code>-E, &#8211;export=</code><i>filename</i></p>
<dd> Specify a .spec file (see <code>SPEC FILE SYNTAX</code> for details), or a standard Windows .def file that defines the exports of the DLL or executable that is being built.</p>
<dt><code>&#8211;external-symbols</code></p>
<dd> Allow linking to external symbols directly from the spec file. Normally symbols exported by a dll have to be defined in the dll itself; this option makes it possible to use symbols defined in another Unix library (for symbols defined in another dll, a <i>forward</i> specification must be used instead).</p>
<dt><code>-f&nbsp;<wbr></code><i>option</i></p>
<dd> Specify a code generation option. Currently <code>-fPIC</code> and <code>-fasynchronous-unwind-tables</code> are supported. Other options are ignored for compatibility with the C compiler.</p>
<dt><code>&#8211;fake-module</code></p>
<dd> Create a fake PE module for a dll or exe, instead of the normal assembly or object file. The PE module contains the resources for the module, but no executable code.</p>
<dt><code>-F, &#8211;filename=</code><i>filename</i></p>
<dd> Set the file name of the module. The default is to use the base name of the spec file (without any extension).</p>
<dt><code>-h, &#8211;help</code></p>
<dd> Display a usage message and exit.</p>
<dt><code>-H, &#8211;heap=</code><i>size</i></p>
<dd> Specify the size of the module local heap in bytes (only valid for Win16 modules); default is no local heap.</p>
<dt><code>-I&nbsp;<wbr></code><i>directory</i></p>
<dd> Ignored for compatibility with the C compiler.</p>
<dt><code>-k, &#8211;kill-at</code></p>
<dd> Remove the stdcall decorations from the symbol names in the generated .def file. Only meaningful in <code>&#8211;def</code> mode.</p>
<dt><code>-K&nbsp;<wbr></code><i>flags</i></p>
<dd> Ignored for compatibility with the C compiler.</p>
<dt><code>&#8211;large-address-aware</code></p>
<dd> Set a flag in the executable to notify the loader that this application supports address spaces larger than 2 gigabytes.</p>
<dt><code>&#8211;ld-cmd=</code><i>ld-command</i></p>
<dd> Specify the command to use to link the object files; the default is <code>ld</code>.</p>
<dt><code>-L, &#8211;library-path=</code><i>directory</i></p>
<dd> Append the specified directory to the list of directories that are searched for import libraries.</p>
<dt><code>-l, &#8211;library=</code><i>name</i></p>
<dd> Import the specified library, looking for a corresponding <i>libname.def</i> file in the directories specified with the <code>-L</code> option.</p>
<dt><code>-m16, -m32, -m64</code></p>
<dd> Generate respectively 16-bit, 32-bit or 64-bit code.</p>
<dt><code>-marm, -mthumb, -march=</code><i>option</i><code>, -mcpu=</code><i>option</i></p>
<dd> Set code generation options for the assembler.</p>
<dt><code>-M, &#8211;main-module=</code><i>module</i></p>
<dd> When building a 16-bit dll, set the name of its 32-bit counterpart to <i>module</i>. This is used to enforce that the load order for the 16-bit dll matches that of the 32-bit one.</p>
<dt><code>-N, &#8211;dll-name=</code><i>dllname</i></p>
<dd> Set the internal name of the module. It is only used in Win16 modules. The default is to use the base name of the spec file (without any extension). This is used for KERNEL, since it lives in KRNL386.EXE. It shouldn&#8217;t be needed otherwise.</p>
<dt><code>&#8211;nm-cmd=</code><i>nm-command</i></p>
<dd> Specify the command to use to get the list of undefined symbols; the default is <code>nm</code>.</p>
<dt><code>&#8211;nxcompat=</code><i>yes</i>|<i>no</i></p>
<dd> Specify whether the module is compatible with no-exec support. The default is yes.</p>
<dt><code>-o, &#8211;output=</code><i>file</i></p>
<dd> Set the name of the output file (default is standard output). If the output file name ends in .o, the text output is sent to a temporary file that is then assembled to produce the specified .o file.</p>
<dt><code>-r, &#8211;res=</code><i>rsrc.res</i></p>
<dd> Load resources from the specified binary resource file. The <i>rsrc.res</i> file can be produced from a source resource file with <code><a href="/docs/linux/man/1-wrc/">wrc</a></code>(1) (or with a Windows resource compiler).<br />
 This option is only necessary for Win16 resource files, the Win32 ones can simply listed as <i>input files</i> and will automatically be handled correctly (though the <code>-r</code> option will also work for Win32 files).</p>
<dt><code>&#8211;save-temps</code></p>
<dd> Do not delete the various temporary files that <code>winebuild</code> generates.</p>
<dt><code>&#8211;subsystem=</code><i>subsystem</i>[<code>:</code><i>major</i>[<code>.</code><i>minor</i>]]</p>
<dd> Set the subsystem of the executable, which can be one of the following:<br />
 <code>console</code> for a command line executable,<br />
 <code>windows</code> for a graphical executable,<br />
 <code>native</code> for a native-mode dll,<br />
 <code>wince</code> for a ce dll.<br />
 The entry point of a command line executable is a normal C <code>main</code> function. A <code>wmain</code> function can be used instead if you need the argument array to use Unicode strings. A graphical executable has a <code>WinMain</code> entry point.<br />
 Optionally a major and minor subsystem version can also be specified; the default subsystem version is 4.0.</p>
<dt><code>-u, &#8211;undefined=</code><i>symbol</i></p>
<dd> Add <i>symbol</i> to the list of undefined symbols when invoking the linker. This makes it possible to force a specific module of a static library to be included when resolving imports.</p>
<dt><code>-v, &#8211;verbose</code></p>
<dd> Display the various subcommands being invoked by <code>winebuild</code>.</p>
<dt><code>&#8211;version</code></p>
<dd> Display the program version and exit.</p>
<dt><code>-w, &#8211;warnings</code></p>
<dd> Turn on warnings.</dl>
<h2>SPEC FILE SYNTAX</h2>
<h3>General syntax</h3>
<p> A spec file should contain a list of ordinal declarations. The general syntax is the following: </p>
<p> <i>ordinal functype</i> [<i>flags</i>]&nbsp;<wbr><i>exportname</i>&nbsp;<wbr><code>(</code>&nbsp;<wbr>[<i>args&#8230;</i>]<i>&nbsp;<wbr></i><code>)</code>&nbsp;<wbr>[<i>handler</i>]<br />
 <i>ordinal&nbsp;<wbr></i><code>variable</code> [<i>flags</i>]&nbsp;<wbr><i>exportname</i>&nbsp;<wbr><code>(</code>&nbsp;<wbr>[<i>data&#8230;</i>]<i>&nbsp;<wbr></i><code>)</code><br />
 <i>ordinal&nbsp;<wbr></i><code>extern</code> [<i>flags</i>]&nbsp;<wbr><i>exportname</i>&nbsp;<wbr>[<i>symbolname</i>]<br />
 <i>ordinal&nbsp;<wbr></i><code>stub</code> [<i>flags</i>]&nbsp;<wbr><i>exportname</i>&nbsp;<wbr>[&nbsp;<wbr><code>(</code><i>args&#8230;</i><code>)</code>&nbsp;<wbr>]<br />
 <i>ordinal&nbsp;<wbr></i><code>equate</code> [<i>flags</i>]&nbsp;<wbr><i>exportname data</i><br />
 <code>#&nbsp;<wbr></code><i>comments</i> </p>
<p> Declarations must fit on a single line, except if the end of line is escaped using a backslash character. The <code>#</code> character anywhere in a line causes the rest of the line to be ignored as a comment. </p>
<p> <i>ordinal</i> specifies the ordinal number corresponding to the entry point, or &#8216;@&#8217; for automatic ordinal allocation (Win32 only). </p>
<p> <i>flags</i> is a series of optional flags, preceded by a &#8216;-&#8216; character. The supported flags are:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>-norelay</code></p>
<dd> The entry point is not displayed in relay debugging traces (Win32 only).</p>
<dt><code>-noname</code></p>
<dd> The entry point will be exported by ordinal instead of by name. The name is still available for importing.</p>
<dt><code>-ret16</code></p>
<dd> The function returns a 16-bit value (Win16 only).</p>
<dt><code>-ret64</code></p>
<dd> The function returns a 64-bit value (Win32 only).</p>
<dt><code>-register</code></p>
<dd> The function uses CPU register to pass arguments.</p>
<dt><code>-private</code></p>
<dd> The function cannot be imported from other dlls, it can only be accessed through GetProcAddress.</p>
<dt><code>-ordinal</code></p>
<dd> The entry point will be imported by ordinal instead of by name. The name is still exported.</p>
<dt><code>-arch=</code><i>cpu</i>[<code>,</code><i>cpu</i>]</p>
<dd> The entry point is only available on the specified CPU architecture(s). The names <code>win32</code> and <code>win64</code> match all 32-bit or 64-bit CPU architectures respectively. In 16-bit dlls, specifying <code>-arch=win32</code> causes the entry point to be exported from the 32-bit wrapper module.</dl>
</dl>
<h3>Function ordinals</h3>
<p> Syntax:<br />
 <i>ordinal functype</i> [<i>flags</i>]&nbsp;<wbr><i>exportname</i>&nbsp;<wbr><code>(</code>&nbsp;<wbr>[<i>args&#8230;</i>]<i>&nbsp;<wbr></i><code>)</code>&nbsp;<wbr>[<i>handler</i>] </p>
<p> This declaration defines a function entry point. The prototype defined by <i>exportname</i>&nbsp;<wbr><code>(</code>&nbsp;<wbr>[<i>args&#8230;</i>]<i>&nbsp;<wbr></i><code>)</code> specifies the name available for dynamic linking and the format of the arguments. &#8216;@&#8217; can be used instead of <i>exportname</i> for ordinal-only exports. </p>
<p> <i>functype</i> should be one of:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>stdcall</code></p>
<dd> for a normal Win32 function</p>
<dt><code>pascal</code></p>
<dd> for a normal Win16 function</p>
<dt><code>cdecl</code></p>
<dd> for a Win16 or Win32 function using the C calling convention</p>
<dt><code>varargs</code></p>
<dd> for a Win16 or Win32 function using the C calling convention with a variable number of arguments</p>
<dt><code>thiscall</code></p>
<dd> for a Win32 function using the <i>thiscall</i> calling convention (first parameter in %ecx register on i386)</dl>
</dl>
<p> <i>args</i> should be one or several of:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>word</code></p>
<dd> (16-bit unsigned value)</p>
<dt><code>s_word</code></p>
<dd> (16-bit signed word)</p>
<dt><code>long</code></p>
<dd> (pointer-sized integer value)</p>
<dt><code>int64</code></p>
<dd> (64-bit integer value)</p>
<dt><code>int128</code></p>
<dd> (128-bit integer value)</p>
<dt><code>float</code></p>
<dd> (32-bit floating point value)</p>
<dt><code>double</code></p>
<dd> (64-bit floating point value)</p>
<dt><code>ptr</code></p>
<dd> (linear pointer)</p>
<dt><code>str</code></p>
<dd> (linear pointer to a null-terminated ASCII string)</p>
<dt><code>wstr</code></p>
<dd> (linear pointer to a null-terminated Unicode string)</p>
<dt><code>segptr</code></p>
<dd> (segmented pointer)</p>
<dt><code>segstr</code></p>
<dd> (segmented pointer to a null-terminated ASCII string).</p>
<dt>
<dd>Note: The 16-bit and segmented pointer types are only valid for Win16 functions.</dl>
</dl>
<p> <i>handler</i> is the name of the actual C function that will implement that entry point in 32-bit mode. The handler can also be specified as <i>dllname</i><code>.</code><i>function</i> to define a forwarded function (one whose implementation is in another dll). If <i>handler</i> is not specified, it is assumed to be identical to <i>exportname.</i> </p>
<p> This first example defines an entry point for the 32-bit GetFocus() call:</p>
<dl>
<dt>
<dd> @ stdcall GetFocus() GetFocus</dl>
<p> This second example defines an entry point for the 16-bit CreateWindow() call (the ordinal 100 is just an example); it also shows how long lines can be split using a backslash:</p>
<dl>
<dt>
<dd> 100 pascal CreateWindow(ptr ptr long s_word s_word s_word \<br />
&nbsp;<wbr>s_word word word word ptr)&nbsp;<wbr>WIN_CreateWindow</dl>
<p> To declare a function using a variable number of arguments, specify the function as <code>varargs</code> and declare it in the C file with a &#8216;&#8230;&#8217; parameter for a Win32 function, or with an extra VA_LIST16 argument for a Win16 function. See the wsprintf* functions in user.exe.spec and user32.spec for an example.</p>
<h3>Variable ordinals</h3>
<p> Syntax:<br />
 <i>ordinal&nbsp;<wbr></i><code>variable</code> [<i>flags</i>]&nbsp;<wbr><i>exportname</i>&nbsp;<wbr><code>(</code>&nbsp;<wbr>[<i>data&#8230;</i>]<i>&nbsp;<wbr></i><code>)</code> </p>
<p> This declaration defines data storage as 32-bit words at the ordinal specified. <i>exportname</i> will be the name available for dynamic linking. <i>data</i> can be a decimal number or a hex number preceded by &quot;0x&quot;. The following example defines the variable VariableA at ordinal 2 and containing 4 ints:</p>
<dl>
<dt>
<dd> 2 variable VariableA(-1 0xff 0 0)</dl>
<p> This declaration only works in Win16 spec files. In Win32 you should use <code>extern</code> instead (see below).</p>
<h3>Extern ordinals</h3>
<p> Syntax:<br />
 <i>ordinal&nbsp;<wbr></i><code>extern</code> [<i>flags</i>]&nbsp;<wbr><i>exportname</i>&nbsp;<wbr>[<i>symbolname</i>] </p>
<p> This declaration defines an entry that simply maps to a C symbol (variable or function). It only works in Win32 spec files. <i>exportname</i> will point to the symbol <i>symbolname</i> that must be defined in the C code. Alternatively, it can be of the form <i>dllname</i><code>.</code><i>symbolname</i> to define a forwarded symbol (one whose implementation is in another dll). If <i>symbolname</i> is not specified, it is assumed to be identical to <i>exportname.</i></p>
<h3>Stub ordinals</h3>
<p> Syntax:<br />
 <i>ordinal&nbsp;<wbr></i><code>stub</code> [<i>flags</i>]&nbsp;<wbr><i>exportname</i>&nbsp;<wbr>[&nbsp;<wbr><code>(</code><i>args&#8230;</i><code>)</code>&nbsp;<wbr>] </p>
<p> This declaration defines a stub function. It makes the name and ordinal available for dynamic linking, but will terminate execution with an error message if the function is ever called.</p>
<h3>Equate ordinals</h3>
<p> Syntax:<br />
 <i>ordinal&nbsp;<wbr></i><code>equate</code> [<i>flags</i>]&nbsp;<wbr><i>exportname data</i> </p>
<p> This declaration defines an ordinal as an absolute value. <i>exportname</i> will be the name available for dynamic linking. <i>data</i> can be a decimal number or a hex number preceded by &quot;0x&quot;.</p>
<h2>AUTHORS</h2>
<p> <code>winebuild</code> has been worked on by many people over the years. The main authors are Robert J. Amstadt, Alexandre Julliard, Martin von Loewis, Ulrich Weigand and Eric Youngdale. Many other people have contributed new features and bug fixes. For a complete list, see the git commit logs.</p>
<h2>BUGS</h2>
<p> It is not yet possible to use a PE-format dll in an import specification; only Wine dlls can be imported. </p>
<p> Bugs can be reported on the <code>Wine bug tracker</code></p>
<h2>AVAILABILITY</h2>
<p> <code>winebuild</code> is part of the Wine distribution, which is available through WineHQ, the <code>Wine development headquarters</code></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-wine/">wine</a></code>(1), <code><a href="/docs/linux/man/1-winegcc/">winegcc</a></code>(1), <code><a href="/docs/linux/man/1-wrc/">wrc</a></code>(1),<br />
 <code>Wine documentation and support</code> </p>
<h2>Index</h2>
