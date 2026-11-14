---
title: "stdset_terminate(3)"
name: "stdset_terminate"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdset_terminate/"
---

std::set_terminate - std::set_terminate

<h2>Synopsis</h2>

Defined in header &lt;exception&gt; 
std::terminate_handler set_terminate( std::terminate_handler f ) throw(); <i>(until C++11)</i> 
std::terminate_handler set_terminate( std::terminate_handler f ) noexcept; <i>(since C++11)</i> 
Makes f the new global terminate handler function and returns the previously installed std::terminate_handler. 
This function is thread-safe. Every call to std::set_terminate synchronizes-with (see std::memory_order) the subsequent std::set_terminate and std::get_terminate <i>(since C++11)</i> 

<h2>Parameters</h2>

f - pointer to function of type std::terminate_handler, or null pointer

<h2>Return value</h2>

The previously-installed terminate handler, or a null pointer value if none was installed. 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;cstdlib&gt;

#include &lt;exception&gt;
int main()

{
    std::set_terminate([]() { std::cout &lt;&lt; &quot;Unhandled exception\n&quot;; std::abort(); });
    throw 1;
}
</code></pre>

<h2>Possible output:</h2>

&nbsp;<wbr>&nbsp;Unhandled exception 
&nbsp;<wbr>&nbsp;bash: line 7: 7743 Aborted (core dumped) ./a.out

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;function called when exception handling fails 
terminate <i>(function)</i> 
get_terminate obtains the current terminate_handler 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i> 
<i>(C++11)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;the type of the function called by std::terminate 
terminate_handler <i>(typedef)</i> 
