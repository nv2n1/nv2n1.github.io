---
title: "atlas_funky_encmap(3)"
name: "atlas_funky_encmap"
section: "3"
letter: "a"
url: "/docs/linux/man/3-atlas_funky_encmap/"
description: "Atlas::Funky::EncMap – Encoder in Map state."
---

<p>Atlas::Funky::EncMap &#8211; Encoder in Map state. </p>
<h2>Synopsis</h2>
<p>#include &lt;<a href="file:/usr/include/FEncoder.h">FEncoder.h</a>&gt; </p>
<h3>Public Member Functions</h3>
<p><code>EncMap</code> (B &amp;<code>b</code>) </p>
<p> <code>EncMapValue</code>&lt; B, <code>EncMap</code>&lt; B, T &gt; &gt; <code>operator&lt;&lt;</code> (const std::string &amp;name)<br />
 <i>Start a value with its name. </i><br />
 T <code>operator&lt;&lt;</code> (<code>EndMap</code>)<br />
 <i>End this map. </i></p>
<h3>Protected Attributes</h3>
<p>B &amp; <code>b</code><br />
 <i>The bridge or encoder that is written to. </i></p>
<h2>Detailed Description</h2>
<h3>template&lt;class B, class T&gt; class Atlas::Funky::EncMap&lt; B, T &gt;</h3>
<p>Encoder in Map state. </p>
<p> <code>See also:</code></p>
<dl COMPACT>
<dd><code>Atlas Funky Encoder</code></dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Atlas-C++ from the source code.</p>
