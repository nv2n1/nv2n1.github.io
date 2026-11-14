---
title: "atlas_exception(3)"
name: "atlas_exception"
section: "3"
letter: "a"
url: "/docs/linux/man/3-atlas_exception/"
description: "Atlas::Exception – Base class for all exceptions thrown by Atlas-C++."
---

<p>Atlas::Exception &#8211; Base class for all exceptions thrown by Atlas-C++. </p>
<h2>Synopsis</h2>
<p>#include &lt;<a href="file:/usr/include/Exception.h">Exception.h</a>&gt; </p>
<p> Inherited by <code>Atlas::Message::WrongTypeException</code>, Atlas::Objects::DefaultLoadingException, <code>Atlas::Objects::NoSuchAttrException</code>, Atlas::Objects::NoSuchFactoryException, and Atlas::Objects::NullSmartPtrDereference. </p>
<h3>Public Member Functions</h3>
<p><code>Exception</code> (const std::string &amp;d=&#8217;UNKNOWN ERROR&#8217;) </p>
<p> const std::string &amp; <code>getDescription</code> () const </p>
<p> virtual const char * <code>what</code> () const throw () </p>
<h3>Protected Attributes</h3>
<p>std::string <code>m_description</code> </p>
<h2>Detailed Description</h2>
<p>Base class for all exceptions thrown by Atlas-C++. </p>
<p> All subclasses should pass in a description of the exceptional circumstance encountered. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Atlas-C++ from the source code.</p>
