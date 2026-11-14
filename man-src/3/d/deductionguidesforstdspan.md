---
title: "deductionguidesforstdspan(3)"
name: "deductionguidesforstdspan"
section: "3"
letter: "d"
url: "/docs/linux/man/3-deductionguidesforstdspan/"
description: "deductionguidesforstd::span – deductionguidesforstd::span"
---

<p>deductionguidesforstd::span &#8211; deductionguidesforstd::span</p>
<h2>Synopsis</h2>
<p>Defined in header &lt;span&gt;<br />
template&lt;class T, std::size_t N&gt; <code>(1)</code><br />
span(T (&amp;)[N]) -&gt; span&lt;T, N&gt;;<br />
template&lt;class T, std::size_t N&gt; <code>(2)</code><br />
span(std::array&lt;T, N&gt;&amp;) -&gt; span&lt;T, N&gt;;<br />
template&lt;class T, std::size_t N&gt; <code>(3)</code><br />
span(const std::array&lt;T, N&gt;&amp;) -&gt; span&lt;const T, N&gt;;<br />
template&lt;class Container&gt; <code>(4)</code><br />
span(Container&amp;) -&gt; span&lt;typename Container::value_type&gt;;<br />
template&lt;class Container&gt; <code>(5)</code><br />
span(const Container&amp;) -&gt; span&lt;const typename Container::value_type&gt;; </p>
<p>Five deduction_guides are provided for span.<br />
(1-3) allow the static extent to be deduced from built-in arrays and std::array.<br />
(4-5) allow the element type to be deduced from containers that supply a nested type value_type.</p>
