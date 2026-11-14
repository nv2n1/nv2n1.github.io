---
title: "stdstrtolstdstrtoll(3)"
name: "stdstrtolstdstrtoll"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdstrtolstdstrtoll/"
description: "std::strtol,std::strtoll – std::strtol,std::strtoll"
---

<p>std::strtol,std::strtoll &#8211; std::strtol,std::strtoll</p>
<h2>Synopsis</h2>
<p>Defined in header &lt;cstdlib&gt;<br />
long strtol( const char *str, char **str_end, int base );<br />
long long strtoll( const char *str, char **str_end, int base ); <i>(since C++11)</i> </p>
<pre><code>Interprets an integer value in a byte string pointed to by str.

Discards any whitespace characters (as identified by calling isspace()) until the first non-whitespace character is found, then takes as many characters as possible to form a valid base-n (where n=base) integer number representation and converts them to an integer value. The valid integer value consists of the following parts:</code></pre>
<p>* (optional) plus or minus sign<br />
* (optional) prefix <code>(0)</code> indicating octal base (applies only when the base is 8 or 0)<br />
* (optional) prefix (0x or 0X) indicating hexadecimal base (applies only when the base is 16 or 0)<br />
* a sequence of digits<br />
The set of valid values for base is {0,2,3,&#8230;,36}. The set of valid digits for base-2 integers is {0,1}, for base-3 integers is {0,1,2}, and so on. For bases larger than 10, valid digits include alphabetic characters, starting from Aa for base-11 integer, to Zz for base-36 integer. The case of the characters is ignored.<br />
Additional numeric formats may be accepted by the currently installed C locale.<br />
If the value of base is 0, the numeric base is auto-detected: if the prefix is 0, the base is octal, if the prefix is 0x or 0X, the base is hexadecimal, otherwise the base is decimal.<br />
If the minus sign was part of the input sequence, the numeric value calculated from the sequence of digits is negated as if by unary_minus in the result type.<br />
The functions sets the pointer pointed to by str_end to point to the character past the last character interpreted. If str_end is NULL, it is ignored.<br />
If the str is empty or does not have the expected form, no conversion is performed, and (if str_end is not NULL) the value of str is stored in the object pointed to by str_end. </p>
<h2>Parameters</h2>
<p>str &#8211; pointer to the null-terminated byte string to be interpreted<br />
str_end &#8211; pointer to a pointer to character.<br />
base &#8211; base of the interpreted integer value</p>
<h2>Return value</h2>
<p>* If successful, an integer value corresponding to the contents of str is returned.<br />
* If the converted value falls out of range of corresponding return type, a range error occurs (setting errno to ERANGE) and LONG_MAX, LONG_MIN, LLONG_MAX or LLONG_MIN is returned.<br />
* If no conversion can be performed, 0 is returned. </p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;iostream&gt;

#include &lt;string&gt;

#include &lt;cerrno&gt;

#include &lt;cstdlib&gt;
int main()

{
    const char *p = &quot;10 200000000000000000000000000000 30 -40&quot;;
    char *end;
    std::cout &lt;&lt; &quot;Parsing '&quot; &lt;&lt; p &lt;&lt; &quot;':
&quot;;
    for (long i = std::strtol(p, &amp;end, 10);
         p != end;
         i = std::strtol(p, &amp;end, 10)) {
        std::cout &lt;&lt; &quot;'&quot; &lt;&lt; std::string(p, end - p) &lt;&lt; &quot;' -&gt; &quot;;
        p = end;
        if (errno == ERANGE) {
            std::cout &lt;&lt; &quot;range error, got &quot;;
            errno = 0;
        }
        std::cout &lt;&lt; i &lt;&lt; '
';
    }
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;Parsing &#8217;10 200000000000000000000000000000 30 -40&#8242;:<br />
&nbsp;<wbr>&nbsp;&#8217;10&#8217; -&gt; 10<br />
&nbsp;<wbr>&nbsp;&#8216; 200000000000000000000000000000&#8217; -&gt; range error, got 9223372036854775807<br />
&nbsp;<wbr>&nbsp;&#8216; 30&#8217; -&gt; 30<br />
&nbsp;<wbr>&nbsp;&#8216; -40&#8217; -&gt; -40</p>
<h2>See also</h2>
<p>atoi converts a byte string to an integer value<br />
atol <i>(function)</i><br />
atoll<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;converts a byte string to an unsigned integer value<br />
strtoul <i>(function)</i><br />
strtoull<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;converts a wide string to an integer value<br />
wcstol <i>(function)</i><br />
wcstoll<br />
strtof converts a byte string to a floating point value<br />
strtod <i>(function)</i><br />
strtold<br />
from_chars converts a character sequence to an integer or floating-point value<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++17)</i> </p>
