---
title: "fvwmbacker(1)"
name: "fvwmbacker"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fvwmbacker/"
description: "FvwmBacker – the fvwm background changer module"
---

<p>FvwmBacker &#8211; the fvwm background changer module </p>
<h2>Synopsis</h2>
<p>Module FvwmBacker </p>
<p> <i>FvwmBacker</i> can only be invoked by fvwm. Command line invocation of the <i>FvwmBacker</i> module will not work. </p>
<h2>Description</h2>
<p>The FvwmBacker module provides functionality to change the background when changing desktops. Any command can be executed to change the backgrounds. Actually, any arbitrary command can be sent to fvwm to execute, so you could also do things such as changing window border colors, etc. </p>
<h2>Copyrights</h2>
<p>The FvwmBacker module is the original work of Mike Finger. </p>
<p> Copyright 1994, Mike Finger. The author makes no guarantees or warranties of any kind about the use of this module. Use this module at your own risk. You may freely use this module or any portion of it for any purpose as long as the copyright is kept intact. </p>
<h2>Initialization</h2>
<p>During initialization, <i>FvwmBacker</i> gets config info from <code>fvwm</code>&#8216;s module configuration database (see <i><a href="/docs/linux/man/1-fvwm/">fvwm</a></i>(1), section <code>MODULE COMMANDS</code>). Available options are discussed in a later section. </p>
<h2>Invocation</h2>
<p>FvwmBacker can be invoked by fvwm during initialization by inserting the line </p>
<pre>AddToFunc StartFunction I Module FvwmBacker</pre>
<p>in the .fvwm2rc file. </p>
<p> FvwmBacker can be started using a &#8216;Module FvwmBacker&#8217; command or stopped using a &#8216;KillModule FvwmBacker&#8217; command at any time when fvwm is running. </p>
<p> FvwmBacker must reside in a directory that is listed in the ModulePath option of fvwm for it to be executed by fvwm. </p>
<h2>Configuration Options</h2>
<p>The following options can be placed in the .fvwm2rc file </p>
<dl>
<dt>*FvwmBacker: Command <i>(Desk d, Page x y) command</i></p>
<dd>Specifies the <i>command</i> to execute when the viewport matches the arguments for the desk d, page x coordinate and y coordinate. Any or all of these three numeric arguments can be replaced with an asterisk (*) to indicate that any value matches, in this case Desk or Page parts can be skipped. </p>
<p> If either the <i>Desk</i> or the <i>Page</i> parts are omitted, the command is not executed if only the desk or the page is switched. If neither is given, the command is executed only once when the module is started. This is not the same as using asterisks for the numeric arguments: if asterisks are used, the command is always executed when only the desk or page changes, if the corresponding part is omitted, the command is never executed when only the desk or page changes. </p>
<p> If the <i>command</i> is <i>-solid</i> FvwmBacker uses the next argument as a color in the X database and sets the background to that color without generating a system call to xsetroot (only single word color names may be used). </p>
<p> If the <i>command</i> is <i>colorset</i> FvwmBacker uses the background specified in colorset <i>n</i> for the given desk. Please refer to the man page of the FvwmTheme module for details about colorsets. </p>
<p> Otherwise the command is sent to fvwm to execute. </p>
<dt>*FvwmBacker: RetainPixmap</p>
<dd>Causes FvwmBacker to retain and publish the Pixmap with which the background has been set. This works only for the <i>-solid</i> or <i>colorset</i> commands. This is useful for applications which want to use the root Pixmap on the background to simulate transparency (for example, Eterm and Aterm use this method). This option should also be used for the RootTransparent colorset option (see the FvwmTheme man page). Note: with a colorset background this command may add a lot of memory to the X server. For example, this adds the pixmap width times height bytes with a TiledPixmap image, screen_width times screen_height bytes with a Pixmap image or a C,B,D,R,S or Y Gradient and screen_width bytes with a VGradient or screen height bytes with an HGradient. </p>
<dt>*FvwmBacker: DoNotRetainPixmap</p>
<dd>Cancels the effect of the previous option. This is the default. </p>
</dl>
<h2>Run-Time Configuration</h2>
<p>It it possible to replace FvwmBacker&#8217;s configuration at run-time, although it is not yet possible to remove existing configuration lines. This is done by simply removing the old configuration from withing fvwm and then read a new one. This can be done in many ways, for example by using an fvwm function or one of the modules <code>FvwmCommand</code> or <code>FvwmConsole</code>. </p>
<p> Example: </p>
<pre>DestroyModuleConfig FvwmBacker*
*FvwmBacker: Command (Desk 0) -solid black
*FvwmBacker: Command (Desk 1) -solid blue</pre>
<h2>Old-Style Options</h2>
<p>There is continued support for the now deprecated option: </p>
<dl>
<dt>*FvwmBacker: Desk <i>d command</i></p>
<dd>It is functionally equivalent to omitting the page coordinates with <i>*FvwmBacker: Command</i>: </p>
<pre>*FvwmBacker: Command (Desk Id) command</pre>
</dl>
<h2>Sample Configuration</h2>
<p>The following are excerpts from an .fvwm2rc file which describe FvwmBacker initialization commands: </p>
<pre>####
# Set Up Backgrounds for different desktop pages (2 desks, 3x2 pages).
####
*FvwmBacker: Command (Page 2 *) -solid steelblue
*FvwmBacker: Command (Desk 0, Page 0 0) Exec fvwm-root $[HOME]/bg2.xpm
*FvwmBacker: Command (Desk 0, Page 0 1) -solid midnightblue
*FvwmBacker: Command (Desk 0, Page 1 *) -solid yellow
*FvwmBacker: Command (Desk 1, Page * 0) -solid navy
*FvwmBacker: Command (Desk 1, Page * 1) Colorset 5</pre>
<h2>Author</h2>
<p>Mike Finger (mfinger [at] mermaid.micro.umn.edu)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>(Mike_Finger [at] atk.com)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>(doodman on IRC, check the&nbsp;<wbr>#linux channel)</p>
<h2>Modified by</h2>
<p>Andrew Davison (davison [at] cs.monash.edu.au) </p>
<p> Michael Han (mikehan [at] best.com) </p>
<p> Mikhael Goikhman (migo [at] homemail.com)</p>
