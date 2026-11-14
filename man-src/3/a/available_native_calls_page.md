---
title: "available_native_calls_page(3)"
name: "available_native_calls_page"
section: "3"
letter: "a"
url: "/docs/linux/man/3-available_native_calls_page/"
description: "Available_Native_Calls_Page – Available Calls Embryo provides a minimal set of native calls that can be used within any Embryo script."
---

<p>Available_Native_Calls_Page &#8211; Available Calls Embryo provides a minimal set of native calls that can be used within any Embryo script. </p>
<p> Those calls are detailed here. </p>
<p> <code>Note:</code></p>
<dl COMPACT>
<dd>Some of the &#8216;core&#8217; functions here are also described in the full Small documentation given</dl>
<p> <code>Todo</code></p>
<dl COMPACT>
<dd>Finish this section.</dl>
<h2>Argument Functions</h2>
<h3>numargs</h3>
<p>Returns the number of arguments passed to a function. Useful when dealing with variable argument lists.</p>
<h3>getarg(arg, index=0)</h3>
<p>Retrieves the argument number arg. If the argument is an array, use index to specify the index of the array to return.</p>
<h3>setargs(arg, index=0, value)</h3>
<p>Sets the argument number arg to the given arg. index specifies the index of arg to set if arg is an array.</p>
<h2>String Functions</h2>
<p>Functions that work on strings.</p>
<h3>atoi</h3>
<p>Translates an number in string form into an integer.</p>
<h3>fnmatch</h3>
<p>Buggered if I know what this does?</p>
<h3>strcmp</h3>
<p>String comparing function.</p>
<h2>Float Functions</h2>
<h3>float</h3>
<h3>atof</h3>
<h3>float_mul</h3>
<h3>float_div</h3>
<h3>float_add</h3>
<h3>float_sub</h3>
<h3>fract</h3>
<h3>round</h3>
<h3>float_cmp</h3>
<h3>sqrt</h3>
<h3>pow</h3>
<h3>log</h3>
<h3>sin</h3>
<h3>cos</h3>
<h3>tan</h3>
<h3>abs</h3>
<p>Returns the absolute value of the given float.</p>
<h2>Time Functions</h2>
<h3>seconds()</h3>
<h3>date</h3>
<h2>Random Functions</h2>
<h3>rand()</h3>
<p>Returns a random integer.</p>
<h3>randf()</h3>
<p>Returns a random float.</p>
