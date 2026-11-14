---
title: "gpm(8)"
name: "gpm"
section: "8"
letter: "g"
url: "/docs/linux/man/8-gpm/"
description: "gpm – a cut and paste utility and mouse server for virtual consoles"
---

<p>gpm &#8211; a cut and paste utility and mouse server for virtual consoles</p>
<h2>Synopsis</h2>
<p><code>gpm</code> [ <i>options</i> ]</p>
<h2>Description</h2>
<p>This package tries to be a useful mouse server for applications running on the Linux console. It is based on the &quot;selection&quot; package, and some of its code comes from selection itself. This package is intended as a replacement for &quot;selection&quot; as a cut-and-paste mechanism; it also provides additional facilities. The &quot;selection&quot; package offered the first cut-and-paste implementation for Linux using two mouse buttons, and the cut buffer is still called &quot;selection buffer&quot; or just &quot;selection&quot; throughout this document. The information below is extracted from the texinfo file, which is the preferred source of information. The gpm executable is meant to act like a daemon (thus, gpmd would be a better name for it). This section is meant to describe the command-line options for gpm, while its internals are outlined in the next section. Due to restrictions in the ioctl(TIOCLINUX) system call, gpm must be run by the superuser. The restrictions have been added in the last 1.1 kernels to fix a security hole related to selection and screen dumping. The server can be configured to match the user&#8217;s taste, and any application using the mouse will inherit the server&#8217;s attitude. From release 1.02 up to 1.19.2 is was possible for any user logged on the system console to change the mouse feeling using the -q option. This is no longer possible for security reasons. As of 0.97 the server program puts itself in the background. To kill gpm you can just reinvoke it with the -k cmdline switch, although killall gpm can be a better choice. </p>
<h2>Special Commands</h2>
<p>Version 1.10 adds the capability to execute special commands on certain circumstances. Special commands default to rebooting and halting the system, but the user can specify his/her personal choice. The capability to invoke commands using the mouse is a handy one for programmers, because it allows to issue a clean shutdown when the keyboard is locked and no network is available to restore the system to a sane state. </p>
<p> Special commands are toggled by triple-clicking the left and right button &#8212; an unlikely event during normal mouse usage. The easiest way to triple-click is pressing one of the buttons and triple-click the other one. When special processing is toggled, a message appears on the console (and the speaker beeps twice, if you have a speaker); if the user releases all the buttons and presses one of them again within three seconds, then the special command corresponding to the button is executed. </p>
<p> The default special commands are:</p>
<dl>
<dt>left button</p>
<dd>Reboot the system by signalling the init process</p>
<dt>middle button (if any)</p>
<dd>Execute /sbin/shutdown -h now</p>
<dt>right button</p>
<dd>Execute /sbin/shutdown -r now </p>
</dl>
<p> The -S command line switch enables special command processing and allows to change the three special commands. To accept the default commands use -S &quot;&quot; (i.e., specify an empty argument). To specify your own commands, use a colon-separated list to specify commands associated to the left, middle and right button. If any of the commands is empty, it is interpreted as `send a signal to the init process&#8217;. This particular operation is supported, in addition to executing external commands, because sometimes bad bugs put the system to the impossibility to fork; in these rare case the programmer should be able to shutdown the system anyways, and killing init from a running process is the only way to do it. </p>
<p> As an example, -S &quot;:telinit 1:/sbin/halt&quot;, associates killing init to the left button, going single user to the middle one, and halting the system to the right button. </p>
<p> System administrators should obviously be careful about special commands, as gpm runs with superuser permissions. Special commands are best suited for computers whose mouse can be physically accessed only by trusted people.</p>
<h2>Command Line Options</h2>
<p>Available command line options are the following:</p>
<dl>
<dt>-a <code>accel</code></p>
<dd>Set the acceleration value used when a single motion event is longer than <code>delta</code> (see -d).</p>
<dt>-A[<code>limit</code>]</p>
<dd>Start up with selection pasting disabled. This is intended as a security measure; a plausible attack on a system seems to be to stuff a nasty shell command into the selection buffer (rm -rf /) including the terminating line break, then all the victim has to do is click the middle mouse button .. As of version 1.17.2, this has developed into a more general aging mechanism; the gpm daemon can disable (age) selection pasting automatically after a period of inactivity. To enable this mode just give the optional <code>limit</code> parameter (no space in between !) which is interpreted as the time in seconds for which a selection is considered valid and pastable. As of version 1.15.7, a trivial program called disable-paste is provided. The following makes a good addition to /etc/profile if you allow multiple users to work on your console. </p>
</dl>
<p> case $( /usr/bin/tty ) in<br />
 /dev/tty[0-9]*) /usr/bin/disable-paste ;;<br />
 esac</p>
<dl>
<dt>-b <code>baud</code></p>
<dd>Set the baud rate.</p>
<dt>-B <code>sequence</code></p>
<dd>Set the button sequence. 123 is the normal sequence, 321 can be used by left-handed people, and 132 can be useful with two-button mice (especially within Emacs). All the button permutations are allowable.</p>
<dt>-d <code>delta</code></p>
<dd>Set the delta value. When a single motion event is longer than <code>delta</code>, <code>accel</code> is used as a multiplying factor. (Must be 2 or above)</p>
<dt>-D</p>
<dd>Do not automatically enter background operation when started, and log messages to the standard error stream, not the syslog mechanism. This is useful for debugging; in previous releases it was done with a compile-time option.</p>
<dt>-g <code>number</code></p>
<dd>With glidepoint devices, emulate the specified button with tapping. <code>number</code> must be 1, 2, or 3, and refers to the button number before the -B button remapping is performed. This option applies to the mman and ps2 decoding. No button is emulated by default because the ps2 tapping is incompatible with some normal ps2 mice</p>
<dt>-h</p>
<dd>Print a summary of command line options.</p>
<dt>-i <code>interval</code></p>
<dd>Set <code>interval</code> to be used as an upper time limit for multiple clicks. If the interval between button-up and button-down events is less than <code>limit</code>, the press is considered a double or triple click. Time is in milliseconds.</p>
<dt>-k</p>
<dd>Kill a running gpm. This can be used by busmouse users to kill gpm before running X (unless they use -R or the single-open limitation is removed from the kernel).</p>
<dt>-l <code>charset</code></p>
<dd>Choose the inword() look up table. The <code>charset</code> argument is a list of characters. &#8211; is used to specify a range and \ is used to escape the next character or to provide octal codes. Only visible character can appear in <code>charset</code> because control characters can&#8217;t appear in text-mode video memory, whence selection is cut.</p>
<dt>-m <code>filename</code></p>
<dd>Choose the mouse file to open. Must be before -t and -o.</p>
<dt>-M</p>
<dd>Enable multiple mode. The daemon will read two different mouse devices. Any subsequent option will refer to the second device, while any preceding option will be used for the first device. This option automatically forces the repeater (-R) option on.</p>
<dt>-o <code>list-of-extra-options</code></p>
<dd>The option works similary to the &#8220;-o&#8221; option of mount; it is used to specify a list of &#8220;extra options&#8221; that are specific to each mouse type. The list is comma-separated. The options dtr, rts or both are used by the serial initialization to toggle the modem lines like, compatibly with earlier gpm versions; note however that using -o dtr associated with non-plain-serial mouse types may now generate an error. And by the way, use -o after -m and after -t. </p>
<dt>-p</p>
<dd>Forces the pointer to be visible while selecting. This is the behaviour of selection-1.7, but it is sometimes confusing. The default is not to show the pointer, which can be confusing as well.</p>
<dt>-r <code>number</code></p>
<dd>Set the responsiveness. A higher responsiveness is used for a faster cursor motion.</p>
<dt>-R[<code>name</code>]</p>
<dd>Causes gpm to act as a repeater: any mouse data received while in graphic mode will be produced on the fifo /dev/gpmdata in protocol <code>name</code>, given as an optional argument (no space in between !). In principle, you can use the same names as for the -t option, although repeating into some protocols may not be implemented for a while. In addition, you can specify raw as the <code>name</code>, to repeat the mouse data byte by byte, without any protocol translation. If <code>name</code> is omitted, it defaults to msc. Using gpm in repeater mode, you can configure the X server to use its fifo as a mouse device. This option is useful for bus-mouse owners to override the single-open limitation. It is also an easy way to manage those stupid dual-mode mice which force you to keep the middle button down while changing video mode. The option is forced on by the -M option.</p>
<dt>-s <code>number</code></p>
<dd>Set the sample rate for the mouse device.</p>
<dt>-S <code>commands</code></p>
<dd>Enable special-command processing, and optionally specify custom commands as a colon-separated list. See above for a detailed description of special commands.</p>
<dt>-t <code>name</code></p>
<dd>Set the mouse type. Use -t help to get a list of allowable types. Since version 1.18.1, the list also shows which protocols are available as repeaters (see -R above), by marking them with an asterisk (&#8220;*&#8221;). </p>
<p> Use -t after you selected the mouse device with -m.</p>
<dt>-v</p>
<dd>Print version information and exit.</p>
<dt>-2</p>
<dd>Force two buttons. This means that the middle button, if any, will be taken as it was the right one.</p>
<dt>-3</p>
<dd>Force three buttons. By default the mouse is considered to be a 2-buttons one, until the middle button is pressed. If three buttons are there, the right one is used to extend the selection, and the middle one is used to paste it. Beware: if you use the -3 option with a 2-buttons mouse, you won&#8217;t be able to paste the selection. </p>
</dl>
<h2>Operation</h2>
<p>To select text press the left mouse button and drag the mouse. To paste text in the same or another console, press the middle button. The right button is used to extend the selection, like in `xterm&#8217;. </p>
<p> Two-button mice use the right button to paste text. </p>
<p> Double and triple clicks select whole word and whole lines. Use of the `-p&#8217; option is recommended for best visual feedback. </p>
<p> If a trailing space after the contents of a line is highlighted, and if there is no other text on the remainder of the line, the rest of the line will be selected automatically. If a number of lines are selected, highlighted trailing spaces on each line will be removed from the selection buffer. </p>
<p> Any output on the virtual console holding the selection will clear the highlighted selection from the screen, to maintain integrity of the display, although the contents of the paste buffer will be unaffected. </p>
<p> The selection mechanism is disabled if the controlling virtual console is placed in graphics mode, for example when running X11, and is re-enabled when text mode is resumed. (But see BUGS section below.)</p>
<h2>Bugs</h2>
<p>The gpm server may have problems interacting with X: if your mouse is a single-open device (i.e. a bus mouse), you should kill gpm before starting X, or use the -R option (see above). To kill gpm just invoke gpm -k. This problem doesn&#8217;t apply to serial mice. Two instances of gpm can&#8217;t run on the same system. If you have two mice use the -M option (see above). While the current console is in graphic mode, gpm sleeps until text mode is back (unless -R is used). Thus, it won&#8217;t reply to clients. Anyways, it is unlikely that mouse-eager clients will spur out in hidden consoles. The clients shipped out with gpm are not updated, thus there are potential security risks when using them. </p>
<h2>Authors</h2>
<pre>Andrew Haylett &lt;ajh [at] gec-mrc.co.uk&gt; (the original selection code)
Ian Zimmerman &lt;itz [at] speakeasy.org&gt; (old maintainer)
Alessandro Rubini &lt;rubini [at] linux.it&gt; (old maintainer (still helps a lot))
Nico Schottelius &lt;nico [at] schottelius.org&gt; (maintainer)
Many many contributors, to both selection and gpm.</pre>
<h2>Maintainers</h2>
<p>The current maintainer is Nico Schottelius. But without the help of Alessandro Rubini and the mailing list it would be impossible for me to maintain gpm. The development mailing list can be reached under gpm [at] lists.linux.it. More information on the list is in the README file part of the source distribution of gpm.</p>
<h2>Files</h2>
<pre>/var/run/gpm.pid The PID of the running gpm
/dev/gpmctl A control socket for clients
/dev/gpmdata The fifo written to by a <code>repeater</code> (`-R') daemon.</pre>
<h2>See Also</h2>
<pre><code> <a href="//www.systutorials.com/docs/linux/man/1-mev/">mev</a>(1)</code> A sample client for the gpm daemon.
<code> <a href="//www.systutorials.com/docs/linux/man/1-gpm-root/">gpm-root</a>(1)</code> An handler for Control-Mouse events.</pre>
<p>The info file about `gpm&#8217;, which gives more complete information and explains how to write a gpm client. </p>
