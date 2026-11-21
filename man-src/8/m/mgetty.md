---

title: "mgetty(8)"
name: "mgetty"
section: "8"
letter: "m"
url: "/docs/linux/man/8-mgetty/"
description: "mgetty – smart modem getty"
---

<p>mgetty &#8211; smart modem getty </p>
<p> <code>mgetty</code> [<code>options</code>] ttydevice [<i>gettydefs</i>]  </p>
<p> Mgetty is a ``smart&#8217;&#8216; getty replacement, designed for use with Hayes compatible data and data/fax modems. Mgetty knows about modem initialization, manual modem answering (so your modem doesn&#8217;t answer if the machine isn&#8217;t ready), UUCP locking (so you can use the same device for dial-in and dial-out). Mgetty provides very extensive logging facilities. </p>
<p>This manpage doesn&#8217;t try to detail mgetty setup in detail, it just lists the most important options. For detailed instructions, see the info file mgetty.info (mgetty.texi). </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-k &lt;space&gt;</code></dt>
<dd> <p> Tells <i>mgetty</i> to leave &lt;space&gt; kbytes free on disk when receiving a fax. </p>
 </dd>
<dt><code>-x &lt;debug level&gt;</code></dt>
<dd> <p> Use the given level of verbosity for logging - 0 means no logging, 9 is really noisy. The log file is usually /tmp/log_mg.&lt;device&gt; </p>
 </dd>
<dt><code>-s &lt;speed&gt;</code></dt>
<dd> <p> Set the port speed to use, e.g. &quot;-s 19200&quot;. </p>
 </dd>
<dt><code>-r</code></dt>
<dd> <p> Tells <i>mgetty</i> that it is running on a direct line. UUCP locking is done, but no modem initialization whatsoever. </p>
 </dd>
<dt><code>-p &lt;login prompt&gt;</code></dt>
<dd> <p> Use the given string to prompt users for their login names. Various tokens are allowed in this string. These tokens are: @ for the system name, \n, \g, \f, for newline, bell, and form feed, respectively. \v and \r will expand to the OS version and release. \P, \l and \L will expand to the tty name (&quot;ttyS0&quot;). \Y will give the Caller ID, \I the &quot;CONNECT foobar&quot; string returned by the modem, and \S or \b will output the port speed. \N and \U give the number of users currently logged in. \C will be changed into the result of ctime(), and \D or \d and \t or \T will output the date and time, respectively. Finally, \&lt;digit&gt; will use digit as octal/decimal/hexadecimal representation of the character to follow. </p>
<p>The default prompt is specified at compile time. </p>
 </dd>
<dt><code>-n #</code></dt>
<dd> <p> Tells <i>mgetty</i> to pick up the phone after the #th RING. Default is 1. </p>
 </dd>
<dt><code>-R &lt;t&gt;</code></dt>
<dd> <p> Tells <i>mgetty</i> to go into &quot;ringback&quot; (aka &quot;ring-twice&quot;) mode. That means: the first call is never answered, instead the caller has to hang up after the phone RINGs, wait 30 seconds, and then call again in the next &lt;t&gt; seconds for mgetty to pick up. If no call comes, mgetty will exit. </p>
<p>I do not really recommend using this, better get a second phone line for the modem. </p>
 </dd>
<dt><code>-i &lt;issue file&gt;</code></dt>
<dd> <p> Output &lt;issue file&gt; instead of /etc/issue before prompting for the user name. The same token substitutions as for the the login prompt are done in this file. </p>
 </dd>
<dt><code>-D</code></dt>
<dd> <p> Tells <i>mgetty</i> that the modem is to be treated as a DATA modem, no fax initialization is attempted. </p>
 </dd>
<dt><code>-F</code></dt>
<dd> <p> Tells <i>mgetty</i> that DATA calls are not allowed and the modem should be set to Fax-Only. </p>
 </dd>
<dt><code>-C &lt;class&gt;</code></dt>
<dd> <p> Tells <i>mgetty</i> how to treat the modem. Possible values for &lt;class&gt; are &quot;auto&quot; (default, try to find out whether the modem supports fax), &quot;cls2&quot; (use the class 2 fax command set, even if the modem supports class 2.0), &quot;c2.0&quot; (use the class 2.0 fax command set), &quot;data&quot; (data only, exactly as the -D switch). </p>
 </dd>
<dt><code>-S &lt;g3 file&gt;</code></dt>
<dd> <p> If a call comes in and requests fax polling, <i>mgetty</i> will send the named file. Note: not all fax modems support poll sending. </p>
 </dd>
<dt><code>-I &lt;fax id&gt;</code></dt>
<dd> <p> Use the given fax station ID for fax identification. Not used for data modems. </p>
 </dd>
<dt><code>-b</code></dt>
<dd> <p> Open the port in blocking mode. Best used in combination with &quot;-r&quot;. This is the default if <i>mgetty</i> is called as <i>getty.</i> You may want to use this if you want to use the two-device / kernel-locking scheme of the Linux and SunOS operating systems (/dev/ttyS.. and /dev/cua..). I do not recommend it, it&#8217;s just included for completeness, and to be able to use mgetty as a full-featured getty replacement. </p>
 </dd>
<dt><code>-a</code></dt>
<dd> <p> Use autobauding. That is, after a connection is made, <i>mgetty</i> parses the &quot;CONNECT foo&quot; response code of the modem and sets the port speed to the first integer found after the &quot;CONNECT&quot; string, &quot;foo&quot; in this example. You need this if your modem insist on changing its DTE speed to match the line speed. I recommend against using it, better leave the port speed locked at a fixed value. The feature is included because old modems exist which cannot use a fixed (locked) port speed. </p>
 </dd>
<dt><code>-m &#8216;expect send ...&#8216;</code></dt>
<dd> <p> Set the &quot;chat sequence&quot; used to initialize the modem. For an empty expect part, use empty double quotes (&quot;&quot;). Since the sequence contains spaces, you have to enclose all of it in single quotes(&#8216;&#8216;). Example: </p>
<p>mgetty -m &#8216;&quot;&quot; ATH0 OK&#8217; </p>
 </dd></dl>
<h2>FILES</h2>
<dl>
<dt><code>/etc/mgetty+sendfax/mgetty.config</code></dt>
<dd> <p> Main configuration file. </p>
 </dd>
<dt><code>/etc/mgetty+sendfax/login.config</code></dt>
<dd> <p> controls whether (and when) <i>mgetty</i> should call some other program for user login instead of /bin/login. How this is done is explained in this file. </p>
 </dd>
<dt><code>/etc/mgetty+sendfax/dialin.config</code></dt>
<dd> <p> controls acceptance/denial of incoming calls based on the caller&#8217;s number. Available only if you have &quot;caller ID&quot; and your modem supports it. </p>
 </dd>
<dt><code>/etc/nologin.ttyxx</code></dt>
<dd> <p> controls whether mgetty should pick up the phone upon incoming calls. If the file exists, calls are completely ignored. You can use this, for example, to stop mgetty during day time, and let it pick up at night only, by creating and removing /etc/nologin.ttyxx via the <i>cron</i> program at the appropriate time. </p>
 </dd>
<dt><code>/etc/issue</code></dt>
<dd> <p> will be printed after a connection is established, and before the with the &#8216;-i&#8217; option. </p>
 </dd>
<dt><code>/var/log/mgetty.ttyxx.log</code></dt>
<dd> <p> Debug log file, see below. </p>
 </dd></dl>
<h2>DIAGNOSTICS</h2>
<p> If <i>mgetty</i> doesn&#8217;t work the way it should, the main source of diagnostic data is the <i>log file.</i> It can be found in &quot;/var/log/mgetty.ttyxx.log&quot; (for the mgetty process handling &quot;ttyxx&quot;). If it doesn&#8217;t contain enough details, enhance the log level with the &#8216;-x&#8217; option to mgetty, e.g. &quot;-x 5&quot;. </p>
<p>Many of the common problems and solutions are discussed in the mgetty manual and the FAQ. Please see the WWW page at <a rel="nofollow" href="http://alpha.greenie.net/mgetty/">http://alpha.greenie.net/mgetty/</a> for both. </p>
<h2>BUGS</h2>
<p> Not all of <i>mgetty</i> configuration can be done at run-time yet. Things like flow control and file paths (log file / lock file) must be configured by changing the source and recompiling. </p>
<p>Users never read manuals... </p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-g32pbm/">g32pbm</a>(1), <a href="/docs/linux/man/8-sendfax/">sendfax</a>(8), <a href="/docs/linux/man/8-getty/">getty</a>(8), <a href="/docs/linux/man/4-mgettydefs/">mgettydefs</a>(4), mgetty.info  </p>
<h2>AUTHOR</h2>
<p> <i>mgetty</i> is Copyright (C) 1993 by Gert Doering, &lt;gert [at] greenie.muc.de&gt;. </p>
