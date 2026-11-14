---
title: "sc_ncresult(3)"
name: "sc_ncresult"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_ncresult/"
description: "sc::NCResult –"
---

<p>sc::NCResult &#8211; </p>
<p> This is similar to <code>Result</code>, but can be used with non-class types.</p>
<h2>Synopsis</h2>
<p> #include &lt;<a href="file:/usr/include/comptmpl.h">comptmpl.h</a>&gt; </p>
<p> Inherits <code>sc::ResultInfo</code>.</p>
<h3>Public Member Functions</h3>
<p> <code>NCResult</code> (<code>Compute</code> *c) </p>
<p> <code>NCResult</code> (const <code>NCResult</code>&lt; T &gt; &amp;r, <code>Compute</code> *c) </p>
<p> <code>operator T &amp;</code> () </p>
<p> T &amp; <code>result</code> () </p>
<p> T &amp; <code>result_noupdate</code> () </p>
<p> const T &amp; <code>result_noupdate</code> () const </p>
<p> void <code>operator=</code> (const T &amp;a) </p>
<p> void <code>operator=</code> (const <code>NCResult</code>&lt; T &gt; &amp;r) </p>
<h2>Detailed Description</h2>
<h3>template&lt;class T&gt; class sc::NCResult&lt; T &gt;</h3>
<p> This is similar to <code>Result</code>, but can be used with non-class types. </p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for MPQC from the source code.</p>
