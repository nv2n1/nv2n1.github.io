---
title: "fuse(1)"
name: "fuse"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fuse/"
description: "fuse – Sinclair ZX Spectrum emulator"
---

<h2 class="name">NAME</h2>
<p> fuse &#8211; Sinclair ZX Spectrum emulator </p>
<h2>SYNOPSIS</h2>
<p> <code>fuse</code> [<i>options</i>]</p>
<h2>DESCRIPTION</h2>
<p> Fuse is a Sinclair ZX Spectrum emulator. It supports several models (including the 128), with quite faithful emulation of the display and sound. </p>
<p> The emulator can load any of the formats supported by <i><a href="/docs/linux/man/3-libspectrum/">libspectrum</a></i>(3) &#8211; this includes Z80, SNA and SZX snapshots, and TAP and TZX virtual-tape files. Saving to SZX, Z80 and SNA snapshots and TZX and TAP tape files is supported. The SLT extension to the Z80 format is partly supported (enough for multi-load games); however, loading of the old DAT-file variant is not. DSK disk images are supported when emulating a +3, TRD and SCL disk images are supported when emulating a Pentagon or Scorpion and DCK cartridge images are supported when emulating a Timex 2068 variant. Interface II ROM cartridges are also supported. </p>
<p> Finally, there is also support for reading and writing the RZX input recording format. </p>
<p> See the <code>COMPRESSED FILES</code> section for details on reading files compressed with <i><a href="/docs/linux/man/3-bzip2/">bzip2</a></i>(3) or <i><a href="/docs/linux/man/3-gzip/">gzip</a></i>(3).</p>
<h2>OPTIONS</h2>
<p> <i>&#8211;accelerate-loader</i></p>
<dl>
<dt>
<dd> Specify whether Fuse should attempt to accelerate tape loaders by &quot;short circuiting&quot; the loading loop. This will in general speed up loading, but may cause some loaders to fail. (Enabled by default, but you can use `<i>&#8211;no-accelerate-loader</i>&#8216; to disable). The same as the General Options dialog&#8217;s <i>Accelerate loaders</i> option.</dl>
<p> <i>&#8211;aspect-hint</i></p>
<dl>
<dt>
<dd> Specify whether the GTK+ and Xlib user interfaces should `hint&#8217; to the window manager about the preferred aspect ratio for the graphics window, thus preventing resizing to non-square sizes which lead to Fuse not displaying correctly. This option has been observed to cause problems with some window managers when using the GTK+ UI which can prevent the window from being resized or moved at all. (Enabled by default, but you can use `<i>&#8211;no-aspect-hint</i>&#8216; to disable). See also the `<i>&#8211;strict-aspect-hint</i>&#8216; option.</dl>
<p> <i>&#8211;autosave-settings</i></p>
<dl>
<dt>
<dd> Specify whether Fuse&#8217;s current settings should be automatically saved on exit. The same as the General Options dialog&#8217;s <i>Auto-save settings</i> option.</dl>
<p> <i>&#8211;auto-load</i></p>
<dl>
<dt>
<dd> Specify whether tape and disk files should be automatically loaded when they are opened using the <i>File, Open&#8230;</i> menu option. (Enabled by default, but you can use `<i>&#8211;no-auto-load</i>&#8216; to disable). Same as the General Options dialog&#8217;s <i>Auto-load media</i> option.</dl>
<p> <i>&#8211;beeper-stereo</i></p>
<dl>
<dt>
<dd> Specify whether fake stereo should be added to the emulation of the Spectrum beeper. Same as the Sound Options dialog&#8217;s <i>Beeper pseudo-stereo</i> option.</dl>
<p> <i>&#8211;beta128</i></p>
<dl>
<dt>
<dd> Emulate a Beta 128 interface. Same as the Peripherals Options dialog&#8217;s <i>Beta 128 interface</i> option.</dl>
<dl>
<dt>
<dd> <i>&#8211;betadisk</i> Specify a Betadisk image to load.</dl>
<p> <i>&#8211;bw-tv</i></p>
<dl>
<dt>
<dd> Specify whether the display should simulate a colour or black and white television. This option is effective under the GTK+, Xlib and SDL user interfaces: the others will always simulate a colour TV. The same as the General Options dialog&#8217;s <i>Black and white TV</i> option.</dl>
<p> <i>&#8211;competition-code code</i></p>
<dl>
<dt>
<dd> Specify the code to be written to competition mode RZX files. The same as the RZX Options dialog&#8217;s <i>Competition code</i> option.</dl>
<p> <i>&#8211;competition-mode</i></p>
<dl>
<dt>
<dd> Specify whether input recordings should be made in `competition mode&#8217;. The same as the RZX Options dialog&#8217;s <i>Competition mode</i> option.</dl>
<p> <i>&#8211;compress-rzx</i></p>
<dl>
<dt>
<dd> Specify whether RZX files should be written out compressed. (Enabled by default, but you can use `<i>&#8211;no-compress-rzx</i>&#8216; to disable). Same as the RZX Options dialog&#8217;s <i>Compress RZX data</i> option.</dl>
<p> <i>&#8211;confirm-actions</i></p>
<dl>
<dt>
<dd> Specify whether `dangerous&#8217; actions (those which could cause data loss, for example resetting the Spectrum) require confirmation before occurring. (Enabled by default, but you can use `<i>&#8211;no-confirm-actions</i>&#8216; to disable). This option is effective under the GTK+ UI, and is the same as the General Options dialog&#8217;s <i>Confirm actions</i> option.</dl>
<p> <i>&#8211;debugger-command string</i></p>
<dl>
<dt>
<dd> Specify a debugger command to be run before emulator startup. This can be used to set breakpoints or the like. Currently, this is the only method to input multi-line debugger commands. (See the <code>MONITOR/DEBUGGER</code> section for more information).</dl>
<p> <i>&#8211;detect-loader</i></p>
<dl>
<dt>
<dd> Specify whether Fuse should attempt to detect when the tape is being accessed and start and stop the virtual tape playing automatically. (Enabled by default, but you can use `<i>&#8211;no-detect-loader</i>&#8216; to disable). Same as the General Options dialog&#8217;s <i>Detect loaders</i> option.</dl>
<p> <i>&#8211;divide</i></p>
<dl>
<dt>
<dd> Emulate the DivIDE interface. The same as the Peripherals Options dialog&#8217;s <i>DivIDE interface</i> option.</dl>
<p> <i>&#8211;divide-masterfile file</i><br />
 <i>&#8211;divide-slavefile file</i></p>
<dl>
<dt>
<dd> Specify an IDE image to be loaded into the DivIDE&#8217;s emulated master and slave drives respectively.</dl>
<p> <i>&#8211;divide-write-protect</i></p>
<dl>
<dt>
<dd> Specify that the emulated DivIDE&#8217;s write protect jumper should be considered set. The same as the Peripherals Options dialog&#8217;s <i>DivIDE write protect</i> option.</dl>
<p> <i>&#8211;dock file</i></p>
<dl>
<dt>
<dd> Insert the specified file into the emulated Timex 2068 variant dock; also select the TC2068 on startup if available.</dl>
<p> <i>&#8211;doublescan-mode</i></p>
<dl>
<dt>
<dd> Specify the the framebuffer UI should attempt to use a double scan mode (where each line is displayed twice).</dl>
<p> <i>&#8211;embed-snapshot</i></p>
<dl>
<dt>
<dd> Specify whether a snapshot should be embedded in an RZX file when recording is started from an existing snapshot. (Enabled by default, but you can use `<i>&#8211;no-embed-snapshot</i>&#8216; to disable). Same as the RZX Options dialog&#8217;s <i>Always embed snapshot</i> option.</dl>
<p> <i>&#8211;fastload</i></p>
<dl>
<dt>
<dd> Specify whether Fuse should run at the fastest possible speed when the virtual tape is playing. (Enabled by default, but you can use `<i>&#8211;no-fastload</i>&#8216; to disable). The same as the General Options dialog&#8217;s <i>Fastloading</i> option.</dl>
<p> <i>-f frequency</i><br />
 <i>&#8211;sound-freq frequency</i></p>
<dl>
<dt>
<dd> Specify what frequency Fuse should use for the sound device, the default is 32 kHz, but some devices only support a single frequency or a limited range (e.g. 48 kHz or up to 22 kHz).</dl>
<p> <i>&#8211;full-screen</i></p>
<dl>
<dt>
<dd> Specify whether Fuse should run in full screen mode. This option is effective only under the SDL UI.</dl>
<p> <i>-g filter</i><br />
 <i>&#8211;graphics-filter mode</i></p>
<dl>
<dt>
<dd> Specify which graphics filter to use if available. The default is <i>normal</i>, which uses no filtering. The available options are <i>2x</i>, <i>2xsai</i>, <i>3x</i>, <i>advmame2x</i>, <i>advmame3x</i>, <i>dotmatrix</i>, <i>half</i>, <i>halfskip</i>, <i>normal</i>, <i>super2xsai</i>, <i>supereagle</i>, <i>timex15x</i>, <i>timextv</i>, <i>tv2x</i>, <i>paltv</i>, <i>paltv2x</i>, and <i>paltv3x</i>. See the <code>GRAPHICS FILTERS</code> section for more details.</dl>
<p> <i>&#8211;graphicsfile file</i></p>
<dl>
<dt>
<dd> Set the filename used for graphical output from the emulated ZX printer. See the <code>PRINTER EMULATION</code> section for more details.</dl>
<p> <i>-h</i><br />
 <i>&#8211;help</i></p>
<dl>
<dt>
<dd> Give brief usage help, listing available options.</dl>
<p> <i>&#8211;if2cart file</i></p>
<dl>
<dt>
<dd> Insert the specified file into the emulated Interface II.</dl>
<p> <i>&#8211;interface1</i></p>
<dl>
<dt>
<dd> Emulate a Sinclair Interface I. Same as the Peripherals Options dialog&#8217;s <i>Interface I</i> option.</dl>
<p> <i>&#8211;interface2</i></p>
<dl>
<dt>
<dd> Emulate a Sinclair Interface II. (Enabled by default, but you can use `<i>&#8211;no-interface2</i>&#8216; to disable). Same as the Peripherals Options dialog&#8217;s <i>Interface II</i> option.</dl>
<p> <i>&#8211;issue2</i></p>
<dl>
<dt>
<dd> Emulate an issue 2 keyboard. Same as the General Options dialog&#8217;s <i>Issue 2 keyboard</i> option.</dl>
<p> <i>-j device</i><br />
 <i>&#8211;joystick-1 device</i></p>
<dl>
<dt>
<dd> Read from <i>device</i> to emulate the first joystick. Fuse will use either `<i>/dev/input/js0</i>&#8216; or `<i>/dev/js0</i>&#8216; by default.</dl>
<p> <i>&#8211;joystick-2 device</i></p>
<dl>
<dt>
<dd> As for <i>&#8211;joystick-1</i> but for the second joystick; the default here is either `<i>/dev/input/js1</i>&#8216; or `<i>/dev/js1</i>&#8216;.</dl>
<p> <i>&#8211;joystick-prompt</i></p>
<dl>
<dt>
<dd> If this option is specified, Fuse Fuse will prompt you which form of joystick emulation you wish to use when loading a snapshot. No prompt will be issued if the configuration in the snapshot matches what you are currently using. The same as the General Options dialog&#8217;s <i>Snap joystick prompt</i> option.</dl>
<p> <i>&#8211;kempston</i></p>
<dl>
<dt>
<dd> Emulate a Kempston joystick. Same as the Peripherals Options dialog&#8217;s <i>Kempston joystick</i> option.</dl>
<p> <i>&#8211;kempston-mouse</i></p>
<dl>
<dt>
<dd> Emulate a Kempston mouse. Same as the Peripherals Options dialog&#8217;s <i>Kempston mouse</i> option.</dl>
<p> <i>&#8211;late-timings</i></p>
<dl>
<dt>
<dd> It has been observed that some real Spectrums run such that the screen is rendered one tstate later than on other real hardware. This option specifies that Fuse should emulate such a machine. Same as the General Options dialog&#8217;s <i>Late timings</i> option.</dl>
<p> <i>&#8211;loading-sound</i></p>
<dl>
<dt>
<dd> Specify whether the sound made while tapes are loading should be emulated. (Enabled by default, but you can use `<i>&#8211;no-loading-sound</i>&#8216; to disable). Same as the Sound Options dialog&#8217;s <i>Loading sound</i> option.</dl>
<p> <i>-m type</i><br />
 <i>&#8211;machine type</i></p>
<dl>
<dt>
<dd> Specify machine type to emulate initially. The default is <i>48</i>, a 48K Spectrum. The available options are <i>16</i>, <i>48</i>, <i>128</i>, <i>plus2</i>, <i>plus2a</i>, <i>plus3</i>, <i>2048</i>, <i>2068</i>, <i>ts2068</i>, <i>pentagon</i>, <i>pentagon512</i>, <i>pentagon1024</i>, and <i>scorpion</i>.</dl>
<p> <i>&#8211;microdrive-file file</i><br />
 <i>&#8211;microdrive-2-file file</i><br />
 <i>&#8211;microdrive-3-file file</i><br />
 <i>&#8211;microdrive-4-file file</i><br />
 <i>&#8211;microdrive-5-file file</i><br />
 <i>&#8211;microdrive-6-file file</i><br />
 <i>&#8211;microdrive-7-file file</i><br />
 <i>&#8211;microdrive-8-file file</i></p>
<dl>
<dt>
<dd> Specify Interface I Microdrive cartridge files to open.</dl>
<p> <i>-p file</i><br />
 <i>&#8211;playback file</i></p>
<dl>
<dt>
<dd> Specify an RZX file to begin playback from.</dl>
<p> <i>&#8211;paltv2x</i></p>
<dl>
<dt>
<dd> Specify whether the PAL TV 2x and PAL TV 3x scalers should also produce scanlines along the lines of the TV 2x and Timex TV scalers. The same as the General Options dialog&#8217;s <i>PAL-TV use TV2x effect</i> option.</dl>
<p> <i>&#8211;plus3disk file</i></p>
<dl>
<dt>
<dd> Insert the specified file into the emulated +3&#8217;s A: drive; also select the +3 on startup if available.</dl>
<p> <i>&#8211;plusd</i></p>
<dl>
<dt>
<dd> Emulate a +D interface. Same as the Peripherals Options dialog&#8217;s <i>+D interface</i> option.</dl>
<p> <i>&#8211;plusddisk file</i></p>
<dl>
<dt>
<dd> Insert the specified file into the emulated +D&#8217;s drive 1.</dl>
<p> <i>&#8211;printer</i></p>
<dl>
<dt>
<dd> Specify whether the emulation should include a printer. Same as the Peripherals Options dialog&#8217;s <i>Emulate printers</i> option.</dl>
<p> <i>&#8211;rate frame</i></p>
<dl>
<dt>
<dd> Specify the frame rate, the ratio of spectrum frame updates to real frame updates. Same as the General Options dialog&#8217;s <i>Frame rate</i> option.</dl>
<p> <i>-r file</i><br />
 <i>&#8211;record file</i></p>
<dl>
<dt>
<dd> Specify an RZX file to begin recording to.</dl>
<p> <i>&#8211;rom-16 file</i><br />
 <i>&#8211;rom-48 file</i><br />
 <i>&#8211;rom-128-0 file</i><br />
 <i>&#8211;rom-128-1 file</i><br />
 <i>&#8211;rom-plus2-0 file</i><br />
 <i>&#8211;rom-plus2-1 file</i><br />
 <i>&#8211;rom-plus2a-0 file</i><br />
 <i>&#8211;rom-plus2a-1 file</i><br />
 <i>&#8211;rom-plus2a-2 file</i><br />
 <i>&#8211;rom-plus2a-3 file</i><br />
 <i>&#8211;rom-plus3-0 file</i><br />
 <i>&#8211;rom-plus3-1 file</i><br />
 <i>&#8211;rom-plus3-2 file</i><br />
 <i>&#8211;rom-plus3-3 file</i><br />
 <i>&#8211;rom-plus3e-0 file</i><br />
 <i>&#8211;rom-plus3e-1 file</i><br />
 <i>&#8211;rom-plus3e-2 file</i><br />
 <i>&#8211;rom-plus3e-3 file</i><br />
 <i>&#8211;rom-tc2048 file</i><br />
 <i>&#8211;rom-tc2068-0 file</i><br />
 <i>&#8211;rom-tc2068-1 file</i><br />
 <i>&#8211;rom-ts2068-0 file</i><br />
 <i>&#8211;rom-ts2068-1 file</i><br />
 <i>&#8211;rom-pentagon-0 file</i><br />
 <i>&#8211;rom-pentagon-1 file</i><br />
 <i>&#8211;rom-pentagon-2 file</i><br />
 <i>&#8211;rom-pentagon-3 file</i><br />
 <i>&#8211;rom-scorpion-0 file</i><br />
 <i>&#8211;rom-scorpion-1 file</i><br />
 <i>&#8211;rom-scorpion-2 file</i><br />
 <i>&#8211;rom-scorpion-3 file</i><br />
 <i>&#8211;rom-spec-se-0 file</i><br />
 <i>&#8211;rom-spec-se-1 file</i><br />
 <i>&#8211;rom-interface-1 file</i><br />
 <i>&#8211;rom-plusd file</i><br />
 <i>&#8211;rom-beta128 file</i></p>
<dl>
<dt>
<dd> Specify the file to be used for ROM(s) used for each machine. The options respectively refer to the 16K Spectrum (<i>48.rom</i>), 48K Spectrum (<i>48.rom</i>), the two ROMs for the 128K Spectrum (<i>128-0.rom</i> and <i>128-1.rom</i>), the two ROMs for the +2 (<i>plus2-0.rom</i> and <i>plus2-1.rom</i>), the four ROMs for the +2A (<i>plus3-0.rom</i>, <i>plus3-1.rom</i>, <i>plus3-2.rom</i> and <i>plus3-3.rom</i>), the four ROMs for the +3 (<i>plus3-0.rom</i>, <i>plus3-1.rom</i>, <i>plus3-2.rom</i> and <i>plus3-3.rom</i>), the TC2048 ROM (<i>tc2048.rom</i>), the two ROMs for the TC2068 (<i>tc2068-0.rom</i> and <i>tc2068-1.rom</i>), the two ROMs for the TS2068 (<i>tc2068-0.rom</i> and <i>tc2068-1.rom</i>), the two main ROMs, the TR-DOS ROM and a reset service ROM for the Pentagon (<i>128p-0.rom</i>, <i>128p-1.rom</i>, <i>trdos.rom</i> and <i>gluck.rom</i>), the four ROMs for the Scorpion 256 (<i>256s-0.rom</i>, <i>256s-1.rom</i>, <i>256s-2.rom</i> and <i>256s-3.rom</i>), the two ROMs for the Spectrum SE (<i>se-0.rom</i> and <i>se-1.rom</i>), the Interface I ROM (<i>if1-2.rom</i>), the +D ROM (<i>plusd.rom</i>), and the TR-DOS ROM for Beta 128 emulation with the 128K or +2 (<i>trdos.rom</i>). The names in brackets denote the defaults.</dl>
<p> <i>&#8211;no-rs232-handshake</i></p>
<dl>
<dt>
<dd> This option makes Fuse&#8217;s Interface I emulation assume that the RS-232 line other end is live when you connect the communication channels. See also the `<i>&#8211;rs232-rx</i>&#8216; and `<i>&#8211;rs232-tx</i>&#8216; options.</dl>
<p> <i>&#8211;rs232-rx</i><br />
 <i>&#8211;rs232-tx</i></p>
<dl>
<dt>
<dd> Specify the communication channels (FIFO or file) to be used for Interface I RS-232 emulation as RxD and TxD wire. See also the `<i>&#8211;rs232-handshake</i>&#8216; options.</dl>
<p> <i>&#8211;rzx-autosaves</i></p>
<dl>
<dt>
<dd> Specify that, while recording an RZX file, Fuse should automatically add a snapshot to the recording stream every 5 seconds. (Default to on, but you can use `<i>&#8211;no-rzx-autosaves</i>&#8216; to disable). Same as the RZX Options dialog&#8217;s &quot;Create autosaves&quot; option; see there for more details.</dl>
<p> <i>&#8211;separation</i></p>
<dl>
<dt>
<dd> Give stereo separation of the 128&#8217;s AY sound channels. Same as the General Options dialog&#8217;s <i>AY stereo separation</i> option.</dl>
<p> <i>&#8211;simpleide</i></p>
<dl>
<dt>
<dd> Specify whether Fuse will emulate the simple 8-bit IDE interface as used by the Spectrum +3e. Same as the Peripherals Options dialog&#8217;s <i>Simple 8-bit IDE</i> option.</dl>
<p> <i>&#8211;simpleide-masterfile file</i></p>
<dl>
<dt>
<dd> Specify a HDF file to connect to the emulated Simple 8-bit IDE interface&#8217;s master channel.</dl>
<p> <i>&#8211;simpleide-slavefile file</i></p>
<dl>
<dt>
<dd> Specify a HDF file to connect to the emulated Simple 8-bit IDE interface&#8217;s slave channel.</dl>
<p> <i>&#8211;slt</i></p>
<dl>
<dt>
<dd> Support the SLT trap instruction. (Enabled by default, but you can use `<i>&#8211;no-slt</i>&#8216; to disable). Same as the General Options dialog&#8217;s <i>Use .slt traps</i> option.</dl>
<p> <i>-s file</i><br />
 <i>&#8211;snapshot file</i></p>
<dl>
<dt>
<dd> Specify a snapshot file to load. The file can be in any snapshot format supported by <i><a href="/docs/linux/man/3-libspectrum/">libspectrum</a></i>(3).</dl>
<p> <i>&#8211;sound</i></p>
<dl>
<dt>
<dd> Specify whether Fuse should produce sound. (Enabled by default, but you can use `<i>&#8211;no-sound</i>&#8216; to disable). Same as the Sound Options dialog&#8217;s <i>Sound enabled</i> option.</dl>
<p> <i>&#8211;sound-force-8bit</i></p>
<dl>
<dt>
<dd> Force the use of 8-bit sound, even if 16-bit is possible. Same as the Sound Options dialog&#8217;s <i>Force 8-bit</i> option.</dl>
<p> <i>&#8211;sound-hifi</i></p>
<dl>
<dt>
<dd> Use higher fidelity sound generation to improve the reproduction of some multi-channel beeper tunes by reducing aliasing noise (e.g. Fairlight 2). Same as the Sound Options dialog&#8217;s <i>Hi-fi beeper</i> option.</dl>
<p> <i>-d device</i><br />
 <i>&#8211;sound-device device</i></p>
<dl>
<dt>
<dd> Specify the sound output device to use and any options to give that device. If you are not using the SDL UI or using <i>libao</i> or <i>libasound (ALSA)</i> for sound output, then the <i>device</i> parameter just specifies the device to be used for sound output. </p>
<p> If you are using the SDL UI, the <i>device</i> parameter allows you to specify the audio driver to be used (e.g. dsp, alsa, dma, esd and arts). </p>
<p> If you are using <i>libao</i> for sound output, the <i>device</i> parameter allows you to specify the device used for sound output (either `live&#8217; to a speaker or to a file) and the parameters to be used for that device. In general, the <i>device</i> parameter has the form <i>driver[:param[=value][,param[=value][,&#8230;]]</i>. <i>driver</i> selects the libao driver to be used, either one of the `live&#8217; drivers (<i>aixs</i>, <i>alsa</i>, <i>alsa09</i>, <i>arts</i>, <i>esd</i>, <i>irix</i> , <i>macosx</i>, <i>nas</i>, <i>oss</i> or <i>sun</i>) or a file driver (<i>au</i>, <i>raw</i>, <i>wav</i> or <i>null</i>). The available parameter and value pairs for each device are:</p>
<dl>
<dt>[bu]</p>
<dd> <i>aixs</i>: AIX audio system</p>
<dl>
<dt>
<dd>
<dl>
<dt>[bu]</p>
<dd> dev=<i>device</i><br />
 `<i>device</i>&#8216; gives the AIX sound device.</dl>
</dl>
<dt>[bu]</p>
<dd> <i>alsa</i>: Advanced Linux Sound Architecture version 0.5.x</p>
<dl>
<dt>
<dd>
<dl>
<dt>[bu]</p>
<dd> card=<i>num</i><br />
 `<i>num</i>&#8216; gives the ALSA card number.</p>
<dt>[bu]</p>
<dd> dev=<i>num</i><br />
 `<i>num</i>&#8216; gives the ALSA device number.</p>
<dt>[bu]</p>
<dd> buf_size=<i>num</i><br />
 `<i>num</i>&#8216; gives the ALSA buffer size in bytes.</dl>
</dl>
<dt>[bu]</p>
<dd> <i>alsa09</i>: Advanced Linux Sound Architecture version 0.9+</p>
<dl>
<dt>
<dd>
<dl>
<dt>[bu]</p>
<dd> dev=<i>string</i><br />
 `<i>string</i>&#8216; specfies the ALSA device e.g. hw:1.2</p>
<dt>[bu]</p>
<dd> buffer_time=<i>num</i><br />
 `<i>num</i>&#8216; gives the ALSA buffer time in microseconds.</p>
<dt>[bu]</p>
<dd> period_time=<i>num</i><br />
 `<i>num</i>&#8216; gives the ALSA period time in microseconds.</p>
<dt>[bu]</p>
<dd> use_mmap=<i>yes|y|true|t|1</i><br />
 specifies that libao use memory mapped transfer.</dl>
</dl>
<dt>[bu]</p>
<dd> <i>arts</i>: aRts soundserver: no parameters.</p>
<dt>[bu]</p>
<dd> <i>esd</i>: Enlightened Sound Daemon.</p>
<dl>
<dt>
<dd>
<dl>
<dt>[bu]</p>
<dd> host=<i>string</i><br />
 `<i>string</i>&#8216; gives the ESD host specification.</dl>
</dl>
<dt>[bu]</p>
<dd> <i>irix</i>: IRIX Audio Library: no parameters.</p>
<dt>[bu]</p>
<dd> <i>macosx</i>: MacOS X CoreAudio: no parameters.</p>
<dt>[bu]</p>
<dd> <i>nas</i>: Network Audio System.</p>
<dl>
<dt>
<dd>
<dl>
<dt>[bu]</p>
<dd> host=<i>string</i><br />
 `<i>string</i>&#8216; gives the NAS host specification.</p>
<dt>[bu]</p>
<dd> buf_size=<i>num</i><br />
 `<i>num</i>&#8216; gives the buffer size on the server.</dl>
</dl>
<dt>[bu]</p>
<dd> <i>oss</i>: Open Sound System.</p>
<dl>
<dt>
<dd>
<dl>
<dt>[bu]</p>
<dd> dsp=<i>string</i><br />
 `<i>string</i>&#8216; gives the OSS device to be used e.g. /dev/sound/dsp1</dl>
</dl>
<dt>[bu]</p>
<dd> <i>sun</i>: SUN audio system.</p>
<dl>
<dt>
<dd>
<dl>
<dt>[bu]</p>
<dd> dev=<i>string</i><br />
 `<i>string</i>&#8216; gives the audio device to be used.</dl>
</dl>
<dt>[bu]</p>
<dd> <i>au</i>: SUN Sparc audio file: no parameters.</p>
<dt>[bu]</p>
<dd> <i>raw</i>: raw file.</p>
<dl>
<dt>
<dd>
<dl>
<dt>[bu]</p>
<dd> byteorder=<i>string</i><br />
 `<i>string</i>&#8216; can be any of <i>native</i> (host native byteorder), <i>big</i> (big endian) or <i>little</i> (little endian).</dl>
</dl>
<dt>[bu]</p>
<dd> <i>wav</i>: Microsoft audio file: no parameters.</p>
<dt>[bu]</p>
<dd> <i>null</i>: null output: no parameters.</p>
<dt>[bu]</p>
<dd> <i>debug</i>: for debugging libao.</dl>
<p> Finally, each of the file output types (<i>au</i>, <i>raw</i> and <i>wav</i>) have an extra option `file=<i>filename</i>&#8216; where `<i>filename</i>&#8216; gives the file output will be directed to. This defaults to `<i>fuse-sound.ao</i>&#8216; if it is not specified. </p>
<p> Some examples of use: </p>
<p> <i>fuse -d alsa09:dev=hw:1</i> </p>
<p> causes Fuse to use ALSA 0.9+ output with the second (#1) sound card. </p>
<p> <i>fuse -d raw:byteorder=little,file=enigma.raw</i> </p>
<p> causes Fuse to save little endian words to `<i>enigma.raw</i>&#8216;. </p>
<p> See the `DEVICE&#8217; section of <i><a href="/docs/linux/man/1-ogg123/">ogg123</a>(1)</i> for up to date information of devices and options (except for the `file&#8217; option which is provided by Fuse itself).<br />
 If you are using <i>libasound</i> or <i>ALSA</i> for sound output, the <i>device</i> parameter allows you to specify the device used for sound output and some parameters to be used for that device. In general, the <i>device</i> parameter has the form<br />
 <i>devstr</i> or<br />
 <i>param[=value][,param[=value][,&#8230;][,devstr]</i>.</p>
<dl>
<dt>[bu]</p>
<dd> <i>devstr</i>: selects the ALSA device used, it can be any complex or simple ALSA device name. e.g.: <i>default</i> or <i>hw:0</i> or <i>tee:plughw:0,aq/tmp/out.rawaq,raw</i> See the alsa-lib pcm api reference at <a rel="nofollow" href="http://www.alsa-project.org/alsa-doc/alsa-lib/pcm.html">http://www.alsa-project.org/alsa-doc/alsa-lib/pcm.html</a> for further explanation. </p>
<dt>[bu]</p>
<dd> <i>param</i> and <i>values</i>:</p>
<dl>
<dt>
<dd>
<dl>
<dt>[bu]</p>
<dd> <i>buffer=nnnn</i>: set the ALSA buffer in frames, smaller value cause smaller sound delay but may more buffer underrun (pops and clicks), larger value cause longer delay but fewer underrun. By default Fuse determine the buffer size based on the actual sound frequency.<br />
 If you use some special plugin for your pcm device (e.g.: dmix) or your card not support some needed parameter (e.g. cannot play other only 48 kHz stereo sound like some AC97 sound card) may cause Fuse unable to set the needed buffer size, appropriate sound frequency, channels and so on, therefore you cannot get optimal result or not hear the sound at all. In this case try the <i>plughw:#</i>, (where # mean your card number counted from 0) for ALSA device. </p>
<dt>[bu]</p>
<dd> <i>verbose</i> : if given, fuse report ALSA buffer underruns to <i>stderr</i>
</dl>
</dl>
</dl>
<p> Some examples of use: </p>
<p> <i>fuse -d verbose,buffer=2000</i> </p>
<p> causes Fuse to use the default ALSA device with 2000 frame length buffer and report ALSA buffer underruns on <i>stderr</i>. </p>
<p> <i>fuse -d tee:plughw:0,aq/tmp/aufwm.rawaq,raw</i> </p>
<p> causes Fuse to use the first card and parallel save the raw audio samples into <i>/tmp/aufwm.raw</i> file.
</dl>
<p> <i>&#8211;speed percentage</i></p>
<dl>
<dt>
<dd> Specify the speed (as a percentage of real Spectrum speed) at which emulation should attempt to proceed. Same as the General Options dialog&#8217;s <i>Emulation speed</i> option.</dl>
<p> <i>&#8211;statusbar</i></p>
<dl>
<dt>
<dd> For the GTK+ UI, enables the statusbar beneath the display. For the SDL UI, enables the status icons showing whether the disk and tape are being accessed. Same as the General Options dialog&#8217;s <i>Show statusbar</i> option.</dl>
<p> <i>&#8211;strict-aspect-hint</i></p>
<dl>
<dt>
<dd> For the GTK+ UI, use stricter limits for the aspect ratio limits set by the `<i>&#8211;aspect-hint</i>&#8216; option. This can cause some window managers (for example, <i><a href="/docs/linux/man/1-metacity/">metacity</a></i>(1)) to not allow the window to be resized and moved, but is necessary to prevent others (for example, <i><a href="/docs/linux/man/1-fvwm/">fvwm</a></i>(1)) from being able resize the window away from square.</dl>
<p> <i>-v mode</i><br />
 <i>&#8211;svgamode mode</i></p>
<dl>
<dt>
<dd> Specify which mode to use for the SVGAlib and FB UIs. Available values for <i>mode</i> are `320&#8242; (which corresponds to a 320x240x256 mode), the default and `640&#8242; (a 640x480x256 mode).</dl>
<p> <i>-D mode</i><br />
 <i>&#8211;doublescan-mode mode</i></p>
<dl>
<dt>
<dd> Specify whether to use doublescan modes in the SVGAlib and FB UIs. Available values for <i>mode</i> are 0, 1 and 2. 0 means `never doublescan&#8217; (use 640&#215;480 at either 72 Hz or 60 Hz), whereas 1 and 2 both mean `try to use doublescan&#8217; and will fall back on the 640&#215;480 modes. These latter two are treated identically for SVGA, but for FB, they differ: 1 selects 72 Hz modes (the same size and shape as your typical 640&#215;480), and 2 selects 60 Hz modes (overscan).<br />
 If your monitor displays a blank screen when using 1 or 2, press F10 then try a different option or say `&#8211;svgamode 640&#8242;.</dl>
<p> <i>-t file</i><br />
 <i>&#8211;tape file</i></p>
<dl>
<dt>
<dd> Specify a virtual tape file to use. It must be in TAP or TZX format.</dl>
<p> <i>&#8211;textfile file</i></p>
<dl>
<dt>
<dd> Set the filename used for text output from the emulated printers. See the <code>PRINTER EMULATION</code> section below for more details.</dl>
<p> <i>&#8211;traps</i></p>
<dl>
<dt>
<dd> Support traps for ROM tape loading/saving. (Enabled by default, but you can use `<i>&#8211;no-traps</i>&#8216; to disable). Same as the General Options dialog&#8217;s <i>Use tape traps</i> option.</dl>
<p> <i>&#8211;betadisk file</i></p>
<dl>
<dt>
<dd> Insert the specified file into the emulated Beta disk interface&#8217;s drive A: and select Pentagon mode on startup.</dl>
<p> <i>-V</i><br />
 <i>&#8211;version</i></p>
<dl>
<dt>
<dd> Show which version of Fuse is being used.</dl>
<p> <i>&#8211;writable-roms</i></p>
<dl>
<dt>
<dd> Allow Spectrum programs to overwrite the ROM(s). The same as the General Options dialog&#8217;s <i>Allow writes to ROM</i> option.</dl>
<p> <i>&#8211;zxatasp</i></p>
<dl>
<dt>
<dd> Specify whether Fuse emulate the ZXATASP interface. Same as the Peripherals Options dialog&#8217;s <i>ZXATASP interface</i> option.</dl>
<p> <i>&#8211;zxatasp-upload</i></p>
<dl>
<dt>
<dd> Specify the state of the ZXATASP upload jumper. Same as the Peripherals Options dialog&#8217;s <i>ZXATASP upload</i> option.</dl>
<p> <i>&#8211;zxatasp-write-protect</i></p>
<dl>
<dt>
<dd> Specify the state of the ZXATASP write protect jumper. Same as the Peripherals Options dialog&#8217;s <i>ZXATASP write protect</i> option.</dl>
<p> <i>&#8211;zxatasp-masterfile file</i></p>
<dl>
<dt>
<dd> Specify a HDF file to connect to the emulated ZXATASP interface&#8217;s master channel.</dl>
<p> <i>&#8211;zxatasp-slavefile file</i></p>
<dl>
<dt>
<dd> Specify a HDF file to connect to the emulated ZXATASP interface&#8217;s slave channel.</dl>
<p> <i>&#8211;zxcf</i></p>
<dl>
<dt>
<dd> Specify whether Fuse emulate the ZXCF interface. Same as the Peripherals Options dialog&#8217;s <i>ZXCF interface</i> option.</dl>
<p> <i>&#8211;zxcf-upload</i></p>
<dl>
<dt>
<dd> Specify the state of the ZXCF upload jumper. Same as the Peripherals Options dialog&#8217;s <i>ZXCF upload</i> option.</dl>
<p> <i>&#8211;zxcf-cffile file</i></p>
<dl>
<dt>
<dd> Specify a HDF file to connect to the emulated ZXCF interface.</dl>
<p> All long options which control on/off settings can be disabled using `<i>&#8211;no-foo</i>&#8216; (for an option `<i>&#8211;foo</i>&#8216;). For example, the opposite of `<i>&#8211;issue2</i>&#8216; is `<i>&#8211;no-issue2</i>&#8216;. These options can also be modified while the emulator is running, using the options dialogs &#8211; see the documentation for the <i>Options</i> menu in the <code>MENUS AND KEYS</code> section for details.</p>
<h2>THE VARIOUS FRONT-ENDS</h2>
<p> Fuse supports various front-ends, or UIs (user interfaces). The usual one is GTK+-based, but there are also SDL, Xlib, SVGAlib and framebuffer ones. </p>
<p> The important difference to note is that the GTK+ version uses `native&#8217; dialog boxes etc. (behaving like a fairly normal GUI-based program) while the others use an alternative, Fuse-specific `widget UI&#8217;. This latter front-end is easily spotted by the way it uses the main Fuse window/screen for menus and dialogs, and uses the Spectrum&#8217;s own font.</p>
<h2>MENUS AND KEYS</h2>
<p> Since many of the keys available are devoted to emulation of the Spectrum&#8217;s keyboard, the primary way of controlling Fuse itself (rather than the emulated machine) is via the menus. There are also function key shortcuts for some menu options. </p>
<p> In the GTK+ version, the menu bar is always visible at the top of the Fuse window. You can click on a menu name to pop it up. Alternatively, you can press <i>F1</i> to display a pop-up version of the menu bar, which you can then navigate with the cursor keys or mouse. </p>
<p> In the widget UI pressing <i>F1</i> is the only way to get the main menu; and unlike the GTK+ version, the emulator pauses while the menus are being navigated. The menus show which key to press for each menu option in brackets. Pressing <i>Esc</i> exits a menu, and pressing <i>Enter</i> exits the menu system entirely (as well as `confirming&#8217; any current dialog). </p>
<p> Here&#8217;s what the menu options do, along with the function key mappings for those items which have them: </p>
<p> <i>F3</i><br />
 <i>File, Open&#8230;</i></p>
<dl>
<dt>
<dd> Open a Spectrum file. Snapshots will be loaded into memory; tape images will be inserted into the emulated tape deck, and if the <i>Auto-load media</i> option is set will being loading. Opening a disk image or a Timex dock image will cause the appropriate machine type (+3, Pentagon or TC2068) to be selected with the image inserted, and disks will automatically load if the <i>Auto-load media</i> option is set. See the <code>FILE SELECTION</code> section below for details on how to choose the file. Note that this behaviour is different from previous versions of Fuse, when this option would open only snapshots.</dl>
<p> <i>F2</i><br />
 <i>File, Save Snapshot&#8230;</i></p>
<dl>
<dt>
<dd> Save a snapshot (machine state, memory contents, etc.) to file. You can select the filename to be saved to. If it has a .szx, .z80 or .sna extension, the snapshot will be saved in that format. Otherwise, it will be saved as a .szx file.</dl>
<p> <i>File, Recording, Record&#8230;</i></p>
<dl>
<dt>
<dd> Start recording input to an RZX file, initialised from the current emulation state. You will be prompted for a filename to use.</dl>
<p> <i>File, Recording, Record from snapshot&#8230;</i></p>
<dl>
<dt>
<dd> Start recording input to an RZX file, initialised from a snapshot. You will first be asked for the snapshot to use and then the file to save the recording to.</dl>
<p> <i>Insert</i><br />
 <i>File, Recording, Insert snapshot</i></p>
<dl>
<dt>
<dd> Inserts a snapshot of the current state into the RZX file. This can be used at a later point to roll back to the inserted state by using one of the commands below.</dl>
<p> <i>Delete</i><br />
 <i>File, Recording, Rollback</i></p>
<dl>
<dt>
<dd> Rolls back the recording to the point at which the previous snapshot was inserted. Recording will continue from that point.</dl>
<p> <i>File, Recording, Rollback to&#8230;</i></p>
<dl>
<dt>
<dd> Roll back the recording to any snapshot which has been inserted into the recording.</dl>
<p> <i>File, Recording, Play&#8230;</i></p>
<dl>
<dt>
<dd> Playback recorded input from an RZX file. This lets you replay keypresses recorded previously. RZX files generally contain a snapshot with the Spectrum&#8217;s state at the start of the recording; if the selected RZX file doesn&#8217;t, you&#8217;ll be prompted for a snapshot to load as well.</dl>
<p> <i>File, Recording, Stop</i></p>
<dl>
<dt>
<dd> Stop any currently-recording/playing RZX file.</dl>
<p> <i>File, AY Logging, Record&#8230;</i></p>
<dl>
<dt>
<dd> Start recording the bytes output via the AY-3-8192 sound chip to a PSG file. You will be prompted for a filename to save the recording to.</dl>
<p> <i>File, AY Logging, Stop</i></p>
<dl>
<dt>
<dd> Stop any current AY logging.</dl>
<p> <i>File, Open SCR Screenshot&#8230;</i></p>
<dl>
<dt>
<dd> Load an SCR screenshot (essentially just a binary dump of the Spectrum&#8217;s video memory) onto the current screen. Fuse supports screenshots saved in the Timex hi-colour and hi-res modes as well as `normal&#8217; Spectrum screens, and will make a simple conversion if a hi-colour or hi-res screenshot is loaded onto a non-Timex machine.</dl>
<p> <i>File, Save Screen as SCR&#8230;</i></p>
<dl>
<dt>
<dd> Save a copy of whatever&#8217;s currently displayed on the Spectrum&#8217;s screen as an SCR file. You will be prompted for a filename to save the screenshot to.</dl>
<p> <i>File, Save Screen as PNG&#8230;</i></p>
<dl>
<dt>
<dd> Save the current screen as a PNG file. You will be prompted for a filename to save the screenshot to.</dl>
<p> <i>File, Movies, Record Movie as SCR&#8230;</i></p>
<dl>
<dt>
<dd> Start recording a `movie&#8217; as a series of SCR screenshots. You will be prompted for a filename, and the screenshots will then be saved to `<i>&lt;name&gt;-frame-000000000.scr</i>&#8216;, `<i>&lt;name&gt;-frame-000000001.scr</i>&#8216; and so on.</dl>
<p> <i>File, Movies, Record Movie as PNG&#8230;</i></p>
<dl>
<dt>
<dd> Start recording a `movie&#8217; as a series of PNG images. The filenames used will be the same as for the SCR movie, but with a `<i>.png</i>&#8216; extension instead of `<i>.scr</i>&#8216;.</dl>
<p> <i>File, Movies, Stop Movie Recording</i></p>
<dl>
<dt>
<dd> Stop any movie recording which is currently in progress.</dl>
<p> <i>File, Load Binary Data&#8230;</i></p>
<dl>
<dt>
<dd> Load binary data from a file into the Spectrum&#8217;s memory. After selecting the file to load data from, you can choose where to load the data and how much data to load.</dl>
<p> <i>File, Save Binary Data&#8230;</i></p>
<dl>
<dt>
<dd> Save an arbitrary chunk of the Spectrum&#8217;s memory to a file. Select the file you wish to save to, followed by the location and length of data you wish to save.</dl>
<p> <i>F10</i><br />
 <i>File, Exit</i></p>
<dl>
<dt>
<dd> Exit the emulator. A confirmation dialog will appear checking you actually want to do this.</dl>
<p> <i>F4</i><br />
 <i>Options, General&#8230;</i></p>
<dl>
<dt>
<dd> Display the General Options dialog, letting you configure Fuse. (With the widget UI, the keys shown in brackets toggle the options, <i>Enter</i> confirms any changes, and <i>Esc</i> aborts). Note that any changed settings only apply to the currently-running Fuse. </p>
<p> The options available are: </p>
<p> <i>Emulation speed</i></p>
<dl>
<dt>
<dd> Set how fast Fuse will attempt to emulate the Spectrum, as a percentage of the speed at which the real machine runs. If your machine isn&#8217;t fast enough to keep up with the requested speed, Fuse will just run as fast as it can. Note that if the emulation speed is not exactly 100%, no sound output will be produced.</dl>
<p> <i>Frame rate</i></p>
<dl>
<dt>
<dd> Specify the frame rate, the ratio of spectrum frame updates to real frame updates. This is useful if your machine is having trouble keeping up with the spectrum screen updates.</dl>
<p> <i>Issue 2 keyboard</i></p>
<dl>
<dt>
<dd> Early versions of the Spectrum used a different value for unused bits on the keyboard input ports, and a few games depended on the old value of these bits. Enabling this option switches to the old value, to let you run them.</dl>
<p> <i>Use tape traps</i></p>
<dl>
<dt>
<dd> Ordinarily, Fuse intercepts calls to the ROM tape-loading routine in order to load from tape files more quickly when possible. But this can (rarely) interfere with TZX loading; disabling this option avoids the problem at the cost of slower (i.e. always real-time) tape-loading. When tape-loading traps are disabled, you need to start tape playback manually, by pressing <i>F8</i> or choosing the <i>Media, Tape, Play</i> menu item. Fuse also uses tape traps to intercept the tape-saving routine in the ROM to save tape files quickly, tapes can also be saved using the <i>Media, Tape, Record Start</i> menu item.</dl>
<p> <i>Fastloading</i></p>
<dl>
<dt>
<dd> If this option is enabled, then Fuse will run at the fastest possible speed when the virtual tape is playing, thus dramatically reducing the time it takes to load programs. You may wish to disable this option if you wish to stop the tape at a specific point.</dl>
<p> <i>Detect loaders</i></p>
<dl>
<dt>
<dd> If this option is enabled, Fuse will attempt to detect when a loading routine is in progress, and then automatically start the virtual tape to load the program in. This is done by using a heuristic to identify a loading routine, so is by no means infallible, but works in most cases.</dl>
<p> <i>Auto-load media</i></p>
<dl>
<dt>
<dd> On many occasions when you open a tape or disk file, it&#8217;s because it&#8217;s got a program in you want to load and run. If this option is selected, this will automatically happen for you when you open one of these files using the <i>File, Open&#8230;</i> menu option &#8211; you must then use the Media menu to use tapes or disks for saving data to, or for loading data into an already running program.</dl>
<p> <i>Use .slt traps</i></p>
<dl>
<dt>
<dd> The multi-load aspect of SLT files requires a trap instruction to be supported. This instruction is not generally used except for this trap, but since it&#8217;s not inconceivable that a program could be wanting to use the real instruction instead, you can choose whether to support the trap or not.</dl>
<p> <i>Allow writes to ROM</i></p>
<dl>
<dt>
<dd> If this option is selected, Fuse will happily allow programs to overwrite what would normally be ROM. This probably isn&#8217;t very useful in most circumstances, especially as the 48K ROM overwrites parts of itself.</dl>
<p> <i>Auto-save settings</i></p>
<dl>
<dt>
<dd> If this option is selected, Fuse will automatically write its currently selected options to its configuration file on exit (if <i>libxml2</i> was available when Fuse was compiled). If you turn this option off, you&#8217;ll have to manually use <i>Options, Save</i> afterwards to ensure that this setting gets written to Fuse&#8217;s configuration file.</dl>
<p> <i>MDR cartridge len</i></p>
<dl>
<dt>
<dd> This option controls the number of blocks in a new Microdrive cartridge. If the value smaller than 4 or greater than 254 Fuse assumes 4 or 254.</dl>
<p> <i>RS-232 handshake</i></p>
<dl>
<dt>
<dd> If you turn this option off, Fuse assumes the RS-232 line other end is live when you connect the communication channels. See also the `<i>&#8211;rs232-rx</i>&#8211;rs232-tx<i>&#8216;</i> options.</dl>
<p> <i>Black and white TV</i></p>
<dl>
<dt>
<dd> This option allows you to choose whether to simulate a colour or black and white television. This is effective only under the GTK+, Xlib and SDL user interfaces: the others will always simulate a colour TV.</dl>
<p> <i>PAL-TV use TV2x effect</i></p>
<dl>
<dt>
<dd> This option allows you to choose whether the PAL TV 2x and higher scalers also reproduce scanlines in the same way as the TV 2x, 3x and Timex TV scalers.</dl>
<p> <i>Confirm actions</i></p>
<dl>
<dt>
<dd> Specify whether `dangerous&#8217; actions (those which could cause data loss, for example resetting the Spectrum) require confirmation before occurring.</dl>
<p> <i>Show statusbar</i></p>
<dl>
<dt>
<dd> For the GTK+ UI, enables the statusbar beneath the display. For the SDL UI, enables the status icons showing whether the disk and tape are being accessed. This option has no effect for the other user interfaces.</dl>
<p> <i>Snap joystick prompt</i></p>
<dl>
<dt>
<dd> If set, Fuse will prompt you which physical joystick or keyboard you want to connect to the joystick interface enabled in the snapshot unless it already matches your current configuration.</dl>
<p> <i>Late timings</i></p>
<dl>
<dt>
<dd> If selected, Fuse will cause all screen-related timings (for example, when the screen is rendered and when memory contention occurs) to be one tstate later than &quot;normal&quot;, an effect which is present on some real hardware.</dl>
</dl>
<p> <i>Options, Sound&#8230;</i></p>
<dl>
<dt>
<dd> Display the Sound Options dialog, letting you configure Fuse&#8217;s sound output. (With the widget UI, the keys shown in brackets toggle the options, <i>Enter</i> confirms any changes, and <i>Esc</i> aborts). Note that any changed settings only apply to the currently-running Fuse. </p>
<p> <i>Sound enabled</i></p>
<dl>
<dt>
<dd> Specify whether sound output should be enabled at all. When this option is disabled, Fuse will not make any sound.</dl>
<p> <i>Loading sound</i></p>
<dl>
<dt>
<dd> Normally, Fuse emulates tape-loading noise when loading from TAPs or TZXs in real-time, albeit at a deliberately lower volume than on a real Spectrum. You can disable this option to eliminate the loading noise entirely.</dl>
<p> <i>AY stereo separation</i></p>
<dl>
<dt>
<dd> By default, the sound output is mono, since this is all you got from an unmodified Spectrum. But enabling this option gives you so-called ACB stereo (for sound from the 128&#8217;s AY-3-8912 sound chip). This actually works a little better than ACB stereo modifications for the machine itself, since it uses stereo positioning rather than simply playing on one channel only.</dl>
<p> <i>Beeper pseudo-stereo</i></p>
<dl>
<dt>
<dd> The Spectrum beeper is inherently mono, but enabling this option adds a simple fake-stereo effect. While the slight echo involved can sometimes make beeper noise sound worse, in many cases it gives an acceptable result.</dl>
<p> <i>Force 8-bit</i></p>
<dl>
<dt>
<dd> Force the use of 8-bit sound even if 16-bit (the default) is available. Note that (when the option is enabled) if 8-bit sound isn&#8217;t available then there will be no sound at all, so it&#8217;s best not to use this option unless you have a specific need for it.</dl>
<p> <i>Hi-fi beeper</i></p>
<dl>
<dt>
<dd> Use higher fidelity sound generation to improve the reproduction of some multi-channel beeper tunes by reducing aliasing noise (e.g. Fairlight 2).</dl>
</dl>
<p> <i>Options, Peripherals&#8230;</i></p>
<dl>
<dt>
<dd> Display the Peripherals Options dialog, letting you configure the peripherals which Fuse will consider to be attached to the emulated machines. (With the widget UI, the keys shown in brackets toggle the options, <i>Enter</i> confirms any changes, and <i>Esc</i> aborts). Note that any changed settings only apply to the currently-running Fuse. </p>
<p> <i>Kempston joystick</i></p>
<dl>
<dt>
<dd> If this option is selected, Fuse will emulate a Kempston joystick interface (probably the most widely supported type on the Spectrum). Note that this option is basically equivalent to plugging the interface itself into a Spectrum, not to connecting a joystick; this affects how the Spectrum responds to a read of input port 31. To use a Kempston joystick in a game, this option must be enabled, and you must also select a Kempston joystick the <i>Options, Joysticks</i> menu.</dl>
<p> <i>Kempston mouse</i></p>
<dl>
<dt>
<dd> If this option is selected, Fuse will emulate a Kempston mouse interface. </p>
<p> If you&#8217;re using Fuse full-screen, your mouse is automatically used as if attached to the Kempston interface. Otherwise, you&#8217;ll need to click on the Spectrum display in order to tell Fuse to grab the pointer (and make it invisible); to tell Fuse to release it, click the middle button (or wheel) or press Escape. </p>
<p> With the framebuffer UI, Fuse prefers to use GPM; if this is not available, it will fall back to built-in PS/2 mouse support. In this mode, it tries <i>/dev/input/mice</i>, <i>/dev/mouse</i> then <i>/dev/psaux</i>, stopping when it successfully opens one. The first of these is preferred since (at least on Linux, with a 2.6-series kernel) any type of mouse can be used and any connected mouse may be used.</dl>
<p> <i>Interface I</i></p>
<dl>
<dt>
<dd> If this option is selected, Fuse will emulate the simple Sinclair Interface I, and allow Microdrive cartridges to be connected and disconnected via the <i>Media, Interface I, Microdrive</i> menus. It also enables support for the Interface I RS-232 interface.</dl>
<p> <i>Interface II</i></p>
<dl>
<dt>
<dd> If this option is selected, Fuse will emulate a cartridge port as found on the Interface II. Cartridges can then be inserted and removed via the <i>Media, Cartridge, Interface II</i> menu. Note that the Pentagon, Scorpion, Interface II, ZXATASP and ZXCF all use the same hardware mechanism for accessing some of their extended features, so only one of these should be selected at once or unpredictable behaviour will occur.</dl>
<p> <i>Emulate printers</i></p>
<dl>
<dt>
<dd> If this option is selected, Fuse will emulate a printer. See the <code>PRINTER EMULATION</code> section for more details.</dl>
<p> <i>Simple 8-bit IDE</i></p>
<dl>
<dt>
<dd> If this option is selected, Fuse will emulate the simple 8-bit IDE interface as used by the Spectrum +3e, and allow hard disks to be connected and disconnected via the <i>Media, IDE, Simple 8-bit</i> menu.</dl>
<p> <i>ZXATASP interface</i></p>
<dl>
<dt>
<dd> If this option is selected, Fuse will emulate the ZXATASP interface, which provides both additional RAM and an IDE interface. See the <code>ZXATASP AND ZXCF</code> section for more details.</dl>
<p> <i>ZXATASP upload</i></p>
<dl>
<dt>
<dd> This option controls the state of the ZXATASP upload jumper. See the <code>ZXATASP AND ZXCF</code> section for more details.</dl>
<p> <i>ZXATASP write protect</i></p>
<dl>
<dt>
<dd> This option controls the state of the ZXATASP write protect jumper. See the <code>ZXATASP AND ZXCF</code> section for more details.</dl>
<p> <i>ZXCF interface</i></p>
<dl>
<dt>
<dd> If this option is selected, Fuse will emulate the ZXCF interface, which provides both additional RAM and a CompactFlash interface. See the <code>ZXATASP AND ZXCF</code> section for more details.</dl>
<p> <i>ZXCF upload</i></p>
<dl>
<dt>
<dd> This option controls the state of the ZXCF upload jumper. See the <code>ZXATASP AND ZXCF</code> section for more details.</dl>
<p> <i>DivIDE interface</i></p>
<dl>
<dt>
<dd> If this option is selected, Fuse will emulate the DivIDE interface. See the <code>DIVIDE</code> section for more details.</dl>
<p> <i>DivIDE write protect</i></p>
<dl>
<dt>
<dd> This option controls the state of the DivIDE write protection jumper. See the <code>DIVIDE</code> section for more details.</dl>
<p> <i>+D interface</i></p>
<dl>
<dt>
<dd> If this option is selected, Fuse will emulate the +D interface. See the <code>+D EMULATION</code> section for more details.</dl>
<p> <i>Beta 128 interface</i></p>
<dl>
<dt>
<dd> If this option is selected, Fuse will emulate the Beta 128 interface. See the <code>BETA 128 EMULATION</code> section for more details. Beta 128 emulation is enabled for the Pentagon and Scorpion machines regardless of this option.</dl>
</dl>
<p> <i>Options, RZX&#8230;</i></p>
<dl>
<dt>
<dd> Display the RZX Options dialog, letting you configure how Fuse&#8217;s deals with RZX input recordings. (With the widget UI, the keys shown in brackets toggle the options, <i>Enter</i> confirms any changes, and <i>Esc</i> aborts). Note that any changed settings only apply to the currently-running Fuse. </p>
<p> <i>Create autosaves</i></p>
<dl>
<dt>
<dd> If this option is selected, Fuse will add a snapshot into the recording stream every 5 seconds while creating an RZX file, thus enabling the rollback facilities to be used without having to explicitly add snapshots into the stream. Older snapshots will be pruned from the stream to keep the file size and number of snapshots down: each snapshot up to 15 seconds will be kept, then one snapshot every 15 seconds until one minute, then one snapshot every minute until 5 minutes, and then one snapshot every 5 minutes. Note that this &quot;pruning&quot; applies only to automatically inserted snapshots: snapshots manually inserted into the stream will never be pruned.</dl>
<p> <i>Compress RZX data</i></p>
<dl>
<dt>
<dd> If this option is selected, and <i>zlib</i> was available when Fuse was compiled, any RZX files written by Fuse will be compressed. This is generally a good thing as it makes the files significantly smaller, and you probably want to turn it off only if you&#8217;re debugging the RZX files or there&#8217;s some other program which doesn&#8217;t support compressed RZX files.</dl>
<p> <i>Competition mode</i></p>
<dl>
<dt>
<dd> Any input recordings which are started when this option is selected will be made in `competition mode&#8217;. In essence, this means that Fuse will act just like a real Spectrum would: you can&#8217;t load snapshots, pause the emulation in any way, change the speed or anything that you couldn&#8217;t do on the real machine. If any of these things are attempted, or if the emulated Fuse is running more than 5% faster or slower than normal Spectrum speed, then the recording will immediately be stopped. </p>
<p> If <i>libgcrypt</i> was available when Fuse was compiled, then recordings made with competition mode active will be digitally signed, in theory to `certify&#8217; that it was made with the above restrictions in place. <code>However, this procedure is not secure (and cannot be made so), so the presence of any signature on an RZX file should not be taken as providing proof that it was made with competition mode active.</code> This feature is included in Fuse solely as it was one of the requirements for Fuse to be used in an on-line tournament.</dl>
<p> <i>Competition code</i></p>
<dl>
<dt>
<dd> The numeric code entered here will be written into any RZX files made in competition mode. This is another feature for on-line tournaments which can be used to `prove&#8217; that the recording was made after a specific code was released. If you&#8217;re not playing in such a tournament, you can safely ignore this option.</dl>
<p> <i>Always embed snapshot</i></p>
<dl>
<dt>
<dd> Specify whether a snapshot should be embedded in an RZX file when recording is started from an existing snapshot.</dl>
</dl>
<p> <i>Options, Joysticks</i></p>
<dl>
<dt>
<dd> Fuse can emulate many of the common types of joystick which were available for the Spectrum. The input for these emulated joysticks can be taken from real joysticks attached to the emulating machine (configured via the <i>Options, Joysticks, Joystick 1&#8230;</i> and <i>Options, Joysticks, Joystick 2&#8230;</i> options), or from the <i>q</i>, <i>a</i>, <i>o</i>, <i>p</i>, and <i>Space</i> keys on the emulating machines keyboard, configured via the <i>Options, Joysticks, Keyboard&#8230;</i> option. Note that when using the keyboard to emulate a joystick, the <i>q</i>, <i>a</i>, <i>o</i>, <i>p</i>, and <i>Space</i> keys will not have their normal effect (to avoid problems with games which do things like use <i>p</i> for pause when using a joystick). </p>
<p> Each of the joysticks (including the `fake&#8217; keyboard joystick) can be configured to emulate any one of the following joystick types:</p>
<dl>
<dt>
<dd>
<p> <i>None</i></p>
<dl>
<dt>
<dd> No joystick: any input will simply be ignored.</dl>
<p> <i>Cursor</i></p>
<dl>
<dt>
<dd> A cursor joystick, equivalent to pressing <i>5</i> (left), <i>6</i> (down), <i>7</i> (up), <i>8</i> (right), and <i>0</i> (fire).</dl>
<p> <i>Kempston</i></p>
<dl>
<dt>
<dd> A Kempston joystick, read from input port 31. Note that the <i>Options, Peripherals, Kempston interface</i> option must also be set for the input to be recognised.</dl>
<p> <i>Sinclair 1</i><br />
 <i>Sinclair 2</i></p>
<dl>
<dt>
<dd> The `left&#8217; and `right&#8217; Sinclair joysticks, equivalent to pressing <i>1</i> (left), <i>2</i> (right), <i>3</i> (down), <i>4</i> (up), and <i>5</i> (fire), or <i>6</i> (left), <i>7</i> (right), <i>8</i> (down), <i>9</i> (up), and <i>0</i> (fire) respectively.</dl>
<p> <i>Timex 1</i><br />
 <i>Timex 2</i></p>
<dl>
<dt>
<dd> The `left&#8217; and `right&#8217; joysticks as attached to the Timex 2068 variant&#8217;s built-in joystick interface.</dl>
</dl>
<p> For the real joysticks, it is also possible to configure (although currently only when using the GTK+ interface) what effect each button on the joystick will have: this can be <i>Joystick Fire</i>, equivalent to pressing the emulated joystick&#8217;s fire button, <i>Nothing</i>, meaning to have no effect, or any Spectrum key, meaning that pressing that button will be equivalent to pressing that Spectrum key.</dl>
<p> <i>Options, Select ROMs</i></p>
<dl>
<dt>
<dd> An individual dialog is available for each Spectrum variant emulated by Fuse which allows selection of the ROM(s) used by that machine. Simply select the ROM you wish to use, and then reset the Spectrum for the change to take effect.</dl>
<p> <i>Options, Filter&#8230;</i></p>
<dl>
<dt>
<dd> Select the graphics filter currently in use. See the <code>GRAPHICS FILTERS</code> section for more details.</dl>
<p> <i>Options, Save</i></p>
<dl>
<dt>
<dd> If <i>libxml2</i> was available when Fuse was compiled, this will cause Fuse&#8217;s current options to be written to <i>.fuserc</i> in your home directory, from which they will be picked up again when Fuse is restarted. The best way to update this file is by using this option, but it&#8217;s a simple XML file and shouldn&#8217;t be too hard to edit by hand if you really want to.</dl>
<p> <i>Pause</i><br />
 <i>Machine, Pause</i></p>
<dl>
<dt>
<dd> Pause or unpause emulation. This option is available only under the GTK+ UI; to pause the other user interfaces, simply press F1 to bring up the main menu.</dl>
<p> <i>F5</i><br />
 <i>Machine, Reset</i></p>
<dl>
<dt>
<dd> Reset the emulated Spectrum. Again, you get a chance to cancel this if you&#8217;re using the GTK+ UI.</dl>
<p> <i>Machine, Hard reset</i></p>
<dl>
<dt>
<dd> Reset the emulated Spectrum. A hard reset is equivalent to turning the Spectrum&#8217;s power off, and then turning it back on. Again, you get a chance to cancel this if you&#8217;re using the GTK+ UI.</dl>
<p> <i>F9</i><br />
 <i>Machine, Select&#8230;</i></p>
<dl>
<dt>
<dd> Choose a type of Spectrum to emulate. An brief overview of the Sinclair, Amstrad and Timex can be found at <i><a rel="nofollow" href="http://www.nvg.ntnu.no/sinclair/computers/zxspectrum/zxspectrum.htm">http://www.nvg.ntnu.no/sinclair/computers/zxspectrum/zxspectrum.htm</a></i> while more technical information can be found at <i><a rel="nofollow" href="http://www.worldofspectrum.org/faq/reference/reference.htm">http://www.worldofspectrum.org/faq/reference/reference.htm</a></i>, and <i><a rel="nofollow" href="http://www.worldofspectrum.org/faq/reference/tmxreference.htm">http://www.worldofspectrum.org/faq/reference/tmxreference.htm</a></i>. </p>
<p> <i>Spectrum 16K</i><br />
 <i>Spectrum 48K</i></p>
<dl>
<dt>
<dd> The original machines as released by Sinclair in 1982 with 16 or 48K of RAM respectively.</dl>
<p> <i>Spectrum 128K</i></p>
<dl>
<dt>
<dd> The 128K machine as released by Sinclair in 1985 (Spain) or 1986 (UK).</dl>
<p> <i>Spectrum +2</i></p>
<dl>
<dt>
<dd> The first machine released by Amstrad, in 1986. From an emulation point of view, the +2 is virtually identical to the 128K.</dl>
<p> <i>Spectrum +2A</i><br />
 <i>Spectrum +3</i></p>
<dl>
<dt>
<dd> The two machines released by Amstrad in 1988. Technically very similar to each other, except that the +3 features a 3&quot; disk drive while the +2A does not.</dl>
<p> <i>Spectrum +3e</i></p>
<dl>
<dt>
<dd> A +3 with modified ROMs allowing access to IDE hard disks via the simple 8-bit interface, as activated from the <i>Options, Peripherals</i> dialog. See <i><a rel="nofollow" href="http://www.zxplus3e.plus.com/">http://www.zxplus3e.plus.com/</a></i> for more details.</dl>
<p> <i>Timex TC2048</i><br />
 <i>Timex TC2068</i></p>
<dl>
<dt>
<dd> The variants of the Spectrum as released by Timex in Portugal.</dl>
<p> <i>Timex TS2068</i></p>
<dl>
<dt>
<dd> The variant of the Spectrum released by Timex in North America.</dl>
<p> <i>Pentagon 128K</i></p>
<dl>
<dt>
<dd> Russian clone of the Spectrum. There were many different machines called Pentagon from 1989 to 2006, this machine corresponds to a 1991 era Pentagon-128K with the optional AY sound chip and the integrated Beta 128 disk interface, and is the version of the machine most often emulated. More technical details can be found at <i><a rel="nofollow" href="http://www.worldofspectrum.org/rusfaq/index.html">http://www.worldofspectrum.org/rusfaq/index.html</a></i>,</dl>
<p> <i>Pentagon 512K</i><br />
 <i>Pentagon 1024K</i></p>
<dl>
<dt>
<dd> Newer versions of the Pentagon Russian Spectrum clones which incorporate more memory and the &quot;Mr Gluk Reset Service&quot; ROM offering a more powerful firmware.</dl>
<p> <i>Scorpion ZS 256</i></p>
<dl>
<dt>
<dd> Another Russian clone of the Spectrum. Some details can be found at <i><a rel="nofollow" href="http://www.worldofspectrum.org/rusfaq/index.html">http://www.worldofspectrum.org/rusfaq/index.html</a></i>, like all the Russian clones they they have built in 3.5&quot; disk drives, accessed via the Beta 128 disk interface and TR-DOS (the Technology Research Disk Operating System). The most important distinction from the Pentagon 128k and similar machines is the display timing details.</dl>
<p> <i>Spectrum SE</i></p>
<dl>
<dt>
<dd> A recent variant designed by Andrew Owen and Jarek Adamski, which is possibly best thought of as a cross between the 128K machine and the Timex variants, allowing 272K of RAM to be accessed. Some more details are available at <i><a rel="nofollow" href="http://www.worldofspectrum.org/faq/reference/sereference.htm">http://www.worldofspectrum.org/faq/reference/sereference.htm</a></i>.</dl>
</dl>
<p> <i>Machine, Debugger&#8230;</i></p>
<dl>
<dt>
<dd> Start the monitor/debugger. See the <code>MONITOR/DEBUGGER</code> section for more information.</dl>
<p> <i>Machine, Poke Finder&#8230;</i></p>
<dl>
<dt>
<dd> Start the `poke finder&#8217;. See the <code>POKE FINDER</code> section for more information.</dl>
<p> <i>Machine, Memory Browser&#8230;</i></p>
<dl>
<dt>
<dd> Start the memory browser. It should be fairly obvious what this does; perhaps the only thing worth noting is that emulation is paused until you close the window.</dl>
<p> <i>Machine, NMI</i></p>
<dl>
<dt>
<dd> Sends a non-maskable interrupt to the emulated Spectrum. Due to a typo in the standard 48K ROM, this will cause a reset, but modified ROMs are available which make use of this feature. When the +D is emulated, this is used to access the +D&#8217;s screenshot and snapshot features (see the <code>+D EMULATION</code> section below).</dl>
<p> <i>F7</i><br />
 <i>Media, Tape, Open&#8230;</i></p>
<dl>
<dt>
<dd> Choose a TAP or TZX virtual-tape file to load from. See the <code>FILE SELECTION</code> section below for details on how to choose the file. If <i>Auto-load media</i> is set in the General Options dialog (as it is by default), you may use the <i>File, Open&#8230;</i> menu option instead, and the tape will begin loading automatically. Otherwise, you have to start the load in the emulated machine (with LOAD &quot;&quot; or the 128&#8217;s Tape Loader option, though you may need to reset first). </p>
<p> To <i>guarantee</i> that TZX files will load properly, you should select the file, make sure tape-loading traps are disabled in the General Options dialog, then press <i>F8</i> (or do <i>Media, Tape, Play</i>). That said, most TZXs will work with tape-loading traps enabled (often quickly loading partway, then loading the rest real-time), so you might want to try it that way first.</dl>
<p> <i>F8</i><br />
 <i>Media, Tape, Play</i></p>
<dl>
<dt>
<dd> Start playing the TAP or TZX file, if required. (Choosing the option (or pressing <i>F8</i>) again pauses playback, and a further press resumes). To explain &#8211; if tape-loading traps have been disabled (in the General Options dialog), starting the loading process in the emulated machine isn&#8217;t enough. You also have to `press play&#8217;, so to speak :-), and this is how you do that. You may also need to `press play&#8217; like this in certain other circumstances, e.g. TZXs containing multi-load games may have a stop-the-tape request (which Fuse obeys).</dl>
<p> <i>Media, Tape, Browse</i></p>
<dl>
<dt>
<dd> Browse through the current tape. A brief display of each of the data blocks on the current tape will appear, from which you can select which block Fuse will play next. With the GTK+ UI, emulation will continue while the browser is displayed; double-clicking on a block will select it. In the other UIs, emulation is paused and you can use the cursor keys and press <i>Enter</i> to select it. If you decide you don&#8217;t want to change block, just press <i>Escape</i>.</dl>
<p> <i>Media, Tape, Rewind</i></p>
<dl>
<dt>
<dd> Rewind the current virtual tape, so it can be read again from the beginning.</dl>
<p> <i>Media, Tape, Clear</i></p>
<dl>
<dt>
<dd> Clear the current virtual tape. This is particularly useful when you want a `clean slate&#8217; to add newly-saved files to, before doing <i>Media, Tape, Write&#8230;</i> (or <i>F6</i>).</dl>
<p> <i>F6</i><br />
 <i>Media, Tape, Write&#8230;</i></p>
<dl>
<dt>
<dd> Write the current virtual-tape contents to a TZX file. You will be prompted for a filename. The virtual-tape contents are the contents of the previously-loaded tape (if any has been loaded since you last did a <i>Media, Tape, Clear</i>), followed by anything you&#8217;ve saved from the emulated machine since. These newly-saved files are <i>not</i> written to any tape file until you choose this option!</dl>
<p> <i>Media, Tape, Record Start</i></p>
<dl>
<dt>
<dd> Starts directly recording the output from the emulated Spectrum to the current virtual-tape. This is useful when you want to record using a non-standard ROM or from a custom save routine. Most tape operations are disabled during recording. Stop recording with the <i>Media, Tape, Write&#8230;</i> menu option.</dl>
<p> <i>Media, Tape, Record Stop</i></p>
<dl>
<dt>
<dd> Stops the direct recording and places the new recording into the virtual-tape.</dl>
<p> <i>Media, Interface I</i></p>
<dl>
<dt>
<dd> Virtual Microdrive images are accessible only when the Interface I is active from the <i>Options, Peripherals</i> menu. Note that any changes to the Microdrive image will not be written to the file on disk until the appropriate `eject and write&#8217; option is used.</dl>
<p> <i>Media, Interface I, Microdrive 1, Insert New</i></p>
<dl>
<dt>
<dd> Insert a new (unformatted) Microdrive cartridge into emulated Microdrive 1.</dl>
<p> <i>Media, Interface I, Microdrive 1, Insert&#8230;</i></p>
<dl>
<dt>
<dd> Insert an existing Microdrive cartridge image into emulated Microdrive 1. You will be prompted for a filename.</dl>
<p> <i>Media, Interface I, Microdrive 1, Eject</i></p>
<dl>
<dt>
<dd> Eject the Microdrive image in Microdrive 1. If the image has been modified, you will be asked as to whether you want any changes saved.</dl>
<p> <i>Media, Interface I, Microdrive 1, Eject and write&#8230;</i></p>
<dl>
<dt>
<dd> Write the Microdrive image in Microdrive 1 to a file, and then eject the image. You will be prompted for a filename.</dl>
<p> <i>Media, Interface I, Microdrive 1, Write protect, Enable</i></p>
<dl>
<dt>
<dd> Enable the write protect tab for the image in Microdrive 1.</dl>
<p> <i>Media, Interface I, Microdrive 1, Write protect, Disable</i></p>
<dl>
<dt>
<dd> Disable the write protect tab for the image in Microdrive 1.</dl>
<p> <i>Media, Interface I, Microdrive 2, &#8230;</i><br />
 <i>Media, Interface I, Microdrive 3, &#8230;</i><br />
 <i>Media, Interface I, Microdrive 4, &#8230;</i><br />
 <i>Media, Interface I, Microdrive 5, &#8230;</i><br />
 <i>Media, Interface I, Microdrive 6, &#8230;</i><br />
 <i>Media, Interface I, Microdrive 7, &#8230;</i><br />
 <i>Media, Interface I, Microdrive 8, &#8230;</i></p>
<dl>
<dt>
<dd> Equivalent options for the other emulated Microdrives.</dl>
<p> <i>Media, Interface I, RS232, Plug RxD</i><br />
 <i>Media, Interface I, RS232, Unplug RxD</i><br />
 <i>Media, Interface I, RS232, Plug TxD</i><br />
 <i>Media, Interface I, RS232, Unplug TxD</i></p>
<dl>
<dt>
<dd> Connect or disconnect a communication channels (FIFO or file) to use as the RS-232 TxD or RxD wire.</dl>
<p> <i>Media, Disk</i></p>
<dl>
<dt>
<dd> Virtual floppy disk images are accessible when emulating a +3, +3e, Pentagon or Scorpion, or when the Beta 128 or +D interface options are enabled and a machine compatible with the chosen interface is selected. (See <code>THE .DSK FORMAT</code>, <code>BETA 128 EMULATION</code> and <code>+D EMULATION</code> sections below for notes on the file formats supported). </p>
<p> Once again, any changes made to a disk image will not affect the file which was `inserted&#8217; into the drive. If you do want to keep any changes, use the appropriate `eject and write&#8217; option before exiting Fuse.</dl>
<p> <i>Media, Disk, +3, Drive A:, Insert&#8230;</i></p>
<dl>
<dt>
<dd> Select a disk-image file to read/write in the +3&#8217;s emulated drive A:.</dl>
<p> <i>Media, Disk, +3, Drive A:, Eject</i></p>
<dl>
<dt>
<dd> Deselect the disk image currently in the +3&#8217;s emulated drive A: &#8211; or from the emulated machine&#8217;s perspective, eject it. Note that any changes made to the image will not be saved.</dl>
<p> <i>Media, Disk, +3, Drive A:, Eject and write&#8230;</i></p>
<dl>
<dt>
<dd> Deselect the disk image currently in the +3&#8217;s drive A: and write the current state of the disk to a file. You will be prompted for a filename.</dl>
<p> <i>Media, Disk, +3, Drive B:, Insert&#8230;</i></p>
<dl>
<dt>
<dd> As above, but for the +3&#8217;s drive B:. Fuse emulates drive B: as a second 3&quot; drive.</dl>
<p> <i>Media, Disk, +3, Drive B:, Eject</i></p>
<dl>
<dt>
<dd> As above, but for drive B:.</dl>
<p> <i>Media, Disk, +3, Drive B:, Eject and write</i></p>
<dl>
<dt>
<dd> As above, but for drive B:.</dl>
<p> <i>Media, Disk, Beta, Drive A:, Insert New</i></p>
<dl>
<dt>
<dd> Insert a new (unformatted) disk into the emulated Beta drive A:.</dl>
<p> <i>Media, Disk, Beta, Drive A:, Insert&#8230;</i><br />
 <i>Media, Disk, Beta, Drive A:, Eject</i><br />
 <i>Media, Disk, Beta, Drive A:, Eject and write&#8230;</i></p>
<dl>
<dt>
<dd> As above, but for the emulated Beta disk drive A:.</dl>
<p> <i>Media, Disk, Beta, Drive A:, Write protect, Enable</i></p>
<dl>
<dt>
<dd> Enable the write protect tab for the image in Beta drive A:.</dl>
<p> <i>Media, Disk, Beta, Drive A:, Write protect, Disable</i></p>
<dl>
<dt>
<dd> Disable the write protect tab for the image in Beta drive A:.</dl>
<p> <i>Media, Disk, Beta, Drive B:, &#8230;</i><br />
 <i>Media, Disk, Beta, Drive C:, &#8230;</i><br />
 <i>Media, Disk, Beta, Drive D:, &#8230;</i></p>
<dl>
<dt>
<dd> As above, but for the remaining emulated Beta disk interface drives.</dl>
<p> <i>Media, Disk, +D, Drive 1, Insert New</i><br />
 <i>Media, Disk, +D, Drive 1, Insert&#8230;</i><br />
 <i>Media, Disk, +D, Drive 1, Eject</i><br />
 <i>Media, Disk, +D, Drive 1, Eject and write&#8230;</i><br />
 <i>Media, Disk, +D, Drive 1, Write protect, Enable</i><br />
 <i>Media, Disk, +D, Drive 1, Write protect, Disable</i><br />
 <i>Media, Disk, +D, Drive 2, &#8230;</i></p>
<dl>
<dt>
<dd> As above, but for the emulated +D drives.</dl>
<p> <i>Media, Cartridge, Timex Dock, Insert&#8230;</i></p>
<dl>
<dt>
<dd> Insert a cartridge into the Timex 2068 dock. This will cause the emulated machine to be changed to the TC2068 (if it wasn&#8217;t already a 2068 variant) and reset.</dl>
<p> <i>Media, Cartridge, Timex Dock, Eject</i></p>
<dl>
<dt>
<dd> Remove the cartridge from the Timex 2068 dock. This will cause the emulated machine to be reset.</dl>
<p> <i>Media, Cartridge, Interface II, Insert&#8230;</i></p>
<dl>
<dt>
<dd> Insert a cartridge into the Interface II cartridge slot. This will cause the emulated machine to be reset and the cartridge loaded.</dl>
<p> <i>Media, Cartridge, Interface II, Eject&#8230;</i></p>
<dl>
<dt>
<dd> Remove the cartridge from the Interface II cartridge slot. This will cause the emulated machine to be reset.</dl>
<p> <i>Media, IDE, Simple 8-bit, Master, Insert&#8230;</i></p>
<dl>
<dt>
<dd> Connect an IDE hard disk to the simple 8-bit interface&#8217;s master channel.</dl>
<p> <i>Media, IDE, Simple 8-bit, Master, Commit</i></p>
<dl>
<dt>
<dd> Cause any writes which have been done to virtual hard disk attached to the simple 8-bit interface&#8217;s master channel to be committed to the real disk, such that they survive the virtual disk being ejected.</dl>
<p> <i>Media, IDE, Simple 8-bit, Master, Eject</i></p>
<dl>
<dt>
<dd> Eject the virtual hard disk from the simple 8-bit interface&#8217;s master channel. Note that any writes to the virtual hard disk will be lost unless the <i>Media, IDE, Simple 8-bit, Master, Commit</i> option is used before the disk is ejected.</dl>
<p> <i>Media, IDE, Simple 8-bit, Slave, Insert&#8230;</i><br />
 <i>Media, IDE, Simple 8-bit, Slave, Commit</i><br />
 <i>Media, IDE, Simple 8-bit, Slave, Eject</i></p>
<dl>
<dt>
<dd> The same as the <i>Media, IDE, Simple 8-bit, Master</i> entries above, but for the simple 8-bit interface&#8217;s slave channel.</dl>
<p> <i>Media, IDE, ZXATASP, Master, Insert&#8230;</i><br />
 <i>Media, IDE, ZXATASP, Master, Commit</i><br />
 <i>Media, IDE, ZXATASP, Master, Eject</i><br />
 <i>Media, IDE, ZXATASP, Slave, Insert&#8230;</i><br />
 <i>Media, IDE, ZXATASP, Slave, Commit</i><br />
 <i>Media, IDE, ZXATASP, Slave, Eject</i></p>
<dl>
<dt>
<dd> The same as the <i>Media, IDE, Simple 8-bit, Master</i> entries above, but for the two channels of the ZXATASP interface.</dl>
<p> <i>Media, IDE, ZXCF CompactFlash, Insert&#8230;</i><br />
 <i>Media, IDE, ZXCF CompactFlash, Commit</i><br />
 <i>Media, IDE, ZXCF CompactFlash, Eject</i></p>
<dl>
<dt>
<dd> The same as the <i>Media, IDE, Simple 8-bit, Master</i> entries above, but for the ZXCF interface&#8217;s CompactFlash slot.</dl>
<p> <i>Media, IDE, DivIDE, Master, Insert&#8230;</i><br />
 <i>Media, IDE, DivIDE, Master, Commit</i><br />
 <i>Media, IDE, DivIDE, Eject</i><br />
 <i>Media, IDE, DivIDE, Slave, Insert&#8230;</i><br />
 <i>Media, IDE, DivIDE, Slave, Commit</i><br />
 <i>Media, IDE, DivIDE, Eject</i></p>
<dl>
<dt>
<dd> The same as the <i>Media, IDE, Simple 8-bit</i> entries above, but for the two channels of the DivIDE interface.</dl>
<p> <i>Help, Keyboard picture&#8230;</i></p>
<dl>
<dt>
<dd> Display a diagram showing the Spectrum keyboard, and the various keywords that can be generated with each key from (48K) BASIC. Under the GTK+ UI, this will appear in a separate window and emulation continues. With the other UIs, the picture remains onscreen (and the emulator paused) until you press <i>Esc</i> or <i>Enter</i>.</dl>
<h2>KEY MAPPINGS</h2>
<p> When emulating the Spectrum, keys <i>F1</i> to <i>F10</i> are used as shortcuts for various menu items, as described above. The alphanumeric keys (along with <i>Enter</i> and <i>Space</i>) are mapped as-is to the Spectrum keys. The other key mappings are:</p>
<dl>
<dt><i>Shift</i></p>
<dd> emulated as Caps Shift</p>
<dt><i>Control</i>, <i>Alt</i>, and <i>Meta</i></p>
<dd> emulated as Symbol Shift (most other modifiers are also mapped to this)</p>
<dt><i>Backspace</i></p>
<dd> emulated as Caps-0 (Delete)</p>
<dt><i>Esc</i></p>
<dd> emulated as Caps-1 (Edit)</p>
<dt><i>Caps Lock</i></p>
<dd> emulated as Caps-2</p>
<dt><i>Cursor keys</i></p>
<dd> emulated as Caps-5/6/7/8 (as appropriate)</p>
<dt><i>Tab</i></p>
<dd> emulated as Caps Shift-Symbol Shift (Extended Mode)</dl>
<p> Some further punctuation keys are supported, if they exist on your keyboard &#8211; `<i>,</i>&#8216;, `<i>.</i>&#8216;, `<i>/</i>&#8216;, `<i>;</i>&#8216;, `<i>aq</i>&#8216;, `<i>#</i>&#8216;, `<i>&#8211;</i>&#8216;, and `<i>=</i>&#8216;. These are mapped to the appropriate symbol-shifted keys on the Spectrum. </p>
<p> A list of keys applicable when using the file selection dialogs is given in the <code>FILE SELECTION</code> section below.</p>
<h2>DISPLAY SIZE</h2>
<p> Some of Fuse&#8217;s UIs allow resizing of the emulated Spectrum&#8217;s display. For the window-based ones (GTK+ and Xlib), you can resize the window by, well, resizing it. :-) Exactly how this works depends on your window manager; you may have to make the window over twice the width and height of the original size before it actually scales up. Fuse attempts to keep the window `square&#8217;, but with some window managers this can mean the window will never resize at all. If you experience this problem, the `<i>&#8211;no-aspect-hint</i>&#8216; option may help. </p>
<p> If you&#8217;re using the SDL UI under X11, the window will automatically resize to be the correct size for the graphics filter selected.</p>
<h2>GRAPHICS FILTERS</h2>
<p> Fuse has the ability to apply essentially arbitrary filters between building its image of the Spectrum&#8217;s screen, and displaying it on the emulating machine&#8217;s monitor. These filters can be used to do various forms of smoothing, emulation of TV scanlines and various other possibilities. Support for graphics filters varies between the different user interfaces, but there are two general classes: the GTK+, Xlib and SDL user interfaces (and the saving of .png screenshots) support `interpolating&#8217; filters which use a palette larger than the Spectrum&#8217;s 16 colours, while the SVGAlib user interface supports only `non-interpolating&#8217; filters. The framebuffer user interface currently does not support filters at all. </p>
<p> A further complication arises due to the fact that the Timex machines have their high-resolution video mode with twice the horizontal resolution. To deal with this, Fuse treats these machines as having a `normal&#8217; display size which is twice the size of a normal Spectrum&#8217;s screen, leading to a different set of filters being available for these machines. Note that any of the double or triple-sizing filters are available for Timex machines only when using the SDL user interface. </p>
<p> The available filters, along with their short name used to select them from the command line, are: </p>
<p> <i>Timex half (smoothed) </i>(<i>half</i>)<br />
 <i>Timex half (skipping) </i>(<i>halfskip</i>)</p>
<dl>
<dt>
<dd> Two Timex-machine specific filters which scale the screen down to half normal (Timex) size; that is, the same size as a normal Spectrum screen. The difference between these two filters is in how they handle the high-resolution mode: the `smoothed&#8217; version is an interpolating filter which averages pairs of adjacent pixels, while the `skipping&#8217; version is a non-interpolating filter which simply drops every other pixel.</dl>
<p> <i>Normal </i>(<i>normal</i>)</p>
<dl>
<dt>
<dd> The simplest filter: just display one pixel for every pixel on the Spectrum&#8217;s screen.</dl>
<p> <i>Double size </i>(<i>2x</i>)</p>
<dl>
<dt>
<dd> Scale the displayed screen up to double size.</dl>
<p> <i>Triple size </i>(<i>3x</i>)</p>
<dl>
<dt>
<dd> Scale the displayed screen up to triple size. Available only with the GTK+, Xlib and SDL user interfaces or when saving screenshots of non-Timex machines.</dl>
<p> <i>2xSaI </i>(<i>2xsai</i>)<br />
 <i>Super 2xSaI </i>(<i>super2xsai</i>)<br />
 <i>SuperEagle </i>(<i>supereagle</i>)</p>
<dl>
<dt>
<dd> Three interpolating filters which apply successively more smoothing. All three double the size of the displayed screen.</dl>
<p> <i>AdvMAME2x </i>(<i>advmame2x</i>)</p>
<dl>
<dt>
<dd> A double-sizing, non-interpolating filter which attempts to smooth diagonal lines.</dl>
<p> <i>AdvMAME3x </i>(<i>advmame3x</i>)</p>
<dl>
<dt>
<dd> Very similar to <i>AdvMAME2x</i>, except that it triples the size of the displayed screen. Available only with the GTK+, Xlib and SDL user interfaces or when saving screenshots of non-Timex machines.</dl>
<p> <i>TV 2x </i>(<i>tv2x</i>)<br />
 <i>TV 3x </i>(<i>tv3x</i>)<br />
 <i>Timex TV </i>(<i>timextv</i>)</p>
<dl>
<dt>
<dd> Three filters which attempt to emulate the effect of television scanlines. The first is a double-sizing filter for non-Timex machines, the second is a similar triple-sizing filter, while the last is a single-sizing filter for Timex machines (note that this means TV 2X and Timex TV produce the same size output).</dl>
<p> <i>PAL TV</i>(<i>paltv</i>)<br />
 <i>PAL TV 2x </i>(<i>paltv2x</i>)<br />
 <i>PAL TV 3x </i>(<i>paltv3x</i>)</p>
<dl>
<dt>
<dd> Three filters which attempt to emulate the effect of the PAL TV system which layers a lower-resolution colour image over the top of a higher-resolution black-and-white image. The filters can also optionally add scanlines like the other TV series scalers.</dl>
<p> <i>Dot matrix </i>(<i>dotmatrix</i>)</p>
<dl>
<dt>
<dd> A double-sizing filter which emulates the effect of a dot-matrix display.</dl>
<p> <i>Timex 1.5x </i>(<i>timex15x</i>)</p>
<dl>
<dt>
<dd> An interpolating Timex-specific filter which scales the Timex screen up to 1.5x its usual size (which is therefore 3x the size of a `normal&#8217; Spectrum screen). Available only for the GTK+ and SDL user interfaces or when saving screenshots.</dl>
<h2>THE EMULATED SPECTRUM</h2>
<p> The emulated Spectrum is, by default, an unmodified 48K Spectrum with a tape player and ZX Printer attached. Oh, and apparently some magical snapshot load/save machine which is probably best glossed over for the sake of the analogy. :-) </p>
<p> To emulate different kinds of Spectrum, select the <i>Machine, Select&#8230;</i> menu option, or press <i>F9</i>. </p>
<p> The Spectrum emulation is paused when any dialogs appear. In the widget UI, it&#8217;s also paused when menus or the keyboard picture are displayed.</p>
<h2>PRINTER EMULATION</h2>
<p> The various models of Spectrum supported a range of ways to connect printers, three of which are supported by Fuse. Different printers are made available for the different models:</p>
<dl>
<dt><i>16</i>, <i>48</i>, <i>TC2048</i>, <i>TC2068</i>, <i>TS2068</i></p>
<dd> ZX Printer</p>
<dt><i>128</i>/<i>+2</i>/<i>Pentagon</i></p>
<dd> Serial printer (text-only)</p>
<dt><i>+2A</i>, <i>+3</i></p>
<dd> Parallel printer (text-only)</dl>
<p> If +D emulation is in use and printer emulation is enabled, text-only emulation of the +D&#8217;s parallel printer interface is provided. </p>
<p> Any printout is appended to one (or both) of two files, depending on the printer &#8211; these default to <i>printout.txt</i> for text output, and <i>printout.pbm</i> for graphics (PBM images are supported by most image viewers and converters). These names can be changed with the <i>&#8211;textfile</i> and <i>&#8211;graphicsfile</i> options from the command line or configuration file. While the ZX Printer can <i>only</i> output graphically, simulated text output is generated at the same time using a crude sort of OCR based on the current character set (a bit like using SCREEN$). There is currently no support for graphics when using the serial/parallel output, though any escape codes used will be `printed&#8217; faithfully. (!) </p>
<p> By the way, it&#8217;s not a good idea to modify the <i>printout.pbm</i> file outside of Fuse if you want to continue appending to it. The header needs to have a certain layout for Fuse to be able to continue appending to it correctly, and the file will be overwritten if it can&#8217;t be appended to.</p>
<h2>ZXATASP AND ZXCF</h2>
<p> The ZXATASP and ZXCF interfaces are two peripherals designed by Sami Vehmaa which significantly extend the capabilities of the Spectrum. More details on both are available from Sami&#8217;s homepage, <i><a rel="nofollow" href="http://user.tninet.se/~vjz762w/">http://user.tninet.se/~vjz762w/</a></i>, but a brief overview is given here. </p>
<p> The real ZXATASP comes with either 128K or 512K of RAM and the ability to connect an IDE hard disks and a CompactFlash card, while the ZXCF comes with 128K, 512K or 1024K of RAM and the ability to connect a CompactFlash card. From an emulation point of view, the two interfaces are actually very similar as a CompactFlash card is logically just an IDE hard disk. Currently, Fuse&#8217;s emulation is fixed at having 512K of RAM in the ZXATASP and 1024K in the ZXCF. </p>
<p> To activate the ZXATASP, simply select the <i>ZXATASP interface</i> option from the <i>Options, Peripherals&#8230;</i> dialog. The state of the upload and write protect jumpers is then controlled by the <i>ZXATASP upload</i> and <i>ZXATASP write protect</i> options. Similarly, the ZXCF is controlled by the <i>ZXCF interface</i> and <i>ZXCF upload</i> options (the ZXCF write protect is software controlled). </p>
<p> If you&#8217;re using either the ZXATASP or ZXCF, you almost certainly want to investigate ResiDOS, the operating system designed for use with the ZXATASP and ZXCF. ResiDOS provides facilities for using the extra RAM, accessing the mass storage devices and a task manager allowing virtually instant switching between programs on the Spectrum. See <i><a rel="nofollow" href="http://www.zxplus3e.plus.com/residos/index.html">http://www.zxplus3e.plus.com/residos/index.html</a></i> for more details.</p>
<h2>DIVIDE</h2>
<p> The DivIDE is another IDE interface for the Spectrum, of which full details can be found at <i><a rel="nofollow" href="http://baze.au.com/divide/">http://baze.au.com/divide/</a></i>. The interface can be activated via the <i>DivIDE interface</i> option from the <i>Options, Peripherals&#8230;</i> dialog, and the state of its write protect jumper controlled via the <i>DivIDE write protect option</i>. If you&#8217;re going to be using the DivIDE, you&#8217;ll probably want one of the firmwares available from the DivIDE homepage.</p>
<h2>FILE SELECTION</h2>
<p> The way you select a file (whether snapshot or tape file) depends on which UI you&#8217;re using. So firstly, here&#8217;s how to use the GTK+ file selector. </p>
<p> The selector shows the directories and files in the current directory in two separate subwindows. If either list is too big to fit in the window, you can use the scrollbar to see the rest (by dragging the slider, for example), or you can use <i>Shift-Tab</i> (to move the keyboard focus to a subwindow) and use the cursor keys. To change directory, double-click it. </p>
<p> To choose a file to load you can either double-click it, or click it then click <i>Ok</i>. Or click <i>Cancel</i> to abort. </p>
<p> If you&#8217;re using the keyboard, probably the easiest way to use the selector is to just ignore it and type in the name. This isn&#8217;t as irksome as it sounds, since the filename input box has filename completion &#8211; type part of a directory or file name, then press <i>Tab</i>. It should complete it. If it was a directory, it moves to that directory; if the completion was ambiguous, it completes as much as possible, and narrows the filenames shown to those which match. You should press <i>Enter</i> when you&#8217;ve finished typing the filename, or <i>Esc</i> to abort. </p>
<p> Now, if you&#8217;re using the widget UI &#8211; the one using the Spectrum font &#8211; the selector works a bit differently. The files and directories are all listed in a single two-column-wide window (the directories are shown at the top, ending in `/&#8217;) &#8211; the names may be truncated onscreen if they&#8217;re too long to fit. </p>
<p> To move the cursor, you can either use the cursor keys, or the Spectrum equivalents <i>5</i>/<i>6</i>/<i>7</i>/<i>8</i>, or (similarly) <i>h</i>/<i>j</i>/<i>k</i>/<i>l</i>. For faster movement, the <i>Page Up</i>, <i>Page Down</i>, <i>Home</i>, and <i>End</i> keys are supported and do what you&#8217;d expect. To select a file or directory, press <i>Enter</i>. To abort, press <i>Esc</i>. </p>
<p> With both selectors, do bear in mind that <i>all</i> files are shown, whether Fuse would be able to load them or not.</p>
<h2>MONITOR/DEBUGGER</h2>
<p> Firstly, note that the vast majority of this section applies only if you&#8217;re using the GTK+ user interface; if you&#8217;re using one of the widget user interfaces, you&#8217;ll get a very basic monitor which shows the current values of the registers and allows you to single step through execution or continue. </p>
<p> If you are using the GTK+ user interface, Fuse features a moderately powerful, completely transparent monitor/debugger, which can be activated via the <i>Machine, Debugger &#8230;</i> menu option. A debugger window will appear, showing the current state of the emulated machine: the top-left `pane&#8217; shows the current state of the Z80 and the last bytes written to any emulated peripherals. The bottom-left pane lists any active breakpoints. Moving right, the next pane shows where the Spectrum&#8217;s 64K memory map (the `<i>W?</i>&#8216; and `<i>C?</i>&#8216; indicate whether each 8K chunk is writable or contended respectively), and the next a disassembly, which by default starts at the current program counter, although this can be modified either by the `disassemble&#8217; command (see below) or by dragging the scrollbar next to it. The next pane shows the current stack, and the final pane any `events&#8217; which are due to occur and could affect emulation. Any of these panes can be removed by use of the <i>View</i> menu. Below the displays are an entry box for debugger commands, and five buttons for controlling the debugger: </p>
<p> <i>Evaluate</i></p>
<dl>
<dt>
<dd> Evaluate the command currently in the entry box.</dl>
<p> <i>Single Step</i></p>
<dl>
<dt>
<dd> Run precisely one Z80 opcode and then stop emulation again.</dl>
<p> <i>Continue</i></p>
<dl>
<dt>
<dd> Restart emulation, but leave the debugger window open. Note that the debugger window will not be updated while emulation is running.</dl>
<p> <i>Break</i></p>
<dl>
<dt>
<dd> Stop emulation and return to the debugger.</dl>
<p> <i>Close</i></p>
<dl>
<dt>
<dd> Close the debugger window and restart emulation.</dl>
<p> Double-clicking on an entry in the stack pane will cause emulation to run until the program counter reaches the value stored at that address, while double-clicking on an entry in the `events&#8217; pane will cause emulation to run until that time is reached. </p>
<p> The main power of the debugger is via the commands entered into the entry box, which are similar in nature (but definitely not identical to or as powerful as) to those in <i><a href="/docs/linux/man/1-gdb/">gdb</a></i>(1). In general, the debugger is case-insensitive, and numbers will be interpreted as decimal, unless prefixed by either `<i>0x</i>&#8216; or `<i>$</i>&#8216; when they will be interpreted as hex. Each command can be abbreviated to the portion not in curly braces. </p>
<p> ba{se} <i>number</i></p>
<dl>
<dt>
<dd> Change the debugger window to displaying output in base <i>number</i>. Available values are 10 (decimal) or 16 (hex).</dl>
<p> br{eakpoint} [<i>address</i>] [<i>condition</i>]</p>
<dl>
<dt>
<dd> Set a breakpoint to stop emulation and return to the debugger whenever an opcode is executed at <i>address</i> and <i>condition</i> evaluates true. If <i>address</i> is omitted, it defaults to the current value of PC.</dl>
<p> br{eakpoint} p{ort} (r{ead}|w{rite}) <i>port </i>[<i>condition</i>]</p>
<dl>
<dt>
<dd> Set a breakpoint to trigger whenever IO port <i>port</i> is read from or written to and <i>condition</i> evaluates true.</dl>
<p> br{eakpoint} (r{ead}|w{rite}) [<i>address</i>] [<i>condition</i>]</p>
<dl>
<dt>
<dd> Set a breakpoint to trigger whenever memory location <i>address</i> is read from (other than via an opcode fetch) or written to and <i>condition</i> evaluates true. <i>Address</i> again defaults to the current value of PC if omitted.</dl>
<p> br{eakpoint} ti{me} <i>time </i>[<i>condition</i>]</p>
<dl>
<dt>
<dd> Set a breakpoint to occur <i>time</i> tstates after the start of the every frame, assuming <i>condition</i> evaluates true (if one is given).</dl>
<p> br{eakpoint} ev{ent} <i>area</i>:<i>detail</i> [<i>condition</i>]</p>
<dl>
<dt>
<dd> Set a breakpoint to occur when the event specified by <i>area</i>:<i>detail</i> occurs and <i>condition</i> evaluates to true. The events which can be caught are: </p>
<p> divide:page<br />
 divide:unpage</p>
<dl>
<dt>
<dd> The DivIDE interface is paged into or out of memory respectively</dl>
<p> if1:page<br />
 if1:unpage</p>
<dl>
<dt>
<dd> The Interface 1 shadow ROM is paged into or out of memory</dl>
<p> rzx:end</p>
<dl>
<dt>
<dd> An RZX recording finishes playing</dl>
<p> tape:play<br />
 tape:stop</p>
<dl>
<dt>
<dd> The emulated tape starts or stops playing</dl>
<p> zxcf:page<br />
 zxcf:unpage</p>
<dl>
<dt>
<dd> The ZXCF interface is paged into or out of memory</dl>
<p> zxatasp:page<br />
 zxatasp:unpage</p>
<dl>
<dt>
<dd> The ZXATASP interface is paged into or out of memory</dl>
<p> In all cases, the event can be specified as <i>area</i>:* to catch all events from that area.</dl>
<p> cl{ear} [<i>address</i>]</p>
<dl>
<dt>
<dd> Remove all breakpoints at <i>address</i> or the current value of PC if <i>address</i> is omitted. Port read/write breakpoints are unaffected.</dl>
<p> com{mmands} <i>id &lt;newline&gt;</i><br />
 <i>&lt;debugger command&gt; &lt;newline&gt;</i><br />
 <i>&lt;debugger command&gt; &lt;newline&gt;</i><br />
 <i>&#8230;</i><br />
 end</p>
<dl>
<dt>
<dd> Set things such that the specified debugger commands will be automatically executed when breakpoint <i>id</i> is triggered. There is currently no user interface for entering multi-line debugger commands, so the only way to specify this command is on the command-line via the &#8211;debugger-command option.</dl>
<p> cond{ition} <i>id </i>[<i>condition</i>]</p>
<dl>
<dt>
<dd> Set breakpoint <i>id</i> to trigger only when <i>condition</i> is true, or unconditionally if <i>condition</i> is omitted.</dl>
<p> co{ntinue}</p>
<dl>
<dt>
<dd> Equivalent to the <i>Continue</i> button.</dl>
<p> del{ete} [<i>id</i>]</p>
<dl>
<dt>
<dd> Remove breakpoint <i>id</i>, or all breakpoints if <i>id</i> is omitted.</dl>
<p> di{sassemble} <i>address</i></p>
<dl>
<dt>
<dd> Set the centre panel disassembly to begin at <i>address</i>.</dl>
<p> ex{it}</p>
<dl>
<dt>
<dd> Exit the emulator immediately.</dl>
<p> fi{nish}</p>
<dl>
<dt>
<dd> Exit from the current CALL or equivalent. This isn&#8217;t infallible: it works by setting a temporary breakpoint at the current contents of the stack pointer, so will not function correctly if the code returns to some other point or plays with its stack in other ways. Also, setting this breakpoint doesn&#8217;t disable other breakpoints, which may trigger before this one. In that case, the temporary breakpoint remains, and the `continue&#8217; command can be used to return to it.</dl>
<p> i{gnore} <i>id count</i></p>
<dl>
<dt>
<dd> Do not trigger the next <i>count</i> times that breakpoint <i>id</i> would have triggered.</dl>
<p> n{ext}</p>
<dl>
<dt>
<dd> Step to the opcode following the current one. As with the `finish&#8217; command, this works by setting a temporary breakpoint at the next opcode, so is not infallible.</dl>
<p> o{ut} <i>port value</i></p>
<dl>
<dt>
<dd> Write <i>value</i> to IO port <i>port</i>.</dl>
<p> pr{int} <i>expression</i></p>
<dl>
<dt>
<dd> Print the value of <i>expression</i> to standard output.</dl>
<p> se{t} <i>address value</i></p>
<dl>
<dt>
<dd> Poke <i>value</i> into memory at <i>address</i>.</dl>
<p> se{t} <i>register value</i></p>
<dl>
<dt>
<dd> Set the value of the Z80 register <i>register</i> to <i>value</i>.</dl>
<p> se{t} $<i>variable</i> <i>value</i></p>
<dl>
<dt>
<dd> Set the value of the debugger variable <i>variable</i> to <i>value</i>.</dl>
<p> s{tep}</p>
<dl>
<dt>
<dd> Equivalent to the <i>Single Step</i> button.</dl>
<p> t{breakpoint} [<i>options</i>]</p>
<dl>
<dt>
<dd> This is the same as the `breakpoint&#8217; command in its various forms, except that that breakpoint is temporary: it will trigger once and once only, and then be removed.</dl>
<p> Addresses can be specified in one of two forms: either an absolute addresses, specified by an integer in the range 0x0000 to 0xFFFF or as a `<i>page</i>:<i>offset</i>&#8216; combination, which refers to a location <i>offset</i> bytes into into memory bank <i>page</i>, independent of where that bank is currently paged into memory. RAM pages are indicated simply by an integer, while ROMs are prefixed by `<i>R</i>&#8216; (e.g. offset 0x1234 in ROM 1 is specified as `<i>R1:0x1234</i>&#8216;). Pages selected via the /ROMCS line are prefixed with `<i>C</i>&#8216;, while the Timex Dock and Exrom use prefixes `<i>D</i>&#8216; and `<i>X</i>&#8216; respectively. The 48K machines are treated as having a permanent mapping of page 5 at 0x4000, page 2 at 0x8000 and page 0 at 0xC000; the 16K Spectrum is treated as having page 5 at 0x4000 and no page at 0x8000 and 0xC000. </p>
<p> Anywhere the debugger is expecting a numeric value, except where it expects a breakpoint id, you can instead use a numeric expression, which uses a restricted version of C&#8217;s syntax; exactly the same syntax is used for conditional breakpoints, with `0&#8242; being false and any other value being true. In numeric expressions, you can use integer constants (all calculations are done in integers), register names (which simply evaluate to the value of the register), debugger variables, parentheses, the standard four numeric operations (`+&#8217;, `-&#8216;, `*&#8217; and `/&#8217;), the (non-)equality operators `==&#8217; and `!=&#8217;, the comparison operators `&gt;&#8217;, `&lt;&#8216;, `&gt;=&#8217; and `&lt;=&#8217;, bitwise and (`&amp;&#8217;), or (`|&#8217;) and exclusive or (`^&#8217;) and logical and (`&amp;&amp;&#8217;) and or (`||&#8217;).</p>
<h2>THE POKE FINDER</h2>
<p> The `poke finder&#8217; is a tool which is designed to make the task of finding (infinite lives etc.) pokes for games a bit easier: it is similar to the `Lifeguard&#8217; utility which was available for use with the Multiface. It works by maintaining a list of locations in which the current number of lives (etc.) may be stored, and having the ability to remove from that list any locations which don&#8217;t contain a specified value. </p>
<p> The poke finder dialog contains an entry box for specifying the value to be searched for, a count of the current number of possible locations and, if there are less than 20 possible locations, a list of the possible locations (in `page:offset&#8217; format). The five buttons act as follows: </p>
<p> <i>Incremented</i></p>
<dl>
<dt>
<dd> Remove from the list of possible locations all addresses which have not been incremented since the last search.</dl>
<p> <i>Decremented</i></p>
<dl>
<dt>
<dd> Remove from the list of possible locations all addresses which have not been decremented since the last search.</dl>
<p> <i>Search</i></p>
<dl>
<dt>
<dd> Remove from the list of possible locations all addresses which do not contain the value specified in the `Search for&#8217; field.</dl>
<p> <i>Reset</i></p>
<dl>
<dt>
<dd> Reset the poke finder so that all locations are considered possible.</dl>
<p> <i>Close</i></p>
<dl>
<dt>
<dd> Close the dialog. Note that this does not reset the current state of the poke finder.</dl>
<p> Double-clicking on an entry in the list of possible locations will cause a breakpoint to be set to trigger whenever that location is written to. </p>
<p> An example of how to use this may make things a bit clearer. We&#8217;ll use the 128K version of Gryzor. Load the game, define keys to suit and start playing. Immediately pause the game and bring up the poke finder dialog. We note that we currently have 6 lives, so enter `6&#8242; into the `Search for&#8217; field and click `Search&#8217;. This reduces the number of possible locations to around 931 (you may get a slightly different number depending on exactly when you paused the game). Play along a bit and then (deliberately) lose a life. Pause the game again. As we now have 5 lives, replace the `6&#8242; in the &#8216;Search for&#8217; field with a `5&#8242; and click `Search&#8217; again. This then reduces the list of possible locations to just one: page 2, offset 0x00BC. This is the only location in memory which stored `6&#8242; when we had 6 lives and `5&#8242; when we had 5 lives, so its pretty likely that this is where the lives count is stored. Double-clicking on the `2:0x00BC&#8217; entry in the dialog will set the appropriate breakpoint (you may wish to open the debugger at this point to confirm this). Play along a bit more. When you next lose a life, emulation is stopped with PC at 0x91CD. Scrolling up a few addresses in the debugger&#8217;s disassembly pane shows a value was loaded from 0x80BC (our hypothetical lives counter), decremented and then stored again to 0x80BC, which looks very much like the code to reduce the number of lives. We can now use the debugger to replace the decrement with a NOP (`set 0x91c9 0&#8242;), and playing the game some more after this reveals that this has worked and we now have infinite lives.</p>
<h2>THE .DSK FORMAT</h2>
<p> In general, disk images for the +3 Spectrum are thought of as being in DSK format. However, this is actually an slight oversimplification; there in in fact <i>two</i> similar, but not identical, DSK formats. (The difference can be seen by doing `head -1 <i>dskfile</i>&#8216;: one format will start `MV &#8211; CPCEMU&#8217; and the other will start `EXTENDED&#8217;). </p>
<p> Fuse supports both the `CPCEMU&#8217; and `EXTENDED&#8217; formats.</p>
<h2>BETA 128 EMULATION</h2>
<p> Fuse supports .SCL and .TRD images in its Pentagon and Scorpion emulation, and also under 128K and +2 (but not +2A) emulation if the <i>Beta 128 interface</i> option from the <i>Options, Peripherals&#8230;</i> dialog is enabled.</p>
<h2>+D EMULATION</h2>
<p> Fuse supports .MGT and .IMG images in its +D emulation. The +D&#8217;s printer port is emulated. (See the <code>PRINTER EMULATION </code> section for more details.) The +D may only be used with 48K, 128K and +2 (not +2A) emulation. To access disks, load G+DOS, by inserting a disk containing the DOS file (+SYS) and entering &quot;RUN&quot;. Once DOS is loaded, you can load to/from +D disks by prefixing filenames with `d<i>n</i>&#8216; where `<i>n</i>&#8216; is the number of the drive in use. For example, `<i>LOAD d1dqmyfiledq</i>&#8216; would load the file named `myfile&#8217; from the emulated drive 1. Microdrive syntax may also be used. </p>
<p> To save a snapshot, choose the `Machine, NMI&#8217; menu option, and then press `4&#8242; to save a 48K snapshot, or `5&#8242; to save a 128K snapshot. When saving a 128K snapshot, you must then press Y or N to indicate whether the screen changed while saving the snapshot, to finish saving. You can also choose `3&#8242; to save a screenshot to disk. Options `1&#8242; and `2&#8242; allow screenshots to be printed (in monochrome) if printer emulation is enabled.</p>
<h2>DISK FILE FORMATS</h2>
<p> Fuse supports several disk image formats in its +D and Beta 128 emulation. </p>
<p> For reading: </p>
<p> <i>.UDI</i></p>
<dl>
<dt>
<dd> Ultra Disk Image; for specification please see <i><a rel="nofollow" href="http://zxmak.narod.ru/docs.htm">http://zxmak.narod.ru/docs.htm</a></i><br />
 This is the only image format which can store all the relevant information of the recorded data on a magnetic disk, so it can be used for any <i>non standard</i> disk format. Fuse can store and read not just MFM but FM formatted disk data in/from this container.</dl>
<p> <i>.FDI</i></p>
<dl>
<dt>
<dd> UKV Spectrum Debugger disk image format.</dl>
<p> <i>.MGT</i> <i>.IMG</i></p>
<dl>
<dt>
<dd> DISCiPLE/+D file formats.</dl>
<p> <i>.SAD</i> <i>.SDF</i></p>
<dl>
<dt>
<dd> For compatibility with SAM Coup&#8217;e disk images using these formats. Note that SAM Coup&#8217;e `.DSK&#8217; images share the same format as `.MGT&#8217;.</dl>
<p> <i>.TRD</i></p>
<dl>
<dt>
<dd> TR-DOS disk image; for detailed information please see <i><a rel="nofollow" href="http://www.retroplay.com/Mecenate/ramsoft/tr-info.zip">http://www.retroplay.com/Mecenate/ramsoft/tr-info.zip</a></i></dl>
<p> <i>.SCL</i></p>
<dl>
<dt>
<dd> A simple archive format for TR-DOS disk files.</dl>
<p> <i>.TD0</i></p>
<dl>
<dt>
<dd> Teledisk image format; Fuse supports only files not created with &quot;Advanced Compression&quot;. Detailed description found in <i><a rel="nofollow" href="http://www.classiccmp.org/dunfield/img/td0notes.txt">http://www.classiccmp.org/dunfield/img/td0notes.txt</a></i> and <i><a rel="nofollow" href="http://www.fpns.net/willy/wteledsk.htm">http://www.fpns.net/willy/wteledsk.htm</a></i></dl>
<p> <i>.DSK</i></p>
<dl>
<dt>
<dd> CPC disk image format; Fuse supports the plain old and the new extended CPC format too. Further information please see the <code>THE .DSK FORMAT</code> section and the CPCEMU manual section 7.7.1 <i><a rel="nofollow" href="http://www.cpc-emu.org/linux/cpcemu_e.txt">http://www.cpc-emu.org/linux/cpcemu_e.txt</a></i></dl>
<p> Fuse supports most of them for writing: <i>.UDI .FDI .MGT .IMG .SAD .TRD .SCL .DSK</i> (only the old CPC format).<br />
 You can save disk images with any output format, just select the appropriate extension. (e.g. <i>` elite3.udi &#8216;</i> to save as an UDI file) There is a <i>.LOG</i> ` image &#8216; format for debugging purpose. This is a plain text file contains three dump of the loaded disk image at different details. Not all image format can store all disk image. You cannot save a disk image with an inappropriate format that loses some information (e.g. variable track length or sector length).</p>
<h2>COMPRESSED FILES</h2>
<p> Assuming the appropriate libraries were available when <i><a href="/docs/linux/man/3-libspectrum/">libspectrum</a></i>(3) was compiled, snapshots, tape images, dock cartridges and input recording files can be read from files compressed with <i><a href="/docs/linux/man/3-bzip2/">bzip2</a></i>(3) or <i><a href="/docs/linux/man/3-gzip/">gzip</a></i>(3) just as if they were uncompressed. There is currently no support for reading compressed +3, +D or Beta disk images.</p>
<h2>BUGS</h2>
<p> Selecting a startup filter doesn&#8217;t work properly with user interfaces other than SDL. </p>
<p> Attempting to replay an RZX file without an embedded snapshot from the command-line doesn&#8217;t work if you do `./fuse <i>rzxfile snapshot</i>&#8216;. `./fuse <i>snapshot rzxfile</i>&#8216; does work though, so use that instead. </p>
<p> Changing virtual consoles when using SVGAlib for joystick support causes Fuse to exit. If this is a problem, compile Fuse with the `<i>&#8211;disable-ui-joystick</i>&#8216; option. </p>
<p> The poke finder can&#8217;t search outside `normal&#8217; RAM. </p>
<p> Using the <i>Options, Joysticks, Joystick 1&#8230;</i> or <i>Options, Joysticks, Joystick 2&#8230;</i> options under GTK+ 2.x produces a large number of GTK+ critical warnings. This is a GTK+ bug (#144427), which is fixed in GTK+ 2.4.4. </p>
<p> The libao file output devices not work properly with the GTK+ UI. No error reporting, but the created file does not contain any sound data. If you use a `weak&#8217; machine alsa09 makes a lot of clicks and pops and will output `<i>ALSA: underrun, at least 0ms.</i>&#8216; error messages.</p>
<h2>FILES</h2>
<p> <i>~/.fuserc</i></p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/3-bzip2/">bzip2</a></i>(3), <i><a href="/docs/linux/man/1-fuse-utils/">fuse-utils</a></i>(1), <i><a href="/docs/linux/man/3-gzip/">gzip</a></i>(3), <i><a href="/docs/linux/man/3-libspectrum/">libspectrum</a></i>(3), <i><a href="/docs/linux/man/1-ogg123/">ogg123</a></i>(1), <i><a href="/docs/linux/man/1-xspect/">xspect</a></i>(1), <i><a href="/docs/linux/man/1-xzx/">xzx</a></i>(1) </p>
<p> The comp.sys.sinclair Spectrum FAQ, at<br />
 <i><a rel="nofollow" href="http://www.worldofspectrum.org/faq/index.html">http://www.worldofspectrum.org/faq/index.html</a></i>.</p>
<h2>AUTHOR</h2>
<p> Philip Kendall (philip-fuse [at] shadowmagic.org.uk). </p>
<p> Matan Ziv-Av wrote the SVGAlib and framebuffer UIs, the glib replacement code, and did some work on the OSS-specific sound code and the original widget UI code. </p>
<p> Russell Marks wrote the sound emulation and OSS-specific sound code, the joystick emulation, some of the printer code, and the original version of this man page. </p>
<p> John Elliott&#8217;s lib765 and libdsk libraries were used for the original +3 disk and disk image support. </p>
<p> Ian Collier wrote the ZX Printer emulation (for xz80). </p>
<p> Darren Salt wrote the original versions of the code for +3 emulation, SLT support, MITSHM support (for the Xlib UI), TZX raw data blocks, RZX embedded snapshots and compression, the Kempston mouse emulation and made many improvements to the widget code. </p>
<p> Alexander Yurchenko wrote the OpenBSD/Solaris-specific sound code. </p>
<p> Fredrick Meunier wrote the TC2048, TS2068, Pentagon and Spectrum SE support, the CoreAudio sound code, as well as maintaining the OS X port and importing the graphics filter code. </p>
<p> Ludvig Strigeus and The ScummVM project wrote the original graphics filter code. </p>
<p> Dmitry Sanarin wrote the original Beta disk interface emulation (for Glukalka). </p>
<p> Witold Filipczyk wrote the TC2068 support. </p>
<p> Matthew Westcott wrote the AY logging code and the DivIDE emulation. </p>
<p> Marek Januszewski wrote various bits of code to make Fuse work under Win32, including the DirectDraw user interface. </p>
<p> Stuart Brady wrote the +D emulation, Scorpion emulation and the HP-UX sound code. </p>
<p> Garry Lancaster wrote the 8-bit IDE, ZXATASP and ZXCF interface emulations. </p>
<p> Gergely Szasz wrote the Interface I and Microdrive emulation, the PAL TV scalers, the TV 3x scaler, the movie logging code, the libao sound code, the upd765 disk controller used in the +3 and made many improvements to the widget code. </p>
<h2>Index</h2>
