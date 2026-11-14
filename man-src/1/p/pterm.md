---
title: "pterm(1)"
name: "pterm"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pterm/"
description: "pterm – yet another X terminal emulator"
---

<h2>NAME</h2>
<p> pterm &#8211; yet another X terminal emulator</p>
<h2>SYNOPSIS</h2>
<pre><code>
pterm &amp;nbsp;
[&amp;nbsp; options &amp; nbsp;]
</code></pre>
<h2>DESCRIPTION</h2>
<p> <code>pterm</code> is a terminal emulator for X. It is based on a port of the terminal emulation engine in the Windows SSH client PuTTY.</p>
<h2>OPTIONS</h2>
<p> The command-line options supported by <code>pterm</code> are:</p>
<dl>
<dt><code>-e</code> <i>command</i> [ <i>arguments</i> ]</p>
<dd> Specify a command to be executed in the new terminal. Everything on the command line after this option will be passed straight to the <code>execvp</code> system call; so if you need the command to redirect its input or output, you will have to use <code>sh</code>:</p>
<dl>
<dt>
<dd>
<pre>
pterm -e sh -c&nbsp;<wbr>'mycommand&nbsp;<wbr>&lt;&nbsp;<wbr>inputfile'
</pre>
</dl>
<dt><code>&#8211;display</code> <i>display-name</i></p>
<dd> Specify the X display on which to open <code>pterm</code>. (Note this option has a double minus sign, even though none of the others do. This is because this option is supplied automatically by GTK. Sorry.)</p>
<dt><code>-name</code> <i>name</i></p>
<dd> Specify the name under which <code>pterm</code> looks up X resources. Normally it will look them up as (for example) <code>pterm.Font</code>. If you specify `<code>-name xyz</code>&#8216;, it will look them up as <code>xyz.Font</code> instead. This allows you to set up several different sets of defaults and choose between them.</p>
<dt><code>-fn</code> <i>font-name</i></p>
<dd> Specify the font to use for normal text displayed in the terminal.</p>
<dt><code>-fb</code> <i>font-name</i></p>
<dd> Specify the font to use for bold text displayed in the terminal. If the <code>BoldAsColour</code> resource is set to 1 (the default), bold text will be displayed in different colours instead of a different font, so this option will be ignored. If <code>BoldAsColour</code> is set to 0 or 2 and you do not specify a bold font, <code>pterm</code> will overprint the normal font to make it look bolder.</p>
<dt><code>-fw</code> <i>font-name</i></p>
<dd> Specify the font to use for double-width characters (typically Chinese, Japanese and Korean text) displayed in the terminal.</p>
<dt><code>-fwb</code> <i>font-name</i></p>
<dd> Specify the font to use for bold double-width characters (typically Chinese, Japanese and Korean text). Like <code>-fb</code>, this will be ignored unless the <code>BoldAsColour</code> resource is set to 0 or 2.</p>
<dt><code>-geometry</code> <i>geometry</i></p>
<dd> Specify the size of the terminal, in rows and columns of text. See <i><a href="/docs/linux/man/7-x/">X</a>(7)</i> for more information on the syntax of geometry specifications.</p>
<dt><code>-sl</code> <i>lines</i></p>
<dd> Specify the number of lines of scrollback to save off the top of the terminal.</p>
<dt><code>-fg</code> <i>colour</i></p>
<dd> Specify the foreground colour to use for normal text.</p>
<dt><code>-bg</code> <i>colour</i></p>
<dd> Specify the background colour to use for normal text.</p>
<dt><code>-bfg</code> <i>colour</i></p>
<dd> Specify the foreground colour to use for bold text, if the <code>BoldAsColour</code> resource is set to 1 (the default) or 2.</p>
<dt><code>-bbg</code> <i>colour</i></p>
<dd> Specify the foreground colour to use for bold reverse-video text, if the <code>BoldAsColour</code> resource is set to 1 (the default) or 2. (This colour is best thought of as the bold version of the background colour; so it only appears when text is displayed <i>in</i> the background colour.)</p>
<dt><code>-cfg</code> <i>colour</i></p>
<dd> Specify the foreground colour to use for text covered by the cursor.</p>
<dt><code>-cbg</code> <i>colour</i></p>
<dd> Specify the background colour to use for text covered by the cursor. In other words, this is the main colour of the cursor.</p>
<dt><code>-title</code> <i>title</i></p>
<dd> Specify the initial title of the terminal window. (This can be changed under control of the server.)</p>
<dt><code>-ut-</code> or <code>+ut</code></p>
<dd> Tells <code>pterm</code> not to record your login in the <code>utmp</code>, <code>wtmp</code> and <code>lastlog</code> system log files; so you will not show up on <code>finger</code> or <code>who</code> listings, for example.</p>
<dt><code>-ut</code></p>
<dd> Tells <code>pterm</code> to record your login in <code>utmp</code>, <code>wtmp</code> and <code>lastlog</code>: this is the opposite of <code>-ut-</code>. This is the default option: you will probably only need to specify it explicitly if you have changed the default using the <code>StampUtmp</code> resource.</p>
<dt><code>-ls-</code> or <code>+ls</code></p>
<dd> Tells <code>pterm</code> not to execute your shell as a login shell.</p>
<dt><code>-ls</code></p>
<dd> Tells <code>pterm</code> to execute your shell as a login shell: this is the opposite of <code>-ls-</code>. This is the default option: you will probably only need to specify it explicitly if you have changed the default using the <code>LoginShell</code> resource.</p>
<dt><code>-sb-</code> or <code>+sb</code></p>
<dd> Tells <code>pterm</code> not to display a scroll bar.</p>
<dt><code>-sb</code></p>
<dd> Tells <code>pterm</code> to display a scroll bar: this is the opposite of <code>-sb-</code>. This is the default option: you will probably only need to specify it explicitly if you have changed the default using the <code>ScrollBar</code> resource.</p>
<dt><code>-log</code> <i>filename</i></p>
<dd> This option makes <code>pterm</code> log all the terminal output to a file as well as displaying it in the terminal.</p>
<dt><code>-cs</code> <i>charset</i></p>
<dd> This option specifies the character set in which <code>pterm</code> should assume the session is operating. This character set will be used to interpret all the data received from the session, and all input you type or paste into <code>pterm</code> will be converted into this character set before being sent to the session.</p>
<dl>
<dt>
<dd>
<p> Any character set name which is valid in a MIME header (and supported by <code>pterm</code>) should be valid here (examples are `<code>ISO-8859-1</code>&#8216;, `<code>windows-1252</code>&#8216; or `<code>UTF-8</code>&#8216;). Also, any character encoding which is valid in an X logical font description should be valid (`<code>ibm-cp437</code>&#8216;, for example). </p>
<p> <code>pterm</code>&#8216;s default behaviour is to use the same character encoding as its primary font. If you supply a Unicode (<code>iso10646-1</code>) font, it will default to the UTF-8 character set. </p>
<p> Character set names are case-insensitive.</dl>
<dt><code>-nethack</code></p>
<dd> Tells <code>pterm</code> to enable NetHack keypad mode, in which the numeric keypad generates the NetHack <code>hjklyubn</code> direction keys. This enables you to play NetHack with the numeric keypad without having to use the NetHack <code>number_pad</code> option (which requires you to press `<code>n</code>&#8216; before any repeat count). So you can move with the numeric keypad, and enter repeat counts with the normal number keys.</p>
<dt><code>-xrm</code> <i>resource-string</i></p>
<dd> This option specifies an X resource string. Useful for setting resources which do not have their own command-line options. For example:</p>
<dl>
<dt>
<dd>
<pre>
pterm -xrm&nbsp;<wbr>'ScrollbarOnLeft: 1'
</pre>
</dl>
<dt><code>-help</code>, <code>&#8211;help</code></p>
<dd> Display a message summarizing the available options.</p>
<dt><code>-pgpfp</code></p>
<dd> Display the fingerprints of the PuTTY PGP Master Keys, to aid in verifying new files released by the PuTTY team.</dl>
<h2>X RESOURCES</h2>
<p> <code>pterm</code> can be more completely configured by means of X resources. All of these resources are of the form <code>pterm.FOO</code> for some <code>FOO</code>; you can make <code>pterm</code> look them up under another name, such as <code>xyz.FOO</code>, by specifying the command-line option `<code>-name xyz</code>&#8216;.</p>
<dl>
<dt><code>pterm.CloseOnExit</code></p>
<dd> This option should be set to 0, 1 or 2; the default is 2. It controls what <code>pterm</code> does when the process running inside it terminates. When set to 2 (the default), <code>pterm</code> will close its window as soon as the process inside it terminates. When set to 0, <code>pterm</code> will print the process&#8217;s exit status, and the window will remain present until a key is pressed (allowing you to inspect the scrollback, and copy and paste text out of it).</p>
<dl>
<dt>
<dd>
<p> When this setting is set to 1, <code>pterm</code> will close immediately if the process exits cleanly (with an exit status of zero), but the window will stay around if the process exits with a non-zero code or on a signal. This enables you to see what went wrong if the process suffers an error, but not to have to bother closing the window in normal circumstances.</dl>
<dt><code>pterm.WarnOnClose</code></p>
<dd> This option should be set to either 0 or 1; the default is 1. When set to 1, <code>pterm</code> will ask for confirmation before closing its window when you press the close button.</p>
<dt><code>pterm.TerminalType</code></p>
<dd> This controls the value set in the <code>TERM</code> environment variable inside the new terminal. The default is `<code>xterm</code>&#8216;.</p>
<dt><code>pterm.BackspaceIsDelete</code></p>
<dd> This option should be set to either 0 or 1; the default is 1. When set to 0, the ordinary Backspace key generates the Backspace character (<code>^H</code>); when set to 1, it generates the Delete character (<code>^?</code>). Whichever one you set, the terminal device inside <code>pterm</code> will be set up to expect it.</p>
<dt><code>pterm.RXVTHomeEnd</code></p>
<dd> This option should be set to either 0 or 1; the default is 0. When it is set to 1, the Home and End keys generate the control sequences they would generate in the <code>rxvt</code> terminal emulator, instead of the more usual ones generated by other emulators.</p>
<dt><code>pterm.LinuxFunctionKeys</code></p>
<dd> This option can be set to any number between 0 and 5 inclusive; the default is 0. The modes vary the control sequences sent by the function keys; for more complete documentation, it is probably simplest to try each option in `<code>pterm -e cat</code>&#8216;, and press the keys to see what they generate.</p>
<dt><code>pterm.NoApplicationKeys</code></p>
<dd> This option should be set to either 0 or 1; the default is 0. When set to 1, it stops the server from ever switching the numeric keypad into application mode (where the keys send function-key-like sequences instead of numbers or arrow keys). You probably only need this if some application is making a nuisance of itself.</p>
<dt><code>pterm.NoApplicationCursors</code></p>
<dd> This option should be set to either 0 or 1; the default is 0. When set to 1, it stops the server from ever switching the cursor keys into application mode (where the keys send slightly different sequences). You probably only need this if some application is making a nuisance of itself.</p>
<dt><code>pterm.NoMouseReporting</code></p>
<dd> This option should be set to either 0 or 1; the default is 0. When set to 1, it stops the server from ever enabling mouse reporting mode (where mouse clicks are sent to the application instead of controlling cut and paste).</p>
<dt><code>pterm.NoRemoteResize</code></p>
<dd> This option should be set to either 0 or 1; the default is 0. When set to 1, it stops the server from being able to remotely control the size of the <code>pterm</code> window.</p>
<dt><code>pterm.NoAltScreen</code></p>
<dd> This option should be set to either 0 or 1; the default is 0. When set to 1, it stops the server from using the `alternate screen&#8217; terminal feature, which lets full-screen applications leave the screen exactly the way they found it.</p>
<dt><code>pterm.NoRemoteWinTitle</code></p>
<dd> This option should be set to either 0 or 1; the default is 0. When set to 1, it stops the server from remotely controlling the title of the <code>pterm</code> window.</p>
<dt><code>pterm.NoRemoteQTitle</code></p>
<dd> This option should be set to either 0 or 1; the default is 1. When set to 1, it stops the server from remotely requesting the title of the <code>pterm</code> window.</p>
<dl>
<dt>
<dd>
<p> This feature is a <i>POTENTIAL SECURITY HAZARD</i>. If a malicious application can write data to your terminal (for example, if you merely <code>cat</code> a file owned by someone else on the server machine), it can change your window title (unless you have disabled this using the <code>NoRemoteWinTitle</code> resource) and then use this service to have the new window title sent back to the server as if typed at the keyboard. This allows an attacker to fake keypresses and potentially cause your server-side applications to do things you didn&#8217;t want. Therefore this feature is disabled by default, and we recommend you do not turn it on unless you <i>really</i> know what you are doing.</dl>
<dt><code>pterm.NoDBackspace</code></p>
<dd> This option should be set to either 0 or 1; the default is 0. When set to 1, it disables the normal action of the Delete (<code>^?</code>) character when sent from the server to the terminal, which is to move the cursor left by one space and erase the character now under it.</p>
<dt><code>pterm.ApplicationCursorKeys</code></p>
<dd> This option should be set to either 0 or 1; the default is 0. When set to 1, the default initial state of the cursor keys are application mode (where the keys send function-key-like sequences instead of numbers or arrow keys). When set to 0, the default state is the normal one.</p>
<dt><code>pterm.ApplicationKeypad</code></p>
<dd> This option should be set to either 0 or 1; the default is 0. When set to 1, the default initial state of the numeric keypad is application mode (where the keys send function-key-like sequences instead of numbers or arrow keys). When set to 0, the default state is the normal one.</p>
<dt><code>pterm.NetHackKeypad</code></p>
<dd> This option should be set to either 0 or 1; the default is 0. When set to 1, the numeric keypad operates in NetHack mode. This is equivalent to the <code>-nethack</code> command-line option.</p>
<dt><code>pterm.Answerback</code></p>
<dd> This option controls the string which the terminal sends in response to receiving the <code>^E</code> character (`tell me about yourself&#8217;). By default this string is `<code>PuTTY</code>&#8216;.</p>
<dt><code>pterm.HideMousePtr</code></p>
<dd> This option should be set to either 0 or 1; the default is 0. When it is set to 1, the mouse pointer will disappear if it is over the <code>pterm</code> window and you press a key. It will reappear as soon as you move it.</p>
<dt><code>pterm.WindowBorder</code></p>
<dd> This option controls the number of pixels of space between the text in the <code>pterm</code> window and the window frame. The default is 1. You can increase this value, but decreasing it to 0 is not recommended because it can cause the window manager&#8217;s size hints to work incorrectly.</p>
<dt><code>pterm.CurType</code></p>
<dd> This option should be set to either 0, 1 or 2; the default is 0. When set to 0, the text cursor displayed in the window is a rectangular block. When set to 1, the cursor is an underline; when set to 2, it is a vertical line.</p>
<dt><code>pterm.BlinkCur</code></p>
<dd> This option should be set to either 0 or 1; the default is 0. When it is set to 1, the text cursor will blink when the window is active.</p>
<dt><code>pterm.Beep</code></p>
<dd> This option should be set to either 0 or 2 (yes, 2); the default is 0. When it is set to 2, <code>pterm</code> will respond to a bell character (<code>^G</code>) by flashing the window instead of beeping.</p>
<dt><code>pterm.BellOverload</code></p>
<dd> This option should be set to either 0 or 1; the default is 0. When it is set to 1, <code>pterm</code> will watch out for large numbers of bells arriving in a short time and will temporarily disable the bell until they stop. The idea is that if you <code>cat</code> a binary file, the frantic beeping will mostly be silenced by this feature and will not drive you crazy.</p>
<dl>
<dt>
<dd>
<p> The bell overload mode is activated by receiving N bells in time T; after a further time S without any bells, overload mode will turn itself off again. </p>
<p> Bell overload mode is always deactivated by any keypress in the terminal. This means it can respond to large unexpected streams of data, but does not interfere with ordinary command-line activities that generate beeps (such as filename completion).</dl>
<dt><code>pterm.BellOverloadN</code></p>
<dd> This option counts the number of bell characters which will activate bell overload if they are received within a length of time T. The default is 5.</p>
<dt><code>pterm.BellOverloadT</code></p>
<dd> This option specifies the time period in which receiving N or more bells will activate bell overload mode. It is measured in microseconds, so (for example) set it to 1000000 for one second. The default is 2000000 (two seconds).</p>
<dt><code>pterm.BellOverloadS</code></p>
<dd> This option specifies the time period of silence required to turn off bell overload mode. It is measured in microseconds, so (for example) set it to 1000000 for one second. The default is 5000000 (five seconds of silence).</p>
<dt><code>pterm.ScrollbackLines</code></p>
<dd> This option specifies how many lines of scrollback to save above the visible terminal screen. The default is 200. This resource is equivalent to the <code>-sl</code> command-line option.</p>
<dt><code>pterm.DECOriginMode</code></p>
<dd> This option should be set to either 0 or 1; the default is 0. It specifies the default state of DEC Origin Mode. (If you don&#8217;t know what that means, you probably don&#8217;t need to mess with it.)</p>
<dt><code>pterm.AutoWrapMode</code></p>
<dd> This option should be set to either 0 or 1; the default is 1. It specifies the default state of auto wrap mode. When set to 1, very long lines will wrap over to the next line on the terminal; when set to 0, long lines will be squashed against the right-hand edge of the screen.</p>
<dt><code>pterm.LFImpliesCR</code></p>
<dd> This option should be set to either 0 or 1; the default is 0. When set to 1, the terminal will return the cursor to the left side of the screen when it receives a line feed character.</p>
<dt><code>pterm.WinTitle</code></p>
<dd> This resource is the same as the <code>-T</code> command-line option: it controls the initial title of the window. The default is `<code>pterm</code>&#8216;.</p>
<dt><code>pterm.TermWidth</code></p>
<dd> This resource is the same as the width part of the <code>-geometry</code> command-line option: it controls the number of columns of text in the window. The default is 80.</p>
<dt><code>pterm.TermHeight</code></p>
<dd> This resource is the same as the width part of the <code>-geometry</code> command-line option: it controls the number of columns of text in the window. The defaults is 24.</p>
<dt><code>pterm.Font</code></p>
<dd> This resource is the same as the <code>-fn</code> command-line option: it controls the font used to display normal text. The default is `<code>fixed</code>&#8216;.</p>
<dt><code>pterm.BoldFont</code></p>
<dd> This resource is the same as the <code>-fb</code> command-line option: it controls the font used to display bold text when <code>BoldAsColour</code> is set to 0 or 2. The default is unset (the font will be bolded by printing it twice at a one-pixel offset).</p>
<dt><code>pterm.WideFont</code></p>
<dd> This resource is the same as the <code>-fw</code> command-line option: it controls the font used to display double-width characters. The default is unset (double-width characters cannot be displayed).</p>
<dt><code>pterm.WideBoldFont</code></p>
<dd> This resource is the same as the <code>-fwb</code> command-line option: it controls the font used to display double-width characters in bold, when <code>BoldAsColour</code> is set to 0 or 2. The default is unset (double-width characters are displayed in bold by printing them twice at a one-pixel offset).</p>
<dt><code>pterm.ShadowBoldOffset</code></p>
<dd> This resource can be set to an integer; the default is -1. It specifies the offset at which text is overprinted when using `shadow bold&#8217; mode. The default (1) means that the text will be printed in the normal place, and also one character to the right; this seems to work well for most X bitmap fonts, which have a blank line of pixels down the right-hand side. For some fonts, you may need to set this to -1, so that the text is overprinted one pixel to the left; for really large fonts, you may want to set it higher than 1 (in one direction or the other).</p>
<dt><code>pterm.BoldAsColour</code></p>
<dd> This option should be set to either 0, 1, or 2; the default is 1. It specifies how bold text should be displayed. When set to 1, bold text is shown by displaying it in a brighter colour; when set to 0, bold text is shown by displaying it in a heavier font; when set to 2, both effects happen at once (a heavy font <i>and</i> a brighter colour).</p>
<dt><code>pterm.Colour0</code>, <code>pterm.Colour1</code>, &#8230;, <code>pterm.Colour21</code></p>
<dd> These options control the various colours used to display text in the <code>pterm</code> window. Each one should be specified as a triple of decimal numbers giving red, green and blue values: so that black is `<code>0,0,0</code>&#8216;, white is `<code>255,255,255</code>&#8216;, red is `<code>255,0,0</code>&#8216; and so on.</p>
<dl>
<dt>
<dd>
<p> Colours 0 and 1 specify the foreground colour and its bold equivalent (the <code>-fg</code> and <code>-bfg</code> command-line options). Colours 2 and 3 specify the background colour and its bold equivalent (the <code>-bg</code> and <code>-bbg</code> command-line options). Colours 4 and 5 specify the text and block colours used for the cursor (the <code>-cfg</code> and <code>-cbg</code> command-line options). Each even number from 6 to 20 inclusive specifies the colour to be used for one of the ANSI primary colour specifications (black, red, green, yellow, blue, magenta, cyan, white, in that order); the odd numbers from 7 to 21 inclusive specify the bold version of each colour, in the same order. The defaults are: </p>
<pre>
pterm.Colour0: 187,187,187
pterm.Colour1: 255,255,255
pterm.Colour2: 0,0,0
pterm.Colour3: 85,85,85
pterm.Colour4: 0,0,0
pterm.Colour5: 0,255,0
pterm.Colour6: 0,0,0
pterm.Colour7: 85,85,85
pterm.Colour8: 187,0,0
pterm.Colour9: 255,85,85
pterm.Colour10: 0,187,0
pterm.Colour11: 85,255,85
pterm.Colour12: 187,187,0
pterm.Colour13: 255,255,85
pterm.Colour14: 0,0,187
pterm.Colour15: 85,85,255
pterm.Colour16: 187,0,187
pterm.Colour17: 255,85,255
pterm.Colour18: 0,187,187
pterm.Colour19: 85,255,255
pterm.Colour20: 187,187,187
pterm.Colour21: 255,255,255
</pre>
</dl>
<dt><code>pterm.RectSelect</code></p>
<dd> This option should be set to either 0 or 1; the default is 0. When set to 0, dragging the mouse over several lines selects to the end of each line and from the beginning of the next; when set to 1, dragging the mouse over several lines selects a rectangular region. In each case, holding down Alt while dragging gives the other behaviour.</p>
<dt><code>pterm.MouseOverride</code></p>
<dd> This option should be set to either 0 or 1; the default is 1. When set to 1, if the application requests mouse tracking (so that mouse clicks are sent to it instead of doing selection), holding down Shift will revert the mouse to normal selection. When set to 0, mouse tracking completely disables selection.</p>
<dt><code>pterm.Printer</code></p>
<dd> This option is unset by default. If you set it, then server-controlled printing is enabled: the server can send control sequences to request data to be sent to a printer. That data will be piped into the command you specify here; so you might want to set it to `<code>lpr</code>&#8216;, for example, or `<code>lpr -Pmyprinter</code>&#8216;.</p>
<dt><code>pterm.ScrollBar</code></p>
<dd> This option should be set to either 0 or 1; the default is 1. When set to 0, the scrollbar is hidden (although Shift-PageUp and Shift-PageDown still work). This is the same as the <code>-sb</code> command-line option.</p>
<dt><code>pterm.ScrollbarOnLeft</code></p>
<dd> This option should be set to either 0 or 1; the default is 0. When set to 1, the scrollbar will be displayed on the left of the terminal instead of on the right.</p>
<dt><code>pterm.ScrollOnKey</code></p>
<dd> This option should be set to either 0 or 1; the default is 0. When set to 1, any keypress causes the position of the scrollback to be reset to the very bottom.</p>
<dt><code>pterm.ScrollOnDisp</code></p>
<dd> This option should be set to either 0 or 1; the default is 1. When set to 1, any activity in the display causes the position of the scrollback to be reset to the very bottom.</p>
<dt><code>pterm.LineCodePage</code></p>
<dd> This option specifies the character set to be used for the session. This is the same as the <code>-cs</code> command-line option.</p>
<dt><code>pterm.NoRemoteCharset</code></p>
<dd> This option disables the terminal&#8217;s ability to change its character set when it receives escape sequences telling it to. You might need to do this to interoperate with programs which incorrectly change the character set to something they think is sensible.</p>
<dt><code>pterm.BCE</code></p>
<dd> This option should be set to either 0 or 1; the default is 1. When set to 1, the various control sequences that erase parts of the terminal display will erase in whatever the current background colour is; when set to 0, they will erase in black always.</p>
<dt><code>pterm.BlinkText</code></p>
<dd> This option should be set to either 0 or 1; the default is 0. When set to 1, text specified as blinking by the server will actually blink on and off; when set to 0, <code>pterm</code> will use the less distracting approach of making the text&#8217;s background colour bold.</p>
<dt><code>pterm.StampUtmp</code></p>
<dd> This option should be set to either 0 or 1; the default is 1. When set to 1, <code>pterm</code> will log the login in the various system log files. This resource is equivalent to the <code>-ut</code> command-line option.</p>
<dt><code>pterm.LoginShell</code></p>
<dd> This option should be set to either 0 or 1; the default is 1. When set to 1, <code>pterm</code> will execute your shell as a login shell. This resource is equivalent to the <code>-ls</code> command-line option.</dl>
<h2>BUGS</h2>
<p> Most of the X resources have silly names. (Historical reasons from PuTTY, mostly.) </p>
<h2>Index</h2>
