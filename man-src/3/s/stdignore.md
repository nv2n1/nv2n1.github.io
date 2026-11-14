---
title: "stdignore(3)"
name: "stdignore"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdignore/"
---

std::ignore - std::ignore

<h2>Synopsis</h2>

Defined in header &lt;tuple&gt; 
const /*unspecified*/ ignore; <i>(since C++11)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(until C++17)</i> 
inline constexpr /*unspecified*/ ignore; <i>(since C++17)</i> 
An object of unspecified type such that any value can be assigned to it with no effect. Intended for use with std::tie when unpacking a std::tuple, as a placeholder for the arguments that are not used. 

<h2>Example</h2>

unpack a pair returned by set.insert(), but only save the boolean. 
 // Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;string&gt;

#include &lt;set&gt;

#include &lt;tuple&gt;
int main()

{
    std::set&lt;std::string&gt; set_of_str;
    bool inserted = false;
    std::tie(std::ignore, inserted) = set_of_str.insert(&quot;Test&quot;);
    if (inserted) {
        std::cout &lt;&lt; &quot;Value was inserted successfully\n&quot;;
    }
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;Value was inserted successfully

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;creates a tuple of lvalue references or unpacks a tuple into individual objects 
tie <i>(function template)</i> 
