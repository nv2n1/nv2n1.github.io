---
title: "pidl(1)"
name: "pidl"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pidl/"
---

<h2 class="name">NAME</h2>
 

 pidl - An IDL compiler written in Perl 

<h2>SYNOPSIS</h2>

 pidl --help 

 pidl [--outputdir[=OUTNAME]] [--includedir <font SIZE="-1">DIR...</font>] [--parse-idl-tree] [--dump-idl-tree] [--dump-ndr-tree] [--header[=OUTPUT]] [--python[=OUTPUT]] [--ndr-parser[=OUTPUT]] [--client] [--server] [--warn-compat] [--quiet] [--verbose] [--template] [--ws-parser[=OUTPUT]] [--diff] [--dump-idl] [--tdr-parser[=OUTPUT]] [--samba3-ndr-client[=OUTPUT]] [--samba3-ndr-server[=OUTPUT]] [--typelib=[<font SIZE="-1">OUTPUT</font>]] [&lt;idlfile&gt;.idl]...

<h2>DESCRIPTION</h2>

 pidl is an <font SIZE="-1">IDL</font> compiler written in Perl that aims to be somewhat compatible with the midl compiler. <font SIZE="-1">IDL</font> is short for ``Interface Definition Language''. 

 pidl can generate stubs for <font SIZE="-1">DCE/RPC</font> server code, <font SIZE="-1">DCE/RPC</font> client code and Wireshark dissectors for <font SIZE="-1">DCE/RPC</font> traffic. 

 <font SIZE="-1">IDL</font> compilers like pidl take a description of an interface as their input and use it to generate C (though support for other languages may be added later) code that can use these interfaces, pretty print data sent using these interfaces, or even generate Wireshark dissectors that can parse data sent over the wire by these interfaces. 

 pidl takes <font SIZE="-1">IDL</font> files in the same format as is used by midl, converts it to a .pidl file (which contains pidl's internal representation of the interface) and can then generate whatever output you need. .pidl files should be used for debugging purposes only. Write your interface definitions in .idl format. 

 The goal of pidl is to implement a <font SIZE="-1">IDL</font> compiler that can be used while developing the <font SIZE="-1">RPC</font> subsystem in Samba (for both marshalling/unmarshalling and debugging purposes).

<h2>OPTIONS</h2>

<dl>
<dt><i>--help</i>
<dd> Show list of available options.
<dt><i>--version</i>
<dd> Show pidl version
<dt><i>--outputdir </i><font SIZE="-1"><i>OUTNAME</i></font><i></i>
<dd> Write output files to the specified directory. Defaults to the current directory.
<dt><i>--includedir </i><font SIZE="-1"><i>DIR</i></font><i></i>
<dd> Add <font SIZE="-1">DIR</font> to the search path used by the preprocessor. This option can be specified multiple times.
<dt><i>--parse-idl-tree</i>
<dd> Read internal tree structure from input files rather than assuming they contain <font SIZE="-1">IDL.</font>
<dt><i>--dump-idl</i>
<dd> Generate a new <font SIZE="-1">IDL</font> file. File will be named <font SIZE="-1">OUTNAME</font>.idl.
<dt><i>--header</i>
<dd> Generate a C header file for the specified interface. Filename defaults to <font SIZE="-1">OUTNAME</font>.h.
<dt><i>--ndr-parser</i>
<dd> Generate a C file and C header containing <font SIZE="-1">NDR</font> parsers. The filename for the parser defaults to ndr_OUTNAME.c. The header filename will be the parser filename with the extension changed from .c to .h.
<dt><i>--tdr-parser</i>
<dd> Generate a C file and C header containing <font SIZE="-1">TDR</font> parsers. The filename for the parser defaults to tdr_OUTNAME.c. The header filename will be the parser filename with the extension changed from .c to .h.
<dt><i>--typelib</i>
<dd> Write type information to the specified file.
<dt><i>--server</i>
<dd> Generate boilerplate for the <font SIZE="-1">RPC</font> server that implements the interface. Filename defaults to ndr_OUTNAME_s.c.
<dt><i>--template</i>
<dd> Generate stubs for a <font SIZE="-1">RPC</font> server that implements the interface. Output will be written to stdout.
<dt><i>--ws-parser</i>
<dd> Generate an Wireshark dissector (in C) and header file. The dissector filename defaults to packet-dcerpc-OUTNAME.c while the header filename defaults to packet-dcerpc-OUTNAME.h. 

 Pidl will read additional data from an Wireshark conformance file if present. Such a file should have the same location as the <font SIZE="-1">IDL</font> file but with the extension <i>cnf</i> rather than <i>idl</i>. See Parse::Pidl::Wireshark::Conformance for details on the format of this file.
<dt><i>--diff</i>
<dd> Parse an <font SIZE="-1">IDL</font> file, generate a new <font SIZE="-1">IDL</font> file based on the internal data structures and see if there are any differences with the original <font SIZE="-1">IDL</font> file. Useful for debugging pidl.
<dt><i>--dump-idl-tree</i>
<dd> Tell pidl to dump the internal tree representation of an <font SIZE="-1">IDL</font> file the to disk. Useful for debugging pidl.
<dt><i>--dump-ndr-tree</i>
<dd> Tell pidl to dump the internal <font SIZE="-1">NDR</font> information tree it generated from the <font SIZE="-1">IDL</font> file to disk. Useful for debugging pidl.
<dt><i>--samba3-ndr-client</i>
<dd> Generate client calls for Samba3, to be placed in rpc_client/. Instead of calling out to the code in Samba3's rpc_parse/, this will call out to Samba4's <font SIZE="-1">NDR</font> code instead.
<dt><i>--samba3-ndr-server</i>
<dd> Generate server calls for Samba3, to be placed in rpc_server/. Instead of calling out to the code in Samba3's rpc_parse/, this will call out to Samba4's <font SIZE="-1">NDR</font> code instead.</dl>

<h2>IDL SYNTAX</h2>

 <font SIZE="-1">IDL</font> files are always preprocessed using the C preprocessor. 

 Pretty much everything in an interface (the interface itself, functions, parameters) can have attributes (or properties whatever name you give them). Attributes always prepend the element they apply to and are surrounded by square brackets ([]). Multiple attributes are separated by comma's; arguments to attributes are specified between parentheses. 

 See the section <font SIZE="-1">COMPATIBILITY</font> for the list of attributes that pidl supports. 

 C-style comments can be used.

<h3><font SIZE="-1">CONFORMANT ARRAYS</font></h3>

 A conformant array is one with that ends in [*] or []. The strange things about conformant arrays are that they can only appear as the last element of a structure (unless there is a pointer to the conformant array, of course) and the array size appears before the structure itself on the wire. 

 So, in this example: 

 <pre><code>
typedef struct {
    long abc;
    long count;
    long foo;
    [size_is(count)] long s[*];
} Struct1;
</code></pre> 

 it appears like this: 

 
[size_is][abc][count][foo][s...]
 

 the first [size_is] field is the allocation size of the array, and occurs before the array elements and even before the structure alignment. 

 Note that <i>size_is()</i> can refer to a constant, but that doesn't change the wire representation. It does not make the array a fixed array. 

 midl.exe would write the above array as the following C header: 

 
typedef struct {
    long abc;
    long count;
    long foo;
    long s[1];
} Struct1;
 

 pidl takes a different approach, and writes it like this: 

 
typedef struct {
    long abc;
    long count;
    long foo;
    long *s;
} Struct1;


<h3><font SIZE="-1">VARYING ARRAYS</font></h3>

 A varying array looks like this: 

 
typedef struct {
    long abc;
    long count;
    long foo;
    [size_is(count)] long *s;
} Struct1;
 

 This will look like this on the wire: 

 
[abc][count][foo][PTR_s][count][s...]


<h3><font SIZE="-1">FIXED ARRAYS</font></h3>

 A fixed array looks like this: 

 
typedef struct {
    long s[10];
} Struct1;
 

 The <font SIZE="-1">NDR</font> representation looks just like 10 separate long declarations. The array size is not encoded on the wire. 

 pidl also supports ``inline'' arrays, which are not part of the <font SIZE="-1">IDL/NDR</font> standard. These are declared like this: 

 
typedef struct {
    uint32 foo;
    uint32 count;
    uint32 bar;
    long s[count];
} Struct1;
 

 This appears like this: 

 
[foo][count][bar][s...]
 

 Fixed arrays are an extension added to support some of the strange embedded structures in security descriptors and spoolss. 

 This section is by no means complete. See the OpenGroup and <font SIZE="-1">MSDN </font><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>documentation for additional information.

<h2>COMPATIBILITY WITH MIDL</h2>

<h3>Missing features in pidl</h3>

 The following <font SIZE="-1">MIDL</font> features are not (yet) implemented in pidl or are implemented with an incompatible interface:
<dl>
<dt>&bull;
<dd> Asynchronous communication
<dt>&bull;
<dd> Typelibs (.tlb files)
<dt>&bull;
<dd> Datagram support (ncadg_*)</dl>

<h3>Supported attributes and statements</h3>

 in, out, ref, length_is, switch_is, size_is, uuid, case, default, string, unique, ptr, pointer_default, v1_enum, object, helpstring, range, local, call_as, endpoint, switch_type, progid, coclass, iid_is, represent_as, transmit_as, import, include, cpp_quote.

<h3><font SIZE="-1">PIDL</font> Specific properties</h3>

<dl>
<dt>public
<dd> The [public] property on a structure or union is a pidl extension that forces the generated pull/push functions to be non-static. This allows you to declare types that can be used between modules. If you don't specify [public] then pull/push functions for other than top-level functions are declared static.
<dt>noprint
<dd> The [noprint] property is a pidl extension that allows you to specify that pidl should not generate a ndr_print_*() function for that structure or union. This is used when you wish to define your own print function that prints a structure in a nicer manner. A good example is the use of [noprint] on dom_sid, which allows the pretty-printing of SIDs.
<dt>value
<dd> The [value(expression)] property is a pidl extension that allows you to specify the value of a field when it is put on the wire. This allows fields that always have a well-known value to be automatically filled in, thus making the <font SIZE="-1">API</font> more programmer friendly. The expression can be any C expression.
<dt>relative
<dd> The [relative] property can be supplied on a pointer. When it is used it declares the pointer as a spoolss style ``relative'' pointer, which means it appears on the wire as an offset within the current encapsulating structure. This is not part of normal <font SIZE="-1">IDL/NDR,</font> but it is a very useful extension as it avoids the manual encoding of many complex structures.
<dt>subcontext(length)
<dd> Specifies that a size of <i>length</i> bytes should be read, followed by a blob of that size, which will be parsed as <font SIZE="-1">NDR.</font> 

 <i>subcontext()</i> is deprecated now, and should not be used in new code. Instead, use <i>represent_as()</i> or <i>transmit_as()</i>.
<dt>flag
<dd> Specify boolean options, mostly used for low-level <font SIZE="-1">NDR</font> options. Several options can be specified using the | character. Note that flags are inherited by substructures!
<dt>nodiscriminant
<dd> The [nodiscriminant] property on a union means that the usual uint16 discriminent field at the start of the union on the wire is omitted. This is not normally allowed in <font SIZE="-1">IDL/NDR,</font> but is used for some spoolss structures.
<dt>charset(name)
<dd> Specify that the array or string uses the specified charset. If this attribute is specified, pidl will take care of converting the character data from this format to the host format. Commonly used values are <font SIZE="-1">UCS2, DOS</font> and <font SIZE="-1">UTF8.</font></dl>

<h3>Unsupported <font SIZE="-1">MIDL</font> properties or statements</h3>

 aggregatable, appobject, async_uuid, bindable, control, defaultbind, defaultcollelem, defaultvalue, defaultvtable, dispinterface, displaybind, dual, entry, first_is, helpcontext, helpfile, helpstringcontext, helpstringdll, hidden, idl_module, idl_quote, id, immediatebind, importlib, includelib, last_is, lcid, licensed, max_is, module, ms_union, no_injected_text, nonbrowsable, noncreatable, nonextensible, odl, oleautomation, optional, pragma, propget, propputref, propput, readonly, requestedit, restricted, retval, source, uidefault, usesgetlasterror, vararg, vi_progid, wire_marshal.

<h2>EXAMPLES</h2>

 <pre><code>
#Generating an Wireshark parser
$./ pidl-- ws - parser-- atsvc.idl
#Generating a TDR parser and header
                        $./
                    pidl-- tdr -
    parser-- header-- regf.idl
#Generating a Samba3 client and server
            $./
        pidl-- samba3 -
    ndr - client-- samba3 - ndr - server-- dfs.idl
#Generating a Samba4 NDR parser, client and server
                                          $./
                                      pidl-- ndr -
    parser-- ndr - client-- ndr - server-- samr.idl
</code></pre>

<h2>SEE ALSO</h2>

 &lt;<a rel="nofollow" HREF="http://msdn.microsoft.com/library/en-us/rpc/rpc/field_attributes.asp">http://msdn.microsoft.com/library/en-us/rpc/rpc/field_attributes.asp</a>&gt;, &lt;<a rel="nofollow" HREF="http://wiki.wireshark.org/DCE/RPC">http://wiki.wireshark.org/DCE/RPC</a>&gt;, &lt;<a rel="nofollow" HREF="http://www.samba.org/">http://www.samba.org/</a>&gt;, <i><a HREF="/docs/linux/man/1-yapp/">yapp</a></i>(1)

<h2>LICENSE</h2>

 pidl is licensed under the <font SIZE="-1">GNU</font> General Public License &lt;<a rel="nofollow" HREF="http://www.gnu.org/licenses/gpl.html">http://www.gnu.org/licenses/gpl.html</a>&gt;.

<h2>AUTHOR</h2>

 pidl was written by Andrew Tridgell, Stefan Metzmacher, Tim Potter and Jelmer Vernooij. The current maintainer is Jelmer Vernooij. 

 This manpage was written by Jelmer Vernooij, partially based on the original pidl <font SIZE="-1">README</font> by Andrew Tridgell. 

<h2>Index</h2>



<dt><a HREF="#lbAJ">COMPATIBILITY WITH MIDL</a>
<dd>


<dt><a HREF="#lbAO">EXAMPLES</a>
<dd>
<dt><a HREF="#lbAP">SEE ALSO</a>
<dd>
<dt><a HREF="#lbAQ">LICENSE</a>
<dd>
<dt><a HREF="#lbAR">AUTHOR</a>
<dd></dl>
