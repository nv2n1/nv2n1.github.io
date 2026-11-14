---
title: "stdstrcspn(3)"
name: "stdstrcspn"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdstrcspn/"
---

std::strcspn - std::strcspn

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;cstring&gt;

    size_t strcspn(const char *dest, const char *src);
Returns the length of the maximum initial segment of the byte string pointed to by dest, that consists of only the characters not found in byte string pointed to by src.

The function name stands for &quot;complementary span&quot;
</code></pre>

<h2>Parameters</h2>

dest - pointer to the null-terminated byte string to be analyzed 
src - pointer to the null-terminated byte string that contains the characters to search for

<h2>Return value</h2>

The length of the maximum initial segment that contains only characters not found in the byte string pointed to by src 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;string&gt;

#include &lt;cstring&gt;

#include &lt;iostream&gt;
const char *invalid = &quot;*$#&quot;;

int main()

{
    std::string s = &quot;abcde312$#@&quot;;
    size_t valid_len = std::strcspn(s.c_str(), invalid);
    if (valid_len != s.size())
        std::cout &lt;&lt; &quot;'&quot; &lt;&lt; s &lt;&lt; &quot;' contains invalid chars starting at position &quot;
                  &lt;&lt; valid_len &lt;&lt; '\n';
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;'abcde312$#@' contains invalid chars starting at position 8

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns the length of the maximum initial segment that consists 
strspn of only the characters found in another byte string 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns the length of the maximum initial segment that consists 
wcscspn of only the wide not found in another wide string 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;finds the first location of any character from a set of separators 
strpbrk <i>(function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;find first occurrence of characters 
find_first_of <i>(public member function of std::basic_string&lt;CharT,Traits,Allocator&gt;)</i> 
