---
title: "stdexperimentalfilesystempathreplace_filename(3)"
name: "stdexperimentalfilesystempathreplace_filename"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalfilesystempathreplace_filename/"
---

std::experimental::filesystem::path::replace_filename - std::experimental::filesystem::path::replace_filename

<h2>Synopsis</h2>

path&amp; replace_filename( const path&amp; replacement ); (filesystem TS) 
Replaces a single filename component with replacement. 
Equivalent to the following: <pre><code>remove_filename();

operator/=(replacement);</code></pre> 
The behavior is undefined if the path has no filename component (has_filename returns false). 

<h2>Parameters</h2>

<i>(none)</i>

<h2>Return value</h2>

*this 

<h2>Exceptions</h2>

<i>(none)</i>

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;experimental/filesystem&gt;

namespace fs = std::experimental::filesystem;
int main()

{
    std::cout &lt;&lt; fs::path(&quot;/foo&quot;).replace_filename(&quot;bar&quot;) &lt;&lt; '\n'
              &lt;&lt; fs::path(&quot;/&quot;).replace_filename(&quot;bar&quot;) &lt;&lt; '\n';
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;&quot;/bar&quot; 
&nbsp;<wbr>&nbsp;&quot;bar&quot;

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;replaces the extension 
replace_extension <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns the filename path component 
filename <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;removes filename path component 
remove_filename <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;checks if the corresponding path element is not empty 
has_filename <i>(public member function)</i> 
