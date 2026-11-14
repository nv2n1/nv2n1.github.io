---
title: "scalegrid(3)"
name: "scalegrid"
section: "3"
letter: "s"
url: "/docs/linux/man/3-scalegrid/"
description: "QuantLib::SampledCurve – This class contains a sampled curve."
---

<p>QuantLib::SampledCurve &#8211; This class contains a sampled curve. </p>
<h2>Synopsis</h2>
<pre><code>void swap (SampledCurve &amp;)



void setLogGrid (Real min, Real max)



void regridLogGrid (Real min, Real max)



void shiftGrid (Real s)



void scaleGrid (Real s)



void regrid (const Array &amp;new_grid)



template&lt;class T &gt; void regrid (const Array &amp;new_grid, T func)



template&lt;class T &gt; const SampledCurve &amp; transform (T x)



template&lt;class T &gt; const SampledCurve &amp; transformGrid (T x)</code></pre>
<h3>Public Member Functions</h3>
<p>void swap (SampledCurve &amp;)</p>
<p>void setLogGrid (Real min, Real max)</p>
<p>void regridLogGrid (Real min, Real max)</p>
<p>void shiftGrid (Real s)</p>
<p>void scaleGrid (Real s)</p>
<p>void regrid (const Array &amp;new_grid)</p>
<p>template&lt;class T &gt; void regrid (const Array &amp;new_grid, T func)</p>
<p>template&lt;class T &gt; const SampledCurve &amp; transform (T x)</p>
<p>template&lt;class T &gt; const SampledCurve &amp; transformGrid (T x) <code>inspectors</code><br />
 void swap (SampledCurve &amp;)</p>
<p>void setLogGrid (Real min, Real max)</p>
<p>void regridLogGrid (Real min, Real max)</p>
<p>void shiftGrid (Real s)</p>
<p>void scaleGrid (Real s)</p>
<p>void regrid (const Array &amp;new_grid)</p>
<p>template&lt;class T &gt; void regrid (const Array &amp;new_grid, T func)</p>
<p>template&lt;class T &gt; const SampledCurve &amp; transform (T x)</p>
<p>template&lt;class T &gt; const SampledCurve &amp; transformGrid (T x) <code>modifiers</code><br />
 void swap (SampledCurve &amp;)</p>
<p>void setLogGrid (Real min, Real max)</p>
<p>void regridLogGrid (Real min, Real max)</p>
<p>void shiftGrid (Real s)</p>
<p>void scaleGrid (Real s)</p>
<p>void regrid (const Array &amp;new_grid)</p>
<p>template&lt;class T &gt; void regrid (const Array &amp;new_grid, T func)</p>
<p>template&lt;class T &gt; const SampledCurve &amp; transform (T x)</p>
<p>template&lt;class T &gt; const SampledCurve &amp; transformGrid (T x) <code>calculations</code> </p>
<p> <code>Real</code> <code>valueAtCenter</code> () const </p>
<p> <code>Real</code> <code>firstDerivativeAtCenter</code> () const </p>
<p> <code>Real</code> <code>secondDerivativeAtCenter</code> () const<br />
 <code>utilities</code> </p>
<pre><code>void swap (SampledCurve &amp;)



void setLogGrid (Real min, Real max)



void regridLogGrid (Real min, Real max)



void shiftGrid (Real s)



void scaleGrid (Real s)



void regrid (const Array &amp;new_grid)



template&lt;class T &gt; void regrid (const Array &amp;new_grid, T func)



template&lt;class T &gt; const SampledCurve &amp; transform (T x)



template&lt;class T &gt; const SampledCurve &amp; transformGrid (T x)</code></pre>
<h2>Detailed Description</h2>
<p>This class contains a sampled curve. </p>
<p> Initially the class will contain one indexed curve</p>
<h2>Member Function Documentation</h2>
<h3><code>Real</code> valueAtCenter () const</h3>
<p><code>Possible enhancements</code></p>
<dl>
<dd>replace or complement with a more general function valueAt(spot)</dl>
<h3><code>Real</code> firstDerivativeAtCenter () const</h3>
<p><code>Possible enhancements</code></p>
<dl>
<dd>replace or complement with a more general function firstDerivativeAt(spot)</dl>
<h3><code>Real</code> secondDerivativeAtCenter () const</h3>
<p><code>Possible enhancements</code></p>
<dl>
<dd>replace or complement with a more general function secondDerivativeAt(spot)</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
