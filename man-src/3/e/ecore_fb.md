---
title: "ecore_fb(3)"
name: "ecore_fb"
section: "3"
letter: "e"
url: "/docs/linux/man/3-ecore_fb/"
description: "Ecore_Fb.h – Ecore frame buffer system functions."
---

<p>Ecore_Fb.h &#8211; Ecore frame buffer system functions. </p>
<h2>Synopsis</h2>
<h3>Data Structures</h3>
<p>struct <code>_Ecore_Fb_Event_Key_Down</code><br />
 <i>FB Key Down event. </i><br />
 struct <code>_Ecore_Fb_Event_Key_Up</code><br />
 <i>FB Key Up event. </i><br />
 struct <code>_Ecore_Fb_Event_Mouse_Button_Down</code><br />
 <i>FB Mouse Down event. </i><br />
 struct <code>_Ecore_Fb_Event_Mouse_Button_Up</code><br />
 <i>FB Mouse Up event. </i><br />
 struct <code>_Ecore_Fb_Event_Mouse_Move</code><br />
 <i>FB Mouse Move event. </i><br />
 struct <code>_Ecore_Fb_Event_Mouse_Wheel</code><br />
 <i>FB Mouse Wheel event. </i></p>
<h3>Typedefs</h3>
<p>typedef struct <code>_Ecore_Fb_Event_Key_Down</code> <code>Ecore_Fb_Event_Key_Down</code><br />
 <i>FB Key Down event. </i><br />
 typedef struct <code>_Ecore_Fb_Event_Key_Up</code> <code>Ecore_Fb_Event_Key_Up</code><br />
 <i>FB Key Up event. </i><br />
 typedef struct <code>_Ecore_Fb_Event_Mouse_Button_Down</code> <code>Ecore_Fb_Event_Mouse_Button_Down</code><br />
 <i>FB Mouse Down event. </i><br />
 typedef struct <code>_Ecore_Fb_Event_Mouse_Button_Up</code> <code>Ecore_Fb_Event_Mouse_Button_Up</code><br />
 <i>FB Mouse Up event. </i><br />
 typedef struct <code>_Ecore_Fb_Event_Mouse_Move</code> <code>Ecore_Fb_Event_Mouse_Move</code><br />
 <i>FB Mouse Move event. </i><br />
 typedef struct <code>_Ecore_Fb_Event_Mouse_Wheel</code> <code>Ecore_Fb_Event_Mouse_Wheel</code><br />
 <i>FB Mouse Wheel event. </i></p>
<h3>Functions</h3>
<p>EAPI void <code>ecore_fb_callback_gain_set</code> (void(*func)(void *data), void *data)<br />
 <i>To be documented. </i><br />
 EAPI void <code>ecore_fb_callback_lose_set</code> (void(*func)(void *data), void *data)<br />
 <i>To be documented. </i><br />
 EAPI int <code>ecore_fb_shutdown</code> (void)<br />
 <i>Shuts down the Ecore_Fb library. </i><br />
 EAPI void <code>ecore_fb_size_get</code> (int *w, int *h)<br />
 <i>Retrieves the width and height of the current frame buffer in pixels. </i><br />
 EAPI void <code>ecore_fb_touch_screen_calibrate_set</code> (int xscale, int xtrans, int yscale, int ytrans, int xyswap)<br />
 <i>Calibrates the touschreen using the given parameters. </i><br />
 EAPI void <code>ecore_fb_touch_screen_calibrate_get</code> (int *xscale, int *xtrans, int *yscale, int *ytrans, int *xyswap)<br />
 <i>Retrieves the calibration parameters of the touchscreen. </i></p>
<h3>Variables</h3>
<p>EAPI int <code>ECORE_FB_EVENT_KEY_DOWN</code><br />
 <i>FB Key Down event. </i><br />
 EAPI int <code>ECORE_FB_EVENT_KEY_UP</code><br />
 <i>FB Key Up event. </i><br />
 EAPI int <code>ECORE_FB_EVENT_MOUSE_BUTTON_DOWN</code><br />
 <i>FB Mouse Down event. </i><br />
 EAPI int <code>ECORE_FB_EVENT_MOUSE_BUTTON_UP</code><br />
 <i>FB Mouse Up event. </i><br />
 EAPI int <code>ECORE_FB_EVENT_MOUSE_MOVE</code><br />
 <i>FB Mouse Move event. </i><br />
 EAPI int <code>ECORE_FB_EVENT_MOUSE_WHEEL</code><br />
 <i>FB Mouse Wheel event. </i></p>
<h2>Detailed Description</h2>
<p>Ecore frame buffer system functions. </p>
<h2>Function Documentation</h2>
<h3>EAPI void ecore_fb_callback_gain_set (void(*)(void *data) func, void * data)</h3>
<p>To be documented. </p>
<p> FIXME: To be fixed. </p>
<p> <code>Todo</code></p>
<dl COMPACT>
<dd>Documentation: Find out what this does.</dl>
<p> References ecore_fb_callback_gain_set(). </p>
<p> Referenced by ecore_evas_fb_new(), and ecore_fb_callback_gain_set().</p>
<h3>EAPI void ecore_fb_callback_lose_set (void(*)(void *data) func, void * data)</h3>
<p>To be documented. </p>
<p> FIXME: To be fixed. </p>
<p> <code>Todo</code></p>
<dl COMPACT>
<dd>Documentation: Find out what this does.</dl>
<p> References ecore_fb_callback_lose_set(). </p>
<p> Referenced by ecore_evas_fb_new(), and ecore_fb_callback_lose_set().</p>
<h3>EAPI void ecore_fb_size_get (int * w, int * h)</h3>
<p>Retrieves the width and height of the current frame buffer in pixels. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>w</i> Pointer to an integer in which to store the width.<br />
 <i>h</i> Pointer to an interge in which to store the height.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Ecore from the source code.</p>
