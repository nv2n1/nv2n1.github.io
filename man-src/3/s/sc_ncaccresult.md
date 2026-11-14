---
title: "sc_ncaccresult(3)"
name: "sc_ncaccresult"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_ncaccresult/"
description: "sc::NCAccResult –"
---

<p>sc::NCAccResult &#8211; </p>
<p> This associates a result non-class datum with an accuracy.</p>
<h2>Synopsis</h2>
<p> #include &lt;<a href="file:/usr/include/comptmpl.h">comptmpl.h</a>&gt; </p>
<p> Inherits <code>sc::AccResultInfo</code>.</p>
<h3>Public Member Functions</h3>
<p> <code>NCAccResult</code> (<code>Compute</code> *c) </p>
<p> <code>NCAccResult</code> (const <code>NCAccResult</code>&lt; T &gt; &amp;r, <code>Compute</code> *c) </p>
<p> <code>operator T &amp;</code> () </p>
<p> T &amp; <code>result</code> () </p>
<p> T &amp; <code>result_noupdate</code> () </p>
<p> const T &amp; <code>result_noupdate</code> () const </p>
<p> void <code>operator=</code> (const T &amp;a) </p>
<p> void <code>operator=</code> (const <code>NCAccResult</code>&lt; T &gt; &amp;r) </p>
<p> void <code>restore_state</code> (<code>StateIn</code> &amp;s) </p>
<p> void <code>save_data_state</code> (<code>StateOut</code> &amp;s) </p>
<p> <code>NCAccResult</code> (<code>StateIn</code> &amp;s, <code>Compute</code> *c) </p>
<h2>Detailed Description</h2>
<h3>template&lt;class T&gt; class sc::NCAccResult&lt; T &gt;</h3>
<p> This associates a result non-class datum with an accuracy. </p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for MPQC from the source code.</p>
