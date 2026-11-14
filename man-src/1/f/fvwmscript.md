---
title: "fvwmscript(1)"
name: "fvwmscript"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fvwmscript/"
description: "FvwmScript – module to build graphic user interface"
---

<p>FvwmScript &#8211; module to build graphic user interface</p>
<h2>Synopsis</h2>
<p>FvwmScript must be spawned by Fvwm. It will not work from the command line. </p>
<h2>Description</h2>
<p>FvwmScript is a module which allows you to build many graphical applications such as desktop accessories, button panel with pop up menus, modal dialogs&#8230; At the startup, FvwmScript reads the file which is specified on the command line. This file contains the script. This script is not included in the configuration file of Fvwm. </p>
<p> An FvwmScript script is fully controllable by using the keyboard. (Shift)-Tab circulates around the widgets, Return simulates a mouse click, the arrows move the cursor or change the values of the widget and Escape &quot;cancels&quot; for Menu and PopupMenu. </p>
<h2>Invocation</h2>
<p>FvwmScript can be invoked by inserting the line `Module FvwmScript name_of_script&#8217; in the .fvwm2rc file. The file &quot;name_of_script&quot; can start with a slash, in which case, it&#8217;s a fully qualified path, and the file is read. If &quot;name_of_script&quot; does not start with a slash, FvwmScript will look in a few different places. If the .fvwm2rc contained the command line `*FvwmScript: Path path_of_the_script_directory&#8217;, FvwmScript will try that directory. If that doesn&#8217;t work, FvwmScript tries the system configuration directory and the user configuration directory as described under the &quot;Read&quot; command in the fvwm man page. </p>
<p> The command to start FvwmScript can be placed on a line by itself, if FvwmScript is to be spawned during fvwm&#8217;s initialization, or can be bound to a menu or mouse button or keystroke to invoke it later. </p>
<h2>Configuration Options</h2>
<p>The following commands can be used in the config file (see <i><a href="/docs/linux/man/1-fvwm/">fvwm</a></i>(1), section <code>MODULE COMMANDS</code> for details). They are used only if the corresponding script commands are not used in the script. </p>
<dl>
<dt>*FvwmScript: DefaultFont <i>font</i></p>
<dd>Specifies the default font to be used. If not specified with this command or in the script with the Font command, fixed font is assumed. </p>
<dt>*FvwmScript: DefaultFore <i>color</i></p>
<dd>Specifies the default foreground color to be used. If not specified with this command or in the script with the ForeColor command, black is used. </p>
<dt>*FvwmScript: DefaultBack <i>color</i></p>
<dd>Specifies the default background color to be used. If not specified with this command or in the script with the BackColor command, grey85 is used. </p>
<dt>*FvwmScript: DefaultHilight <i>color</i></p>
<dd>Specifies the default hilight color to be used. If not specified with this command or in the script with the HilightColor command, grey100 is used. </p>
<dt>*FvwmScript: DefaultShadow <i>color</i></p>
<dd>Specifies the default shadow color to be used. If not specified with this command or in the script with the ShadowColor command, grey55 is used. </p>
<dt>*FvwmScript: DefaultColorset <i>colorset</i></p>
<dd>Tells the module to use colorset <i>colorset</i> as the default colorset. Refer to the FvwmTheme man page for details about colorsets. </p>
</dl>
<h2>Anatomy Of A Script</h2>
<p>FvwmScript uses a particular programming language. A script is composed of five parts. Heading contains general characteristics of the window and default properties for all widgets. The second part contains instructions whom are executed at the startup of the script. The third part contains periodic tasks which are executed every second. The fourth part contains instructions which are executed at exit. And the last part contains the description of widgets. A widget consists of eleven types of items: text labels, single-line text inputs, radio buttons, checkbox, push buttons, horizontal and vertical scrollbars, rectangles, pop up menus, swallowexecs and mini scrollbars. </p>
<h2>Heading Of A Script</h2>
<p>The syntax is as follows: </p>
<dl>
<dt>WindowTitle <i>string</i></p>
<dd>This option sets the window title. </p>
<dt>WindowSize <i>width height</i></p>
<dd>This option sets window size. <i>width</i> and <i>height</i> are numerical value. </p>
<dt>WindowPosition <i>x y</i></p>
<dd>This option sets window position. <i>x</i> and <i>y</i> are numerical value. </p>
<dt>ForeColor {<i>color</i>}</p>
<dd>This option sets the default foreground color for all widgets. </p>
<dt>BackColor {<i>color</i>}</p>
<dd>This option sets the default background color for all widgets. </p>
<dt>HilightColor {<i>color</i>}</p>
<dd>This option sets the default hilight color for all widgets. </p>
<dt>ShadowColor {<i>color</i>}</p>
<dd>This option sets the default shadow color for all widgets. </p>
<dt>Colorset {<i>n</i>}</p>
<dd>This option sets the default colorset for all widgets. </p>
<dt>Font {<i>font</i>}</p>
<dd>This option sets the default font for all widgets. </p>
<dt>UseGettext [<i>locale_path</i>]</p>
<dd>Enable the use of the gettext mechanism which is used by the WindowLocaleTitle, LocaleTitle, ChangeLocaleTitle instructions and the Gettext function. If no argument is given, the default FvwmScript locale catalog is used. This catalog is under the locale fvwm installation directory and the text domain is FvwmScript (install_prefix/share/locale/*/LC_MESSAGES/FvwmScript.mo). You can reset this catalog or add some catalogs exactly in the same way than with the <code>LocalePath</code> fvwm command (see the fvwm manual page). This instruction should be placed before the WindowLocaleTitle instruction. </p>
<dt>WindowLocaleTitle <i>string</i></p>
<dd>This option sets the window title, but use the locale catalog(s) defined with UseGettext. </p>
</dl>
<h2>Initialisation</h2>
<p>This part contains instructions which will be executed at the startup. For example: </p>
<pre>Init
 Begin
 Do &quot;Exec cat tada.voc &gt; /dev/dsp&quot;
 WarpPointer 1
 Set $ToDo=Restart
 End</pre>
<p>These instructions are used to play a sound, move the pointer to widget 1 and to initialize $ToDo to &quot;Restart&quot; at every startup. </p>
<h2>Periodic Tasks</h2>
<p>This part of the script contains instructions that are executed every second. For example: </p>
<pre>PeriodicTasks
 Begin
 If (RemainderOfDiv (GetTime) 10)==0 Then
 Do {Exec xcalc}
 End</pre>
<p>This example shows how to launch xcalc every 10 seconds. </p>
<h2>The Quit Function</h2>
<p>This part of the script contains instructions that are executed when the script exits (after the Quit instruction or if you close the window with the Close, Delete or Destroy fvwm command). For Example </p>
<pre>QuitFunc
 Begin
 Do {Echo bye, bye}
 End</pre>
<p>Be aware that if you used the KillModule fvwm command to close the script, some instructions or functions which rely on the existence of a communication link between the script and fvwm will not be executed (for example the Do command). To smoothly kill a script with an fvwm command see the <code>COMMANDS</code> section. </p>
<h2>Main Of A Script</h2>
<p>The second part of the script contains the description for every widget in the script. Each widget description has two parts. The first part describes initial properties, the second part contains instructions that are executed when the widget receives messages. All widgets can send and receive messages. All messages are identified by a number. The message &quot;UserAction&quot; is sent to a widget when the user operates the widget. The syntax for the first part is: </p>
<pre>Widget id # A number between 1 and 999 inclusive
Property
 Type string
 Size width height
 Position x y
 Title { string }
 Value int
 MaxValue int
 MinValue int
 Font string
 ForeColor { color }
 BackColor { color }
 HilightColor { color }
 ShadowColor { color }
 Colorset int
 Flags flagsOpt</pre>
<p>The flagsOpt option to Flags is a space separated list containing one or more of the keywords <i>Hidden</i>, <i>NoReliefString</i>, <i>NoFocus</i>, <i>Left</i> / <i>Center</i> / <i>Right</i>. <i>Hidden</i> is used to specify if the widget is hidden at startup. <i>NoReliefString</i> specifies if strings are drawn with relief or not. <i>NoFocus</i> specifies if the widget can get the keyboard focus or not. By default all widgets take focus, except Rectangle, HDipstick and VDipstick which cannot. Moreover, the NoFocus widgets are skipped when you circulate around the widgets with the (Shift-)Tab short cut. <i>Left</i> / <i>Center</i> / <i>Right</i> specifies the text position. These apply only to ItemDraw, List, Menu, PopupMenu and PushButton. The default is <i>Center</i> for ItemDraw and PushButton and <i>Left</i> for the other widgets. </p>
<p> LocaleTitle can be used in place of Title, for using the locale catalog(s) defined with UseGettext. </p>
<p> The position of every widget must be specified. </p>
<p> The syntax for the second part is: </p>
<pre>Main
 Case message of
 SingleClic:
 Begin
 # list of instructions which will be
 # executed when widget receives
 # message &quot;SingleClic&quot;. This message is
 # generated by the user.
 End
 1 :
 Begin
 # list of instructions which will be
 # executed when widget receives
 # message 1
 End
 End</pre>
<h2>List Of Widgets</h2>
<p>There is fifteen types of widgets. </p>
<dl>
<dt><code>CheckBox</code>: Display check box with a string.</p>
<dd><code>Title</code>: title of the check box. </p>
<p> <code>Value</code>: if Value is equal to 1, the box is checked else it is not. </p>
<p> The <code>Size</code> property is ignored. </p>
<dt><code>HDipstick</code>: Display a horizontal dipstick.</p>
<dd>This widget can be used to display disk usage. </p>
<p> <code>Value</code>: specify the current value of the dipstick. </p>
<p> <code>MinValue</code>: specify the minimum value of the dipstick. </p>
<p> <code>MaxValue</code>: specify the maximum value of the dipstick. </p>
<p> A minimum size of 30&#215;11 is imposed. </p>
<dt><code>HScrollBar</code>: Display an horizontal scrollbar.</p>
<dd><code>Value</code>: position of the thumb. </p>
<p> <code>MaxValue</code>: upper limit of Value. </p>
<p> <code>MinValue</code>: lower limit of Value. </p>
<p> The height property is ignored and a minimum width is imposed. The width should be at least the range plus 37 if all values are to be selectable e.g. a min of 0 and max of 10 has a range of 11 and therefore should have a minimum width of 48. </p>
<dt><code>ItemDraw</code>: Display an icon and/or a string.</p>
<dd><code>Title</code>: string to display. </p>
<p> <code>Icon</code>: icon to display. </p>
<p> <code>MaxValue</code>: x coordinate of the cursor. </p>
<p> <code>MinValue</code>: y coordinate of the cursor. </p>
<p> The size is made large enough to contain the title and/or the icon. </p>
<dt><code>List</code>: Display a list.</p>
<dd>List lets user to choose between various options. </p>
<p> <code>Value</code>: specify which option is selected. </p>
<p> <code>MinValue</code>: First visible option. </p>
<p> <code>Title</code>: title contains options displayed in the list. The syntax is the following: {Option 1|Option 2|&#8230;|Option N}. All menus are displayed at the top of window. </p>
<p> A minimum height of three items is imposed and the width is made to be at least 108. </p>
<dt><code>Menu</code>: Display a menu whom lets user to choose a option.</p>
<dd>Items of type Menu are layed out from left to right along the top of the window. The size and position properties are ignored. </p>
<p> <code>Value</code>: specify which option is selected. </p>
<p> <code>Title</code>: title contains options displayed in the menu. The syntax is the following: {Option 1|Option 2|&#8230;|Option N}. </p>
<dt><code>MiniScroll</code>: Display a very small vertical scrollbar.</p>
<dd><code>Value</code>: position of the thumb. </p>
<p> <code>MaxValue</code>: upper limit of Value. </p>
<p> <code>MinValue</code>: lower limit of Value. </p>
<p> The size is set to 19&#215;34. </p>
<dt><code>PopupMenu</code>: Display a pop up menu.</p>
<dd><code>Value</code>: specify what option is selected. </p>
<p> <code>Title</code>: the title has the following syntax: {Option 1|Option 2|&#8230;|Option N}.&quot;Option 1|Option 2|&#8230;|Option N&quot; is the pop up menu which is displayed when pressing mouse button. </p>
<p> The size property is ignored. </p>
<dt><code>PushButton</code>: Display push button with an icon and/or a string.</p>
<dd><code>Title</code>: this string has the following syntax {Title of the button|Option 1|Option 2|Option3|&#8230;|Option N}. &quot;Option 1|Option 2|&#8230;|Option N&quot; is the pop up menu which is displayed when pressing the right button. </p>
<p> <code>Icon</code>: icon to display. </p>
<p> The button is made large enough to fit the icon and or label. </p>
<dt><code>RadioButton</code>: Display radio button with a string.</p>
<dd><code>Title</code>: title of the radio button. </p>
<p> <code>Value</code>: if Value is equal to 1, the box is checked else it is not. </p>
<p> The size property is ignored </p>
<dt><code>Rectangle</code>: Display a rectangle.</p>
<dd>&nbsp;<wbr>This type of widget can be used to decorate window. </p>
<dt><code>SwallowExec</code></p>
<dd>This type of widget causes FvwmScript to spawn an process, and capture the first window whose name or resource is equal to Title, and display it in the script window. </p>
<p> <code>Title</code>: specify the window name which be captured and displayed in the script window. </p>
<p> <code>SwallowExec</code>: specify the command line to execute to spawn the process. Modules can also be swallowed. </p>
<p> <code>Value</code>: specify the looking of the border. Possible value: -1, 0, 1. </p>
<p> The size is made to be at least 30&#215;30 </p>
<dt><code>TextField</code>: Display a text input field.</p>
<dd>The text input field can be used to edit a single-line string. </p>
<p> <code>Title</code>: content of text field. </p>
<p> <code>Value</code>: position of the insert point. </p>
<p> <code>MinValue</code>: position of the end of the selection. </p>
<p> <code>MaxValue</code>: first visible character of the title </p>
<p> The height property is ignored, the width is made to be at least 40 pixels wider than the initial contents. </p>
<dt><code>VDipstick</code>: Display a vertical dipstick.</p>
<dd><code>Value</code>: specify the current value of the dipstick. </p>
<p> <code>MinValue</code>: specify the minimum value of the dipstick. </p>
<p> <code>MaxValue</code>: specify the maximum value of the dipstick. </p>
<p> The size is made to be at least 11&#215;30. </p>
<dt><code>VScrollBar</code>: Display a vertical scrollbar.</p>
<dd><code>Value</code>: position of the thumb. </p>
<p> <code>MaxValue</code>: upper limit of Value. </p>
<p> <code>MinValue</code>: lower limit of Value. </p>
<p> The width property is ignored and a minimum height is imposed. The height should be at least the range plus 37 if all values are to be selectable e.g. a min of 0 and max of 10 has a range of 11 and therefore should have a minimum height of 48. </p>
</dl>
<h2>Instructions</h2>
<p>Here is the description of all instructions. </p>
<dl>
<dt>HideWidget <i>id</i> : hide the widget numbered <i>id</i>.</p>
<dd>
<dt>ShowWidget <i>id</i>: show the widget numbered <i>id</i>.</p>
<dd>
<dt>ChangeValue <i>id1 id2</i></p>
<dd>Set the value of the widget numbered <i>id1</i> to <i>id2</i>. </p>
<dt>ChangeMaxValue <i>id1 id2</i></p>
<dd>Set the maximum value of the widget numbered <i>id1</i> to <i>id2</i>. </p>
<dt>ChangeMinValue <i>id1 id2</i></p>
<dd>Set the minimum value of the widget numbered <i>id1</i> to <i>id2</i>. </p>
<dt>ChangeTitle <i>id1 id2</i></p>
<dd>Set the title of the widget numbered <i>id1</i> to <i>id2</i>. </p>
<dt>ChangeWindowTitle <i>string</i></p>
<dd>Set the title of the window to <i>string</i>. </p>
<dt>ChangeWindowTitleFromArg <i>numarg</i></p>
<dd>Set the title of the window to the value of the <i>numarg</i>-th script argument. </p>
<dt>ChangeLocaleTitle <i>id1 id2</i></p>
<dd>As ChangeTitle but use the locale catalog(s) defined with UseGettext. </p>
<dt>ChangeIcon <i>id1 id2</i></p>
<dd>Set the icon of the widget numbered <i>id1</i> to <i>id2</i>. </p>
<dt>ChangeForeColor <i>id1</i> {<i>color</i>}</p>
<dd>Set the foreground color of the widget numbered <i>id1</i> to {<i>color</i>}. </p>
<dt>ChangeBackColor <i>id1</i> {<i>color</i>}</p>
<dd>Set the background color of the widget numbered <i>id1</i> to {<i>color</i>}. </p>
<dt>ChangeColorSet <i>id1</i> <i>id2</i></p>
<dd>Set the colorset of the widget numbered <i>id1</i> to <i>id2</i>. Specifying widget 0 sets the main window colorset. </p>
<dt>ChangePosition <i>id1 x y</i></p>
<dd>Move the widget numbered <i>id1</i> to position (<i>x</i>,<i>y</i>). </p>
<dt>ChangeSize <i>id1 width height</i></p>
<dd>Set the size of the widget numbered <i>id1</i> to (<i>width</i>,<i>height</i>). </p>
<dt>ChangeFont <i>id1 newfont</i></p>
<dd>Set the font of the widget numbered <i>id1</i> to <i>newfont</i>. </p>
<dt>WarpPointer <i>id</i></p>
<dd>Warp the mouse pointer into the widget numbered <i>id</i>. </p>
<dt>WriteToFile <i>filename</i> {<i>str1</i>} {<i>str2</i>} etc</p>
<dd>Write to the file <i>filename</i> the string which is the concatenation of all arguments <i>str1</i>, <i>str2</i>, etc. </p>
<dt>Do {<i>command args</i>}</p>
<dd>Execute the fvwm command inside the Do block. Any fvwm command as described in the fvwm2 man page can be used. Commands are sent from this module to the fvwm main program for processing. The length of the command and arguments can not exceed 988 characters. </p>
<dt>Set $<i>var</i>={<i>str</i>1} {<i>str2</i>} etc</p>
<dd>Concatenate all arguments to a string and set the variable $<i>var</i> to this string. </p>
<dt>Quit: quit the program.</p>
<dd>
<dt>SendSignal <i>id1 id2</i></p>
<dd>Send a message numbered <i>id2</i> to widget <i>id1</i>. </p>
<dt>SendToScript <i>id_script</i> {<i>str1</i>1} {<i>str2</i>} etc</p>
<dd>Send a message to the script identified by id_script. The message is the concatenation of str1, str2&#8230; </p>
<dt>Key <i>Keyname</i> <i>Modifier</i> <i>id</i> <i>sig</i> <i>str1</i> <i>str2</i> etc</p>
<dd>Binds a keyboard key to the instruction </p>
<p> SendSignal <i>id</i> <i>sig</i> </p>
<p> and sets the &quot;last string&quot; to the concatenation of str1, str2&#8230; (see the LastString function). The <i>Keyname</i> and <i>Modifiers</i> fields are defined as in the fvwm Key command. </p>
</dl>
<h2>Arguments</h2>
<p>Most of commands use arguments. There are two kinds of arguments: numbers and strings. A numerical argument is a value which is between -32000 and +32000. A string is always surrounded with braces. Variables always begin with the character &quot;$&quot; and can contain both numbers and strings. </p>
<h2>Functions</h2>
<p>All functions use arguments. Functions can return both a string and a number. The syntax is: </p>
<pre>(function argument1 argument2 etc)</pre>
<p>Here is the complete list of arguments: </p>
<dl>
<dt>(GetTitle <i>id</i>)</p>
<dd>Return the title of the widget numbered <i>id</i>. </p>
<dt>(GetValue <i>id</i>)</p>
<dd>Return the current value of the widget numbered <i>id</i>. </p>
<dt>(GetMinValue <i>id</i>)</p>
<dd>Return the current Min value of the widget numbered <i>id</i>. </p>
<dt>(GetMaxValue <i>id</i>)</p>
<dd>Return the current Max value of the widget numbered <i>id</i>. </p>
<dt>(GetFore <i>id</i>)</p>
<dd>Return the current RGB foreground value of the widget numbered <i>id</i> in the hex format RRGGBB. </p>
<dt>(GetBack <i>id</i>)</p>
<dd>Return the current RGB background value of the widget numbered <i>id</i> in the hex format RRGGBB. </p>
<dt>(GetHilight <i>id</i>)</p>
<dd>Return the current RGB hilight value of the widget numbered <i>id</i> in the hex format RRGGBB. </p>
<dt>(GetShadow <i>id</i>)</p>
<dd>Return the current RGB shadow value of the widget numbered <i>id</i> in the hex format RRGGBB. </p>
<dt>(GetOutput {<i>str</i>} <i>int1 int2</i>)</p>
<dd>Executes the command <i>str</i>, gets the standard output and returns the word which is in the line <i>int1</i> and in the position <i>int2</i>. If <i>int2</i> is equal to -1, GetOutput returns the complete line. </p>
<dt>(NumToHex <i>int</i>)</p>
<dd>Return the hexadecimal value of <i>int</i>. </p>
<dt>(HexToNum {<i>str</i>})</p>
<dd>Return the decimal value of <i>str</i>, <i>str</i> must be an hexadecimal value. </p>
<dt>(Add <i>int1 int2</i>)</p>
<dd>Return the result of (<i>int1</i>+<i>int2</i>). </p>
<dt>(Mult <i>int1 int2</i>)</p>
<dd>Return the result of (<i>int1</i>*<i>int2</i>). </p>
<dt>(Div <i>int1 int2</i>)</p>
<dd>Return the result of (<i>int1</i>/<i>int2</i>). </p>
<dt>(StrCopy {<i>str</i>} <i>int1 int2</i>)</p>
<dd>Return the string whom is between position int1 and int2. For example, (StrCopy {Hello} 1 2) returns {He} </p>
<dt>(LaunchScript {<i>str</i>})</p>
<dd>This function launches the script named str and returns an identification number. This number is necessary to use the functions SendToScript and ReceiveFromScript. The string str contains the script name and some arguments. </p>
<dt>(GetScriptArgument {<i>int</i>})</p>
<dd>This function returns the argument script used in the function LaunchScript. If int is equal to zero, GetScriptArgument returns the name of the script. </p>
<dt>(GetScriptFather)</p>
<dd>This function returns the identification number of the script father. </p>
<dt>(ReceivFromScript {<i>int</i>})</p>
<dd>This function returns the message sent by the script numbered int. </p>
<dt>(RemainderOfDiv {<i>int1 int2</i>}): t</p>
<dd>This function returns the remainder of the division (<i>int1</i>/<i>int2</i>). </p>
<dt>(GetTime)</p>
<dd>This function returns the time in seconds. </p>
<dt>(GetPid)</p>
<dd>This function returns the process id of the script. </p>
<dt>(Gettext {<i>str</i>})</p>
<dd>This function return the translation of <i>str</i> by using the locale catalog(s) defined with UseGettext. </p>
<dt>(SendMsgAndGet {<i>comId</i>} {<i>cmd</i>} <i>bool</i>)</p>
<dd>Sends the command <i>cmd</i> with identifier <i>comId</i> to an external program ready to communicate with the script using a protocol specific to FvwmScript. If <i>bool</i> is 0 FvwmScript does not wait for an answer from the external program. In this case the returned value is 1 if the message can be sent to the external program and 0 if this is not the case. If <i>bool</i> is 1, then FvwmScript waits for an answer from the external program and the return value is this answer (a line of no more than 32000 characters). If the communication fails, the returned value is 0. See the section <code>A COMMUNICATION PROTOCOL</code> for a description of the communication protocol used. </p>
<dt>(Parse {<i>str</i>} <i>int</i>)</p>
<dd>where <i>str</i> must be a string of the form: </p>
<pre> X1S1X2S2X3S3...SnXn</pre>
<p>where the Xn are numbers containing four decimal digits and where Sn are strings of length exactly Xn. The returned value is the string S<i>int</i>. If <i>int</i> is out of range (e.g., &gt;n) the returned value is the empty string. If <i>str</i> is not of the specified form, the return value is unpredictable (but empty in the average). This function is useful to handle strings returned by the SendMsgAndGet function. </p>
<dt>(LastString)</p>
<dd>This function returns the &quot;current working string&quot; for the Key instruction and the SendString command (see the <code>COMMANDS</code> section). At startup this string is empty, but when a Key binding is detected (respectively, a SendString command is received), then this string is set to the string associated to the instruction (respectively, to the command). </p>
</dl>
<h2>Conditional Loops</h2>
<p>There are three kinds of conditional loops. The instruction &quot;If-Then-Else&quot; has the following syntax: </p>
<pre>If $ToDo=={Open xcalc} Then
 Do {Exec xcalc &amp;} # List of instructions
Else
Begin
 Do {Exec killall xcalc &amp;} # List of instructions
 Do {Exec echo xcalc killed &gt; /dev/console}
End</pre>
<p>The second part &quot;Else-Begin-End&quot; is optional. If the loop contains only one instruction, Begin and End can be omitted. The instruction &quot;While-Do&quot; has the following syntax: </p>
<pre>While $i&lt;5 Do
Begin
 Set $i=(Add i 1) # List of instructions
End</pre>
<p>Two strings can be compared with &quot;==&quot; and two numbers can be compared with &quot;&lt;&quot;, &quot;&lt;=&quot;, &quot;==&quot;, &quot;&gt;=&quot;, &quot;&gt;&quot;. The loop &quot;For-Do-Begin-End&quot; has the following syntax: </p>
<pre>For $i=1 To 20 Do
Begin
 Do {Exec xcalc &amp;}# List of instructions
End</pre>
<h2>Commands</h2>
<p>The following fvwm command may be executed at any time </p>
<p> SendToModule <i>ScriptName</i> SendString <i>id</i> <i>sig</i> <i>str</i> </p>
<p> it sends to any module with alias or name which matches <i>ScriptName</i> the string </p>
<p> SendString <i>id</i> <i>sig</i> <i>str</i> </p>
<p> When an FvwmScript receives such a message it sends to the Widget <i>id</i> the signal numbered <i>sig</i> and the string <i>str</i> can be obtained with the LastString function. Let us give an example. Say that you have a script MyScript with the widget: </p>
<pre>Widget 50
Property
 Type PushButton
 Title {Quit}
 ...
Main
Case message of
 SingleClic:
 Begin
 Quit
 End
 1 :
 Begin
 Set $str = (LastString)
 If $str == {Quit} Then
 Quit
 Else
 ChangeTitle 33 $str
 End
End</pre>
<p>Then the command </p>
<pre>SendToModule MyScript SendString 50 1 str</pre>
<p>forces MyScript to exit if str is equal to &quot;Quit&quot; and if not it changes the title of Widget 33 to str. </p>
<p> This command can be used to change the window title </p>
<p> SendToModule <i>ScriptName</i> ChangeWindowTitle <i>newTitle</i> <i>[oldTitle]</i> </p>
<p> it causes that any module with alias or name which matches <i>ScriptName</i> changes its associated window title to <i>newTitle</i>. The optional argument <i>oldTitle</i> makes sense when there are several instances of the same script. It permits one to avoid changing the name of all these instances by specifying the name of the window associated to the target script (see the example below). </p>
<pre>+ I Module FvwmScript FvwmStorageSend &quot;/dev/hda6&quot;
+ I Wait FvwmStorageSend
+ I SendToModule FvwmStorageSend ChangeWindowTitle HDA6
+ I Module FvwmScript FvwmStorageSend &quot;/dev/hda1&quot;
+ I Wait FvwmStorageSend
+ I SendToModule FvwmStorageSend ChangeWindowTitle HDA1 FvwmStorageSend</pre>
<p>Without the FvwmStorageSend argument in the last case, the SendToModule command would have changed to HDA1 the name of both instances of FvwmStorageSend. </p>
<h2>Examples</h2>
<p>You will find examples of scripts in the fvwm configuration directory. </p>
<p> FvwmScript-BellSetup, FvwmScript-KeyboardSetup, FvwmScript-PointerSetup and FvwmScript-ScreenSetup are a set of scripts that modify X settings. These scripts save preferences into a file named ~/.xinit-fvwmrc (If you want to use another file name, give it as the first argument of the script). If you want to load these preferences at every startup, you have to include the line &quot;.xinit-fvwmrc&quot; in your .xinitrc (or .xsession) file before starting fvwm. </p>
<p> FvwmScript-BaseConfig modifies fvwm focus and paging mouse policy, window placement, opacity and other features of the move and resize commands, snap attraction and shading animation. This script saves preferences into a file named .FvwmBaseConfig in the user&#8217;s data directory (i.e., $HOME/.fvwm or $FVWM_USERDIR if set). If you want to load these preferences at every startup you must add the line &quot;Read .FvwmBaseConfig&quot; in your fvwm configuration file. If you want to use another file name, give it as the first argument of the script. When you click on Ok or Apply an fvwm function that you may define named BaseConfigOkFunc or BaseConfigApplyFunc is called. This allows for reloading specific application styles that the script has destroyed (e.g., AddToFunc BaseConfigOkFunc I Read MyAppStyle). </p>
<p> FvwmScript-Buttons is a buttons panel which can replace FvwmButtons (this script supports popup menus and requires xload, xclock, FvwmPager, TkDesk). FvwmScript-Colorset allows you to edit your colorset (see FvwmTheme). FvwmScript-Date allows you to set date and time. FvwmScript-FileBrowser is a file browser used by the other scripts. FvwmScript-Find is an elementary front-end to find. FvwmScript-Quit allows one to quit fvwm, restart fvwm or some other window manager, or shut down and reboot the computer. FvwmScript-ScreenDump is a screen dumper. FvwmScript-WidgetDemo is a pure example script. See the next section for FvwmScript-ComExample. </p>
<h2>A Communication Protocol</h2>
<p>FvwmScript is a weak (but simple) programming language. If you need to deal with a lot of data and/or you need to use complex algorithms you should use an external program (in perl for example) and &quot;send&quot; the desired information to your FvwmScript script. The first approach is to use the GetOutput function. This is simple but you should rerun your external program each time you need information from it (and this may cause performances problems). The second approach is to use the SendMsgAndGet function which extends FvwmScript by using any programming language which can deal with named pipes (fifos). We describe this solution in this section. (A third approach is to use fvwm-themes-com from the fvwm-themes package, but in fact the SendMsgAndGet method is an implementation of fvwm-themes-com inside FvwmScript and this gives better performance). </p>
<p> Basically, you start an &quot;external&quot; program (the program for short) from your FvwmScript script (the script for short). This program runs in the background and you use the SendMsgAndGet function in your script to ask questions or to give instructions to the program. The program must strictly respect a certain communication protocol. First of all there is an identifier <i>comId</i> for the communication, it should contain the process id of the script for a good implementation of the protocol (use the GetPid function and pass the <i>comId</i> via an option to the program). The protocol uses two fifos, in the fvwm user directory, named: .tmp-com-in-<i>comId</i> and .tmp-com-out-<i>comId</i>. The program should create and listen on the .tmp-com-in-<i>comId</i> fifo. Then, when FvwmScript executes a function of the form: </p>
<p> Set $answer = (SendMsgAndGet {<i>comId</i>} {<i>cmd</i>} <i>bool</i>) </p>
<p> FvwmScript writes the <i>cmd</i> on this fifo. This way the program can read the <i>cmd</i> and can execute the appropriate action (it should remove the in fifo to support multi-communications). If <i>bool</i> is 0, FvwmScript does not wait for an answer from the program and return 1 if the previous actions succeed and 0 if they failed (then the program should &quot;go back&quot; to the in fifo). If <i>bool</i> is 1, then FvwmScript waits (20 sec) for an answer from the program and in turn returns the answer to the script (note that <i>bool</i> is not passed to the program as it must know which commands need an answer). To answer, the program creates the .tmp-com-out-<i>comId</i> fifo and writes the answer on it. The program should wait until FvwmScript reads the answer and then it should remove the out fifo and go back to the in fifo. The answer should consist of one line of no more than 32000 characters (take a look at the Parse function to handle multiple lines as one line). </p>
<p> A simple way to understand this protocol and to write scripts and programs that use it is to take a look at the (not useful) example FvwmScript-ComExample and fvwm-script-ComExample.pl (that can found in the fvwm data directory). Moreover, this implementation of the protocol solves questions as: What to do if the script exits for a bad reason? What to do if the program exits for a bad reason? &#8230;etc. </p>
<h2>Bugs</h2>
<p>FvwmScript crashes if widgets are accessed that have not been defined. </p>
<h2>Author</h2>
<p>&nbsp;<wbr>Frederic Cordier&nbsp;<wbr>(cordie97 [at] cui.unige.ch or f-cord96 [at] univ-lyon1.fr). </p>
<h2>Contributor</h2>
<p>&nbsp;<wbr>Eddy J. Gurney&nbsp;<wbr>(eddy [at] gizmo.aa.ans.net).</p>
