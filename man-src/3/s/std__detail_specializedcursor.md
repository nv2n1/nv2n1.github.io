---
title: "std__detail_specializedcursor(3)"
name: "std__detail_specializedcursor"
section: "3"
letter: "s"
url: "/docs/linux/man/3-std__detail_specializedcursor/"
description: "std::__detail::_SpecializedCursor< _FwdIterT > –"
---

<p>std::__detail::_SpecializedCursor&lt; _FwdIterT &gt; &#8211;</p>
<h2>Synopsis</h2>
<p> Inherits <code>std::__detail::_PatternCursor</code>.</p>
<h3>Public Member Functions</h3>
<p><code>_SpecializedCursor</code> (const _FwdIterT &amp;__b, const _FwdIterT __e) </p>
<p> bool <code>_M_at_end</code> () const </p>
<p> const _FwdIterT &amp; <code>_M_begin</code> () const </p>
<p> std::iterator_traits<br />
 &lt; _FwdIterT &gt;::value_type <code>_M_current</code> () const &quot; </p>
<p> const _FwdIterT &amp; <code>_M_end</code> () const </p>
<p> void <code>_M_next</code> () </p>
<p> _FwdIterT <code>_M_pos</code> () const</p>
<h2>Detailed Description</h2>
<h3>template&lt;typename _FwdIterT&gt;class std::__detail::_SpecializedCursor&lt; _FwdIterT &gt;</h3>
<p>Provides a cursor into the specific target string. </p>
<p> Definition at line 53 of file regex_cursor.h.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for libstdc++ from the source code.</p>
