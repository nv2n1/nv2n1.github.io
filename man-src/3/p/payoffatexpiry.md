---
title: "payoffatexpiry(3)"
name: "payoffatexpiry"
section: "3"
letter: "p"
url: "/docs/linux/man/3-payoffatexpiry/"
description: "QuantLib::EarlyExercise – Early-exercise base class."
---

<p>QuantLib::EarlyExercise &#8211; Early-exercise base class. </p>
<h2>Synopsis</h2>
<pre><code>EarlyExercise (Type type, bool payoffAtExpiry=false)



bool payoffAtExpiry () const</code></pre>
<p> Inherits <code>QuantLib::Exercise</code>. Inherited by <code>AmericanExercise</code>, and <code>BermudanExercise</code>.</p>
<h3>Public Member Functions</h3>
<pre><code>EarlyExercise (Type type, bool payoffAtExpiry=false)



bool payoffAtExpiry () const</code></pre>
<h2>Detailed Description</h2>
<p>Early-exercise base class. </p>
<p> The payoff can be at exercise (the default) or at expiry</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
