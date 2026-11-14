---
title: "stdsystem_category(3)"
name: "stdsystem_category"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdsystem_category/"
---

std::system_category - std::system_category

<h2>Synopsis</h2>

Defined in header &lt;system_error&gt; 
const std::error_category&amp; system_category() noexcept; <i>(since C++11)</i> <pre><code>Obtains a reference to the static error category object for errors reported by the operating system. The object is required to override the virtual function std::error_category::name() to return a pointer to the string &quot;system&quot;. It is also required to override the virtual function std::error_category::default_error_condition() to map the error codes that match POSIX errno values to std::generic_category.
</code></pre>

<h2>Parameters</h2>

<i>(none)</i>

<h2>Return value</h2>

A reference to the static object of unspecified runtime type, derived from std::error_category. 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;system_error&gt;

#include &lt;iomanip&gt;

#include &lt;string&gt;
int main()

{
    std::error_condition econd = std::system_category().default_error_condition(EDOM);
    std::cout &lt;&lt; &quot;Category: &quot; &lt;&lt; econd.category().name() &lt;&lt; '\n'
              &lt;&lt; &quot;Value: &quot; &lt;&lt; econd.value() &lt;&lt; '\n'
              &lt;&lt; &quot;Message: &quot; &lt;&lt; econd.message() &lt;&lt; '\n';
    econd = std::system_category().default_error_condition(10001);
    std::cout &lt;&lt; &quot;Category: &quot; &lt;&lt; econd.category().name() &lt;&lt; '\n'
              &lt;&lt; &quot;Value: &quot; &lt;&lt; econd.value() &lt;&lt; '\n'
              &lt;&lt; &quot;Message: &quot; &lt;&lt; econd.message() &lt;&lt; '\n';
}
</code></pre>

<h2>Possible output:</h2>

&nbsp;<wbr>&nbsp;Category: generic 
&nbsp;<wbr>&nbsp;Value: 33 
&nbsp;<wbr>&nbsp;Message: Numerical argument out of domain 
&nbsp;<wbr>&nbsp;Category: system 
&nbsp;<wbr>&nbsp;Value: 10001 
&nbsp;<wbr>&nbsp;Message: Unknown error 10001

<h2>See also</h2>

generic_category identifies the generic error category 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i> 
<i>(C++11)</i> 
errc the std::error_condition enumeration listing all standard &lt;cerrno&gt; macro constants 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class)</i> 
<i>(C++11)</i> 
