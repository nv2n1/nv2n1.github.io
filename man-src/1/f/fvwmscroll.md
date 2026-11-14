---
title: "fvwmscroll(1)"
name: "fvwmscroll"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fvwmscroll/"
description: "FvwmScroll – the fvwm scroll-bar module"
---

<p>FvwmScroll &#8211; the fvwm scroll-bar module </p>
<h2>Synopsis</h2>
<p>FvwmScroll is spawned by fvwm, so no command line invocation will work. </p>
<h2>Description</h2>
<p>The FvwmScroll module prompts the user to select a target window, if the module was not launched from within a window context in Fvwm. After that, it adds scroll bars to the selected window, to reduce the total desktop space consumed by the window. </p>
<p> FvwmScroll should not be used with windows which move or resize themselves, nor should it be used with windows which set the WM_COLORMAP_WINDOWS property. Operation is fine with windows that have a private colormap. </p>
<h2>Copyrights</h2>
<p>The FvwmScroll program, and the concept for interfacing this module to the Window Manager, are all original work by Robert Nation. </p>
<p> Copyright 1994, Robert Nation. No guarantees or warranties or anything are provided or implied in any way whatsoever. Use this program at your own risk. Permission to use this program for any purpose is given, as long as the copyright is kept intact. </p>
<h2>Initialization</h2>
<p>During initialization, <i>FvwmScroll</i> gets config info from <code>fvwm</code>&#8216;s module configuration database (see <i><a href="/docs/linux/man/1-fvwm/">fvwm</a></i>(1), section <code>MODULE COMMANDS</code>) to determine which colors to use. </p>
<p> If the FvwmScroll executable is linked to another name, ie ln -s FvwmScroll MoreScroll, then another module called MoreScroll can be started, with a completely different configuration than FvwmScroll, simply by changing the keyword FvwmScroll to MoreScroll. </p>
<h2>Invocation</h2>
<p>FvwmScroll can be invoked by binding the action &#8216;Module FvwmScroll x y&#8217; to a menu or key-stroke in the .fvwm2rc file. The parameter x and y are either integers or integers immediately followed by a p, which describe the horizontal and vertical size modification of the window. An integer describe a size reduction. An integer followed by a p describe a size as a percentage of the height or the width of a full screen but the size is never larger than the original window size (0p will do nothing). Fvwm will search directory specified in the ModulePath configuration option to attempt to locate FvwmScroll. Although nothing keeps you from launching FvwmScroll at start-up time, you probably don&#8217;t want to. </p>
<h2>Configuration Options</h2>
<dl>
<dt>*FvwmScroll: Colorset <i>n</i></p>
<dd>Tells the module to use colorset <i>n</i>. See FvwmTheme. </p>
<dt>*FvwmScroll: Back <i>color</i></p>
<dd>Tells the module to use <i>color</i> instead of black for the window background. Switches off the Colorset option. </p>
</dl>
<h2>Bugs</h2>
<p>When the scroll bars are removed by clicking on the button in the lower right corner, the window does not restore its location correctly. </p>
<h2>Author</h2>
<p>Robert Nation</p>
