---
title: "stdlocaleclassic(3)"
name: "stdlocaleclassic"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdlocaleclassic/"
description: "std::locale::classic – std::locale::classic"
---

<p>std::locale::classic &#8211; std::locale::classic</p>
<h2>Synopsis</h2>
<pre><code>Defined in header&lt;locale&gt;

    static const locale &amp;classic();</code></pre>
<p>Obtains a reference to the C++ locale that implements the classic &quot;C&quot; locale semantics. This locale, unlike the global locale, cannot be altered. </p>
<h2>Parameters</h2>
<p>none</p>
<h2>Return value</h2>
<p>Returns a reference to the &quot;C&quot; locale. </p>
<h2>Notes</h2>
<p>Some of the standard-required facets, such as the UTF-8/UTF-32 conversion facet std::codecvt&lt;char32_t, char, std::mbstate_t&gt;, have no equivalents in the &quot;C&quot; locale, but they are nevertheless present in the locale returned by std::locale::classic(), as in any other locale constructed in a C++ program. </p>
<h2>Example</h2>
<p>&nbsp;This section is incomplete<br />
&nbsp;Reason: no example </p>
<h2>See also</h2>
<p>global changes the global locale<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member function)</i><br />
<code>[static]</code> </p>
