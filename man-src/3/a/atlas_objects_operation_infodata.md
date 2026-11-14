---
title: "atlas_objects_operation_infodata(3)"
name: "atlas_objects_operation_infodata"
section: "3"
letter: "a"
url: "/docs/linux/man/3-atlas_objects_operation_infodata/"
description: "Atlas::Objects::Operation::InfoData – This is base operator for operations that tell you info about objects or events."
---

<p>Atlas::Objects::Operation::InfoData &#8211; This is base operator for operations that tell you info about objects or events. </p>
<h2>Synopsis</h2>
<p>#include &lt;<a href="file:/usr/include/Operation.h">Operation.h</a>&gt; </p>
<p> Inherits <code>Atlas::Objects::Operation::RootOperationData</code>. </p>
<p> Inherited by <code>Atlas::Objects::Operation::ErrorData</code>, and <code>Atlas::Objects::Operation::PerceptionData</code>. </p>
<h3>Public Member Functions</h3>
<p>virtual <code>InfoData</code> * <code>copy</code> () const<br />
 <i>Copy this object. </i><br />
 virtual bool <code>instanceOf</code> (int classNo) const<br />
 <i>Is this instance of some class? </i><br />
 virtual void <code>iterate</code> (int &amp;current_class, std::string &amp;attr) const<br />
 <i>Iterate over the attributes of this instance. </i><br />
 virtual void <code>free</code> ()<br />
 <i>Free an instance of this class, returning it to the memory pool. </i><br />
 virtual <code>InfoData</code> * <code>getDefaultObject</code> ()<br />
 <i>Get the reference object that contains the default values for attributes of instances of the same class as this object. </i></p>
<h3>Static Public Member Functions</h3>
<p>static <code>InfoData</code> * <code>alloc</code> ()<br />
 <i>Allocate a new instance of this class, using an existing instance if available. </i><br />
 static <code>InfoData</code> * <code>getDefaultObjectInstance</code> ()<br />
 <i>Get the reference object that contains the default values for attributes of instances of this class. </i></p>
<h3>Protected Member Functions</h3>
<p><code>InfoData</code> (<code>InfoData</code> *defaults=NULL)<br />
 <i>Construct a </i><code>InfoData</code> class definition.<br />
 virtual <code>~InfoData</code> ()<br />
 <i>Default destructor. </i></p>
<h2>Detailed Description</h2>
<p>This is base operator for operations that tell you info about objects or events. </p>
<h2>Member Function Documentation</h2>
<h3>static <code>InfoData</code>* Atlas::Objects::Operation::InfoData::alloc () [static]</h3>
<p>Allocate a new instance of this class, using an existing instance if available. </p>
<p> This is the key function for implementing the memory pool for the <code>Atlas::Objects</code> API. </p>
<p> Reimplemented from <code>Atlas::Objects::Operation::RootOperationData</code>. </p>
<p> Reimplemented in <code>Atlas::Objects::Operation::PerceptionData</code>, <code>Atlas::Objects::Operation::SightData</code>, <code>Atlas::Objects::Operation::AppearanceData</code>, <code>Atlas::Objects::Operation::DisappearanceData</code>, <code>Atlas::Objects::Operation::SoundData</code>, <code>Atlas::Objects::Operation::SmellData</code>, <code>Atlas::Objects::Operation::FeelData</code>, and <code>Atlas::Objects::Operation::ErrorData</code>.</p>
<h3>virtual void Atlas::Objects::Operation::InfoData::free () [virtual]</h3>
<p>Free an instance of this class, returning it to the memory pool. </p>
<p> This function in combination with <code>alloc()</code> handle the memory pool. </p>
<p> Reimplemented from <code>Atlas::Objects::Operation::RootOperationData</code>. </p>
<p> Reimplemented in <code>Atlas::Objects::Operation::PerceptionData</code>, <code>Atlas::Objects::Operation::SightData</code>, <code>Atlas::Objects::Operation::AppearanceData</code>, <code>Atlas::Objects::Operation::DisappearanceData</code>, <code>Atlas::Objects::Operation::SoundData</code>, <code>Atlas::Objects::Operation::SmellData</code>, <code>Atlas::Objects::Operation::FeelData</code>, and <code>Atlas::Objects::Operation::ErrorData</code>.</p>
<h3>virtual <code>InfoData</code>* Atlas::Objects::Operation::InfoData::getDefaultObject () [virtual]</h3>
<p>Get the reference object that contains the default values for attributes of instances of the same class as this object. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>a pointer to the default object.</dl>
<p> Reimplemented from <code>Atlas::Objects::Operation::RootOperationData</code>. </p>
<p> Reimplemented in <code>Atlas::Objects::Operation::PerceptionData</code>, <code>Atlas::Objects::Operation::SightData</code>, <code>Atlas::Objects::Operation::AppearanceData</code>, <code>Atlas::Objects::Operation::DisappearanceData</code>, <code>Atlas::Objects::Operation::SoundData</code>, <code>Atlas::Objects::Operation::SmellData</code>, <code>Atlas::Objects::Operation::FeelData</code>, and <code>Atlas::Objects::Operation::ErrorData</code>.</p>
<h3>static <code>InfoData</code>* Atlas::Objects::Operation::InfoData::getDefaultObjectInstance () [static]</h3>
<p>Get the reference object that contains the default values for attributes of instances of this class. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>a pointer to the default object.</dl>
<p> Reimplemented from <code>Atlas::Objects::Operation::RootOperationData</code>. </p>
<p> Reimplemented in <code>Atlas::Objects::Operation::PerceptionData</code>, <code>Atlas::Objects::Operation::SightData</code>, <code>Atlas::Objects::Operation::AppearanceData</code>, <code>Atlas::Objects::Operation::DisappearanceData</code>, <code>Atlas::Objects::Operation::SoundData</code>, <code>Atlas::Objects::Operation::SmellData</code>, <code>Atlas::Objects::Operation::FeelData</code>, and <code>Atlas::Objects::Operation::ErrorData</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Atlas-C++ from the source code.</p>
