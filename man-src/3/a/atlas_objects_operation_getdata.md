---
title: "atlas_objects_operation_getdata(3)"
name: "atlas_objects_operation_getdata"
section: "3"
letter: "a"
url: "/docs/linux/man/3-atlas_objects_operation_getdata/"
description: "Atlas::Objects::Operation::GetData – Generic operation for getting info about things."
---

<p>Atlas::Objects::Operation::GetData &#8211; Generic operation for getting info about things. </p>
<h2>Synopsis</h2>
<p>#include &lt;<a href="file:/usr/include/Operation.h">Operation.h</a>&gt; </p>
<p> Inherits <code>Atlas::Objects::Operation::ActionData</code>. </p>
<p> Inherited by <code>Atlas::Objects::Operation::LoginData</code>, and <code>Atlas::Objects::Operation::PerceiveData</code>. </p>
<h3>Public Member Functions</h3>
<p>virtual <code>GetData</code> * <code>copy</code> () const<br />
 <i>Copy this object. </i><br />
 virtual bool <code>instanceOf</code> (int classNo) const<br />
 <i>Is this instance of some class? </i><br />
 virtual void <code>iterate</code> (int &amp;current_class, std::string &amp;attr) const<br />
 <i>Iterate over the attributes of this instance. </i><br />
 virtual void <code>free</code> ()<br />
 <i>Free an instance of this class, returning it to the memory pool. </i><br />
 virtual <code>GetData</code> * <code>getDefaultObject</code> ()<br />
 <i>Get the reference object that contains the default values for attributes of instances of the same class as this object. </i></p>
<h3>Static Public Member Functions</h3>
<p>static <code>GetData</code> * <code>alloc</code> ()<br />
 <i>Allocate a new instance of this class, using an existing instance if available. </i><br />
 static <code>GetData</code> * <code>getDefaultObjectInstance</code> ()<br />
 <i>Get the reference object that contains the default values for attributes of instances of this class. </i></p>
<h3>Protected Member Functions</h3>
<p><code>GetData</code> (<code>GetData</code> *defaults=NULL)<br />
 <i>Construct a </i><code>GetData</code> class definition.<br />
 virtual <code>~GetData</code> ()<br />
 <i>Default destructor. </i></p>
<h2>Detailed Description</h2>
<p>Generic operation for getting info about things. </p>
<h2>Member Function Documentation</h2>
<h3>static <code>GetData</code>* Atlas::Objects::Operation::GetData::alloc () [static]</h3>
<p>Allocate a new instance of this class, using an existing instance if available. </p>
<p> This is the key function for implementing the memory pool for the <code>Atlas::Objects</code> API. </p>
<p> Reimplemented from <code>Atlas::Objects::Operation::ActionData</code>. </p>
<p> Reimplemented in <code>Atlas::Objects::Operation::PerceiveData</code>, <code>Atlas::Objects::Operation::LookData</code>, <code>Atlas::Objects::Operation::ListenData</code>, <code>Atlas::Objects::Operation::SniffData</code>, <code>Atlas::Objects::Operation::TouchData</code>, <code>Atlas::Objects::Operation::LoginData</code>, and <code>Atlas::Objects::Operation::LogoutData</code>.</p>
<h3>virtual void Atlas::Objects::Operation::GetData::free () [virtual]</h3>
<p>Free an instance of this class, returning it to the memory pool. </p>
<p> This function in combination with <code>alloc()</code> handle the memory pool. </p>
<p> Reimplemented from <code>Atlas::Objects::Operation::ActionData</code>. </p>
<p> Reimplemented in <code>Atlas::Objects::Operation::PerceiveData</code>, <code>Atlas::Objects::Operation::LookData</code>, <code>Atlas::Objects::Operation::ListenData</code>, <code>Atlas::Objects::Operation::SniffData</code>, <code>Atlas::Objects::Operation::TouchData</code>, <code>Atlas::Objects::Operation::LoginData</code>, and <code>Atlas::Objects::Operation::LogoutData</code>.</p>
<h3>virtual <code>GetData</code>* Atlas::Objects::Operation::GetData::getDefaultObject () [virtual]</h3>
<p>Get the reference object that contains the default values for attributes of instances of the same class as this object. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>a pointer to the default object.</dl>
<p> Reimplemented from <code>Atlas::Objects::Operation::ActionData</code>. </p>
<p> Reimplemented in <code>Atlas::Objects::Operation::PerceiveData</code>, <code>Atlas::Objects::Operation::LookData</code>, <code>Atlas::Objects::Operation::ListenData</code>, <code>Atlas::Objects::Operation::SniffData</code>, <code>Atlas::Objects::Operation::TouchData</code>, <code>Atlas::Objects::Operation::LoginData</code>, and <code>Atlas::Objects::Operation::LogoutData</code>.</p>
<h3>static <code>GetData</code>* Atlas::Objects::Operation::GetData::getDefaultObjectInstance () [static]</h3>
<p>Get the reference object that contains the default values for attributes of instances of this class. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>a pointer to the default object.</dl>
<p> Reimplemented from <code>Atlas::Objects::Operation::ActionData</code>. </p>
<p> Reimplemented in <code>Atlas::Objects::Operation::PerceiveData</code>, <code>Atlas::Objects::Operation::LookData</code>, <code>Atlas::Objects::Operation::ListenData</code>, <code>Atlas::Objects::Operation::SniffData</code>, <code>Atlas::Objects::Operation::TouchData</code>, <code>Atlas::Objects::Operation::LoginData</code>, and <code>Atlas::Objects::Operation::LogoutData</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Atlas-C++ from the source code.</p>
