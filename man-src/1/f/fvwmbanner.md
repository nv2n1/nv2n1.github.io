---
title: "fvwmbanner(1)"
name: "fvwmbanner"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fvwmbanner/"
---

FvwmBanner - the Fvwm Banner module 

<h2>Synopsis</h2>Module FvwmBanner 

 <i>FvwmBanner</i> can only be invoked by fvwm. Command line invocation of the <i>FvwmBanner</i> module will not work. 

<h2>Description</h2>FvwmBanner displays an Fvwm Logo in the center of the screen for 3 seconds. 

<h2>Copyrights</h2>None. 

<h2>Initialization</h2>Nothing interesting. 

<h2>Invocation</h2>FvwmBanner can be invoked by the command 'Module FvwmBanner'. This can be bound to a menu or key-stroke in the .fvwm2rc file, but more likely you would do this in the StartFunction or InitFunction, for example: 

 <pre>AddToFunc InitFunction &quot;I&quot; Module FvwmBanner</pre>You can also give it an optional file parameter, like 'FvwmBanner doomface.xpm' or specify an alternate default pixmap via configuration options (see &quot;*FvwmBanner: Pixmap&quot; below). Fvwm will search the ImagePath to find the image, or you can use the full path to the image. 

<h2>Configuration Options</h2><dl><dt>*FvwmBanner: NoDecor
<dd>Tells FvwmBanner to create a window that Fvwm will not manage and not decorate. 

<dt>*FvwmBanner: Pixmap <i>file</i>
<dd>Tells FvwmBanner to display <i>file</i> instead of the built in pixmap. 

<dt>*FvwmBanner: Timeout <i>sec</i>
<dd>Tells FvwmBanner to display for <i>sec</i> seconds instead of default of 3 seconds. 

</dl><h2>Author</h2>Robert Nation
