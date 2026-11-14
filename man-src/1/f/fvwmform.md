---
title: "fvwmform(1)"
name: "fvwmform"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fvwmform/"
description: "FvwmForm – input form module for Fvwm"
---

<p>FvwmForm &#8211; input form module for Fvwm</p>
<h2>Synopsis</h2>
<p><code>Module FvwmForm</code> [ <i>Alias</i> ] </p>
<p> FvwmForm must be spawned by Fvwm. If invoked from the command line, FvwmForm prints its version number and exits.</p>
<h2>Description</h2>
<p>FvwmForm provides a mechanism to get user input and act accordingly. This is achieved by means of a form that the user can fill out, and from which the user can select actions he wants Fvwm to take. A form consists of five types of items: text labels, single-line text inputs, mutually-exclusive selections, multiple-choice selections, and action buttons. These items are arranged into several lines, with a very flexible layout. </p>
<p> A text label only serves the purpose of explanation. It cannot accept any input. </p>
<p> A timeout entry provides a mechanism for timing out the form and performing a certain action when the timeout occurs. The countdown is displayed similar to a text label except that it updates with the amount of time left. </p>
<p> A text input field can be used to edit a single-line string. FvwmForm accepts Emacs-style cursor movement keys. See FvwmFormInput for details. Mouse copy is not supported, but you can paste. </p>
<p> A selection consists of several choices. </p>
<p> The selection itself is a logical entity that doesn&#8217;t have any display feature. </p>
<p> Each choice is displayed as a push-button followed by a explanatory text label. When selected, an exclusive choice shows a circle in the middle, while a multiple choice shows a check. </p>
<p> An action button, when activated sends one or more commands to Fvwm or executes shell commands. The shell commands can contain the content of the input fields on the form and reflect the setting of choices on the form. </p>
<p> The action buttons can be activated thru keyboard or mouse.</p>
<h2>Initialization</h2>
<p>FvwmForm invoked without an alias uses configuration commands starting with &quot;*FvwmForm&quot;. </p>
<p> Normally you would invoke FvwmForm with an alias representing the name of a form, its configuration commands and configuration file. For example, the command &quot;Module FvwmForm Rlogin&quot; uses configuration commands starting with &quot;*Rlogin&quot;, and reads the optional configuration file &quot;Rlogin&quot;. </p>
<p> All forms, regardless of alias, scan first for configuration commands that start with &quot;*FvwmFormDefault&quot;. These commands normally come from the builtin form &quot;FvwmForm-Form&quot; which saves commands to the file &quot;.FvwmForm&quot;. </p>
<p> The physical reading of the optional input file, &quot;.FvwmForm&quot;, is done only the first time FvwmForm is invoked, or after &quot;FvwmForm-Form&quot; updates the file. </p>
<p> When the file &quot;.FvwmForm&quot; is read, it is done by sending the command &quot;Read .FvwmForm Quiet&quot; to fvwm. Because of the way the &quot;read&quot; command works, the file can reside in your personal fvwm user directory, or be in the fvwm data directory. See the description of the read command in the fvwm man page for more information about the environment variable $FVWM_USERDIR. </p>
<p> Then FvwmForm reads the rest of the configuration fvwm has stored up. Fvwm stores configuration on an ongoing basis. The initial configuration comes from the .fvwm2rc file. Other sources, including &quot;Read&quot; commands can define a form. </p>
<p> When letting FvwmForm and fvwm read files, remember that these files contain commands that can execute shell commands, so you should be careful about setting permissions on these files. </p>
<p> When FvwmForm is invoked with a window context, e.g. from a window menu, all commands it sends to Fvwm will have that window context. This would allow FvwmForm to control the window it is invoked from. </p>
<p> After all the configuration commands have been read, FvwmForm displays the form defined by the commands. </p>
<h2>Defaults</h2>
<p>FvwmForm creates a built-in form named &quot;FvwmForm-Form&quot; that creates a file called &quot;.FvwmForm&quot;. This file contains saved default form colors and fonts. Other forms use these defaults unless they are overridden within the form. </p>
<p> The default creating form would normally be invoked from a &quot;module menu&quot;. For example, if you call your module menu &quot;Module-Popup&quot;, you would add the line: </p>
<pre>AddToMenu &quot;Module-Popup&quot; &quot;FvwmForm Defaults&quot; FvwmForm FvwmForm-Form</pre>
<p>When you select &quot;FvwmForm Defaults&quot; from your module menu, a form is displayed that shows the current defaults and allows you to change them. If you activate the &quot;Save Restart Me&quot; button, the &quot;.FvwmForm&quot; file is written and &quot;FvwmForm-Form&quot; exits and restarts to show the new defaults. </p>
<p> An example of what this file might contain after a save is: </p>
<pre> # This file last created by FvwmForm-Form on Sun Nov 28 11:18:26 EST 1999.
 *FvwmFormDefault: Font 10x20
 *FvwmFormDefault: InputFont 8x13bold
 *FvwmFormDefault: ButtonFont 10x20
 *FvwmFormDefault: TimeoutFont 10x20
 *FvwmFormDefault: Fore white
 *FvwmFormDefault: Back cornflowerblue
 *FvwmFormDefault: Colorset -1
 *FvwmFormDefault: ItemFore green
 *FvwmFormDefault: ItemBack gray40
 *FvwmFormDefault: ItemColorset -1
 *FvwmFormDefault: ButtonPointer hand2
 *FvwmFormDefault: ButtonInPointer star
 *FvwmFormDefault: InputPointer gumby
 *FvwmFormDefault: ButtonPointerFore blue
 *FvwmFormDefault: ButtonPointerBack gray
 *FvwmFormDefault: ButtonInPointerFore gray
 *FvwmFormDefault: ButtonInPointerBack blue
 *FvwmFormDefault: InputPointerFore
 *FvwmFormDefault: InputPointerBack</pre>
<p>The commands in this file are just like any other FvwmForm command except that they start with &quot;*FvwmFormDefault&quot;. </p>
<p> FvwmForm only reads the file &quot;.FvwmForm&quot; the first time it is started or after the file is changed by &quot;FvwmForm-Form&quot;. It does so by sending the command &quot;*FvwmFormDefault: Read x&quot;. With &quot;x&quot; set to &quot;y&quot; or &quot;n&quot;. &quot;n&quot; makes FvwmForm send a &quot;read .FvwmForm quiet&quot; command to fvwm. </p>
<h2>Variable Substitution</h2>
<p>If you supply variables and values on the command line used to start FvwmForm (like this): </p>
<pre>Module FvwmForm MyForm ACTION=Browse &quot;TITLE=Browse Form&quot;</pre>
<p>Then all FvwmForm input commands undergo variable substitution. The variables from the command line are exported. Then every command gets expanded using the variables from the environment. For example, assuming the above invocation of &quot;MyForm&quot;, commands would be changed like this: </p>
<pre>Before *MyForm: Text &quot;$TITLE, Home $HOME, Going to $ACTION&quot;
After *MyForm: TEXT &quot;Browse Form, Home /home/me, Going to Browse&quot;</pre>
<p>Using this facility should make it possible for one form to be used for different sets of input data. </p>
<h2>Configuration</h2>
<p>The following commands can be set in the .fvwm2rc file or thru any of the other ways that fvwm can accept commands. The simplest technique is to create a file in the read-only architecture-independent data directory, [PREFIX/share/fvwm] or your personal fvwm directory [$HOME/.fvwm], that matches the form alias. </p>
<p> In the following paragraphs the string &quot;FvwmForm&quot; would normally be the form alias. </p>
<p> FvwmForm reads commands before the form is ever displayed, and while the form is being displayed. </p>
<p> The following commands are accepted before the form is displayed: </p>
<pre>Back
Button
ButtonFont
ButtonInPointer
ButtonInPointerFore
ButtonInPointerBack
ButtonPointer
ButtonPointerFore
ButtonPointerBack
Choice
Command
Colorset
Font
Fore
GrabServer
Input
InputFont
InputPointer
ItemBack
ItemColorset
ItemFore
InputPointerFore
InputPointerBack
Line
Message
PadVText
Position
Selection
Separator
Text
Timeout
TimeoutFont
Title
UseData
WarpPointer</pre>
<p>The following commands are accepted while the form is displayed: </p>
<pre>Map
Stop
UnMap</pre>
<p>The &quot;Map&quot;, &quot;UnMap&quot; and &quot;Stop&quot; facility is under development and is currently not explained in this document, since it is likely to change. </p>
<p> The order of the options DOES matter. The first background text color, &quot;*FvwmFormBack&quot;, encountered before a displayable item sets the default background color for the entire form. </p>
<p> Other than that, colors, fonts, text, choices and buttons can be intermixed in any order. The are no builtin limits on form size, number of items on a form, or number of fonts or colors used. </p>
<dl>
<dt><code>*FvwmForm: GrabServer</code></p>
<dd>This option makes FvwmForm grab the mouse pointer on startup. This feature is useful for things like logout verification.</p>
<dt><code>*FvwmForm: WarpPointer</code></p>
<dd>This option makes FvwmForm warp the mouse pointer into its window on startup. It saves the user some mouse-travelling.</p>
<dt><code>*FvwmForm: Geometry </code><i>geometry</i></p>
<dd>Specifies the FvwmForm window location. This is similar to what the Position option does but is more flexible.</p>
<dt><code>*FvwmForm: Position </code><i>x</i> <i>y</i></p>
<dd>Puts the FvwmForm window at location (<i>x</i>, <i>y</i>) on the screen. By convention, a negative <i>x</i> (<i>y</i>) value measures distance from the right (bottom) of the screen. </p>
<p> If this option is omitted, FvwmForm starts at the center of the screen.</p>
<dt><code>*FvwmForm: Colorset </code><i>n</i></p>
<dd>Tells the module to use colorset <i>n</i>. See FvwmTheme.</p>
<dt><code>*FvwmForm: Back </code><i>color</i></p>
<dd>Specifies the background color of the FvwmForm window and any text in the window. The first background color FvwmForm reads determines the overall screen background color. Switches off the Colorset option. See DEFAULTS.</p>
<dt><code>*FvwmForm: Fore </code><i>color</i></p>
<dd>Specifies the foreground color for displaying text labels. Switches off the Colorset option. See DEFAULTS.</p>
<dt><code>*FvwmForm: ItemColorset </code><i>n</i></p>
<dd>Tells the module to use colorset <i>n</i> for items. See FvwmTheme.</p>
<dt><code>*FvwmForm: ItemBack </code><i>color</i></p>
<dd>Specifies the background color for the text input windows, and the buttons. Buttons are displayed as 3D depressable buttons. Inputs are displayed as 3D indented fields. Medium shade background colors work best. Switches off the ItemColorset option. See DEFAULTS.</p>
<dt><code>*FvwmForm: ItemFore </code><i>color</i></p>
<dd>Specifies the foreground color for the text input strings and button text. Switches off the ItemColorset option. See DEFAULTS.</p>
<dt><code>*FvwmForm: Font </code><i>font</i></p>
<dd>Specifies the font for displaying plain text. See DEFAULTS.</p>
<dt><code>*FvwmForm: ButtonFont </code><i>font</i></p>
<dd>Specifies the font for text in the action buttons. See DEFAULTS.</p>
<dt><code>*FvwmForm: InputFont </code><i>font</i></p>
<dd>Specifies the font for text input. See DEFAULTS.</p>
<dt><code>*FvwmForm: TimeoutFont </code><i>font</i></p>
<dd>Specifies the font for display the timeout counter and related text. See DEFAULTS.</p>
<dt><code>*FvwmForm: Line </code><i>justification</i></p>
<dd>Starts a new line. A line can contain any number of text, input, buttons and choice items. A FvwmForm window can have any number of lines. The width of the window is that of the longest line. </p>
<p> Justification of items in the line is specified by <i>justification</i>, which can be one of the following:</p>
<dt><i>left</i></p>
<dd>Items are justified to the left of the window.</p>
<dt><i>right</i></p>
<dd>Items are justified to the right of the window.</p>
<dt><i>center</i></p>
<dd>Items are placed in the center of the window.</p>
<dt><i>expand</i></p>
<dd>If there is only one item in the line, the item is centered in the window. If two or more items are present, they are spread to fill the whole width of the window.</p>
<dt><code>*FvwmForm: Message</code></p>
<dd>Defines a text area on the form that contains the last error message from fvwm. For purposes of determining form size, the message area is considered to be 80 bytes long. Its actual length is the same as the message received. If the message exceeds 80 bytes, you can see the rest of the message by resizing the form. </p>
<p> You should not attempt to put any text, buttons or input fields on the same line after a message field. Messages greater than 80 bytes will overlay the remainder of the line.</p>
<dt><code>*FvwmForm: PadVText </code><i>Pixels</i></p>
<dd>The number of pixels used as vertical padding between text items, line to line. The default is 6 which looks good on lines containing text intermixed with input boxes, choices or buttons. </p>
<p> For straight text, such as might appear on a help form, padding of zero looks better. </p>
<p> (There are lots of other padding values used in form layout which can&#8217;t currently be changed with commands.)</p>
<dt><code>*FvwmForm: Text </code><i>string</i></p>
<dd>Displays <i>string</i> as plain text. Line breaks must be achieved by multiple *FvwmForm: Line and *FvwmForm: Text options. Blanks may be used to provide extra padding between items.</p>
<dt><code>*FvwmForm: Title </code><i>string</i></p>
<dd>Displays <i>string</i> as the window&#8217;s title. The string must be enclosed in double quotes. Using this command with anything other than a string enclosed in quotes creates a blank title. If this command is not used, the window title is the form alias.</p>
<dt><code>*FvwmForm: Input </code><i>name</i> <i>size</i> <i>init_string</i></p>
<dd>Specifies a text input item with name <i>name</i>. A sub window of <i>size</i> characters in width is used for editing. If <i>init_string</i> is present, it is the initial string when FvwmForm starts or resets itself. The default initial string is &quot;&quot;. </p>
<p> You can mouse paste into an input field using button 2. Buttons 1 and 3 move the cursor in an input field. </p>
<p> Input fields are always in insert mode, overtyping is not supported. </p>
<p> Emacs type keystrokes are supported. </p>
<p> Control-a, Home and Begin move to the front of an input field. Control-e and End move to the end of an input field. Control-b and Left move left in an input field. Control-f and Right move right in an input field. Control-p, Up, and Shift-Tab move to a previous input field if any, if the form has one input field, recall previous value. Control-n, Down, Return, Line-feed and Tab move to the next input field if any, if the form has one input field, for control-n and Down, restore previous input value. Control-h moves backward in an input field erasing a character. Control-d and Delete delete the next character in an input field. Control-k erases for the cursor to the end of an input field. Control-u erases the entire input field. </p>
<p> When a form executes a command, all the input values are saved in a ring of input history 50 items deep. </p>
<p> Meta(mod2)-&quot;&lt;&quot; retrieves the previous value of an input field. Meta(mod2)-&quot;&gt;&quot; retrieves the next value of an input field. </p>
<p> (For forms with one input field, use the much easier arrow keys.) </p>
<dt><code>*FvwmForm: Selection </code><i>name</i> <i>type</i></p>
<dd>This option starts a selection item with name <i>name</i>. Its choices are specified in following configuration commands. The option <i>type</i> is one of the following:</p>
<dt><i>single</i></p>
<dd>The selections are mutually exclusive.</p>
<dt><i>multiple</i></p>
<dd>This is a multiple-choice selection. </p>
<dt><code>*FvwmForm: Separator</code></p>
<dd>Draws a 2 pixel shaded line across the form as a visual indication of a separate area. </p>
<dt><code>*FvwmForm: Choice </code><i>name</i> <i>value</i> on | off <i>string</i></p>
<dd>Specifies a choice for a proceeding selection. The choice item has a <i>name</i> and a <i>value</i> these are used in commands. See *FvwmForm: Command. The <i>string</i> is displayed to the right of the choice button as a label. </p>
<p> The choice assumes the specified initial state (&quot;on&quot; means selected) when FvwmForm starts or resets. If the selections are mutually exclusive, FvwmForm does NOT detect inconsistencies in the initial states of the choices, i.e. two or none of the choices can be selected. However, once the user selects a choice, FvwmForm assures only one is selected.</p>
<dt><code>*FvwmForm: Button </code><i>type</i> <i>string</i> [<i>key</i>]</p>
<dd>This option specifies an action button. The button has <i>string</i> as a label, and executes a set of Fvwm <i>command</i> when it is activated. The commands are the following *FvwmForm: Commands. </p>
<p> The optional <i>key</i> specifies a keyboard shortcut that activates the button. It is in either a control character, specified as ^@, ^A, &#8230;, ^_, or a function key, specified as F1, F2, &#8230;, F35. Control keys that are used for cursor movement in text input fields cannot activate any buttons, with the exception of TAB (^I), RETURN (^M), LINEFEED (^J), which can activate a button when the cursor is in the last text input field. </p>
<p> The behavior of the button is determined by <i>type</i>:</p>
<dt>continue</p>
<dd>FvwmForm continues execution after sending the commands.</p>
<dt>restart</p>
<dd>After sending the commands, FvwmForm resets all the values to the initial ones, and then continues execution.</p>
<dt>quit</p>
<dd>FvwmForm quits after sending the commands.</p>
<dt><code>*FvwmForm: Command </code><i>command</i></p>
<dd>This option specifies an Fvwm command associated with the current button. There can be more than one command attached to a button. Commands that appear before any *FvwmForm: Button option are executed at start-up time. This is usually a beep that gets the user&#8217;s attention. </p>
<p> Commands starting with an exclamation mark (!) are executed by FvwmForm, all other commands are sent to Fvwm for execution. Before sending each command to Fvwm, FvwmForm recognizes variables of the following forms, and supply values to them.</p>
<dt><code>$(</code><i>name</i>)</p>
<dd>If <i>name</i> corresponds to a text input field, the result is the user&#8217;s input string. The special chars single-quote, double-quote and backslash are preceded by a backslash. </p>
<p> If <i>name</i> corresponds to a choice, the result is the value of the choice (as specified in *FvwmForm: Choice) if the choice is selected. If the choice is not selected, the result is a blank string. </p>
<p> If <i>name</i> corresponds to a selection, the result will be a list of the selected values of all its choices separated by spaces.</p>
<dt><code>$(</code><i>name</i>?<i>string</i>)</p>
<dd>If <i>name</i> is a text input field and its value is not an empty string, the result is <i>string</i>, with recursive variable substitution applied. If the input value is empty, the result is empty. </p>
<p> If <i>name</i> is a choice and it is selected, the result is <i>string</i>, with recursive variable substitution applied. If the choice is not selected, the result is empty.</p>
<dt><code>$(</code><i>name</i>!<i>string</i>)</p>
<dd>The same as the above, except that the converse conditions are taken. </p>
<p> When using the &quot;?&quot; and &quot;!&quot; forms to pass a string, the string is delimited by a right parenthesis. If you need to put a right parenthesis in a string, precede the right parenthesis with a backslash. </p>
<dt><code>*FvwmForm: UseData </code><i>datafile</i> <i>leading</i></p>
<dd>Tells FvwmForm to read a data file and extract data from module commands that match the &quot;leading&quot; argument and an input, choice, or selection variable in a form. </p>
<p> This lets a form display current fvwm module configuration data. For an example of how this works, examine the file &quot;FvwmForm-Rlogin&quot; which is installed in read-only architecture-independent data directory, [PREFIX/share/fvwm] and shown below. </p>
<p> For choices, the setting of the button is represented as the word &quot;on&quot;, all other values for a setting are treated as off. </p>
<p> For selections, the setting of each choice button is determined by matching the current value of the selection against each choice. Currently, this only works correctly for selections that allow a single choice.</p>
<dt><code>*FvwmForm: ButtonPointer </code><i>pointername</i></p>
<dd>Change the default mouse pointer (hand2) used when hovering over a button. The pointername must be one of the names defined in the include file X11/cursorfont.h (without the XC_ prefix). See DEFAULTS. </p>
<dt><code>*FvwmForm: ButtonInPointer </code><i>pointername</i></p>
<dd>Change the default mouse pointer (hand1) used while a button is pressed in. The pointername must be one of the names defined in the include file X11/cursorfont.h (without the XC_ prefix). See DEFAULTS. </p>
<dt><code>*FvwmForm: InputPointer </code><i>pointername</i></p>
<dd>Change the default mouse pointer (xterm) used while the pointer is over a text field. The pointername must be one of the names defined in the include file X11/cursorfont.h (without the XC_ prefix). See DEFAULTS. </p>
<dt><code>*FvwmForm: ButtonPointerFore|Back </code><i>color</i></p>
<dd>Change the default mouse pointer foreground and background colors used when hovering over a button. See DEFAULTS. </p>
<dt><code>*FvwmForm: ButtonInPointerFore|Back </code><i>color</i></p>
<dd>Change the default mouse pointer foreground and background colors used while a button is pressed in. See DEFAULTS. </p>
<dt><code>*FvwmForm: InputPointerFore|Back </code><i>color</i></p>
<dd>Change the default mouse pointer foreground and background colors used while the pointer is over a text field. See DEFAULTS. </p>
<dt><code>*FvwmForm: Timeout </code><i>seconds</i> <i>command</i> <i>text</i></p>
<dd>Set up FvwmForm to time out after the amount of <i>seconds</i> specified. When the timer hits zero, <i>command</i> executes. The <i>text</i> field is displayed much like a <i>Text</i> field, except that a &#8216;%%&#8217; in the line is replaced automatically by the amount of time left on the timer. The value gets updated every second as the timer counts down. There can only be one timeout field per form. </p>
</dl>
<h2>Examples</h2>
<p>All of the following &quot;examples&quot; are installed in the read-only architecture-independent data directory, [PREFIX/share/fvwm], during fvwm installation. </p>
<p> The following commands create a menu to invoke the examples: </p>
<pre>DestroyMenu Forms
AddToMenu Forms &quot;&amp;Q. QuitVerify&quot; Module FvwmForm FvwmForm-QuitVerify
AddToMenu Forms &quot;&amp;C. Capture&quot; Module FvwmForm FvwmForm-Capture
AddToMenu Forms &quot;&amp;R. Rlogin&quot; Module FvwmForm FvwmForm-Rlogin
AddToMenu Forms &quot;&amp;T. Talk&quot; Module FvwmForm FvwmForm-Talk</pre>
<h2>EXAMPLE 1 &#8211; Quit Verify</h2>
<p>This example simulates the mwm way of confirming logout. Return does the logout, Escape cancels logout. It times out after 20 seconds and performs the equivalent of the &#8216;Logout&#8217; button. </p>
<pre>DestroyModuleConfig FvwmForm-QuitVerify: *
*FvwmForm-QuitVerify: GrabServer
*FvwmForm-QuitVerify: WarpPointer
*FvwmForm-QuitVerify: Command Beep
*FvwmForm-QuitVerify: Line center
*FvwmForm-QuitVerify: Text &quot;Do you really want to logout?&quot;
*FvwmForm-QuitVerify: Line expand
*FvwmForm-QuitVerify: Button quit &quot;Logout&quot; ^M
*FvwmForm-QuitVerify: Command Quit
*FvwmForm-QuitVerify: Button restart &quot;Restart&quot; ^R
*FvwmForm-QuitVerify: Command Restart
*FvwmForm-QuitVerify: Button quit &quot;Cancel&quot; ^[
*FvwmForm-QuitVerify: Command Nop
*FvwmForm-QuitVerify: Timeout 20 Quit &quot;Automatic logout will occur in %% seconds.&quot;</pre>
<h2>EXAMPLE 2 &#8211; Remote Login</h2>
<p>This example lets the user type in a host name, an optional user name, and opens an xterm window from the remote host. </p>
<pre>DestroyModuleConfig FvwmForm-Rlogin: *
*FvwmForm-Rlogin: WarpPointer
*FvwmForm-Rlogin: Line center
*FvwmForm-Rlogin: Text &quot;Login to Remote Host&quot;
*FvwmForm-Rlogin: Line center
*FvwmForm-Rlogin: Text &quot;Host:&quot;
*FvwmForm-Rlogin: Input HostName 20 &quot;&quot;
*FvwmForm-Rlogin: Line center
*FvwmForm-Rlogin: Selection UserSel single
*FvwmForm-Rlogin: Choice Default Default on &quot;same user&quot;
*FvwmForm-Rlogin: Choice Custom Custom off &quot;user:&quot;
*FvwmForm-Rlogin: Input UserName 10 &quot;&quot;
*FvwmForm-Rlogin: Line expand
*FvwmForm-Rlogin: Button quit &quot;Login&quot; ^M
*FvwmForm-Rlogin: Command Exec exec ssh $(Custom?-l $(UserName)) $(HostName) xterm -T xterm@$(HostName) -display $HOSTDISPLAY &amp;
# Before saving the data, remove any previously saved data:
*FvwmForm-Rlogin: Command DestroyModuleConfig FvwmForm-RloginDefault: *
# The &quot;Login&quot; button causes a login and a saving of the current data:
*FvwmForm-Rlogin: Command !( /bin/echo \
 &quot;# Created by FvwmForm-Rlogin on: `/bin/date`.&quot;; /bin/echo \
 '*FvwmForm-RloginDefault: HostName $(HostName)'; /bin/echo \
 '*FvwmForm-RloginDefault: UserName $(UserName)'; /bin/echo \
 '*FvwmForm-RloginDefault: Default $(Default?on)'; /bin/echo \
 '*FvwmForm-RloginDefault: Custom $(Custom?on)' \
) &gt; ${FVWM_USERDIR}/.FvwmForm-Rlogin
*FvwmForm-Rlogin: Button restart &quot;Reset&quot;
*FvwmForm-Rlogin: Button quit &quot;Cancel&quot; ^[
*FvwmForm-Rlogin: Command Nop
# Tell FvwmForm to read vars from the .FvwmForm-RloginDefault file:
*FvwmForm-Rlogin: UseData .FvwmForm-Rlogin *FvwmForm-RloginDefault</pre>
<h2>EXAMPLE 3 &#8211; Capture Window</h2>
<p>This example provides a front-end to xwd, xwud, and xpr. </p>
<pre>DestroyModuleConfig FvwmForm-Capture: *
*FvwmForm-Capture: Line center
*FvwmForm-Capture: Text &quot;Capture Window&quot;
*FvwmForm-Capture: Line left
*FvwmForm-Capture: Text &quot;File: &quot;
*FvwmForm-Capture: Input file 25 &quot;/tmp/Capture&quot;
*FvwmForm-Capture: Line left
*FvwmForm-Capture: Text &quot;Printer: &quot;
*FvwmForm-Capture: Input printer 20 &quot;$PRINTER&quot;
*FvwmForm-Capture: Line expand
*FvwmForm-Capture: Selection PtrType single
*FvwmForm-Capture: Choice PS ps on &quot;PostScript&quot;
*FvwmForm-Capture: Choice Ljet ljet off &quot;HP LaserJet&quot;
*FvwmForm-Capture: Line left
*FvwmForm-Capture: Text &quot;xwd options:&quot;
*FvwmForm-Capture: Line expand
*FvwmForm-Capture: Selection Options multiple
*FvwmForm-Capture: Choice Brd -nobdrs off &quot;No border&quot;
*FvwmForm-Capture: Choice Frm -frame on &quot;With frame&quot;
*FvwmForm-Capture: Choice XYZ -xy off &quot;XY format&quot;
*FvwmForm-Capture: Line expand
*FvwmForm-Capture: Button continue &quot;Capture&quot; ^M
*FvwmForm-Capture: Command Exec exec xwd -out $(file) $(Options) &amp;
*FvwmForm-Capture: Button continue &quot;Preview&quot;
*FvwmForm-Capture: Command Exec exec xwud -in $(file) &amp;
*FvwmForm-Capture: Button continue &quot;Print&quot;
*FvwmForm-Capture: Command Exec exec xpr -device $(PtrType) $(file) | lpr -P $(printer) &amp;
*FvwmForm-Capture: Button quit &quot;Quit&quot;</pre>
<h2>EXAMPLE 4 &#8211; Talk Form</h2>
<p>This example provides a replacement for the module FvwmTalk. There are 2 forms, &quot;FvwmForm-Talk.&quot; which executes commands, or sends commands to fvwm for execution, and &quot;FvwmForm-TalkHelp.&quot; which is a help form. </p>
<p> In the help form, notice how vertical line spacing is changed. Normal FvwmForm line spacing assumes text is intermixed with buttons, help forms require different spacing. </p>
<pre># FvwmForm-Talk - Basic replacement for FvwmTalk
DestroyModuleConfig FvwmForm-Talk: *
*FvwmForm-Talk: WarpPointer
# Layout
*FvwmForm-Talk: Line center
*FvwmForm-Talk: Text &quot;Talk to Fvwm&quot;
*FvwmForm-Talk: Line left
*FvwmForm-Talk: Text &quot;Command:&quot;
*FvwmForm-Talk: Input Command 80 &quot;&quot;
*FvwmForm-Talk: Line left
*FvwmForm-Talk: Text &quot;Msg:&quot;
*FvwmForm-Talk: Message
*FvwmForm-Talk: Line center
# Buttons
*FvwmForm-Talk: Button restart &quot;Return - Execute&quot; ^M
*FvwmForm-Talk: Command $(Command)
*FvwmForm-Talk: Button continue &quot;F1 - Help&quot; F1
*FvwmForm-Talk: Command Module FvwmForm FvwmForm-TalkHelp
*FvwmForm-Talk: Button restart &quot;F3 - Reset input&quot; F3
*FvwmForm-Talk: Command Nop
*FvwmForm-Talk: Button quit &quot;F4 - Dismiss&quot; F4
*FvwmForm-Talk: Command Nop</pre>
<pre># FvwmForm-TalkHelp - Help Text for FvwmForm-Talk
DestroyModuleConfig FvwmForm-TalkHelp: *
*FvwmForm-TalkHelp: WarpPointer
# Layout
*FvwmForm-TalkHelp: Line center
*FvwmForm-TalkHelp: Text &quot;Talk to Fvwm - Help&quot;
*FvwmForm-TalkHelp: Line left
*FvwmForm-TalkHelp: Text &quot; &quot;
*FvwmForm-TalkHelp: Line left
*FvwmForm-TalkHelp: PadVText 0
*FvwmForm-TalkHelp: Text &quot;Enter commands in the *FvwmForm-TalkHelp: Line left
*FvwmForm-TalkHelp: Text &quot;Commands beginning with *FvwmForm-TalkHelp: Line left
*FvwmForm-TalkHelp: Text &quot;shell as a sub-process of the form.&quot;
*FvwmForm-TalkHelp: Line left
*FvwmForm-TalkHelp: Text &quot;All other commands are sent to fvwm for execution.&quot;
*FvwmForm-TalkHelp: Line left
*FvwmForm-TalkHelp: Text &quot;&quot;
*FvwmForm-TalkHelp: Line left
*FvwmForm-TalkHelp: Text &quot;Fvwm error messages are shown on the *FvwmForm-TalkHelp: Line left
*FvwmForm-TalkHelp: Text &quot;&quot;
# Buttons
*FvwmForm-TalkHelp: Line center
*FvwmForm-TalkHelp: Button quit &quot;Return - Dismiss&quot; ^M
*FvwmForm-TalkHelp: Command Nop</pre>
<h2>Bugs And Limitations</h2>
<p>FvwmForm is a fairly simple method of providing input. There is no input validation facility. FvwmForm has no way of dealing with lists. </p>
<p> Report bugs to the fvwm-workers list. </p>
<h2>Copyrights</h2>
<p>FvwmForm is original work of Thomas Zuwei Feng (ztfeng [at] math.princeton.edu). </p>
<p> Copyright Feb 1995, Thomas Zuwei Feng. No guarantees or warranties are provided or implied in any way whatsoever. Use this program at your own risk. Permission to use, modify, and redistribute this program is hereby given, provided that this copyright is kept intact. </p>
<h2>Changes</h2>
<p>During the fall of 1998, Dan Espen removed all form size limits, added unlimited font and color changing, form spacing control, configuration file reading, global control of appearance, synchronous command execution, Error message display, variable substitution, configurable pointers, and lots of other damage. No additional copyright is imposed.</p>
