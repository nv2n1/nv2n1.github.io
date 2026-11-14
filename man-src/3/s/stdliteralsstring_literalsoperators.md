---
title: "stdliteralsstring_literalsoperators(3)"
name: "stdliteralsstring_literalsoperators"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdliteralsstring_literalsoperators/"
description: "std::literals::string_literals::operator\"\"s – std::literals::string_literals::operator\"\"s"
---

<p>std::literals::string_literals::operator&quot;&quot;s &#8211; std::literals::string_literals::operator&quot;&quot;s</p>
<h2>Synopsis</h2>
<p>Defined in header &lt;string&gt;<br />
string operator &quot;&quot; s(const char *str, std::size_t len); <code>(1)</code> <i>(since C++14)</i><br />
u8string operator &quot;&quot; s(const char8_t *str, std::size_t len); <code>(2)</code> <i>(since C++20)</i><br />
u16string operator &quot;&quot; s(const char16_t *str, std::size_t len); <code>(3)</code> <i>(since C++14)</i><br />
u32string operator &quot;&quot; s(const char32_t *str, std::size_t len); <code>(4)</code> <i>(since C++14)</i><br />
wstring operator &quot;&quot; s(const wchar_t *str, std::size_t len); <code>(5)</code> <i>(since C++14)</i> </p>
<pre><code>Forms a string literal of the desired type.

1) returns std::string{str, len}

2) returns std::u8string{str, len}

3) returns std::u16string{str, len}

4) returns std::u32string{str, len}

5) returns std::wstring{str, len}
</code></pre>
<h2>Parameters</h2>
<p>str &#8211; pointer to the beginning of the raw character array literal<br />
len &#8211; length of the raw character array literal</p>
<h2>Return value</h2>
<p>The string literal. </p>
<h2>Notes</h2>
<p>These operators are declared in the namespace std::literals::string_literals, where both literals and string_literals are inline namespaces. Access to these operators can be gained with using namespace std::literals, using namespace std::string_literals, and using namespace std::literals::string_literals.<br />
std::chrono::duration also defines operator&quot;&quot;s, to represent literal seconds, but it is an arithmetic literal: 10.0s and 10s are ten seconds, but &quot;10&quot;s is a string. </p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;string&gt;

#include &lt;iostream&gt;
int main()

{
    using namespace std::string_literals;
    std::string s1 = &quot;abc
