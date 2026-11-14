---
title: "stdexperimentalfilesystempathcompare(3)"
name: "stdexperimentalfilesystempathcompare"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalfilesystempathcompare/"
---

std::experimental::filesystem::path::compare - std::experimental::filesystem::path::compare

<h2>Synopsis</h2>

<pre><code>int compare(const path &amp;p) const;
(1)(filesystem TS)

    int compare(const string_type &amp;str) const;
(2)(filesystem TS)

    int compare(const value_type *s) const;
(3)(filesystem TS)</code></pre> 
Compares the lexical representations of the path and another path. 
1) Returns a value less than, equal to or greater than 0 if the native representation of the path (native()) is respectively lexicographically less than, equal to or greater than the native representation of p (p.native()). Comparison is performed element-wise, as if by iterating both paths from begin() to end(). 
2) Equivalent to compare(path(str)). 
3) Equivalent to compare(path(s)). 

<h2>Parameters</h2>

p - a path to compare to 
str - a string representing path to compare to 
s - a null-terminated string representing path to compare to

<h2>Return value</h2>

A value less than 0 if the path is lexicographically less than the given path. 
A value equal to 0 if the path is lexicographically equal to the given path. 
A value greater than 0 if the path is lexicographically greater than the given path. 

<h2>Exceptions</h2>

1) 
noexcept specification: 
noexcept 
2-3) <i>(none)</i>

<h2>Notes</h2>

For two-way comparisons, binary_operators may be more suitable. 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;experimental/filesystem&gt;

namespace fs = std::experimental::filesystem;

void demo(int rc, fs::path p1, fs::path p2)
{
    if (rc &lt; 0)
        std::cout &lt;&lt; p1 &lt;&lt; &quot; &lt; &quot; &lt;&lt; p2 &lt;&lt; '\n';
    else if (rc &gt; 0)
        std::cout &lt;&lt; p1 &lt;&lt; &quot; &gt; &quot; &lt;&lt; p2 &lt;&lt; '\n';
    else if (rc == 0)
        std::cout &lt;&lt; p1 &lt;&lt; &quot;==&quot; &lt;&lt; p2 &lt;&lt; '\n';
}

int main()
{
    fs::path p1 = &quot;/a/b/&quot;; // as if &quot;a/b/.&quot; for lexicographical iteration
    fs::path p2 = &quot;/a/b/#&quot;;
    demo(p1.compare(p2), p1, p2);
    demo(p1.compare(&quot;a/b/_&quot;), p1, &quot;a/b/_&quot;);
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;&quot;/a/b/&quot; &gt; &quot;/a/b/#&quot; 
&nbsp;<wbr>&nbsp;&quot;/a/b/&quot; &lt; &quot;a/b/_&quot;

<h2>See also</h2>

operator== 
operator!= lexicographically compares two paths 
operator&lt; <i>(function)</i> 
operator&lt;= 
operator&gt; 
operator&gt;= 
