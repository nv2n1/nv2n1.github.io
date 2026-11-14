---
title: "stdexperimentalfilesystembeginrecursive_directory_iterator(3)"
name: "stdexperimentalfilesystembeginrecursive_directory_iterator"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalfilesystembeginrecursive_directory_iterator/"
description: "std::experimental::filesystem::begin(recursive_directory_iterator),std::experimental::filesystem::end(recursive_directory_iterator) – std::experimental::filesystem::begin(recursive_directory_iterat..."
---

<p>std::experimental::filesystem::begin(recursive_directory_iterator),std::experimental::filesystem::end(recursive_directory_iterator) &#8211; std::experimental::filesystem::begin(recursive_directory_iterator),std::experimental::filesystem::end(recursive_directory_iterator)</p>
<h2>Synopsis</h2>
<p>recursive_directory_iterator begin( recursive_directory_iterator iter ); <code>(1)</code> (filesystem TS)<br />
recursive_directory_iterator end( const recursive_directory_iterator&amp; ); <code>(2)</code> (filesystem TS)<br />
1) Returns iter unchanged<br />
2) Returns a default-constructed recursive_directory_iterator, which serves as the end iterator. The argument is ignored.<br />
These non-member functions enable the use of recursive_directory_iterators with range-based for loops. </p>
<h2>Parameters</h2>
<p>iter &#8211; a recursive_directory_iterator</p>
<h2>Return value</h2>
<p>1) iter unchanged<br />
2) End iterator (default-constructed recursive_directory_iterator) </p>
<h2>Exceptions</h2>
<p>noexcept specification:<br />
noexcept</p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;fstream&gt;

#include &lt;iostream&gt;

#include &lt;experimental/filesystem&gt;

namespace fs = std::experimental::filesystem;
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
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;range-based for loop support<br />
filesystem::begin(filesystem::directory_iterator) <i>(function)</i><br />
filesystem::end(filesystem::directory_iterator) </p>
