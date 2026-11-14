---
title: "stdstrspn(3)"
name: "stdstrspn"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdstrspn/"
---

std::strspn - std::strspn

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;cstring&gt;

    size_t strspn(const char *dest, const char *src);</code></pre> 
Returns the length of the maximum initial segment (span) of the byte string pointed to by dest, that consists of only the characters found in byte string pointed to by src. 

<h2>Parameters</h2>

dest - pointer to the null-terminated byte string to be analyzed 
src - pointer to the null-terminated byte string that contains the characters to search for

<h2>Return value</h2>

The length of the maximum initial segment that contains only characters from byte string pointed to by src 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;cstring&gt;

#include &lt;string&gt;

#include &lt;iostream&gt;
const char *low_alpha = &quot;qwertyuiopasdfghjklzxcvbnm&quot;;

int main()

{
    std::string s = &quot;abcde312$#@&quot;;
    std::size_t spnsz = std::strspn(s.c_str(), low_alpha);
    std::cout &lt;&lt; &quot;After skipping initial lowercase letters from '&quot; &lt;&lt; s
              &lt;&lt; &quot;'\nThe remainder is '&quot; &lt;&lt; s.substr(spnsz) &lt;&lt; &quot;'\n&quot;;
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;After skipping initial lowercase letters from 'abcde312$#@' 
&nbsp;<wbr>&nbsp;The remainder is '312$#@'

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns the length of the maximum initial segment that consists 
strcspn of only the characters not found in another byte string 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns the length of the maximum initial segment that consists 
wcsspn of only the wide characters found in another wide string 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;finds the first location of any character from a set of separators 
strpbrk <i>(function)</i> 
