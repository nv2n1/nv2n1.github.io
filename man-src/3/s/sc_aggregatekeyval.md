---
title: "sc_aggregatekeyval(3)"
name: "sc_aggregatekeyval"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_aggregatekeyval/"
description: "sc::AggregateKeyVal –"
---

<p>sc::AggregateKeyVal &#8211; </p>
<p> This takes several <code>KeyVal</code> objects and makes them look like one <code>KeyVal</code> object.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;keyval.h&gt;</code></pre>
<p> Inherits <code>sc::KeyVal</code>.</p>
<h3>Public Member Functions</h3>
<p>void <code>errortrace</code> (std::ostream &amp;fp=ExEnv::err0())<br />
 <i>Write a message to fp describing the error. </i><br />
 void <code>dump</code> (std::ostream &amp;fp=ExEnv::err0())<br />
 <i>Write a message to fp describing the error. </i> <code>Constructors.</code><br />
 These contructors create an <code>AggregateKeyVal</code> that is formed from several other <code>KeyVal</code> objects. The search order is keyval1, keyval2, and so on. All <code>KeyVal</code> objects including and after the first null <code>KeyVal</code> will be ignored.<br />
 <code>AggregateKeyVal</code> (const <code>Ref</code>&lt; <code>KeyVal</code> &gt; &amp;keyval1) </p>
<p> <code>AggregateKeyVal</code> (const <code>Ref</code>&lt; <code>KeyVal</code> &gt; &amp;keyval1, const <code>Ref</code>&lt; <code>KeyVal</code> &gt; &amp;keyval2) </p>
<p> <code>AggregateKeyVal</code> (const <code>Ref</code>&lt; <code>KeyVal</code> &gt; &amp;keyval1, const <code>Ref</code>&lt; <code>KeyVal</code> &gt; &amp;keyval2, const <code>Ref</code>&lt; <code>KeyVal</code> &gt; &amp;keyval3) </p>
<p> <code>AggregateKeyVal</code> (const <code>Ref</code>&lt; <code>KeyVal</code> &gt; &amp;keyval1, const <code>Ref</code>&lt; <code>KeyVal</code> &gt; &amp;keyval2, const <code>Ref</code>&lt; <code>KeyVal</code> &gt; &amp;keyval3, const <code>Ref</code>&lt; <code>KeyVal</code> &gt; &amp;keyval4)</p>
<h3>Protected Member Functions</h3>
<p>int <code>key_exists</code> (const char *)<br />
 <i>Ultimately called by exists. </i><br />
 <code>Ref</code>&lt; <code>KeyValValue</code> &gt; <code>key_value</code> (const char *, const <code>KeyValValue</code> &amp;def)<br />
 <i>Ultimately called by value. </i></p>
<h2>Detailed Description</h2>
<p>This takes several <code>KeyVal</code> objects and makes them look like one <code>KeyVal</code> object. </p>
<p> When a key is sought first <code>KeyVal</code>, then the next, and so on is searched until the keyword is found.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
