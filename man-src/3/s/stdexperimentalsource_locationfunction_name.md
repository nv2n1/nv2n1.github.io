---
title: "stdexperimentalsource_locationfunction_name(3)"
name: "stdexperimentalsource_locationfunction_name"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalsource_locationfunction_name/"
---

std::experimental::source_location::function_name - std::experimental::source_location::function_name

<h2>Synopsis</h2>

constexpr const char* function_name() const noexcept; (library fundamentals TS v2) 
Returns the name of the function associated with the position represented by this object, if any. 

<h2>Parameters</h2>

<i>(none)</i>

<h2>Return value</h2>

If this object represents a position in a body of a function, returns an implementation-defined null-terminated byte string corresponding to the name of the function. 
Otherwise, an empty string is returned. 

<h2>Example</h2>

&nbsp;This section is incomplete 
&nbsp;Reason: no example 

<h2>See also</h2>

<pre><code>return the line number represented by this object

line      (public member function)
return the column number represented by this object

column    (public member function)
return the file name represented by this object

file_name (public member function)




</code></pre>
