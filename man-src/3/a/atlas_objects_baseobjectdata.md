---
title: "atlas_objects_baseobjectdata(3)"
name: "atlas_objects_baseobjectdata"
section: "3"
letter: "a"
url: "/docs/linux/man/3-atlas_objects_baseobjectdata/"
description: "Atlas::Objects::BaseObjectData – Atlas base object class."
---

<p>Atlas::Objects::BaseObjectData &#8211; <code>Atlas</code> base object class. </p>
<h2>Synopsis</h2>
<p>#include &lt;<a href="file:/usr/include/BaseObject.h">BaseObject.h</a>&gt; </p>
<p> Inherited by <code>Atlas::Objects::RootData</code>. </p>
<h3>Classes</h3>
<p>class <code>const_iterator</code> </p>
<p> class <code>iterator</code><br />
 <i>The </i><code>iterator</code> first iterates over the contents of m_obj-&gt;m_attributes, holding an <code>iterator</code> to the attributes map in m_I.</p>
<h3>Public Member Functions</h3>
<p><code>BaseObjectData</code> (<code>BaseObjectData</code> *defaults)<br />
 <i>Construct a new </i><code>BaseObjectData</code> from a subclass.<br />
 int <code>getClassNo</code> () const<br />
 <i>Get class number:. </i><br />
 int <code>getAttrFlags</code> () const </p>
<p> virtual <code>BaseObjectData</code> * <code>copy</code> () const =0 </p>
<p> virtual bool <code>instanceOf</code> (int classNo) const<br />
 <i>Is this instance of some class? </i><br />
 bool <code>hasAttr</code> (const std::string &amp;name) const<br />
 <i>Check whether the attribute &#8216;name&#8217; exists. </i><br />
 bool <code>hasAttrFlag</code> (int flag) const<br />
 <i>Check whether the attribute &#8216;name&#8217; exists. </i><br />
 const <code>Atlas::Message::Element</code> <code>getAttr</code> (const std::string &amp;name) const throw (NoSuchAttrException)<br />
 <i>Retrieve the attribute &#8216;name&#8217;. </i><br />
 virtual int <code>copyAttr</code> (const std::string &amp;name, <code>Atlas::Message::Element</code> &amp;attr) const<br />
 <i>Retrieve the attribute &#8216;name&#8217;. </i><br />
 virtual void <code>setAttr</code> (const std::string &amp;name, const <code>Atlas::Message::Element</code> &amp;attr)<br />
 <i>Set the attribute &#8216;name&#8217; to the value given by &#8216;attr&#8217;. </i><br />
 virtual void <code>removeAttr</code> (const std::string &amp;name)<br />
 <i>Remove the attribute &#8216;name&#8217;. </i><br />
 virtual void <code>removeAttrFlag</code> (int flag)<br />
 <i>Remove the attribute &#8216;name&#8217;. </i><br />
 const Atlas::Message::MapType <code>asMessage</code> () const<br />
 <i>Convert this object to a Object. </i><br />
 virtual void <code>addToMessage</code> (Atlas::Message::MapType &amp;) const<br />
 <i>Write this object to an existing Element. </i><br />
 virtual void <code>sendContents</code> (<code>Atlas::Bridge</code> &amp;b) const<br />
 <i>Send the contents of this object to a </i><code>Bridge</code>.<br />
 void <code>incRef</code> () </p>
<p> void <code>decRef</code> () </p>
<p> virtual void <code>free</code> ()=0<br />
 <i>Free an instance of this class, returning it to the memory pool. </i><br />
 <code>iterator</code> <code>begin</code> () </p>
<p> <code>iterator</code> <code>end</code> () </p>
<p> <code>iterator</code> <code>find</code> (const std::string &amp;) </p>
<p> const_iterator <code>begin</code> () const </p>
<p> const_iterator <code>end</code> () const </p>
<p> const_iterator <code>find</code> (const std::string &amp;) const </p>
<h3>Static Public Member Functions</h3>
<p>static <code>BaseObjectData</code> * <code>alloc</code> ()<br />
 <i>Allocate a new instance of this class, using an existing instance if available. </i></p>
<h3>Protected Member Functions</h3>
<p>virtual int <code>getAttrClass</code> (const std::string &amp;name) const<br />
 <i>Find the class which contains the attribute &#8216;name&#8217;. </i><br />
 virtual int <code>getAttrFlag</code> (const std::string &amp;name) const<br />
 <i>Find the flag for the attribute &#8216;name&#8217;. </i><br />
 virtual void <code>iterate</code> (int &amp;current_class, std::string &amp;attr) const<br />
 <i>Iterate over the attributes of this instance. </i></p>
<h3>Protected Attributes</h3>
<p>int <code>m_class_no</code> </p>
<p> int <code>m_refCount</code> </p>
<p> <code>BaseObjectData</code> * <code>m_defaults</code> </p>
<p> <code>BaseObjectData</code> * <code>m_next</code> </p>
<p> std::map&lt; std::string, <code>Atlas::Message::Element</code> &gt; <code>m_attributes</code> </p>
<p> int <code>m_attrFlags</code> </p>
<h3>Friends</h3>
<p>class <code>iterator</code> </p>
<p> class <code>const_iterator</code> </p>
<h2>Detailed Description</h2>
<p><code>Atlas</code> base object class. </p>
<p> This is class is the base from which all classes used to represent high level objects are derived. In this release of Atlas-C++, all classes that inherit from <code>BaseObjectData</code> are designed to be used with SmartPtr and should have the suffix Data on the end of their name. All the subclasses of <code>BaseObjectData</code> included with Atlas-C++ are automatically generated from the <code>Atlas</code> spec at release time. For each subclass a typedef is created of a specialisation of SmartPtr aliasing it to the name of the class without the Data suffix. Thus RootOperationData has an associate type RootOperation which is a typedef for SmartPtr&lt;RootOperationData&gt;. Each class also has an associated integer identifier used to identify classes of its type. The SmartPtr class is designed to store unused instances of the data objects in a memory pool, and reuse instances as they are required. In order to re-use instances without re-constructing all their members, a system of flags is used to mark which members are in use. When an instance is re-used these flags are cleared, indicating that none of the members are in use.</p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>Atlas::Objects::BaseObjectData::BaseObjectData (<code>BaseObjectData</code> * defaults)</h3>
<p>Construct a new <code>BaseObjectData</code> from a subclass. </p>
<p> Initialises flags to zero, and stores a pointer to the reference object that provides default values for all attributes. Subclasses must pass in a pointer to their class specific reference object.</p>
<h2>Member Function Documentation</h2>
<h3>static <code>BaseObjectData</code>* Atlas::Objects::BaseObjectData::alloc () [inline, static]</h3>
<p>Allocate a new instance of this class, using an existing instance if available. </p>
<p> This is the key function for implementing the memory pool for the <code>Atlas::Objects</code> API. </p>
<p> Reimplemented in <code>Atlas::Objects::Entity::AnonymousData</code>, <code>Atlas::Objects::Entity::AdminEntityData</code>, <code>Atlas::Objects::Entity::AccountData</code>, <code>Atlas::Objects::Entity::PlayerData</code>, <code>Atlas::Objects::Entity::AdminData</code>, <code>Atlas::Objects::Entity::GameData</code>, <code>Atlas::Objects::Entity::GameEntityData</code>, <code>Atlas::Objects::Operation::GenericData</code>, <code>Atlas::Objects::Operation::ActionData</code>, <code>Atlas::Objects::Operation::CreateData</code>, <code>Atlas::Objects::Operation::CombineData</code>, <code>Atlas::Objects::Operation::DivideData</code>, <code>Atlas::Objects::Operation::CommunicateData</code>, <code>Atlas::Objects::Operation::TalkData</code>, <code>Atlas::Objects::Operation::DeleteData</code>, <code>Atlas::Objects::Operation::SetData</code>, <code>Atlas::Objects::Operation::AffectData</code>, <code>Atlas::Objects::Operation::MoveData</code>, <code>Atlas::Objects::Operation::WieldData</code>, <code>Atlas::Objects::Operation::GetData</code>, <code>Atlas::Objects::Operation::PerceiveData</code>, <code>Atlas::Objects::Operation::LookData</code>, <code>Atlas::Objects::Operation::ListenData</code>, <code>Atlas::Objects::Operation::SniffData</code>, <code>Atlas::Objects::Operation::TouchData</code>, <code>Atlas::Objects::Operation::LoginData</code>, <code>Atlas::Objects::Operation::LogoutData</code>, <code>Atlas::Objects::Operation::ImaginaryData</code>, <code>Atlas::Objects::Operation::UseData</code>, <code>Atlas::Objects::Operation::InfoData</code>, <code>Atlas::Objects::Operation::PerceptionData</code>, <code>Atlas::Objects::Operation::SightData</code>, <code>Atlas::Objects::Operation::AppearanceData</code>, <code>Atlas::Objects::Operation::DisappearanceData</code>, <code>Atlas::Objects::Operation::SoundData</code>, <code>Atlas::Objects::Operation::SmellData</code>, <code>Atlas::Objects::Operation::FeelData</code>, <code>Atlas::Objects::Operation::ErrorData</code>, <code>Atlas::Objects::RootData</code>, <code>Atlas::Objects::Entity::RootEntityData</code>, and <code>Atlas::Objects::Operation::RootOperationData</code>.</p>
<h3>const Atlas::Message::MapType Atlas::Objects::BaseObjectData::asMessage () const</h3>
<p>Convert this object to a Object. </p>
<p> This is now legacy, and implemented using addToMessage.</p>
<h3>virtual int Atlas::Objects::BaseObjectData::copyAttr (const std::string &amp; name, <code>Atlas::Message::Element</code> &amp; attr) const [virtual]</h3>
<p>Retrieve the attribute &#8216;name&#8217;. </p>
<p> Return non-zero if it does not exist. </p>
<p> Reimplemented in <code>Atlas::Objects::Entity::AccountData</code>, <code>Atlas::Objects::RootData</code>, <code>Atlas::Objects::Entity::RootEntityData</code>, and <code>Atlas::Objects::Operation::RootOperationData</code>.</p>
<h3>virtual void Atlas::Objects::BaseObjectData::free () [pure virtual]</h3>
<p>Free an instance of this class, returning it to the memory pool. </p>
<p> This function in combination with <code>alloc()</code> handle the memory pool. </p>
<p> Implemented in <code>Atlas::Objects::Entity::AnonymousData</code>, <code>Atlas::Objects::Entity::AdminEntityData</code>, <code>Atlas::Objects::Entity::AccountData</code>, <code>Atlas::Objects::Entity::PlayerData</code>, <code>Atlas::Objects::Entity::AdminData</code>, <code>Atlas::Objects::Entity::GameData</code>, <code>Atlas::Objects::Entity::GameEntityData</code>, <code>Atlas::Objects::Operation::GenericData</code>, <code>Atlas::Objects::Operation::ActionData</code>, <code>Atlas::Objects::Operation::CreateData</code>, <code>Atlas::Objects::Operation::CombineData</code>, <code>Atlas::Objects::Operation::DivideData</code>, <code>Atlas::Objects::Operation::CommunicateData</code>, <code>Atlas::Objects::Operation::TalkData</code>, <code>Atlas::Objects::Operation::DeleteData</code>, <code>Atlas::Objects::Operation::SetData</code>, <code>Atlas::Objects::Operation::AffectData</code>, <code>Atlas::Objects::Operation::MoveData</code>, <code>Atlas::Objects::Operation::WieldData</code>, <code>Atlas::Objects::Operation::GetData</code>, <code>Atlas::Objects::Operation::PerceiveData</code>, <code>Atlas::Objects::Operation::LookData</code>, <code>Atlas::Objects::Operation::ListenData</code>, <code>Atlas::Objects::Operation::SniffData</code>, <code>Atlas::Objects::Operation::TouchData</code>, <code>Atlas::Objects::Operation::LoginData</code>, <code>Atlas::Objects::Operation::LogoutData</code>, <code>Atlas::Objects::Operation::ImaginaryData</code>, <code>Atlas::Objects::Operation::UseData</code>, <code>Atlas::Objects::Operation::InfoData</code>, <code>Atlas::Objects::Operation::PerceptionData</code>, <code>Atlas::Objects::Operation::SightData</code>, <code>Atlas::Objects::Operation::AppearanceData</code>, <code>Atlas::Objects::Operation::DisappearanceData</code>, <code>Atlas::Objects::Operation::SoundData</code>, <code>Atlas::Objects::Operation::SmellData</code>, <code>Atlas::Objects::Operation::FeelData</code>, <code>Atlas::Objects::Operation::ErrorData</code>, <code>Atlas::Objects::RootData</code>, <code>Atlas::Objects::Entity::RootEntityData</code>, and <code>Atlas::Objects::Operation::RootOperationData</code>.</p>
<h3>const <code>Atlas::Message::Element</code> Atlas::Objects::BaseObjectData::getAttr (const std::string &amp; name) const throw (<code>NoSuchAttrException</code>)</h3>
<p>Retrieve the attribute &#8216;name&#8217;. </p>
<p> Throws <code>NoSuchAttrException</code> if it does not exist. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Atlas-C++ from the source code.</p>
