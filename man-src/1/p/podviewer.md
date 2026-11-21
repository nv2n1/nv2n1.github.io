---

title: "podviewer(1)"
name: "podviewer"
section: "1"
letter: "p"
url: "/docs/linux/man/1-podviewer/"
---

podviewer - a Gtk2-Perl POD Reading Program 

<pre>
        podviewer [FILE|MODULE|FUNCTION|POD]
</pre>

<tt>&quot;podviewer&quot;</tt> provides a simple and attractive way to read Perl's <font SIZE="-1">POD</font> documentation. You can use it to read the Perl <font SIZE="-1">POD</font> pages, module documentation and information about Perl's builtin functions.

<h2>KEYBOARD SHORTCUTS</h2>

 <tt>&quot;podviewer&quot;</tt> supports a wide number of keyboard shortcuts. They are documented here.
<dl>
<dt>&bull;
</dt><dd> <tt>&quot;Ctrl-U&quot;</tt> or <tt>&quot;Alt-Up&quot;</tt> 
 Go up a level. That is, if you're reading the documentation for <tt>&quot;Foo::Bar&quot;</tt>, typing <tt>&quot;Ctrl-U&quot;</tt> will take you to the <tt>&quot;Foo&quot;</tt> page.
</dd><dt>&bull;
</dt><dd> <tt>&quot;Alt-Left&quot;</tt> 
 Go back in your browsing history.
</dd><dt>&bull;
</dt><dd> <tt>&quot;Alt-Right&quot;</tt> 
 Go forward in your browsing history.
</dd><dt>&bull;
</dt><dd> <tt>&quot;Ctrl-H&quot;</tt> 
 Go home. If you have the <tt>&quot;home&quot;</tt> option set in your config (see below), entering <tt>&quot;Ctrl-H&quot;</tt> will take you there.
</dd><dt>&bull;
</dt><dd> <tt>&quot;Ctrl-L&quot;</tt> 
 This toggles the document index.
</dd><dt>&bull;
</dt><dd> <tt>&quot;Ctrl-O&quot;</tt> 
 This pops up a dialog allowing you to choose a document to read.
</dd><dt>&bull;
</dt><dd> <tt>&quot;Ctrl-R&quot;</tt> or <tt>&quot;F5&quot;</tt> 
 This reloads the current document.
</dd><dt>&bull;
</dt><dd> <tt>&quot;Ctrl-Q&quot;</tt> 
 This quits the program.
</dd><dt>&bull;
</dt><dd> <tt>&quot;Ctrl-F&quot;</tt> 
 This pops up a dialog for you to enter some search text.
</dd><dt>&bull;
</dt><dd> <tt>&quot;Ctrl-G&quot;</tt> 
 This performs the previous search, but from the most recently found result. You can also repeat the previous search by pressing enter when the cursor is in the search box.
</dd><dt>&bull;
</dt><dd> <tt>&quot;F1&quot;</tt> 
 Loads this document.</dd></dl>

<h2>CONFIGURATION OPTIONS</h2>

 <tt>&quot;podviewer&quot;</tt> stores its configuration settings in a resource file, located at <tt>&quot;$HOME/.podviewrc&quot;</tt>. This file contains simple <tt>&quot;name=value&quot;</tt> pairs for various things:
<dl>
<dt>&bull;
</dt><dd> <tt>&quot;icon-size&quot;</tt> 
 If you want to change the size of the icons on the toolbar, change this value. The values are standard Gtk+ stock values.
</dd><dt>&bull;
</dt><dd> <tt>&quot;home&quot;</tt> 
 This is the name of the document you want to be your home page. This page is loaded when you start the program without arguments, hit the Home button, or type <tt>&quot;Ctrl-H&quot;</tt>.</dd></dl>

<h2>SEE ALSO</h2>

<dl>
<dt>&bull;
</dt><dd> Gtk2 or &lt;<a rel="nofollow" HREF="http://gtk2-perl.sf.net/">http://gtk2-perl.sf.net/</a>&gt;
</dd><dt>&bull;
</dt><dd> &lt;<a rel="nofollow" HREF="http://developer.gnome.org/doc/API/2.0/gtk/GtkTextView.html">http://developer.gnome.org/doc/API/2.0/gtk/GtkTextView.html</a>&gt;
</dd><dt>&bull;
</dt><dd> Gtk2::Ex::PodViewer::Parser</dd></dl>

<h2>AUTHORS</h2>

 Gavin Brown, Torsten Schoenfeld and Scott Arrington.

<h2>COPYRIGHT</h2>

 (c) 2003-2005 Gavin Brown (gavin.brown [at] uk.com). All rights reserved. This program is free software; you can redistribute it and/or modify it under the same terms as Perl itself.
