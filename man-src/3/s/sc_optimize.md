---
title: "sc_optimize(3)"
name: "sc_optimize"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_optimize/"
description: "sc::Optimize –"
---

<p>sc::Optimize &#8211; </p>
<p> The <code>Optimize</code> class is an abstract base class for classes that find the extreme points of Function&#8217;s.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;opt.h&gt;</code></pre>
<p> Inherits <code>sc::SavableState</code>. Inherited by <code>sc::EFCOpt</code>, <code>sc::GDIISOpt</code>, <code>sc::LineOpt</code>, <code>sc::NewtonOpt</code>, <code>sc::QNewtonOpt</code>, and <code>sc::SteepestDescentOpt</code>.</p>
<h3>Public Member Functions</h3>
<pre><code>Optimize (StateIn &amp;)


Restore the state of a Function object.


Optimize (const Ref&lt; KeyVal &gt; &amp;)


The KeyVal constructor reads the following information:.


void save_data_state (StateOut &amp;)


Save the base classes (with save_data_state) and the members in the same order that the StateIn CTOR initializes them.


virtual int optimize ()


Do the optimization.


void set_checkpoint ()


Set up for checkpointing.


void set_checkpoint_file (const char *)



void set_function (const Ref&lt; Function &gt; &amp;)


Set the function to be optimized.


void set_max_iterations (int)


Set the iteration limit.


virtual void init ()


Initialize the optimizer.


virtual int update ()=0


Take a step.


virtual void apply_transform (const Ref&lt; NonlinearTransform &gt; &amp;)



Ref&lt; Function &gt; function () const


Returns information about the Function being optimized.


Ref&lt; SCMatrixKit &gt; matrixkit () const



RefSCDimension dimension () const



Protected Attributes
int max_iterations_



int n_iterations_



int ckpt_



int print_timings_



double max_stepsize_



char * ckpt_file



Ref&lt; Function &gt; function_



Ref&lt; Convergence &gt; conv_</code></pre>
<h2>Detailed Description</h2>
<p>The <code>Optimize</code> class is an abstract base class for classes that find the extreme points of Function&#8217;s.</p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>sc::Optimize::Optimize (const <code>Ref</code>&lt; <code>KeyVal</code> &gt; &amp;)</h3>
<p>The <code>KeyVal</code> constructor reads the following information:. .IP &quot;checkpoint&quot; 1c If true, the optimization will be checkpointed. The default is false. </p>
<dl>
<dt>checkpoint_file</p>
<dd>The name of the checkpoint file. The name defaults to opt_ckpt.dat.</dl>
<dl>
<dt>max_iterations</p>
<dd>The maximum number of interations. The default is 10.</dl>
<dl>
<dt>max_stepsize</p>
<dd>The maximum stepsize. The default is 0.6.</dl>
<dl>
<dt>function</p>
<dd>A <code>Function</code> object. There is no default.</dl>
<dl>
<dt>convergence</p>
<dd>This can be either a floating <code>point</code> number or a <code>Convergence</code> object. If it is a floating <code>point</code> number then it is the convergence criterion. See the description <code>Convergence</code> class for the default.</dl>
<h2>Member Function Documentation</h2>
<h3>virtual int sc::Optimize::optimize () [virtual]</h3>
<p>Do the optimization. Returns nonzero if the optimization is complete.</p>
<h3>void sc::Optimize::save_data_state (<code>StateOut</code> &amp;) [virtual]</h3>
<p>Save the base classes (with save_data_state) and the members in the same order that the <code>StateIn</code> CTOR initializes them. This must be implemented by the derived class if the class has data. </p>
<p> Reimplemented from <code>sc::SavableState</code>. </p>
<p> Reimplemented in <code>sc::EFCOpt</code>, <code>sc::GDIISOpt</code>, <code>sc::NewtonOpt</code>, <code>sc::LineOpt</code>, <code>sc::QNewtonOpt</code>, and <code>sc::SteepestDescentOpt</code>.</p>
<h3>virtual int sc::Optimize::update () [pure virtual]</h3>
<p>Take a step. Returns 1 if the optimization has converged, otherwise 0. </p>
<p> Implemented in <code>sc::EFCOpt</code>, <code>sc::GDIISOpt</code>, <code>sc::MCSearch</code>, <code>sc::NewtonOpt</code>, <code>sc::Backtrack</code>, <code>sc::QNewtonOpt</code>, and <code>sc::SteepestDescentOpt</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
