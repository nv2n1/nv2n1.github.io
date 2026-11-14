---
title: "evas_object_event_flags_group(3)"
name: "evas_object_event_flags_group"
section: "3"
letter: "e"
url: "/docs/linux/man/3-evas_object_event_flags_group/"
description: "Evas Object Event Flag Functions – Functions that deal with how events on an Evas Object are processed."
---

<p>Evas Object Event Flag Functions &#8211; Functions that deal with how events on an Evas Object are processed. </p>
<h3>Functions</h3>
<p>EAPI void <code>evas_object_pass_events_set</code> (<code>Evas_Object</code> *obj, Evas_Bool pass)<br />
 <i>Set an object&#8217;s pass events state. </i><br />
 EAPI Evas_Bool <code>evas_object_pass_events_get</code> (const <code>Evas_Object</code> *obj)<br />
 <i>Determine whether an object is set to pass events. </i><br />
 EAPI void <code>evas_object_repeat_events_set</code> (<code>Evas_Object</code> *obj, Evas_Bool repeat)<br />
 <i>Set an object&#8217;s repeat events state. </i><br />
 EAPI Evas_Bool <code>evas_object_repeat_events_get</code> (const <code>Evas_Object</code> *obj)<br />
 <i>Determine whether an object is set to repeat events. </i><br />
 EAPI void <code>evas_object_propagate_events_set</code> (<code>Evas_Object</code> *obj, Evas_Bool prop)<br />
 <i>Set whether events on a smart member object should propagate to its parent. </i><br />
 EAPI Evas_Bool <code>evas_object_propagate_events_get</code> (const <code>Evas_Object</code> *obj)<br />
 <i>Determine whether an object is set to propagate events. </i></p>
<h2>Detailed Description</h2>
<p>Functions that deal with how events on an Evas Object are processed.</p>
<h2>Function Documentation</h2>
<h3>EAPI Evas_Bool evas_object_pass_events_get (const <code>Evas_Object</code> * obj)</h3>
<p>Determine whether an object is set to pass events. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i></dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>pass events state</dl>
<h3>EAPI void evas_object_pass_events_set (<code>Evas_Object</code> * obj, Evas_Bool pass)</h3>
<p>Set an object&#8217;s pass events state. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> the evas object<br />
 <i>pass</i> whether to pass events or not</dl>
<p> If pass is true, this will cause events on obj to be ignored. They will be triggered on the next lower object (that is not set to pass events) instead. </p>
<p> If pass is false, events will be processed as normal.</p>
<h3>EAPI Evas_Bool evas_object_propagate_events_get (const <code>Evas_Object</code> * obj)</h3>
<p>Determine whether an object is set to propagate events. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i></dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>propogate events state</dl>
<h3>EAPI void evas_object_propagate_events_set (<code>Evas_Object</code> * obj, Evas_Bool prop)</h3>
<p>Set whether events on a smart member object should propagate to its parent. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> the smart member object<br />
 <i>prop</i> wheter to propagate events or not</dl>
<p> This function has no effect if obj is not a member of a smart object. </p>
<p> If prop is true, events occuring on this object will propagate on to the smart object of which obj is a member. </p>
<p> If prop is false, events for which callbacks are set on the member object, obj, will not be passed on to the parent smart object. </p>
<p> The default value is true.</p>
<h3>EAPI Evas_Bool evas_object_repeat_events_get (const <code>Evas_Object</code> * obj)</h3>
<p>Determine whether an object is set to repeat events. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i></dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>repeat events state</dl>
<h3>EAPI void evas_object_repeat_events_set (<code>Evas_Object</code> * obj, Evas_Bool repeat)</h3>
<p>Set an object&#8217;s repeat events state. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> the object<br />
 <i>repeat</i> wheter to repeat events or not</dl>
<p> If repeat is true, this will cause events on obj to trigger callbacks, but also to be repeated on the next lower object in the stack. </p>
<p> If repeat is false, events occuring on obj will be processed normally.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Evas from the source code.</p>
