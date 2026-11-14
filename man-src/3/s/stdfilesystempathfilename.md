---
title: "stdfilesystempathfilename(3)"
name: "stdfilesystempathfilename"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdfilesystempathfilename/"
---

std::filesystem::path::filename - std::filesystem::path::filename

<h2>Synopsis</h2>

path filename() const; <i>(since C++17)</i> 
Returns the generic-format filename component of the path. 
Equivalent to relative_path().empty() ? path() : *--end(). 

<h2>Parameters</h2>

<i>(none)</i>

<h2>Return value</h2>

The filename identified by the path. 

<h2>Exceptions</h2>

<i>(none)</i>

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;filesystem&gt;

namespace fs = std::filesystem;
int main()

{
    std::cout &lt;&lt; fs::path(&quot;/foo/bar.txt&quot;).filename() &lt;&lt; '\n'
              &lt;&lt; fs::path(&quot;/foo/.bar&quot;).filename() &lt;&lt; '\n'
              &lt;&lt; fs::path(&quot;/foo/bar/&quot;).filename() &lt;&lt; '\n'
              &lt;&lt; fs::path(&quot;/foo/.&quot;).filename() &lt;&lt; '\n'
              &lt;&lt; fs::path(&quot;/foo/..&quot;).filename() &lt;&lt; '\n'
              &lt;&lt; fs::path(&quot;.&quot;).filename() &lt;&lt; '\n'
              &lt;&lt; fs::path(&quot;..&quot;).filename() &lt;&lt; '\n'
              &lt;&lt; fs::path(&quot;/&quot;).filename() &lt;&lt; '\n'
              &lt;&lt; fs::path(&quot;//host&quot;).filename() &lt;&lt; '\n';
}
</code></pre>

<h2>Possible output:</h2>

&nbsp;<wbr>&nbsp;&quot;bar.txt&quot; 
&nbsp;<wbr>&nbsp;&quot;.bar&quot; 
&nbsp;<wbr>&nbsp;&quot;&quot; 
&nbsp;<wbr>&nbsp;&quot;.&quot; 
&nbsp;<wbr>&nbsp;&quot;..&quot; 
&nbsp;<wbr>&nbsp;&quot;.&quot; 
&nbsp;<wbr>&nbsp;&quot;..&quot; 
&nbsp;<wbr>&nbsp;&quot;&quot; 
&nbsp;<wbr>&nbsp;&quot;host&quot;

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns the file extension path component 
extension <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns the stem path component 
stem <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;replaces the last path component with another path 
replace_filename <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;checks if the corresponding path element is not empty 
has_filename <i>(public member function)</i> 
