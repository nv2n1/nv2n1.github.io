---
title: "x86_64-w64-mingw32-dlltool(1)"
name: "x86_64-w64-mingw32-dlltool"
section: "1"
letter: "x"
url: "/docs/linux/man/1-x86_64-w64-mingw32-dlltool/"
description: "dlltool – Create files needed to build and use DLLs."
---

<h2 class="name">NAME</h2>
<p> dlltool &#8211; Create files needed to build and use DLLs. </p>
<h2>SYNOPSIS</h2>
<p> dlltool [<code>-d</code>|<code>&#8211;input-def</code> <i>def-file-name</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>-b</code>|<code>&#8211;base-file</code>&nbsp;<wbr><i>base-file-name</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>-e</code>|<code>&#8211;output-exp</code>&nbsp;<wbr><i>exports-file-name</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>-z</code>|<code>&#8211;output-def</code>&nbsp;<wbr><i>def-file-name</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>-l</code>|<code>&#8211;output-lib</code>&nbsp;<wbr><i>library-file-name</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>-y</code>|<code>&#8211;output-delaylib</code>&nbsp;<wbr><i>library-file-name</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>&#8211;export-all-symbols</code>]&nbsp;<wbr>[<code>&#8211;no-export-all-symbols</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>&#8211;exclude-symbols</code>&nbsp;<wbr><i>list</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>&#8211;no-default-excludes</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>-S</code>|<code>&#8211;as</code>&nbsp;<wbr><i>path-to-assembler</i>]&nbsp;<wbr>[<code>-f</code>|<code>&#8211;as-flags</code>&nbsp;<wbr><i>options</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>-D</code>|<code>&#8211;dllname</code>&nbsp;<wbr><i>name</i>]&nbsp;<wbr>[<code>-m</code>|<code>&#8211;machine</code>&nbsp;<wbr><i>machine</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>-a</code>|<code>&#8211;add-indirect</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>-U</code>|<code>&#8211;add-underscore</code>]&nbsp;<wbr>[<code>&#8211;add-stdcall-underscore</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>-k</code>|<code>&#8211;kill-at</code>]&nbsp;<wbr>[<code>-A</code>|<code>&#8211;add-stdcall-alias</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>-p</code>|<code>&#8211;ext-prefix-alias</code>&nbsp;<wbr><i>prefix</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>-x</code>|<code>&#8211;no-idata4</code>]&nbsp;<wbr>[<code>-c</code>|<code>&#8211;no-idata5</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>&#8211;use-nul-prefixed-import-tables</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>-I</code>|<code>&#8211;identify</code>&nbsp;<wbr><i>library-file-name</i>]&nbsp;<wbr>[<code>&#8211;identify-strict</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>-i</code>|<code>&#8211;interwork</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>-n</code>|<code>&#8211;nodelete</code>]&nbsp;<wbr>[<code>-t</code>|<code>&#8211;temp-prefix</code>&nbsp;<wbr><i>prefix</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>-v</code>|<code>&#8211;verbose</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>-h</code>|<code>&#8211;help</code>]&nbsp;<wbr>[<code>-V</code>|<code>&#8211;version</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>&#8211;no-leading-underscore</code>]&nbsp;<wbr>[<code>&#8211;leading-underscore</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>[object-file &#8230;]</p>
<h2>DESCRIPTION</h2>
<p> <code>dlltool</code> reads its inputs, which can come from the <code>-d</code> and <code>-b</code> options as well as object files specified on the command line. It then processes these inputs and if the <code>-e</code> option has been specified it creates a exports file. If the <code>-l</code> option has been specified it creates a library file and if the <code>-z</code> option has been specified it creates a def file. Any or all of the <code>-e</code>, <code>-l</code> and <code>-z</code> options can be present in one invocation of dlltool. </p>
<p> When creating a <font SIZE="-1">DLL,</font> along with the source for the <font SIZE="-1">DLL,</font> it is necessary to have three other files. <code>dlltool</code> can help with the creation of these files. </p>
<p> The first file is a <i>.def</i> file which specifies which functions are exported from the <font SIZE="-1">DLL,</font> which functions the <font SIZE="-1">DLL</font> imports, and so on. This is a text file and can be created by hand, or <code>dlltool</code> can be used to create it using the <code>-z</code> option. In this case <code>dlltool</code> will scan the object files specified on its command line looking for those functions which have been specially marked as being exported and put entries for them in the <i>.def</i> file it creates. </p>
<p> In order to mark a function as being exported from a <font SIZE="-1">DLL,</font> it needs to have an <code>-export:&lt;name_of_function&gt;</code> entry in the <code>.drectve</code> section of the object file. This can be done in C by using the <i>asm()</i> operator: </p>
<pre><code>
asm(".section .drectve");
asm(".ascii \"-export:my_func\"");

int my_func(void)
{
    ...
}
</code></pre>
<p> The second file needed for <font SIZE="-1">DLL</font> creation is an exports file. This file is linked with the object files that make up the body of the <font SIZE="-1">DLL</font> and it handles the interface between the <font SIZE="-1">DLL</font> and the outside world. This is a binary file and it can be created by giving the <code>-e</code> option to <code>dlltool</code> when it is creating or reading in a <i>.def</i> file. </p>
<p> The third file needed for <font SIZE="-1">DLL</font> creation is the library file that programs will link with in order to access the functions in the <font SIZE="-1">DLL </font>(an `import library&#8217;). This file can be created by giving the <code>-l</code> option to dlltool when it is creating or reading in a <i>.def</i> file. </p>
<p> If the <code>-y</code> option is specified, dlltool generates a delay-import library that can be used instead of the normal import library to allow a program to link to the dll only as soon as an imported function is called for the first time. The resulting executable will need to be linked to the static delayimp library containing _<i>_delayLoadHelper2()</i>, which in turn will import LoadLibraryA and GetProcAddress from kernel32. </p>
<p> <code>dlltool</code> builds the library file by hand, but it builds the exports file by creating temporary files containing assembler statements and then assembling these. The <code>-S</code> command line option can be used to specify the path to the assembler that dlltool will use, and the <code>-f</code> option can be used to pass specific flags to that assembler. The <code>-n</code> can be used to prevent dlltool from deleting these temporary assembler files when it is done, and if <code>-n</code> is specified twice then this will prevent dlltool from deleting the temporary object files it used to build the library. </p>
<p> Here is an example of creating a <font SIZE="-1">DLL</font> from a source file <code>dll.c</code> and also creating a program (from an object file called <code>program.o</code>) that uses that <font SIZE="-1">DLL:</font> </p>
<pre>
          gcc -c dll.c
          dlltool -e exports.o -l dll.lib dll.o
          gcc dll.o exports.o -o dll.dll
          gcc program.o dll.lib -o program
</pre>
<p> <code>dlltool</code> may also be used to query an existing import library to determine the name of the <font SIZE="-1">DLL</font> to which it is associated. See the description of the <code>-I</code> or <code>&#8211;identify</code> option.</p>
<h2>OPTIONS</h2>
<p> The command line options have the following meanings:</p>
<dl>
<dt><code>-d</code> <i>filename</i></p>
<dd>
<dt><code>&#8211;input-def</code> <i>filename</i></p>
<dd> Specifies the name of a <i>.def</i> file to be read in and processed.</p>
<dt><code>-b</code> <i>filename</i></p>
<dd>
<dt><code>&#8211;base-file</code> <i>filename</i></p>
<dd> Specifies the name of a base file to be read in and processed. The contents of this file will be added to the relocation section in the exports file generated by dlltool.</p>
<dt><code>-e</code> <i>filename</i></p>
<dd>
<dt><code>&#8211;output-exp</code> <i>filename</i></p>
<dd> Specifies the name of the export file to be created by dlltool.</p>
<dt><code>-z</code> <i>filename</i></p>
<dd>
<dt><code>&#8211;output-def</code> <i>filename</i></p>
<dd> Specifies the name of the <i>.def</i> file to be created by dlltool.</p>
<dt><code>-l</code> <i>filename</i></p>
<dd>
<dt><code>&#8211;output-lib</code> <i>filename</i></p>
<dd> Specifies the name of the library file to be created by dlltool.</p>
<dt><code>-y</code> <i>filename</i></p>
<dd>
<dt><code>&#8211;output-delaylib</code> <i>filename</i></p>
<dd> Specifies the name of the delay-import library file to be created by dlltool.</p>
<dt><code>&#8211;export-all-symbols</code></p>
<dd> Treat all global and weak defined symbols found in the input object files as symbols to be exported. There is a small list of symbols which are not exported by default; see the <code>&#8211;no-default-excludes</code> option. You may add to the list of symbols to not export by using the <code>&#8211;exclude-symbols</code> option.</p>
<dt><code>&#8211;no-export-all-symbols</code></p>
<dd> Only export symbols explicitly listed in an input <i>.def</i> file or in <code>.drectve</code> sections in the input object files. This is the default behaviour. The <code>.drectve</code> sections are created by <code>dllexport</code> attributes in the source code.</p>
<dt><code>&#8211;exclude-symbols</code> <i>list</i></p>
<dd> Do not export the symbols in <i>list</i>. This is a list of symbol names separated by comma or colon characters. The symbol names should not contain a leading underscore. This is only meaningful when <code>&#8211;export-all-symbols</code> is used.</p>
<dt><code>&#8211;no-default-excludes</code></p>
<dd> When <code>&#8211;export-all-symbols</code> is used, it will by default avoid exporting certain special symbols. The current list of symbols to avoid exporting is <code>DllMain@12</code>, <code>DllEntryPoint@0</code>, <code>impure_ptr</code>. You may use the <code>&#8211;no-default-excludes</code> option to go ahead and export these special symbols. This is only meaningful when <code>&#8211;export-all-symbols</code> is used.</p>
<dt><code>-S</code> <i>path</i></p>
<dd>
<dt><code>&#8211;as</code> <i>path</i></p>
<dd> Specifies the path, including the filename, of the assembler to be used to create the exports file.</p>
<dt><code>-f</code> <i>options</i></p>
<dd>
<dt><code>&#8211;as-flags</code> <i>options</i></p>
<dd> Specifies any specific command line options to be passed to the assembler when building the exports file. This option will work even if the <code>-S</code> option is not used. This option only takes one argument, and if it occurs more than once on the command line, then later occurrences will override earlier occurrences. So if it is necessary to pass multiple options to the assembler they should be enclosed in double quotes.</p>
<dt><code>-D</code> <i>name</i></p>
<dd>
<dt><code>&#8211;dll-name</code> <i>name</i></p>
<dd> Specifies the name to be stored in the <i>.def</i> file as the name of the <font SIZE="-1">DLL</font> when the <code>-e</code> option is used. If this option is not present, then the filename given to the <code>-e</code> option will be used as the name of the <font SIZE="-1">DLL.</font></p>
<dt><code>-m</code> <i>machine</i></p>
<dd>
<dt><code>-machine</code> <i>machine</i></p>
<dd> Specifies the type of machine for which the library file should be built. <code>dlltool</code> has a built in default type, depending upon how it was created, but this option can be used to override that. This is normally only useful when creating DLLs for an <font SIZE="-1">ARM</font> processor, when the contents of the <font SIZE="-1">DLL</font> are actually encode using Thumb instructions.</p>
<dt><code>-a</code></p>
<dd>
<dt><code>&#8211;add-indirect</code></p>
<dd> Specifies that when <code>dlltool</code> is creating the exports file it should add a section which allows the exported functions to be referenced without using the import library. Whatever the hell that means!</p>
<dt><code>-U</code></p>
<dd>
<dt><code>&#8211;add-underscore</code></p>
<dd> Specifies that when <code>dlltool</code> is creating the exports file it should prepend an underscore to the names of <i>all</i> exported symbols.</p>
<dt><code>&#8211;no-leading-underscore</code></p>
<dd>
<dt><code>&#8211;leading-underscore</code></p>
<dd> Specifies whether standard symbol should be forced to be prefixed, or not.</p>
<dt><code>&#8211;add-stdcall-underscore</code></p>
<dd> Specifies that when <code>dlltool</code> is creating the exports file it should prepend an underscore to the names of exported <i>stdcall</i> functions. Variable names and non-stdcall function names are not modified. This option is useful when creating GNU-compatible import libs for third party DLLs that were built with MS-Windows tools.</p>
<dt><code>-k</code></p>
<dd>
<dt><code>&#8211;kill-at</code></p>
<dd> Specifies that when <code>dlltool</code> is creating the exports file it should not append the string <code>@ &lt;number&gt;</code>. These numbers are called ordinal numbers and they represent another way of accessing the function in a <font SIZE="-1">DLL,</font> other than by name.</p>
<dt><code>-A</code></p>
<dd>
<dt><code>&#8211;add-stdcall-alias</code></p>
<dd> Specifies that when <code>dlltool</code> is creating the exports file it should add aliases for stdcall symbols without <code>@ &lt;number&gt;</code> in addition to the symbols with <code>@ &lt;number&gt;</code>.</p>
<dt><code>-p</code></p>
<dd>
<dt><code>&#8211;ext-prefix-alias</code> <i>prefix</i></p>
<dd> Causes <code>dlltool</code> to create external aliases for all <font SIZE="-1">DLL</font> imports with the specified prefix. The aliases are created for both external and import symbols with no leading underscore.</p>
<dt><code>-x</code></p>
<dd>
<dt><code>&#8211;no-idata4</code></p>
<dd> Specifies that when <code>dlltool</code> is creating the exports and library files it should omit the <tt>&quot;.idata4&quot;</tt> section. This is for compatibility with certain operating systems.</p>
<dt><code>&#8211;use-nul-prefixed-import-tables</code></p>
<dd> Specifies that when <code>dlltool</code> is creating the exports and library files it should prefix the <tt>&quot;.idata4&quot;</tt> and <tt>&quot;.idata5&quot;</tt> by zero an element. This emulates old gnu import library generation of <tt>&quot;dlltool&quot;</tt>. By default this option is turned off.</p>
<dt><code>-c</code></p>
<dd>
<dt><code>&#8211;no-idata5</code></p>
<dd> Specifies that when <code>dlltool</code> is creating the exports and library files it should omit the <tt>&quot;.idata5&quot;</tt> section. This is for compatibility with certain operating systems.</p>
<dt><code>-I</code> <i>filename</i></p>
<dd>
<dt><code>&#8211;identify</code> <i>filename</i></p>
<dd> Specifies that <code>dlltool</code> should inspect the import library indicated by <i>filename</i> and report, on <tt>&quot;stdout&quot;</tt>, the name(s) of the associated <font SIZE="-1">DLL</font>(s). This can be performed in addition to any other operations indicated by the other options and arguments. <code>dlltool</code> fails if the import library does not exist or is not actually an import library. See also <code>&#8211;identify-strict</code>.</p>
<dt><code>&#8211;identify-strict</code></p>
<dd> Modifies the behavior of the <code>&#8211;identify</code> option, such that an error is reported if <i>filename</i> is associated with more than one <font SIZE="-1">DLL.</font></p>
<dt><code>-i</code></p>
<dd>
<dt><code>&#8211;interwork</code></p>
<dd> Specifies that <code>dlltool</code> should mark the objects in the library file and exports file that it produces as supporting interworking between <font SIZE="-1">ARM</font> and Thumb code.</p>
<dt><code>-n</code></p>
<dd>
<dt><code>&#8211;nodelete</code></p>
<dd> Makes <code>dlltool</code> preserve the temporary assembler files it used to create the exports file. If this option is repeated then dlltool will also preserve the temporary object files it uses to create the library file.</p>
<dt><code>-t</code> <i>prefix</i></p>
<dd>
<dt><code>&#8211;temp-prefix</code> <i>prefix</i></p>
<dd> Makes <code>dlltool</code> use <i>prefix</i> when constructing the names of temporary assembler and object files. By default, the temp file prefix is generated from the pid.</p>
<dt><code>-v</code></p>
<dd>
<dt><code>&#8211;verbose</code></p>
<dd> Make dlltool describe what it is doing.</p>
<dt><code>-h</code></p>
<dd>
<dt><code>&#8211;help</code></p>
<dd> Displays a list of command line options and then exits.</p>
<dt><code>-V</code></p>
<dd>
<dt><code>&#8211;version</code></p>
<dd> Displays dlltool&#8217;s version number and then exits.</p>
<dt><code>@</code><i>file</i></p>
<dd> Read command-line options from <i>file</i>. The options read are inserted in place of the original @<i>file</i> option. If <i>file</i> does not exist, or cannot be read, then the option will be treated literally, and not removed. </p>
<p> Options in <i>file</i> are separated by whitespace. A whitespace character may be included in an option by surrounding the entire option in either single or double quotes. Any character (including a backslash) may be included by prefixing the character to be included with a backslash. The <i>file</i> may itself contain additional @<i>file</i> options; any such options will be processed recursively.</dl>
<h2>SEE ALSO</h2>
<p> The Info pages for <i>binutils</i>.</p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 1991-2014 Free Software Foundation, Inc. </p>
<p> Permission is granted to copy, distribute and/or modify this document under the terms of the <font SIZE="-1">GNU</font> Free Documentation License, Version 1.3 or any later version published by the Free Software Foundation; with no Invariant Sections, with no Front-Cover Texts, and with no Back-Cover Texts. A copy of the license is included in the section entitled &#8220;<font SIZE="-1">GNU</font> Free Documentation License&#8221;. </p>
<h2>Index</h2>
