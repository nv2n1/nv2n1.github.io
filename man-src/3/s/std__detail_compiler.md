---
title: "std__detail_compiler(3)"
name: "std__detail_compiler"
section: "3"
letter: "s"
url: "/docs/linux/man/3-std__detail_compiler/"
description: "std::__detail::_Compiler< _InIter, _TraitsT > –"
---

<p>std::__detail::_Compiler&lt; _InIter, _TraitsT &gt; &#8211;</p>
<h2>Synopsis</h2>
<h3>Public Types</h3>
<p>typedef std::iterator_traits<br />
 &lt; _InIter &gt;::value_type <code>_CharT</code>&quot; </p>
<p> typedef<br />
 <code>regex_constants::syntax_option_type</code> <code>_FlagT</code>&quot; </p>
<p> typedef _InIter <code>_IterT</code> </p>
<p> typedef <code>std::basic_string</code>&lt; _CharT &gt; <code>_StringT</code></p>
<h3>Public Member Functions</h3>
<p><code>_Compiler</code> (const _InIter &amp;__b, const _InIter &amp;__e, _TraitsT &amp;__traits, _FlagT __flags) </p>
<p> const <code>_Nfa</code> &amp; <code>_M_nfa</code> () const</p>
<h2>Detailed Description</h2>
<h3>template&lt;typename _InIter, typename _TraitsT&gt;class std::__detail::_Compiler&lt; _InIter, _TraitsT &gt;</h3>
<p>Builds an NFA from an input iterator interval. </p>
<p> Definition at line 634 of file regex_compiler.h.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for libstdc++ from the source code.</p>
