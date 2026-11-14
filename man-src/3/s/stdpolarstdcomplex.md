---
title: "stdpolarstdcomplex(3)"
name: "stdpolarstdcomplex"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdpolarstdcomplex/"
---

std::polar(std::complex) - std::polar(std::complex)

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;complex&gt;

    template &lt;class T&gt;

    complex&lt;T&gt; polar(const T &amp;r, const T &amp;theta = T());</code></pre> 
Returns a complex number with magnitude r and phase angle theta. 
The behavior is undefined if r is negative or NaN, or if theta is infinite. 

<h2>Parameters</h2>

r - magnitude 
theta - phase angle

<h2>Return value</h2>

a complex number determined by r and theta 
Defect reports 
The following behavior-changing defect reports were applied retroactively to previously published C++ standards. 
DR Applied to Behavior as published Correct behavior 
LWG_2459 C++98 behavior unclear for some inputs made undefined 
LWG_2870 C++98 default value of parameter theta not dependent made dependent 

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns the magnitude of a complex number 
abs(std::complex) <i>(function template)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns the phase angle 
arg <i>(function template)</i> 
