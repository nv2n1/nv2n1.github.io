---
title: "ecore_imf_evas_group(3)"
name: "ecore_imf_evas_group"
section: "3"
letter: "e"
url: "/docs/linux/man/3-ecore_imf_evas_group/"
description: "Ecore Input Method Context Evas Helper Functions – Helper functions to make it easy to use Evas with Ecore_IMF."
---

<p>Ecore Input Method Context Evas Helper Functions &#8211; Helper functions to make it easy to use Evas with Ecore_IMF. </p>
<h3>Functions</h3>
<p>EAPI void <code>ecore_imf_evas_event_mouse_in_wrap</code> (Evas_Event_Mouse_In *evas_event, Ecore_IMF_Event_Mouse_In *imf_event)<br />
 <i>Converts a &#8216;mouse_in&#8217; event from Evas to the corresponding event of Ecore_IMF. </i><br />
 EAPI void <code>ecore_imf_evas_event_mouse_out_wrap</code> (Evas_Event_Mouse_Out *evas_event, Ecore_IMF_Event_Mouse_Out *imf_event)<br />
 <i>Converts a &#8216;mouse_out&#8217; event from Evas to the corresponding event of Ecore_IMF. </i><br />
 EAPI void <code>ecore_imf_evas_event_mouse_move_wrap</code> (Evas_Event_Mouse_Move *evas_event, Ecore_IMF_Event_Mouse_Move *imf_event)<br />
 <i>Converts a &#8216;mouse_move&#8217; event from Evas to the corresponding event of Ecore_IMF. </i><br />
 EAPI void <code>ecore_imf_evas_event_mouse_down_wrap</code> (Evas_Event_Mouse_Down *evas_event, Ecore_IMF_Event_Mouse_Down *imf_event)<br />
 <i>Converts a &#8216;mouse_down&#8217; event from Evas to the corresponding event of Ecore_IMF. </i><br />
 EAPI void <code>ecore_imf_evas_event_mouse_up_wrap</code> (Evas_Event_Mouse_Up *evas_event, Ecore_IMF_Event_Mouse_Up *imf_event)<br />
 <i>Converts a &#8216;mouse_up&#8217; event from Evas to the corresponding event of Ecore_IMF. </i><br />
 EAPI void <code>ecore_imf_evas_event_mouse_wheel_wrap</code> (Evas_Event_Mouse_Wheel *evas_event, Ecore_IMF_Event_Mouse_Wheel *imf_event)<br />
 <i>Converts a &#8216;mouse_wheel&#8217; event from Evas to the corresponding event of Ecore_IMF. </i><br />
 EAPI void <code>ecore_imf_evas_event_key_down_wrap</code> (Evas_Event_Key_Down *evas_event, Ecore_IMF_Event_Key_Down *imf_event)<br />
 <i>Converts a &#8216;key_down&#8217; event from Evas to the corresponding event of Ecore_IMF. </i><br />
 EAPI void <code>ecore_imf_evas_event_key_up_wrap</code> (Evas_Event_Key_Up *evas_event, Ecore_IMF_Event_Key_Up *imf_event)<br />
 <i>Converts a &#8216;key_up&#8217; event from Evas to the corresponding event of Ecore_IMF. </i></p>
<h2>Detailed Description</h2>
<p>Helper functions to make it easy to use Evas with Ecore_IMF.</p>
<h2>Function Documentation</h2>
<h3>EAPI void ecore_imf_evas_event_key_down_wrap (Evas_Event_Key_Down * evas_event, Ecore_IMF_Event_Key_Down * imf_event)</h3>
<p>Converts a &#8216;key_down&#8217; event from Evas to the corresponding event of Ecore_IMF. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>evas_event</i> The received Evas event.<br />
 <i>imf_event</i> The location to store the converted Ecore_IMF event.</dl>
<h3>EAPI void ecore_imf_evas_event_key_up_wrap (Evas_Event_Key_Up * evas_event, Ecore_IMF_Event_Key_Up * imf_event)</h3>
<p>Converts a &#8216;key_up&#8217; event from Evas to the corresponding event of Ecore_IMF. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>evas_event</i> The received Evas event.<br />
 <i>imf_event</i> The location to store the converted Ecore_IMF event.</dl>
<h3>EAPI void ecore_imf_evas_event_mouse_down_wrap (Evas_Event_Mouse_Down * evas_event, Ecore_IMF_Event_Mouse_Down * imf_event)</h3>
<p>Converts a &#8216;mouse_down&#8217; event from Evas to the corresponding event of Ecore_IMF. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>evas_event</i> The received Evas event.<br />
 <i>imf_event</i> The location to store the converted Ecore_IMF event.</dl>
<h3>EAPI void ecore_imf_evas_event_mouse_in_wrap (Evas_Event_Mouse_In * evas_event, Ecore_IMF_Event_Mouse_In * imf_event)</h3>
<p>Converts a &#8216;mouse_in&#8217; event from Evas to the corresponding event of Ecore_IMF. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>evas_event</i> The received Evas event.<br />
 <i>imf_event</i> The location to store the converted Ecore_IMF event.</dl>
<h3>EAPI void ecore_imf_evas_event_mouse_move_wrap (Evas_Event_Mouse_Move * evas_event, Ecore_IMF_Event_Mouse_Move * imf_event)</h3>
<p>Converts a &#8216;mouse_move&#8217; event from Evas to the corresponding event of Ecore_IMF. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>evas_event</i> The received Evas event.<br />
 <i>imf_event</i> The location to store the converted Ecore_IMF event.</dl>
<h3>EAPI void ecore_imf_evas_event_mouse_out_wrap (Evas_Event_Mouse_Out * evas_event, Ecore_IMF_Event_Mouse_Out * imf_event)</h3>
<p>Converts a &#8216;mouse_out&#8217; event from Evas to the corresponding event of Ecore_IMF. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>evas_event</i> The received Evas event.<br />
 <i>imf_event</i> The location to store the converted Ecore_IMF event.</dl>
<h3>EAPI void ecore_imf_evas_event_mouse_up_wrap (Evas_Event_Mouse_Up * evas_event, Ecore_IMF_Event_Mouse_Up * imf_event)</h3>
<p>Converts a &#8216;mouse_up&#8217; event from Evas to the corresponding event of Ecore_IMF. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>evas_event</i> The received Evas event.<br />
 <i>imf_event</i> The location to store the converted Ecore_IMF event.</dl>
<h3>EAPI void ecore_imf_evas_event_mouse_wheel_wrap (Evas_Event_Mouse_Wheel * evas_event, Ecore_IMF_Event_Mouse_Wheel * imf_event)</h3>
<p>Converts a &#8216;mouse_wheel&#8217; event from Evas to the corresponding event of Ecore_IMF. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>evas_event</i> The received Evas event.<br />
 <i>imf_event</i> The location to store the converted Ecore_IMF event.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Ecore from the source code.</p>
