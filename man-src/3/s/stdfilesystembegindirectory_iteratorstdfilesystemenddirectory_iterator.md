---
title: "stdfilesystembegindirectory_iteratorstdfilesystemenddirectory_iterator(3)"
name: "stdfilesystembegindirectory_iteratorstdfilesystemenddirectory_iterator"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdfilesystembegindirectory_iteratorstdfilesystemenddirectory_iterator/"
description: "std::filesystem::begin(directory_iterator),std::filesystem::end(directory_iterator) – std::filesystem::begin(directory_iterator),std::filesystem::end(directory_iterator)"
---

<p>std::filesystem::begin(directory_iterator),std::filesystem::end(directory_iterator) &#8211; std::filesystem::begin(directory_iterator),std::filesystem::end(directory_iterator)</p>
<h2>Synopsis</h2>
<p>directory_iterator begin( directory_iterator iter ) noexcept; <code>(1)</code> <i>(since C++17)</i><br />
directory_iterator end( const directory_iterator&amp; ) noexcept; <code>(2)</code> <i>(since C++17)</i><br />
1) Returns iter unchanged<br />
2) Returns a default-constructed directory_iterator, which serves as the end iterator. The argument is ignored.<br />
These non-member functions enable the use of directory_iterators with range-based for loops. </p>
<h2>Parameters</h2>
<p>iter &#8211; a directory_iterator</p>
<h2>Return value</h2>
<p>1) iter unchanged<br />
2) End iterator (default-constructed directory_iterator) </p>
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
    std::ofstream(&quot;sandbox/file2.txt&quot;);
    for (auto &amp;p : fs::directory_iterator(&quot;sandbox&quot;))
        std::cout &lt;&lt; p &lt;&lt; '
';
    fs::remove_all(&quot;sandbox&quot;);
}
</code></pre>
<h2>Possible output:</h2>
<p>&nbsp;<wbr>&nbsp;&quot;sandbox/a&quot;<br />
&nbsp;<wbr>&nbsp;&quot;sandbox/file1.txt&quot;<br />
&nbsp;<wbr>&nbsp;&quot;sandbox/file2.txt&quot;</p>
<h2>See also</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;range-based for loop support<br />
begin(std::filesystem::recursive_directory_iterator) <i>(function)</i><br />
end(std::filesystem::recursive_directory_iterator) </p>
