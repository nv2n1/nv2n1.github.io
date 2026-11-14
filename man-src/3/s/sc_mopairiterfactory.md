---
title: "sc_mopairiterfactory(3)"
name: "sc_mopairiterfactory"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_mopairiterfactory/"
description: "sc::MOPairIterFactory –"
---

<p>sc::MOPairIterFactory &#8211; </p>
<p> This class produces <code>MOPairIter</code> objects.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;pairiter.h&gt;

Public Member Functions</code></pre>
<p> <code>Ref</code>&lt; <code>SpatialMOPairIter</code> &gt; <code>mopairiter</code> (const <code>Ref</code>&lt; <code>MOIndexSpace</code> &gt; &amp;space1, const <code>Ref</code>&lt; <code>MOIndexSpace</code> &gt; &amp;space2)<br />
 <i>Constructs an appropriate </i><code>MOPairIter</code> object.<br />
 <code>RefSCDimension</code> <code>scdim_aa</code> (const <code>Ref</code>&lt; <code>MOIndexSpace</code> &gt; &amp;space1, const <code>Ref</code>&lt; <code>MOIndexSpace</code> &gt; &amp;space2)<br />
 <i>Constructs an appropriate </i><code>RefSCDimension</code> object for same-spin pair.<br />
 <code>RefSCDimension</code> <code>scdim_ab</code> (const <code>Ref</code>&lt; <code>MOIndexSpace</code> &gt; &amp;space1, const <code>Ref</code>&lt; <code>MOIndexSpace</code> &gt; &amp;space2)<br />
 <i>Constructs an appropriate </i><code>RefSCDimension</code> object for different-spin pair.</p>
<h2>Detailed Description</h2>
<p>This class produces <code>MOPairIter</code> objects.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
