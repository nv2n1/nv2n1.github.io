---
title: "sc_scmatrixjointsubblockiter(3)"
name: "sc_scmatrixjointsubblockiter"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_scmatrixjointsubblockiter/"
description: "sc::SCMatrixJointSubblockIter –"
---

<p>sc::SCMatrixJointSubblockIter &#8211;</p>
<h2>Synopsis</h2>
<p> Inherits <code>sc::SCMatrixSubblockIter</code>.</p>
<h3>Public Member Functions</h3>
<pre><code>SCMatrixJointSubblockIter (const Ref&lt; SCMatrixSubblockIter &gt; &amp;, const Ref&lt; SCMatrixSubblockIter &gt; &amp;, const Ref&lt; SCMatrixSubblockIter &gt; &amp;=0, const Ref&lt; SCMatrixSubblockIter &gt; &amp;=0, const Ref&lt; SCMatrixSubblockIter &gt; &amp;=0)



void begin ()


Start at the beginning.


int ready ()


Returns nonzero if there is another block.


void next ()


Proceed to the next block.


SCMatrixBlock * block ()


Return the current block.


SCMatrixBlock * block (int i)



Protected Attributes
int niters_



Ref&lt; SCMatrixSubblockIter &gt; * iters_
</code></pre>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
