---
title: "step_iterator(3)"
name: "step_iterator"
section: "3"
letter: "s"
url: "/docs/linux/man/3-step_iterator/"
description: "QuantLib::step_iterator – Iterator advancing in constant steps."
---

<p>QuantLib::step_iterator &#8211; Iterator advancing in constant steps. </p>
<h2>Synopsis</h2>
<pre><code>step_iterator (const Iterator &amp;base, Size step)



template&lt;class OtherIterator &gt; step_iterator (const step_iterator&lt; OtherIterator &gt; &amp;i, typename boost::enable_if_convertible&lt; OtherIterator, Iterator &gt;::type *=0)



Size step () const



void increment ()



void decrement ()



void advance (typename super_t::difference_type n)



super_t::difference_type distance_to (const step_iterator &amp;i) const



Related Functions

(Note that these are not member functions.)


template&lt;class Iterator &gt; step_iterator&lt; Iterator &gt; make_step_iterator (Iterator it, Size step)


helper function to create step iterators</code></pre>
<p> Inherits boost::iterator_adaptor&lt;step_iterator&lt;Iterator&gt;, Iterator&gt;.</p>
<h3>Public Member Functions</h3>
<pre><code>step_iterator (const Iterator &amp;base, Size step)



template&lt;class OtherIterator &gt; step_iterator (const step_iterator&lt; OtherIterator &gt; &amp;i, typename boost::enable_if_convertible&lt; OtherIterator, Iterator &gt;::type *=0)



Size step () const



void increment ()



void decrement ()



void advance (typename super_t::difference_type n)



super_t::difference_type distance_to (const step_iterator &amp;i) const



Related Functions

(Note that these are not member functions.)


template&lt;class Iterator &gt; step_iterator&lt; Iterator &gt; make_step_iterator (Iterator it, Size step)


helper function to create step iterators</code></pre>
<h2>Detailed Description</h2>
<h3>template&lt;class Iterator&gt; class QuantLib::step_iterator&lt; Iterator &gt;</h3>
<p>Iterator advancing in constant steps. </p>
<p> This iterator advances an underlying random-access iterator in steps of $ n $ positions, where $ n $ is a positive integer given upon construction.</p>
<h2>Friends And Related Function Documentation</h2>
<h3><code>step_iterator</code>&lt; Iterator &gt; make_step_iterator (Iterator it, Size step) [related]</h3>
<p>helper function to create step iterators</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
