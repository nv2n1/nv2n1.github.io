---
title: "setterm(1)"
name: "setterm"
section: "1"
letter: "s"
url: "/docs/linux/man/1-setterm/"
description: "setterm – set terminal attributes"
---

<h2 class="name">NAME</h2>
<p> setterm &#8211; set terminal attributes </p>
<h2>SYNOPSIS</h2>
<p> <code>setterm</code> [options]</p>
<h2>DESCRIPTION</h2>
<p> <code>setterm</code> writes to standard output a character string that will invoke the specified terminal capabilities. Where possible <i>terminfo</i> is consulted to find the string to use. Some options however (marked &quot;virtual consoles only&quot; below) do not correspond to a <code><a href="/docs/linux/man/5-terminfo/">terminfo</a></code>(5) capability. In this case, if the terminal type is &quot;con&quot; or &quot;linux&quot; the string that invokes the specified capabilities on the PC Minix virtual console driver is output. Options that are not implemented by the terminal are ignored.</p>
<h2>OPTIONS</h2>
<p> For boolean options (<code>on</code> or <code>off</code>), the default is <code>on</code>. </p>
<p> Below, an <i>8-color</i> can be <code>black</code>, <code>red</code>, <code>green</code>, <code>yellow</code>, <code>blue</code>, <code>magenta</code>, <code>cyan</code>, or <code>white</code>. </p>
<p> A <i>16-color</i> can be an <i>8-color</i>, or <code>grey</code>, or <code>bright</code> followed by <code>red</code>, <code>green</code>, <code>yellow</code>, <code>blue</code>, <code>magenta</code>, <code>cyan</code>, or <code>white</code>. </p>
<p> The various color options may be set independently, at least on virtual consoles, though the results of setting multiple modes (for example, <code>&#8211;underline</code> and <code>&#8211;half-bright</code>) are hardware-dependent. </p>
<p> The optional arguments require &#8216;=&#8217; (equals sign) and not space between the option and the argument. For example &#8211;option=argument. </p>
<p> <code>&#8211;appcursorkeys</code> on|off</p>
<dl>
<dt>
<dd> Sets Cursor Key Application Mode on or off. When on, ESC O A, ESC O B, etc. will be sent for the cursor keys instead of ESC [ A, ESC [ B, etc. See the <i>vi and Cursor-Keys</i> section of the <i>Text-Terminal-HOWTO</i> for how this can cause problems for <code>vi</code> users. Virtual consoles only.</dl>
<p> <code>&#8211;append</code> <i>console_number</i></p>
<dl>
<dt>
<dd> Like <code>&#8211;dump</code>, but appends to the snapshot file instead of overwriting it. Only works if no <code>&#8211;dump</code> options are given.</dl>
<p> <code>&#8211;background</code> <i>8-color</i>|default</p>
<dl>
<dt>
<dd> Sets the background text color.</dl>
<p> <code>&#8211;blank</code>[=0-60|force|poke]</p>
<dl>
<dt>
<dd> Sets the interval of inactivity, in minutes, after which the screen will be automatically blanked (using APM if available). Without an argument, it gets the blank status (returns which vt was blanked, or zero for an unblanked vt). Virtual consoles only. </p>
<p> The <code>force</code> argument keeps the screen blank even if a key is pressed. </p>
<p> The <code>poke</code> argument unblanks the screen.</dl>
<p> <code>&#8211;bfreq</code>[=<i>number</i>]</p>
<dl>
<dt>
<dd> Sets the bell frequency in Hertz. Without an argument, it defaults to <code>0</code>. Virtual consoles only.</dl>
<p> <code>&#8211;blength</code>[=0-2000]</p>
<dl>
<dt>
<dd> Sets the bell duration in milliseconds. Without an argument, it defaults to <code>0</code>. Virtual consoles only.</dl>
<p> <code>&#8211;blink</code> on|off</p>
<dl>
<dt>
<dd> Turns blink mode on or off. Except on a virtual console, <code>&#8211;blink off</code> turns off all attributes (bold, half-brightness, blink, reverse).</dl>
<p> <code>&#8211;bold</code> on|off</p>
<dl>
<dt>
<dd> urns bold (extra bright) mode on or off. Except on a virtual console, <code>&#8211;bold off</code> turns off all attributes (bold, half-brightness, blink, reverse).</dl>
<p> <code>&#8211;clear</code>[=all|rest]</p>
<dl>
<dt>
<dd> Without an argument or with the argument <code>all</code>, the entire screen is cleared and the cursor is set to the home position, just like <code><a href="/docs/linux/man/1-clear/">clear</a></code>(1) does. With the argument <code>rest</code>, the screen is cleared from the current cursor position to the end.</dl>
<p> <code>&#8211;clrtabs</code>[=<i>tab1 tab2 tab3</i> &#8230;]</p>
<dl>
<dt>
<dd> Clears tab stops from the given horizontal cursor positions, in the range <code>1-160</code>. Without arguments, it clears all tab stops. Virtual consoles only.</dl>
<p> <code>&#8211;cursor</code> on|off</p>
<dl>
<dt>
<dd> Turns the terminal&#8217;s cursor on or off.</dl>
<p> <code>&#8211;default</code></p>
<dl>
<dt>
<dd> Sets the terminal&#8217;s rendering options to the default values.</dl>
<p> <code>&#8211;dump</code>[=<i>console_number</i>]</p>
<dl>
<dt>
<dd> Writes a snapshot of the virtual console with the given number to the file specified with the <code>&#8211;file</code> option, overwriting its contents; the default is <i>screen.dump</i>. Without an argument, it dumps the current virtual console. This overrides <code>&#8211;append</code>.</dl>
<p> <code>&#8211;file</code> <i>filename</i></p>
<dl>
<dt>
<dd> Sets the snapshot file name for any <code>&#8211;dump</code> or <code>&#8211;append</code> options on the same command line. If this option is not present, the default is <i>screen.dump</i> in the current directory. A path name that exceeds the system maximum will be truncated, see <code>PATH_MAX</code> from <i>linux/limits.h</i> for the value.</dl>
<p> <code>&#8211;foreground</code> <i>8-color</i>|default</p>
<dl>
<dt>
<dd> Sets the foreground text color.</dl>
<p> <code>&#8211;half-bright</code> on|off</p>
<dl>
<dt>
<dd> Turns dim (half-brightness) mode on or off. Except on a virtual console, <code>&#8211;half-bright off</code> turns off all attributes (bold, half-brightness, blink, reverse).</dl>
<p> <code>&#8211;hbcolor</code> [bright] <i>16-color</i></p>
<dl>
<dt>
<dd> Sets the color for half-bright characters.</dl>
<p> <code>&#8211;initialize</code></p>
<dl>
<dt>
<dd> Displays the terminal initialization string, which typically sets the terminal&#8217;s rendering options, and other attributes to the default values.</dl>
<p> <code>&#8211;inversescreen</code> on|off</p>
<dl>
<dt>
<dd> Swaps foreground and background colors for the whole screen.</dl>
<p> <code>&#8211;linewrap</code> on|off</p>
<dl>
<dt>
<dd> Makes the terminal continue on a new line when a line is full.</dl>
<p> <code>&#8211;msg</code> on|off</p>
<dl>
<dt>
<dd> Enables or disables the sending of kernel <code>printk</code>() messages to the console. Virtual consoles only.</dl>
<p> <code>&#8211;msglevel</code> 0-8</p>
<dl>
<dt>
<dd> Sets the console logging level for kernel <code>printk()</code> messages. All messages strictly more important than this will be printed, so a logging level of <code>0</code> has the same effect as <code>&#8211;msg on</code> and a logging level of <code>8</code> will print all kernel messages. <code><a href="/docs/linux/man/8-klogd/">klogd</a></code>(8) may be a more convenient interface to the logging of kernel messages. </p>
<p> Virtual consoles only.</dl>
<p> <code>&#8211;powerdown</code>[=0-60]</p>
<dl>
<dt>
<dd> Sets the VESA powerdown interval in minutes. Without an argument, it defaults to <code>0</code> (disable powerdown). If the console is blanked or the monitor is in suspend mode, then the monitor will go into vsync suspend mode or powerdown mode respectively after this period of time has elapsed.</dl>
<p> <code>&#8211;powersave</code> <i>mode</i></p>
<dl>
<dt>
<dd> Valid values for <i>mode</i> are: </p>
<p> <code>vsync|on</code></p>
<dl>
<dt>
<dd> Puts the monitor into VESA vsync suspend mode.</dl>
<p> <code>hsync</code></p>
<dl>
<dt>
<dd> Puts the monitor into VESA hsync suspend mode.</dl>
<p> <code>powerdown</code></p>
<dl>
<dt>
<dd> Puts the monitor into VESA powerdown mode.</dl>
<p> <code>off</code></p>
<dl>
<dt>
<dd> Turns monitor VESA powersaving features.</dl>
</dl>
<p> <code>&#8211;regtabs</code>[=1-160]</p>
<dl>
<dt>
<dd> Clears all tab stops, then sets a regular tab stop pattern, with one tab every specified number of positions. Without an argument, it defaults to <code>8</code>. Virtual consoles only.</dl>
<p> <code>&#8211;repeat</code> on|off</p>
<dl>
<dt>
<dd> Turns keyboard repeat on or off. Virtual consoles only.</dl>
<p> <code>&#8211;reset</code></p>
<dl>
<dt>
<dd> Displays the terminal reset string, which typically resets the terminal to its power-on state.</dl>
<p> <code>&#8211;resize</code></p>
<dl>
<dt>
<dd> Reset terminal size by assessing maximum row and column. This is useful when actual geometry and kernel terminal driver are not in sync. Most notable use case is with serial consoles, that do not use <code><a href="//www.systutorials.com/docs/linux/man/3p-ioctl/">ioctl</a></code>(3p) but just byte streams and breaks.</dl>
<p> <code>&#8211;reverse</code> on|off</p>
<dl>
<dt>
<dd> Turns reverse video mode on or off. Except on a virtual console, <code>&#8211;reverse off</code> turns off all attributes (bold, half-brightness, blink, reverse).</dl>
<p> <code>&#8211;store</code></p>
<dl>
<dt>
<dd> Stores the terminal&#8217;s current rendering options (foreground and background colors) as the values to be used at reset-to-default. Virtual consoles only.</dl>
<p> <code>&#8211;tabs</code>[=<i>tab1 tab2 tab3</i> &#8230;]</p>
<dl>
<dt>
<dd> Sets tab stops at the given horizontal cursor positions, in the range <code>1-160</code>. Without arguments, it shows the current tab stop settings.</dl>
<p> <code>&#8211;term</code> <i>terminal_name</i></p>
<dl>
<dt>
<dd> Overrides the <code>TERM</code> environment variable.</dl>
<p> <code>&#8211;ulcolor</code> [bright] <i>16-color</i></p>
<dl>
<dt>
<dd> Sets the color for underlined characters. Virtual consoles only.</dl>
<p> <code>&#8211;underline</code> on|off</p>
<dl>
<dt>
<dd> Turns underline mode on or off.</dl>
<p> <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Displays version information and exits.</dl>
<p> <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Displays a help text and exits.</dl>
<h2>COMPATIBILITY</h2>
<p> Since version 2.25 <code>setterm</code> has support for long options with two hyphens, for example <code>&#8211;help</code>, beside the historical long options with a single hyphen, for example <code>-help</code>. In scripts it is better to use the backward-compatible single hyphen rather than the double hyphen. Currently there are no plans nor good reasons to discontinue single-hyphen compatibility.</p>
<h2>BUGS</h2>
<p> Differences between the Minix and Linux versions are not documented.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-stty/">stty</a></code>(1), <code><a href="/docs/linux/man/1-tput/">tput</a></code>(1), <code><a href="/docs/linux/man/4-tty/">tty</a></code>(4), <code><a href="/docs/linux/man/5-terminfo/">terminfo</a></code>(5)</p>
<h2>REPORTING BUGS</h2>
<p> For bug reports, use the issue tracker at <i></i> &lt;<a rel="nofollow" href="https://github.com/karelzak/util-linux/issues">https://github.com/karelzak/util-linux/issues</a>&gt;.</p>
<h2>AVAILABILITY</h2>
<p> The <code>setterm</code> command is part of the util-linux package which can be downloaded from <i>Linux Kernel Archive</i> &lt;<a rel="nofollow" href="https://www.kernel.org/pub/linux/utils/util-linux/">https://www.kernel.org/pub/linux/utils/util-linux/</a>&gt;. </p>
<h2>Index</h2>
