---
title: "atlas_objects_entity_adminentitydata(3)"
name: "atlas_objects_entity_adminentitydata"
section: "3"
letter: "a"
url: "/docs/linux/man/3-atlas_objects_entity_adminentitydata/"
description: "Atlas::Objects::Entity::AdminEntityData – All classes and objects used for adminitrativive purposes."
---

<p>Atlas::Objects::Entity::AdminEntityData &#8211; All classes and objects used for adminitrativive purposes. </p>
<h2>Synopsis</h2>
<p>#include &lt;<a href="file:/usr/include/Entity.h">Entity.h</a>&gt; </p>
<p> Inherits <code>Atlas::Objects::Entity::RootEntityData</code>. </p>
<p> Inherited by <code>Atlas::Objects::Entity::AccountData</code>, and <code>Atlas::Objects::Entity::GameData</code>. </p>
<h3>Public Member Functions</h3>
<p>virtual <code>AdminEntityData</code> * <code>copy</code> () const<br />
 <i>Copy this object. </i><br />
 virtual bool <code>instanceOf</code> (int classNo) const<br />
 <i>Is this instance of some class? </i><br />
 virtual void <code>iterate</code> (int &amp;current_class, std::string &amp;attr) const<br />
 <i>Iterate over the attributes of this instance. </i><br />
 virtual void <code>free</code> ()<br />
 <i>Free an instance of this class, returning it to the memory pool. </i><br />
 virtual <code>AdminEntityData</code> * <code>getDefaultObject</code> ()<br />
 <i>Get the reference object that contains the default values for attributes of instances of the same class as this object. </i></p>
<h3>Static Public Member Functions</h3>
<p>static <code>AdminEntityData</code> * <code>alloc</code> ()<br />
 <i>Allocate a new instance of this class, using an existing instance if available. </i><br />
 static <code>AdminEntityData</code> * <code>getDefaultObjectInstance</code> ()<br />
 <i>Get the reference object that contains the default values for attributes of instances of this class. </i></p>
<h3>Protected Member Functions</h3>
<p><code>AdminEntityData</code> (<code>AdminEntityData</code> *defaults=NULL)<br />
 <i>Construct a </i><code>AdminEntityData</code> class definition.<br />
 virtual <code>~AdminEntityData</code> ()<br />
 <i>Default destructor. </i></p>
<h2>Detailed Description</h2>
<p>All classes and objects used for adminitrativive purposes. </p>
<p> Later in hierarchy tree objtype changes to &#8216;object&#8217; when actual game objects are made.</p>
<h2>Member Function Documentation</h2>
<h3>static <code>AdminEntityData</code>* Atlas::Objects::Entity::AdminEntityData::alloc () [static]</h3>
<p>Allocate a new instance of this class, using an existing instance if available. </p>
<p> This is the key function for implementing the memory pool for the <code>Atlas::Objects</code> API. </p>
<p> Reimplemented from <code>Atlas::Objects::Entity::RootEntityData</code>. </p>
<p> Reimplemented in <code>Atlas::Objects::Entity::AccountData</code>, <code>Atlas::Objects::Entity::PlayerData</code>, <code>Atlas::Objects::Entity::AdminData</code>, and <code>Atlas::Objects::Entity::GameData</code>.</p>
<h3>virtual void Atlas::Objects::Entity::AdminEntityData::free () [virtual]</h3>
<p>Free an instance of this class, returning it to the memory pool. </p>
<p> This function in combination with <code>alloc()</code> handle the memory pool. </p>
<p> Reimplemented from <code>Atlas::Objects::Entity::RootEntityData</code>. </p>
<p> Reimplemented in <code>Atlas::Objects::Entity::AccountData</code>, <code>Atlas::Objects::Entity::PlayerData</code>, <code>Atlas::Objects::Entity::AdminData</code>, and <code>Atlas::Objects::Entity::GameData</code>.</p>
<h3>virtual <code>AdminEntityData</code>* Atlas::Objects::Entity::AdminEntityData::getDefaultObject () [virtual]</h3>
<p>Get the reference object that contains the default values for attributes of instances of the same class as this object. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>a pointer to the default object.</dl>
<p> Reimplemented from <code>Atlas::Objects::Entity::RootEntityData</code>. </p>
<p> Reimplemented in <code>Atlas::Objects::Entity::AccountData</code>, <code>Atlas::Objects::Entity::PlayerData</code>, <code>Atlas::Objects::Entity::AdminData</code>, and <code>Atlas::Objects::Entity::GameData</code>.</p>
<h3>static <code>AdminEntityData</code>* Atlas::Objects::Entity::AdminEntityData::getDefaultObjectInstance () [static]</h3>
<p>Get the reference object that contains the default values for attributes of instances of this class. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>a pointer to the default object.</dl>
<p> Reimplemented from <code>Atlas::Objects::Entity::RootEntityData</code>. </p>
<p> Reimplemented in <code>Atlas::Objects::Entity::AccountData</code>, <code>Atlas::Objects::Entity::PlayerData</code>, <code>Atlas::Objects::Entity::AdminData</code>, and <code>Atlas::Objects::Entity::GameData</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Atlas-C++ from the source code.</p>
