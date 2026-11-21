---
title: "monodis(1)"
name: "monodis"
section: "1"
letter: "m"
url: "/docs/linux/man/1-monodis/"
description: "monodis – CIL image content dumper and disassembler."
---

<h2>NAME</h2>
<p> monodis &#8211; CIL image content dumper and disassembler.</p>
<h2>SYNOPSIS</h2>
<p> <code>monodis</code> [-h] [&#8211;help] [&#8211;output=FILENAME] [&#8211;mscorlib] [&#8211;assembly] [&#8211;assemblyref] [&#8211;classlayout] [&#8211;constant] [&#8211;customattr] [&#8211;declsec] [&#8211;event] [&#8211;exported] [&#8211;fields] [&#8211;file] [&#8211;forward-decls] [&#8211;genericpar] [&#8211;implmap] [&#8211;interface] [&#8211;manifest] [&#8211;marshal] [&#8211;memberref] [&#8211;method] [&#8211;methodimpl] [&#8211;methodsem] [&#8211;methodspec] [&#8211;module] [&#8211;moduleref] [&#8211;mresources] [&#8211;presources] [&#8211;nested] [&#8211;param] [&#8211;parconst] [&#8211;property] [&#8211;propertymap] [&#8211;standalonesig] [&#8211;typedef] [&#8211;typeref] [&#8211;typespec] [&#8211;blob] [&#8211;strings] [&#8211;userstrings] [FILES&#8230;]</p>
<h2>DESCRIPTION</h2>
<p> The <i>monodis</i> program is used to dump the contents an ECMA/ISO CIL image (contained in .EXE files that contain extended PE/COFF CIL code). </p>
<p> To roundtrip assemblies using ilasm, it is best to use the &#8211;output argument, as that will make monodis save the embedded resources in files that can later be properly embedded back by ilasm. </p>
<p> Additionally, the tool can be used to dump the contents of the various ECMA CIL metadata tables.</p>
<h2>OPTIONS</h2>
<p> The following Generic options are supported:</p>
<dl>
<dt><i>&#8211;help, -h</i></dt>
<dd> Displays usage instructions.</dd>
<dt><i>&#8211;output=FILENAME</i></dt>
<dd> Write output into <i>FILENAME</i> and dump any embedded managed resources.</dd>
<dt><i>&#8211;mscorlib</i></dt>
<dd> For non-corlib assemblies, use &quot;mscorlib&quot; as the assembly name. This is useful for round-tripping the IL with ilasm.</dd>
<dt><i>&#8211;show-method-tokens</i></dt>
<dd> Display tokens for disassembled methods.</dd></dl>
<h2>OPTIONS TO DISPLAY METADATA TABLES</h2>
<p> The following options are used to display metadata tables instead of disassembling the CIL image.</p>
<dl>
<dt><i>&#8211;assembly</i></dt>
<dd> Dumps the contents of the Assembly table.</dd>
<dt><i>&#8211;assemblyref</i></dt>
<dd> Dumps the contents of the AssemblyRef table.</dd>
<dt><i>&#8211;classlayout</i></dt>
<dd> Dumps the contents of the ClassLayout table.</dd>
<dt><i>&#8211;constant</i></dt>
<dd> Dumps the contents of the Constant table.</dd>
<dt><i>&#8211;customattr</i></dt>
<dd> Dumps the contents of the CustomAttribute table.</dd>
<dt><i>&#8211;declsec</i></dt>
<dd> Dumps the contents of the DeclSec table.</dd>
<dt><i>&#8211;event</i></dt>
<dd> Dumps the contents of the Event table.</dd>
<dt><i>&#8211;exported</i></dt>
<dd> Dumps the contents of the ExportedType table.</dd>
<dt><i>&#8211;fields</i></dt>
<dd> Dumps the contents of the Field table.</dd>
<dt><i>&#8211;file</i></dt>
<dd> Dumps the contents of the File table.</dd>
<dt><i>&#8211;forward-decls</i></dt>
<dd> Dumps forward declarations for classes.</dd>
<dt><i>&#8211;genericpar</i></dt>
<dd> Dumps the contents of the GenericParam table.</dd>
<dt><i>&#8211;implmap</i></dt>
<dd> Dumps the contents of the ImplMap table.</dd>
<dt><i>&#8211;interface</i></dt>
<dd> Dumps the contents of the InterfaceImpl table.</dd>
<dt><i>&#8211;manifest</i></dt>
<dd> Dumps the contents of the ManifestResource table.</dd>
<dt><i>&#8211;marshal</i></dt>
<dd> Dumps the contents of the FieldMarshal table.</dd>
<dt><i>&#8211;memberref</i></dt>
<dd> Dumps the contents of the MemberRef table.</dd>
<dt><i>&#8211;method</i></dt>
<dd> Dumps the contents of the MethodDef table.</dd>
<dt><i>&#8211;methodimpl</i></dt>
<dd> Dumps the contents of the MethodImpl table.</dd>
<dt><i>&#8211;methodspec</i></dt>
<dd> Dumps the contents of the MethodSpec table.</dd>
<dt><i>&#8211;methodsem</i></dt>
<dd> Dumps the contents of the MethodSemantics table.</dd>
<dt><i>&#8211;module</i></dt>
<dd> Dumps the contents of the Module table.</dd>
<dt><i>&#8211;moduleref</i></dt>
<dd> Dumps the contents of the ModuleRef table.</dd>
<dt><i>&#8211;mresources</i></dt>
<dd> Saves all the managed resources embedded in the assembly into the current directory. To get a list of the embedded resources use the &#8211;manifest option.</dd>
<dt><i>&#8211;presources</i></dt>
<dd> Prints offsets and names of manifest resources embedded in the assembly.</dd>
<dt><i>&#8211;nested</i></dt>
<dd> Dumps the contents of the NestedClass table.</dd>
<dt><i>&#8211;param</i></dt>
<dd> Dumps the contents of the Param table.</dd>
<dt><i>&#8211;parconst</i></dt>
<dd> Dumps the contents of the GenericParameterConstraint table.</dd>
<dt><i>&#8211;property</i></dt>
<dd> Dumps the contents of the Property table.</dd>
<dt><i>&#8211;propertymap</i></dt>
<dd> Dumps the contents of the PropertyMap table.</dd>
<dt><i>&#8211;standalonesig</i></dt>
<dd> Dumps the contents of the StandAloneSig table.</dd>
<dt><i>&#8211;typedef</i></dt>
<dd> Dumps the contents of the TypeDef table.</dd>
<dt><i>&#8211;typespec</i></dt>
<dd> Dumps the contents of the TypeSpec table.</dd>
<dt><i>&#8211;typeref</i></dt>
<dd> Dumps the contents of the TypeRef table.</dd>
<dt><i>&#8211;blob</i></dt>
<dd> Dumps the entire contents of the blob stream as hex.</dd>
<dt><i>&#8211;strings</i></dt>
<dd> Dumps the contents of the Strings heap.</dd>
<dt><i>&#8211;userstrings</i></dt>
<dd> Dumps the contents of the User-Strings heap</dd></dl>
<p> If no flags are specified the program dumps the content of the image in a format that can be used to rountrip the code. </p>
<h2>ENVIRONMENT VARIABLES</h2>
<dl>
<dt><i>MONO_PATH</i></dt>
<dd> Provides a search path to mono and mint where to look for library files. Directories are separated by the platform path separator (colons on unix). Example: <code>/home/username/lib:/usr/local/mono/lib</code></dd></dl>
<h2>AUTHOR</h2>
<p> monodis was written by Miguel de Icaza, Paolo Molaro and Dietmar Maurer.</p>
<h2>SEE ALSO</h2>
<p> <code>pedump(1)</code> </p>
