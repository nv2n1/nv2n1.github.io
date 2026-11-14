---
title: "sc_forcelink(3)"
name: "sc_forcelink"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_forcelink/"
description: "sc::ForceLink –"
---

<p>sc::ForceLink &#8211; </p>
<p> This, together with <code>ForceLinkBase</code>, is used to force code for particular classes to be linked into executables.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;class.h&gt;</code></pre>
<p> Inherits <code>sc::ForceLinkBase&lt; A &gt;</code>.</p>
<h3>Public Member Functions</h3>
<p><code>DescribedClass</code> * <code>create</code> (A a)</p>
<h2>Detailed Description</h2>
<h3>template&lt;class T, class A = const Ref&lt;KeyVal&gt; &amp;&gt; class sc::ForceLink&lt; T, A &gt;</h3>
<p>This, together with <code>ForceLinkBase</code>, is used to force code for particular classes to be linked into executables. </p>
<p> Objects are created from input and checkpoint files by using class name lookup to find that class&#8217;s <code>ClassDesc</code> object. The <code>ClassDesc</code> object has members that can create the class. Unfortunately, linking in a library doesn&#8217;t cause code for the the <code>ClassDesc</code>, and thus the class itself, to be linked. <code>ForceLink</code> objects are created in linkage.h files for each library. The code containing the main routine for an executable can include these linkage files to force code for that library&#8217;s classes to be linked.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
