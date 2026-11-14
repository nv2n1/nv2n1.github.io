---
title: "sensord(8)"
name: "sensord"
section: "8"
letter: "s"
url: "/docs/linux/man/8-sensord/"
description: "sensord – Sensor information logging daemon."
---

<p>sensord &#8211; Sensor information logging daemon.</p>
<h2>Synopsis</h2>
<p><code>sensord [</code> <i>options</i> <code>] [</code> <i>chips</i> <code>]</code> </p>
<h2>Description</h2>
<p><code>Sensord</code> is a daemon that can be used to periodically log sensor readings from hardware health-monitoring chips to <code><a href="/docs/linux/man/3-syslog/">syslog</a></code>(3) or a round-robin database (RRD) and to alert when a sensor alarm is signalled; for example, if a fan fails, a temperature limit is exceeded, etc. </p>
<h2>Options</h2>
<dl>
<dt>-i, &#8211;interval time</p>
<dd>Specify the interval between scanning for sensor alarms; the default is to scan every minute. </p>
<p> The time should be specified as a raw integer (seconds) or with a suffix `s&#8217; for seconds, `m&#8217; for minutes or `h&#8217; for hours; for example, the default interval is `60&#8242; or `1m&#8217;. </p>
<p> Specify an interval of zero to suppress scanning explicitly for alarms.</p>
<dt>-l, &#8211;log-interval time</p>
<dd>Specify the interval between logging all sensor readings; the default is to log all readings every half hour. </p>
<p> The time is specified as before; e.g., `30m&#8217;. </p>
<p> Specify an interval of zero to suppress logging of regular sensor readings.</p>
<dt>-t, &#8211;rrd-interval time</p>
<dd>Specify the interval between logging all sensor readings to a round-robin database; the default is to log all readings every five minutes <code>if</code> a round-robin database is configured. </p>
<p> The time is specified as before; e.g., `5m&#8217;.</p>
<dt>-T, &#8211;rrd-no-average</p>
<dd>Specify that the round-robin database should not be averaged. </p>
<dt>-r, &#8211;rrd-file file</p>
<dd>Specify a round-robin database into which to log all sensor readings; e.g., `/var/log/sensord.rrd&#8217;. This database will be created if it does not exist. By default, no round-robin database is used. </p>
<p> See the section <code>ROUND ROBIN DATABASES</code> below for more details.</p>
<dt>-c, &#8211;config-file file</p>
<dd>Specify a <code><a href="/docs/linux/man/3-libsensors/">libsensors</a></code>(3) configuration file. If no file is specified, the libsensors default configuration file is used. </p>
<dt>-p, &#8211;pid-file file</p>
<dd>Specify what PID file to write; the default is to write the file `/var/run/sensord.pid&#8217;. You should always specify an absolute path here. The file is removed when the daemon exits.</p>
<dt>-f, &#8211;syslog-facility facility</p>
<dd>Specify the <code><a href="/docs/linux/man/3-syslog/">syslog</a></code>(3) facility to use when logging sensor readings and alarms; the default is to use <i>daemon</i>. </p>
<p> Other possible facilities include <i>local0</i> through <i>local7</i>, and <i>user</i>.</p>
<dt>-g, &#8211;rrd-cgi directory</p>
<dd>Prints out a sample <code><a href="/docs/linux/man/1-rrdcgi/">rrdcgi</a></code>(1) CGI script that can be used to display graphs of recent sensor information in a Web page, and exits. You must specify the world-writable, Web-accessible directory where the graphs should be stored; the CGI script assumes that this will be accessed under the `/sensord/&#8217; directory on the Webserver. See the section <code>ROUND ROBIN DATABASES</code> below for more details.</p>
<dt>-a, &#8211;load-average</p>
<dd>Include the load average in the RRD database. You should also specify this flag when you create the CGI script.</p>
<dt>-d, &#8211;debug</p>
<dd>Prints a small amount of additional debugging information.</p>
<dt>-h, &#8211;help</p>
<dd>Prints a help message and exits.</p>
<dt>-v, &#8211;version</p>
<dd>Displays the program version and exits.</dl>
<h2>Chips</h2>
<p>To restrict the devices that are scanned by this daemon, you may optionally specify a list of chip names. By default, all available chips are scanned. </p>
<p> A typical chip name would be `w83782d-*&#8217; (you may want to escape the `*&#8217; for your shell) which would scan any W83782D chips on any bus. See <code><a href="/docs/linux/man/5-sensors-conf/">sensors.conf</a></code>(5) for more details. Another option is to simply not load the sensor modules for chips in which you have no interest.</p>
<h2>Signals</h2>
<p>Upon receipt of a SIGTERM (see <code><a href="/docs/linux/man/7-signal/">signal</a></code>(7) for details) this daemon should gracefully shut down. </p>
<p> Upon receipt of a SIGHUP, this daemon will rescan the kernel interface for chips and features, and reload the libsensors configuration file.</p>
<h2>Logging</h2>
<p>All messages from this daemon are logged to <code><a href="/docs/linux/man/3-syslog/">syslog</a></code>(3) under the program name `sensord&#8217; and facility <i>daemon</i>, or whatever is specified on the command line. </p>
<p> Regular sensor readings are logged at the level <i>info</i>. Alarms are logged at the level <i>alert</i>. Inconsequential status messages are logged at the minimum level, <i>debug</i>, when debugging is enabled. </p>
<p> You can use an appropriate `/etc/syslog.conf&#8217; file to direct these messages in a useful manner. See <code><a href="/docs/linux/man/5-syslog-conf/">syslog.conf</a></code>(5) for full details. Assuming you set the logging facility to local4, the following is a sample configuration:</p>
<dl>
<dd>
<pre># Sample syslog.conf entries
*.info;...;local4.none;local4.warn /var/log/messages
local4.info -/var/log/sensors
local4.alert /dev/console
local4.alert *</pre>
</dl>
<p> The first line ensures that regular sensor readings do not clutter `/var/log/messages&#8217;; we first say `local4.none&#8217; to eliminate informational messages; then `local4.warn&#8217; to enable warnings and above. The second line says to log all regular sensor readings to `/var/log/sensors&#8217;; the leading hyphen `-&#8216; means that this file is not flushed after every message. The final two lines ensure that alarms are printed to the system console as well as to all connected users (in addition to `/var/log/messages&#8217; and `/var/log/sensors&#8217;).</p>
<h2>Log Rotation</h2>
<p>On a typical system with a good sensor chip, expect about 2KB per sensor reading in the log file. This works out at about 3MB per month. You should be rotating your syslog files anyway, but just to be sure you&#8217;ll want to use something like <code><a href="/docs/linux/man/8-logrotate/">logrotate</a></code>(8) or equivalent. You might, for example, want an entry in `/etc/logrotate.d/syslog&#8217; containing:</p>
<dl>
<dd>
<pre># Sample logrotate.d entry
/var/log/sensors {
 postrotate
 /usr/sbin/killall -HUP syslogd
 endscript
}</pre>
</dl>
<p> Note, of course, that you want to restart <code><a href="/docs/linux/man/8-syslogd/">syslogd</a></code>(8) and not <code><a href="/docs/linux/man/8-sensord/">sensord</a></code>(8)</p>
<h2>Alarms</h2>
<p>Alarms generally indicate a critical condition; for example, a fan failure or an unacceptable temperature or voltage. However, some sensor chips do not support alarms, while others are incorrectly configured and may signal alarms incorrectly. </p>
<p> Note that some drivers may lack support for alarm reporting even though the chips they support do have alarms. As of Linux 2.6.23, many drivers still don&#8217;t report alarms in a format suitable for libsensors 3.</p>
<h2>Beeps</h2>
<p>If you see `(beep)&#8217; beside any sensor reading, that just means that your system is configured to issue an audio warning from the motherboard if an alarm is signalled on that sensor.</p>
<h2>Round Robin Databases</h2>
<p><code><a href="/docs/linux/man/8-sensord/">Sensord</a></code>(8) provides support for storing sensor readings in a round-robin database. This may be a useful alternative to the use of <code><a href="/docs/linux/man/3-syslog/">syslog</a></code>(3). </p>
<p> Round-robin databases are constant-size databases that can be used to store, for example, a week&#8217;s worth of sensor readings. Subsequent readings stored in the database will overwrite readings that are over a week old. This capability is extremely useful because it allows useful information to be stored in an easily-accessible manner for a useful length of time, without the burden of ever-growing log files. </p>
<p> The <code><a href="/docs/linux/man/1-rrdtool/">rrdtool</a></code>(1) utility and its associated library provide the basic framework for the round-robin database beneath <code><a href="/docs/linux/man/8-sensord/">sensord</a></code>(8). In addition, the <code><a href="/docs/linux/man/1-rrdcgi/">rrdcgi</a></code>(1) and <code><a href="/docs/linux/man/1-rrdgraph/">rrdgraph</a></code>(1) utilities provide support for generating graphs of these data for display in a Web page. </p>
<p> If you wish to use the default configuration of round-robin database, which holds one week of sensor readings at five-minute intervals, then simply start <code><a href="/docs/linux/man/8-sensord/">sensord</a></code>(8) and specify where you want the database stored. It will automatically be created and configured using these default parameters. </p>
<p> If you wish readings to be stored for a longer period, or want multiple readings to be averaged into each database entry, then you must manually create and configure the database before starting <code><a href="/docs/linux/man/8-sensord/">sensord</a></code>(8). Consult the <code><a href="/docs/linux/man/1-rrdcreate/">rrdcreate</a></code>(1) manual for details. Note that the database must match exactly the names and order of sensors read by <code><a href="/docs/linux/man/8-sensord/">sensord</a></code>(8). It is recommended that you create the default database and then use <code><a href="/docs/linux/man/1-rrdinfo/">rrdinfo</a></code>(1) to obtain this information, and/or <code><a href="/docs/linux/man/1-rrdtune/">rrdtune</a></code>(1) to change it. </p>
<p> After creating the round-robin database, you must then configure your Web server to display the sensor information. This assumes that you have a Web server preconfigured and functioning on your machine. <code><a href="/docs/linux/man/8-sensord/">Sensord</a></code>(8) provides a command-line option <code>&#8211;rrd-cgi</code> to generate a basic CGI script to display these graphs; you can then customize this script as desired. Consult the <code><a href="/docs/linux/man/1-rrdcgi/">rrdcgi</a></code>(1) manual for details. This CGI script requires a world-writable, Web-accessible directory into which to write the graphs that it generates. </p>
<p> An example of how to set up Web-accessible graphs of recent sensor readings follows:</p>
<dl>
<dd>
<pre>sensord --log-interval 0 \
 --load-average \
 --rrd-file /var/log/sensord.rrd</pre>
</dl>
<p> Here, we start <code><a href="/docs/linux/man/8-sensord/">sensord</a></code>(8) and configure it to store readings in a round-robin database; note that we disable logging of sensor readings to <code><a href="/docs/linux/man/3-syslog/">syslog</a></code>(3), and enable logging of the load average.</p>
<dl>
<dd>
<pre>mkdir /var/www/sensord
chown www-data:staff /var/www/sensord
chmod a=rwxs /var/www/sensord</pre>
</dl>
<p> Here, we create a world-writable, Web-accessible directory in which graphs will be stored; we set the ownership and permissions on this directory appropriately. You will have to determine the location and ownership that is appropriate for your machine.</p>
<dl>
<dd>
<pre>sensord --load-average \
 --rrd-file /var/log/sensord.rrd \
 --rrd-cgi /var/www/sensord \
 &gt; /usr/lib/cgi-bin/sensord.cgi
chmod a+rx /usr/lib/cgi-bin/sensord.cgi</pre>
</dl>
<p> Here, we create a CGI script that will display sensor readings from the database. You must specify the location of the round-robin database, the location of the directory where the images should be stored, and whether you want the load average displayed. The <code>&#8211;rrd-cgi</code> command-line parameter causes <code><a href="/docs/linux/man/8-sensord/">sensord</a></code>(8) to display a suitable CGI script on <code>stdout</code> and then to exit. You will need to write this script to the CGI bin directory of your Web server, and edit the script if the image directory you chose is not the `/sensord/&#8217; directory of your Web server. </p>
<p> Finally, you should be able to view your sensor readings from the URL `<a rel="nofollow" href="http://localhost/cgi-bin/sensord.cgi'.">http://localhost/cgi-bin/sensord.cgi&#8217;.</a></p>
<h2>Modules</h2>
<p>It is expected that all required sensor modules are loaded prior to this daemon being started. This can either be achieved with a system specific module loading scheme (e.g., listing the required modules in the file `/etc/modules&#8217; under Debian) or with explicit <code><a href="/docs/linux/man/1-modprobe/">modprobe</a></code>(1) commands in an init script before loading the daemon. </p>
<p> For example, a `sensord&#8217; initialization script might contain (among others) the following commands:</p>
<dl>
<dd>
<pre># Sample init.d scriptlet
echo -n &quot;Loading AMD756 module: &quot;
modprobe i2c-amd756 || { echo Fail. ; exit 1 ; }
echo OK.
echo -n &quot;Loading W83781D module: &quot;
modprobe w83781d || { echo Fail. ; exit 1 ; }
echo OK.
echo -n &quot;Starting sensord: &quot;
daemon sensord</pre>
</dl>
<p> Ignore the platform-specific shell functions; the general idea should be fairly clear.</p>
<h2>Errors</h2>
<p>Errors encountered by this daemon are logged to <code><a href="/docs/linux/man/8-syslogd/">syslogd</a></code>(8) after which the daemon will exit.</p>
<h2>Bugs</h2>
<p>Round-robin database support doesn&#8217;t cope with multiple sensor chips having duplicate sensor labels.</p>
<h2>Files</h2>
<p><i>/etc/sensors3.conf</i><br />
 <i>/etc/sensors.conf</i></p>
<dl>
<dd>The system-wide <code><a href="/docs/linux/man/3-libsensors/">libsensors</a></code>(3) configuration file. See <code><a href="/docs/linux/man/5-sensors-conf/">sensors.conf</a></code>(5) for further details.</dl>
<p> <i>/etc/syslog.conf</i></p>
<dl>
<dd>The system-wide <code><a href="/docs/linux/man/3-syslog/">syslog</a></code>(3) / <code><a href="/docs/linux/man/8-syslogd/">syslogd</a></code>(8) configuration file. See <code><a href="/docs/linux/man/5-syslog-conf/">syslog.conf</a></code>(5) for further details.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/5-sensors-conf/">sensors.conf</a>(5)</p>
<h2>Authors</h2>
<p><code>Sensord</code> was written by Merlin Hughes &lt;merlin [at] merlin.org&gt;. Basics of round-robin databases were misappropriated from Mark D. Studebaker.</p>
