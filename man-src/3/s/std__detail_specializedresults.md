---
title: "std__detail_specializedresults(3)"
name: "std__detail_specializedresults"
section: "3"
letter: "s"
url: "/docs/linux/man/3-std__detail_specializedresults/"
description: "std::__detail::_SpecializedResults< _FwdIterT, _Alloc > –"
---

<p>std::__detail::_SpecializedResults&lt; _FwdIterT, _Alloc &gt; &#8211;</p>
<h2>Synopsis</h2>
<p> Inherits <code>std::__detail::_Results</code>.</p>
<h3>Public Member Functions</h3>
<p><code>_SpecializedResults</code> (const _Automaton::_SizeT __size, const <code>_SpecializedCursor</code>&lt; _FwdIterT &gt; &amp;__cursor, <code>match_results</code>&lt; _FwdIterT, _Alloc &gt; &amp;__m) </p>
<p> void <code>_M_set_matched</code> (int __i, bool __is_matched) </p>
<p> void <code>_M_set_pos</code> (int __i, int __j, const <code>_PatternCursor</code> &amp;__pc)</p>
<h2>Detailed Description</h2>
<h3>template&lt;typename _FwdIterT, typename _Alloc&gt;class std::__detail::_SpecializedResults&lt; _FwdIterT, _Alloc &gt;</h3>
<p>A _Results facade specialized for wrapping a templated match_results. </p>
<p> Definition at line 55 of file regex_grep_matcher.h.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for libstdc++ from the source code.</p>
