---
title: "atlas_objects_dispatcher(3)"
name: "atlas_objects_dispatcher"
section: "3"
letter: "a"
url: "/docs/linux/man/3-atlas_objects_dispatcher/"
description: "Atlas::Objects::Dispatcher – Objects hierarchy dispatcher."
---

<p>Atlas::Objects::Dispatcher &#8211; <code>Objects</code> hierarchy dispatcher. </p>
<h2>Synopsis</h2>
<p>#include &lt;<a href="file:/usr/include/Dispatcher.h">Dispatcher.h</a>&gt; </p>
<p> Inherits <code>Atlas::Objects::ObjectsDecoder</code>. </p>
<h3>Public Member Functions</h3>
<p>virtual <code>~Dispatcher</code> ()<br />
 <i>Default destructor. </i><br />
 void <code>addMethod</code> (int, objectArrivedPtr method)<br />
 <i>Add a new method for </i><code>Objects</code> class defined by application.</p>
<h3>Protected Member Functions</h3>
<p>virtual void <code>unknownObjectArrived</code> (const Root &amp;)<br />
 <i>An unknown object has arrived. </i><br />
 virtual void <code>objectArrived</code> (const Root &amp;)<br />
 <i>An object has arrived for dispatch. </i><br />
 virtual void <code>dispatchObject</code> (const Root &amp;obj)<br />
 <i>call right object*Arrived method </i><br />
 virtual void <code>objectRootArrived</code> (const Root &amp;)<br />
 <i>Override this to get called when a Root object arrives. </i><br />
 virtual void <code>objectRootEntityArrived</code> (const Entity::RootEntity &amp;)<br />
 <i>Override this to get called when a RootEntity object arrives. </i><br />
 virtual void <code>objectAdminEntityArrived</code> (const Entity::AdminEntity &amp;)<br />
 <i>Override this to get called when a AdminEntity object arrives. </i><br />
 virtual void <code>objectAccountArrived</code> (const Entity::Account &amp;)<br />
 <i>Override this to get called when a Account object arrives. </i><br />
 virtual void <code>objectPlayerArrived</code> (const Entity::Player &amp;)<br />
 <i>Override this to get called when a Player object arrives. </i><br />
 virtual void <code>objectAdminArrived</code> (const Entity::Admin &amp;)<br />
 <i>Override this to get called when a Admin object arrives. </i><br />
 virtual void <code>objectGameArrived</code> (const Entity::Game &amp;)<br />
 <i>Override this to get called when a Game object arrives. </i><br />
 virtual void <code>objectGameEntityArrived</code> (const Entity::GameEntity &amp;)<br />
 <i>Override this to get called when a GameEntity object arrives. </i><br />
 virtual void <code>objectRootOperationArrived</code> (const Operation::RootOperation &amp;)<br />
 <i>Override this to get called when a RootOperation object arrives. </i><br />
 virtual void <code>objectActionArrived</code> (const Operation::Action &amp;)<br />
 <i>Override this to get called when a Action object arrives. </i><br />
 virtual void <code>objectCreateArrived</code> (const Operation::Create &amp;)<br />
 <i>Override this to get called when a Create object arrives. </i><br />
 virtual void <code>objectCombineArrived</code> (const Operation::Combine &amp;)<br />
 <i>Override this to get called when a Combine object arrives. </i><br />
 virtual void <code>objectDivideArrived</code> (const Operation::Divide &amp;)<br />
 <i>Override this to get called when a Divide object arrives. </i><br />
 virtual void <code>objectCommunicateArrived</code> (const Operation::Communicate &amp;)<br />
 <i>Override this to get called when a Communicate object arrives. </i><br />
 virtual void <code>objectTalkArrived</code> (const Operation::Talk &amp;)<br />
 <i>Override this to get called when a Talk object arrives. </i><br />
 virtual void <code>objectDeleteArrived</code> (const Operation::Delete &amp;)<br />
 <i>Override this to get called when a Delete object arrives. </i><br />
 virtual void <code>objectSetArrived</code> (const Operation::Set &amp;)<br />
 <i>Override this to get called when a Set object arrives. </i><br />
 virtual void <code>objectAffectArrived</code> (const Operation::Affect &amp;)<br />
 <i>Override this to get called when a Affect object arrives. </i><br />
 virtual void <code>objectMoveArrived</code> (const Operation::Move &amp;)<br />
 <i>Override this to get called when a Move object arrives. </i><br />
 virtual void <code>objectWieldArrived</code> (const Operation::Wield &amp;)<br />
 <i>Override this to get called when a Wield object arrives. </i><br />
 virtual void <code>objectGetArrived</code> (const Operation::Get &amp;)<br />
 <i>Override this to get called when a Get object arrives. </i><br />
 virtual void <code>objectPerceiveArrived</code> (const Operation::Perceive &amp;)<br />
 <i>Override this to get called when a Perceive object arrives. </i><br />
 virtual void <code>objectLookArrived</code> (const Operation::Look &amp;)<br />
 <i>Override this to get called when a Look object arrives. </i><br />
 virtual void <code>objectListenArrived</code> (const Operation::Listen &amp;)<br />
 <i>Override this to get called when a Listen object arrives. </i><br />
 virtual void <code>objectSniffArrived</code> (const Operation::Sniff &amp;)<br />
 <i>Override this to get called when a Sniff object arrives. </i><br />
 virtual void <code>objectTouchArrived</code> (const Operation::Touch &amp;)<br />
 <i>Override this to get called when a Touch object arrives. </i><br />
 virtual void <code>objectLoginArrived</code> (const Operation::Login &amp;)<br />
 <i>Override this to get called when a Login object arrives. </i><br />
 virtual void <code>objectLogoutArrived</code> (const Operation::Logout &amp;)<br />
 <i>Override this to get called when a Logout object arrives. </i><br />
 virtual void <code>objectImaginaryArrived</code> (const Operation::Imaginary &amp;)<br />
 <i>Override this to get called when a Imaginary object arrives. </i><br />
 virtual void <code>objectUseArrived</code> (const Operation::Use &amp;)<br />
 <i>Override this to get called when a Use object arrives. </i><br />
 virtual void <code>objectInfoArrived</code> (const Operation::Info &amp;)<br />
 <i>Override this to get called when a Info object arrives. </i><br />
 virtual void <code>objectPerceptionArrived</code> (const Operation::Perception &amp;)<br />
 <i>Override this to get called when a Perception object arrives. </i><br />
 virtual void <code>objectSightArrived</code> (const Operation::Sight &amp;)<br />
 <i>Override this to get called when a Sight object arrives. </i><br />
 virtual void <code>objectAppearanceArrived</code> (const Operation::Appearance &amp;)<br />
 <i>Override this to get called when a Appearance object arrives. </i><br />
 virtual void <code>objectDisappearanceArrived</code> (const Operation::Disappearance &amp;)<br />
 <i>Override this to get called when a Disappearance object arrives. </i><br />
 virtual void <code>objectSoundArrived</code> (const Operation::Sound &amp;)<br />
 <i>Override this to get called when a Sound object arrives. </i><br />
 virtual void <code>objectSmellArrived</code> (const Operation::Smell &amp;)<br />
 <i>Override this to get called when a Smell object arrives. </i><br />
 virtual void <code>objectFeelArrived</code> (const Operation::Feel &amp;)<br />
 <i>Override this to get called when a Feel object arrives. </i><br />
 virtual void <code>objectErrorArrived</code> (const Operation::Error &amp;)<br />
 <i>Override this to get called when a Error object arrives. </i><br />
 virtual void <code>objectAnonymousArrived</code> (const Entity::Anonymous &amp;)<br />
 <i>Override this to get called when a Anonymous object arrives. </i><br />
 virtual void <code>objectGenericArrived</code> (const Operation::Generic &amp;)<br />
 <i>Override this to get called when a Generic object arrives. </i></p>
<h3>Protected Attributes</h3>
<p>methodMap_t <code>m_methods</code><br />
 <i>Store extension methods for </i><code>Objects</code> classes defined by application.</p>
<h2>Detailed Description</h2>
<p><code>Objects</code> hierarchy dispatcher. </p>
<p> This dispatcher can be bound to a codec, will assemble incoming messages, check their type, convert them into the appropriate instance in the <code>Objects</code> hierarchy and call the relevant member functions, which subclasses can conveniently override to pick up the object. </p>
<p> <code>See also:</code></p>
<dl COMPACT>
<dd>Atlas::Objects::Encoder</dl>
<p> <code>Author:</code></p>
<dl COMPACT>
<dd>Stefanus Du Toit &lt;sdt [at] gmx.net&gt;</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Atlas-C++ from the source code.</p>
