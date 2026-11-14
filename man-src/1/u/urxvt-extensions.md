---
title: "urxvt-extensions(1)"
name: "urxvt-extensions"
section: "1"
letter: "u"
url: "/docs/linux/man/1-urxvt-extensions/"
---

<h2 class="name">NAME</h2>
 

 urxvt-extensions - briefly list urxvt perl extensions 

<h2>SYNOPSIS</h2>

 <pre>
   urxvt -pe extension-name
</pre>

<h2>DESCRIPTION</h2>

 This manpage briefly lists the rxvt-unicode extensions available in this version of rxvt-unicode. For information on how to write urxvt extensions, see the urxvt-extensions manpage. 

 Extensions that use resources for configuration are loaded automatically when their resources are specified as command-line switches. Any extension can be loaded explicitly with the <tt>&quot;-pe&quot;</tt> switch.

<h2>EXTENSION LIST</h2>

 background - manage terminal background 

 bell-command - execute a command when the bell rings 

 block-graphics-to-ascii - map block graphics to ascii characters 

 clipboard-osc - implement the clipboard operating system command sequence 

 confirm-paste - ask for confirmation before pasting multiline text 

 digital-clock - display a digital clock overlay 

 eval - evaluate arbitrary perl code using actions 

 example-refresh-hooks - example of how to use refresh hooks 

 keysym-list - implement the ``list'' keysym expansion. 

 kuake - kuake-like hotkey terminal 

 matcher - match strings in terminal output and change their rendition 

 option-popup - option menu (enabled by default) 

 overlay-osc - implement <font SIZE="-1">OSC</font> to manage overlays 

 readline - improve readline editing (enabled by default) 

 remote-clipboard - manage a shared and possibly remote clipboard 

 searchable-scrollback - incremental scrollback search (enabled by default) 

 selection - more intelligent selection (enabled by default) 

 selection-autotransform - automatically transform select text 

 selection-pastebin - automatic pastebin upload 

 selection-popup (enabled by default) 

 selection-to-clipboard - copy the selection to the clipboard each time a selection is made 

 tabbed - tabbed interface to urxvt 

 xim-onthespot - implement <font SIZE="-1">XIM </font>``on-the-spot'' behaviour

<h2>SEE ALSO</h2>

 <i><a HREF="/docs/linux/man/1-urxvt/">urxvt</a></i>(1), <i><a HREF="/docs/linux/man/3-urxvtperl/">urxvtperl</a></i>(3) 

<h2>Index</h2>


