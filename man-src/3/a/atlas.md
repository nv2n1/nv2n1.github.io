---
title: "atlas(3)"
name: "atlas"
section: "3"
letter: "a"
url: "/docs/linux/man/3-atlas/"
description: "Atlas – The Atlas namespace."
---

<p>Atlas &#8211; The <code>Atlas</code> namespace. </p>
<h2>Synopsis</h2>
<h3>Namespaces</h3>
<p>namespace <code>Net</code><br />
 <i>The </i><code>Atlas</code> network communication namespace. </p>
<p> namespace <code>Objects</code><br />
 <i>The </i><code>Atlas</code> high level <code>Objects</code> namespace. </p>
<h3>Classes</h3>
<p>class <code>Bridge</code><br />
 <i></i><code>Atlas</code> stream bridge.<br />
 class <code>Codec</code><br />
 <i></i><code>Atlas</code> stream codec.<br />
 class <code>EncoderBase</code><br />
 <i>Base class forwarding to </i><code>Atlas::Bridge</code> as skeleton for other encoders.<br />
 class <code>Exception</code><br />
 <i>Base class for all exceptions thrown by Atlas-C++. </i><br />
 class <code>Filter</code><br />
 <i></i><code>Atlas</code> stream filter.<br />
 class <code>filterbuf</code> </p>
<p> class <code>Formatter</code><br />
 <i></i><code>Atlas</code> stream formatter.<br />
 class <code>Negotiate</code><br />
 <i>Negotiation of codecs and filters for an </i><code>Atlas</code> connection.<br />
 class <code>Task</code> </p>
<h3>Typedefs</h3>
<p>typedef int <code>int_type</code> </p>
<h2>Detailed Description</h2>
<p>The <code>Atlas</code> namespace. </p>
<p> This namespace contains the whole of the Atlas-C++ library, and which is divided into a hierarchy of other namespaces. The main namespaces of interest to the application developers are the <code>Atlas::Net</code> namespace containing classes to handle establishing network connections, and the <code>Atlas::Objects</code> namespace containing classes used to handle high level <code>Atlas</code> data. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Atlas-C++ from the source code.</p>
