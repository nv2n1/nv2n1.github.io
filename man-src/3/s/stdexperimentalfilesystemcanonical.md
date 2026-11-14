---
title: "stdexperimentalfilesystemcanonical(3)"
name: "stdexperimentalfilesystemcanonical"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalfilesystemcanonical/"
description: "std::experimental::filesystem::canonical – std::experimental::filesystem::canonical"
---

<p>std::experimental::filesystem::canonical &#8211; std::experimental::filesystem::canonical</p>
<h2>Synopsis</h2>
<pre><code>Defined in header&lt;experimental / filesystem&gt;

    path canonical(const path &amp;p, const path &amp;base = current_path());
(1)(filesystem TS)

    path canonical(const path &amp;p, error_code &amp;ec);
(2)(filesystem TS)

    path canonical(const path &amp;p, const path &amp;base, error_code &amp;ec);
(3)(filesystem TS)</code></pre>
<p>Converts path p to a canonical absolute path, i.e. an absolute path that has no dot, dot-dot elements or symbolic links.<br />
If p is not an absolute path, the function behaves as if it is first made absolute by absolute(p, base) or absolute(p) for <code>(2)</code><br />
The path p must exist. </p>
<h2>Parameters</h2>
<p>p &#8211; a path which may be absolute or relative to base, and which must be an existing path<br />
base &#8211; base path to be used in case p is relative<br />
ec &#8211; error code to store error status to</p>
<h2>Return value</h2>
<p>An absolute path that resolves to the same file as absolute(p, base) (or absolute(p) for <code>(2)</code>). </p>
<h2>Exceptions</h2>
<p>The overload that does not take a error_code&amp; parameter throws filesystem_error on underlying OS API errors, constructed with p as the first argument, base as the second argument, and the OS error code as the error code argument. std::bad_alloc may be thrown if memory allocation fails. The overload taking a error_code&amp; parameter sets it to the OS API error code if an OS API call fails, and executes ec.clear() if no errors occur. This overload has<br />
noexcept specification:<br />
noexcept<br />
This function is modeled after the POSIX realpath.</p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;iostream&gt;

#include &lt;experimental/filesystem&gt;

namespace fs = std::experimental::filesystem;

int main()

{
    fs::path p = fs::path(&quot;..&quot;) / &quot;..&quot; / &quot;AppData&quot;;
    std::cout &lt;&lt; &quot;Current path is &quot; &lt;&lt; fs::current_path() &lt;&lt; '
'
              &lt;&lt; &quot;Canonical path for &quot; &lt;&lt; p &lt;&lt; &quot; is &quot; &lt;&lt; fs::canonical(p) &lt;&lt; '
';
}
</code></pre>
<h2>Possible output:</h2>
<p>&nbsp;<wbr>&nbsp;Current path is &quot;C:
