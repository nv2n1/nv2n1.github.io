---
title: "sc_scelementmaxabs(3)"
name: "sc_scelementmaxabs"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_scelementmaxabs/"
description: "sc::SCElementMaxAbs –"
---

<p>sc::SCElementMaxAbs &#8211;</p>
<h2>Synopsis</h2>
<p> Inherits <code>sc::SCElementOp</code>.</p>
<h3>Public Member Functions</h3>
<p><code>SCElementMaxAbs</code> (<code>StateIn</code> &amp;) </p>
<p> void <code>save_data_state</code> (<code>StateOut</code> &amp;)<br />
 <i>Save the base classes (with save_data_state) and the members in the same order that the </i><code>StateIn</code> CTOR initializes them.<br />
 void <code>process</code> (<code>SCMatrixBlockIter</code> &amp;)<br />
 <i>This is the fallback routine to process blocks and is called by process_spec members that are not overridden. </i><br />
 int <code>has_collect</code> ()<br />
 <i>If duplicates of the </i><code>SCElementOp</code> exist (that is, there is more than one node), then if has_collect returns nonzero then collect is called with a <code>MessageGrp</code> reference after all of the blocks have been processed.<br />
 void <code>defer_collect</code> (int) </p>
<p> void <code>collect</code> (const <code>Ref</code>&lt; <code>MessageGrp</code> &gt; &amp;) </p>
<p> void <code>collect</code> (const <code>Ref</code>&lt; <code>SCElementOp</code> &gt; &amp;) </p>
<p> double <code>result</code> ()</p>
<h2>Member Function Documentation</h2>
<h3>int sc::SCElementMaxAbs::has_collect () [virtual]</h3>
<p>If duplicates of the <code>SCElementOp</code> exist (that is, there is more than one node), then if has_collect returns nonzero then collect is called with a <code>MessageGrp</code> reference after all of the blocks have been processed. The default return value of has_collect is 0 and collect&#8217;s default action is do nothing. If defer_collect member is called with nonzero, collect will do nothing (this is only used by the blocked matrices). </p>
<p> Reimplemented from <code>sc::SCElementOp</code>.</p>
<h3>void sc::SCElementMaxAbs::process (<code>SCMatrixBlockIter</code> &amp;) [virtual]</h3>
<p>This is the fallback routine to process blocks and is called by process_spec members that are not overridden. </p>
<p> Implements <code>sc::SCElementOp</code>.</p>
<h3>void sc::SCElementMaxAbs::save_data_state (<code>StateOut</code> &amp;) [virtual]</h3>
<p>Save the base classes (with save_data_state) and the members in the same order that the <code>StateIn</code> CTOR initializes them. This must be implemented by the derived class if the class has data. </p>
<p> Reimplemented from <code>sc::SavableState</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
