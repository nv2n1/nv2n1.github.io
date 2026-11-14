---
title: "sc_backtrack(3)"
name: "sc_backtrack"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_backtrack/"
description: "sc::Backtrack –"
---

<p>sc::Backtrack &#8211;</p>
<h2>Synopsis</h2>
<p> Inherits <code>sc::LineOpt</code>.</p>
<h3>Public Member Functions</h3>
<p><code>Backtrack</code> (const <code>Ref</code>&lt; <code>KeyVal</code> &gt; &amp;) </p>
<p> int <code>update</code> ()<br />
 <i>Take a step. </i></p>
<h3>Protected Attributes</h3>
<pre><code>double backtrack_factor_</code></pre>
<h2>Member Function Documentation</h2>
<h3>int sc::Backtrack::update () [virtual]</h3>
<p>Take a step. Returns 1 if the optimization has converged, otherwise 0. </p>
<p> Implements <code>sc::Optimize</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
