---

title: "pidl(1)"
name: "pidl"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pidl/"
---

pidl - An IDL compiler written in Perl 

<h2>SYNOPSIS</h2>

 pidl --help 

 pidl [--outputdir[=OUTNAME]] [--includedir DIR...] [--parse-idl-tree] [--dump-idl-tree] [--dump-ndr-tree] [--header[=OUTPUT]] [--python[=OUTPUT]] [--ndr-parser[=OUTPUT]] [--client] [--server] [--warn-compat] [--quiet] [--verbose] [--template] [--ws-parser[=OUTPUT]] [--diff] [--dump-idl] [--tdr-parser[=OUTPUT]] [--samba3-ndr-client[=OUTPUT]] [--samba3-ndr-server[=OUTPUT]] [--typelib=[OUTPUT]] [&lt;idlfile&gt;.idl]...

<h2>DESCRIPTION</h2>

 pidl is an IDL compiler written in Perl that aims to be somewhat compatible with the midl compiler. IDL is short for ``Interface Definition Language''. 

 pidl can generate stubs for DCE/RPC server code, DCE/RPC client code and Wireshark dissectors for DCE/RPC traffic. 

 IDL compilers like pidl take a description of an interface as their input and use it to generate C (though support for other languages may be added later) code that can use these interfaces, pretty print data sent using these interfaces, or even generate Wireshark dissectors that can parse data sent over the wire by these interfaces. 

 pidl takes IDL files in the same format as is used by midl, converts it to a .pidl file (which contains pidl's internal representation of the interface) and can then generate whatever output you need. .pidl files should be used for debugging purposes only. Write your interface definitions in .idl format. 

 The goal of pidl is to implement a IDL compiler that can be used while developing the RPC subsystem in Samba (for both marshalling/unmarshalling and debugging purposes).

<h2>OPTIONS</h2>

<dl>
<dt><i>--help</i>
</dt><dd> Show list of available options.
</dd><dt><i>--version</i>
</dt><dd> Show pidl version
</dd><dt><i>--outputdir </i><i>OUTNAME</i><i></i>
</dt><dd> Write output files to the specified directory. Defaults to the current directory.
</dd><dt><i>--includedir </i><i>DIR</i><i></i>
</dt><dd> Add DIR to the search path used by the preprocessor. This option can be specified multiple times.
</dd><dt><i>--parse-idl-tree</i>
</dt><dd> Read internal tree structure from input files rather than assuming they contain IDL.
</dd><dt><i>--dump-idl</i>
</dt><dd> Generate a new IDL file. File will be named OUTNAME.idl.
</dd><dt><i>--header</i>
</dt><dd> Generate a C header file for the specified interface. Filename defaults to OUTNAME.h.
</dd><dt><i>--ndr-parser</i>
</dt><dd> Generate a C file and C header containing NDR parsers. The filename for the parser defaults to ndr_OUTNAME.c. The header filename will be the parser filename with the extension changed from .c to .h.
</dd><dt><i>--tdr-parser</i>
</dt><dd> Generate a C file and C header containing TDR parsers. The filename for the parser defaults to tdr_OUTNAME.c. The header filename will be the parser filename with the extension changed from .c to .h.
</dd><dt><i>--typelib</i>
</dt><dd> Write type information to the specified file.
</dd><dt><i>--server</i>
</dt><dd> Generate boilerplate for the RPC server that implements the interface. Filename defaults to ndr_OUTNAME_s.c.
</dd><dt><i>--template</i>
</dt><dd> Generate stubs for a RPC server that implements the interface. Output will be written to stdout.
</dd><dt><i>--ws-parser</i>
</dt><dd> Generate an Wireshark dissector (in C) and header file. The dissector filename defaults to packet-dcerpc-OUTNAME.c while the header filename defaults to packet-dcerpc-OUTNAME.h. 
 Pidl will read additional data from an Wireshark conformance file if present. Such a file should have the same location as the IDL file but with the extension <i>cnf</i> rather than <i>idl</i>. See Parse::Pidl::Wireshark::Conformance for details on the format of this file.
</dd><dt><i>--diff</i>
</dt><dd> Parse an IDL file, generate a new IDL file based on the internal data structures and see if there are any differences with the original IDL file. Useful for debugging pidl.
</dd><dt><i>--dump-idl-tree</i>
</dt><dd> Tell pidl to dump the internal tree representation of an IDL file the to disk. Useful for debugging pidl.
</dd><dt><i>--dump-ndr-tree</i>
</dt><dd> Tell pidl to dump the internal NDR information tree it generated from the IDL file to disk. Useful for debugging pidl.
</dd><dt><i>--samba3-ndr-client</i>
</dt><dd> Generate client calls for Samba3, to be placed in rpc_client/. Instead of calling out to the code in Samba3's rpc_parse/, this will call out to Samba4's NDR code instead.
</dd><dt><i>--samba3-ndr-server</i>
</dt><dd> Generate server calls for Samba3, to be placed in rpc_server/. Instead of calling out to the code in Samba3's rpc_parse/, this will call out to Samba4's NDR code instead.</dd></dl>

<h2>IDL SYNTAX</h2>

 IDL files are always preprocessed using the C preprocessor. 

 Pretty much everything in an interface (the interface itself, functions, parameters) can have attributes (or properties whatever name you give them). Attributes always prepend the element they apply to and are surrounded by square brackets ([]). Multiple attributes are separated by comma's; arguments to attributes are specified between parentheses. 

 See the section COMPATIBILITY for the list of attributes that pidl supports. 

 C-style comments can be used.

<h3>CONFORMANT ARRAYS</h3>

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


<h3>VARYING ARRAYS</h3>

 A varying array looks like this: 

 
typedef struct {
    long abc;
    long count;
    long foo;
    [size_is(count)] long *s;
} Struct1;
 

 This will look like this on the wire: 

 
[abc][count][foo][PTR_s][count][s...]


<h3>FIXED ARRAYS</h3>

 A fixed array looks like this: 

 
typedef struct {
    long s[10];
} Struct1;
 

 The NDR representation looks just like 10 separate long declarations. The array size is not encoded on the wire. 

 pidl also supports ``inline'' arrays, which are not part of the IDL/NDR standard. These are declared like this: 

 
typedef struct {
    uint32 foo;
    uint32 count;
    uint32 bar;
    long s[count];
} Struct1;
 

 This appears like this: 

 
[foo][count][bar][s...]
 

 Fixed arrays are an extension added to support some of the strange embedded structures in security descriptors and spoolss. 

 This section is by no means complete. See the OpenGroup and MSDN <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>documentation for additional information.

<h2>COMPATIBILITY WITH MIDL</h2>

<h3>Missing features in pidl</h3>

 The following MIDL features are not (yet) implemented in pidl or are implemented with an incompatible interface:
<dl>
<dt>&bull;
</dt><dd> Asynchronous communication
</dd><dt>&bull;
</dt><dd> Typelibs (.tlb files)
</dd><dt>&bull;
</dt><dd> Datagram support (ncadg_*)</dd></dl>

<h3>Supported attributes and statements</h3>

 in, out, ref, length_is, switch_is, size_is, uuid, case, default, string, unique, ptr, pointer_default, v1_enum, object, helpstring, range, local, call_as, endpoint, switch_type, progid, coclass, iid_is, represent_as, transmit_as, import, include, cpp_quote.

<h3>PIDL Specific properties</h3>

<dl>
<dt>public
</dt><dd> The [public] property on a structure or union is a pidl extension that forces the generated pull/push functions to be non-static. This allows you to declare types that can be used between modules. If you don't specify [public] then pull/push functions for other than top-level functions are declared static.
</dd><dt>noprint
</dt><dd> The [noprint] property is a pidl extension that allows you to specify that pidl should not generate a ndr_print_*() function for that structure or union. This is used when you wish to define your own print function that prints a structure in a nicer manner. A good example is the use of [noprint] on dom_sid, which allows the pretty-printing of SIDs.
</dd><dt>value
</dt><dd> The [value(expression)] property is a pidl extension that allows you to specify the value of a field when it is put on the wire. This allows fields that always have a well-known value to be automatically filled in, thus making the API more programmer friendly. The expression can be any C expression.
</dd><dt>relative
</dt><dd> The [relative] property can be supplied on a pointer. When it is used it declares the pointer as a spoolss style ``relative'' pointer, which means it appears on the wire as an offset within the current encapsulating structure. This is not part of normal IDL/NDR, but it is a very useful extension as it avoids the manual encoding of many complex structures.
</dd><dt>subcontext(length)
</dt><dd> Specifies that a size of <i>length</i> bytes should be read, followed by a blob of that size, which will be parsed as NDR. 
 <i>subcontext()</i> is deprecated now, and should not be used in new code. Instead, use <i>represent_as()</i> or <i>transmit_as()</i>.
</dd><dt>flag
</dt><dd> Specify boolean options, mostly used for low-level NDR options. Several options can be specified using the | character. Note that flags are inherited by substructures!
</dd><dt>nodiscriminant
</dt><dd> The [nodiscriminant] property on a union means that the usual uint16 discriminent field at the start of the union on the wire is omitted. This is not normally allowed in IDL/NDR, but is used for some spoolss structures.
</dd><dt>charset(name)
</dt><dd> Specify that the array or string uses the specified charset. If this attribute is specified, pidl will take care of converting the character data from this format to the host format. Commonly used values are UCS2, DOS and UTF8.</dd></dl>

<h3>Unsupported MIDL properties or statements</h3>

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

 pidl is licensed under the GNU General Public License &lt;<a rel="nofollow" HREF="http://www.gnu.org/licenses/gpl.html">http://www.gnu.org/licenses/gpl.html</a>&gt;.

<h2>AUTHOR</h2>

 pidl was written by Andrew Tridgell, Stefan Metzmacher, Tim Potter and Jelmer Vernooij. The current maintainer is Jelmer Vernooij. 

 This manpage was written by Jelmer Vernooij, partially based on the original pidl README by Andrew Tridgell. 



<dt><a HREF="#lbAJ">COMPATIBILITY WITH MIDL</a>
</dt><dd>


</dd><dt><a HREF="#lbAO">EXAMPLES</a>
</dt><dd>
</dd><dt><a HREF="#lbAP">SEE ALSO</a>
</dt><dd>
</dd><dt><a HREF="#lbAQ">LICENSE</a>
</dt><dd>
</dd><dt><a HREF="#lbAR">AUTHOR</a>
</dt><dd></dd></dl>
