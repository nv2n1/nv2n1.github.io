---
title: "sc_mointstransformfactory(3)"
name: "sc_mointstransformfactory"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_mointstransformfactory/"
description: "sc::MOIntsTransformFactory –"
---

<p>sc::MOIntsTransformFactory &#8211; </p>
<p> <code>MOIntsTransformFactory</code> is a factory that produces MOIntsTransform objects.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;transform_factory.h&gt;</code></pre>
<p> Inherits <code>sc::SavableState</code>.</p>
<h3>Public Types</h3>
<pre><code>enum StoreMethod { mem_posix =  0, posix =  1, mem_mpi =  2, mpi =  3, mem_only =  4 }


Describes the method of storing transformed MO integrals.



Public Member Functions</code></pre>
<p> <code>MOIntsTransformFactory</code> (<code>StateIn</code> &amp;) </p>
<p> <code>MOIntsTransformFactory</code> (const <code>Ref</code>&lt; <code>Integral</code> &gt; &amp;integral, const <code>Ref</code>&lt; <code>MOIndexSpace</code> &gt; &amp;space1, const <code>Ref</code>&lt; <code>MOIndexSpace</code> &gt; &amp;space2=0, const <code>Ref</code>&lt; <code>MOIndexSpace</code> &gt; &amp;space3=0, const <code>Ref</code>&lt; <code>MOIndexSpace</code> &gt; &amp;space4=0) </p>
<p> void <code>save_data_state</code> (<code>StateOut</code> &amp;)<br />
 <i>Save the base classes (with save_data_state) and the members in the same order that the </i><code>StateIn</code> CTOR initializes them.<br />
 void <code>set_spaces</code> (const <code>Ref</code>&lt; <code>MOIndexSpace</code> &gt; &amp;space1, const <code>Ref</code>&lt; <code>MOIndexSpace</code> &gt; &amp;space2=0, const <code>Ref</code>&lt; <code>MOIndexSpace</code> &gt; &amp;space3=0, const <code>Ref</code>&lt; <code>MOIndexSpace</code> &gt; &amp;space4=0)<br />
 <i>Sets the orbital spaces. </i><br />
 void <code>set_top_mole</code> (const <code>Ref</code>&lt; <code>MolecularEnergy</code> &gt; &amp;top_mole)<br />
 <i>Specifies the top-level </i><code>MolecularEnergy</code> object to use for checkpointing.<br />
 void <code>set_ints_method</code> (const <code>StoreMethod</code> method)<br />
 <i>Sets the method of storing transformed MO integrals. Default method is mem_posix. </i><br />
 void <code>set_file_prefix</code> (const std::string &amp;prefix)<br />
 <i>Sets the name of the file to hold the integrals. </i><br />
 void <code>set_debug</code> (int debug) </p>
<p> void <code>set_dynamic</code> (bool dynamic) </p>
<p> void <code>set_print_percent</code> (double print_percent) </p>
<p> void <code>set_memory</code> (size_t nbytes) </p>
<p> <code>Ref</code>&lt; <code>Integral</code> &gt; <code>integral</code> () const<br />
 <i>Returns the </i><code>Integral</code> factory.<br />
 const <code>StoreMethod</code> <code>ints_method</code> () const<br />
 <i>Returns the method of storing transformed MO integrals. </i><br />
 const std::string <code>file_prefix</code> () const<br />
 <i>Sets the name of the file to hold the integrals. </i><br />
 const int <code>debug</code> () const </p>
<p> const bool <code>dynamic</code> () const </p>
<p> const double <code>print_percent</code> () const </p>
<p> const size_t <code>memory</code> () const </p>
<p> <code>Ref</code>&lt; <code>MOIndexSpace</code> &gt; <code>space1</code> () const<br />
 <i>Returns </i><code>MOIndexSpace</code> object 1.<br />
 <code>Ref</code>&lt; <code>MOIndexSpace</code> &gt; <code>space2</code> () const<br />
 <i>Returns </i><code>MOIndexSpace</code> object 2.<br />
 <code>Ref</code>&lt; <code>MOIndexSpace</code> &gt; <code>space3</code> () const<br />
 <i>Returns </i><code>MOIndexSpace</code> object 3.<br />
 <code>Ref</code>&lt; <code>MOIndexSpace</code> &gt; <code>space4</code> () const<br />
 <i>Returns </i><code>MOIndexSpace</code> object 4.<br />
 <code>Ref</code>&lt; <code>TwoBodyMOIntsTransform</code> &gt; <code>twobody_transform_13</code> (const std::string &amp;id)<br />
 <i>Creates an </i><code>TwoBodyMOIntsTransform</code> object that will compute (pq|rs) integrals stored in qs blocks for each pr.<br />
 <code>Ref</code>&lt; <code>TwoBodyMOIntsTransform</code> &gt; <code>twobody_transform_12</code> (const std::string &amp;id)<br />
 <i>Creates an </i><code>TwoBodyMOIntsTransform</code> object that will compute (pq|rs) integrals stored in rs blocks for each pq.</p>
<h2>Detailed Description</h2>
<p><code>MOIntsTransformFactory</code> is a factory that produces MOIntsTransform objects.</p>
<h2>Member Function Documentation</h2>
<h3>void sc::MOIntsTransformFactory::save_data_state (<code>StateOut</code> &amp;) [virtual]</h3>
<p>Save the base classes (with save_data_state) and the members in the same order that the <code>StateIn</code> CTOR initializes them. This must be implemented by the derived class if the class has data. </p>
<p> Reimplemented from <code>sc::SavableState</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
