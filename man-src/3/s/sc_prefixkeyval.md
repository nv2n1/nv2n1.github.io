---
title: "sc_prefixkeyval(3)"
name: "sc_prefixkeyval"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_prefixkeyval/"
description: "sc::PrefixKeyVal –"
---

<p>sc::PrefixKeyVal &#8211; </p>
<p> <code>PrefixKeyVal</code> is a <code>KeyVal</code> that searches a different <code>KeyVal</code> using modified keys.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;keyval.h&gt;</code></pre>
<p> Inherits <code>sc::KeyVal</code>.</p>
<h3>Public Member Functions</h3>
<p>void <code>errortrace</code> (std::ostream &amp;fp=ExEnv::err0())<br />
 <i>Write a message to fp describing the error. </i><br />
 void <code>dump</code> (std::ostream &amp;fp=ExEnv::err0())<br />
 <i>Write a message to fp describing the error. </i> <code>Constructors.</code><br />
 Construct a <code>PrefixKeyVal</code>, using the given prefix and indices.<br />
 <code>PrefixKeyVal</code> (const <code>Ref</code>&lt; <code>KeyVal</code> &gt; &amp;, int i) </p>
<p> <code>PrefixKeyVal</code> (const <code>Ref</code>&lt; <code>KeyVal</code> &gt; &amp;, int i, int j) </p>
<p> <code>PrefixKeyVal</code> (const <code>Ref</code>&lt; <code>KeyVal</code> &gt; &amp;, int i, int j, int k) </p>
<p> <code>PrefixKeyVal</code> (const <code>Ref</code>&lt; <code>KeyVal</code> &gt; &amp;, int i, int j, int k, int l) </p>
<p> <code>PrefixKeyVal</code> (const <code>Ref</code>&lt; <code>KeyVal</code> &gt; &amp;, const char *prefix) </p>
<p> <code>PrefixKeyVal</code> (const <code>Ref</code>&lt; <code>KeyVal</code> &gt; &amp;, const char *prefix, int i) </p>
<p> <code>PrefixKeyVal</code> (const <code>Ref</code>&lt; <code>KeyVal</code> &gt; &amp;, const char *prefix, int i, int j) </p>
<p> <code>PrefixKeyVal</code> (const <code>Ref</code>&lt; <code>KeyVal</code> &gt; &amp;, const char *prefix, int i, int j, int k) </p>
<p> <code>PrefixKeyVal</code> (const <code>Ref</code>&lt; <code>KeyVal</code> &gt; &amp;, const char *prefix, int i, int j, int k, int l)</p>
<h2>Detailed Description</h2>
<p><code>PrefixKeyVal</code> is a <code>KeyVal</code> that searches a different <code>KeyVal</code> using modified keys. </p>
<p> This is convenient for reading keys grouped together with a common prefix. Consider the following code: </p>
<pre> sc::Ref&lt;sc::KeyVal&gt; keyval = new <code>sc::PrefixKeyVal</code>('A',original_keyval);
 int r = keyval-&gt;intvalue('x');</pre>
<p>&nbsp;<wbr>This code will assign to r the value associated with&nbsp;<wbr>&#8216;x&#8217;&nbsp;<wbr>in keyval. keyval will search for&nbsp;<wbr>&#8216;x&#8217;&nbsp;<wbr>by searching for&nbsp;<wbr>&#8216;A::x&#8217;&nbsp;<wbr>in original_keyval. </p>
<p> This class is important for implementing constructors that take <code>KeyVal</code> arguments. When an object is being constructed from a <code>KeyVal</code>, it may contain another object that must be constructed from a <code>KeyVal</code>. In order to let the sub-object read the correct keywords from the <code>KeyVal</code>, without knowledge of the containing objects keyword prefix, a <code>PrefixKeyVal</code> can be constructed. For example, the code </p>
<pre> class A: public DescribedClass {
 double f0_;
 public:
 A(const Ref&lt;KeyVal&gt; &amp;keyval): f0_(keyval-&gt;doublevalue('f0')) {}
 }
 class B: public DescribedClass {
 double f1_;
 Ref&lt;A&gt; a_;
 public:
 B(const Ref&lt;KeyVal&gt; &amp;keyval):
 f1_(keyval-&gt;doublevalue('f1')),
 a_(new PrefixKeyVal(keyval,'a'))
 {}
 };</pre>
<p>&nbsp;<wbr>can be used to read&nbsp;<wbr><code>ParsedKeyVal</code>&nbsp;<wbr>input that looks like&nbsp;<wbr> </p>
<pre> b&lt;B&gt;: (
 f1 = 1.0
 a&lt;A&gt;: (
 f0 = 2.0
 )
 )</pre>
<p>&nbsp;<wbr></p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
