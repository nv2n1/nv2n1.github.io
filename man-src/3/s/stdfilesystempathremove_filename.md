---
title: "stdfilesystempathremove_filename(3)"
name: "stdfilesystempathremove_filename"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdfilesystempathremove_filename/"
description: "std::filesystem::path::remove_filename – std::filesystem::path::remove_filename"
---

<p>std::filesystem::path::remove_filename &#8211; std::filesystem::path::remove_filename</p>
<h2>Synopsis</h2>
<p>path&amp; remove_filename() <code>(1)</code> <i>(since C++17)</i><br />
Removes a single generic-format filename component (as returned by filename) from the given generic-format path.<br />
After this function completes, has_filename returns false. </p>
<h2>Parameters</h2>
<p><i>(none)</i></p>
<h2>Return value</h2>
<p>*this </p>
<h2>Exceptions</h2>
<p><i>(none)</i></p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;iostream&gt;

#include &lt;filesystem&gt;

namespace fs = std::filesystem;
int main()

{
    std::cout &lt;&lt; fs::path(&quot;foo/bar&quot;).remove_filename() &lt;&lt; '
'
              &lt;&lt; fs::path(&quot;foo/&quot;).remove_filename() &lt;&lt; '
'
              &lt;&lt; fs::path(&quot;/foo&quot;).remove_filename() &lt;&lt; '
'
              &lt;&lt; fs::path(&quot;/&quot;).remove_filename() &lt;&lt; '
';
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;&quot;foo/&quot;<br />
&nbsp;<wbr>&nbsp;&quot;foo/&quot;<br />
&nbsp;<wbr>&nbsp;&quot;/&quot;<br />
&nbsp;<wbr>&nbsp;&quot;/&quot;</p>
<h2>See also</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns the filename path component<br />
filename <i>(public member function)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;replaces the last path component with another path<br />
replace_filename <i>(public member function)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;checks if the corresponding path element is not empty<br />
has_filename <i>(public member function)</i> </p>
