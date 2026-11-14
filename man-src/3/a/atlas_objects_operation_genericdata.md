---
title: "atlas_objects_operation_genericdata(3)"
name: "atlas_objects_operation_genericdata"
section: "3"
letter: "a"
url: "/docs/linux/man/3-atlas_objects_operation_genericdata/"
description: "Atlas::Objects::Operation::GenericData – Base operation for all operators."
---

<p>Atlas::Objects::Operation::GenericData &#8211; Base operation for all operators. </p>
<h2>Synopsis</h2>
<p>#include &lt;<a href="file:/usr/include/Generic.h">Generic.h</a>&gt; </p>
<p> Inherits <code>Atlas::Objects::Operation::RootOperationData</code>. </p>
<h3>Public Member Functions</h3>
<p>void <code>setType</code> (const std::string &amp;, int)<br />
 <i>Set the type of this object. </i><br />
 virtual <code>GenericData</code> * <code>copy</code> () const<br />
 <i>Copy this object. </i><br />
 virtual bool <code>instanceOf</code> (int classNo) const<br />
 <i>Is this instance of some class? </i><br />
 virtual void <code>iterate</code> (int &amp;current_class, std::string &amp;attr) const<br />
 <i>Iterate over the attributes of this instance. </i><br />
 virtual void <code>free</code> ()<br />
 <i>Free an instance of this class, returning it to the memory pool. </i><br />
 virtual <code>GenericData</code> * <code>getDefaultObject</code> ()<br />
 <i>Get the reference object that contains the default values for attributes of instances of the same class as this object. </i></p>
<h3>Static Public Member Functions</h3>
<p>static <code>GenericData</code> * <code>alloc</code> ()<br />
 <i>Allocate a new instance of this class, using an existing instance if available. </i><br />
 static <code>GenericData</code> * <code>getDefaultObjectInstance</code> ()<br />
 <i>Get the reference object that contains the default values for attributes of instances of this class. </i></p>
<h3>Protected Member Functions</h3>
<p><code>GenericData</code> (<code>GenericData</code> *defaults=NULL)<br />
 <i>Construct a </i><code>GenericData</code> class definition.<br />
 virtual <code>~GenericData</code> ()<br />
 <i>Default destructor. </i></p>
<h2>Detailed Description</h2>
<p>Base operation for all operators. </p>
<p> This is base operation for all other operations and defines basic attributes. You can use this as starting point for browsing whole operation hiearchy. refno refers to operation this is reply for. In examples all attributes that are just as examples (and thus world specific) are started with &#8216;e_&#8217;.</p>
<h2>Member Function Documentation</h2>
<h3>static <code>GenericData</code>* Atlas::Objects::Operation::GenericData::alloc () [static]</h3>
<p>Allocate a new instance of this class, using an existing instance if available. </p>
<p> This is the key function for implementing the memory pool for the <code>Atlas::Objects</code> API. </p>
<p> Reimplemented from <code>Atlas::Objects::Operation::RootOperationData</code>.</p>
<h3>virtual void Atlas::Objects::Operation::GenericData::free () [virtual]</h3>
<p>Free an instance of this class, returning it to the memory pool. </p>
<p> This function in combination with <code>alloc()</code> handle the memory pool. </p>
<p> Reimplemented from <code>Atlas::Objects::Operation::RootOperationData</code>.</p>
<h3>virtual <code>GenericData</code>* Atlas::Objects::Operation::GenericData::getDefaultObject () [virtual]</h3>
<p>Get the reference object that contains the default values for attributes of instances of the same class as this object. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>a pointer to the default object.</dl>
<p> Reimplemented from <code>Atlas::Objects::Operation::RootOperationData</code>.</p>
<h3>static <code>GenericData</code>* Atlas::Objects::Operation::GenericData::getDefaultObjectInstance () [static]</h3>
<p>Get the reference object that contains the default values for attributes of instances of this class. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>a pointer to the default object.</dl>
<p> Reimplemented from <code>Atlas::Objects::Operation::RootOperationData</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Atlas-C++ from the source code.</p>
