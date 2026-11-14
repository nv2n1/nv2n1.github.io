---
title: "stdrandom_deviceoperator(3)"
name: "stdrandom_deviceoperator"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdrandom_deviceoperator/"
description: "std::random_device::operator() – std::random_device::operator()"
---

<p>std::random_device::operator() &#8211; std::random_device::operator()</p>
<h2>Synopsis</h2>
<p>result_type operator()(); <i>(since C++11)</i><br />
Generates a non-deterministic uniformly-distributed random value. </p>
<h2>Parameters</h2>
<p><i>(none)</i></p>
<h2>Return value</h2>
<p>A random number uniformly distributed in [min(), max()]. </p>
<h2>Exceptions</h2>
<p>Throws an implementation-defined exception derived from std::exception if a random number could not be generated.</p>
<h2>See also</h2>
<p>min gets the smallest possible value in the output range<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member function)</i><br />
<code>[static]</code><br />
max gets the largest possible value in the output range<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member function)</i><br />
<code>[static]</code> </p>
