---
title: "atlas_objects_operation_deletedata(3)"
name: "atlas_objects_operation_deletedata"
section: "3"
letter: "a"
url: "/docs/linux/man/3-atlas_objects_operation_deletedata/"
description: "Atlas::Objects::Operation::DeleteData – Delete something."
---

<p>Atlas::Objects::Operation::DeleteData &#8211; Delete something. </p>
<h2>Synopsis</h2>
<p>#include &lt;<a href="file:/usr/include/Operation.h">Operation.h</a>&gt; </p>
<p> Inherits <code>Atlas::Objects::Operation::ActionData</code>. </p>
<h3>Public Member Functions</h3>
<p>virtual <code>DeleteData</code> * <code>copy</code> () const<br />
 <i>Copy this object. </i><br />
 virtual bool <code>instanceOf</code> (int classNo) const<br />
 <i>Is this instance of some class? </i><br />
 virtual void <code>iterate</code> (int &amp;current_class, std::string &amp;attr) const<br />
 <i>Iterate over the attributes of this instance. </i><br />
 virtual void <code>free</code> ()<br />
 <i>Free an instance of this class, returning it to the memory pool. </i><br />
 virtual <code>DeleteData</code> * <code>getDefaultObject</code> ()<br />
 <i>Get the reference object that contains the default values for attributes of instances of the same class as this object. </i></p>
<h3>Static Public Member Functions</h3>
<p>static <code>DeleteData</code> * <code>alloc</code> ()<br />
 <i>Allocate a new instance of this class, using an existing instance if available. </i><br />
 static <code>DeleteData</code> * <code>getDefaultObjectInstance</code> ()<br />
 <i>Get the reference object that contains the default values for attributes of instances of this class. </i></p>
<h3>Protected Member Functions</h3>
<p><code>DeleteData</code> (<code>DeleteData</code> *defaults=NULL)<br />
 <i>Construct a </i><code>DeleteData</code> class definition.<br />
 virtual <code>~DeleteData</code> ()<br />
 <i>Default destructor. </i></p>
<h2>Detailed Description</h2>
<p>Delete something. </p>
<h2>Member Function Documentation</h2>
<h3>static <code>DeleteData</code>* Atlas::Objects::Operation::DeleteData::alloc () [static]</h3>
<p>Allocate a new instance of this class, using an existing instance if available. </p>
<p> This is the key function for implementing the memory pool for the <code>Atlas::Objects</code> API. </p>
<p> Reimplemented from <code>Atlas::Objects::Operation::ActionData</code>.</p>
<h3>virtual void Atlas::Objects::Operation::DeleteData::free () [virtual]</h3>
<p>Free an instance of this class, returning it to the memory pool. </p>
<p> This function in combination with <code>alloc()</code> handle the memory pool. </p>
<p> Reimplemented from <code>Atlas::Objects::Operation::ActionData</code>.</p>
<h3>virtual <code>DeleteData</code>* Atlas::Objects::Operation::DeleteData::getDefaultObject () [virtual]</h3>
<p>Get the reference object that contains the default values for attributes of instances of the same class as this object. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>a pointer to the default object.</dl>
<p> Reimplemented from <code>Atlas::Objects::Operation::ActionData</code>.</p>
<h3>static <code>DeleteData</code>* Atlas::Objects::Operation::DeleteData::getDefaultObjectInstance () [static]</h3>
<p>Get the reference object that contains the default values for attributes of instances of this class. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>a pointer to the default object.</dl>
<p> Reimplemented from <code>Atlas::Objects::Operation::ActionData</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Atlas-C++ from the source code.</p>
