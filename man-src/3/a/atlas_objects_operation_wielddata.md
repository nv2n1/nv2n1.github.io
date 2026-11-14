---
title: "atlas_objects_operation_wielddata(3)"
name: "atlas_objects_operation_wielddata"
section: "3"
letter: "a"
url: "/docs/linux/man/3-atlas_objects_operation_wielddata/"
description: "Atlas::Objects::Operation::WieldData – Attach a tool to the character entity at a pre-defined location so that the character can use it."
---

<p>Atlas::Objects::Operation::WieldData &#8211; Attach a tool to the character entity at a pre-defined location so that the character can use it. </p>
<h2>Synopsis</h2>
<p>#include &lt;<a href="file:/usr/include/Operation.h">Operation.h</a>&gt; </p>
<p> Inherits <code>Atlas::Objects::Operation::SetData</code>. </p>
<h3>Public Member Functions</h3>
<p>virtual <code>WieldData</code> * <code>copy</code> () const<br />
 <i>Copy this object. </i><br />
 virtual bool <code>instanceOf</code> (int classNo) const<br />
 <i>Is this instance of some class? </i><br />
 virtual void <code>iterate</code> (int &amp;current_class, std::string &amp;attr) const<br />
 <i>Iterate over the attributes of this instance. </i><br />
 virtual void <code>free</code> ()<br />
 <i>Free an instance of this class, returning it to the memory pool. </i><br />
 virtual <code>WieldData</code> * <code>getDefaultObject</code> ()<br />
 <i>Get the reference object that contains the default values for attributes of instances of the same class as this object. </i></p>
<h3>Static Public Member Functions</h3>
<p>static <code>WieldData</code> * <code>alloc</code> ()<br />
 <i>Allocate a new instance of this class, using an existing instance if available. </i><br />
 static <code>WieldData</code> * <code>getDefaultObjectInstance</code> ()<br />
 <i>Get the reference object that contains the default values for attributes of instances of this class. </i></p>
<h3>Protected Member Functions</h3>
<p><code>WieldData</code> (<code>WieldData</code> *defaults=NULL)<br />
 <i>Construct a </i><code>WieldData</code> class definition.<br />
 virtual <code>~WieldData</code> ()<br />
 <i>Default destructor. </i></p>
<h2>Detailed Description</h2>
<p>Attach a tool to the character entity at a pre-defined location so that the character can use it. </p>
<h2>Member Function Documentation</h2>
<h3>static <code>WieldData</code>* Atlas::Objects::Operation::WieldData::alloc () [static]</h3>
<p>Allocate a new instance of this class, using an existing instance if available. </p>
<p> This is the key function for implementing the memory pool for the <code>Atlas::Objects</code> API. </p>
<p> Reimplemented from <code>Atlas::Objects::Operation::SetData</code>.</p>
<h3>virtual void Atlas::Objects::Operation::WieldData::free () [virtual]</h3>
<p>Free an instance of this class, returning it to the memory pool. </p>
<p> This function in combination with <code>alloc()</code> handle the memory pool. </p>
<p> Reimplemented from <code>Atlas::Objects::Operation::SetData</code>.</p>
<h3>virtual <code>WieldData</code>* Atlas::Objects::Operation::WieldData::getDefaultObject () [virtual]</h3>
<p>Get the reference object that contains the default values for attributes of instances of the same class as this object. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>a pointer to the default object.</dl>
<p> Reimplemented from <code>Atlas::Objects::Operation::SetData</code>.</p>
<h3>static <code>WieldData</code>* Atlas::Objects::Operation::WieldData::getDefaultObjectInstance () [static]</h3>
<p>Get the reference object that contains the default values for attributes of instances of this class. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>a pointer to the default object.</dl>
<p> Reimplemented from <code>Atlas::Objects::Operation::SetData</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Atlas-C++ from the source code.</p>
