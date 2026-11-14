---
title: "ncid(1)"
name: "ncid"
section: "1"
letter: "n"
url: "/docs/linux/man/1-ncid/"
description: "ncid – Network Caller ID Client"
---

<h2>NAME</h2>
<p> <code>ncid</code> &#8211; Network Caller ID Client</p>
<h2>SYNOPSIS</h2>
<p> <code>ncid</code> [options] [arguments] </p>
<p> <code>tivocid</code> [options] [arguments] </p>
<p> <code>tivoncid</code> [options] [arguments] </p>
<p> <i>Options:</i> </p>
<pre><code>
[--no - gui]
    [--call - prog | -C]
    [--delay seconds | -D seconds]
    [--message | -M]
    [--nocid | -N]
    [--program PROGRAM | -P PROGRAM]
    [--pidfile FILE | -p PIDFILE]
    [--raw | -R]
    [--ring count | -r count]
    [--tivo | -T]
    [--PopupTime seconds | -t seconds]
    [--verbose | -V]
</code></pre>
<p> <i>Arguments:</i> </p>
<p>[IP_ADDRESS | HOSTNAME]<br />
    [PORT_NUMBER]</p>
<h2>DESCRIPTION</h2>
<p> <code>Ncid</code> displays Caller ID information sent to it by the Caller ID server. In the default GUI mode, if the server is configured to send the CID Call Log, it will load the call log in the CID log window at startup. The call log is updated by <i>ncid</i> whenever a call is received. </p>
<p> <code>Ncid</code> can also display <i>Phone Call</i><code> if the modem used by the server does not send the Caller ID information to it. This is useful if a visual indication is wanted for ringing. </p>
<p> Ncid</code> also has a message window that will send a single line message to the server which, in turn, will send it to all connected clients. </p>
<p> <code>Ncid</code> runs on Linux and Windows 98, ME, XP, 2000, NT. In the GUI mode, it will pop up, and go on top whenever a call comes in. In addition, it will display itself on whatever desktop is active in Linux. If <i>ncid</i> is given the &#8211;no-gui option, it will either output to a external program, output module, or use the verbose mode to display the CID information in a terminal window. </p>
<p> If <i>ncid</i> is named <i>tivocid</i>, it will start in a no-gui mode and output to a external program called <i>out2osd</i> which displays the Caller ID on a TV using a TiVo. </p>
<p> If <i>ncid</i> is named <i>tivoncid</i>, it will start in a no-gui mode and output to a module called <i>ncid-tivo</i> which displays the Caller ID on a TV using a TiVo. This option uses the TiVo program, <i>text2osd</i>, instead of <i>out2osd</i>. </p>
<p> If <i>ncid</i> is configured to output to a external program, it will test for it, and if it is not found, or if it is not executable, it will terminate with a error message. </p>
<p> The configuration file for <i>ncid</i> is /etc/ncid/ncid.conf. </p>
<p> The distributed output modules are listed in the ncidmodules man page, can be customized as needed in the /etc/ncid/ncidmodules.conf file: </p>
<p> Whenever the server connection is broken, <i>ncid</i> will normally try to reconnect once a minute. It provides a visual record of the countdown and number of tries. If the delay between attempts is set to zero seconds, <i>ncid</i> will not attempt a reconnect. </p>
<p> The file menu provides three menu items in the GUI mode:</p>
<dl>
<dt><code>reconnect</code></p>
<dd> provides an immediate reconnect and a reload of the call log file. This provides a way to synchronize <i>ncid</i> with the server call log in the event of a network problem.</p>
<dt><code>clear</code></p>
<dd> clears the call log</p>
<dt><code>quit</code></p>
<dd> terminates <i>ncid</i>.</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;no-gui</code></p>
<dd> Do not display CID information using a GUI<br />
 Default: display CID using a GUI, except if called tivocid</p>
<dt><code>&#8211;call-prog | -C</code></p>
<dd> Output the Caller ID information to a external program or output module.<br />
 Default: does not call a external program unless name is tivocid or tivoncid</p>
<dt><code>&#8211;delay SECONDS | -D SECONDS</code></p>
<dd> Delay SECONDS between server connection attempts if SECONDS &gt; 0.<br />
 Only one attempt to connect to server if SECONDS = 0.<br />
 Default: 60 seconds</p>
<dt><code>&#8211;message | -M</code></p>
<dd> Send messages to the output modules</p>
<dt><code>&#8211;nocid | -N</code></p>
<dd> Configure ncid to indicate <i>Phone Call</i> on the first ring received from the modem. It requires a modem that indicates ring, but does not require a modem that supports caller id.</p>
<dt><code>&#8211;pidfile | -p</code></p>
<dd> Name of PID file to create. Set to <i>/var/run/ncid.pid</i><code> in a rc or init script when used as a service. Set to </code><i>/var/run/OUTPUTMODULE.pid</i><code> in a rc or init script when used as a service and when using a output module. There is no default. If pidfile is not set, no pid file will be used.</p>
<dt>&#8211;program PROGRAM | -P PROGRAM</code></p>
<dd> Name of the output module (program) to use. Some output modules are ncid-kpopup, ncid-page, and ncid-speak.<br />
 Default PATH: /usr/share/ncid<br />
 Default PROGRAM: ncid-speak</p>
<dt><code>&#8211;raw | -R</code></p>
<dd> display data received from the CID Server<br />
 Default: raw data not displayed</p>
<dt><code>&#8211;ring count | -r count</code></p>
<dd> Call output module on specific ring count.<br />
 For modems that indicate RING, count can be: 0 2 3 4 5 6 7 8 9<br />
 For VoIP, using a SIP gateway, count can be: -2 -1<br />
 A count of -1 incdicates a hangup before answer.<br />
 A count of -2 incdicates a hangup after answer.<br />
 Default: output module called as soon as CID received</p>
<dt><code>&#8211;Tivo | -T</code></p>
<dd> This option is for a TiVo using out2osd or text2osd<br />
 Changes output to 2 lines: name number line<br />
 Default output is 5 lines: date time number name line</p>
<dt><code>&#8211;PopupTime seconds | -t seconds</code></p>
<dd> Time for the popup to stay on top of all windows. Range is 1 second to 99 seconds<br />
 Default popup time os 5 seconds</p>
<dt><code>&#8211;verbose | -V</code></p>
<dd> display formatted CID information, including CID log file<br />
 Default: silent</dl>
<h3>Arguments</h3>
<dl>
<dt><code>IP_ADDRESS | HOSTNAME</code></p>
<dd> set the IP Address<br />
 Default: 127.0.0.1 (localhost)</p>
<dt><code>PORT_NUMBER</code></p>
<dd> set the port number<br />
 Default: 3333</dl>
<h2>FILES</h2>
<p> /etc/ncid/*<br />
 /usr/share/ncid/*</p>
<h2>EXAMPLES</h2>
<pre><code>
#run ncid in a terminal window, server on remote host
ncid-- no - gui tardis.drwho.home
#only speak Caller ID
                ncid-- no -
    gui-- call - prog-- program ncid - speak
#send CID output to GUI and speak it
                                           ncid-- call -
    prog-- program / usr / local / bin / ncid - speak
#send CID output to a cell phone after third ring
                                                    ncid-- no -
    gui-- call - prog-- program ncid - page-- ring 3
#send CID output to a cell phone on hangup before answer
    ncid-- no -
    gui-- call - prog-- program ncid - page-- ring - 1
#indicate ring on a popup module as a message
    ncid-- no -
    gui-- nocid-- message-- call - prog-- program ncid - kpopup
#run ncid on a TiVo using out2osd, server on remote host
                                                             tivocid 192.168.0.1
</code></pre>
<h2>SEE ALSO</h2>
<p> ncid.conf.5, ncidmodules.1, ncidmodules.conf.5, ncidd.8, ncidd.conf.5, ncidd.alias.5, sip2ncid.8, sip2ncid.conf.5, ncidsip.8, ncidsip.conf.5 </p>
<h2>Index</h2>
