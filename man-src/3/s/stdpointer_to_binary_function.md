---
title: "stdpointer_to_binary_function(3)"
name: "stdpointer_to_binary_function"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdpointer_to_binary_function/"
---

std::pointer_to_binary_function - std::pointer_to_binary_function

<h2>Synopsis</h2>

<pre><code>template&lt;

class Arg1,                                                                            (deprecated in C++11)

class Arg2,                                                                            (removed in C++17)

class Result

&gt; class pointer_to_binary_function : public std::binary_function&lt;Arg1, Arg2, Result&gt;;</code></pre> 
std::pointer_to_binary_function is a function object that acts as a wrapper around a binary function. 

<h2>Member functions</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;constructs a new pointer_to_binary_function object with the supplied function 
constructor <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;calls the stored function 
operator() <i>(public member function)</i> 

 

 
&nbsp;std::pointer_to_binary_function::pointer_to_binary_function 

 

 
explicit pointer_to_binary_function( Result (*f)(Arg1,Arg2) ); 

 
Constructs a pointer_to_binary_function function object with the stored function f.

<h2>Parameters</h2>

f - pointer to a function to store 

 

 
&nbsp;std::pointer_to_binary_function::operator() 

 

 
Result operator()( Arg1 x1, Arg2 x2 ) const; 

 
Calls the stored function.

<h2>Parameters</h2>

x1, x2 - arguments to pass to the function

<h2>Return value</h2>

The value returned by the called function. 

<h2>See also</h2>

pointer_to_unary_function adaptor-compatible wrapper for a pointer to unary function 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i> 
(deprecated in C++11) 
(removed in C++17) 
ptr_fun creates an adaptor-compatible function object wrapper from a pointer to function 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
(deprecated in C++11) 
(removed in C++17) 
