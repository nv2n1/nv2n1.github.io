---
title: "fvwmdragwell(1)"
name: "fvwmdragwell"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fvwmdragwell/"
description: "FvwmDragWell – A XDND drag well"
---

<p>FvwmDragWell &#8211; A XDND drag well </p>
<h2>Synopsis</h2>
<p><code>FvwmDragWell</code> </p>
<p> FvwmDragWell is a Xdnd drag well. The user sends the data and type to the drag well via a fvwm SendToModule command. The drag well indicates that it received the information via a crude animation. The user may then drag the information from the well to other applications that support the Xdnd standard. The fvwm module FvwmWharf accepts drops of type &quot;text/uri-list&quot;. </p>
<h2>Initialization</h2>
<p>During initialization, <i>FvwmDragWell</i> gets config info from <code>fvwm</code>&#8216;s module configuration database (see <i><a href="/docs/linux/man/1-fvwm/">fvwm</a></i>(1), section <code>MODULE COMMANDS</code>). If the FvwmDragWell executable is linked to another name, i.e. ln -s FvwmDragWell OtherDragWell, then another module called OtherDragWell can be started, with a completely different configuration than FvwmDragWell, simply by changing the keyword FvwmDragWell to OtherDragWell. This way multiple FvwmDragWell programs may be used. </p>
<h2>Use</h2>
<p>Data is sent to the module from fvwm using the SendToModule Command. The form of the send to module command is: </p>
<pre>SendToModule modulename dragtype type-string, dragdata data</pre>
<p>type-string is a quoted string that declares the type of &quot;data&quot; and how the data will be exported. The &quot;typestring&quot; string is converted to an XAtom. The user should use standard Mime type strings, all in lower case. Note that the module does no data conversion. </p>
<p> There is one exception to the above format. If the datatype string is omitted, the module assumes that the user is passing a file or directory path. In this case, the string &quot;file://$hostname/&quot; is prepended to the data, and the data is exported as type &quot;text/uri-list&quot;. </p>
<p> Examples: </p>
<pre>SendToModule FvwmDragWell dragdata /usr/local/libexec/fvwm/2.4.0</pre>
<p>On hostname saturn, the drag well will convert the data to &quot;file://saturn/usr/local/libexec/fvwm/2.4.0&quot; and will export the data as type &quot;text/uri-list&quot;. The long form of this command would be </p>
<pre>SendToModule FvwmDragWell dragtype text/uri-list, \
 dragdata file://saturn/usr/local/libexec/fvwm/2.3.8</pre>
<h2>Invocation</h2>
<p>FvwmDragWell must be invoked from fvwm, so no command line invocation will work. </p>
<h2>Configuration Options</h2>
<p>FvwmDragWell reads the same .fvwm2rc file as fvwm reads when it starts up, and looks for certain configuration options: </p>
<dl>
<dt>*FvwmDragWell: Geometry <i>geometry</i></p>
<dd>Completely or partially specifies the Fvwm window location and geometry, in standard X11 notation. The default size is 48&#215;48. </p>
<dt>*FvwmDragWell: DragWellGeometry <i>geometry</i></p>
<dd>Specifies the geometry of the drag box in the FvwmDragWell window, in the standard X11 notation. Default is 30&#215;30+9+9 </p>
<dt>*FvwmDragWell: Colorset <i>colorset</i></p>
<dd>The colorset is used for the background and shading of the drag well. See the man page of FvwmTheme for a description of colorsets. </p>
<dt>*FvwmDragWell: Fore <i>Color</i></p>
<dd>The foreground color. The default foreground color is grey60. </p>
<dt>*FvwmDragWell: Back <i>Color</i></p>
<dd>The background color. The default background color is black. </p>
<dt>*FvwmDragWell: Shadow <i>Color</i></p>
<dd>The shadow color of the button relief. The default foreground relief color is grey20. </p>
<dt>*FvwmDragWell: Hilite <i>Color</i></p>
<dd>The hilight color of the button relief. The default background relief color is grey90. </p>
</dl>
<h2>Bugs</h2>
<h2>CREDITS and COPYRIGHTS</h2>
<p>The concept for interfacing this module to the Window Manager by Robert Nation. No guarantees or warranties or anything are provided or implied in any way whatsoever. Use this program at your own risk. Permission to use this program for any purpose is given, as long as the copyright is kept intact.</p>
