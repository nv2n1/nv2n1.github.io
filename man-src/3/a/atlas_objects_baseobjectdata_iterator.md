---
title: "atlas_objects_baseobjectdata_iterator(3)"
name: "atlas_objects_baseobjectdata_iterator"
section: "3"
letter: "a"
url: "/docs/linux/man/3-atlas_objects_baseobjectdata_iterator/"
description: "Atlas::Objects::BaseObjectData::iterator – The iterator first iterates over the contents of m_obj->m_attributes, holding an iterator to the attributes map in m_I."
---

<p>Atlas::Objects::BaseObjectData::iterator &#8211; The <code>iterator</code> first iterates over the contents of m_obj-&gt;m_attributes, holding an <code>iterator</code> to the attributes map in m_I. </p>
<h2>Synopsis</h2>
<p>#include &lt;<a href="file:/usr/include/BaseObject.h">BaseObject.h</a>&gt; </p>
<h3>Classes</h3>
<p>class <code>PsuedoElement</code> </p>
<h3>Public Types</h3>
<p>typedef std::pair&lt; std::string, PsuedoElement &gt; <code>value_type</code> </p>
<h3>Public Member Functions</h3>
<p><code>iterator</code> (const <code>iterator</code> &amp;I) </p>
<p> <code>iterator</code> (<code>BaseObjectData</code> &amp;obj, int current_class) </p>
<p> <code>iterator</code> &amp; <code>operator=</code> (const <code>iterator</code> &amp;I) </p>
<p> <code>iterator</code> &amp; <code>operator++</code> () </p>
<p> <code>iterator</code> <code>operator++</code> (int) </p>
<p> bool <code>operator==</code> (const <code>iterator</code> &amp;I) const </p>
<p> bool <code>operator!=</code> (const <code>iterator</code> &amp;I) const </p>
<p> const value_type &amp; <code>operator*</code> () const </p>
<p> const value_type * <code>operator-&gt;</code> () const </p>
<h3>Friends</h3>
<p>class <code>BaseObjectData</code> </p>
<p> class <code>const_iterator</code> </p>
<p> class <code>PsuedoElement</code> </p>
<h2>Detailed Description</h2>
<p>The <code>iterator</code> first iterates over the contents of m_obj-&gt;m_attributes, holding an <code>iterator</code> to the attributes map in m_I. </p>
<p> When m_I reaches the end, it iterates through the named attributes in each of the classes, starting with the terminal child and working its way up to the ultimate parent, <code>BaseObjectData</code>. It stores the class number in m_current_class and the name of the current attribute in m_val.first. Since <code>BaseObjectData</code> has no named attributes, an <code>iterator</code> with m_current_class == BASE_OBJECT_NO is considered to be the end of the map. The <code>iterator</code> constructor has an argument which lets you begin() at the first named attribute in some class, and only iterate through that class and its parents. The same <code>iterator</code>, treated as an end(), lets you iterate through all attributes which are either named in derived classes or in m_attributes. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Atlas-C++ from the source code.</p>
