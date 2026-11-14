---
title: "stdlocalefacet(3)"
name: "stdlocalefacet"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdlocalefacet/"
description: "std::locale::facet – std::locale::facet"
---

<p>std::locale::facet &#8211; std::locale::facet</p>
<h2>Synopsis</h2>
<pre><code>Defined in header &lt;locale&gt;

class locale::facet;</code></pre>
<p>std::locale::facet is the base class for facets. It provides a common base class so that locales could store pointers to the facets they implement in a single indexed container, and it abstracts support for facet reference counting. Whenever a facet is added to a locale, the locale increments the reference count in the facet (through an implementation-specific mechanism). Whenever a locale is destructed or modified, it decrements the reference count in each facet it no longer implements. Whenever a facet&#8217;s reference count becomes zero, the locale performs delete static_cast&lt;std::locale::facet*&gt;(f) where f is the pointer to the facet. </p>
<h2>Member functions</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;constructs a new facet with specified reference count<br />
constructor <i>(protected member function)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;the copy assignment operator is deleted<br />
operator= <i>(protected member function)</i> </p>
<p>destructor the destructor is protected virtual<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(virtual protected member function)</i><br />
<code>[virtual]</code></p>
<h2>Example</h2>
<p>&nbsp;This section is incomplete<br />
&nbsp;Reason: no example </p>
<h2>See also</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;the facet index type: each facet class must declare or inherit a public static member of this type<br />
id <i>(class)</i> </p>
