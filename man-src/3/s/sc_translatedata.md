---
title: "sc_translatedata(3)"
name: "sc_translatedata"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_translatedata/"
description: "sc::TranslateData –"
---

<p>sc::TranslateData &#8211; </p>
<p> Generic data translation.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;translate.h&gt;</code></pre>
<p> Inherited by <code>sc::TranslateDataByteSwap</code>.</p>
<h3>Public Member Functions</h3>
<p>virtual char <code>format_code</code> ()<br />
 <i>Returns a code for the type of format for the external data. </i><br />
 virtual void <code>to_native</code> (char *, int n)<br />
 <i>Translates to native format in-place. </i><br />
 virtual void <code>to_external</code> (char *, int n)<br />
 <i>Translates to external format in-place. </i><br />
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
<p> virtual void <code>to_native</code> (char *target, const void *source, int n)<br />
 <i>Translates to native format. </i><br />
 virtual void <code>to_external</code> (void *target, const char *source, int n)<br />
 <i>Translates to external format. </i><br />
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
<h3>Static Public Member Functions</h3>
<p>static <code>TranslateData</code> * <code>vctor</code> (char code)<br />
 <i>A virtual constructor that choses a specialization based on the format code. </i></p>
<h2>Detailed Description</h2>
<p>Generic data translation.</p>
<h2>Member Function Documentation</h2>
<h3>virtual void sc::TranslateData::to_external (void * target, const char * source, int n) [virtual]</h3>
<p>Translates to external format. Similar routines exist for all the basic types. </p>
<p> Reimplemented in <code>sc::TranslateDataByteSwap</code>.</p>
<h3>virtual void sc::TranslateData::to_external (char *, int n) [virtual]</h3>
<p>Translates to external format in-place. Similar routines exist for all the basic types. </p>
<p> Reimplemented in <code>sc::TranslateDataByteSwap</code>.</p>
<h3>virtual void sc::TranslateData::to_native (char * target, const void * source, int n) [virtual]</h3>
<p>Translates to native format. Similar routines exist for all the basic types. </p>
<p> Reimplemented in <code>sc::TranslateDataByteSwap</code>.</p>
<h3>virtual void sc::TranslateData::to_native (char *, int n) [virtual]</h3>
<p>Translates to native format in-place. Similar routines exist for all the basic types. </p>
<p> Reimplemented in <code>sc::TranslateDataByteSwap</code>.</p>
<h3>static <code>TranslateData</code>* sc::TranslateData::vctor (char code) [static]</h3>
<p>A virtual constructor that choses a specialization based on the format code.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
