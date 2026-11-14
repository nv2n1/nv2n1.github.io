---
title: "fog(1)"
name: "fog"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fog/"
---

<h2>NAME</h2>

 Fog - The console Form Designer for GNU/Linux Version 1.4

<h2>DESCRIPTION</h2>

 Fog (Form Designer) is part of the GnuDOS package, which is a library of functions for use under the GNU/Linux console/xterm. It provides four utilities: Kbd (for keyboard handling), Screen (for screen handling), Dialogs (for drawing dialog and input boxes), and Strings (for string manipulation). GnuDOS is basically an idea of easing life for console users who came from a DOS-like environment and want to learn how to use the GNU system, and for programmers, who like to write console programs for such users. Some of the common problems that face console programs are handled by the library (like needing to get user input in terms of &quot;keypress&quot; not &quot;keypress+ENTER&quot; as is done with the basic C library functions. Another thing is the ease by which a programmer can draw complete informative dialog boxes and get user input through input boxes by simple call to a library function!. Other things like positioning the cursor and colorizing the screen from within your C programs is just a few function calls away!.

<h2>FILES</h2>

 <i>formname.fog</i> An input file containing information about form design for use with fog. 
 <i>main.c</i> One of the output files of fog. Contains the main() function plus an event handler function for button clicks (or ENTERs) if there are buttons on the form. 
 <i>fog_header.h</i> One of the output files of fog. Contains the function declarations and global variable definitions. 
 <i>form_design.c</i> One of the output files of fog. Contains the function definitions of the following functions: init_form(), close_form(), refresh_form(), and input_loop().

<h2>TODO</h2>

 - Add mouse support 
 - Add more key definitions to the Kbd utility 
 - Add printing functionality 
 - Testing and debugging!

<h2>SEE ALSO</h2>

 info fog, info gnudos

<h2>AUTHOR</h2>

 Mohammed Isam &lt;mohammed_isam1984 [at] yahoo.com&gt; 

<h2>Index</h2>


