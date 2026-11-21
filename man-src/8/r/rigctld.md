---
title: "rigctld(8)"
name: "rigctld"
section: "8"
letter: "r"
url: "/docs/linux/man/8-rigctld/"
description: "rigctld – Hamlib TCP rig control daemon"
---
<p>rigctld &#8211; Hamlib TCP rig control daemon </p>
<h2>SYNOPSIS</h2>
<p> <code>rigctld</code> [<i>OPTION</i>]...  </p>
<h2>DESCRIPTION</h2>
<p> The <code>rigctld</code> program is a NEW <code>Hamlib</code> rig control daemon ready for testing that handles client requests via TCP sockets. This allows multiple user programs to share one radio (this needs testing), except on Win32 where pthreads are not available. Multiple radios can be controlled on different TCP ports by use of multiple <code>rigctld</code> processes. The syntax of the commands are the same as <code>rigctl</code>. It is hoped that <code>rigctld</code> will be especially useful for client authors using languages such as Perl, Python, PHP, and others. </p>
<p> <code>rigctld</code> communicates to a client through a TCP socket using text commands shared with <code>rigctl</code>. The protocol is simple; commands are sent to <code>rigctld</code> on one line and <code>rigctld</code> responds to &quot;get&quot; commands with the requested values, one per line, when successful, otherwise, it responds with one line &quot;RPRT x&quot;, where x is a negative number indicating the error code. Commands that do not return values respond with the line &quot;RPRT x&quot;, where x is zero when successful, otherwise is a regative number indicating the error code. Each line is terminated with a newline &#8216;\n&#8217; character. This protocol is primarily for use by the <i>NET rigctl</i> (rig model 2)backend. </p>
<p>A separate <code>Extended Response</code> protocol extends the above behavior by echoing the received command string as a header, any returned values as a key: value pair, and the &quot;RPRT x&quot; string as the end of response marker which includes the <code>Hamlib</code> success or failure value. See the <i>PROTOCOL</i> section for details. Consider using this protocol for clients that will interact with <code>rigctld</code> directly through a TCP socket. </p>
<p>Keep in mind that <code>Hamlib</code> is BETA level software. While a lot of backend libraries lack complete rig support, the basic functions are usually well supported. The API may change without publicized notice, while an advancement of the minor version (e.g. 1.1.x to 1.2.x) indicates such a change. </p>
<p>Please report bugs and provide feedback at the e-mail address given in the <i>REPORTING BUGS</i> section. Patches and code enhancements are also welcome.  </p>
<h2>OPTIONS</h2>
<p> This program follows the usual GNU command line syntax, with long options starting with two dashes (&#8216;-&#8216;). </p>
<p>Here is a summary of the supported options: </p>
<dl>
<dt><code>-m, --model=id</code></dt>
<dd> <p> Select radio model number. See the -l, --list option below. </p>
 </dd>
<dt><code>-r, --rig-file=device</code></dt>
<dd> <p> Use <i>device</i> as the file name of the port the radio is connected. Often a serial port, but could be a USB to serial adapter or USB port device. Typically /dev/ttyS0, /dev/ttyS1, /dev/ttyUSB0, etc. on Linux or COM1, COM2, etc. on Win32. </p>
 </dd>
<dt><code>-p, --ptt-file=device</code></dt>
<dd> <p> Use <i>device</i> as the file name of the Push-To-Talk device using a device file as described above. </p>
 </dd>
<dt><code>-d, --dcd-file=device</code></dt>
<dd> <p> Use <i>device</i> as the file name of the Data Carrier Detect device using a device file as described above. </p>
 </dd>
<dt><code>-P, --ptt-type=type</code></dt>
<dd> <p> Use <i>type</i> of Push-To-Talk device. Supported types are RIG (CAT command), DTR, RTS, PARALLEL, NONE. </p>
 </dd>
<dt><code>-D, --dcd-type=type</code></dt>
<dd> <p> Use <i>type</i> of Data Carrier Detect device. Supported types are RIG (CAT command), DSR, CTS, CD, PARALLEL, NONE. </p>
 </dd>
<dt><code>-s, --serial-speed=baud</code></dt>
<dd> <p> Set serial speed to <i>baud</i> rate. Uses maximum serial speed from rig backend capabilities (set by -m above) as the default. </p>
 </dd>
<dt><code>-c, --civaddr=id</code></dt>
<dd> <p> Use <i>id</i> as the CI-V address to communicate with the rig. Only useful for Icom rigs. </p>
<p> <code>N.B.</code>: The <i>id</i> is in decimal notation, unless prefixed by <i>0x</i> for a hexadecimal value. </p>
 </dd>
<dt><code>-T, --listen-addr=IPADDR</code></dt>
<dd> <p> Use <i>IPADDR</i> as the listening IP address. The default is ANY. </p>
<p>N.B.: This option seems mandatory on Win32, eg: -T 127.0.0.1 </p>
 </dd>
<dt><code>-t, --port=number</code></dt>
<dd> <p> Use <i>number</i> as the TCP listening port. The default is 4532. </p>
<p> <code>N.B.</code>: As <code>rotctld</code>&#8216;s default port is 4533, it is advisable to use even numbered ports for <code>rigctld</code>, e.g. 4532, 4534, 4536, etc. </p>
<p>N.B.: This option seems mandatory on Win32, eg: -t 4532 </p>
 </dd>
<dt><code>-L, --show-conf</code></dt>
<dd> <p> List all config parameters for the radio defined with -m above. </p>
 </dd>
<dt><code>-C, --set-conf=parm=val[,parm=val]*</code></dt>
<dd> <p> Set config parameter. e.g. --set-conf=stop_bits=2 </p>
<p>Use -L option for a list. </p>
 </dd>
<dt><code>-l, --list</code></dt>
<dd> <p> List all model numbers defined in <code>Hamlib</code> and exit. As of 1.2.15.1 the list is sorted by model number. </p>
<p> <code>N.B.</code> In Linux the list can be scrolled back using Shift-PageUp/ Shift-PageDown, or using the scrollbars of a virtual terminal in X or the cmd window in Windows. The output can be piped to &#8216;more&#8217; or &#8216;less&#8217;, e.g. &#8216;rigctld -l | more&#8217;. </p>
 </dd>
<dt><code>-u, --dump-caps</code></dt>
<dd> <p> Dump capabilities for the radio defined with -m above and exit. </p>
 </dd>
<dt><code>-o, --vfo</code></dt>
<dd> <p> Set vfo mode, requiring an extra VFO argument in front of each appropriate command (except <i>\set_vfo</i>!). Otherwise, &#8216;currVFO&#8217; is assumed when this option is not set and an extra VFO argument is not used. See <i>\chk_vfo</i> below. </p>
 </dd>
<dt><code>-e, --end-marker</code></dt>
<dd> <p> Use END marker in rigctld protocol. </p>
<p> <code>N.B.</code>: This option should be considered obsolete. Please consider using the Extended Response protocol instead (see <i>PROTOCOL</i> below). This option will be removed in a future Hamlib release. </p>
 </dd>
<dt><code>-v, --verbose</code></dt>
<dd> <p> Set verbose mode, cumulative (see <i>DIAGNOSTICS</i> below). </p>
 </dd>
<dt><code>-h, --help</code></dt>
<dd> <p> Show a summary of these options and exit. </p>
 </dd>
<dt><code>-V, --version</code></dt>
<dd> <p> Show the version of <code>rigctld</code> and exit. </p>
 </dd></dl>
<p> <code>N.B.</code> Some options may not be implemented by a given backend and will return an error. This is most likely to occur with the <i>--set-conf</i> and <i>--show-conf</i> options. </p>
<p>Please note that the backend for the radio to be controlled, or the radio itself may not support some commands. In that case, the operation will fail with a <code>Hamlib</code> error code.  </p>
<h2>COMMANDS</h2>
<p> Commands can be sent over the TCP socket either as a single char, or as a long command name plus the value(s) space separated on one &#8216;\n&#8217; terminated line. See <i>PROTOCOL</i>. </p>
<p>Since most of the <code>Hamlib</code> operations have a <i>set</i> and a <i>get</i> method, an upper case letter will be used for <i>set</i> methods whereas the corresponding lower case letter refers to the <i>get</i> method. Each operation also has a long name; prepend a backslash to send a long command name. </p>
<p>Example (Perl): `print $socket &quot;\\dump_caps\n&quot;;&#8216; to see what the radio&#8217;s backend can do <br />
 (<code>N.B.</code>: In Perl and many other languages a &#8216;\&#8216; will need to be escaped with a preceding &#8216;\&#8216; so that even though two backslash characters appear in the code, only one will be passed to <code>rigctld</code>. This is a possible bug, beware!). </p>
<p>Please note that the backend for the radio to be controlled, or the radio itself may not support some commands. In that case, the operation will fail with a <code>Hamlib</code> error message. </p>
<p>Here is a summary of the supported commands (In the case of &quot;set&quot; commands the quoted string is replaced by the value in the description. In the case of &quot;get&quot; commands the quoted string is the key name of the value returned.): </p>
<dl>
<dt><code>F, set_freq &#8216;Frequency&#8217;</code></dt>
<dd> <p> Set &#8216;Frequency&#8217;, in Hz. </p>
 </dd>
<dt><code>f, get_freq</code></dt>
<dd> <p> Get &#8216;Frequency&#8217;, in Hz. </p>
 </dd>
<dt><code>M, set_mode &#8216;Mode&#8217; &#8216;Passband&#8217;</code></dt>
<dd> <p> Set &#8216;Mode&#8217;: USB, LSB, CW, CWR, RTTY, RTTYR, AM, FM, WFM, AMS, PKTLSB, PKTUSB, PKTFM, ECSSUSB, ECSSLSB, FAX, SAM, SAL, SAH, DSB. </p>
<p>Set &#8216;Passband&#8217; in Hz, or &#8216;0&#8217; for the Hamlib backend default. </p>
 </dd>
<dt><code>m, get_mode</code></dt>
<dd> <p> Get &#8216;Mode&#8217; &#8216;Passband&#8217;. </p>
<p>Returns Mode as a string from <i>set_mode</i> above and Passband in Hz. </p>
 </dd>
<dt><code>V, set_vfo &#8216;VFO&#8217;</code></dt>
<dd> <p> Set &#8216;VFO&#8217;: VFOA, VFOB, VFOC, currVFO, VFO, MEM, Main, Sub, TX, RX. </p>
<p>In VFO mode only a single VFO parameter is required. </p>
 </dd>
<dt><code>v, get_vfo</code></dt>
<dd> <p> Get current &#8216;VFO&#8217;. </p>
<p>Returns VFO as a string from <i>set_vfo</i> above. </p>
 </dd>
<dt><code>J, set_rit &#8216;RIT&#8217;</code></dt>
<dd> <p> Set &#8216;RIT&#8217;, in Hz, can be + or -. </p>
<p>A value of &#8216;0&#8217; resets RIT and *should* turn RIT off. If not, file a bug report against the Hamlib backend. </p>
 </dd>
<dt><code>j, get_rit</code></dt>
<dd> <p> Get &#8216;RIT&#8217;, in Hz. </p>
 </dd>
<dt><code>Z, set_xit &#8216;XIT&#8217;</code></dt>
<dd> <p> Set &#8216;XIT&#8217;, in Hz can be + or -. </p>
<p>A value of &#8216;0&#8217; resets RIT and *should* turn RIT off. If not, file a bug report against the Hamlib backend. </p>
 </dd>
<dt><code>z, get_xit</code></dt>
<dd> <p> Get &#8216;XIT&#8217;, in Hz. </p>
 </dd>
<dt><code>T, set_ptt &#8216;PTT&#8217;</code></dt>
<dd> <p> Set &#8216;PTT&#8217;, 0 (RX) or 1 (TX). </p>
 </dd>
<dt><code>t, get_ptt</code></dt>
<dd> <p> Get &#8216;PTT&#8217; status. </p>
 </dd>
<dt><code>0x8b, get_dcd</code></dt>
<dd> <p> Get &#8216;DCD&#8217; (squelch) status, 0 (Closed) or 1 (Open) </p>
 </dd>
<dt><code>R, set_rptr_shift &#8216;Rptr Shift&#8217;</code></dt>
<dd> <p> Set &#8216;Rptr Shift&#8217;: &quot;+&quot;, &quot;-&quot; or something else for none. </p>
 </dd>
<dt><code>r, get_rptr_shift</code></dt>
<dd> <p> Get &#8216;Rptr Shift&#8217;. Returns &quot;+&quot;, &quot;-&quot; or &quot;None&quot;. </p>
 </dd>
<dt><code>O, set_rptr_offs &#8216;Rptr Offset&#8217;</code></dt>
<dd> <p> Set &#8216;Rptr Offset&#8217;, in Hz. </p>
 </dd>
<dt><code>o, get_rptr_offs</code></dt>
<dd> <p> Get &#8216;Rptr Offset&#8217;, in Hz. </p>
 </dd>
<dt><code>C, set_ctcss_tone &#8216;CTCSS Tone&#8217;</code></dt>
<dd> <p> Set &#8216;CTCSS Tone&#8217;, in tenths of Hz. </p>
 </dd>
<dt><code>c, get_ctcss_tone</code></dt>
<dd> <p> Get &#8216;CTCSS Tone&#8217;, in tenths of Hz. </p>
 </dd>
<dt><code>D, set_dcs_code &#8216;DCS Code&#8217;</code></dt>
<dd> <p> Set &#8216;DCS Code&#8217;. </p>
 </dd>
<dt><code>d, get_dcs_code</code></dt>
<dd> <p> Get &#8216;DCS Code&#8217;. </p>
 </dd>
<dt><code>0x90, set_ctcss_sql &#8216;CTCSS Sql&#8217;</code></dt>
<dd> <p> Set &#8216;CTCSS Sql&#8217; tone, in tenths of Hz. </p>
 </dd>
<dt><code>0x91, get_ctcss_sql</code></dt>
<dd> <p> Get &#8216;CTCSS Sql&#8217; tone, in tenths of Hz. </p>
 </dd>
<dt><code>0x92, set_dcs_sql &#8216;DCS Sql&#8217;</code></dt>
<dd> <p> Set &#8216;DCS Sql&#8217; code. </p>
 </dd>
<dt><code>0x93, get_dcs_sql</code></dt>
<dd> <p> Get &#8216;DCS Sql&#8217; code. </p>
 </dd>
<dt><code>I, set_split_freq &#8216;Tx Frequency&#8217;</code></dt>
<dd> <p> Set &#8216;TX Frequency&#8217;, in Hz. </p>
 </dd>
<dt><code>i, get_split_freq</code></dt>
<dd> <p> Get &#8216;TX Frequency&#8217;, in Hz. </p>
 </dd>
<dt><code>X, set_split_mode &#8216;TX Mode&#8217; &#8216;TX Passband&#8217;</code></dt>
<dd> <p> Set &#8216;TX Mode&#8217;: AM, FM, CW, CWR, USB, LSB, RTTY, RTTYR, WFM, AMS, PKTLSB, PKTUSB, PKTFM, ECSSUSB, ECSSLSB, FAX, SAM, SAL, SAH, DSB. </p>
<p>The &#8216;TX Passband&#8217; is the exact passband in Hz, or &#8216;0&#8217; for the Hamlib backend default. </p>
 </dd>
<dt><code>x, get_split_mode</code></dt>
<dd> <p> Get &#8216;TX Mode&#8217; and &#8216;TX Passband&#8217;. </p>
<p>Returns TX mode as a string from <i>set_split_mode</i> above and TX passband in Hz. </p>
 </dd>
<dt><code>S, set_split_vfo &#8216;Split&#8217; &#8216;TX VFO&#8217;</code></dt>
<dd> <p> Set &#8216;Split&#8217; mode, &#8216;0&#8217; or &#8216;1&#8217;, and &#8216;TX VFO&#8217; from <i>set_vfo</i> above. </p>
 </dd>
<dt><code>s, get_split_vfo</code></dt>
<dd> <p> Get &#8216;Split&#8217; mode, &#8216;0&#8217; or &#8216;1&#8217;, and &#8216;TX VFO&#8217;. </p>
 </dd>
<dt><code>N, set_ts &#8216;Tuning Step&#8217;</code></dt>
<dd> <p> Set &#8216;Tuning Step&#8217;, in Hz. </p>
 </dd>
<dt><code>n, get_ts</code></dt>
<dd> <p> Get &#8216;Tuning Step&#8217;, in Hz. </p>
 </dd>
<dt><code>U, set_func &#8216;Func&#8217; &#8216;Func Status&#8217;</code></dt>
<dd> <p> Set &#8216;Func&#8217; &#8216;Func Status&#8217;. </p>
<p>Func is one of: FAGC, NB, COMP, VOX, TONE, TSQL, SBKIN, FBKIN, ANF, NR, AIP, APF, MON, MN, RF, ARO, LOCK, MUTE, VSC, REV, SQL, ABM, BC, MBC, AFC, SATMODE, SCOPE, RESUME, TBURST, TUNER. </p>
<p>Func Status argument is a non null value for &quot;activate&quot;, &quot;de-activate&quot; otherwise, much as TRUE/FALSE definitions in C language. </p>
 </dd>
<dt><code>u, get_func</code></dt>
<dd> <p> Get &#8216;Func&#8217; &#8216;Func Status&#8217;. </p>
<p>Returns Func as a string from <i>set_func</i> above and Func status as a non null value. </p>
 </dd>
<dt><code>L, set_level &#8216;Level&#8217; &#8216;Level Value&#8217;</code></dt>
<dd> <p> Set &#8216;Level&#8217; and &#8216;Level Value&#8217;. </p>
<p>Level is one of: PREAMP, ATT, VOX, AF, RF, SQL, IF, APF, NR, PBT_IN, PBT_OUT, CWPITCH, RFPOWER, MICGAIN, KEYSPD, NOTCHF, COMP, AGC, BKINDL, BAL, METER, VOXGAIN, ANTIVOX, SLOPE_LOW, SLOPE_HIGH, RAWSTR, SQLSTAT, SWR, ALC, STRENGTH. </p>
<p>The Level Value can be a float or an integer. </p>
 </dd>
<dt><code>l, get_level</code></dt>
<dd> <p> Get &#8216;Level&#8217; &#8216;Level Value&#8217;. </p>
<p>Returns Level as a string from <i>set_level</i> above and Level value as a float or integer. </p>
 </dd>
<dt><code>P, set_parm &#8216;Parm&#8217; &#8216;Parm Value&#8217;</code></dt>
<dd> <p> Set &#8216;Parm&#8217; &#8216;Parm Value&#8217; </p>
<p>Parm is one of: ANN, APO, BACKLIGHT, BEEP, TIME, BAT, KEYLIGHT. </p>
 </dd>
<dt><code>p, get_parm</code></dt>
<dd> <p> Get &#8216;Parm&#8217; &#8216;Parm Value&#8217;. </p>
<p>Returns Parm as a string from <i>set_parm</i> above and Parm Value as a float or integer. </p>
 </dd>
<dt><code>B, set_bank &#8216;Bank&#8217;</code></dt>
<dd> <p> Set &#8216;Bank&#8217;. Sets the current memory bank number. </p>
 </dd>
<dt><code>E, set_mem &#8216;Memory#&#8216;</code></dt>
<dd> <p> Set &#8216;Memory#&#8216; channel number. </p>
 </dd>
<dt><code>e, get_mem</code></dt>
<dd> <p> Get &#8216;Memory#&#8216; channel number. </p>
 </dd>
<dt><code>G, vfo_op &#8216;Mem/VFO Op&#8217;</code></dt>
<dd> <p> Perform &#8216;Mem/VFO Op&#8217;. </p>
<p>Mem VFO operation is one of: CPY, XCHG, FROM_VFO, TO_VFO, MCL, UP, DOWN, BAND_UP, BAND_DOWN, LEFT, RIGHT, TUNE, TOGGLE. </p>
 </dd>
<dt><code>g, scan &#8216;Scan Fct&#8217; &#8216;Scan Channel&#8217;</code></dt>
<dd> <p> Perform &#8216;Scan Fct&#8217; &#8216;Scan Channel&#8217;. </p>
<p>Scan function/channel is one of: STOP, MEM, SLCT, PRIO, PROG, DELTA, VFO, PLT. </p>
 </dd>
<dt><code>H, set_channel &#8216;Channel&#8217;</code></dt>
<dd> <p> Set memory &#8216;Channel&#8217; data. Not implemented yet. </p>
 </dd>
<dt><code>h, get_channel</code></dt>
<dd> <p> Get memory &#8216;Channel&#8217; data. Not implemented yet. </p>
 </dd>
<dt><code>A, set_trn &#8216;Transceive&#8217;</code></dt>
<dd> <p> Set &#8216;Transceive&#8217; mode (reporting event): OFF, RIG, POLL. </p>
 </dd>
<dt><code>a, get_trn</code></dt>
<dd> <p> Get &#8216;Transceive&#8217; mode (reporting event) as in <i>set_trn</i> above. </p>
 </dd>
<dt><code>Y, set_ant &#8216;Antenna&#8217;</code></dt>
<dd> <p> Set &#8216;Antenna&#8217; number (0, 1, 2, ..). </p>
 </dd>
<dt><code>y, get_ant</code></dt>
<dd> <p> Get &#8216;Antenna&#8217; number (0, 1, 2, ..). </p>
 </dd>
<dt><code>*, reset &#8216;Reset&#8217;</code></dt>
<dd> <p> Perform rig &#8216;Reset&#8217;. </p>
<p>0 = None, 1 = Software reset, 2 = VFO reset, 4 = Memory Clear reset, 8 = Master reset. Since these values are defined as a bitmask in rig.h, it should be possible to AND these values together to do multiple resets at once, if the backend supports it or supports a reset action via rig control at all. </p>
 </dd>
<dt><code>b, send_morse &#8216;Morse&#8217;</code></dt>
<dd> <p> Send &#8216;Morse&#8217; symbols. </p>
 </dd>
<dt><code>0x87, set_powerstat &#8216;Power Status&#8217;</code></dt>
<dd> <p> Set power On/Off/Standby &#8216;Power Status&#8217;. </p>
<p>0 = Power Off, 1 = Power On, 2 = Power Standby. Defined as a bitmask in rig.h. </p>
 </dd>
<dt><code>0x88, get_powerstat</code></dt>
<dd> <p> Get power On/Off/Standby &#8216;Power Status&#8217; as in <i>set_powerstat</i> above. </p>
 </dd>
<dt><code>0x89, send_dtmf &#8216;Digits&#8217;</code></dt>
<dd> <p> Set DTMF &#8216;Digits&#8217;. </p>
 </dd>
<dt><code>0x8a, recv_dtmf</code></dt>
<dd> <p> Get DTMF &#8216;Digits&#8217;. </p>
 </dd>
<dt><code>_, get_info</code></dt>
<dd> <p> Get misc information about the rig (no VFO in &#8216;VFO mode&#8217; or value is passed). </p>
 </dd>
<dt><code>1, dump_caps</code></dt>
<dd> <p> Not a real rig remote command, it just dumps capabilities, i.e. what the backend knows about this model, and what it can do. TODO: Ensure this is in a consistent format so it can be read into a hash, dictionary, etc. Bug reports requested. </p>
<p> <code>N.B.</code>: This command will produce many lines of output so be very careful if using a fixed length array! For example, running this command against the Dummy backend results in over 5kB of text output. </p>
<p>VFO parameter not used in &#8216;VFO mode&#8217;. </p>
 </dd>
<dt><code>2, power2mW &#8216;Power [0.0..1.0]&#8216; &#8216;Frequency&#8217; &#8216;Mode&#8217;</code></dt>
<dd> <p> Returns &#8216;Power mW&#8217; </p>
<p>Converts a Power value in a range of <i>0.0 ... 1.0</i> to the real transmit power in milli-Watts (integer). The <i>frequency</i> and <i>mode</i> also need to be provided as output power may vary according to these values. </p>
<p>VFO parameter not used in &#8216;VFO mode&#8217;. </p>
 </dd>
<dt><code>4, mW2power &#8216;Power mW&#8217; &#8216;Frequency&#8217; &#8216;Mode&#8217;</code></dt>
<dd> <p> Returns &#8216;Power [0.0..1.0]&#8216; </p>
<p>Converts the real transmit power in milli-Watts (integer) to a Power value in a range of <i>0.0 ... 1.0</i>. The <i>frequency</i> and <i>mode</i> also need to be provided as output power may vary according to these values. </p>
<p>VFO parameter not used in &#8216;VFO mode&#8217;. </p>
 </dd>
<dt><code>w, send_cmd &#8216;Cmd&#8217;</code></dt>
<dd> <p> Send raw command string to rig. </p>
<p>For binary protocols enter values as \0xAA\0xBB. Expect a &#8216;Reply&#8217; from the rig which will likely be a binary block or an ASCII string. </p>
 </dd>
<dt><code>chk_vfo</code></dt>
<dd> <p> Returns &quot;CHKVFO 1\n&quot; (single line only) if <code>rigctld</code> was invoked with the <i>-o</i> or <i>--vfo</i> option, &quot;CHKVFO 0\n&quot; if not. </p>
<p>When in VFO mode the client will need to pass &#8216;VFO&#8217; as the first parameter to <i>\set</i> or <i>\get</i> commands. &#8216;VFO&#8217; is one of the strings defined for <i>\set_vfo</i> above. </p>
 </dd></dl>
<h2>PROTOCOL</h2>
<p> <code>Default Protocol</code> </p>
<p>The <code>rigctld</code> protocol is intentionally simple. Commands are entered on a single line with any needed values. In Perl, reliable results are obtained by terminating each command string with a newline character, &#8216;\n&#8217;. </p>
<p>Example <i>set</i> (Perl code): </p>
<p>print $socket &quot;F 14250000\n&quot;; <br />
 print $socket &quot;\\set_mode LSB 2400\n&quot;; # escape leading &#8216;\&#8216; </p>
<p>A one line response will be sent as a reply to <i>set</i> commands, &quot;RPRT <i>x</i>\n&quot; where <i>x</i> is the Hamlib error code with &#8216;0&#8217; indicating success of the command. </p>
<p>Responses from <code>rigctld</code> <i>get</i> commands are text values and match the same tokens used in the <i>set</i> commands. Each value is returned on its own line. On error the string &quot;RPRT <i>x</i>\n&quot; is returned where <i>x</i> is the Hamlib error code. </p>
<p>Example <i>get</i> (Perl code): </p>
<p>print $socket &quot;f\n&quot;; <br />
 &quot;14250000\n&quot; </p>
<p>Most <i>get</i> functions return one to three values. A notable exception is the <i>\dump_caps</i> function which returns many lines of key:value pairs. </p>
<p>This protocol is primarily used by the <i>NET rigctl</i> (rigctl model 2) backend which allows applications already written for Hamlib&#8217;s C API to take advantage of <code>rigctld</code> without the need of rewriting application code. An application&#8217;s user can select rig model 2 (&quot;NET rigctl&quot;) and then set rig_pathname to &quot;localhost:4532&quot; or other network host:port (set by the <i>-t</i> option above). </p>
<p> <code>Extended Response Protocol</code> </p>
<p>An <i>EXPERIMENTAL</i> Extended Response protocol has been introduced into <code>rigctld</code> as of February 16, 2010. This protocol adds several rules to the strings returned by <code>rigctld</code> and adds a rule for the command syntax. </p>
<p>1. The command received by <code>rigctld</code> is echoed with its long command name followed by the value(s) (if any) received from the client terminated by the specified response separator as the record line of the response. </p>
<p>2. The last line of each block is the string &quot;RPRT <i>x</i>\n&quot; where <i>x</i> is the numeric return value of the Hamlib backend function that was called by the command. </p>
<p>3. Any records consisting of data values returned by the rig backend are prepended by a string immediately followed by a colon then a space and then the value terminated by the response separator. e.g. &quot;Frequency: 14250000\n&quot; when the command was prepended by &#8216;+&#8216;. </p>
<p>4. All commands received will be acknowledged by <code>rigctld</code> with lines from rules 1 and 2. Lines from rule 3 are only returned when data values must be returned to the client. </p>
<p>An example response to a <i>+\set_mode</i> command sent from the shell prompt (note the prepended &#8216;+&#8216;): </p>
<p>$ echo &quot;+M USB 2400&quot; | nc -w 1 localhost 4532 <br />
 set_mode: USB 2400 <br />
 RPRT 0 </p>
<p>In this case the long command name and values are returned on the first line and the second line contains the end of block marker and the numeric rig backend return value indicating success. </p>
<p>An example response to a <i>\get_mode</i> query: </p>
<p>$ echo &quot;+\get_mode&quot; | nc -w 1 localhost 4532 <br />
 get_mode: <br />
 Mode: USB <br />
 Passband: 2400 <br />
 RPRT 0 </p>
<p>In this case, as no value is passed to <code>rigctld</code>, the first line consists only of the long command name. The final line shows that the command was processed successfully by the rig backend. </p>
<p>Invoking the Extended Response protocol requires prepending a command with a punctuation character. As shown in the examples above, prepending a &#8216;+&#8216; character to the command results in the responses being separated by a newline character (&#8216;\n&#8217;). Any other punctuation character recognized by the C <i>ispunct()</i> function except &#8216;\&#8216;, &#8216;?&#8216;, or &#8216;_&#8216; will cause that character to become the response separator and the entire response will be on one line. </p>
<p>Separator character summary: </p>
<dl>
<dt><code>&#8216;+&#8216;</code></dt>
<dd> <p> <br />
 Each record of the response is appended with a newline (&#8216;\n&#8217;). </p>
 </dd>
<dt><code>&#8216;;&#8216;, &#8216;|&#8216;, or &#8216;,&#8216;</code></dt>
<dd> <p> <br />
 Each record of the response is appended by the given character resulting in entire response on one line. </p>
<p>Common record separators for text representations of spreadsheet data, etc. </p>
 </dd>
<dt><code>&#8216;?&#8216;</code></dt>
<dd> <p> <br />
 Reserved for &#8216;help&#8217; in rigctl short command </p>
 </dd>
<dt><code>&#8216;_&#8216;</code></dt>
<dd> <p> <br />
 Reserved for \get_info short command </p>
 </dd>
<dt><code>&#8216;#&#8216;</code></dt>
<dd> <p> <br />
 Reserved for comments when reading a command file script </p>
<p>Other punctuation characters have not been tested! Use at your own risk. </p>
 </dd></dl>
<p>For example, invoking a <i>;\get_mode</i> query with a leading &#8216;;&#8216; returns: </p>
<p>get_mode:;Mode: USB;Passband: 2400;RPRT 0 </p>
<p>Or, using the pipe character &#8216;|&#8216; returns: </p>
<p>get_mode:|Mode: USB|Passband: 2400|RPRT 0 </p>
<p>And a \set_mode command prepended with a &#8216;|&#8216; returns: </p>
<p>set_mode: USB 2400|RPRT 0 </p>
<p>Such a format will allow reading a response as a single event using a preferred response separator. Other punctuation characters have not been tested! </p>
<p>The following commands have been tested with the Extended Response protocol and the included <code>testctld.pl</code> script: <br />
 <i>\set_freq</i> <i>\get_freq</i> <i>\set_split_freq</i> <i>\get_split_freq</i> <br />
 <i>\set_mode</i> <i>\get_mode</i> <i>\set_split_mode</i> <i>\get_split_mode</i> <br />
 <i>\set_vfo</i> <i>\get_vfo</i> <i>\set_split_vfo</i> <i>\get_split_vfo</i> <br />
 <i>\set_rit</i> <i>\get_rit</i> <br />
 <i>\set_xit</i> <i>\get_xit</i> <br />
 <i>\set_ptt</i> <i>\get_ptt</i> <br />
 <i>\power2mW</i> <i>\mW2power</i> <br />
 <i>\dump_caps</i>  </p>
<h2>EXAMPLES</h2>
<p> Start <code>rigctld</code> for a Yaesu FT-920 using a USB-to-serial adapter and backgrounding on Linux: </p>
<p>$ rigctld -m 114 -r /dev/ttyUSB1 &amp; </p>
<p>Start <code>rigctld</code> for a Yaesu FT-920 using a USB to serial adapter while setting baud rate and stop bits, and backgrounding: </p>
<p>$ rigctld -m 114 -r /dev/ttyUSB1 -s 4800 -C stop_bits=2 &amp; </p>
<p>Start <code>rigctld</code> for an Elecraft K3 using COM2 on Win32 and specifying the listening address and port: </p>
<p>C:\&gt; rigctld -m 229 -r COM2 -T 127.0.0.1 -t 4532 </p>
<p>Connect to the already running <code>rigctld</code>, and set current frequency to 14.266 MHz with a 1 second read timeout using the default protocol from the shell prompt on POSIX: </p>
<p>$ echo &quot;\set_freq 14266000&quot; | nc -w 1 localhost 4532 </p>
<p>Connect to a running <code>rigctld</code> with <code>rigctl</code> on the local host on POSIX: </p>
<p>$ rigctl -m 2 </p>
<p>and on Win32: </p>
<p>C:\&gt; rigctl -m 2 -r 127.0.0.1:4532  </p>
<h2>DIAGNOSTICS</h2>
<p> The <code>-v</code>, <code>--verbose</code>, option allows different levels of diagnostics to be output to <code>stderr</code> and correspond to -v for BUG, -vv for ERR, -vvv for WARN, -vvvv for VERBOSE, or -vvvvv for TRACE. </p>
<p>A given verbose level is useful for providing needed debugging information to the email address below. For example, TRACE output shows all of the values sent to and received from the radio which is very useful for radio backend library development and may be requested by the developers. See the <code>README.betatester</code> and <code>README.developer</code> files for more information.  </p>
<h2>SECURITY</h2>
<p> No authentication whatsoever; DO NOT leave this TCP port open wide to the Internet. Please ask if stronger security is needed or consider using an SSH tunnel. </p>
<p>As <code>rigctld</code> does not need any greater permissions than <code>rigctl</code>, it is advisable to not start <code>rigctld</code> as <i>root</i> or another system user account in order to limit any vulnerability.  </p>
<h2>BUGS</h2>
<p> The daemon is not detaching and backgrounding itself. </p>
<p>Much testing needs to be done.  </p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to &lt;hamlib-developer [at] lists.sourceforge.net&gt;. </p>
<p>We are already aware of the bugs in the previous section :-)  </p>
<h2>AUTHORS</h2>
<p> Written by Stephane Fillod, Nate Bargmann, and the Hamlib Group </p>
<p>&lt;<a rel="nofollow" href="http://www.hamlib.org">http://www.hamlib.org</a>&gt;.  </p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2000-2010 Stephane Fillod <br />
 Copyright &#169; 2011-2012 Nate Bargmann <br />
 Copyright &#169; 2000-2010 the Hamlib Group. </p>
<p>This is free software; see the source for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-rigctl/">rigctl</a></code>(1), <code>hamlib</code>(3) </p>
<h2>Index</h2>
<dl>
<dt><a href="#lbAB">NAME</a></dt>
<dd>  </dd>
<dt><a href="#lbAC">SYNOPSIS</a></dt>
<dd>  </dd>
<dt><a href="#lbAD">DESCRIPTION</a></dt>
<dd>  </dd>
<dt><a href="#lbAE">OPTIONS</a></dt>
<dd>  </dd>
<dt><a href="#lbAF">COMMANDS</a></dt>
<dd>  </dd>
<dt><a href="#lbAG">PROTOCOL</a></dt>
<dd>  </dd>
<dt><a href="#lbAH">EXAMPLES</a></dt>
<dd>  </dd>
<dt><a href="#lbAI">DIAGNOSTICS</a></dt>
<dd>  </dd>
<dt><a href="#lbAJ">SECURITY</a></dt>
<dd>  </dd>
<dt><a href="#lbAK">BUGS</a></dt>
<dd>  </dd>
<dt><a href="#lbAL">REPORTING BUGS</a></dt>
<dd>  </dd>
<dt><a href="#lbAM">AUTHORS</a></dt>
<dd>  </dd>
<dt><a href="#lbAN">COPYRIGHT</a></dt>
<dd>  </dd>
<dt><a href="#lbAO">SEE ALSO</a></dt>
<dd>  </dd></dl>
