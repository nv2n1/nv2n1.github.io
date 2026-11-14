---
title: "sc_selfconsistentextrapolation(3)"
name: "sc_selfconsistentextrapolation"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_selfconsistentextrapolation/"
description: "sc::SelfConsistentExtrapolation –"
---

<p>sc::SelfConsistentExtrapolation &#8211; </p>
<p> The <code>SelfConsistentExtrapolation</code> abstract class is used to iteratively solve equations requiring a self consistent solution, such as,.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;scextrap.h&gt;</code></pre>
<p> Inherits <code>sc::SavableState</code>. Inherited by <code>sc::DIIS</code>.</p>
<h3>Public Member Functions</h3>
<pre><code>SelfConsistentExtrapolation (StateIn &amp;)



SelfConsistentExtrapolation (const Ref&lt; KeyVal &gt; &amp;)


The only keyword read is tolerance#, which is usually not needed since the objects using SelfConsistentExtrapolation should set the tolerances as needed.


void save_data_state (StateOut &amp;)


Save the base classes (with save_data_state) and the members in the same order that the StateIn CTOR initializes them.


void set_tolerance (double t)



double tolerance ()



double error ()



int converged ()



virtual int extrapolate (const Ref&lt; SCExtrapData &gt; &amp;data, const Ref&lt; SCExtrapError &gt; &amp;error)=0



virtual void start_extrapolation ()



virtual void reinitialize ()=0



Protected Member Functions
void set_error (double e)</code></pre>
<h2>Detailed Description</h2>
<p>The <code>SelfConsistentExtrapolation</code> abstract class is used to iteratively solve equations requiring a self consistent solution, such as,. </p>
<p> [ polation::SelfConsistentExtrapolation (const <code>Ref</code>&lt; <code>KeyVal</code> &gt; &amp;)&quot; </p>
<p> The only keyword read is tolerance#, which is usually not needed since the objects using <code>SelfConsistentExtrapolation</code> should set the tolerances as needed.</p>
<h2>Member Function Documentation</h2>
<h3>void sc::SelfConsistentExtrapolation::save_data_state (<code>StateOut</code> &amp;) [virtual]</h3>
<p>Save the base classes (with save_data_state) and the members in the same order that the <code>StateIn</code> CTOR initializes them. This must be implemented by the derived class if the class has data. </p>
<p> Reimplemented from <code>sc::SavableState</code>. </p>
<p> Reimplemented in <code>sc::DIIS</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
