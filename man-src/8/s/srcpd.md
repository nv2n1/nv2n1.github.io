---
title: "srcpd(8)"
name: "srcpd"
section: "8"
letter: "s"
url: "/docs/linux/man/8-srcpd/"
description: "srcpd – SRCP speaking daemon"
---

<p>srcpd &#8211; SRCP speaking daemon</p>
<h2>Synopsis</h2>
<p><code>srcpd</code> [ options ] </p>
<h2>Description</h2>
<p>This is not a complete manual. You have to consult the project home page at <a rel="nofollow" href="http://srcpd.sourceforge.net/">http://srcpd.sourceforge.net/</a> for full documentation! <code>srcpd</code> is a UNIX daemon speaking the Simple Railroad Command Protocol (SRCP). Upon start up it reads in the system wide configuration file named <code>srcpd.conf</code>. Contents and structure of this XML-file is explained in detail in the <code>srcpd.conf (5)</code> man page. The SRCP specification is published on <a rel="nofollow" href="http://srcpd.sourceforge.net/srcp.">http://srcpd.sourceforge.net/srcp.</a> </p>
<h2>Options</h2>
<dl>
<dt><code>-h</code></p>
<dd>Prints some useful help about command line options and exit</p>
<dt><code>-n</code></p>
<dd>Do not daemonize upon start-up. The srcpd does not switch into background mode. This option can be used with the Ubuntu upstart system.</p>
<dt><code>-v</code></p>
<dd>Print program version, SRCP level and exit</p>
<dt><code>-f&nbsp;<wbr>&lt;filename&gt;</code></p>
<dd>Use the specified filename as the configuration file. The default value will be defined at compile time and can be displayed using the <code>-h</code> parameter. </p>
</dl>
<h2>Notes</h2>
<h3>Getting started</h3>
<p>The <code>srcpd</code> system service (daemon) is compliant to the Filesystem Hierarchy Standard (FHS, <a rel="nofollow" href="http://www.pathname.com/fhs/">http://www.pathname.com/fhs/</a>). For more information and special options about daemon usage please refer to to your system documentation. The following instructions are on a general level of information. </p>
<h2>Notes</h2>
<p>Please first start assembling a configuration file (<i>srcpd.conf</i>) fitting exactly your needs to connect to your model railway controller interface. Save this file to the directory for host specific system configuration (<i>/etc</i>). The default configuration file delivered with this software must be replaced by the new one. As soon as the adapted configuration file is at the right place, the daemon can be started using this command:</p>
<dl>
<dd>
<pre>/etc/init.d/srcpd start</pre>
</dl>
<p> If the <code>srcpd</code> is already running, the daemon first must be stopped to get it aware of the new setup. Stopping the daemon is executed in analogy to the start command:</p>
<dl>
<dd>
<pre>/etc/init.d/srcpd stop</pre>
</dl>
<p> Under certain conditions it is also possible to get the daemon re-read its configuration file without stopping it. With respect to hardware access rules under UNIXlike systems, the group and/or user rights must be properly set in <i>srcpd.conf</i> to let the daemon access the appropriate hardware resources at any time. Common model railway interfaces will require access rights for serial lines (RS232, USB), which can be achieved using the proper group rights (e.g. <code>dialout</code>). The <code>ddl-s88</code> module uses a special system function (ioperm) which always needs root rights to perform successfully. To let srcpd re-read its configuration file, assumed the setup mentioned before is correct, the following command can be used:</p>
<dl>
<dd>
<pre>/etc/init.d/srcpd reload</pre>
</dl>
<p> The log file <i>/var/log/messages</i> or <i>/var/log/syslog</i> of the syslog daemon can be used to monitor occurring errors on daemon start or during current operation. With root rights the upcoming messages can be continuously watched in a separate terminal:</p>
<dl>
<dd>
<pre>tail -f /var/log/messages</pre>
</dl>
<p> or</p>
<dl>
<dd>
<pre>tail -f /var/log/syslog</pre>
</dl>
<p> The verbosity of these messages can be adjusted using the configuration file <i>srcpd.conf</i>. For more information refer to the adequate man page. </p>
<h2>See Also</h2>
<p>srcpd.conf (5) </p>
<h2>Bugs</h2>
<p>Possibly there are some bugs. Please report them to the project developer mailing list. </p>
<h2>Authors</h2>
<p>This man page was written by Matthias Trute (mtrute [at] users.sourceforge.net), Frank Schimschke (schmischi [at] users.sourceforge.net) and Guido Scholz (gscholz [at] users.sourceforge.net).</p>
<h2>License</h2>
<p>GNU General Public License, Version 2</p>
