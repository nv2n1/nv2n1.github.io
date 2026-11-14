---
title: "std__detail_rangematcher(3)"
name: "std__detail_rangematcher"
section: "3"
letter: "s"
url: "/docs/linux/man/3-std__detail_rangematcher/"
description: "std::__detail::_RangeMatcher< _InIterT, _TraitsT > –"
---

<p>std::__detail::_RangeMatcher&lt; _InIterT, _TraitsT &gt; &#8211;</p>
<h2>Synopsis</h2>
<h3>Public Types</h3>
<p>typedef _TraitsT::char_type <code>_CharT</code> </p>
<p> typedef <code>std::basic_string</code>&lt; _CharT &gt; <code>_StringT</code></p>
<h3>Public Member Functions</h3>
<pre><code>void _M_add_char (_CharT __c)



void _M_add_character_class (const _StringT &amp;__s)



void _M_add_collating_element (const _StringT &amp;__s)



void _M_add_equivalence_class (const _StringT &amp;__s)



_M_is_non_matching (__is_non_matching)



void _M_make_range ()



bool operator() (const _PatternCursor &amp;__pc) const



Public Attributes</code></pre>
<p> <code>__pad0__</code>: _M_traits(__t) </p>
<p> bool <code>_M_is_non_matching</code> </p>
<p> const _TraitsT &amp; <code>_M_traits</code></p>
<h2>Detailed Description</h2>
<h3>template&lt;typename _InIterT, typename _TraitsT&gt;struct std::__detail::_RangeMatcher&lt; _InIterT, _TraitsT &gt;</h3>
<p>Matches a character range (bracket expression) </p>
<p> Definition at line 152 of file regex_nfa.h.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for libstdc++ from the source code.</p>
