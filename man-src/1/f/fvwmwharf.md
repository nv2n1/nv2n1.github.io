---
title: "fvwmwharf(1)"
name: "fvwmwharf"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fvwmwharf/"
description: "FvwmWharf – the AfterStep application \"dock\" module ported to Fvwm."
---

<p>FvwmWharf &#8211; the AfterStep application &quot;dock&quot; module ported to Fvwm. </p>
<h2>Synopsis</h2>
<p>FvwmWharf is spawned by Fvwm, so no command line invocation will work. </p>
<h2>Description</h2>
<p>The FvwmWharf module is a free-floating application loader that can execute programs, &quot;Swallow&quot; running programs, and contain &quot;Folders&quot; of more applications, among other things. The user can press the first button at any time to trigger invocation of one of these functions, or the user can press button two in order to cause the entire Wharf to withdraw to the nearest corner in an iconified state. FvwmWharf only works when fvwm is used as the window manager. </p>
<h2>Copyrights</h2>
<p>The FvwmWharf module is copyright 1995 and 1996 by a variety of contributors. They are, in alphabetical order, Beat Christen, Frank Fejes, Alfredo Kenji Kojima, Dan Weeks, and Bo Yang </p>
<p> The GoodStuff program, and the concept for interfacing this module to the Window Manager, are all original work by Robert Nation </p>
<p> No guarantees or warranties or anything are provided or implied in any way whatsoever. Use this program at your own risk. Permission to use this program for any purpose is given, as long as the copyright is kept intact. </p>
<h2>Initialization</h2>
<p>During initialization, <i>FvwmWharf</i> gets config info from <code>fvwm</code>&#8216;s module configuration database (see <i><a href="/docs/linux/man/1-fvwm/">fvwm</a></i>(1), section <code>MODULE COMMANDS</code>) to obtain a description of button panel geometry, color, icons, and actions. </p>
<p> If the FvwmWharf executable is linked to another name, ie ln -s FvwmWharf Pier, then another module called Pier can be started, with a completely different configuration than FvwmWharf, simply by changing the keywords FvwmWharf&#8230; to Pier&#8230;. This way multiple button-bars can be used. </p>
<h2>Invocation</h2>
<p>FvwmWharf should be invoked in the same way as other fvwm modules. </p>
<h2>Configuration Options</h2>
<dl>
<dt>*FvwmWharfAnimate</p>
<dd>If specified, the opening and closing of Folders will be animated, rather than simply drawn in one frame. </p>
<dt>*FvwmWharfAnimateMain</p>
<dd>Designates that full-length Wharf windows will be animated. </p>
<dt>*FvwmWharfBgColor <i>color</i></p>
<dd>If <i>*FvwmWharfTextureType 0</i> is specified, <i>FvwmWharf</i>&#8216;s buttons will be filled with <i>color</i>. </p>
<dt>*FvwmWharfColorset <i>colorset</i></p>
<dd>Tells the module to use colorset <i>colorset</i> for the background of all buttons. This option disables the options &#8216;BgColor&#8217;, &#8216;TextureType&#8217; and &#8216;TextureColor&#8217; if specified after these and is disabled by them if used before any of them in the configuration. Please refer to the man page of the FvwmTheme module for details about colorsets. </p>
<dt>*FvwmWharfColumns <i>columns</i></p>
<dd>Specifies the number of columns of buttons to be created. If unspecified, the number of columns will be set to 1. If the columns are set to a number greater than 1 then there will be that number of columns with enough rows to satisfy the requested number of buttons. </p>
<dt>*FvwmWharfForceSize</p>
<dd>If specified, will force pixmaps larger than 64&#215;64 to the default size. Pixmaps smaller than 64&#215;64 are not supported. </p>
<dt>*FvwmWharfFullPush</p>
<dd>If specified, the entire FvwmWharf button background will be moved down and to the right when pushed. Especially useful with *FvwmWharfNoBorder textures. </p>
<dt>*FvwmWharfGeometry <i>geometry</i></p>
<dd>Specifies the FvwmWharf window location and/or size. If the size is not specified, FvwmWharf will auto-size itself in a reasonable manner. The geometry is a standard X11 window geometry specification. This option is pre-set in the Nextstep(tm) style section for a consistent look and feel with NEXTSTEP(tm). Secondary FvwmWharf invocations from links may have their own geometry. </p>
<dt>*FvwmWharfMaxColors <i>number</i></p>
<dd>Specifies the maximum <i>number</i> of colors to use on a gradient fill. </p>
<dt>*FvwmWharfNoBorder</p>
<dd>Denotes that beveled borders should not be drawn around the FvwmWharf button. Useful with textures that include their own bevels. </p>
<dt>*FvwmWharfPixmap <i>pixmap</i></p>
<dd>Sets the pixmap file to be used as <i>FvwmWharf</i>&#8216;s button. To be used with <i>*FvwmWharfTextureType 128</i>. </p>
<dt>*FvwmWharfTextureColor <i>from</i> <i>to</i></p>
<dd>When used with a <i>*FvwmWharfTextureType</i> of 1 to 5, designates the ends of the gradient range to be used on <i>FvwmWharf</i>&#8216;s buttons. </p>
<dt>*FvwmWharfTextureType <i>type</i></p>
<dd>Specifies the type of gradient fill to be used on <i>FvwmWharf</i>&#8216;s buttons. Valid values are: </p>
<pre>0 - No texture - use <i>FvwmWharfBgColor</i> to set the desired color
1 - Gradient from upper-left to lower right
2 - Horizontal one way gradient from top to bottom
3 - Horizontal cylindrical gradient from top/bottom to center
4 - Vertical one way gradient from left to right
5 - Vertical cylindrical gradient from left/right to center
128 - User specified pixmap</pre>
<p>The default is the builtin <i>FvwmWharf</i> texture pixmap. </p>
<dt>*FvwmWharf <i>label icon command</i></p>
<dd>Specifies a window manager built-in command or folder to activate (folders will be discussed below), as described in the Fvwm man page, which should be executed when a button is pressed. The label field is an internal item that is still around from the GoodStuff module. The icon field specifies an X11 bitmap file, XPM color icon file, or a comma-delimited set of pixmaps containing the icon(s) to display on the button. FvwmWharf will search through the path specified in the ImagePath configuration item to find the icon file. </p>
<p> NOTE: Icons must have one transparent pixel or the definition of a transparent color in order to be valid. </p>
<p> If <i>command</i> is an fvwm Exec command, then the button will appear pushed in until the mouse button is released. </p>
<p> A single extension to the fvwm built-in command set is provided. A command of the form: </p>
<pre>*FvwmWharf junk clock.xpm Swallow &quot;Clock&quot; asclock -shape -12</pre>
<p>will cause FvwmWharf to spawn an asclock process, and capture the first window whose name or resource is &quot;Clock&quot;, and display it in the button-bar. This is handy for applications like xclock, xbiff, xload, asclock, and asmail. </p>
<p> Modules can be swallowed by specifying the word Module: </p>
<pre>*FvwmWharf pager nil Swallow &quot;Desktop&quot; Module FvwmPager 0 0</pre>
<p>NOTE: if you use xclock for this application, you will want to specify xclock -padding 0. </p>
<p> <i>Swallow</i> option tries to force an application to be 48 by 48 pixels. A special option <i>MaxSwallow</i> can be used to leave an application at its own size (but less then 64&#215;64). MaxSwallow is invoked the same way Swallow is. If you want an application to fill all the button place, you should start it with a proper geometry flag, like &quot;xload -g 64&#215;64&quot; or, if you want to leave a 3d-look: &quot;xload -g 60&#215;60&quot;. </p>
<p> Note, not all applications are good for swallowing, some can&#8217;t be resized at all, some can&#8217;t be resized exactly to 48&#215;48 or 64&#215;64, you are responsible for choosing suitable applications to be swallowed. </p>
<p> To create folder &quot;slide-outs&quot; in <code>FvwmWharf</code> the following format must be used: </p>
<pre>*FvwmWharf files Folders.xpm Folder
*FvwmWharf xftp 3DRings.xpm Exec xftp
*FvwmWharf xdir FolderDeposit.xpm Exec xdir
*FvwmWharf moxfm FilingCabinet.xpm Exec moxfm
*FvwmWharf ~Folders</pre>
<p>The first line of this set tells FvwmWharf that this button definition will be a folder. All of the button definitions between the <i>Folder</i> and the line with the definition of <i>*FvwmWharf ~Folders</i> will appear on the &quot;files&quot; folder when it is exposed. To expose the &quot;files&quot; folder simply click on the FvwmWharf button with the Folders.xpm icon showing. A button bar will appear perpendicular to your FvwmWharf bar and toward the center of the screen. On this smaller bar will be the three icons that were configured between the <i>Folder</i> and <i>~Folder</i> parts of the FvwmWharf configuration. As many folder buttons may be configured as is room on your screen. The only items that may not be configured within folders are Swallowed applications and more folders. </p>
</dl>
<h2>Drag And Drop</h2>
<p><i>FvwmWharf</i> supports the OffiX Drag and Drop standard. In order to have Drag and Drop enabled on a particular button, the following syntax must be adhered to: </p>
<pre>*FvwmWharf nil nil DropExec &quot;<i>program</i>&quot; <i>program</i> %s
*FvwmWharf <i>program</i> <i>iconname</i> Exec &quot;<i>program</i>&quot; <i>program</i></pre>
<p>The button will call <i>program</i> when pushed. If a file is dragged onto into it, <i>program</i> will be called with %s being replaced by the dropped filename. </p>
<h2>Authors</h2>
<pre>Beat Christen (bchriste [at] iiic.ethz.ch)
Frank Fejes (frank [at] ssax.com)
Alfredo Kengi Kojima (kojima [at] inf.ufrgs.br)
Dan Weeks (dan [at] mango.sfasu.edu)
Bo Yang (eric [at] coeus.ucsd.edu)</pre>
