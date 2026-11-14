---
title: "atlas_objects_nosuchattrexception(3)"
name: "atlas_objects_nosuchattrexception"
section: "3"
letter: "a"
url: "/docs/linux/man/3-atlas_objects_nosuchattrexception/"
description: "Atlas::Objects::NoSuchAttrException – An exception indicating the requested attribute does not exist."
---

<p>Atlas::Objects::NoSuchAttrException &#8211; An exception indicating the requested attribute does not exist. </p>
<h2>Synopsis</h2>
<p>#include &lt;<a href="file:/usr/include/BaseObject.h">BaseObject.h</a>&gt; </p>
<p> Inherits <code>Atlas::Exception</code>. </p>
<h3>Public Member Functions</h3>
<p><code>NoSuchAttrException</code> (const std::string &amp;name) </p>
<p> const std::string &amp; <code>getName</code> () const<br />
 <i>Get the name of the attribute which does not exist. </i></p>
<h2>Detailed Description</h2>
<p>An exception indicating the requested attribute does not exist. </p>
<p> This is thrown by Root::getAttr() [and derivatives thereof!] </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Atlas-C++ from the source code.</p>
