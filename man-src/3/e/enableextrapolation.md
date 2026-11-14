---
title: "enableextrapolation(3)"
name: "enableextrapolation"
section: "3"
letter: "e"
url: "/docs/linux/man/3-enableextrapolation/"
description: "QuantLib::Extrapolator – base class for classes possibly allowing extrapolation"
---

<p>QuantLib::Extrapolator &#8211; base class for classes possibly allowing extrapolation </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/math/interpolations/extrapolation.hpp&gt; </p>
<p> Inherited by <code>Interpolation</code>, <code>Interpolation2D</code>, and <code>TermStructure</code>. </p>
<h3>Public Member Functions</h3>
<p><code>modifiers</code> </p>
<p> void <code>enableExtrapolation</code> (bool b=true)<br />
 <i>enable extrapolation in subsequent calls </i><br />
 void <code>disableExtrapolation</code> (bool b=true)<br />
 <i>disable extrapolation in subsequent calls </i> </p>
<p> <code>inspectors</code> </p>
<p> bool <code>allowsExtrapolation</code> () const<br />
 <i>tells whether extrapolation is enabled </i></p>
<h2>Detailed Description</h2>
<p>base class for classes possibly allowing extrapolation </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
