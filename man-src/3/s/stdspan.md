---
title: "stdspan(3)"
name: "stdspan"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdspan/"
description: "std::span<T,Extent>::subspan – std::span<T,Extent>::subspan"
---

<p>std::span&lt;T,Extent&gt;::subspan &#8211; std::span&lt;T,Extent&gt;::subspan</p>
<h2>Synopsis</h2>
<pre><code>template &lt;std::size_t Offset,

          std::size_t Count = std::dynamic_extent&gt;
(1)

    constexpr std::span&lt;element_type, E /* see below */&gt; subspan() const;

constexpr std::span&lt;element_type, std::dynamic_extent&gt;

subspan(std::size_t Offset, (2)

                                std::size_t Count = std::dynamic_extent) const;</code></pre>
<p>Obtains a span that is a view over the Count elements of this span starting at offset Offset. If Count is std::dynamic_extent, the number of elements in the subspan is size() &#8211; offset (i.e., it ends at the end of *this.).<br />
The behavior is undefined if either Offset or Count is out of range. This happens if<br />
* Offset is greater than size();<br />
* Count is not std::dynamic_extent and Offset + Count is greater than size().<br />
The extent E of the span returned by <code>(1)</code> is determined as follows:<br />
* If Count is not std::dynamic_extent, Count;<br />
* Otherwise, if Extent is not std::dynamic_extent, Extent &#8211; Offset;<br />
* Otherwise, std::dynamic_extent. </p>
<h2>Return value</h2>
<p>The requested subspan r, such that r.data() == this-&gt;data() + Offset. If Count is std::dynamic_extent, r.size() == this-&gt;size() &#8211; Offset; otherwise r.size() == Count. </p>
<h2>See also</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;obtains a subspan consisting of the first N elements of the sequence<br />
first <i>(public member function)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;obtains a subspan consisting of the last N elements of the sequence<br />
last <i>(public member function)</i> </p>
