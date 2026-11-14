---
title: "stdatoistdatolstdatoll(3)"
name: "stdatoistdatolstdatoll"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdatoistdatolstdatoll/"
---

std::atoi,std::atol,std::atoll - std::atoi,std::atol,std::atoll

<h2>Synopsis</h2>

Defined in header &lt;cstdlib&gt; 
int atoi( const char *str ); 
long atol( const char *str ); 
long long atoll( const char *str ); <i>(since C++11)</i> 
Interprets an integer value in a byte string pointed to by str. 
Discards any whitespace characters until the first non-whitespace character is found, then takes as many characters as possible to form a valid integer number representation and converts them to an integer value. The valid integer value consists of the following parts: 
* (optional) plus or minus sign 
* numeric digits 

<h2>Parameters</h2>

str - pointer to the null-terminated byte string to be interpreted

<h2>Return value</h2>

Integer value corresponding to the contents of str on success. If the converted value falls out of range of corresponding return type, the return value is undefined. If no conversion can be performed, 0 is returned. 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;cstdlib&gt;
int main()

{
    const char *str1 = &quot;42&quot;;
    const char *str2 = &quot;3.14159&quot;;
    const char *str3 = &quot;31337 with words&quot;;
    const char *str4 = &quot;words and 2&quot;;
    int num1 = std::atoi(str1);
    int num2 = std::atoi(str2);
    int num3 = std::atoi(str3);
    int num4 = std::atoi(str4);
    std::cout &lt;&lt; &quot;std::atoi(\&quot;&quot; &lt;&lt; str1 &lt;&lt; &quot;\&quot;) is &quot; &lt;&lt; num1 &lt;&lt; '\n';
    std::cout &lt;&lt; &quot;std::atoi(\&quot;&quot; &lt;&lt; str2 &lt;&lt; &quot;\&quot;) is &quot; &lt;&lt; num2 &lt;&lt; '\n';
    std::cout &lt;&lt; &quot;std::atoi(\&quot;&quot; &lt;&lt; str3 &lt;&lt; &quot;\&quot;) is &quot; &lt;&lt; num3 &lt;&lt; '\n';
    std::cout &lt;&lt; &quot;std::atoi(\&quot;&quot; &lt;&lt; str4 &lt;&lt; &quot;\&quot;) is &quot; &lt;&lt; num4 &lt;&lt; '\n';
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;std::atoi(&quot;42&quot;) is 42 
&nbsp;<wbr>&nbsp;std::atoi(&quot;3.14159&quot;) is 3 
&nbsp;<wbr>&nbsp;std::atoi(&quot;31337 with words&quot;) is 31337 
&nbsp;<wbr>&nbsp;std::atoi(&quot;words and 2&quot;) is 0

<h2>See also</h2>

stoi 
stol 
stoll converts a string to a signed integer 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i> 
<i>(C++11)</i> 
<i>(C++11)</i> 
<i>(C++11)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;converts a byte string to an integer value 
strtol <i>(function)</i> 
strtoll 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;converts a byte string to an unsigned integer value 
strtoul <i>(function)</i> 
strtoull 
