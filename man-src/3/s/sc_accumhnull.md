---
title: "sc_accumhnull(3)"
name: "sc_accumhnull"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_accumhnull/"
description: "sc::AccumHNull –"
---

<p>sc::AccumHNull &#8211;</p>
<h2>Synopsis</h2>
<p> Inherits <code>sc::AccumH</code>.</p>
<h3>Public Member Functions</h3>
<p><code>AccumHNull</code> (<code>StateIn</code> &amp;) </p>
<p> <code>AccumHNull</code> (const <code>Ref</code>&lt; <code>KeyVal</code> &gt; &amp;) </p>
<p> void <code>save_data_state</code> (<code>StateOut</code> &amp;)<br />
 <i>Save the base classes (with save_data_state) and the members in the same order that the </i><code>StateIn</code> CTOR initializes them.<br />
 void <code>accum</code> (const <code>RefSymmSCMatrix</code> &amp;h)</p>
<h2>Member Function Documentation</h2>
<h3>void sc::AccumHNull::save_data_state (<code>StateOut</code> &amp;) [virtual]</h3>
<p>Save the base classes (with save_data_state) and the members in the same order that the <code>StateIn</code> CTOR initializes them. This must be implemented by the derived class if the class has data. </p>
<p> Reimplemented from <code>sc::AccumH</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
