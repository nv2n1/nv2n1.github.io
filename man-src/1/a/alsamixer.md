---
title: "alsamixer(1)"
name: "alsamixer"
section: "1"
letter: "a"
url: "/docs/linux/man/1-alsamixer/"
description: "alsamixer – soundcard mixer for ALSA soundcard driver, with ncurses interface"
---

<h2 class="name">NAME</h2>
<p> alsamixer &#8211; soundcard mixer for ALSA soundcard driver, with ncurses interface </p>
<h2>SYNOPSIS</h2>
<p> <code>alsamixer</code> [<i>options</i>] </p>
<h2>DESCRIPTION</h2>
<p> <code>alsamixer</code> is an ncurses mixer program for use with the ALSA soundcard drivers. It supports multiple soundcards with multiple devices. </p>
<h2>OPTIONS</h2>
<dl>
<dt><i>-h, &#8211;help</i></p>
<dd> Help: show available flags. </p>
<dt><i>-c, &#8211;card</i> &lt;card number or identification&gt;</p>
<dd> Select the soundcard to use, if you have more than one. Cards are numbered from 0 (the default). </p>
<dt><i>-D, &#8211;device</i> &lt;device identification&gt;</p>
<dd> Select the mixer device to control. </p>
<dt><i>-V, &#8211;view</i> &lt;mode&gt;</p>
<dd> Select the starting view mode, either <i>playback</i>, <i>capture</i> or <i>all</i>. </p>
<dt><i>-g, &#8211;no-color</i></p>
<dd> Toggle the using of colors. </p>
</dl>
<h2>MIXER VIEWS</h2>
<p> The top-left corner of <code>alsamixer</code> shows some basic information: the card name, the mixer chip name, the current view mode and the currently selected mixer item. When the mixer item is switched off, <i>[Off]</i> is displayed in its name. </p>
<p> Volume bars are located below the basic information area. You can scroll left/right when all controls can&#8217;t be put in a single screen. The name of each control is shown in the bottom below the volume bars. The currently selected item is drawn in red and/or emphasized. </p>
<p> Each mixer control with volume capability shows a box and the current volume filled in that box. The volume percentages are displayed below the volume bar for left and right channels. For a mono control, only one value is shown there. </p>
<p> When a mixer control is turned off, <i>M</i> (mute) appears below the volume bar. When it&#8217;s turned on, <i>O</i> in green appears instead. You can toggle the switch via <i>m</i> key. </p>
<p> When a mixer control has capture capability, the capture flag appears below the volume bar, too. When the capture is turned off, &#8212;&#8212;- is shown. <i>CAPTURE</i> in red appears when the capture switch is turned on. In addition, <i>L</i> and <i>R</i> letters appear in left and right side to indicate that left and the right channels are turned on. </p>
<p> Some controls have the enumeration list, and don&#8217;t show boxes but only texts which indicate the currently active item. You can change the item via up/down keys. </p>
<h2>VIEW MODES</h2>
<p> <code>alsamixer</code> has three view modes: playback, capture and all. In the playback view, only the controls related with playback are shown. Similarly, only the controls for capture (recording) are shown in the capture view. The all view mode shows all controls. The current view mode is displayed in the top-left position together with the mixer name, etc. </p>
<p> The default view mode is the playback view. You can change it via <i>-V</i> option. </p>
<p> Each view mode can be switched via keyboard commands, too. See the next section. </p>
<h2>KEYBOARD COMMANDS</h2>
<p> <code>alsamixer</code> recognizes the following keyboard commands to control the soundcard. Commands shown here in upper case can also be given in lower case. To be reminded of these keystrokes, hit the <i>h</i> key. </p>
<h3>General Controls</h3>
<p> The <i>Left</i> and <i>right arrow</i> keys are used to select the channel (or device, depending on your preferred terminology). You can also use <i>n</i> (&quot;next&quot;) and <i>p</i> (&quot;previous&quot;). </p>
<p> The <i>Up</i> and <i>Down Arrows</i> control the volume for the currently selected device. You can also use <i>+</i> or <i>&#8211;</i> for the same purpose. Both the left and right signals are affected. For independent left and right control, see below.<br />
&nbsp; The <i>B</i> or <i>=</i> key adjusts the balance of volumes on left and right channels. </p>
<p> <i>M</i> toggles muting for the current channel (both left and right). If the hardware supports it, you can mute left and right independently by using <i>,</i> (or <i>&lt;</i>) and <i>.</i> (or <i>&gt;</i>) respectively. </p>
<p> <i>SPACE</i> enables recording for the current channel. If any other channels have recording enabled, they will have their recording function disabled first. This only works for valid input channels, of course. </p>
<p> <i>L</i> re-draws the screen. </p>
<h3>View Mode Controls</h3>
<p> Function keys are used to change view modes. You can switch to the help mode and the proc info mode via <i>F1</i> and <i>F2</i> keys, respectively. On terminals that can&#8217;t use function keys like gnome-terminal, <i>?</i> and <i>/</i> keys can be used alternatively for help and proc modes. </p>
<p> <i>F3</i>, <i>F4</i> and <i>F5</i> keys are used to switch to playback, capture and all view mode, respectively. <i>TAB</i> key toggles the current view mode circularly. </p>
<h3>Quick Volume Changes</h3>
<p> <i>PageUp</i> increases volume by 5. </p>
<p> <i>PageDown</i> decreases volume by 5. </p>
<p> <i>End</i> sets volume to 0. </p>
<p> You can also control left &amp; right levels for the current channel independently, as follows: </p>
<p> [<i>Q</i> | <i>W</i> | <i>E</i> ] &#8212; turn UP [ left | both | right ] </p>
<p> [<i>Z</i> | <i>X</i> | <i>C</i> ] &#8212; turn DOWN [ left | both | right ] </p>
<p> If the currently selected mixer channel is not a stereo channel, then all UP keys will work like <i>W</i>, and all DOWN keys will work like <i>X</i>. </p>
<p> The number keys from <i>0</i> to <i>9</i> are to change the absolute volume quickly. They correspond to 0 to 90% volume. </p>
<h3>Selecting the Sound Card</h3>
<p> You can select another sound card by pressing the <i>F6</i> or <i>S</i> keys. This will show a list of available sound cards to choose from, and an entry to enter the mixer device name by hand. </p>
<h3>Exiting</h3>
<p> Quit the program with <i>ALT Q</i>, or by hitting <i>ESC</i>. Please note that you might need to hit <i>ESC</i> twice on some terminals since it&#8217;s regarded as a prefix key. </p>
<h2>VOLUME MAPPING</h2>
<p> In <code>alsamixer</code>, the volume is mapped to a value that is more natural for a human ear. The mapping is designed so that the position in the interval is proportional to the volume as a human ear would perceive it, i.e. the position is the cubic root of the linear sample multiplication factor. For controls with a small range (24 dB or less), the mapping is linear in the dB values so that each step has the same size visually. </p>
<p> Only for controls without dB information, a linear mapping of the hardware volume register values is used (this is the same algorithm as used in the old <code>alsamixer</code>). </p>
<h2>FILES</h2>
<p> Configuration is read from the following files: </p>
<p> <i>$XDG_CONFIG_HOME</i>/alsamixer.rc </p>
<p> <i>$HOME</i>/.config/alsamixer.rc </p>
<h2>CONFIGURATION</h2>
<p> Comments start with &#8216;#&#8217;. </p>
<dl>
<dt><code>color</code> <i>element</i> <i>foreground</i> <i>background</i> [<i>attribute&#8230;</i>]</p>
<dd>
<p> Valid values for <i>foreground</i> and <i>background</i> are: red, green, yellow, blue, magenta, cyan, white, black, none / default. </p>
<p> Valid values for <i>attribute</i> are: bold, normal, reverse, underline, dim, italic, blink. </p>
<p> See section <code>THEME ELEMENTS</code> for a list of <i>elements</i>. </p>
<dt><code>set</code> <i>option</i> <i>value</i></p>
<dd>
<p> <code>mouse_wheel_step</code> <i>&lt;N&gt;</i> </p>
<p> Set the mouse wheel step to <i>&lt;N&gt;</i> </p>
<p> <code>mouse_wheel_focuses_control</code> <i>0|1</i> </p>
<p> If enabled (<i>1</i>), mixer controls can be changed by hovering over them and scrolling the mouse wheel. </p>
<p> <code>background</code> <i>color</i> </p>
<p> Set the default background color </p>
<dt><code>bind</code> <i>key_definition</i> <i>command</i></p>
<dd>
<p> A <i>key_definition</i> may be:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;&#8211; a single character<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;&#8211; a combination with control: C-a<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;&#8211; a combination with alt: M-a<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;&#8211; a special keyname: Enter, Escape, PageUp, PageDown, Left, Down, Right, Up, Home, End, Backspace, F1 .. F12 </p>
<p> See section <code>COMMANDS</code> for a list of <i>commands</i>. </p>
</dl>
<h3>COMMANDS</h3>
<dl>
<dt><i>textbox_close</i></p>
<dd> Close textbox </p>
<dt><i>textbox_up</i> / <i>textbox_down</i></p>
<dd> Scroll text up/down by one line </p>
<dt><i>textbox_left</i> / <i>textbox_right</i></p>
<dd> Scroll text left/right by one column </p>
<dt><i>textbox_page_up</i> / <i>textbox_page_down</i></p>
<dd> Scroll text up/down one page </p>
<dt><i>textbox_page_left</i> / <i>textbox_page_right</i></p>
<dd> Scroll text left/right one page </p>
<dt><i>textbox_top</i> / <i>textbox_bottom</i></p>
<dd> Go to top/bottom position of text </p>
<dt><i>mixer_balance_volumes</i></p>
<dd> Balance both channels </p>
<dt><i>mixer_close</i></p>
<dd> Close alsamixer application </p>
<dt><i>mixer_help</i></p>
<dd> Show help </p>
<dt><i>mixer_mode_playback</i></p>
<dd> Show playback controls </p>
<dt><i>mixer_mode_capture</i></p>
<dd> Show capture controls </p>
<dt><i>mixer_mode_all</i></p>
<dd> Show playback and capture controls </p>
<dt><i>mixer_mode_toggle</i></p>
<dd> Toggle between playback/capture/all controls </p>
<dt><i>mixer_refresh</i></p>
<dd> Refresh screen </p>
<dt><i>mixer_previous</i> / <i>mixer_next</i></p>
<dd> Select previous/next mixer control </p>
<dt><i>mixer_control_focus_&lt;N&gt;</i></p>
<dd> Focus control number <i>&lt;N&gt;</i>. </p>
<dt><i>mixer_control_set_&lt;N&gt;</i>[<i>_left</i>|<i>_right</i>]</p>
<dd> Change volume of current control to <i>&lt;N&gt;</i> percent. </p>
<dt><i>mixer_control_up_&lt;N&gt;</i>[<i>_left</i>|<i>_right</i>]</p>
<dd> Increase volume of current control by <i>&lt;N&gt;</i> percent. </p>
<dt><i>mixer_control_down_&lt;N&gt;</i>[<i>_left</i>|<i>_right</i>]</p>
<dd> Decrease volume of current control by <i>&lt;N&gt;</i> percent. </p>
<dt><i>mixer_toggle_mute</i>[<i>_left</i>|<i>_right</i>]</p>
<dd> Toggle mute state of both/left/right channels </p>
<dt><i>mixer_toggle_capture</i>[<i>_left</i>|<i>_right</i>]</p>
<dd> Toggle capture state of both/left/right channels </p>
<dt><i>mixer_select_card</i></p>
<dd> Show window for selecting sound card </p>
<dt><i>mixer_system_information</i></p>
<dd> Show system information </p>
</dl>
<h3>THEME ELEMENTS</h3>
<dl>
<dt><i>mixer_frame</i> Color of the box around the mixer</p>
<dd>
<dt><i>mixer_text</i> Color of text at the top of the mixer</p>
<dd>
<dt><i>mixer_active</i> Color of <i>AlsaMixer</i> heading</p>
<dd>
<dt><i>ctl_frame</i> Color of the frame around the mixer controls</p>
<dd>
<dt><i>ctl_mute</i> Color indicating the mute state (<i>MM</i>)</p>
<dd>
<dt><i>ctl_nomute</i> Color indicating the unmute state (<i>00</i>)</p>
<dd>
<dt><i>ctl_capture</i> Color of <i>CAPTURE</i> text</p>
<dd>
<dt><i>ctl_nocapture</i> Colof of disabled capture label</p>
<dd>
<dt><i>ctl_label</i> Color of label underneath mixer controls</p>
<dd>
<dt><i>ctl_label_focus</i> Color of label underneath focused mixer control</p>
<dd>
<dt><i>ctl_mark_focus</i> Color of <i>&lt;&gt;</i> marks beside focused mixer label</p>
<dd>
<dt><i>ctl_bar_lo</i> Color of lower volume bar</p>
<dd>
<dt><i>ctl_bar_mi</i> Color of middle volume bar</p>
<dd>
<dt><i>ctl_bar_hi</i> Color of top volume bar</p>
<dd>
<dt><i>ctl_inactive</i> Color for inactive control</p>
<dd>
<dt><i>ctl_label_inactive</i> Color for inactive label</p>
<dd>
<dt><i>errormsg</i> Color used for error message</p>
<dd>
<dt><i>infomsg</i> Color used for information message</p>
<dd>
<dt><i>textbox</i> Color used for textbox (user input)</p>
<dd>
<dt><i>textfield</i> Color used for textbox</p>
<dd>
<dt><i>menu</i> Color used for menu</p>
<dd>
<dt><i>menu_selected</i> Color used for selected entry in menu</p>
<dd>
</dl>
<h2>SEE ALSO</h2>
<p> <code> <a href="/docs/linux/man/1-amixer/">amixer</a>(1), <a href="/docs/linux/man/1-aplay/">aplay</a>(1), <a href="/docs/linux/man/1-arecord/">arecord</a>(1) </code> </p>
<h2>AUTHOR</h2>
<p> <code>alsamixer</code> has been written by Tim Janik and been further improved by Jaroslav Kysela &lt;perex [at] perex.cz&gt; and Clemens Ladisch &lt;clemens [at] ladisch.de&gt;. </p>
<p> This manual page was provided by Paul Winkler &lt;zarmzarm [at] erols.com&gt;. </p>
<h2>Index</h2>
