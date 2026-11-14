---
title: "xmltvgui(3)"
name: "xmltvgui"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmltvgui/"
---

<pre> XMLTV::GUI - Handles the choice of UI for XMLTV</pre><h2>Synopsis</h2><pre> use XMLTV::GUI;
 my $gui_type = get_gui_type($opt_gui);
 
 where $opt_gui is the commandline option given for --gui and $gui_type is
 one of 'term+progressbar', 'term' and 'tk'.</pre>Determines the type of output the user has requested for <font SIZE="-1">XMLTV</font> to communicate through.
<h2>Author</h2>Andy Balaam, axis3x3 [at] users.sourceforge.net. Distributed as part of the xmltv package.
<h2>See Also</h2><font SIZE="-1">XMLTV</font>
