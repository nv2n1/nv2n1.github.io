---
title: "tcalc(1)"
name: "tcalc"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tcalc/"
description: "tcalc – The terminal calculator"
---

<h2>NAME</h2>
<p> tcalc &#8211; The terminal calculator</p>
<h2>SYNOPSIS</h2>
<p> <code>tcalc [OPTIONS] [file-name]</code></p>
<h2>DESCRIPTION</h2>
<p> The terminal calculator is a small and helpful program to help users of the GNU/Linux terminal do calculations simply and quickly. The formula to be calculated can be fed to tcalc through the command line. Alternatively, tcalc can be run with no formula and then the free mode is started, in which the calculator will wait for user input, do the necessary calculations and print out the result, and the cycle will repeat until the user enters &#8216;q&#8217; or &#8216;quit&#8217;. </p>
<p> The calculator works with the decimal, hexadecimal, octal, and binary number systems. It automatically identifies hex numbers if entered with a preceding &quot;0x&quot; or &quot;0X&quot;, octal by preceding the number with a zero, binaries by preceding the number with &#8216;b&#8217; and decimals by absence of all of the above. Alternatively, the user can indicate the type of input by setting the &#8216;format&#8217; argument (See below). </p>
<p> Math functions defined are:<br />
 &#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;<br />
&nbsp;<wbr>&nbsp;<wbr>acos(x)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Arc cosine of X<br />
&nbsp;<wbr>&nbsp;<wbr>asin(x)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Arc sine of X<br />
&nbsp;<wbr>&nbsp;<wbr>atan(x)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Arc tangent of X<br />
&nbsp;<wbr>&nbsp;<wbr>atan2(y, x)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Arc tangent of Y/X<br />
&nbsp;<wbr>&nbsp;<wbr>cos(x)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Cosine of X<br />
&nbsp;<wbr>&nbsp;<wbr>sin(x)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Sine of X<br />
&nbsp;<wbr>&nbsp;<wbr>tan(x)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Tangent of X<br />
&nbsp;<wbr>&nbsp;<wbr>cosh(x)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Hyperbolic cosine of X<br />
&nbsp;<wbr>&nbsp;<wbr>sinh(x)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Hyperbolic sine of X<br />
&nbsp;<wbr>&nbsp;<wbr>tanh(x)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Hyperbolic tangent of X<br />
&nbsp;<wbr>&nbsp;<wbr>acosh(x)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Hyperbolic arc cosine of X<br />
&nbsp;<wbr>&nbsp;<wbr>asinh(x)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Hyperbolic arc sine of X<br />
&nbsp;<wbr>&nbsp;<wbr>atanh(x)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Hyperbolic arc tangent of X<br />
&nbsp;<wbr>&nbsp;<wbr>exp(x)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Exponential function of X<br />
&nbsp;<wbr>&nbsp;<wbr>log(x)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Natural logarithm of X<br />
&nbsp;<wbr>&nbsp;<wbr>log10(x)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Base-ten logarithm of X<br />
&nbsp;<wbr>&nbsp;<wbr>pow(x, y)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>X to the power Y<br />
&nbsp;<wbr>&nbsp;<wbr>sqrt(x)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Square root of X<br />
&nbsp;<wbr>&nbsp;<wbr>cbrt(x)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Cube root of X<br />
&nbsp;<wbr>&nbsp;<wbr>ceil(x)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Smallest integral value not less than X<br />
&nbsp;<wbr>&nbsp;<wbr>floor(x)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Largest integer not greater than X<br />
&nbsp;<wbr>&nbsp;<wbr>fabs(x)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Absolute value of X<br />
&nbsp;<wbr>&nbsp;<wbr>round(x)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Round X to nearest integral value, rounding halfway cases away<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>from zero<br />
&nbsp;<wbr>&nbsp;<wbr>trunc(x)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Round X to the integral value in floating-point format nearest<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>but not larger in magnitude<br />
 These functions can be called within a formula. to have a printout of the above list, use the &quot;-m&quot; or &quot;&#8211;math&quot; flags (see below). </p>
<p> The free mode:<br />
 &#8212;&#8212;&#8212;&#8212;&#8211;<br />
 If you start tcalc with no command line formula and no input file, this will invoke the free mode. You will see a &#8216;&gt;&#8217; prompt indicating this mode. Enter your formulas one by one, ending each one with an ENTER, and tcalc will process the formula and output the result. You can enter other commands like</p>
<h2>Index</h2>
