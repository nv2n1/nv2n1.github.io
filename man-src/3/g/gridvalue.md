---
title: "gridvalue(3)"
name: "gridvalue"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gridvalue/"
description: "QuantLib::SampledCurve – This class contains a sampled curve."
---

<p>QuantLib::SampledCurve &#8211; This class contains a sampled curve. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/math/sampledcurve.hpp&gt; </p>
<h3>Public Member Functions</h3>
<p><code>SampledCurve</code> (Size gridSize=0) </p>
<p> <code>SampledCurve</code> (const <code>Array</code> &amp;grid) </p>
<p> <code>SampledCurve</code> &amp; <code>operator=</code> (const <code>SampledCurve</code> &amp;) </p>
<p> <code>inspectors</code> </p>
<p> const <code>Array</code> &amp; <code>grid</code> () const </p>
<p> <code>Array</code> &amp; <code>grid</code> () </p>
<p> const <code>Array</code> &amp; <code>values</code> () const </p>
<p> <code>Array</code> &amp; <code>values</code> () </p>
<p> <code>Real</code> <code>gridValue</code> (Size i) const </p>
<p> <code>Real</code> &amp; <code>gridValue</code> (Size i) </p>
<p> <code>Real</code> <code>value</code> (Size i) const </p>
<p> <code>Real</code> &amp; <code>value</code> (Size i) </p>
<p> Size <code>size</code> () const </p>
<p> bool <code>empty</code> () const </p>
<p> <code>modifiers</code> </p>
<p> void <code>setGrid</code> (const <code>Array</code> &amp;) </p>
<p> void <code>setValues</code> (const <code>Array</code> &amp;) </p>
<p> template&lt;class F &gt; void <code>sample</code> (const F &amp;f) </p>
<p> <code>calculations</code> </p>
<p> <code>Real</code> <code>valueAtCenter</code> () const </p>
<p> <code>Real</code> <code>firstDerivativeAtCenter</code> () const </p>
<p> <code>Real</code> <code>secondDerivativeAtCenter</code> () const </p>
<p> <code>utilities</code> </p>
<p> void <code>swap</code> (<code>SampledCurve</code> &amp;) </p>
<p> void <code>setLogGrid</code> (<code>Real</code> min, <code>Real</code> max) </p>
<p> void <code>regridLogGrid</code> (<code>Real</code> min, <code>Real</code> max) </p>
<p> void <code>shiftGrid</code> (<code>Real</code> s) </p>
<p> void <code>scaleGrid</code> (<code>Real</code> s) </p>
<p> void <code>regrid</code> (const <code>Array</code> &amp;new_grid) </p>
<p> template&lt;class T &gt; void <code>regrid</code> (const <code>Array</code> &amp;new_grid, T func) </p>
<p> template&lt;class T &gt; const <code>SampledCurve</code> &amp; <code>transform</code> (T x) </p>
<p> template&lt;class T &gt; const <code>SampledCurve</code> &amp; <code>transformGrid</code> (T x) </p>
<h2>Detailed Description</h2>
<p>This class contains a sampled curve. </p>
<p> Initially the class will contain one indexed curve</p>
<h2>Member Function Documentation</h2>
<h3><code>Real</code> valueAtCenter () const</h3>
<p><code>Possible enhancements</code></p>
<dl COMPACT>
<dd>replace or complement with a more general function valueAt(spot)</dl>
<h3><code>Real</code> firstDerivativeAtCenter () const</h3>
<p><code>Possible enhancements</code></p>
<dl COMPACT>
<dd>replace or complement with a more general function firstDerivativeAt(spot)</dl>
<h3><code>Real</code> secondDerivativeAtCenter () const</h3>
<p><code>Possible enhancements</code></p>
<dl COMPACT>
<dd>replace or complement with a more general function secondDerivativeAt(spot)</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
