---
title: "stdwcstolstdwcstoll(3)"
name: "stdwcstolstdwcstoll"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdwcstolstdwcstoll/"
description: "std::wcstol,std::wcstoll – std::wcstol,std::wcstoll"
---

<p>std::wcstol,std::wcstoll &#8211; std::wcstol,std::wcstoll</p>
<h2>Synopsis</h2>
<p>Defined in header &lt;cwchar&gt;<br />
long wcstol( const wchar_t* str, wchar_t** str_end, int base );<br />
long long wcstoll( const wchar_t* str, wchar_t** str_end, int base ); <i>(since C++11)</i> </p>
<pre><code>Interprets an integer value in a wide string pointed to by str.

Discards any whitespace characters (as identified by calling isspace()) until the first non-whitespace character is found, then takes as many characters as possible to form a valid base-n (where n=base) integer number representation and converts them to an integer value. The valid integer value consists of the following parts:</code></pre>
<p>* (optional) plus or minus sign<br />
* (optional) prefix <code>(0)</code> indicating octal base (applies only when the base is 8 or 0)<br />
* (optional) prefix (0x or 0X) indicating hexadecimal base (applies only when the base is 16 or 0)<br />
* a sequence of digits<br />
The set of valid values for base is {0,2,3,&#8230;,36}. The set of valid digits for base-2 integers is {0,1}, for base-3 integers is {0,1,2}, and so on. For bases larger than 10, valid digits include alphabetic characters, starting from Aa for base-11 integer, to Zz for base-36 integer. The case of the characters is ignored.<br />
Additional numeric formats may be accepted by the currently installed C locale.<br />
If the value of base is 0, the numeric base is auto-detected: if the prefix is 0, the base is octal, if the prefix is 0x or 0X, the base is hexadecimal, otherwise the base is decimal.<br />
If the minus sign was part of the input sequence, the numeric value calculated from the sequence of digits is negated as if by unary_minus in the result type.<br />
The functions sets the pointer pointed to by str_end to point to the wide character past the last character interpreted. If str_end is NULL, it is ignored. </p>
<h2>Parameters</h2>
<p>str &#8211; pointer to the null-terminated wide string to be interpreted<br />
str_end &#8211; pointer to a pointer to wide character<br />
base &#8211; base of the interpreted integer value</p>
<h2>Return value</h2>
<p>Integer value corresponding to the contents of str on success. If the converted value falls out of range of corresponding return type, range error occurs and LONG_MAX, LONG_MIN, LLONG_MAX or LLONG_MIN is returned. If no conversion can be performed, 0 is returned. </p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;iostream&gt;

#include &lt;string&gt;

#include &lt;errno.h&gt;

#include &lt;cwchar&gt;
int main()

{
    const wchar_t *p = L&quot;10 200000000000000000000000000000 30 -40&quot;;
    wchar_t *end;
    std::wcout &lt;&lt; &quot;Parsing L'&quot; &lt;&lt; p &lt;&lt; &quot;':
&quot;;
    for (long i = std::wcstol(p, &amp;end, 10);
         p != end;
         i = std::wcstol(p, &amp;end, 10)) {
        std::wcout &lt;&lt; &quot;'&quot; &lt;&lt; std::wstring(p, end - p) &lt;&lt; &quot;' -&gt; &quot;;
        p = end;
        if (errno == ERANGE) {
            std::wcout &lt;&lt; &quot;range error, got &quot;;
            errno = 0;
        }
        std::wcout &lt;&lt; i &lt;&lt; '
';
    }
}
</code></pre>
<h2>Possible output:</h2>
<p>&nbsp;<wbr>&nbsp;Parsing L&#8217;10 200000000000000000000000000000 30 -40&#8242;:<br />
&nbsp;<wbr>&nbsp;&#8217;10&#8217; -&gt; 10<br />
&nbsp;<wbr>&nbsp;&#8216; 200000000000000000000000000000&#8217; -&gt; range error, got 9223372036854775807<br />
&nbsp;<wbr>&nbsp;&#8216; 30&#8217; -&gt; 30<br />
&nbsp;<wbr>&nbsp;&#8216; -40&#8217; -&gt; -40</p>
<h2>See also</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;converts a byte string to an integer value<br />
strtol <i>(function)</i><br />
strtoll<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;converts a wide string to an unsigned integer value<br />
wcstoul <i>(function)</i><br />
wcstoull </p>
