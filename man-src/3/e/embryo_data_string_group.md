---
title: "embryo_data_string_group(3)"
name: "embryo_data_string_group"
section: "3"
letter: "e"
url: "/docs/linux/man/3-embryo_data_string_group/"
description: "Embryo Data String Functions – Functions that operate on strings in the memory of a virtual machine."
---

<p>Embryo Data String Functions &#8211; Functions that operate on strings in the memory of a virtual machine. </p>
<h3>Functions</h3>
<p>EAPI int <code>embryo_data_string_length_get</code> (Embryo_Program *ep, Embryo_Cell *str_cell)<br />
 <i>Retrieves the length of the string starting at the given cell. </i><br />
 EAPI void <code>embryo_data_string_get</code> (Embryo_Program *ep, Embryo_Cell *str_cell, char *dst)<br />
 <i>Copies the string starting at the given cell to the given buffer. </i><br />
 EAPI void <code>embryo_data_string_set</code> (Embryo_Program *ep, const char *src, Embryo_Cell *str_cell)<br />
 <i>Copies string in the given buffer into the virtual machine memory starting at the given cell. </i><br />
 EAPI Embryo_Cell * <code>embryo_data_address_get</code> (Embryo_Program *ep, Embryo_Cell addr)<br />
 <i>Retreives a pointer to the address in the virtual machine given by the given cell. </i></p>
<h2>Detailed Description</h2>
<p>Functions that operate on strings in the memory of a virtual machine.</p>
<h2>Function Documentation</h2>
<h3>EAPI Embryo_Cell* embryo_data_address_get (Embryo_Program * ep, Embryo_Cell addr)</h3>
<p>Retreives a pointer to the address in the virtual machine given by the given cell. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ep</i> The program whose virtual machine address is being queried.<br />
 <i>addr</i> The given cell.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>A pointer to the cell at the given address.</dl>
<p> Referenced by embryo_program_run().</p>
<h3>EAPI void embryo_data_string_get (Embryo_Program * ep, Embryo_Cell * str_cell, char * dst)</h3>
<p>Copies the string starting at the given cell to the given buffer. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ep</i> The program the cell is part of.<br />
 <i>str_cell</i> Pointer to the first cell of the string.<br />
 <i>dst</i> The given buffer.</dl>
<h3>EAPI int embryo_data_string_length_get (Embryo_Program * ep, Embryo_Cell * str_cell)</h3>
<p>Retrieves the length of the string starting at the given cell. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ep</i> The program the cell is part of.<br />
 <i>str_cell</i> Pointer to the first cell of the string.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The length of the string. 0 is returned if there is an error.</dl>
<h3>EAPI void embryo_data_string_set (Embryo_Program * ep, const char * src, Embryo_Cell * str_cell)</h3>
<p>Copies string in the given buffer into the virtual machine memory starting at the given cell. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ep</i> The program the cell is part of.<br />
 <i>src</i> The given buffer.<br />
 <i>str_cell</i> Pointer to the first cell to copy the string to.</dl>
<p> Referenced by embryo_program_run().</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Embryo from the source code.</p>
