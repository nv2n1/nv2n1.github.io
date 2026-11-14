---
title: "embryo_swap_group(3)"
name: "embryo_swap_group"
section: "3"
letter: "e"
url: "/docs/linux/man/3-embryo_swap_group/"
description: "Byte Swapping Functions – Functions that are used to ensure that integers passed to the virtual machine are in small endian format."
---

<p>Byte Swapping Functions &#8211; Functions that are used to ensure that integers passed to the virtual machine are in small endian format. </p>
<h3>Functions</h3>
<p>EAPI void <code>embryo_swap_16</code> (unsigned short *v)<br />
 <i>Ensures that the given unsigned short integer is in the small endian format. </i><br />
 EAPI void <code>embryo_swap_32</code> (unsigned int *v)<br />
 <i>Ensures that the given unsigned integer is in the small endian format. </i></p>
<h2>Detailed Description</h2>
<p>Functions that are used to ensure that integers passed to the virtual machine are in small endian format. </p>
<p> These functions are used to ensure that the virtual machine operates correctly on big endian machines.</p>
<h2>Function Documentation</h2>
<h3>EAPI void embryo_swap_16 (unsigned short * v)</h3>
<p>Ensures that the given unsigned short integer is in the small endian format. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>v</i> Pointer to the given integer.</dl>
<h3>EAPI void embryo_swap_32 (unsigned int * v)</h3>
<p>Ensures that the given unsigned integer is in the small endian format. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>v</i> Pointer to the given integer.</dl>
<p> Referenced by embryo_program_load().</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Embryo from the source code.</p>
