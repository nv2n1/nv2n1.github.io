---
title: "stdlocaleglobal(3)"
name: "stdlocaleglobal"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdlocaleglobal/"
description: "std::locale::global – std::locale::global"
---

<p>std::locale::global &#8211; std::locale::global</p>
<h2>Synopsis</h2>
<pre><code>Defined in header&lt;locale&gt;

    static locale global(const locale &amp;loc);
Replaces the global C++ locale with loc, which means all future calls to the std::locale default constructor will now return a copy of loc.If loc has a name, also replaces the C locale as if by std::setlocale(LC_ALL, loc.name().c_str());
.This function is the only way to modify the global C++ locale, which is otherwise equivalent to std::locale::classic() at program startup.
</code></pre>
<h2>Parameters</h2>
<p>loc &#8211; the new global C++ locale</p>
<h2>Return value</h2>
<p>The previous value of the global C++ locale. </p>
<h2>Example</h2>
<p>&nbsp;This section is incomplete<br />
&nbsp;Reason: no example </p>
<h2>See also</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;constructs a new locale<br />
constructor <i>(public member function)</i><br />
classic obtains a reference to the &quot;C&quot; locale<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member function)</i><br />
<code>[static]</code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;gets and sets the current C locale<br />
setlocale <i>(function)</i> </p>
