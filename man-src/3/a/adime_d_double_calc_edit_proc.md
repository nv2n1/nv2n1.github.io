---
title: "adime_d_double_calc_edit_proc(3)"
name: "adime_d_double_calc_edit_proc"
section: "3"
letter: "a"
url: "/docs/linux/man/3-adime_d_double_calc_edit_proc/"
description: "adime_d_double_calc_edit_proc"
---

<h2>NAME</h2>
<p> adime_d_double_calc_edit_proc</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/adime.h">adime.h</a>&gt;</code> </p>
<p> <code>int adime_d_double_calc_edit_proc(int msg, DIALOG *d, int c);</code></p>
<h2>DESCRIPTION</h2>
<p> Gui proc for an edit box accepting a mathematical expression whose result is a floating point number. The result is calculated and displayed on a separate gui object as the user types. The edit box has a 3d-ish look. </p>
<p> The dp2 field points to a `struct ADIME_EDIT_NUMBER *&#8217; which holds some information about the behavior of the edit box: </p>
<pre><code>
typedef struct ADIME_EDIT_NUMBER {
    int is_signed;           /* Set for integer formats if it is signed. */
    int is_float;            /* Set if we only have float, not double. */
    double min_val, max_val; /* Range for numbers. */
    DIALOG *result_object;   /* DIALOG object to display result in. */
} ADIME_EDIT_NUMBER;
</code></pre>
<p> The `result_object&#8217; will be used to display the result of the expression. There is an `adime_d_calc_edit_result_proc&#8217; object type which is designed to be used as `result_object&#8217;, but you may of course write your own object to take care of this. Whenever the user changes the text in the `adime_d_double_calc_edit_proc&#8217;, the result is printed to the `dp&#8217; field of `result_object&#8217;; hence you must have set the dp field of `result_object&#8217; to a text buffer with enough space (256 bytes is safe). The `result_object&#8217; will then be sent a `MSG_DRAW&#8217; message with the `c&#8217; parameter set to 2 if there is an error in the expression or 1 if it is ok. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-adime_d_calc_edit_result_proc/">adime_d_calc_edit_result_proc</a></code>(3), <code><a href="/docs/linux/man/3-adime_d_int_calc_edit_proc/">adime_d_int_calc_edit_proc</a></code>(3) </p>
<h2>Index</h2>
