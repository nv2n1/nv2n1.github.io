---

title: "stty(1)"
name: "stty"
section: "1"
letter: "s"
url: "/docs/linux/man/1-stty/"
description: "stty – change and print terminal line settings"
---

<p> stty &#8211; change and print terminal line settings </p>
<h2>SYNOPSIS</h2>
<p> <code>stty</code> [<i>,-F DEVICE | &#8211;file=DEVICE/</i>] [<i>,SETTING/</i>]&#8230;<br />
 <code>stty</code> [<i>,-F DEVICE | &#8211;file=DEVICE/</i>] [<i>,-a|&#8211;all/</i>]<br />
 <code>stty</code> [<i>,-F DEVICE | &#8211;file=DEVICE/</i>] [<i>,-g|&#8211;save/</i>]</p>
<h2>DESCRIPTION</h2>
<p> Print or change terminal characteristics. </p>
<p> Mandatory arguments to long options are mandatory for short options too.</p>
<dl>
<dt><code>-a</code>, <code>&#8211;all</code></dt>
<dd> print all current settings in human-readable form</dd>
<dt><code>-g</code>, <code>&#8211;save</code></dt>
<dd> print all current settings in a stty-readable form</dd>
<dt><code>-F</code>, <code>&#8211;file</code>=<i>,DEVICE/</i></dt>
<dd> open and use the specified DEVICE instead of stdin</dd>
<dt><code>&#8211;help</code></dt>
<dd> display this help and exit</dd>
<dt><code>&#8211;version</code></dt>
<dd> output version information and exit</dd></dl>
<p> Optional &#8211; before SETTING indicates negation. An * marks non-POSIX settings. The underlying system defines which settings are available.</p>
<h3>Special characters:</h3>
<dl>
<dt>* discard CHAR</dt>
<dd> CHAR will toggle discarding of output</dd>
<dt>eof CHAR</dt>
<dd> CHAR will send an end of file (terminate the input)</dd>
<dt>eol CHAR</dt>
<dd> CHAR will end the line</dd>
<dt>* eol2 CHAR</dt>
<dd> alternate CHAR for ending the line</dd>
<dt>erase CHAR</dt>
<dd> CHAR will erase the last character typed</dd>
<dt>intr CHAR</dt>
<dd> CHAR will send an interrupt signal</dd>
<dt>kill CHAR</dt>
<dd> CHAR will erase the current line</dd>
<dt>* lnext CHAR</dt>
<dd> CHAR will enter the next character quoted</dd>
<dt>quit CHAR</dt>
<dd> CHAR will send a quit signal</dd>
<dt>* rprnt CHAR</dt>
<dd> CHAR will redraw the current line</dd>
<dt>start CHAR</dt>
<dd> CHAR will restart the output after stopping it</dd>
<dt>stop CHAR</dt>
<dd> CHAR will stop the output</dd>
<dt>susp CHAR</dt>
<dd> CHAR will send a terminal stop signal</dd>
<dt>* swtch CHAR</dt>
<dd> CHAR will switch to a different shell layer</dd>
<dt>* werase CHAR</dt>
<dd> CHAR will erase the last word typed</dd></dl>
<h3>Special settings:</h3>
<dl>
<dt>N</dt>
<dd> set the input and output speeds to N bauds</dd>
<dt>* cols N</dt>
<dd> tell the kernel that the terminal has N columns</dd>
<dt>* columns N</dt>
<dd> same as cols N</dd>
<dt>* [-]drain</dt>
<dd> wait for transmission before applying settings (on by default)</dd>
<dt>ispeed N</dt>
<dd> set the input speed to N</dd>
<dt>* line N</dt>
<dd> use line discipline N</dd>
<dt>min N</dt>
<dd> with <code>-icanon</code>, set N characters minimum for a completed read</dd>
<dt>ospeed N</dt>
<dd> set the output speed to N</dd>
<dt>* rows N</dt>
<dd> tell the kernel that the terminal has N rows</dd>
<dt>* size</dt>
<dd> print the number of rows and columns according to the kernel</dd>
<dt>speed</dt>
<dd> print the terminal speed</dd>
<dt>time N</dt>
<dd> with <code>-icanon</code>, set read timeout of N tenths of a second</dd></dl>
<h3>Control settings:</h3>
<dl>
<dt>[-]clocal</dt>
<dd> disable modem control signals</dd>
<dt>[-]cread</dt>
<dd> allow input to be received</dd>
<dt>* [-]crtscts</dt>
<dd> enable RTS/CTS handshaking</dd>
<dt>csN</dt>
<dd> set character size to N bits, N in [5..8]</dd>
<dt>[-]cstopb</dt>
<dd> use two stop bits per character (one with &#8216;-&#8216;)</dd>
<dt>[-]hup</dt>
<dd> send a hangup signal when the last process closes the tty</dd>
<dt>[-]hupcl</dt>
<dd> same as [-]hup</dd>
<dt>[-]parenb</dt>
<dd> generate parity bit in output and expect parity bit in input</dd>
<dt>[-]parodd</dt>
<dd> set odd parity (or even parity with &#8216;-&#8216;)</dd>
<dt>* [-]cmspar</dt>
<dd> use &quot;stick&quot; (mark/space) parity</dd></dl>
<h3>Input settings:</h3>
<dl>
<dt>[-]brkint</dt>
<dd> breaks cause an interrupt signal</dd>
<dt>[-]icrnl</dt>
<dd> translate carriage return to newline</dd>
<dt>[-]ignbrk</dt>
<dd> ignore break characters</dd>
<dt>[-]igncr</dt>
<dd> ignore carriage return</dd>
<dt>[-]ignpar</dt>
<dd> ignore characters with parity errors</dd>
<dt>* [-]imaxbel</dt>
<dd> beep and do not flush a full input buffer on a character</dd>
<dt>[-]inlcr</dt>
<dd> translate newline to carriage return</dd>
<dt>[-]inpck</dt>
<dd> enable input parity checking</dd>
<dt>[-]istrip</dt>
<dd> clear high (8th) bit of input characters</dd>
<dt>* [-]iutf8</dt>
<dd> assume input characters are UTF-8 encoded</dd>
<dt>* [-]iuclc</dt>
<dd> translate uppercase characters to lowercase</dd>
<dt>* [-]ixany</dt>
<dd> let any character restart output, not only start character</dd>
<dt>[-]ixoff</dt>
<dd> enable sending of start/stop characters</dd>
<dt>[-]ixon</dt>
<dd> enable XON/XOFF flow control</dd>
<dt>[-]parmrk</dt>
<dd> mark parity errors (with a 255-0-character sequence)</dd>
<dt>[-]tandem</dt>
<dd> same as [-]ixoff</dd></dl>
<h3>Output settings:</h3>
<dl>
<dt>* bsN</dt>
<dd> backspace delay style, N in [0..1]</dd>
<dt>* crN</dt>
<dd> carriage return delay style, N in [0..3]</dd>
<dt>* ffN</dt>
<dd> form feed delay style, N in [0..1]</dd>
<dt>* nlN</dt>
<dd> newline delay style, N in [0..1]</dd>
<dt>* [-]ocrnl</dt>
<dd> translate carriage return to newline</dd>
<dt>* [-]ofdel</dt>
<dd> use delete characters for fill instead of NUL characters</dd>
<dt>* [-]ofill</dt>
<dd> use fill (padding) characters instead of timing for delays</dd>
<dt>* [-]olcuc</dt>
<dd> translate lowercase characters to uppercase</dd>
<dt>* [-]onlcr</dt>
<dd> translate newline to carriage return-newline</dd>
<dt>* [-]onlret</dt>
<dd> newline performs a carriage return</dd>
<dt>* [-]onocr</dt>
<dd> do not print carriage returns in the first column</dd>
<dt>[-]opost</dt>
<dd> postprocess output</dd>
<dt>* tabN</dt>
<dd> horizontal tab delay style, N in [0..3]</dd>
<dt>* tabs</dt>
<dd> same as tab0</dd>
<dt>* <code>-tabs</code></dt>
<dd> same as tab3</dd>
<dt>* vtN</dt>
<dd> vertical tab delay style, N in [0..1]</dd></dl>
<h3>Local settings:</h3>
<dl>
<dt>[-]crterase</dt>
<dd> echo erase characters as backspace-space-backspace</dd>
<dt>* crtkill</dt>
<dd> kill all line by obeying the echoprt and echoe settings</dd>
<dt>* <code>-crtkill</code></dt>
<dd> kill all line by obeying the echoctl and echok settings</dd>
<dt>* [-]ctlecho</dt>
<dd> echo control characters in hat notation (&#8216;^c&#8217;)</dd>
<dt>[-]echo</dt>
<dd> echo input characters</dd>
<dt>* [-]echoctl</dt>
<dd> same as [-]ctlecho</dd>
<dt>[-]echoe</dt>
<dd> same as [-]crterase</dd>
<dt>[-]echok</dt>
<dd> echo a newline after a kill character</dd>
<dt>* [-]echoke</dt>
<dd> same as [-]crtkill</dd>
<dt>[-]echonl</dt>
<dd> echo newline even if not echoing other characters</dd>
<dt>* [-]echoprt</dt>
<dd> echo erased characters backward, between &#8216;\&#8217; and &#8216;/&#8217;</dd>
<dt>* [-]extproc</dt>
<dd> enable &quot;LINEMODE&quot;; useful with high latency links</dd>
<dt>* [-]flusho</dt>
<dd> discard output</dd>
<dt>[-]icanon</dt>
<dd> enable special characters: erase, kill, werase, rprnt</dd>
<dt>[-]iexten</dt>
<dd> enable non-POSIX special characters</dd>
<dt>[-]isig</dt>
<dd> enable interrupt, quit, and suspend special characters</dd>
<dt>[-]noflsh</dt>
<dd> disable flushing after interrupt and quit special characters</dd>
<dt>* [-]prterase</dt>
<dd> same as [-]echoprt</dd>
<dt>* [-]tostop</dt>
<dd> stop background jobs that try to write to the terminal</dd>
<dt>* [-]xcase</dt>
<dd> with icanon, escape with &#8216;\&#8217; for uppercase characters</dd></dl>
<h3>Combination settings:</h3>
<dl>
<dt>* [-]LCASE</dt>
<dd> same as [-]lcase</dd>
<dt>cbreak</dt>
<dd> same as <code>-icanon</code></dd>
<dt><code>-cbreak</code></dt>
<dd> same as icanon</dd>
<dt>cooked</dt>
<dd> same as brkint ignpar istrip icrnl ixon opost isig icanon, eof and eol characters to their default values</dd>
<dt><code>-cooked</code></dt>
<dd> same as raw</dd>
<dt>crt</dt>
<dd> same as echoe echoctl echoke</dd>
<dt>dec</dt>
<dd> same as echoe echoctl echoke <code>-ixany</code> intr ^c erase 0177 kill ^u</dd>
<dt>* [-]decctlq</dt>
<dd> same as [-]ixany</dd>
<dt>ek</dt>
<dd> erase and kill characters to their default values</dd>
<dt>evenp</dt>
<dd> same as parenb <code>-parodd</code> cs7</dd>
<dt><code>-evenp</code></dt>
<dd> same as <code>-parenb</code> cs8</dd>
<dt>* [-]lcase</dt>
<dd> same as xcase iuclc olcuc</dd>
<dt>litout</dt>
<dd> same as <code>-parenb</code> <code>-istrip</code> <code>-opost</code> cs8</dd>
<dt><code>-litout</code></dt>
<dd> same as parenb istrip opost cs7</dd>
<dt>nl</dt>
<dd> same as <code>-icrnl</code> <code>-onlcr</code></dd>
<dt><code>-nl</code></dt>
<dd> same as icrnl <code>-inlcr</code> <code>-igncr</code> onlcr <code>-ocrnl</code> <code>-onlret</code></dd>
<dt>oddp</dt>
<dd> same as parenb parodd cs7</dd>
<dt><code>-oddp</code></dt>
<dd> same as <code>-parenb</code> cs8</dd>
<dt>[-]parity</dt>
<dd> same as [-]evenp</dd>
<dt>pass8</dt>
<dd> same as <code>-parenb</code> <code>-istrip</code> cs8</dd>
<dt><code>-pass8</code></dt>
<dd> same as parenb istrip cs7</dd>
<dt>raw</dt>
<dd> same as <code>-ignbrk</code> <code>-brkint</code> <code>-ignpar</code> <code>-parmrk</code> <code>-inpck</code> <code>-istrip</code> <code>-inlcr</code> <code>-igncr</code> <code>-icrnl</code> <code>-ixon</code> <code>-ixoff</code> <code>-icanon</code> <code>-opost</code> <code>-isig</code> <code>-iuclc</code> <code>-ixany</code> <code>-imaxbel</code> <code>-xcase</code> min 1 time 0</dd>
<dt><code>-raw</code></dt>
<dd> same as cooked</dd>
<dt>sane</dt>
<dd> same as cread <code>-ignbrk</code> brkint <code>-inlcr</code> <code>-igncr</code> icrnl icanon iexten echo echoe echok <code>-echonl</code> <code>-noflsh</code> <code>-ixoff</code> <code>-iutf8</code> <code>-iuclc</code> <code>-ixany</code> imaxbel <code>-xcase</code> <code>-olcuc</code> <code>-ocrnl</code> opost <code>-ofill</code> onlcr <code>-onocr</code> <code>-onlret</code> nl0 cr0 tab0 bs0 vt0 ff0 isig <code>-tostop</code> <code>-ofdel</code> <code>-echoprt</code> echoctl echoke <code>-extproc</code> <code>-flusho</code>, all special characters to their default values</dd></dl>
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
