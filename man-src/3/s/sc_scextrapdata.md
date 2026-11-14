---
title: "sc_scextrapdata(3)"
name: "sc_scextrapdata"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_scextrapdata/"
description: "sc::SCExtrapData –"
---

<p>sc::SCExtrapData &#8211; </p>
<p> <code>SCExtrapData</code> hold the data to be extrapolated needed by <code>SelfConsistentExtrapolation</code>.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;scextrap.h&gt;</code></pre>
<p> Inherits <code>sc::SavableState</code>. Inherited by <code>sc::SymmSCMatrix2SCExtrapData</code>, <code>sc::SymmSCMatrix4SCExtrapData</code>, <code>sc::SymmSCMatrixNSCExtrapData</code>, and <code>sc::SymmSCMatrixSCExtrapData</code>.</p>
<h3>Public Member Functions</h3>
<p><code>SCExtrapData</code> ()<br />
 <i>Construct a new </i><code>SCExtrapData</code>.<br />
 <code>SCExtrapData</code> (<code>StateIn</code> &amp;)<br />
 <i>Constructor to restore </i><code>SCExtrapData</code> from a <code>StateIn</code> object.<br />
 void <code>save_data_state</code> (<code>StateOut</code> &amp;)<br />
 <i>Save the base classes (with save_data_state) and the members in the same order that the </i><code>StateIn</code> CTOR initializes them.<br />
 virtual <code>SCExtrapData</code> * <code>copy</code> ()=0<br />
 <i>Return a copy of this. </i><br />
 virtual void <code>zero</code> ()=0<br />
 <i>Set this to zero. </i><br />
 virtual void <code>accumulate_scaled</code> (double scale, const <code>Ref</code>&lt; <code>SCExtrapData</code> &gt; &amp;)=0<br />
 <i>The passed </i><code>SCExtrapData</code> is accumulated into this after applying the scaling factor.</p>
<h2>Detailed Description</h2>
<p><code>SCExtrapData</code> hold the data to be extrapolated needed by <code>SelfConsistentExtrapolation</code>.</p>
<h2>Member Function Documentation</h2>
<h3>virtual void sc::SCExtrapData::accumulate_scaled (double scale, const <code>Ref</code>&lt; <code>SCExtrapData</code> &gt; &amp;) [pure virtual]</h3>
<p>The passed <code>SCExtrapData</code> is accumulated into this after applying the scaling factor.</p>
<h3>virtual <code>SCExtrapData</code>* sc::SCExtrapData::copy () [pure virtual]</h3>
<p>Return a copy of this. </p>
<p> Implemented in <code>sc::SymmSCMatrixSCExtrapData</code>, <code>sc::SymmSCMatrix2SCExtrapData</code>, <code>sc::SymmSCMatrix4SCExtrapData</code>, and <code>sc::SymmSCMatrixNSCExtrapData</code>.</p>
<h3>void sc::SCExtrapData::save_data_state (<code>StateOut</code> &amp;) [virtual]</h3>
<p>Save the base classes (with save_data_state) and the members in the same order that the <code>StateIn</code> CTOR initializes them. This must be implemented by the derived class if the class has data. </p>
<p> Reimplemented from <code>sc::SavableState</code>. </p>
<p> Reimplemented in <code>sc::SymmSCMatrixSCExtrapData</code>, <code>sc::SymmSCMatrix2SCExtrapData</code>, <code>sc::SymmSCMatrix4SCExtrapData</code>, and <code>sc::SymmSCMatrixNSCExtrapData</code>.</p>
<h3>virtual void sc::SCExtrapData::zero () [pure virtual]</h3>
<p>Set this to zero. </p>
<p> Implemented in <code>sc::SymmSCMatrixSCExtrapData</code>, <code>sc::SymmSCMatrix2SCExtrapData</code>, <code>sc::SymmSCMatrix4SCExtrapData</code>, and <code>sc::SymmSCMatrixNSCExtrapData</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
