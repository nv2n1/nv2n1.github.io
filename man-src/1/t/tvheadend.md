---
title: "tvheadend(1)"
name: "tvheadend"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tvheadend/"
description: "tvheadend – Advanced TV streaming server/relay"
---

<h2>NAME</h2>
<p> tvheadend &nbsp;<wbr>&#8211; Advanced TV streaming server/relay</p>
<h2>SYNOPSIS</h2>
<p> <code>tvheadend</code> [<i>OPTIONS</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>Tvheadend</code> is a streaming server/relay supporing a variety of sources and multiple output formats. It is primarily inteded to be used in together with the <code>Showtime</code> Media player.</p>
<h2>OPTIONS</h2>
<p> All arguments are optional.</p>
<dl>
<dt><code>-v</code>, <code>&#8211;version</code></p>
<dd> Show version information.</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Show built-in help information (may be more up to date).</p>
<dt><code>-c</code>, <code>&#8211;config</code></p>
<dd> Specify an alternate config path; the default is <i>${HOME}/.hts</i></p>
<dt><code>-f</p>
<dd> Fork and become a background process (deamon). Default no.</p>
<dt>-u</code> <i>username</i>, <code>&#8211;user</code> <i>username</i></p>
<dd> Run as user <i>username</i>. Only applicable if daemonizing. Default is to use the uid of 1 (daemon on most systems).</p>
<dt><code>-g</code> <i>groupname</i>, <code>&#8211;group </code><i>groupname</i></p>
<dd> Run as group <i>groupname</i>. Only applicable if daemonizing. Default is to use the &#8216;video&#8217; group. If the &#8216;video&#8217; group does not exist, gid 1 (daemon) will be used.</p>
<dt><code>-p</code> <i>pidpath</i>, <code>&#8211;pid </code><i>pidpath</i></p>
<dd> Specify alternative PID path file (default /var/run/tvheadend.pid).</p>
<dt><code>-C</code>, <code>&#8211;firstrun</code></p>
<dd> If no useraccount exist then create one with no username and no password. Use with care as it will allow world-wide administrative access to your Tvheadend installation until you edit the access-control from within the Tvheadend UI.</p>
<dt><code>-a</code>, <code>&#8211;adapters</code></p>
<dd> Only use specified DVB adapters (comma separated).</p>
<dt><code>-6</code>, <code>&#8211;ipv6</code></p>
<dd> Listen on IPv6.</p>
<dt><code>-b</code> <i>address</i>, <code>&#8211;bindaddr</code> <i>address</i></p>
<dd> Specify an interface IP address on which incoming HTTP and HTSP connections will be accepted. By default, connections are accepted on all interfaces.</p>
<dt><code>&#8211;http_port</p>
<dd> Specify alternative http port (default 9881).</p>
<dt>&#8211;http_root</p>
<dd> Specify alternative http webroot.</p>
<dt>&#8211;htsp_port</p>
<dd> Specify alternative htsp port (default 9882).</p>
<dt>&#8211;htsp_port2</p>
<dd> Specify extra htsp port.</p>
<dt>-d</code>, <code>&#8211;debug</code></p>
<dd> Enable all debug.</p>
<dt><code>-s</code>, <code>&#8211;syslog</code></p>
<dd> Enable debug to syslog.</p>
<dt><code>&#8211;uidebug</p>
<dd> Enable web UI debug.</p>
<dt>-l</code>, <code>&#8211;log</code></p>
<dd> Log to file.</p>
<dt><code>-A</code>, <code>&#8211;abort</code></p>
<dd> Immediately abort on startup (for debug).</p>
<dt><code>&#8211;noacl</p>
<dd> Do not perform any access control checking.</p>
<dt>-R</code>, <code>&#8211;dvbraw</code></p>
<dd> Use rawts file to create virtual adapter.</p>
<dt><code>-r</code>, <code>&#8211;rawts</code></p>
<dd> Use rawts file to generate virtual services.</p>
<dt><code>-j</code>, <code>&#8211;join</code></p>
<dd> Subscribe to a service permanently.</dl>
<h2>LOGGING</h2>
<p> All activity inside tvheadend is logged to syslog using log facility <code>LOG_DAEMON</code>.</p>
<h2>SETUP</h2>
<h3>Access to video adapters</h3>
<p> In order for Tvheadend to control the video adapters on the system it must be granted access to those devices. Most systems have a &#8216;video&#8217; group with write access to the video adapter devices. When Tvheadend is started as a daemon it will automatcially change its primary group to &#8216;video&#8217; in order to access these groups. If your system is configured in a different way you can either change the group membership of the video adapters (/dev/dvb, etc) or reconfigure the Tvheadend startup parameters. This is most likely the behaviour if you have installed Tvheadend from a distribution package. </p>
<p> If Tvheadend is started without the &#8216;-f&#8217; argument it will not daemonize nor change its primary userid/groupid. Rather it will run with the permissions granted to the user executing the binary. If that&#8217;s the case you must make sure the current user is granted with access to the video devices.</p>
<h3>Configuration</h3>
<p> All configuration in Tvheadend is maintained via its embedded web server running on port 9981. Just point your browser to: </p>
<pre>
   <a rel="nofollow" href="http://hostname:9981/">http://hostname:9981/</a>
</pre>
<p> By default <i>everyone (also from remote hosts)</i> is allowed <i>full</i> access to <i>all</i> features / settings in the web user interface. If this is the first time you setup Tvheadend you are most encouraged to enter the web user interface, selected the &#8216;Configuration&#8217; + &#8216;Access Control&#8217; tab and make reasonable changes. Futher help / documentationcan be obtained inside the web interface.</p>
<h3>Settings</h3>
<p> Settings are stored in the current users home directory. Thus, if Tvheadend is run as a system daemon a dedicated user needs to be created and Tvheadend should be launched with the &#8216;-u&#8217; argument. Also notice that XMLTV will read store cache and configuration from the user home directory. </p>
<p> If daemonizing, tvheadend will writes it pid in /var/run/tvheadend.pid</p>
<h2>AUTHOR</h2>
<p> <code>Tvheadend</code> and this man page is maintained by Andreas Oeman </p>
<p> (andreas a tvheadend d org) </p>
<p> You may also visit #hts at irc.freenode.net</p>
<h2>SEE ALSO</h2>
<p> <code><a rel="nofollow" href="https://tvheadend.org">https://tvheadend.org</a></code> </p>
<h2>Index</h2>
