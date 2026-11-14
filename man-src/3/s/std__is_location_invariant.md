---
title: "std__is_location_invariant(3)"
name: "std__is_location_invariant"
section: "3"
letter: "s"
url: "/docs/linux/man/3-std__is_location_invariant/"
description: "std::__is_location_invariant< _Tp > –"
---

<p>std::__is_location_invariant&lt; _Tp &gt; &#8211;</p>
<h2>Synopsis</h2>
<p> Inherits <code>std::integral_constant&lt; bool,(is_pointer&lt; _Tp &gt;::value||is_member_pointer&lt; _Tp &gt;::value)&gt;</code>. Inherited by std::__is_location_invariant&lt; _Simple_type_wrapper&lt; _Tp &gt; &gt;.</p>
<h3>Public Types</h3>
<p>typedef <code>integral_constant</code><br />
 &lt; bool, __v &gt; <code>type</code>&quot; </p>
<p> typedef bool <code>value_type</code></p>
<h3>Public Member Functions</h3>
<p>constexpr <code>operator value_type</code> ()</p>
<h3>Static Public Attributes</h3>
<pre><code>static constexpr bool value</code></pre>
<h2>Detailed Description</h2>
<h3>template&lt;typename _Tp&gt;struct std::__is_location_invariant&lt; _Tp &gt;</h3>
<p>Trait identifying &#8216;location-invariant&#8217; types, meaning that the address of the object (or any of its members) will not escape. Also implies a trivial copy constructor and assignment operator. </p>
<p> Definition at line 1781 of file functional.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for libstdc++ from the source code.</p>
