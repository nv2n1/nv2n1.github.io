---
title: "terminal-colors-d(5)"
name: "terminal-colors-d"
section: "5"
letter: "t"
url: "/docs/linux/man/5-terminal-colors-d/"
description: "terminal-colors.d – configure output colorization for various utilities"
---

<p>terminal-colors.d &#8211; configure output colorization for various utilities</p>
<h2>Synopsis</h2>
<p>/etc/terminal-colors.d/<i>[[name][@term].][type]</i></p>
<h2>Description</h2>
<p>Files in this directory determine the default behavior for utilities when coloring output. </p>
<p> The <i>name</i> is a utility name. The name is optional and when none is specified then the file is used for all unspecified utilities. </p>
<p> The <i>term</i> is a terminal identifier (the TERM environment variable). The terminal identifier is optional and when none is specified then the file is used for all unspecified terminals. </p>
<p> The <i>type</i> is a file type. Supported file types are: </p>
<p> <code>disable</code></p>
<dl>
<dd>Turns off output colorization for all compatible utilities.</dl>
<p> <code>enable</code></p>
<dl>
<dd>Turns on output colorization; any matching <code>disable</code> files are ignored.</dl>
<p> <code>scheme</code></p>
<dl>
<dd>Specifies colors used for output. The file format may be specific to the utility, the default format is described below.</dl>
<p> If there are more files that match for a utility, then the file with the more specific filename wins. For example, the filename &quot;@xterm.scheme&quot; has less priority than &quot;dmesg [at] xterm.scheme&quot;. The lowest priority are those files without a utility name and terminal identifier (e.g., &quot;disable&quot;). </p>
<p> The user-specific <i>$XDG_CONFIG_HOME/terminal-colors.d</i> or <i>$HOME/.config/terminal-colors.d</i> overrides the global setting.</p>
<h2>Default Scheme Files Format</h2>
<p>The following statement is recognized:</p>
<dl>
<dd><code>name color-sequence</code>
</dl>
<p> The <code>name</code> is a logical name of color sequence (for example &quot;error&quot;). The names are specific to the utilities. For more details always see the COLORS section in the man page for the utility. </p>
<p> The <code>color-sequence</code> is a color name, ASCII color sequences or escape sequences.</p>
<h3>Color names</h3>
<p>black, blink, blue, bold, brown, cyan, darkgray, gray, green, halfbright, lightblue, lightcyan, lightgray, lightgreen, lightmagenta, lightred, magenta, red, reset, reverse, and yellow.</p>
<h3>ANSI color sequences</h3>
<p>The color sequences are composed of sequences of numbers separated by semicolons. The most common codes are:</p>
<dl>
<dd>
<table BORDER>
<tr VALIGN=top>
<td>
<p> 0 </td>
<td>
<p> to restore default color
</td>
</tr>
<tr VALIGN=top>
<td>
<p> 1 </td>
<td>
<p> for brighter colors
</td>
</tr>
<tr VALIGN=top>
<td>
<p> 4 </td>
<td>
<p> for underlined text
</td>
</tr>
<tr VALIGN=top>
<td>
<p> 5 </td>
<td>
<p> for flashing text
</td>
</tr>
<tr VALIGN=top>
<td>
<p> 30 </td>
<td>
<p> for black foreground
</td>
</tr>
<tr VALIGN=top>
<td>
<p> 31 </td>
<td>
<p> for red foreground
</td>
</tr>
<tr VALIGN=top>
<td>
<p> 32 </td>
<td>
<p> for green foreground
</td>
</tr>
<tr VALIGN=top>
<td>
<p> 33 </td>
<td>
<p> for yellow (or brown) foreground
</td>
</tr>
<tr VALIGN=top>
<td>
<p> 34 </td>
<td>
<p> for blue foreground
</td>
</tr>
<tr VALIGN=top>
<td>
<p> 35 </td>
<td>
<p> for purple foreground
</td>
</tr>
<tr VALIGN=top>
<td>
<p> 36 </td>
<td>
<p> for cyan foreground
</td>
</tr>
<tr VALIGN=top>
<td>
<p> 37 </td>
<td>
<p> for white (or gray) foreground
</td>
</tr>
<tr VALIGN=top>
<td>
<p> 40 </td>
<td>
<p> for black background
</td>
</tr>
<tr VALIGN=top>
<td>
<p> 41 </td>
<td>
<p> for red background
</td>
</tr>
<tr VALIGN=top>
<td>
<p> 42 </td>
<td>
<p> for green background
</td>
</tr>
<tr VALIGN=top>
<td>
<p> 43 </td>
<td>
<p> for yellow (or brown) background
</td>
</tr>
<tr VALIGN=top>
<td>
<p> 44 </td>
<td>
<p> for blue background
</td>
</tr>
<tr VALIGN=top>
<td>
<p> 45 </td>
<td>
<p> for purple background
</td>
</tr>
<tr VALIGN=top>
<td>
<p> 46 </td>
<td>
<p> for cyan background
</td>
</tr>
<tr VALIGN=top>
<td>
<p> 47 </td>
<td>
<p> for white (or gray) background
</td>
</tr>
</table>
</dl>
<h3>Escape sequences</h3>
<p>To specify control or blank characters in the color sequences, C-style \-escaped notation can be used:</p>
<dl>
<dd>
<table BORDER>
<tr VALIGN=top>
<td>
<p> <code></code> </td>
<td>
<p> Bell (ASCII 7)
</td>
</tr>
<tr VALIGN=top>
<td>
<p> <code></code> </td>
<td>
<p> Backspace (ASCII 8)
</td>
</tr>
<tr VALIGN=top>
<td>
<p> <code></code> </td>
<td>
<p> Escape (ASCII 27)
</td>
</tr>
<tr VALIGN=top>
<td>
<p> <code></code> </td>
<td>
<p> Form feed (ASCII 12)
</td>
</tr>
<tr VALIGN=top>
<td>
<p> <code>
</code> </td>
<td>
<p> Newline (ASCII 10)
</td>
</tr>
<tr VALIGN=top>
<td>
<p> <code></code> </td>
<td>
<p> Carriage Return (ASCII 13)
</td>
</tr>
<tr VALIGN=top>
<td>
<p> <code>	</code> </td>
<td>
<p> Tab (ASCII 9)
</td>
</tr>
<tr VALIGN=top>
<td>
<p> <code></code> </td>
<td>
<p> Vertical Tab (ASCII 11)
</td>
</tr>
<tr VALIGN=top>
<td>
<p> <code>\?</code> </td>
<td>
<p> Delete (ASCII 127)
</td>
</tr>
<tr VALIGN=top>
<td>
<p> <code>\_</code> </td>
<td>
<p> Space
</td>
</tr>
<tr VALIGN=top>
<td>
<p> <code>\</code> </td>
<td>
<p> Backslash (\)
</td>
</tr>
<tr VALIGN=top>
<td>
<p> <code>\^</code> </td>
<td>
<p> Caret (^)
</td>
</tr>
<tr VALIGN=top>
<td>
<p> <code>\#</code> </td>
<td>
<p> Hash mark (#)
</td>
</tr>
</table>
</dl>
<p> Please note that escapes are necessary to enter a space, backslash, caret, or any control character anywhere in the string, as well as a hash mark as the first character. </p>
<p> For example, to use a red background for alert messages in the output of <code><a href="/docs/linux/man/1-dmesg/">dmesg</a></code>(1), use:</p>
<dl>
<dd><code>echo &#8216;alert 37;41&#8217; &gt;&gt; /etc/terminal-colors.d/dmesg.scheme</code>
</dl>
<h3>Comments</h3>
<p>Lines where the first non-blank character is a # (hash) are ignored. Any other use of the hash character is not interpreted as introducing a comment.</p>
<h2>Environment</h2>
<p>TERMINAL_COLORS_DEBUG=all</p>
<dl>
<dd>enables debug output.</dl>
<h2>Files</h2>
<p><i>$XDG_CONFIG_HOME/terminal-colors.d</i> </p>
<p> <i>$HOME/.config/terminal-colors.d</i> </p>
<p> <i>/etc/terminal-colors.d</i></p>
<h2>Example</h2>
<p>Disable colors for all compatible utilities:</p>
<dl>
<dd><code>touch /etc/terminal-colors.d/disable</code>
</dl>
<p> Disable colors for all compatible utils on a vt100 terminal:</p>
<dl>
<dd><code>touch /etc/terminal-colors.d/@vt100.disable</code>
</dl>
<p> Disable colors for all compatible utils except <code><a href="/docs/linux/man/1-dmesg/">dmesg</a></code>(1):</p>
<dl>
<dd><code>touch /etc/terminal-colors.d/disable</code> </p>
<p> <code>touch /etc/terminal-colors.d/dmesg.enable</code>
</dl>
<h2>Compatibility</h2>
<p>The terminal-colors.d functionality is currently supported by all util-linux utilities which provides colorized output. For more details always see the COLORS section in the man page for the utility.</p>
<h2>Reporting Bugs</h2>
<p>For bug reports, use the issue tracker at <i></i> &lt;<a rel="nofollow" href="https://github.com/karelzak/util-linux/issues">https://github.com/karelzak/util-linux/issues</a>&gt;.</p>
<h2>Availability</h2>
<p><code>terminal-colors.d</code> is part of the util-linux package which can be downloaded from <i>Linux Kernel Archive</i> &lt;<a rel="nofollow" href="https://www.kernel.org/pub/linux/utils/util-linux/">https://www.kernel.org/pub/linux/utils/util-linux/</a>&gt;.</p>
