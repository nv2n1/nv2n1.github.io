---
title: "stdbit_cast(3)"
name: "stdbit_cast"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdbit_cast/"
---

std::bit_cast - std::bit_cast

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;bit&gt;

    template &lt;class To, class From&gt;
    (since C++ 20)

        constexpr To bit_cast(const From &amp;from) noexcept;</code></pre> 
Obtain a value of type To by reinterpreting the object representation of from. Every bit in the value representation of the returned To object is equal to the corresponding bit in the object representation of from. The values of padding bits in the returned To object are unspecified. 
If there is no value of type To corresponding to the value representation produced, the behavior is undefined. If there are multiple such values, which value is produced is unspecified. 
This overload only participates in overload resolution if sizeof(To) == sizeof(From) and both To and From are TriviallyCopyable types. 
This function template is constexpr if and only if each of To, From and the types of all subobjects of To and From: 
* is not a union type; 
* is not a pointer type; 
* is not a pointer to member type; 
* is not a volatile-qualified type; and 
* has no non-static data member of reference type. 

<h2>Return value</h2>

An object of type To whose value representation is as described above. 

<h2>Notes</h2>

reinterpret_cast (or equivalent explicit_cast) between pointer or reference types shall not be used to reinterpret object representation in most cases because of the type_aliasing_rule. 
Before std::bit_cast, std::memcpy can be used when it is needed to interpret the object representation as one of another type: template &lt;class To, class From&gt;

typename std::enable_if&lt;
    (sizeof(To) == sizeof(From)) &amp;&amp;
        std::is_trivially_copyable&lt;From&gt;::value &amp;&amp;
        std::is_trivial&lt;To&gt;::value,
    // this implementation requires that To is trivially default constructible
    To&gt;::type

// constexpr support needs compiler magic

bit_cast(const From &amp;src) noexcept

{
    To dst;
    std::memcpy(&amp;dst, &amp;src, sizeof(To));
    return dst;
}


<h2>Example</h2>

// Run this code <pre><code>#include &lt;cstdint&gt;

#include &lt;bit&gt;

#include &lt;iostream&gt;
constexpr double f64v = 19880124.0;

constexpr auto u64v = std::bit_cast&lt;std::uint64_t&gt;(f64v);
constexpr std::uint64_t u64v2 = 0x3fe9000000000000ull;

constexpr auto f64v2 = std::bit_cast&lt;double&gt;(u64v2);
int main()

{
    std::cout
        &lt;&lt; std::fixed &lt;&lt; f64v &lt;&lt; &quot;f64.to_bits() == 0x&quot;
        &lt;&lt; std::hex &lt;&lt; u64v &lt;&lt; &quot;u64\n&quot;;
    std::cout
        &lt;&lt; &quot;f64::from_bits(0x&quot; &lt;&lt; std::hex &lt;&lt; u64v2 &lt;&lt; &quot;u64) == &quot;
        &lt;&lt; std::fixed &lt;&lt; f64v2 &lt;&lt; &quot;f64\n&quot;;
}
</code></pre>

<h2>Possible output:</h2>

&nbsp;<wbr>&nbsp;19880124.000000f64.to_bits() == 0x4172f58bc0000000u64 
&nbsp;<wbr>&nbsp;f64::from_bits(0x3fe9000000000000u64) == 0.781250f64
