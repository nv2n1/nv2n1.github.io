---
title: "sc_twobodygrid(3)"
name: "sc_twobodygrid"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_twobodygrid/"
description: "sc::TwoBodyGrid –"
---

<p>sc::TwoBodyGrid &#8211; </p>
<p> Class <code>TwoBodyGrid</code> describes a set of coordinates of 2 particles.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;twobodygrid.h&gt;</code></pre>
<p> Inherits <code>sc::SavableState</code>.</p>
<h3>Public Member Functions</h3>
<p><code>TwoBodyGrid</code> (<code>StateIn</code> &amp;) </p>
<p> <code>TwoBodyGrid</code> (const <code>Ref</code>&lt; <code>KeyVal</code> &gt; &amp;)<br />
 <i>The </i><code>KeyVal</code> constructor.<br />
 void <code>save_data_state</code> (<code>StateOut</code> &amp;)<br />
 <i>Save the base classes (with save_data_state) and the members in the same order that the </i><code>StateIn</code> CTOR initializes them.<br />
 const std::string &amp; <code>name</code> () const </p>
<p> int <code>nelem</code> () const </p>
<p> const <code>SCVector3</code> &amp; <code>origin</code> () const </p>
<p> <code>SCVector3</code> <code>xyz1</code> (int i, const <code>SCVector3</code> &amp;O=<code>SCVector3</code>(0.0)) const<br />
 <i>Cartesian coordinates of particle 1 at grid </i><code>point</code> i with respect to origin O.<br />
 <code>SCVector3</code> <code>xyz2</code> (int i, const <code>SCVector3</code> &amp;O=<code>SCVector3</code>(0.0)) const<br />
 <i>Cartesian coordinates of particle 2 at grid </i><code>point</code> i with respect to origin O.<br />
 <code>SCVector3</code> <code>rtp1</code> (int i, const <code>SCVector3</code> &amp;O=<code>SCVector3</code>(0.0)) const<br />
 <i>Spherical polar coordinates of particle 1 at grid </i><code>point</code> i with respect to origin O.<br />
 <code>SCVector3</code> <code>rtp2</code> (int i, const <code>SCVector3</code> &amp;O=<code>SCVector3</code>(0.0)) const<br />
 <i>Spherical polar coordinates of particle 2 at grid </i><code>point</code> i with respect to origin O.<br />
 void <code>print</code> (std::ostream &amp;o=ExEnv::out0()) const<br />
 <i>Prints out this. </i></p>
<h2>Detailed Description</h2>
<p>Class <code>TwoBodyGrid</code> describes a set of coordinates of 2 particles.</p>
<h2>Member Function Documentation</h2>
<h3>void sc::TwoBodyGrid::save_data_state (<code>StateOut</code> &amp;) [virtual]</h3>
<p>Save the base classes (with save_data_state) and the members in the same order that the <code>StateIn</code> CTOR initializes them. This must be implemented by the derived class if the class has data. </p>
<p> Reimplemented from <code>sc::SavableState</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
