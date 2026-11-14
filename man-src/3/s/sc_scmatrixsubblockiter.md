---
title: "sc_scmatrixsubblockiter(3)"
name: "sc_scmatrixsubblockiter"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_scmatrixsubblockiter/"
description: "sc::SCMatrixSubblockIter –"
---

<p>sc::SCMatrixSubblockIter &#8211; </p>
<p> Objects of class <code>SCMatrixSubblockIter</code> are used to iterate through the blocks of a matrix.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;block.h&gt;</code></pre>
<p> Inherits <code>sc::RefCount</code>. Inherited by <code>sc::SCMatrixCompositeSubblockIter</code>, <code>sc::SCMatrixJointSubblockIter</code>, <code>sc::SCMatrixListSubblockIter</code>, <code>sc::SCMatrixNullSubblockIter</code>, and <code>sc::SCMatrixSimpleSubblockIter</code>.</p>
<h3>Public Types</h3>
<p>enum <code>Access</code> { <code>Read</code>, <code>Write</code>, <code>Accum</code>, <code>None</code> }</p>
<h3>Public Member Functions</h3>
<pre><code>SCMatrixSubblockIter (Access access)


The access variable should be one of Read, Write, Accum, and None, with the SCMatrixSubblockIter:: scope operator applied.


virtual void begin ()=0


Start at the beginning.


virtual int ready ()=0


Returns nonzero if there is another block.


virtual void next ()=0


Proceed to the next block.


virtual SCMatrixBlock * block ()=0


Return the current block.


Access access () const


Return the type of Access allowed for these blocks.



Protected Attributes</code></pre>
<p> Access <code>access_</code></p>
<h2>Detailed Description</h2>
<p>Objects of class <code>SCMatrixSubblockIter</code> are used to iterate through the blocks of a matrix. </p>
<p> The object must be deleted before using the matrix that owns the blocks that <code>SCMatrixSubblockIter</code> is iterating through.</p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>sc::SCMatrixSubblockIter::SCMatrixSubblockIter (Access access) [inline]</h3>
<p>The access variable should be one of Read, Write, Accum, and None, with the <code>SCMatrixSubblockIter</code>:: scope operator applied.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
