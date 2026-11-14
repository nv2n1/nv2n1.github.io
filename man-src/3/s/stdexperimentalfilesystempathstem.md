---
title: "stdexperimentalfilesystempathstem(3)"
name: "stdexperimentalfilesystempathstem"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalfilesystempathstem/"
---

std::experimental::filesystem::path::stem - std::experimental::filesystem::path::stem

<h2>Synopsis</h2>

path stem() const; (filesystem TS) 
Returns the filename identified by the path stripped of its extension. 
Returns the substring from the beginning of filename() up to and not including the last period (.) character. 
If the filename is one of the special filesystem components dot or dot-dot, or if it has no periods, the function returns the entire filename(). 

<h2>Parameters</h2>

<i>(none)</i>

<h2>Return value</h2>

The stem of the filename identified by the path. 

<h2>Exceptions</h2>

<i>(none)</i>

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;experimental/filesystem&gt;

namespace fs = std::experimental::filesystem;
int main()

{
    std::cout &lt;&lt; fs::path(&quot;/foo/bar.txt&quot;).stem() &lt;&lt; '\n'
              &lt;&lt; fs::path(&quot;/foo/.bar&quot;).stem() &lt;&lt; '\n';
    for (fs::path p = &quot;foo.bar.baz.tar&quot;; !p.extension().empty(); p = p.stem())
        std::cout &lt;&lt; p.extension() &lt;&lt; '\n';
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;&quot;bar&quot; 
&nbsp;<wbr>&nbsp;&quot;&quot; 
&nbsp;<wbr>&nbsp;&quot;.tar&quot; 
&nbsp;<wbr>&nbsp;&quot;.baz&quot; 
&nbsp;<wbr>&nbsp;&quot;.bar&quot;

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns the filename path component 
filename <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns the file extension path component 
extension <i>(public member function)</i> 
