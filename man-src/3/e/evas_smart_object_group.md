---
title: "evas_smart_object_group(3)"
name: "evas_smart_object_group"
section: "3"
letter: "e"
url: "/docs/linux/man/3-evas_smart_object_group/"
description: "Evas Smart Object Functions – Functions dealing with evas smart objects."
---

<p>Evas Smart Object Functions &#8211; Functions dealing with evas smart objects. </p>
<h3>Functions</h3>
<p>EAPI void <code>evas_object_smart_data_set</code> (<code>Evas_Object</code> *obj, void *data)<br />
 <i>Store a pointer to user data for a smart object. </i><br />
 EAPI void * <code>evas_object_smart_data_get</code> (const <code>Evas_Object</code> *obj)<br />
 <i>Retrieve user data stored on a smart object. </i><br />
 EAPI <code>Evas_Smart</code> * <code>evas_object_smart_smart_get</code> (const <code>Evas_Object</code> *obj)<br />
 <i>Get the Evas_Smart from which </i>obj was created.<br />
 EAPI void <code>evas_object_smart_member_add</code> (<code>Evas_Object</code> *obj, <code>Evas_Object</code> *smart_obj)<br />
 <i>Set an evas object as a member of a smart object. </i><br />
 EAPI void <code>evas_object_smart_member_del</code> (<code>Evas_Object</code> *obj)<br />
 <i>Removes a member object from a smart object. </i><br />
 EAPI <code>Evas_Object</code> * <code>evas_object_smart_parent_get</code> (const <code>Evas_Object</code> *obj)<br />
 <i>Gets the smart parent of an Evas_Object. </i><br />
 EAPI <code>Evas_Object</code> * <code>evas_object_smart_add</code> (<code>Evas</code> *e, <code>Evas_Smart</code> *s)<br />
 <i>Instantiates a new smart object described by </i>s.<br />
 EAPI void <code>evas_object_smart_callback_add</code> (<code>Evas_Object</code> *obj, const char *event, void(*func)(void *data, <code>Evas_Object</code> *obj, void *event_info), const void *data)<br />
 <i>Add a callback for the smart event specified by </i>event.<br />
 EAPI void * <code>evas_object_smart_callback_del</code> (<code>Evas_Object</code> *obj, const char *event, void(*func)(void *data, <code>Evas_Object</code> *obj, void *event_info))<br />
 <i>Remove a smart callback. </i><br />
 EAPI void <code>evas_object_smart_callback_call</code> (<code>Evas_Object</code> *obj, const char *event, void *event_info)<br />
 <i>Call any smart callbacks on </i>obj for event.<br />
 EAPI void <code>evas_object_smart_need_recalculate_set</code> (<code>Evas_Object</code> *obj, Evas_Bool value)<br />
 <i>Set the need_recalculate flag of given smart object. </i><br />
 EAPI Evas_Bool <code>evas_object_smart_need_recalculate_get</code> (<code>Evas_Object</code> *obj)<br />
 <i>Get the current value of need_recalculate flag. </i><br />
 EAPI void <code>evas_object_smart_calculate</code> (<code>Evas_Object</code> *obj)<br />
 <i>Call user provided calculate() and unset need_calculate. </i><br />
 EAPI void <code>evas_object_smart_changed</code> (<code>Evas_Object</code> *obj)<br />
 <i>Mark smart object as changed, dirty. </i><br />
 EAPI void <code>evas_object_smart_move_children_relative</code> (<code>Evas_Object</code> *obj, Evas_Coord dx, Evas_Coord dy)<br />
 <i>Moves all children objects relative to given offset. </i><br />
 EAPI <code>Evas_Object</code> * <code>evas_object_smart_clipped_clipper_get</code> (<code>Evas_Object</code> *obj)<br />
 <i>Get the clipper object for the given clipped smart object. </i><br />
 EAPI void <code>evas_object_smart_clipped_member_add</code> (<code>Evas_Object</code> *obj, <code>Evas_Object</code> *member)<br />
 <i>Add the given member to clipped smart object. </i><br />
 EAPI void <code>evas_object_smart_clipped_member_del</code> (<code>Evas_Object</code> *member)<br />
 <i>Remove the given member from clipped smart object. </i><br />
 EAPI void <code>evas_object_smart_clipped_smart_set</code> (<code>Evas_Smart_Class</code> *sc)<br />
 <i>Set smart class callbacks so it implements the &#8216;Clipped Smart Object&#8217;. </i></p>
<h2>Detailed Description</h2>
<p>Functions dealing with evas smart objects. </p>
<p> Smart objects are groupings of primitive evas objects that behave as a cohesive group. For instance, a file manager icon may be a smart object composed of an image object, a text label and two rectangles that appear behind the image and text when the icon is selected. As a smart object, the normal evas api could be used on the icon object.</p>
<h2>Function Documentation</h2>
<h3>EAPI <code>Evas_Object</code>* evas_object_smart_add (<code>Evas</code> * e, <code>Evas_Smart</code> * s)</h3>
<p>Instantiates a new smart object described by s. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>e</i> the evas on which to add the object<br />
 <i>s</i> the Evas_Smart describing the smart object</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>a new Evas_Object</dl>
<h3>EAPI void evas_object_smart_calculate (<code>Evas_Object</code> * obj)</h3>
<p>Call user provided calculate() and unset need_calculate. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> the smart object</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>if flag is set or not.</dl>
<h3>EAPI void evas_object_smart_callback_add (<code>Evas_Object</code> * obj, const char * event, void(*)(void *data, <code>Evas_Object</code> *obj, void *event_info) func, const void * data)</h3>
<p>Add a callback for the smart event specified by event. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> a smart object<br />
 <i>event</i> the event name<br />
 <i>func</i> the callback function<br />
 <i>data</i> user data to be passed to the callback function</dl>
<p> References evas_list_prepend().</p>
<h3>EAPI void evas_object_smart_callback_call (<code>Evas_Object</code> * obj, const char * event, void * event_info)</h3>
<p>Call any smart callbacks on obj for event. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> the smart object<br />
 <i>event</i> the event name<br />
 <i>event_info</i> an event specific struct of info to pass to the callback</dl>
<p> This should be called internally in the smart object when some specific event has occured. The documentation for the smart object should include a list of possible events and what type of event_info to expect. </p>
<p> References _Evas_List::data, and _Evas_List::next.</p>
<h3>EAPI void* evas_object_smart_callback_del (<code>Evas_Object</code> * obj, const char * event, void(*)(void *data, <code>Evas_Object</code> *obj, void *event_info) func)</h3>
<p>Remove a smart callback. </p>
<p> Removes a callback that was added by <code>evas_object_smart_callback_add()</code> </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> a smart object<br />
 <i>event</i> the event name<br />
 <i>func</i> the callback function</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>the data pointer</dl>
<p> References _Evas_List::data, and _Evas_List::next.</p>
<h3>EAPI void evas_object_smart_changed (<code>Evas_Object</code> * obj)</h3>
<p>Mark smart object as changed, dirty. </p>
<p> This will inform the scene that it changed and needs to be redraw, also setting need_recalculate on the given object. </p>
<p> <code>See also:</code></p>
<dl COMPACT>
<dd><code>evas_object_smart_need_recalculate_set()</code>.</dl>
<p> References evas_object_smart_need_recalculate_set().</p>
<h3>EAPI <code>Evas_Object</code>* evas_object_smart_clipped_clipper_get (<code>Evas_Object</code> * obj)</h3>
<p>Get the clipper object for the given clipped smart object. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> the clipped smart object to retrieve the associated clipper.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>the clipper object.</dl>
<p> <code>See also:</code></p>
<dl COMPACT>
<dd>evas_object_smart_clipped_smart_add()</dl>
<p> References evas_object_smart_data_get().</p>
<h3>EAPI void evas_object_smart_clipped_member_add (<code>Evas_Object</code> * obj, <code>Evas_Object</code> * member)</h3>
<p>Add the given member to clipped smart object. </p>
<p> This method is equivalent to <code>evas_object_smart_member_add()</code>, but will do extra work required to have clipped smart object to use the clipper, also shows the clipper if this is the first object and object is visible. </p>
<p> <code>Warning:</code></p>
<dl COMPACT>
<dd>the parameter order is different from <code>evas_object_smart_member_add()</code></dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> the smart object to use.<br />
 <i>member</i> the child/member to add to <i>obj</i></dl>
<p> <code>Todo</code></p>
<dl COMPACT>
<dd>add member_add() callback to Evas_Smart_Class.</dl>
<p> References evas_object_clip_set(), evas_object_show(), evas_object_smart_member_add(), and evas_object_visible_get().</p>
<h3>EAPI void evas_object_smart_clipped_member_del (<code>Evas_Object</code> * member)</h3>
<p>Remove the given member from clipped smart object. </p>
<p> This method is equivalent to <code>evas_object_smart_member_del()</code>, but will do extra work required to have clipped smart object to stop using the clipper, also hide the clipper if this is the last object. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>member</i> the child/member to remove from its parent smart object.</dl>
<p> <code>Todo</code></p>
<dl COMPACT>
<dd>add member_del() callback to Evas_Smart_Class.</dl>
<p> References evas_object_clip_unset(), evas_object_clipees_get(), evas_object_hide(), evas_object_smart_member_del(), and evas_object_smart_parent_get().</p>
<h3>EAPI void evas_object_smart_clipped_smart_set (<code>Evas_Smart_Class</code> * sc)</h3>
<p>Set smart class callbacks so it implements the &#8216;Clipped Smart Object&#8217;. </p>
<p> This call will assign all the required methods of Evas_Smart_Class, if one wants to &#8216;subclass&#8217; it, call this function and later override values, if one wants to call the original method, save it somewhere, example: </p>
<pre> static Evas_Smart_Class parent_sc = {NULL};
 static void my_class_smart_add(Evas_Object *o)
 {
 parent_sc.add(o);
 evas_object_color_set(evas_object_smart_clipped_clipper_get(o),
 255, 0, 0, 255);
 }
 Evas_Smart_Class *my_class_new(void)
 {
 static Evas_Smart_Class sc = {'MyClass'};
 if (parent_sc.name)
 {
 evas_object_smart_clipped_smart_set(&amp;sc);
 parent_sc = sc;
 sc.add = my_class_smart_add;
 }
 return &amp;sc;
 }</pre>
<p>Default behavior is:</p>
<dl COMPACT>
<dt>*</p>
<dd>add: creates a hidden clipper with &#8216;infinite&#8217; size;</p>
<dt>*</p>
<dd>del: delete all children objects;</p>
<dt>*</p>
<dd>move: move all objects relative relatively;</p>
<dt>*</p>
<dd>resize: not defined;</p>
<dt>*</p>
<dd>show: if there are children objects, show clipper;</p>
<dt>*</p>
<dd>hide: hides clipper;</p>
<dt>*</p>
<dd>color_set: set the color of clipper;</p>
<dt>*</p>
<dd>clip_set: set clipper of clipper;</p>
<dt>*</p>
<dd>clip_unset: unset the clipper of clipper;</dl>
<h3>EAPI void* evas_object_smart_data_get (const <code>Evas_Object</code> * obj)</h3>
<p>Retrieve user data stored on a smart object. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The smart object</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>A pointer to data stored using <code>evas_object_smart_data_set()</code>, or NULL if none has been set.</dl>
<p> Referenced by evas_object_smart_clipped_clipper_get().</p>
<h3>EAPI void evas_object_smart_data_set (<code>Evas_Object</code> * obj, void * data)</h3>
<p>Store a pointer to user data for a smart object. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The smart object<br />
 <i>data</i> A pointer to user data</dl>
<h3>EAPI void evas_object_smart_member_add (<code>Evas_Object</code> * obj, <code>Evas_Object</code> * smart_obj)</h3>
<p>Set an evas object as a member of a smart object. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The member object<br />
 <i>smart_obj</i> The smart object</dl>
<p> Members will automatically be stacked and layered with the smart object. The various stacking function will operate on members relative to the other members instead of the entire canvas. </p>
<p> Non-member objects can not interleave a smart object&#8217;s members. </p>
<p> References evas_object_smart_member_del(). </p>
<p> Referenced by evas_object_smart_clipped_member_add().</p>
<h3>EAPI void evas_object_smart_member_del (<code>Evas_Object</code> * obj)</h3>
<p>Removes a member object from a smart object. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> the member object</dl>
<p> This removes a member object from a smart object. The object will still be on the canvas, but no longer associated with whichever smart object it was associated with. </p>
<p> Referenced by evas_object_smart_clipped_member_del(), and evas_object_smart_member_add().</p>
<h3>EAPI void evas_object_smart_move_children_relative (<code>Evas_Object</code> * obj, Evas_Coord dx, Evas_Coord dy)</h3>
<p>Moves all children objects relative to given offset. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> the smart evas object to use.<br />
 <i>dx</i> horizontal offset.<br />
 <i>dy</i> vertical offset.</dl>
<p> References _Evas_List::data, evas_list_free(), evas_object_geometry_get(), evas_object_move(), and _Evas_List::next.</p>
<h3>EAPI Evas_Bool evas_object_smart_need_recalculate_get (<code>Evas_Object</code> * obj)</h3>
<p>Get the current value of need_recalculate flag. </p>
<p> <code>Note:</code></p>
<dl COMPACT>
<dd>this flag will be unset during the render phase, after calculate() is called if one is provided. If no calculate() is provided, then the flag will be left unchanged after render phase.</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> the smart object</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>if flag is set or not.</dl>
<h3>EAPI void evas_object_smart_need_recalculate_set (<code>Evas_Object</code> * obj, Evas_Bool value)</h3>
<p>Set the need_recalculate flag of given smart object. </p>
<p> If this flag is set then calculate() callback (method) of the given smart object will be called, if one is provided, during render phase usually <code>evas_render()</code>. After this step, this flag will be automatically unset. </p>
<p> If no calculate() is provided, this flag will be left unchanged. </p>
<p> <code>Note:</code></p>
<dl COMPACT>
<dd>just setting this flag will not make scene dirty and <code>evas_render()</code> will have no effect. To do that, use <code>evas_object_smart_changed()</code>, that will automatically call this function with 1 as parameter.</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> the smart object<br />
 <i>value</i> if one want to set or unset the need_recalculate flag.</dl>
<p> Referenced by evas_object_smart_changed().</p>
<h3>EAPI <code>Evas_Object</code>* evas_object_smart_parent_get (const <code>Evas_Object</code> * obj)</h3>
<p>Gets the smart parent of an Evas_Object. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> the Evas_Object you want to get the parent</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Returns the smart parent of <i>obj</i>, or NULL if <i>obj</i> is not a smart member of another Evas_Object</dl>
<p> Referenced by evas_object_smart_clipped_member_del().</p>
<h3>EAPI <code>Evas_Smart</code>* evas_object_smart_smart_get (const <code>Evas_Object</code> * obj)</h3>
<p>Get the Evas_Smart from which obj was created. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> a smart object</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>the Evas_Smart</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Evas from the source code.</p>
