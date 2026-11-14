---
title: "stdfilesystempathreplace_extension(3)"
name: "stdfilesystempathreplace_extension"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdfilesystempathreplace_extension/"
---

std::filesystem::path::replace_extension - std::filesystem::path::replace_extension

<h2>Synopsis</h2>

<pre><code>path &amp;replace_extension(const path &amp;replacement = path());
(1)(since C++ 17)
        Replaces the extension with replacement
    or removes it when the default value of replacement is used.

       Firstly,
    if this path has an extension(), it is removed from the generic - format view of the pathname.

                                                                      Then,
    a dot character is appended to the generic - format view of the pathname, if replacement is not empty or does not begin with a dot character.

                                                                                                             Then replacement is appended as if by
                                                                                                             operator+=(replacement)
</code></pre>

<h2>Parameters</h2>

replacement - the extension to replace with

<h2>Return value</h2>

*this 

<h2>Exceptions</h2>

<i>(none)</i>

<h2>Notes</h2>

The type of replacement is std::filesystem::path even though it is not intended to represent an object on the file system in order to correctly account for the filesystem character encoding. 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;filesystem&gt;

namespace fs = std::filesystem;
int main()

{
    fs::path p = &quot;/foo/bar.jpeg&quot;;
    std::cout &lt;&lt; &quot;Was: &quot; &lt;&lt; p &lt;&lt; '\n';
    p.replace_extension(&quot;.jpg&quot;);
    std::cout &lt;&lt; &quot;Now: &quot; &lt;&lt; p &lt;&lt; '\n';
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;Was: &quot;/foo/bar.jpeg&quot; 
&nbsp;<wbr>&nbsp;Now: &quot;/foo/bar.jpg&quot;

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns the file extension path component 
extension <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns the filename path component 
filename <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns the stem path component 
stem <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;checks if the corresponding path element is not empty 
has_extension <i>(public member function)</i> 
