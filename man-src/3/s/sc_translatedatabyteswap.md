---
title: "sc_translatedatabyteswap(3)"
name: "sc_translatedatabyteswap"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_translatedatabyteswap/"
description: "sc::TranslateDataByteSwap –"
---

<p>sc::TranslateDataByteSwap &#8211; </p>
<p> Data translation to an external representation with bytes swapped.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;translate.h&gt;</code></pre>
<p> Inherits <code>sc::TranslateData</code>.</p>
<h3>Public Member Functions</h3>
<p>virtual char <code>format_code</code> ()<br />
 <i>Returns a code for the type of format for the external data. </i><br />
 virtual void <code>to_native</code> (char *, int n)<br />
 <i>Overridden translation routines exist for all the basic types. </i><br />
 virtual void <code>to_external</code> (char *, int n)<br />
 <i>Overridden translation routines exist for all the basic types. </i><br />
 virtual void <code>to_native</code> (short *, int n) </p>
<p> virtual void <code>to_external</code> (short *, int n) </p>
<p> virtual void <code>to_native</code> (unsigned int *, int n) </p>
<p> virtual void <code>to_external</code> (unsigned int *, int n) </p>
<p> virtual void <code>to_native</code> (int *, int n) </p>
<p> virtual void <code>to_external</code> (int *, int n) </p>
<p> virtual void <code>to_native</code> (long *, int n) </p>
<p> virtual void <code>to_external</code> (long *, int n) </p>
<p> virtual void <code>to_native</code> (float *, int n) </p>
<p> virtual void <code>to_external</code> (float *, int n) </p>
<p> virtual void <code>to_native</code> (double *, int n) </p>
<p> virtual void <code>to_external</code> (double *, int n) </p>
<p> virtual void <code>to_native</code> (char *, const void *, int n)<br />
 <i>Overridden translation routines exist for all the basic types. </i><br />
 virtual void <code>to_external</code> (void *, const char *, int n)<br />
 <i>Overridden translation routines exist for all the basic types. </i><br />
 virtual void <code>to_native</code> (short *, const void *, int n) </p>
<p> virtual void <code>to_external</code> (void *, const short *, int n) </p>
<p> virtual void <code>to_native</code> (unsigned int *, const void *, int n) </p>
<p> virtual void <code>to_external</code> (void *, const unsigned int *, int n) </p>
<p> virtual void <code>to_native</code> (int *, const void *, int n) </p>
<p> virtual void <code>to_external</code> (void *, const int *, int n) </p>
<p> virtual void <code>to_native</code> (long *, const void *, int n) </p>
<p> virtual void <code>to_external</code> (void *, const long *, int n) </p>
<p> virtual void <code>to_native</code> (float *, const void *, int n) </p>
<p> virtual void <code>to_external</code> (void *, const float *, int n) </p>
<p> virtual void <code>to_native</code> (double *, const void *, int n) </p>
<p> virtual void <code>to_external</code> (void *, const double *, int n)</p>
<h2>Detailed Description</h2>
<p>Data translation to an external representation with bytes swapped.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
