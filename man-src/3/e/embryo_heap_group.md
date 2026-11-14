---
title: "embryo_heap_group(3)"
name: "embryo_heap_group"
section: "3"
letter: "e"
url: "/docs/linux/man/3-embryo_heap_group/"
description: "Heap Functions – The heap is an area of memory that can be allocated for program use at runtime."
---

<p>Heap Functions &#8211; The heap is an area of memory that can be allocated for program use at runtime. </p>
<h3>Functions</h3>
<p>EAPI Embryo_Cell <code>embryo_data_heap_push</code> (Embryo_Program *ep, int cells)<br />
 <i>Increases the size of the heap of the given virtual machine by the given number of Embryo_Cells. </i><br />
 EAPI void <code>embryo_data_heap_pop</code> (Embryo_Program *ep, Embryo_Cell down_to)<br />
 <i>Decreases the size of the heap of the given virtual machine down to the given size. </i></p>
<h2>Detailed Description</h2>
<p>The heap is an area of memory that can be allocated for program use at runtime. </p>
<p> The heap functions here change the amount of heap memory available.</p>
<h2>Function Documentation</h2>
<h3>EAPI void embryo_data_heap_pop (Embryo_Program * ep, Embryo_Cell down_to)</h3>
<p>Decreases the size of the heap of the given virtual machine down to the given size. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ep</i> The program with the given virtual machine.<br />
 <i>down_to</i> The given size.</dl>
<h3>EAPI Embryo_Cell embryo_data_heap_push (Embryo_Program * ep, int cells)</h3>
<p>Increases the size of the heap of the given virtual machine by the given number of Embryo_Cells. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ep</i> The program with the given virtual machine.<br />
 <i>cells</i> The given number of Embryo_Cells.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The address of the new memory region on success. EMBRYO_CELL_NONE otherwise.</dl>
<p> References EMBRYO_CELL_NONE. </p>
<p> Referenced by embryo_program_run().</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Embryo from the source code.</p>
