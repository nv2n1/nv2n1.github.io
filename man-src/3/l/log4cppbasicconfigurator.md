---
title: "log4cppbasicconfigurator(3)"
name: "log4cppbasicconfigurator"
section: "3"
letter: "l"
url: "/docs/linux/man/3-log4cppbasicconfigurator/"
description: "log4cpp::BasicConfigurator –"
---

<p>log4cpp::BasicConfigurator &#8211; </p>
<p> This class implements a trivial default configuration for <code>log4cpp</code>: it adds a <code>FileAppender</code> that logs to stdout and uses a <code>BasicLayout</code> to the root <code>Category</code>.</p>
<h2>Synopsis</h2>
<p>#include &lt;BasicConfigurator.hh&gt;</p>
<h3>Static Public Member Functions</h3>
<p>static void <code>configure</code> ()<br />
 <i>Performs a minimal configuration of </i><code>log4cpp</code>.</p>
<h2>Detailed Description</h2>
<p>This class implements a trivial default configuration for <code>log4cpp</code>: it adds a <code>FileAppender</code> that logs to stdout and uses a <code>BasicLayout</code> to the root <code>Category</code>. </p>
<p> <code>Since:</code></p>
<dl COMPACT>
<dd>0.3.2</dl>
<h2>Member Function Documentation</h2>
<h3>void log4cpp::BasicConfigurator::configure () [static]</h3>
<p>Performs a minimal configuration of <code>log4cpp</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for log4cpp from the source code.</p>
