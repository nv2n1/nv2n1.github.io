---
title: "stdexperimentalfilesystempathroot_directory(3)"
name: "stdexperimentalfilesystempathroot_directory"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalfilesystempathroot_directory/"
---

std::experimental::filesystem::path::root_directory - std::experimental::filesystem::path::root_directory

<h2>Synopsis</h2>

path root_directory() const; (filesystem TS) 
Returns the root directory of the path. If the path does not include root name, returns path(). 

<h2>Parameters</h2>

<i>(none)</i>

<h2>Return value</h2>

The root directory of the path. 

<h2>Exceptions</h2>

<i>(none)</i>

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;experimental/filesystem&gt;

namespace fs = std::experimental::filesystem;
int main()

{
    fs::path p = fs::current_path();
    std::cout &lt;&lt; &quot;The current path &quot; &lt;&lt; p &lt;&lt; &quot; decomposes into:\n&quot;
              &lt;&lt; &quot;root name &quot; &lt;&lt; p.root_name() &lt;&lt; '\n'
              &lt;&lt; &quot;root directory &quot; &lt;&lt; p.root_directory() &lt;&lt; '\n'
              &lt;&lt; &quot;relative path &quot; &lt;&lt; p.relative_path() &lt;&lt; '\n';
}
</code></pre>

<h2>Possible output:</h2>

&nbsp;<wbr>&nbsp;The current path &quot;C:\Users\abcdef\Local Settings\temp&quot; decomposes into: 
&nbsp;<wbr>&nbsp;root name &quot;C:&quot; 
&nbsp;<wbr>&nbsp;root directory &quot;\&quot; 
&nbsp;<wbr>&nbsp;relative path &quot;Users\abcdef\Local Settings\temp&quot;

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns the root-name of the path, if present 
root_name <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns the root path of the path, if present 
root_path <i>(public member function)</i> 
