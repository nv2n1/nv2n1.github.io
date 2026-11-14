---
title: "stdcollatehashstdcollatedo_hash(3)"
name: "stdcollatehashstdcollatedo_hash"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdcollatehashstdcollatedo_hash/"
---

std::collate&lt;CharT&gt;::hash,std::collate&lt;CharT&gt;::do_hash - std::collate&lt;CharT&gt;::hash,std::collate&lt;CharT&gt;::do_hash

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;locale&gt;

    public : (1)

                 long hash(const CharT *beg, const CharT *end) const;

protected:
(2)

    virtual long do_hash(const CharT *beg, const CharT *end) const;</code></pre> 
1) Public member function, calls the protected virtual member function do_hash of the most derived class. 
2) Converts the character sequence [beg, end) to an integer value that is equal to the hash obtained for all strings that collate equivalent in this locale (compare() returns 0). For two strings that do not collate equivalent, the probability that their hashes are equal should be very small, approaching 1.0/std::numeric_limits&lt;unsigned long&gt;::max(). 

<h2>Parameters</h2>

beg - pointer to the first character in the sequence to hash 
end - one past the end pointer for the sequence to hash

<h2>Return value</h2>

The hash value that respects collation order 

<h2>Note</h2>

The system-supplied locales normally do not collate two strings as equivalent (compare() does not return 0) if basic_string::operator== returns false, but a user-installed std::collate facet may provide different collation rules, for example, it may treat strings as equivalent if they have the same Unicode normalized form.

<h2>Example</h2>

Demonstrates a locale-aware unordered container 
 // Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;string&gt;

#include &lt;locale&gt;

#include &lt;unordered_set&gt;
struct CollateHash {
    template &lt;typename CharT&gt;
    std::size_t operator()(const std::basic_string&lt;CharT&gt; &amp;s) const
    {
        return std::use_facet&lt;std::collate&lt;CharT&gt;&gt;(std::locale()).hash(&amp;s[0], &amp;s[0] + s.size());
    }
};

struct CollateEq {
    template &lt;typename CharT&gt;
    bool operator()(const std::basic_string&lt;CharT&gt; &amp;s1,
                    const std::basic_string&lt;CharT&gt; &amp;s2) const
    {
        return std::use_facet&lt;std::collate&lt;CharT&gt;&gt;(std::locale()).compare(&amp;s1[0], &amp;s1[0] + s1.size(), &amp;s2[0], &amp;s2[0] + s2.size()) == 0;
    }
};
int main()

{
    std::locale::global(std::locale(&quot;en_US.utf8&quot;));
    std::wcout.imbue(std::locale());
    std::unordered_set&lt;std::wstring, CollateHash, CollateEq&gt; s2 = {L&quot;Foo&quot;, L&quot;Bar&quot;};
    for (auto &amp;str : s2)
        std::wcout &lt;&lt; str &lt;&lt; ' ';
    std::cout &lt;&lt; '\n';
}
</code></pre>

<h2>Possible output:</h2>

&nbsp;<wbr>&nbsp;Bar Foo

<h2>See also</h2>

std::hash&lt;std::string&gt; 
std::hash&lt;std::u8string&gt; 
std::hash&lt;std::u16string&gt; 
std::hash&lt;std::u32string&gt; 
std::hash&lt;std::wstring&gt; 
std::hash&lt;std::pmr::string&gt; 
std::hash&lt;std::pmr::u8string&gt; 
std::hash&lt;std::pmr::u16string&gt; 
std::hash&lt;std::pmr::u32string&gt; 
std::hash&lt;std::pmr::wstring&gt; hash support for strings 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template specialization)</i> 
<i>(C++11)</i> 
(C++20) 
<i>(C++11)</i> 
<i>(C++11)</i> 
<i>(C++11)</i> 
(C++20) 
(C++20) 
(C++20) 
(C++20) 
(C++20) 
