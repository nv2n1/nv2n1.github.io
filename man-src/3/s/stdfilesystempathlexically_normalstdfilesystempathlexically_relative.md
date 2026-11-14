---
title: "stdfilesystempathlexically_normalstdfilesystempathlexically_relative(3)"
name: "stdfilesystempathlexically_normalstdfilesystempathlexically_relative"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdfilesystempathlexically_normalstdfilesystempathlexically_relative/"
description: "std::filesystem::path::lexically_normal,std::filesystem::path::lexically_relative, – std::filesystem::path::lexically_normal,std::filesystem::path::lexically_relative,"
---

<p>std::filesystem::path::lexically_normal,std::filesystem::path::lexically_relative, &#8211; std::filesystem::path::lexically_normal,std::filesystem::path::lexically_relative,</p>
<h2>Synopsis</h2>
<p>path lexically_normal()&nbsp;<wbr>const;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><code>(1)</code>&nbsp;<wbr><i>(since C++17)</i><br />
path lexically_relative(const path&amp;&nbsp;<wbr>base)&nbsp;<wbr>const;&nbsp;<wbr>&nbsp;<wbr><code>(2)</code>&nbsp;<wbr><i>(since C++17)</i><br />
path lexically_proximate(const path&amp;&nbsp;<wbr>base)&nbsp;<wbr>const;&nbsp;<wbr><code>(3)</code>&nbsp;<wbr><i>(since C++17)</i><br />
1)&nbsp;<wbr>Returns&nbsp;<wbr>*this converted to normal form in its generic format<br />
2)&nbsp;<wbr>Returns&nbsp;<wbr>*this made relative to base. </p>
<pre><code>*First, if root_name () != base.root_name() || is_absolute() != base.is_absolute()

            || (!has_root_directory() &amp;&amp; base.has_root_directory()),
    returns a

        default -
        constructed path.
            *Otherwise,
    first determines the first mismatched element of *this and base as if

    by auto [a, b] = mismatch(begin(), end(), base.begin(), base.end()),
                then
                            *if a
                        == end() and
                    b == base.end(),
                returns path(&quot;.&quot;);
  * otherwise, define N as the number of nonempty filename elements that are neither

 dot nor dot-dot in [b, base.end()), minus the number of dot-dot filename

 elements, If N &lt; 0, returns a default-constructed path.
  * otherwise, if N = 0 and a == end() || a-&gt;empty(), returns path(&quot;.&quot;).
  * otherwise returns an object composed from
* a default-constructed path() followed by
  * N applications of operator/=(path(&quot;..&quot;)), followed by
  * one application of operator/= for each element in the half-open range [a, end())</code></pre>
<p>3)&nbsp;<wbr>If the value of lexically_relative(base)&nbsp;<wbr>is not an empty path, return it.<br />
Otherwise return&nbsp;<wbr>*this. </p>
<h2>Parameters</h2>
<p><i>(none)</i></p>
<h2>Return value</h2>
<p>1)&nbsp;<wbr>The normal form of the path<br />
2)&nbsp;<wbr>The relative form of the path<br />
3)&nbsp;<wbr>The proximate form of the path </p>
<h2>Exceptions</h2>
<p><i>(none)</i></p>
<h2>Notes</h2>
<p>These conversions are purely lexical. They do not check that the paths exist, do not<br />
follow symlinks, and do not access the filesystem at all. For symlink-following<br />
counterparts of lexically_relative and lexically_proximate, see relative and<br />
proximate.<br />
On Windows, the returned path has backslashes&nbsp;<wbr>(the preferred separators), </p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;iostream&gt;

#include &lt;filesystem&gt;

#include &lt;cassert&gt;

namespace fs = std::filesystem;
int main()

{
    assert(fs::path(&quot;foo/./bar/..&quot;).lexically_normal() == &quot;foo/&quot;);
    assert(fs::path(&quot;foo/.///bar/../&quot;).lexically_normal() == &quot;foo/&quot;);
    assert(fs::path(&quot;/a/d&quot;).lexically_relative(&quot;/a/b/c&quot;) == &quot;../../d&quot;);
    assert(fs::path(&quot;/a/b/c&quot;).lexically_relative(&quot;/a/d&quot;) == &quot;../b/c&quot;);
    assert(fs::path(&quot;a/b/c&quot;).lexically_relative(&quot;a&quot;) == &quot;b/c&quot;);
    assert(fs::path(&quot;a/b/c&quot;).lexically_relative(&quot;a/b/c/x/y&quot;) == &quot;../..&quot;);
    assert(fs::path(&quot;a/b/c&quot;).lexically_relative(&quot;a/b/c&quot;) == &quot;.&quot;);
    assert(fs::path(&quot;a/b&quot;).lexically_relative(&quot;c/d&quot;) == &quot;../../a/b&quot;);
}</code></pre>
<p>&nbsp;<wbr>&nbsp;<wbr>Defect reports<br />
The following behavior-changing defect reports were applied retroactively to<br />
previously published C++&nbsp;<wbr>standards.<br />
DR&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Applied to&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Behavior as published&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Correct behavior<br />
LWG 3096 C++17&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>trailing&nbsp;<wbr>&quot;/&quot;&nbsp;<wbr>and&nbsp;<wbr>&quot;/.&quot;&nbsp;<wbr>are handled incorrectly corrected </p>
<h2>See also</h2>
<p>relative&nbsp;<wbr>&nbsp;<wbr>composes a relative path<br />
proximate&nbsp;<wbr><i>(function)</i><br />
<i>(C++17)</i> </p>
