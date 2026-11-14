---
title: "console_ioctl(4)"
name: "console_ioctl"
section: "4"
letter: "c"
url: "/docs/linux/man/4-console_ioctl/"
description: "ioctl_console – ioctls for console terminal and virtual consoles"
---

<p>ioctl_console &#8211; ioctls for console terminal and virtual consoles</p>
<h2>Description</h2>
<p>The following Linux-specific <code><a href="/docs/linux/man/2-ioctl/">ioctl</a></code>(2) requests are supported for console terminals and virtual consoles. Each requires a third argument, assumed here to be <i>argp</i>.</p>
<dl>
<dt><code>KDGETLED</code></p>
<dd>Get state of LEDs. <i>argp</i> points to a <i>char</i>. The lower three bits of <i>*argp</i> are set to the state of the LEDs, as follows: </p>
<table>
<tr VALIGN=top>
<td>LED_CAP </td>
<td>0x04</td>
<td>caps lock led
</td>
</tr>
<tr VALIGN=top>
<td>LED_NUM </td>
<td>0x02</td>
<td>num lock led
</td>
</tr>
<tr VALIGN=top>
<td>LED_SCR </td>
<td>0x01</td>
<td>scroll lock led
</td>
</tr>
</table>
<dt><code>KDSETLED</code></p>
<dd>Set the LEDs. The LEDs are set to correspond to the lower three bits of the unsigned long integer in <i>argp</i>. However, if a higher order bit is set, the LEDs revert to normal: displaying the state of the keyboard functions of caps lock, num lock, and scroll lock.</dl>
<p> Before Linux 1.1.54, the LEDs just reflected the state of the corresponding keyboard flags, and KDGETLED/KDSETLED would also change the keyboard flags. Since Linux 1.1.54 the LEDs can be made to display arbitrary information, but by default they display the keyboard flags. The following two ioctls are used to access the keyboard flags.</p>
<dl>
<dt><code>KDGKBLED</code></p>
<dd>Get keyboard flags CapsLock, NumLock, ScrollLock (not lights). <i>argp</i> points to a char which is set to the flag state. The low order three bits (mask 0x7) get the current flag state, and the low order bits of the next nibble (mask 0x70) get the default flag state. (Since Linux 1.1.54.)</p>
<dt><code>KDSKBLED</code></p>
<dd>Set keyboard flags CapsLock, NumLock, ScrollLock (not lights). <i>argp</i> is an unsigned long integer that has the desired flag state. The low order three bits (mask 0x7) have the flag state, and the low order bits of the next nibble (mask 0x70) have the default flag state. (Since Linux 1.1.54.)</p>
<dt><code>KDGKBTYPE</code></p>
<dd>Get keyboard type. This returns the value KB_101, defined as 0x02.</p>
<dt><code>KDADDIO</code></p>
<dd>Add I/O port as valid. Equivalent to <i>ioperm(arg,1,1)</i>.</p>
<dt><code>KDDELIO</code></p>
<dd>Delete I/O port as valid. Equivalent to <i>ioperm(arg,1,0)</i>.</p>
<dt><code>KDENABIO</code></p>
<dd>Enable I/O to video board. Equivalent to <i>ioperm(0x3b4, 0x3df-0x3b4+1, 1)</i>.</p>
<dt><code>KDDISABIO</code></p>
<dd>Disable I/O to video board. Equivalent to <i>ioperm(0x3b4, 0x3df-0x3b4+1, 0)</i>.</p>
<dt><code>KDSETMODE</code></p>
<dd>Set text/graphics mode. <i>argp</i> is an unsigned integer containing one of: </p>
<table>
<tr VALIGN=top>
<td>KD_TEXT</td>
<td>0x00
</td>
</tr>
<tr VALIGN=top>
<td>KD_GRAPHICS</td>
<td>0x01
</td>
</tr>
</table>
<dt><code>KDGETMODE</code></p>
<dd>Get text/graphics mode. <i>argp</i> points to an <i>int</i> which is set to one of the values shown above for <code>KDSETMODE</code>.</p>
<dt><code>KDMKTONE</code></p>
<dd>Generate tone of specified length. The lower 16 bits of the unsigned long integer in <i>argp</i> specify the period in clock cycles, and the upper 16 bits give the duration in msec. If the duration is zero, the sound is turned off. Control returns immediately. For example, <i>argp</i> = (125&lt;&lt;16) + 0x637 would specify the beep normally associated with a ctrl-G. (Thus since Linux 0.99pl1; broken in Linux 2.1.49-50.)</p>
<dt><code>KIOCSOUND</code></p>
<dd>Start or stop sound generation. The lower 16 bits of <i>argp</i> specify the period in clock cycles (that is, <i>argp</i> = 1193180/frequency). <i>argp</i> = 0 turns sound off. In either case, control returns immediately.</p>
<dt><code>GIO_CMAP</code></p>
<dd>Get the current default color map from kernel. <i>argp</i> points to a 48-byte array. (Since Linux 1.3.3.)</p>
<dt><code>PIO_CMAP</code></p>
<dd>Change the default text-mode color map. <i>argp</i> points to a 48-byte array which contains, in order, the Red, Green, and Blue values for the 16 available screen colors: 0 is off, and 255 is full intensity. The default colors are, in order: black, dark red, dark green, brown, dark blue, dark purple, dark cyan, light grey, dark grey, bright red, bright green, yellow, bright blue, bright purple, bright cyan and white. (Since Linux 1.3.3.)</p>
<dt><code>GIO_FONT</code></p>
<dd>Gets 256-character screen font in expanded form. <i>argp</i> points to an 8192-byte array. Fails with error code <code>EINVAL</code> if the currently loaded font is a 512-character font, or if the console is not in text mode.</p>
<dt><code>GIO_FONTX</code></p>
<dd>Gets screen font and associated information. <i>argp</i> points to a <i>struct consolefontdesc</i> (see <code>PIO_FONTX</code>). On call, the <i>charcount</i> field should be set to the maximum number of characters that would fit in the buffer pointed to by <i>chardata</i>. On return, the <i>charcount</i> and <i>charheight</i> are filled with the respective data for the currently loaded font, and the <i>chardata</i> array contains the font data if the initial value of <i>charcount</i> indicated enough space was available; otherwise the buffer is untouched and <i>errno</i> is set to <code>ENOMEM</code>. (Since Linux 1.3.1.)</p>
<dt><code>PIO_FONT</code></p>
<dd>Sets 256-character screen font. Load font into the EGA/VGA character generator. <i>argp</i> points to an 8192-byte map, with 32 bytes per character. Only the first <i>N</i> of them are used for an 8x<i>N</i> font (0 &lt; <i>N</i> &lt;= 32). This call also invalidates the Unicode mapping.</p>
<dt><code>PIO_FONTX</code></p>
<dd>Sets screen font and associated rendering information. <i>argp</i> points to a</p>
<dd>struct consolefontdesc {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned short charcount;&nbsp;<wbr>&nbsp;/*&nbsp;characters in font<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(256 or 512)&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned short charheight;&nbsp;/*&nbsp;scan lines per<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;character&nbsp;(1-32)&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;*chardata;&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;font data in<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;expanded form&nbsp;*/ };</p>
<dd>If necessary, the screen will be appropriately resized, and <code>SIGWINCH</code> sent to the appropriate processes. This call also invalidates the Unicode mapping. (Since Linux 1.3.1.)</p>
<dt><code>PIO_FONTRESET</code></p>
<dd>Resets the screen font, size and Unicode mapping to the bootup defaults. <i>argp</i> is unused, but should be set to NULL to ensure compatibility with future versions of Linux. (Since Linux 1.3.28.)</p>
<dt><code>GIO_SCRNMAP</code></p>
<dd>Get screen mapping from kernel. <i>argp</i> points to an area of size E_TABSZ, which is loaded with the font positions used to display each character. This call is likely to return useless information if the currently loaded font is more than 256 characters.</p>
<dt><code>GIO_UNISCRNMAP</code></p>
<dd>Get full Unicode screen mapping from kernel. <i>argp</i> points to an area of size <i>E_TABSZ*sizeof(unsigned short)</i>, which is loaded with the Unicodes each character represent. A special set of Unicodes, starting at U+F000, are used to represent &quot;direct to font&quot; mappings. (Since Linux 1.3.1.)</p>
<dt><code>PIO_SCRNMAP</code></p>
<dd>Loads the &quot;user definable&quot; (fourth) table in the kernel which maps bytes into console screen symbols. <i>argp</i> points to an area of size E_TABSZ.</p>
<dt><code>PIO_UNISCRNMAP</code></p>
<dd>Loads the &quot;user definable&quot; (fourth) table in the kernel which maps bytes into Unicodes, which are then translated into screen symbols according to the currently loaded Unicode-to-font map. Special Unicodes starting at U+F000 can be used to map directly to the font symbols. (Since Linux 1.3.1.)</p>
<dt><code>GIO_UNIMAP</code></p>
<dd>Get Unicode-to-font mapping from kernel. <i>argp</i> points to a</p>
<dd>struct unimapdesc {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned short&nbsp;<wbr>&nbsp;entry_ct;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct unipair&nbsp;*entries; };</p>
<dd>where <i>entries</i> points to an array of</p>
<dd>struct unipair {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned short unicode;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned short fontpos; };</p>
<dd>(Since Linux 1.1.92.)</p>
<dt><code>PIO_UNIMAP</code></p>
<dd>Put unicode-to-font mapping in kernel. <i>argp</i> points to a <i>struct unimapdesc</i>. (Since Linux 1.1.92)</p>
<dt><code>PIO_UNIMAPCLR</code></p>
<dd>Clear table, possibly advise hash algorithm. <i>argp</i> points to a</p>
<dd>struct unimapinit {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned short advised_hashsize;&nbsp;<wbr>&nbsp;/*&nbsp;0 if no opinion&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned short advised_hashstep;&nbsp;<wbr>&nbsp;/*&nbsp;0 if no opinion&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned short advised_hashlevel;&nbsp;/*&nbsp;0 if no opinion&nbsp;*/ };</p>
<dd>(Since Linux 1.1.92.)</p>
<dt><code>KDGKBMODE</code></p>
<dd>Gets current keyboard mode. <i>argp</i> points to a <i>long</i> which is set to one of these: </p>
<table>
<tr VALIGN=top>
<td>K_RAW</td>
<td>0x00 /* Raw (scancode) mode */
</td>
</tr>
<tr VALIGN=top>
<td>K_XLATE</td>
<td>0x01 /* Translate keycodes using keymap */
</td>
</tr>
<tr VALIGN=top>
<td>K_MEDIUMRAW</td>
<td>0x02 /* Medium raw (scancode) mode */
</td>
</tr>
<tr VALIGN=top>
<td>K_UNICODE</td>
<td>0x03 /* Unicode mode */
</td>
</tr>
<tr VALIGN=top>
<td>K_OFF</td>
<td>0x04 /* Disabled mode; since Linux 2.6.39 */
</td>
</tr>
</table>
<dt><code>KDSKBMODE</code></p>
<dd>Sets current keyboard mode. <i>argp</i> is a <i>long</i> equal to one of the values shown for <code>KDGKBMODE</code>.</p>
<dt><code>KDGKBMETA</code></p>
<dd>Gets meta key handling mode. <i>argp</i> points to a <i>long</i> which is set to one of these: </p>
<table>
<tr VALIGN=top>
<td>K_METABIT</td>
<td>0x03</td>
<td>set high order bit
</td>
</tr>
<tr VALIGN=top>
<td>K_ESCPREFIX</td>
<td>0x04</td>
<td>escape prefix
</td>
</tr>
</table>
<dt><code>KDSKBMETA</code></p>
<dd>Sets meta key handling mode. <i>argp</i> is a <i>long</i> equal to one of the values shown above for <code>KDGKBMETA</code>.</p>
<dt><code>KDGKBENT</code></p>
<dd>Gets one entry in key translation table (keycode to action code). <i>argp</i> points to a</p>
<dd>struct kbentry {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned char&nbsp;<wbr>&nbsp;kb_table;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned char&nbsp;<wbr>&nbsp;kb_index;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned short kb_value; };</p>
<dd>with the first two members filled in: <i>kb_table</i> selects the key table (0 &lt;= <i>kb_table</i> &lt; MAX_NR_KEYMAPS), and <i>kb_index</i> is the keycode (0 &lt;= <i>kb_index</i> &lt; NR_KEYS). <i>kb_value</i> is set to the corresponding action code, or K_HOLE if there is no such key, or K_NOSUCHMAP if <i>kb_table</i> is invalid.</p>
<dt><code>KDSKBENT</code></p>
<dd>Sets one entry in translation table. <i>argp</i> points to a <i>struct kbentry</i>.</p>
<dt><code>KDGKBSENT</code></p>
<dd>Gets one function key string. <i>argp</i> points to a</p>
<dd>struct kbsentry {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned char kb_func;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned char kb_string[512]; };</p>
<dd><i>kb_string</i> is set to the (null-terminated) string corresponding to the <i>kb_func</i>th function key action code.</p>
<dt><code>KDSKBSENT</code></p>
<dd>Sets one function key string entry. <i>argp</i> points to a <i>struct kbsentry</i>.</p>
<dt><code>KDGKBDIACR</code></p>
<dd>Read kernel accent table. <i>argp</i> points to a</p>
<dd>struct kbdiacrs {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned int&nbsp;<wbr>&nbsp;<wbr>&nbsp;kb_cnt;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct kbdiacr kbdiacr[256]; };</p>
<dd>where <i>kb_cnt</i> is the number of entries in the array, each of which is a</p>
<dd>struct kbdiacr {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned char diacr;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned char base;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned char result; };</p>
<dt><code>KDGETKEYCODE</code></p>
<dd>Read kernel keycode table entry (scan code to keycode). <i>argp</i> points to a</p>
<dd>struct kbkeycode {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned int scancode;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned int keycode; };</p>
<dd><i>keycode</i> is set to correspond to the given <i>scancode</i>. (89 &lt;= <i>scancode</i> &lt;= 255 only. For 1 &lt;= <i>scancode</i> &lt;= 88, <i>keycode</i>==<i>scancode</i>.) (Since Linux 1.1.63.)</p>
<dt><code>KDSETKEYCODE</code></p>
<dd>Write kernel keycode table entry. <i>argp</i> points to a <i>struct kbkeycode</i>. (Since Linux 1.1.63.)</p>
<dt><code>KDSIGACCEPT</code></p>
<dd>The calling process indicates its willingness to accept the signal <i>argp</i> when it is generated by pressing an appropriate key combination. (1 &lt;= <i>argp</i> &lt;= NSIG). (See <i>spawn_console</i>() in <i>linux/drivers/char/keyboard.c</i>.)</p>
<dt><code>VT_OPENQRY</code></p>
<dd>Returns the first available (non-opened) console. <i>argp</i> points to an <i>int</i> which is set to the number of the vt (1 &lt;= <i>*argp</i> &lt;= MAX_NR_CONSOLES).</p>
<dt><code>VT_GETMODE</code></p>
<dd>Get mode of active vt. <i>argp</i> points to a</p>
<dd>struct vt_mode {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;<wbr>&nbsp;mode;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;vt mode&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;<wbr>&nbsp;waitv;&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;if set, hang on writes if not active&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;short relsig;&nbsp;<wbr>&nbsp;/*&nbsp;signal to raise on release req&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;short acqsig;&nbsp;<wbr>&nbsp;/*&nbsp;signal to raise on acquisition&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;short frsig;&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;unused&nbsp;(set to 0)&nbsp;*/ };</p>
<dd>which is set to the mode of the active vt. <i>mode</i> is set to one of these values: </p>
<table>
<tr VALIGN=top>
<td>VT_AUTO</td>
<td>auto vt switching
</td>
</tr>
<tr VALIGN=top>
<td>VT_PROCESS</td>
<td>process controls switching
</td>
</tr>
<tr VALIGN=top>
<td>VT_ACKACQ</td>
<td>acknowledge switch
</td>
</tr>
</table>
<dt><code>VT_SETMODE</code></p>
<dd>Set mode of active vt. <i>argp</i> points to a <i>struct vt_mode</i>.</p>
<dt><code>VT_GETSTATE</code></p>
<dd>Get global vt state info. <i>argp</i> points to a</p>
<dd>struct vt_stat {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned short v_active;&nbsp;<wbr>&nbsp;/*&nbsp;active vt&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned short v_signal;&nbsp;<wbr>&nbsp;/*&nbsp;signal to send&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned short v_state;&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;vt bit mask&nbsp;*/ };</p>
<dd>For each vt in use, the corresponding bit in the <i>v_state</i> member is set. (Kernels 1.0 through 1.1.92.)</p>
<dt><code>VT_RELDISP</code></p>
<dd>Release a display.</p>
<dt><code>VT_ACTIVATE</code></p>
<dd>Switch to vt <i>argp</i> (1 &lt;= <i>argp</i> &lt;= MAX_NR_CONSOLES).</p>
<dt><code>VT_WAITACTIVE</code></p>
<dd>Wait until vt <i>argp</i> has been activated.</p>
<dt><code>VT_DISALLOCATE</code></p>
<dd>Deallocate the memory associated with vt <i>argp</i>. (Since Linux 1.1.54.)</p>
<dt><code>VT_RESIZE</code></p>
<dd>Set the kernel&#8217;s idea of screensize. <i>argp</i> points to a</p>
<dd>struct vt_sizes {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned short v_rows;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;#&nbsp;rows&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned short v_cols;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;#&nbsp;columns&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned short v_scrollsize;&nbsp;/*&nbsp;no longer used&nbsp;*/ };</p>
<dd>Note that this does not change the videomode. See <code><a href="/docs/linux/man/8-resizecons/">resizecons</a></code>(8). (Since Linux 1.1.54.)</p>
<dt><code>VT_RESIZEX</code></p>
<dd>Set the kernel&#8217;s idea of various screen parameters. <i>argp</i> points to a</p>
<dd>struct vt_consize {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned short v_rows;&nbsp;<wbr>&nbsp;/*&nbsp;number of rows&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned short v_cols;&nbsp;<wbr>&nbsp;/*&nbsp;number of columns&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned short v_vlin;&nbsp;<wbr>&nbsp;/*&nbsp;number of pixel rows<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;on screen&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned short v_clin;&nbsp;<wbr>&nbsp;/*&nbsp;number of pixel rows<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;per character&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned short v_vcol;&nbsp;<wbr>&nbsp;/*&nbsp;number of pixel columns<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;on screen&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned short v_ccol;&nbsp;<wbr>&nbsp;/*&nbsp;number of pixel columns<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;per character&nbsp;*/ };</p>
<dd>Any parameter may be set to zero, indicating &quot;no change&quot;, but if multiple parameters are set, they must be self-consistent. Note that this does not change the videomode. See <code><a href="/docs/linux/man/8-resizecons/">resizecons</a></code>(8). (Since Linux 1.3.3.)</dl>
<p> The action of the following ioctls depends on the first byte in the struct pointed to by <i>argp</i>, referred to here as the <i>subcode</i>. These are legal only for the superuser or the owner of the current terminal.</p>
<dl>
<dt><code>TIOCLINUX, subcode=0</code></p>
<dd>Dump the screen. Disappeared in Linux 1.1.92. (With kernel 1.1.92 or later, read from <i>/dev/vcsN</i> or <i>/dev/vcsaN</i> instead.)</p>
<dt><code>TIOCLINUX, subcode=1</code></p>
<dd>Get task information. Disappeared in Linux 1.1.92.</p>
<dt><code>TIOCLINUX, subcode=2</code></p>
<dd>Set selection. <i>argp</i> points to a</p>
<dd>struct {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;<wbr>&nbsp;subcode;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;short xs, ys, xe, ye;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;short sel_mode; };</p>
<dd><i>xs</i> and <i>ys</i> are the starting column and row. <i>xe</i> and <i>ye</i> are the ending column and row. (Upper left corner is row=column=1.) <i>sel_mode</i> is 0 for character-by-character selection, 1 for word-by-word selection, or 2 for line-by-line selection. The indicated screen characters are highlighted and saved in the static array sel_buffer in <i>devices/char/console.c</i>.</p>
<dt><code>TIOCLINUX, subcode=3</code></p>
<dd>Paste selection. The characters in the selection buffer are written to <i>fd</i>.</p>
<dt><code>TIOCLINUX, subcode=4</code></p>
<dd>Unblank the screen.</p>
<dt><code>TIOCLINUX, subcode=5</code></p>
<dd>Sets contents of a 256-bit look up table defining characters in a &quot;word&quot;, for word-by-word selection. (Since Linux 1.1.32.)</p>
<dt><code>TIOCLINUX, subcode=6</code></p>
<dd><i>argp</i> points to a char which is set to the value of the kernel variable <i>shift_state</i>. (Since Linux 1.1.32.)</p>
<dt><code>TIOCLINUX, subcode=7</code></p>
<dd><i>argp</i> points to a char which is set to the value of the kernel variable <i>report_mouse</i>. (Since Linux 1.1.33.)</p>
<dt><code>TIOCLINUX, subcode=8</code></p>
<dd>Dump screen width and height, cursor position, and all the character-attribute pairs. (Kernels 1.1.67 through 1.1.91 only. With kernel 1.1.92 or later, read from <i>/dev/vcsa*</i> instead.)</p>
<dt><code>TIOCLINUX, subcode=9</code></p>
<dd>Restore screen width and height, cursor position, and all the character-attribute pairs. (Kernels 1.1.67 through 1.1.91 only. With kernel 1.1.92 or later, write to <i>/dev/vcsa*</i> instead.)</p>
<dt><code>TIOCLINUX, subcode=10</code></p>
<dd>Handles the Power Saving feature of the new generation of monitors. VESA screen blanking mode is set to <i>argp[1]</i>, which governs what screen blanking does:</p>
<dl>
<dd>
<dl>
<dt>0:</p>
<dd>Screen blanking is disabled.</p>
<dt>1:</p>
<dd>The current video adapter register settings are saved, then the controller is programmed to turn off the vertical synchronization pulses. This puts the monitor into &quot;standby&quot; mode. If your monitor has an Off_Mode timer, then it will eventually power down by itself.</p>
<dt>2:</p>
<dd>The current settings are saved, then both the vertical and horizontal synchronization pulses are turned off. This puts the monitor into &quot;off&quot; mode. If your monitor has no Off_Mode timer, or if you want your monitor to power down immediately when the blank_timer times out, then you choose this option. (<i>Caution:</i> Powering down frequently will damage the monitor.) (Since Linux 1.1.76.)</dl>
</dl>
</dl>
<h2>Return Value</h2>
<p>On success, 0 is returned. On error, -1 is returned, and <i>errno</i> is set.</p>
<h2>Errors</h2>
<p><i>errno</i> may take on these values:</p>
<dl>
<dt><code>EBADF</code></p>
<dd>The file descriptor is invalid.</p>
<dt><code>EINVAL</code></p>
<dd>The file descriptor or <i>argp</i> is invalid.</p>
<dt><code>ENOTTY</code></p>
<dd>The file descriptor is not associated with a character special device, or the specified request does not apply to it.</p>
<dt><code>EPERM</code></p>
<dd>Insufficient permission.</dl>
<h2>Notes</h2>
<p><code>Warning</code>: Do not regard this man page as documentation of the Linux console ioctls. This is provided for the curious only, as an alternative to reading the source. Ioctl&#8217;s are undocumented Linux internals, liable to be changed without warning. (And indeed, this page more or less describes the situation as of kernel version 1.1.94; there are many minor and not-so-minor differences with earlier versions.) </p>
<p> Very often, ioctls are introduced for communication between the kernel and one particular well-known program (fdisk, hdparm, setserial, tunelp, loadkeys, selection, setfont, etc.), and their behavior will be changed when required by this particular program. </p>
<p> Programs using these ioctls will not be portable to other versions of UNIX, will not work on older versions of Linux, and will not work on future versions of Linux. </p>
<p> Use POSIX functions.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-dumpkeys/">dumpkeys</a></code>(1), <code><a href="/docs/linux/man/1-kbd_mode/">kbd_mode</a></code>(1), <code><a href="/docs/linux/man/1-loadkeys/">loadkeys</a></code>(1), <code><a href="/docs/linux/man/1-mknod/">mknod</a></code>(1), <code><a href="/docs/linux/man/1-setleds/">setleds</a></code>(1), <code><a href="/docs/linux/man/1-setmetamode/">setmetamode</a></code>(1), <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2), <code><a href="/docs/linux/man/2-fcntl/">fcntl</a></code>(2), <code><a href="/docs/linux/man/2-ioctl_tty/">ioctl_tty</a></code>(2), <code><a href="/docs/linux/man/2-ioperm/">ioperm</a></code>(2), <code><a href="/docs/linux/man/3-termios/">termios</a></code>(3), <code><a href="/docs/linux/man/4-console_codes/">console_codes</a></code>(4), <code><a href="/docs/linux/man/4-mt/">mt</a></code>(4), <code><a href="/docs/linux/man/4-sd/">sd</a></code>(4), <code><a href="/docs/linux/man/4-tty/">tty</a></code>(4), <code><a href="/docs/linux/man/4-ttys/">ttyS</a></code>(4), <code><a href="/docs/linux/man/4-vcs/">vcs</a></code>(4), <code><a href="/docs/linux/man/4-vcsa/">vcsa</a></code>(4), <code><a href="/docs/linux/man/7-charsets/">charsets</a></code>(7), <code><a href="/docs/linux/man/8-mapscrn/">mapscrn</a></code>(8), <code><a href="/docs/linux/man/8-resizecons/">resizecons</a></code>(8), <code><a href="/docs/linux/man/8-setfont/">setfont</a></code>(8) </p>
<p> <i>/usr/include/linux/kd.h</i>, <i>/usr/include/linux/vt.h</i></p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
