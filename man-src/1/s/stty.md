---
title: "stty(1)"
name: "stty"
section: "1"
letter: "s"
url: "/docs/linux/man/1-stty/"
description: "stty – change and print terminal line settings"
---

<h2 class="name">NAME</h2>
<p> stty &#8211; change and print terminal line settings </p>
<h2>SYNOPSIS</h2>
<p> <code>stty</code> [<i>,-F DEVICE | &#8211;file=DEVICE/</i>] [<i>,SETTING/</i>]&#8230;<br />
 <code>stty</code> [<i>,-F DEVICE | &#8211;file=DEVICE/</i>] [<i>,-a|&#8211;all/</i>]<br />
 <code>stty</code> [<i>,-F DEVICE | &#8211;file=DEVICE/</i>] [<i>,-g|&#8211;save/</i>]</p>
<h2>DESCRIPTION</h2>
<p> Print or change terminal characteristics. </p>
<p> Mandatory arguments to long options are mandatory for short options too.</p>
<dl>
<dt><code>-a</code>, <code>&#8211;all</code></p>
<dd> print all current settings in human-readable form</p>
<dt><code>-g</code>, <code>&#8211;save</code></p>
<dd> print all current settings in a stty-readable form</p>
<dt><code>-F</code>, <code>&#8211;file</code>=<i>,DEVICE/</i></p>
<dd> open and use the specified DEVICE instead of stdin</p>
<dt><code>&#8211;help</code></p>
<dd> display this help and exit</p>
<dt><code>&#8211;version</code></p>
<dd> output version information and exit</dl>
<p> Optional &#8211; before SETTING indicates negation. An * marks non-POSIX settings. The underlying system defines which settings are available.</p>
<h3>Special characters:</h3>
<dl>
<dt>* discard CHAR</p>
<dd> CHAR will toggle discarding of output</p>
<dt>eof CHAR</p>
<dd> CHAR will send an end of file (terminate the input)</p>
<dt>eol CHAR</p>
<dd> CHAR will end the line</p>
<dt>* eol2 CHAR</p>
<dd> alternate CHAR for ending the line</p>
<dt>erase CHAR</p>
<dd> CHAR will erase the last character typed</p>
<dt>intr CHAR</p>
<dd> CHAR will send an interrupt signal</p>
<dt>kill CHAR</p>
<dd> CHAR will erase the current line</p>
<dt>* lnext CHAR</p>
<dd> CHAR will enter the next character quoted</p>
<dt>quit CHAR</p>
<dd> CHAR will send a quit signal</p>
<dt>* rprnt CHAR</p>
<dd> CHAR will redraw the current line</p>
<dt>start CHAR</p>
<dd> CHAR will restart the output after stopping it</p>
<dt>stop CHAR</p>
<dd> CHAR will stop the output</p>
<dt>susp CHAR</p>
<dd> CHAR will send a terminal stop signal</p>
<dt>* swtch CHAR</p>
<dd> CHAR will switch to a different shell layer</p>
<dt>* werase CHAR</p>
<dd> CHAR will erase the last word typed</dl>
<h3>Special settings:</h3>
<dl>
<dt>N</p>
<dd> set the input and output speeds to N bauds</p>
<dt>* cols N</p>
<dd> tell the kernel that the terminal has N columns</p>
<dt>* columns N</p>
<dd> same as cols N</p>
<dt>* [-]drain</p>
<dd> wait for transmission before applying settings (on by default)</p>
<dt>ispeed N</p>
<dd> set the input speed to N</p>
<dt>* line N</p>
<dd> use line discipline N</p>
<dt>min N</p>
<dd> with <code>-icanon</code>, set N characters minimum for a completed read</p>
<dt>ospeed N</p>
<dd> set the output speed to N</p>
<dt>* rows N</p>
<dd> tell the kernel that the terminal has N rows</p>
<dt>* size</p>
<dd> print the number of rows and columns according to the kernel</p>
<dt>speed</p>
<dd> print the terminal speed</p>
<dt>time N</p>
<dd> with <code>-icanon</code>, set read timeout of N tenths of a second</dl>
<h3>Control settings:</h3>
<dl>
<dt>[-]clocal</p>
<dd> disable modem control signals</p>
<dt>[-]cread</p>
<dd> allow input to be received</p>
<dt>* [-]crtscts</p>
<dd> enable RTS/CTS handshaking</p>
<dt>csN</p>
<dd> set character size to N bits, N in [5..8]</p>
<dt>[-]cstopb</p>
<dd> use two stop bits per character (one with &#8216;-&#8216;)</p>
<dt>[-]hup</p>
<dd> send a hangup signal when the last process closes the tty</p>
<dt>[-]hupcl</p>
<dd> same as [-]hup</p>
<dt>[-]parenb</p>
<dd> generate parity bit in output and expect parity bit in input</p>
<dt>[-]parodd</p>
<dd> set odd parity (or even parity with &#8216;-&#8216;)</p>
<dt>* [-]cmspar</p>
<dd> use &quot;stick&quot; (mark/space) parity</dl>
<h3>Input settings:</h3>
<dl>
<dt>[-]brkint</p>
<dd> breaks cause an interrupt signal</p>
<dt>[-]icrnl</p>
<dd> translate carriage return to newline</p>
<dt>[-]ignbrk</p>
<dd> ignore break characters</p>
<dt>[-]igncr</p>
<dd> ignore carriage return</p>
<dt>[-]ignpar</p>
<dd> ignore characters with parity errors</p>
<dt>* [-]imaxbel</p>
<dd> beep and do not flush a full input buffer on a character</p>
<dt>[-]inlcr</p>
<dd> translate newline to carriage return</p>
<dt>[-]inpck</p>
<dd> enable input parity checking</p>
<dt>[-]istrip</p>
<dd> clear high (8th) bit of input characters</p>
<dt>* [-]iutf8</p>
<dd> assume input characters are UTF-8 encoded</p>
<dt>* [-]iuclc</p>
<dd> translate uppercase characters to lowercase</p>
<dt>* [-]ixany</p>
<dd> let any character restart output, not only start character</p>
<dt>[-]ixoff</p>
<dd> enable sending of start/stop characters</p>
<dt>[-]ixon</p>
<dd> enable XON/XOFF flow control</p>
<dt>[-]parmrk</p>
<dd> mark parity errors (with a 255-0-character sequence)</p>
<dt>[-]tandem</p>
<dd> same as [-]ixoff</dl>
<h3>Output settings:</h3>
<dl>
<dt>* bsN</p>
<dd> backspace delay style, N in [0..1]</p>
<dt>* crN</p>
<dd> carriage return delay style, N in [0..3]</p>
<dt>* ffN</p>
<dd> form feed delay style, N in [0..1]</p>
<dt>* nlN</p>
<dd> newline delay style, N in [0..1]</p>
<dt>* [-]ocrnl</p>
<dd> translate carriage return to newline</p>
<dt>* [-]ofdel</p>
<dd> use delete characters for fill instead of NUL characters</p>
<dt>* [-]ofill</p>
<dd> use fill (padding) characters instead of timing for delays</p>
<dt>* [-]olcuc</p>
<dd> translate lowercase characters to uppercase</p>
<dt>* [-]onlcr</p>
<dd> translate newline to carriage return-newline</p>
<dt>* [-]onlret</p>
<dd> newline performs a carriage return</p>
<dt>* [-]onocr</p>
<dd> do not print carriage returns in the first column</p>
<dt>[-]opost</p>
<dd> postprocess output</p>
<dt>* tabN</p>
<dd> horizontal tab delay style, N in [0..3]</p>
<dt>* tabs</p>
<dd> same as tab0</p>
<dt>* <code>-tabs</code></p>
<dd> same as tab3</p>
<dt>* vtN</p>
<dd> vertical tab delay style, N in [0..1]</dl>
<h3>Local settings:</h3>
<dl>
<dt>[-]crterase</p>
<dd> echo erase characters as backspace-space-backspace</p>
<dt>* crtkill</p>
<dd> kill all line by obeying the echoprt and echoe settings</p>
<dt>* <code>-crtkill</code></p>
<dd> kill all line by obeying the echoctl and echok settings</p>
<dt>* [-]ctlecho</p>
<dd> echo control characters in hat notation (&#8216;^c&#8217;)</p>
<dt>[-]echo</p>
<dd> echo input characters</p>
<dt>* [-]echoctl</p>
<dd> same as [-]ctlecho</p>
<dt>[-]echoe</p>
<dd> same as [-]crterase</p>
<dt>[-]echok</p>
<dd> echo a newline after a kill character</p>
<dt>* [-]echoke</p>
<dd> same as [-]crtkill</p>
<dt>[-]echonl</p>
<dd> echo newline even if not echoing other characters</p>
<dt>* [-]echoprt</p>
<dd> echo erased characters backward, between &#8216;\&#8217; and &#8216;/&#8217;</p>
<dt>* [-]extproc</p>
<dd> enable &quot;LINEMODE&quot;; useful with high latency links</p>
<dt>* [-]flusho</p>
<dd> discard output</p>
<dt>[-]icanon</p>
<dd> enable special characters: erase, kill, werase, rprnt</p>
<dt>[-]iexten</p>
<dd> enable non-POSIX special characters</p>
<dt>[-]isig</p>
<dd> enable interrupt, quit, and suspend special characters</p>
<dt>[-]noflsh</p>
<dd> disable flushing after interrupt and quit special characters</p>
<dt>* [-]prterase</p>
<dd> same as [-]echoprt</p>
<dt>* [-]tostop</p>
<dd> stop background jobs that try to write to the terminal</p>
<dt>* [-]xcase</p>
<dd> with icanon, escape with &#8216;\&#8217; for uppercase characters</dl>
<h3>Combination settings:</h3>
<dl>
<dt>* [-]LCASE</p>
<dd> same as [-]lcase</p>
<dt>cbreak</p>
<dd> same as <code>-icanon</code></p>
<dt><code>-cbreak</code></p>
<dd> same as icanon</p>
<dt>cooked</p>
<dd> same as brkint ignpar istrip icrnl ixon opost isig icanon, eof and eol characters to their default values</p>
<dt><code>-cooked</code></p>
<dd> same as raw</p>
<dt>crt</p>
<dd> same as echoe echoctl echoke</p>
<dt>dec</p>
<dd> same as echoe echoctl echoke <code>-ixany</code> intr ^c erase 0177 kill ^u</p>
<dt>* [-]decctlq</p>
<dd> same as [-]ixany</p>
<dt>ek</p>
<dd> erase and kill characters to their default values</p>
<dt>evenp</p>
<dd> same as parenb <code>-parodd</code> cs7</p>
<dt><code>-evenp</code></p>
<dd> same as <code>-parenb</code> cs8</p>
<dt>* [-]lcase</p>
<dd> same as xcase iuclc olcuc</p>
<dt>litout</p>
<dd> same as <code>-parenb</code> <code>-istrip</code> <code>-opost</code> cs8</p>
<dt><code>-litout</code></p>
<dd> same as parenb istrip opost cs7</p>
<dt>nl</p>
<dd> same as <code>-icrnl</code> <code>-onlcr</code></p>
<dt><code>-nl</code></p>
<dd> same as icrnl <code>-inlcr</code> <code>-igncr</code> onlcr <code>-ocrnl</code> <code>-onlret</code></p>
<dt>oddp</p>
<dd> same as parenb parodd cs7</p>
<dt><code>-oddp</code></p>
<dd> same as <code>-parenb</code> cs8</p>
<dt>[-]parity</p>
<dd> same as [-]evenp</p>
<dt>pass8</p>
<dd> same as <code>-parenb</code> <code>-istrip</code> cs8</p>
<dt><code>-pass8</code></p>
<dd> same as parenb istrip cs7</p>
<dt>raw</p>
<dd> same as <code>-ignbrk</code> <code>-brkint</code> <code>-ignpar</code> <code>-parmrk</code> <code>-inpck</code> <code>-istrip</code> <code>-inlcr</code> <code>-igncr</code> <code>-icrnl</code> <code>-ixon</code> <code>-ixoff</code> <code>-icanon</code> <code>-opost</code> <code>-isig</code> <code>-iuclc</code> <code>-ixany</code> <code>-imaxbel</code> <code>-xcase</code> min 1 time 0</p>
<dt><code>-raw</code></p>
<dd> same as cooked</p>
<dt>sane</p>
<dd> same as cread <code>-ignbrk</code> brkint <code>-inlcr</code> <code>-igncr</code> icrnl icanon iexten echo echoe echok <code>-echonl</code> <code>-noflsh</code> <code>-ixoff</code> <code>-iutf8</code> <code>-iuclc</code> <code>-ixany</code> imaxbel <code>-xcase</code> <code>-olcuc</code> <code>-ocrnl</code> opost <code>-ofill</code> onlcr <code>-onocr</code> <code>-onlret</code> nl0 cr0 tab0 bs0 vt0 ff0 isig <code>-tostop</code> <code>-ofdel</code> <code>-echoprt</code> echoctl echoke <code>-extproc</code> <code>-flusho</code>, all special characters to their default values</dl>
<p> Handle the tty line connected to standard input. Without arguments, prints baud rate, line discipline, and deviations from stty sane. In settings, CHAR is taken literally, or coded as in ^c, 0x37, 0177 or 127; special values ^- or undef used to disable special characters.</p>
<h2>AUTHOR</h2>
<p> Written by David MacKenzie.</p>
<h2>REPORTING BUGS</h2>
<p> GNU coreutils online help: &lt;<a rel="nofollow" href="https://www.gnu.org/software/coreutils/">https://www.gnu.org/software/coreutils/</a>&gt;<br />
 Report any translation bugs to &lt;<a rel="nofollow" href="https://translationproject.org/team/">https://translationproject.org/team/</a>&gt;</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2020 Free Software Foundation, Inc. License GPLv3+: GNU GPL version 3 or later &lt;<a rel="nofollow" href="https://gnu.org/licenses/gpl.html">https://gnu.org/licenses/gpl.html</a>&gt;.<br />
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.</p>
<h2>SEE ALSO</h2>
<p> Full documentation &lt;<a rel="nofollow" href="https://www.gnu.org/software/coreutils/stty">https://www.gnu.org/software/coreutils/stty</a>&gt;<br />
 or available locally via: info &#8216;(coreutils) stty invocation&#8217; </p>
<h2>Index</h2>
