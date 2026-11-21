---

title: "xvkbd(1)"
name: "xvkbd"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xvkbd/"
description: "xvkbd – virtual keyboard for X window system"
---

<p> <i>xvkbd</i> is a virtual (graphical) keyboard program for X Window System which provides a facility to enter characters onto other clients (software) by clicking on a keyboard displayed on the screen. This may be used for systems without a hardware keyboard such as kiosk terminals or handheld devices. This program also has a facility to send characters specified as the command line option to another client. </p>
<p> The standard keyboard layout is based on the traditional US layout, but some other keyboard layout (see &quot;Screenshot&quot;) are also supported. The default window size may be too large for systems with small screen, but it can be configured to use smaller space (220x90 pixels, for example). For details, see also &quot;Screenshot&quot; and &quot;How to Customize <i>xvkbd</i>&quot; below, and resouce files in the distribution. </p>
<p> <i>xvkbd</i> version 2.1 and later support word completion and <i>xvkbd</i> version 4.0 and later will now learns the used words for word completion , which may make it easier to enter long words with <i>xvkbd</i>. </p>
<p> <i>IMPORTANT NOTE:</i> When invoking <i>xvkbd</i> from display managers such as XDM, GDM, etc., always use <i>xvkbd</i> with <code>-secure</code> option or you will have serious security risk. </p>
<h2>Environment</h2>
<p> <i>xvkbd</i> will work on X11R5 or X11R6. It is tested on <i>redhat Linux</i> and <i>Solaris</i>, and it will work also on most UNIX-like systems. </p>
<p> This program uses <i>Xaw</i> (use of <i>Xaw3d</i> is recommended) and no special library is required. </p>
<h2>Operation</h2>
<h2>Input Keys</h2>
<p> When <i>xvkbd</i> is started, the image of a keyboard will be displayed on the screen. Clicking any key on the <i>xvkbd</i> window will send the character to the focused window as if the key had been actually typed with the hardware keyboard. </p>
<p> If you want to input upper-case alphabets or other characters on the upper position on the keyboard, you should click the key after selecting <i>Shift</i> by clicking it, or click the key with mouse button 3 (maybe right button) or mouse button 4. In the similar manner, if you want to input <i>Control</i>ed characters, you should click the key after clicking <i>Control</i>, or click the key with mouse button 2 (maybe middle button). <i>Alt</i> and <i>Meta</i> can be used in the similar manner with <i>Control</i>, but there are no shortcuts with mouse buttons. </p>
<h2>``Quick Modifiers''</h2>
<p> <i>xvkbd</i> 2.5 and later support another way to input characters with modifiers such as <i>Shift</i>, <i>Control</i>, <i>AltGr</i>, etc., which may be useful especially for machines with touch panels such as PDAs - we would call it <i>&quot;Quick Modifiers&quot;</i>. </p>
<p> <i>Quick Modifiers</i> can be enabled/disabled by the ``<i>Enable &quot;Quick Modifiers?</i>&#8216;&#8216; entry on the property panel. If <i>Quick Modifiers</i> is enabled, it will be activated by pressing a key on the <i>xvkbd</i> window, move the pointer outside of the key, and then release the mouse button or equivalent. </p>
<p> The direction of the pointer motion will select the modifier: </p>
<pre><code>  up - Shift
  right - AltGr
  right-up - Shift AltGr
  left - Control
  left-up - Shift Control
  down - Meta
  left-down - Alt
</code></pre>
<h2>Setting Input Focus</h2>
<p> If you are using a window manager and clients where you can set input focus by clicking mouse button on the window (and you don&#8217;t have to keep pointer in the window after that), you can simply set input focus in the normal way and then click keys on the <i>xvkbd</i> window - the character will be sent to the selected position. </p>
<p> If you are using a window manager or clients where you must keep the pointer in the input field to input from the keyboard, or if the input focus is switched to the <i>xvkbd</i> window when you clicked on the key on the <i>xvkbd</i> window, you must make <i>xvkbd</i> to set input focus explicitly by clicking the <i>Focus</i> button on the <i>xvkbd</i> window and then click on the input field. This input focus can be cleared by clicking <i>Focus</i> button with mouse button 3, or simply clicking <i>Focus</i> button twice. </p>
<h2>Word Completion</h2>
<p> Choosing ``<i>Word Completion...</i>&#8216;&#8216; in the main menu will popup the <i>Word Completion</i> panel. </p>
<p> When you entered characters by clicked keys on the <i>xvkbd</i> window as usual while the <i>Word Completion</i> panel open, words started with the characters will be listed in the panel, and you can enter the remaining characters of the selected word by clicking one of the words in the list. </p>
<p> <br />
&nbsp;<wbr>&nbsp;When&nbsp;``<i>Integrate Completion Panel?</i>&#8216;&#8216;&nbsp;on the property panel is set on, <br />
&nbsp;<wbr>&nbsp;completion panel will be displayed on the main window when required. <br />
&nbsp;<wbr>&nbsp;.PP The dictionary (list of words) file is <code>/usr/share/xvkbd/words.english</code> by default, but it can be changed with <i>Static Dictionary</i> on the property panel. </p>
<p> <br />
&nbsp;<wbr>&nbsp;In addition,&nbsp;<i>xvkbd</i>&nbsp;records the used words and those scores in&nbsp;<code>$HOME/.xvkbd.words</code>. <br />
&nbsp;<wbr>&nbsp;  </p>
<h2>Main Menu</h2>
<p> Pressing the ``xvkbd&#8217;&#8216; logo on the main keyboard (placed near left-bottom corner in the default configuration) will popup the main menu. </p>
<p> The menu contains following items: </p>
<dl>
<dt><i>About...</i></dt>
<dd> <p> Show short description of this program. </p>
 </dd>
<dt><i>Manual...</i></dt>
<dd> <p> Launch manual page reader. </p>
 </dd>
<dt><i>Keypad...</i></dt>
<dd> <p> Open the Keypad panel. </p>
 </dd>
<dt><i>Sun Function Keys...</i></dt>
<dd> <p> Open the Sun Function Keys panel. </p>
 </dd>
<dt><i>Dead Keys...</i></dt>
<dd> <p> Open the Dead Keys panel which can be used to enter Latin characters with accent symbol in double stroke. </p>
 </dd>
<dt><i>Word Completion...</i></dt>
<dd> <p> Open the Word Completion panel. </p>
 </dd></dl>
<dl>
<dt><i>Change Keyboard Layout...</i></dt>
<dd> <p> Open a popup window to change the keyboard layout. In the default configuration, Default (US), Belgian, Danish, French, German, Icelandic, Italian, Japanese (JIS-X-6002), Japanese (JIS-X-6004), Korean, Norwegian, Portuguese, Russian, Spanish, Swedish, Swiss/German, United Kingdom and Latin-1 are available. </p>
 </dd>
<dt><i>Edit Function Keys...</i></dt>
<dd> <p> Open a popup window to edit string assigned to function keys. See also &quot;Assigning Text to Function Keys&quot;. </p>
 </dd>
<dt><i>Show Keypad?</i></dt>
<dd> <p> Toggle show/hide of the keypad on the main window. </p>
 </dd>
<dt><i>Show Function Keys?</i></dt>
<dd> <p> Toggle show/hide of the function keys on the main window. </p>
 </dd>
<dt><i>Property...</i></dt>
<dd> <p> Popup the Property panel. </p>
 </dd>
<dt><i>Connect to Remote Display...</i></dt>
<dd> <p> Open a panel to specify the name of a remote display (in the meaning of the X Window System) to connect, so that following key events will be sent to windows on the remote display. </p>
 </dd>
<dt><i>Revert to Local Display</i></dt>
<dd> <p> Disconnect from the remote display so that following key events will be sent to windows on the local display. </p>
 </dd></dl>
<h2>Property Panel</h2>
<dl>
<dt><i>Enable &quot;Quick Modifiers&quot;?</i></dt>
<dd> <p> Toggle enable/disable of the <i>Quick Modifiers</i> feature. </p>
 </dd>
<dt><i>Lock Shift?</i></dt>
<dd> <p> Toggle locking/momentary of <i>Shift</i> keys. </p>
 </dd>
<dt><i>Lock AltGr?</i></dt>
<dd> <p> Toggle locking/momentary of <i>AltGr</i> key. </p>
 </dd>
<dt><i>Lock Control, Alt and Meta?</i></dt>
<dd> <p> Toggle locking/momentary of <i>Control</i>, <i>Alt</i> and <i>Meta</i> keys. </p>
 </dd>
<dt><i>Always on Top?</i></dt>
<dd> <p> If this entry is set ON, <i>xvkbd</i> attempts to keep the <i>xvkbd</i> window always on the top of the display (i.e. not to be hidden by other windows). This feature is experimental, and care should be taken as this feature can cause problem in some situations. </p>
 </dd>
<dt><i>Behave as Toolbar Window?</i></dt>
<dd> <p> <i>xvkbd</i> attempts to be a toolbar window when it is used with some kind of window managers such as Matchbox window manager. </p>
 </dd>
<dt><i>Use XTEST Extension?</i></dt>
<dd> <p> XTEST extension will be used if this entry is checked. If this entry is set inactive, the X server does not support XTEST extension. </p>
 </dd>
<dt><i>Jump Pointer?</i></dt>
<dd> <p> If this entry is set ON, <i>xvkbd</i> will temporary jump the pointer to the focused window, if XTEST extension is to be used to simulate keyboard events. </p>
 </dd>
<dt><i>Key-Click Sound</i></dt>
<dd> <p> Set on/off and duration of key-click sound. </p>
 </dd>
<dt><i>Automatic Click</i></dt>
<dd> <p> Set on/off of the automatic click feature and the delay before automatic click is activated. If this feature is set, <i>xvkbd</i> will work as if left mouse button is clicked when mouse pointer is moved on a button and stays long enough. You may want to set <i>Jump Pointer?</i> to OFF to avoid auto-repeating. </p>
 </dd>
<dt><i>Completion:</i></dt>
<dd>  </dd>
<dt><br />
&nbsp;<wbr>&nbsp;<i>Static Dictionary</i></dt>
<dd> <p> <br />
&nbsp;<wbr>&nbsp;Set the filename to be used for word completion. <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;This setting take precedence over the&nbsp;`<code>xvkbd.dictFile</code>&#8216;&nbsp;resource <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;and the&nbsp;<code>-dict</code>&nbsp;option. <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Default:&nbsp;<code>/usr/share/xvkbd/words.english</code> </p>
 </dd>
<dt><br />
&nbsp;<wbr>&nbsp;<i>Dynamic Dictionary Weight</i></dt>
<dd> <p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;This parameter controls&nbsp;&quot;learning&quot;&nbsp;of recently used words. <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;When this value is set 0,&nbsp;<i>xvkbd</i>&nbsp;will not learn used words. <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;With higher value setting,&nbsp;<i>xvkbd</i>&nbsp;will quickly <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;learn the used words and effectively ignores frequency information <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;in the Static Dictionary. <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Default: 1. </p>
 </dd>
<dt><br />
&nbsp;<wbr>&nbsp;<i>Insert Blank after Completion?&quot;</i></dt>
<dd> <p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;If this button is set on, <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>xvkbd</i>&nbsp;will insert blank&nbsp;(&#8216;&nbsp;&#8216;)&nbsp;automatically after word completion <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if the next character is not blank nor punctuations. </p>
 </dd>
<dt><br />
&nbsp;<wbr>&nbsp;<i>Integrate Completion Panel?&quot;</i></dt>
<dd> <p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;If this button is set on, <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;word completion panel will be inegrated at top of the main window <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;and will be activated when required. </p>
 </dd></dl>
<h2>Options</h2>
<p> <i>xvkbd</i> accept following command line options, in addition to general options such as `<code>-display</code>&#8216;. </p>
<dl>
<dt><code>-version</code></dt>
<dd> <p> Display version information and exit. </p>
 </dd>
<dt><code>-xsendevent</code></dt>
<dd> <p> Make <i>xvkbd</i> to use <i>XSendEvent()</i> to simulate keyboard events, as it was in <i>xvkbd</i> version 1.0. <i>xvkbd</i> version 1.1 and later will try to use XTEST extension instead in the default configuration. Because it is not unusual applications to ignore keyboard events generated with <code>-xsendevent</code>, you shouldn&#8217;t use <code>-xsendevent</code> option unless it is really required. </p>
<p> If XTEST extension is not supported by the X server, <i>xvkbd</i> will automatically switch to this mode. </p>
<p> Resource `<code>xvkbd.xtest: false</code>&#8216; has the same function. </p>
 </dd>
<dt><code>-no-sync</code></dt>
<dd> <p> Normally, <i>xvkbd</i> attempts to synchronize with the destinating client step by step. This can cause problem when the client (or the X server) responded too slow. In such situation, maybe this <code>-no-sync</code> can solve the problem. </p>
<p> Resource `<code>xvkbd.noSync: true</code>&#8216; has the same function. </p>
 </dd>
<dt><code>-no-jump-pointer</code></dt>
<dd> <p> Make <i>xvkbd</i> not to jump the pointer when sending events. In the default, <i>xvkbd</i> will temporary jump the pointer to the focused window, if input focus is set explicitly via <i>Focus</i> button, and XTEST extension is to be used to simulate keyboard events. </p>
<p> Resource `<code>xvkbd.jumpPointer: false</code>&#8216; has the same function. </p>
 </dd>
<dt><code>-no-back-pointer</code></dt>
<dd> <p> Make <i>xvkbd</i> not to jump the pointer back to the original position after events has been sent. Maybe this can be useful when using <i>xvkbd</i> to move the pointer position. </p>
<p> Resource `<code>xvkbd.jumpPointerBack: false</code>&#8216; has the same function. </p>
 </dd>
<dt><code>-modal</code></dt>
<dd> <p> Make labels on keys in the <i>xvkbd</i> window to be set independently for each of four shift states, not shifted, <i>Shift</i>, <i>AltGr</i> and <i>Shift</i>-<i>AltGr</i>. This is useful when you want to make the <i>xvkbd</i> window very small. </p>
<p> See also &quot;Customizing Keyboard Layout&quot; and resouce files in the distribution. </p>
<p> Resource `<code>xvkbd.modalKeytop: true</code>&#8216; has the same function. </p>
 </dd>
<dt><code>-geometry [</code><i>width</i>x <i>height</i>][<code>+</code><i>xoff</i>+<i>yoff</i>] </dt>
<dd> <p> Set window geometry (size and position). </p>
<p> You can use form like <code>-geometry 400x130</code> to specify the window size, <code>-geometry +100+100</code> to specify the window position from left/top edge of the screen, and <code>-geometry 400x130+100+100</code> to specify both the size and the position. You can specify position from right/bottom edge of the screen by using <code>-</code> instead of <code>+</code>, but please note that you must take account of size of the window border. (If you specify `<code>-geometry -0-0</code>&#8216;, the window will not fit in the screen.) </p>
<p> This can be set by <code>xvkbd.windowGeometry</code> resource (note that it is not <code>xvkbd.geometry</code>), too. </p>
 </dd>
<dt><code>-no-resize</code></dt>
<dd> <p> Disable resize of the <i>xvkbd</i> window. </p>
<p> Resource `<code>xvkbd.resizable: false</code>&#8216; has the same function. </p>
 </dd>
<dt><code>-no-repeat</code></dt>
<dd> <p> Do not auto-repeat even if key is depressed long time. </p>
<p> If auto-repeat is enabled (this is the default), time before start auto-repeat can be set as `<code>xvkbd*Repeater.initialDelay: 600</code>&#8216;, and period of repeat can be set as `<code>xvkbd*Repeater.minimumDelay: 100</code>&#8216; (unit of there parameters are milli-seconds). </p>
<p> Resource `<code>xvkbd.autoRepeat: false</code>&#8216; has the same function. </p>
 </dd>
<dt><code>-no-functionkey</code></dt>
<dd> <p> Do not display function keys. </p>
<p> Resource `<code>xvkbd.functionkey: false</code>&#8216; has the same function. </p>
 </dd>
<dt><code>-no-keypad</code></dt>
<dd> <p> Do not display keypad. </p>
<p> Resource `<code>xvkbd.keypad: false</code>&#8216; has the same function. </p>
 </dd>
<dt><code>-compact</code></dt>
<dd> <p> Do not display function keys nor keypad. </p>
<p> Resource `<code>xvkbd.compact: true</code>&#8216; has the same function. </p>
 </dd>
<dt><code>-keypad</code></dt>
<dd> <p> Display only keypad. This option will be ignored if `<code>-no-keypad</code>&#8216; or `<code>-compact</code>&#8216; is specified. </p>
<p> Resource `<code>xvkbd.keypadOnly: true</code>&#8216; has the same function. </p>
 </dd>
<dt><code>-text </code><i>string</i></dt>
<dd> <p> Send the string to the focused window (see also `<code>-window</code>&#8216; option). </p>
<p> If this option is specified, <i>xvkbd</i> will not open its window and terminate soon after sending the string. </p>
<p> The string can contain: </p>
 </dd>
<dt> - </dt>
<dd> <p> <code>\r</code> - Return </p>
 </dd>
<dt> - </dt>
<dd> <p> <code>\t</code> - Tab </p>
 </dd>
<dt> - </dt>
<dd> <p> <code>\b</code> - Backspace </p>
 </dd>
<dt> - </dt>
<dd> <p> <code>\e</code> - Escape </p>
 </dd>
<dt> - </dt>
<dd> <p> <code>\d</code> - Delete </p>
 </dd>
<dt> - </dt>
<dd> <p> <code>\S</code> - Shift (modify the next character; please note that modify with ``<code>\S</code>&#8216;&#8216; will be ignored in many cases. For example, ``<code>a\Cb\ScD\CE</code>&#8216;&#8216; will be interpreted as <code>a</code>, Control-<code>b</code>, <code>c</code>, Shift-<code>D</code>, and Control-Shift-<code>E</code>.) </p>
 </dd>
<dt> - </dt>
<dd> <p> <code>\C</code> - Control (modify the next character) </p>
 </dd>
<dt> - </dt>
<dd> <p> <code>\A</code> - Alt (modify the next character) </p>
 </dd>
<dt> - </dt>
<dd> <p> <code>\M</code> - Meta (modify the next character) </p>
 </dd>
<dt> - </dt>
<dd> <p> <code>\W</code> - Super (modify the next character) <br />
&nbsp;<wbr>&nbsp;.IP&nbsp;&quot;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;-&nbsp;&quot;&nbsp;6 <code>\[</code><i>keysym</i><code>]</code> - the keysym <i>keysym</i> (e.g., <code>\[Left]</code>), which will be processed in the similar matter with other general characters </p>
 </dd>
<dt> - </dt>
<dd> <p> <code>\{</code><i>keysym</i><code>}</code> - the keysym <i>keysym</i> (e.g., <code>\{Left}</code>), which will be processed in more primitive matter and can also be used for modofier keys such as <i>Control_L</i>, <i>Meta_L</i>, etc.; also, <code>\{+</code><i>keysym</i><code>}</code> and <code>\{+</code><i>keysym</i><code>}</code> will simulate press and release of the key, respectively </p>
 </dd>
<dt> - </dt>
<dd> <p> <code>\D</code><i>digit</i> - delay <i>digit</i> * 100 ms </p>
 </dd>
<dt> - </dt>
<dd> <p> <code>\x</code><i>value</i> - move mouse pointer (use &quot;+&quot; or &quot;-&quot; for relative motion) </p>
 </dd>
<dt> - </dt>
<dd> <p> <code>\y</code><i>value</i> - move mouse pointer (use &quot;+&quot; or &quot;-&quot; for relative motion) </p>
 </dd>
<dt> - </dt>
<dd> <p> <code>\m</code><i>digit</i> - simulate click of the specified mouse button </p>
 </dd>
<dt><code>-file </code><i>filename</i></dt>
<dd> <p> Send the contents of the specified file to the focused window (see also `<code>-window</code>&#8216; option). If ``<code>-</code>&#8216;&#8216; was specified as the <i>filename</i>, string to be sent will be read from the standard input (stdin). </p>
<p> If this option is specified, <i>xvkbd</i> will not open its window and terminate soon after sending the string. </p>
 </dd>
<dt><code>-utf16</code></dt>
<dd> <p> When used with <code>-file</code> option, make <i>xvkbd</i> to accept UTF16 characters in the file. </p>
 </dd>
<dt><code>-delay </code><i>value</i></dt>
<dd> <p> Put <i>value</i> ms of delay for evey characters when sending characters with <code>-text</code> or <code>-file</code>. Maybe this is useful when problem arises when characters are entered too fast. </p>
<p> Resource `<code>xvkbd.textDelay: </code><i>value</i>&#8216; has the same function. </p>
 </dd>
<dt><code>-window </code><i>window</i></dt>
<dd> <p> Specify the ID (hexadecimal value leaded with `<code>0x</code>&#8216;, or decimal value), the name (instance name or class name) of the window, or the title of the window to set input focus. It is possible to use wildcard characters `<code>*</code>&#8216; and `<code>?</code>&#8216; to match the window name or the window title. </p>
<p> If this is not specified, <i>xvkbd</i> will use input focus under control of the window manager, unless focus is specified explicitly via <i>Focus</i> button. Even if this option is specified, you can set input focus to other windows using <i>Focus</i> button, or clear the input focus. </p>
<p> If there are two or more windows which have the name specified with this option, the window which was found first will be selected. </p>
 </dd>
<dt><code>-widget </code><i>widget-name</i></dt>
<dd> <p> Specify the name of the widget to set the input focus. To use this feature, the client must support <i>Editres</i> protocol. In general, this option will be used with `<code>-window</code>&#8216; option. </p>
<p> If you want to set input focus to the widget <code>foo.bar.zot</code>, you can write <code>zot</code>, <code>bar.zot</code> or <code>foo.bar.zot</code> as <i>widget-name</i>. To avoid confusion, the <i>widget-name</i> should match with a single widget of the client. </p>
<p> For example, </p>
<p> <code>xvkbd -window xarchie -widget searchText -text &quot;\Ca\Ckabc\r</code>&quot; </p>
<p> will enter the string ``<code>abc</code>&#8216;&#8216; to the ``Search Term&#8217;&#8216; field of a <code>xarchie</code> window. </p>
 </dd>
<dt><code>-remote-display </code><i>display</i></dt>
<dd> <p> Specify the display (in the meaning of the X Window System) to connect; <br />
&nbsp;<wbr>&nbsp;see also&nbsp;<i>Connect to Remote Display...</i>. </p>
 </dd>
<dt><code>-true-keypad</code></dt>
<dd> <p> If this option is specified, <i>xvkbd</i> will attempt to use <i>keysym</i>s such as <i>XK_KP_1</i> instead of <i>XK_1</i>. </p>
<p> Resource `<code>xvkbd.keypadKeysym: true</code>&#8216; has the same function. </p>
 </dd>
<dt><code>-dict </code><i>filename</i></dt>
<dd> <p> Specify the default dictionary (list of words) file to be used for word completion. The `<i>Completion Dictionary</i>&#8216; filename set on the Property panel takes precedence over this. </p>
<p> Resource `<code>xvkbd.dictFile: </code><i>filename</i>&#8216; has the same function. </p>
<p> See also ``Making your own completion dictionary&#8217;&#8216;. </p>
 </dd>
<dt><code>-minimizable</code></dt>
<dd> <p> Make <i>xvkbd</i> window can be minimized (iconified) even if no window manager is in use. When this feature is enabled, small triangle will be displayed at left ot the <i>xvkbd</i> main menu, and <i>xvkbd</i> window will be minimized when the triangle is clicked. </p>
<p> Resource `<code>xvkbd.minimizable: true</code>&#8216; has the same function. </p>
 </dd>
<dt><code>-secure</code></dt>
<dd> <p> Disable invocation of external commands, including user assigned command and the online manual reader. Connection to another displays would also be disabled. This option may be useful when <i>xvkbd</i> is to be run with some kind of privileges. </p>
<p> Resource `<code>xvkbd.secure: true</code>&#8216; has the same function. </p>
 </dd>
<dt><code>-nonexitable</code></dt>
<dd> <p> Disable termination of the <i>xvkbd</i> program. This option may be useful when <i>xvkbd</i> is to be run automatically for systems with no keyboards and users should not terminate the <i>xvkbd</i>. </p>
<p> Resource `<code>xvkbd.nonexitable: true</code>&#8216; has the same function. </p>
 </dd>
<dt><code>-xdm</code></dt>
<dd> <p> Same as <code>-secure -nonexitable</code>. When <i>xvkbd</i> is to be run for login screen, it would be suggested to use this option. </p>
 </dd>
<dt><code>-modifiers </code><i>modifiers</i></dt>
<dd> <p> Normally, <i>xvkbd</i> will activate modifiers (control, shift, etc.) only while sending characters. If modifiers were specified with this option, the specified modifiers will be activated while corresponding key on the <i>xvkbd</i> window is in active. For example, you can specify <code>-modifiers shift,control,meta,alt</code> to apply this for those four modifiers. Maybe this can be useful when attempting to decorate the mouse operations with the modifiers. Please note that the modifiers will also be applied when attempting to click on the <i>xvkbd</i> window and which can prevent the correct operation in some situations. </p>
<p> Resource `<code>xvkbd.positiveModifiers: </code><i>modifiers...</i>&#8216; has the same function. </p>
 </dd>
<dt><code>-debug</code></dt>
<dd> <p> Make <i>xvkbd</i> to output debug information. It also disables keyboard width adjustment, to help adjusting key size when making keyboard layout file. It also make <i>xvkbd</i> to accept signals SIGINT and SIGQUIT, which otherwise be ignored. </p>
 </dd>
<dt><code>-version</code></dt>
<dd> <p> Output version information and exit. </p>
 </dd></dl>
<h2>Screenshot</h2>
<dl>
<dt>Default (US)</dt>
<dd> <p> <a rel="nofollow" href="http://t-sato.in.coocan.jp/xvkbd/xvkbd-normal.gif">http://t-sato.in.coocan.jp/xvkbd/xvkbd-normal.gif</a> </p>
 </dd>
<dt>Belgian</dt>
<dd> <p> <a rel="nofollow" href="http://t-sato.in.coocan.jp/xvkbd/xvkbd-belgian.gif">http://t-sato.in.coocan.jp/xvkbd/xvkbd-belgian.gif</a> </p>
 </dd>
<dt>Danish</dt>
<dd> <p> <a rel="nofollow" href="http://t-sato.in.coocan.jp/xvkbd/xvkbd-danish.gif">http://t-sato.in.coocan.jp/xvkbd/xvkbd-danish.gif</a> </p>
 </dd>
<dt>French</dt>
<dd> <p> <a rel="nofollow" href="http://t-sato.in.coocan.jp/xvkbd/xvkbd-french.gif">http://t-sato.in.coocan.jp/xvkbd/xvkbd-french.gif</a> </p>
<p> <a rel="nofollow" href="http://t-sato.in.coocan.jp/xvkbd/xvkbd-french2.gif">http://t-sato.in.coocan.jp/xvkbd/xvkbd-french2.gif</a> </p>
 </dd>
<dt>German</dt>
<dd> <p> <a rel="nofollow" href="http://t-sato.in.coocan.jp/xvkbd/xvkbd-german.gif">http://t-sato.in.coocan.jp/xvkbd/xvkbd-german.gif</a> </p>
 </dd>
<dt>Icelandic</dt>
<dd> <p> <a rel="nofollow" href="http://t-sato.in.coocan.jp/xvkbd/xvkbd-icelandic.gif">http://t-sato.in.coocan.jp/xvkbd/xvkbd-icelandic.gif</a> </p>
 </dd>
<dt>Italian</dt>
<dd> <p> <a rel="nofollow" href="http://t-sato.in.coocan.jp/xvkbd/xvkbd-italian.gif">http://t-sato.in.coocan.jp/xvkbd/xvkbd-italian.gif</a> </p>
 </dd>
<dt>Japanese (JIS-X-6002)</dt>
<dd> <p> <a rel="nofollow" href="http://t-sato.in.coocan.jp/xvkbd/xvkbd-jisx6002.gif">http://t-sato.in.coocan.jp/xvkbd/xvkbd-jisx6002.gif</a> </p>
 </dd>
<dt>Japanese (JIS-X-6004)</dt>
<dd> <p> <a rel="nofollow" href="http://t-sato.in.coocan.jp/xvkbd/xvkbd-jisx6004.gif">http://t-sato.in.coocan.jp/xvkbd/xvkbd-jisx6004.gif</a> </p>
 </dd>
<dt>Norwegian</dt>
<dd> <p> <a rel="nofollow" href="http://t-sato.in.coocan.jp/xvkbd/xvkbd-norwegian.gif">http://t-sato.in.coocan.jp/xvkbd/xvkbd-norwegian.gif</a> </p>
 </dd>
<dt>Portuguese</dt>
<dd> <p> <a rel="nofollow" href="http://t-sato.in.coocan.jp/xvkbd/xvkbd-portuguese.gif">http://t-sato.in.coocan.jp/xvkbd/xvkbd-portuguese.gif</a> </p>
 </dd>
<dt>Spanish</dt>
<dd> <p> <a rel="nofollow" href="http://t-sato.in.coocan.jp/xvkbd/xvkbd-spanish.gif">http://t-sato.in.coocan.jp/xvkbd/xvkbd-spanish.gif</a> </p>
 </dd>
<dt>Swedish</dt>
<dd> <p> <a rel="nofollow" href="http://t-sato.in.coocan.jp/xvkbd/xvkbd-swedish.gif">http://t-sato.in.coocan.jp/xvkbd/xvkbd-swedish.gif</a> </p>
 </dd>
<dt>Swiss/German</dt>
<dd> <p> <a rel="nofollow" href="http://t-sato.in.coocan.jp/xvkbd/xvkbd-swissgerman.gif">http://t-sato.in.coocan.jp/xvkbd/xvkbd-swissgerman.gif</a> </p>
 </dd>
<dt>United Kingdom</dt>
<dd> <p> <a rel="nofollow" href="http://t-sato.in.coocan.jp/xvkbd/xvkbd-uk.gif">http://t-sato.in.coocan.jp/xvkbd/xvkbd-uk.gif</a> </p>
 </dd>
<dt>Latin-1</dt>
<dd> <p> <a rel="nofollow" href="http://t-sato.in.coocan.jp/xvkbd/xvkbd-latin1.gif">http://t-sato.in.coocan.jp/xvkbd/xvkbd-latin1.gif</a> </p>
 </dd>
<dt>Small Keyboard (maybe suitable for PDAs)</dt>
<dd> <p> <a rel="nofollow" href="http://t-sato.in.coocan.jp/xvkbd/xvkbd-small.gif">http://t-sato.in.coocan.jp/xvkbd/xvkbd-small.gif</a> </p>
 </dd>
<dt>Hebrew</dt>
<dd> <p> <a rel="nofollow" href="http://t-sato.in.coocan.jp/xvkbd/xvkbd-hebrew.gif">http://t-sato.in.coocan.jp/xvkbd/xvkbd-hebrew.gif</a> </p>
 </dd>
<dt>Greek</dt>
<dd> <p> <a rel="nofollow" href="http://t-sato.in.coocan.jp/xvkbd/xvkbd-greek.gif">http://t-sato.in.coocan.jp/xvkbd/xvkbd-greek.gif</a> </p>
 </dd>
<dt>Turkish</dt>
<dd> <p> <a rel="nofollow" href="http://t-sato.in.coocan.jp/xvkbd/xvkbd-turkish.gif">http://t-sato.in.coocan.jp/xvkbd/xvkbd-turkish.gif</a> </p>
 </dd>
<dt>Slovene</dt>
<dd> <p> <a rel="nofollow" href="http://t-sato.in.coocan.jp/xvkbd/xvkbd-slovene.gif">http://t-sato.in.coocan.jp/xvkbd/xvkbd-slovene.gif</a> </p>
 </dd>
<dt>Korean</dt>
<dd> <p> <a rel="nofollow" href="http://t-sato.in.coocan.jp/xvkbd/xvkbd-korean.gif">http://t-sato.in.coocan.jp/xvkbd/xvkbd-korean.gif</a> </p>
 </dd>
<dt>Russian (Cyrillic)</dt>
<dd> <p> <a rel="nofollow" href="http://t-sato.in.coocan.jp/xvkbd/xvkbd-russian.gif">http://t-sato.in.coocan.jp/xvkbd/xvkbd-russian.gif</a> </p>
 </dd></dl>
<h2>Download</h2>
<dl>
<dt><i>Latest Official Release</i></dt>
<dd> <p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp; <i><a rel="nofollow" href="http://t-sato.in.coocan.jp/xvkbd/xvkbd-4.0.tar.gz">http://t-sato.in.coocan.jp/xvkbd/xvkbd-4.0.tar.gz</a></i> <br />
 - source of version 4.0 (2019-08-31) </p>
 </dd>
<dt>previous release</dt>
<dd> <p> <a rel="nofollow" href="http://t-sato.in.coocan.jp/xvkbd/xvkbd-3.9.tar.gz">http://t-sato.in.coocan.jp/xvkbd/xvkbd-3.9.tar.gz</a> <br />
 - source of version 3.9 (2018-02-25) </p>
<p> <a rel="nofollow" href="http://t-sato.in.coocan.jp/xvkbd/xvkbd-3.8.tar.gz">http://t-sato.in.coocan.jp/xvkbd/xvkbd-3.8.tar.gz</a> <br />
 - source of version 3.8 (2017-06-06) </p>
<p> <a rel="nofollow" href="http://t-sato.in.coocan.jp/xvkbd/xvkbd-3.7.tar.gz">http://t-sato.in.coocan.jp/xvkbd/xvkbd-3.7.tar.gz</a> <br />
 - source of version 3.7 (2015-09-12) </p>
 </dd></dl>
<p> <i>xvkbd</i> is distributed under the terms of the GNU General Public License. </p>
<h2>Install</h2>
<h2>xmkmf</h2>
<dl>
<dt> o </dt>
<dd> <p> <i>untar</i> the source in a directory, and move to the directory </p>
 </dd>
<dt> o </dt>
<dd> <p> If you wish to use genuine <i>Xaw</i> instead of <i>Xaw3d</i>, edit <code>Imakefile</code> and remove (or comment-out) `<code>#define XAW3D</code>&#8216;. </p>
<p> When you are installing <i>xvkbd</i> (for example) in very old systems, you may also want to remove `<code>#define XTEST</code>&#8216; and `<code>#define I18N</code>&#8216; to disable XTEST and internationalization facility respectively. </p>
 </dd>
<dt> o </dt>
<dd> <p> Run: <code>xmkmf; make install install.man</code> </p>
 </dd></dl>
<h2>configure</h2>
<p> Alternatively, maybe you can: </p>
<dl>
<dt> o </dt>
<dd> <p> <i>untar</i> the source in a directory, and move to the directory </p>
 </dd>
<dt> o </dt>
<dd> <p> Run: <code>./configure; make; make install</code> </p>
 </dd></dl>
<h2>Customization</h2>
<i></i><h2>How to Customize xvkbd</h2>
<p> Some degree of customization of <i>xvkbd</i> is possible by setting resources. Some resources are already described above, and resources to customizing keyboard layout are described below. </p>
<p> To set resources, you can: </p>
<dl>
<dt> o </dt>
<dd> <p> put them in your <code>$HOME/.Xdefaults</code> file, or </p>
 </dd>
<dt> o </dt>
<dd> <p> load them via <i><a href="/docs/linux/man/1-xrdb/">xrdb</a></i>(1), or </p>
 </dd>
<dt> o </dt>
<dd> <p> set the filename to the <code>$XENVIRONMENT</code> environment variable, or </p>
 </dd>
<dt> o </dt>
<dd> <p> put them in application default directory as `<code>XVkbd-</code><i>suffix</i>&#8216; and set resource ``<code>xvkbd.customization: -</code><i>suffix</i>&#8216;&#8216;, or </p>
 </dd>
<dt> o </dt>
<dd> <p> put them in application default directory as <code>XVkbd</code>. </p>
 </dd></dl>
<p> Here, <i>application default directory</i> can be either of: </p>
<dl>
<dt> o </dt>
<dd> <p> directories specified with <code>$XUSERFILESEACHPATH</code>, <code>$XAPPLRESDIR</code> or else <code>$HOME</code> environment variable </p>
 </dd>
<dt> o </dt>
<dd> <p> system&#8217;s application default directory specified with <code>$XFILESEACHPATH</code> environment variable, or else the directory specified when compiling the X (e.g., <code>/usr/lib/X11/app-defaults</code>) </p>
 </dd></dl>
<p> When the application default file is to be stored in the system&#8217;s application default directory, the file must contain ``<code>#include &quot;XVkbd-common&quot;</code>&#8216;&#8216; near top of the file. </p>
<p> <i>xvkbd</i> is distributed with some application default files, and they will be installed in the system&#8217;s application default directory. </p>
<h2>Making Window Small</h2>
<p> Size (and position) of <i>xvkbd</i> window can be set by `<code>xvkbd.windowGeometry</code>&#8216; resource. When making window small, you may need to choose the smaller font, too. </p>
<pre><code>  xvkbd.windowGeometry: 220x90
  xvkbd.compact: true
  xvkbd*Font: 6x12
</code></pre>
<p> You may also want to set: </p>
<pre><code>  xvkbd.modalKeytop: true
</code></pre>
<p> to display only the labels for the current shift state, instead of trying to always display all of them in the small keytop. </p>
<p> See also <code>XVkbd-small.ad</code> in the <i>xvkbd</i> distribution. </p>
<h2>Removing Unwanted Keys</h2>
<p> Keys on <i>xvkbd</i> window can be removed by setting their width to 1. The resource name of the keys that start with a capital letter (and of the <code>space</code> key) is the same as the key itself, the others are of the form <i>&lt;row&gt;,&lt;col&gt;</i> (counting from zero). </p>
<p> To remove <i>Compose</i> key and make <i>Shift</i> key larger, you can write: </p>
<pre><code>  xvkbd*Multi_key.width: 1
  xvkbd*Shift_R.width: 75
</code></pre>
<p> To remove right <i>Alt</i> and <i>Meta</i> key, you can write: </p>
<pre><code>  xvkbd*Alt_R.width: 1
  xvkbd*Meta_R.width: 1
</code></pre>
<h2>Customizing Keyboard Layout</h2>
<p> Layout of keys on the <i>xvkbd</i> window can be customized with following resources: </p>
<dl>
<dt><code>xvkbd.NormalKeys</code></dt>
<dd> <p> list of keys available when neighter of <i>Shift</i> and <i>AltGr</i> are selected </p>
 </dd>
<dt><code>xvkbd.ShiftKeys</code></dt>
<dd> <p> list of keys available when <i>Shift</i> is selected </p>
 </dd>
<dt><code>xvkbd.AltgrKeys</code></dt>
<dd> <p> list of keys available when <i>AltGr</i> is selected </p>
 </dd>
<dt><code>xvkbd.ShiftAltgrKeys</code></dt>
<dd> <p> list of keys available when both <i>AltGr</i> and <i>Shift</i> are selected </p>
 </dd>
<dt><code>xvkbd.KeyLabels</code></dt>
<dd> <p> list of labels displayed on the keys </p>
 </dd>
<dt><code>xvkbd.NormalKeyLabels</code></dt>
<dd> <p> list of labels displayed on the keys <br />
&nbsp;<wbr>&nbsp;when neither of&nbsp;<i>Shift</i>&nbsp;and&nbsp;<i>AltGr</i>&nbsp;are selected. </p>
 </dd>
<dt><code>xvkbd.ShiftKeyLabels</code></dt>
<dd> <p> list of labels displayed on the keys <br />
&nbsp;<wbr>&nbsp;when&nbsp;<i>Shift</i>&nbsp;is selected </p>
 </dd>
<dt><code>xvkbd.AltgrKeyLabels</code></dt>
<dd> <p> list of labels displayed on the keys <br />
&nbsp;<wbr>&nbsp;when&nbsp;<i>AltGr</i>&nbsp;is selected </p>
 </dd>
<dt><code>xvkbd.ShiftAltgrKeyLabels</code></dt>
<dd> <p> list of labels displayed on the keys <br />
&nbsp;<wbr>&nbsp;when both&nbsp;<i>AltGr</i>&nbsp;and&nbsp;<i>Shift</i>&nbsp;are selected </p>
 </dd></dl>
<p> Four resources to set labels on the keys (<code>xvkbd.NormalKeyLabels</code>, <code>xvkbd.ShiftKeyLabels</code>, <code>xvkbd.AltgrKeyLabels</code> and <code>xvkbd.ShiftAltgrKeyLabels</code>) will be used instead of <code>xvkbd.KeyLabels</code> when <code>xvkbd.modalKeytop</code> resoruce is set <code>true</code>. </p>
<p> In all of those resources, each keys are separated by spaces, and rows of keys are terminated with `<code> \n\</code>&#8216; (note that `<code>\n</code>&#8216; must have space before it). Please refer <code>XVkbd-german.ad</code> and <code>XVkbd-latin1.ad</code> in the <i>xvkbd</i> distribution for more about these resources. </p>
<p> <code>XVkbd-german</code> and <code>XVkbd-latin1</code> will be installed in the system&#8217;s application default directory, and setting the resource ``<code>xvkbd.customization: -german</code>&#8216;&#8216; will make <i>xvkbd</i> to use the German layout. For another method to activate those settings, please refer &quot;How to Customize <i>xvkbd</i>&quot; above. </p>
<h2>Assigning Text to Function Keys</h2>
<p> Text can be assigned to each function keys (and, actually, to most other keys). If text is assigned to the function key, clicking on the key will send the assigned text instead of the function key itself. When pointer is on a key where text is assigned, the text will be displayed near the key. </p>
<p> The setting will be read from a text file which contains text for each function keys as: </p>
<pre><code>  F1 text for F1
  F2 text for F2
  s:F1 text for Shift-F1
  c:F1 text for Control-F1
  m:F1 text for Meta-F1
  a:F1 text for Alt-F1
  ...
</code></pre>
<p> `<code>s:</code>&#8216;, `<code>c:</code>&#8216;, `<code>m:</code>&#8216; and `<code>a:</code>&#8216; before the keys name indicates four modifiers (<i>Shift</i>, <i>Control</i>, <i>Meta</i> and <i>Alt</i>) respectively. </p>
<p> If the first character of the assigned string is `<code>!</code>&#8216;, the string will be used as command to be executed when the key is clicked. To assign string starting with `<code>!</code>&#8216; or `<code>\</code>&#8216;, put `<code>\</code>&#8216; before the string. </p>
<p> The file is <code>$HOME/.xvkbd</code> in default, and it can be changed by setting the filename with <code>xvkbd.keyFile</code> resource. </p>
<p> For <code>F1</code> to <code>F12</code> with or without <i>Shift</i> modifier, it is possible to edit the assigned string on a panel popped up via &quot;<i>Edit Function Keys...</i>&quot; in the main menu. </p>
<h2>Miscellaneous Informations</h2>
<h2>Notes</h2>
<dl>
<dt> o </dt>
<dd> <p> On <i>XFree86</i>, resolution switch with <i>Ctrl + Alt + Keypad-Plus</i> and <i>Ctrl + Alt + Keypad-Minus</i> may be simulated. However, <i>Ctrl + Alt + Backspace</i> will not be simulated. </p>
 </dd>
<dt> o </dt>
<dd> <p> <i>Shift</i> is used to decide key to be sent and it will not used to set modifier bit when sending the event. You can use <code>xev</code> command to check what is actually sent. </p>
 </dd>
<dt> o </dt>
<dd> <p> If <i>Alt</i> or <i>Meta</i> is not defined as modifier, the key can&#8217;t be used as modifier. You can use `<code>xmodmap -pm</code>&#8216; to check how modifiers are defined. </p>
 </dd>
<dt> o </dt>
<dd> <p> <i>Num Lock</i> (and maybe other modifiers) on the physical keyboard may not work correctly when <i>xvkbd</i> is in use. </p>
 </dd></dl>
<h2>Additional Informations</h2>
<dl>
<dt>ChangeLog</dt>
<dd> <p> <a rel="nofollow" href="http://t-sato.in.coocan.jp/xvkbd/ChangeLog">http://t-sato.in.coocan.jp/xvkbd/ChangeLog</a> </p>
 </dd>
<dt>FAQ - Possible Problems and Solutions</dt>
<dd> <p> <a rel="nofollow" href="http://t-sato.in.coocan.jp/xvkbd/faq.html">http://t-sato.in.coocan.jp/xvkbd/faq.html</a> </p>
 </dd>
<dt>Hints to use <code>xvkbd -text</code></dt>
<dd> <p> <a rel="nofollow" href="http://t-sato.in.coocan.jp/xvkbd/xvkbd-text.html">http://t-sato.in.coocan.jp/xvkbd/xvkbd-text.html</a> </p>
 </dd>
<dt>Note about how to send key events</dt>
<dd> <p> <a rel="nofollow" href="http://t-sato.in.coocan.jp/xvkbd/events.html">http://t-sato.in.coocan.jp/xvkbd/events.html</a> </p>
 </dd></dl>
<h2>Author</h2>
<p> <i>xvkbd</i> was written by Tom Sato, and it is distributed under the terms of the GNU General Public License Version 2 or any later version. </p>
<p> Please send any feedback (such as bug reports, requests or comments) to Tom Sato &lt;VEF00200 [at] nifty.com&gt;. </p>
<p> The latest version of this software and more information about it may be available at <a rel="nofollow" href="http://t-sato.in.coocan.jp/xvkbd/.">http://t-sato.in.coocan.jp/xvkbd/.</a> </p>
