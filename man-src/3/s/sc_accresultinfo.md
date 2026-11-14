---
title: "sc_accresultinfo(3)"
name: "sc_accresultinfo"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_accresultinfo/"
description: "sc::AccResultInfo –"
---

<p>sc::AccResultInfo &#8211; </p>
<p> This is like <code>ResultInfo</code> but the accuracy with which a result was computed as well as the desired accuracy are stored.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;compute.h&gt;</code></pre>
<p> Inherits <code>sc::ResultInfo</code>. Inherited by <code>sc::AccResult&lt; RefDiagSCMatrix &gt;</code>, <code>sc::AccResult&lt; RefSCMatrix &gt;</code>, <code>sc::AccResult&lt; RefSCVector &gt;</code>, <code>sc::AccResult&lt; RefSymmSCMatrix &gt;</code>, <code>sc::NCAccResult&lt; double &gt;</code>, <code>sc::AccResult&lt; T &gt;</code>, <code>sc::NCAccResult&lt; T &gt;</code>, and <code>sc::SSAccResult&lt; T &gt;</code>.</p>
<h3>Public Member Functions</h3>
<p><code>AccResultInfo</code> (<code>Compute</code> *c) </p>
<p> double <code>actual_accuracy</code> () const </p>
<p> double <code>desired_accuracy</code> () const </p>
<p> void <code>set_desired_accuracy</code> (double) </p>
<p> void <code>set_actual_accuracy</code> (double) </p>
<p> int <code>computed_to_desired_accuracy</code> () const </p>
<p> int <code>needed</code> () const</p>
<h3>Protected Member Functions</h3>
<pre><code>AccResultInfo (StateIn &amp;, Compute *)



AccResultInfo (const AccResultInfo &amp;, Compute *)



virtual void save_data_state (StateOut &amp;)



virtual void restore_state (StateIn &amp;)



AccResultInfo &amp; operator= (const AccResultInfo &amp;)



void update ()</code></pre>
<h2>Detailed Description</h2>
<p>This is like <code>ResultInfo</code> but the accuracy with which a result was computed as well as the desired accuracy are stored.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
