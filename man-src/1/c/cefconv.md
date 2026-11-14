---
title: "cefconv(1)"
name: "cefconv"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cefconv/"
description: "cefconv – convert a TeX document containing CEF macros into `preprocessed’ form."
---

<h2 class="name">NAME</h2>
<p> cefconv &#8211; convert a TeX document containing CEF macros into `preprocessed&#8217; form. </p>
<h2>SYNOPSIS</h2>
<p> <code>cefconv</code> &lt; <i>infile</i> &gt; <i>outfile</i></p>
<h2>DESCRIPTION</h2>
<p> The <code>Chinese Encoding Framework</code> (<code>CEF</code>) developed by Christian Wittern makes it possible to include CJK characters in various encodings using the SGML macros <code>&amp;CX-aabb;</code> for Big 5 and CNS encoding and <code>&amp;U-aabb;</code> for Unicode (<code>X</code> denotes a number between 0 and 7; 0 represents Big 5 encoding, 1-7 CNS encoding planes 1-7. <code>aabb</code> is either a decimal or hexadecimal number) </p>
<p> <code>cefconv</code> converts the CEF macros into a form which can directly processed with LaTeX 2e. </p>
<p> This filter is part of the <code>CJK</code> macro package for LaTeX 2e.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-sjisconv/">sjisconv</a></code>(1), <code><a href="/docs/linux/man/1-bg5conv/">bg5conv</a></code>(1), <code><a href="/docs/linux/man/1-cef5conv/">cef5conv</a></code>(1), <code><a href="/docs/linux/man/1-cefsconv/">cefsconv</a></code>(1), <code><a href="/docs/linux/man/1-extconv/">extconv</a></code>(1),<br />
 the <code>CJK</code> documentation files.</p>
<h2>AUTHOR</h2>
<p> Werner Lemberg </p>
<h2>Index</h2>
