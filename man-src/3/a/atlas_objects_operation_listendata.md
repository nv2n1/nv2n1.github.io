---
title: "atlas_objects_operation_listendata(3)"
name: "atlas_objects_operation_listendata"
section: "3"
letter: "a"
url: "/docs/linux/man/3-atlas_objects_operation_listendata/"
description: "Atlas::Objects::Operation::ListenData – Listen (something)."
---

<p>Atlas::Objects::Operation::ListenData &#8211; Listen (something). </p>
<h2>Synopsis</h2>
<p>#include &lt;<a href="file:/usr/include/Operation.h">Operation.h</a>&gt; </p>
<p> Inherits <code>Atlas::Objects::Operation::PerceiveData</code>. </p>
<h3>Public Member Functions</h3>
<p>virtual <code>ListenData</code> * <code>copy</code> () const<br />
 <i>Copy this object. </i><br />
 virtual bool <code>instanceOf</code> (int classNo) const<br />
 <i>Is this instance of some class? </i><br />
 virtual void <code>iterate</code> (int &amp;current_class, std::string &amp;attr) const<br />
 <i>Iterate over the attributes of this instance. </i><br />
 virtual void <code>free</code> ()<br />
 <i>Free an instance of this class, returning it to the memory pool. </i><br />
 virtual <code>ListenData</code> * <code>getDefaultObject</code> ()<br />
 <i>Get the reference object that contains the default values for attributes of instances of the same class as this object. </i></p>
<h3>Static Public Member Functions</h3>
<p>static <code>ListenData</code> * <code>alloc</code> ()<br />
 <i>Allocate a new instance of this class, using an existing instance if available. </i><br />
 static <code>ListenData</code> * <code>getDefaultObjectInstance</code> ()<br />
 <i>Get the reference object that contains the default values for attributes of instances of this class. </i></p>
<h3>Protected Member Functions</h3>
<p><code>ListenData</code> (<code>ListenData</code> *defaults=NULL)<br />
 <i>Construct a </i><code>ListenData</code> class definition.<br />
 virtual <code>~ListenData</code> ()<br />
 <i>Default destructor. </i></p>
<h2>Detailed Description</h2>
<p>Listen (something). </p>
<p> This is base operation for all other operations and defines basic attributes. You can use this as starting point for browsing whole operation hiearchy. refno refers to operation this is reply for. In examples all attributes that are just as examples (and thus world specific) are started with &#8216;e_&#8217;.</p>
<h2>Member Function Documentation</h2>
<h3>static <code>ListenData</code>* Atlas::Objects::Operation::ListenData::alloc () [static]</h3>
<p>Allocate a new instance of this class, using an existing instance if available. </p>
<p> This is the key function for implementing the memory pool for the <code>Atlas::Objects</code> API. </p>
<p> Reimplemented from <code>Atlas::Objects::Operation::PerceiveData</code>.</p>
<h3>virtual void Atlas::Objects::Operation::ListenData::free () [virtual]</h3>
<p>Free an instance of this class, returning it to the memory pool. </p>
<p> This function in combination with <code>alloc()</code> handle the memory pool. </p>
<p> Reimplemented from <code>Atlas::Objects::Operation::PerceiveData</code>.</p>
<h3>virtual <code>ListenData</code>* Atlas::Objects::Operation::ListenData::getDefaultObject () [virtual]</h3>
<p>Get the reference object that contains the default values for attributes of instances of the same class as this object. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>a pointer to the default object.</dl>
<p> Reimplemented from <code>Atlas::Objects::Operation::PerceiveData</code>.</p>
<h3>static <code>ListenData</code>* Atlas::Objects::Operation::ListenData::getDefaultObjectInstance () [static]</h3>
<p>Get the reference object that contains the default values for attributes of instances of this class. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>a pointer to the default object.</dl>
<p> Reimplemented from <code>Atlas::Objects::Operation::PerceiveData</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Atlas-C++ from the source code.</p>
