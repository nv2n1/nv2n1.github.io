---
title: "stdregex_traitslookup_collatename(3)"
name: "stdregex_traitslookup_collatename"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdregex_traitslookup_collatename/"
---

std::regex_traits&lt;CharT&gt;::lookup_collatename - std::regex_traits&lt;CharT&gt;::lookup_collatename

<h2>Synopsis</h2>

<pre><code>template &lt;class ForwardIt&gt;

string_type lookup_collatename(ForwardIt first, ForwardIt last) const;</code></pre> 
If the character sequence [first, last) represents the name of a valid collating element in the currently imbued locale, returns the name of that collating element. Otherwise, returns an empty string. 
Collating elements are the symbols found in POSIX regular expressions between [. and .]. For example, [.a.] matches the character a in the C locale. [.tilde.] matches the character ~ in the C locale as well. [.ch.] matches the digraph ch in Czech locale, but generates std::regex_error with error code std::regex_constants::error_collate in most other locales. 

<h2>Parameters</h2>

first, last - a pair of iterators which determines the sequence of characters that represents a collating element name

<h2>Type requirements</h2>

- 
ForwardIt must meet the requirements of LegacyForwardIterator.

<h2>Return value</h2>

The representation of the named collating element as a character string. 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;string&gt;

#include &lt;regex&gt;
struct noisy_traits : std::regex_traits&lt;char&gt; {
    template &lt;class Iter&gt;
    string_type lookup_collatename(Iter first, Iter last) const
    {
        string_type result = regex_traits::lookup_collatename(first, last);
        std::cout &lt;&lt; &quot;regex_traits&lt;&gt;::lookup_collatename(\&quot;&quot;
                  &lt;&lt; string_type(first, last)
                  &lt;&lt; &quot;\&quot;) returns \&quot;&quot; &lt;&lt; result &lt;&lt; &quot;\&quot;\n&quot;;
        return result;
    }
};
int main()

{
    std::string str = &quot;z|}a&quot;; // C locale collation order: x,y,z,{,|,},~
    std::basic_regex&lt;char, noisy_traits&gt; re(&quot;[x-[.tilde.]]*a&quot;, std::regex::basic);
    std::cout &lt;&lt; std::boolalpha &lt;&lt; std::regex_match(str, re) &lt;&lt; '\n';
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;regex_traits&lt;&gt;::lookup_collatename(&quot;tilde&quot;) returns &quot;~&quot; 
&nbsp;<wbr>&nbsp;true
