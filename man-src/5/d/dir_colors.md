---
title: "dir_colors(5)"
name: "dir_colors"
section: "5"
letter: "d"
url: "/docs/linux/man/5-dir_colors/"
description: "dir_colors – configuration file for"
---

<p>dir_colors &#8211; configuration file for </p>
<p> <a href="/docs/linux/man/1-dircolors/">dircolors</a>(1)</p>
<h2>Description</h2>
<p>The program <code><a href="/docs/linux/man/1-ls/">ls</a></code>(1) uses the environment variable <code>LS_COLORS</code> to determine the colors in which the filenames are to be displayed. This environment variable is usually set by a command like </p>
<dl>
<dd>eval `dircolors some_path/dir_colors`</dd></dl>
<p> found in a system default shell initialization file, like <i>/etc/profile</i> or <i>/etc/csh.cshrc</i>. (See also <code><a href="/docs/linux/man/1-dircolors/">dircolors</a></code>(1).) Usually, the file used here is <i>/etc/DIR_COLORS</i> and can be overridden by a <i>.dir_colors</i> file in one&#8217;s home directory. </p>
<p> This configuration file consists of several statements, one per line. Anything right of a hash mark (#) is treated as a comment, if the hash mark is at the beginning of a line or is preceded by at least one whitespace. Blank lines are ignored. </p>
<p> The <i>global</i> section of the file consists of any statement before the first <code>TERM</code> statement. Any statement in the global section of the file is considered valid for all terminal types. Following the global section is one or more <i>terminal-specific</i> sections, preceded by one or more <code>TERM</code> statements which specify the terminal types (as given by the <code>TERM</code> environment variable) the following declarations apply to. It is always possible to override a global declaration by a subsequent terminal-specific one. </p>
<p> The following statements are recognized; case is insignificant:</p>
<dl>
<dt><code>TERM </code><i>terminal-type</i></dt>
<dd>Starts a terminal-specific section and specifies which terminal it applies to. Multiple <code>TERM</code> statements can be used to create a section which applies for several terminal types.</dd>
<dt><code>COLOR yes|all|no|none|tty</code></dt>
<dd>(Slackware only; ignored by GNU <code><a href="/docs/linux/man/1-dircolors/">dircolors</a></code>(1).) Specifies that colorization should always be enabled (<i>yes</i> or <i>all</i>), never enabled (<i>no</i> or <i>none</i>), or enabled only if the output is a terminal (<i>tty</i>). The default is <i>no</i>.</dd>
<dt><code>EIGHTBIT yes|no</code></dt>
<dd>(Slackware only; ignored by GNU <code><a href="/docs/linux/man/1-dircolors/">dircolors</a></code>(1).) Specifies that eight-bit ISO 8859 characters should be enabled by default. For compatibility reasons, this can also be specified as 1 for <i>yes</i> or 0 for <i>no</i>. The default is <i>no</i>.</dd>
<dt><code>OPTIONS </code><i>options</i></dt>
<dd>(Slackware only; ignored by GNU <code><a href="/docs/linux/man/1-dircolors/">dircolors</a></code>(1).) Adds command-line options to the default <code>ls</code> command line. The options can be any valid <code>ls</code> command-line options, and should include the leading minus sign. Note that <code>dircolors</code> does not verify the validity of these options.</dd>
<dt><code>NORMAL </code><i>color-sequence</i></dt>
<dd>Specifies the color used for normal (nonfilename) text.</dd>
<dd>Synonym: <code>NORM</code>.</dd>
<dt><code>FILE </code><i>color-sequence</i></dt>
<dd>Specifies the color used for a regular file.</dd>
<dt><code>DIR </code><i>color-sequence</i></dt>
<dd>Specifies the color used for directories.</dd>
<dt><code>LINK </code><i>color-sequence</i></dt>
<dd>Specifies the color used for a symbolic link.</dd>
<dd>Synonyms: <code>LNK</code>, <code>SYMLINK</code>.</dd>
<dt><code>ORPHAN </code><i>color-sequence</i></dt>
<dd>Specifies the color used for an orphaned symbolic link (one which points to a nonexistent file). If this is unspecified, <code>ls</code> will use the <code>LINK</code> color instead.</dd>
<dt><code>MISSING </code><i>color-sequence</i></dt>
<dd>Specifies the color used for a missing file (a nonexistent file which nevertheless has a symbolic link pointing to it). If this is unspecified, <code>ls</code> will use the <code>FILE</code> color instead.</dd>
<dt><code>FIFO </code><i>color-sequence</i></dt>
<dd>Specifies the color used for a FIFO (named pipe).</dd>
<dd>Synonym: <code>PIPE</code>.</dd>
<dt><code>SOCK </code><i>color-sequence</i></dt>
<dd>Specifies the color used for a socket.</dd>
<dt><code>DOOR </code><i>color-sequence</i></dt>
<dd>(Supported since fileutils 4.1) Specifies the color used for a door (Solaris 2.5 and later).</dd>
<dt><code>BLK </code><i>color-sequence</i></dt>
<dd>Specifies the color used for a block device special file.</dd>
<dd>Synonym: <code>BLOCK</code>.</dd>
<dt><code>CHR </code><i>color-sequence</i></dt>
<dd>Specifies the color used for a character device special file.</dd>
<dd>Synonym: <code>CHAR</code>.</dd>
<dt><code>EXEC </code><i>color-sequence</i></dt>
<dd>Specifies the color used for a file with the executable attribute set.</dd>
<dt><code>SUID </code><i>color-sequence</i></dt>
<dd>Specifies the color used for a file with the set-user-ID attribute set.</dd>
<dd>Synonym: <code>SETUID</code>.</dd>
<dt><code>SGID </code><i>color-sequence</i></dt>
<dd>Specifies the color used for a file with the set-group-ID attribute set.</dd>
<dd>Synonym: <code>SETGID</code>.</dd>
<dt><code>STICKY </code><i>color-sequence</i></dt>
<dd>Specifies the color used for a directory with the sticky attribute set.</dd>
<dt><code>STICKY_OTHER_WRITABLE </code><i>color-sequence</i></dt>
<dd>Specifies the color used for an other-writable directory with the executable attribute set.</dd>
<dd>Synonym: <code>OWT</code>.</dd>
<dt><code>OTHER_WRITABLE </code><i>color-sequence</i></dt>
<dd>Specifies the color used for an other-writable directory without the executable attribute set.</dd>
<dd>Synonym: <code>OWR</code>.</dd>
<dt><code>LEFTCODE </code><i>color-sequence</i></dt>
<dd>Specifies the <i>left code</i> for non-ISO 6429 terminals (see below).</dd>
<dd>Synonym: <code>LEFT</code>.</dd>
<dt><code>RIGHTCODE </code><i>color-sequence</i></dt>
<dd>Specifies the <i>right code</i> for non-ISO 6429 terminals (see below).</dd>
<dd>Synonym: <code>RIGHT</code>.</dd>
<dt><code>ENDCODE </code><i>color-sequence</i></dt>
<dd>Specifies the <i>end code</i> for non-ISO 6429 terminals (see below).</dd>
<dd>Synonym: <code>END</code>.</dd>
<dt><code>*</code><i>extension</i> <i>color-sequence</i></dt>
<dd>Specifies the color used for any file that ends in <i>extension</i>.</dd>
<dt><code> .</code><i>extension</i> <i>color-sequence</i></dt>
<dd>Same as <code>*</code>.<i>extension</i>. Specifies the color used for any file that ends in .<i>extension</i>. Note that the period is included in the extension, which makes it impossible to specify an extension not starting with a period, such as <code>~</code> for <code>emacs</code> backup files. This form should be considered obsolete.</dd></dl>
<h3>ISO 6429 (ANSI) color sequences</h3>
<p>Most color-capable ASCII terminals today use ISO 6429 (ANSI) color sequences, and many common terminals without color capability, including <code>xterm</code> and the widely used and cloned DEC VT100, will recognize ISO 6429 color codes and harmlessly eliminate them from the output or emulate them. <code>ls</code> uses ISO 6429 codes by default, assuming colorization is enabled. </p>
<p> ISO 6429 color sequences are composed of sequences of numbers separated by semicolons. The most common codes are:</p>
<dl>
<dd>
<table>
<tr VALIGN=top>
<td>
&nbsp;0</td>
<td>to restore default color
</td>
</tr>
<tr VALIGN=top>
<td>
&nbsp;1</td>
<td>for brighter colors
</td>
</tr>
<tr VALIGN=top>
<td>
&nbsp;4</td>
<td>for underlined text
</td>
</tr>
<tr VALIGN=top>
<td>
&nbsp;5</td>
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
</dd></dl>
<p> Not all commands will work on all systems or display devices. </p>
<p> <code>ls</code> uses the following defaults: </p>
<table>
<tr VALIGN=top>
<td><code>NORMAL</code></td>
<td>0 </td>
<td>Normal (nonfilename) text
</td>
</tr>
<tr VALIGN=top>
<td><code>FILE</code></td>
<td>0 </td>
<td>Regular file
</td>
</tr>
<tr VALIGN=top>
<td><code>DIR</code></td>
<td>32 </td>
<td>Directory
</td>
</tr>
<tr VALIGN=top>
<td><code>LINK</code></td>
<td>36 </td>
<td>Symbolic link
</td>
</tr>
<tr VALIGN=top>
<td><code>ORPHAN</code></td>
<td>undefined</td>
<td>Orphaned symbolic link
</td>
</tr>
<tr VALIGN=top>
<td><code>MISSING</code></td>
<td>undefined</td>
<td>Missing file
</td>
</tr>
<tr VALIGN=top>
<td><code>FIFO</code></td>
<td>31 </td>
<td>Named pipe (FIFO)
</td>
</tr>
<tr VALIGN=top>
<td><code>SOCK</code></td>
<td>33 </td>
<td>Socket
</td>
</tr>
<tr VALIGN=top>
<td><code>BLK</code></td>
<td>44;37 </td>
<td>Block device
</td>
</tr>
<tr VALIGN=top>
<td><code>CHR</code></td>
<td>44;37 </td>
<td>Character device
</td>
</tr>
<tr VALIGN=top>
<td><code>EXEC</code></td>
<td>35 </td>
<td>Executable file
</td>
</tr>
</table>
<p> A few terminal programs do not recognize the default properly. If all text gets colorized after you do a directory listing, change the <code>NORMAL</code> and <code>FILE</code> codes to the numerical codes for your normal foreground and background colors.</p>
<h3>Other terminal types (advanced configuration)</h3>
<p>If you have a color-capable (or otherwise highlighting) terminal (or printer!) which uses a different set of codes, you can still generate a suitable setup. To do so, you will have to use the <code>LEFTCODE</code>, <code>RIGHTCODE</code>, and <code>ENDCODE</code> definitions. </p>
<p> When writing out a filename, <code>ls</code> generates the following output sequence: <code>LEFTCODE</code> <i>typecode</i> <code>RIGHTCODE</code> <i>filename</i> <code>ENDCODE</code>, where the <i>typecode</i> is the color sequence that depends on the type or name of file. If the <code>ENDCODE</code> is undefined, the sequence <code>LEFTCODE NORMAL RIGHTCODE</code> will be used instead. The purpose of the left- and rightcodes is merely to reduce the amount of typing necessary (and to hide ugly escape codes away from the user). If they are not appropriate for your terminal, you can eliminate them by specifying the respective keyword on a line by itself. </p>
<p> <code>NOTE:</code> If the <code>ENDCODE</code> is defined in the global section of the setup file, it <i>cannot</i> be undefined in a terminal-specific section of the file. This means any <code>NORMAL</code> definition will have no effect. A different <code>ENDCODE</code> can, however, be specified, which would have the same effect.</p>
<h3>Escape sequences</h3>
<p>To specify control- or blank characters in the color sequences or filename extensions, either C-style \-escaped notation or <code>stty</code>-style ha-notation can be used. The C-style notation includes the following characters:</p>
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
<td><code>
</code></td>
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
<td><code>\<i>nnn</i></code></td>
<td>Any character (octal notation)
</td>
</tr>
<tr VALIGN=top>
<td><code></code><br />
</td>
</tr>
<tr VALIGN=top>
<td><code>\x <i>nnn</i></code></td>
<td>Any character (hexadecimal notation)
</td>
</tr>
<tr VALIGN=top>
<td><code>\_</code></td>
<td>Space
</td>
</tr>
<tr VALIGN=top>
<td><code>\\</code></td>
<td>Backslash (\)
</td>
</tr>
<tr VALIGN=top>
<td><code>\ha</code></td>
<td>Caret (ha)
</td>
</tr>
<tr VALIGN=top>
<td><code>\#</code></td>
<td>Hash mark (#)
</td>
</tr>
</table>
</dl>
<p> Note that escapes are necessary to enter a space, backslash, caret, or any control character anywhere in the string, as well as a hash mark as the first character.  </p>
<h2>FILES</h2>
<dl>
<dt><i>/etc/DIR_COLORS</i></dt>
<dd> <p> (Slackware, SuSE and RedHat only; ignored by GNU <code><a href="/docs/linux/man/1-dircolors/">dircolors</a></code>(1) and thus Debian.) System-wide configuration file. </p>
 </dd>
<dt><i>~/.dir_colors</i></dt>
<dd> <p> (Slackware, SuSE and RedHat only; ignored by GNU <code><a href="/docs/linux/man/1-dircolors/">dircolors</a></code>(1) and thus Debian.) Per-user configuration file. </p>
 </dd></dl>
<p> This page describes the <code>dir_colors</code> file format as used in the fileutils-4.1 package; other versions may differ slightly.  </p>
<h2>NOTES</h2>
<p> The default <code>LEFTCODE</code> and <code>RIGHTCODE</code> definitions, which are used by ISO 6429 terminals are: </p>
<dl>
<dd> <table>
<tr VALIGN=top>
<td><code>LEFTCODE</code></td>
<td>\e[
</td>
</tr>
<tr VALIGN=top>
<td><code>RIGHTCODE</code></td>
<td>m
</td>
</tr>
</table>
 </dd></dl>
<p> The default <code>ENDCODE</code> is undefined.  </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-dircolors/">dircolors</a></code>(1), <code><a href="/docs/linux/man/1-ls/">ls</a></code>(1), <code><a href="/docs/linux/man/1-stty/">stty</a></code>(1), <code><a href="/docs/linux/man/1-xterm/">xterm</a></code>(1)  </p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
