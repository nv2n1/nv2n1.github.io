---
title: "evas_object_callback_group(3)"
name: "evas_object_callback_group"
section: "3"
letter: "e"
url: "/docs/linux/man/3-evas_object_callback_group/"
description: "Object Callback Functions – Functions that add and remove callbacks to evas objects."
---

<p>Object Callback Functions &#8211; Functions that add and remove callbacks to evas objects. </p>
<h3>Functions</h3>
<p>EAPI void <code>evas_object_event_callback_add</code> (<code>Evas_Object</code> *obj, <code>Evas_Callback_Type</code> type, void(*func)(void *data, <code>Evas</code> *e, <code>Evas_Object</code> *obj, void *event_info), const void *data)<br />
 <i>Add a callback function to an object. </i><br />
 EAPI void * <code>evas_object_event_callback_del</code> (<code>Evas_Object</code> *obj, <code>Evas_Callback_Type</code> type, void(*func)(void *data, <code>Evas</code> *e, <code>Evas_Object</code> *obj, void *event_info))<br />
 <i>Delete a callback function from an object. </i><br />
 EAPI void * <code>evas_object_event_callback_del_full</code> (<code>Evas_Object</code> *obj, <code>Evas_Callback_Type</code> type, void(*func)(void *data, <code>Evas</code> *e, <code>Evas_Object</code> *obj, void *event_info), const void *data)<br />
 <i>Delete a callback function from an object. </i></p>
<h2>Detailed Description</h2>
<p>Functions that add and remove callbacks to evas objects.</p>
<h2>Function Documentation</h2>
<h3>EAPI void evas_object_event_callback_add (<code>Evas_Object</code> * obj, <code>Evas_Callback_Type</code> type, void(*)(void *data, <code>Evas</code> *e, <code>Evas_Object</code> *obj, void *event_info) func, const void * data)</h3>
<p>Add a callback function to an object. </p>
<p> <code>Todo</code></p>
<dl COMPACT>
<dd>Move this next code example and most of the documentation for this next function into the group documentation.</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> Object to attach a callback to<br />
 <i>type</i> The type of event that will trigger the callback<br />
 <i>func</i> The function to be called when the event is triggered<br />
 <i>data</i> The data pointer to be passed to func</dl>
<p> This function adds a function callback to an object when the event of type type occurs on object obj. The function is func. </p>
<p> In the event of a memory allocation error during addition of the callback to the object, <code>evas_alloc_error()</code> should be used to determine the nature of the error, if any, and the program should sensibly try and recover. </p>
<p> The function will be passed the pointer data when it is called. A callback function must look like this: </p>
<pre> void callback (void *data, Evas *e, Evas_Object *obj, void *event_info);</pre>
<p>The first parameter data in this function will be the same value passed to <code>evas_object_event_callback_add()</code> as the data parameter. The second parameter is a convenience for the programmer to know what evas canvas the event occured on. The third parameter obj is the Object handle on which the event occured. The foruth parameter event_info is a pointer to a data structure that may or may not be passed to the callback, depending on the event type that triggered the callback. </p>
<p> The event type type to trigger the function may be one of EVAS_CALLBACK_MOUSE_IN, EVAS_CALLBACK_MOUSE_OUT, EVAS_CALLBACK_MOUSE_DOWN, EVAS_CALLBACK_MOUSE_UP, EVAS_CALLBACK_MOUSE_MOVE, EVAS_CALLBACK_MOUSE_WHEEL, EVAS_CALLBACK_FREE, EVAS_CALLBACK_KEY_DOWN, EVAS_CALLBACK_KEY_UP, EVAS_CALLBACK_FOCUS_IN, EVAS_CALLBACK_FOCUS_OUT, EVAS_CALLBACK_SHOW, EVAS_CALLBACK_HIDE, EVAS_CALLBACK_MOVE, EVAS_CALLBACK_RESIZE or EVAS_CALLBACK_RESTACK. This determines the kind of event that will trigger the callback to be called. The event_info pointer passed to the callback will be one of the following, depending on the event triggering it: </p>
<p> EVAS_CALLBACK_MOUSE_IN: event_info = pointer to Evas_Event_Mouse_In </p>
<p> This event is triggered when the mouse pointer enters the region of the object obj. This may occur by the mouse pointer being moved by <code>evas_event_feed_mouse_move()</code> or evas_event_feed_mouse_move_data() calls, or by the object being shown, raised, moved, resized, or other objects being moved out of the way, hidden, lowered or moved out of the way. </p>
<p> EVAS_CALLBACK_MOUSE_OUT: event_info = pointer to Evas_Event_Mouse_Out </p>
<p> This event is triggered exactly like EVAS_CALLBACK_MOUSE_IN is, but occurs when the mouse pointer exits an object. Note that no out events will be reported if the mouse pointer is implicitly grabbed to an object (the mouse buttons are down at all and any were pressed on that object). An out event will be reported as soon as the mouse is no longer grabbed (no mouse buttons are depressed). Out events will be reported once all buttons are released, if the mouse has left the object. </p>
<p> EVAS_CALLBACK_MOUSE_DOWN: event_info = pointer to Evas_Event_Mouse_Down </p>
<p> This event is triggered by a mouse button being depressed while over an object. If pointermode is EVAS_OBJECT_POINTER_MODE_AUTOGRAB (default) this causes this object to passively grab the mouse until all mouse buttons have been released. That means if this mouse button is the first to be pressed, all future mouse events will be reported to only this object until no buttons are down. That includes mouse move events, in and out events, and further button presses. When all buttons are released, event propagation occurs as normal. </p>
<p> EVAS_CALLBACK_MOUSE_UP: event_info = pointer to Evas_Event_Mouse_Up </p>
<p> This event is triggered by a mouse button being released while over an object or when passively grabbed to an object. If this is the last mouse button to be raised on an object then the passive grab is released and event processing will continue as normal. </p>
<p> EVAS_CALLBACK_MOUSE_MOVE: event_info = pointer to Evas_Event_Mouse_Move </p>
<p> This event is triggered by the mouse pointer moving while over an object or passively grabbed to an object. </p>
<p> EVAS_CALLBACK_MOUSE_WHEEL: event_info = pointer to Evas_Event_Mouse_Wheel </p>
<p> This event is triggered by the mouse wheel being rolled while over an object or passively grabbed to an object. </p>
<p> EVAS_CALLBACK_FREE: event_info = NULL </p>
<p> This event is triggered just before Evas is about to free all memory used by an object and remove all references to it. This is useful for programs to use if they attached data to an object and want to free it when the object is deleted. The object is still valid when this callback is called, but after this callback returns, there is no guarantee on the object&#8217;s validity. </p>
<p> EVAS_CALLBACK_KEY_DOWN: event_info = pointer to Evas_Event_Key_Down </p>
<p> This callback is called when a key is pressed and the focus is on the object, or a key has been grabbed to a particular object which wants to intercept the key press regardless of what object has the focus. </p>
<p> EVAS_CALLBACK_KEY_UP: event_info = pointer to Evas_Event_Key_Up </p>
<p> This callback is called when a key is released and the focus is on the object, or a key has been grabbed to a particular object which wants to intercept the key release regardless of what object has the focus. </p>
<p> EVAS_CALLBACK_FOCUS_IN: event_info = NULL </p>
<p> This event is called when an object gains the focus. When the callback is called the object has already gained the focus. </p>
<p> EVAS_CALLBACK_FOCUS_OUT: event_info = NULL </p>
<p> This event is triggered by an object losing the focus. When the callback is called the object has already lost the focus. </p>
<p> EVAS_CALLBACK_SHOW: event_info = NULL </p>
<p> This event is triggered by the object being shown by <code>evas_object_show()</code>. </p>
<p> EVAS_CALLBACK_HIDE: event_info = NULL </p>
<p> This event is triggered by an object being hidden by <code>evas_object_hide()</code>. </p>
<p> EVAS_CALLBACK_MOVE: event_info = NULL </p>
<p> This event is triggered by an object being moved. <code>evas_object_move()</code> can trigger this, as can any object-specific manipulations that would mean the object&#8217;s origin could move. </p>
<p> EVAS_CALLBACK_RESIZE: event_info = NULL </p>
<p> This event is triggered by an object being resized. Resizes can be triggered by <code>evas_object_resize()</code> or by any object-specific calls that may cause the object to resize. </p>
<p> Example: </p>
<pre> extern Evas_Object *object;
 extern void *my_data;
 void down_callback(void *data, Evas *e, Evas_Object *obj, void *event_info);
 void up_callback(void *data, Evas *e, Evas_Object *obj, void *event_info);
 evas_object_event_callback_add(object, EVAS_CALLBACK_MOUSE_UP, up_callback, my_data);
 if (evas_alloc_error() != EVAS_ALLOC_ERROR_NONE)
 {
 fprintf(stderr, 'ERROR: Callback registering failed! Abort!);
 exit(-1);
 }
 evas_object_event_callback_add(object, EVAS_CALLBACK_MOUSE_DOWN, down_callback, my_data);
 if (evas_alloc_error() != EVAS_ALLOC_ERROR_NONE)
 {
 fprintf(stderr, 'ERROR: Callback registering failed! Abort!);
 exit(-1);
 }</pre>
<p>&nbsp;<wbr></p>
<h3>EAPI void* evas_object_event_callback_del (<code>Evas_Object</code> * obj, <code>Evas_Callback_Type</code> type, void(*)(void *data, <code>Evas</code> *e, <code>Evas_Object</code> *obj, void *event_info) func)</h3>
<p>Delete a callback function from an object. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> Object to remove a callback from<br />
 <i>type</i> The type of event that was triggering the callback<br />
 <i>func</i> The function that was to be called when the event was triggered</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The data pointer that was to be passed to the callback</dl>
<p> This function removes the most recently added callback from the object obj which was triggered by the event type type and was calling the function func when triggered. If the removal is successful it will also return the data pointer that was passed to <code>evas_object_event_callback_add()</code> when the callback was added to the object. If not successful NULL will be returned. </p>
<p> Example: </p>
<pre> extern Evas_Object *object;
 void *my_data;
 void up_callback(void *data, Evas *e, Evas_Object *obj, void *event_info);
 my_data = evas_object_event_callback_del(object, EVAS_CALLBACK_MOUSE_UP, up_callback);</pre>
<p>&nbsp;<wbr></p>
<h3>EAPI void* evas_object_event_callback_del_full (<code>Evas_Object</code> * obj, <code>Evas_Callback_Type</code> type, void(*)(void *data, <code>Evas</code> *e, <code>Evas_Object</code> *obj, void *event_info) func, const void * data)</h3>
<p>Delete a callback function from an object. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> Object to remove a callback from<br />
 <i>type</i> The type of event that was triggering the callback<br />
 <i>func</i> The function that was to be called when the event was triggered<br />
 <i>data</i> The data pointer that was to be passed to the callback</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The data pointer that was to be passed to the callback</dl>
<p> This function removes the most recently added callback from the object obj which was triggered by the event type type and was calling the function func with data data when triggered. If the removal is successful it will also return the data pointer that was passed to <code>evas_object_event_callback_add()</code> (that will be the same as the parameter) when the callback was added to the object. If not successful NULL will be returned. </p>
<p> Example: </p>
<pre> extern Evas_Object *object;
 void *my_data;
 void up_callback(void *data, Evas *e, Evas_Object *obj, void *event_info);
 my_data = evas_object_event_callback_del_full(object, EVAS_CALLBACK_MOUSE_UP, up_callback, data);</pre>
<p>&nbsp;<wbr></p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Evas from the source code.</p>
