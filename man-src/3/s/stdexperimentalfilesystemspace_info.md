---
title: "stdexperimentalfilesystemspace_info(3)"
name: "stdexperimentalfilesystemspace_info"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalfilesystemspace_info/"
---

std::experimental::filesystem::space_info - std::experimental::filesystem::space_info

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;experimental / filesystem&gt;

    struct space_info {

    uintmax_t capacity;

    uintmax_t free;
    (filesystem TS)

        uintmax_t available;
};</code></pre> 
Represents the filesystem information as determined by space 
The members have the following meaning: 
* capacity -- total size of the filesystem, in bytes 
* free -- free space on the filesystem, in bytes 
* available -- free space available to a non-privileged process (may be equal or less than free) 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;experimental/filesystem&gt;

namespace fs = std::experimental::filesystem;

int main()

{
    fs::space_info devi = fs::space(&quot;/dev/null&quot;);
    fs::space_info tmpi = fs::space(&quot;/tmp&quot;);
    std::cout &lt;&lt; &quot;.        Capacity       Free      Available\n&quot;
              &lt;&lt; &quot;/dev:   &quot; &lt;&lt; devi.capacity &lt;&lt; &quot;   &quot;
              &lt;&lt; devi.free &lt;&lt; &quot;   &quot; &lt;&lt; devi.available &lt;&lt; '\n'
              &lt;&lt; &quot;/tmp: &quot; &lt;&lt; tmpi.capacity &lt;&lt; &quot; &quot;
              &lt;&lt; tmpi.free &lt;&lt; &quot; &quot; &lt;&lt; tmpi.available &lt;&lt; '\n';
}
</code></pre>

<h2>Possible output:</h2>

&nbsp;<wbr>&nbsp;. Capacity Free Available 
&nbsp;<wbr>&nbsp;/dev: 4175114240 4175110144 4175110144 
&nbsp;<wbr>&nbsp;/tmp: 420651237376 411962273792 390570749952

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;determines available free space on the file system 
space <i>(function)</i> 
