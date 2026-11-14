---
title: "eterm(1)"
name: "eterm"
section: "1"
letter: "e"
url: "/docs/linux/man/1-eterm/"
description: "Eterm – the Enlightened terminal emulator for the X Window System"
---

<p>Eterm &#8211; the Enlightened terminal emulator for the X Window System</p>
<h2>Synopsis</h2>
<p><code>Eterm</code> [<i>options</i>] </p>
<h2>Description</h2>
<p><code>Eterm</code> &#8212; version <code>0.9.5</code> &#8212; is a color vt102 terminal emulator intended as an <i><a href="/docs/linux/man/1-xterm/">xterm</a></i>(1) replacement. It is designed with a Freedom of Choice philosophy, leaving as much power, flexibility, and freedom as possible in the hands of the user. It is designed to look good and work well, but takes a feature-rich approach rather than one of minimalism. <code>Eterm</code> uses Imlib for advanced graphic abilities. See below for details.</p>
<h2>Options</h2>
<p>The <code>Eterm</code> options are listed below. In keeping with the freedom-of-choice philosophy, options may be eliminated or default values chosen at compile-time, so options and defaults listed may not accurately reflect the version installed on your system. </p>
<p> Options that do not take a parameter (besides -h and &#8211;help) are boolean. If you use the POSIX (short) option, you are forcing the parameter to &quot;true&quot;. If you use the long option, you can use any of the accepted boolean values, which are &quot;yes&quot;, &quot;on&quot;, &quot;1&quot;, and &quot;true&quot; to turn the option on, or &quot;no&quot;, &quot;off&quot;, &quot;0&quot;, or &quot;false&quot; to turn the option off. The same is true for boolean values in the configuration file. </p>
<dl>
<dt><code>-t</code><i> theme</i><code>, &#8211;theme </code><i>theme</i></p>
<dd>Load specified <i>theme.</i> Consult the FAQ for more details on what constitutes an Eterm <i>theme.</i></p>
<dt><code>-X</code><i> conffile</i><code>, &#8211;config-file </code><i>conffile</i></p>
<dd>Use an alternative user config file name. Otherwise Eterm uses the default, which is <i>user.cfg.</i> The theme config file is always <i>theme.cfg.</i></p>
<dt><code>-d</code><i> displayname</i><code>, &#8211;display </code><i>displayname</i></p>
<dd>Attempt to open a window on the named X display <i>displayname.</i> In the absence of this option, the display specified by the <code>DISPLAY</code> environment variable is used.</p>
<dt><code>&#8211;debug</code><i> level</i></p>
<dd>Show debugging output. <i>level</i> is an integer between 0 and 5 which determines how verbose the debugging output is.</p>
<dt><code>&#8211;install</code></p>
<dd>Tells Eterm to install its own colormap rather than using the default one.</p>
<dt><code>-h</code>,<code> &#8211;help</code></p>
<dd>Print out a message describing available options.</p>
<dt><code>&#8211;version</code></p>
<dd>Print <code>Eterm</code> version and compile-time configuration.</p>
<dt><code>-r</code>,<code> &#8211;reverse-video</code></p>
<dd>Reverse video, swaps the foreground and background colors.</p>
<dt><code>-b</code><i> color</i><code>, &#8211;background-color </code><i>color</i></p>
<dd>Set <i>color</i> as the background color. <code>NOTE:</code> this will actually be the foreground color if reverse video is also selected.</p>
<dt><code>-f</code><i> color</i><code>, &#8211;foreground-color </code><i>color</i></p>
<dd>Set <i>color</i> as the foreground (text) color. <code>NOTE:</code> this will actually be the background color if reverse video is also selected.</p>
<dt><code>&#8211;color0</code><i> color</i></p>
<dd>
<dt><code>&#8230;</code></p>
<dd>
<dt><code>&#8211;color15</code><i> color</i></p>
<dd>Use <i>color</i> as color X.</p>
<dt><code>&#8211;colorBD</code><i> color</i></p>
<dd>Use <i>color</i> as the bold color.</p>
<dt><code>&#8211;colorUL</code><i> color</i></p>
<dd>Use <i>color</i> as the underline color.</p>
<dt><code>&#8211;pointer-color</code><i> color</i></p>
<dd>Use <i>color</i> as the pointer color.</p>
<dt><code>-c</code><i> color</i><code>, &#8211;cursor-color </code><i>color</i></p>
<dd>Use <i>color</i> as the cursor color.</p>
<dt><code>&#8211;cursor-text-color</code><i> color</i></p>
<dd>Use <i>color</i> as the cursor text color.</p>
<dt><code>-g</code><i> geom</i><code>, &#8211;geometry </code><i>geom</i></p>
<dd>Window geometry as Width x Height+X coord+Y coord, i.e 100&#215;200+0+100</p>
<dt><code>-i</code>,<code>&#8211;iconic</code></p>
<dd>Start in iconified state (only if the window manager supports iconification).</p>
<dt><code>-n</code><i> name</i><code>, &#8211;name </code><i>name</i></p>
<dd>Sets name of current instance to <i>name.</i> This will affect the icon title and the window title string unless they are otherwise explicitly set.</p>
<dt><code>-T</code><i> title</i><code>, &#8211;title </code><i>title</i></p>
<dd>Sets window&#8217;s title text to <i>title.</i></p>
<dt><code>&#8211;icon-name</code><i> text</i></p>
<dd>Sets the icon title text to <i>text.</i></p>
<dt><code>-B</code><i> type</i><code>, &#8211;scrollbar-type </code><i>type</i></p>
<dd>Specifies the <i>type</i> scrollbar style should be used. <i>type</i> can be any of <code>motif</code>, <code>xterm</code>, or <code>next</code>.</p>
<dt><code>&#8211;scrollbar-width</code><i> width</i></p>
<dd>Set the width of the scrollbar, in pixels, to <i>width</i>. Eterm does not impose any restrictions on this value, but it should be reasonable.</p>
<dt><code>-D</code><i> desktop</i><code>, &#8211;desktop </code><i>desktop</i></p>
<dd>Starts the Eterm on the specified desktop. <i>desktop</i> should be an integer between 0 and your highest-numbered desktop. <code>NOTE</code>: You must have a GNOME-compliant window manager for this feature to work. Please see <a rel="nofollow" href="http://www.gnome.org/devel/gnomewm/">http://www.gnome.org/devel/gnomewm/</a> for more information on the <code>_WIN_WORKSPACE</code> property and how to support it.</p>
<dt><code>&#8211;line-space</code><i> num</i></p>
<dd>Size of the extra gap, in pixels, to provide between lines in the terminal window.</p>
<dt><code>&#8211;bold-font</code><i> font</i></p>
<dd>Sets the bold text font to <i>font</i>.</p>
<dt><code>-F</code><i> font</i><code>, &#8211;font </code><i>font</i></p>
<dd>Sets the normal text font to <i>font</i>.</p>
<dt><code>&#8211;default-font-index</code><i> num</i></p>
<dd>Specifies the index of the default (normal) text font.</p>
<dt><code>&#8211;font1</code><i> font</i></p>
<dd>
<dt><code>&#8230;</code></p>
<dd>
<dt><code>&#8211;font4</code><i> font</i></p>
<dd>Sets the font at the specified index (1-4) to <i>font</i>.</p>
<dt><code>&#8211;proportional</code></p>
<dd>Specifies that the font in use is proportional and requests standard deviation-based character cell spacing. Terminals must use fixed-width character cells to maintain proper columnal alignment, even when proportionally-spaced fonts are in use. Some proportionally-spaced fonts vary greatly between the minimum and maximum character widths. This option chooses a character cell size which is up to two standard deviations above the average character width but will not exceed the maximum width of the largest glyph. Note that characters larger than the chosen cell width will overwrite (or be overwritten by) other characters and may tend to leave pixel droppings. This behavior is an expected side-effect of an imperfect scenario. If you object to this behavior, do not use this option.</p>
<dt><code>&#8211;font-fx</code><i> effects</i></p>
<dd>Specifies the effects to apply to the terminal window font. The value of <i>effects</i> is a single string containing a series of corner/color pairs. These pairs define toward which corner a drop shadow of each character should be made, and what color that shadow will be. The corner is specified first using the following keywords: <code>top_left</code> or <code>tl</code>, <code>top_right</code> or <code>tr</code>, <code>bottom_left</code> or <code>bl</code>, and <code>bottom_right</code> or <code>br</code>. Each corner specifier is then followed by a color. </p>
<p> There are also several shortcuts for doing common effects. You can get a single-color outline by using the keyword <code>outline</code> followed by a color. A single-color drop shadow is also available using the keyword <code>shadow</code> followed by an optional corner specifier (<code>bottom_right</code> being the default) and a color. For a 3-D embossed look, use <code>emboss</code><i> dark_color</i> <i>light_color</i>. The opposite effect, a carved-out look, can be obtained with <code>carved</code><i> dark_color</i> <i>light_color</i>. (Of course, with those last two, the 3-D look will only work if you choose the light and dark colors wisely.) </p>
<p> Finally, for no font effects at all, simply specify the keyword <code>none</code>. </p>
<p> The default value is <code>bottom_right black</code> which yields a black drop shadow, greatly improving the visibility of lightly-colored fonts on top of light spots in a background image. Note that font effects are not active in solid color mode.</p>
<dt><code>-P</code><i> pic</i><code>, &#8211;background-pixmap </code><i>pic</i></p>
<dd>Use <i>pic</i> as the background image. <i>pic</i> can be in any format that Imlib understands. Currently this means just about anything, including JPG, PNG, GIF, TIFF, PPM, etc. The image is tiled by default. To specify alternate geometry, follow the filename with an <code>@</code> sign and the geometry string. Image geometry is specified as <code>@</code><i>w</i><code>x</code><i>h</i><code>+</code><i>x</i><code>+</code><i>y</i><code>:</code><i>ops</i> where <i>w</i> and <i>h</i> are the horizontal/vertical scaling percentages, <i>x</i> and <i>y</i> are the horizontal/vertical alignment percentages, and <i>ops</i> is a colon-delimited list of operations: <code>tiled</code> (to tile the image), <code>propscaled</code> (for proportional scaling). Note that these operations can be combined for various effects.</p>
<dt><code>-I</code><i> pic</i><code>, &#8211;icon </code><i>pic</i></p>
<dd>Sets the icon pixmap file to <i>pic</i>. Works similarly to the <code>-P</code> option above.</p>
<dt><code>&#8211;up-arrow-pixmap</code><i> pic</i></p>
<dd>As above, except the scrollbar&#8217;s up-arrow is set.</p>
<dt><code>&#8211;down-arrow-pixmap</code><i> pic</i></p>
<dd>As above, except the scrollbar&#8217;s down-arrow is set.</p>
<dt><code>&#8211;trough-pixmap</code><i> pic</i></p>
<dd>As above, except the scrollbar&#8217;s background (trough) is set.</p>
<dt><code>&#8211;anchor-pixmap</code><i> pic</i></p>
<dd>As above, except the scrollbar&#8217;s anchor image is set.</p>
<dt><code>&#8211;menu-pixmap</code><i> pic</i></p>
<dd>As above, except the menu background image is set.</p>
<dt><code>-O</code>,<code> &#8211;trans</code></p>
<dd>This gives a pseudo-transparent Eterm. The image is taken directly from the root window, so any requests for changing the pixmap are ignored. If you do not use Enlightenment (<a rel="nofollow" href="http://www.enlightenment.org/)">http://www.enlightenment.org/)</a> as your window manager (or another compliant window manager&#8230;I have been told that WindowMaker works also), you will need to use the <i>Esetroot</i> program (found in the <code>utils/</code> directory) to set your root background image.</p>
<dt><code>-0</code>, <code>&#8211;itrans</code></p>
<dd>Activate the immotile transparency optimization for transparent Eterm windows. Note that this does NOT activate transparency; you must still include the <code>-O</code> or <code>&#8211;trans</code> option. This option should be used on transparent windows which are shaded or tinted and which do not move around on the desktop much. See the <code>Mon Mar 6 21:11:13 PST 2000</code> ChangeLog entry for a more detailed explanation.</p>
<dt><code>&#8211;viewport-mode</code></p>
<dd>This activates a special Eterm mode which is hard to describe in words. Basically, imagine the effect you get with pseudo-transparency, where the desktop background moves through the Eterm window as you move the window, so that it always aligns with the desktop image. Now, imagine the same effect, but the image used isn&#8217;t the desktop image but any pixmap you choose. The image is scaled or tiled up to the size of the desktop, and dragging the Eterm around the screen reveals different portions of the image as you move, much like a small viewport window in a ship or submarine does. The effect is especially keen if you open several Eterms in this mode with the same image.</p>
<dt><code>&#8211;shade</code><i> percentage</i></p>
<dd>Shade the background image/transparency by a specified percentage.</p>
<dt><code>&#8211;tint</code><i> mask</i></p>
<dd>
<dt><code>&#8211;tint</code><i> color</i></p>
<dd>Tints the background pixmap (either an image file or the transparent portion can be shaded). The <i>mask</i> is an integer, usually specified in hexadecimal in the form 0x<code>RRGGBB</code>, where <code>RR</code>, <code>GG</code>, and <code>BB</code> are hexadecimal numbers between <code>00</code> and <code>ff</code> (<code>0</code> and <code>255</code> decimal) which represent the brightness of the image&#8217;s red, green, and blue values, respectively. A value of <code>00</code> will mask that color out entirely, while a value of <code>ff</code> will not change that color at all. </p>
<p> You may also specify an X <i>color</i> such as <code>grey75</code> or <code>MidnightBlue</code> or <code>#babb7f</code> instead of a <i>mask</i>.</p>
<dt><code>&#8211;cmod</code> <i>brightness</i> [ <i>contrast</i> [ <i>gamma </i>] ]</p>
<dd>Specifies a color modifier to apply to the image overall. Each of the three values is a number greater than or equal to 0. The numbers can be specified as decimal, octal (if preceded by &quot;0&quot;), or hexadecimal (if preceded by &quot;0x&quot;). A value of 256 (0x100) represents 100%, or &quot;leave that value unchanged.&quot; 0 represents 0%, 512 (0x200) is 200%, etc. However, be aware that overflow can occur with excessively high values. Only the <i>brightness</i> value is required for this option. Keep in mind, though, that you must specify <i>brightness</i> with <i>contrast</i>, and both of these with <i>gamma</i>.</p>
<dt><code>&#8211;cmod-red</code> <i>brightness</i> [ <i>contrast</i> [ <i>gamma </i>] ]</p>
<dd>Same as above, except that the modifier applies to the red values of the image.</p>
<dt><code>&#8211;cmod-green</code> <i>brightness</i> [ <i>contrast</i> [ <i>gamma </i>] ]</p>
<dd>Same as above, except that the modifier applies to the green values of the image.</p>
<dt><code>&#8211;cmod-blue</code> <i>brightness</i> [ <i>contrast</i> [ <i>gamma </i>] ]</p>
<dd>Same as above, except that the modifier applies to the blue values of the image.</p>
<dt><code>-p</code><i> newpath</i><code>, &#8211;path </code><i>newpath</i></p>
<dd>Sets the pic search path. When the <code>&#8211;background-pixmap</code> or other pixmap options are used, this path will be used to find the image.</p>
<dt><code>&#8211;cache</code><i> size</i></p>
<dd>Specify the <i>size</i> in bytes for the Imlib2 cache.</p>
<dt><code>-N</code><i> list</i><code>, &#8211;anim </code><i>list</i></p>
<dd>Specifies an animation list to be use in cycling the background pixmap. The <i>list</i> consists of two or more words. The first word defines the delay, in seconds, between updates of the background. This should be set to a reasonable value to insure that Eterm doesn&#8217;t spend all its time rendering backgrounds. All remaining words specify background images and have the same syntax as the <code>-P</code> option above, including the optional geometry string.</p>
<dt><code>-M</code><i> font</i><code>, &#8211;mfont </code><i>font</i></p>
<dd>Sets the normal multibyte text font to <i>font.</i></p>
<dt><code>&#8211;mfont1</code><i> font</i></p>
<dd>
<dt><code>&#8230;</code></p>
<dd>
<dt><code>&#8211;mfont4</code><i> font</i></p>
<dd>Sets multibyte font X to <i>font.</i></p>
<dt><code>&#8211;mencoding</code><i> encoding</i></p>
<dd>Sets multichar encoding mode (eucj or sjis or euckr)</p>
<dt><code>&#8211;input-method</code><i> method</i></p>
<dd>Sets XIM input method</p>
<dt><code>&#8211;preedit-type</code><i> type</i></p>
<dd>Sets XIM preedit type</p>
<dt><code>-l,</code> &#8211;login-shell</p>
<dd>Makes the new shell a login shell.</p>
<dt><code>-s,</code> &#8211;scrollbar</p>
<dd>Enables the scrollbar. (Default)</p>
<dt><code>-u,</code> &#8211;utmp-logging</p>
<dd>Tries to enable proper utmp logging. For this to work, Eterm probably needs to run setuid or setgid, usually setuid root.</p>
<dt><code>-v,</code> &#8211;visual-bell</p>
<dd>Enables the &quot;visual bell&quot;. Means the window will flash or blink rather than beep.</p>
<dt><code>-H,</code> &#8211;home-on-output</p>
<dd>Jump to bottom on output.</p>
<dt><code>&#8211;home-on-input</code></p>
<dd>Jump to bottom on input.</p>
<dt><code>-q</code>, <code>&#8211;no-input</code></p>
<dd>Keeps Eterm from accepting keyboard input, and keeps the window manager from focusing it. Useful for log tailers and such.</p>
<dt><code>&#8211;scrollbar-right</code></p>
<dd>Display scrollbar on the right hand side.</p>
<dt><code>&#8211;scrollbar-floating</code></p>
<dd>Display the scrollbar without a trough.</p>
<dt><code>&#8211;scrollbar-popup</code></p>
<dd>Display the scrollbar only when the Eterm window is focused.</p>
<dt><code>-x,</code> &#8211;borderless</p>
<dd>This option forces Eterm to have no borders.</p>
<dt><code>-S,</code> &#8211;sticky</p>
<dd>Start Eterm as a sticky window (shows on all desktops)</p>
<dt><code>-m,</code> &#8211;map-alert</p>
<dd>Un-iconify on beep.</p>
<dt><code>-8,</code> &#8211;meta8</p>
<dd>Causes the Meta key to set the 8th bit in the char.</p>
<dt><code>&#8211;double-buffer</code></p>
<dd>Rather than drawing text directly onto the window, this option causes Eterm to allocate an additional pixmap the size of the terminal window into which the background *and* the text are rendered. This pixmap is then set as the window background. Double-buffering uses additional memory in the X server, but it allows Eterm to ignore expose events so redraws are faster.</p>
<dt><code>&#8211;no-cursor</code></p>
<dd>Disables the text cursor.</p>
<dt><code>&#8211;pause</code></p>
<dd>After the child process terminates, Eterm will wait for a keypress before exiting.</p>
<dt><code>&#8211;xterm-select</code></p>
<dd>Duplicate&#8217;s xterm&#8217;s treatment of cutchars. The only real difference is what happens when you double click on a single cutchar between two words. If this option is on, only that single character gets selected. If it is off, that character is selected along with the two words. The latter behavior is useful for double-clicking on the space between someone&#8217;s first and last names, or the @ sign in an e-mail address, etc.</p>
<dt><code>&#8211;select-line</code></p>
<dd>If activated, this option causes a triple click to select the entire line from beginning to end. If off, a triple-click selects just from the current word to the end of the line.</p>
<dt><code>&#8211;select-trailing-spaces</code></p>
<dd>Determines whether or not trailing spaces in a selection are maintained (on) or discarded (off).</p>
<dt><code>&#8211;report-as-keysyms</code></p>
<dd>Reports certain keystrokes as keysyms and modifiers rather than escape sequences. <code>NOTE:</code> This option is intended for use only with programs that support this special Eterm mode. Do not enable it unless you are executing a program which uses this mode.</p>
<dt><code>&#8211;buttonbar</code></p>
<dd>Toggle the display of all buttonbars.</p>
<dt><code>&#8211;resize-gravity</code></p>
<dd>If true, Eterm will automatically detect the nearest corner, and font-change resizes will cause the Eterm window to gravitate toward that corner.</p>
<dt><code>&#8211;overstrike-bold</code></p>
<dd>If true (default), Eterm will simulate a bold font by printing each character twice, offsetting the second pass by one pixel. This makes the characters seem thicker without the need for a special font. You may wish to disable this if you use a specific color for bold.</p>
<dt><code>&#8211;bold-brightens-foreground</code></p>
<dd>If true (default), Eterm will use the &quot;bold&quot; ANSI color attribute to brighten the foreground color by using the high-intensity colors (8 through 15) rather than the low-intensity colors (0 through 7). Note that having a specific color selected for bold will override this.</p>
<dt><code>&#8211;blink-brightens-background</code></p>
<dd>If true (default), Eterm will use the &quot;blink&quot; ANSI color attribute to brighten the background color by using the high-intensity colors (8 through 15) rather than the low-intensity colors (0 through 7).</p>
<dt><code>&#8211;colors-suppress-bold</code></p>
<dd>If true (default), any colored text (that is, any text not rendered using the default foreground color) will not be given any other special treatment for bolding (e.g., bold font or bold overstrike).</p>
<dt><code>&#8211;big-font-key</code><i> keysym</i></p>
<dd>Specify a keysym to increase the font size. Default is Shift and the + key on the keypad. Ctrl-&gt; or Meta-&gt; may also work (if you #define one of the hotkeys in src/feature.h).</p>
<dt><code>&#8211;small-font-key</code><i> keysym</i></p>
<dd>Specify a keysym to decrease the font size. Default is Shift and the &#8211; key on the keypad. Ctrl-&lt; or Meta-&lt; may also work (if you #define one of the hotkeys in src/feature.h).</p>
<dt><code>&#8211;meta-mod</code><i> num</i></p>
<dd>Specify which X modifier (1-5) to treat as the Meta key. See <i><a href="/docs/linux/man/1-xmodmap/">xmodmap</a></i>(1) and the output of <code>xmodmap -pm</code> for more details.</p>
<dt><code>&#8211;alt-mod</code><i> num</i></p>
<dd>Same as <code>&#8211;meta-mod</code>, but for the Alt key.</p>
<dt><code>&#8211;numlock-mod</code><i> num</i></p>
<dd>Same as <code>&#8211;meta-mod</code>, but for the NumLock key.</p>
<dt><code>&#8211;greek-keyboard</code><i> mode</i></p>
<dd>Use Greek keyboard mapping (iso or ibm).</p>
<dt><code>&#8211;app-keypad</code></p>
<dd>Start Eterm in application keypad mode (as opposed to normal keypad mode).</p>
<dt><code>&#8211;app-cursor</code></p>
<dd>Start Eterm in application cursor key mode (as opposed to normal cursor key mode).</p>
<dt><code>-L</code><i> num</i><code>, &#8211;save-lines </code><i>num</i></p>
<dd>Set the number of lines in the scrollback buffer to <i>num.</i></p>
<dt><code>-a</code><i> size</i><code>, &#8211;min-anchor-size </code><i>size</i></p>
<dd>Specifies the minimum size, in pixels high, of the scrollbar anchor. <code>NOTE:</code> This causes abnormal scrolling behavior when combined with large scrollback buffers!</p>
<dt><code>-w</code><i> width</i><code>, &#8211;border-width </code><i>width</i></p>
<dd>Set the window&#8217;s border width to <i>width.</i> The border this controls is the gap between the edge of the X window and the edge of the terminal window; this has nothing to do with the window border&#8217;s your window manager supplies.</p>
<dt><code>&#8211;print-pipe</code><i> pipe</i></p>
<dd>The pipe for the PrintScreen function.</p>
<dt><code>&#8211;cut-chars</code><i> separators</i></p>
<dd>The seperators for double-click selection.</p>
<dt><code>&#8211;finished-title</code><i> title</i></p>
<dd>Specifies the string Eterm should add to its title bar if <code>&#8211;pause</code> is specified and the child process completes.</p>
<dt><code>&#8211;finished-text</code><i> text</i></p>
<dd>Same as above, but displays text in the terminal window.</p>
<dt><code>&#8211;term-name</code><i> TERM</i></p>
<dd>Use <i>TERM</i> for the value $TERM.</p>
<dt><code>&#8211;pipe-name</code><i> pipe</i></p>
<dd>Specifies a named pipe from which to display output. This is useful for systems where syslog output goes to a named pipe, like <code>/dev/xconsole</code> on Debian.</p>
<dt><code>-a </code><i>line</i><code>, &#8211;attribute </code><i>line</i></p>
<dd>This option is used to pass config file attributes on the command line. <i>line</i> should be a single string, so you will almost certainly have to quote it. The first word of <i>line</i> must be the context (see config file section below) which should parse the rest of the <i>line</i>. So, for example, you could specify the foreground color like so: <code>-a &#8216;color foreground blue&#8217;</code>. Or you could add a binding: <code>-a &#8216;actions bind anymod button1 to script exit&#8217;</code>. Note that this option may only be used with config file attributes that are not context-sensitive; i.e., menus and imageclasses cannot be specified using this option.</p>
<dt><code>-C,</code> &#8211;console</p>
<dd>Grab console messages. Depending on your system, Eterm may need to be setuid root to do this.</p>
<dt><code>-e</code><i> command</i><code>, &#8211;exec </code><i>command</i></p>
<dd>Execute <i>command</i> rather than a shell. Forces Eterm mode.</p>
<dt><code>-U</code><i> URL</i><code>, &#8211;url </code><i>URL</i></p>
<dd>Pick up a &quot;screen&quot; session at <i>URL</i> rather than a local (-U &quot;&quot;) one. URLs look like so (<a href="screen://user@host.dom:port/screen_options">screen://user@host.dom:port/screen_options</a>), with all parts optional, defaulting to &quot;<a href="screen://current_user@localhost:22/-RDD">screen://current_user@localhost:22/-RDD</a>&quot;. Forces Escreen mode, overrides &#8211;exec. Note that only screen-options (see &quot;man screen&quot;) are allowed; do not pass a command (with or without arguments) here: to pass a command to the screen-session, use <i>screen [&lt;options&gt;] &lt;command&gt; [&lt;args&gt;]</i> instead.</p>
<dt><code>-Z</code><i> lclport:fw:fwport,delay</i><code>, &#8211;fw </code><i>lclport:fw:fwport,delay</i></p>
<dd>The URL given to -U is in an intranet behind firewall <i>fw</i> so we&#8217;ll build an SSH-tunnel to that firewall (to port 22/SSH, or <i>fwport</i> if given) from our local machine (using any available port-number, or <i>lclport</i> if given). Then, after <i>delay</i> seconds (or a sensible default if not given), we will try to open a screen session on the host behind the firewall using <i>ssh -p localport &#8230; localhost screen</i> cf. <i>ssh -L</i> </p>
</dl>
<h2>Themes</h2>
<p>Eterm is built on the philosophy of Freedom of Choice. Each user should be able to choose the environment in which he or she wishes to exist, and the tools used should support that. In accordance with that philosophy, Eterm is extremely configurable. Eterm supports a concept called &quot;themes,&quot; which should be familiar to users of Enlightenment, icewm, or Microsoft Windows 95/98/NT. The general concept of a theme is a collection of resources that change as many aspects of a programs look and feel as possible. For example, an Enlightenment theme allows you to customize menus, window borders, desktops, icons, iconbars, and everything else about how E looks and feels. </p>
<p> An Eterm theme consists of a primary configuration file, always called &quot;theme.cfg&quot;, residing in a directory bearing the same name as the theme. This directory must be a child of one of the directories specified by CONFIG_SEARCH_PATH in src/feature.h. The theme may also contain additional configuration files referenced by the primary theme.cfg file, as well as pixmaps, menu files, documentation, etc., which are allowable as extensions to the minimum requirement of an Eterm theme. </p>
<p> By convention and default, Eterm themes should be stored under ~/.Eterm/themes/&lt;theme_name&gt;/ or /usr/share/Eterm/themes/&lt;theme_name&gt;. </p>
<p> Eterm now supports the existence of a user configuration file as a suppliment to the theme configuration file. The default name for this file is user.cfg, and it follows the exact same syntax as any other configuration file. It is searched for using the same algorithm used for the theme.cfg file, and any settings in the user.cfg will override any previous values for those settings defined by the theme. Thus, it is recommended that any user.cfg files not be complete config files, but rather only contain those values which the user wishes to explicitly override. </p>
<p> NOTE: If you have a user.cfg file in the Eterm theme directory or in ~/.Eterm/, it will override <code>any</code> previous settings, even if you are running a different theme. For example, if you run the trans theme, but ~/.Eterm/themes/Eterm/user.cfg has a mode line which sets the image mode to &quot;image&quot; rather than &quot;trans,&quot; you will not get transparency. This is why user.cfg files should be kept small and only override settings that you know you want to enforce. If, on the other hand, you were running the trans theme and had a user.cfg file in the trans theme (or in ~/.Eterm/themes/trans/), that user.cfg would be found before the one in the Eterm theme. </p>
<p> Almost all command line options can be enabled/disabled in the theme&#8217;s configuration file (the default is /usr/share/Eterm/themes/Eterm/theme.cfg). The next section contains details on the format and usage of the configuration file. </p>
<h2>Configuration</h2>
<p>Since Eterm 0.9.5 is based on the concept of themes, it is vital that you have a thorough understanding of the previous section before taking on this one. The previous section and this one were written by the same person who wrote the Eterm code which handles options, config files, and themes, so it&#8217;s probably the most authoritative documentation on the subject you&#8217;re going to find. </p>
<p> From here on out, I will assume you&#8217;ve read the above text and know how to change the default value for the theme. It is highly recommended that you have a copy of the Eterm theme config file that comes with Eterm handy while you read this documentation. </p>
<p> Okay, first the general idea. The theme.cfg file is composed of comments and non-comments. Comments begin with a pound sign and continue to the end of the line. Lines of whitespace are also ignored. The rest of the file is the config stuff, which is divided into sections (called &quot;contexts&quot;) and variables (called &quot;attributes&quot;). There are several contexts which are listed below in sections. Each attribute must be inside a certain context to be valid. For instance, while the &quot;foreground&quot; attribute is perfectly acceptable in the color context, it would be rejected if found in, say, the toggles context. This allows for better organization of the config file as well as for multiple contexts to have attributes of the same name (like the <code>scrollbar</code> attributes in the color and toggles section). </p>
<p> Each context must be enclosed in a begin&#8230;end pair that specifies the type of section. The statement &quot;begin toggles&quot; starts the toggles context, and the next &quot;end&quot; statement would terminate it. (You&#8217;ll notice that some &quot;end&quot; statements have the context name after them. This is for readability only; any text after the word &quot;end&quot; is ignored.) </p>
<p> The rest of this section will contain a step-by-step analysis of the config file, including what can go in each section. Note that some attributes (and even entire contexts) may not be available depending on what support was compiled into Eterm by the person who built it. </p>
<dl>
<dt>MAGIC NUMBER</p>
<dd>The first line of the config file must contain a &quot;magic number&quot; type line that lets Eterm verify that it&#8217;s reading an Eterm config file and not something else (like an Enlightenment 0.13 and earlier config file). The line should look like this: </p>
<p> &lt;Eterm-VERSION&gt; </p>
<p> where VERSION is the Eterm version for which the config file is intended. For example, config files written for Eterm 0.9 should have &quot;&lt;Eterm-0.9&gt;&quot; as their first line, followed immediately by a newline.</p>
<dt>COLOR CONTEXT</p>
<dd>This context contains color specifications. With the exception of the terminal colors 0-15, all <i>color</i>s should be either a valid color name or an RGB string as outlined in the <i><a href="/docs/linux/man/7-x11/">X11</a></i>(7) man page. </p>
<dl>
<dd><code>foreground</code><i> color</i></p>
<dl>
<dd>Use <i>color</i> for the foreground (text) color.</dl>
<p> <code>background</code><i> color</i></p>
<dl>
<dd>Use <i>color</i> for the background color.</dl>
<p> <code>cursor</code><i> color</i></p>
<dl>
<dd>Use <i>color</i> for the cursor color.</dl>
<p> <code>cursor_text</code><i> color</i></p>
<dl>
<dd>Use <i>color</i> for the cursor text color.</dl>
<p> <code>pointer</code><i> color</i></p>
<dl>
<dd>Use <i>color</i> for the mouse pointer color.</dl>
<p> <code>video</code> { <code>normal</code> | <code>reverse</code> }</p>
<dl>
<dd><code>normal</code> will not reverse the foreground and background colors. <code>reverse</code> (meaning reverse video) will.</dl>
<p> <code>color</code><i> num</i><i>color</i></p>
<dl>
<dd>Set terminal color <i>num</i> (0-15) to the color name, string, or set of 3 decimal/hex/octal RGB values specified by <i>color</i>.</dl>
<p> <code>color</code> { <code>bd</code> | <code>ul</code> } <i>color</i></p>
<dl>
<dd>Set terminal bold (<code>bd</code>) or underline (<code>ul</code>) color to the color name, string, or set of 3 decimal/hex/octal RGB values specified by <i>color</i>.</dl>
</dl>
<dt>ATTRIBUTES CONTEXT</p>
<dd>This context contains X11 attributes. Most of these are dependent upon the cooperation of the window manager. </p>
<dl>
<dd><code>geometry</code><i> geom</i></p>
<dl>
<dd>Use the geometry string <i>geom</i> to specify the startup geometry. <i>geom</i> should be in the format <i>W</i><code>x</code><i>H+X+Y</i> where <i>W</i> is the width, <i>H</i> is the height, and <i>+X</i> and <i>+Y</i> are the X and Y offsets. If the signs on <i>X</i> and <i>Y</i> are positive, the coordinates are offsets (in pixels) from the left and top, respectively, of the screen. If the signs are negative, the offsets are relative to the right and bottom of the screen, respectively.</dl>
<p> <code>title</code><i> title</i></p>
<dl>
<dd>Use <i>title</i> as the text in the title bar of the Eterm window.</dl>
<p> <code>name</code><i> name</i></p>
<dl>
<dd>Use <i>name</i> as the resource name of the Eterm window.</dl>
<p> <code>iconname</code><i> name</i></p>
<dl>
<dd>Use <i>name</i> as the icon name of the Eterm window icon.</dl>
<p> <code>desktop</code><i> num</i></p>
<dl>
<dd>Start Eterm on desktop <i>num</i>. <code>NOTE</code>: This requires a GNOME-compliant Window Manager. Please see <a rel="nofollow" href="http://www.gnome.org/devel/gnomewm/">http://www.gnome.org/devel/gnomewm/</a> for more information on the <code>_WIN_WORKSPACE</code> property and how to support it.</dl>
<p> <code>scrollbar_type</code><i> type</i></p>
<dl>
<dd>Use a scrollbar with the <i>type</i> style. <i>type</i> can be any of <code>motif</code>, <code>xterm</code>, or <code>next</code>.</dl>
<p> <code>scrollbar_width</code><i> num</i></p>
<dl>
<dd>Use a scrollbar that is <i>num</i> pixels wide.</dl>
<p> <code>font</code><i> num</i><i>font</i><br />
 <code>font bold </code><i>font</i></p>
<dl>
<dd>Set the <i>num</i>th font, or the <code>bold</code> font, to <i>font</i>.</dl>
<p> <code>font default</code><i> num</i></p>
<dl>
<dd>Specifies that the <i>num</i>th font should be considered the &quot;default&quot; font.</dl>
<p> <code>font proportional</code><i> boolean</i></p>
<dl>
<dd>Specifies that the font in use is proportional and requests standard deviation-based character cell spacing. Terminals must use fixed-width character cells to maintain proper columnal alignment, even when proportionally-spaced fonts are in use. Some proportionally-spaced fonts vary greatly between the minimum and maximum character widths. This option chooses a character cell size which is up to two standard deviations above the average character width but will not exceed the maximum width of the largest glyph. Note that characters larger than the chosen cell width will overwrite (or be overwritten by) other characters and may tend to leave pixel droppings. This behavior is an expected side-effect of an imperfect scenario. If you object to this behavior, do not use this option.</dl>
<p> <code>font fx</code><i> effects</i></p>
<dl>
<dd>Specifies the effects to apply to the terminal window font. The value of <i>effects</i> is a single string containing a series of corner/color pairs. These pairs define toward which corner a drop shadow of each character should be made, and what color that shadow will be. The corner is specified first using the following keywords: <code>top_left</code> or <code>tl</code>, <code>top_right</code> or <code>tr</code>, <code>bottom_left</code> or <code>bl</code>, and <code>bottom_right</code> or <code>br</code>. Each corner specifier is then followed by a color. </p>
<p> There are also several shortcuts for doing common effects. You can get a single-color outline by using the keyword <code>outline</code> followed by a color. A single-color drop shadow is also available using the keyword <code>shadow</code> followed by an optional corner specifier (<code>bottom_right</code> being the default) and a color. For a 3-D embossed look, use <code>emboss</code><i> dark_color</i> <i>light_color</i>. The opposite effect, a carved-out look, can be obtained with <code>carved</code><i> dark_color</i> <i>light_color</i>. (Of course, with those last two, the 3-D look will only work if you choose the light and dark colors wisely.) </p>
<p> Finally, for no font effects at all, simply specify the keyword <code>none</code>. </p>
<p> The default value is <code>bottom_right black</code> which yields a black drop shadow, greatly improving the visibility of lightly-colored fonts on top of light spots in a background image. Note that font effects are not active in solid color mode.</dl>
</dl>
<dt>IMAGECLASSES CONTEXT</p>
<dd>This context contains global image attributes. It also provides the parent context for defining images via the &quot;image&quot; context. </p>
<dl>
<dd><code>icon</code><i> filename</i></p>
<dl>
<dd>Use <i>filename</i> as the icon image for the Eterm window. <i>filename</i> can be an absolute path, relative to the current theme, or relative to one of the directories in the <code>path</code> attribute listed below.</dl>
<p> <code>cache</code><i> num</i></p>
<dl>
<dd>Sets the Imlib2 cache size to <i>num</i> bytes. The default is 0.</dl>
<p> <code>path</code><i> directory_list</i></p>
<dl>
<dd>Specifies a colon-delimited list of directories relative to which Eterm should search for image and menu files. The syntax for <i>directory_list</i> is precisely the same as that of the <code>$PATH</code> environment variable in UNIX shells.</dl>
<p> <code>anim</code><i> interval</i><i> images &#8230;</i></p>
<dl>
<dd>Specifies an animation list to be use in cycling the background pixmap. The <i>interval</i> defines the delay, in seconds, between updates of the background. This should be set to a reasonable value to insure that Eterm doesn&#8217;t spend all its time rendering backgrounds. All the <i>images</i> specify background images and have the same syntax as the <code>-P</code> option above, including the optional geometry string.</dl>
</dl>
<dt>IMAGE CONTEXT</p>
<dd>This context defines all the attributes of a particular image. There can be (and usually are) several image contexts per theme, one for each class of image. </p>
<dl>
<dd><code>type</code><i> class</i></p>
<dl>
<dd>Specifies the type, or <i>class</i>, of the image that is going to be defined in that context. This MUST be the first attribute defined in the image context. Valid classes are: <code>background</code>, <code>trough</code>, <code>anchor</code>, <code>up_arrow</code>, <code>down_arrow</code>, <code>left_arrow</code>, <code>right_arrow</code>, <code>menu</code>, <code>menuitem</code>, <code>submenu</code>, <code>button</code>, and <code>buttonbar</code>. Note that the left and right arrows, while valid, don&#8217;t do anything just yet. All the subsequent attributes up to the next <code>type</code> definition will be applied to that image class.</dl>
</dl>
<dl>
<dd><code>mode</code> <i>initial_mode</i> [ <code>allow</code> <i>allowed_modes</i> ]</p>
<dl>
<dd>Specifies the initial mode for this image class as well as the modes which the image class is allowed to use. <i>initial_mode</i> is the mode that the image will have on startup (unless overridden by command-line options. <i>allowed_modes</i> is a list of one or more modes. The image will be prevented from switching to any mode not listed in the <code>allow</code> section. If the <code>allow</code> section is omitted entirely, the image will never be permitted to change from the <i>initial_mode</i>. If no <code>mode</code> line is specified for an image class, the default is equivalent to <code>mode solid allow solid</code>. Valid mode names are <code>image</code> (to use an image), <code>trans</code> (for transparency), <code>viewport</code> (for viewport mode), <code>auto</code> (for auto mode, which requires Enlightenment 0.16 or better), and <code>solid</code> (which is a solid color only).</dl>
</dl>
<dl>
<dd><code>state</code> { <code>normal</code> | <code>selected</code> | <code>clicked</code> | <code>disabled</code> }</p>
<dl>
<dd>This sets the state of the image you are about to define. Up until the next <code>state</code> attribute that is encountered (or until you change types), all attributes will apply to that particular state of the image. You should at minimum define the <code>normal</code> state of the image. It will be used as the default if the attributes for the other states are not specified. However, each image state has self-contained options. Therefore, if you define multiple states for an image class, you must define ALL attributes needed by that state. The sample themes supplied with Eterm demonstrate how to define 1-, 2-, 3-, and 4-state images.</dl>
<p> The above attributes affect the image class as a whole. All remaining attributes in this context affect only the current state of the image class.</dl>
<dl>
<dd><code>color</code><i> fg</i><i>bg</i></p>
<dl>
<dd>Sets the foreground and background colors for this imageclass. The foreground color is used for text, and the background color is used for the object itself. If an invalid color is specified, the default value for <i>fg</i> is white, and the default for <i>bg</i> is black.</dl>
</dl>
<dl>
<dd><code>file</code><i> filename</i></p>
<dl>
<dd>Sets the filename from which to load the image file. This is used for the <code>image</code> mode. If you allow the image mode for your image, don&#8217;t forget to supply an image file! Note that you can also supply an image geometry string here by adding an <code>@</code> symbol and the geometry string to the end of the filename. See below for the syntax of the geometry string. <i>filename</i> must be an absolute path or a path relative to one of the directories in the <code>path</code> attribute. Note that the image is verified and loaded when this attribute is encountered during parsing.</dl>
</dl>
<dl>
<dd><code>geom</code><i> image_geometry</i></p>
<dl>
<dd>Specifies the geometry and geometry-related operations which are to be applied to the image. This attribute only applies to image classes using the <code>image</code> mode. Image geometry is specified as <i>w</i><code>x</code><i>h</i><code>+</code><i>x</i><code>+</code><i>y</i><code>:</code><i>ops</i> where <i>w</i> and <i>h</i> are the horizontal/vertical scaling percentages, <i>x</i> and <i>y</i> are the horizontal/vertical alignment percentages, and <i>ops</i> is a colon-delimited list of operations: <code>tiled</code> (to tile the image), <code>propscaled</code> (for proportional scaling). Note that these operations can be combined for various effects.</dl>
</dl>
<dl>
<dd><code>cmod</code> { <code>image</code> | <code>red</code> | <code>green</code> | <code>blue</code> } <i>brightness</i> [ <i>contrast</i> [ <i>gamma</i> ] ]<br />
 <code>colormod</code> { <code>image</code> | <code>red</code> | <code>green</code> | <code>blue</code> } <i>brightness</i> [ <i>contrast</i> [ <i>gamma</i> ] ]</p>
<dl>
<dd>Specifies a color modifier to apply to the image. The second keyword determines whether the modifier will be applied to the image overall, the red values, the green values, or the blue values. Each of the three parameters is a number greater than or equal to 0. The numbers can be specified as decimal, octal (if preceded by &quot;0&quot;), or hexadecimal (if preceded by &quot;0x&quot;). A value of 256 (0x100) represents 100%, or &quot;leave that value unchanged.&quot; 0 represents 0%, 512 (0x200) is 200%, etc. However, be aware that overflow can occur with excessively high values. Only the <i>brightness</i> value is required for this option. Keep in mind, though, that you must specify <i>brightness</i> with <i>contrast</i>, and both of these with <i>gamma</i>.</dl>
</dl>
<dl>
<dd><code>border</code><i> left right top bottom</i></p>
<dl>
<dd>Specifies that the image has borders which should not be scaled with the rest of the image. This is primarily used for images that have a beveled look, so that the bevel will not end up getting scaled and lose the bevel effect. All four parameter values are in pixels, just like the equivalent options for E themes and Gtk+ pixmap themes.</dl>
</dl>
<dl>
<dd><code>bevel</code> { <code>up</code> | <code>down</code> } <i>left right top bottom</i></p>
<dl>
<dd>Adds a bevel to an image class. This can be done to any image class using the <code>image</code> or <code>trans</code> modes. The parameters are pixel values which represent the width of each edge of the bevel. This is especially useful if you want to use tiled images or transparency for the arrow or anchor scrollbar widgets, or for menus.</dl>
</dl>
<dl>
<dd><code>padding</code><i> left right top bottom</i></p>
<dl>
<dd>This is used only for the <code>submenu</code> image class. It defines the amount of pixels on each side to reserve so that the text will not overwrite part of the image. Works just like the same option in Enlightenment themes.</dl>
</dl>
<dt>MENU CONTEXT</p>
<dd>This context is used to create a menu. There is one instance of this context per menu, and the menus should be defined in submenu-menu order; i.e., any menu that refers to another menu (as its submenu) should be defined after the submenu is defined. Within the menu context, there should be a menuitem subcontext for each menu item (with the exception of the shorthand for separators). </p>
<dl>
<dd><code>title</code><i> menu_title</i></p>
<dl>
<dd>This specifies the title for the menu to be defined. This MUST be the first attribute given after the &quot;begin menu&quot;. The title must be unique amongst all the menus. It may contain spaces, but don&#8217;t forget to enclose it in single or double quotes if it does. Any future references to the menu will use the title.</dl>
</dl>
<dl>
<dd><code>font</code><i> font_name</i></p>
<dl>
<dd>Tells Eterm to use <i>font_name</i> as the font for this menu. If not given, the default terminal font is used.</dl>
</dl>
<dl>
<dd><code>sep</code> or <code>&#8211;</code></p>
<dl>
<dd>These symbols can be used as shorthand to insert a separator into the menu.</dl>
</dl>
<dt>MENUITEM CONTEXT</p>
<dd>This is a subcontext of the menu context which creates a single item for a menu. There can be (and usually are) several menuitem contexts per menu. </p>
<dl>
<dd><code>text</code><i> label</i></p>
<dl>
<dd>This is the text that is displayed for this menuitem. It is left-justified in the menu window. It can have spaces, but enclose <i>label</i> in quotes if it does.</dl>
</dl>
<dl>
<dd><code>rtext</code><i> label</i></p>
<dl>
<dd>This is text which is right-justified next to the menuitem text. This is generally used to show what keystrokes correspond to a particular menu item, like &quot;C-x C-c&quot; for the &quot;Exit&quot; menuitem in an Emacs menu.</dl>
</dl>
<dl>
<dd><code>action</code> { <code>string</code> | <code>echo</code> | <code>submenu</code> | <code>script</code> } <i>param<br />
 </i><code>action separator</code></p>
<dl>
<dd>Specifies the action to occur when the menuitem is chosen. If you specify <code>separator</code>, nothing else is needed. The other action types require a parameter, <i>param</i>. <code>string</code> specifies a string to be sent to Eterm for handling (escape codes, for example). <code>echo</code> specifies a string to be sent to the client program (for sending commands to a shell, or keystrokes to an application like emacs or mutt). If you use either of these action types, <i>param</i> will be parsed for escape codes (, C-, and the like) before being sent. <code>submenu</code> specifies a submenu which should be displayed when this item is selected, and <i>param</i> is the title of the submenu to show. The submenu must have already been defined. The <code>script</code> action type executes the Eterm-builtin script contained in <i>param</i>. See the section below for more details on the builtin Eterm functions allowed for this action type.</dl>
</dl>
<dt>ACTION CONTEXT</p>
<dd>Actions are key or mouse button bindings which activate certain behaviors. Any action that can be triggered through an escape code can be bound to a key or mouse button, with or without modifiers. You can also bind menus to keystrokes or mouse buttons. </p>
<dl>
<dd><code>bind</code> [ <i>modifiers</i> ] { <i>keysym</i> | <i>button</i> } <code>to</code> { <code>string</code> | <code>echo</code> | <code>menu</code> | <code> script </code> } <i>param</i></p>
<dl>
<dd>Binds a <i>keysym</i> or a mouse <i>button</i> to an action. The action syntax follows the keyword <code>to</code> and is identical to the syntax used for menus (see above). There can be any number of <i>modifiers</i> (so long as the combination is reasonable) but only one <i>keysym</i> or <i>button</i>. Valid <i>modifiers</i> are <code>ctrl</code>, <code>shift</code>, <code>lock</code>, <code>mod1</code> through <code>mod5</code>, <code>alt</code>, <code>meta</code>, and <code>anymod</code> (which allows any modifier). If none are given, the keypress must not have modifier keys in use or the action will not be triggered. Use <code>anymod</code> to allow any arbitrary modifier key to be used. The <i>keysym</i> can be given in text (case-sensitive) or as a hex number. <i>button</i>s should be specified as <code>button1</code> through <code>button5</code>. Also note that <code>alt</code> and <code>meta</code> will be equivalent to one or more of <code>mod1</code> through <code>mod5</code>, as well as perhaps each other, based on your modifier settings. You can view these settings using <code>xmodmap -pm</code>. See also the <code>alt_mod</code> and <code>meta_mod</code> options below.</dl>
</dl>
<dt>BUTTON_BAR CONTEXT</p>
<dd>The buttonbar is an addition to Eterm 0.9.1 which allows users to have a fully-customizeable buttonbar at the top or bottom of each terminal window. Buttons on the buttonbar can be used just like menuitems; they can popup menus (like a menubar), or they can activate any other action a menuitem can. </p>
<dl>
<dd><code>font</code><i> font</i></p>
<dl>
<dd>Specifies the font in which button labels will be displayed.</dl>
<p> <code>dock</code> { <code>top</code> | <code>bottom</code> | <code>no</code> }</p>
<dl>
<dd>Specify whether or not to dock the buttonbar, and if so, whether to dock it at the top or the bottom of the Eterm window. Note that only <code>top</code> and <code>bottom</code> are currently enabled.</dl>
<p> <code>visible</code><i> boolean</i></p>
<dl>
<dd>Toggle whether or not this particular buttonbar will be visible on startup.</dl>
<p> <code>button</code> [ <i>text</i> ] [ <code>icon</code> <i>filename</i> ] <code>action</code> { <code>string</code> | <code>echo</code> | <code>menu</code> | <code> script</code> } <i>param</i></p>
<dl>
<dd>Binds an action to a button. The usage of <i>param</i> and the action types work the same here as they do for menuitems. Also note that you may specify some <i>text</i> or an <code>icon</code> or both, but you cannot omit both.</dl>
</dl>
<dt>MULTICHAR CONTEXT</p>
<dd>Behavior for multi-byte fonts and encodings are defined here. This context does not exist by default. </p>
<dl>
<dd><code>encoding</code> { <code>eucj</code> | <code>sjis</code> | <code>euckr</code> | <code>big5</code> | <code>gb</code> | <code>iso-10646</code> }</p>
<dl>
<dd>Specifies the encoding method. Patches to support other encoding methods are encouraged.</dl>
</dl>
<dl>
<dd><code>font</code><i> num</i><i>font</i></p>
<dl>
<dd>Set the <i>num</i>th multichar font to <i>font</i>.</dl>
</dl>
<dt>XIM CONTEXT</p>
<dd>This context controls locale-based behavior. </p>
<dl>
<dd><code>input_method</code><i> input_method</i></p>
<dl>
<dd>Specify your input method program of choice.</dl>
</dl>
<dl>
<dd><code>preedit_type</code> { <code>OverTheSpot</code> | <code>OffTheSpot</code> | <code>Root</code> }</p>
<dl>
<dd>Specify your preedit type of choice.</dl>
</dl>
<dt>ESCREEN CONTEXT</p>
<dd>This context allows for customizations specific to Escreen mode. See the Escreen section below for more details. </p>
<dl>
<dd><code>url</code><i> protocol</i><code>://</code><i>user</i><code>@</code><i>host</i><code>:</code><i>port</i><code>/</code><i>params</i></p>
<dl>
<dd>Connect to (or create) a particular screen session via a URL-type construct. Standard URL rules apply. The <i>protocol</i> should be either <code>screen</code> (the default) or <code>twin</code>. If <i>user</i>, <i>host</i>, and/or <i>port</i> are specified, an ssh connection is made to the remote server using the given login information. The default is to create/attach to a local session. </p>
<p> Any <i>params</i> that are given are passed directly to the underlying protocol and are separated from each other by a plus sign (<code>+</code>).</dl>
</dl>
<dl>
<dd><code>firewall</code><i> localport</i><code>:</code><i>firewall</i><code>:</code><i>remoteport</i></p>
<dl>
<dd>Bounce the connection through a firewall via ssh.</dl>
</dl>
<dl>
<dd><code>delay</code><i> secs</i></p>
<dl>
<dd>Specify the amount of time to wait before sending the screen/twin initialization sequence. This is required to insure that the remote session has been established prior to sending the init sequence.</dl>
</dl>
<dl>
<dd><code>bbar_font</code><i> font</i></p>
<dl>
<dd>Font to use for the Escreen buttonbar. The default is <code>-*-helvetica-medium-r-normal&#8211;10-*-*-*-p-*-iso8859-1</code>.</dl>
</dl>
<dl>
<dd><code>bbar_dock</code> { <code>top</code> | <code>bottom</code> | <code>no</code> }</p>
<dl>
<dd>Dock the Escreen buttonbar as specified. Note that only <code>top</code> and <code>bottom</code> are currently enabled.</dl>
</dl>
<dt>TOGGLES CONTEXT</p>
<dd>This context contains boolean variables which can be toggled on or off. Valid values for the attributes in this section are &quot;yes&quot;, &quot;on&quot;, &quot;1&quot;, and &quot;true&quot; to turn the option on, or &quot;no&quot;, &quot;off&quot;, &quot;0&quot;, or &quot;false&quot; to turn the option off. These values are denoted by <i>boolean</i>. They all default to false unless otherwise noted. </p>
<dl>
<dd><code>map_alert</code><i> boolean</i></p>
<dl>
<dd>If true, Eterm will un-iconify itself when it receives a beep (ASCII 0x07).</dl>
<p> <code>visual_bell</code><i> boolean</i></p>
<dl>
<dd>If true, Eterm will flash rather than sending a beep.</dl>
<p> <code>login_shell</code><i> boolean</i></p>
<dl>
<dd>If true, Eterm will prepend &#8216;-&#8216; to the shell name when calling it. Depending on your shell, this may modify its startup behavior.</dl>
<p> <code>scrollbar</code><i> boolean</i></p>
<dl>
<dd>This turns on and off the display of the scrollbar. Default is on.</dl>
<p> <code>utmp_logging</code><i> boolean</i></p>
<dl>
<dd>If true, Eterm will attempt to make an entry in the utmp file to record the login information. Eterm may need to run privileged to do this.</dl>
<p> <code>meta8</code><i> boolean</i></p>
<dl>
<dd>Toggles the interpretation of the Meta key setting the 8th bit in a character.</dl>
<p> <code>iconic</code><i> boolean</i></p>
<dl>
<dd>If true, Eterm will launch as an icon.</dl>
<p> <code>home_on_output</code><i> boolean</i></p>
<dl>
<dd>Zoom to the bottom of the scrollback buffer on output.</dl>
<p> <code>home_on_input</code><i> boolean</i></p>
<dl>
<dd>Zoom to the bottom of the scrollback buffer on input.</dl>
<p> <code>no_input</code><i> boolean</i></p>
<dl>
<dd>If true, Eterm will not accept any keyboard input and will ask the window manager to not allow it to be focused.</dl>
<p> <code>scrollbar_floating</code><i> boolean</i></p>
<dl>
<dd>If true, the scrollbar will have no trough.</dl>
<p> <code>scrollbar_right</code><i> boolean</i></p>
<dl>
<dd>If true, Eterm will put the scrollbar on the right of the window (default is left).</dl>
<p> <code>scrollbar_popup</code><i> boolean</i></p>
<dl>
<dd>If true, Eterm will hide the scrollbar when the Eterm window loses focus and restore it when focus is regained. Default is to not change the scrollbar state based on focus.</dl>
<p> <code>borderless</code><i> boolean</i></p>
<dl>
<dd>If true, Eterm will run with no window borders. This also means that the window can not be moved or resized. You will want to specify a <code>geometry</code> with this attribute.</dl>
<p> <code>double_buffer</code><i> boolean</i></p>
<dl>
<dd>Rather than drawing text directly onto the window, this causes Eterm to allocate an additional pixmap the size of the terminal window into which the background *and* the text are rendered. This pixmap is then set as the window background. Double-buffering uses additional memory in the X server, but it allows Eterm to ignore expose events so redraws are faster.</dl>
<p> <code>no_cursor</code><i> boolean</i></p>
<dl>
<dd>If true, Eterm will not display a text cursor.</dl>
<p> <code>pause</code><i> boolean</i></p>
<dl>
<dd>After the child process terminates, Eterm will wait for a keypress before exiting.</dl>
<p> <code>xterm_select</code><i> boolean</i></p>
<dl>
<dd>Duplicate&#8217;s xterm&#8217;s treatment of cutchars. The only real difference is what happens when you double click on a single cutchar between two words. If this option is on, only that single character gets selected. If it is off, that character is selected along with the two words. The latter behavior is useful for double-clicking on the space between someone&#8217;s first and last names, or the @ sign in an e-mail address, etc.</dl>
<p> <code>select_line</code><i> boolean</i></p>
<dl>
<dd>If true, this attribute causes a triple click to select the entire line from beginning to end. If false (default), a triple-click selects from the current word to the end of the line.</dl>
<p> <code>select_trailing_spaces</code><i> boolean</i></p>
<dl>
<dd>If true, this attribute causes spaces at the end of a line to be included as part of the selection text when selecting. The default is to strip these trailing spaces.</dl>
<p> <code>report_as_keysyms</code><i> boolean</i></p>
<dl>
<dd>Reports certain keystrokes as keysyms and modifiers rather than escape sequences. <code>NOTE:</code> This option is intended for use only with programs that support this special Eterm mode. Do not enable it unless you are executing a program which uses this mode.</dl>
<p> <code>itrans</code><i> boolean</i><br />
 <code>immotile_trans</code><i> boolean</i></p>
<dl>
<dd>Toggles the immotile transparency optimization for transparent Eterm windows. Note that this does NOT activate transparency; you must still activate &quot;trans&quot; mode for the background image. This option should be used on transparent windows which are shaded or tinted and which do not move around on the desktop much. See the <code>Mon Mar 6 21:11:13 PST 2000</code> ChangeLog entry for a more detailed explanation.</dl>
<p> <code>buttonbar</code><i> boolean</i></p>
<dl>
<dd>Toggle the display of all buttonbars.</dl>
<p> <code>resize_gravity</code><i> boolean</i></p>
<dl>
<dd>If true, Eterm will automatically detect the nearest corner, and font-change resizes will cause the Eterm window to gravitate toward that corner.</dl>
<p> <code>overstrike_bold</code><i> boolean</i></p>
<dl>
<dd>If true (default), Eterm will simulate a bold font by printing each character twice, offsetting the second pass by one pixel. This makes the characters seem thicker without the need for a special font. You may wish to disable this if you use a specific color for bold.</dl>
<p> <code>bold_brightens_foreground</code><i> boolean</i></p>
<dl>
<dd>If true (default), Eterm will use the &quot;bold&quot; ANSI color attribute to brighten the foreground color by using the high-intensity colors (8 through 15) rather than the low-intensity colors (0 through 7). Note that having a specific color selected for bold will override this.</dl>
<p> <code>blink_brightens_background</code><i> boolean</i></p>
<dl>
<dd>If true (default), Eterm will use the &quot;blink&quot; ANSI color attribute to brighten the background color by using the high-intensity colors (8 through 15) rather than the low-intensity colors (0 through 7).</dl>
<p> <code>colors_suppress_bold</code><i> boolean</i></p>
<dl>
<dd>If true (default), any colored text (that is, any text not rendered using the default foreground color) will not be given any other special treatment for bolding (e.g., bold font or bold overstrike).</dl>
<p> <code>sticky</code><i> boolean</i></p>
<dl>
<dd>If true, Eterm will make its window sticky (shows on all desktops).</dl>
</dl>
<dt>KEYBOARD CONTEXT</p>
<dd>This context contains keyboard-related configuration options. </p>
<dl>
<dd><code>smallfont_key</code><i> keysym</i></p>
<dl>
<dd>Specify a keysym to decrease the font size. Default is Shift and the &#8211; key on the keypad. Ctrl-&lt; or Meta-&lt; may also work (if you #define one of the hotkeys in src/feature.h).</dl>
<p> <code>bigfont_key</code><i> keysym</i></p>
<dl>
<dd>Specify a keysym to increase the font size. Default is Shift and the + key on the keypad. Ctrl-&gt; or Meta-&gt; may also work (if you #define one of the hotkeys in src/feature.h).</dl>
<p> <code>keysym</code><i> keysym</i><i>string</i></p>
<dl>
<dd>Define keysym <i>keysym</i> to send <i>string</i> instead of its default. <i>keysym</i> must be between 0xff00 and 0xffff or Eterm will complain.</dl>
<p> <code>meta_mod</code><i> num</i></p>
<dl>
<dd>Specify which X modifier (1-5) to treat as the Meta key. See <i><a href="/docs/linux/man/1-xmodmap/">xmodmap</a></i>(1) and the output of <code>xmodmap -pm</code> for more details.</dl>
<p> <code>alt_mod</code><i> num</i></p>
<dl>
<dd>Same as <code>meta_mod</code>, but for the Alt key.</dl>
<p> <code>numlock_mod</code><i> num</i></p>
<dl>
<dd>Same as <code>meta_mod</code>, but for the NumLock key.</dl>
<p> <code>greek</code><i> boolean</i> { <code>iso</code> | <code>ibm</code> }</p>
<dl>
<dd>Turn on/off greek keyboard support, and set which greek mode to use.</dl>
<p> <code>app_keypad</code><i> boolean</i></p>
<dl>
<dd>Turn on/off application keypad mode on startup.</dl>
<p> <code>app_cursor</code><i> boolean</i></p>
<dl>
<dd>Turn on/off application cursor key mode on startup.</dl>
</dl>
<dt>MISC CONTEXT</p>
<dd>This context contains miscellaneous attributes that really didn&#8217;t belong anywhere else. </p>
<dl>
<dd><code>print_pipe</code><i> command</i></p>
<dl>
<dd>Set the command to which to pipe print requests (printscreen) to <i>command</i>.</dl>
<p> <code>save_lines</code><i> num</i></p>
<dl>
<dd>Set the number of lines in the scrollback buffer to <i>num</i>.</dl>
<p> <code>cut_chars</code><i> string</i></p>
<dl>
<dd>Define the characters used as word delimiters to the characters contained in <i>string</i>.</dl>
<p> <code>min_anchor_size</code><i> num</i></p>
<dl>
<dd>Sets the minimum size, in pixels, of the scrollbar anchor (the part your mouse grabs onto and moves around) to <i>num</i>.</dl>
<p> <code>border_width</code><i> num</i></p>
<dl>
<dd>Sets the width of the border between the text window and the X window to <i>num</i>.</dl>
<p> <code>line_space</code><i> num</i></p>
<dl>
<dd>Put <i>num</i> pixels&#8217; worth of space between each row of the terminal window.</dl>
<p> <code>finished_title</code><i> title</i></p>
<dl>
<dd>Specifies that <i>title</i> should be displayed in the title bar of a paused Eterm when the child process has completed.</dl>
<p> <code>finished_text</code><i> text</i></p>
<dl>
<dd>Specifies that <i>text</i> should be displayed in the terminal window of a paused Eterm when the child process has completed.</dl>
<p> <code>term_name</code><i> name</i></p>
<dl>
<dd>Use <i>name</i> as the <code>$TERM</code> environment variable, which controls which termcap/terminfo entry gets used. The default is <code>Eterm</code>.</dl>
<p> <code>exec</code><i> command</i></p>
<dl>
<dd>Rather than executing a shell, this will cause Eterm to spawn <i>command</i> as its child process. You can only have one of these!</dl>
</dl>
<dt>BUILT-IN FUNCTIONS</p>
<dd>Eterm has a set of built-in functions which are available in config files. Each one accepts zero or more parameters and outputs a series of zero or more words. &quot;Words&quot; are defined in shell terms; i.e., words are separated by whitespace, and single or double quotes can be used to encapsulate words which contain whitespace themselves. You also employ backquotes to execute a command whose output can become part of the config file itself or can be passed to a built-in function as its parameter list. Built-in functions and backquotes may be used anywhere their output would be valid. Built-in functions are prefixed with the <code>%</code> character. </p>
<dl>
<dd><code>%appname()</code></p>
<dl>
<dd>Returns the application name, a hyphen, and the version number. Currently this is the string <code>Eterm-0.9.5</code>.</dl>
<p> <code>%exec(</code><i>command</i><code>)</code></p>
<dl>
<dd>Executes <i>command</i> and returns the result. Basically it&#8217;s exactly like using backquotes.</dl>
<p> <code>%get(</code><i>variable</i><code>)</code></p>
<dl>
<dd>Retrieve the value of a config file variable. Refer to the <code>%put()</code> function below.</dl>
<p> <code>%put(</code><i>variable value</i><code>)</code></p>
<dl>
<dd>Create a config variable named <i>variable</i> and assign it the value of <i>value</i>. The value can then subsequently be retrieved using <code>%get(</code><i>variable</i><code>)</code></dl>
<p> <code>%random(</code><i>params</i><code>)</code></p>
<dl>
<dd>This function randomly chooses one of the words which compose <i>params</i> and returns that. The default themes that come with Eterm use this function to choose random backgrounds, but backgrounds aren&#8217;t the only things that can be randomized with this function. You can randomize anything&#8230;colors, toggles, fonts, tinting, etc.</dl>
<p> <code>%version()</code></p>
<dl>
<dd>Returns the version number. Currently this is the string <code>0.9.5</code>.</dl>
</dl>
<dt>PREPROCESSING</p>
<dd>Eterm supports the <code>%include</code><i> file</i> directive to allow for separation of the configuration information into multiple files. Eterm will load and parse <i>file</i> just like any other config file, but will treat its contents as if they replaced the directive itself. </p>
<p> You may also request that the config file be run through an external preprocessor (such as m4 or cpp) before Eterm reads it. This is done via the <code>%preproc</code><i> command</i> directive. You may specify anything you like for <i>command</i> so long as it accepts input on STDIN and sends output to STDOUT. See the <code>menus.cfg</code> file in the default <code>chooser</code> theme for an example. </p>
<dt>SCRIPT FUNCTIONS</p>
<dd>One of the action types which can be bound to keypresses, mouse buttons, menuitems, or buttonbar buttons is a <code>script</code>. The script must be a single word (i.e., containing no spaces or enclosed in quotes) and consists of one or more calls to the script functions below. Each call is separated from the next by a semicolon (<code>;</code>). Function parameters are enclosed in parentheses; the parentheses are optional if no parameters are to be passed. Commas and/or whitespace separate parameters from each other. </p>
<dl>
<dd><code>copy(</code><i>buffer</i><code>)</code></p>
<dl>
<dd>Copies the current selection to the specified clipboard or cut buffer. <i>buffer</i> is either a number <code>0</code>&#8211;<code>7</code>, in which case the selection is copied to the cut buffer specified, or one of the words <code>clipboard</code>, <code>primary</code>, or <code>secondary</code> (or any initial substring thereof), in which case the selection is copied to the specified clipboard. You may omit <i>buffer</i>, in which case the default buffer is <code>primary</code> (XA_PRIMARY in Xlib-speak).</dl>
<p> <code>echo(</code><i>string</i><code>)</code></p>
<dl>
<dd>Send the specified <i>string</i> to the subcommand. Exactly equivalent to the <code>echo</code> action.</dl>
<p> <code>es_display(</code><i>cmd</i><code>, </code><i>params</i><code>)</code><br />
 Aliases: <code>es_disp</code></p>
<dl>
<dd>This is a master function which permits manipulation of Escreen displays through the use of a series of subcommands. The specified <i>cmd</i> determines what, if any, <i>params</i> are permitted. Available subcommands are:</p>
<dl>
<dd><code>goto</code> &#8211; Switch to the specified display (0-9)<br />
 <code>prev</code> &#8211; Switch to the previous display<br />
 <code>next</code> &#8211; Switch to the next display<br />
 <code>toggle</code> &#8211; Toggle display<br />
 <code>new</code> &#8211; Create a new display. A name for the new display may be passed as a parameter, or <code>ask</code> to prompt the user for the name.<br />
 <code>rename</code> &#8211; Change the name of the current display. A name for the new display may be passed as a parameter, or <code>ask</code> to prompt the user for the name.<br />
 <code>kill</code> &#8211; Terminate the current (or specified) display.<br />
 <code>watch</code> &#8211; Toggle monitoring of the current/specified display for activity.<br />
 <code>scrollback</code> &#8211; View the scrollback for the current/specified display.</dl>
</dl>
<p> <code>es_region(</code><i>cmd</i><code>, </code><i>params</i><code>)</code><br />
 Aliases: <code>es_reg es_win es_window</code></p>
<dl>
<dd>This is a master function which permits manipulation of Escreen display regions through the use of a series of subcommands. The specified <i>cmd</i> determines what, if any, <i>params</i> are permitted. Available subcommands are:</p>
<dl>
<dd><code>goto</code> &#8211; Switch to the specified region (0-9)<br />
 <code>prev</code> &#8211; Switch to the previous region<br />
 <code>next</code> &#8211; Switch to the next region<br />
 <code>toggle</code> &#8211; Toggle region<br />
 <code>new</code> &#8211; Create a new region. A name for the new region may be passed as a parameter, or <code>ask</code> to prompt the user for the name.<br />
 <code>rename</code> &#8211; Change the name of the current region. A name for the new region may be passed as a parameter, or <code>ask</code> to prompt the user for the name.<br />
 <code>kill</code> &#8211; Terminate the current (or specified) region.<br />
 <code>only</code> &#8211; Maximize the current/specified region to the full display.<br />
 <code>watch</code> &#8211; Toggle monitoring of the current/specified region for activity.<br />
 <code>scrollback</code> &#8211; View the scrollback for the current/specified region.</dl>
</dl>
<p> <code>es_statement(</code><i>statement</i><code>)</code></p>
<dl>
<dd>Execute an Escreen (screen/twin) command directly.</dl>
<p> <code>es_reset()</code><br />
 Aliases: <code>es_rst</code></p>
<dl>
<dd>Reset the Escreen session</dl>
<p> <code>exec_dialog(</code><i>command</i><code>)</code></p>
<dl>
<dd>The same as <code>exec</code>/<code>spawn</code>, but this function presents the user with a dialog box in which she can edit/confirm the command to be run and specify additional parameters if needed.</dl>
<p> <code>exit(</code><i>message</i><code>)</code><br />
 <code>exit(</code><i>code</i><code>)</code><br />
 Aliases: <code>die quit</code></p>
<dl>
<dd>Exit Eterm with an optional <i>message</i> or an integer return <i>code</i>. Either parameter may be specified, but not both. If neither is specified, a <i>code</i> of <code>0</code> (zero) is the default.</dl>
<p> <code>kill(</code><i>signal</i><code>)</code></p>
<dl>
<dd>Sends the specified signal to Eterm&#8217;s primary child process (either your shell, or whatever you specify for Eterm to execute). For the time being, <i>signal</i> must be numeric. <code>SIGTERM</code> is the default if <i>signal</i> is omitted.</dl>
<p> <code>msgbox(</code><i>message</i><code>)</code></p>
<dl>
<dd>Displays a small dialog box containing <i>message</i> and waits for a keypress before continuing.</dl>
<p> <code>nop()</code></p>
<dl>
<dd>Does absolutely nothing except waste time. :-)</dl>
<p> <code>paste(</code><i>buffer</i><code>)</code></p>
<dl>
<dd>Pastes the contents of the specified clipboard or cut buffer into the terminal window. <i>buffer</i> is either a number <code>0</code>&#8211;<code>7</code>, in which case the selection is pasted from the cut buffer specified, or one of the words <code>clipboard</code>, <code>primary</code>, or <code>secondary</code> (or any initial substring thereof), in which case the contents of the specified clipboard are pasted. You may omit <i>buffer</i>, in which case the default buffer is <code>primary</code> (XA_PRIMARY in Xlib-speak).</dl>
<p> <code>save(</code><i>type</i><code>, </code><i>filename</i><code>)</code></p>
<dl>
<dd>Save the current theme/user configuration. <i>type</i> can be either <code>user</code> or <code>theme</code>; the default is <code>user</code>. <i>filename</i> is the file to which the settings should be saved. It may contain a path which is either absolute or relative to the theme directory. The default filename for <code>user</code> is <code>user.cfg</code>, and the default filename for <code>theme</code> is <code>theme.cfg</code>.</dl>
<p> <code>save_buff(</code><i>filename</i><code>)</code></p>
<dl>
<dd>Dumps the contents of the scrollback buffer to the specified file.</dl>
<p> <code>scroll(</code><i>n</i><code>)</code></p>
<dl>
<dd>Scrolls backward or forward in the scrollback buffer. <i>n</i> is a floating point number followed by an optional unit specifier. The unit specifier is one of: <code>lines</code> or <code>l</code>; <code>pages</code> or <code>p</code>; or <code>buffers</code> or <code>b</code>. The floating point number may be separated from the unit specifier by whitespace or a comma, but it is not required. The floating point number should be positive to scroll down (forward) and negative to scroll up (backward). For example, the key sequence Shift-PgUp is equivalent to <code>scroll(-1p)</code>. You may also specify fractional quantities, such as <code>scroll(0.5p)</code> to scroll down half a page. The default unit if not specified is <code>lines</code>.</dl>
<p> <code>search(</code><i>str</i><code>)</code></p>
<dl>
<dd>Presents a dialog box into which the user may enter a search term. The default value is set to <i>str</i>. All occurances of the specified search string are highlighted in the scrollback buffer, and Eterm jumps back to the most recent one. Searching again with the same keyword will clear the previous highlighting.</dl>
<p> <code>spawn(</code><i>command</i><code>)</code><br />
 Aliases: <code>exec</code></p>
<dl>
<dd>Spawns a secondary child process to execute <i>command</i>, or <code>Eterm</code> if no value is passed.</dl>
<p> <code>string(</code><i>string</i><code>)</code></p>
<dl>
<dd>The specified <i>string</i> is parsed via Eterm. This is exactly identical to the <code>string</code> action.</dl>
</dl>
</dl>
<h2>Escreen</h2>
<p>Escreen is a screen/twin interface layer which allows Eterm to interoperate with GNU <code>screen</code> and with Massimiliano Ghilardi&#8217;s <code>twin</code> software. This allows Eterm to support multiple subshell sessions within a single window. On the surface, this feature works similarly to the &quot;tabbed&quot; sessions offered by programs like <code>konsole</code> and <code>multi-gnome-terminal</code>. However, Escreen has the advantage of being an interface to existing software, thus providing additional capabilities like multiple regions per display, detach/reattach capability, seamless remote session support, firewall support, and more. </p>
<p> Escreen support is still somewhat experimental and is thus not compiled into Eterm by default. To enable it, you must compile with <code>&#8211;enable-escreen</code> and/or <code>&#8211;enable-etwin</code> (depending on whether you have screen, twin, or both). If you installed from a package, you can use <code>Eterm &#8211;version</code> and check for either <code>+ESCREEN</code> (enabled) or <code>-ESCREEN</code> (disabled). </p>
<p> For best results, if you wish to use Escreen mode, do so by invoking Eterm with the Escreen theme (<code>Eterm -t Escreen</code>). This theme supplies default key bindings, the basic Escreen menu, color definitions, etc. for use by the Escreen engine. Most importantly, it supplies the required <code>url</code> parameter in order to invoke Escreen mode. </p>
<p> Consult the README.Escreen file for more in-depth discussion of Escreen mode. </p>
<h2>Authors</h2>
<p>Michael Jennings (mej [at] eterm.org) </p>
<h2>URL(s)</h2>
<p>Eterm Home Page &#8212; <a rel="nofollow" href="http://www.eterm.org/">http://www.eterm.org/</a><br />
 Author&#8217;s Home Page &#8212; <a rel="nofollow" href="http://www.kainx.org/">http://www.kainx.org/</a></p>
