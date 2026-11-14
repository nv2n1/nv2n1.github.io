---
title: "stdexperimentalsource_locationcurrent(3)"
name: "stdexperimentalsource_locationcurrent"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalsource_locationcurrent/"
---

std::experimental::source_location::current - std::experimental::source_location::current

<h2>Synopsis</h2>

<pre><code>static constexpr source_location current() noexcept;  (library fundamentals TS v2)</code></pre> 
Constructs a new source_location object. 

<h2>Return value</h2>

If current() is invoked directly (via a function call that names current()), it returns a source_location object with implementation-defined values representing the location of the call. The values should be affected by the #line_preprocessor_directive in the same manner as the predefined macros __LINE__ and __FILE__. 
If current() is invoked in any other manner, the return value is unspecified. 
Remarks 
If current() is used in an initializer_for_a_non-static_data_member, the return value corresponds to the location of the constructor or aggregate_initialization that initializes the data member. 

<h2>Notes</h2>

When current() is used in a default argument, the return value will correspond to the location of the call to current() at the call site. 

<h2>Parameters</h2>

<i>(none)</i>

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;constructs a new source_location with implementation-defined values 
constructor <i>(public member function)</i> 
