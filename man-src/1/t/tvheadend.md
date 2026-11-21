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
<dt><code>-v</code>, <code>&#8211;version</code></dt>
<dd> Show version information.</dd>
<dt><code>-h</code>, <code>&#8211;help</code></dt>
<dd> Show built-in help information (may be more up to date).</dd>
<dt><code>-c</code>, <code>&#8211;config</code></dt>
<dd> Specify an alternate config path; the default is <i>${HOME}/.hts</i></dd>
<dt><code>-f</dt>
<dd> Fork and become a background process (deamon). Default no.</dd>
<dt>-u</code> <i>username</i>, <code>&#8211;user</code> <i>username</i></dt>
<dd> Run as user <i>username</i>. Only applicable if daemonizing. Default is to use the uid of 1 (daemon on most systems).</dd>
<dt><code>-g</code> <i>groupname</i>, <code>&#8211;group </code><i>groupname</i></dt>
<dd> Run as group <i>groupname</i>. Only applicable if daemonizing. Default is to use the &#8216;video&#8217; group. If the &#8216;video&#8217; group does not exist, gid 1 (daemon) will be used.</dd>
<dt><code>-p</code> <i>pidpath</i>, <code>&#8211;pid </code><i>pidpath</i></dt>
<dd> Specify alternative PID path file (default /var/run/tvheadend.pid).</dd>
<dt><code>-C</code>, <code>&#8211;firstrun</code></dt>
<dd> If no useraccount exist then create one with no username and no password. Use with care as it will allow world-wide administrative access to your Tvheadend installation until you edit the access-control from within the Tvheadend UI.</dd>
<dt><code>-a</code>, <code>&#8211;adapters</code></dt>
<dd> Only use specified DVB adapters (comma separated).</dd>
<dt><code>-6</code>, <code>&#8211;ipv6</code></dt>
<dd> Listen on IPv6.</dd>
<dt><code>-b</code> <i>address</i>, <code>&#8211;bindaddr</code> <i>address</i></dt>
<dd> Specify an interface IP address on which incoming HTTP and HTSP connections will be accepted. By default, connections are accepted on all interfaces.</dd>
<dt><code>&#8211;http_port</dt>
<dd> Specify alternative http port (default 9881).</dd>
<dt>&#8211;http_root</dt>
<dd> Specify alternative http webroot.</dd>
<dt>&#8211;htsp_port</dt>
<dd> Specify alternative htsp port (default 9882).</dd>
<dt>&#8211;htsp_port2</dt>
<dd> Specify extra htsp port.</dd>
<dt>-d</code>, <code>&#8211;debug</code></dt>
<dd> Enable all debug.</dd>
<dt><code>-s</code>, <code>&#8211;syslog</code></dt>
<dd> Enable debug to syslog.</dd>
<dt><code>&#8211;uidebug</dt>
<dd> Enable web UI debug.</dd>
<dt>-l</code>, <code>&#8211;log</code></dt>
<dd> Log to file.</dd>
<dt><code>-A</code>, <code>&#8211;abort</code></dt>
<dd> Immediately abort on startup (for debug).</dd>
<dt><code>&#8211;noacl</dt>
<dd> Do not perform any access control checking.</dd>
<dt>-R</code>, <code>&#8211;dvbraw</code></dt>
<dd> Use rawts file to create virtual adapter.</dd>
<dt><code>-r</code>, <code>&#8211;rawts</code></dt>
<dd> Use rawts file to generate virtual services.</dd>
<dt><code>-j</code>, <code>&#8211;join</code></dt>
<dd> Subscribe to a service permanently.</dd></dl>
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
