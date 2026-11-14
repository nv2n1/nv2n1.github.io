---
title: "stdliteralsstring_view_literalsoperatorsv(3)"
name: "stdliteralsstring_view_literalsoperatorsv"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdliteralsstring_view_literalsoperatorsv/"
description: "std::literals::string_view_literals::operator\"\"sv – std::literals::string_view_literals::operator\"\"sv"
---

<p>std::literals::string_view_literals::operator&quot;&quot;sv &#8211; std::literals::string_view_literals::operator&quot;&quot;sv</p>
<h2>Synopsis</h2>
<p>Defined in header &lt;string_view&gt;<br />
constexpr string_view operator &quot;&quot; sv(const char* str, size_t len) noexcept; <code>(1)</code> <i>(since C++17)</i><br />
constexpr u8string_view operator &quot;&quot; sv(const char8_t* str, size_t len) noexcept; <code>(2)</code> <i>(since C++20)</i><br />
constexpr u16string_view operator &quot;&quot; sv(const char16_t* str, size_t len) noexcept; <code>(3)</code> <i>(since C++17)</i><br />
constexpr u32string_view operator &quot;&quot; sv(const char32_t* str, size_t len) noexcept; <code>(4)</code> <i>(since C++17)</i><br />
constexpr wstring_view operator &quot;&quot; sv(const wchar_t* str, size_t len) noexcept; <code>(5)</code> <i>(since C++17)</i> </p>
<pre><code>Forms a string view of a character literal.

1) returns std::string_view{str, len}

2) returns std::u8string_view{str, len}

3) returns std::u16string_view{str, len}

4) returns std::u32string_view{str, len}

5) returns std::wstring_view{str, len}
</code></pre>
<h2>Parameters</h2>
<p>str &#8211; pointer to the beginning of the raw character array literal<br />
len &#8211; length of the raw character array literal</p>
<h2>Return value</h2>
<p>The string_view literal. </p>
<h2>Notes</h2>
<p>These operators are declared in the namespace std::literals::string_view_literals, where both literals and string_view_literals are inline namespaces. Access to these operators can be gained with using namespace std::literals, using namespace std::string_view_literals, and using namespace std::literals::string_view_literals. </p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;string_view&gt;

#include &lt;iostream&gt;
int main()

{
    using namespace std::literals;
    std::string_view s1 = &quot;abc
