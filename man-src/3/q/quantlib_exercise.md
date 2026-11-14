---
title: "quantlib_exercise(3)"
name: "quantlib_exercise"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_exercise/"
description: "QuantLib::Exercise – Base exercise class."
---

<p>QuantLib::Exercise &#8211; Base exercise class. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/exercise.hpp&gt; </p>
<p> Inherited by <code>EarlyExercise</code>, and <code>EuropeanExercise</code>. </p>
<h3>Public Types</h3>
<p>enum <code>Type</code> { <code>American</code>, <code>Bermudan</code>, <code>European</code> } </p>
<h3>Public Member Functions</h3>
<p><code>Exercise</code> (Type type) </p>
<p> Type <code>type</code> () const </p>
<p> <code>Date</code> <code>date</code> (Size index) const </p>
<p> const std::vector&lt; <code>Date</code> &gt; &amp; <code>dates</code> () const<br />
 <i>Returns all exercise dates. </i><br />
 <code>Date</code> <code>lastDate</code> () const </p>
<h3>Protected Attributes</h3>
<p>std::vector&lt; <code>Date</code> &gt; <code>dates_</code> </p>
<p> Type <code>type_</code> </p>
<h2>Detailed Description</h2>
<p>Base exercise class. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
