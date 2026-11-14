---
title: "stdexperimentalfilesystemrecursive_directory_iteratordepth(3)"
name: "stdexperimentalfilesystemrecursive_directory_iteratordepth"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalfilesystemrecursive_directory_iteratordepth/"
---

std::experimental::filesystem::recursive_directory_iterator::depth - std::experimental::filesystem::recursive_directory_iterator::depth

<h2>Synopsis</h2>

<pre><code>int depth() const;
(filesystem TS)</code></pre> 
Returns the number of directories from the starting directory to the currently iterated directory, i.e. the current depth of the directory hierarchy. 
The starting directory has depth of 0, its subdirectories have depth 1, etc. 
The behavior is undefined if *this is the end iterator. 

<h2>Parameters</h2>

<i>(none)</i>

<h2>Return value</h2>

Current depth of the directory hierarchy. 

<h2>Exceptions</h2>

<i>(none)</i>

<h2>Example</h2>

this example uses iteration depth to calculate the indentation of a directory tree printout 
 // Run this code <pre><code>#include &lt;fstream&gt;

#include &lt;iostream&gt;

#include &lt;string&gt;

#include &lt;experimental/filesystem&gt;

namespace fs = std::experimental::filesystem;
int main()

{
    fs::create_directories(&quot;sandbox/a/b/c&quot;);
    fs::create_directories(&quot;sandbox/a/b/d/e&quot;);
    std::ofstream(&quot;sandbox/a/b/file1.txt&quot;);
    fs::create_symlink(&quot;a&quot;, &quot;sandbox/syma&quot;);
    for (auto i = fs::recursive_directory_iterator(&quot;sandbox&quot;);
         i != fs::recursive_directory_iterator();
         ++i) {
        std::cout &lt;&lt; std::string(i.depth(), ' ') &lt;&lt; *i;
        if (fs::is_symlink(i-&gt;symlink_status()))
            std::cout &lt;&lt; &quot; -&gt; &quot; &lt;&lt; fs::read_symlink(*i);
        std::cout &lt;&lt; '\n';
    }
    fs::remove_all(&quot;sandbox&quot;);
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;&quot;sandbox/a&quot; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;&quot;sandbox/a/b&quot; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&quot;sandbox/a/b/c&quot; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&quot;sandbox/a/b/d&quot; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&quot;sandbox/a/b/d/e&quot; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&quot;sandbox/a/b/file1.txt&quot; 
&nbsp;<wbr>&nbsp;&quot;sandbox/syma&quot; -&gt; &quot;a&quot;
