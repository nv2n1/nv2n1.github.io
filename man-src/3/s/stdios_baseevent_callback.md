---
title: "stdios_baseevent_callback(3)"
name: "stdios_baseevent_callback"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdios_baseevent_callback/"
description: "std::ios_base::event_callback – std::ios_base::event_callback"
---

<p>std::ios_base::event_callback &#8211; std::ios_base::event_callback</p>
<h2>Synopsis</h2>
<pre><code>typedef void (*event_callback)(event type, ios_base &amp;ios, int index);</code></pre>
<p>The type of function callbacks that can be registered using register_callback() to be called on specific events.<br />
type is a value of type ios_base::event which indicates the type of the event that will invoke this callback.<br />
ios refers to the stream object for which the callback is invoked: *this is passed as the argument when callbacks are invoked by std::ios_base and std::basic_ios member functions.<br />
index is the user-provided value passed to register_callback() when registering the function. </p>
<h2>See also</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;copies formatting information<br />
copyfmt <i>(public member function of std::basic_ios&lt;CharT,Traits&gt;)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;sets locale<br />
imbue <i>(public member function)</i><br />
destructor destructs the object<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(virtual public member function)</i><br />
<code>[virtual]</code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;registers event callback function<br />
register_callback <i>(public member function)</i> </p>
