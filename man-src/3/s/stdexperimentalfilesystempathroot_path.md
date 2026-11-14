---
title: "stdexperimentalfilesystempathroot_path(3)"
name: "stdexperimentalfilesystempathroot_path"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalfilesystempathroot_path/"
---

std::experimental::filesystem::path::root_path - std::experimental::filesystem::path::root_path

<h2>Synopsis</h2>

path root_path() const; (filesystem TS) 
Returns the root path of the path. If the path does not include root path, returns path(). 
Effectively, returns the following: root_name() / root_directory() 

<h2>Parameters</h2>

<i>(none)</i>

<h2>Return value</h2>

The root path of the path. 

<h2>Exceptions</h2>

<i>(none)</i>

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;experimental/filesystem&gt;

namespace fs = std::experimental::filesystem;
int main()

{
    std::cout &lt;&lt; &quot;Current root path is: &quot; &lt;&lt; fs::current_path().root_path() &lt;&lt; '\n';
}
</code></pre>

<h2>Possible output:</h2>

&nbsp;<wbr>&nbsp;Current root path is: &quot;C:\&quot;

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns the root-name of the path, if present 
root_name <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns the root directory of the path, if present 
root_directory <i>(public member function)</i> 
