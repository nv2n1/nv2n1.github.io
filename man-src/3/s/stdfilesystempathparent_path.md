---
title: "stdfilesystempathparent_path(3)"
name: "stdfilesystempathparent_path"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdfilesystempathparent_path/"
---

std::filesystem::path::parent_path - std::filesystem::path::parent_path

<h2>Synopsis</h2>

path parent_path() const; <i>(since C++17)</i> 
Returns the path to the parent directory. 
If has_relative_path() returns false, the result is a copy of *this Otherwise, the result is a path whose generic format pathname is the longest prefix of the generic format pathname of *this that produces one fewer element in its iteration. 

<h2>Parameters</h2>

<i>(none)</i>

<h2>Return value</h2>

The path to the parent directory. 

<h2>Exceptions</h2>

<i>(none)</i>

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;filesystem&gt;

namespace fs = std::filesystem;

int main()

{
    for (fs::path p : {&quot;/var/tmp/example.txt&quot;, &quot;/&quot;, &quot;/var/tmp/.&quot;})
        std::cout &lt;&lt; &quot;The parent path of &quot; &lt;&lt; p
                  &lt;&lt; &quot; is &quot; &lt;&lt; p.parent_path() &lt;&lt; '\n';
}
</code></pre>

<h2>Possible output:</h2>

&nbsp;<wbr>&nbsp;The parent path of &quot;/var/tmp/example.txt&quot; is &quot;/var/tmp&quot; 
&nbsp;<wbr>&nbsp;The parent path of &quot;/&quot; is &quot;/&quot; 
&nbsp;<wbr>&nbsp;The parent path of &quot;/var/tmp/.&quot; is &quot;/var/tmp&quot;
