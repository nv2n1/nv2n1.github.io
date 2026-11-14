---
title: "stdexperimentalfilesystempathparent_path(3)"
name: "stdexperimentalfilesystempathparent_path"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalfilesystempathparent_path/"
---

std::experimental::filesystem::path::parent_path - std::experimental::filesystem::path::parent_path

<h2>Synopsis</h2>

path parent_path() const; (filesystem TS) 
Returns the path to the parent directory. Returns empty path if empty() or there's only a single element in the path (begin() == --end(). 
The resulting path is constructed by appending all elements in a range [begin(), --end()) to an empty path. 

<h2>Parameters</h2>

<i>(none)</i>

<h2>Return value</h2>

The path to the parent directory. 

<h2>Exceptions</h2>

<i>(none)</i>

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;experimental/filesystem&gt;

namespace fs = std::experimental::filesystem;

int main()

{
    for (fs::path p : {&quot;/var/tmp/example.txt&quot;, &quot;/&quot;, &quot;/var/tmp/.&quot;})
        std::cout &lt;&lt; &quot;The parent path of &quot; &lt;&lt; p
                  &lt;&lt; &quot; is &quot; &lt;&lt; p.parent_path() &lt;&lt; '\n';
}
</code></pre>

<h2>Possible output:</h2>

&nbsp;<wbr>&nbsp;The parent path of &quot;/var/tmp/example.txt&quot; is &quot;/var/tmp&quot; 
&nbsp;<wbr>&nbsp;The parent path of &quot;/&quot; is &quot;&quot; 
&nbsp;<wbr>&nbsp;The parent path of &quot;/var/tmp/.&quot; is &quot;/var/tmp&quot;

<h2>See also</h2>

&nbsp;This section is incomplete 
