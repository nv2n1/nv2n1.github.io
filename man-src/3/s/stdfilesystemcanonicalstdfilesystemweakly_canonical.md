---
title: "stdfilesystemcanonicalstdfilesystemweakly_canonical(3)"
name: "stdfilesystemcanonicalstdfilesystemweakly_canonical"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdfilesystemcanonicalstdfilesystemweakly_canonical/"
---

std::filesystem::canonical,std::filesystem::weakly_canonical - std::filesystem::canonical,std::filesystem::weakly_canonical

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;filesystem&gt;

    path canonical(const std::filesystem::path &amp;p);
(1)(since C++ 17)

    path canonical(const std::filesystem::path &amp;p, (2)(since C++ 17)

                                                       std::error_code &amp;ec);

path weakly_canonical(const std::filesystem::path &amp;p);
(3)(since C++ 17)

    path weakly_canonical(const std::filesystem::path &amp;p, (4)(since C++ 17)

                                                              std::error_code &amp;ec);
1-2) Converts path p to a canonical absolute path, i.e. an absolute path that has no dot, dot-dot elements or symbolic links in its generic format representation. If p is not an absolute path, the function behaves as if it is first made absolute by std::filesystem::absolute(p). The path p must exist.

3-4) Returns a path composed by operator/= from the result of calling canonical() with a path argument composed of the leading elements of p that exist (as determined by status(p) or status(p, ec)), if any, followed by the elements of p that do not exist, if any. The resulting path is in normal_form.
</code></pre>

<h2>Parameters</h2>

p - a path which may be absolute or relative; for canonical it must be an existing path 
ec - error code to store error status to

<h2>Return value</h2>

1-2) An absolute path that resolves to the same file as std::filesystem::absolute(p). 
3-4) A normal path of the form canonical(x)/y, where x is a path composed of the longest leading sequence of elements in p that exist, and y is a path composed of the remaining trailing non-existent elements of p 

<h2>Exceptions</h2>

The overload that does not take a std::error_code&amp; parameter throws filesystem_error on underlying OS API errors, constructed with p as the first path argument and the OS error code as the error code argument. The overload taking a std::error_code&amp; parameter sets it to the OS API error code if an OS API call fails, and executes ec.clear() if no errors occur. Any overload not marked noexcept may throw std::bad_alloc if memory allocation fails.

<h2>Notes</h2>

The function canonical() is modeled after the POSIX realpath. 
The function weakly_canonical() was introduced to simplify operational semantics of relative(). 
Defect reports 
The following behavior-changing defect reports were applied retroactively to previously published C++ standards. 
DR Applied to Behavior as published Correct behavior 
LWG_2956 C++17 canonical has a spurious base parameter removed 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;filesystem&gt;

namespace fs = std::filesystem;

int main()

{
    fs::path p = fs::path(&quot;..&quot;) / &quot;..&quot; / &quot;AppData&quot;;
    std::cout &lt;&lt; &quot;Current path is &quot; &lt;&lt; fs::current_path() &lt;&lt; '\n'
              &lt;&lt; &quot;Canonical path for &quot; &lt;&lt; p &lt;&lt; &quot; is &quot; &lt;&lt; fs::canonical(p) &lt;&lt; '\n';
}
</code></pre>

<h2>Possible output:</h2>

&nbsp;<wbr>&nbsp;Current path is &quot;C:\Users\abcdef\AppData\Local\Temp&quot; 
&nbsp;<wbr>&nbsp;Canonical path for &quot;..\..\AppData&quot; is &quot;C:\Users\abcdef\AppData&quot;

<h2>See also</h2>

path represents a path 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class)</i> 
<i>(C++17)</i> 
absolute composes an absolute path 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i> 
<i>(C++17)</i> 
relative composes a relative path 
proximate <i>(function)</i> 
<i>(C++17)</i> 
