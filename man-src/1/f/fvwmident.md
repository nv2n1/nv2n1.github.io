---
title: "fvwmident(1)"
name: "fvwmident"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fvwmident/"
description: "FvwmIdent – the Fvwm identify-window module"
---

<p>FvwmIdent &#8211; the Fvwm identify-window module </p>
<h2>Synopsis</h2>
<p>FvwmIdent is spawned by fvwm, so no command line invocation will work. </p>
<h2>Description</h2>
<p>The FvwmIdent module prompts the user to select a target window, if the module was not launched from within a window context in Fvwm. After that, it pops up a window with information about the window which was selected. </p>
<h2>Copyrights</h2>
<p>The FvwmIdent program, and the concept for interfacing this module to the Window Manager, are all original work by Robert Nation and Nobutaka Suzuki. </p>
<p> Copyright 1994, Robert Nation and Nobutaka Suzuki. No guarantees or warranties or anything are provided or implied in any way whatsoever. Use this program at your own risk. Permission to use this program for any purpose is given, as long as the copyright is kept intact. </p>
<h2>Initialization</h2>
<p>During initialization, <i>FvwmIdent</i> gets config info from <code>fvwm</code>&#8216;s module configuration database (see <i><a href="/docs/linux/man/1-fvwm/">fvwm</a></i>(1), section <code>MODULE COMMANDS</code>) to determine which colors and font to use. </p>
<p> If the FvwmIdent executable is linked to another name, ie ln -s FvwmIdent MoreIdentify, then another module called MoreIdentify can be started, with a completely different configuration than FvwmIdent, simply by changing the keyword FvwmIdent to MoreIdentify. This way multiple clutter-reduction programs can be used. </p>
<h2>Invocation</h2>
<p>FvwmIdent can be invoked by binding the action &#8216;Module FvwmIdent&#8217; to a menu or key-stroke in the .fvwm2rc file. Fvwm will search directory specified in the ModulePath configuration option to attempt to locate FvwmIdent. Although nothing keeps you from launching FvwmIdent at start-up time, you probably don&#8217;t want to. Clicking into the FvwmIdent window or pressing a key while it has focus closes FvwmIdent. Pressing mouse button 2 in the window restarts FvwmIdent and asks for a new window to select. </p>
<h2>Configuration Options</h2>
<p>FvwmIdent reads the same .fvwm2rc file as fvwm reads when it starts up, and looks for lines as listed below: </p>
<dl>
<dt>*FvwmIdent: Colorset <i>n</i></p>
<dd>Tells the module to use colorset <i>n</i>. See FvwmTheme. </p>
<dt>*FvwmIdent: Fore <i>color</i></p>
<dd>Tells the module to use <i>color</i> instead of black for text. Switches off the Colorset option. </p>
<dt>*FvwmIdent: Back <i>color</i></p>
<dd>Tells the module to use <i>color</i> instead of white for the window background. Switches off the Colorset option. </p>
<dt>*FvwmIdent: Font <i>fontname</i></p>
<dd>Tells the module to use <i>fontname</i> instead of fixed for text. </p>
<dt>*FvwmIdent: MinimalLayer <i>layer</i></p>
<dd>FvwmIdent places its window on the layer of a target window. But not below the minimal layer. By default, the minimal layer is 4 just like the fvwm default layer. If <i>layer</i> is 0, the layer of the target window is always used. If <i>layer</i> is &quot;default&quot; or not specified, the default behavior is restored. If <i>layer</i> is &quot;none&quot;, FvwmIdent is placed as a normal window even if the target window is above it. </p>
</dl>
<h2>Author</h2>
<p>Robert Nation and Nobutaka Suzuki (nobuta-s [at] is.aist-nara.ac.jp).</p>
