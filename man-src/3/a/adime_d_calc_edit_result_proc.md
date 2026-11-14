---
title: "adime_d_calc_edit_result_proc(3)"
name: "adime_d_calc_edit_result_proc"
section: "3"
letter: "a"
url: "/docs/linux/man/3-adime_d_calc_edit_result_proc/"
description: "adime_d_calc_edit_result_proc"
---

<h2>NAME</h2>
<p> adime_d_calc_edit_result_proc</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/adime.h">adime.h</a>&gt;</code> </p>
<p> <code>int adime_d_calc_edit_result_proc(int msg, DIALOG *d, int c);</code></p>
<h2>DESCRIPTION</h2>
<p> Dialog proc for the result of a calculator edit box. The difference between this and Allegro&#8217;s `d_text_proc()&#8217; is that it uses the c parameter to find the color to draw with (see `d_double_calc_edit_proc()&#8217;), and it also erases its whole area even if the text doesn&#8217;t fill it. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-adime_d_int_calc_edit_proc/">adime_d_int_calc_edit_proc</a></code>(3), <code><a href="/docs/linux/man/3-adime_d_double_calc_edit_proc/">adime_d_double_calc_edit_proc</a></code>(3) </p>
<h2>Index</h2>
