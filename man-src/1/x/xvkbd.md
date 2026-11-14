---
title: "xvkbd(1)"
name: "xvkbd"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xvkbd/"
description: "xvkbd – virtual keyboard for X window system"
---

<h2 class="name">NAME</h2>
<p> xvkbd &#8211; virtual keyboard for X window system</p>
<h2>DESCRIPTION</h2>
<p> <i>xvkbd</i> is a virtual (graphical) keyboard program for X Window System which provides a facility to enter characters onto other clients (software) by clicking on a keyboard displayed on the screen. This may be used for systems without a hardware keyboard such as kiosk terminals or handheld devices. This program also has a facility to send characters specified as the command line option to another client. </p>
<p> The standard keyboard layout is based on the traditional US layout, but some other keyboard layout (see &quot;Screenshot&quot;) are also supported. The default window size may be too large for systems with small screen, but it can be configured to use smaller space (220&#215;90 pixels, for example). For details, see also &quot;Screenshot&quot; and &quot;How to Customize <i>xvkbd</i>&quot; below, and resouce files in the distribution. </p>
<p> <i>xvkbd</i> version 2.1 and later support word completion and <i>xvkbd</i> version 4.0 and later will now learns the used words for word completion , which may make it easier to enter long words with <i>xvkbd</i>. </p>
<p> <i>IMPORTANT NOTE:</i> When invoking <i>xvkbd</i> from display managers such as XDM, GDM, etc., always use <i>xvkbd</i> with <code>-secure</code> option or you will have serious security risk. </p>
<h2>Environment</h2>
<p> <i>xvkbd</i> will work on X11R5 or X11R6. It is tested on <i>redhat Linux</i> and <i>Solaris</i>, and it will work also on most UNIX-like systems. </p>
<p> This program uses <i>Xaw</i> (use of <i>Xaw3d</i> is recommended) and no special library is required. </p>
<h2>Operation</h2>
<h2> Input Keys</h2>
<p> When <i>xvkbd</i> is started, the image of a keyboard will be displayed on the screen. Clicking any key on the <i>xvkbd</i> window will send the character to the focused window as if the key had been actually typed with the hardware keyboard. </p>
<p> If you want to input upper-case alphabets or other characters on the upper position on the keyboard, you should click the key after selecting <i>Shift</i> by clicking it, or click the key with mouse button 3 (maybe right button) or mouse button 4. In the similar manner, if you want to input <i>Control</i>ed characters, you should click the key after clicking <i>Control</i>, or click the key with mouse button 2 (maybe middle button). <i>Alt</i> and <i>Meta</i> can be used in the similar manner with <i>Control</i>, but there are no shortcuts with mouse buttons. </p>
<h2> &#8220;Quick Modifiers&#8221;</h2>
<p> <i>xvkbd</i> 2.5 and later support another way to input characters with modifiers such as <i>Shift</i>, <i>Control</i>, <i>AltGr</i>, etc., which may be useful especially for machines with touch panels such as PDAs &#8211; we would call it <i>&quot;Quick Modifiers&quot;</i>. </p>
<p> <i>Quick Modifiers</i> can be enabled/disabled by the &#8220;<i>Enable &quot;Quick Modifiers?</i>&#8221; entry on the property panel. If <i>Quick Modifiers</i> is enabled, it will be activated by pressing a key on the <i>xvkbd</i> window, move the pointer outside of the key, and then release the mouse button or equivalent. </p>
<p> The direction of the pointer motion will select the modifier: </p>
<pre>
  up        - Shift
  right     - AltGr
  right-up  - Shift AltGr
  left      - Control
  left-up   - Shift Control
  down      - Meta
  left-down - Alt
</pre>
<h2> Setting Input Focus</h2>
<p> If you are using a window manager and clients where you can set input focus by clicking mouse button on the window (and you don&#8217;t have to keep pointer in the window after that), you can simply set input focus in the normal way and then click keys on the <i>xvkbd</i> window &#8211; the character will be sent to the selected position. </p>
<p> If you are using a window manager or clients where you must keep the pointer in the input field to input from the keyboard, or if the input focus is switched to the <i>xvkbd</i> window when you clicked on the key on the <i>xvkbd</i> window, you must make <i>xvkbd</i> to set input focus explicitly by clicking the <i>Focus</i> button on the <i>xvkbd</i> window and then click on the input field. This input focus can be cleared by clicking <i>Focus</i> button with mouse button 3, or simply clicking <i>Focus</i> button twice. </p>
<h2> Word Completion</h2>
<p> Choosing &#8220;<i>Word Completion&#8230;</i>&#8221; in the main menu will popup the <i>Word Completion</i> panel. </p>
<p> When you entered characters by clicked keys on the <i>xvkbd</i> window as usual while the <i>Word Completion</i> panel open, words started with the characters will be listed in the panel, and you can enter the remaining characters of the selected word by clicking one of the words in the list. </p>
<p>&nbsp;<wbr>&nbsp;When&nbsp;&#8220;<i>Integrate Completion Panel?</i>&#8221;&nbsp;on the property panel is set on,<br />
&nbsp;<wbr>&nbsp;completion panel will be displayed on the main window when required.<br />
&nbsp;<wbr>&nbsp;.PP The dictionary (list of words) file is <code>/usr/share/xvkbd/words.english</code> by default, but it can be changed with <i>Static Dictionary</i> on the property panel. </p>
<p>&nbsp;<wbr>&nbsp;In addition,&nbsp;<i>xvkbd</i>&nbsp;records the used words and those scores in&nbsp;<code>$HOME/.xvkbd.words</code>.<br />
&nbsp;<wbr>&nbsp;</p>
<h2> Main Menu</h2>
<p> Pressing the &#8220;xvkbd&#8221; logo on the main keyboard (placed near left-bottom corner in the default configuration) will popup the main menu. </p>
<p> The menu contains following items:</p>
<dl>
<dt><i>About&#8230;</i></p>
<dd> Show short description of this program.</p>
<dt><i>Manual&#8230;</i></p>
<dd> Launch manual page reader.</p>
<dt><i>Keypad&#8230;</i></p>
<dd> Open the Keypad panel.</p>
<dt><i>Sun Function Keys&#8230;</i></p>
<dd> Open the Sun Function Keys panel.</p>
<dt><i>Dead Keys&#8230;</i></p>
<dd> Open the Dead Keys panel which can be used to enter Latin characters with accent symbol in double stroke.</p>
<dt><i>Word Completion&#8230;</i></p>
<dd> Open the Word Completion panel.</dl>
<dl>
<dt><i>Change Keyboard Layout&#8230;</i></p>
<dd> Open a popup window to change the keyboard layout. In the default configuration, Default (US), Belgian, Danish, French, German, Icelandic, Italian, Japanese (JIS-X-6002), Japanese (JIS-X-6004), Korean, Norwegian, Portuguese, Russian, Spanish, Swedish, Swiss/German, United Kingdom and Latin-1 are available.</p>
<dt><i>Edit Function Keys&#8230;</i></p>
<dd> Open a popup window to edit string assigned to function keys. See also &quot;Assigning Text to Function Keys&quot;.</p>
<dt><i>Show Keypad?</i></p>
<dd> Toggle show/hide of the keypad on the main window.</p>
<dt><i>Show Function Keys?</i></p>
<dd> Toggle show/hide of the function keys on the main window.</p>
<dt><i>Property&#8230;</i></p>
<dd> Popup the Property panel.</p>
<dt><i>Connect to Remote Display&#8230;</i></p>
<dd> Open a panel to specify the name of a remote display (in the meaning of the X Window System) to connect, so that following key events will be sent to windows on the remote display.</p>
<dt><i>Revert to Local Display</i></p>
<dd> Disconnect from the remote display so that following key events will be sent to windows on the local display. </p>
</dl>
<h2> Property Panel</h2>
<dl>
<dt><i>Enable &quot;Quick Modifiers&quot;?</i></p>
<dd> Toggle enable/disable of the <i>Quick Modifiers</i> feature.</p>
<dt><i>Lock Shift?</i></p>
<dd> Toggle locking/momentary of <i>Shift</i> keys.</p>
<dt><i>Lock AltGr?</i></p>
<dd> Toggle locking/momentary of <i>AltGr</i> key.</p>
<dt><i>Lock Control, Alt and Meta?</i></p>
<dd> Toggle locking/momentary of <i>Control</i>, <i>Alt</i> and <i>Meta</i> keys.</p>
<dt><i>Always on Top?</i></p>
<dd> If this entry is set ON, <i>xvkbd</i> attempts to keep the <i>xvkbd</i> window always on the top of the display (i.e. not to be hidden by other windows). This feature is experimental, and care should be taken as this feature can cause problem in some situations.</p>
<dt><i>Behave as Toolbar Window?</i></p>
<dd> <i>xvkbd</i> attempts to be a toolbar window when it is used with some kind of window managers such as Matchbox window manager.</p>
<dt><i>Use XTEST Extension?</i></p>
<dd> XTEST extension will be used if this entry is checked. If this entry is set inactive, the X server does not support XTEST extension.</p>
<dt><i>Jump Pointer?</i></p>
<dd> If this entry is set ON, <i>xvkbd</i> will temporary jump the pointer to the focused window, if XTEST extension is to be used to simulate keyboard events.</p>
<dt><i>Key-Click Sound</i></p>
<dd> Set on/off and duration of key-click sound.</p>
<dt><i>Automatic Click</i></p>
<dd> Set on/off of the automatic click feature and the delay before automatic click is activated. If this feature is set, <i>xvkbd</i> will work as if left mouse button is clicked when mouse pointer is moved on a button and stays long enough. You may want to set <i>Jump Pointer?</i> to OFF to avoid auto-repeating.</p>
<dt><i>Completion:</i></p>
<dd>
<dt>
&nbsp;<wbr>&nbsp;<i>Static Dictionary</i></p>
<dd>
&nbsp;<wbr>&nbsp;Set the filename to be used for word completion.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;This setting take precedence over the&nbsp;`<code>xvkbd.dictFile</code>&#8216;&nbsp;resource<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;and the&nbsp;<code>-dict</code>&nbsp;option.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Default:&nbsp;<code>/usr/share/xvkbd/words.english</code></p>
<dt>
&nbsp;<wbr>&nbsp;<i>Dynamic Dictionary Weight</i></p>
<dd>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;This parameter controls&nbsp;&quot;learning&quot;&nbsp;of recently used words.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;When this value is set 0,&nbsp;<i>xvkbd</i>&nbsp;will not learn used words.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;With higher value setting,&nbsp;<i>xvkbd</i>&nbsp;will quickly<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;learn the used words and effectively ignores frequency information<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;in the Static Dictionary.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Default: 1.</p>
<dt>
&nbsp;<wbr>&nbsp;<i>Insert Blank after Completion?&quot;</i></p>
<dd>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;If this button is set on,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>xvkbd</i>&nbsp;will insert blank&nbsp;(&#8216;&nbsp;&#8216;)&nbsp;automatically after word completion<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if the next character is not blank nor punctuations.</p>
<dt>
&nbsp;<wbr>&nbsp;<i>Integrate Completion Panel?&quot;</i></p>
<dd>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;If this button is set on,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;word completion panel will be inegrated at top of the main window<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;and will be activated when required. </p>
</dl>
<h2> Options</h2>
<p> <i>xvkbd</i> accept following command line options, in addition to general options such as `<code>-display</code>&#8216;. </p>
<dl>
<dt><code>-version</code></p>
<dd> Display version information and exit.</p>
<dt><code>-xsendevent</code></p>
<dd> Make <i>xvkbd</i> to use <i>XSendEvent()</i> to simulate keyboard events, as it was in <i>xvkbd</i> version 1.0. <i>xvkbd</i> version 1.1 and later will try to use XTEST extension instead in the default configuration. Because it is not unusual applications to ignore keyboard events generated with <code>-xsendevent</code>, you shouldn&#8217;t use <code>-xsendevent</code> option unless it is really required. </p>
<p> If XTEST extension is not supported by the X server, <i>xvkbd</i> will automatically switch to this mode. </p>
<p> Resource `<code>xvkbd.xtest: false</code>&#8216; has the same function.</p>
<dt><code>-no-sync</code></p>
<dd> Normally, <i>xvkbd</i> attempts to synchronize with the destinating client step by step. This can cause problem when the client (or the X server) responded too slow. In such situation, maybe this <code>-no-sync</code> can solve the problem. </p>
<p> Resource `<code>xvkbd.noSync: true</code>&#8216; has the same function.</p>
<dt><code>-no-jump-pointer</code></p>
<dd> Make <i>xvkbd</i> not to jump the pointer when sending events. In the default, <i>xvkbd</i> will temporary jump the pointer to the focused window, if input focus is set explicitly via <i>Focus</i> button, and XTEST extension is to be used to simulate keyboard events. </p>
<p> Resource `<code>xvkbd.jumpPointer: false</code>&#8216; has the same function.</p>
<dt><code>-no-back-pointer</code></p>
<dd> Make <i>xvkbd</i> not to jump the pointer back to the original position after events has been sent. Maybe this can be useful when using <i>xvkbd</i> to move the pointer position. </p>
<p> Resource `<code>xvkbd.jumpPointerBack: false</code>&#8216; has the same function.</p>
<dt><code>-modal</code></p>
<dd> Make labels on keys in the <i>xvkbd</i> window to be set independently for each of four shift states, not shifted, <i>Shift</i>, <i>AltGr</i> and <i>Shift</i>&#8211;<i>AltGr</i>. This is useful when you want to make the <i>xvkbd</i> window very small. </p>
<p> See also &quot;Customizing Keyboard Layout&quot; and resouce files in the distribution. </p>
<p> Resource `<code>xvkbd.modalKeytop: true</code>&#8216; has the same function.</p>
<dt><code>-geometry [</code><i>width</i>x<i>height</i>][<code>+</code><i>xoff</i>+<i>yoff</i>]</p>
<dd> Set window geometry (size and position). </p>
<p> You can use form like <code>-geometry 400&#215;130</code> to specify the window size, <code>-geometry +100+100</code> to specify the window position from left/top edge of the screen, and <code>-geometry 400&#215;130+100+100</code> to specify both the size and the position. You can specify position from right/bottom edge of the screen by using <code>&#8211;</code> instead of <code>+</code>, but please note that you must take account of size of the window border. (If you specify `<code>-geometry -0-0</code>&#8216;, the window will not fit in the screen.) </p>
<p> This can be set by <code>xvkbd.windowGeometry</code> resource (note that it is not <code>xvkbd.geometry</code>), too.</p>
<dt><code>-no-resize</code></p>
<dd> Disable resize of the <i>xvkbd</i> window. </p>
<p> Resource `<code>xvkbd.resizable: false</code>&#8216; has the same function.</p>
<dt><code>-no-repeat</code></p>
<dd> Do not auto-repeat even if key is depressed long time. </p>
<p> If auto-repeat is enabled (this is the default), time before start auto-repeat can be set as `<code>xvkbd*Repeater.initialDelay: 600</code>&#8216;, and period of repeat can be set as `<code>xvkbd*Repeater.minimumDelay: 100</code>&#8216; (unit of there parameters are milli-seconds). </p>
<p> Resource `<code>xvkbd.autoRepeat: false</code>&#8216; has the same function.</p>
<dt><code>-no-functionkey</code></p>
<dd> Do not display function keys. </p>
<p> Resource `<code>xvkbd.functionkey: false</code>&#8216; has the same function.</p>
<dt><code>-no-keypad</code></p>
<dd> Do not display keypad. </p>
<p> Resource `<code>xvkbd.keypad: false</code>&#8216; has the same function.</p>
<dt><code>-compact</code></p>
<dd> Do not display function keys nor keypad. </p>
<p> Resource `<code>xvkbd.compact: true</code>&#8216; has the same function.</p>
<dt><code>-keypad</code></p>
<dd> Display only keypad. This option will be ignored if `<code>-no-keypad</code>&#8216; or `<code>-compact</code>&#8216; is specified. </p>
<p> Resource `<code>xvkbd.keypadOnly: true</code>&#8216; has the same function.</p>
<dt><code>-text </code><i>string</i></p>
<dd> Send the string to the focused window (see also `<code>-window</code>&#8216; option). </p>
<p> If this option is specified, <i>xvkbd</i> will not open its window and terminate soon after sending the string. </p>
<p> The string can contain:</p>
<dt> &#8211;</p>
<dd> <code></code> &#8211; Return</p>
<dt> &#8211;</p>
<dd> <code>	</code> &#8211; Tab</p>
<dt> &#8211;</p>
<dd> <code></code> &#8211; Backspace</p>
<dt> &#8211;</p>
<dd> <code></code> &#8211; Escape</p>
<dt> &#8211;</p>
<dd> <code>\d</code> &#8211; Delete</p>
<dt> &#8211;</p>
<dd> <code>\S</code> &#8211; Shift (modify the next character; please note that modify with &#8220;<code>\S</code>&#8221; will be ignored in many cases. For example, &#8220;<code>a\Cb\ScD\CE</code>&#8221; will be interpreted as <code>a</code>, Control-<code>b</code>, <code>c</code>, Shift-<code>D</code>, and Control-Shift-<code>E</code>.)</p>
<dt> &#8211;</p>
<dd> <code>\C</code> &#8211; Control (modify the next character)</p>
<dt> &#8211;</p>
<dd> <code>\A</code> &#8211; Alt (modify the next character)</p>
<dt> &#8211;</p>
<dd> <code>\M</code> &#8211; Meta (modify the next character)</p>
<dt> &#8211;</p>
<dd> <code>\W</code> &#8211; Super (modify the next character)<br />
&nbsp;<wbr>&nbsp;.IP&nbsp;&quot;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&#8211;&nbsp;&quot;&nbsp;6 <code>\[</code><i>keysym</i><code>]</code> &#8211; the keysym <i>keysym</i> (e.g., <code>\[Left]</code>), which will be processed in the similar matter with other general characters</p>
<dt> &#8211;</p>
<dd> <code>\{</code><i>keysym</i><code>}</code> &#8211; the keysym <i>keysym</i> (e.g., <code>\{Left}</code>), which will be processed in more primitive matter and can also be used for modofier keys such as <i>Control_L</i>, <i>Meta_L</i>, etc.; also, <code>\{+</code><i>keysym</i><code>}</code> and <code>\{+</code><i>keysym</i><code>}</code> will simulate press and release of the key, respectively</p>
<dt> &#8211;</p>
<dd> <code>\D</code><i>digit</i> &#8211; delay <i>digit</i> * 100 ms</p>
<dt> &#8211;</p>
<dd> <code>
