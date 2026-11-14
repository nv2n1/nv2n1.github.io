---
title: "uildumpsymboltable(3)"
name: "uildumpsymboltable"
section: "3"
letter: "u"
url: "/docs/linux/man/3-uildumpsymboltable/"
description: "UilDumpSymbolTable — Dumps the contents of a named UIL symbol table to standard output"
---

<p><code>UilDumpSymbolTable</code> &#8212; Dumps the contents of a named UIL symbol table to standard output</p>
<h2>Synopsis</h2>
<pre>#include &lt;uil/UilDef.h&gt;
<code>void UilDumpSymbolTable</code>(
<code>sym_entry_type *root_ptr</code>);</pre>
<h2>Description</h2>
<p>The <code>UilDumpSymbolTable</code> function dumps the contents of a UIL symbol table pointer to standard output.</p>
<dl COMPACT>
<dt><i>root_ptr</i></p>
<dd>Specifies a pointer to the the symbol table root entry. This value can be taken from the <code>parse_tree_root</code> part of the <code>Uil_compile_desc_type</code> data structure returned by <code>Uil</code>.</dl>
<p> By following the link from the root entry, you can traverse the entire parse tree. Symbol table entries are in the following format: </p>
<p> <code>hex.address</code> <code>symbol.type</code> <code>symbol.data</code> <code>prev.source.position</code> <code>source.position</code> <code>modification.record</code> </p>
<p> where:</p>
<dl COMPACT>
<dt><code>hex.address</code></p>
<dd>Specifies the hexadecimal address of this entry in the symbol table.</p>
<dt><code>symbol.type</code></p>
<dd>Specifies the type of this symbol table entry. Some possible types are <i>root</i>, <i>module</i>, <i>value</i>, <i>procedure</i>, and <i>widget</i>.</p>
<dt><code>symbol.data</code></p>
<dd>Specifies data for the symbol table entry. The data varies with the type of the entry. Often it contains pointers to other symbol table entries, or the actual data for the data type.</p>
<dt><code>prev.source.position</code></p>
<dd>Specifies the end point in the source code for the previous source item.</p>
<dt><code>source.position</code></p>
<dd>Specifies the range of positions in the source code for this symbol.</dl>
<p> The exact data structures for each symbol type are defined in the include file <code>UilSymDef.h</code>. Note that this file is automatically included when an application includes the file <code>UilDef.h</code>.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-uil/">Uil</a></code>(3)</p>
