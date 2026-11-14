---
title: "libvga(5)"
name: "libvga"
section: "5"
letter: "l"
url: "/docs/linux/man/5-libvga/"
description: "libvga.config, svgalibrc – the svgalib configuration file"
---

<p>libvga.config, svgalibrc &#8211; the svgalib configuration file</p>
<h2>Description</h2>
<p>The svgalib configuration is usually located in <i>/etc/vga/libvga.config </i> though one can reconfigure this location when recompiling svgalib. In the configuration file, everything between a <code>#</code> and the end of the line is ignored. Empty lines are also ignored. Since the driver you will use may not know all config options here, unknown commands are silently ignored. Please think of that when something does not work as you expect. I know this is a nuisance because malformed configuration statements do not cause errors. Multiple commands are allowed in one line, and commands can exceed lines. Actually, svgalib simply reads a list of whitespace separated tokens from the file until it finds one it knows and it then assumes the following tokens to be arguments of that command until one is encountered which may not be an argument. New style options are in general case insensitive whereas the old style options are case sensitive. The old style options are included to allow for old config files still being used. For completeness they are documented in the <code>OBSOLETE COMMANDS</code> section. You should not use them anymore. In addition, <code><a href="/docs/linux/man/7-svgalib/">svgalib</a></code>(7) parses the files <i>~/.svgalibrc</i> and the file given in the environment variable <code>SVGALIB_CONFIG_FILE</code>. Finally, the contents of the environment variable <code>SVGALIB_CONFIG</code> are parsed like the files before. Configuration commands which control hardware settings that might cause harm to your hardware are called <code>privileged</code>. By default the <code>privileged</code> commands can only be used in the main configuration file <i>/etc/vga/libvga.config </i> for safety (s.t. a non root user can not cause any harm to your hardware by misconfiguring <code><a href="/docs/linux/man/7-svgalib/">svgalib</a></code>(7)). Enable them in the other locations as well with the command <code>overrideenable</code> in the main config file. <code>BEWARE!</code> This allows every user to change the monitor and clocks (and other configs) and thus damaging the hardware. I <code>strongly</code> discourage the use of <code>overrideenable</code> except for debugging/testing purposes. </p>
<h2>Required Configuration</h2>
<p>Please do not allow the vastness of options to confuse you. Generally svgalib uses well chosen defaults and is able to autodetect everything. Thus generally you don&#8217;t need to specify much. When installing svgalib it provides a sample <i>/etc/vga/libvga.config</i> file which contains most of the required configuration. Just edit it to your needs. </p>
<p> Generally you only need to use:</p>
<dl>
<dt><code>mouse</code></p>
<dd>To specify if you use anything else then a Microsoft compatible mouse.</p>
<dt><code>mdev</code></p>
<dd>If the mouse device file is <code>not</code> <i>/dev/input/mice</i> which is the actual mouse device file. You will usually need to use this command if you want to use the SpaceTec Spaceball device (which is not your usual mouse). </p>
<dt><code>setRTS</code>, <code>clearRTS</code>, <code>leaveRTS</code>, <code>setDTR</code>, <code>clearDTR</code>, and <code>leaveDTR</code></p>
<dd>if your mouse needs it to enter your desired mouse protocol.</p>
<dt><code>monitor</code>, or (better) <code>HorizSync</code> and <code>VertRefresh</code></p>
<dd>to specify the capabilities of your monitor. </p>
</dl>
<h3>If you use the EGA chipset driver</h3>
<dl>
<dt><code>monotext</code> or <code>colortext</code></p>
<dd>to specify if your EGA card is in monochrome or color configuration.</dl>
<h3>If you use the Mach32 chipset driver</h3>
<p>You should consider reading <code><a href="/docs/linux/man/7-svgalib-mach32/">svgalib.mach32</a></code>(7).</p>
<dl>
<dt><code>Clocks </code><i>clock1 clock2 clock3 </i><code>&#8230;</code></p>
<dd>to specify the Mach32 clocks. This is mandatory. However, if you omit it. svgalib will autodetect clocks and modify your <i>/etc/vga/libvga.config</i> file and abort. After this, every svgalib application started will find the proper <code>Clocks</code> command.</p>
<dt><code>mach32eeprom /etc/vga/mach32.eeprom</code></p>
<dd>is recommended to avoid slowish reads of the Mach32 EEPROM which will also cause annoying screen flickering.</dl>
<h3>If you use the Mach64 chipset driver</h3>
<dl>
<dt><code>Chipset Mach64</code></p>
<dd>if you want to use the experimental pre-alpha driver</dl>
<h3>If you use the S3 chipset driver</h3>
<p>I don&#8217;t have much knowledge on the S3, but it seems to me that you need: </p>
<dl>
<dt><code>Clocks</code><i> clock1 clock2 </i><code>&#8230;</code></p>
<dd>to specify the clocks (take them from your Xfree86 configuration).</dl>
<p> or</p>
<dl>
<dt><code>ClockChip icd2061a </code><i>number</i></p>
<dd>if you have an Icd2061a clockchip.</p>
<dt><code>Ramdac </code><i>chipname</i></p>
<dd>if your Ramdac is not detected properly.</p>
<dt><code>Dacspeed </code><i>speed</i></p>
<dd>if the default chosen is not right (probably too restrictive).</dl>
<p> The remaining options are really only to be used in case of problems which you&#8217;ll not generally encounter.</p>
<h3>If you use the VESA chipset driver</h3>
<dl>
<dt><code>VesaText</code></p>
<dd>forces the driver to set 80&#215;25 text mode, before any standard vga mode setting. Fixes text mode restoring with many cards, as well as standard VGA modes.</p>
<dt><code>VesaSave</code></p>
<dd>selects the bitmap to save and restore, using VESA functions. see VESA documentation for bits&#8217; meanings. The default is 1110 (=14) which is good for most cards, but some give better results with other numbers.<br />
&nbsp;<wbr></dl>
<h2>General Options (Handled By The Main Module)</h2>
<h3>Mouse configuration</h3>
<dl>
<dt><code>mouse </code><i>mousetype</i></p>
<dd>where <i>mousetype</i> is one of: <code>Microsoft</code>, <code>MouseSystems</code>, <code>MMSeries</code>, <code>Logitech</code>, <code>Busmouse</code>, <code>PS2</code>, <code>MouseMan</code>, <code>gpm</code>, <code>Spaceball</code>, <code>none</code>, <code>IntelliMouse</code>, or <code>IMPS2</code>. <i>mousetype</i> can also be a number (<code>0</code> &#8211; <code>9</code>) for the keywords <code>Microsoft</code> &#8211; <code>none</code>. </p>
<p> <code>gpm</code> allows for (hopefully) peaceful interaction with gpm, <code>Spaceball</code> enables support for the 6-axes Spacetec Spaceball mouse (well, probably more like a trackball), <code>IntelliMouse</code> and <code>IMPS2</code> refer to the Microsoft IntelliMouse or Logitech MouseMan+, where <code>IntelliMouse</code> is for serial port and <code>IMPS2</code> for such a mouse on the PS/2 port. </p>
<p> Note that it is not possible to specify the Microsoft IntelliMouse or Logitech MouseMan+ by a number. This is due to historical and compatibility reasons. </p>
<dt><code>mouse_override</code></p>
<dd>This command is only available if <code>ALLOW_MOUSE_OVERRIDE</code> was set in <i>Makefile.cfg</i> when svgalib was compiled (which is the default). </p>
<p> If given, svgalib ignores any mouse type the program specifies but uses the type configured with the <code>mouse</code> command. </p>
<p> For example, DOOM does not recognize <code>MouseMan</code> as a valid mouse type and defaults the mouse type to <code>MouseSystems.</code> This command allows to make svgalib ignore whatever DOOM specifies and use <code>MouseMan</code> anyway. </p>
<dt><code>mdev </code><i>mousedevice</i></p>
<dd>Usually <i>/dev/input/mice</i> (the default) will be the mouse device. However, esp. with the Spacetec Spaceball you may want to specify a different device for <code><a href="/docs/linux/man/7-svgalib/">svgalib</a></code>(7) to use: </p>
<p> <code>mdev /dev/ttyS0 </code># mouse is at /dev/ttyS0 </p>
</dl>
<p> Some multiprotocol mice use the state of RTS and DTR to find out which protocol to enable: </p>
<dl>
<dt><code>setRTS</code></p>
<dd>set the RTS wire.</p>
<dt><code>clearRTS</code></p>
<dd>clear the RTS wire.</p>
<dt><code>leaveRTS</code></p>
<dd>leave the RTS wire alone (default) (Wire is usually set)</p>
<dt><code>setDTR</code></p>
<dd>set the DTR wire.</p>
<dt><code>clearDTR</code></p>
<dd>clear the DTR wire.</p>
<dt><code>leaveDTR</code></p>
<dd>leave the DTR wire alone (default) (Wire is usually set) </p>
</dl>
<p> For example my mouse can emulate Microsoft and MouseSystems. It needs a low RTS to go into MouseSystems mode. Thus I use: </p>
<p> <code>mouse MouseSystems clearRTS</code> </p>
<p> Still I could just use <code>mouse Microsoft</code> and use the mouse with that protocol.. But then only 2 buttons instead of 3 are supported (not that I know many svgalib programs that uses more than 2 buttons.) </p>
<p> Other mice might need <code>clearDTR</code> as well or one set and clear. Try yourself. </p>
<p> Note: Having crtscts handshake enabled on the mouse tty may interfere with this option. Do not do that. </p>
<p> Finally, a special goodie for wheel mice: </p>
<dl>
<dt><code>mouse_fake_kbd_event </code><i>upscancode</i><i>downscancode</i></p>
<dd>sends a fake keyboard event to the program when the wheel on a Microsoft IntelliMouse, Logitech MouseMan+, or similar wheel mouse is turned. </p>
<p> The up and down scancodes are the scancodes of the keys to simulate when the wheel is turned up and down, respectively. </p>
<p> The following can be specified for the scancodes: letters (<code>A</code>&#8211;<code>Z</code>), numbers (<code>0</code>&#8211;<code>9</code>), function keys (<code>F1</code>&#8211;<code>F12</code>), or any of the following &#8211; <code>ESCAPE</code>, <code>MINUS</code>, <code>EQUAL</code>, <code>BACKSPACE</code>, <code>TAB</code>, <code>BRACKET_LEFT</code>, <code>BRACKET_RIGHT</code>, <code>ENTER</code>, <code>LEFTCONTROL</code>, <code>SEMICOLON</code>, <code>APOSTROPHE</code>, <code>GRAVE</code>, <code>LEFTSHIFT</code>, <code>BACKSLASH</code>, <code>COMMA</code>, <code>PERIOD</code>, <code>SLASH</code>, <code>RIGHTSHIFT</code>, <code>KEYPADMULTIPLY</code>, <code>LEFTALT</code>, <code>SPACE</code>, <code>CAPSLOCK</code>, <code>NUMLOCK</code>, <code>SCROLLLOCK</code>, <code>KEYPAD7</code>, <code>CURSORUPLEFT</code>, <code>KEYPAD8</code>, <code>CURSORUP</code>, <code>KEYPAD9</code>, <code>CURSORUPRIGHT</code>, <code>KEYPADMINUS</code>, <code>KEYPAD4</code>, <code>CURSORLEFT</code>, <code>KEYPAD5</code>, <code>KEYPAD6</code>, <code>CURSORRIGHT</code>, <code>KEYPADPLUS</code>, <code>KEYPAD1</code>, <code>CURSORDOWNLEFT</code>, <code>KEYPAD2</code>, <code>CURSORDOWN</code>, <code>KEYPAD3</code>, <code>CURSORDOWNRIGHT</code>, <code>KEYPAD0</code>, <code>KEYPADPERIOD</code>, <code>KEYPADCENTER</code>, <code>RIGHTCONTROL</code>, <code>CONTROL</code>, <code>KEYPADDIVIDE</code>, <code>PRINTSCREEN</code>, <code>RIGHTALT</code>, <code>BREAK</code>, <code>BREAK_ALTERNATIVE</code>, <code>HOME</code>, <code>CURSORBLOCKUP</code>, <code>PAGEUP</code>, <code>CURSORBLOCKLEFT</code>, <code>CURSORBLOCKRIGHT</code>, <code>END</code>, <code>CURSORBLOCKDOWN</code>, <code>PAGEDOWN</code>, <code>INSERT</code>. </p>
<p> Note that this option has no effect unless the IntelliMouse or IMPS2 mouse type is used (see above). Also note that the simulated keypresses are instantaneous, so they cannot be used for functions that require a key to be held down for a certain length of time. </p>
<p> This example simulates a press of the left bracket ([) when the wheel is turned up and a press of the right bracket (]) when the wheel is turned down (good for selecting items in Quake II): </p>
<p> <code>mouse_fake_kbd_event BRACKET_LEFT BRACKET_RIGHT</code> </p>
</dl>
<h3>Mouse acceleration</h3>
<p>Svgalib versions 1.3.0 and later use the following commands to control the logarithmic mouse acceleration:</p>
<dl>
<dd>
<dl>
<dt><code>mouse_force</code></p>
<dd>If given, force use of input parameters even if they seem strange.</p>
<dt><code>mouse_maxdelta</code><i> &lt;integer&gt;</i></p>
<dd>Set max delta BEFORE acceleration.</p>
<dt><code>mouse_accel_maxdelta</code><i> &lt;integer&gt;</i></p>
<dd>Set max delta AFTER acceleration.</p>
<dt><code>mouse_accel_thresh</code><i> &lt;integer&gt;</i></p>
<dd>Set acceleration threshold.</p>
<dt><code>mouse_accel_power</code><i> &lt;float&gt;</i></p>
<dd>Set input variable for power mode.</p>
<dt><code>mouse_accel_mult</code><i> &lt;float&gt;</i></p>
<dd>Set acceleration factor.</p>
<dt><code>mouse_accel_type</code> {<code>0</code>|<code>off</code>|<code>normal</code>|<code>power</code>|<code>linear</code>}</p>
<dd>Set the type of acceleration. The following strings are valid values:</p>
<dl>
<dd>
<dl>
<dt><code>0</code> or <code>off</code></p>
<dd>No acceleration.</p>
<dt><code>normal</code></p>
<dd>No acceleration while delta is less than <code>mouse_accel_thresh</code> but multiplied by <code>mouse_accel_mult</code> if more.<br />
 Originally done by Mike Chapman &lt;mike [at] paranoia.com&gt;.</p>
<dt><code>power</code></p>
<dd>The acceleration factor is a power function of delta until it reaches <code>mouse_accel_mult</code> After that it&#8217;s a simple multiplication. Basically it&#8217;s like the normal mode but the acceleration factor grows as you move your mouse faster and faster, not just turns in and out. If the acceleration factor reaches <code>mouse_accel_mult</code> it turns into a plain multiplication. </p>
<p> Threshold has the same meaning as in normal mode. The one I use for *uaking&#8230; :) </p>
<p> It is calculated like this: </p>
<p> if (abs(dx) &gt; 1) /* to prevent losing resolution */ </p>
<p>&nbsp;<wbr>&nbsp;<wbr>dx&nbsp;<wbr>=&nbsp;<wbr>(abs(dx)&nbsp;<wbr>&gt;=<br />
 <code> mouse_accel_thresh</code> ) ? </p>
<p>&nbsp;<wbr>(float)dx&nbsp;<wbr>*<br />
 <code> mouse_accel_mult</code> : </p>
<p>&nbsp;<wbr>(float)dx&nbsp;<wbr>* </p>
<p>&nbsp;<wbr>&nbsp;<wbr>m_accel_powertable[abs(dx)];</p>
<dt><code>linear</code></p>
<dd>The acceleration factor grows linear with the delta until it reaches <code>mouse_accel_thresh</code>. After that it is a simple multiplication. (I know that it can be done with setting <code>mouse_accel_power</code> to 1, but it was one minute to implement&#8230; and uses no memory&#8230; and&#8230;) </p>
<p> It is calculated like this: </p>
<p> if (abs(dx) &gt; 1) </p>
<p>&nbsp;<wbr>&nbsp;<wbr>dx&nbsp;<wbr>=&nbsp;<wbr>(abs(dx)&nbsp;<wbr>&gt;=<br />
 <code> mouse_accel_thresh</code> ) ? </p>
<p>&nbsp;<wbr>(float)dx&nbsp;<wbr>*<br />
 <code> mouse_accel_mult</code> : </p>
<p>&nbsp;<wbr>(float)dx&nbsp;<wbr>*&nbsp;<wbr>abs(dx)&nbsp;<wbr>*<br />
 <code> mouse_accel_mult</code> /<br />
 <code> mouse_accel_thresh</code> ;</dl>
</dl>
<p> The enhanced acceleration was done by 101 (Attila Lendvai) &lt;101 [at] kempelen.inf.bme.hu&gt;</dl>
</dl>
<h3>Joystick configuration</h3>
<p>As of now, svgalib supports up to four joystick devices. You must have joystick support in your kernel to support this. </p>
<dl>
<dt><code>joystick0 </code><i>device</i></p>
<dd>sets the device name to use for joystick 0. The commands <code>joystick1</code>, <code>joystick2</code> and <code>joystick3</code> configure the other joysticks. By default the names <i>/dev/js0</i>, <i>/dev/js1</i>, <i>/dev/js2</i> and <i>/dev/js3</i> are used. </p>
</dl>
<h3>Keyboard configuration</h3>
<dl>
<dt><code>kbd_fake_mouse_event</code><i> scancode </i><code>[</code><i>flag(s)</i><code>] </code><i>command</i><code> [</code><i>argument</i><code>]</code></p>
<dd>, as it says, sends a fake mouse event to the program. <i>Scancode</i> is a raw scancode as you can find them in <i>&lt;keyboard/vgakeyboard.h&gt;</i>. </p>
<dd>Supported <i>flag(s)</i> are:</p>
<dl>
<dd>
<dl>
<dt><code>down</code></p>
<dd>trigger event when the key is pressed (default).</p>
<dt><code>up</code></p>
<dd>the opposite.</p>
<dt><code>both</code></p>
<dd>trigger in both case, if pressed or released.</p>
<dt><code>repeat</code></p>
<dd>repeat events if the key is kept pressed (off by default).</dl>
</dl>
<dd>Supported commands are:</p>
<dl>
<dd>
<dl>
<dt><code>delta</code>[<code>xyz</code>]</p>
<dd>send a fake delta event as if you have moved your mouse. If the <i>parameter</i> is <code>off</code> or <code>on</code> it will turn off/on the respective mouse axis (requires a <i>parameter</i>, of course)</p>
<dt><code>button</code>[<code>123</code>]</p>
<dd>send a fake event that the mouse button is pressed or released as given by the <i>parameter</i> (<code>pressed</code> or <code>released</code>)</dl>
</dl>
<dd>Here are some examples: </p>
<p> This is one I use in *uake: it turns around, looks down a bit and when the key is released it does the opposite, so it gets back to the starting state. With this one and the help of a rocket you can fly though the whole map :) (Scancode 28 is <code>&lt;Enter&gt;</code>): </p>
<p> <code> kbd_fake_mouse_event 28 both deltax 8182</code><br />
 <code> down deltay -1500</code><br />
 <code> up deltay 1500</code> </p>
<p> This one will switch off the y axis of the mouse while the key <code>&lt;Right Ctrl&gt;</code> is kept pressed. </p>
<p> <code> kbd_fake_mouse_event 97 down deltay off</code><br />
 <code> up deltay on</code> </p>
<p> This one is the same as if you were pressing the left mouse button. (But if you move your mouse then the button state will reset even if you keep <code>&lt;Right Ctrl&gt;</code> down&#8230;) </p>
<p> <code> kbd_fake_mouse_event 97 down button1 pressed</code><br />
 <code> up button1 released</code> </p>
<p> <code>NOTE:</code> This does only work when the keyboard is in raw keyboard mode! </p>
<p> Yet another feature brought to you by 101 (Attila Lendvai) &lt;101 [at] kempelen.inf.bme.hu&gt; </p>
<dt><code>nosigint</code></p>
<dd>This command disables generation of a <code>SIGINT</code> signal when <code>&lt;Ctrl-C&gt;</code> is pressed. </p>
<p> This works regardless of ordinary or raw keyboard mode (albeit the hot key might be different from <code>&lt;Ctrl-C&gt;</code> in the first case). </p>
<p> <code>Note</code> that this is a very dangerous option. Disabling <code>SIGINT</code> will lock you in programs which can only by quit by <code>&lt;Ctrl-C&gt;</code>! However, there were request for it for Quake playing.</p>
<dt><code>sigint</code> (default)</p>
<dd>Enables generation of <code>SIGINT</code>. </p>
</dl>
<h3>Monitor configuration</h3>
<dl>
<dt><code>HorizSync </code><i>min_kHz max_kHz</i></p>
<dd>
<dt><code>VertRefresh </code><i>min_Hz max_Hz</i></p>
<dd>specifies the range of frequencies acceptable to your monitor. They obsolete the <code>monitor</code> settings below, and this shouldn&#8217;t be used if <code>HorizSync</code> and <code>VertRefresh</code> are defined. Examples: </p>
<p> <code>HorizSync 31.5 35.5</code><br />
 <code>VertRefresh 50 70</code> </p>
<dt><code>monitor</code><i> monitor_class</i></p>
<dd>where <i>monitor_class</i> is a digit <code>0</code> &#8211; <code>6</code> or the maximal horizontal frequency in kHz. Examples: </p>
<p> <code>monitor 0</code> # Max horizontal sync is 31.5 kHz<br />
 <code>monitor 1</code> # Max horizontal sync is 35.1 kHz<br />
 <code>monitor 2</code> # Max horizontal sync is 35.5 kHz<br />
 <code>monitor 3</code> # Max horizontal sync is 37.9 kHz<br />
 <code>monitor 4</code> # Max horizontal sync is 48.3 kHz<br />
 <code>monitor 5</code> # Max horizontal sync is 56.0 kHz<br />
 <code>monitor 6</code> # No restrictions. </p>
<p> For your convenience you may specify the max horizontal sync explicitly. The correct class will the be chosen. You may use floats consisting of digits and a decimal point for this too: </p>
<p> <code>monitor 40.0</code> # equivalent to monitor 3 </p>
<p> This command is <code>privileged</code>. </p>
</dl>
<h3>Mode timings</h3>
<p>It is now possible to define modetimings for some cards (see the info on your card in <code><a href="/docs/linux/man/7-svgalib/">svgalib</a></code>(7)). The syntax is: </p>
<dl>
<dt><code>modeline </code><i>label pxcl HDsp HSS HSE HTot VDsp VSS VSE VTot flags</i></p>
<dd>
<dl>
<dd>
<dl>
<dt><i>label </i>string</p>
<dd>(ignored by svgalib) mainly there to be compatible with XF86Config. I use the format &quot;Width x Height @ Vert.Refresh&quot;, but that&#8217;s just personal taste&#8230;</p>
<dt><i>pxcl </i>float</p>
<dd>the pixel clock in MHz </p>
<dt><i>HDsp</i></p>
<dd>
<dt><i>VDsp </i>integer</p>
<dd>size of the visible area (horizontal/vertical) </p>
<dt><i>HSS</i></p>
<dd>
<dt><i>VSS </i>integer</p>
<dd>Sync start (horizontal/vertical) </p>
<dt><i>HSE</i></p>
<dd>
<dt><i>VSE </i>integer</p>
<dd>Sync end (horizontal/vertical) </p>
<dt><i>HTot</i></p>
<dd>
<dt><i>VTot </i>integer</p>
<dd>Total width/height (end of back porch) </p>
<dt><i>flags </i><code>+hsync -hsync +vsync -vsync interlace interlaced</code></p>
<dd><code>doublescan</code> Sync polarity, interlace mode</dl>
</dl>
<p> Everything should be on one line. The values for the horizontal timings must be multiples of eight. </p>
<p> These are preferred over the default timings (if monitor and chipset can handle them). The format is identical to the one used by XFree86, but the label following the modeline keyword is ignored by vgalib. </p>
<p> Here some examples: </p>
<p> <code>modeline 640&#215;480@100 43 640 664 824 848 480 483 490 504</code><br />
 <code>modeline 800&#215;600@73 50 800 856 976 1024 600 637 643 666</code><br />
 <code>modeline 1024&#215;768@75 85 1024 1048 1376 1400 768 771 780 806</code> </p>
<p> <code>IMPORTANT!</code> Not all drivers, that is SVGA cards, use the values. Only drivers using timing.c. As of this writing, drivers using this feature are: Ark, Cirrus, Chips &amp; Technologies, Et6000, S3. </p>
<p> The Mach32 driver provides a similar feature separately, you have to use the <code>define</code> command described below. </p>
<p> ET4000 (and to some extent EGA) allow one to use a binary file created by some utility. All other chipset driver use predefined timings that are hardcoded in register dumps within the drivers. See <code><a href="/docs/linux/man/7-svgalib-et4000/">svgalib.et4000</a></code>(7) for more information. </p>
</dl>
<h3>Chipset detection</h3>
<p>Usually svgalib does a good job autodetecting your hardware. However, if auto detection fails (or you want to fall back to a simpler driver, say VGA, as a bug work around), you may force detection of your chipset with </p>
<dl>
<dt><code>chipset </code><i>type</i></p>
<dd>where <i>type</i> is (currently) one of: <code>VGA</code>, <code>ET4000</code>, <code>Cirrus</code>, <code>TVGA</code>, <code>Oak</code>, <code>EGA</code>, <code>S3</code>, <code>ET3000</code>, <code>Mach32</code>, <code>GVGA6400</code>, <code>ARK</code>, <code>ATI</code>, <code>ALI</code>, <code>Mach64</code>, <code>C&amp;T</code>, <code>APM</code>, <code>NV3</code>, <code>ET6000</code>, <code>VESA</code>, <code>MX</code>, <code>PARADISE</code>, and <code>RAGE</code>. </p>
<p> You can also specify a number in range <code>1 &#8211; 22</code> to specify the <i>type</i><code>-th</code> chipset type or <code>0</code> to enforce autodetection. </p>
<p> Warning, incorrect settings may damage your hardware. This command is <code>privileged</code>. </p>
<dt><code>chipset </code><i>type param1 param2</i></p>
<dd>use this form if the size of memory or an additional configuration option is misdetected. For example: </p>
<p> <code>chipset Mach32 0 2048</code> </p>
<p> Note that always two integers have to be specified. Usually (Mach32) the second parameter is the memory amount. Look at the *_init function of the specific device driver sources or information on that type of cards in <code><a href="/docs/linux/man/7-svgalib/">svgalib</a></code>(7). </p>
<p> Note that there is a more convenient command <code>setuplinear</code> for enforcing specific memory-aperture configurations for Mach32 </p>
<p> This command is <code>privileged</code>. </p>
</dl>
<h3>Specific options required for the EGA-driver.</h3>
<dl>
<dt><code>monotext</code></p>
<dd>Card is in monochrome emulation mode</p>
<dt><code>colortext</code></p>
<dd>Card is in color emulation mode </p>
<p> This command is <code>privileged</code>. </p>
</dl>
<h3>RAMDAC configuration</h3>
<p>Some chipsets (e.g. S3 and ARK) allow specifying a RAMDAC type. If your RAMDAC is not autodetected, you can try specifying it: </p>
<dl>
<dt><code>Ramdac Sierra32K</code></p>
<dd>
<dt><code>Ramdac SC15025</code></p>
<dd>
<dt><code>Ramdac SDAC</code></p>
<dd>S3 SDAC</p>
<dt><code>Ramdac GenDAC</code></p>
<dd>S3 GenDAC</p>
<dt><code>Ramdac ATT20C490</code></p>
<dd>AT&amp;T 20C490, 491, 492 (and compatibles)</p>
<dt><code>Ramdac ATT20C498</code></p>
<dd>AT&amp;T 20C498</p>
<dt><code>Ramdac IBMRGB52x</code></p>
<dd>IBM RGB524, 526, 528 (and compatibles)</dl>
<p> <code>BEWARE!</code> The Mach32 driver features an own <code>ramdac</code> command (which is usually not required). If you have a Mach32, see <code><a href="/docs/linux/man/7-svgalib-mach32/">svgalib.mach32</a></code>(7). </p>
<dl>
<dt><code>Dacspeed </code><i>speed</i></p>
<dd><i>speed</i> is a floating point number in MHz (like in <code>Dacspeed</code>40.0 ) specifying the maximal allowable pixel clock of the Ramdac in use. Currently this option is only supported by the S3 driver. The Mach32 driver supports <code>maxclock8</code>, <code>maxclock16</code>, <code>maxclock24</code>, and <code>maxclock32</code> commands which have a similar effect. Nevertheless, the Mach32 has a very good idea on the capabilities of the Ramdac in use. The settings are more intended to specify the VGA memory bandwidth. </p>
</dl>
<h3>Pixel clocks</h3>
<dl>
<dt><code>Clocks </code><i>list of clock values as floats or ints</i></p>
<dd>Some chipsets need a list of dot clocks for optimum operation. Some includes or supports a programmable clock chip. You&#8217;ll need to specify them here. </p>
<p> Fixed clocks example: (The following is just an example, get the values for your card from you X setup) </p>
<p> <code>Clocks 25.175 28.3 40 70 50 75 36 44.9 0 118 77 31.5 110 65 72 93.5</code> </p>
<p> <code>BEWARE!</code> The <code>Clocks</code> command for the Mach32 features only integer clocks. Please round your clocks to the next integer data. The Mach32 only uses these values to check monitor requirements and to compare the quality of modes. The rounding errors are of no importance there as the difference in the resulting monitor timings is barely measurable. See the Mach32 section below.</p>
<dt><code>Clockchip ICD2061A</code></p>
<dd>Configure for a programmable clockchip. <code>ICD2061A</code> is the only one supported right now. </p>
</dl>
<h3>Miscellaneous options</h3>
<dl>
<dt><code>security revoke-all-privs</code></p>
<dd>Make sure it is impossible to regain root access after <code><a href="/docs/linux/man/3-vga_init/">vga_init</a></code>(3) was called. (default)</p>
<dt><code>security compat</code></p>
<dd>For compatibility to pre 1.2.11, do not close a security hole using saved uids.</p>
<dt><code>verbose</code></p>
<dd>Mach32: show messages while processing all info to build up a mode table.</p>
<dt><code>quiet</code></p>
<dd>Turn verbose messages off (default).</p>
<dt><code>nolinear</code></p>
<dd>Inhibit use of a linear mmaped frame buffer.</p>
<dt><code>linear</code></p>
<dd>Allow (not enforce!) use of a linear mmaped frame buffer.</p>
<dt><code>overrideenable</code></p>
<dd>Allow <code>privileged</code> commands outside the main configuration file. </p>
</dl>
<h3>Common options currently used by Mach32 only</h3>
<p>Options that may be useful for all drivers, but currently are only supported by Mach32 (Please read <code><a href="/docs/linux/man/7-svgalib-mach32/">svgalib.mach32</a></code>(7) if you use one): </p>
<dl>
<dt><code>maxclock16 </code><i>maxclk</i></p>
<dd>The maximum pixel clock to use for 16bpp modes. This is used by Mach32 to find out which settings may be used for 16bpp modes. the Mach32 default for this is 2000, thus it is effectively switched off. <i>maxclk</i> must be an integer. </p>
<dt><code>maxclock24 </code><i>maxclk</i></p>
<dd>The maximum clock to use for 24bpp modes. (see above) Experience showed that the Mach32 default 49 is good for my 2MB VRAM card. </p>
<dt><code>maxclock32 </code><i>maxclk</i></p>
<dd>The same for 32bpp modes (24bpp with one fill byte for faster memory access (not fully implemented (esp. for Mach32) yet). Mach32 default (good for my VRAM card) is 39. </p>
<dt><code>maxclock8 </code><i>maxclk</i></p>
<dd>Just for completeness the same for 8bpp modes (I doubt anyone needs it), default is 2000 to disable this feature. </p>
</dl>
<p> The <code>maxclock</code> commands are <code>privileged</code>. </p>
<dl>
<dt><code>clocks </code><i>list of clocks</i></p>
<dd>Sets the frequencies of the clocks the chips can generate. Exactly 16 values have to be specified for mach32. Use 0 to disable a specific clock. </p>
<p> Note that the mach32 can divide clocks by 2. Thus there are actually 32 clocks And you can also use the divided clocks in a define command. On contrary to Xfree96 or the <code>clocks</code> command above only integers are allowed for Mach32. Simply round them to the nearest integer. </p>
<p> This line is mandatory for Mach32. If it is not there it will be auto detected and added at the beginning of the config file. The program will then exit and when you start it next, everything should be ok. </p>
<p> Common clock values for Mach32:</p>
<dl>
<dd>
<dl>
<dt>Clock chip 18811-0:</p>
<dd><code>clocks 43 49 92 36 50 56 0 45</code><br />
 <code> 30 32 110 80 40 45 75 65</code> </p>
<dt>Clock chip 18811-1:</p>
<dd>due to Xfree86 info valid for: Ultra pro ISA, Ultra pro EISA, Ultra pro VLB(68800-3) </p>
<p> <code>clocks 100 126 92 36 50 56 0 45</code><br />
 <code> 135 32 110 80 40 45 75 65</code> </p>
<dt>Clock chip 1881 (ICS2494):</p>
<dd>due to Xfree86 info valid for: Ultra pro VLB (6880006) </p>
<p> <code>clocks 18 22 25 28 36 44 50 56</code><br />
 <code> 30 32 37 39 40 0 75 65</code></dl>
</dl>
<dd>In my own correspondence with ATI they say every Mach32 would have a 18811-1, so it should be possible just to take the 18811-1 line. However I have now reports of third party cards and motherboards with on board Mach32 chips, so be careful. </p>
<p> Please read <code><a href="/docs/linux/man/7-svgalib-mach32/">svgalib.mach32</a></code>(7) for additional info on clocks. </p>
<p> The <code>clocks</code> command is <code>privileged</code>. </p>
<dt><code>variablelinelength</code></p>
<dd>Sometimes a mode cannot be realized with the logical linelength = pixels in a row * bytes per pixel. (definitely true for Mach32 800&#215;600). The default behavior of Mach32 is to adjust <i>xbytes</i> (see <code><a href="/docs/linux/man/3-vga_getmodeinfo/">vga_getmodeinfo</a></code>(3)) in the info table appropriately. </p>
<p> This command enforces this default operation and adjusts <i>xbytes</i> appropriately, thus overriding the standard svgalib mode. This may yield to problems with ..umm.. not well designed applications. </p>
<dt><code>duplicatelinelength</code></p>
<dd>Don&#8217;t touch the standard mode but create an exact copy, a dynamic mode, with the adjusted <i>xbytes</i> value. Expect noise at some pixels in 800&#215;600 for more than 256 colors on Mach32 when not using the dynamic mode. </p>
<dt><code>strictlinelength</code></p>
<dd>Same as above but delete the standard mode thus creating the non conforming <i>xbytes</i> modes only as dynamic modes. </p>
</dl>
<p> To enforce the standard linelength for non-conforming modes use <code>setlinelength</code> below. </p>
<p> The linelength commands are <code>not privileged</code>. </p>
<p> In the following commands a mode is specified with <i>horz</i>X<i>vert</i>X<i>colors</i>. Valid settings for colors in the mach32 driver are: 256, 32K, 64K, 16M, 16M4. 16M4 is for the 16M colors with 32bpp modes. These are expected to support slightly faster drawing. </p>
<p> Examples: <code>640x480x256</code>, <code>1024x768x64K</code>, etc&#8230; </p>
<dl>
<dt><code>inhibit </code><i>mode1</i><code> [</code><i>mode2</i><i>mode3</i><code>&#8230;]</code></p>
<dd>Switch the specified SVGA-Modes off. For example: </p>
<p> <code>inhibit 800x600x32K 800x600x64K 800x600x16M</code> </p>
<p> disallows the maybe toasted mach32 800&#215;600 modes. </p>
<p> The <code>inhibit</code> command is <code>not privileged</code>. </p>
<dt><code>setlinelength </code><i>length</i><i>mode1</i><code> [</code><i>mode2</i><i>mode3</i><code>&#8230;]</code></p>
<dd>Force the logical line length (<i>xbytes</i>) in the given modes to length pixels (not bytes!). See also <code>variablelinelength</code>, <code>strictlinelength</code>, and <code>duplicatelinelength</code> above. For example: </p>
<p> <code>setlinelength 800 800x600x32K 800x600x64K 800x600x16M</code> </p>
<p> sets the linelength, and thus <i>xbytes</i>, for the <code>800&#215;600</code> modes to the equivalent of 800 pixels. For Mach32 this will give badly designed applications an 800&#215;600 with which they can cope. However, the Mach32 will generate a noisy video signal in some configurations. </p>
<p> The <code>setlinelength</code> command is <code>not privileged</code>. </p>
<dt><code>define </code><i>mode1</i><code> [</code><i>mode2</i><i>mode3</i><code>&#8230;] </code><i>clock horz_timing vert_timing flags</i></p>
<dd>where <i>clock</i> is a clock in MHz (as an integer! Has to be known by the driver. (one of the set clocks, or the exact half of one)). Only clocks in a <code>clocks</code> command issued before the <code>define</code> can be used. </p>
<p> You may use <code>:</code><i>n</i> to specify the <i>n</i>-th<i>clock</i> (<i>n</i> = 0 .. 31 for mach32). </p>
<p> <i>horz_timing</i> is four integers: <i>hdisp h_sync_strt h_sync_wid h_total</i>. </p>
<p> <i>vert_timing</i> has the same format but for vertical. </p>
<p> You may specify one or more <i>flags</i> out of: <code>Interlace</code>, <code>+vsync</code>, <code>-vsync</code>, <code>+hsync</code>, or <code>-hsync</code> to select interlace mode and polarity of sync signals. This format is almost the same Xfree uses, s.t. you may use their mode table and the modegen spreadsheet package for mode creation. You simple need to round the clock to the next integer, add the resolution instead of the timing name for Xfree and replace the <code>modeline</code> keyword with <code>define</code>. Here is a 1024x768x256 mode as example: </p>
<p> <code>define 1024x768x256 80 1024 1024 1184 1312</code><br />
 <code> 768 768 772 791 +vsync -hsync</code> </p>
<p> or </p>
<p> <code>define 1024x768x256 1024x768x32K 1024x768x64K</code><br />
 <code> :11 1024 1024 1184 1312 768 768 772 791</code> </p>
<p> (yes any whitespace in a command is allowed, even a newline !) </p>
<p> Both commands define the same timings (if the 11-th clock is 80) but the first explicitly specifies the polarity of sync signals whereas the second declares that these timings are also to be used for a 32K and 64K mode. </p>
<p> The <code>define</code> command is <code>privileged</code>. </p>
</dl>
<p> There is one really dangerous option (except faking clocks). Please use it only if you are sure what you are doing. Wrong setup will lead to multiple components accessing your bus at once and thus to probable hardware damage: </p>
<dl>
<dt><code>setuplinear</code><i> address size</i></p>
<dd>Sets up a linear frame buffer at <i>address</i> of size <i>size</i> (both are given in MB). If the values make sense (for example address &lt;16MB for ISA cards) the linear aperture is setup. Since the Mach32-driver auto detects configured address itself, I strongly discourage use of this command. However I was asked for it as some PCI mach32-cards didn&#8217;t setup the linear aperture correctly. </p>
<p> Please ensure that the address range from <i>address</i> to <i>address</i> + <i>size</i> (exclusively) is not used in your system. Obey that due to memory remapping for example 16MB Ram may exceed the 16MB address limit. </p>
<p> Valid Mach32 values for size are 1 and 4 (only 4 in PCI configurations), <i>address</i> + <i>size</i> have to be below 16MB for ISA, 4GB for multiplexed PCI, and 128MB else. Example: (my setup) </p>
<p> <code>setuplinear 64 4</code> </p>
<p> for a 4MB linear frame buffer at address 0x4000000. </p>
<p> It is also valid to specify <code>setuplinear 0 0</code>. This will actually disable/de-configure any linear frame buffer. Useful to disable mach32 aperture even if it is enabled in the EEPROM. </p>
<p> The <code>setuplinear</code> command is <code>privileged</code>. </p>
<dt><code>blit </code><i>subcommand1 subcommand2</i><code> &#8230;</code></p>
<dd>This is a command to control the Mach32 support for oldstyle accelerator functions. </p>
<p> Valid <i>subcommand</i>s are <code>bit</code>, <code>fill</code>, <code>image</code>, and <code>hlinelist</code>. They enable support for the corresponding blit functions. Precede them with <code>no</code> to turn them off (no space after <code>no</code> allowed). Use <code>memimage</code> to emulate the <code>image</code> blit using a linearframebuffer, which is usually much faster for Mach32. Use <code>nomemimage</code> to never use this emulation. On the Mach32 this emulation can be used in more resolutions than the actual imageblit accelerator function. Again order is vital! (esp. for the <code>*image</code> commands). </p>
<p> As the Mach32 now has also new style <code><a href="/docs/linux/man/3-vga_accel/">vga_accel</a></code>(3) support there are now also the <i>subcommand</i>s: <code>settrans</code>, <code>setrop</code>, <code>fillbox</code>, <code>screencopy</code>, <code>drawline</code>, <code>putimage</code>, <code>drawhlinelist</code>, <code>putbitmap</code>, <code>screencopymono</code>, <code>setmode</code>, <code>polyline</code>, <code>polyhline</code>, and <code>polyfillmode</code>. Which are also supported with a leading <code>no</code>. They allow to control support for the subfunctions of <code><a href="/docs/linux/man/3-vga_accel/">vga_accel</a></code>(3). In addition, <code>memimage</code> emulation applies to <code>putimage</code> as well. </p>
<p> Some examples: </p>
<dl>
<dd>
<dl>
<dt><code>blit image nomemimage</code></p>
<dd>Use IO-style imageblt where possible. Don&#8217;t emulate it in any resolution.</p>
<dt><code>blit image memimage</code></p>
<dd>Use emulated imageblt where possible.</p>
<dt><code>blit memimage image</code></p>
<dd>Use IO-style imageblt where possible, and the emulation where possible in the remaining modes.</p>
<dt><code>blit noimage</code></p>
<dd>Disable support for imageblt.</dl>
</dl>
<dd>Mach32 default is: </p>
<p> <code>blit bit fill image hlinelist settrans setrop</code><br />
 <code> fillbox screencopy drawline putimage</code><br />
 <code> drawhlinelist putbitmap screencopymono</code><br />
 <code> setmode polyline polyhline polyfillmode</code><br />
 <code> memimage</code> </p>
<p> The <code>blit</code> command is <code>not privileged</code>. </p>
</dl>
<p> The Mach32 has also a few intermediate debug options for low level timing adjust. They are: </p>
<p> <code>vfifo8</code><i> number</i><br />
 <code>vfifo16</code><i> number</i><br />
 <code>vfifo24</code><i> number</i><br />
 <code>vfifo32</code><i> number</i><br />
 <code>blank</code><i> number</i><br />
 <code>latch</code><i> number</i> </p>
<p> There also options which are useful to support broken Mach32 cards or third party hardware based on Mach32 which does not follow the ATI specifications completely. For example: </p>
<p> <code>vendor ati</code><br />
 <code>misc_ctl keep-off</code><br />
 <code>svgaclocks 9</code><br />
 <code>ramdac auto</code> </p>
<p> For details about these options see <code><a href="/docs/linux/man/7-svgalib-mach32/">svgalib.mach32</a></code>(7). All of them are <code>privileged</code>.</p>
<h2>Obsolete Commands</h2>
<p>Very old svgalib versions used a different style configuration file. For compatibility, svgalib can still parse these old options. Generally the options consist of one character (case sensitive) followed by a number. Whitespace characters (space, tab, newline) can be used after the characters <code>m</code> and <code>M</code> and the number. </p>
<p> The old svgalib versions actually allowed a new option character to follow a number immediately. The current parser requires white space after the numbers. </p>
<p> Of course, you should not use these cryptic forms anymore. The obsolete commands are: </p>
<dl>
<dt><code>m</code><i>number</i></p>
<dd>Specify the mouse type like <code>mouse</code><i> number</i> does.</p>
<dt><code>M</code><i>class</i></p>
<dd>Specify the monitor class like <code>monitor</code><i> class</i> does.</p>
<dt><code>C</code><i>number</i></p>
<dd>Force usage of the <i>number</i>-th chipset driver from the list of supported drivers <code><a href="/docs/linux/man/1-vga/">VGA</a></code>(1), <code><a href="/docs/linux/man/2-et4000/">ET4000</a></code>(2), <code><a href="/docs/linux/man/3-cirrus/">Cirrus</a></code>(3), <code><a href="/docs/linux/man/4-tvga/">TVGA</a></code>(4), <code><a href="/docs/linux/man/5-oak/">Oak</a></code>(5), <code><a href="/docs/linux/man/6-ega/">EGA</a></code>(6), <code><a href="/docs/linux/man/7-s3/">S3</a></code>(7), <code><a href="/docs/linux/man/8-et3000/">ET3000</a></code>(8), <code><a href="/docs/linux/man/9-mach32/">Mach32</a></code>(9), <code>GVGA6400</code>(10), <code>ARK</code>(11), <code>ATI</code>(12), <code>ALI</code>(13), <code>Mach64</code>(14), <code>C&amp;T</code>(15), <code>APM</code>(16), <code>NV3</code>(17), <code>ET6000</code>(18), <code>VESA</code>(19), <code>MX</code>(20), <code>PARADISE</code>(21), and <code>RAGE</code>(22). </p>
<p> <code>C0</code> reenables auto detection of the chipset (default). </p>
<dt><code>c</code><i>flag</i></p>
<dd>When using the EGA chipset driver, the card is in monochrome emulation mode for <i>flag</i> = 0 and in color emulation mode for <i>flag</i> = 1.</dl>
<h2>Files</h2>
<p><i>/etc/vga/libvga.config</i><br />
 <i>/etc/vga/libvga.et4000</i></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-svgalib/">svgalib</a></code>(7), <code><a href="/docs/linux/man/7-svgalib-et4000/">svgalib.et4000</a></code>(7), <code><a href="/docs/linux/man/7-svgalib-chips/">svgalib.chips</a></code>(7), <code><a href="/docs/linux/man/7-svgalib-mach32/">svgalib.mach32</a></code>(7), </p>
<h2>Author</h2>
<p>The newstyle configuration file was first implemented and documented by Michael Weller &lt;eowmob [at] exp-math.uni-essen.de&gt;. However, other people added new features. </p>
<p> Finally this page was edited by Michael Weller &lt;eowmob [at] exp-math.uni-essen.de&gt;.</p>
