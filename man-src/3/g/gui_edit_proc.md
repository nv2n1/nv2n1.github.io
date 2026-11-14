---
title: "gui_edit_proc(3)"
name: "gui_edit_proc"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gui_edit_proc/"
description: "gui_shadow_box_proc, gui_ctext_proc, gui_button_proc, gui_edit_proc, gui_list_proc, gui_text_list_proc – Hooks to customise the look and feel of Allegro dialogs."
---

<h2>NAME</h2>
<p> gui_shadow_box_proc, gui_ctext_proc, gui_button_proc, gui_edit_proc, gui_list_proc, gui_text_list_proc &#8211; Hooks to customise the look and feel of Allegro dialogs.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>extern int (*gui_shadow_box_proc)(int msg, struct DIALOG *d, int c);</code> </p>
<p> <code>extern int (*gui_ctext_proc)(int msg, struct DIALOG *d, int c);</code> </p>
<p> <code>extern int (*gui_button_proc)(int msg, struct DIALOG *d, int c);</code> </p>
<p> <code>extern int (*gui_edit_proc)(int msg, struct DIALOG *d, int c);</code> </p>
<p> <code>extern int (*gui_list_proc)(int msg, struct DIALOG *d, int c);</code> </p>
<p> <code>extern int (*gui_text_list_proc)(int msg, struct DIALOG *d, int c);</code></p>
<h2>DESCRIPTION</h2>
<p> If set, these functions will be used by the standard Allegro dialogs. This allows you to customise the look and feel, much like gui_fg_color and gui_bg_color, but much more flexibly. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-alert/">alert</a></code>(3), <code><a href="/docs/linux/man/3-alert3/">alert3</a></code>(3), <code><a href="/docs/linux/man/3-file_select_ex/">file_select_ex</a></code>(3), <code><a href="/docs/linux/man/3-gfx_mode_select/">gfx_mode_select</a></code>(3), <code><a href="/docs/linux/man/3-gui_fg_color/">gui_fg_color</a></code>(3) </p>
<h2>Index</h2>
