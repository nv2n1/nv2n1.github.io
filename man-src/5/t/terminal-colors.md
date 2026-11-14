---
title: "terminal-colors(5)"
name: "terminal-colors"
section: "5"
letter: "t"
url: "/docs/linux/man/5-terminal-colors/"
description: "terminal-colors.d – Configure output colorization for various utilities"
---

<p>terminal-colors.d &#8211; Configure output colorization for various utilities</p>
<h2>Synopsis</h2>
<p>/etc/terminal-colors.d/[[<i>name</i>][@<i>term</i>].][<i>type</i>]</p>
<h2>Description</h2>
<p>Files in this directory determine the default behavior for utilities when coloring output. The <i>name</i> is a utility name. The name is optional and when none is specified then the file is used for all unspecified utilities. The <i>term</i> is a terminal identifier (the TERM environment variable). The terminal identifier is optional and when none is specified then the file is used for all unspecified terminals. The <i>type</i> is a file type. Supported file types are:</p>
<dl>
<dt><code>disable</code></p>
<dd>Turns off output colorization for all compatible utilities.</p>
<dt><code>enable</code></p>
<dd>Turns on output colorization; any matching <code>disable</code> files are ignored.</p>
<dt><code>scheme</code></p>
<dd>Specifies colors used for output. The file format may be specific to the utility, the default format is described below.</dl>
<p> If there are more files that match for a utility, then the file with the more specific filename wins. For example, the filename &quot;@xterm.scheme&quot; has less priority than &quot;dmesg [at] xterm.scheme&quot;. The lowest priority are those files without a utility name and terminal identifier (e.g. &quot;disable&quot;). The user-specific <i>$XDG_CONFIG_HOME/terminal-colors.d</i> or <i>$HOME/.config/terminal-colors.d</i> overrides the global setting. </p>
<h2>Examples</h2>
<p>Disable colors for all compatible utilities:</p>
<dl>
<dd><code>touch /etc/terminal-colors.d/disable</code>
</dl>
<p> Disable colors for all compatible utils on a vt100 terminal:</p>
<dl>
<dd><code>touch /etc/terminal-colors.d/@vt100.disable</code>
</dl>
<p> Disable colors for all compatible utils except <a href="/docs/linux/man/1-dmesg/">dmesg</a>(1):</p>
<dl>
<dd><code>touch /etc/terminal-colors.d/disable</code> <code>touch /etc/terminal-colors.d/dmesg.enable</code>
</dl>
<h2>Default Scheme Files Format</h2>
<p>The following statement is recognized: </p>
<dl>
<dd><code>name color-sequence</code>
</dl>
<p> The <code>name</code> is a logical name of color sequence (for example &quot;error&quot;). The names are specific to the utilities. For more details always see the COLORS section in the man page for the utility. </p>
<p> The <code>color-sequence</code> is a color name, ASCII color sequences or escape sequences.</p>
<h3>Color names</h3>
<p>black, blue, brown, cyan, darkgray, gray, green, lightblue, lightcyan lightgray, lightgreen, lightmagenta, lightred, magenta, red and yellow</p>
<h3>ANSI color sequences</h3>
<p>The color sequences are composed of sequences of numbers separated by semicolons. The most common codes are: </p>
<dl>
<dd>
<table>
<tr VALIGN=top>
<td>
&nbsp;<wbr>0</td>
<td>to restore default color
</td>
</tr>
<tr VALIGN=top>
<td>
&nbsp;<wbr>1</td>
<td>for brighter colors
</td>
</tr>
<tr VALIGN=top>
<td>
&nbsp;<wbr>4</td>
<td>for underlined text
</td>
</tr>
<tr VALIGN=top>
<td>
&nbsp;<wbr>5</td>
<td>for flashing text
</td>
</tr>
<tr VALIGN=top>
<td>30</td>
<td>for black foreground
</td>
</tr>
<tr VALIGN=top>
<td>31</td>
<td>for red foreground
</td>
</tr>
<tr VALIGN=top>
<td>32</td>
<td>for green foreground
</td>
</tr>
<tr VALIGN=top>
<td>33</td>
<td>for yellow (or brown) foreground
</td>
</tr>
<tr VALIGN=top>
<td>34</td>
<td>for blue foreground
</td>
</tr>
<tr VALIGN=top>
<td>35</td>
<td>for purple foreground
</td>
</tr>
<tr VALIGN=top>
<td>36</td>
<td>for cyan foreground
</td>
</tr>
<tr VALIGN=top>
<td>37</td>
<td>for white (or gray) foreground
</td>
</tr>
<tr VALIGN=top>
<td>40</td>
<td>for black background
</td>
</tr>
<tr VALIGN=top>
<td>41</td>
<td>for red background
</td>
</tr>
<tr VALIGN=top>
<td>42</td>
<td>for green background
</td>
</tr>
<tr VALIGN=top>
<td>43</td>
<td>for yellow (or brown) background
</td>
</tr>
<tr VALIGN=top>
<td>44</td>
<td>for blue background
</td>
</tr>
<tr VALIGN=top>
<td>45</td>
<td>for purple background
</td>
</tr>
<tr VALIGN=top>
<td>46</td>
<td>for cyan background
</td>
</tr>
<tr VALIGN=top>
<td>47</td>
<td>for white (or gray) background
</td>
</tr>
</table>
</dl>
<h3>Escape sequences</h3>
<p>To specify control or blank characters in the color sequences, C-style \-escaped notation can be used: </p>
<dl>
<dd>
<table>
<tr VALIGN=top>
<td><code></code></td>
<td>Bell (ASCII 7)
</td>
</tr>
<tr VALIGN=top>
<td><code></code></td>
<td>Backspace (ASCII 8)
</td>
</tr>
<tr VALIGN=top>
<td><code></code></td>
<td>Escape (ASCII 27)
</td>
</tr>
<tr VALIGN=top>
<td><code></code></td>
<td>Form feed (ASCII 12)
</td>
</tr>
<tr VALIGN=top>
<td><code>
</code></td>
<td>Newline (ASCII 10)
</td>
</tr>
<tr VALIGN=top>
<td><code></code></td>
<td>Carriage Return (ASCII 13)
</td>
</tr>
<tr VALIGN=top>
<td><code>	</code></td>
<td>Tab (ASCII 9)
</td>
</tr>
<tr VALIGN=top>
<td><code></code></td>
<td>Vertical Tab (ASCII 11)
</td>
</tr>
<tr VALIGN=top>
<td><code>\?</code></td>
<td>Delete (ASCII 127)
</td>
</tr>
<tr VALIGN=top>
<td><code>\_</code></td>
<td>Space
</td>
</tr>
<tr VALIGN=top>
<td><code>\</code></td>
<td>Backslash (\)
</td>
</tr>
<tr VALIGN=top>
<td><code>\^</code></td>
<td>Caret (^)
</td>
</tr>
<tr VALIGN=top>
<td><code>\#</code></td>
<td>Hash mark (#)
</td>
</tr>
</table>
</dl>
<p> Please note that escapes are necessary to enter a space, backslash, caret, or any control character anywhere in the string, as well as a hash mark as the first character. </p>
<p> For example, to use a red background for alert messages in the output of <code><a href="/docs/linux/man/1-dmesg/">dmesg</a></code>(1), use: </p>
<dl>
<dd><code>echo &#8216;alert 37;41&#8217; &gt;&gt; /etc/terminal-colors.d/dmesg.scheme</code>
</dl>
<h2>Files</h2>
<p><code>$XDG_CONFIG_HOME/terminal-colors.d</code><br />
 <code>$HOME/.config/terminal-colors.d</code><br />
 <code>/etc/terminal-colors.d</code></p>
<h2>Compatibility</h2>
<p>The terminal-colors.d functionality is currently supported by all util-linux utilities which provides colorized output. For more details always see the COLORS section in the man page for the utility.</p>
<h2>Availability</h2>
<p>terminal-colors.d is part of the util-linux package and is available from Linux Kernel Archive</p>
