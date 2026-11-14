---
title: "atlas_objects_entity_rootentitydata(3)"
name: "atlas_objects_entity_rootentitydata"
section: "3"
letter: "a"
url: "/docs/linux/man/3-atlas_objects_entity_rootentitydata/"
description: "Atlas::Objects::Entity::RootEntityData – Starting point for entity hierarchy."
---

<p>Atlas::Objects::Entity::RootEntityData &#8211; Starting point for entity hierarchy. </p>
<h2>Synopsis</h2>
<p>#include &lt;<a href="file:/usr/include/RootEntity.h">RootEntity.h</a>&gt; </p>
<p> Inherits <code>Atlas::Objects::RootData</code>. </p>
<p> Inherited by <code>Atlas::Objects::Entity::AdminEntityData</code>, <code>Atlas::Objects::Entity::AnonymousData</code>, and <code>Atlas::Objects::Entity::GameEntityData</code>. </p>
<h3>Public Member Functions</h3>
<p>virtual <code>RootEntityData</code> * <code>copy</code> () const<br />
 <i>Copy this object. </i><br />
 virtual bool <code>instanceOf</code> (int classNo) const<br />
 <i>Is this instance of some class? </i><br />
 virtual int <code>copyAttr</code> (const std::string &amp;name, <code>Atlas::Message::Element</code> &amp;attr) const<br />
 <i>Retrieve the attribute &#8216;name&#8217;. </i><br />
 virtual void <code>setAttr</code> (const std::string &amp;name, const <code>Atlas::Message::Element</code> &amp;attr)<br />
 <i>Set the attribute &#8216;name&#8217; to the value given by&#8217;attr&#8217;. </i><br />
 virtual void <code>removeAttr</code> (const std::string &amp;name)<br />
 <i>Remove the attribute &#8216;name&#8217;. This will not work for static attributes. </i><br />
 virtual void <code>sendContents</code> (<code>Atlas::Bridge</code> &amp;b) const<br />
 <i>Send the contents of this object to a </i><code>Bridge</code>.<br />
 virtual void <code>addToMessage</code> (Atlas::Message::MapType &amp;) const<br />
 <i>Write this object to an existing Element. </i><br />
 void <code>setLoc</code> (const std::string &amp;val)<br />
 <i>Set the &#8216;loc&#8217; attribute. </i><br />
 void <code>setPos</code> (const std::vector&lt; double &gt; &amp;val)<br />
 <i>Set the &#8216;pos&#8217; attribute. </i><br />
 void <code>setPosAsList</code> (const Atlas::Message::ListType &amp;val)<br />
 <i>Set the &#8216;pos&#8217; attribute AsList. </i><br />
 void <code>setVelocity</code> (const std::vector&lt; double &gt; &amp;val)<br />
 <i>Set the &#8216;velocity&#8217; attribute. </i><br />
 void <code>setVelocityAsList</code> (const Atlas::Message::ListType &amp;val)<br />
 <i>Set the &#8216;velocity&#8217; attribute AsList. </i><br />
 void <code>setContains</code> (const std::list&lt; std::string &gt; &amp;val)<br />
 <i>Set the &#8216;contains&#8217; attribute. </i><br />
 void <code>setContainsAsList</code> (const Atlas::Message::ListType &amp;val)<br />
 <i>Set the &#8216;contains&#8217; attribute AsList. </i><br />
 void <code>setStampContains</code> (double val)<br />
 <i>Set the &#8216;stamp_contains&#8217; attribute. </i><br />
 const std::string &amp; <code>getLoc</code> () const<br />
 <i>Retrieve the &#8216;loc&#8217; attribute. </i><br />
 std::string &amp; <code>modifyLoc</code> ()<br />
 <i>Retrieve the &#8216;loc&#8217; attribute as a non-const reference. </i><br />
 const std::vector&lt; double &gt; &amp; <code>getPos</code> () const<br />
 <i>Retrieve the &#8216;pos&#8217; attribute. </i><br />
 std::vector&lt; double &gt; &amp; <code>modifyPos</code> ()<br />
 <i>Retrieve the &#8216;pos&#8217; attribute as a non-const reference. </i><br />
 const Atlas::Message::ListType <code>getPosAsList</code> () const<br />
 <i>Retrieve the &#8216;pos&#8217; attribute AsList. </i><br />
 const std::vector&lt; double &gt; &amp; <code>getVelocity</code> () const<br />
 <i>Retrieve the &#8216;velocity&#8217; attribute. </i><br />
 std::vector&lt; double &gt; &amp; <code>modifyVelocity</code> ()<br />
 <i>Retrieve the &#8216;velocity&#8217; attribute as a non-const reference. </i><br />
 const Atlas::Message::ListType <code>getVelocityAsList</code> () const<br />
 <i>Retrieve the &#8216;velocity&#8217; attribute AsList. </i><br />
 const std::list&lt; std::string &gt; &amp; <code>getContains</code> () const<br />
 <i>Retrieve the &#8216;contains&#8217; attribute. </i><br />
 std::list&lt; std::string &gt; &amp; <code>modifyContains</code> ()<br />
 <i>Retrieve the &#8216;contains&#8217; attribute as a non-const reference. </i><br />
 const Atlas::Message::ListType <code>getContainsAsList</code> () const<br />
 <i>Retrieve the &#8216;contains&#8217; attribute AsList. </i><br />
 double <code>getStampContains</code> () const<br />
 <i>Retrieve the &#8216;stamp_contains&#8217; attribute. </i><br />
 double &amp; <code>modifyStampContains</code> ()<br />
 <i>Retrieve the &#8216;stamp_contains&#8217; attribute as a non-const reference. </i><br />
 bool <code>isDefaultLoc</code> () const<br />
 <i>Is &#8216;loc&#8217; value default? </i><br />
 bool <code>isDefaultPos</code> () const<br />
 <i>Is &#8216;pos&#8217; value default? </i><br />
 bool <code>isDefaultVelocity</code> () const<br />
 <i>Is &#8216;velocity&#8217; value default? </i><br />
 bool <code>isDefaultContains</code> () const<br />
 <i>Is &#8216;contains&#8217; value default? </i><br />
 bool <code>isDefaultStampContains</code> () const<br />
 <i>Is &#8216;stamp_contains&#8217; value default? </i><br />
 virtual void <code>free</code> ()<br />
 <i>Free an instance of this class, returning it to the memory pool. </i><br />
 virtual <code>RootEntityData</code> * <code>getDefaultObject</code> ()<br />
 <i>Get the reference object that contains the default values for attributes of instances of the same class as this object. </i></p>
<h3>Static Public Member Functions</h3>
<p>static <code>RootEntityData</code> * <code>alloc</code> ()<br />
 <i>Allocate a new instance of this class, using an existing instance if available. </i><br />
 static <code>RootEntityData</code> * <code>getDefaultObjectInstance</code> ()<br />
 <i>Get the reference object that contains the default values for attributes of instances of this class. </i></p>
<h3>Protected Member Functions</h3>
<p><code>RootEntityData</code> (<code>RootEntityData</code> *defaults=NULL)<br />
 <i>Construct a </i><code>RootEntityData</code> class definition.<br />
 virtual <code>~RootEntityData</code> ()<br />
 <i>Default destructor. </i><br />
 virtual int <code>getAttrClass</code> (const std::string &amp;name) const<br />
 <i>Find the class which contains the attribute &#8216;name&#8217;. </i><br />
 virtual int <code>getAttrFlag</code> (const std::string &amp;name) const<br />
 <i>Find the flag for the attribute &#8216;name&#8217;. </i><br />
 void <code>sendLoc</code> (<code>Atlas::Bridge</code> &amp;) const<br />
 <i>Send the &#8216;loc&#8217; attribute to an </i><code>Atlas::Bridge</code>.<br />
 void <code>sendPos</code> (<code>Atlas::Bridge</code> &amp;) const<br />
 <i>Send the &#8216;pos&#8217; attribute to an </i><code>Atlas::Bridge</code>.<br />
 void <code>sendVelocity</code> (<code>Atlas::Bridge</code> &amp;) const<br />
 <i>Send the &#8216;velocity&#8217; attribute to an </i><code>Atlas::Bridge</code>.<br />
 void <code>sendContains</code> (<code>Atlas::Bridge</code> &amp;) const<br />
 <i>Send the &#8216;contains&#8217; attribute to an </i><code>Atlas::Bridge</code>.<br />
 void <code>sendStampContains</code> (<code>Atlas::Bridge</code> &amp;) const<br />
 <i>Send the &#8216;stamp_contains&#8217; attribute to an </i><code>Atlas::Bridge</code>.<br />
 virtual void <code>iterate</code> (int &amp;current_class, std::string &amp;attr) const<br />
 <i>Iterate over the attributes of this instance. </i></p>
<h3>Protected Attributes</h3>
<p>std::string <code>attr_loc</code><br />
 <i>Reference object for coordinates (location). </i><br />
 std::vector&lt; double &gt; <code>attr_pos</code><br />
 <i>Position coordinates, usually world is 3D. </i><br />
 std::vector&lt; double &gt; <code>attr_velocity</code><br />
 <i>Velocity object is moving, usually world is 3D. </i><br />
 std::list&lt; std::string &gt; <code>attr_contains</code><br />
 <i>List of objects that use this object as reference system (usually same as what this object contains). </i><br />
 double <code>attr_stamp_contains</code><br />
 <i>Last time any object that uses this as reference recursively has been modified. </i></p>
<h2>Detailed Description</h2>
<p>Starting point for entity hierarchy. </p>
<p> Later in hierarchy tree objtype changes to &#8216;object&#8217; when actual game objects are made.</p>
<h2>Member Function Documentation</h2>
<h3>static <code>RootEntityData</code>* Atlas::Objects::Entity::RootEntityData::alloc () [static]</h3>
<p>Allocate a new instance of this class, using an existing instance if available. </p>
<p> This is the key function for implementing the memory pool for the <code>Atlas::Objects</code> API. </p>
<p> Reimplemented from <code>Atlas::Objects::RootData</code>. </p>
<p> Reimplemented in <code>Atlas::Objects::Entity::AnonymousData</code>, <code>Atlas::Objects::Entity::AdminEntityData</code>, <code>Atlas::Objects::Entity::AccountData</code>, <code>Atlas::Objects::Entity::PlayerData</code>, <code>Atlas::Objects::Entity::AdminData</code>, <code>Atlas::Objects::Entity::GameData</code>, and <code>Atlas::Objects::Entity::GameEntityData</code>.</p>
<h3>virtual int Atlas::Objects::Entity::RootEntityData::copyAttr (const std::string &amp; name, <code>Atlas::Message::Element</code> &amp; attr) const [virtual]</h3>
<p>Retrieve the attribute &#8216;name&#8217;. </p>
<p> Return non-zero if it does not exist. </p>
<p> Reimplemented from <code>Atlas::Objects::RootData</code>. </p>
<p> Reimplemented in <code>Atlas::Objects::Entity::AccountData</code>.</p>
<h3>virtual void Atlas::Objects::Entity::RootEntityData::free () [virtual]</h3>
<p>Free an instance of this class, returning it to the memory pool. </p>
<p> This function in combination with <code>alloc()</code> handle the memory pool. </p>
<p> Reimplemented from <code>Atlas::Objects::RootData</code>. </p>
<p> Reimplemented in <code>Atlas::Objects::Entity::AnonymousData</code>, <code>Atlas::Objects::Entity::AdminEntityData</code>, <code>Atlas::Objects::Entity::AccountData</code>, <code>Atlas::Objects::Entity::PlayerData</code>, <code>Atlas::Objects::Entity::AdminData</code>, <code>Atlas::Objects::Entity::GameData</code>, and <code>Atlas::Objects::Entity::GameEntityData</code>.</p>
<h3>virtual <code>RootEntityData</code>* Atlas::Objects::Entity::RootEntityData::getDefaultObject () [virtual]</h3>
<p>Get the reference object that contains the default values for attributes of instances of the same class as this object. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>a pointer to the default object.</dl>
<p> Reimplemented from <code>Atlas::Objects::RootData</code>. </p>
<p> Reimplemented in <code>Atlas::Objects::Entity::AnonymousData</code>, <code>Atlas::Objects::Entity::AdminEntityData</code>, <code>Atlas::Objects::Entity::AccountData</code>, <code>Atlas::Objects::Entity::PlayerData</code>, <code>Atlas::Objects::Entity::AdminData</code>, <code>Atlas::Objects::Entity::GameData</code>, and <code>Atlas::Objects::Entity::GameEntityData</code>.</p>
<h3>static <code>RootEntityData</code>* Atlas::Objects::Entity::RootEntityData::getDefaultObjectInstance () [static]</h3>
<p>Get the reference object that contains the default values for attributes of instances of this class. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>a pointer to the default object.</dl>
<p> Reimplemented from <code>Atlas::Objects::RootData</code>. </p>
<p> Reimplemented in <code>Atlas::Objects::Entity::AnonymousData</code>, <code>Atlas::Objects::Entity::AdminEntityData</code>, <code>Atlas::Objects::Entity::AccountData</code>, <code>Atlas::Objects::Entity::PlayerData</code>, <code>Atlas::Objects::Entity::AdminData</code>, <code>Atlas::Objects::Entity::GameData</code>, and <code>Atlas::Objects::Entity::GameEntityData</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Atlas-C++ from the source code.</p>
