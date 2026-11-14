---
title: "atlas_objects_operation_setdata(3)"
name: "atlas_objects_operation_setdata"
section: "3"
letter: "a"
url: "/docs/linux/man/3-atlas_objects_operation_setdata/"
description: "Atlas::Objects::Operation::SetData – Sets attributes for existing entity."
---

<p>Atlas::Objects::Operation::SetData &#8211; Sets attributes for existing entity. </p>
<h2>Synopsis</h2>
<p>#include &lt;<a href="file:/usr/include/Operation.h">Operation.h</a>&gt; </p>
<p> Inherits <code>Atlas::Objects::Operation::ActionData</code>. </p>
<p> Inherited by <code>Atlas::Objects::Operation::AffectData</code>, <code>Atlas::Objects::Operation::MoveData</code>, and <code>Atlas::Objects::Operation::WieldData</code>. </p>
<h3>Public Member Functions</h3>
<p>virtual <code>SetData</code> * <code>copy</code> () const<br />
 <i>Copy this object. </i><br />
 virtual bool <code>instanceOf</code> (int classNo) const<br />
 <i>Is this instance of some class? </i><br />
 virtual void <code>iterate</code> (int &amp;current_class, std::string &amp;attr) const<br />
 <i>Iterate over the attributes of this instance. </i><br />
 virtual void <code>free</code> ()<br />
 <i>Free an instance of this class, returning it to the memory pool. </i><br />
 virtual <code>SetData</code> * <code>getDefaultObject</code> ()<br />
 <i>Get the reference object that contains the default values for attributes of instances of the same class as this object. </i></p>
<h3>Static Public Member Functions</h3>
<p>static <code>SetData</code> * <code>alloc</code> ()<br />
 <i>Allocate a new instance of this class, using an existing instance if available. </i><br />
 static <code>SetData</code> * <code>getDefaultObjectInstance</code> ()<br />
 <i>Get the reference object that contains the default values for attributes of instances of this class. </i></p>
<h3>Protected Member Functions</h3>
<p><code>SetData</code> (<code>SetData</code> *defaults=NULL)<br />
 <i>Construct a </i><code>SetData</code> class definition.<br />
 virtual <code>~SetData</code> ()<br />
 <i>Default destructor. </i></p>
<h2>Detailed Description</h2>
<p>Sets attributes for existing entity. </p>
<h2>Member Function Documentation</h2>
<h3>static <code>SetData</code>* Atlas::Objects::Operation::SetData::alloc () [static]</h3>
<p>Allocate a new instance of this class, using an existing instance if available. </p>
<p> This is the key function for implementing the memory pool for the <code>Atlas::Objects</code> API. </p>
<p> Reimplemented from <code>Atlas::Objects::Operation::ActionData</code>. </p>
<p> Reimplemented in <code>Atlas::Objects::Operation::AffectData</code>, <code>Atlas::Objects::Operation::MoveData</code>, and <code>Atlas::Objects::Operation::WieldData</code>.</p>
<h3>virtual void Atlas::Objects::Operation::SetData::free () [virtual]</h3>
<p>Free an instance of this class, returning it to the memory pool. </p>
<p> This function in combination with <code>alloc()</code> handle the memory pool. </p>
<p> Reimplemented from <code>Atlas::Objects::Operation::ActionData</code>. </p>
<p> Reimplemented in <code>Atlas::Objects::Operation::AffectData</code>, <code>Atlas::Objects::Operation::MoveData</code>, and <code>Atlas::Objects::Operation::WieldData</code>.</p>
<h3>virtual <code>SetData</code>* Atlas::Objects::Operation::SetData::getDefaultObject () [virtual]</h3>
<p>Get the reference object that contains the default values for attributes of instances of the same class as this object. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>a pointer to the default object.</dl>
<p> Reimplemented from <code>Atlas::Objects::Operation::ActionData</code>. </p>
<p> Reimplemented in <code>Atlas::Objects::Operation::AffectData</code>, <code>Atlas::Objects::Operation::MoveData</code>, and <code>Atlas::Objects::Operation::WieldData</code>.</p>
<h3>static <code>SetData</code>* Atlas::Objects::Operation::SetData::getDefaultObjectInstance () [static]</h3>
<p>Get the reference object that contains the default values for attributes of instances of this class. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>a pointer to the default object.</dl>
<p> Reimplemented from <code>Atlas::Objects::Operation::ActionData</code>. </p>
<p> Reimplemented in <code>Atlas::Objects::Operation::AffectData</code>, <code>Atlas::Objects::Operation::MoveData</code>, and <code>Atlas::Objects::Operation::WieldData</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Atlas-C++ from the source code.</p>
