---
title: "make_step_iterator(3)"
name: "make_step_iterator"
section: "3"
letter: "m"
url: "/docs/linux/man/3-make_step_iterator/"
description: "QuantLib::step_iterator – Iterator advancing in constant steps."
---

<h2 class="name">NAME</h2>
<p> QuantLib::step_iterator &#8211; Iterator advancing in constant steps. </p>
<h2>SYNOPSIS</h2>
<p> #include &lt;ql/utilities/steppingiterator.hpp&gt; </p>
<p> Inherits boost::iterator_adaptor&lt;step_iterator&lt;Iterator&gt;, Iterator&gt;. </p>
<h3>Public Member Functions</h3>
<p> <code>step_iterator</code> (const Iterator &amp;base, Size step) </p>
<p> template&lt;class OtherIterator &gt; <code>step_iterator</code> (const <code>step_iterator</code>&lt; OtherIterator &gt; &amp;i, typename boost::enable_if_convertible&lt; OtherIterator, Iterator &gt;::type *=0) </p>
<p> Size <code>step</code> () const </p>
<p> void <code>increment</code> () </p>
<p> void <code>decrement</code> () </p>
<p> void <code>advance</code> (typename super_t::difference_type n) </p>
<p> super_t::difference_type <code>distance_to</code> (const <code>step_iterator</code> &amp;i) const </p>
<h3>Related Functions</h3>
<p> (Note that these are not member functions.)<br />
 template&lt;class Iterator &gt; <code>step_iterator</code>&lt; Iterator &gt; <code>make_step_iterator</code> (Iterator it, Size step)<br />
 <i>helper function to create step iterators </i></p>
<h2>Detailed Description</h2>
<h3>template&lt;class Iterator&gt; class QuantLib::step_iterator&lt; Iterator &gt;</h3>
<p> Iterator advancing in constant steps. </p>
<p> This iterator advances an underlying random-access iterator in steps of $ n $ positions, where $ n $ is a positive integer given upon construction.</p>
<h2>Friends And Related Function Documentation</h2>
<h3><code>step_iterator</code>&lt; Iterator &gt; make_step_iterator (Iterator it, Size step) [related]</h3>
<p> helper function to create step iterators </p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for QuantLib from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbAJ">Author</a></p>
<dd></dl>
