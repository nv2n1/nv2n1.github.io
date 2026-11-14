---
title: "file_select_ex(3)"
name: "file_select_ex"
section: "3"
letter: "f"
url: "/docs/linux/man/3-file_select_ex/"
description: "file_select_ex – Displays the Allegro file selector with a caption."
---

<h2>NAME</h2>
<p> file_select_ex &#8211; Displays the Allegro file selector with a caption.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>int file_select_ex(const char *message, char *path, const char *ext,</code> <code>int size, int w, int h);</code></p>
<h2>DESCRIPTION</h2>
<p> Displays the Allegro file selector, with the message as caption. The path parameter contains the initial filename to display (this can be used to set the starting directory, or to provide a default filename for a save-as operation). The user selection is returned by altering the path buffer, whose maximum capacity in bytes is specified by the size parameter. Note that it should have room for at least 80 characters (not bytes), so you should reserve 6x that amount, just to be sure. The list of files is filtered according to the file extensions in the ext parameter. Passing NULL includes all files; &quot;PCX;BMP&quot; includes only files with one of the fields in the extension list can begin with a slash, followed by a set of attribute characters. Any attribute written on its own, or with a &#8216;+&#8217; before it, indicates to include only files which have that attribute set. Any attribute with a &#8216;-&#8216; before it indicates to leave out any files with that attribute. The flag characters are &#8216;r&#8217; (read-only), example, an extension string of &quot;PCX;BMP;/+r-h&quot; will display only PCX or BMP files that are read-only and not hidden. The directories are not affected in the same way as the other files by the extension string: the extensions are never taken into account for them and the other attributes are taken into account only when &#8216;d&#8217; is mentioned in the string; in other words, all directories are included when &#8216;d&#8217; is not mentioned in the string. The file selector is stretched to the width and height specified in the w and h parameters, and to the size of the standard Allegro font. If either the width or height argument is set to zero, it is stretched to the corresponding screen dimension. This function returns zero if it was closed with the Cancel button or non-zero if it was OK&#8217;d. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-gui_fg_color/">gui_fg_color</a></code>(3) </p>
<h2>Index</h2>
