---
title: "sc_lineopt(3)"
name: "sc_lineopt"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_lineopt/"
description: "sc::LineOpt –"
---

<p>sc::LineOpt &#8211; </p>
<p> The <code>LineOpt</code> abstract class is used to perform one dimensional optimizations.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;opt.h&gt;</code></pre>
<p> Inherits <code>sc::Optimize</code>. Inherited by <code>sc::Backtrack</code>, and <code>sc::MCSearch</code>.</p>
<h3>Public Member Functions</h3>
<p><code>LineOpt</code> (<code>StateIn</code> &amp;) </p>
<p> <code>LineOpt</code> (const <code>Ref</code>&lt; <code>KeyVal</code> &gt; &amp;) </p>
<p> void <code>save_data_state</code> (<code>StateOut</code> &amp;)<br />
 <i>Save the base classes (with save_data_state) and the members in the same order that the </i><code>StateIn</code> CTOR initializes them.<br />
 virtual void <code>init</code> (<code>RefSCVector</code> &amp;direction)<br />
 <i>Initializes the line search object. </i><br />
 virtual void <code>init</code> (<code>RefSCVector</code> &amp;direction, <code>Ref</code>&lt; <code>Function</code> &gt; function)<br />
 <i>Initializes the line search object. </i><br />
 void <code>apply_transform</code> (const <code>Ref</code>&lt; <code>NonlinearTransform</code> &gt; &amp;)<br />
 <i>Applies a nonlinear transform. </i><br />
 double <code>decrease_factor</code> ()<br />
 <i>Returns factor for sufficient decrease test. </i><br />
 double <code>set_decrease_factor</code> (double factor)<br />
 <i>Sets factor for sufficient decrease test. </i></p>
<h3>Protected Member Functions</h3>
<pre><code>int sufficient_decrease (RefSCVector &amp;step)



Protected Attributes
double decrease_factor_



RefSCVector initial_x_



double initial_value_



RefSCVector initial_grad_



RefSCVector search_direction_



Ref&lt; Function &gt; function_</code></pre>
<h2>Detailed Description</h2>
<p>The <code>LineOpt</code> abstract class is used to perform one dimensional optimizations.</p>
<h2>Member Function Documentation</h2>
<h3>virtual void sc::LineOpt::init (<code>RefSCVector</code> &amp; direction, <code>Ref</code>&lt; <code>Function</code> &gt; function) [virtual]</h3>
<p>Initializes the line search object. First argument is a search direction, second argument is a function object to optimize. Use this method when a function must be passed to the <code>Optimize</code> base class. </p>
<p> Reimplemented in <code>sc::MCSearch</code>.</p>
<h3>virtual void sc::LineOpt::init (<code>RefSCVector</code> &amp; direction) [virtual]</h3>
<p>Initializes the line search object. Argument is a search direction. Use of this method assumes the <code>Optimize</code> base class already has a function object (got it from a keyval or elsewhere). </p>
<p> Reimplemented in <code>sc::MCSearch</code>.</p>
<h3>void sc::LineOpt::save_data_state (<code>StateOut</code> &amp;) [virtual]</h3>
<p>Save the base classes (with save_data_state) and the members in the same order that the <code>StateIn</code> CTOR initializes them. This must be implemented by the derived class if the class has data. </p>
<p> Reimplemented from <code>sc::Optimize</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
