---
title: "atlas_objects_rootdata(3)"
name: "atlas_objects_rootdata"
section: "3"
letter: "a"
url: "/docs/linux/man/3-atlas_objects_rootdata/"
description: "Atlas::Objects::RootData – All objects inherit from this."
---

<p>Atlas::Objects::RootData &#8211; All objects inherit from this. </p>
<h2>Synopsis</h2>
<p>#include &lt;<a href="file:/usr/include/Root.h">Root.h</a>&gt; </p>
<p> Inherits <code>Atlas::Objects::BaseObjectData</code>. </p>
<p> Inherited by <code>Atlas::Objects::Entity::RootEntityData</code>, and <code>Atlas::Objects::Operation::RootOperationData</code>. </p>
<h3>Public Member Functions</h3>
<p>virtual <code>RootData</code> * <code>copy</code> () const<br />
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
 void <code>setId</code> (const std::string &amp;val)<br />
 <i>Set the &#8216;id&#8217; attribute. </i><br />
 void <code>setParents</code> (const std::list&lt; std::string &gt; &amp;val)<br />
 <i>Set the &#8216;parents&#8217; attribute. </i><br />
 void <code>setParentsAsList</code> (const Atlas::Message::ListType &amp;val)<br />
 <i>Set the &#8216;parents&#8217; attribute AsList. </i><br />
 void <code>setStamp</code> (double val)<br />
 <i>Set the &#8216;stamp&#8217; attribute. </i><br />
 void <code>setObjtype</code> (const std::string &amp;val)<br />
 <i>Set the &#8216;objtype&#8217; attribute. </i><br />
 void <code>setName</code> (const std::string &amp;val)<br />
 <i>Set the &#8216;name&#8217; attribute. </i><br />
 const std::string &amp; <code>getId</code> () const<br />
 <i>Retrieve the &#8216;id&#8217; attribute. </i><br />
 std::string &amp; <code>modifyId</code> ()<br />
 <i>Retrieve the &#8216;id&#8217; attribute as a non-const reference. </i><br />
 const std::list&lt; std::string &gt; &amp; <code>getParents</code> () const<br />
 <i>Retrieve the &#8216;parents&#8217; attribute. </i><br />
 std::list&lt; std::string &gt; &amp; <code>modifyParents</code> ()<br />
 <i>Retrieve the &#8216;parents&#8217; attribute as a non-const reference. </i><br />
 const Atlas::Message::ListType <code>getParentsAsList</code> () const<br />
 <i>Retrieve the &#8216;parents&#8217; attribute AsList. </i><br />
 double <code>getStamp</code> () const<br />
 <i>Retrieve the &#8216;stamp&#8217; attribute. </i><br />
 double &amp; <code>modifyStamp</code> ()<br />
 <i>Retrieve the &#8216;stamp&#8217; attribute as a non-const reference. </i><br />
 const std::string &amp; <code>getObjtype</code> () const<br />
 <i>Retrieve the &#8216;objtype&#8217; attribute. </i><br />
 std::string &amp; <code>modifyObjtype</code> ()<br />
 <i>Retrieve the &#8216;objtype&#8217; attribute as a non-const reference. </i><br />
 const std::string &amp; <code>getName</code> () const<br />
 <i>Retrieve the &#8216;name&#8217; attribute. </i><br />
 std::string &amp; <code>modifyName</code> ()<br />
 <i>Retrieve the &#8216;name&#8217; attribute as a non-const reference. </i><br />
 bool <code>isDefaultId</code> () const<br />
 <i>Is &#8216;id&#8217; value default? </i><br />
 bool <code>isDefaultParents</code> () const<br />
 <i>Is &#8216;parents&#8217; value default? </i><br />
 bool <code>isDefaultStamp</code> () const<br />
 <i>Is &#8216;stamp&#8217; value default? </i><br />
 bool <code>isDefaultObjtype</code> () const<br />
 <i>Is &#8216;objtype&#8217; value default? </i><br />
 bool <code>isDefaultName</code> () const<br />
 <i>Is &#8216;name&#8217; value default? </i><br />
 virtual void <code>free</code> ()<br />
 <i>Free an instance of this class, returning it to the memory pool. </i><br />
 virtual <code>RootData</code> * <code>getDefaultObject</code> ()<br />
 <i>Get the reference object that contains the default values for attributes of instances of the same class as this object. </i></p>
<h3>Static Public Member Functions</h3>
<p>static <code>RootData</code> * <code>alloc</code> ()<br />
 <i>Allocate a new instance of this class, using an existing instance if available. </i><br />
 static <code>RootData</code> * <code>getDefaultObjectInstance</code> ()<br />
 <i>Get the reference object that contains the default values for attributes of instances of this class. </i></p>
<h3>Protected Member Functions</h3>
<p><code>RootData</code> (<code>RootData</code> *defaults=NULL)<br />
 <i>Construct a </i><code>RootData</code> class definition.<br />
 virtual <code>~RootData</code> ()<br />
 <i>Default destructor. </i><br />
 virtual int <code>getAttrClass</code> (const std::string &amp;name) const<br />
 <i>Find the class which contains the attribute &#8216;name&#8217;. </i><br />
 virtual int <code>getAttrFlag</code> (const std::string &amp;name) const<br />
 <i>Find the flag for the attribute &#8216;name&#8217;. </i><br />
 void <code>sendId</code> (<code>Atlas::Bridge</code> &amp;) const<br />
 <i>Send the &#8216;id&#8217; attribute to an </i><code>Atlas::Bridge</code>.<br />
 void <code>sendParents</code> (<code>Atlas::Bridge</code> &amp;) const<br />
 <i>Send the &#8216;parents&#8217; attribute to an </i><code>Atlas::Bridge</code>.<br />
 void <code>sendStamp</code> (<code>Atlas::Bridge</code> &amp;) const<br />
 <i>Send the &#8216;stamp&#8217; attribute to an </i><code>Atlas::Bridge</code>.<br />
 void <code>sendObjtype</code> (<code>Atlas::Bridge</code> &amp;) const<br />
 <i>Send the &#8216;objtype&#8217; attribute to an </i><code>Atlas::Bridge</code>.<br />
 void <code>sendName</code> (<code>Atlas::Bridge</code> &amp;) const<br />
 <i>Send the &#8216;name&#8217; attribute to an </i><code>Atlas::Bridge</code>.<br />
 virtual void <code>iterate</code> (int &amp;current_class, std::string &amp;attr) const<br />
 <i>Iterate over the attributes of this instance. </i></p>
<h3>Protected Attributes</h3>
<p>std::string <code>attr_id</code><br />
 <i>Id of object. </i><br />
 std::list&lt; std::string &gt; <code>attr_parents</code><br />
 <i>List of objects this inherits attributes from. </i><br />
 double <code>attr_stamp</code><br />
 <i>Last time this object was modified. </i><br />
 std::string <code>attr_objtype</code><br />
 <i>What kind of object this is. </i><br />
 std::string <code>attr_name</code><br />
 <i>Name of object. </i></p>
<h2>Detailed Description</h2>
<p>All objects inherit from this. </p>
<h2>Member Function Documentation</h2>
<h3>static <code>RootData</code>* Atlas::Objects::RootData::alloc () [static]</h3>
<p>Allocate a new instance of this class, using an existing instance if available. </p>
<p> This is the key function for implementing the memory pool for the <code>Atlas::Objects</code> API. </p>
<p> Reimplemented from <code>Atlas::Objects::BaseObjectData</code>. </p>
<p> Reimplemented in <code>Atlas::Objects::Entity::AnonymousData</code>, <code>Atlas::Objects::Entity::AdminEntityData</code>, <code>Atlas::Objects::Entity::AccountData</code>, <code>Atlas::Objects::Entity::PlayerData</code>, <code>Atlas::Objects::Entity::AdminData</code>, <code>Atlas::Objects::Entity::GameData</code>, <code>Atlas::Objects::Entity::GameEntityData</code>, <code>Atlas::Objects::Operation::GenericData</code>, <code>Atlas::Objects::Operation::ActionData</code>, <code>Atlas::Objects::Operation::CreateData</code>, <code>Atlas::Objects::Operation::CombineData</code>, <code>Atlas::Objects::Operation::DivideData</code>, <code>Atlas::Objects::Operation::CommunicateData</code>, <code>Atlas::Objects::Operation::TalkData</code>, <code>Atlas::Objects::Operation::DeleteData</code>, <code>Atlas::Objects::Operation::SetData</code>, <code>Atlas::Objects::Operation::AffectData</code>, <code>Atlas::Objects::Operation::MoveData</code>, <code>Atlas::Objects::Operation::WieldData</code>, <code>Atlas::Objects::Operation::GetData</code>, <code>Atlas::Objects::Operation::PerceiveData</code>, <code>Atlas::Objects::Operation::LookData</code>, <code>Atlas::Objects::Operation::ListenData</code>, <code>Atlas::Objects::Operation::SniffData</code>, <code>Atlas::Objects::Operation::TouchData</code>, <code>Atlas::Objects::Operation::LoginData</code>, <code>Atlas::Objects::Operation::LogoutData</code>, <code>Atlas::Objects::Operation::ImaginaryData</code>, <code>Atlas::Objects::Operation::UseData</code>, <code>Atlas::Objects::Operation::InfoData</code>, <code>Atlas::Objects::Operation::PerceptionData</code>, <code>Atlas::Objects::Operation::SightData</code>, <code>Atlas::Objects::Operation::AppearanceData</code>, <code>Atlas::Objects::Operation::DisappearanceData</code>, <code>Atlas::Objects::Operation::SoundData</code>, <code>Atlas::Objects::Operation::SmellData</code>, <code>Atlas::Objects::Operation::FeelData</code>, <code>Atlas::Objects::Operation::ErrorData</code>, <code>Atlas::Objects::Entity::RootEntityData</code>, and <code>Atlas::Objects::Operation::RootOperationData</code>.</p>
<h3>virtual int Atlas::Objects::RootData::copyAttr (const std::string &amp; name, <code>Atlas::Message::Element</code> &amp; attr) const [virtual]</h3>
<p>Retrieve the attribute &#8216;name&#8217;. </p>
<p> Return non-zero if it does not exist. </p>
<p> Reimplemented from <code>Atlas::Objects::BaseObjectData</code>. </p>
<p> Reimplemented in <code>Atlas::Objects::Entity::AccountData</code>, <code>Atlas::Objects::Entity::RootEntityData</code>, and <code>Atlas::Objects::Operation::RootOperationData</code>.</p>
<h3>virtual void Atlas::Objects::RootData::free () [virtual]</h3>
<p>Free an instance of this class, returning it to the memory pool. </p>
<p> This function in combination with <code>alloc()</code> handle the memory pool. </p>
<p> Implements <code>Atlas::Objects::BaseObjectData</code>. </p>
<p> Reimplemented in <code>Atlas::Objects::Entity::AnonymousData</code>, <code>Atlas::Objects::Entity::AdminEntityData</code>, <code>Atlas::Objects::Entity::AccountData</code>, <code>Atlas::Objects::Entity::PlayerData</code>, <code>Atlas::Objects::Entity::AdminData</code>, <code>Atlas::Objects::Entity::GameData</code>, <code>Atlas::Objects::Entity::GameEntityData</code>, <code>Atlas::Objects::Operation::GenericData</code>, <code>Atlas::Objects::Operation::ActionData</code>, <code>Atlas::Objects::Operation::CreateData</code>, <code>Atlas::Objects::Operation::CombineData</code>, <code>Atlas::Objects::Operation::DivideData</code>, <code>Atlas::Objects::Operation::CommunicateData</code>, <code>Atlas::Objects::Operation::TalkData</code>, <code>Atlas::Objects::Operation::DeleteData</code>, <code>Atlas::Objects::Operation::SetData</code>, <code>Atlas::Objects::Operation::AffectData</code>, <code>Atlas::Objects::Operation::MoveData</code>, <code>Atlas::Objects::Operation::WieldData</code>, <code>Atlas::Objects::Operation::GetData</code>, <code>Atlas::Objects::Operation::PerceiveData</code>, <code>Atlas::Objects::Operation::LookData</code>, <code>Atlas::Objects::Operation::ListenData</code>, <code>Atlas::Objects::Operation::SniffData</code>, <code>Atlas::Objects::Operation::TouchData</code>, <code>Atlas::Objects::Operation::LoginData</code>, <code>Atlas::Objects::Operation::LogoutData</code>, <code>Atlas::Objects::Operation::ImaginaryData</code>, <code>Atlas::Objects::Operation::UseData</code>, <code>Atlas::Objects::Operation::InfoData</code>, <code>Atlas::Objects::Operation::PerceptionData</code>, <code>Atlas::Objects::Operation::SightData</code>, <code>Atlas::Objects::Operation::AppearanceData</code>, <code>Atlas::Objects::Operation::DisappearanceData</code>, <code>Atlas::Objects::Operation::SoundData</code>, <code>Atlas::Objects::Operation::SmellData</code>, <code>Atlas::Objects::Operation::FeelData</code>, <code>Atlas::Objects::Operation::ErrorData</code>, <code>Atlas::Objects::Entity::RootEntityData</code>, and <code>Atlas::Objects::Operation::RootOperationData</code>.</p>
<h3>virtual <code>RootData</code>* Atlas::Objects::RootData::getDefaultObject () [virtual]</h3>
<p>Get the reference object that contains the default values for attributes of instances of the same class as this object. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>a pointer to the default object.</dl>
<p> Reimplemented in <code>Atlas::Objects::Entity::AnonymousData</code>, <code>Atlas::Objects::Entity::AdminEntityData</code>, <code>Atlas::Objects::Entity::AccountData</code>, <code>Atlas::Objects::Entity::PlayerData</code>, <code>Atlas::Objects::Entity::AdminData</code>, <code>Atlas::Objects::Entity::GameData</code>, <code>Atlas::Objects::Entity::GameEntityData</code>, <code>Atlas::Objects::Operation::GenericData</code>, <code>Atlas::Objects::Operation::ActionData</code>, <code>Atlas::Objects::Operation::CreateData</code>, <code>Atlas::Objects::Operation::CombineData</code>, <code>Atlas::Objects::Operation::DivideData</code>, <code>Atlas::Objects::Operation::CommunicateData</code>, <code>Atlas::Objects::Operation::TalkData</code>, <code>Atlas::Objects::Operation::DeleteData</code>, <code>Atlas::Objects::Operation::SetData</code>, <code>Atlas::Objects::Operation::AffectData</code>, <code>Atlas::Objects::Operation::MoveData</code>, <code>Atlas::Objects::Operation::WieldData</code>, <code>Atlas::Objects::Operation::GetData</code>, <code>Atlas::Objects::Operation::PerceiveData</code>, <code>Atlas::Objects::Operation::LookData</code>, <code>Atlas::Objects::Operation::ListenData</code>, <code>Atlas::Objects::Operation::SniffData</code>, <code>Atlas::Objects::Operation::TouchData</code>, <code>Atlas::Objects::Operation::LoginData</code>, <code>Atlas::Objects::Operation::LogoutData</code>, <code>Atlas::Objects::Operation::ImaginaryData</code>, <code>Atlas::Objects::Operation::UseData</code>, <code>Atlas::Objects::Operation::InfoData</code>, <code>Atlas::Objects::Operation::PerceptionData</code>, <code>Atlas::Objects::Operation::SightData</code>, <code>Atlas::Objects::Operation::AppearanceData</code>, <code>Atlas::Objects::Operation::DisappearanceData</code>, <code>Atlas::Objects::Operation::SoundData</code>, <code>Atlas::Objects::Operation::SmellData</code>, <code>Atlas::Objects::Operation::FeelData</code>, <code>Atlas::Objects::Operation::ErrorData</code>, <code>Atlas::Objects::Entity::RootEntityData</code>, and <code>Atlas::Objects::Operation::RootOperationData</code>.</p>
<h3>static <code>RootData</code>* Atlas::Objects::RootData::getDefaultObjectInstance () [static]</h3>
<p>Get the reference object that contains the default values for attributes of instances of this class. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>a pointer to the default object.</dl>
<p> Reimplemented in <code>Atlas::Objects::Entity::AnonymousData</code>, <code>Atlas::Objects::Entity::AdminEntityData</code>, <code>Atlas::Objects::Entity::AccountData</code>, <code>Atlas::Objects::Entity::PlayerData</code>, <code>Atlas::Objects::Entity::AdminData</code>, <code>Atlas::Objects::Entity::GameData</code>, <code>Atlas::Objects::Entity::GameEntityData</code>, <code>Atlas::Objects::Operation::GenericData</code>, <code>Atlas::Objects::Operation::ActionData</code>, <code>Atlas::Objects::Operation::CreateData</code>, <code>Atlas::Objects::Operation::CombineData</code>, <code>Atlas::Objects::Operation::DivideData</code>, <code>Atlas::Objects::Operation::CommunicateData</code>, <code>Atlas::Objects::Operation::TalkData</code>, <code>Atlas::Objects::Operation::DeleteData</code>, <code>Atlas::Objects::Operation::SetData</code>, <code>Atlas::Objects::Operation::AffectData</code>, <code>Atlas::Objects::Operation::MoveData</code>, <code>Atlas::Objects::Operation::WieldData</code>, <code>Atlas::Objects::Operation::GetData</code>, <code>Atlas::Objects::Operation::PerceiveData</code>, <code>Atlas::Objects::Operation::LookData</code>, <code>Atlas::Objects::Operation::ListenData</code>, <code>Atlas::Objects::Operation::SniffData</code>, <code>Atlas::Objects::Operation::TouchData</code>, <code>Atlas::Objects::Operation::LoginData</code>, <code>Atlas::Objects::Operation::LogoutData</code>, <code>Atlas::Objects::Operation::ImaginaryData</code>, <code>Atlas::Objects::Operation::UseData</code>, <code>Atlas::Objects::Operation::InfoData</code>, <code>Atlas::Objects::Operation::PerceptionData</code>, <code>Atlas::Objects::Operation::SightData</code>, <code>Atlas::Objects::Operation::AppearanceData</code>, <code>Atlas::Objects::Operation::DisappearanceData</code>, <code>Atlas::Objects::Operation::SoundData</code>, <code>Atlas::Objects::Operation::SmellData</code>, <code>Atlas::Objects::Operation::FeelData</code>, <code>Atlas::Objects::Operation::ErrorData</code>, <code>Atlas::Objects::Entity::RootEntityData</code>, and <code>Atlas::Objects::Operation::RootOperationData</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Atlas-C++ from the source code.</p>
