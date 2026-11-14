---
title: "stdrel_ops(3)"
name: "stdrel_ops"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdrel_ops/"
description: "std::rel_ops –"
---

<p>std::rel_ops &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions</h3>
<p>template&lt;class _Tp &gt; bool <code>operator!=</code> (const _Tp &amp;__x, const _Tp &amp;__y) </p>
<p> template&lt;class _Tp &gt; bool <code>operator&lt;=</code> (const _Tp &amp;__x, const _Tp &amp;__y) </p>
<p> template&lt;class _Tp &gt; bool <code>operator&gt;</code> (const _Tp &amp;__x, const _Tp &amp;__y) </p>
<p> template&lt;class _Tp &gt; bool <code>operator&gt;=</code> (const _Tp &amp;__x, const _Tp &amp;__y)</p>
<h2>Detailed Description</h2>
<p>The generated relational operators are sequestered here.</p>
<h2>Function Documentation</h2>
<h3>template&lt;class _Tp &gt; bool std::rel_ops::operator!= (const _Tp &amp;__x, const _Tp &amp;__y) [inline]</h3>
<p>Defines != for arbitrary types, in terms of ==. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>__x</i> A thing.<br />
 <i>__y</i> Another thing.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>__x != __y</dl>
<p> This function uses == to determine its result. </p>
<p> Definition at line 87 of file stl_relops.h.</p>
<h3>template&lt;class _Tp &gt; bool std::rel_ops::operator&lt;= (const _Tp &amp;__x, const _Tp &amp;__y) [inline]</h3>
<p>Defines &lt;= for arbitrary types, in terms of &lt;. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>__x</i> A thing.<br />
 <i>__y</i> Another thing.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>__x &lt;= __y</dl>
<p> This function uses &lt; to determine its result. </p>
<p> Definition at line 113 of file stl_relops.h.</p>
<h3>template&lt;class _Tp &gt; bool std::rel_ops::operator&gt; (const _Tp &amp;__x, const _Tp &amp;__y) [inline]</h3>
<p>Defines &gt; for arbitrary types, in terms of &lt;. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>__x</i> A thing.<br />
 <i>__y</i> Another thing.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>__x &gt; __y</dl>
<p> This function uses &lt; to determine its result. </p>
<p> Definition at line 100 of file stl_relops.h.</p>
<h3>template&lt;class _Tp &gt; bool std::rel_ops::operator&gt;= (const _Tp &amp;__x, const _Tp &amp;__y) [inline]</h3>
<p>Defines &gt;= for arbitrary types, in terms of &lt;. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>__x</i> A thing.<br />
 <i>__y</i> Another thing.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>__x &gt;= __y</dl>
<p> This function uses &lt; to determine its result. </p>
<p> Definition at line 126 of file stl_relops.h.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for libstdc++ from the source code.</p>
