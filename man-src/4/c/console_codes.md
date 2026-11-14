---
title: "console_codes(4)"
name: "console_codes"
section: "4"
letter: "c"
url: "/docs/linux/man/4-console_codes/"
description: "console_codes – Linux console escape and control sequences"
---

<p>console_codes &#8211; Linux console escape and control sequences</p>
<h2>Description</h2>
<p>The Linux console implements a large subset of the VT102 and ECMA-48/ISO 6429/ANSI X3.64 terminal controls, plus certain private-mode sequences for changing the color palette, character-set mapping, and so on. In the tabular descriptions below, the second column gives ECMA-48 or DEC mnemonics (the latter if prefixed with DEC) for the given function. Sequences without a mnemonic are neither ECMA-48 nor VT102. After all the normal output processing has been done, and a stream of characters arrives at the console driver for actual printing, the first thing that happens is a translation from the code used for processing to the code used for printing. If the console is in UTF-8 mode, then the incoming bytes are first assembled into 16-bit Unicode codes. Otherwise, each byte is transformed according to the current mapping table (which translates it to a Unicode value). See the <code>Character Sets</code> section below for discussion. In the normal case, the Unicode value is converted to a font index, and this is stored in video memory, so that the corresponding glyph (as found in video ROM) appears on the screen. Note that the use of Unicode (and the design of the PC hardware) allows us to use 512 different glyphs simultaneously. If the current Unicode value is a control character, or we are currently processing an escape sequence, the value will treated specially. Instead of being turned into a font index and rendered as a glyph, it may trigger cursor movement or other control functions. See the <code>Linux Console Controls</code> section below for discussion. It is generally not good practice to hard-wire terminal controls into programs. Linux supports a <code><a href="/docs/linux/man/5-terminfo/">terminfo</a></code>(5) database of terminal capabilities. Rather than emitting console escape sequences by hand, you will almost always want to use a terminfo-aware screen library or utility such as <code><a href="/docs/linux/man/3-ncurses/">ncurses</a></code>(3), <code><a href="/docs/linux/man/1-tput/">tput</a></code>(1), or <code><a href="/docs/linux/man/1-reset/">reset</a></code>(1).</p>
<h3>Linux console controls</h3>
<p>This section describes all the control characters and escape sequences that invoke special functions (i.e., anything other than writing a glyph at the current cursor location) on the Linux console. <code>Control characters</code> A character is a control character if (before transformation according to the mapping table) it has one of the 14 codes 00 (NUL), 07 (BEL), 08 (BS), 09 (HT), 0a (LF), 0b (VT), 0c (FF), 0d (CR), 0e (SO), 0f (SI), 18 (CAN), 1a (SUB), 1b (ESC), 7f (DEL). One can set a &quot;display control characters&quot; mode (see below), and allow 07, 09, 0b, 18, 1a, 7f to be displayed as glyphs. On the other hand, in UTF-8 mode all codes 00-1f are regarded as control characters, regardless of any &quot;display control characters&quot; mode. If we have a control character, it is acted upon immediately and then discarded (even in the middle of an escape sequence) and the escape sequence continues with the next character. (However, ESC starts a new escape sequence, possibly aborting a previous unfinished one, and CAN and SUB abort any escape sequence.) The recognized control characters are BEL, BS, HT, LF, VT, FF, CR, SO, SI, CAN, SUB, ESC, DEL, CSI. They do what one would expect:</p>
<dl>
<dd>BEL (0x07, <code>haG</code>) beeps;</p>
<dd>BS (0x08, <code>haH</code>) backspaces one column (but not past the beginning of the line);</p>
<dd>HT (0x09, <code>haI</code>) goes to the next tab stop or to the end of the line if there is no earlier tab stop;</p>
<dd>LF (0x0A, <code>haJ</code>), VT (0x0B, <code>haK</code>) and FF (0x0C, <code>haL</code>) all give a linefeed, and if LF/NL (new-line mode) is set also a carriage return;</p>
<dd>CR (0x0D, <code>haM</code>) gives a carriage return;</p>
<dd>SO (0x0E, <code>haN</code>) activates the G1 character set;</p>
<dd>SI (0x0F, <code>haO</code>) activates the G0 character set;</p>
<dd>CAN (0x18, <code>haX</code>) and SUB (0x1A, <code>haZ</code>) abort escape sequences;</p>
<dd>ESC (0x1B, <code>ha[</code>) starts an escape sequence;</p>
<dd>DEL (0x7F) is ignored;</p>
<dd>CSI (0x9B) is equivalent to ESC [.</dl>
<p> <code>ESC- but not CSI-sequences</code> </p>
<table>
<tr VALIGN=top>
<td>ESC c</td>
<td>RIS</td>
<td>Reset.
</td>
</tr>
<tr VALIGN=top>
<td>ESC D</td>
<td>IND</td>
<td>Linefeed.
</td>
</tr>
<tr VALIGN=top>
<td>ESC E</td>
<td>NEL</td>
<td>Newline.
</td>
</tr>
<tr VALIGN=top>
<td>ESC H</td>
<td>HTS</td>
<td>Set tab stop at current column.
</td>
</tr>
<tr VALIGN=top>
<td>ESC M</td>
<td>RI</td>
<td>Reverse linefeed.
</td>
</tr>
<tr VALIGN=top>
<td>ESC Z</td>
<td>DECID</td>
<td> DEC private identification. The kernel returns the string ESC [ ? 6 c, claiming that it is a VT102.
</td>
</tr>
<tr VALIGN=top>
<td>ESC 7</td>
<td>DECSC</td>
<td> Save current state (cursor coordinates, attributes, character sets pointed at by G0, G1).
</td>
</tr>
<tr VALIGN=top>
<td>ESC 8</td>
<td>DECRC</td>
<td>Restore state most recently saved by ESC 7.
</td>
</tr>
<tr VALIGN=top>
<td>ESC [</td>
<td>CSI</td>
<td>Control sequence introducer
</td>
</tr>
<tr VALIGN=top>
<td>ESC %</td>
<td></td>
<td>Start sequence selecting character set
</td>
</tr>
<tr VALIGN=top>
<td>ESC % @</td>
<td></td>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Select default (ISO 646 / ISO 8859-1)
</td>
</tr>
<tr VALIGN=top>
<td>ESC % G</td>
<td></td>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Select UTF-8
</td>
</tr>
<tr VALIGN=top>
<td>ESC % 8</td>
<td></td>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Select UTF-8 (obsolete)
</td>
</tr>
<tr VALIGN=top>
<td>ESC # 8</td>
<td>DECALN</td>
<td>DEC screen alignment test &#8211; fill screen with E&#8217;s.
</td>
</tr>
<tr VALIGN=top>
<td>ESC (</td>
<td></td>
<td>Start sequence defining G0 character set
</td>
</tr>
<tr VALIGN=top>
<td>ESC ( B</td>
<td></td>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Select default (ISO 8859-1 mapping)
</td>
</tr>
<tr VALIGN=top>
<td>ESC ( 0</td>
<td></td>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Select VT100 graphics mapping
</td>
</tr>
<tr VALIGN=top>
<td>ESC ( U</td>
<td></td>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Select null mapping &#8211; straight to character ROM
</td>
</tr>
<tr VALIGN=top>
<td>ESC ( K</td>
<td></td>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Select user mapping &#8211; the map that is loaded by
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td></td>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;the utility <code><a href="/docs/linux/man/8-mapscrn/">mapscrn</a></code>(8).
</td>
</tr>
<tr VALIGN=top>
<td>ESC )</td>
<td></td>
<td>Start sequence defining G1
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td></td>
<td>(followed by one of B, 0, U, K, as above).
</td>
</tr>
<tr VALIGN=top>
<td>ESC &gt;</td>
<td>DECPNM</td>
<td>Set numeric keypad mode
</td>
</tr>
<tr VALIGN=top>
<td>ESC =</td>
<td>DECPAM</td>
<td>Set application keypad mode
</td>
</tr>
<tr VALIGN=top>
<td>ESC ]</td>
<td>OSC</td>
<td> (Should be: Operating system command) ESC ] P <i>nrrggbb</i>: set palette, with parameter given in 7 hexadecimal digits after the final P :-(. Here <i>n</i> is the color (0-15), and <i>rrggbb</i> indicates the red/green/blue values (0-255). ESC ] R: reset palette
</td>
</tr>
</table>
<p> <code>ECMA-48 CSI sequences</code> CSI (or ESC [) is followed by a sequence of parameters, at most NPAR (16), that are decimal numbers separated by semicolons. An empty or absent parameter is taken to be 0. The sequence of parameters may be preceded by a single question mark. However, after CSI [ (or ESC [ [) a single character is read and this entire sequence is ignored. (The idea is to ignore an echoed function key.) The action of a CSI sequence is determined by its final character. </p>
<table>
<tr VALIGN=top>
<td>@</td>
<td>ICH</td>
<td>Insert the indicated # of blank characters.
</td>
</tr>
<tr VALIGN=top>
<td>A</td>
<td>CUU</td>
<td>Move cursor up the indicated # of rows.
</td>
</tr>
<tr VALIGN=top>
<td>B</td>
<td>CUD</td>
<td>Move cursor down the indicated # of rows.
</td>
</tr>
<tr VALIGN=top>
<td>C</td>
<td>CUF</td>
<td>Move cursor right the indicated # of columns.
</td>
</tr>
<tr VALIGN=top>
<td>D</td>
<td>CUB</td>
<td>Move cursor left the indicated # of columns.
</td>
</tr>
<tr VALIGN=top>
<td>E</td>
<td>CNL</td>
<td>Move cursor down the indicated # of rows, to column 1.
</td>
</tr>
<tr VALIGN=top>
<td>F</td>
<td>CPL</td>
<td>Move cursor up the indicated # of rows, to column 1.
</td>
</tr>
<tr VALIGN=top>
<td>G</td>
<td>CHA</td>
<td>Move cursor to indicated column in current row.
</td>
</tr>
<tr VALIGN=top>
<td>H</td>
<td>CUP</td>
<td>Move cursor to the indicated row, column (origin at 1,1).
</td>
</tr>
<tr VALIGN=top>
<td>J</td>
<td>ED</td>
<td>Erase display (default: from cursor to end of display).
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td></td>
<td>ESC [ 1 J: erase from start to cursor.
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td></td>
<td>ESC [ 2 J: erase whole display.
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td></td>
<td>ESC [ 3 J: erase whole display including scroll-back
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td></td>
<td> buffer (since Linux 3.0).
</td>
</tr>
<tr VALIGN=top>
<td>K</td>
<td>EL</td>
<td>Erase line (default: from cursor to end of line).
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td></td>
<td>ESC [ 1 K: erase from start of line to cursor.
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td></td>
<td>ESC [ 2 K: erase whole line.
</td>
</tr>
<tr VALIGN=top>
<td>L</td>
<td>IL</td>
<td>Insert the indicated # of blank lines.
</td>
</tr>
<tr VALIGN=top>
<td>M</td>
<td>DL</td>
<td>Delete the indicated # of lines.
</td>
</tr>
<tr VALIGN=top>
<td>P</td>
<td>DCH</td>
<td>Delete the indicated # of characters on current line.
</td>
</tr>
<tr VALIGN=top>
<td>X</td>
<td>ECH</td>
<td>Erase the indicated # of characters on current line.
</td>
</tr>
<tr VALIGN=top>
<td>a</td>
<td>HPR</td>
<td>Move cursor right the indicated # of columns.
</td>
</tr>
<tr VALIGN=top>
<td>c</td>
<td>DA</td>
<td>Answer ESC [ ? 6 c: &quot;I am a VT102&quot;.
</td>
</tr>
<tr VALIGN=top>
<td>d</td>
<td>VPA</td>
<td>Move cursor to the indicated row, current column.
</td>
</tr>
<tr VALIGN=top>
<td>e</td>
<td>VPR</td>
<td>Move cursor down the indicated # of rows.
</td>
</tr>
<tr VALIGN=top>
<td>f</td>
<td>HVP</td>
<td>Move cursor to the indicated row, column.
</td>
</tr>
<tr VALIGN=top>
<td>g</td>
<td>TBC</td>
<td>Without parameter: clear tab stop at current position.
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td></td>
<td>ESC [ 3 g: delete all tab stops.
</td>
</tr>
<tr VALIGN=top>
<td>h</td>
<td>SM</td>
<td>Set Mode (see below).
</td>
</tr>
<tr VALIGN=top>
<td>l</td>
<td>RM</td>
<td>Reset Mode (see below).
</td>
</tr>
<tr VALIGN=top>
<td>m</td>
<td>SGR</td>
<td>Set attributes (see below).
</td>
</tr>
<tr VALIGN=top>
<td>n</td>
<td>DSR</td>
<td>Status report (see below).
</td>
</tr>
<tr VALIGN=top>
<td>q</td>
<td>DECLL</td>
<td>Set keyboard LEDs.
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td></td>
<td>ESC [ 0 q: clear all LEDs
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td></td>
<td>ESC [ 1 q: set Scroll Lock LED
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td></td>
<td>ESC [ 2 q: set Num Lock LED
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td></td>
<td>ESC [ 3 q: set Caps Lock LED
</td>
</tr>
<tr VALIGN=top>
<td>r</td>
<td>DECSTBM</td>
<td>Set scrolling region; parameters are top and bottom row.
</td>
</tr>
<tr VALIGN=top>
<td>s</td>
<td>?</td>
<td>Save cursor location.
</td>
</tr>
<tr VALIGN=top>
<td>u</td>
<td>?</td>
<td>Restore cursor location.
</td>
</tr>
<tr VALIGN=top>
<td>`</td>
<td>HPA</td>
<td>Move cursor to indicated column in current row.
</td>
</tr>
</table>
<p> <code>ECMA-48 Set Graphics Rendition</code> The ECMA-48 SGR sequence ESC [ <i>parameters</i> m sets display attributes. Several attributes can be set in the same sequence, separated by semicolons. An empty parameter (between semicolons or string initiator or terminator) is interpreted as a zero. </p>
<table>
<tr VALIGN=top>
<td>param</td>
<td>result
</td>
</tr>
<tr VALIGN=top>
<td>0</td>
<td>reset all attributes to their defaults
</td>
</tr>
<tr VALIGN=top>
<td>1</td>
<td>set bold
</td>
</tr>
<tr VALIGN=top>
<td>2</td>
<td>set half-bright (simulated with color on a color display)
</td>
</tr>
<tr VALIGN=top>
<td>4</td>
<td> set underscore (simulated with color on a color display) (the colors used to simulate dim or underline are set using ESC ] &#8230;)
</td>
</tr>
<tr VALIGN=top>
<td>5</td>
<td>set blink
</td>
</tr>
<tr VALIGN=top>
<td>7</td>
<td>set reverse video
</td>
</tr>
<tr VALIGN=top>
<td>10</td>
<td> reset selected mapping, display control flag, and toggle meta flag (ECMA-48 says &quot;primary font&quot;).
</td>
</tr>
<tr VALIGN=top>
<td>11</td>
<td> select null mapping, set display control flag, reset toggle meta flag (ECMA-48 says &quot;first alternate font&quot;).
</td>
</tr>
<tr VALIGN=top>
<td>12</td>
<td> select null mapping, set display control flag, set toggle meta flag (ECMA-48 says &quot;second alternate font&quot;). The toggle meta flag causes the high bit of a byte to be toggled before the mapping table translation is done.
</td>
</tr>
<tr VALIGN=top>
<td>21</td>
<td> set underline; before Linux 4.17, this value set normal intensity (as is done in many other terminals)
</td>
</tr>
<tr VALIGN=top>
<td>22</td>
<td>set normal intensity
</td>
</tr>
<tr VALIGN=top>
<td>24</td>
<td>underline off
</td>
</tr>
<tr VALIGN=top>
<td>25</td>
<td>blink off
</td>
</tr>
<tr VALIGN=top>
<td>27</td>
<td>reverse video off
</td>
</tr>
<tr VALIGN=top>
<td>30</td>
<td>set black foreground
</td>
</tr>
<tr VALIGN=top>
<td>31</td>
<td>set red foreground
</td>
</tr>
<tr VALIGN=top>
<td>32</td>
<td>set green foreground
</td>
</tr>
<tr VALIGN=top>
<td>33</td>
<td>set brown foreground
</td>
</tr>
<tr VALIGN=top>
<td>34</td>
<td>set blue foreground
</td>
</tr>
<tr VALIGN=top>
<td>35</td>
<td>set magenta foreground
</td>
</tr>
<tr VALIGN=top>
<td>36</td>
<td>set cyan foreground
</td>
</tr>
<tr VALIGN=top>
<td>37</td>
<td>set white foreground
</td>
</tr>
<tr VALIGN=top>
<td>38</td>
<td> 256/24-bit foreground color follows, shoehorned into 16 basic colors (before Linux 3.16: set underscore on, set default foreground color)
</td>
</tr>
<tr VALIGN=top>
<td>39</td>
<td> set default foreground color (before Linux 3.16: set underscore off, set default foreground color)
</td>
</tr>
<tr VALIGN=top>
<td>40</td>
<td>set black background
</td>
</tr>
<tr VALIGN=top>
<td>41</td>
<td>set red background
</td>
</tr>
<tr VALIGN=top>
<td>42</td>
<td>set green background
</td>
</tr>
<tr VALIGN=top>
<td>43</td>
<td>set brown background
</td>
</tr>
<tr VALIGN=top>
<td>44</td>
<td>set blue background
</td>
</tr>
<tr VALIGN=top>
<td>45</td>
<td>set magenta background
</td>
</tr>
<tr VALIGN=top>
<td>46</td>
<td>set cyan background
</td>
</tr>
<tr VALIGN=top>
<td>47</td>
<td>set white background
</td>
</tr>
<tr VALIGN=top>
<td>48</td>
<td> 256/24-bit background color follows, shoehorned into 8 basic colors
</td>
</tr>
<tr VALIGN=top>
<td>49</td>
<td>set default background color
</td>
</tr>
<tr VALIGN=top>
<td>90..97</td>
<td>set foreground to bright versions of 30..37
</td>
</tr>
<tr VALIGN=top>
<td>100.107</td>
<td>set background, same as 40..47 (bright not supported)
</td>
</tr>
</table>
<p> Commands 38 and 48 require further arguments: </p>
<table>
<tr VALIGN=top>
<td>;5;x</td>
<td> 256 color: values 0..15 are IBGR (black, red, green, &#8230; white), 16..231 a 6x6x6 color cube, 232..255 a grayscale ramp
</td>
</tr>
<tr VALIGN=top>
<td>;2;r;g;b</td>
<td>24-bit color, r/g/b components are in the range 0..255
</td>
</tr>
</table>
<p> <code>ECMA-48 Mode Switches</code></p>
<dl>
<dt>ESC [ 3 h</p>
<dd>DECCRM (default off): Display control chars.</p>
<dt>ESC [ 4 h</p>
<dd>DECIM (default off): Set insert mode.</p>
<dt>ESC [ 20 h</p>
<dd>LF/NL (default off): Automatically follow echo of LF, VT or FF with CR.</dl>
<p> <code>ECMA-48 Status Report Commands</code></p>
<dl>
<dt>ESC [ 5 n</p>
<dd>Device status report (DSR): Answer is ESC [ 0 n (Terminal OK).</p>
<dt>ESC [ 6 n</p>
<dd>Cursor position report (CPR): Answer is ESC [ <i>y</i> ; <i>x</i> R, where <i>x,y</i> is the cursor location.</dl>
<p> <code>DEC Private Mode (DECSET/DECRST) sequences</code> These are not described in ECMA-48. We list the Set Mode sequences; the Reset Mode sequences are obtained by replacing the final &#8216;h&#8217; by &#8216;l&#8217;.</p>
<dl>
<dt>ESC [ ? 1 h</p>
<dd>DECCKM (default off): When set, the cursor keys send an ESC O prefix, rather than ESC [.</p>
<dt>ESC [ ? 3 h</p>
<dd>DECCOLM (default off = 80 columns): 80/132 col mode switch. The driver sources note that this alone does not suffice; some user-mode utility such as <code><a href="/docs/linux/man/8-resizecons/">resizecons</a></code>(8) has to change the hardware registers on the console video card.</p>
<dt>ESC [ ? 5 h</p>
<dd>DECSCNM (default off): Set reverse-video mode.</p>
<dt>ESC [ ? 6 h</p>
<dd>DECOM (default off): When set, cursor addressing is relative to the upper left corner of the scrolling region.</p>
<dt>ESC [ ? 7 h</p>
<dd>DECAWM (default on): Set autowrap on. In this mode, a graphic character emitted after column 80 (or column 132 of DECCOLM is on) forces a wrap to the beginning of the following line first.</p>
<dt>ESC [ ? 8 h</p>
<dd>DECARM (default on): Set keyboard autorepeat on.</p>
<dt>ESC [ ? 9 h</p>
<dd>X10 Mouse Reporting (default off): Set reporting mode to 1 (or reset to 0)&#8212;see below.</p>
<dt>ESC [ ? 25 h</p>
<dd>DECTECM (default on): Make cursor visible.</p>
<dt>ESC [ ? 1000 h</p>
<dd>X11 Mouse Reporting (default off): Set reporting mode to 2 (or reset to 0)&#8212;see below.</dl>
<p> <code>Linux Console Private CSI Sequences</code> The following sequences are neither ECMA-48 nor native VT102. They are native to the Linux console driver. Colors are in SGR parameters: 0 = black, 1 = red, 2 = green, 3 = brown, 4 = blue, 5 = magenta, 6 = cyan, 7 = white; 8-15 = bright versions of 0-7. </p>
<table>
<tr VALIGN=top>
<td>ESC [ 1 ; <i>n</i> ]</td>
<td>Set color <i>n</i> as the underline color.
</td>
</tr>
<tr VALIGN=top>
<td>ESC [ 2 ; <i>n</i> ]</td>
<td>Set color <i>n</i> as the dim color.
</td>
</tr>
<tr VALIGN=top>
<td>ESC [ 8 ] </td>
<td>Make the current color pair the default attributes.
</td>
</tr>
<tr VALIGN=top>
<td>ESC [ 9 ; <i>n</i> ]</td>
<td>Set screen blank timeout to <i>n</i> minutes.
</td>
</tr>
<tr VALIGN=top>
<td>ESC [ 10 ; <i>n</i> ]</td>
<td>Set bell frequency in Hz.
</td>
</tr>
<tr VALIGN=top>
<td>ESC [ 11 ; <i>n</i> ]</td>
<td>Set bell duration in msec.
</td>
</tr>
<tr VALIGN=top>
<td>ESC [ 12 ; <i>n</i> ]</td>
<td>Bring specified console to the front.
</td>
</tr>
<tr VALIGN=top>
<td>ESC [ 13 ] </td>
<td>Unblank the screen.
</td>
</tr>
<tr VALIGN=top>
<td>ESC [ 14 ; <i>n</i> ] </td>
<td>Set the VESA powerdown interval in minutes.
</td>
</tr>
<tr VALIGN=top>
<td>ESC [ 15 ]</td>
<td> Bring the previous console to the front (since Linux 2.6.0).
</td>
</tr>
<tr VALIGN=top>
<td>ESC [ 16 ; <i>n</i> ]</td>
<td> Set the cursor blink interval in milliseconds (since Linux 4.2).
</td>
</tr>
</table>
<h3>Character sets</h3>
<p>The kernel knows about 4 translations of bytes into console-screen symbols. The four tables are: a) Latin1 -&gt; PC, b) VT100 graphics -&gt; PC, c) PC -&gt; PC, d) user-defined. There are two character sets, called G0 and G1, and one of them is the current character set. (Initially G0.) Typing <code>haN</code> causes G1 to become current, <code>haO</code> causes G0 to become current. These variables G0 and G1 point at a translation table, and can be changed by the user. Initially they point at tables a) and b), respectively. The sequences ESC ( B and ESC ( 0 and ESC ( U and ESC ( K cause G0 to point at translation table a), b), c) and d), respectively. The sequences ESC ) B and ESC ) 0 and ESC ) U and ESC ) K cause G1 to point at translation table a), b), c) and d), respectively. The sequence ESC c causes a terminal reset, which is what you want if the screen is all garbled. The oft-advised &quot;echo haVhaO&quot; will make only G0 current, but there is no guarantee that G0 points at table a). In some distributions there is a program <code><a href="/docs/linux/man/1-reset/">reset</a></code>(1) that just does &quot;echo ha[c&quot;. If your terminfo entry for the console is correct (and has an entry rs1=\Ec), then &quot;tput reset&quot; will also work. The user-defined mapping table can be set using <code><a href="/docs/linux/man/8-mapscrn/">mapscrn</a></code>(8). The result of the mapping is that if a symbol c is printed, the symbol s = map[c] is sent to the video memory. The bitmap that corresponds to s is found in the character ROM, and can be changed using <code><a href="/docs/linux/man/8-setfont/">setfont</a></code>(8).</p>
<h3>Mouse tracking</h3>
<p>The mouse tracking facility is intended to return <code><a href="/docs/linux/man/1-xterm/">xterm</a></code>(1)-compatible mouse status reports. Because the console driver has no way to know the device or type of the mouse, these reports are returned in the console input stream only when the virtual terminal driver receives a mouse update ioctl. These ioctls must be generated by a mouse-aware user-mode application such as the <code><a href="/docs/linux/man/8-gpm/">gpm</a></code>(8) daemon. The mouse tracking escape sequences generated by <code><a href="/docs/linux/man/1-xterm/">xterm</a></code>(1) encode numeric parameters in a single character as <i>value</i>+040. For example, &#8216;!&#8217; is 1. The screen coordinate system is 1-based. The X10 compatibility mode sends an escape sequence on button press encoding the location and the mouse button pressed. It is enabled by sending ESC [ ? 9 h and disabled with ESC [ ? 9 l. On button press, <code><a href="/docs/linux/man/1-xterm/">xterm</a></code>(1) sends ESC [ M <i>bxy</i> (6 characters). Here <i>b</i> is button-1, and <i>x</i> and <i>y</i> are the x and y coordinates of the mouse when the button was pressed. This is the same code the kernel also produces. Normal tracking mode (not implemented in Linux 2.0.24) sends an escape sequence on both button press and release. Modifier information is also sent. It is enabled by sending ESC [ ? 1000 h and disabled with ESC [ ? 1000 l. On button press or release, <code><a href="/docs/linux/man/1-xterm/">xterm</a></code>(1) sends ESC [ M <i>bxy</i>. The low two bits of <i>b</i> encode button information: 0=MB1 pressed, 1=MB2 pressed, 2=MB3 pressed, 3=release. The upper bits encode what modifiers were down when the button was pressed and are added together: 4=Shift, 8=Meta, 16=Control. Again <i>x</i> and <i>y</i> are the x and y coordinates of the mouse event. The upper left corner is (1,1).</p>
<h3>Comparisons with other terminals</h3>
<p>Many different terminal types are described, like the Linux console, as being &quot;VT100-compatible&quot;. Here we discuss differences between the Linux console and the two most important others, the DEC VT102 and <code><a href="/docs/linux/man/1-xterm/">xterm</a></code>(1). <code>Control-character handling</code> The VT102 also recognized the following control characters:</p>
<dl>
<dd>NUL (0x00) was ignored;</p>
<dd>ENQ (0x05) triggered an answerback message;</p>
<dd>DC1 (0x11, <code>haQ</code>, XON) resumed transmission;</p>
<dd>DC3 (0x13, <code>haS</code>, XOFF) caused VT100 to ignore (and stop transmitting) all codes except XOFF and XON.</dl>
<p> VT100-like DC1/DC3 processing may be enabled by the terminal driver. The <code><a href="/docs/linux/man/1-xterm/">xterm</a></code>(1) program (in VT100 mode) recognizes the control characters BEL, BS, HT, LF, VT, FF, CR, SO, SI, ESC. <code>Escape sequences</code> VT100 console sequences not implemented on the Linux console: </p>
<table>
<tr VALIGN=top>
<td>ESC N</td>
<td>SS2</td>
<td>Single shift 2. (Select G2 character set for the next
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td></td>
<td>character only.)
</td>
</tr>
<tr VALIGN=top>
<td>ESC O</td>
<td>SS3</td>
<td>Single shift 3. (Select G3 character set for the next
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td></td>
<td>character only.)
</td>
</tr>
<tr VALIGN=top>
<td>ESC P</td>
<td>DCS</td>
<td>Device control string (ended by ESC \)
</td>
</tr>
<tr VALIGN=top>
<td>ESC X</td>
<td>SOS</td>
<td>Start of string.
</td>
</tr>
<tr VALIGN=top>
<td>ESC ha</td>
<td>PM</td>
<td>Privacy message (ended by ESC \)
</td>
</tr>
<tr VALIGN=top>
<td>ESC \</td>
<td>ST</td>
<td>String terminator
</td>
</tr>
<tr VALIGN=top>
<td>ESC * &#8230;</td>
<td></td>
<td>Designate G2 character set
</td>
</tr>
<tr VALIGN=top>
<td>ESC + &#8230;</td>
<td></td>
<td>Designate G3 character set
</td>
</tr>
</table>
<p> The program <code><a href="/docs/linux/man/1-xterm/">xterm</a></code>(1) (in VT100 mode) recognizes ESC c, ESC # 8, ESC &gt;, ESC =, ESC D, ESC E, ESC H, ESC M, ESC N, ESC O, ESC P &#8230; ESC \, ESC Z (it answers ESC [ ? 1 ; 2 c, &quot;I am a VT100 with advanced video option&quot;) and ESC ha &#8230; ESC \ with the same meanings as indicated above. It accepts ESC (, ESC ), ESC *, ESC + followed by 0, A, B for the DEC special character and line drawing set, UK, and US-ASCII, respectively. The user can configure <code><a href="/docs/linux/man/1-xterm/">xterm</a></code>(1) to respond to VT220-specific control sequences, and it will identify itself as a VT52, VT100, and up depending on the way it is configured and initialized. It accepts ESC ] (OSC) for the setting of certain resources. In addition to the ECMA-48 string terminator (ST), <code><a href="/docs/linux/man/1-xterm/">xterm</a></code>(1) accepts a BEL to terminate an OSC string. These are a few of the OSC control sequences recognized by <code><a href="/docs/linux/man/1-xterm/">xterm</a></code>(1): </p>
<table>
<tr VALIGN=top>
<td>ESC ] 0 ; <i>txt</i> ST</td>
<td>Set icon name and window title to <i>txt</i>.
</td>
</tr>
<tr VALIGN=top>
<td>ESC ] 1 ; <i>txt</i> ST</td>
<td>Set icon name to <i>txt</i>.
</td>
</tr>
<tr VALIGN=top>
<td>ESC ] 2 ; <i>txt</i> ST</td>
<td>Set window title to <i>txt</i>.
</td>
</tr>
<tr VALIGN=top>
<td>ESC ] 4 ; <i>num</i>; <i>txt</i> ST</td>
<td>Set ANSI color <i>num</i> to <i>txt</i>.
</td>
</tr>
<tr VALIGN=top>
<td>ESC ] 10 ; <i>txt</i> ST</td>
<td>Set dynamic text color to <i>txt</i>.
</td>
</tr>
<tr VALIGN=top>
<td>ESC ] 4 6 ; <i>name</i> ST</td>
<td>Change log file to <i>name</i> (normally disabled
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>by a compile-time option)
</td>
</tr>
<tr VALIGN=top>
<td>ESC ] 5 0 ; <i>fn</i> ST</td>
<td>Set font to <i>fn</i>.
</td>
</tr>
</table>
<p> It recognizes the following with slightly modified meaning (saving more state, behaving closer to VT100/VT220): </p>
<table>
<tr VALIGN=top>
<td>ESC 7 DECSC</td>
<td>Save cursor</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>ESC 8 DECRC</td>
<td>Restore cursor</td>
<td>
</td>
</tr>
</table>
<p> It also recognizes </p>
<table>
<tr VALIGN=top>
<td>ESC F</td>
<td></td>
<td>Cursor to lower left corner of screen (if enabled by
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td></td>
<td><code><a href="/docs/linux/man/1-xterm/">xterm</a></code>(1)&#8217;s <code>hpLowerleftBugCompat</code> resource)
</td>
</tr>
<tr VALIGN=top>
<td>ESC l</td>
<td></td>
<td>Memory lock (per HP terminals).
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td></td>
<td>Locks memory above the cursor.
</td>
</tr>
<tr VALIGN=top>
<td>ESC m</td>
<td></td>
<td>Memory unlock (per HP terminals).
</td>
</tr>
<tr VALIGN=top>
<td>ESC n</td>
<td>LS2</td>
<td>Invoke the G2 character set.
</td>
</tr>
<tr VALIGN=top>
<td>ESC o</td>
<td>LS3</td>
<td>Invoke the G3 character set.
</td>
</tr>
<tr VALIGN=top>
<td>ESC |</td>
<td>LS3R</td>
<td>Invoke the G3 character set as GR.
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td></td>
<td>Has no visible effect in xterm.
</td>
</tr>
<tr VALIGN=top>
<td>ESC }</td>
<td>LS2R</td>
<td>Invoke the G2 character set as GR.
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td></td>
<td>Has no visible effect in xterm.
</td>
</tr>
<tr VALIGN=top>
<td>ESC ~</td>
<td>LS1R</td>
<td>Invoke the G1 character set as GR.
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td></td>
<td>Has no visible effect in xterm.
</td>
</tr>
</table>
<p> It also recognizes ESC % and provides a more complete UTF-8 implementation than Linux console. <code>CSI Sequences</code> Old versions of <code><a href="/docs/linux/man/1-xterm/">xterm</a></code>(1), for example, from X11R5, interpret the blink SGR as a bold SGR. Later versions which implemented ANSI colors, for example, XFree86 3.1.2A in 1995, improved this by allowing the blink attribute to be displayed as a color. Modern versions of xterm implement blink SGR as blinking text and still allow colored text as an alternate rendering of SGRs. Stock X11R6 versions did not recognize the color-setting SGRs until the X11R6.8 release, which incorporated XFree86 xterm. All ECMA-48 CSI sequences recognized by Linux are also recognized by <i>xterm</i>, however <code><a href="/docs/linux/man/1-xterm/">xterm</a></code>(1) implements several ECMA-48 and DEC control sequences not recognized by Linux. The <code><a href="/docs/linux/man/1-xterm/">xterm</a></code>(1) program recognizes all of the DEC Private Mode sequences listed above, but none of the Linux private-mode sequences. For discussion of <code><a href="/docs/linux/man/1-xterm/">xterm</a></code>(1)&#8217;s own private-mode sequences, refer to the <i>Xterm Control Sequences</i> document by Edward Moy, Stephen Gildea, and Thomas E. Dickey available with the X distribution. That document, though terse, is much longer than this manual page. For a chronological overview,  details changes to xterm. The <i>vttest</i> program  demonstrates many of these control sequences. The <code><a href="/docs/linux/man/1-xterm/">xterm</a></code>(1) source distribution also contains sample scripts which exercise other features.</p>
<h2>Notes</h2>
<p>ESC 8 (DECRC) is not able to restore the character set changed with ESC %.</p>
<h2>Bugs</h2>
<p>In 2.0.23, CSI is broken, and NUL is not ignored inside escape sequences. </p>
<p> Some older kernel versions (after 2.0) interpret 8-bit control sequences. These &quot;C1 controls&quot; use codes between 128 and 159 to replace ESC [, ESC ] and similar two-byte control sequence initiators. There are fragments of that in modern kernels (either overlooked or broken by changes to support UTF-8), but the implementation is incomplete and should be regarded as unreliable. </p>
<p> Linux &quot;private mode&quot; sequences do not follow the rules in ECMA-48 for private mode control sequences. In particular, those ending with ] do not use a standard terminating character. The OSC (set palette) sequence is a greater problem, since <code><a href="/docs/linux/man/1-xterm/">xterm</a></code>(1) may interpret this as a control sequence which requires a string terminator (ST). Unlike the <code><a href="/docs/linux/man/1-setterm/">setterm</a></code>(1) sequences which will be ignored (since they are invalid control sequences), the palette sequence will make <code><a href="/docs/linux/man/1-xterm/">xterm</a></code>(1) appear to hang (though pressing the return-key will fix that). To accommodate applications which have been hardcoded to use Linux control sequences, set the <code><a href="/docs/linux/man/1-xterm/">xterm</a></code>(1) resource <code>brokenLinuxOSC</code> to true. </p>
<p> An older version of this document implied that Linux recognizes the ECMA-48 control sequence for invisible text. It is ignored.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/2-ioctl_console/">ioctl_console</a></code>(2), <code><a href="/docs/linux/man/7-charsets/">charsets</a></code>(7)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
