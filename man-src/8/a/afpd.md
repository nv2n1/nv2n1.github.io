---
title: "afpd(8)"
name: "afpd"
section: "8"
letter: "a"
url: "/docs/linux/man/8-afpd/"
description: "afpd – AppleTalk Filing Protocol daemon"
---

<p>afpd &#8211; AppleTalk Filing Protocol daemon</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>afpd</code> [-duptDTvI] [-f&nbsp;<wbr><i>defaultvolumes</i>] [-s&nbsp;<wbr><i>systemvolumes</i>] [-n&nbsp;<wbr><i>nbpname</i>] [-c&nbsp;<wbr><i>maxconnections</i>] [-g&nbsp;<wbr><i>guest</i>] [-P&nbsp;<wbr><i>pidfile</i>] [-S&nbsp;<wbr><i>port</i>] [-L&nbsp;<wbr><i>message</i>] [-F&nbsp;<wbr><i>config</i>] [-U&nbsp;<wbr><i>uamsv</i>] [-m&nbsp;<wbr><i>umask</i>]</dl>
<h2>Description</h2>
<p><code>afpd</code></p>
<dd>provides an AppleTalk Filing Protocol (AFP) interface to the Unix file system. It is normally started at boot time from /etc/rc. The list of volumes offered to the user is generated from /etc/atalk//AppleVolumes.system and one of /etc/atalk//AppleVolumes.default, ~/AppleVolumes, or ~/.AppleVolumes. The AppleVolumes files is used to specify volumes to mount and file name extension mappings. It is formatted as follows, one specification per line: pathname [ volumename ] .extension [ type [ creator ] ] If volumename is unspecified, the last component of pathname is used. No two volumes may have the same name. If type is unspecified &#8216;????&#8217; is used. If creator is unspecified &#8216;UNIX&#8217; is used. The extension &#8216;.&#8217; sets the default creator and type for otherwise untyped Unix files. Blank lines and lines beginning with `#&#8217; are ignored. </p>
<h2>Options</h2>
<p>-d</p>
<dl>
<dd>Specifies that the daemon should not fork. If netatalk has been configured with <i>&#8211;enable-debug1</i>, a trace of all AFP commands will be written to stdout.</dl>
<p> -p</p>
<dl>
<dd>Prevents clients from saving their passwords. (Equivalent to &#8211;<code>nosavepasswd</code> in afpd.conf.)</dl>
<p> -t</p>
<dl>
<dd>Allows clients to change their passwords. (Equivalent to <code>-setpasswd</code> in afpd.conf.)</dl>
<p> -D</p>
<dl>
<dd>Use DDP (AppleTalk) as transport protocol. (Equivalent to <code>-ddp</code> in afpd.cond.)</dl>
<p> -T</p>
<dl>
<dd>Use TCP/IP as transport protocol. (Equivalent to <code>-tcp</code> in afpd.conf.)</dl>
<p> -v</p>
<dl>
<dd>Print version information and exit.</dl>
<p> -I</p>
<dl>
<dd>Use a platform specific icon. (Equivalent to <code>-icon</code> in afpd.conf.)</dl>
<p> -f <i>defaultvolumes</i></p>
<dl>
<dd>Specifies that <i>defaultvolumes</i> should be read for a list of default volumes to offer, instead of /etc/atalk//AppleVolumes.default.</dl>
<p> -s <i>systemvolumes</i></p>
<dl>
<dd>Specifies that <i>systemvolumes</i> should be read for a list of volume that all users will be offered, instead of /etc/atalk//AppleVolumes.system.</dl>
<p> -u</p>
<dl>
<dd>Read the user&#8217;s AppleVolumes file first. This option causes volume names in the user&#8217;s AppleVolumes file to override volume names in the system&#8217;s AppleVolumes file. The default is to read the system AppleVolumes file first. Note that this option doesn&#8217;t effect the precendence of filename extension mappings: the user&#8217;s AppleVolumes file always has precedence.</dl>
<p> -n <i>nbpname</i></p>
<dl>
<dd>Specifies that <i>nbpname</i> should be used for NBP registration, instead of the first component of the hostname in the local zone.</dl>
<p> -c <i>maxconnections</i></p>
<dl>
<dd>Specifies the maximum number of connections to allow for this <code>afpd</code>. The default is 20.</dl>
<p> -g <i>guest</i></p>
<dl>
<dd>Specifies the name of the guest account. The default is &#8216;<i>nobody</i>&#8216;.</dl>
<p> -P <i>pidfile</i></p>
<dl>
<dd>Specifies the file in which <code>afpd</code> stores its process id.</dl>
<p> -S <i>port</i></p>
<dl>
<dd>Specifies the port to register with when doing AFPoverTCP. Defaults to 548. (Equivalent to <code>-port </code>in afpd.conf.)</dl>
<p> -L <i>message</i></p>
<dl>
<dd>Specifies the login message that will be sent to clients. (Equivalent to <code>-loginmsg</code> in afpd.conf.)</dl>
<p> -F <i>configfile</i></p>
<dl>
<dd>Specifies the configuration file to use. (Defaults to /etc/atalk//netatalk/afpd.conf.)</dl>
<p> -U <i>uams</i></p>
<dl>
<dd>Comma-separated list of UAMs to use for the authentication process. (Equivalent to <code>-uamlist</code> in afpd.conf.)</dl>
<p> -m <i>umask</i></p>
<dl>
<dd>Use this <i>umask</i> for the creation of folders in Netatalk.</dl>
<h2>Signals</h2>
<p>Signals that are sent to the main <code>afpd</code> process are propagated to the children, so all will be affected. </p>
<p> SIGHUP</p>
<dl>
<dd>Sending a <code>SIGHUP</code> to afpd will cause it to reload its configuration files.</dl>
<p> SIGUSR1</p>
<dl>
<dd>The <code>afpd</code> process will send the message &quot;The server is going down for maintenance.&quot; to the client and shut itself down in 5 minutes. New connections are not allowed. If this is sent to a child afpd, the other children are not affected. However, the main process will still exit, disabling all new connections.</dl>
<p> SIGUSR2</p>
<dl>
<dd>The <code>afpd</code> process will look in the message directory configured at build time for a file named message.pid. For each one found, a the contents will be sent as a message to the associated AFP client. The file is removed after the message is sent. This should only be sent to a child <code>afpd</code>. Warning: If the &#8211;with-message-dir option was not used, this will kill the <code>afpd</code> process </p>
<p> To shut down a user&#8217;s <code>afpd</code> process it is recommended that <code>SIGKILL (-9)</code> <i>NOT</i> be used, except as a last resort, as this may leave the CNID database in an inconsistent state. The safe way to terminate an <code>afpd</code> is to send it a <code>SIGTERM (-15)</code> signal and wait for it to die on its own.</dl>
<h2>Files</h2>
<p>/etc/atalk//AppleVolumes.default</p>
<dl>
<dd>list of default volumes to mount</dl>
<p> /etc/atalk//AppleVolumes.system</p>
<dl>
<dd>list of volumes to offer all users</dl>
<p> ~/AppleVolumes</p>
<dl>
<dd>user&#8217;s list of volumes to mount</dl>
<p> /etc/atalk//netatalk/msg/message.pid</p>
<dl>
<dd>contains messages to be sent to users.</dl>
<h2>Bugs</h2>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-hosts_access/">hosts_access</a></code>(5), <code><a href="/docs/linux/man/5-afpd-conf/">afpd.conf</a></code>(5), <code><a href="/docs/linux/man/5-applevolumes-default/">AppleVolumes.default</a></code>(5), <code><a href="/docs/linux/man/5-applevolumes-system/">AppleVolumes.system</a></code>(5). </p>
