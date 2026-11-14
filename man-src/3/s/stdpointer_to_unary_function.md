---
title: "stdpointer_to_unary_function(3)"
name: "stdpointer_to_unary_function"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdpointer_to_unary_function/"
---

std::pointer_to_unary_function - std::pointer_to_unary_function

<h2>Synopsis</h2>

<pre><code>template&lt;

class Arg,                                                                    (deprecated in C++11)

class Result                                                                  (removed in C++17)

&gt; class pointer_to_unary_function : public std::unary_function&lt;Arg, Result&gt;;</code></pre> 
std::pointer_to_unary_function is a function object that acts as a wrapper around a unary function. 

<h2>Member functions</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;constructs a new pointer_to_unary_function object with the supplied function 
constructor <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;calls the stored function 
operator() <i>(public member function)</i> 

 

 
&nbsp;std::pointer_to_unary_function::pointer_to_unary_function 

 

 
explicit pointer_to_unary_function( Result (*f)(Arg) ); 

 
Constructs a pointer_to_unary_function function object with the stored function f.

<h2>Parameters</h2>

f - pointer to a function to store 

 

 
&nbsp;std::pointer_to_unary_function::operator() 

 

 
Result operator()( Arg x ) const; 

 
Calls the stored function.

<h2>Parameters</h2>

x - argument to pass to the function

<h2>Return value</h2>

The value returned by the called function. 

<h2>See also</h2>

pointer_to_binary_function adaptor-compatible wrapper for a pointer to binary function 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i> 
(deprecated in C++11) 
(removed in C++17) 
ptr_fun creates an adaptor-compatible function object wrapper from a pointer to function 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
(deprecated in C++11) 
(removed in C++17) 
