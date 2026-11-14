---
title: "adime_double2string(3)"
name: "adime_double2string"
section: "3"
letter: "a"
url: "/docs/linux/man/3-adime_double2string/"
description: "adime_double2string"
---

<h2>NAME</h2>
<p> adime_double2string</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/adime.h">adime.h</a>&gt;</code> </p>
<p> <code>void adime_double2string(double x, char *buf);</code></p>
<h2>DESCRIPTION</h2>
<p> Function for pretty-printing floating point numbers: The number gets at most 10 digits to the left of the decimal point, at most 9 to the right of it, and at most 10 totally. If the absolute value of the number is &gt;= 10000000000 or &lt; 0.000001, it is written in exponential form instead. Exponential form has at most 6 digits in the mantissa, so that the total number of digits never exceeds 9. Does not support Unicode. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-adime_udouble2string/">adime_udouble2string</a></code>(3) </p>
<h2>Index</h2>
