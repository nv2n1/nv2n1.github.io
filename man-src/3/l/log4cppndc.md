---
title: "log4cppndc(3)"
name: "log4cppndc"
section: "3"
letter: "l"
url: "/docs/linux/man/3-log4cppndc/"
description: "log4cpp::NDC –"
---

<p>log4cpp::NDC &#8211; </p>
<p> The <code>NDC</code> class implements <i>nested diagnostic contexts</i> as defined by Neil Harrison in the article &#8216;Patterns for Logging Diagnostic Messages&#8217; part of the book &#8216;&lt;i&gt;Pattern Languages of Program Design 3&lt;/i&gt;&#8217; edited by Martin et al.</p>
<h2>Synopsis</h2>
<p>#include &lt;NDC.hh&gt;</p>
<h3>Classes</h3>
<p>struct <code>DiagnosticContext</code> </p>
<h3>Public Types</h3>
<p>typedef std::vector<br />
 &lt; <code>DiagnosticContext</code> &gt; <code>ContextStack</code>&quot; </p>
<h3>Public Member Functions</h3>
<p><code>NDC</code> () </p>
<p> virtual <code>~NDC</code> () </p>
<p> virtual void <code>_clear</code> () </p>
<p> virtual <code>ContextStack</code> * <code>_cloneStack</code> () </p>
<p> virtual const std::string &amp; <code>_get</code> () const </p>
<p> virtual size_t <code>_getDepth</code> () const </p>
<p> virtual void <code>_inherit</code> (<code>ContextStack</code> *stack) </p>
<p> virtual std::string <code>_pop</code> () </p>
<p> virtual void <code>_push</code> (const std::string &amp;message) </p>
<p> virtual void <code>_setMaxDepth</code> (int maxDepth) </p>
<h3>Static Public Member Functions</h3>
<p>static void <code>clear</code> ()<br />
 <i>Clear any nested disgnostic information if any. </i><br />
 static <code>ContextStack</code> * <code>cloneStack</code> ()<br />
 <i>Clone the diagnostic context for the current thread. </i><br />
 static const std::string &amp; <code>get</code> ()<br />
 <i>Get the current diagnostic context string. </i><br />
 static size_t <code>getDepth</code> ()<br />
 <i>Get the current nesting depth of this diagnostic context. </i><br />
 static void <code>inherit</code> (<code>ContextStack</code> *stack) </p>
<p> static std::string <code>pop</code> ()<br />
 <i>Clients should call this method before leaving a diagnostic context. </i><br />
 static void <code>push</code> (const std::string &amp;message)<br />
 <i>Push new diagnostic context information for the current thread. </i><br />
 static void <code>setMaxDepth</code> (int maxDepth)<br />
 <i>Set the maximum nesting depth for the current </i><code>NDC</code>.<br />
 static <code>NDC</code> &amp; <code>getNDC</code> ()<br />
 <i>Return the </i><code>NDC</code> for the current thread.</p>
<h3>Public Attributes</h3>
<p><code>ContextStack</code> <code>_stack</code> </p>
<h2>Detailed Description</h2>
<p>The <code>NDC</code> class implements <i>nested diagnostic contexts</i> as defined by Neil Harrison in the article &#8216;Patterns for Logging Diagnostic Messages&#8217; part of the book &#8216;&lt;i&gt;Pattern Languages of Program Design 3&lt;/i&gt;&#8217; edited by Martin et al. </p>
<p> A Nested Diagnostic Context, or <code>NDC</code> in short, is an instrument to distinguish interleaved log output from different sources. Log output is typically interleaved when a server handles multiple clients near-simulatanously. </p>
<p> Interleaved log output can still be meaningful if each log entry from different contexts had a distinctive stamp. This is where NDCs come into play. </p>
<p> <i></i><code>Note that NDCs are managed on a per thread basis</code>. <code>NDC</code> operations such as push, pop, clear, getDepth and setMaxDepth affect the <code>NDC</code> of the <i>current</i> thread only. NDCs of other threads remain unaffected. </p>
<p> To build an <code>NDC</code> one uses the push operation. Simply put, </p>
<dl COMPACT>
<dt>&bull;</p>
<dd>Contexts can be nested.</dl>
<dl COMPACT>
<dt>&bull;</p>
<dd>When entering a context, call <code>NDC.push</code>. As a side effect, if there is no nested diagnostic context for the current thread, this method will create it.</dl>
<dl COMPACT>
<dt>&bull;</p>
<dd>When leaving a context, call <code>NDC.pop</code>.</dl>
<p> There is no penalty for forgetting to match each push operation with a corresponding pop, except the obvious mismatch between the real application context and the context set in the <code>NDC</code>. </p>
<p> Custom Layouts may include the nested diagnostic context for the current thread in log messages, without any user intervention. Hence, even if a server is serving multiple clients simultaneously, the logs emanating from the same code (belonging to the same category) can still be distinguished because each client request will have a different <code>NDC</code> tag. </p>
<p> <i>Unfortunately, unlike Java, C++ does not have platform independent multithreading support. Therefore, currently </i><code>log4cpp</code> is not multithread aware, it implicitly assumes only one thread exists, the main process thread.</p>
<h2>Member Typedef Documentation</h2>
<h3>typedef std::vector&lt;<code>DiagnosticContext</code>&gt; <code>log4cpp::NDC::ContextStack</code></h3>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>log4cpp::NDC::NDC ()</h3>
<h3>log4cpp::NDC::~NDC () [virtual]</h3>
<h2>Member Function Documentation</h2>
<h3>void log4cpp::NDC::_clear () [virtual]</h3>
<h3><code>NDC::ContextStack</code> * log4cpp::NDC::_cloneStack () [virtual]</h3>
<h3>const std::string &amp; log4cpp::NDC::_get () const [virtual]</h3>
<h3>size_t log4cpp::NDC::_getDepth () const [virtual]</h3>
<h3>void log4cpp::NDC::_inherit (<code>NDC::ContextStack</code> *stack) [virtual]</h3>
<h3>std::string log4cpp::NDC::_pop () [virtual]</h3>
<h3>void log4cpp::NDC::_push (const std::string &amp;message) [virtual]</h3>
<h3>void log4cpp::NDC::_setMaxDepth (intmaxDepth) [virtual]</h3>
<h3>void log4cpp::NDC::clear () [static]</h3>
<p>Clear any nested disgnostic information if any. This method is useful in cases where the same thread can be potentially used over and over in different unrelated contexts. </p>
<p> This method is equivalent to calling the setMaxDepth method with a zero maxDepth argument.</p>
<h3><code>NDC::ContextStack</code> * log4cpp::NDC::cloneStack () [static]</h3>
<p>Clone the diagnostic context for the current thread. Internally a diagnostic context is represented as a stack. A given thread can supply the stack (i.e. diagnostic context) to a child thread so that the child can inherit the parent thread&#8217;s diagnostic context. </p>
<p> The child thread uses the inherit method to inherit the parent&#8217;s diagnostic context. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Stack A clone of the current thread&#8217;s diagnostic context.</dl>
<h3>const std::string &amp; log4cpp::NDC::get () [static]</h3>
<p>Get the current diagnostic context string. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>the context string.</dl>
<h3>size_t log4cpp::NDC::getDepth () [static]</h3>
<p>Get the current nesting depth of this diagnostic context. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>the nesting depth</dl>
<h3><code>NDC</code> &amp; log4cpp::NDC::getNDC () [static]</h3>
<p>Return the <code>NDC</code> for the current thread. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>the <code>NDC</code> for the current thread</dl>
<h3>void log4cpp::NDC::inherit (<code>NDC::ContextStack</code> *stack) [static]</h3>
<h3>std::string log4cpp::NDC::pop () [static]</h3>
<p>Clients should call this method before leaving a diagnostic context. The returned value is the value that was pushed last. If no context is available, then the empty string &#8221; is returned. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>String The innermost diagnostic context.</dl>
<h3>void log4cpp::NDC::push (const std::string &amp;message) [static]</h3>
<p>Push new diagnostic context information for the current thread. The contents of the message parameter is determined solely by the client. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>message</i> The new diagnostic context information.</dl>
<h3>void log4cpp::NDC::setMaxDepth (intmaxDepth) [static]</h3>
<p>Set the maximum nesting depth for the current <code>NDC</code>. Curently NDCs do not enforce a maximum depth and consequentially this method has no effect. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>maxDepth</i> the maximum nesting depth</dl>
<h2>Member Data Documentation</h2>
<h3><code>ContextStack</code> log4cpp::NDC::_stack</h3>
<h2>Author</h2>
<p>Generated automatically by Doxygen for log4cpp from the source code.</p>
