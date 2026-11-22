---

title: "widl(1)"
name: "widl"
section: "1"
letter: "w"
url: "/docs/linux/man/1-widl/"
description: "widl – Wine Interface Definition Language (IDL) compiler"
---

<p> widl &#8211; Wine Interface Definition Language (IDL) compiler</p>
<h2>SYNOPSIS</h2>
<p> <code>widl</code> [<i>options</i>] <i>IDL_file</i><br/>
 <code>widl</code> [<i>options</i>] <code>&#8211;dlldata-only</code> <i>name1</i> [<i>name2</i>&#8230;]</p>
<h2>DESCRIPTION</h2>
<p> When no options are used the program will generate a header file, and possibly client and server stubs, proxy and dlldata files, a typelib, and a UUID file, depending on the contents of the IDL file. If any of the options <code>-c</code>, <code>-h</code>, <code>-p</code>, <code>-s</code>, <code>-t</code>, <code>-u</code> or <code>&#8211;local-stubs</code> is given, <code>widl</code> will only generate the requested files, and no others. When run with <code>&#8211;dlldata-only</code>, widl will only generate a dlldata file, and it will contain a list of the names passed as arguments. Usually the way this file is updated is that each time <code>widl</code> is run, it reads any existing dlldata file, and if necessary regenerates it with the same list of names, but with the present proxy file included. </p>
<p> When run without any arguments, <code>widl</code> will print a help message. </p>
<h2>OPTIONS</h2>
<p> <code>General options:</code></p>
<dl>
<dt><code>-V</code></dt>
<dd> Print version number and exit.</dd>
<dt><code>-o, &#8211;output=</code><i>name</dt>
<dd> Set the name of the output file. When generating multiple output files, this sets only the base name of the file; the respective output files are then named name</i>.h, <i>name</i>_p.c, etc. If a full file name with extension is specified, only that file is generated.</dd>
<dt><code>-b </code><i>cpu-manufacturer</i>[<code>&#8211;</code><i>kernel</i>]<code>&#8211;</code><i>os</i></dt>
<dd> Set the target architecture when cross-compiling. The target specification is in the standard autoconf format as returned by <code>config.sub</code>.</dd></dl>
<p> <code>Header options:</code></p>
<dl>
<dt><code>-h</code></dt>
<dd> Generate header files. The default output filename is <i>infile</i><code>.h</code>.</dd>
<dt><code>&#8211;oldnames</code></dt>
<dd> Use old naming conventions.</dd></dl>
<p> <code>Type library options:</code></p>
<dl>
<dt><code>-t</code></dt>
<dd> Generate a type library. The default output filename is <i>infile</i><code>.tlb</code>. If the output file name ends in <code>.res</code>, a binary resource file containing the type library is generated instead.</dd>
<dt><code>-m32, -m64</code></dt>
<dd> Generate a Win32 or Win64 type library respectively.</dd></dl>
<p> <code>UUID file options:</code></p>
<dl>
<dt><code>-u</code></dt>
<dd> Generate a UUID file. The default output filename is <i>infile</i><code>_i.c</code>.</dd></dl>
<p> <code>Proxy/stub generation options:</code></p>
<dl>
<dt><code>-c</code></dt>
<dd> Generate a client stub file. The default output filename is <i>infile</i><code>_c.c</code>.</dd>
<dt><code>-Os</code></dt>
<dd> Generate inline stubs.</dd>
<dt><code>-Oi</code></dt>
<dd> Generate old-style interpreted stubs.</dd>
<dt><code>-Oif, -Oic, -Oicf</code></dt>
<dd> Generate new-style fully interpreted stubs.</dd>
<dt><code>-p</code></dt>
<dd> Generate a proxy. The default output filename is <i>infile</i><code>_p.c</code>.</dd>
<dt><code>&#8211;prefix-all=</code><i>prefix</i></dt>
<dd> Prefix to put on the name of both client and server stubs.</dd>
<dt><code>&#8211;prefix-client=</code><i>prefix</i></dt>
<dd> Prefix to put on the name of client stubs.</dd>
<dt><code>&#8211;prefix-server=</code><i>prefix</i></dt>
<dd> Prefix to put on the name of server stubs.</dd>
<dt><code>-s</code></dt>
<dd> Generate a server stub file. The default output filename is <i>infile</i><code>_s.c</code>.</dd>
<dt><code>&#8211;win32</code>, <code>&#8211;win64</code></dt>
<dd> Only generate 32-bit or 64-bit code respectively (the default is to generate both 32-bit and 64-bit versions into the same destination file).</dd></dl>
<dl>
<dt><code>&#8211;winrt</code></dt>
<dd> Enable Windows Runtime mode.</dd>
<dt><code>&#8211;ns_prefix</code></dt>
<dd> Prefix namespaces with ABI namespace.</dd></dl>
<p> <code>Registration script options:</code></p>
<dl>
<dt><code>-r</code></dt>
<dd> Generate a registration script. The default output filename is <i>infile</i><code>_r.rgs</code>. If the output file name ends in <code>.res</code>, a binary resource file containing the script is generated instead.</dd></dl>
<p> <code>Dlldata file options:</code></p>
<dl>
<dt><code>&#8211;dlldata-only</code><i> name1 </i>[<i>name2</i>&#8230;]</dt>
<dd> Regenerate the dlldata file from scratch using the specified proxy names. The default output filename is <code>dlldata.c</code>.</dd></dl>
<p> <code>Preprocessor options:</code></p>
<dl>
<dt><code>-I </code><i>path</i></dt>
<dd> Add a header search directory to path. Multiple search directories are allowed.</dd>
<dt><code>-D </code><i>id</i>[<code>=</code><i>val</i>]</dt>
<dd> Define preprocessor macro <i>id</i> with value <i>val</i>.</dd>
<dt><code>-E</code></dt>
<dd> Preprocess only.</dd>
<dt><code>-N</code></dt>
<dd> Do not preprocess input.</dd></dl>
<p> <code>Debug options:</code></p>
<dl>
<dt><code>-W</code></dt>
<dd> Enable pedantic warnings.</dd>
<dt><code>-d </code><i>n</i></dt>
<dd> Set debug level to the non negative integer <i>n</i>. If prefixed with <code>0x</code>, it will be interpreted as an hexadecimal number. For the meaning of values, see the <code>DEBUG</code> section.</dd></dl>
<p> <code>Miscellaneous options:</code></p>
<dl>
<dt><code>-app_config</code></dt>
<dd> Ignored, present for midl compatibility.</dd>
<dt><code>&#8211;local-stubs=</code><i>file</i></dt>
<dd> Generate empty stubs for call_as/local methods in an object interface and write them to <i>file</i>.</dd></dl>
<h2>DEBUG</h2>
<p> Debug level <i>n</i> is a bitmask with the following meaning:<br/>
&nbsp;<wbr>*&nbsp;<wbr>0x01 Tell which resource is parsed&nbsp;<wbr>(verbose mode)<br/>
&nbsp;<wbr>*&nbsp;<wbr>0x02 Dump internal structures<br/>
&nbsp;<wbr>*&nbsp;<wbr>0x04 Create a parser trace&nbsp;<wbr>(yydebug=1)<br/>
&nbsp;<wbr>*&nbsp;<wbr>0x08 Preprocessor messages<br/>
&nbsp;<wbr>*&nbsp;<wbr>0x10 Preprocessor lex messages<br/>
&nbsp;<wbr>*&nbsp;<wbr>0x20 Preprocessor yacc trace</p>
<h2>BUGS</h2>
<p> Bugs can be reported on the <code>Wine bug tracker</code></p>
<h2>AUTHORS</h2>
<p> <code>widl</code> was originally written by Ove Kåven. It has been improved by Rob Shearman, Dan Hipschman, and others. For a complete list, see the git commit logs. This man page was originally written by Hannu Valtonen and then updated by Dan Hipschman.</p>
<h2>AVAILABILITY</h2>
<p> <code>widl</code> is part of the Wine distribution, which is available through WineHQ, the <code>Wine development headquarters</code></p>
<h2>SEE ALSO</h2>
<p> <code>Wine documentation and support</code> </p>
