---
title: "log4cpplayoutsfactory(3)"
name: "log4cpplayoutsfactory"
section: "3"
letter: "l"
url: "/docs/linux/man/3-log4cpplayoutsfactory/"
description: "log4cpp::LayoutsFactory –"
---

<p>log4cpp::LayoutsFactory &#8211; </p>
<h2>Synopsis</h2>
<p>#include &lt;LayoutsFactory.hh&gt;</p>
<h3>Public Types</h3>
<p>typedef <code>FactoryParams</code> <code>params_t</code> </p>
<p> typedef std::auto_ptr&lt; <code>Layout</code> &gt;(* <code>create_function_t</code> )(const <code>params_t</code> &amp;params) </p>
<h3>Public Member Functions</h3>
<p>void <code>registerCreator</code> (const std::string &amp;class_name, <code>create_function_t</code> create_function) </p>
<p> std::auto_ptr&lt; <code>Layout</code> &gt; <code>create</code> (const std::string &amp;class_name, const <code>params_t</code> &amp;params) </p>
<p> bool <code>registed</code> (const std::string &amp;class_name) const </p>
<h3>Static Public Member Functions</h3>
<p>static <code>LayoutsFactory</code> &amp; <code>getInstance</code> () </p>
<h2>Member Typedef Documentation</h2>
<h3>typedef std::auto_ptr&lt;<code>Layout</code>&gt;(* log4cpp::LayoutsFactory::create_function_t)(const <code>params_t</code> &amp;params)</h3>
<h3>typedef <code>FactoryParams</code> <code>log4cpp::LayoutsFactory::params_t</code></h3>
<h2>Member Function Documentation</h2>
<h3>std::auto_ptr&lt; <code>Layout</code> &gt; log4cpp::LayoutsFactory::create (const std::string &amp;class_name, const <code>params_t</code> &amp;params)</h3>
<h3><code>LayoutsFactory</code> &amp; log4cpp::LayoutsFactory::getInstance () [static]</h3>
<h3>bool log4cpp::LayoutsFactory::registed (const std::string &amp;class_name) const</h3>
<h3>void log4cpp::LayoutsFactory::registerCreator (const std::string &amp;class_name, <code>create_function_t</code>create_function)</h3>
<h2>Author</h2>
<p>Generated automatically by Doxygen for log4cpp from the source code.</p>
