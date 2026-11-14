---
title: "stdstoistdstolstdstoll(3)"
name: "stdstoistdstolstdstoll"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdstoistdstolstdstoll/"
description: "std::stoi,std::stol,std::stoll – std::stoi,std::stol,std::stoll"
---

<p>std::stoi,std::stol,std::stoll &#8211; std::stoi,std::stol,std::stoll</p>
<h2>Synopsis</h2>
<pre><code>Defined in header&lt;string&gt;

    int stoi(const std::string &amp;str, std::size_t *pos = 0, int base = 10);
(1)(since C++ 11)

    int stoi(const std::wstring &amp;str, std::size_t *pos = 0, int base = 10);

long stol(const std::string &amp;str, std::size_t *pos = 0, int base = 10);
(2)(since C++ 11)

    long stol(const std::wstring &amp;str, std::size_t *pos = 0, int base = 10);

long long stoll(const std::string &amp;str, std::size_t *pos = 0, int base = 10);
(3)(since C++ 11)

    long long stoll(const std::wstring &amp;str, std::size_t *pos = 0, int base = 10);
Interprets a signed integer value in the string str.

1) calls std::strtol(str.c_str(), &amp;ptr, base) or std::wcstol(str.c_str(), &amp;ptr, base)

2) calls std::strtol(str.c_str(), &amp;ptr, base) or std::wcstol(str.c_str(), &amp;ptr, base)

3) calls std::strtoll(str.c_str(), &amp;ptr, base) or std::wcstoll(str.c_str(), &amp;ptr, base)

Discards any whitespace characters (as identified by calling isspace()) until the first non-whitespace character is found, then takes as many characters as possible to form a valid base-n (where n=base) integer number representation and converts them to an integer value. The valid integer value consists of the following parts:</code></pre>
<p>* (optional) plus or minus sign<br />
* (optional) prefix <code>(0)</code> indicating octal base (applies only when the base is 8 or 0)<br />
* (optional) prefix (0x or 0X) indicating hexadecimal base (applies only when the base is 16 or 0)<br />
* a sequence of digits<br />
The set of valid values for base is {0,2,3,&#8230;,36}. The set of valid digits for base-2 integers is {0,1}, for base-3 integers is {0,1,2}, and so on. For bases larger than 10, valid digits include alphabetic characters, starting from Aa for base-11 integer, to Zz for base-36 integer. The case of the characters is ignored.<br />
Additional numeric formats may be accepted by the currently installed C locale.<br />
If the value of base is 0, the numeric base is auto-detected: if the prefix is 0, the base is octal, if the prefix is 0x or 0X, the base is hexadecimal, otherwise the base is decimal.<br />
If the minus sign was part of the input sequence, the numeric value calculated from the sequence of digits is negated as if by unary_minus in the result type.<br />
If pos is not a null pointer, then a pointer ptr &#8211; internal to the conversion functions &#8211; will receive the address of the first unconverted character in str.c_str(), and the index of that character will be calculated and stored in *pos, giving the number of characters that were processed by the conversion. </p>
<h2>Parameters</h2>
<p>str &#8211; the string to convert<br />
pos &#8211; address of an integer to store the number of characters processed<br />
base &#8211; the number base</p>
<h2>Return value</h2>
<p>The string converted to the specified signed integer type. </p>
<h2>Exceptions</h2>
<p>* std::invalid_argument if no conversion could be performed<br />
* std::out_of_range if the converted value would fall out of the range of the result type or if the underlying function (std::strtol or std::strtoll) sets errno to ERANGE.</p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;iostream&gt;

#include &lt;string&gt;
int main()

{
    std::string str1 = &quot;45&quot;;
    std::string str2 = &quot;3.14159&quot;;
    std::string str3 = &quot;31337 with words&quot;;
    std::string str4 = &quot;words and 2&quot;;
    int myint1 = std::stoi(str1);
    int myint2 = std::stoi(str2);
    int myint3 = std::stoi(str3);
    // error: 'std::invalid_argument'
    // int myint4 = std::stoi(str4);
    std::cout &lt;&lt; &quot;std::stoi(\&quot;&quot; &lt;&lt; str1 &lt;&lt; &quot;\&quot;) is &quot; &lt;&lt; myint1 &lt;&lt; '
';
    std::cout &lt;&lt; &quot;std::stoi(\&quot;&quot; &lt;&lt; str2 &lt;&lt; &quot;\&quot;) is &quot; &lt;&lt; myint2 &lt;&lt; '
';
    std::cout &lt;&lt; &quot;std::stoi(\&quot;&quot; &lt;&lt; str3 &lt;&lt; &quot;\&quot;) is &quot; &lt;&lt; myint3 &lt;&lt; '
';
    // std::cout &lt;&lt; &quot;std::stoi(\&quot;&quot; &lt;&lt; str4 &lt;&lt; &quot;\&quot;) is &quot; &lt;&lt; myint4 &lt;&lt; '
';
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;std::stoi(&quot;45&quot;) is 45<br />
&nbsp;<wbr>&nbsp;std::stoi(&quot;3.14159&quot;) is 3<br />
&nbsp;<wbr>&nbsp;std::stoi(&quot;31337 with words&quot;) is 31337</p>
<h2>See also</h2>
<p>atoi converts a byte string to an integer value<br />
atol <i>(function)</i><br />
atoll<br />
stoul<br />
stoull converts a string to an unsigned integer<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
stof<br />
stod<br />
stold converts a string to a floating point value<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
to_string converts an integral or floating point value to string<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++11)</i><br />
from_chars converts a character sequence to an integer or floating-point value<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++17)</i> </p>
