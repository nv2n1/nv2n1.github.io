---
title: "evas_output_method(3)"
name: "evas_output_method"
section: "3"
letter: "e"
url: "/docs/linux/man/3-evas_output_method/"
description: "Evas Render Engine Functions – Functions that are used to set the render engine for a given function, and then get that engine working."
---

<p>Evas Render Engine Functions &#8211; Functions that are used to set the render engine for a given function, and then get that engine working. </p>
<h3>Functions</h3>
<p>EAPI void <code>evas_output_method_set</code> (<code>Evas</code> *e, int render_method)<br />
 <i>Sets the output engine for the given evas. </i><br />
 EAPI int <code>evas_output_method_get</code> (const <code>Evas</code> *e)<br />
 <i>Retrieves the number of the output engine used for the given evas. </i><br />
 EAPI <code>Evas_Engine_Info</code> * <code>evas_engine_info_get</code> (const <code>Evas</code> *e)<br />
 <i>Retrieves the current render engine info struct from the given evas. </i><br />
 EAPI void <code>evas_engine_info_set</code> (<code>Evas</code> *e, <code>Evas_Engine_Info</code> *info)<br />
 <i>Applies the engine settings for the given evas from the given </i>Evas_Engine_Info structure.<br />
 EAPI int <code>evas_render_method_lookup</code> (const char *name)<br />
 <i>Look up a numeric ID from a string name of a rendering engine. </i><br />
 EAPI <code>Evas_List</code> * <code>evas_render_method_list</code> (void)<br />
 <i>List all the rendering engines compiled into the copy of the Evas library. </i><br />
 EAPI void <code>evas_render_method_list_free</code> (<code>Evas_List</code> *list)<br />
 <i>This function should be called to free a list of engine names. </i></p>
<h2>Detailed Description</h2>
<p>Functions that are used to set the render engine for a given function, and then get that engine working. </p>
<p> The following code snippet shows how they can be used to initialise an evas that uses the X11 software engine: </p>
<pre> Evas *evas;
 Evas_Engine_Info_Software_X11 *einfo;
 extern Display *display;
 extern Window win;
 evas = evas_new();
 evas_output_method_set(evas, evas_render_method_lookup('software_x11'));
 evas_output_size_set(evas, 640, 480);
 evas_output_viewport_set(evas, 0, 0, 640, 480);
 einfo = (Evas_Engine_Info_Software_X11 *)evas_engine_info_get(evas);
 einfo-&gt;info.display = display;
 einfo-&gt;info.visual = DefaultVisual(display, DefaultScreen(display));
 einfo-&gt;info.colormap = DefaultColormap(display, DefaultScreen(display));
 einfo-&gt;info.drawable = win;
 einfo-&gt;info.depth = DefaultDepth(display, DefaultScreen(display));
 evas_engine_info_set(evas, (Evas_Engine_Info *)einfo);</pre>
<p>&nbsp;<wbr></p>
<h2>Function Documentation</h2>
<h3>EAPI <code>Evas_Engine_Info</code>* evas_engine_info_get (const <code>Evas</code> * e)</h3>
<p>Retrieves the current render engine info struct from the given evas. </p>
<p> The returned structure is publicly modifiable. The contents are valid until either <code>evas_engine_info_set</code> or <code>evas_render</code> are called. </p>
<p> This structure does not need to be freed by the caller. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>e</i> The given evas.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>A pointer to the Engine Info structure. NULL is returned if an engine has not yet been assigned.</dl>
<p> References _Evas_Engine_Info::magic.</p>
<h3>EAPI void evas_engine_info_set (<code>Evas</code> * e, <code>Evas_Engine_Info</code> * info)</h3>
<p>Applies the engine settings for the given evas from the given Evas_Engine_Info structure. </p>
<p> To get the Evas_Engine_Info structure to use, call <code>evas_engine_info_get</code> . Do not try to obtain a pointer to an Evas_Engine_Info structure in any other way. </p>
<p> You will need to call this function at least once before you can create objects on an evas or render that evas. Some engines allow their settings to be changed more than once. </p>
<p> Once called, the info pointer should be considered invalid. </p>
<p> Example: </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>e</i> The pointer to the Evas Canvas<br />
 <i>info</i> The pointer to the Engine Info to use</dl>
<p> References _Evas_Engine_Info::magic.</p>
<h3>EAPI int evas_output_method_get (const <code>Evas</code> * e)</h3>
<p>Retrieves the number of the output engine used for the given evas. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>e</i> The given evas.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The ID number of the output engine being used. 0 is returned if there is an error.</dl>
<h3>EAPI void evas_output_method_set (<code>Evas</code> * e, int render_method)</h3>
<p>Sets the output engine for the given evas. </p>
<p> Once the output engine for an evas is set, any attempt to change it will be ignored. The value for render_method can be found using <code>evas_render_method_lookup</code> . </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>e</i> The given evas.<br />
 <i>render_method</i> The numeric engine value to use.</dl>
<p> References _Evas_List::data, and _Evas_List::next.</p>
<h3>EAPI <code>Evas_List</code>* evas_render_method_list (void)</h3>
<p>List all the rendering engines compiled into the copy of the Evas library. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>A linked list whose data members are C strings of engine names</dl>
<p> Calling this will return a handle (pointer) to an Evas linked list. Each node in the linked list will have the data pointer be a (char *) pointer to the string name of the rendering engine available. The strings should never be modified, neither should the list be modified. This list should be cleaned up as soon as the program no longer needs it using <code>evas_render_method_list_free()</code>. If no engines are available from Evas, NULL will be returned. </p>
<p> Example: </p>
<pre> Evas_List *engine_list, *l;
 engine_list = evas_render_method_list();
 if (!engine_list)
 {
 fprintf(stderr, 'ERROR: Evas supports no engines! Exit.);
 exit(-1);
 }
 printf('Availible Evas Engines:);
 for (l = engine_list; l; l = l-&gt;next)
 {
 char *engine_name;
 engine_name = l-&gt;data;
 printf('%s, engine_name);
 }
 evas_render_method_list_free(engine_list);</pre>
<p>&nbsp;<wbr> </p>
<p> References evas_list_append().</p>
<h3>EAPI void evas_render_method_list_free (<code>Evas_List</code> * list)</h3>
<p>This function should be called to free a list of engine names. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>list</i> The Evas_List base pointer for the engine list to be freed</dl>
<p> When this function is called it will free the engine list passed in as list. The list should only be a list of engines generated by calling <code>evas_render_method_list()</code>. If list is NULL, nothing will happen. </p>
<p> Example: </p>
<pre> Evas_List *engine_list, *l;
 engine_list = evas_render_method_list();
 if (!engine_list)
 {
 fprintf(stderr, 'ERROR: Evas supports no engines! Exit.);
 exit(-1);
 }
 printf('Availible Evas Engines:);
 for (l = engine_list; l; l = l-&gt;next)
 {
 char *engine_name;
 engine_name = l-&gt;data;
 printf('%s, engine_name);
 }
 evas_render_method_list_free(engine_list);</pre>
<p>&nbsp;<wbr> </p>
<p> References _Evas_List::data, and evas_list_remove().</p>
<h3>EAPI int evas_render_method_lookup (const char * name)</h3>
<p>Look up a numeric ID from a string name of a rendering engine. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>name</i> The string name of an engine</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>A numeric (opaque) ID for the rendering engine</dl>
<p> This function looks up a numeric return value for the named engine in the string name. This is a normal C string, NUL byte terminated. The name is case sensitive. If the rendering engine is available, a numeric ID for that engine is returned that is not 0. If the engine is not available, 0 is returned, indicating an invalid engine. </p>
<p> The programmer should NEVER rely on the numeric ID of an engine unless it is returned by this function. Programs should NOT be written accessing render method ID&#8217;s directly, without first obtaining it from this function. </p>
<p> Example: </p>
<pre> int engine_id;
 Evas *evas;
 evas = evas_new();
 if (!evas)
 {
 fprintf(stderr, 'ERROR: Canvas creation failed. Fatal error.);
 exit(-1);
 }
 engine_id = evas_render_method_lookup('software_x11');
 if (!engine_id)
 {
 fprintf(stderr, 'ERROR: Requested rendering engine is absent.);
 exit(-1);
 }
 evas_output_method_set(evas, engine_id);</pre>
<p>&nbsp;<wbr></p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Evas from the source code.</p>
