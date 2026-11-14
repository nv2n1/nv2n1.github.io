---
title: "stdchar_traitsnot_eof(3)"
name: "stdchar_traitsnot_eof"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdchar_traitsnot_eof/"
description: "std::char_traits<CharT>::not_eof – std::char_traits<CharT>::not_eof"
---

<p>std::char_traits&lt;CharT&gt;::not_eof &#8211; std::char_traits&lt;CharT&gt;::not_eof</p>
<h2>Synopsis</h2>
<pre><code>static int_type not_eof( int_type e );                     (until C++11)

static constexpr int_type not_eof( int_type e ) noexcept;  (since C++11)</code></pre>
<p>Checks whether e is not equivalent to eof value.<br />
Formally<br />
* if X::eq_int_type(e, X::eof()) is false, returns e<br />
* otherwise, returns a value f such that X::eq_int_type(f, X::eof()) is false </p>
<h2>Parameters</h2>
<p>e &#8211; value to analyze</p>
<h2>Return value</h2>
<p>e if e and eof value are not equivalent, returns some other non-eof value otherwise. </p>
<h2>Complexity</h2>
<p>Constant.</p>
<h2>See also</h2>
<p>eof returns an eof value<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member function)</i><br />
<code>[static]</code> </p>
