---
title: "atlas_objects_entity_accountdata(3)"
name: "atlas_objects_entity_accountdata"
section: "3"
letter: "a"
url: "/docs/linux/man/3-atlas_objects_entity_accountdata/"
description: "Atlas::Objects::Entity::AccountData – Base class for accounts."
---

<p>Atlas::Objects::Entity::AccountData &#8211; Base class for accounts. </p>
<h2>Synopsis</h2>
<p>#include &lt;<a href="file:/usr/include/Entity.h">Entity.h</a>&gt; </p>
<p> Inherits <code>Atlas::Objects::Entity::AdminEntityData</code>. </p>
<p> Inherited by <code>Atlas::Objects::Entity::AdminData</code>, and <code>Atlas::Objects::Entity::PlayerData</code>. </p>
<h3>Public Member Functions</h3>
<p>virtual <code>AccountData</code> * <code>copy</code> () const<br />
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
 void <code>setUsername</code> (const std::string &amp;val)<br />
 <i>Set the &#8216;username&#8217; attribute. </i><br />
 void <code>setPassword</code> (const std::string &amp;val)<br />
 <i>Set the &#8216;password&#8217; attribute. </i><br />
 void <code>setCharacters</code> (const std::list&lt; std::string &gt; &amp;val)<br />
 <i>Set the &#8216;characters&#8217; attribute. </i><br />
 void <code>setCharactersAsList</code> (const Atlas::Message::ListType &amp;val)<br />
 <i>Set the &#8216;characters&#8217; attribute AsList. </i><br />
 const std::string &amp; <code>getUsername</code> () const<br />
 <i>Retrieve the &#8216;username&#8217; attribute. </i><br />
 std::string &amp; <code>modifyUsername</code> ()<br />
 <i>Retrieve the &#8216;username&#8217; attribute as a non-const reference. </i><br />
 const std::string &amp; <code>getPassword</code> () const<br />
 <i>Retrieve the &#8216;password&#8217; attribute. </i><br />
 std::string &amp; <code>modifyPassword</code> ()<br />
 <i>Retrieve the &#8216;password&#8217; attribute as a non-const reference. </i><br />
 const std::list&lt; std::string &gt; &amp; <code>getCharacters</code> () const<br />
 <i>Retrieve the &#8216;characters&#8217; attribute. </i><br />
 std::list&lt; std::string &gt; &amp; <code>modifyCharacters</code> ()<br />
 <i>Retrieve the &#8216;characters&#8217; attribute as a non-const reference. </i><br />
 const Atlas::Message::ListType <code>getCharactersAsList</code> () const<br />
 <i>Retrieve the &#8216;characters&#8217; attribute AsList. </i><br />
 bool <code>isDefaultUsername</code> () const<br />
 <i>Is &#8216;username&#8217; value default? </i><br />
 bool <code>isDefaultPassword</code> () const<br />
 <i>Is &#8216;password&#8217; value default? </i><br />
 bool <code>isDefaultCharacters</code> () const<br />
 <i>Is &#8216;characters&#8217; value default? </i><br />
 virtual void <code>free</code> ()<br />
 <i>Free an instance of this class, returning it to the memory pool. </i><br />
 virtual <code>AccountData</code> * <code>getDefaultObject</code> ()<br />
 <i>Get the reference object that contains the default values for attributes of instances of the same class as this object. </i></p>
<h3>Static Public Member Functions</h3>
<p>static <code>AccountData</code> * <code>alloc</code> ()<br />
 <i>Allocate a new instance of this class, using an existing instance if available. </i><br />
 static <code>AccountData</code> * <code>getDefaultObjectInstance</code> ()<br />
 <i>Get the reference object that contains the default values for attributes of instances of this class. </i></p>
<h3>Protected Member Functions</h3>
<p><code>AccountData</code> (<code>AccountData</code> *defaults=NULL)<br />
 <i>Construct a </i><code>AccountData</code> class definition.<br />
 virtual <code>~AccountData</code> ()<br />
 <i>Default destructor. </i><br />
 virtual int <code>getAttrClass</code> (const std::string &amp;name) const<br />
 <i>Find the class which contains the attribute &#8216;name&#8217;. </i><br />
 virtual int <code>getAttrFlag</code> (const std::string &amp;name) const<br />
 <i>Find the flag for the attribute &#8216;name&#8217;. </i><br />
 void <code>sendUsername</code> (<code>Atlas::Bridge</code> &amp;) const<br />
 <i>Send the &#8216;username&#8217; attribute to an </i><code>Atlas::Bridge</code>.<br />
 void <code>sendPassword</code> (<code>Atlas::Bridge</code> &amp;) const<br />
 <i>Send the &#8216;password&#8217; attribute to an </i><code>Atlas::Bridge</code>.<br />
 void <code>sendCharacters</code> (<code>Atlas::Bridge</code> &amp;) const<br />
 <i>Send the &#8216;characters&#8217; attribute to an </i><code>Atlas::Bridge</code>.<br />
 virtual void <code>iterate</code> (int &amp;current_class, std::string &amp;attr) const<br />
 <i>Iterate over the attributes of this instance. </i></p>
<h3>Protected Attributes</h3>
<p>std::string <code>attr_username</code><br />
 <i>Username for account usually. </i><br />
 std::string <code>attr_password</code><br />
 <i>Password for account usually. </i><br />
 std::list&lt; std::string &gt; <code>attr_characters</code><br />
 <i>List of characters account can control. </i></p>
<h2>Detailed Description</h2>
<p>Base class for accounts. </p>
<p> Later in hierarchy tree objtype changes to &#8216;object&#8217; when actual game objects are made.</p>
<h2>Member Function Documentation</h2>
<h3>static <code>AccountData</code>* Atlas::Objects::Entity::AccountData::alloc () [static]</h3>
<p>Allocate a new instance of this class, using an existing instance if available. </p>
<p> This is the key function for implementing the memory pool for the <code>Atlas::Objects</code> API. </p>
<p> Reimplemented from <code>Atlas::Objects::Entity::AdminEntityData</code>. </p>
<p> Reimplemented in <code>Atlas::Objects::Entity::PlayerData</code>, and <code>Atlas::Objects::Entity::AdminData</code>.</p>
<h3>virtual int Atlas::Objects::Entity::AccountData::copyAttr (const std::string &amp; name, <code>Atlas::Message::Element</code> &amp; attr) const [virtual]</h3>
<p>Retrieve the attribute &#8216;name&#8217;. </p>
<p> Return non-zero if it does not exist. </p>
<p> Reimplemented from <code>Atlas::Objects::Entity::RootEntityData</code>.</p>
<h3>virtual void Atlas::Objects::Entity::AccountData::free () [virtual]</h3>
<p>Free an instance of this class, returning it to the memory pool. </p>
<p> This function in combination with <code>alloc()</code> handle the memory pool. </p>
<p> Reimplemented from <code>Atlas::Objects::Entity::AdminEntityData</code>. </p>
<p> Reimplemented in <code>Atlas::Objects::Entity::PlayerData</code>, and <code>Atlas::Objects::Entity::AdminData</code>.</p>
<h3>virtual <code>AccountData</code>* Atlas::Objects::Entity::AccountData::getDefaultObject () [virtual]</h3>
<p>Get the reference object that contains the default values for attributes of instances of the same class as this object. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>a pointer to the default object.</dl>
<p> Reimplemented from <code>Atlas::Objects::Entity::AdminEntityData</code>. </p>
<p> Reimplemented in <code>Atlas::Objects::Entity::PlayerData</code>, and <code>Atlas::Objects::Entity::AdminData</code>.</p>
<h3>static <code>AccountData</code>* Atlas::Objects::Entity::AccountData::getDefaultObjectInstance () [static]</h3>
<p>Get the reference object that contains the default values for attributes of instances of this class. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>a pointer to the default object.</dl>
<p> Reimplemented from <code>Atlas::Objects::Entity::AdminEntityData</code>. </p>
<p> Reimplemented in <code>Atlas::Objects::Entity::PlayerData</code>, and <code>Atlas::Objects::Entity::AdminData</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Atlas-C++ from the source code.</p>
