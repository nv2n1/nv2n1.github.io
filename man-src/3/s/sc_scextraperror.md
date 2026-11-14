---
title: "sc_scextraperror(3)"
name: "sc_scextraperror"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_scextraperror/"
description: "sc::SCExtrapError –"
---

<p>sc::SCExtrapError &#8211; </p>
<p> <code>SCExtrapError</code> holds the error data needed by <code>SelfConsistentExtrapolation</code>.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;scextrap.h&gt;</code></pre>
<p> Inherits <code>sc::SavableState</code>. Inherited by <code>sc::SymmSCMatrixSCExtrapError</code>.</p>
<h3>Public Member Functions</h3>
<pre><code>SCExtrapError ()


Construct a new SCExtrapError.


SCExtrapError (StateIn &amp;)


Constructor to restore SCExtrapError from a StateIn object.


void save_data_state (StateOut &amp;)


Save the base classes (with save_data_state) and the members in the same order that the StateIn CTOR initializes them.


virtual double error ()=0


Returns some measure of the total error.


virtual double scalar_product (const Ref&lt; SCExtrapError &gt; &amp;)=0


Performs a scalar product between this and the given SCExtrapError.</code></pre>
<h2>Detailed Description</h2>
<p><code>SCExtrapError</code> holds the error data needed by <code>SelfConsistentExtrapolation</code>.</p>
<h2>Member Function Documentation</h2>
<h3>void sc::SCExtrapError::save_data_state (<code>StateOut</code> &amp;) [virtual]</h3>
<p>Save the base classes (with save_data_state) and the members in the same order that the <code>StateIn</code> CTOR initializes them. This must be implemented by the derived class if the class has data. </p>
<p> Reimplemented from <code>sc::SavableState</code>. </p>
<p> Reimplemented in <code>sc::SymmSCMatrixSCExtrapError</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
