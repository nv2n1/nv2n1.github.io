---
title: "path(3)"
name: "path"
section: "3"
letter: "p"
url: "/docs/linux/man/3-path/"
description: "QuantLib::Path – single-factor random walk"
---

<p>QuantLib::Path &#8211; single-factor random walk </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/methods/montecarlo/path.hpp&gt; </p>
<h3>Public Member Functions</h3>
<p><code>Path</code> (const <code>TimeGrid</code> &amp;timeGrid, const <code>Array</code> &amp;values=<code>Array</code>()) </p>
<p> <code>inspectors</code> </p>
<p> bool <code>empty</code> () const </p>
<p> Size <code>length</code> () const </p>
<p> <code>Real</code> <code>operator[]</code> (Size i) const<br />
 <i>asset value at the $ i $-th point </i><br />
 <code>Real</code> <code>at</code> (Size i) const </p>
<p> <code>Real</code> &amp; <code>operator[]</code> (Size i) </p>
<p> <code>Real</code> &amp; <code>at</code> (Size i) </p>
<p> <code>Real</code> <code>value</code> (Size i) const </p>
<p> <code>Real</code> &amp; <code>value</code> (Size i) </p>
<p> <code>Time</code> <code>time</code> (Size i) const<br />
 <i>time at the $ i $-th point </i><br />
 <code>Real</code> <code>front</code> () const<br />
 <i>initial asset value </i><br />
 <code>Real</code> &amp; <code>front</code> () </p>
<p> <code>Real</code> <code>back</code> () const<br />
 <i>final asset value </i><br />
 <code>Real</code> &amp; <code>back</code> () </p>
<p> const <code>TimeGrid</code> &amp; <code>timeGrid</code> () const<br />
 <i>time grid </i></p>
<h3>iterators</h3>
<p>typedef Array::const_iterator <code>iterator</code> </p>
<p> typedef Array::const_reverse_iterator <code>reverse_iterator</code> </p>
<p> iterator <code>begin</code> () const </p>
<p> iterator <code>end</code> () const </p>
<p> reverse_iterator <code>rbegin</code> () const </p>
<p> reverse_iterator <code>rend</code> () const </p>
<h2>Detailed Description</h2>
<p>single-factor random walk </p>
<p> <code>Note:</code></p>
<dl COMPACT>
<dd>the path includes the initial asset value as its first point.</dl>
<p> <code>Examples: </code> </p>
<p> <code>DiscreteHedging.cpp</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
