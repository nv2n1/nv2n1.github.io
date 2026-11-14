---
title: "std__detail_charmatcher(3)"
name: "std__detail_charmatcher"
section: "3"
letter: "s"
url: "/docs/linux/man/3-std__detail_charmatcher/"
description: "std::__detail::_CharMatcher< _InIterT, _TraitsT > –"
---

<p>std::__detail::_CharMatcher&lt; _InIterT, _TraitsT &gt; &#8211;</p>
<h2>Synopsis</h2>
<h3>Public Types</h3>
<p>typedef _TraitsT::char_type <code>char_type</code></p>
<h3>Public Member Functions</h3>
<p><code>_M_c</code> (_M_traits.translate(__c)) </p>
<p> bool <code>operator()</code> (const <code>_PatternCursor</code> &amp;__pc) const</p>
<h3>Public Attributes</h3>
<p><code>__pad0__</code>: _M_traits(__t) </p>
<p> char_type <code>_M_c</code> </p>
<p> const _TraitsT &amp; <code>_M_traits</code></p>
<h2>Detailed Description</h2>
<h3>template&lt;typename _InIterT, typename _TraitsT&gt;struct std::__detail::_CharMatcher&lt; _InIterT, _TraitsT &gt;</h3>
<p>Matches a single character. </p>
<p> Definition at line 129 of file regex_nfa.h.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for libstdc++ from the source code.</p>
