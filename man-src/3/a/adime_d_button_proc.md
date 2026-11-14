---
title: "adime_d_button_proc(3)"
name: "adime_d_button_proc"
section: "3"
letter: "a"
url: "/docs/linux/man/3-adime_d_button_proc/"
description: "adime_d_button_proc"
---

<h2>NAME</h2>
<p> adime_d_button_proc</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/adime.h">adime.h</a>&gt;</code> </p>
<p> <code>int adime_d_button_proc(int msg, DIALOG *d, int c)</code></p>
<h2>DESCRIPTION</h2>
<p> Similar to Allegro&#8217;s `d_button_proc()&#8217;, but with 3d-ish style. It also has a slightly different behaviour: Unlike `d_button_proc()&#8217;, the D_EXIT flag has no effect. Instead you need to set the `d1&#8242; field to one of the three constants: </p>
<p> ADIME_BUTTON_TOGGLE </p>
<p> The button behaves like a check box, i.e. when clicked it toggles between being in and being out. </p>
<p> ADIME_BUTTON_EXIT </p>
<p> The button exits the dialog when clicked. </p>
<p> ADIME_BUTTON_CALLBACK </p>
<p> If you provide a callback function in the dp2 field, then it will be called whenever the button is clicked. This callback should have the form `int my_callback(DIALOG *d)&#8217;, and its return value will be passed back to the dialog manager. </p>
<h2>Index</h2>
