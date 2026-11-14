---
title: "stdmake_error_conditionstderrc(3)"
name: "stdmake_error_conditionstderrc"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdmake_error_conditionstderrc/"
---

std::make_error_condition(std::errc) - std::make_error_condition(std::errc)

<h2>Synopsis</h2>

Defined in header &lt;system_error&gt; 
std::error_condition make_error_condition( std::errc e ) noexcept; <i>(since C++11)</i> 
Creates an error condition for an errc value e. Sets the error code to int(e) and error category to std::generic_category. 

<h2>Parameters</h2>

e - standard error code

<h2>Return value</h2>

Error condition for e. 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;system_error&gt;

#include &lt;string&gt;

#include &lt;iostream&gt;
int main()

{
    auto err = std::make_error_condition(std::errc::invalid_argument);
    std::cout &lt;&lt; err.message() &lt;&lt; '\n';
}
</code></pre>

<h2>Possible output:</h2>

&nbsp;<wbr>&nbsp;Invalid argument
