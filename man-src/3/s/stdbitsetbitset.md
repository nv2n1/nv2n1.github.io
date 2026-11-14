---
title: "stdbitsetbitset(3)"
name: "stdbitsetbitset"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdbitsetbitset/"
description: "std::bitset<N>::bitset – std::bitset<N>::bitset"
---

<p>std::bitset&lt;N&gt;::bitset &#8211; std::bitset&lt;N&gt;::bitset</p>
<h2>Synopsis</h2>
<pre><code>bitset();
(until C++ 11)

    constexpr bitset() noexcept;
(since C++ 11)

    bitset(unsigned long val);
(until C++ 11)

    constexpr bitset(unsigned long long val) noexcept;
(since C++ 11)

    template &lt;class CharT, class Traits, class Alloc&gt;

    explicit bitset(const std::basic_string&lt;CharT, Traits, Alloc&gt; &amp;str,

                    typename std::basic_string&lt;CharT, Traits, Alloc&gt;::size_type(until C++ 11)

                        pos = 0,

                    typename std::basic_string&lt;CharT, Traits, Alloc&gt;::size_type

                        n = std::basic_string&lt;CharT, Traits, Alloc&gt;::npos);

template &lt;class CharT, class Traits, class Alloc&gt;

explicit bitset(const std::basic_string&lt;CharT, Traits, Alloc&gt; &amp;str, (1)

                                                                        typename std::basic_string&lt;CharT, Traits, Alloc&gt;::size_type(2)

                                                                            pos = 0,
                (3)(since C++ 11)

                    typename std::basic_string&lt;CharT, Traits, Alloc&gt;::size_type

                        n = std::basic_string&lt;CharT, Traits, Alloc&gt;::npos,

                CharT zero = CharT('0'),

                CharT one = CharT('1'));

template &lt;class CharT&gt;

explicit bitset(const CharT *str,

                typename std::basic_string&lt;CharT&gt;::size_type(4)(since C++ 11)

                    n = std::basic_string&lt;CharT&gt;::npos,

                CharT zero = CharT('0'),

                CharT one = CharT('1'));</code></pre>
<p>Constructs a new bitset from one of several optional data sources:<br />
1) Default constructor. Constructs a bitset with all bits set to zero.<br />
2) Constructs a bitset, initializing the first (rightmost, least significant) M bit positions to the corresponding bit values of val, where M is the smaller of the number of bits in an unsigned long long and the number of bits N in the bitset being constructed. If M is less than N (the bitset is longer than<br />
32<br />
<i>(until C++11)</i><br />
64<br />
<i>(since C++11)</i> bits, for typical implementations of unsigned<br />
long<br />
<i>(since C++11)</i>long), the remaining bit positions are initialized to zeroes.<br />
3) Constructs a bitset using the characters in the std::basic_string str. An optional starting position pos and length n can be provided, as well as characters denoting alternate values for set (one) and unset (zero) bits. Traits::eq() is used to compare the character values.<br />
The effective length of the initializing string is min(n, str.size() &#8211; pos).<br />
If pos &gt; str.size(), this constructor throws std::out_of_range. If any characters examined in str are not zero or one, it throws std::invalid_argument.<br />
4) Similar to <code>(3)</code>, but uses a CharT* instead of a std::basic_string. Equivalent to bitset(n == basic_string&lt;CharT&gt;::npos ? basic_string&lt;CharT&gt;(str) : basic_string&lt;CharT&gt;(str, n), 0, n, zero, one) </p>
<h2>Parameters</h2>
<p>val &#8211; number used to initialize the bitset<br />
str &#8211; string used to initialize the bitset<br />
pos &#8211; a starting offset into str<br />
n &#8211; number of characters to use from str<br />
one &#8211; alternate character for set bits in str<br />
zero &#8211; alternate character for unset bits in str</p>
<h2>Exceptions</h2>
<p>3) std::out_of_range if pos &gt; str.size(), std::invalid_argument if any character is not one or zero<br />
4) std::invalid_argument if any character is not one or zero</p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;bitset&gt;

#include &lt;string&gt;

#include &lt;iostream&gt;

#include &lt;climits&gt;
int main()

{
    // empty constructor
    std::bitset&lt;8&gt; b1;              // [0,0,0,0,0,0,0,0]
                                    // unsigned long long constructor
    std::bitset&lt;8&gt; b2(42);          // [0,0,1,0,1,0,1,0]
    std::bitset&lt;70&gt; bl(ULLONG_MAX); // [0,0,0,0,0,0,1,1,1,...,1,1,1] in C++11
    std::bitset&lt;8&gt; bs(0xfff0);      // [1,1,1,1,0,0,0,0]
                                    // string constructor
    std::string bit_string = &quot;110010&quot;;
    std::bitset&lt;8&gt; b3(bit_string);       // [0,0,1,1,0,0,1,0]
    std::bitset&lt;8&gt; b4(bit_string, 2);    // [0,0,0,0,0,0,1,0]
    std::bitset&lt;8&gt; b5(bit_string, 2, 3); // [0,0,0,0,0,0,0,1]
                                         // string constructor using custom zero/one digits
    std::string alpha_bit_string = &quot;aBaaBBaB&quot;;
    std::bitset&lt;8&gt; b6(alpha_bit_string, 0, alpha_bit_string.size(),
                      'a', 'B');                // [0,1,0,0,1,1,0,1]
                                                // char* constructor using custom digits
    std::bitset&lt;8&gt; b7(&quot;XXXXYYYY&quot;, 8, 'X', 'Y'); // [0,0,0,0,1,1,1,1]
    std::cout &lt;&lt; b1 &lt;&lt; '
'
              &lt;&lt; b2 &lt;&lt; '
'
              &lt;&lt; bl &lt;&lt; '
'
              &lt;&lt; bs &lt;&lt; '
'
              &lt;&lt; b3 &lt;&lt; '
'
              &lt;&lt; b4 &lt;&lt; '
'
              &lt;&lt; b5 &lt;&lt; '
'
              &lt;&lt; b6 &lt;&lt; '
'
              &lt;&lt; b7 &lt;&lt; '
';
}
</code></pre>
<h2>Possible output:</h2>
<p>&nbsp;<wbr>&nbsp;00000000<br />
&nbsp;<wbr>&nbsp;00101010<br />
&nbsp;<wbr>&nbsp;0000001111111111111111111111111111111111111111111111111111111111111111<br />
&nbsp;<wbr>&nbsp;11110000<br />
&nbsp;<wbr>&nbsp;00110010<br />
&nbsp;<wbr>&nbsp;00000010<br />
&nbsp;<wbr>&nbsp;00000001<br />
&nbsp;<wbr>&nbsp;01001101<br />
&nbsp;<wbr>&nbsp;00001111</p>
<h2>See also</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;sets bits to true or given value<br />
set <i>(public member function)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;sets bits to false<br />
reset <i>(public member function)</i> </p>
