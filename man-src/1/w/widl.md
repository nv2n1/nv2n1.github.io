---
title: "widl(1)"
name: "widl"
section: "1"
letter: "w"
url: "/docs/linux/man/1-widl/"
description: "widl – Wine Interface Definition Language (IDL) compiler"
---

<h2>NAME</h2>
<p> widl &#8211; Wine Interface Definition Language (IDL) compiler</p>
<h2>SYNOPSIS</h2>
<p> <code>widl</code> [<i>options</i>] <i>IDL_file</i><br />
 <code>widl</code> [<i>options</i>] <code>&#8211;dlldata-only</code> <i>name1</i> [<i>name2</i>&#8230;]</p>
<h2>DESCRIPTION</h2>
<p> When no options are used the program will generate a header file, and possibly client and server stubs, proxy and dlldata files, a typelib, and a UUID file, depending on the contents of the IDL file. If any of the options <code>-c</code>, <code>-h</code>, <code>-p</code>, <code>-s</code>, <code>-t</code>, <code>-u</code> or <code>&#8211;local-stubs</code> is given, <code>widl</code> will only generate the requested files, and no others. When run with <code>&#8211;dlldata-only</code>, widl will only generate a dlldata file, and it will contain a list of the names passed as arguments. Usually the way this file is updated is that each time <code>widl</code> is run, it reads any existing dlldata file, and if necessary regenerates it with the same list of names, but with the present proxy file included. </p>
<p> When run without any arguments, <code>widl</code> will print a help message. </p>
<h2>OPTIONS</h2>
<p> <code>General options:</code></p>
<dl>
<dt><code>-V</code></p>
<dd> Print version number and exit.</p>
<dt><code>-o, &#8211;output=</code><i>name</p>
<dd> Set the name of the output file. When generating multiple output files, this sets only the base name of the file; the respective output files are then named name</i>.h, <i>name</i>_p.c, etc. If a full file name with extension is specified, only that file is generated.</p>
<dt><code>-b </code><i>cpu-manufacturer</i>[<code>&#8211;</code><i>kernel</i>]<code>&#8211;</code><i>os</i></p>
<dd> Set the target architecture when cross-compiling. The target specification is in the standard autoconf format as returned by <code>config.sub</code>.</dl>
<p> <code>Header options:</code></p>
<dl>
<dt><code>-h</code></p>
<dd> Generate header files. The default output filename is <i>infile</i><code>.h</code>.</p>
<dt><code>&#8211;oldnames</code></p>
<dd> Use old naming conventions.</dl>
<p> <code>Type library options:</code></p>
<dl>
<dt><code>-t</code></p>
<dd> Generate a type library. The default output filename is <i>infile</i><code>.tlb</code>. If the output file name ends in <code>.res</code>, a binary resource file containing the type library is generated instead.</p>
<dt><code>-m32, -m64</code></p>
<dd> Generate a Win32 or Win64 type library respectively.</dl>
<p> <code>UUID file options:</code></p>
<dl>
<dt><code>-u</code></p>
<dd> Generate a UUID file. The default output filename is <i>infile</i><code>_i.c</code>.</dl>
<p> <code>Proxy/stub generation options:</code></p>
<dl>
<dt><code>-c</code></p>
<dd> Generate a client stub file. The default output filename is <i>infile</i><code>_c.c</code>.</p>
<dt><code>-Os</code></p>
<dd> Generate inline stubs.</p>
<dt><code>-Oi</code></p>
<dd> Generate old-style interpreted stubs.</p>
<dt><code>-Oif, -Oic, -Oicf</code></p>
<dd> Generate new-style fully interpreted stubs.</p>
<dt><code>-p</code></p>
<dd> Generate a proxy. The default output filename is <i>infile</i><code>_p.c</code>.</p>
<dt><code>&#8211;prefix-all=</code><i>prefix</i></p>
<dd> Prefix to put on the name of both client and server stubs.</p>
<dt><code>&#8211;prefix-client=</code><i>prefix</i></p>
<dd> Prefix to put on the name of client stubs.</p>
<dt><code>&#8211;prefix-server=</code><i>prefix</i></p>
<dd> Prefix to put on the name of server stubs.</p>
<dt><code>-s</code></p>
<dd> Generate a server stub file. The default output filename is <i>infile</i><code>_s.c</code>.</p>
<dt><code>&#8211;win32</code>, <code>&#8211;win64</code></p>
<dd> Only generate 32-bit or 64-bit code respectively (the default is to generate both 32-bit and 64-bit versions into the same destination file).</dl>
<dl>
<dt><code>&#8211;winrt</code></p>
<dd> Enable Windows Runtime mode.</p>
<dt><code>&#8211;ns_prefix</code></p>
<dd> Prefix namespaces with ABI namespace.</dl>
<p> <code>Registration script options:</code></p>
<dl>
<dt><code>-r</code></p>
<dd> Generate a registration script. The default output filename is <i>infile</i><code>_r.rgs</code>. If the output file name ends in <code>.res</code>, a binary resource file containing the script is generated instead.</dl>
<p> <code>Dlldata file options:</code></p>
<dl>
<dt><code>&#8211;dlldata-only</code><i> name1 </i>[<i>name2</i>&#8230;]</p>
<dd> Regenerate the dlldata file from scratch using the specified proxy names. The default output filename is <code>dlldata.c</code>.</dl>
<p> <code>Preprocessor options:</code></p>
<dl>
<dt><code>-I </code><i>path</i></p>
<dd> Add a header search directory to path. Multiple search directories are allowed.</p>
<dt><code>-D </code><i>id</i>[<code>=</code><i>val</i>]</p>
<dd> Define preprocessor macro <i>id</i> with value <i>val</i>.</p>
<dt><code>-E</code></p>
<dd> Preprocess only.</p>
<dt><code>-N</code></p>
<dd> Do not preprocess input.</dl>
<p> <code>Debug options:</code></p>
<dl>
<dt><code>-W</code></p>
<dd> Enable pedantic warnings.</p>
<dt><code>-d </code><i>n</i></p>
<dd> Set debug level to the non negative integer <i>n</i>. If prefixed with <code>0x</code>, it will be interpreted as an hexadecimal number. For the meaning of values, see the <code>DEBUG</code> section.</dl>
<p> <code>Miscellaneous options:</code></p>
<dl>
<dt><code>-app_config</code></p>
<dd> Ignored, present for midl compatibility.</p>
<dt><code>&#8211;local-stubs=</code><i>file</i></p>
<dd> Generate empty stubs for call_as/local methods in an object interface and write them to <i>file</i>.</dl>
<h2>DEBUG</h2>
<p> Debug level <i>n</i> is a bitmask with the following meaning:<br />
&nbsp;<wbr>*&nbsp;<wbr>0x01 Tell which resource is parsed&nbsp;<wbr>(verbose mode)<br />
&nbsp;<wbr>*&nbsp;<wbr>0x02 Dump internal structures<br />
&nbsp;<wbr>*&nbsp;<wbr>0x04 Create a parser trace&nbsp;<wbr>(yydebug=1)<br />
&nbsp;<wbr>*&nbsp;<wbr>0x08 Preprocessor messages<br />
&nbsp;<wbr>*&nbsp;<wbr>0x10 Preprocessor lex messages<br />
&nbsp;<wbr>*&nbsp;<wbr>0x20 Preprocessor yacc trace</p>
<h2>BUGS</h2>
<p> Bugs can be reported on the <code>Wine bug tracker</code></p>
<h2>AUTHORS</h2>
<p> <code>widl</code> was originally written by Ove Kåven. It has been improved by Rob Shearman, Dan Hipschman, and others. For a complete list, see the git commit logs. This man page was originally written by Hannu Valtonen and then updated by Dan Hipschman.</p>
<h2>AVAILABILITY</h2>
<p> <code>widl</code> is part of the Wine distribution, which is available through WineHQ, the <code>Wine development headquarters</code></p>
<h2>SEE ALSO</h2>
<p> <code>Wine documentation and support</code> </p>
<h2>Index</h2>
