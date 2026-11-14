---
title: "sc_translatedataout(3)"
name: "sc_translatedataout"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_translatedataout/"
description: "sc::TranslateDataOut –"
---

<p>sc::TranslateDataOut &#8211; </p>
<p> Convert data to other formats.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;translate.h&gt;

Public Member Functions</code></pre>
<p> <code>TranslateDataOut</code> (<code>StateOut</code> *s, <code>TranslateData</code> *t)<br />
 <i>Write to s using the translation defined by t. </i><br />
 virtual int <code>put</code> (const char *, int)<br />
 <i>Translate and write the data. </i><br />
 virtual int <code>put</code> (const short *, int) </p>
<p> virtual int <code>put</code> (const unsigned int *, int) </p>
<p> virtual int <code>put</code> (const int *, int) </p>
<p> virtual int <code>put</code> (const long *, int) </p>
<p> virtual int <code>put</code> (const float *, int) </p>
<p> virtual int <code>put</code> (const double *, int) </p>
<p> <code>TranslateData</code> * <code>translator</code> ()<br />
 <i>Returns the translator. </i></p>
<h3>Protected Member Functions</h3>
<pre><code>int putv (const void *d, int s)</code></pre>
<h2>Detailed Description</h2>
<p>Convert data to other formats. </p>
<p> The generated data is inserted into a <code>StateOut</code> object.</p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>sc::TranslateDataOut::TranslateDataOut (<code>StateOut</code> * s, <code>TranslateData</code> * t)</h3>
<p>Write to s using the translation defined by t. The t argument will be deleted by this.</p>
<h2>Member Function Documentation</h2>
<h3>virtual int sc::TranslateDataOut::put (const char *, int) [virtual]</h3>
<p>Translate and write the data. A similar member exists for each basic type.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
