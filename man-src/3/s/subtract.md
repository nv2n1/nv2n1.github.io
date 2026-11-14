---
title: "subtract(3)"
name: "subtract"
section: "3"
letter: "s"
url: "/docs/linux/man/3-subtract/"
description: "QuantLib::CompositeInstrument – Composite instrument"
---

<p>QuantLib::CompositeInstrument &#8211; Composite instrument </p>
<h2>Synopsis</h2>
<pre><code>void add (const boost::shared_ptr&lt; Instrument &gt; &amp;instrument, Real multiplier=1.0)


adds an instrument to the composite


void subtract (const boost::shared_ptr&lt; Instrument &gt; &amp;instrument, Real multiplier=1.0)


shorts an instrument from the composite



Instrument interface</code></pre>
<p> Inherits <code>QuantLib::Instrument</code>.</p>
<h3>Public Member Functions</h3>
<pre><code>void add (const boost::shared_ptr&lt; Instrument &gt; &amp;instrument, Real multiplier=1.0)


adds an instrument to the composite


void subtract (const boost::shared_ptr&lt; Instrument &gt; &amp;instrument, Real multiplier=1.0)


shorts an instrument from the composite



Instrument interface</code></pre>
<p> bool <code>isExpired</code> () const<br />
 <i>returns whether the instrument is still tradable. </i><br />
 void <code>performCalculations</code> () const</p>
<h2>Detailed Description</h2>
<p>Composite instrument </p>
<p> This instrument is an aggregate of other instruments. Its NPV is the sum of the NPVs of its components, each possibly multiplied by a given factor. </p>
<p> <code>Example: </code> <code>static replication of a down-and-out barrier option </code> </p>
<p> <code>Warning</code></p>
<dl>
<dd>Methods that drive the calculation directly (such as <code>recalculate()</code>, <code>freeze()</code> and others) might not work correctly.</dl>
<p> <code>Examples: </code> </p>
<p> <code>Replication.cpp</code>.</p>
<h2>Member Function Documentation</h2>
<h3>void performCalculations () const [protected, virtual]</h3>
<p>In case a pricing engine is <code>not</code> used, this method must be overridden to perform the actual calculations and set any needed results. In case a pricing engine is used, the default implementation can be used. </p>
<p> Reimplemented from <code>Instrument</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
