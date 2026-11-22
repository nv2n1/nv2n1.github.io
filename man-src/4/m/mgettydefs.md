---

title: "mgettydefs(4)"
name: "mgettydefs"
section: "4"
letter: "m"
url: "/docs/linux/man/4-mgettydefs/"
description: "mgettydefs – speed and terminal settings used by mgetty"
---

<p>mgettydefs &#8211; speed and terminal settings used by mgetty </p>

<p> The <code>/etc/gettydefs</code> file contains information used by <i>mgetty</i>(1) to set up the speed and terminal settings for a line. It also supplies information on what the <i>login</i> prompt should look like. </p>
<p>Many versions of UNIX have a version of <i>getty</i>(1) that also reads <code>/etc/gettydefs</code>. Both <i>mgetty</i> and <i>getty</i> expect similar formats in <code>/etc/gettydefs</code> except that, when used by <i>mgetty</i>, extended functionality is available. Even so, the additional functions are simply ignored by standard <i>getty</i>, so they can co-exist using the same file. Note, however, that <i>mgetty</i> can be compiled to use a file different from <code>/etc/gettydefs </code> if your <i>getty</i> gets upset about the extensions. This manual page documents <code>/etc/gettydefs</code> and describes the extended functionality available when used by <i>mgetty</i>(1). This document will refer to <i>getty</i>(1) except where <i>mgetty</i>&#8216;s behaviour is different. </p>
<p>Each entry in <code>/etc/gettydefs</code> has the following format: </p>
<dl>
<dd> <p> label# initial-flags # final-flags # login-prompt #next-label </p>
 </dd></dl>
<p>Each entry is followed by a blank line. The login prompt field can contain quoted characters which will be converted to other values. The sequences and their substitutions are: </p>
<dl>
<dt><code>\n</code></dt>
<dd> <p> newline </p>
 </dd>
<dt><code>\r</code></dt>
<dd> <p> carriage return </p>
 </dd>
<dt><code>\g</code></dt>
<dd> <p> beep </p>
 </dd>
<dt><code>\b</code></dt>
<dd> <p> backspace </p>
 </dd>
<dt><code>\v</code></dt>
<dd> <p> vertical tab (VT) </p>
 </dd>
<dt><code>\f</code></dt>
<dd> <p> formfeed </p>
 </dd>
<dt><code>\t</code></dt>
<dd> <p> tab </p>
 </dd>
<dt><code>\L</code></dt>
<dd> <p> portname </p>
 </dd>
<dt><code>\C</code></dt>
<dd> <p> time in <i><a href="/docs/linux/man/3-ctime/">ctime</a></i>(3) format. </p>
 </dd>
<dt><code>\N</code></dt>
<dd> <p> number of users currently logged in </p>
 </dd>
<dt><code>\U</code></dt>
<dd> <p> number of users currently logged in </p>
 </dd>
<dt><code>\D</code></dt>
<dd> <p> date in DD/MM format </p>
 </dd>
<dt><code>\T</code></dt>
<dd> <p> time in hh:mm:ss format </p>
 </dd>
<dt><code>\I</code></dt>
<dd> <p> modem CONNECT attributes </p>
 </dd>
<dt><code>\sequence</code></dt>
<dd> <p> where &quot;sequence&quot; is a valid strtol format, such as: \0nnn (octal), \0xnnn (hex), or \nnn (decimal). </p>
 </dd></dl>
<p>Note that standard <i>getty</i> usually only supports \b, \r and \n. </p>
<p>The various fields are: </p>
<dl>
<dt><i>label</i></dt>
<dd> <p> This is the string against which <i>getty</i> tries to match its second argument. It is often the speed, such as <code>1200</code>, at which the terminal is supposed to run, but it need not be (see below). </p>
 </dd>
<dt><i>initial-flags</i></dt>
<dd> <p> These flags are the initial <i><a href="/docs/linux/man/2-ioctl/">ioctl</a></i>(2) settings to which the terminal is to be set if a terminal type is not specified to <i>getty</i>. The flags that <i>getty</i> understands are the ones listed in <i><a href="/docs/linux/man/7-termio/">termio</a></i>(7)). <i>mgetty</i> is usually compiled for <i>termios</i>(7) and often has a more complete set than <i>getty</i>. </p>
 </dd>
<dt>Normally only the speed flag is required in the</dt>
<dd> <p> <i>initial-flags</i>. <i>getty</i> automatically sets the terminal to raw input mode and takes care of the other flags. If the &quot;-s&quot; option is used with <i>mgetty</i>(1) the speed setting is ignored. The <i>initial-flag</i> settings remain in effect until <i>getty</i> executes <i><a href="/docs/linux/man/1-login/">login</a></i>(1). </p>
 </dd>
<dt><i>final-flags</i></dt>
<dd> <p> These flags take the same values as the <i>initial-flags</i> and are set just before <i>getty</i> executes <i>login</i>. The speed flag is again required, except with <i>mgetty</i> if the -s flag was supplied. Two other commonly specified <i>final-flags</i> are <code>TAB3</code>,  so that tabs are sent to the terminal as spaces, and <code>HUPCL</code>,  so that the line is hung up on the final close. </p>
 </dd>
<dt><i>login-prompt</i></dt>
<dd> <p> This entire field is printed as the <i>login-prompt</i>. Unlike the above fields where white space (a space, tab or new-line) is ignored, they are included in the <i>login-prompt</i> field. This field is ignored if the &quot;-p&quot; option has been specified to <i>mgetty</i>(1). </p>
 </dd>
<dt><i>next-label</i></dt>
<dd> <p> specifies the label to use if the user user types a <i>&lt;break&gt;</i> character, or <i>getty</i> detects a reception error. <i>Getty</i> searches for the entry with <i>next-label</i> as its <i>label</i> field and set up the terminal for those settings. Usually, a series of speeds are linked together in this fashion, into a closed set; for instance, <code>2400</code> linked to <code>1200</code>, which in turn is linked to <code>300</code>, which finally is linked to <code>2400</code>. <i>next-label</i> is ignored with <i>mgetty</i>(1). </p>
 </dd></dl>
<p>Several additional composite settings are available for <i>initial-flags</i> and <i>final-flags</i>. The following composite flags are supported by <i>mgetty</i> and are usually supported by <i>getty</i>: </p>
<dl>
<dt><code>SANE</code></dt>
<dd> <p> equivalent to ``stty sane&#8217;&#8216;. (BRKINT, IGNPAR, ISTRIP, ICRNL, IXON, OPOST, CS8, CREAD, ISIG, ICANON, ECHO, ECHOK) </p>
 </dd>
<dt><code>ODDP</code></dt>
<dd> <p> Odd parity (CS7, PARENB, PARODD) </p>
 </dd>
<dt><code>PARITY</code>,<code>EVENP</code></dt>
<dd> <p> even parity (CS7, PARENB) </p>
 </dd>
<dt><code>-ODDP</code>,<code>-PARITY</code>,<code>-EVENP</code></dt>
<dd> <p> no parity (resets PARENB, PARODD, and sets CS8) </p>
 </dd>
<dt><code>RAW</code></dt>
<dd> <p> raw I/O (no canonical processing) (turns off OPOST, ICANON) </p>
 </dd>
<dt><code>-RAW</code>,<code>COOKED</code></dt>
<dd> <p> enable canonical processing (turns on OPOST, ICANON) </p>
 </dd>
<dt><code>NL</code></dt>
<dd> <p> Ignore newlines. (ICRNL, ONLCR) </p>
 </dd>
<dt><code>-NL</code></dt>
<dd> <p> Respect newlines (turns INLCR, IGNCR, ICRNL, ONLCR, OCRNL, ONLRET off) </p>
 </dd>
<dt><code>LCASE</code></dt>
<dd> <p> Ignore case - treat all as lowercase. (IUCLC, OLCUC, XCASE) Is set if mgetty believes login is entirely uppercase. </p>
 </dd>
<dt><code>-LCASE</code></dt>
<dd> <p> Repect case (turns off IUCLC, OLCUC and XCASE) </p>
 </dd>
<dt><code>TABS</code></dt>
<dd> <p> output tabs as tabs </p>
 </dd>
<dt><code>-TABS</code>,<code>TAB3</code></dt>
<dd> <p> output tabs as spaces </p>
 </dd>
<dt><code>EK</code></dt>
<dd> <p> Sets VERASE to &quot;#&quot; and VKILL to CKILL respectively. (note that while many gettys default VERASE to &quot;#&quot;. <i>mgetty</i> defaults VERASE to backspace.) </p>
 </dd></dl>
<p>Additionally, <i>mgetty</i> (but not <i>getty</i>) can set any of the control characters listed in the <code>c_cc</code> termio(termios) structure by the use of two tokens: </p>
<p>&lt;character name&gt; &lt;value&gt; </p>
<p>Eg: </p>
<p>VERASE ^h </p>
<p>The value can be set as ``^&lt;character&gt;&#8216;&#8216;, ``\nnn&#8217;&#8216; or ``\&lt;character&gt;&#8216;&#8216; (normal UNIX \ escapes). </p>
<p>See the <i><a href="/docs/linux/man/7-termio/">termio</a></i>(7) or <i>termios</i>(7) manual pages to a list of which ``V&#8217;&#8216; variables can be changed. Note that many of these can be changed in the c_cc array, but won&#8217;t have any effect. </p>
<p>If <i>getty</i> is called without a second argument, the first entry of <code>/etc/gettydefs</code> is used by <i>getty</i>, thus making the first entry of <code>/etc/gettydefs</code> the default entry. It is also used if <i>getty</i> cannot find the specified <i>label</i>. <i>Mgetty</i> use a default label of ``n&#8217;&#8216;, but this can be changed in the configuration. If <code>/etc/gettydefs</code> itself is missing, there is one entry built into the command which brings up a terminal at <code>300</code> (configuration parameter in <i>mgetty</i>) baud. </p>
<p>It is strongly recommended that after making or modifying <code>/etc/gettydefs</code>, it be run through <i>getty</i> with the check option to be sure there are no errors.  </p>
<h2>EXAMPLES</h2>
<p> The following two lines show an example of 300/1200 baud toggle, which is useful for dial-up ports: </p>
<dl>
<dd> <p> 1200# B1200 HUPCL # B1200 SANE IXANY TAB3 #login: #300 <br/>
 300# B300 HUPCL # B300 SANE IXANY TAB3 #login: #1200 </p>
 </dd></dl>
<p>The following line shows a typical 9600 baud entry for a hard-wired connection (not currently supported for <i>mgetty</i>): </p>
<dl>
<dd> <p> 9600# B9600 # B9600 SANE IXANY IXANY ECHOE TAB3 #login: #9600 </p>
 </dd></dl>
<p>The following line is a typical smart-modem setup, suitable for <i>mgetty</i>: </p>
<dl>
<dd> <pre><code>19200mg#
    B19200 #
    B19200 SANE VERASE \b VINTR \003 HUPCL #
    \n\D \T \N Users @!login: #19200mg
</code></pre>
 </dd></dl>
<h2>FILES</h2>
<p> /etc/gettydefs  </p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/8-mgetty/">mgetty</a>(8), <a href="/docs/linux/man/8-getty/">getty</a>(8), <a href="/docs/linux/man/1-login/">login</a>(1), <a href="/docs/linux/man/2-ioctl/">ioctl</a>(2), <a href="/docs/linux/man/7-termio/">termio</a>(7), termios(7). </p>
