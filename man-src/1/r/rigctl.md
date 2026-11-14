---
title: "rigctl(1)"
name: "rigctl"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rigctl/"
description: "rigctl – control radio transceivers and receivers"
---

<h2 class="name">NAME</h2>
<p> rigctl &#8211; control radio transceivers and receivers </p>
<h2>SYNOPSIS</h2>
<p> <code>rigctl</code> [<i>OPTION</i>]&#8230; [<i>COMMAND</i>]&#8230;</p>
<h2>DESCRIPTION</h2>
<p> Control radio transceivers and receivers. <code>rigctl</code> accepts <code>commands</code> from the command line as well as in interactive mode if none are provided on the command line. </p>
<p> Keep in mind that <code>Hamlib</code> is BETA level software. While a lot of backend libraries lack complete rig support, the basic functions are usually well supported. The API may change without publicized notice, while an advancement of the minor version (e.g. 1.1.x to 1.2.x) indicates such a change. </p>
<p> Please report bugs and provide feedback at the e-mail address given in the REPORTING BUGS section. Patches and code enhancements are also welcome.</p>
<h2>OPTIONS</h2>
<p> This program follows the usual GNU command line syntax, with long options starting with two dashes (`-&#8216;). </p>
<p> Here is a summary of the supported options:</p>
<dl>
<dt><code>-m, &#8211;model=id</code></p>
<dd> Select radio model number. See model list (use &#8216;rigctl -l&#8217;). </p>
<p> NB: <code>rigctl</code> (or third party software) will use rig model 1901 when using <code>rpc.rigd</code> or rig model 2 for NET rigctl (rigctld).</p>
<dt><code>-r, &#8211;rig-file=device</code></p>
<dd> Use <i>device</i> as the file name of the port the radio is connected. Often a serial port, but could be a USB to serial adapter. Typically /dev/ttyS0, /dev/ttyS1, /dev/ttyUSB0, etc. on Linux or COM1, COM2, etc. on Win32. </p>
<p> Also used to specify the host and port to connect to a listening rotctld daemon on POSIX: </p>
<p> -r localhost:4532 </p>
<p> and on Win32: </p>
<p> -r 127.0.0.1:4532</p>
<dt><code>-p, &#8211;ptt-file=device</code></p>
<dd> Use <i>device</i> as the file name of the Push-To-Talk device using a device file as described above.</p>
<dt><code>-d, &#8211;dcd-file=device</code></p>
<dd> Use <i>device</i> as the file name of the Data Carrier Detect device using a device file as described above.</p>
<dt><code>-P, &#8211;ptt-type=type</code></p>
<dd> Use <i>type</i> of Push-To-Talk device. Supported types are RIG, DTR, RTS, PARALLEL, NONE, overriding PTT type defined in the rig&#8217;s backend. </p>
<p> Some side effects of this command are that when type is set to DTR, read PTT state comes from Hamlib frontend, not read from the radio. When set to NONE, PTT state cannot be read or set even if rig backend supports reading/setting PTT status from the rig.</p>
<dt><code>-D, &#8211;dcd-type=type</code></p>
<dd> Use <i>type</i> of Data Carrier Detect device. Supported types are RIG, DSR, CTS, CD, PARALLEL, NONE.</p>
<dt><code>-s, &#8211;serial-speed=baud</code></p>
<dd> Set serial speed to <i>baud</i> rate. Uses maximum serial speed from rig backend capabilities as the default.</p>
<dt><code>-c, &#8211;civaddr=id</code></p>
<dd> Use <i>id</i> as the CI-V address to communicate with the rig. Only useful for Icom rigs. </p>
<p> NB: the <i>id</i> is in decimal notation, unless prefixed by <i>0x</i>, in which case it is hexadecimal.</p>
<dt><code>-t, &#8211;send-cmd-term=char</code></p>
<dd> Change the termination <i>char</i> for text protocol when using the <i>send_cmd</i> command. The default value is &lt;CR&gt; (0x0d). Non ASCII printable characters can be specified as an ASCII number, in hexadecimal format, prepended with 0x. You may pass an empty string for no termination char. The string &#8216;-1&#8217; tells rigctl to switch to binary protocol. See the <i>send_cmd</i> command for further explanation. </p>
<p> For example, to specify a command terminator for Kenwood style text commands pass &quot;-t &#8216;;&#8217;&quot; to rigctl. See EXAMPLES below.</p>
<dt><code>-L, &#8211;show-conf</code></p>
<dd> List all config parameters for the radio defined with -m above.</p>
<dt><code>-C, &#8211;set-conf=parm=val[,parm=val]*</code></p>
<dd> Set config parameter. e.g. stop_bits=2 </p>
<p> Use -L option for a list.</p>
<dt><code>-l, &#8211;list</code></p>
<dd> List all model numbers defined in <code>Hamlib</code> and exit. As of 1.2.15.1 the list is sorted by model number. </p>
<p> <code>N.B.</code> In Linux the list can be scrolled back using Shift-PageUp/ Shift-PageDown, or using the scrollbars of a virtual terminal in X or the cmd window in Windows. The output can be piped to &#8216;more&#8217; or &#8216;less&#8217;, e.g. &#8216;rigctl -l | more&#8217;.</p>
<dt><code>-u, &#8211;dump-caps</code></p>
<dd> Dump capabilities for the radio defined with -m above and exit.</p>
<dt><code>-o, &#8211;vfo</code></p>
<dd> Set vfo mode, requiring an extra VFO argument in front of each appropriate command. Otherwise, VFO_CURR is assumed when this option is not set.</p>
<dt><code>-v, &#8211;verbose</code></p>
<dd> Set verbose mode, cumulative (see DIAGNOSTICS below).</p>
<dt><code>-h, &#8211;help</code></p>
<dd> Show summary of these options and exit.</p>
<dt><code>-V, &#8211;version</code></p>
<dd> Show version of <code>rigctl</code> and exit.</dl>
<p> <code>N.B.</code> Some options may not be implemented by a given backend and will return an error. This is most likely to occur with the <i>&#8211;set-conf</i> and <i>&#8211;show-conf</i> options. </p>
<p> Please note that the backend for the radio to be controlled, or the radio itself may not support some commands. In that case, the operation will fail with a <code>Hamlib</code> error code.</p>
<h2>COMMANDS</h2>
<p> Commands can be entered either as a single char, or as a long command name. Basically, the commands do not take a dash in front of them on the command line, as the options do. They may be typed in when in interactive mode or provided as argument(s) in command line interface mode. </p>
<p> Since most of the <code>Hamlib</code> operations have a <i>set</i> and a <i>get</i> method, an upper case letter will be used for <i>set</i> method whereas the corresponding lower case letter refers to the <i>get</i> method. Each operation also has a long name; in interactive mode, prepend a backslash to enter a long command name. </p>
<p> Example: Use &quot;\dump_caps&quot; to see what this radio can do. </p>
<p> Please note that the backend for the radio to be controlled, or the radio itself may not support some commands. In that case, the operation will fail with a <code>Hamlib</code> error message. </p>
<p> Here is a summary of the supported commands (In the case of &quot;set&quot; commands the quoted string is replaced by the value in the description. In the case of &quot;get&quot; commands the quoted string is the key name of the value returned.):</p>
<dl>
<dt><code>Q|q, exit rigctl</code></p>
<dd> Exit rigctl in interactive mode. </p>
<p> When rigctl is controlling the rig directly, will close the rig backend and port. When rigctl is connected to rigctld (rig model 2), the TCP/IP connection to rigctld is closed and rigctld remains running, available for another TCP/IP network connection.</p>
<dt><code>F, set_freq &#8216;Frequency&#8217;</code></p>
<dd> Set &#8216;Frequency&#8217;, in Hz.</p>
<dt><code>f, get_freq</code></p>
<dd> Get &#8216;Frequency&#8217;, in Hz.</p>
<dt><code>M, set_mode &#8216;Mode&#8217; &#8216;Passband&#8217;</code></p>
<dd> Set &#8216;Mode&#8217;: USB, LSB, CW, CWR, RTTY, RTTYR, AM, FM, WFM, AMS, PKTLSB, PKTUSB, PKTFM, ECSSUSB, ECSSLSB, FAX, SAM, SAL, SAH, DSB. </p>
<p> Set &#8216;Passband&#8217; in Hz, or &#8216;0&#8217; for the Hamlib backend default.</p>
<dt><code>m, get_mode</code></p>
<dd> Get &#8216;Mode&#8217; &#8216;Passband&#8217;. </p>
<p> Returns Mode as a string from <i>set_mode</i> above and Passband in Hz.</p>
<dt><code>V, set_vfo &#8216;VFO&#8217;</code></p>
<dd> Set &#8216;VFO&#8217;: VFOA, VFOB, VFOC, currVFO, VFO, MEM, Main, Sub, TX, RX. </p>
<p> In VFO mode only a single VFO parameter is required.</p>
<dt><code>v, get_vfo</code></p>
<dd> Get current &#8216;VFO&#8217;. </p>
<p> Returns VFO as a string from <i>set_vfo</i> above.</p>
<dt><code>J, set_rit &#8216;RIT&#8217;</code></p>
<dd> Set &#8216;RIT&#8217;, in Hz, can be + or -. </p>
<p> A value of &#8216;0&#8217; resets RIT and *should* turn RIT off. If not, file a bug report against the Hamlib backend.</p>
<dt><code>j, get_rit</code></p>
<dd> Get &#8216;RIT&#8217;, in Hz.</p>
<dt><code>Z, set_xit &#8216;XIT&#8217;</code></p>
<dd> Set &#8216;XIT&#8217;, in Hz can be + or -. </p>
<p> A value of &#8216;0&#8217; resets RIT and *should* turn RIT off. If not, file a bug report against the Hamlib backend.</p>
<dt><code>z, get_xit</code></p>
<dd> Get &#8216;XIT&#8217;, in Hz.</p>
<dt><code>T, set_ptt &#8216;PTT&#8217;</code></p>
<dd> Set &#8216;PTT&#8217;, 0 (RX), 1 (TX), 2 (TX mic), 3 (TX data).</p>
<dt><code>t, get_ptt</code></p>
<dd> Get &#8216;PTT&#8217; status.</p>
<dt><code>0x8b, get_dcd</code></p>
<dd> Get &#8216;DCD&#8217; (squelch) status, 0 (Closed) or 1 (Open)</p>
<dt><code>R, set_rptr_shift &#8216;Rptr Shift&#8217;</code></p>
<dd> Set &#8216;Rptr Shift&#8217;: &quot;+&quot;, &quot;-&quot; or something else for none.</p>
<dt><code>r, get_rptr_shift</code></p>
<dd> Get &#8216;Rptr Shift&#8217;. Returns &quot;+&quot;, &quot;-&quot; or &quot;None&quot;.</p>
<dt><code>O, set_rptr_offs &#8216;Rptr Offset&#8217;</code></p>
<dd> Set &#8216;Rptr Offset&#8217;, in Hz.</p>
<dt><code>o, get_rptr_offs</code></p>
<dd> Get &#8216;Rptr Offset&#8217;, in Hz.</p>
<dt><code>C, set_ctcss_tone &#8216;CTCSS Tone&#8217;</code></p>
<dd> Set &#8216;CTCSS Tone&#8217;, in tenths of Hz.</p>
<dt><code>c, get_ctcss_tone</code></p>
<dd> Get &#8216;CTCSS Tone&#8217;, in tenths of Hz.</p>
<dt><code>D, set_dcs_code &#8216;DCS Code&#8217;</code></p>
<dd> Set &#8216;DCS Code&#8217;.</p>
<dt><code>d, get_dcs_code</code></p>
<dd> Get &#8216;DCS Code&#8217;.</p>
<dt><code>0x90, set_ctcss_sql &#8216;CTCSS Sql&#8217;</code></p>
<dd> Set &#8216;CTCSS Sql&#8217; tone, in tenths of Hz.</p>
<dt><code>0x91, get_ctcss_sql</code></p>
<dd> Get &#8216;CTCSS Sql&#8217; tone, in tenths of Hz.</p>
<dt><code>0x92, set_dcs_sql &#8216;DCS Sql&#8217;</code></p>
<dd> Set &#8216;DCS Sql&#8217; code.</p>
<dt><code>0x93, get_dcs_sql</code></p>
<dd> Get &#8216;DCS Sql&#8217; code.</p>
<dt><code>I, set_split_freq &#8216;Tx Frequency&#8217;</code></p>
<dd> Set &#8216;TX Frequency&#8217;, in Hz.</p>
<dt><code>i, get_split_freq</code></p>
<dd> Get &#8216;TX Frequency&#8217;, in Hz.</p>
<dt><code>X, set_split_mode &#8216;TX Mode&#8217; &#8216;TX Passband&#8217;</code></p>
<dd> Set &#8216;TX Mode&#8217;: AM, FM, CW, CWR, USB, LSB, RTTY, RTTYR, WFM, AMS, PKTLSB, PKTUSB, PKTFM, ECSSUSB, ECSSLSB, FAX, SAM, SAL, SAH, DSB. </p>
<p> The &#8216;TX Passband&#8217; is the exact passband in Hz, or &#8216;0&#8217; for the Hamlib backend default.</p>
<dt><code>x, get_split_mode</code></p>
<dd> Get &#8216;TX Mode&#8217; and &#8216;TX Passband&#8217;. </p>
<p> Returns TX mode as a string from <i>set_split_mode</i> above and TX passband in Hz.</p>
<dt><code>S, set_split_vfo &#8216;Split&#8217; &#8216;TX VFO&#8217;</code></p>
<dd> Set &#8216;Split&#8217; mode, &#8216;0&#8217; or &#8216;1&#8217;, and &#8216;TX VFO&#8217; from <i>set_vfo</i> above.</p>
<dt><code>s, get_split_vfo</code></p>
<dd> Get &#8216;Split&#8217; mode, &#8216;0&#8217; or &#8216;1&#8217;, and &#8216;TX VFO&#8217;.</p>
<dt><code>N, set_ts &#8216;Tuning Step&#8217;</code></p>
<dd> Set &#8216;Tuning Step&#8217;, in Hz.</p>
<dt><code>n, get_ts</code></p>
<dd> Get &#8216;Tuning Step&#8217;, in Hz.</p>
<dt><code>U, set_func &#8216;Func&#8217; &#8216;Func Status&#8217;</code></p>
<dd> Set &#8216;Func&#8217; &#8216;Func Status&#8217;. </p>
<p> Func is one of: FAGC, NB, COMP, VOX, TONE, TSQL, SBKIN, FBKIN, ANF, NR, AIP, APF, MON, MN, RF, ARO, LOCK, MUTE, VSC, REV, SQL, ABM, BC, MBC, AFC, SATMODE, SCOPE, RESUME, TBURST, TUNER. </p>
<p> Func Status argument is a non null value for &quot;activate&quot;, &quot;de-activate&quot; otherwise, much as TRUE/FALSE definitions in C language.</p>
<dt><code>u, get_func</code></p>
<dd> Get &#8216;Func&#8217; &#8216;Func Status&#8217;. </p>
<p> Returns Func as a string from <i>set_func</i> above and Func status as a non null value.</p>
<dt><code>L, set_level &#8216;Level&#8217; &#8216;Level Value&#8217;</code></p>
<dd> Set &#8216;Level&#8217; and &#8216;Level Value&#8217;. </p>
<p> Level is one of: PREAMP, ATT, VOX, AF, RF, SQL, IF, APF, NR, PBT_IN, PBT_OUT, CWPITCH, RFPOWER, MICGAIN, KEYSPD, NOTCHF, COMP, AGC (0:OFF, 1:SUPERFAST, 2:FAST, 3:SLOW, 4:USER, 5:MEDIUM, 6:AUTO), BKINDL, BAL, METER, VOXGAIN, ANTIVOX, SLOPE_LOW, SLOPE_HIGH, RAWSTR, SWR, ALC, STRENGTH. </p>
<p> The Level Value can be a float or an integer.</p>
<dt><code>l, get_level</code></p>
<dd> Get &#8216;Level&#8217; &#8216;Level Value&#8217;. </p>
<p> Returns Level as a string from <i>set_level</i> above and Level value as a float or integer.</p>
<dt><code>P, set_parm &#8216;Parm&#8217; &#8216;Parm Value&#8217;</code></p>
<dd> Set &#8216;Parm&#8217; &#8216;Parm Value&#8217; </p>
<p> Parm is one of: ANN, APO, BACKLIGHT, BEEP, TIME, BAT, KEYLIGHT.</p>
<dt><code>p, get_parm</code></p>
<dd> Get &#8216;Parm&#8217; &#8216;Parm Value&#8217;. </p>
<p> Returns Parm as a string from <i>set_parm</i> above and Parm Value as a float or integer.</p>
<dt><code>B, set_bank &#8216;Bank&#8217;</code></p>
<dd> Set &#8216;Bank&#8217;. Sets the current memory bank number.</p>
<dt><code>E, set_mem &#8216;Memory#&#8217;</code></p>
<dd> Set &#8216;Memory#&#8217; channel number.</p>
<dt><code>e, get_mem</code></p>
<dd> Get &#8216;Memory#&#8217; channel number.</p>
<dt><code>G, vfo_op &#8216;Mem/VFO Op&#8217;</code></p>
<dd> Perform &#8216;Mem/VFO Op&#8217;. </p>
<p> Mem VFO operation is one of: CPY, XCHG, FROM_VFO, TO_VFO, MCL, UP, DOWN, BAND_UP, BAND_DOWN, LEFT, RIGHT, TUNE, TOGGLE.</p>
<dt><code>g, scan &#8216;Scan Fct&#8217; &#8216;Scan Channel&#8217;</code></p>
<dd> Perform &#8216;Scan Fct&#8217; &#8216;Scan Channel&#8217;. </p>
<p> Scan function/channel is one of: STOP, MEM, SLCT, PRIO, PROG, DELTA, VFO, PLT.</p>
<dt><code>H, set_channel &#8216;Channel&#8217;</code></p>
<dd> Set memory &#8216;Channel&#8217; data. Not implemented yet.</p>
<dt><code>h, get_channel</code></p>
<dd> Get memory &#8216;Channel&#8217; data. Not implemented yet.</p>
<dt><code>A, set_trn &#8216;Transceive&#8217;</code></p>
<dd> Set &#8216;Transceive&#8217; mode (reporting event): OFF, RIG, POLL.</p>
<dt><code>a, get_trn</code></p>
<dd> Get &#8216;Transceive&#8217; mode (reporting event) as in <i>set_trn</i> above.</p>
<dt><code>Y, set_ant &#8216;Antenna&#8217;</code></p>
<dd> Set &#8216;Antenna&#8217; number (0, 1, 2, ..).</p>
<dt><code>y, get_ant</code></p>
<dd> Get &#8216;Antenna&#8217; number (0, 1, 2, ..).</p>
<dt><code>*, reset &#8216;Reset&#8217;</code></p>
<dd> Perform rig &#8216;Reset&#8217;. </p>
<p> 0 = None, 1 = Software reset, 2 = VFO reset, 4 = Memory Clear reset, 8 = Master reset. Since these values are defined as a bitmask in rig.h, it should be possible to AND these values together to do multiple resets at once, if the backend supports it or supports a reset action via rig control at all.</p>
<dt><code>b, send_morse &#8216;Morse&#8217;</code></p>
<dd> Send &#8216;Morse&#8217; symbols.</p>
<dt><code>0x87, set_powerstat &#8216;Power Status&#8217;</code></p>
<dd> Set power On/Off/Standby &#8216;Power Status&#8217;. </p>
<p> 0 = Power Off, 1 = Power On, 2 = Power Standby. Defined as a bitmask in rig.h.</p>
<dt><code>0x88, get_powerstat</code></p>
<dd> Get power On/Off/Standby &#8216;Power Status&#8217; as in <i>set_powerstat</i> above.</p>
<dt><code>0x89, send_dtmf &#8216;Digits&#8217;</code></p>
<dd> Set DTMF &#8216;Digits&#8217;.</p>
<dt><code>0x8a, recv_dtmf</code></p>
<dd> Get DTMF &#8216;Digits&#8217;.</p>
<dt><code>_, get_info</code></p>
<dd> Get misc information about the rig (no VFO in &#8216;VFO mode&#8217; or value is passed).</p>
<dt><code>1, dump_caps</code></p>
<dd> Not a real rig remote command, it just dumps capabilities, i.e. what the backend knows about this model, and what it can do. </p>
<p> TODO: Ensure this is in a consistent format so it can be read into a hash, dictionary, etc. Bug reports requested. </p>
<p> <code>N.B.</code>: This command will produce many lines of output so be very careful if using a fixed length array! For example, running this command against the Dummy backend results in over 5kB of text output. </p>
<p> VFO parameter not used in &#8216;VFO mode&#8217;.</p>
<dt><code>2, power2mW &#8216;Power [0.0..1.0]&#8217; &#8216;Frequency&#8217; &#8216;Mode&#8217;</code></p>
<dd> Returns &#8216;Power mW&#8217; </p>
<p> Converts a Power value in a range of <i>0.0 &#8230; 1.0</i> to the real transmit power in milli-Watts (integer). The <i>frequency</i> and <i>mode</i> also need to be provided as output power may vary according to these values. </p>
<p> VFO parameter not used in &#8216;VFO mode&#8217;.</p>
<dt><code>4, mW2power &#8216;Power mW&#8217; &#8216;Frequency&#8217; &#8216;Mode&#8217;</code></p>
<dd> Returns &#8216;Power [0.0..1.0]&#8217; </p>
<p> Converts the real transmit power in milli-Watts (integer) to a Power value in a range of <i>0.0 &#8230; 1.0</i>. The <i>frequency</i> and <i>mode</i> also need to be provided as output power may vary according to these values. </p>
<p> VFO parameter not used in &#8216;VFO mode&#8217;.</p>
<dt><code>w, send_cmd &#8216;Cmd&#8217;</code></p>
<dd> Send raw command string to rig. This is useful for testing and troubleshooting rig commands and responses when developing a backend. </p>
<p> For binary protocols enter values as ��. Expect a &#8216;Reply&#8217; from the rig which will likely be a binary block or an ASCII string depending on the rig&#8217;s protocol (see your radio&#8217;s computer control documentation). </p>
<p> The command terminator, set by the <i>send-cmd-term</i> option above, will terminate each command string sent to the radio. This character should not be a part of the input string.</dl>
<h2>EXAMPLES</h2>
<p> Start <code>rigctl</code> for a Yaesu FT-920 using a USB to serial adapter on Linux in interactive mode: </p>
<p> $ rigctl -m 114 -r /dev/ttyUSB1 </p>
<p> Start <code>rigctl</code> for a Yaesu FT-920 using COM1 on Win32 while generating TRACE output to <code>stderr</code>: </p>
<p> C:\&gt; rigctl -m 114 -r COM1 -vvvvv </p>
<p> Start <code>rigctl</code> for a Yaesu FT-920 using a USB to serial adapter while setting baud rate and stop bits: </p>
<p> $ rigctl -m 114 -r /dev/ttyUSB1 -s 4800 -C stop_bits=2 </p>
<p> Start <code>rigctl</code> for an Elecraft K3 using a USB to serial adapter while specifying a command terminator for the &#8216;w&#8217; command: </p>
<p> $ rigctl -m 229 -r /dev/ttyUSB0 -t&#8217;;&#8217; </p>
<p> Start <code>rigctl</code> using <code>rpc.rigd</code> and setting the frequency and mode: </p>
<p> $ rigctl -m 1901 -r localhost F 7253500 M LSB 0 </p>
<p> Connect to a running <code>rigctld</code> with rig model 2 (&quot;NET rigctl&quot;) on the local host and specifying the TCP port on POSIX: </p>
<p> $ rigctl -m 2 -r localhost:4532 </p>
<p> and on Win32: </p>
<p> C:\&gt; rigctl -m 2 -r 127.0.0.1:4532</p>
<h2>DIAGNOSTICS</h2>
<p> The <code>-v</code>, <code>&#8211;verbose</code> option allows different levels of diagnostics to be output to <code>stderr</code> and correspond to -v for BUG, -vv for ERR, -vvv for WARN, -vvvv for VERBOSE, or -vvvvv for TRACE. </p>
<p> A given verbose level is useful for providing needed debugging information to the email address below. For example, TRACE output shows all of the values sent to and received from the radio which is very useful for radio backend library development and may be requested by the developers.</p>
<h2>EXIT STATUS</h2>
<p> <code>rigctl</code> exits with:<br />
 0 if all operations completed normally;<br />
 1 if there was an invalid command line option or argument;<br />
 2 if an error was returned by <code>Hamlib</code>.</p>
<h2>BUGS</h2>
<p> set_chan has no entry method as of yet, hence left unimplemented. </p>
<p> This almost empty section&#8230;</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to &lt;hamlib-developer [at] lists.sourceforge.net&gt;. </p>
<p> We are already aware of the bugs in the previous section :-)</p>
<h2>AUTHORS</h2>
<p> Written by Stephane Fillod, Nate Bargmann, and the Hamlib Group </p>
<p> &lt;<a rel="nofollow" href="http://www.hamlib.org">http://www.hamlib.org</a>&gt;.</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2000-2010 Stephane Fillod<br />
 Copyright &#169; 2010-2012 Nate Bargmann<br />
 Copyright &#169; 2000-2010 the Hamlib Group. </p>
<p> This is free software; see the source for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-hamlib/">hamlib</a></code>(3), <code><a href="/docs/linux/man/8-rpc-rigd/">rpc.rigd</a></code>(8) <code><a href="/docs/linux/man/8-rigctld/">rigctld</a>(8)</code> </p>
<h2>Index</h2>
