---
title: "stdfilesystempathrelative_path(3)"
name: "stdfilesystempathrelative_path"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdfilesystempathrelative_path/"
---

std::filesystem::path::relative_path - std::filesystem::path::relative_path

<h2>Synopsis</h2>

path relative_path() const; <i>(since C++17)</i> 
Returns path relative to root-path, that is, a pathname composed of every generic-format component of *this after root-path. If *this is an empty path, returns an empty path. 

<h2>Parameters</h2>

<i>(none)</i>

<h2>Return value</h2>

Path relative to the root_path. 

<h2>Exceptions</h2>

<i>(none)</i>

<h2>Examples</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;filesystem&gt;

namespace fs = std::filesystem;
int main()

{
    fs::path p = fs::current_path();
    std::cout &lt;&lt; &quot;The current path &quot; &lt;&lt; p &lt;&lt; &quot; decomposes into:\n&quot;
              &lt;&lt; &quot;root-path &quot; &lt;&lt; p.root_path() &lt;&lt; '\n'
              &lt;&lt; &quot;relative path &quot; &lt;&lt; p.relative_path() &lt;&lt; '\n';
}
</code></pre>

<h2>Possible output:</h2>

&nbsp;<wbr>&nbsp;The current path &quot;C:\Users\abcdef\Local Settings\temp&quot; decomposes into: 
&nbsp;<wbr>&nbsp;root-path &quot;C:\&quot; 
&nbsp;<wbr>&nbsp;relative path &quot;Users\abcdef\Local Settings\temp&quot;

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns the root-name of the path, if present 
root_name <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns the root directory of the path, if present 
root_directory <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns the root path of the path, if present 
root_path <i>(public member function)</i> 
