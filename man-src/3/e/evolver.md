---
title: "evolver(3)"
name: "evolver"
section: "3"
letter: "e"
url: "/docs/linux/man/3-evolver/"
description: "QuantLib::FiniteDifferenceModel – Generic finite difference model."
---

<h2 class="name">NAME</h2>
<p> QuantLib::FiniteDifferenceModel &#8211; Generic finite difference model. </p>
<h2>SYNOPSIS</h2>
<p> #include &lt;ql/methods/finitedifferences/finitedifferencemodel.hpp&gt; </p>
<h3>Public Types</h3>
<p> typedef Evolver::traits <code>traits</code> </p>
<p> typedef traits::operator_type <code>operator_type</code> </p>
<p> typedef traits::array_type <code>array_type</code> </p>
<p> typedef traits::bc_set <code>bc_set</code> </p>
<p> typedef traits::condition_type <code>condition_type</code> </p>
<h3>Public Member Functions</h3>
<p> <code>FiniteDifferenceModel</code> (const operator_type &amp;L, const bc_set &amp;bcs, const std::vector&lt; <code>Time</code> &gt; &amp;stoppingTimes=std::vector&lt; <code>Time</code> &gt;()) </p>
<p> <code>FiniteDifferenceModel</code> (const Evolver &amp;evolver, const std::vector&lt; <code>Time</code> &gt; &amp;stoppingTimes=std::vector&lt; <code>Time</code> &gt;()) </p>
<p> const Evolver &amp; <code>evolver</code> () const </p>
<p> void <code>rollback</code> (array_type &amp;a, <code>Time</code> from, <code>Time</code> to, Size steps) </p>
<p> void <code>rollback</code> (array_type &amp;a, <code>Time</code> from, <code>Time</code> to, Size steps, const condition_type &amp;condition) </p>
<h2>Detailed Description</h2>
<h3>template&lt;class Evolver&gt; class QuantLib::FiniteDifferenceModel&lt; Evolver &gt;</h3>
<p> Generic finite difference model. </p>
<h2>Member Function Documentation</h2>
<h3>void rollback (array_type &amp; a, <code>Time</code> from, <code>Time</code> to, Size steps)</h3>
<p> solves the problem between the given times. </p>
<p> <code>Warning</code></p>
<dl>
<dt>
<dd> being this a rollback, from must be a later time than to.</dl>
<h3>void rollback (array_type &amp; a, <code>Time</code> from, <code>Time</code> to, Size steps, const condition_type &amp; condition)</h3>
<p> solves the problem between the given times, applying a condition at every step. </p>
<p> <code>Warning</code></p>
<dl>
<dt>
<dd> being this a rollback, from must be a later time than to.</dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for QuantLib from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbAK">Author</a></p>
<dd></dl>
