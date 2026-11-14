---
title: "xdotool(1)"
name: "xdotool"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xdotool/"
description: "xdotool – command-line X11 automation tool"
---

<h2 class="name">NAME</h2>
<p> xdotool &#8211; command-line X11 automation tool </p>
<h2>SYNOPSIS</h2>
<p> <code>xdotool</code> <i>cmd</i> <i>args&#8230;</i> </p>
<p> Notation: Some documentation uses <i>[window]</i> to denote an optional window argument. This case means that the argument, if not present, will default to &#8220;%1&#8221;. See &#8220;<font SIZE="-1">WINDOW STACK&#8221;</font> for what &#8220;%1&#8221; means.</p>
<h2>DESCRIPTION</h2>
<p> <code>xdotool</code> lets you programmatically (or manually) simulate keyboard input and mouse activity, move and resize windows, etc. It does this using X11&#8217;s <font SIZE="-1">XTEST</font> extension and other Xlib functions. </p>
<p> There is some support for Extended Window Manager Hints (aka <font SIZE="-1">EWMH</font> or NetWM). See the &#8220;<font SIZE="-1">EXTENDED WINDOW MANAGER HINTS&#8221;</font> section for more information.</p>
<h2>KEYBOARD COMMANDS</h2>
<dl>
<dt><code>key</code> <i>[options]</i> <i>keystroke</i> [<i>keystroke</i> &#8230;]</p>
<dd> Options:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>&#8211;window window</code></p>
<dd> Send keystrokes to a specific window id. You can use &#8220;<font SIZE="-1">WINDOW STACK&#8221;</font> references like &#8220;%1&#8221; and &#8220;%@&#8221; here. If there is a window stack, then &#8220;%1&#8221; is the default, otherwise the current window is used. </p>
<p> See also: &#8220;<font SIZE="-1">SENDEVENT NOTES&#8221;</font> and &#8220;<font SIZE="-1">WINDOW STACK&#8221;</font></p>
<dt><code>&#8211;clearmodifiers</code></p>
<dd> Clear modifiers before sending keystrokes. See <font SIZE="-1">CLEARMODIFIERS</font> below.</p>
<dt><code>&#8211;delay milliseconds</code></p>
<dd> Delay between keystrokes. Default is 12ms.</dl>
</dl>
<dl>
<dt>
<dd>
<p> Type a given keystroke. Examples being &#8220;alt+r&#8221;, &#8220;Control_L+J&#8221;, &#8220;ctrl+alt+n&#8221;, &#8220;BackSpace&#8221;. </p>
<p> Generally, any valid X Keysym string will work. Multiple keys are separated by &#8216;+&#8217;. Aliases exist for &#8220;alt&#8221;, &#8220;ctrl&#8221;, &#8220;shift&#8221;, &#8220;super&#8221;, and &#8220;meta&#8221; which all map to Foo_L, such as Alt_L and Control_L, etc. </p>
<p> In cases where your keyboard doesn&#8217;t actually have the key you want to type, xdotool will automatically find an unused keycode and use that to type the key. </p>
<p> With respect to &#8220;<font SIZE="-1">COMMAND CHAINING&#8221;</font>, this command consumes the remainder of the arguments or until a new xdotool command is seen, because no xdotool commands are valid keystrokes. </p>
<p> Example: Send the keystroke &#8220;F2&#8221;<br />
&nbsp;xdotool key F2 </p>
<p> Example: Send &#8216;a&#8217; with an accent over it (not on English keyboards, but still works with xdotool)<br />
&nbsp;xdotool key Aacute </p>
<p> Example: Send ctrl+l and then BackSpace as separate keystrokes:<br />
&nbsp;xdotool key ctrl+l BackSpace </p>
<p> Example: Send ctrl+c to all windows matching title &#8216;gdb&#8217; (See &#8220;<font SIZE="-1">COMMAND CHAINING&#8221;</font>)<br />
&nbsp;xdotool search &#8211;name gdb key ctrl+c</dl>
<dt><code>keydown</code> <i>[options]</i> <i>keystroke</i></p>
<dd> Same as above, except only keydown (press) events are sent.</p>
<dt><code>keyup</code> <i>keystroke</i></p>
<dd> Same as above, except only keyup (release) events are sent.</p>
<dt><code>type</code> <i>[options]</i> <i>something to type</i></p>
<dd> Options:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>&#8211;window windowid</code></p>
<dd> Send keystrokes to a specific window id. See &#8220;<font SIZE="-1">SENDEVENT NOTES&#8221;</font> below. The default, if no window is given, depends on the window stack. If the window stack is empty the current window is typed at using <font SIZE="-1">XTEST.</font> Otherwise, the default is &#8220;%1&#8221; (see &#8220;<font SIZE="-1">WINDOW STACK&#8221;</font>).</p>
<dt><code>&#8211;delay milliseconds</code></p>
<dd> Delay between keystrokes. Default is 12ms.</p>
<dt><code>&#8211;clearmodifiers</code></p>
<dd> Clear modifiers before sending keystrokes. See <font SIZE="-1">CLEARMODIFIERS</font> below.</dl>
</dl>
<dl>
<dt>
<dd>
<p> Types as if you had typed it. Supports newlines and tabs (<font SIZE="-1">ASCII</font> newline and tab). Each keystroke is separated by a delay given by the <code>&#8211;delay</code> option. </p>
<p> With respect to &#8220;<font SIZE="-1">COMMAND CHAINING&#8221;</font>, this command consumes the remainder of the arguments and types them. That is, no commands can chain after &#8216;type&#8217;. </p>
<p> Example: to type &#8216;Hello world!&#8217; you would do:<br />
&nbsp;xdotool type&nbsp;&#8216;Hello world!&#8217;</dl>
</dl>
<h2>MOUSE COMMANDS</h2>
<dl>
<dt><code>mousemove</code> <i>[options]</i> <i>x y </i><font SIZE="-1"><i>OR</i></font><i> &#8216;restore&#8217;</i></p>
<dd> Move the mouse to the specific X and Y coordinates on the screen. </p>
<p> You can move the mouse to the previous location if you specify &#8216;restore&#8217; instead of an X and Y coordinate. Restoring only works if you have moved previously in this same command invocation. Further, it does not work with the &#8211;window option. </p>
<p> For example, to click the top-left corner of the screen and move the mouse to the original position before you moved it, use this:<br />
&nbsp;xdotool mousemove 0 0 click 1 mousemove restore</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>&#8211;window </code><font SIZE="-1"><code>WINDOW</code></font></p>
<dd> Specify a window to move relative to. Coordinates 0,0 are at the top left of the window you choose. </p>
<p> &#8220;<font SIZE="-1">WINDOW STACK&#8221;</font> references are valid here, such as <tt>%1</tt> and %@. Though, using %@ probably doesn&#8217;t make sense.</p>
<dt><code>&#8211;screen </code><font SIZE="-1"><code>SCREEN</code></font></p>
<dd> Move the mouse to the specified screen to move to. This is only useful if you have multiple screens and <font SIZE="-1">ARE NOT</font> using Xinerama. </p>
<p> The default is the current screen. If you specify &#8211;window, the &#8211;screen flag is ignored.</p>
<dt><code>&#8211;polar</code></p>
<dd> Use polar coordinates. This makes &#8216;x&#8217; an angle (in degrees, 0-360, etc) and &#8216;y&#8217; the distance. </p>
<p> Rotation starts at &#8216;up&#8217; (0 degrees) and rotates clockwise: 90 = right, 180 = down, 270 = left. </p>
<p> The origin defaults to the center of the current screen. If you specify a &#8211;window, then the origin is the center of that window.</p>
<dt><code>&#8211;clearmodifiers</code></p>
<dd> See <font SIZE="-1">CLEARMODIFIERS</font></p>
<dt><code>&#8211;sync</code></p>
<dd> After sending the mouse move request, wait until the mouse is actually moved. If no movement is necessary, we will not wait. This is useful for scripts that depend on actions being completed before moving on. </p>
<p> Note: We wait until the mouse moves at all, not necessarily that it actually reaches your intended destination. Some applications lock the mouse cursor to certain regions of the screen, so waiting for any movement is better in the general case than waiting for a specific target.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>mousemove_relative</code> [options] <i>x</i> <i>y</i></p>
<dd> Move the mouse x,y pixels relative to the current position of the mouse cursor.</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>&#8211;polar</code></p>
<dd> Use polar coordinates. This makes &#8216;x&#8217; an angle (in degrees, 0-360, etc) and &#8216;y&#8217; the distance. </p>
<p> Rotation starts at &#8216;up&#8217; (0 degrees) and rotates clockwise: 90 = right, 180 = down, 270 = left.</p>
<dt><code>&#8211;sync</code></p>
<dd> After sending the mouse move request, wait until the mouse is actually moved. If no movement is necessary, we will not wait. This is useful for scripts that depend on actions being completed before moving on. </p>
<p> Note that we wait until the mouse moves at all, not necessarily that it actually reaches your intended destination. Some applications lock the mouse cursor to certain regions of the screen, so waiting for any movement is better in the general case than waiting for a specific target.</p>
<dt><code>&#8211;clearmodifiers</code></p>
<dd> See <font SIZE="-1">CLEARMODIFIERS</font></dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>click</code> <i>[options]</i> <i>button</i></p>
<dd> Send a click, that is, a mousedown followed by mouseup for the given button with a short delay between the two (currently 12ms). </p>
<p> Buttons generally map this way: Left mouse is 1, middle is 2, right is 3, wheel up is 4, wheel down is 5.</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>&#8211;clearmodifiers</code></p>
<dd> Clear modifiers before clicking. See <font SIZE="-1">CLEARMODIFIERS</font> below.</p>
<dt><code>&#8211;repeat</code> <font SIZE="-1">REPEAT</font></p>
<dd> Specify how many times to click. Default is 1. For a double-click, use &#8216;&#8211;repeat 2&#8217;</p>
<dt><code>&#8211;delay</code> <font SIZE="-1">MILLISECONDS</font></p>
<dd> Specify how long, in milliseconds, to delay between clicks. This option is not used if the <i>&#8211;repeat</i> flag is set to 1 (default).</p>
<dt><code>&#8211;window</code> <font SIZE="-1">WINDOW</font></p>
<dd> Specify a window to send a click to. See &#8220;<font SIZE="-1">SENDEVENT NOTES&#8221;</font> below for caveats. Uses the current mouse position when generating the event. </p>
<p> The default, if no window is given, depends on the window stack. If the window stack is empty the current window is typed at using <font SIZE="-1">XTEST.</font> Otherwise, the default is &#8220;%1&#8221; (see &#8220;<font SIZE="-1">WINDOW STACK&#8221;</font>).</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>mousedown</code> <i>[options]</i> <i>button</i></p>
<dd> Same as <code>click</code>, except only a mouse down is sent.</p>
<dt><code>mouseup</code> <i>[options]</i> <i>button</i></p>
<dd> Same as <code>click</code>, except only a mouse up is sent.</p>
<dt><code>getmouselocation</code> <i>[&#8211;shell]</i></p>
<dd> Outputs the x, y, screen, and window id of the mouse cursor. Screen numbers will be nonzero if you have multiple monitors and are not using Xinerama.</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>&#8211;shell</code></p>
<dd> This makes getmouselocation output shell data you can eval. Example: </p>
<pre>
 % xdotool getmouselocation --shell
 X=880
 Y=443
 SCREEN=0
 WINDOW=16777250
 % eval $(xdotool getmouselocation --shell)
 % echo $X,$Y
 714,324
</pre>
</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>behave_screen_edge</code> <i>[options]</i> <i>where</i> <i>command &#8230;</i></p>
<dd> Bind an action to events when the mouse hits the screen edge or corner. </p>
<p> Options are:</p>
<dl>
<dt>
<dd>
<dl>
<dt><i>&#8211;delay </i><font SIZE="-1"><i>MILLISECONDS</i></font><i></i></p>
<dd> Delay in milliseconds before running the command. This allows you to require a given edge or corner to be held for a short period before your command will run. If you leave the edge or corner before the delay expires then the time will reset.</p>
<dt><i>&#8211;quiesce </i><font SIZE="-1"><i>MILLISECONDS</i></font><i></i></p>
<dd> Delay in milliseconds before the next command will run. This helps prevent accidentally running your command extra times; especially useful if you have a very short &#8211;delay (like the default of 0).</dl>
</dl>
<dl>
<dt>
<dd>
<p> Event timeline </p>
<pre>
 * Mouse hits an edge or corner.
 * If delay is nonzero, the mouse must stay in this edge or corner until delay time expires.
 * If still in the edge/corner, trigger.
 * If quiesce is nonzero, then there is a cool-down period where the next
   trigger cannot occur
</pre>
<p> Valid &#8216;where&#8217; values are:</p>
<dl>
<dt>left</p>
<dd>
<dt>top-left</p>
<dd>
<dt>top</p>
<dd>
<dt>top-right</p>
<dd>
<dt>right</p>
<dd>
<dt>bottom-left</p>
<dd>
<dt>bottom</p>
<dd>
<dt>bottom-right</p>
<dd></dl>
</dl>
<dl>
<dt>
<dd>
<p> Examples:<br />
&nbsp;#&nbsp;Activate google-chrome when you move the mouse to the bottom-left corner:<br />
&nbsp;xdotool behave_screen_edge bottom-left&nbsp;\<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;search &#8211;class google-chrome windowactivate </p>
<pre><code>
#Go to the next workspace(right).Known to work in GNOME(metacity and compiz)
xdotool behave_screen_edge-- delay 500 bottom - right key XF86Forward
#Activate firefox and do a web search in a new tab for text in your clipboard
                                                    xdotool behave_screen_edge-- delay 1000 top -
    left
        search-- classname Navigator
            windowactivate-- sync key-- delay 250 ctrl +
    t ctrl + k ctrl + v Return
</code></pre>
</dl>
</dl>
<h2>WINDOW COMMANDS</h2>
<dl>
<dt><code>search</code> <i>[options]</i> <i>pattern</i></p>
<dd> Search for windows with titles, names, or classes with a regular expression pattern. The output is line-delimited list of X window identifiers. If you are using &#8220;<font SIZE="-1">COMMAND CHAINING&#8221;</font>, the search command will only write window ids to stdout if it is the last (or only) command in the chain; otherwise, it is silent. </p>
<p> The result is saved to the window stack for future chained commands. See &#8220;<font SIZE="-1">WINDOW STACK&#8221;</font> and &#8220;<font SIZE="-1">COMMAND CHAINING&#8221;</font> for details. </p>
<p> The default options are <tt>&quot;--name --class --classname&quot;</tt> (unless you specify one one or more of &#8211;name &#8211;class or &#8211;classname). </p>
<p> The options available are:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>&#8211;class</code></p>
<dd> Match against the window class.</p>
<dt><code>&#8211;classname</code></p>
<dd> Match against the window classname.</p>
<dt><code>&#8211;maxdepth</code> N</p>
<dd> Set recursion/child search depth. Default is -1, meaning infinite. 0 means no depth, only root windows will be searched. If you only want toplevel windows, set maxdepth of 1 (or 2, depending on how your window manager does decorations).</p>
<dt><code>&#8211;name</code></p>
<dd> Match against the window name. This is the same string that is displayed in the window titlebar.</p>
<dt><code>&#8211;onlyvisible</code></p>
<dd> Show only visible windows in the results. This means ones with map state IsViewable.</p>
<dt><code>&#8211;pid </code><font SIZE="-1"><code>PID</code></font></p>
<dd> Match windows that belong to a specific process id. This may not work for some X applications that do not set this metadata on its windows.</p>
<dt><code>&#8211;screen N</code></p>
<dd> Select windows only on a specific screen. Default is to search all screens. Only meaningful if you have multiple displays and are not using Xinerama.</p>
<dt><code>&#8211;desktop N</code></p>
<dd> Only match windows on a certain desktop. &#8216;N&#8217; is a number. The default is to search all desktops.</p>
<dt><code>&#8211;limit N</code></p>
<dd> Stop searching after finding N matching windows. Specifying a limit will help speed up your search if you only want a few results. </p>
<p> The default is no search limit (which is equivalent to &#8216;&#8211;limit 0&#8217;)</p>
<dt><code>&#8211;title</code></p>
<dd> <font SIZE="-1">DEPRECATED.</font> See &#8211;name.</p>
<dt><code>&#8211;all</code></p>
<dd> Require that all conditions be met. For example: </p>
<pre>
 xdotool search --all --pid 1424 --name &quot;Hello World&quot;
</pre>
<p> This will match only windows that have &#8220;Hello World&#8221; as a name and are owned by pid 1424.</p>
<dt><code>&#8211;any</code></p>
<dd> Match windows that match any condition (logically, &#8216;or&#8217;). This is on by default. For example: </p>
<pre>
 xdotool search --any --pid 1424 --name &quot;Hello World&quot;
</pre>
<p> This will match any windows owned by pid 1424 or windows with name &#8220;Hello World&#8221;</p>
<dt><code>&#8211;sync </code></p>
<dd> Block until there are results. This is useful when you are launching an application and want to wait until the application window is visible. For example: </p>
<pre>
 google-chrome &amp;
 xdotool search --sync --onlyvisible --class &quot;google-chrome&quot;
</pre>
</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>selectwindow</code></p>
<dd> Get the window id (for a client) by clicking on it. Useful for having scripts query you humans for what window to act on. For example, killing a window by clicking on it: </p>
<pre>
 xdotool selectwindow windowkill
</pre>
<dt><code>behave</code> <i>window</i> <i>action</i> <i>command &#8230;</i></p>
<dd> Bind an action to an event on a window. This lets you run additional xdotool commands whenever a matched event occurs. </p>
<p> The command run as a result of the behavior is run with <tt>%1</tt> being the window that was acted upon. Examples follow after the event list. </p>
<p> The following are valid events:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>mouse-enter</code></p>
<dd> Fires when the mouse enters a window. This is similar to &#8216;mouse over&#8217; events in javascript, if that helps.</p>
<dt><code>mouse-leave</code></p>
<dd> Fires when the mouse leaves a window. This is the opposite of &#8216;mouse-enter&#8217;</p>
<dt><code>mouse-click</code></p>
<dd> Fires when the mouse is clicked. Specifically, when the mouse button is released.</p>
<dt><code>focus</code></p>
<dd> Fires when the window gets input focus.</p>
<dt><code>blur</code></p>
<dd> Fires when the window loses focus.</dl>
</dl>
<dl>
<dt>
<dd>
<p> Examples: </p>
<pre>
 # Print the cursor location whenever the mouse enters a currently-visible
 # window:
 xdotool search --onlyvisible . behave %@ mouse-enter getmouselocation
 # Print the window title and pid whenever an xterm gets focus
 xdotool search --class xterm behave %@ focus getwindowname getwindowpid
 # Emulate focus-follows-mouse
 xdotool search . behave %@ mouse-enter windowfocus
</pre>
</dl>
<dt><code>getwindowpid</code> <i>[window]</i></p>
<dd> Output the <font SIZE="-1">PID</font> owning a given window. This requires effort from the application owning a window and may not work for all windows. This uses _NET_WM_PID property of the window. See &#8220;<font SIZE="-1">EXTENDED WINDOW MANAGER HINTS&#8221;</font> below for more information. </p>
<p> If no window is given, the default is &#8216;%1&#8217;. If no windows are on the stack, then this is an error. See &#8220;<font SIZE="-1">WINDOW STACK&#8221;</font> for more details. </p>
<p> Example: Find the <font SIZE="-1">PID</font> for all xterms:<br />
&nbsp;xdotool search &#8211;class xterm getwindowpid&nbsp;%@</p>
<dt><code>getwindowname</code> <i>[window]</i></p>
<dd> Output the name of a given window, also known as the title. This is the text displayed in the window&#8217;s titlebar by your window manager. </p>
<p> If no window is given, the default is &#8216;%1&#8217;. If no windows are on the stack, then this is an error. See &#8220;<font SIZE="-1">WINDOW STACK&#8221;</font> for more details.</p>
<dt><code>getwindowgeometry</code> [options] <i>[window]</i></p>
<dd> Output the geometry (location and position) of a window. The values include: x, y, width, height, and screen number.</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>&#8211;shell</code></p>
<dd> Output values suitable for &#8216;eval&#8217; in a shell.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>getwindowfocus</code> [-f]</p>
<dd> Prints the window id of the currently focused window. Saves the result to the window stack. See &#8220;<font SIZE="-1">WINDOW STACK&#8221;</font> for more details. </p>
<p> If the current window has no <font SIZE="-1">WM_CLASS</font> property, we assume it is not a normal top-level window and traverse up the parents until we find a window with a <font SIZE="-1">WM_CLASS</font> set and return that window id. </p>
<p> If you really want the window currently having focus and don&#8217;t care if it has a <font SIZE="-1">WM_CLASS</font> setting, then use &#8216;getwindowfocus -f&#8217;</p>
<dt><code>windowsize</code> [options] [window] width height</p>
<dd> Set the window size of the given window. If no window is given, <tt>%1</tt> is the default. See &#8220;<font SIZE="-1">WINDOW STACK&#8221;</font> and &#8220;<font SIZE="-1">COMMAND CHAINING&#8221;</font> for more details. </p>
<p> Percentages are valid for width and height. They are relative to the geometry of the screen the window is on. For example, to make a window the full width of the screen, but half height: </p>
<pre>
 xdotool windowsize I&lt;window&gt; 100% 50%
</pre>
<p> Percentages are valid with &#8211;usehints and still mean pixel-width relative to the screen size. </p>
<p> The options available are:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>&#8211;usehints</code></p>
<dd> Use window sizing hints (when available) to set width and height. This is useful on terminals for setting the size based on row/column of text rather than pixels.</p>
<dt><code>&#8211;sync</code></p>
<dd> After sending the window size request, wait until the window is actually resized. If no change is necessary, we will not wait. This is useful for scripts that depend on actions being completed before moving on. </p>
<p> Note: Because many window managers may ignore or alter the original resize request, we will wait until the size changes from its original size, not necessary to the requested size.</dl>
</dl>
<dl>
<dt>
<dd>
<p> Example: To set a terminal to be 80&#215;24 characters, you would use:<br />
&nbsp;xdotool windowsize &#8211;usehints&nbsp;<i>some_windowid</i>&nbsp;80 24</dl>
<dt><code>windowmove</code> <i>[options]</i> <i>[window]</i> <i>x</i> <i>y</i></p>
<dd> Move the window to the given position. If no window is given, <tt>%1</tt> is the default. See &#8220;<font SIZE="-1">WINDOW STACK&#8221;</font> and &#8220;<font SIZE="-1">COMMAND CHAINING&#8221;</font> for more details. </p>
<p> If the given x coordinate is literally &#8216;x&#8217;, then the window&#8217;s current x position will be unchanged. The same applies for &#8216;y&#8217;. </p>
<p> Examples: </p>
<pre>
 xdotool getactivewindow windowmove 100 100    # Moves to 100,100
 xdotool getactivewindow windowmove x 100      # Moves to x,100
 xdotool getactivewindow windowmove 100 y      # Moves to 100,y
 xdotool getactivewindow windowmove 100 y      # Moves to 100,y
</pre>
<p> Percentages are valid for width and height. They are relative to the geometry of the screen the window is on. For example, to make a window the full width of the screen, but half height: </p>
<pre>
 xdotool windowmove I&lt;window&gt; 100% 50%
</pre>
<dl>
<dt>
<dd>
<dl>
<dt><code>&#8211;sync</code></p>
<dd> After sending the window move request, wait until the window is actually moved. If no movement is necessary, we will not wait. This is useful for scripts that depend on actions being completed before moving on.</p>
<dt><code>&#8211;relative</code></p>
<dd> Make movement relative to the current window position.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>windowfocus</code> <i>[options]</i> <i>[window]</i></p>
<dd> Focus a window. If no window is given, <tt>%1</tt> is the default. See &#8220;<font SIZE="-1">WINDOW STACK&#8221;</font> and &#8220;<font SIZE="-1">COMMAND CHAINING&#8221;</font> for more details. </p>
<p> Uses XSetInputFocus which may be ignored by some window managers or programs.</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>&#8211;sync</code></p>
<dd> After sending the window focus request, wait until the window is actually focused. This is useful for scripts that depend on actions being completed before moving on.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>windowmap</code> <i>[options]</i> <i>[window]</i></p>
<dd> Map a window. In X11 terminology, mapping a window means making it visible on the screen. If no window is given, <tt>%1</tt> is the default. See &#8220;<font SIZE="-1">WINDOW STACK&#8221;</font> and &#8220;<font SIZE="-1">COMMAND CHAINING&#8221;</font> for more details.</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>&#8211;sync</code></p>
<dd> After requesting the window map, wait until the window is actually mapped (visible). This is useful for scripts that depend on actions being completed before moving on.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>windowminimize</code> <i>[options]</i> <i>[window]</i></p>
<dd> Minimize a window. In X11 terminology, this is called &#8216;iconify.&#8217; If no window is given, <tt>%1</tt> is the default. See &#8220;<font SIZE="-1">WINDOW STACK&#8221;</font> and &#8220;<font SIZE="-1">COMMAND CHAINING&#8221;</font> for more details.</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>&#8211;sync</code></p>
<dd> After requesting the window minimize, wait until the window is actually minimized. This is useful for scripts that depend on actions being completed before moving on.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>windowraise</code> <i>[window_id=%1]</i></p>
<dd> Raise the window to the top of the stack. This may not work on all window managers. If no window is given, <tt>%1</tt> is the default. See &#8220;<font SIZE="-1">WINDOW STACK&#8221;</font> and &#8220;<font SIZE="-1">COMMAND CHAINING&#8221;</font> for more details.</p>
<dt><code>windowreparent</code> <i>[source_window]</i> <i>destination_window</i></p>
<dd> Reparent a window. This moves the <i>source_window</i> to be a child window of <i>destination_window</i>. If no source is given, <tt>%1</tt> is the default. &#8220;<font SIZE="-1">WINDOW STACK&#8221;</font> window references (like <tt>%1</tt>) are valid for both <i>source_window</i> and <i>destination_window</i> See &#8220;<font SIZE="-1">WINDOW STACK&#8221;</font> and &#8220;<font SIZE="-1">COMMAND CHAINING&#8221;</font> for more details.</p>
<dt><code>windowclose</code> <i>[window]</i></p>
<dd> Close a window. This action will destroy the window, but will not try to kill the client controlling it. If no window is given, <tt>%1</tt> is the default. See &#8220;<font SIZE="-1">WINDOW STACK&#8221;</font> and &#8220;<font SIZE="-1">COMMAND CHAINING&#8221;</font> for more details.</p>
<dt><code>windowkill</code> <i>[window]</i></p>
<dd> Kill a window. This action will destroy the window and kill the client controlling it. If no window is given, <tt>%1</tt> is the default. See <font SIZE="-1">WINDOW STACK</font> and &#8220;<font SIZE="-1">COMMAND CHAINING&#8221;</font> for more details.</p>
<dt><code>windowunmap</code> <i>[options]</i> <i>[window_id=%1]</i></p>
<dd> Unmap a window, making it no longer appear on your screen. If no window is given, <tt>%1</tt> is the default. See &#8220;<font SIZE="-1">WINDOW STACK&#8221;</font> and &#8220;<font SIZE="-1">COMMAND CHAINING&#8221;</font> for more details.</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>&#8211;sync</code></p>
<dd> After requesting the window unmap, wait until the window is actually unmapped (hidden). This is useful for scripts that depend on actions being completed before moving on.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>set_window</code> <i>[options]</i> <i>[windowid=%1]</i></p>
<dd> Set properties about a window. If no window is given, <tt>%1</tt> is the default. See &#8220;<font SIZE="-1">WINDOW STACK&#8221;</font> and &#8220;<font SIZE="-1">COMMAND CHAINING&#8221;</font> for more details. </p>
<p> Options:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>&#8211;name newname</code></p>
<dd> Set window <font SIZE="-1">WM_NAME</font> (the window title, usually)</p>
<dt><code>&#8211;icon-name newiconname</code></p>
<dd> Set window <font SIZE="-1">WM_ICON_NAME</font> (the window title when minimized, usually)</p>
<dt><code>&#8211;role newrole</code></p>
<dd> Set window <font SIZE="-1">WM_WINDOW_ROLE</font></p>
<dt><code>&#8211;classname newclassname</code></p>
<dd> Set window class name (not to be confused with window class)</p>
<dt><code>&#8211;class newclass</code></p>
<dd> Set window class (not to be confused with window class name)</p>
<dt><code>&#8211;urgency value</code></p>
<dd> Set window urgency hint. If the value is 1, the window will be marked urgent, and the window manager will somehow highlight it for the user&#8217;s attention. If the value is 0, the window will be marked non-urgent.</p>
<dt><code>&#8211;overrideredirect value</code></p>
<dd> Set window&#8217;s override_redirect value. This value is a hint to the window manager for whether or not it should be managed. If the redirect value is 0, then the window manager will draw borders and treat this window normally. If the value is 1, the window manager will ignore this window. </p>
<p> If you change this value, your window manager may not notice the change until the window is mapped again, so you may want to issue &#8216;windowunmap&#8217; and &#8216;windowmap&#8217; to make the window manager take note.</dl>
</dl>
<dl>
<dt>
<dd></dl>
</dl>
<h2>DESKTOP AND WINDOW COMMANDS</h2>
<p> These commands follow the <font SIZE="-1">EWMH</font> standard. See the section &#8220;<font SIZE="-1">EXTENDED WINDOW MANAGER HINTS&#8221;</font> for more information.</p>
<dl>
<dt><code>windowactivate</code> <i>[options]</i> <i>[window]</i></p>
<dd> Activate the window. This command is different from windowfocus: if the window is on another desktop, we will switch to that desktop. It also uses a different method for bringing the window up. I recommend trying this command before using windowfocus, as it will work on more window managers. </p>
<p> If no window is given, <tt>%1</tt> is the default. See &#8220;<font SIZE="-1">WINDOW STACK&#8221;</font> and &#8220;<font SIZE="-1">COMMAND CHAINING&#8221;</font> for more details.</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>&#8211;sync</code></p>
<dd> After sending the window activation, wait until the window is actually activated. This is useful for scripts that depend on actions being completed before moving on.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>getactivewindow</code></p>
<dd> Output the current active window. This command is often more reliable than getwindowfocus. The result is saved to the window stack. See &#8220;<font SIZE="-1">WINDOW STACK&#8221;</font> for more details.</p>
<dt><code>set_num_desktops</code> <i>number</i></p>
<dd> Changes the number of desktops or workspaces.</p>
<dt><code>get_num_desktops</code></p>
<dd> Output the current number of desktops.</p>
<dt><code>get_desktop_viewport</code> <i>[&#8211;shell]</i></p>
<dd> Report the current viewport&#8217;s position. If &#8211;shell is given, the output is friendly to shell eval. </p>
<p> Viewports are sometimes used instead of &#8216;virtual desktops&#8217; on some window managers. A viewport is simply a view on a very large desktop area.</p>
<dt><code>set_desktop_viewport</code> <i>x</i> <i>y</i></p>
<dd> Move the viewport to the given position. Not all requests will be obeyed &#8211; some windowmangers only obey requests that align to workspace boundaries, such as the screen size. </p>
<p> For example, if your screen is 1280&#215;800, you can move to the 2nd workspace by doing:<br />
&nbsp;xdotool set_desktop_viewport 1280 0</p>
<dt><code>set_desktop</code> <i>[options]</i> <i>desktop_number</i></p>
<dd> Change the current view to the specified desktop.</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>&#8211;relative</code></p>
<dd> Use relative movements instead of absolute. This lets you move relative to the current desktop.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>get_desktop</code></p>
<dd> Output the current desktop in view.</p>
<dt><code>set_desktop_for_window</code> <i>[window]</i> <i>desktop_number</i></p>
<dd> Move a window to a different desktop. If no window is given, <tt>%1</tt> is the default. See &#8220;<font SIZE="-1">WINDOW STACK&#8221;</font> and &#8220;<font SIZE="-1">COMMAND CHAINING&#8221;</font> for more details.</p>
<dt><code>get_desktop_for_window</code> <i>[window]</i></p>
<dd> Output the desktop currently containing the given window. Move a window to a different desktop. If no window is given, <tt>%1</tt> is the default. See <font SIZE="-1">WINDOW STACK</font> and &#8220;<font SIZE="-1">COMMAND CHAINING&#8221;</font> for more details.</dl>
<h2>MISCELLANEOUS COMMANDS</h2>
<dl>
<dt><code>exec</code> <i>[options]</i> <i>command</i> <i>[&#8230;]</i></p>
<dd> Execute a program. This is often useful when combined with behave_screen_edge to do things like locking your screen. </p>
<p> Options:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>&#8211;sync</code></p>
<dd> Block until the child process exits. The child process exit status is then passed to the parent process (xdotool) which copies it.</dl>
</dl>
<dl>
<dt>
<dd>
<p> Examples:<br />
&nbsp;#&nbsp;Lock the screen when the mouse sits in the top-right corner<br />
&nbsp;xdotool behave_screen_edge &#8211;delay 1000 top-right&nbsp;\<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;exec gnome-screensaver-command &#8211;lock<br />
&nbsp;#&nbsp;Substitute&nbsp;&#8216;xscreensaver-command -lock&#8217;&nbsp;if you use that program. </p>
<pre>
 # The following will fail to move the mouse because we use '--sync' and
 # /bin/false exits nonzero:
 xdotool exec --sync /bin/false mousemove 0 0
 # This succeeds, though, since we do not use --sync on the exec command.
 xdotool exec /bin/false mousemove 0 0
</pre>
</dl>
<dt><code>sleep</code> <i>seconds</i></p>
<dd> Sleep for a specified period. Fractions of seconds (like 1.3, or 0.4) are valid, here.</dl>
<h2>SCRIPTS</h2>
<p> xdotool can read a list of commands via stdin or a file if you want. A script will fail when any command fails. </p>
<p> Truthfully, &#8216;script&#8217; mode isn&#8217;t fully fleshed out and may fall below your expectations. If you have suggestions, please email the list or file a bug (See <font SIZE="-1">CONTACT</font>). </p>
<p> Scripts can use positional arguments (Represented by <tt>$1</tt>, <tt>$2</tt>, &#8230;) and environment variables (like <tt>$HOME</tt> or <tt>$WINDOWID</tt>). Quoting arguments should work as expected. </p>
<p> Scripts are processed for parameter and environment variable expansion and then run as if you had invoked xdotool with the entire script on one line (using <font SIZE="-1">COMMAND CHAINING</font>).</p>
<dl>
<dt>&bull;</p>
<dd> Read commands from a file: </p>
<pre>
 xdotool filename
</pre>
<dt>&bull;</p>
<dd> Read commands from stdin: </p>
<pre>
 xdotool -
</pre>
<dt>&bull;</p>
<dd> Read commands from a redirected file </p>
<pre>
 xdotool - &lt; myfile
</pre>
</dl>
<p> You can also write scripts that only execute xdotool. Example: </p>
<pre>
 #!/usr/local/bin/xdotool
 search --onlyvisible --classname $1
 windowsize %@ $2 $3
 windowraise %@
 windowmove %1 0 0
 windowmove %2 $2 0
 windowmove %3 0 $3
 windowmove %4 $2 $3
</pre>
<p> This script will take all windows matched by the classname query given by arg1 ($1) and sizes/moves them into a 2&#215;2 grid with windows sized by the 2nd and 3rd parameters. </p>
<p> Here&#8217;s an example usage: </p>
<pre>
 % ./myscript xterm 600 400
</pre>
<p> Running it like this will take 4 visible xterms, raise them, and move them into a 2&#215;2 tile grid with each window 600&#215;400 pixels in size.</p>
<h2>CLEARMODIFIERS</h2>
<p> Any command taking the <i>&#8211;clearmodifiers</i> flag will attempt to clear any active input modifiers during the command and restore them afterwards. </p>
<p> For example, if you were to run this command:<br />
&nbsp;xdotool key a </p>
<p> The result would be &#8216;a&#8217; or &#8216;A&#8217; depending on whether or not you were holding the shift key on your keyboard. Often it is undesirable to have any modifiers active, so you can tell xdotool to clear any active modifiers. </p>
<p> The order of operations if you hold shift while running &#8216;xdotool key &#8211;clearmodifiers a&#8217; is this:</p>
<dl>
<dt>1. Query for all active modifiers (finds shift, in this case)</p>
<dd>
<dt>2. Try to clear shift by sending &#8216;key up&#8217; for the shift key</p>
<dd>
<dt>3. Runs normal &#8216;xdotool key a&#8217;</p>
<dd>
<dt>4. Restore shift key by sending &#8216;key down&#8217; for shift</p>
<dd></dl>
<p> The <i>&#8211;clearmodifiers</i> flag can currently clear of the following:</p>
<dl>
<dt>&bull;</p>
<dd> any key in your active keymap that has a modifier associated with it. (See <i><a href="/docs/linux/man/1-xmodmap/">xmodmap</a></i>(1)&#8217;s &#8216;xmodmap -pm&#8217; output)</p>
<dt>&bull;</p>
<dd> mouse buttons (1, 2, 3, 4, and 5)</p>
<dt>&bull;</p>
<dd> caps lock</dl>
<h2>SENDEVENT NOTES</h2>
<p> If you are trying to send key input to a specific window, and it does not appear to be working, then it&#8217;s likely your application is ignoring the events xdotool is generating. This is fairly common. </p>
<p> Sending keystrokes to a specific window uses a different <font SIZE="-1">API</font> than simply typing to the active window. If you specify &#8216;xdotool type &#8211;window 12345 hello&#8217; xdotool will generate key events and send them directly to window 12345. However, X11 servers will set a special flag on all events generated in this way (see XEvent.xany.send_event in X11&#8217;s manual). Many programs observe this flag and reject these events. </p>
<p> It is important to note that for key and mouse events, we only use XSendEvent when a specific window is targeted. Otherwise, we use <font SIZE="-1">XTEST</font>. </p>
<p> Some programs can be configured to accept events even if they are generated by xdotool. Seek the documentation of your application for help. </p>
<p> Specific application notes (from the author&#8217;s testing): * Firefox 3 seems to ignore all input when it does not have focus. * xterm can be configured while running with ctrl+leftclick, &#8216;Allow SendEvents&#8217; * gnome-terminal appears to accept generated input by default.</p>
<h2>WINDOW STACK</h2>
<p> Certain commands (search, getactivewindow, getwindowfocus) will find windows for you. These results generally printed to stdout, but they are also saved to memory for future use during the lifetime of the xdotool process. See &#8220;<font SIZE="-1">COMMAND CHAINING&#8221;</font> for more information. </p>
<p> The only modifications support for the window stack are to replace it. That is, two of two sequential searches, only the last one&#8217;s results will be the window stack.</p>
<h2>COMMAND CHAINING</h2>
<p> xdotool supports running multiple commands on a single invocation. Generally, you&#8217;ll start with a search command (see &#8220;<font SIZE="-1">WINDOW STACK&#8221;</font>) and then perform a set of actions on those results. </p>
<p> To query the window stack, you can use special notation &#8220;%N&#8221; where N is a number or the &#8216;@&#8217; symbol. If <tt>%N</tt> is given, the Nth window will be selected from the window stack. Generally you will only want the first window or all windows. Note that the order of windows in the window stack corresponds to the window stacking order, i.e. the bottom-most window will be reported first (see <i><a href="/docs/linux/man/3-xquerytree/">XQueryTree</a></i>(3)). Thus the order of the windows in the window stack may not be consistent across invocations. </p>
<p> The notation described above is used as the &#8220;window&#8221; argument for any given command. </p>
<p> For example, to resize all xterms to 80&#215;24: </p>
<pre>
 xdotool search --class xterm -- windowsize --usehints %@ 80 24
</pre>
<p> Resize move the current window: </p>
<pre>
 xdotool getactivewindow windowmove 0 0
</pre>
<p> In all cases, the default window argument, if omitted, will default to &#8220;%1&#8221;. It is obviously an error if you omit the window argument and the window stack is empty. If you try to use the window stack and it is empty, it is also an error. </p>
<p> To activate the first firefox window found: </p>
<pre>
 xdotool search --class firefox windowactivate
</pre>
<p> These would error: </p>
<pre>
 xdotool windowactivate
 xdotool windowactivate %1
 xdotool windowactivate %@
</pre>
<p> When xdotool exits, the current window stack is lost. </p>
<p> Additionally, commands that modify the &#8220;<font SIZE="-1">WINDOW STACK&#8221;</font> will not print the results if they are not the last command. For example: </p>
<pre>
 # Output the active window:
 % xdotool getactivewindow
 20971533
 # Output the pid of the active window, but not the active window id:
 % xdotool getactivewindow getwindowpid
 4686
</pre>
<h2>EXTENDED WINDOW MANAGER HINTS</h2>
<p> The following pieces of the <font SIZE="-1">EWMH</font> standard are supported:</p>
<dl>
<dt>_NET_SUPPORTED</p>
<dd> Asks the window manager what is supported</p>
<dt>_NET_CURRENT_DESKTOP</p>
<dd> Query and set the current desktop. Support for this enables these commands: <tt>&quot;set_desktop&quot;</tt>, <tt>&quot;get_desktop&quot;</tt>.</p>
<dt>_NET_WM_DESKTOP</p>
<dd> Query and set what desktop a window is living in. Support for this enables these commands: <tt>&quot;set_desktop_for_window&quot;</tt>, <tt>&quot;get_desktop_for_window&quot;</tt>.</p>
<dt>_NET_ACTIVE_WINDOW</p>
<dd> Allows you to query and set the active window by asking the window manager to bring it forward. Support for this enables these commands: <tt>&quot;windowactivate&quot;</tt>, <tt>&quot;getactivewindow&quot;</tt>.</p>
<dt>_NET_WM_PID</p>
<dd> This feature is application dependent, not window-manager dependent. Query the <font SIZE="-1">PID</font> owning a given window. Support for this enables these commands: <tt>&quot;getwindowpid&quot;</tt>.</dl>
<h2>SUPPORTED FEATURES</h2>
<p> xdotool (and libxdo) will try to function under all circumstances. However, there may be some cases where functionality is not provided by your X server or by your window manager. In these cases, xdotool will try to detect and tell you if an action requires a feature not currently supported by your system. </p>
<p> For window-manager specific features, see &#8220;<font SIZE="-1">EXTENDED WINDOW MANAGER HINTS&#8221;</font>.</p>
<dl>
<dt><font SIZE="-1">XTEST</font></p>
<dd> If your X server does not support <font SIZE="-1">XTEST,</font> then some typing and mouse movement features may not work. Specifically, typing and mouse actions that act on the &#8220;current window&#8221; (window 0 in libxdo) are unlikely to work. </p>
<p> In most cases, <font SIZE="-1">XTEST</font> is a feature you can enable on your X server if it is not enabled by default. </p>
<p> You can see the list of supported X extensions by typing &#8216;xdpyinfo&#8217; and looking the text &#8216;number of extensions: &#8230;&#8217;</dl>
<h2>BUGS</h2>
<p> Typing unusual symbols under non-us keybindings is known to occasionally send the wrong character.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-xprop/">xprop</a></i>(1), <i><a href="/docs/linux/man/1-xwininfo/">xwininfo</a></i>(1), </p>
<p> Project site: &lt;<a rel="nofollow" href="http://www.semicomplete.com/projects/xdotool">http://www.semicomplete.com/projects/xdotool</a>&gt; </p>
<p> Source code and Issues: &lt;<a rel="nofollow" href="https://github.com/jordansissel/xdotool">https://github.com/jordansissel/xdotool</a>&gt; </p>
<p> <font SIZE="-1">EWMH</font> specification: &lt;<a rel="nofollow" href="http://standards.freedesktop.org/wm-spec/wm-spec-1.3.html">http://standards.freedesktop.org/wm-spec/wm-spec-1.3.html</a>&gt;</p>
<h2>CONTACT</h2>
<p> Please send questions to xdotool-users [at] googlegroups.com. File bugs and feature requests at the following <font SIZE="-1">URL:</font> </p>
<p> &lt;<a rel="nofollow" href="https://github.com/jordansissel/xdotool/issues">https://github.com/jordansissel/xdotool/issues</a>&gt; </p>
<p> Alternately, if you prefer email, feel free to file bugs by emailing the list. What works for you :)</p>
<h2>AUTHOR</h2>
<p> xdotool was written by Jordan Sissel. </p>
<p> This manual page was written originally by Daniel Kahn Gillmor &lt;dkg [at] fifthhorseman.net&gt; for the Debian project (but may be used by others). It is maintained by Jordan Sissel. </p>
<p> Patches, ideas, and other contributions by many, nice folks. See the <font SIZE="-1">CHANGELIST</font> file for who provided what. </p>
<h2>Index</h2>
