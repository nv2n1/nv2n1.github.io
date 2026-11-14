---
title: "stdrethrow_exception(3)"
name: "stdrethrow_exception"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdrethrow_exception/"
---

std::rethrow_exception - std::rethrow_exception

<h2>Synopsis</h2>

Defined in header &lt;exception&gt; 
[[noreturn]] void rethrow_exception( std::exception_ptr p ) <i>(since C++11)</i> 
Throws the previously captured exception object, referred to by the exception pointer p. 

<h2>Parameters</h2>

p - non-null std::exception_ptr

<h2>Return value</h2>

<i>(none)</i> 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;string&gt;

#include &lt;exception&gt;

#include &lt;stdexcept&gt;
void handle_eptr(std::exception_ptr eptr) // passing by value is ok

{
    try {
        if (eptr) {
            std::rethrow_exception(eptr);
        }
    } catch (const std::exception &amp;e) {
        std::cout &lt;&lt; &quot;Caught exception \&quot;&quot; &lt;&lt; e.what() &lt;&lt; &quot;\&quot;\n&quot;;
    }
}
int main()

{
    std::exception_ptr eptr;
    try {
        std::string().at(1); // this generates an std::out_of_range
    } catch (...) {
        eptr = std::current_exception(); // capture
    }
    handle_eptr(eptr);

} // destructor for std::out_of_range called here, when the eptr is destructed
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;Caught exception &quot;basic_string::at&quot;

<h2>See also</h2>

exception_ptr shared pointer type for handling exception objects 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(typedef)</i> 
<i>(C++11)</i> 
current_exception captures the current exception in a std::exception_ptr 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i> 
<i>(C++11)</i> 
