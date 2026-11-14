---
title: "tweak(1)"
name: "tweak"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tweak/"
description: "tweak – efficient hex editor"
---

<h2>NAME</h2>
<p> <code>tweak</code> &#8211; efficient hex editor</p>
<h2>SYNOPSIS</h2>
<pre><code>
tweak &amp;nbsp;
[-l &amp; nbsp; | &amp;nbsp; - f] &amp; nbsp;
[-e] &amp; nbsp;
[-w &amp; nbsp; width] &amp; nbsp;
[-o &amp; nbsp; offset] &amp; nbsp;
filename
</code></pre>
<h2>DESCRIPTION</h2>
<p> <code>tweak</code> is a hex editor. It allows you to edit a file at very low level, letting you see the full and exact binary contents of the file. It can be useful for modifying binary files such as executables, editing disk or CD images, debugging programs that generate binary file formats incorrectly, and many other things. </p>
<p> Unlike simpler hex editors, <code>tweak</code> possesses a fully functional insert mode. This is not useful when editing many of the types of file described above, but can be useful in other situations. Also, an insert mode makes it easy to use <code>tweak</code> to construct new files from scratch. </p>
<p> When you open a file in <code>tweak</code>, you can expect to see the screen contents looking something like this: </p>
<p>00000000 &amp; nbsp;<br />
&amp;nbsp;<br />
&amp;nbsp;<br />
7F 45 4C 46 01 01 01 00 &amp; nbsp;<br />
&amp;nbsp;<br />
&amp;nbsp;<br />
.ELF&#8230;.00000008 &amp; nbsp;<br />
&amp;nbsp;<br />
&amp;nbsp;<br />
00 00 00 00 00 00 00 00 &amp; nbsp;<br />
&amp;nbsp;<br />
&amp;nbsp;<br />
&#8230;&#8230;..00000010 &amp; nbsp;<br />
&amp;nbsp;<br />
&amp;nbsp;<br />
02 00 03 00 01 00 00 00 &amp; nbsp;<br />
&amp;nbsp;<br />
&amp;nbsp;<br />
&#8230;&#8230;..00000018 &amp; nbsp;<br />
&amp;nbsp;<br />
&amp;nbsp;<br />
D0 8E 04 08 34 00 00 00 &amp; nbsp;<br />
&amp;nbsp;<br />
&amp;nbsp;<br />
&#8230; .4&#8230; 00000020 &amp; nbsp;<br />
&amp;nbsp;<br />
&amp;nbsp;<br />
2C EF 01 00 00 00 00 00 &amp; nbsp;<br />
&amp;nbsp;<br />
&amp;nbsp;<br />
, &#8230;&#8230;.</p>
<p> The central column shows you the hexadecimal value of each byte in the file you are editing. The column on the right shows the ASCII interpretation of those bytes, where applicable. In the example above, the sequence <code>45 4C 46</code> on the first line translates into the ASCII upper-case letters `ELF&#8217;, but the subsequent sequence <code>01 01 01 00</code> does not have any printable ASCII representation and so the right-hand column simply prints dots. </p>
<p> The column on the left shows the position within the file of the start of each row. </p>
<p> In fact, when you start <code>tweak</code>, you will usually see 16 bytes of the file per row, not 8 as shown above. However, this is configurable if your screen is narrower &#8211; or wider &#8211; than the usual 80 columns, or if the file you are editing consists of fixed-size records of some other size. </p>
<p> By default, <code>tweak</code> does not load its entire input file into memory. Instead, it loads it <i>lazily</i>, reading from the file on disk when you request a view of a part of the file it doesn&#8217;t have stored. When you modify the file, it stores your modifications in memory, but continues to refer to the original disk file for the parts you have not touched. This means you can edit extremely large files (for example, entire CD images) without difficulty; opening such a file is instantaneous, making modifications causes <code>tweak</code>&#8216;s memory usage to grow with the size of the changes rather than the size of the whole file, and only when saving the altered version will <code>tweak</code> have to read through the entire input file to write the output. </p>
<p> However, this mode of operation has a disadvantage, which is that if the input file is modified by another program while <code>tweak</code> is running, <code>tweak</code>&#8216;s internal data structures will not be sufficient to keep track, and it is likely that the file written out will contain a mixture of the old and new contents of the input file. Therefore, you can disable this lazy loading if you need to; see the <code>-e</code> option below.</p>
<h2>OPTIONS</h2>
<p> This section lists the command-line options supported by <code>tweak</code>.</p>
<dl>
<dt><code>-f</code></p>
<dd> Runs <code>tweak</code> in `fix&#8217; mode, i.e. with the insert function entirely disabled. This might be useful if you are editing a file in which the insert mode is of no use (executables, for example, tend to have strong dependencies on precise file offsets which make it almost impossible to insert data in one without rendering it unusable) and you want to avoid turning it on by mistake.</p>
<dt><code>-l</code></p>
<dd> Runs <code>tweak</code> in `look&#8217; mode. In this mode <code>tweak</code> does not allow you to modify the data at all; it becomes simply a tool for examining a file in detail.</p>
<dt><code>-e</code></p>
<dd> Runs <code>tweak</code> in `eager&#8217; mode. In this mode <code>tweak</code> will read its entire input file when starting up. This causes it to take up more memory, but means that it has no dependency on the input file remaining unmodified, and other programs can alter it if they need to without causing trouble.</p>
<dt><code>-w</code> <i>width</i></p>
<dd> Specifies the number of bytes <code>tweak</code> will display per line. The default is 16, which fits neatly in an 80-column screen.</p>
<dt><code>-o</code> <i>offset</i></p>
<dd> If this option is specified, <code>tweak</code> will ensure that the given file offset occurs at the start of a line. For example, if you loaded a file using the options <code>-w 8 -o 0x13</code>, you might see a display a bit like this:</p>
<dl>
<dt>
<dd>
<pre><code>
00000000 &amp; nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
7F 45 4C &amp; nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
.EL 00000003 &amp; nbsp;
&amp;nbsp;
&amp;nbsp;
46 01 01 01 00 00 00 00 &amp; nbsp;
&amp;nbsp;
&amp;nbsp;
F.......0000000B &amp; nbsp;
&amp;nbsp;
&amp;nbsp;
00 00 00 00 00 02 00 03 &amp; nbsp;
&amp;nbsp;
&amp;nbsp;
........00000013 &amp; nbsp;
&amp;nbsp;
&amp;nbsp;
00 01 00 00 00 D0 8E 04 &amp; nbsp;
&amp;nbsp;
&amp;nbsp;
........0000001B &amp; nbsp;
&amp;nbsp;
&amp;nbsp;
08 34 00 00 00 2C EF 01 &amp; nbsp;
&amp;nbsp;
&amp;nbsp;
.4..., ..
</code></pre>
<p> By putting only three bytes of the file on the very first line, <code>tweak</code> has arranged that the file offset 0x13 (19 in decimal) appears at the beginning of the fourth line. </p>
<p> You might use this option if you knew you were editing a file in a particular format. For example, if your file contained a 53-byte header followed by a series of 22-byte records, you might find it useful to specify the options <code>-w 22 -o 53</code>. This would arrange that after the header, each individual record of the file would appear on precisely one line of <code>tweak</code>&#8216;s display.</dl>
<dt><code>-D</code></p>
<dd> If this option is specified, <code>tweak</code> will not attempt to load and edit a file at all, but will simply produce its default <code>.tweakrc</code> file on standard output. This is a useful way to give yourself a starting point if you want to begin reconfiguring <code>tweak</code>&#8216;s keyboard layout.</dl>
<h2>KEYS</h2>
<p> This section describes all the editing keys supported by <code>tweak</code> by default. The default key bindings for <code>tweak</code> are basically Emacs-like.</p>
<h3>Movement keys</h3>
<p> The Emacs cursor movement keys should all work, and their counterparts in ordinary function keys ought to work too:</p>
<dl>
<dt><code>&bull;</code></p>
<dd> <code>^P</code> and <code>^N</code> go to the previous and next lines; Up and Down should do the same.</p>
<dt><code>&bull;</code></p>
<dd> <code>^B</code> and <code>^F</code> go back and forward one character; Left and Right should do the same.</p>
<dt><code>&bull;</code></p>
<dd> <code>M-v</code> and <code>^V</code> go up and down one screenful at a time; Page Up and Page Down should do the same.</p>
<dt><code>&bull;</code></p>
<dd> <code>^A</code> and <code>^E</code> go to the beginning and end of the line; Home and End should do the same.</dl>
<p> Press <code>M-&lt;</code> and <code>M-&gt;</code> go to the beginning and end of the file. </p>
<p> Press <code>^X g</code> to go to a particular byte position in the file; you will be asked to type in the position you want. You can enter it in decimal, or as a hex number with `<code>0x</code>&#8216; before it.</p>
<h3>Editing keys</h3>
<p> Press Return to move the cursor between the hex section of the screen and the ASCII section. </p>
<p> When in the hex section, you can enter hexadecimal digits to alter data; when in the ASCII section, you can directly type ASCII text. </p>
<p> In ASCII mode, you can also press <code>^Q</code> to literally quote the next input character; for example, if you want to insert a Control-V, you can press <code>^Q^V</code> and <code>tweak</code> will automatically insert the byte value 0x16. </p>
<p> Press <code>^X^I</code>, or the Insert key if you have one, to toggle between overwrite mode and insert mode. In insert mode, typing hex or ASCII input will insert new bytes containing the values you provide. Also, you can then press Backspace to delete the byte to the left of the cursor, or <code>^D</code> or Delete to delete the byte under the cursor.</p>
<h3>Cut and paste</h3>
<p> Press <code>^@</code> (this character may be generated by the key combination Control-@, or Control-2, or Control-Space) to mark the end of a selection region. After you do this, the bytes between that mark and the cursor will be highlighted. Press <code>^@</code> again to abandon the selection. </p>
<p> Press <code>M-w</code> while a selection is active to copy the selected region into <code>tweak</code>&#8216;s cut buffer. </p>
<p> In insert mode, you also have the option of pressing <code>^W</code> to <i>cut</i> the selected region completely out of the file and place it in the cut buffer. </p>
<p> Finally, press <code>^Y</code> to paste the cut buffer contents back into the file (this will overwrite or insert depending on the current mode).</p>
<h3>Searching</h3>
<p> Press <code>^S</code> to search for a byte sequence. You will be asked to enter some text to search for on the bottom line of the screen. You can type this text in ASCII, or as a sequence of hex byte values prefixed with backslashes (<code>\</code>). For example, if you wanted to search for the byte value 5 followed by the word `hello&#8217;, you might enter <code>hello</code>. If you want to specify a literal backslash character, you can either enter it in hex (as <code>\5C</code>), or simply double it on input (<code>\</code>). </p>
<p> Press <code>^R</code> to search backwards instead of forwards from the current cursor position. </p>
<p> Since <code>tweak</code> deals in pure binary data, searches are always case-sensitive.</p>
<h3>Controlling the display</h3>
<p> If you press <code>^X w</code>, you will be asked to enter a new display width. This has the same effect as passing the <code>-w</code> option on the command line. Similarly, pressing <code>^X o</code> allows you to enter a new display offset, equivalent to the <code>-o</code> option. </p>
<p> By default, the current file position and file size are displayed on <code>tweak</code>&#8216;s status line in hex. If you prefer them in decimal, you can press <code>^X x</code> or <code>^X h</code> to toggle them between hex and decimal.</p>
<h3>Miscellaneous</h3>
<p> Press <code>^L</code> to redraw the screen and recentre the cursor. Press <code>^Z</code> to suspend <code>tweak</code> and return temporarily to the shell. </p>
<p> Press <code>^X^S</code> to save the file you are editing. </p>
<p> Press <code>^X^C</code> to exit <code>tweak</code>. (If you do this with changes unsaved, you will be asked whether you want to save them.)</p>
<h2>CONFIGURATION FILE</h2>
<p> <code>tweak</code>&#8216;s keyboard bindings are configurable. It will attempt to read a file from your home directory called <code>.tweakrc</code>, and if it finds one it will use the keyboard bindings described in it. If it does not find one, it will use its internal default bindings. </p>
<p> Most of the directives in <code>.tweakrc</code> are of the form `<code>bind command-name key</code>&#8216;. For example, `<code>bind exit ^X^C</code>&#8216;. Additionally, there are two other directives, <code>width</code> and <code>offset</code>, which give the default display parameters if no <code>-w</code> and <code>-o</code> options are specified. </p>
<p> The easiest way to learn about the <code>.tweakrc</code> file is to begin by having <code>tweak</code> output its internal default one: </p>
<pre>
tweak -D&nbsp;<wbr>&gt;&nbsp;<wbr>$HOME/.tweakrc
</pre>
<p> Then you can read the default file, learn the <code>tweak</code> internal command names, and edit the file to do what you want.</p>
<h2>BUGS</h2>
<p> This man page probably ought to contain an explicit list of internal command names, rather than simply referring you to the default <code>.tweakrc</code>. </p>
<h2>Index</h2>
