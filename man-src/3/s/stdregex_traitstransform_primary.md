---
title: "stdregex_traitstransform_primary(3)"
name: "stdregex_traitstransform_primary"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdregex_traitstransform_primary/"
---

std::regex_traits&lt;CharT&gt;::transform_primary - std::regex_traits&lt;CharT&gt;::transform_primary

<h2>Synopsis</h2>

<pre><code>template &lt;class ForwardIt&gt;

string_type transform_primary(ForwardIt first, ForwardIt last) const;</code></pre> 
For the character sequence [first, last), obtains the primary sort key in the imbued locale's collating order, that is, the sort key that is based on the positions of the letters and collation units in the national alphabet, ignoring case, diacritics, variants, etc. If a primary sort key compares less than another primary sort key with operator&lt;, then the character sequence that produced the first sort key comes before the character sequence that produced the second sort key, in the currently imbued locale's primary collation order. 
The regex library uses this trait to match characters against equivalence classes. For example, the regex [[=a=]] is equivalent to the character c1 if traits.transform_primary(c1) is equivalent to traits.transform_primary(&quot;a&quot;) (which is true for any c1 from &quot;AÀÁÂÃÄÅaàáâãäå&quot; in the U.S. English locale). Note that transform_primary() takes a character sequence argument because equivalence classes may be multicharacter, such as [[=ch=]] in Czech or [[=dzs=]] in Hungarian. 
There is no portable way to define primary sort key in terms of std::locale since the conversion from the collation key returned by std::collate::transform() to the primary equivalence key is locale-specific, and if the user replaces the std::collate facet, that conversion is no longer known to the standard library's std::regex_traits. Standard library specializations of std::regex_traits return an empty string unless the std::collate facet of the currently-imbued locale was not replaced by the user, and still matches the system-supplied std::collate facet), in which case std::collate_byname&lt;charT&gt;::transform(first, last) is executed and the sort key it produces is converted to the expected primary sort key using a locale-specific conversion. 

<h2>Parameters</h2>

first, last - a pair of iterators which determines the sequence of characters to compare

<h2>Type requirements</h2>

- 
ForwardIt must meet the requirements of LegacyForwardIterator.

<h2>Return value</h2>

The primary sort key for the character sequence [first, last) in the currently imbued locale, ignoring case, variant, diacritics, etc. 

<h2>Example</h2>

Demonstrates the regex feature that works through transform_primary() 
 // Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;regex&gt;
int main()

{
    std::locale::global(std::locale(&quot;en_US.UTF-8&quot;));
    std::wstring str = L&quot;AÀÁÂÃÄÅaàáâãäå&quot;;
    std::wregex re(L&quot;[[=a=]]*&quot;, std::regex::basic);
    std::cout &lt;&lt; std::boolalpha &lt;&lt; std::regex_match(str, re) &lt;&lt; '\n';
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;true 

 

 
&nbsp;This section is incomplete 
&nbsp;Reason: could use an example with user-defined regex_traits supplying user-defined transform_primary
