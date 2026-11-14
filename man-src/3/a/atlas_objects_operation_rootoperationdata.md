---
title: "atlas_objects_operation_rootoperationdata(3)"
name: "atlas_objects_operation_rootoperationdata"
section: "3"
letter: "a"
url: "/docs/linux/man/3-atlas_objects_operation_rootoperationdata/"
description: "Atlas::Objects::Operation::RootOperationData – Base operation for all operators."
---

<p>Atlas::Objects::Operation::RootOperationData &#8211; Base operation for all operators. </p>
<h2>Synopsis</h2>
<p>#include &lt;<a href="file:/usr/include/RootOperation.h">RootOperation.h</a>&gt; </p>
<p> Inherits <code>Atlas::Objects::RootData</code>. </p>
<p> Inherited by <code>Atlas::Objects::Operation::ActionData</code>, <code>Atlas::Objects::Operation::GenericData</code>, and <code>Atlas::Objects::Operation::InfoData</code>. </p>
<h3>Public Member Functions</h3>
<p>virtual <code>RootOperationData</code> * <code>copy</code> () const<br />
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
 void <code>setSerialno</code> (long val)<br />
 <i>Set the &#8216;serialno&#8217; attribute. </i><br />
 void <code>setRefno</code> (long val)<br />
 <i>Set the &#8216;refno&#8217; attribute. </i><br />
 void <code>setFrom</code> (const std::string &amp;val)<br />
 <i>Set the &#8216;from&#8217; attribute. </i><br />
 void <code>setTo</code> (const std::string &amp;val)<br />
 <i>Set the &#8216;to&#8217; attribute. </i><br />
 void <code>setSeconds</code> (double val)<br />
 <i>Set the &#8216;seconds&#8217; attribute. </i><br />
 void <code>setFutureSeconds</code> (double val)<br />
 <i>Set the &#8216;future_seconds&#8217; attribute. </i><br />
 void <code>setArgs</code> (const std::vector&lt; Root &gt; &amp;val)<br />
 <i>Set the &#8216;args&#8217; attribute. </i><br />
 void <code>setArgsAsList</code> (const Atlas::Message::ListType &amp;val)<br />
 <i>Set the &#8216;args&#8217; attribute AsList. </i><br />
 template&lt;class ObjectData &gt; void <code>setArgs1</code> (const SmartPtr&lt; ObjectData &gt; &amp;val)<br />
 <i>Set the first member of &#8216;args&#8217;. </i><br />
 long <code>getSerialno</code> () const<br />
 <i>Retrieve the &#8216;serialno&#8217; attribute. </i><br />
 long &amp; <code>modifySerialno</code> ()<br />
 <i>Retrieve the &#8216;serialno&#8217; attribute as a non-const reference. </i><br />
 long <code>getRefno</code> () const<br />
 <i>Retrieve the &#8216;refno&#8217; attribute. </i><br />
 long &amp; <code>modifyRefno</code> ()<br />
 <i>Retrieve the &#8216;refno&#8217; attribute as a non-const reference. </i><br />
 const std::string &amp; <code>getFrom</code> () const<br />
 <i>Retrieve the &#8216;from&#8217; attribute. </i><br />
 std::string &amp; <code>modifyFrom</code> ()<br />
 <i>Retrieve the &#8216;from&#8217; attribute as a non-const reference. </i><br />
 const std::string &amp; <code>getTo</code> () const<br />
 <i>Retrieve the &#8216;to&#8217; attribute. </i><br />
 std::string &amp; <code>modifyTo</code> ()<br />
 <i>Retrieve the &#8216;to&#8217; attribute as a non-const reference. </i><br />
 double <code>getSeconds</code> () const<br />
 <i>Retrieve the &#8216;seconds&#8217; attribute. </i><br />
 double &amp; <code>modifySeconds</code> ()<br />
 <i>Retrieve the &#8216;seconds&#8217; attribute as a non-const reference. </i><br />
 double <code>getFutureSeconds</code> () const<br />
 <i>Retrieve the &#8216;future_seconds&#8217; attribute. </i><br />
 double &amp; <code>modifyFutureSeconds</code> ()<br />
 <i>Retrieve the &#8216;future_seconds&#8217; attribute as a non-const reference. </i><br />
 const std::vector&lt; Root &gt; &amp; <code>getArgs</code> () const<br />
 <i>Retrieve the &#8216;args&#8217; attribute. </i><br />
 std::vector&lt; Root &gt; &amp; <code>modifyArgs</code> ()<br />
 <i>Retrieve the &#8216;args&#8217; attribute as a non-const reference. </i><br />
 const Atlas::Message::ListType <code>getArgsAsList</code> () const<br />
 <i>Retrieve the &#8216;args&#8217; attribute AsList. </i><br />
 bool <code>isDefaultSerialno</code> () const<br />
 <i>Is &#8216;serialno&#8217; value default? </i><br />
 bool <code>isDefaultRefno</code> () const<br />
 <i>Is &#8216;refno&#8217; value default? </i><br />
 bool <code>isDefaultFrom</code> () const<br />
 <i>Is &#8216;from&#8217; value default? </i><br />
 bool <code>isDefaultTo</code> () const<br />
 <i>Is &#8216;to&#8217; value default? </i><br />
 bool <code>isDefaultSeconds</code> () const<br />
 <i>Is &#8216;seconds&#8217; value default? </i><br />
 bool <code>isDefaultFutureSeconds</code> () const<br />
 <i>Is &#8216;future_seconds&#8217; value default? </i><br />
 bool <code>isDefaultArgs</code> () const<br />
 <i>Is &#8216;args&#8217; value default? </i><br />
 virtual void <code>free</code> ()<br />
 <i>Free an instance of this class, returning it to the memory pool. </i><br />
 virtual <code>RootOperationData</code> * <code>getDefaultObject</code> ()<br />
 <i>Get the reference object that contains the default values for attributes of instances of the same class as this object. </i></p>
<h3>Static Public Member Functions</h3>
<p>static <code>RootOperationData</code> * <code>alloc</code> ()<br />
 <i>Allocate a new instance of this class, using an existing instance if available. </i><br />
 static <code>RootOperationData</code> * <code>getDefaultObjectInstance</code> ()<br />
 <i>Get the reference object that contains the default values for attributes of instances of this class. </i></p>
<h3>Protected Member Functions</h3>
<p><code>RootOperationData</code> (<code>RootOperationData</code> *defaults=NULL)<br />
 <i>Construct a </i><code>RootOperationData</code> class definition.<br />
 virtual <code>~RootOperationData</code> ()<br />
 <i>Default destructor. </i><br />
 virtual int <code>getAttrClass</code> (const std::string &amp;name) const<br />
 <i>Find the class which contains the attribute &#8216;name&#8217;. </i><br />
 virtual int <code>getAttrFlag</code> (const std::string &amp;name) const<br />
 <i>Find the flag for the attribute &#8216;name&#8217;. </i><br />
 void <code>sendSerialno</code> (<code>Atlas::Bridge</code> &amp;) const<br />
 <i>Send the &#8216;serialno&#8217; attribute to an </i><code>Atlas::Bridge</code>.<br />
 void <code>sendRefno</code> (<code>Atlas::Bridge</code> &amp;) const<br />
 <i>Send the &#8216;refno&#8217; attribute to an </i><code>Atlas::Bridge</code>.<br />
 void <code>sendFrom</code> (<code>Atlas::Bridge</code> &amp;) const<br />
 <i>Send the &#8216;from&#8217; attribute to an </i><code>Atlas::Bridge</code>.<br />
 void <code>sendTo</code> (<code>Atlas::Bridge</code> &amp;) const<br />
 <i>Send the &#8216;to&#8217; attribute to an </i><code>Atlas::Bridge</code>.<br />
 void <code>sendSeconds</code> (<code>Atlas::Bridge</code> &amp;) const<br />
 <i>Send the &#8216;seconds&#8217; attribute to an </i><code>Atlas::Bridge</code>.<br />
 void <code>sendFutureSeconds</code> (<code>Atlas::Bridge</code> &amp;) const<br />
 <i>Send the &#8216;future_seconds&#8217; attribute to an </i><code>Atlas::Bridge</code>.<br />
 void <code>sendArgs</code> (<code>Atlas::Bridge</code> &amp;) const<br />
 <i>Send the &#8216;args&#8217; attribute to an </i><code>Atlas::Bridge</code>.<br />
 virtual void <code>iterate</code> (int &amp;current_class, std::string &amp;attr) const<br />
 <i>Iterate over the attributes of this instance. </i></p>
<h3>Protected Attributes</h3>
<p>long <code>attr_serialno</code><br />
 <i>Serial number. </i><br />
 long <code>attr_refno</code><br />
 <i>Reference to serial number. </i><br />
 std::string <code>attr_from</code><br />
 <i>Source of message/operation. </i><br />
 std::string <code>attr_to</code><br />
 <i>Target of message/operation. </i><br />
 double <code>attr_seconds</code><br />
 <i>Time in seconds. </i><br />
 double <code>attr_future_seconds</code><br />
 <i>Time in seconds to add current time. </i><br />
 std::vector&lt; Root &gt; <code>attr_args</code><br />
 <i>List of arguments this operation has. </i></p>
<h2>Detailed Description</h2>
<p>Base operation for all operators. </p>
<p> This is base operation for all other operations and defines basic attributes. You can use this as starting point for browsing whole operation hiearchy. refno refers to operation this is reply for. In examples all attributes that are just as examples (and thus world specific) are started with &#8216;e_&#8217;.</p>
<h2>Member Function Documentation</h2>
<h3>static <code>RootOperationData</code>* Atlas::Objects::Operation::RootOperationData::alloc () [static]</h3>
<p>Allocate a new instance of this class, using an existing instance if available. </p>
<p> This is the key function for implementing the memory pool for the <code>Atlas::Objects</code> API. </p>
<p> Reimplemented from <code>Atlas::Objects::RootData</code>. </p>
<p> Reimplemented in <code>Atlas::Objects::Operation::GenericData</code>, <code>Atlas::Objects::Operation::ActionData</code>, <code>Atlas::Objects::Operation::CreateData</code>, <code>Atlas::Objects::Operation::CombineData</code>, <code>Atlas::Objects::Operation::DivideData</code>, <code>Atlas::Objects::Operation::CommunicateData</code>, <code>Atlas::Objects::Operation::TalkData</code>, <code>Atlas::Objects::Operation::DeleteData</code>, <code>Atlas::Objects::Operation::SetData</code>, <code>Atlas::Objects::Operation::AffectData</code>, <code>Atlas::Objects::Operation::MoveData</code>, <code>Atlas::Objects::Operation::WieldData</code>, <code>Atlas::Objects::Operation::GetData</code>, <code>Atlas::Objects::Operation::PerceiveData</code>, <code>Atlas::Objects::Operation::LookData</code>, <code>Atlas::Objects::Operation::ListenData</code>, <code>Atlas::Objects::Operation::SniffData</code>, <code>Atlas::Objects::Operation::TouchData</code>, <code>Atlas::Objects::Operation::LoginData</code>, <code>Atlas::Objects::Operation::LogoutData</code>, <code>Atlas::Objects::Operation::ImaginaryData</code>, <code>Atlas::Objects::Operation::UseData</code>, <code>Atlas::Objects::Operation::InfoData</code>, <code>Atlas::Objects::Operation::PerceptionData</code>, <code>Atlas::Objects::Operation::SightData</code>, <code>Atlas::Objects::Operation::AppearanceData</code>, <code>Atlas::Objects::Operation::DisappearanceData</code>, <code>Atlas::Objects::Operation::SoundData</code>, <code>Atlas::Objects::Operation::SmellData</code>, <code>Atlas::Objects::Operation::FeelData</code>, and <code>Atlas::Objects::Operation::ErrorData</code>.</p>
<h3>virtual int Atlas::Objects::Operation::RootOperationData::copyAttr (const std::string &amp; name, <code>Atlas::Message::Element</code> &amp; attr) const [virtual]</h3>
<p>Retrieve the attribute &#8216;name&#8217;. </p>
<p> Return non-zero if it does not exist. </p>
<p> Reimplemented from <code>Atlas::Objects::RootData</code>.</p>
<h3>virtual void Atlas::Objects::Operation::RootOperationData::free () [virtual]</h3>
<p>Free an instance of this class, returning it to the memory pool. </p>
<p> This function in combination with <code>alloc()</code> handle the memory pool. </p>
<p> Reimplemented from <code>Atlas::Objects::RootData</code>. </p>
<p> Reimplemented in <code>Atlas::Objects::Operation::GenericData</code>, <code>Atlas::Objects::Operation::ActionData</code>, <code>Atlas::Objects::Operation::CreateData</code>, <code>Atlas::Objects::Operation::CombineData</code>, <code>Atlas::Objects::Operation::DivideData</code>, <code>Atlas::Objects::Operation::CommunicateData</code>, <code>Atlas::Objects::Operation::TalkData</code>, <code>Atlas::Objects::Operation::DeleteData</code>, <code>Atlas::Objects::Operation::SetData</code>, <code>Atlas::Objects::Operation::AffectData</code>, <code>Atlas::Objects::Operation::MoveData</code>, <code>Atlas::Objects::Operation::WieldData</code>, <code>Atlas::Objects::Operation::GetData</code>, <code>Atlas::Objects::Operation::PerceiveData</code>, <code>Atlas::Objects::Operation::LookData</code>, <code>Atlas::Objects::Operation::ListenData</code>, <code>Atlas::Objects::Operation::SniffData</code>, <code>Atlas::Objects::Operation::TouchData</code>, <code>Atlas::Objects::Operation::LoginData</code>, <code>Atlas::Objects::Operation::LogoutData</code>, <code>Atlas::Objects::Operation::ImaginaryData</code>, <code>Atlas::Objects::Operation::UseData</code>, <code>Atlas::Objects::Operation::InfoData</code>, <code>Atlas::Objects::Operation::PerceptionData</code>, <code>Atlas::Objects::Operation::SightData</code>, <code>Atlas::Objects::Operation::AppearanceData</code>, <code>Atlas::Objects::Operation::DisappearanceData</code>, <code>Atlas::Objects::Operation::SoundData</code>, <code>Atlas::Objects::Operation::SmellData</code>, <code>Atlas::Objects::Operation::FeelData</code>, and <code>Atlas::Objects::Operation::ErrorData</code>.</p>
<h3>virtual <code>RootOperationData</code>* Atlas::Objects::Operation::RootOperationData::getDefaultObject () [virtual]</h3>
<p>Get the reference object that contains the default values for attributes of instances of the same class as this object. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>a pointer to the default object.</dl>
<p> Reimplemented from <code>Atlas::Objects::RootData</code>. </p>
<p> Reimplemented in <code>Atlas::Objects::Operation::GenericData</code>, <code>Atlas::Objects::Operation::ActionData</code>, <code>Atlas::Objects::Operation::CreateData</code>, <code>Atlas::Objects::Operation::CombineData</code>, <code>Atlas::Objects::Operation::DivideData</code>, <code>Atlas::Objects::Operation::CommunicateData</code>, <code>Atlas::Objects::Operation::TalkData</code>, <code>Atlas::Objects::Operation::DeleteData</code>, <code>Atlas::Objects::Operation::SetData</code>, <code>Atlas::Objects::Operation::AffectData</code>, <code>Atlas::Objects::Operation::MoveData</code>, <code>Atlas::Objects::Operation::WieldData</code>, <code>Atlas::Objects::Operation::GetData</code>, <code>Atlas::Objects::Operation::PerceiveData</code>, <code>Atlas::Objects::Operation::LookData</code>, <code>Atlas::Objects::Operation::ListenData</code>, <code>Atlas::Objects::Operation::SniffData</code>, <code>Atlas::Objects::Operation::TouchData</code>, <code>Atlas::Objects::Operation::LoginData</code>, <code>Atlas::Objects::Operation::LogoutData</code>, <code>Atlas::Objects::Operation::ImaginaryData</code>, <code>Atlas::Objects::Operation::UseData</code>, <code>Atlas::Objects::Operation::InfoData</code>, <code>Atlas::Objects::Operation::PerceptionData</code>, <code>Atlas::Objects::Operation::SightData</code>, <code>Atlas::Objects::Operation::AppearanceData</code>, <code>Atlas::Objects::Operation::DisappearanceData</code>, <code>Atlas::Objects::Operation::SoundData</code>, <code>Atlas::Objects::Operation::SmellData</code>, <code>Atlas::Objects::Operation::FeelData</code>, and <code>Atlas::Objects::Operation::ErrorData</code>.</p>
<h3>static <code>RootOperationData</code>* Atlas::Objects::Operation::RootOperationData::getDefaultObjectInstance () [static]</h3>
<p>Get the reference object that contains the default values for attributes of instances of this class. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>a pointer to the default object.</dl>
<p> Reimplemented from <code>Atlas::Objects::RootData</code>. </p>
<p> Reimplemented in <code>Atlas::Objects::Operation::GenericData</code>, <code>Atlas::Objects::Operation::ActionData</code>, <code>Atlas::Objects::Operation::CreateData</code>, <code>Atlas::Objects::Operation::CombineData</code>, <code>Atlas::Objects::Operation::DivideData</code>, <code>Atlas::Objects::Operation::CommunicateData</code>, <code>Atlas::Objects::Operation::TalkData</code>, <code>Atlas::Objects::Operation::DeleteData</code>, <code>Atlas::Objects::Operation::SetData</code>, <code>Atlas::Objects::Operation::AffectData</code>, <code>Atlas::Objects::Operation::MoveData</code>, <code>Atlas::Objects::Operation::WieldData</code>, <code>Atlas::Objects::Operation::GetData</code>, <code>Atlas::Objects::Operation::PerceiveData</code>, <code>Atlas::Objects::Operation::LookData</code>, <code>Atlas::Objects::Operation::ListenData</code>, <code>Atlas::Objects::Operation::SniffData</code>, <code>Atlas::Objects::Operation::TouchData</code>, <code>Atlas::Objects::Operation::LoginData</code>, <code>Atlas::Objects::Operation::LogoutData</code>, <code>Atlas::Objects::Operation::ImaginaryData</code>, <code>Atlas::Objects::Operation::UseData</code>, <code>Atlas::Objects::Operation::InfoData</code>, <code>Atlas::Objects::Operation::PerceptionData</code>, <code>Atlas::Objects::Operation::SightData</code>, <code>Atlas::Objects::Operation::AppearanceData</code>, <code>Atlas::Objects::Operation::DisappearanceData</code>, <code>Atlas::Objects::Operation::SoundData</code>, <code>Atlas::Objects::Operation::SmellData</code>, <code>Atlas::Objects::Operation::FeelData</code>, and <code>Atlas::Objects::Operation::ErrorData</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Atlas-C++ from the source code.</p>
