---
title: "opa_osd_query(1)"
name: "opa_osd_query"
section: "1"
letter: "o"
url: "/docs/linux/man/1-opa_osd_query/"
---

<h2>NAME</h2>

 opa_osd_query 

 

 

 Queries the opasadb for path records. This tool allows you to create an arbitrary path query and view the result.

<h2>Syntax</h2>

 opa_osd_query [ <i>options</i>]

<h2>Options</h2>

 

 

 All arguments are optional, but ill-formed queries can be expected to fail. You must provide at least a pair of LIDs or a pair of GIDs. 

 If you have multiple HFIs, the same LID can appear on more than one HFI, therefore you must specify which HFI to use when searching by LIDs. 

 Numbers can be in decimal, hex, or octal.
<dl>
<dt>
&nbsp;<wbr><i>options</i>&nbsp;<wbr>
<dd> Options. Values include: 

<dl>
<dt>
<dd>
<dl>
<dt>
<dd> 

 -v/--verbose <i>arg</i> Sets debugging level. Range = 1 - 7. 

</dl>
</dl>
 

<dl>
<dt>
<dd>
<dl>
<dt>
<dd> 

 -s/--slid <i>arg</i> Specifies source LID.</dl>
</dl>
 

<dl>
<dt>
<dd>
<dl>
<dt>
<dd> 

 -d/--dlid <i>arg</i> Specifies destination LID.</dl>
</dl>
 

<dl>
<dt>
<dd>
<dl>
<dt>
<dd> 

 -S/--sgid <i>arg</i> Specifies source GID in GID format (0x00000000:0x00000000) or in Inet6 format (x:x:x:x:x:x:x:x).</dl>
</dl>
 

<dl>
<dt>
<dd>
<dl>
<dt>
<dd> 

 -D/--dgid <i>arg</i> Specifies destination GID in GID format (0x00000000:0x00000000) or in Inet6 format (x:x:x:x:x:x:x:x).</dl>
</dl>
 

<dl>
<dt>
<dd>
<dl>
<dt>
<dd> 

 -k/--pkey <i>arg</i> Specifies partition key.</dl>
</dl>
 

<dl>
<dt>
<dd>
<dl>
<dt>
<dd> 

 -i/--sid <i>arg</i> Specifies service ID.</dl>
</dl>
 

<dl>
<dt>
<dd>
<dl>
<dt>
<dd> 

 -h/--hfi <i>arg</i> Specifies the HFI to use. Default = first HFI. The HFI can be identified by name, for example, mthfi0 or by number, for example, 1.</dl>
</dl>
 

<dl>
<dt>
<dd>
<dl>
<dt>
<dd> 

 -p/--port <i>arg</i> Specifies the port to use. Default = first port.</dl>
</dl>
 

<dl>
<dt>
<dd>
<dl>
<dt>
<dd> 

 -H/--help Provides this help text.</dl>
</dl>
 

</dl>

<h2>Example</h2>

 opa_osd_query -s2 -d4 

<h2>Index</h2>


