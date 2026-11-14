---
title: "sc_scmatrixltrisubblockiter(3)"
name: "sc_scmatrixltrisubblockiter"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_scmatrixltrisubblockiter/"
description: "sc::SCMatrixLTriSubBlockIter –"
---

<p>sc::SCMatrixLTriSubBlockIter &#8211;</p>
<h2>Synopsis</h2>
<p> Inherits <code>sc::SCMatrixBlockIter</code>.</p>
<h3>Public Member Functions</h3>
<p><code>SCMatrixLTriSubBlockIter</code> (<code>SCMatrixLTriSubBlock</code> *) </p>
<p> int <code>i</code> ()<br />
 <i>Returns the row index. </i><br />
 int <code>j</code> ()<br />
 <i>Returns the column index. </i><br />
 double <code>get</code> ()<br />
 <i>Return the value of the current element. </i><br />
 void <code>set</code> (double)<br />
 <i>Set the current element to val. </i><br />
 <code>operator int</code> ()<br />
 <i>Return nonzero if there are more elements. </i><br />
 void <code>operator++</code> ()<br />
 <i>Move to the next element. </i><br />
 void <code>reset</code> ()<br />
 <i>Start the iteration over. </i> </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
