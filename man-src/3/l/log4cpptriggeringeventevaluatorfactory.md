---
title: "log4cpptriggeringeventevaluatorfactory(3)"
name: "log4cpptriggeringeventevaluatorfactory"
section: "3"
letter: "l"
url: "/docs/linux/man/3-log4cpptriggeringeventevaluatorfactory/"
description: "log4cpp::TriggeringEventEvaluatorFactory –"
---

<p>log4cpp::TriggeringEventEvaluatorFactory &#8211; </p>
<h2>Synopsis</h2>
<p>#include &lt;TriggeringEventEvaluatorFactory.hh&gt;</p>
<h3>Public Types</h3>
<p>typedef <code>FactoryParams</code> <code>params_t</code> </p>
<p> typedef std::auto_ptr<br />
 &lt; <code>TriggeringEventEvaluator</code> &gt;(* <code>create_function_t</code> )(const <code>params_t</code> &amp;params)&quot; </p>
<h3>Public Member Functions</h3>
<p>void <code>registerCreator</code> (const std::string &amp;class_name, <code>create_function_t</code> create_function) </p>
<p> std::auto_ptr<br />
 &lt; <code>TriggeringEventEvaluator</code> &gt; <code>create</code> (const std::string &amp;class_name, const <code>params_t</code> &amp;params)&quot; </p>
<p> bool <code>registered</code> (const std::string &amp;class_name) const </p>
<h3>Static Public Member Functions</h3>
<p>static<br />
 <code>TriggeringEventEvaluatorFactory</code> &amp; <code>getInstance</code> ()&quot; </p>
<h2>Member Typedef Documentation</h2>
<h3>typedef std::auto_ptr&lt;<code>TriggeringEventEvaluator</code>&gt;(* log4cpp::TriggeringEventEvaluatorFactory::create_function_t)(const <code>params_t</code> &amp;params)</h3>
<h3>typedef <code>FactoryParams</code> <code>log4cpp::TriggeringEventEvaluatorFactory::params_t</code></h3>
<h2>Member Function Documentation</h2>
<h3>std::auto_ptr&lt; <code>TriggeringEventEvaluator</code> &gt; log4cpp::TriggeringEventEvaluatorFactory::create (const std::string &amp;class_name, const <code>params_t</code> &amp;params)</h3>
<h3><code>TriggeringEventEvaluatorFactory</code> &amp; log4cpp::TriggeringEventEvaluatorFactory::getInstance () [static]</h3>
<h3>void log4cpp::TriggeringEventEvaluatorFactory::registerCreator (const std::string &amp;class_name, <code>create_function_t</code>create_function)</h3>
<h3>bool log4cpp::TriggeringEventEvaluatorFactory::registered (const std::string &amp;class_name) const</h3>
<h2>Author</h2>
<p>Generated automatically by Doxygen for log4cpp from the source code.</p>
