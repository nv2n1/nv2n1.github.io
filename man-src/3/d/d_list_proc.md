---
title: "d_list_proc(3)"
name: "d_list_proc"
section: "3"
letter: "d"
url: "/docs/linux/man/3-d_list_proc/"
description: "d_list_proc – Dialog procedure implementing a list box object. Allegro game programming library."
---

<h2>NAME</h2>
<p> d_list_proc &#8211; Dialog procedure implementing a list box object. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>int d_list_proc(int msg, DIALOG *d, int c);</code></p>
<h2>DESCRIPTION</h2>
<p> A list box object. This will allow the user to scroll through a list of items and to select one by clicking or with the arrow keys. If the D_EXIT flag is set, double clicking on a list item will close the dialog. The index of the selected item is held in the d1 field, and d2 is used to store how far it has scrolled through the list. The dp field points to a function which will be called to obtain information about the contents of the list. This should follow the form: </p>
<pre><code>
char *foobar(int index, int *list_size);
</code></pre>
<p> If index is zero or positive, the function should return a pointer to the string which is to be displayed at position index in the list. If index is negative, it should return NULL and list_size should be set to the number of items in the list. </p>
<p> To create a multiple selection listbox, set the dp2 field to an array of byte flags indicating the selection state of each list item (non-zero for selected entries). This table must be at least as big as the number of objects in the list! </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-exgui/">exgui</a></code>(3) </p>
<h2>Index</h2>
