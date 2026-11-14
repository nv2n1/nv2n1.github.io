---
title: "atlas_objects_operation_actiondata(3)"
name: "atlas_objects_operation_actiondata"
section: "3"
letter: "a"
url: "/docs/linux/man/3-atlas_objects_operation_actiondata/"
description: "Atlas::Objects::Operation::ActionData – This is base operator for operations that might have effects."
---

<p>Atlas::Objects::Operation::ActionData &#8211; This is base operator for operations that might have effects. </p>
<h2>Synopsis</h2>
<p>#include &lt;<a href="file:/usr/include/Operation.h">Operation.h</a>&gt; </p>
<p> Inherits <code>Atlas::Objects::Operation::RootOperationData</code>. </p>
<p> Inherited by <code>Atlas::Objects::Operation::CreateData</code>, <code>Atlas::Objects::Operation::DeleteData</code>, <code>Atlas::Objects::Operation::GetData</code>, <code>Atlas::Objects::Operation::ImaginaryData</code>, <code>Atlas::Objects::Operation::SetData</code>, and <code>Atlas::Objects::Operation::UseData</code>. </p>
<h3>Public Member Functions</h3>
<p>virtual <code>ActionData</code> * <code>copy</code> () const<br />
 <i>Copy this object. </i><br />
 virtual bool <code>instanceOf</code> (int classNo) const<br />
 <i>Is this instance of some class? </i><br />
 virtual void <code>iterate</code> (int &amp;current_class, std::string &amp;attr) const<br />
 <i>Iterate over the attributes of this instance. </i><br />
 virtual void <code>free</code> ()<br />
 <i>Free an instance of this class, returning it to the memory pool. </i><br />
 virtual <code>ActionData</code> * <code>getDefaultObject</code> ()<br />
 <i>Get the reference object that contains the default values for attributes of instances of the same class as this object. </i></p>
<h3>Static Public Member Functions</h3>
<p>static <code>ActionData</code> * <code>alloc</code> ()<br />
 <i>Allocate a new instance of this class, using an existing instance if available. </i><br />
 static <code>ActionData</code> * <code>getDefaultObjectInstance</code> ()<br />
 <i>Get the reference object that contains the default values for attributes of instances of this class. </i></p>
<h3>Protected Member Functions</h3>
<p><code>ActionData</code> (<code>ActionData</code> *defaults=NULL)<br />
 <i>Construct a </i><code>ActionData</code> class definition.<br />
 virtual <code>~ActionData</code> ()<br />
 <i>Default destructor. </i></p>
<h2>Detailed Description</h2>
<p>This is base operator for operations that might have effects. </p>
<h2>Member Function Documentation</h2>
<h3>static <code>ActionData</code>* Atlas::Objects::Operation::ActionData::alloc () [static]</h3>
<p>Allocate a new instance of this class, using an existing instance if available. </p>
<p> This is the key function for implementing the memory pool for the <code>Atlas::Objects</code> API. </p>
<p> Reimplemented from <code>Atlas::Objects::Operation::RootOperationData</code>. </p>
<p> Reimplemented in <code>Atlas::Objects::Operation::CreateData</code>, <code>Atlas::Objects::Operation::CombineData</code>, <code>Atlas::Objects::Operation::DivideData</code>, <code>Atlas::Objects::Operation::CommunicateData</code>, <code>Atlas::Objects::Operation::TalkData</code>, <code>Atlas::Objects::Operation::DeleteData</code>, <code>Atlas::Objects::Operation::SetData</code>, <code>Atlas::Objects::Operation::AffectData</code>, <code>Atlas::Objects::Operation::MoveData</code>, <code>Atlas::Objects::Operation::WieldData</code>, <code>Atlas::Objects::Operation::GetData</code>, <code>Atlas::Objects::Operation::PerceiveData</code>, <code>Atlas::Objects::Operation::LookData</code>, <code>Atlas::Objects::Operation::ListenData</code>, <code>Atlas::Objects::Operation::SniffData</code>, <code>Atlas::Objects::Operation::TouchData</code>, <code>Atlas::Objects::Operation::LoginData</code>, <code>Atlas::Objects::Operation::LogoutData</code>, <code>Atlas::Objects::Operation::ImaginaryData</code>, and <code>Atlas::Objects::Operation::UseData</code>.</p>
<h3>virtual void Atlas::Objects::Operation::ActionData::free () [virtual]</h3>
<p>Free an instance of this class, returning it to the memory pool. </p>
<p> This function in combination with <code>alloc()</code> handle the memory pool. </p>
<p> Reimplemented from <code>Atlas::Objects::Operation::RootOperationData</code>. </p>
<p> Reimplemented in <code>Atlas::Objects::Operation::CreateData</code>, <code>Atlas::Objects::Operation::CombineData</code>, <code>Atlas::Objects::Operation::DivideData</code>, <code>Atlas::Objects::Operation::CommunicateData</code>, <code>Atlas::Objects::Operation::TalkData</code>, <code>Atlas::Objects::Operation::DeleteData</code>, <code>Atlas::Objects::Operation::SetData</code>, <code>Atlas::Objects::Operation::AffectData</code>, <code>Atlas::Objects::Operation::MoveData</code>, <code>Atlas::Objects::Operation::WieldData</code>, <code>Atlas::Objects::Operation::GetData</code>, <code>Atlas::Objects::Operation::PerceiveData</code>, <code>Atlas::Objects::Operation::LookData</code>, <code>Atlas::Objects::Operation::ListenData</code>, <code>Atlas::Objects::Operation::SniffData</code>, <code>Atlas::Objects::Operation::TouchData</code>, <code>Atlas::Objects::Operation::LoginData</code>, <code>Atlas::Objects::Operation::LogoutData</code>, <code>Atlas::Objects::Operation::ImaginaryData</code>, and <code>Atlas::Objects::Operation::UseData</code>.</p>
<h3>virtual <code>ActionData</code>* Atlas::Objects::Operation::ActionData::getDefaultObject () [virtual]</h3>
<p>Get the reference object that contains the default values for attributes of instances of the same class as this object. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>a pointer to the default object.</dl>
<p> Reimplemented from <code>Atlas::Objects::Operation::RootOperationData</code>. </p>
<p> Reimplemented in <code>Atlas::Objects::Operation::CreateData</code>, <code>Atlas::Objects::Operation::CombineData</code>, <code>Atlas::Objects::Operation::DivideData</code>, <code>Atlas::Objects::Operation::CommunicateData</code>, <code>Atlas::Objects::Operation::TalkData</code>, <code>Atlas::Objects::Operation::DeleteData</code>, <code>Atlas::Objects::Operation::SetData</code>, <code>Atlas::Objects::Operation::AffectData</code>, <code>Atlas::Objects::Operation::MoveData</code>, <code>Atlas::Objects::Operation::WieldData</code>, <code>Atlas::Objects::Operation::GetData</code>, <code>Atlas::Objects::Operation::PerceiveData</code>, <code>Atlas::Objects::Operation::LookData</code>, <code>Atlas::Objects::Operation::ListenData</code>, <code>Atlas::Objects::Operation::SniffData</code>, <code>Atlas::Objects::Operation::TouchData</code>, <code>Atlas::Objects::Operation::LoginData</code>, <code>Atlas::Objects::Operation::LogoutData</code>, <code>Atlas::Objects::Operation::ImaginaryData</code>, and <code>Atlas::Objects::Operation::UseData</code>.</p>
<h3>static <code>ActionData</code>* Atlas::Objects::Operation::ActionData::getDefaultObjectInstance () [static]</h3>
<p>Get the reference object that contains the default values for attributes of instances of this class. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>a pointer to the default object.</dl>
<p> Reimplemented from <code>Atlas::Objects::Operation::RootOperationData</code>. </p>
<p> Reimplemented in <code>Atlas::Objects::Operation::CreateData</code>, <code>Atlas::Objects::Operation::CombineData</code>, <code>Atlas::Objects::Operation::DivideData</code>, <code>Atlas::Objects::Operation::CommunicateData</code>, <code>Atlas::Objects::Operation::TalkData</code>, <code>Atlas::Objects::Operation::DeleteData</code>, <code>Atlas::Objects::Operation::SetData</code>, <code>Atlas::Objects::Operation::AffectData</code>, <code>Atlas::Objects::Operation::MoveData</code>, <code>Atlas::Objects::Operation::WieldData</code>, <code>Atlas::Objects::Operation::GetData</code>, <code>Atlas::Objects::Operation::PerceiveData</code>, <code>Atlas::Objects::Operation::LookData</code>, <code>Atlas::Objects::Operation::ListenData</code>, <code>Atlas::Objects::Operation::SniffData</code>, <code>Atlas::Objects::Operation::TouchData</code>, <code>Atlas::Objects::Operation::LoginData</code>, <code>Atlas::Objects::Operation::LogoutData</code>, <code>Atlas::Objects::Operation::ImaginaryData</code>, and <code>Atlas::Objects::Operation::UseData</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Atlas-C++ from the source code.</p>
