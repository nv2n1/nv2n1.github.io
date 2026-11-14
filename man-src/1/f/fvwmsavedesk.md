---
title: "fvwmsavedesk(1)"
name: "fvwmsavedesk"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fvwmsavedesk/"
---

FvwmSaveDesk - another fvwm desktop-layout saving module 

<h2>Synopsis</h2>FvwmSaveDesk is spawned by fvwm, so no command line invocation will work. 

<h2>Description</h2>When called, this module will attempt to save your current desktop layout as a definition of extra lines for the function InitFunction into the file <i>.fvwm2desk</i> in your home directory. As explain in the other documentation, this function is called at startup of fvwm. You have to include this file in <i>.fvwm2rc</i> after the definition of the Function Initfunction. You can do this by using the module <i>FvwmM4</i> or <i>FvwmCpp.</i> 

 Your applications must supply certain hints to the X window system. <i>Emacs</i> and <i>Netscape</i>, for example, does not, so FvwmSaveDesk can't get any information from it. 

 Also, FvwmSaveDesk assumes that certain command line options are globally accepted by applications, which may not be the case. 

<h2>Setup Using Fvwmm4 Module</h2>The M4 Macro processor substitutes its macros even in the middle of a word. Because of that you may have problems with predefined macros such as include or define. To avoid this the GNU M4 has an extra option to prefix all builtins with 'm4_'. FvwmM4 can be called with option -m4-prefix and then will provide the option -P to M4. I personally use the FvwmM4 module this way. <pre>fvwm -cmd &quot;FvwmM4 -m4-prefix -m4opt -I$HOME $HOME/.fvwm2rc&quot;</pre>Simply add the following line to the end of .fvwm2rc: <pre>m4_include(`.fvwm2desk') .</pre><h2>Setup Using Fvwmcpp Module</h2>With the FvwmCpp you may have the problem that the preprocessor directives starts with the comment character '#' and will complain about unknown directives, if you have comments in your .fvwm2rc. <pre>fvwm -cmd &quot;FvwmCpp -C-I$HOME $HOME/.fvwm2rc&quot;</pre>Simply add the following line to the end of .fvwm2rc: <pre>#include &quot;.fvwm2desk&quot;</pre><h2>Invocation</h2>FvwmSaveDesk can be invoked by adding it to a menu or binding it to a mouse button or key stroke in the <i>.fvwm2rc</i> file. Fvwm will search directory specified in the ModulePath configuration option to locate FvwmSaveDesk. 

 To insert it to a menu, add the line <pre>+ &quot;Save Desktop&quot; Module FvwmSaveDesk</pre>to the menu definition. I thing binding it to a mouse button is not very useful, but you can do that, by adding for example this line. <pre>Mouse 3 R CS Module FvwmSaveDesk</pre>Than FvwmSaveDesk will be called if you hit the right mouse button on the root window while holding the shift and control button down. 

 You can bind FvwmSaveDesk to a function key F10 for example you have to insert the following line: <pre>Key F10 A Module FvwmSaveDesk</pre>I personally add it as a Button to the module FvwmButtons: <pre>*FvwmButtons SaveDesc desk.xpm Module FvwmSaveDesk</pre><h2>Author</h2>Carsten Paeth (calle [at] calle.in-berlin.de)
