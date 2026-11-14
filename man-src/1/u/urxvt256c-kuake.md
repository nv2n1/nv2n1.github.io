---
title: "urxvt256c-kuake(1)"
name: "urxvt256c-kuake"
section: "1"
letter: "u"
url: "/docs/linux/man/1-urxvt256c-kuake/"
---

<h2 class="name">NAME</h2>
 

 kuake - kuake-like hotkey terminal 

<h2>EXAMPLES</h2>

 <pre>
  @@RXVT_NAME@@ -kuake-hotkey F10
  URxvt.kuake.hotkey: F10
</pre>

<h2>DESCRIPTION</h2>

 A very primitive quake-console-like extension. It was inspired by a description of how the programs <tt>&quot;kuake&quot;</tt> and <tt>&quot;yakuake&quot;</tt> work: Whenever the user presses a global accelerator key (by default <tt>&quot;F10&quot;</tt>), the terminal will show or hide itself. Another press of the accelerator key will hide or show it again. 

 Initially, the window will not be shown when using this extension. 

 This is useful if you need a single terminal that is not using any desktop space most of the time but is quickly available at the press of a key. 

 The accelerator key is grabbed regardless of any modifiers, so this extension will actually grab a physical key just for this function. 

 If you want a quake-like animation, tell your window manager to do so (fvwm can do it). 

<h2>Index</h2>


