---
title: "log4cppappendersfactory(3)"
name: "log4cppappendersfactory"
section: "3"
letter: "l"
url: "/docs/linux/man/3-log4cppappendersfactory/"
description: "log4cpp::AppendersFactory –"
---

<p>log4cpp::AppendersFactory &#8211; </p>
<h2>Synopsis</h2>
<p>#include &lt;AppendersFactory.hh&gt;</p>
<h3>Public Types</h3>
<p>typedef <code>FactoryParams</code> <code>params_t</code> </p>
<p> typedef std::auto_ptr&lt; <code>Appender</code> &gt;(* <code>create_function_t</code> )(const <code>params_t</code> &amp;params) </p>
<h3>Public Member Functions</h3>
<p>void <code>registerCreator</code> (const std::string &amp;class_name, <code>create_function_t</code> create_function) </p>
<p> std::auto_ptr&lt; <code>Appender</code> &gt; <code>create</code> (const std::string &amp;class_name, const <code>params_t</code> &amp;params) </p>
<p> bool <code>registered</code> (const std::string &amp;class_name) const </p>
<h3>Static Public Member Functions</h3>
<p>static <code>AppendersFactory</code> &amp; <code>getInstance</code> () </p>
<h2>Member Typedef Documentation</h2>
<h3>typedef std::auto_ptr&lt;<code>Appender</code>&gt;(* log4cpp::AppendersFactory::create_function_t)(const <code>params_t</code> &amp;params)</h3>
<h3>typedef <code>FactoryParams</code> <code>log4cpp::AppendersFactory::params_t</code></h3>
<h2>Member Function Documentation</h2>
<h3>std::auto_ptr&lt; <code>Appender</code> &gt; log4cpp::AppendersFactory::create (const std::string &amp;class_name, const <code>params_t</code> &amp;params)</h3>
<h3><code>AppendersFactory</code> &amp; log4cpp::AppendersFactory::getInstance () [static]</h3>
<h3>void log4cpp::AppendersFactory::registerCreator (const std::string &amp;class_name, <code>create_function_t</code>create_function)</h3>
<h3>bool log4cpp::AppendersFactory::registered (const std::string &amp;class_name) const</h3>
<h2>Author</h2>
<p>Generated automatically by Doxygen for log4cpp from the source code.</p>
