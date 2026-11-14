---
title: "stdfpos(3)"
name: "stdfpos"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdfpos/"
---

std::fpos - std::fpos

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;ios&gt;

template&lt; class State &gt;

class fpos;</code></pre> 
Specializations of the class template std::fpos identify absolute positions in a stream or in a file. Each object of type fpos holds the byte position in the stream (typically as a private member of type std::streamoff) and the current shift state, a value of type State (typically std::mbstate_t). 
The following specializations of std::fpos are provided: 
Type Definition 
streampos std::fpos&lt;std::char_traits&lt;char&gt;::state_type&gt; 
wstreampos std::fpos&lt;std::char_traits&lt;wchar_t&gt;::state_type&gt; 
u8streampos <i>(since C++20)</i> std::fpos&lt;std::char_traits&lt;char8_t&gt;::state_type&gt; 
u16streampos <i>(since C++11)</i> std::fpos&lt;std::char_traits&lt;char16_t&gt;::state_type&gt; 
u32streampos <i>(since C++11)</i> std::fpos&lt;std::char_traits&lt;char32_t&gt;::state_type&gt; 
All specializations of fpos meet the DefaultConstructible, CopyConstructible, CopyAssignable, Destructible, and EqualityComparable requirements. 
If State is trivially copy constructible, fpos has a trivial copy constructor. If State is trivially copy assignable, fpos has a trivial copy assignment operator. If State is trivially destructible, fpos has a trivial destructor. 
Template parameter 
State - the type representing the shift state

<h2>Type requirements</h2>

- 
State must meet the requirements of Destructible, CopyAssignable, CopyConstructible and DefaultConstructible.

<h2>Member functions</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;gets/sets the value of the shift state 
state <i>(public member function)</i> 

 
In addition, member and non-member functions are provided to support the following operations: 

 
* A default constructor that stores an offset of zero and value-initializes the state object. 

 

 
* A non-explicit constructor that accepts an argument of type (possibly const) std::streamoff, which stores that offset and and value-initializes the state object. This constructor must also accept the special value std::streamoff(-1): the std::fpos constructed in this manner is returned by some stream operations to indicate errors. 

 

 
* Explicit conversion from (possibly const) fpos to std::streamoff. The result is the stored offset. 

 

 
* operator== and operator!= that compare two objects of type (possibly const) std::fpos and returns a value of type convertible to bool. p != q is equivalent to !(p == q). 

 

 
* operator+ and operator- such that, for an object p of type (possibly const) fpos&lt;State&gt; and an object o of type (possibly const) std::streamoff 

 

 

 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* p + o has type fpos&lt;State&gt; and stores an offset that is the result of adding o to the offset of p 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* o + p has a type convertible to fpos&lt;State&gt; and the result of the conversion is equal to p + o 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* p - o has type fpos&lt;State&gt; and stores an offset that is the result of subtracting o from the offset of p 

 

 

 
* operator+= and operator-= which can accept a (possibly const) std::streamoff and adds/subtracts it from the stored offset, respectively. 

 

 
* operator- which can subtract two objects of type (possibly const) std::fpos producing an std::streamoff, such that for two such objects p and q, p == q + (p - q)

<h2>Notes</h2>

 
Defect reports 
The following behavior-changing defect reports were applied retroactively to previously published C++ standards. 
DR Applied to Behavior as published Correct behavior 
P0759R1 C++98 specification was unclear and incomplete cleaned up 
P1148R0 C++11 unclear what header defines u16streampos and u32streampos or what their definitions are made clear 

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;represents relative file/stream position (offset from fpos), sufficient to represent any file size 
streamoff <i>(typedef)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns the output position indicator 
tellp <i>(public member function of std::basic_ostream&lt;CharT,Traits&gt;)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;sets the output position indicator 
seekp <i>(public member function of std::basic_ostream&lt;CharT,Traits&gt;)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;gets the file position indicator 
fgetpos <i>(function)</i> 
