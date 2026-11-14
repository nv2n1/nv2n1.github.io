---
title: "stdfilesystempathextension(3)"
name: "stdfilesystempathextension"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdfilesystempathextension/"
---

std::filesystem::path::extension - std::filesystem::path::extension

<h2>Synopsis</h2>

path extension() const; <i>(since C++17)</i> 
Returns the extension of the filename component of the generic-format view of *this. 
If the filename() component of the generic-format path contains a period (.), and is not one of the special filesystem elements dot or dot-dot, then the extension is the substring beginning at the rightmost period (including the period) and until the end of the pathname. 
If the first character in the filename is a period, that period is ignored (a filename like &quot;.profile&quot; is not treated as an extension) 
If the pathname is either . or .., or if filename() does not contain the . character, then empty path is returned. 
Additional behavior may be defined by the implementations for file systems which append additional elements (such as alternate data streams or partitioned dataset names) to extensions. 

<h2>Parameters</h2>

<i>(none)</i>

<h2>Return value</h2>

The extension of the current pathname or an empty path if there's no extension. 

<h2>Exceptions</h2>

<i>(none)</i>

<h2>Notes</h2>

The extension as returned by this function includes a period to make it possible to distinguish the file that ends with a period <i>(function returns &quot;.&quot;) from a file with no extension (function returns &quot;&quot;)</i> 
On a non-POSIX system, it is possible that p.stem()+p.extension() != p.filename() even though generic-format versions are the same. 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;filesystem&gt;

namespace fs = std::filesystem;
int main()

{
    std::cout &lt;&lt; fs::path(&quot;/foo/bar.txt&quot;).extension() &lt;&lt; '\n'
              &lt;&lt; fs::path(&quot;/foo/bar.&quot;).extension() &lt;&lt; '\n'
              &lt;&lt; fs::path(&quot;/foo/bar&quot;).extension() &lt;&lt; '\n'
              &lt;&lt; fs::path(&quot;/foo/bar.txt/bar.cc&quot;).extension() &lt;&lt; '\n'
              &lt;&lt; fs::path(&quot;/foo/bar.txt/bar.&quot;).extension() &lt;&lt; '\n'
              &lt;&lt; fs::path(&quot;/foo/bar.txt/bar&quot;).extension() &lt;&lt; '\n'
              &lt;&lt; fs::path(&quot;/foo/.&quot;).extension() &lt;&lt; '\n'
              &lt;&lt; fs::path(&quot;/foo/..&quot;).extension() &lt;&lt; '\n'
              &lt;&lt; fs::path(&quot;/foo/.hidden&quot;).extension() &lt;&lt; '\n'
              &lt;&lt; fs::path(&quot;/foo/..bar&quot;).extension() &lt;&lt; '\n';
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;&quot;.txt&quot; 
&nbsp;<wbr>&nbsp;&quot;.&quot; 
&nbsp;<wbr>&nbsp;&quot;&quot; 
&nbsp;<wbr>&nbsp;&quot;.cc&quot; 
&nbsp;<wbr>&nbsp;&quot;.&quot; 
&nbsp;<wbr>&nbsp;&quot;&quot; 
&nbsp;<wbr>&nbsp;&quot;&quot; 
&nbsp;<wbr>&nbsp;&quot;&quot; 
&nbsp;<wbr>&nbsp;&quot;&quot; 
&nbsp;<wbr>&nbsp;&quot;.bar&quot;

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns the filename path component 
filename <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns the stem path component 
stem <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;replaces the extension 
replace_extension <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;checks if the corresponding path element is not empty 
has_extension <i>(public member function)</i> 
