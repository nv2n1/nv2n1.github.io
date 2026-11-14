---
title: "stdlocale_id(3)"
name: "stdlocale_id"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdlocale_id/"
description: "std::locale::id –"
---

<p>std::locale::id &#8211;</p>
<h2>Synopsis</h2>
<h3>Public Member Functions</h3>
<p><code>id</code> () </p>
<p> size_t <code>_M_id</code> () const throw ()</p>
<h3>Friends</h3>
<p>template&lt;typename _Facet &gt; bool <code>has_facet</code> (const <code>locale</code> &amp;) throw () </p>
<p> class <code>locale</code> </p>
<p> class <code>locale::_Impl</code> </p>
<p> template&lt;typename _Facet &gt; const _Facet &amp; <code>use_facet</code> (const <code>locale</code> &amp;)</p>
<h2>Detailed Description</h2>
<p>Facet ID class. </p>
<p> The ID class provides facets with an index used to identify them. Every facet class must define a public static member locale::id, or be derived from a facet that provides this member, otherwise the facet cannot be used in a locale. The locale::id ensures that each class type gets a unique identifier. </p>
<p> Definition at line 436 of file locale_classes.h.</p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>std::locale::id::id () [inline]</h3>
<p>Constructor. </p>
<p> Definition at line 467 of file locale_classes.h.</p>
<h2>Friends And Related Function Documentation</h2>
<h3>template&lt;typename _Facet &gt; bool has_facet (const <code>locale</code> &amp;) [friend]</h3>
<p>Test for the presence of a facet. </p>
<p> has_facet tests the locale argument for the presence of the facet type provided as the template parameter. Facets derived from the facet parameter will also return true. </p>
<p> <code>Template Parameters:</code></p>
<dl>
<dd><i>_Facet</i> The facet type to test the presence of.</dl>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>__loc</i> The locale to test.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>true if __loc contains a facet of type _Facet, else false.</dl>
<p> Definition at line 104 of file locale_classes.tcc.</p>
<h3>template&lt;typename _Facet &gt; const _Facet&amp; use_facet (const <code>locale</code> &amp;) [friend]</h3>
<p>Return a facet. </p>
<p> use_facet looks for and returns a reference to a facet of type Facet where Facet is the template parameter. If has_facet(locale) is true, there is a suitable facet to return. It throws std::bad_cast if the locale doesn&#8217;t contain a facet of type Facet. </p>
<p> <code>Template Parameters:</code></p>
<dl>
<dd><i>_Facet</i> The facet type to access.</dl>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>__loc</i> The locale to use.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>Reference to facet of type Facet.</dl>
<p> <code>Exceptions:</code></p>
<dl>
<dd><i>std::bad_cast</i> if __loc doesn&#8217;t contain a facet of type _Facet.</dl>
<p> Definition at line 132 of file locale_classes.tcc.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for libstdc++ from the source code.</p>
