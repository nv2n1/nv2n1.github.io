---
title: "atlas_objects(3)"
name: "atlas_objects"
section: "3"
letter: "a"
url: "/docs/linux/man/3-atlas_objects/"
description: "Atlas::Objects – The Atlas high level Objects namespace."
---

<p>Atlas::Objects &#8211; The <code>Atlas</code> high level <code>Objects</code> namespace. </p>
<h2>Synopsis</h2>
<h3>Classes</h3>
<p>class <code>NoSuchAttrException</code><br />
 <i>An exception indicating the requested attribute does not exist. </i><br />
 class <code>BaseObjectData</code><br />
 <i></i><code>Atlas</code> base object class.<br />
 class <code>ObjectsDecoder</code><br />
 <i></i><code>Objects</code> hierarchy decoder.<br />
 class <code>Dispatcher</code><br />
 <i></i><code>Objects</code> hierarchy dispatcher.<br />
 class <code>ObjectsEncoder</code><br />
 <i></i><code>Objects</code> hierarchy encoder.<br />
 class <code>DefaultLoadingException</code> </p>
<p> class <code>NoSuchFactoryException</code> </p>
<p> class <code>Factories</code> </p>
<p> class <code>RootData</code><br />
 <i>All objects inherit from this. </i><br />
 class <code>NullSmartPtrDereference</code> </p>
<p> class <code>SmartPtr</code> </p>
<h3>Typedefs</h3>
<p>typedef SmartPtr&lt; <code>RootData</code> &gt; <code>Root</code> </p>
<p> typedef Root(* <code>FactoryMethod</code> )(const std::string &amp;, int) </p>
<p> typedef std::map&lt; const std::string, std::pair&lt; FactoryMethod, int &gt; &gt; <code>FactoryMap</code> </p>
<h3>Functions</h3>
<p>void <code>loadDefaults</code> (const std::string &amp;filename) </p>
<p> SmartPtr&lt; <code>RootData</code> &gt; <code>generic_factory</code> (const std::string &amp;name, int no) </p>
<p> SmartPtr&lt; <code>RootData</code> &gt; <code>anonymous_factory</code> (const std::string &amp;name, int no) </p>
<p> template&lt;typename returnPtrType , class fromType &gt; returnPtrType <code>smart_dynamic_cast</code> (const SmartPtr&lt; fromType &gt; &amp;o) </p>
<p> template&lt;typename returnPtrType , class fromType &gt; returnPtrType <code>smart_static_cast</code> (const SmartPtr&lt; fromType &gt; &amp;o) </p>
<h3>Variables</h3>
<p>std::map&lt; const std::string, Root &gt; <code>objectDefinitions</code> </p>
<p> const std::string <code>ID_ATTR</code> </p>
<p> const std::string <code>PARENTS_ATTR</code> </p>
<p> const std::string <code>STAMP_ATTR</code> </p>
<p> const std::string <code>OBJTYPE_ATTR</code> </p>
<p> const std::string <code>NAME_ATTR</code> </p>
<p> const int <code>ID_FLAG</code> = 1 &lt;&lt; 1 </p>
<p> const int <code>PARENTS_FLAG</code> = 1 &lt;&lt; 2 </p>
<p> const int <code>STAMP_FLAG</code> = 1 &lt;&lt; 3 </p>
<p> const int <code>OBJTYPE_FLAG</code> = 1 &lt;&lt; 4 </p>
<p> const int <code>NAME_FLAG</code> = 1 &lt;&lt; 5 </p>
<h2>Detailed Description</h2>
<p>The <code>Atlas</code> high level <code>Objects</code> namespace. </p>
<p> This namespace contains classes used to handle high level <code>Atlas</code> data. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Atlas-C++ from the source code.</p>
