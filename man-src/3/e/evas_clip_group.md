---
title: "evas_clip_group(3)"
name: "evas_clip_group"
section: "3"
letter: "e"
url: "/docs/linux/man/3-evas_clip_group/"
description: "Clip Functions – Functions that manage the clipping of objects by other objects."
---

<p>Clip Functions &#8211; Functions that manage the clipping of objects by other objects. </p>
<h3>Functions</h3>
<p>EAPI void <code>evas_object_clip_set</code> (<code>Evas_Object</code> *obj, <code>Evas_Object</code> *clip)<br />
 <i>Clip one object to another. </i><br />
 EAPI <code>Evas_Object</code> * <code>evas_object_clip_get</code> (const <code>Evas_Object</code> *obj)<br />
 <i>Get the object clipping this one (if any). </i><br />
 EAPI void <code>evas_object_clip_unset</code> (<code>Evas_Object</code> *obj)<br />
 <i>Disable clipping for an object. </i><br />
 EAPI const <code>Evas_List</code> * <code>evas_object_clipees_get</code> (const <code>Evas_Object</code> *obj)<br />
 <i>Return a list of objects currently clipped by a specific object. </i></p>
<h2>Detailed Description</h2>
<p>Functions that manage the clipping of objects by other objects.</p>
<h2>Function Documentation</h2>
<h3>EAPI <code>Evas_Object</code>* evas_object_clip_get (const <code>Evas_Object</code> * obj)</h3>
<p>Get the object clipping this one (if any). </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The object to get the clipper from</dl>
<p> This function returns the the object clipping obj. If obj not being clipped, NULL is returned. The object obj must be a valid object. </p>
<p> See also <code>evas_object_clip_set()</code>, <code>evas_object_clip_unset()</code> and <code>evas_object_clipees_get()</code>. </p>
<p> Example: </p>
<pre> extern Evas_Object *obj;
 Evas_Object *clipper;
 clipper = evas_object_clip_get(obj);
 if (clipper) evas_object_show(clipper);</pre>
<p>&nbsp;<wbr></p>
<h3>EAPI void evas_object_clip_set (<code>Evas_Object</code> * obj, <code>Evas_Object</code> * clip)</h3>
<p>Clip one object to another. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The object to be clipped<br />
 <i>clip</i> The object to clip obj by</dl>
<p> This function will clip the object obj to the area occupied by the object clipper. This means the object obj will only be visible within the area occupied by the clipping object (clip). The color of the object being clipped will be multiplied by the color of the clipping object, so the resulting color for the clipped object is RESULT = (OBJ * CLIP) / (255 * 255) per color element (red, green, blue and alpha). Clipping is recursive, so clip objects may be clipped by other objects, and their color will in tern be multiplied. You may NOT set up circular clipping lists (i.e. object 1 clips object 2 which clips object 1). The behavior of Evas is undefined in this case. Objects which do not clip others are visible as normal, those that clip 1 or more objects become invisible themselves, only affecting what they clip. If an object ceases to have other objects being clipped by it, it will become visible again. The visibility of an object affects the objects that are clipped by it, so if the object clipping others is not shown, the objects clipped will not be shown either. If the object was being clipped by another object when this function is called, it is implicitly removed from the clipper it is being clipped to, and now is made to clip its new clipper. </p>
<p> At the moment the only objects that can validly be used to clip other objects are rectangle objects. All other object types are invalid and the result of using them is undefined. </p>
<p> The clip object clip must be a valid object, but may also be NULL in which case the effect of this function is the same as calling <code>evas_object_clip_unset()</code> on the obj object. </p>
<p> Example: </p>
<pre> extern Evas *evas;
 extern Evas_Object *obj;
 Evas_Object *clipper;
 clipper = evas_object_rectangle_add(evas);
 evas_object_color_set(clipper, 255, 255, 255, 255);
 evas_object_move(clipper, 10, 10);
 evas_object_resize(clipper, 20, 50);
 evas_object_clip_set(obj, clipper);
 evas_object_show(clipper);</pre>
<p>&nbsp;<wbr> </p>
<p> References evas_list_append(), evas_list_remove(), and evas_object_clip_unset(). </p>
<p> Referenced by evas_object_smart_clipped_member_add().</p>
<h3>EAPI void evas_object_clip_unset (<code>Evas_Object</code> * obj)</h3>
<p>Disable clipping for an object. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The object to cease clipping on</dl>
<p> This function disables clipping for the object obj, if it was already clipped. If it wasn&#8217;t, this has no effect. The object obj must be a valid object. </p>
<p> See also <code>evas_object_clip_set()</code>, <code>evas_object_clipees_get()</code> and <code>evas_object_clip_get()</code>. </p>
<p> Example: </p>
<pre> extern Evas_Object *obj;
 Evas_Object *clipper;
 clipper = evas_object_clip_get(obj);
 if (clipper)
 {
 evas_object_clip_unset(obj);
 evas_object_hide(obj);
 }</pre>
<p>&nbsp;<wbr> </p>
<p> References evas_list_remove(). </p>
<p> Referenced by evas_object_clip_set(), evas_object_del(), and evas_object_smart_clipped_member_del().</p>
<h3>EAPI const <code>Evas_List</code>* evas_object_clipees_get (const <code>Evas_Object</code> * obj)</h3>
<p>Return a list of objects currently clipped by a specific object. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The object to get a list of clippees from</dl>
<p> This returns the inernal list handle that contains all objects clipped by the object obj. If none are clipped, it returns NULL. This list is only valid until the clip list is changed and should be fetched again with another call to <code>evas_object_clipees_get()</code> if any objects being clipped by this object are unclipped, clipped by a new object, are deleted or the clipper is deleted. These operations will invalidate the list returned so it should not be used anymore after that point. Any use of the list after this may have undefined results, not limited just to strange behavior but possible segfaults and other strange memory errors. The object obj must be a valid object. </p>
<p> See also <code>evas_object_clip_set()</code>, <code>evas_object_clip_unset()</code> and <code>evas_object_clip_get()</code>. </p>
<p> Example: </p>
<pre> extern Evas_Object *obj;
 Evas_Object *clipper;
 clipper = evas_object_clip_get(obj);
 if (clipper)
 {
 Evas_List *clippees, *l;
 clippees = evas_object_clipees_get(clipper);
 printf('Clipper clips %i objects, evas_list_count(clippees));
 for (l = clippees; l; l = l-&gt;next)
 {
 Evas_Object *obj_tmp;
 obj_tmp = l-&gt;data;
 evas_object_show(obj_tmp);
 }
 }</pre>
<p>&nbsp;<wbr> </p>
<p> Referenced by evas_object_smart_clipped_member_del().</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Evas from the source code.</p>
