---
title: "stdfilesystembeginrecursive_directory_iterator(3)"
name: "stdfilesystembeginrecursive_directory_iterator"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdfilesystembeginrecursive_directory_iterator/"
description: "std::filesystem::begin(recursive_directory_iterator),std::filesystem::end(recursive_directory_iterator) – std::filesystem::begin(recursive_directory_iterator),std::filesystem::end(recursive_directo..."
---

<p>std::filesystem::begin(recursive_directory_iterator),std::filesystem::end(recursive_directory_iterator) &#8211; std::filesystem::begin(recursive_directory_iterator),std::filesystem::end(recursive_directory_iterator)</p>
<h2>Synopsis</h2>
<p>recursive_directory_iterator begin( recursive_directory_iterator iter ) noexcept; <code>(1)</code> <i>(since C++17)</i><br />
recursive_directory_iterator end( const recursive_directory_iterator&amp; ) noexcept; <code>(2)</code> <i>(since C++17)</i><br />
1) Returns iter unchanged<br />
2) Returns a default-constructed recursive_directory_iterator, which serves as the end iterator. The argument is ignored.<br />
These non-member functions enable the use of recursive_directory_iterators with range-based for loops. </p>
<h2>Parameters</h2>
<p>iter &#8211; a recursive_directory_iterator</p>
<h2>Return value</h2>
<p>1) iter unchanged<br />
2) End iterator (default-constructed recursive_directory_iterator) </p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;fstream&gt;

#include &lt;iostream&gt;

#include &lt;filesystem&gt;

namespace fs = std::filesystem;
int main()

{
    fs::create_directories(&quot;sandbox/a/b&quot;);
    std::ofstream(&quot;sandbox/file1.txt&quot;);
    fs::create_symlink(&quot;a&quot;, &quot;sandbox/syma&quot;);
    for (auto &amp;p : fs::recursive_directory_iterator(&quot;sandbox&quot;))
        std::cout &lt;&lt; p &lt;&lt; '
';
    fs::remove_all(&quot;sandbox&quot;);
}
</code></pre>
<h2>Possible output:</h2>
<p>&nbsp;<wbr>&nbsp;&quot;sandbox/a&quot;<br />
&nbsp;<wbr>&nbsp;&quot;sandbox/a/b&quot;<br />
&nbsp;<wbr>&nbsp;&quot;sandbox/file1.txt&quot;<br />
&nbsp;<wbr>&nbsp;&quot;sandbox/syma&quot;</p>
<h2>See also</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;range-based for loop support<br />
begin(std::filesystem::directory_iterator) <i>(function)</i><br />
end(std::filesystem::directory_iterator) </p>
