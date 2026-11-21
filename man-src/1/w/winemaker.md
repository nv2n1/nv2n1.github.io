---

title: "winemaker(1)"
name: "winemaker"
section: "1"
letter: "w"
url: "/docs/linux/man/1-winemaker/"
description: "winemaker – generate a build infrastructure for compiling Windows programs on Unix"
---

<p> winemaker &#8211; generate a build infrastructure for compiling Windows programs on Unix</p>
<h2>SYNOPSIS</h2>
<p> <code>winemaker </code> [ <code>&#8211;nobanner </code>] [ <code>&#8211;backup </code>| <code>&#8211;nobackup </code>] [ &#8211;nosource-fix ] </p>
<p>&nbsp;<wbr>&nbsp;<wbr>[ <code>&#8211;lower-none </code>| <code>&#8211;lower-all </code>| <code>&#8211;lower-uppercase </code> ] </p>
<p>&nbsp;<wbr>&nbsp;<wbr>[ <code>&#8211;lower-include </code>| <code>&#8211;nolower-include </code>]&nbsp;<wbr>[<code> &#8211;mfc </code>| <code>&#8211;nomfc </code> ] </p>
<p>&nbsp;<wbr>&nbsp;<wbr>[ <code>&#8211;guiexe </code>| <code>&#8211;windows </code>| <code>&#8211;cuiexe </code>| <code>&#8211;console </code>| <code>&#8211;dll </code>| <code>&#8211;lib </code> ] </p>
<p>&nbsp;<wbr>&nbsp;<wbr>[ <code>-D</code><i>macro</i>[=<i>defn</i>] ] [<i>&nbsp;<wbr></i><code>-I</code><i>dir</i> ]&nbsp;<wbr>[ <code>-P</code><i>dir</i> ] [ <code>-i</code><i>dll</i> ] [ <code>-L</code><i>dir</i> ] [ <code>-l</code><i>library </i> ] </p>
<p>&nbsp;<wbr>&nbsp;<wbr>[ <code>&#8211;nodlls </code>] [ <code>&#8211;nomsvcrt </code>] [ <code>&#8211;interactive </code>] [ <code>&#8211;single-target </code><i>name</i> ] </p>
<p>&nbsp;<wbr>&nbsp;<wbr>[ <code>&#8211;generated-files </code>] [ <code>&#8211;nogenerated-files </code>] </p>
<p>&nbsp;<wbr>&nbsp;<wbr>[ <code>&#8211;wine32 </code>]<br />
 <i> work_directory</i> | <i>project_file</i> | <i>workspace_file</i> </p>
<h2>DESCRIPTION</h2>
<p> <code>winemaker</code> is a perl script designed to help you bootstrap the process of converting your Windows sources to Winelib programs. </p>
<p> In order to do this <code>winemaker</code> can perform the following operations: </p>
<p> &#8211; rename your source files and directories to lowercase in the event they got all uppercased during the transfer. </p>
<p> &#8211; perform DOS to Unix (CRLF to LF) conversions. </p>
<p> &#8211; scan the include statements and resource file references to replace the backslashes with forward slashes. </p>
<p> &#8211; during the above step <code>winemaker</code> will also perform a case insensitive search of the referenced file in the include path and rewrite the include statement with the right case if necessary. </p>
<p> &#8211; <code>winemaker</code> will also check other more exotic issues like <i>#pragma pack</i> usage, use of <i>afxres.h</i> in non MFC projects, and more. Whenever it encounters something out of the ordinary, it will warn you about it. </p>
<p> &#8211; <code>winemaker</code> can also scan a complete directory tree at once, guess what are the executables and libraries you are trying to build, match them with source files, and generate the corresponding <i>Makefile</i>. </p>
<p> &#8211; finally <code>winemaker</code> will generate a global <i>Makefile</i> for normal use. </p>
<p> &#8211; <code>winemaker</code> knows about MFC-based project and will generate customized files. </p>
<p> &#8211; <code>winemaker</code> can read existing project files. It supports dsp, dsw, vcproj and sln files. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;nobanner</code></dt>
<dd> Disable the printing of the banner.</dd>
<dt><code>&#8211;backup</code></dt>
<dd> Perform a backup of all the modified source files. This is the default.</dd>
<dt><code>&#8211;nobackup</code></dt>
<dd> Do not backup modified source files.</dd>
<dt><code>&#8211;nosource-fix</code></dt>
<dd> Do no try to fix the source files (e.g. DOS to Unix conversion). This prevents complaints if the files are readonly.</dd>
<dt><code>&#8211;lower-all</code></dt>
<dd> Rename all files and directories to lowercase.</dd>
<dt><code>&#8211;lower-uppercase</code></dt>
<dd> Only rename files and directories that have an all uppercase name. So <i>HELLO.C</i> would be renamed but not <i>World.c</i>.</dd>
<dt><code>&#8211;lower-none</code></dt>
<dd> Do not rename files and directories to lower case. Note that this does not prevent the renaming of a file if its extension cannot be handled as is, e.g. &quot;.Cxx&quot;. This is the default.</dd>
<dt><code>&#8211;lower-include</code></dt>
<dd> When the file corresponding to an include statement (or other form of file reference for resource files) cannot be found, convert that filename to lowercase. This is the default.</dd>
<dt><code>&#8211;nolower-include</code></dt>
<dd> Do not modify the include statement if the referenced file cannot be found.</dd>
<dt><code>&#8211;guiexe </code>| <code>&#8211;windows</code></dt>
<dd> Assume a graphical application when an executable target or a target of unknown type is found. This is the default.</dd>
<dt><code>&#8211;cuiexe </code>| <code>&#8211;console</code></dt>
<dd> Assume a console application when an executable target or a target of unknown type is found.</dd>
<dt><code>&#8211;dll</code></dt>
<dd> Assume a dll when a target of unknown type is found, i.e. when <code>winemaker</code> is unable to determine whether it is an executable, a dll, or a static library,</dd>
<dt><code>&#8211;lib</code></dt>
<dd> Assume a static library when a target of unknown type is found, i.e. when <code>winemaker</code> is unable to determine whether it is an executable, a dll, or a static library,</dd>
<dt><code>&#8211;mfc</code></dt>
<dd> Specify that the targets are MFC based. In such a case <code>winemaker</code> adapts the include and library paths accordingly, and links the target with the MFC library.</dd>
<dt><code>&#8211;nomfc</code></dt>
<dd> Specify that targets are not MFC-based. This option disables use of MFC libraries even if <code>winemaker</code> encounters files <i>stdafx.cpp</i> or <i>stdafx.h</i> that would cause it to enable MFC automatically if neither <code>&#8211;nomfc</code> nor <code>&#8211;mfc</code> was specified.</dd>
<dt><code>-D</code><i>macro</i>[<code>=</code><i>defn</i>]</dt>
<dd> Add the specified macro definition to the global list of macro definitions.</dd>
<dt><code>-I</code><i>dir</i></dt>
<dd> Append the specified directory to the global include path.</dd>
<dt><code>-P</code><i>dir</i></dt>
<dd> Append the specified directory to the global dll path.</dd>
<dt><code>-i</code><i>dll</i></dt>
<dd> Add the Winelib library to the global list of Winelib libraries to import.</dd>
<dt><code>-L</code><i>dir</i></dt>
<dd> Append the specified directory to the global library path.</dd>
<dt><code>-l</code><i>library</i></dt>
<dd> Add the specified library to the global list of libraries to link with.</dd>
<dt><code>&#8211;nodlls</code></dt>
<dd> Do not use the standard set of Winelib libraries for imports. That is, any DLL your code uses must be explicitly passed with <code>-i</code> options. The standard set of libraries is: <i>odbc32.dll</i>, <i>odbccp32.dll</i>, <i>ole32.dll</i>, <i>oleaut32.dll</i> and <i>winspool.drv</i>.</dd>
<dt><code>&#8211;nomsvcrt</code></dt>
<dd> Set some options to tell <code>winegcc</code> not to compile against msvcrt. Use this option if you have cpp-files that include <i>&lt;string&gt;</i>.</dd>
<dt><code>&#8211;interactive</code></dt>
<dd> Use interactive mode. In this mode <code>winemaker</code> will ask you to confirm the list of targets for each directory, and then to provide directory and target specific options.</dd>
<dt><code>&#8211;single-target</code><i> name</i></dt>
<dd> Specify that there is only one target, called <i>name</i>.</dd>
<dt><code>&#8211;generated-files</code></dt>
<dd> Generate the <i>Makefile</i>. This is the default.</dd>
<dt><code>&#8211;nogenerated-files</code></dt>
<dd> Do not generate the <i>Makefile</i>.</dd>
<dt><code>&#8211;wine32</code></dt>
<dd> Generate a 32-bit target. This is useful on wow64 systems. Without that option the default architecture is used. </dd>
</dl>
<h2>EXAMPLES</h2>
<p> Here is a typical <code>winemaker</code> use: </p>
<p> $ winemaker &#8211;lower-uppercase -DSTRICT . </p>
<p> The above tells <code>winemaker</code> to scan the current directory and its subdirectories for source files. Whenever if finds a file or directory which name is all uppercase, it should rename it to lowercase. It should then fix all these source files for compilation with Winelib and generate <i>Makefile</i>s. The <code>-DSTRICT</code> specifies that the <code>STRICT</code> macro must be set when compiling these sources. Finally a <i>Makefile</i> will be created. </p>
<p> The next step would be: </p>
<p> $ make </p>
<p> If at this point you get compilation errors (which is quite likely for a reasonably sized project) then you should consult the Winelib User Guide to find tips on how to resolve them. </p>
<p> For an MFC-based project you would have to run the following commands instead: </p>
<p> $ winemaker &#8211;lower-uppercase &#8211;mfc .<br />
 $ make </p>
<p> For an existing project-file you would have to run the following commands: </p>
<p> $ winemaker myproject.dsp<br />
 $ make </p>
<h2>TODO / BUGS</h2>
<p> In some cases you will have to edit the <i>Makefile</i> or source files manually. </p>
<p> Assuming that the windows executable/library is available, we could use <code>winedump</code> to determine what kind of executable it is (graphical or console), which libraries it is linked with, and which functions it exports (for libraries). We could then restore all these settings for the corresponding Winelib target. </p>
<p> Furthermore <code>winemaker</code> is not very good at finding the library containing the executable: it must either be in the current directory or in the <code>LD_LIBRARY_PATH</code>. </p>
<p> <code>winemaker</code> does not support message files and the message compiler yet. </p>
<p> Bugs can be reported on the <code>Wine bug tracker</code></p>
<h2>AUTHORS</h2>
<p> François Gouget for CodeWeavers<br />
 Dimitrie O. Paun<br />
 André Hentschel</p>
<h2>AVAILABILITY</h2>
<p> <code>winemaker</code> is part of the Wine distribution, which is available through WineHQ, the <code>Wine development headquarters</code></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-wine/">wine</a></code>(1),<br />
 <code>Wine documentation and support</code> </p>
