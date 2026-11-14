---
title: "monitorix-conf(5)"
name: "monitorix-conf"
section: "5"
letter: "m"
url: "/docs/linux/man/5-monitorix-conf/"
description: "monitorix.conf – Configuration file for Monitorix."
---

<p>monitorix.conf &#8211; Configuration file for Monitorix.</p>
<h2>Description</h2>
<p>Monitorix is a free, open source, lightweight system monitoring tool designed to monitor as many services and system resources as possible. It has been created to be used on production Linux/UNIX servers, but due to its simplicity and small size may also be used to monitor embedded devices as well. </p>
<p> It consists mainly of two programs: a collector, called <code>monitorix</code>, which is a Perl daemon that is started automatically like any other system service, and a CGI script called <code>monitorix.cgi</code>. Since 3.0 version Monitorix includes its own HTTP server built in, so you don&#8217;t need to install any web server to use it. </p>
<p> Every time <code>monitorix</code> is started it reads the configuration file from the path specified in the command line (using the <code>-c</code> option), and once checked, it creates the <i>index.html</i> file that will act as the Monitorix main page. </p>
<p> It also creates a file called <i>&lt;base_dir&gt;/cgi/monitorix.conf.path</i> that includes the absolute path of the configuration file. This file will be read by <code>monitorix.cgi</code> to determine the exact location of the configuration file.</p>
<h2>Configuration Options</h2>
<p>Blank lines are ignored, and whitespace before and after a token or value is ignored as well as tabulators, although a value can contain whitespace within. Lines which begin with a # are considered comments and ignored. </p>
<p> If you want to comment out a large block you can use C-style comments. A /* signals the begin of a comment block and the */ signals the end of the comment block. </p>
<p> If an option has multiple values their must be separated by comma. </p>
<p> <code>title</code></p>
<dl>
<dd>A free description of the server; where it is located, the Company name, etc. </p>
<p> Default value: <i>Place a Title Here</i></dl>
<p> <code>hostname</code></p>
<dl>
<dd>The name of the host. </p>
<p> Default value:</dl>
<p> <code>theme_color</code></p>
<dl>
<dd>RRDtool comes with a default white theme, and since Monitorix introduces its own black theme, you have two predefined themes to choose from. </p>
<p> Default value: <i>black</i></dl>
<p> <code>refresh_rate</code></p>
<dl>
<dd>The refresh rate (in seconds) of the statistics web page displayed in your browser. If set to 0, page refreshing is disabled. </p>
<p> Default value: <i>150</i></dl>
<p> <code>iface_mode</code></p>
<dl>
<dd>The interface mode defines the manner in which data is shown in the browser. Since version 1.4.0 it has been possible to display the graphic data using plain text tables. This allows Monitorix to be used by those running screen reader software, and also simplifies automatic data processing through scripts. </p>
<p> The possible values are:</p>
<dl>
<dd><i>graph</i> for rendered graphs.<br />
 <i>text</i> for plain text representation.</dl>
<p> Default value: <i>graph</i></dl>
<p> <code>enable_zoom</code></p>
<dl>
<dd>Zoom allows double clicking any graph in order to see a larger version (zoomed in). This is especially useful for seeing additional detail. </p>
<p> Default value: <i>y</i></dl>
<p> <code>netstats_in_bps</code></p>
<dl>
<dd>This option toggles network values between bits (bps) and Bytes (Bps) per second. By default the values will be shown in Bytes per second (Bps). </p>
<p> Default value: <i>n</i></dl>
<p> <code>disable_javascript_void</code></p>
<dl>
<dd>This option enables or disables the use of javascript:void-URLs when opening windows with zoomed graphs. Some people likes to open links in the background by pressing the middle mouse button in Firefox, and with the default javascript:void-URLs the only they get is an empty window with nothing in it. </p>
<p> Default value: <i>n</i></dl>
<p> <code>temperature_scale</code></p>
<dl>
<dd>This option toggles between values in Celsius or in Fahrenheit in those graphs that represent temperatures. </p>
<p> The possible values are:</p>
<dl>
<dd><i>c</i> for Celsius.<br />
 <i>f</i> for Fahrenheit.</dl>
<p> Default value: <i>c</i></dl>
<p> <code>show_gaps</code></p>
<dl>
<dd>This option, when enabled, shows the gaps (missing data) in the graphs. This is specially useful to detect if the server or Monitorix were stopped for a while, or any other unavailability. </p>
<p> In order to be able to locate those gaps easily in each graph, it uses the white color in the default black theme and the black color in the white theme. These default colors are defined in <i>monitorix.conf</i> so they can be changed as any other option. </p>
<p> Default value: <i>n</i></dl>
<p> <code>global_zoom</code></p>
<dl>
<dd>This option zooms all the graphs (including the legend&#8217;s font size) by the given amount. The factor must be greater than 0 and it accepts decimal values. </p>
<p> This is specially useful for people with big screens that either want to avoid using the browser feature to zoom the contents of the window and for those that watch the graphs from certain distance. </p>
<p> Keep in mind that the contents of the graphs remains with the same detail level all the time, and that it doesn&#8217;t affects to the standard zoomed graph that appears when clicking in the picture. </p>
<p> Default value: <i>1</i></dl>
<p> <code>max_historic_years</code></p>
<dl>
<dd>This option defines the maximum number of years of historical data in all graphs. </p>
<p> WARNING: Every time this value is extended Monitorix will resize every <i>.rrd</i> file accordingly, removing all historical data. </p>
<p> There is no longer any upper limit for this value. </p>
<p> Default value: <i>1</i></dl>
<p> <code>accept_selfsigned_certs</code></p>
<dl>
<dd>This option forces to accept self-signed certificates when collecting values remotely using HTTPS protocol. </p>
<p> Default value: <i>y</i></dl>
<p> <code>priority</code></p>
<dl>
<dd>Sometimes when a server is under heavy use, Monitorix might be unable to collect some statistical data due to its normal priority (0 by default). This makes monitoring useless because graphs are empty during that hard period of time. </p>
<p> In order to mitigate this situation this option sets the priority in which Monitorix will be scheduled by the kernel. The accepted range of values is the same as in the <i>setpriority()</i> system call: that is, from -20 (maximum priority) to 19 (lowest priority). </p>
<p> Default value: <i>0</i></dl>
<p> <code>image_format</code></p>
<dl>
<dd>This is the format of each generated graph. There are only two possible values: <i>PNG</i> and <i>SVG</i>. </p>
<p> Default value: <i>PNG</i></dl>
<p> <code>include_dir</code></p>
<dl>
<dd>The main configuration file is usually called <i>monitorix.conf</i> and its location is provided as part of the command line arguments. In addition, other configuration files may be loaded placing them in the directory pointed by this option. The names must end with .conf to be included. </p>
<p> This option is mainly intended to include third-party modules with their own configuration files without having to modify any file from your Monitorix installation. All modules are located in <i>/usr/lib/monitorix</i> (in some operating systems that path can change). </p>
<p> All the configuration files in there will be loaded in alphabetic order, so the last file loaded will overwrite any previous option. </p>
<p> Default value: <i>/etc/monitorix/conf.d</i></dl>
<p> <code>ip_default_table</code></p>
<dl>
<dd>This option will define in which table Monitorix will put all <i>iptables</i> rules for network traffic accounting monitoring. It only works on Linux. </p>
<p> Although this is a global option, only the graphs <i>port</i>, <i>nginx</i> and <i>traffacct</i> are affected by it. </p>
<p> Default value: <i>filter</i></dl>
<p> <code>ipv6_disabled</code></p>
<dl>
<dd>This option enables or disables the use of the <i>ip6tables</i> command. It only works on Linux. </p>
<p> Although this is a global option, only the graph <i>port</i> is currently affected by it. </p>
<p> Default value: <i>n</i></dl>
<p> <code>url_prefix_proxy</code></p>
<dl>
<dd>This option forces <i>monitorix.cgi</i> to bypass the URL building. This is specially usefull when Monitorix is used behind a reverse proxy. </p>
<p> An example would be: <i><a rel="nofollow" href="http://myexternalwebsite.com">http://myexternalwebsite.com</a></i> </p>
<p> Default value:</dl>
<p> <code>enable_hourly_view</code></p>
<dl>
<dd>This option enables or disables the ability to select the hourly view in the main page. </p>
<p> No .rrd file will change by selecting this option and the historical data won&#8217;t be affected. </p>
<p> Default value: <i>n</i></dl>
<p> <code>user_agent_id</code></p>
<dl>
<dd>This option defines the string to be used to identify Monitorix in the HTTP requests. Its value will be sent as the &quot;User-Agent&quot; header. </p>
<p> The default value will depend on the current Perl version in your system. An example would be <i>libwww-perl/5.833</i>.</dl>
<p> <code>base_dir</code></p>
<dl>
<dd>This is the absolute path to the directory where all the web elements are located: </p>
<dl>
<dd><i>cgi/</i> directory where resides <code>monitorix.cgi</code>.<br />
 <i>imgs/</i> directory for the .png graph images.<br />
 <i>index.html</i> Monitorix main page.<br />
 <i>logo_bot.png</i> Monitorix bottom logo.<br />
 <i>logo_top.png</i> Monitorix top logo.<br />
 <i>monitorixico.png</i> Monitorix favicon logo.</dl>
<p> Default value: <i>/var/lib/monitorix/www/</i><br />
 (depends on the operating system)</dl>
<p> <code>base_lib</code></p>
<dl>
<dd>This is the absolute path to the directory where all of the monthly reports, daily traffic usage, and RRD files are located: </p>
<dl>
<dd><i>reports/</i> monthly reports localization directory.<br />
 <i>usage/</i> daily traffic usage data directory.<br />
 <i>*.rrd</i> RRD files.</dl>
<p> Default value: <i>/var/lib/monitorix/</i><br />
 (depends on the operating system)</dl>
<p> <code>base_url</code></p>
<dl>
<dd>This is the URL prefix that Monitorix utilizes when refering to its own pages and files. </p>
<p> Default value: <i>/monitorix</i></dl>
<p> <code>base_cgi</code></p>
<dl>
<dd>This is the URL prefix that Monitorix utilizes when refering to <code>monitorix.cgi</code>. </p>
<p> Default value: <i>/monitorix-cgi</i></dl>
<h3>Built-in HTTP server</h3>
<p><code>enabled</code></p>
<dl>
<dd>This enables or disables the HTTP server that Monitorix has built-in. This is specially useful for system administrators that don&#8217;t want to install a web server (Apache, Lighttpd, Nginx, etc.) to see the Monitorix graphs. </p>
<p> Default value: <i>y</i></dl>
<p> <code>host</code></p>
<dl>
<dd>This option takes an optional host address for this server to bind to. If none is specified (default) it will bind to all interfaces. </p>
<p> Default value:</dl>
<p> <code>port</code></p>
<dl>
<dd>This is the network port from where the HTTP server will listen on. </p>
<p> Default value: <i>8080</i></dl>
<p> <code>user/group</code></p>
<dl>
<dd>This sets the user and group that the HTTP server will run as. </p>
<p> Default value for user: <i>nobody</i><br />
 Default value for group: <i>nobody</i></dl>
<p> <code>log_file</code></p>
<dl>
<dd>This is the path to the HTTP server log file. </p>
<p> Default value: <i>/var/log/monitorix-httpd</i></dl>
<p> <code>hosts_deny</code></p>
<dl>
<dd>This is a comma delimited set of IP addresses which are not permitted to access Monitorix graphs. There is the special keyword called <i>all</i> that can be used to deny all IP addresses. </p>
<p> The access control uses the same approach as in the TCP-Wrappers; the search stops at the first match: </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>&#8211; Access will be granted when an IP address matches an entry in the <code>hosts_allow</code> list.</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>&#8211; Otherwise, access will be denied when an IP address matches an entry in the <code>hosts_deny</code> list.</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>&#8211; Otherwise, access will be granted.</p>
<p> Default value:</dl>
<p> <code>hosts_allow</code></p>
<dl>
<dd>This is the opposite of <code>hosts_deny</code> option. IP addresses listed here are permitted to access Monitorix graphs. There is also the special keyword called <i>all</i> that can be used to allow access to all IP addresses. </p>
<p> Default value:</dl>
<p> <code>https_url</code></p>
<dl>
<dd>This will force to use the prefix <i>https://</i> in all links. This is special useful if you plan to use a reverse-proxy HTTPS server in front of the Monitorix built-in HTTP. </p>
<p> Default value: n</dl>
<h3>Built-in HTTP server with access authentication</h3>
<p><code>enabled</code></p>
<dl>
<dd>This enables or disables the authentication mechanism to control access to pages and other resources. The only allowed mechanism is Basic and uses the 401 status code and the WWW-Authenticate response header. </p>
<p> It&#8217;s highly recommended to set this option according your needs before start Monitorix. </p>
<p> For more information about the Basic access authentication mechanism and its security implications, please refer to <a rel="nofollow" href="http://en.wikipedia.org/wiki/Basic_access_authentication.">http://en.wikipedia.org/wiki/Basic_access_authentication.</a> </p>
<p> Default value: <i>n</i></dl>
<p> <code>msg</code></p>
<dl>
<dd>This option sets the <i>Realm</i> to be used in the authentication. That message should appear in the client dialog box to help user to identify the secure area. </p>
<p> Default value: <i>Monitorix: Restricted access</i></dl>
<p> <code>htpasswd</code></p>
<dl>
<dd>This option sets the path to the password file that was created with the help of the <i>htpasswd.pl</i> script. That script encrypts and validates passwords using the system&#8217;s crypt() routine. If your Monitorix package doesn&#8217;t come with that script, you may use the similar <i><a href="/docs/linux/man/1-htpasswd/">htpasswd</a></i>(1) program provided with the Apache web server. </p>
<p> The format of the password file consist of one or more lines with a username and password separated by a colon. </p>
<p> The following is an example of a password file: </p>
<p> paul:oGkEsQK6RYIII<br />
 peter:HF1r7qRL4Kg6E </p>
<p> Since the script uses the crypt() algorithm, only the first 8 characters of the password are used to form the password. If the supplied password is longer, the extra characters will be silently discarded. </p>
<p> WARNING: don&#8217;t use the character colon &#8216;:&#8217; as part of your name or password since this character is used as field separator. </p>
<p> Default value: <i>/var/lib/monitorix/htpasswd</i></dl>
<h3>Log files pathnames</h3>
<p><code>log_file</code></p>
<dl>
<dd>This is the path to the Monitorix log file. Please check this file periodically and especially after every update to confirm proper operation. </p>
<p> Default value: <i>/var/log/monitorix</i></dl>
<p> <code>secure_log</code></p>
<dl>
<dd>This is the path to the system log (also known as <i>auth.log</i>, etc.) Monitorix uses this file to report SSH, POP3, FTP and Telnet successful logins. </p>
<p> Default value: <i>/var/log/secure</i></dl>
<p> <code>mail_log</code></p>
<dl>
<dd>This is the path to the mail log file. Monitorix uses this file to report messages sent (supporting Sendmail and Postfix formats), and the MailScanner log format for spam-mail and virus-mail alerts. </p>
<p> Default value: <i>/var/log/maillog</i></dl>
<p> <code>milter_gl</code></p>
<dl>
<dd>This is the path to the dump file of <i>milter-greylist</i>. </p>
<p> Default value: <i>/var/milter-greylist/greylist.db</i></dl>
<p> <code>imap_log</code></p>
<dl>
<dd>This is the path to the IMAP (Dovecot or UW-IMAP) log file. Monitorix uses this file to report IMAP and POP3 successful logins. </p>
<p> Default value: <i>/var/log/imap</i></dl>
<p> <code>hylafax_log</code></p>
<dl>
<dd>This is the path to the Hylafax log file. Monitorix uses this file to report successful FAX dispatches. </p>
<p> Default value: <i>/var/spool/hylafax/etc/xferfaxlog</i></dl>
<p> <code>cups_log</code></p>
<dl>
<dd>This is the path to the CUPS page log file. Monitorix uses this file to report on print jobs. </p>
<p> Default value: <i>/var/log/cups/page_log</i></dl>
<p> <code>ftp_log</code></p>
<dl>
<dd>This is the path to the FTP server (ProFTPD, vsftpd or Pure-FTPd) log. Monitorix uses this file to report FTP successful logins and other FTP-related information. </p>
<p> Default value: <i>/var/log/proftpd/access.log</i></dl>
<p> <code>fail2ban_log</code></p>
<dl>
<dd>This is the path to the Fail2ban log file. Monitorix uses this file to report IP addresses banned. </p>
<p> Default value: <i>/var/log/fail2ban.log</i></dl>
<p> <code>spamassassin_log</code></p>
<dl>
<dd>This is the path to the Spamassassin log file. Monitorix uses this file to report spam-mail alerts. </p>
<p> Default value: <i>/var/log/maillog</i></dl>
<p> <code>clamav_log</code></p>
<dl>
<dd>This is the path to the Clamav log file. Monitorix uses this file to report virus-mail alerts. </p>
<p> Default value: <i>/var/log/clamav/clamav.log</i></dl>
<p> <code>cg_logdir</code></p>
<dl>
<dd>This is the path to the CommuniGate logs directory. Monitorix uses these files to report the number of mail messages successfully received and sent, and to report IMAP and POP3 successful logins. </p>
<p> Default value: <i>/var/CommuniGate/SystemLogs/</i></dl>
<p> <code>squid_log</code></p>
<dl>
<dd>This is the path to the Squid log file. Monitorix uses this file to report on Squid Proxy requests. </p>
<p> Default value: <i>/var/log/squid/access.log</i></dl>
<p> <code>imap_log_date_format</code></p>
<dl>
<dd>This is the Dovecot date format as it appears in the <code>imap_log</code> file. </p>
<p> Default value: <i>%b %d</i></dl>
<p> <code>secure_log_date_format</code></p>
<dl>
<dd>This is <i>secure_log</i> date format. </p>
<p> Default value: <i>%b %e</i></dl>
<h3>Piwik tracking code</h3>
<p><code>enabled</code></p>
<dl>
<dd>This enables the inclusion of the Piwik tracking code in the main <i>index.html</i> file. Please refer to <a rel="nofollow" href="http://piwik.org/docs/tracking-api/">http://piwik.org/docs/tracking-api/</a> for more information on how to fill these fields. </p>
<p> Default value: <i>n</i></dl>
<h3>Enable or disable graphs</h3>
<p><code>graph_enable</code></p>
<dl>
<dd>This enables or disables the monitoring of each graph. Placing a <i>y</i> on a desired graph and restarting Monitorix will automatically create the RRD file for that graph and start gathering information according to its settings.</dl>
<h3>System load average and usage (system.rrd)</h3>
<p><code>loadavg_enabled</code></p>
<dl>
<dd>This section enables or disables the alert capabilities for this graph. Only the alert for the average CPU load is currently implemented. It works as follows: </p>
<p> The CPU load average uses the third value (the one that represents the last 15 minutes of the load average), and if it reaches the <code>loadavg_threshold</code> value for the interval of time defined in <code>loadavg_timeintvl</code>, Monitorix will execute the external alert script defined in <code>loadavg_script</code>. </p>
<p> The default Monitorix installation includes an example of a shell-script alert called <code>monitorix-alert.sh</code> which you can use as a base for your own script. </p>
<p> Default value: <i>n</i></dl>
<p> <code>loadavg_timeintvl</code></p>
<dl>
<dd>This is the period of time (in seconds) that the threshold needs to be exceeded before the external alert script is executed. </p>
<p> Default value: <i>3600</i></dl>
<p> <code>loadavg_threshold</code></p>
<dl>
<dd>This is the value that needs to be reached or exceeded within the specified time period in <code>loadavg_timeintvl</code> to trigger the mechanism for a particular action, which in this case is the execution of an external alert script. </p>
<p> The value of this option is compared against the last 15 minutes of CPU load average. </p>
<p> Default value: <i>5.0</i></dl>
<p> <code>loadavg_script</code></p>
<dl>
<dd>This is the full path name of the script that will be executed by this alert. </p>
<p> It will receive the following three parameters: </p>
<p> 1st &#8211; the value currently defined in <code>loadavg_timeintvl</code>.<br />
 2nd &#8211; the value currently defined in <code>loadavg_threshold</code>.<br />
 3rd &#8211; the current 15min CPU load average. </p>
<p> Default value: <i>/path/to/script.sh</i></dl>
<h3>Global kernel usage (kern.rrd)</h3>
<p>Note that the VFS graph is just informative of how the kernel is balancing its tables. <code>graph_mode</code></p>
<dl>
<dd>This changes the layout of the kernel usage graph, the possible values are <i>r</i> for a real graph, or <i>s</i> for a stacked graph (every line or area is stacked on top of the previous element). </p>
<p> Default value: <i>r</i></dl>
<p> <code>list</code></p>
<dl>
<dd>This is the list of values offered in modern Linux kernels. Older Linux kernels or other Operating Systems may not have all of them. Placing a <i>y</i> or an <i>n</i> will enable or disable the value in the graph.</dl>
<h3>Kernel usage per processor (proc.rrd)</h3>
<p><code>max</code></p>
<dl>
<dd>This is the number of processors or cores that your system has. There is no limit, however keep in mind that every time this number is changed Monitorix will resize the <i>proc.rrd</i> file accordingly, removing all historical data. </p>
<p> Default value: <i>4</i></dl>
<p> <code>graphs_per_row</code></p>
<dl>
<dd>This is the number of processor graphs that will be put in a row. Consider the interaction of this parameter with the <code>size</code> and <code>data</code> options (below) in order to adjust the size and number of graphs in relation to your horizontal screen size. </p>
<p> Default value: <i>2</i></dl>
<p> <code>size</code></p>
<dl>
<dd>This option sets the size of all processors graphs. </p>
<p> The possible values are:</p>
<dl>
<dd><i>main</i> for 450&#215;150 graphs.<br />
 <i>medium</i> for 325&#215;150 graphs.<br />
 <i>medium2</i> for 325&#215;70 graphs.<br />
 <i>small</i> for 200&#215;66 graphs.<br />
 <i>mini</i> for 183&#215;66 graphs.<br />
 <i>tiny</i> for 110&#215;40 graphs.</dl>
<p> Default value: <i>medium</i></dl>
<p> <code>DATA</code></p>
<dl>
<dd>This option will completely enable or disable the legend in the processor graphs. </p>
<p> Default value: <i>y</i></dl>
<h3>HP ProLiant System Health (hptemp.rrd)</h3>
<p><code>list</code></p>
<dl>
<dd>This list will hold the defined temperature sensors for each graph. You must have installed the command <i>hplog</i> that comes with HP ProLiant System Health Application and Command Line Utilities. </p>
<p> Each graph has a limited number of IDs: </p>
<p> <code>graph_0</code> up to 8 IDs.<br />
 <code>graph_1</code> up to 6 IDs.<br />
 <code>graph_2</code> up to 6 IDs. </p>
<p> The following is a configuration example of selected IDs: </p>
<p> # hplog -t<br />
 ID TYPE LOCATION STATUS CURRENT THRESHOLD </p>
<p>&nbsp;<wbr>1&nbsp;<wbr>&nbsp;<wbr>Basic Sensor Ambient&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Normal&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>75F/&nbsp;<wbr>24C 107F/&nbsp;<wbr>42C&nbsp;<wbr> </p>
<p>&nbsp;<wbr>2&nbsp;<wbr>&nbsp;<wbr>Basic Sensor CPU&nbsp;<wbr>(1)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Normal&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>104F/&nbsp;<wbr>40C 179F/&nbsp;<wbr>82C&nbsp;<wbr> </p>
<p>&nbsp;<wbr>3&nbsp;<wbr>&nbsp;<wbr>Basic Sensor CPU&nbsp;<wbr>(2)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Normal&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8212;F/&#8212;C 179F/&nbsp;<wbr>82C&nbsp;<wbr> </p>
<p>&nbsp;<wbr>4&nbsp;<wbr>&nbsp;<wbr>Basic Sensor Memory Board&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Normal&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8212;F/&#8212;C 188F/&nbsp;<wbr>87C&nbsp;<wbr> </p>
<p>&nbsp;<wbr>5&nbsp;<wbr>&nbsp;<wbr>Basic Sensor Memory Board&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Normal&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>82F/&nbsp;<wbr>28C 188F/&nbsp;<wbr>87C&nbsp;<wbr> </p>
<p>&nbsp;<wbr>6&nbsp;<wbr>&nbsp;<wbr>Basic Sensor Memory Board&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Normal&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8212;F/&#8212;C 188F/&nbsp;<wbr>87C&nbsp;<wbr> </p>
<p>&nbsp;<wbr>7&nbsp;<wbr>&nbsp;<wbr>Basic Sensor System Board&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Normal&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>89F/&nbsp;<wbr>32C 192F/&nbsp;<wbr>89C&nbsp;<wbr> </p>
<p>&nbsp;<wbr>8&nbsp;<wbr>&nbsp;<wbr>Basic Sensor System Board&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Normal&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8212;F/&#8212;C 192F/&nbsp;<wbr>89C&nbsp;<wbr> </p>
<p>&nbsp;<wbr>9&nbsp;<wbr>&nbsp;<wbr>Basic Sensor System Board&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Normal&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>84F/&nbsp;<wbr>29C 192F/&nbsp;<wbr>89C&nbsp;<wbr><br />
 10 Basic Sensor System Board Normal 118F/ 48C 230F/110C<br />
 11 Basic Sensor System Board Normal 96F/ 36C 192F/ 89C<br />
 12 Basic Sensor System Board Normal 84F/ 29C 154F/ 68C<br />
 13 Basic Sensor System Board Normal 87F/ 31C 154F/ 68C<br />
 14 Basic Sensor System Board Normal 89F/ 32C 156F/ 69C<br />
 15 Basic Sensor System Board Normal 93F/ 34C 161F/ 72C<br />
 16 Basic Sensor Ambient Normal &#8212;F/&#8212;C 192F/ 89C<br />
 17 Basic Sensor System Board Normal &#8212;F/&#8212;C 192F/ 89C<br />
 18 Basic Sensor SCSI Backplane Normal 32F/ 0C 140F/ 60C </p>
<dl>
<dd>&lt;list&gt;<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>graph_0 = 2, 3</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>graph_1 = 1, 5, 18</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>graph_2 = 7, 9, 10, 11, 12, 13</p>
<p> &lt;/list&gt;</dl>
</dl>
<h3>LM-Sensors and GPU temperatures (lmsens.rrd)</h3>
<p><code>list</code></p>
<dl>
<dd>In this list you may specify the sensors you want to monitor with the same names as they appear in your <i><a href="/docs/linux/man/1-sensors/">sensors</a></i>(1) command. </p>
<p> For example, imagine a <i><a href="/docs/linux/man/1-sensors/">sensors</a></i>(1) output like this: </p>
<p> # sensors<br />
 coretemp-isa-0000<br />
 Adapter: ISA adapter<br />
 Core 0: +51.0°C (high = +78.0°C, crit = +100.0°C) </p>
<p> coretemp-isa-0001<br />
 Adapter: ISA adapter<br />
 Core 1: +49.0°C (high = +78.0°C, crit = +100.0°C) </p>
<p> f71882fg-isa-0a00<br />
 Adapter: ISA adapter<br />
 3.3V: +3.30 V<br />
 Vcore: +1.21 V (max = +2.04 V)<br />
 Vdimm: +1.82 V<br />
 Vchip: +1.38 V<br />
 +5V: +5.00 V<br />
 12V: +14.37 V<br />
 5VSB: +4.33 V<br />
 3VSB: +3.30 V<br />
 Battery: +3.22 V<br />
 CPU: 2035 RPM<br />
 System: 1765 RPM ALARM<br />
 Power: 2110 RPM ALARM<br />
 Aux: 2080 RPM ALARM<br />
 M/B Temp: +36.00 C<br />
 CPU Temp: +29.00 C </p>
<p> Then you may want to configure that <code>list</code> as: </p>
<dl>
<dd>&lt;list&gt;<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>core0 = Core 0</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>core1 = Core 1</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>mb0 = M/B Temp</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>cpu0 = CPU Temp</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>fan0 = CPU</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>fan1 = System</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>fan2 = Power</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>fan3 = Aux</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>volt0 = 3.3V</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>volt1 = VCore</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>volt2 = Vdimm</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>volt3 = Vchip</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>volt4 = \+5V</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>volt5 = 12V</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>volt6 = 5VSB</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>volt7 = 3VSB</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>volt8 = Battery</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>gpu0 = nvidia</p>
<p> &lt;/list&gt;</dl>
<p> Note that you need to escape the plus and minus signs in the voltage labels. It also recommended to enclose the values using double quotes. </p>
<p> The last one, <i>gpu0</i>, is set here just in case you have a supported graphics card and want to monitor its temperature. Currently only NVIDIA and ATI graphic cards are supported; with the values <i>nvidia</i> and <i>ati</i> respectively. It requires the official NVIDIA or ATI drivers. </p>
<p> This list has the following maximums allowed: </p>
<dl>
<dd>Up to 16 <i>core</i> keys (from core0 to core15).<br />
 Up to 2 <i>mb</i> keys (mb0 and mb1).<br />
 Up to 4 <i>cpu</i> keys (from cpu0 to cpu3).<br />
 Up to 9 <i>fan</i> keys (from fan0 to fan8).<br />
 Up to 12 <i>volt</i> keys (from volt0 to volt11).<br />
 Up to 9 <i>gpu</i> keys (from gpu0 to gpu8).</dl>
</dl>
<p> <code>desc</code></p>
<dl>
<dd>This list complements the <code>list</code> option only for the graphs: MB and CPU temperatures, Fans speeds and GPU temperatures. It basically allows you to change the name that will appear in the graph, hiding the real name of the sensor. If no association is defined, then Monitorix will display the name of the key (left side) in the <code>desc</code> option (in uppercase). </p>
<dl>
<dd>&lt;desc&gt;<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>mb0 = M/B</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>fan0 = CPUFan</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>gpu0 = ATI</p>
<p> &lt;/desc&gt;</dl>
<p> Please note that in the default graph all names are limited to 5 characters in order to fit up to 9 different values. In the zoomed graphs the limit is 8 characters.</dl>
<h3>Generic sensors statistics (gensens.rrd)</h3>
<p>This graph is able to monitor up to 9 temperatures and CPU frequencies which, depending of your machine, should appear in the <i>/sys/devices</i> directory. </p>
<p> <code>list</code></p>
<dl>
<dd>This is a fixed list that can only hold two keys (0 and 1). Each key though can hold up to 9 different entries separated by comma which corresponds to the names of the sensors present in your computer. The key 0 is only for temperature sensors and the key 1 is for CPU frequencies. All this is hard-coded and a bit rigid currently but it might change in the future. </p>
<p> An example would be: </p>
<dl>
<dd>&lt;list&gt;<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>0 = temp0, temp1</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>1 = cpu0, cpu1, cpu2, cpu3</p>
<p> &lt;/list&gt;</dl>
</dl>
<p> <code>desc</code></p>
<dl>
<dd>In this option you must associate the complete pathname of the file from where to get the value of each entry defined in the <i>Blist</i>. Following the settings in the example above: </p>
<dl>
<dd>&lt;desc&gt;<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>temp0 = /sys/devices/virtual/thermal/thermal_zone0/temp</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>temp1 = /sys/devices/virtual/thermal/thermal_zone1/temp</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>cpu0 = /sys/devices/system/cpu/cpu0/cpufreq/scaling_cur_freq</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>cpu1 = /sys/devices/system/cpu/cpu1/cpufreq/scaling_cur_freq</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>cpu2 = /sys/devices/system/cpu/cpu2/cpufreq/scaling_cur_freq</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>cpu3 = /sys/devices/system/cpu/cpu3/cpufreq/scaling_cur_freq</p>
<p> &lt;/desc&gt;</dl>
</dl>
<p> <code>unit</code></p>
<dl>
<dd>With this option you can define the order of magnitude associated to a specific value. This is used in both temperatures and CPU frequencies, since this kind of temperature sensors tend to give the value in 1000ths of degrees Celsius. In the case of CPU frequencies the values come in Mhz which means that they need to be converted to Hz by multiplying them by 1000. Therefore you can define something like this: </p>
<dl>
<dd>&lt;unit&gt;<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>temp0 = 1000</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>temp1 = 1000</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>cpu0 = 0.001</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>cpu1 = 0.001</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>cpu2 = 0.001</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>cpu3 = 0.001</p>
<p> &lt;/unit&gt;</dl>
</dl>
<p> <code>map</code></p>
<dl>
<dd>With this option you can optionally rename any of the sensor names defined in the <code>list</code> option. Following the above example: </p>
<dl>
<dd>&lt;map&gt;<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>temp0 = Temperature Zone 0</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>temp1 = Temperature Zone 1</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>cpu0 = CPU0 frequency</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>cpu1 = CPU1 frequency</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>cpu2 = CPU2 frequency</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>cpu3 = CPU3 frequency</p>
<p> &lt;/map&gt;</dl>
<p> All the names are limited to 20 characters.</dl>
<h3>NVIDIA temperatures and usage (nvidia.rrd)</h3>
<p>This graph requires to have installed the official NVIDIA drivers. </p>
<p> <code>max</code></p>
<dl>
<dd>This is the number of NVIDIA cards currently plugged in your system. </p>
<p> The maximum allowed is 9. </p>
<p> Default value: <i>1</i></dl>
<h3>Disk drive temperatures and health (disk.rrd)</h3>
<p>This graph is able to monitor an unlimited number of disk drives. </p>
<p> <code>list</code></p>
<dl>
<dd>This is a list of groups of disk drives that you want to monitor. Each group will become a graph and there may be an unlimited number of groups. You can define device names or paths to devices like <i>/dev/disk/by-path/pci-0000:00:11.0-scsi-0:0:0:0</i>. </p>
<p> WARNING: Every time the number of groups in this option changes, Monitorix will resize the <i>disk.rrd</i> file accordingly, removing all historical data. </p>
<p> To collect the disk drive temperatures and health the <i>smartmontools</i> or the <i>hddtemp</i> command are required. </p>
<p> It is recommended that you first check if either <i><a href="/docs/linux/man/8-smartctl/">smartctl</a></i>(8) or <i>hddtemp</i> are able to collect data from the disk drive(s) that you plan to monitor. You may test this with the following command: </p>
<dl>
<dd># hddtemp /dev/sdb<br />
 /dev/sdb: WDC WD1600AABS-00M1A0: 48°C </p>
</dl>
<p> If you see good results as above, you can add it to the group 0 like this: </p>
<dl>
<dd>&lt;list&gt;<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>0 = /dev/sda, /dev/sdb</p>
<p> &lt;/list&gt;</dl>
<p> The maximum number of disk device names allowed per group is 8.</dl>
<p> <code>realloc_enabled</code></p>
<dl>
<dd>This section enables or disables one of the alert capabilities for this graph; the alert for the number of reallocated sectors in disk. It works as follows: </p>
<p> If the number of reallocated sectors in any of the specified disk device names reaches the <code>realloc_threshold</code> (the interval of time is not used here), Monitorix will execute the external alert script defined in <code>realloc_script</code>. </p>
<p> The default Monitorix installation includes an example of a shell-script alert called <code>monitorix-alert.sh</code> which you can use as a base for your own script. </p>
<p> Default value: <i>n</i></dl>
<p> <code>realloc_timeintvl</code></p>
<dl>
<dd>Not used in this alert. </p>
<p> Default value: <i>0</i></dl>
<p> <code>realloc_threshold</code></p>
<dl>
<dd>This is the value that needs to be reached or exceeded to trigger the mechanism for a particular action, which in this case is the execution of an external alert script. </p>
<p> Default value: <i>1</i></dl>
<p> <code>realloc_script</code></p>
<dl>
<dd>This is the full path name of the script that will be executed by this alert. </p>
<p> It will receive the following three parameters: </p>
<p> 1st &#8211; the value currently defined in <code>realloc_timeintvl</code>.<br />
 2nd &#8211; the value currently defined in <code>realloc_threshold</code>.<br />
 3rd &#8211; the current number of reallocated sectors. </p>
<p> Default value: <i>/path/to/script.sh</i></dl>
<p> <code>pendsect_enabled</code></p>
<dl>
<dd>This section enables or disables one of the alert capabilities for this graph; the alert for the number of current pending sectors (or bad sectors) in disk. It works as follows: </p>
<p> If the number of current pending sectors in any of the specified disk device names reaches the <code>pendsect_threshold</code> (the interval of time is not used here), Monitorix will execute the external alert script defined in <code>pendsect_script</code>. </p>
<p> The default Monitorix installation includes an example of a shell-script alert called <code>monitorix-alert.sh</code> which you can use as a base for your own script. </p>
<p> Default value: <i>n</i></dl>
<p> <code>pendsect_timeintvl</code></p>
<dl>
<dd>Not used in this alert. </p>
<p> Default value: <i>0</i></dl>
<p> <code>pendsect_threshold</code></p>
<dl>
<dd>This is the value that needs to be reached or exceeded to trigger the mechanism for a particular action, which in this case is the execution of an external alert script. </p>
<p> Default value: <i>1</i></dl>
<p> <code>pendsect_script</code></p>
<dl>
<dd>This is the full path name of the script that will be executed by this alert. </p>
<p> It will receive the following three parameters: </p>
<p> 1st &#8211; the value currently defined in <code>pendsect_timeintvl</code>.<br />
 2nd &#8211; the value currently defined in <code>pendsect_threshold</code>.<br />
 3rd &#8211; the current number of pending sectors. </p>
<p> Default value: <i>/path/to/script.sh</i></dl>
<p> <code>accept_invalid_disk</code></p>
<dl>
<dd>During the init stage this graph verifies that every defined device name does exist in the system. If not, then the graph disables itself. </p>
<p> This option changes this behavior and permits to continue working even if the device names defined doesn&#8217;t exist. Keep in mind that you will continue seeing error messages in the logfile. </p>
<p> Default value: <i>n</i></dl>
<h3>Filesystem usage and I/O activity (fs.rrd)</h3>
<p>This graph is able to monitor an unlimited number of filesystems. </p>
<p> <code>list</code></p>
<dl>
<dd>This is a list of groups of mounted filesystems that you want to monitor. Each group will become a graph and there may be an unlimited number of groups. </p>
<p> WARNING: Every time the number of groups in this option changes, Monitorix will resize the <i>fs.rrd</i> file accordingly, removing all historical data. </p>
<p> Take special care to use the same name as appears in the output of the <i><a href="/docs/linux/man/1-df/">df</a></i>(1) command (the <i>swap</i> device is a special case). An example would be: </p>
<dl>
<dd>&lt;list&gt;<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>0 = /, swap, boot, home, /mnt/backup</p>
<p> &lt;/list&gt;</dl>
<p> The maximum number of filesystems allowed per group is 8.</dl>
<p> <code>desc</code></p>
<dl>
<dd>This list complements the <code>list</code> option. It basically allows you to change the name that will appear in the graph, hiding the real name of the mount point. If no association is defined, then Monitorix will display the name specified in the <code>list</code> option. </p>
<dl>
<dd>&lt;desc&gt;<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/ = Root FS</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/home = My Home</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/mnt/backup = Backups</p>
<p> &lt;/desc&gt;</dl>
<p> You can define as much entries as you want.</dl>
<p> <code>devmap</code></p>
<dl>
<dd>This optional list complements the <code>list</code> option. When Monitorix is started, and in order to be able to show I/O activity, it attempts to detect the mapping of devices specified in <code>list</code>, as defined in the <i>df</i> command output column &quot;Mounted on&quot;. In the event that devices are not detected by Monitorix, the <code>devmap</code> option shall be used to manually define them, according to the underlying OS: </p>
<dl>
<dd>Linux (kernel &gt; 2.4)</p>
<dl>
<dd>&lt;devmap&gt; device must match a device listed in the &quot;/proc/diskstats&quot; file.</dl>
</dl>
<dl>
<dd>Linux (kernel &lt;= 2.4)</p>
<dl>
<dd>&lt;devmap&gt; is not used, but because something is defined in &lt;devmap&gt;, Monitorix will extract &quot;disk_io&quot; lines from the &quot;/proc/stat&quot; file.</dl>
</dl>
<dl>
<dd>FreeBSD</p>
<dl>
<dd>&lt;devmap&gt; device recognized by the output of &quot;iostat -xI &lt;dev&gt;&quot; command.</dl>
</dl>
<dl>
<dd>OpenBSD and NetBSD</p>
<dl>
<dd>&lt;devmap&gt; is not used, but because something is defined in &lt;devmap&gt;, Monitorix will use the output of &quot;iostat -DI&quot; command.</dl>
</dl>
<p> Just an example:</p>
<dl>
<dd>&lt;devmap&gt;<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/mnt/home = dm-1</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/mnt/backup = cciss/c0d2p6</p>
<p> &lt;/devmap&gt;</dl>
<p> You can define as much entries as you want.</dl>
<p> <code>alerts</code></p>
<dl>
<dd>This optional list enables the alert capabilities for this graph and complements with the <code>list</code> option. Each alert has three fields separated by comma: the <i>time interval</i>, the <i>threshold</i> and the path to the <i>script</i> to be executed. </p>
<p> The <i>time interval</i> is the period of time (in seconds) that the <i>threshold</i> needs to be exceeded before the external script is executed. </p>
<p> The <i>threshold</i> is the percentage of disk space used in the file system that needs to be reached or exceeded within the specified time in <i>time interval</i> to execute the external script. </p>
<p> The <i>script</i> is the full path name of the script that will be executed by this alert. </p>
<p> Each defined filesystem has its own alert. </p>
<p> The default Monitorix installation includes an example of a shell-script alert called <i>monitorix-alert.sh</i> which you can use as a base for your own script. </p>
<p> The following is an example of an alert defined for the root filesystem: </p>
<dl>
<dd>&lt;alerts&gt;<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/ = 3600, 98, /path/to/script</p>
<p> &lt;/alerts&gt; </p>
</dl>
<p> Such alert means that if the percentage of disk space used in the root filesystem reaches or exceeds 98 (more than 98) during at least one hour (3600 seconds) the script in <i>/path/to/script</i> will be executed. </p>
<p> The external script will receive the following arguments: </p>
<dl>
<dd>1st &#8211; the value defined as <i>time interval</i>.<br />
 2nd &#8211; the value defined as <i>threshold</i>.<br />
 3rd &#8211; the filesystem disk usage. </p>
</dl>
</dl>
<h3>ZFS statistics (zfs.rrd)</h3>
<p>This graph is able to monitor an unlimited number of pools. </p>
<p> <code>max_pools</code></p>
<dl>
<dd>This is the maximum number of pools that you can define in <code>list</code>. There is no limit to the number of pools monitored, but keep in mind that every time this number changes, Monitorix will resize the <i>zfs.rrd</i> file accordingly, removing all historical data. </p>
<p> Default value: <i>5</i> </p>
</dl>
<p> <code>list</code></p>
<dl>
<dd>This is a comma-separated list of pool names. The number of pool names defined here can&#8217;t be greater than the number defined in <code>max_pools</code>.</dl>
<h3>Directory usage statistics (du.rrd)</h3>
<p>This graph is able to monitor the usage of an unlimited number of directories. </p>
<p> IMPORTANT NOTE: The <i>du</i> command makes intensive disk I/O access that might slow down the whole system. Moreover, continued executions of this command will affect the buffer cache mechanism and this will also increase its response time. </p>
<p> <code>list</code></p>
<dl>
<dd>This is a comma-separated list that describes the groups of directories in <code>desc</code>. Put one description for each group. For every group specified you need to specify its description in the <code>desc</code> option. </p>
<p> WARNING: Every time the number of entries in this option changes, Monitorix will resize the <i>du.rrd</i> file accordingly, removing all historical data. </p>
<p> An example would be: </p>
<p> list = System, Users</dl>
<p> <code>desc</code></p>
<dl>
<dd>This is a list of directories per group defined. </p>
<p> &lt;desc&gt;<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>0 = /var/spool/mail, /var/spool/mqueue, /etc, /var/ftp, /tmp</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>1 = /home/ace, /home/gene, /home/paul, /home/peter</p>
<p> &lt;/desc&gt; </p>
<p> The maximum number of directories allowed for each group is 9.</dl>
<p> <code>dirmap</code></p>
<dl>
<dd>This list complements the <code>list</code> option. It basically allows you to change the name that will appear in the graph, hiding the real name of the directory. If no association is defined, then Monitorix will display the name specified in the <code>list</code> option.</dl>
<p> <code>graphs_per_row</code></p>
<dl>
<dd>This is the number of graphs that will be put in a row. </p>
<p> Default value: <i>2</i></dl>
<p> <code>extra_args</code></p>
<dl>
<dd>This option includes any extra argument to the <i>du</i> command executed by Monitorix, which is &quot;du -ks&quot;. This is specially useful if you want to skip directories on differents file systems, in this case just define this option like this: </p>
<dl>
<dd>extra_args = &quot;-x&quot;</dl>
<p> IMPORTANT NOTICE: Keep in mind that including certain flags like &#8216;-h&#8217; (which gives results in human readable format) could make Monitorix unable to interpret the results.</dl>
<h3>Network traffic and usage (net.rrd)</h3>
<p><code>list</code></p>
<dl>
<dd>This is a comma-separated list of network interfaces that you may want to monitor. An example would be: </p>
<dl>
<dd>list = eth0, eth1
</dl>
<p> The maximum number of entries allowed is 10.</dl>
<p> <code>desc</code></p>
<dl>
<dd>This is the option where each network interface specified in <code>list</code> is described. Each definition consists of three parameters separated by comma: the description of the interface and the rigid and limit values. </p>
<p> Put one description for each interface listed. An example would be: </p>
<dl>
<dd>&lt;desc&gt;<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>eth0 = FastEthernet LAN, 0, 1000</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>eth1 = ADSL 10Mbs Internet, 0, 1000</p>
<p> &lt;/desc&gt;</dl>
<p> The maximum number of entries allowed is 10.</dl>
<p> <code>gateway</code></p>
<dl>
<dd>This is where the network interface that acts as the gateway for this server is defined. This is mainly used if you plan to monitor network traffic usage of your devices/networks using the <code>traffacct</code> graph below.</dl>
<h3>Netstat statistics (netstat.rrd)</h3>
<p>This graph shows the state of the all IPv4 and IPv6 network connections. </p>
<p> Only the limit and rigid values can be set here.</p>
<h3>Traffic Control statistics (tc.rrd)</h3>
<p>This graph is able to monitor an unlimited number of network interfaces managed by the <i>tc</i> command. </p>
<p> <code>list</code></p>
<dl>
<dd>This is a comma-separated list of network interfaces that you may want to monitor. An example would be: </p>
<dl>
<dd>list = eth0, eth1
</dl>
</dl>
<p> <code>desc</code></p>
<dl>
<dd>This is the option where you define the queue disciplines you want to monitor for each network interface specified in <code>list</code>. </p>
<p> An example would be: </p>
<dl>
<dd>&lt;desc&gt;<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>eth0 = cbq 1, sfq 10, sfq 20, sfq 30, ingress ffff</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>eth1 = htb 1, pfifo 20, pfifo 21, pfifo 22</p>
<p> &lt;/desc&gt;</dl>
<p> The maximum number of qdiscs allowed is 9.</dl>
<p> <code>map</code></p>
<dl>
<dd>This option complements the <code>desc</code> option. It basically allows you to change the name of the qdiscs that will appear in the graphs. If no association is defined, then Monitorix will show the name as specified in the <code>desc</code> option. </p>
<p> Since the qdisc names have the space character in their names, they can&#8217;t be used as the key in the association, instead you must the use their position number (starting by 0) in the <code>desc</code> option. </p>
<p> An example would be: </p>
<dl>
<dd>&lt;map&gt;<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>&lt;eth0&gt;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>0 = Class Based Queueing</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>1 = Stochastic Fairness Queueing 10</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>&lt;/eth0&gt;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>&lt;eth1&gt;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>0 = Hierarchical Token Bucket</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>&lt;/eth1&gt;</p>
<p> &lt;/map&gt;</dl>
</dl>
<h3>Libvirt statistics (libvirt.rrd)</h3>
<p>This graph is able to monitor an unlimited number of virtual machines managed by Libvirt. </p>
<p> <code>cmd</code></p>
<dl>
<dd>This is the command that will be used to gather statistics from each virtual machine listed in <code>list</code>. </p>
<p> Default value: <i>virsh</i> </p>
<p> An example would be: </p>
<dl>
<dd>cmd = virsh -r -c <a href="qemu:///session">qemu:///session</a></dl>
</dl>
<p> <code>list</code></p>
<dl>
<dd>This is a list of groups of virtual machines that you want to monitor. Each group will become a graph and there may be an unlimited number of groups. </p>
<p> WARNING: Every time the number of groups in this option changes, Monitorix will resize the <i>libvirt.rrd</i> file accordingly, removing all historical data. </p>
<p> An example would be: </p>
<dl>
<dd>&lt;list&gt;<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>0 = centos6, winxp</p>
<p> &lt;/list&gt;</dl>
<p> The maximum number of virtual machines allowed per group is 8.</dl>
<p> <code>desc</code></p>
<dl>
<dd>This list complements the <code>list</code> option and is mandatory for every virtual machine listed. You must define the virtual block device and the MAC address of the virtual network device that you want to monitor for every virtual machine. Just like this: </p>
<dl>
<dd>&lt;desc&gt;<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>centos6 = CentOS 6, vda, 52:54:00:45:d0:e7</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>winxp = MS Windows XP, hda, 52:54:00:97:1c:e5</p>
<p> &lt;/desc&gt;</dl>
<p> You might also define this list using sections for each virtual machine, this way you&#8217;ll be able to define multiple disks and multiple network interfaces for each virtual machine. Just like this: </p>
<dl>
<dd>&lt;desc&gt;<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>&lt;centos6&gt;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>desc = &quot;CentOS 6&quot;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>disk = vda, vdb, vdc</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>net = 52:54:00:45:d0:e7, 52:54:00:45:d0:e8</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>&lt;/centos6&gt;</p>
<p> &lt;/desc&gt;</dl>
<p> To obtain all these values you might want to use the following commands: </p>
<p> # virsh domblklist centos6<br />
 Target Source<br />
 &#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;<br />
 vda /home/jordi/kvm/centos6.img<br />
 hdc &#8211; </p>
<p> # virsh domiflist centos6<br />
 Interface Type Source Model MAC<br />
 &#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;-<br />
 vnet3 network default virtio 52:54:00:45:d0:e7 </p>
<p> This option also allows you to change the name that will appear in the graph, hiding the real name of the virtual machine. If no association is defined, then Monitorix will display the name specified in the <code>list</code> option.</dl>
<h3>Process statistics (process.rrd)</h3>
<p>This graph is able to monitor an unlimited number of processes. This graph requires a Linux kernel version 2.6.20 at least to support process I/O accounting. Some systems with older kernels might also have been ported it though. </p>
<p> <code>list</code></p>
<dl>
<dd>This is a list of groups of processes that you want to monitor. Each group will become a graph and there may be an unlimited number of groups. </p>
<p> WARNING: Every time the number of groups in this option changes, Monitorix will resize the <i>process.rrd</i> file accordingly, removing all historical data. </p>
<p> Monitorix uses the following command to find the processes listed in this option: </p>
<dl>
<dd># ps -eo pid,comm,command </p>
</dl>
<p> Therefore names in the process list must *EXACTLY* correspond to those in the <i>comm</i> (or <i>command</i>) field of the above command (no substring, no wildcard). </p>
<p> An example of this option would be: </p>
<dl>
<dd>&lt;list&gt;<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>0 = httpd, sshd, ntpd, mysqld, proftpd, clamd, imap, sendmail, named, bash</p>
<p> &lt;/list&gt;</dl>
<p> The maximum number of processes allowed per group is 10.</dl>
<p> <code>desc</code></p>
<dl>
<dd>This list complements the <code>list</code> option. It basically allows you to change the name that will appear in the graph, hiding the real name of the process. If no association is defined, then Monitorix will display the name specified in the <code>list</code> option. </p>
<dl>
<dd>&lt;desc&gt;<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>httpd = Apache</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>imap = Dovecot</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>named = Bind</p>
<p> &lt;/desc&gt;</dl>
<p> You can define as much entries as you want.</dl>
<h3>System services demand (serv.rrd)</h3>
<p>This graph requires either <i>MailScanner</i> or <i>amavisd-new</i> mail scanners in order to account spam and virus emails. </p>
<p> <code>mode</code></p>
<dl>
<dd>This option toggles the way the System Services Demand data is represented in the graph. There are two possible values: </p>
<dl>
<dd><i>i</i> for incremental style.<br />
 <i>l</i> for load (peaks) style.</dl>
<p> Default value: <i>i</i></dl>
<h3>Mail statistics (mail.rrd)</h3>
<p>This graph requires either <i>MailScanner</i> or <i>amavisd-new</i> mail scanners in order to account spam and virus emails. Spamassassin and Clamav antivirus are also used for spam and virus email accounting. </p>
<p> <code>mta</code></p>
<dl>
<dd>This option specifies the MTA that Monitorix will use to collect mail statistics. The currently supported MTAs are:</p>
<dl>
<dd><i>Sendmail</i><br />
 <i>Postfix</i></dl>
<p> NOTE: the <i>pflogsumm</i> utility is required when using the <code>Postfix</code> MTA. </p>
<p> Default value: <i>sendmail</i></dl>
<p> <code>greylist</code></p>
<dl>
<dd>This option specifies the Greylisting implementation that Monitorix will use to collect statistical information. In the future more Greylisting software will be supported. </p>
<p> The currently supported Greylist software is:</p>
<dl>
<dd><i>milter-greylist</i></dl>
<p> Default value: <i>milter-greylist</i></dl>
<p> <code>delvd_enabled</code></p>
<dl>
<dd>This section enables or disables one of the alert capabilities for this graph; the alert for the number of delivered messages. It works as follows: </p>
<p> If the number of delivered messages reaches the <code>delvd_threshold</code> value for the interval of time defined in <code>delvd_timeintvl</code>, Monitorix will execute the external alert script defined in <code>delvd_script</code>. </p>
<p> The default Monitorix installation includes an example of a shell-script alert called <code>monitorix-alert.sh</code> which you can use as a base for your own script. </p>
<p> Default value: <i>n</i></dl>
<p> <code>delvd_timeintvl</code></p>
<dl>
<dd>This is the period of time (in seconds) that the threshold needs to be exceeded before the external alert script is executed. </p>
<p> Default value: <i>60</i></dl>
<p> <code>delvd_threshold</code></p>
<dl>
<dd>This is the value that needs to be reached or exceeded within the specified time period in <code>delvd_timeintvl</code> to trigger the mechanism for a particular action, which in this case is the execution of an external alert script. </p>
<p> The value of this option is compared against the number of delivered messages since the last <code>delvd_timeintvl</code> seconds. </p>
<p> Default value: <i>100</i></dl>
<p> <code>delvd_script</code></p>
<dl>
<dd>This is the full path name of the script that will be executed by this alert. </p>
<p> It will receive the following three parameters: </p>
<p> 1st &#8211; the value currently defined in <code>delvd_timeintvl</code>.<br />
 2nd &#8211; the value currently defined in <code>delvd_threshold</code>.<br />
 3rd &#8211; the number of delivered messages. </p>
<p> Default value: <i>/path/to/script.sh</i></dl>
<p> <code>mqueued_enabled</code></p>
<dl>
<dd>This section enables or disables one of the alert capabilities for this graph; the alert for the number of queued messages. It works as follows: </p>
<p> If the number of queued messages reaches the <code>mqueued_threshold</code> value for the interval of time defined in <code>mqueued_timeintvl</code>, Monitorix will execute the external alert script defined in <code>mqueued_script</code>. </p>
<p> The default Monitorix installation includes an example of a shell-script alert called <code>monitorix-alert.sh</code> which you can use as a base for your own script. </p>
<p> Default value: <i>n</i></dl>
<p> <code>mqueued_timeintvl</code></p>
<dl>
<dd>This is the period of time (in seconds) that the threshold needs to be exceeded before the external alert script is executed. </p>
<p> Default value: <i>3600</i></dl>
<p> <code>mqueued_threshold</code></p>
<dl>
<dd>This is the value that needs to be reached or exceeded within the specified time period in <code>mqueued_timeintvl</code> to trigger the mechanism for a particular action, which in this case is the execution of an external alert script. </p>
<p> The value of this option is compared with the number of messages in the mail queue. </p>
<p> Default value: <i>100</i></dl>
<p> <code>mqueued_script</code></p>
<dl>
<dd>This is the full path name of the script that will be executed by this alert. </p>
<p> It will receive the following three parameters: </p>
<p> 1st &#8211; the value currently defined in <code>mqueued_timeintvl</code>.<br />
 2nd &#8211; the value currently defined in <code>mqueued_threshold</code>.<br />
 3rd &#8211; the number of messages in the mail queue. </p>
<p> Default value: <i>/path/to/script.sh</i></dl>
<h3>Network port traffic (port.rrd)</h3>
<p>This graph requires the <i><a href="/docs/linux/man/8-iptables/">iptables</a></i>(8) command and optionally the <i><a href="/docs/linux/man/8-ip6tables/">ip6tables</a></i>(8) command on Linux systems and the <i>ipfw</i> command on *BSD systems. </p>
<p> <code>max</code></p>
<dl>
<dd>This is the number of network ports that you want to monitor. There is no limit to the number of ports monitored, but keep in mind that every time this number changes, Monitorix will resize the <i>port.rrd</i> file accordingly, removing all historical data. </p>
<p> Default value: <i>9</i></dl>
<p> <code>rule</code></p>
<dl>
<dd>This is the rule number that Monitorix will use when using the <i>ipfw</i> command to manage network port activity on *BSD systems. Change it if you think it might conflict with any other rule number. </p>
<p> Default value: <i>24000</i></dl>
<p> <code>list</code></p>
<dl>
<dd>You may define here up to <code>max</code> network port numbers. If you need to monitor the same network port with TCP and UDP protocols, you can add your own suffix to the port number (e.g: 443t and 443u) in order to distinguish it from the double definition in the &lt;desc&gt; block. </p>
<p> If you see a red color in the background of a network port graph, it means that there is not a daemon listening on that port. This can be useful to know if some service gone down unexpectedly.</dl>
<p> <code>desc</code></p>
<dl>
<dd>This is the option where each network port specified in <code>list</code> is described. Each port definition consists of five parameters separated by comma: the port description, the network protocol (<i>tcp</i> or <i>udp</i>), the connection type (<i>in</i>, <i>out</i> or <i>in/out</i>) and the rigid and limit values. </p>
<p> There is also support (Linux only) for IPv6 network ports activity by using protocol names as <i>tcp6</i> or <i>udp6</i>. </p>
<p> An example would be:</p>
<dl>
<dd>list = 25, 25ip6, 80, 53<br />
 &lt;desc&gt;<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>25 = SMTP, tcp, in/out, 0, 1000</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>25ip6 = SMTP, tcp6, in/out, 0, 1000</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>80 = HTTP, tcp, in, 0, 1000</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>53 = DNS, udp, in, 0, 1000</p>
<p> &lt;/desc&gt;</dl>
<p> As you can see, you cannot use the same port number twice. Instead, you must distinguish it with some suffix.</dl>
<p> <code>graphs_per_row</code></p>
<dl>
<dd>This is the number of graphs that will be put in a row. Consider the interaction of this parameter with the <code>max</code> option in order to adjust the size and number of graphs in relation to your horizontal screen size. </p>
<p> Default value: <i>3</i></dl>
<h3>Users using the system (user.rrd)</h3>
<p>Only the limit and rigid values can be set here.</p>
<h3>FTP statistics (<a href="ftp://ftp.rrd">ftp.rrd</a>)</h3>
<p>This graph supports currently ProFTPD, vsftpd and Pure-FTPd log file formats. </p>
<p> For best results with the ProFTPD server I recommend to add the following line in its configuration file: </p>
<p> ExtendedLog /var/log/proftpd/access.log AUTH,DIRS,READ,WRITE </p>
<p> For best results with the vsftpd server I recommend to setup the option <i>xferlog_std_format</i> to <i>NO</i>, and the option <code>ftp_log</code> to <i>/var/log/vsftpd.log</i>. </p>
<p> Pure-FTPd users might want to consider using the system <code>syslog</code> logfile. </p>
<p> <code>server</code></p>
<dl>
<dd>This option specifies the FTP server. The currently supported FTP servers are:</p>
<dl>
<dd><i>ProFTPD</i><br />
 <i>vsftpd</i><br />
 <i>Pure-FTPd</i></dl>
<p> Default value: <i>proftpd</i></dl>
<p> <code>anon_user</code></p>
<dl>
<dd>This option lists the different names (separated by comma) that can adopt the Anonymous user in the FTP server defined in <code>server</code>. </p>
<p> Default value: <i>anonymous, ftp</i></dl>
<h3>Apache statistics (apache.rrd)</h3>
<p>This graph requires that <i>mod_status</i> be loaded and <i>ExtendedStatus</i> option set to <i>On</i> in order to collect full status information of the Apache web server. </p>
<p> This graph is able to monitor an unlimited number of local and remote Apache web servers. </p>
<p> <code>list</code></p>
<dl>
<dd>This is a comma-separated list of URLs of the monitored Apache web servers. </p>
<p> WARNING: Every time the number of entries in this option changes, Monitorix will resize the <i>apache.rrd</i> file accordingly, removing all historical data. </p>
<p> Default value: <i><a rel="nofollow" href="http://localhost/server-status?auto">http://localhost/server-status?auto</a></i></dl>
<p> <code>alerts</code></p>
<dl>
<dd>This optional list enables the alert capabilities for this graph and complements with the <code>list</code> option. Each alert has three fields separated by comma: the <i>time interval</i>, the <i>threshold</i> and the path to the <i>script</i> to be executed. </p>
<p> The <i>time interval</i> is the period of time (in seconds) that the <i>threshold</i> needs to be exceeded before the external script is executed. </p>
<p> The <i>threshold</i> is the number of remaining free slots that needs to be reached or exceeded within the specified time in <i>time interval</i> to execute the external script. </p>
<p> The <i>script</i> is the full path name of the script that will be executed by this alert. </p>
<p> Each defined Apache has its own alert. </p>
<p> The default Monitorix installation includes an example of a shell-script alert called <i>monitorix-alert.sh</i> which you can use as a base for your own script. </p>
<p> The following is an example of an alert defined for the local Apache: </p>
<dl>
<dd>&lt;alerts&gt;<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><a rel="nofollow" href="http://localhost/server-status?auto">http://localhost/server-status?auto</a> = 3600, 5, /path/to/script</p>
<p> &lt;/alerts&gt; </p>
</dl>
<p> Such alert means that if the remaining free slots reaches or exceeds 5 (less than 5) during at least one hour (3600 seconds) the script in <i>/path/to/script</i> will be executed. </p>
<p> The external script will receive the following arguments: </p>
<dl>
<dd>1st &#8211; the value defined as <i>time interval</i>.<br />
 2nd &#8211; the value defined as <i>threshold</i>.<br />
 3rd &#8211; the remaining free slots. </p>
</dl>
</dl>
<h3>Nginx statistics (nginx.rrd)</h3>
<p>This graph may require adding some lines in the configuration file <i>nginx.conf</i>. Please see the <i>README.nginx</i> file to determine the exact steps needed to configure Nginx to get status information. </p>
<p> This graph requires the <i><a href="/docs/linux/man/8-iptables/">iptables</a></i>(8) command on Linux systems, and the <i>ipfw</i> command on *BSD systems. </p>
<p> <code>url</code></p>
<dl>
<dd>This is the URL to be used to collect Nginx stats. </p>
<p> Default value: <i><a rel="nofollow" href="http://localhost/nginx_status">http://localhost/nginx_status</a></i></dl>
<p> <code>port</code></p>
<dl>
<dd>This is the network port the Nginx web server is listening on. It will be used for traffic (with <i>iptables</i>), and for nginx_status if <code>url</code> is not specified. If port of nginx_status is different from <code>port</code> then specify it in the <code>url</code> (<a rel="nofollow" href="http://host:port/nginx_status)">http://host:port/nginx_status)</a> </p>
<p> Default value: <i>80</i></dl>
<p> <code>rule</code></p>
<dl>
<dd>This is the rule number that Monitorix will use when using the <i>ipfw</i> command to manage Nginx network activity on *BSD systems. Change it if you think it might conflict with any other rule number. </p>
<p> Default value: <i>24100</i></dl>
<h3>Lighttpd statistics (lighttpd.rrd)</h3>
<p>This graph requires that <i>mod_status</i> is loaded in order to collect status information from the Lighttpd web server. </p>
<p> This graph is able to monitor an unlimited number of local and remote Lighttpd web servers. </p>
<p> <code>list</code></p>
<dl>
<dd>This is a comma-separated list of URLs of the monitored Lighttpd web servers. </p>
<p> WARNING: Every time the number of entries of this option changes, Monitorix will resize the <i>lighttpd.rrd</i> file accordingly, removing all historical data. </p>
<p> Default value: <i><a rel="nofollow" href="http://localhost/server-status?auto">http://localhost/server-status?auto</a></i></dl>
<h3>MySQL statistics (mysql.rrd)</h3>
<p>This graph requires that you create a password protected MySQL user that is NOT granted privileges on any DB. </p>
<p> Example: </p>
<p> mysql&gt; CREATE USER &#8216;user&#8217;@&#8217;localhost&#8217; IDENTIFIED BY &#8216;password&#8217;;<br />
 mysql&gt; FLUSH PRIVILEGES; </p>
<p> where <i>user</i> is the new user name and <i>password</i> is the password that will be used for that user. </p>
<p> This graph is able to monitor an unlimited number of local and remote MySQL web servers. </p>
<p> NOTE: It is strongly recommended that you restart the MySQL service in order to avoid high peaks that could prevent correct display of the first plotted data. </p>
<p> <code>conn_type</code></p>
<dl>
<dd>This option toggles the way how Monitorix establishes the connection with the MySQL server. There are two possible values: </p>
<dl>
<dd><i>host</i> using the network (hostname and IP address).<br />
 <i>socket</i> using a socket file.</dl>
<p> Default value: <i>host</i></dl>
<p> <code>list</code></p>
<dl>
<dd>This is a comma-separated list of hostnames or path to sockets of MySQL servers. </p>
<p> WARNING: Every time the number of entries of this option change Monitorix will resize the <i>mysql.rrd</i> file accordingly, removing all historical data. </p>
<p> Default value: <i>localhost</i></dl>
<p> <code>desc</code></p>
<dl>
<dd>This is the option where each entry specified in the list is described. Each definition consists of three parameters separated by comma: the port, the username and the password. </p>
<p> An example using the <i>host</i> type would be:</p>
<dl>
<dd>&lt;desc&gt;<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>localhost = 3306, user, secret</p>
<p> &lt;/desc&gt;</dl>
<p> When using the <i>socket</i> type the network port is, of course, irrelevant but its field is still mandatory. This means that you must respect the three comma-separated values. </p>
<p> Some of the values shown in the graphs are the result of a calculation of two values from either <i>SHOW [GLOBAL] STATUS</i> or <i>SHOW VARIABLES</i>. The following is an explanation of them: </p>
<p> <code>Thread Cache Hit Rate</code><br />
 <code>(1 &#8211; (Threads_created / Connections)) * 100</code><br />
 When an application connects to a MySQL database, the database has to create a thread to manage the connection and the queries that will be sent in that connection. The database instructs the kernel to create a new thread, and the kernel allocates resources and creates the thread, then returns it to the MySQL service. When the connection is terminated by the application, MySQL tells the kernel to destroy the thread and free the resources. This create/destroy mechanism causes considerable overhead if the MySQL server has many new connections per second.<br />
 If MySQL doesn&#8217;t destroy the thread when the connection is terminated, but reuses it and assigns it to the next connection then this will decrease the kernel overhead. This is why a high <code>Thread Cache Hit Rate</code> improves MySQL performance and decreases the system&#8217;s CPU usage.<br />
 Setting the parameter <i>thread_cache_size</i> in the <i>my.cnf</i> file accordingly will help to correctly balance between having a great thread cache and keeping MySQL memory consumption reasonable.<br />
 Higher is better. </p>
<p> <code>Query Cache Hit Rate</code><br />
 <code>Qcache_hits / (Qcache_hits + Com_select) * 100</code><br />
 Higher should be considered better.<br />
 A query cache size increase is recommended if the query cache usage is very close to 100% and the query cache hit rate is far from 100%. But sometimes a size increase will not lead to a better hit rate: this means that the increase was not needed and that the application do not run enough cacheable SELECT queries.<br />
 This value should grow proportionally with the number of executed queries as long as the query cache is performing well. Please also have a look at the <code>Query cache usage</code> percentage to know if your query_cache configuration is appropriate. </p>
<p> For more information please refer to <a rel="nofollow" href="http://www.databasejournal.com/features/mysql/article.php/3808841/Optimizing-the-MySQL-Query-Cache.htm">http://www.databasejournal.com/features/mysql/article.php/3808841/Optimizing-the-MySQL-Query-Cache.htm</a> </p>
<p> <code>Query Cache Usage</code><br />
 <code>(1 &#8211; (Qcache_free_memory / query_cache_size)) * 100</code><br />
 This value should be reasonably far from 100%, otherwise consider incrementing the <i>query_cache_size</i> parameter in <i>my.cnf</i>. </p>
<p> <code>Connections Usage</code><br />
 <code>(Max_used_connections / max_connections) * 100</code><br />
 This value should be reasonably far from 100%, otherwise consider incrementing the <i>max_connections</i> parameter in <i>my.cnf</i>. </p>
<p> <code>Key Buffer Usage</code><br />
 <code>(Key_blocks_used / (Key_blocks_used + Key_blocks_unused)) * 100</code><br />
 This value should be reasonably far from 100%, otherwise consider incrementing the <i>key_buffer_size</i> parameter in <i>my.cnf</i>. </p>
<p> <code>InnoDB Buffer Pool Usage</code><br />
 <code>(1 &#8211; (Innodb_buffer_pool_pages_free / Innodb_buffer_pool_pages_total)) * 100</code><br />
 This value should be reasonably far from 100%, otherwise consider incrementing the <i>innodb_buffer_pool_size</i> parameter in <i>my.cnf</i>. </p>
<p> <code>Temp. Tables To Disk</code><br />
 <code>(Created_temp_disk_tables / Created_temp_disk_tables + Created_temp_tables)) * 100</code><br />
 During operation, MySQL has to create some temporary tables (that can be explicit, so created by the web application, or implicit, so for example MySQL has to create one when he runs some &quot;SELECT DISTINCT&quot;, &quot;UNION&quot; or &quot;VIEW&quot; queries). MySQL will prefer to save this tmp tables to memory, for a fast access. But if <i>tmp_table_size</i> gets saturated, he has to write them on the disk instead, making the access slower.<br />
 Note that if you modify the value of <i>tmp_table_size</i> in the MySQL configuration file, you should also modify the value of <i>max_heap_table_size</i> as well, since both values should have the same value because MySQL uses the minimum of both, so raising one of them is useless.<br />
 Therefore this value helps to know how many tmp tables go to the disk instead than to the memory. Keep in mind that some large queries, involving TEXT and BLOB columns, are directly written to the disk instead than to the memory, because they would be too big. So you probably will want to avoid having a high % of tmp tables written to the disk, but you will never reach 0% on a big site, and this is fine.<br />
 Lower is better &#8230; but 0% is not reachable and you should not try to reach it, usually.</dl>
<h3>Varnish cache statistics (varnish.rrd)</h3>
<p>This graph monitors a local installation of the Varnish HTTP accelerator. </p>
<p> Only the limit and rigid values can be set here.</p>
<h3>PageSpeed Module statistics (pagespeed.rrd)</h3>
<p>This graph is able to monitor an unlimited number of PageSpeed installations. </p>
<p> <code>list</code></p>
<dl>
<dd>This is a comma-separated list of URLs of PageSpeed status pages. </p>
<p> WARNING: Every time the number of entries in this option changes, Monitorix will resize the <i>pagespeed.rrd</i> file accordingly, removing all historical data. </p>
<p> Default value: <i><a rel="nofollow" href="http://modpagespeed.com/mod_pagespeed_statistics">http://modpagespeed.com/mod_pagespeed_statistics</a></i></dl>
<p> For more information please refer to <a rel="nofollow" href="https://developers.google.com/speed/pagespeed/module">https://developers.google.com/speed/pagespeed/module</a> and <a href="http://stackoverflow.com/questions/9115595/what-do-the-mod-pagespeed-statistics-mean">http://stackoverflow.com/questions/9115595/what-do-the-mod-pagespeed-statistics-mean</a></p>
<h3>Squid Proxy Web Cache (squid.rrd)</h3>
<p><code>cmd</code></p>
<dl>
<dd>This command displays statistics about the Squid HTTP proxy process and is the main command used to collect all data. </p>
<p> Default value: <i>squidclient -h 127.0.0.1</i> </p>
</dl>
<p> <code>graph_0</code><br />
 <code>graph_1</code></p>
<dl>
<dd>These two lists hold the selected Squid result or status codes to be shown in each graph. Feel free to mix result status and code status in any of the two options. </p>
<p> For more information about the list of all the result and status codes, please refer to <a rel="nofollow" href="http://wiki.squid-cache.org/SquidFaq/SquidLogs.">http://wiki.squid-cache.org/SquidFaq/SquidLogs.</a> </p>
<p> Each graph has a limit number of 9 entries.</dl>
<h3>NFS server statistics (nfss.rrd)</h3>
<p><code>version</code></p>
<dl>
<dd>This option specifies which NFS server version is running in the system in order to correctly gather the correct values. </p>
<p> The possible values are:</p>
<dl>
<dd><i>2</i> for NFS v2.<br />
 <i>3</i> for NFS v3.<br />
 <i>4</i> for NFS v4.</dl>
<p> Default value: <i>3</i> </p>
</dl>
<p> <code>graph_0</code><br />
 <code>graph_1</code><br />
 <code>graph_2</code></p>
<dl>
<dd>These three lists hold the defined NFS server activity statistics to be shown in each graph. Put every statistic name exactly as they appear in the output of the <i><a href="/docs/linux/man/8-nfsstat/">nfsstat</a></i>(8) command. </p>
<p> Each graph has a limit number of 10 entries.</dl>
<h3>NFS client statistics (nfsc.rrd)</h3>
<p><code>version</code></p>
<dl>
<dd>This option specifies which NFS server version is running in the system in order to correctly gather the correct values. </p>
<p> The possible values are:</p>
<dl>
<dd><i>2</i> for NFS v2.<br />
 <i>3</i> for NFS v3.<br />
 <i>4</i> for NFS v4.</dl>
<p> Default value: <i>3</i> </p>
</dl>
<p> <code>graph_1</code><br />
 <code>graph_2</code><br />
 <code>graph_3</code><br />
 <code>graph_4</code><br />
 <code>graph_5</code></p>
<dl>
<dd>These five lists hold the defined NFS client activity statistics to be shown in each graph. Put every statistic name exactly as they appear in the output of the <i><a href="/docs/linux/man/8-nfsstat/">nfsstat</a></i>(8) command. </p>
<p> Each graph has the following limit number of entries: </p>
<p> <code>graph_1</code> up to 10 entries.<br />
 <code>graph_2</code> up to 10 entries.<br />
 <code>graph_3</code> up to 4 entries.<br />
 <code>graph_4</code> up to 4 entries.<br />
 <code>graph_5</code> up to 4 entries.</dl>
<h3>BIND statistics (bind.rrd)</h3>
<p>This graph requires a BIND server with version 9.5 or higher, and in order to see all statistics provided by BIND you must configure the <i>statistics-channels</i> option like this: </p>
<p> statistics-channels { </p>
<p>&nbsp;<wbr>&nbsp;<wbr>inet 127.0.0.1 port 8053;<br />
 }; </p>
<p> This graph is able to monitor an unlimited number of BIND servers. </p>
<p> <code>list</code></p>
<dl>
<dd>This is a comma-separated list of URLs of BIND servers status pages. </p>
<p> WARNING: Every time the number of entries in this option changes, Monitorix will resize the <i>bind.rrd</i> file accordingly, removing all historical data. </p>
<p> Default value: <i><a rel="nofollow" href="http://localhost:8053/">http://localhost:8053/</a></i></dl>
<p> <code>in_queries_list</code></p>
<dl>
<dd>This is a comma-separated list of RR (Resource Records) types for each BIND server specified in <code>list</code> option. The RR types defined here will appear in the Incoming Queries graph which shows the number of incoming queries for each RR type. </p>
<p> For a complete list of RR types check the BIND 9 Administrator Reference Manual at &lt;<a rel="nofollow" href="http://ftp.isc.org/www/bind/arm95/Bv9ARM.html">http://ftp.isc.org/www/bind/arm95/Bv9ARM.html</a>&gt;. </p>
<p> &lt;in_queries_list&gt;<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><a rel="nofollow" href="http://localhost:8053/">http://localhost:8053/</a> = A, AAAA, ANY, DS, MX, NS, PTR, SOA, SRV, TXT, NAPTR, A6, CNAME, SPF, KEY, DNSKEY, HINFO, WKS, PX, NSAP</p>
<p> &lt;/in_queries_list&gt; </p>
<p> The maximum number of RR types allowed for this graph is 20.</dl>
<p> <code>out_queries_list</code></p>
<dl>
<dd>This is a comma-separated list of RR (Resource Records) types for each BIND server. The RR types defined here will appear in the Outgoing Queries graph (_default view) which shows the number of outgoing queries sent by the DNS server resolver for each RR type. </p>
<p> &lt;out_queries_list&gt;<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><a rel="nofollow" href="http://localhost:8053/">http://localhost:8053/</a> = A, AAAA, ANY, DS, MX, NS, PTR, SOA, SRV, TXT, NAPTR, A6, CNAME, SPF, KEY, DNSKEY, HINFO, WKS, PX, NSAP</p>
<p> &lt;/out_queries_list&gt; </p>
<p> The maximum number of RR types allowed for this graph is 20.</dl>
<p> <code>server_stats_list</code></p>
<dl>
<dd>This is a comma-separated list of counters about incoming request processing. The counters defined here will appear in the Server Statistics graph. </p>
<p> &lt;server_stats_list&gt;<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><a rel="nofollow" href="http://localhost:8053/">http://localhost:8053/</a> = Requestv4, Requestv6, ReqEdns0, ReqBadEDNSVer, ReqTSIG, ReqSIG0, ReqBadSIG, ReqTCP, Response, QrySuccess, QryAuthAns, QryNoauthAns, QryReferral, QryNxrrset, QrySERVFAIL, QryNXDOMAIN, QryRecursion, QryDuplicate, QryDropped, QryFailure</p>
<p> &lt;/server_stats_list&gt; </p>
<p> The maximum number of counters allowed for this graph is 20.</dl>
<p> <code>resolver_stats_list</code></p>
<dl>
<dd>This is a comma-separated list of counters about name resolution performed in the internal resolver. The counters defined here will appear in the Resolver Statistics graph (_default view). </p>
<p> &lt;resolver_stats_list&gt;<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><a rel="nofollow" href="http://localhost:8053/">http://localhost:8053/</a> = Queryv4, Queryv6, Responsev4, Responsev6, NXDOMAIN, SERVFAIL, FORMERR, OtherError, EDNS0Fail, Truncated, Lame, Retry, QueryTimeout, GlueFetchv4, GlueFetchv6, GlueFetchv4Fail, GlueFetchv6Fail, ValAttempt, ValOk, ValNegOk</p>
<p> &lt;/resolver_stats_list&gt; </p>
<p> The maximum number of counters allowed for this graph is 20.</dl>
<p> <code>cache_rrsets_list</code></p>
<dl>
<dd>This is a comma-separated list of RR (Resource Records) types for each BIND server. The RR types defined here will appear in the Cache DB RRsets graph (_default view) which shows the number of RRsets per RR type (positive or negative) and nonexistent names stored in the cache database. </p>
<p> &lt;cache_rrsets_list&gt;<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><a rel="nofollow" href="http://localhost:8053/">http://localhost:8053/</a> = A, !A, AAAA, !AAAA, DLV, !DLV, DS, !DS, MX, NS, CNAME, !CNAME, SOA, !SOA, !ANY, PTR, RRSIG, NSEC, DNSKEY, NXDOMAIN</p>
<p> &lt;/cache_rrsets_list&gt; </p>
<p> The maximum number of RR types allowed for this graph is 20.</dl>
<h3>NTP statistics (ntp.rrd)</h3>
<p>This graph is able to monitor an unlimited number of NTP servers. </p>
<p> <code>list</code></p>
<dl>
<dd>This is a comma-separated list of NTP servers. </p>
<p> WARNING: Every time the number of entries in this option changes, Monitorix will resize the <i>ntp.rrd</i> file accordingly, removing all historical data. </p>
<p> Default value: <i>localhost</i></dl>
<p> <code>desc</code></p>
<dl>
<dd>This is a list of groups of Reference Identifier and Kiss-o&#8217;-Death Codes for every hostname specified in the <code>list</code> option. </p>
<p> For more information on these NTP codes:<br />
 &lt;<a rel="nofollow" href="http://www.iana.org/assignments/ntp-parameters/ntp-parameters.xml">http://www.iana.org/assignments/ntp-parameters/ntp-parameters.xml</a>&gt;<br />
 &lt;<a rel="nofollow" href="http://www.iana.org/go/rfc5905">http://www.iana.org/go/rfc5905</a>&gt; </p>
<p> &lt;desc&gt;<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>localhost = AUTH, AUTO, CRYP, DENY, GPS, INIT, NKEY, RATE, RMOT, RSTR</p>
<p> &lt;/desc&gt; </p>
<p> The maximum number of codes allowed for each hostname is 10.</dl>
<p> <code>extra_args</code></p>
<dl>
<dd>This option includes any extra argument to the NTP command executed by Monitorix, which is &quot;ntpq -pn&quot;. This is specially useful if you want to force using IPv4, in this case just define this option like this: </p>
<dl>
<dd>extra_args = &quot;-4&quot;</dl>
<p> Monitorix will add this extra argument to the NTP command which will become as &quot;ntpq -pn -4&quot;.</dl>
<h3>Chrony statistics (chrony.rrd)</h3>
<p>This graph is able to monitor an unlimited number of Chrony daemons. </p>
<p> <code>list</code></p>
<dl>
<dd>This is a comma-separated list of hostnames with the network port running <i>chronyd</i>. The format is &lt;hostname&gt;:&lt;port&gt; being the port number optional. </p>
<p> WARNING: Every time the number of entries in this option changes, Monitorix will resize the <i>chrony.rrd</i> file accordingly, removing all historical data. </p>
<p> Default value: <i>localhost</i></dl>
<h3>Fail2ban statistics (fail2ban.rrd)</h3>
<p>This graph is able to monitor an unlimited number of Fail2ban jails. </p>
<p> <code>list</code></p>
<dl>
<dd>This is a comma-separated list that describes the groups of jails in <code>desc</code>. Put one description for each group. For every group specified you need to specify its description in the <code>desc</code> option. </p>
<p> WARNING: Every time the number of entries in this option changes, Monitorix will resize the <i>fail2ban.rrd</i> file accordingly, removing all historical data. </p>
<p> An example would be: </p>
<p> list = Security, Overload / Abuse</dl>
<p> <code>desc</code></p>
<dl>
<dd>This is a list of jails per group defined in your Fail2ban configuration. </p>
<p> &lt;desc&gt;<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>0 = [apache], [apache-mod-security], [apache-overflows], [courierauth], [ssh], [pam-generic], [php-url-fopen], [vsftpd]</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>1 = [apache-imdbphp], [apache-evasive], [apache-badbots], [apache-robots-txt], [communigate], [named-refused-udp], [named-refused-tcp], [trac-ticketspam]</p>
<p> &lt;/desc&gt; </p>
<p> The maximum number of jails allowed for each group is 9.</dl>
<p> <code>graphs_per_row</code></p>
<dl>
<dd>This is the number of fail2ban graphs that will be put in a row. </p>
<p> Default value: <i>2</i></dl>
<h3>Icecast Streaming Media Server (icecast.rrd)</h3>
<p>This graph is able to monitor an unlimited number of Icecast servers. </p>
<p> <code>list</code></p>
<dl>
<dd>This is a list of URLs of Icecast server status pages. </p>
<p> WARNING: Every time the number of entries in this option changes, Monitorix will resize the <i>icecast.rrd</i> file accordingly, removing all historical data. </p>
<p> Default value: <i><a rel="nofollow" href="http://localhost:8000/status.xsl">http://localhost:8000/status.xsl</a></i></dl>
<p> <code>desc</code></p>
<dl>
<dd>This is a comma-separated list of Mount Points configured for every URL specified in the <code>list</code> option. IMPORTANT: the Mount Points must be specified in the same order that appears in the Icecast Server Status page. </p>
<p> &lt;desc&gt;<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><a rel="nofollow" href="http://localhost:8000/status.xsl">http://localhost:8000/status.xsl</a> = stream1, stream2, stream3</p>
<p> &lt;/desc&gt; </p>
<p> The maximum number of mountpoints allowed for each URL is 9.</dl>
<p> <code>graph_mode</code></p>
<dl>
<dd>This changes the layout of the listeners graph, the possible values are <i>r</i> for a real graph, or <i>s</i> for a stacked graph (every line or area is stacked on top of the previous element). </p>
<p> Default value: <i>r</i></dl>
<h3>Raspberry Pi sensor statistics (raspberrypi.rrd)</h3>
<p>For more information please refer to <a rel="nofollow" href="http://elinux.org/RPI_vcgencmd_usage.">http://elinux.org/RPI_vcgencmd_usage.</a> </p>
<p> <code>cmd</code></p>
<dl>
<dd>This is where the <i>vcgencmd</i> command is installed. </p>
<p> Default value: <i>/opt/vc/bin/vcgencmd</i></dl>
<p> <code>clocks</code></p>
<dl>
<dd>This is a comma-separated list of clock types that will be represented in the first graph. </p>
<p> An example would be: </p>
<p> clocks = arm, core, h264, isp, v3d, uart, emmc, pixel, hdmi </p>
<p> The maximum number of clocks allowed is 9.</dl>
<p> <code>volts</code></p>
<dl>
<dd>This is a comma-separated list of voltage types that will be represented in the third graph. </p>
<p> An example would be: </p>
<p> volts = core, sdram_c, sdram_i, sdram_p </p>
<p> The maximum number of clocks allowed is 6.</dl>
<h3>Alternative PHP Cache statistics (phpapc.rrd)</h3>
<p>This graph is able to monitor an unlimited number of PHP-APC installations. </p>
<p> <code>list</code></p>
<dl>
<dd>This is a comma-separated list of URLs of PHP-APC status pages. </p>
<p> WARNING: Every time the number of entries in this option changes, Monitorix will resize the <i>phpapc.rrd</i> file accordingly, removing all historical data. </p>
<p> Default value: <i><a rel="nofollow" href="http://localhost/apc.php?auto">http://localhost/apc.php?auto</a></i></dl>
<h3>Memcached statistics (memcached.rrd)</h3>
<p>This graph is able to monitor an unlimited number of Memcached installations. </p>
<p> <code>list</code></p>
<dl>
<dd>This is a comma-separated list of hostnames with network port running Memcached. </p>
<p> WARNING: Every time the number of entries in this option changes, Monitorix will resize the <i>memcached.rrd</i> file accordingly, removing all historical data. </p>
<p> Default value: <i>localhost:11211</i></dl>
<h3>APC UPS statistics (apcupsd.rrd)</h3>
<p>This graph is able to monitor an unlimited number of APC UPS (apcupsd) installations. </p>
<p> <code>cmd</code></p>
<dl>
<dd>This is the command that will be used (with the values in <i>list</i>) to get the statistics. </p>
<p> Default value: <i>apcaccess</i></dl>
<p> <code>list</code></p>
<dl>
<dd>This is a comma-separated list of hostnames with the network port running <i>apcupsd</i>. </p>
<p> WARNING: Every time the number of entries in this option changes, Monitorix will resize the <i>apcupsd.rrd</i> file accordingly, removing all historical data. </p>
<p> Default value: <i>localhost:3551</i></dl>
<h3>Network UPS Tools statistics (nut.rrd)</h3>
<p>This graph is able to monitor an unlimited number of Network UPS Tools (upsc) installations. </p>
<p> <code>list</code></p>
<dl>
<dd>This is a comma-separated list of UPS names with optionally the hostname and the network port where it&#8217;s running <i>upsd</i>. The format of each entry must be: </p>
<p> upsname[@hostname[:port]] </p>
<p> WARNING: Every time the number of entries in this option changes, Monitorix will resize the <i>nut.rrd</i> file accordingly, removing all historical data. </p>
<p> Default value: <i>ups [at] localhost</i></dl>
<h3>Wowza Media Server (wowza.rrd)</h3>
<p>This graph is able to monitor an unlimited number of Wowza servers. </p>
<p> <code>list</code></p>
<dl>
<dd>This is a comma-separated list of URLs of Wowza server status pages. Each URL can include the Basic Authentication in the form of <i><a rel="nofollow" href="http://username:password@localhost:8086/connectioncounts">http://username:password@localhost:8086/connectioncounts</a></i>. </p>
<p> WARNING: Every time the number of entries in this option changes, Monitorix will resize the <i>wowza.rrd</i> file accordingly, removing all historical data. </p>
<p> Default value: <i><a rel="nofollow" href="http://localhost:8086/connectioncounts">http://localhost:8086/connectioncounts</a></i></dl>
<p> <code>desc</code></p>
<dl>
<dd>This is a comma-separated list of applications configured for every URL specified in the <code>list</code> option. </p>
<p> &lt;desc&gt;<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><a rel="nofollow" href="http://localhost:8086/connectioncounts">http://localhost:8086/connectioncounts</a> = channel1, channel2, channel3</p>
<p> &lt;/desc&gt; </p>
<p> The maximum number of applications allowed for each URL is 8.</dl>
<h3>Devices interrupt activity (int.rrd)</h3>
<p>Only the limit and rigid values can be set here.</p>
<h3>Verlihub statistics (verlihub.rrd)</h3>
<p>This graph monitors the Verlihub software for DC++ network.</p>
<h3>Monitoring the Internet traffic of your LAN (traffacct.rrd)</h3>
<p>If your server acts as the gateway for a group of PCs, devices or even whole networks in your local LAN, you may want to know how much Internet traffic each one is generating. </p>
<p> This graph requires the <i><a href="/docs/linux/man/8-iptables/">iptables</a></i>(8) command on GNU/Linux systems, and the <i>ipfw</i> command on *BSD systems. </p>
<p> The following are the options you will need to configure to accomplish all of this. </p>
<p> <code>enabled</code></p>
<dl>
<dd>This option enables this feature. </p>
<p> Default value: <i>n</i></dl>
<p> <code>max</code></p>
<dl>
<dd>This is the number of LAN devices you want to monitor. There is no limit, but keep in mind that every time this number changes, Monitorix will resize the <i>traffacct.rrd</i> file, removing all historical data. </p>
<p> Default value: <i>10</i></dl>
<p> <code>graphs_per_row</code></p>
<dl>
<dd>If your horizontal screen resolution is pretty wide, you may want to increase the number of graphs that appear on each row. </p>
<p> Default value: <i>2</i></dl>
<p> <code>list</code></p>
<dl>
<dd>This is a comma-separated list of names of PCs, LAN devices or whole networks that you want to monitor. The only requirement is that all they must utilize this server as their gateway. </p>
<p> If the names in this list are able to be resolved by a DNS query then you don&#8217;t need to define the <code>desc</code> list (below) with corresponding IP addresses, unless you want monthly reports. </p>
<p> An example would be: </p>
<dl>
<dd>list = pc8, printer, scanner, lan3</dl>
</dl>
<p> <code>desc</code></p>
<dl>
<dd>This is the list of IP addresses with network masks and email addresses corresponding to the entries defined in the <code>list</code>. This option is only used when the those entries are not resolvable through a DNS query. </p>
<p> An example would be: </p>
<dl>
<dd>&lt;desc&gt;<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>0 = 192.168.1.101/32, ace [at] example.com</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>1 = 192.168.1.102/32, gene [at] example.com</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>2 = 192.168.1.103/32, paul [at] example.com</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>3 = 192.168.1.104/32, peter [at] example.com</p>
<p> &lt;/desc</dl>
</dl>
<h3>Monthly reports of Internet traffic (traffacct.rrd)</h3>
<p><code>enabled</code></p>
<dl>
<dd>If this option is set to <i>y</i>, Monitorix will send a report of all the monthly Internet activity of the defined devices in <code>list</code> to the specified email address on the first day of each month. </p>
<p> Default value: <i>n</i></dl>
<p> <code>language</code></p>
<dl>
<dd>Define here the language used in the monthly report. </p>
<p> The current possible values are: <i>ca</i>, <i>de</i>, <i>en</i>, <i>it</i>, <i>nl_NL</i>, <i>pl</i> and <i>zh_CN</i>. </p>
<p> Default value: <i>en</i></dl>
<p> <code>default_mail</code></p>
<dl>
<dd>This is the default email address used to send the monthly reports. This option is only used if the second parameter in <code>desc</code> list is empty. </p>
<p> Default value: <i>root [at] localhost</i></dl>
<p> <code>url_prefix</code></p>
<dl>
<dd>This is the prefix of the same URL you use to connect to Monitorix. This is needed in order to get the graphs of the same machine. </p>
<p> Default value: <i><a rel="nofollow" href="http://localhost:8080">http://localhost:8080</a></i></dl>
<p> <code>smtp_hostname</code></p>
<dl>
<dd>This is the hostname that will be used as a SMTP relay to deliver the monthly report emails. </p>
<p> Default value: <i>localhost</i></dl>
<p> <code>from_address</code></p>
<dl>
<dd>This is the address that will be used as remitent for all the monthly report emails. </p>
<p> Default value: <i>noreply [at] example.com</i></dl>
<h3>Monitoring remote servers (Multihost)</h3>
<p>The <i>Multihost</i> feature allows you to monitor an unlimitted number of remote servers that already have Monitorix installed. Make sure that all servers (local and remote) have the same version of Monitorix, otherwise there would be some incompatibilities that would prevent showing correctly the graphs. </p>
<p> <code>enabled</code></p>
<dl>
<dd>This option enables the <i>Multihost</i> feature. </p>
<p> Default value: <i>n</i></dl>
<p> <code>footer_url</code></p>
<dl>
<dd>If set to <i>y</i> Monitorix will show the original URL of each server at the bottom of the graph. Where security is important you may want to hide this information. </p>
<p> Default value: <i>y</i></dl>
<p> <code>graphs_per_row</code></p>
<dl>
<dd>If your horizontal screen resolution is pretty wide, you may want to increase the number of graphs that appear on each row. </p>
<p> Default value: <i>2</i></dl>
<p> <code>remotehost_list</code></p>
<dl>
<dd>This is a comma-separated list with descriptive names of remote servers with Monitorix already installed and working that you plan to monitor from here. </p>
<p> An example of this list would be: </p>
<dl>
<dd>remotehost_list = server 1, server 2, server 3</dl>
</dl>
<p> <code>remotehost_desc</code></p>
<dl>
<dd>This is a numbered list that describes each of the names defined in the <code>remotehost_list</code> option and the remote values of <code>base_url</code> and <code>base_cgi</code> options. </p>
<p> An example would be: </p>
<dl>
<dd>&lt;remotehost_desc&gt;<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>0 = <a rel="nofollow" href="http://www.example.com,/monitorix,/monitorix-cgi">http://www.example.com,/monitorix,/monitorix-cgi</a></p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>1 = <a rel="nofollow" href="http://10.0.0.1,/monitorix,/monitorix-cgi">http://10.0.0.1,/monitorix,/monitorix-cgi</a></p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>2 = <a rel="nofollow" href="http://192.168.0.100:8080,/,/">http://192.168.0.100:8080,/,/</a></p>
<p> &lt;/remotehost_desc&gt;</dl>
<p> As you can see all these three entries use URLs to designate the location of each remote server. This means that each server most also have been enabled the built-in HTTP server, or have been installed a CGI capable web server like Apache.</dl>
<p> <code>groups</code></p>
<dl>
<dd>This enables the server grouping for those environments where there are too much servers to display at the same time. Hence, you can group them in order to show them separatedly. </p>
<p> Default value: <i>n</i></dl>
<p> <code>remotegroup_list</code></p>
<dl>
<dd>This is a list of groups of remote servers with Monitorix already installed and working that you plan to monitor from here. </p>
<p> An example of this list would be: </p>
<dl>
<dd>remotegroup_list = My Group</dl>
</dl>
<p> <code>remotegroup_desc</code></p>
<dl>
<dd>This is a numbered list that describes each of the names defined in the <code>remotegroup_list</code> option. </p>
<p> An example would be: </p>
<dl>
<dd>&lt;remotegroup_desc&gt;<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>0 = server2, server 3</p>
<p> &lt;/remotegroup_desc&gt;</dl>
</dl>
<h3>Automatic email reports (emailreports)</h3>
<p>This allows to send automatically selected graphs to one or more email addresses. This could be specially useful for some system administrators who prefer receiving via email selected graphs instead of browsing to the remote servers every day. </p>
<p> <code>enabled</code></p>
<dl>
<dd>This option enables this feature. Note that you still need to enable the same option for each time interval you want to activate: <i>daily</i>, <i>weekly</i>, <i>monthly</i>, <i>yearly</i>. </p>
<p> Default value: <i>n</i></dl>
<p> <code>url_prefix</code></p>
<dl>
<dd>This is the prefix of the same URL you use to connect to Monitorix. Such URL is needed in order to get the graphs of that machine. </p>
<p> This option supports sending the credentials in the standard HTTP &quot;Authorization&quot; header, just like this: </p>
<p> <a rel="nofollow" href="http://username:password@localhost:8080">http://username:password@localhost:8080</a> </p>
<p> Default value: <i><a rel="nofollow" href="http://localhost:8080">http://localhost:8080</a></i></dl>
<p> <code>smtp_hostname</code></p>
<dl>
<dd>This is the hostname that will be used as a SMTP relay to deliver the automatic email reports.</dl>
<p> <code>method</code></p>
<dl>
<dd>This option specifies the method of sending emails. The current valid options are <i>smtp</i> and <i>relay</i>. By default this option is not defined which is the same as if <i>smtp</i> option was defined. </p>
<p> Default value:</dl>
<p> <code>from_address</code></p>
<dl>
<dd>This is the address that will be used as remitent for all the monthly report emails. </p>
<p> Default value: <i>noreply [at] example.com</i></dl>
<p> <code>hour</code></p>
<dl>
<dd>This is the hour (in 24h format) when the email reports will be sent. </p>
<p> Default value: <i>0</i></dl>
<p> <code>minute</code></p>
<dl>
<dd>This is the minute when the email reports will be sent. </p>
<p> Default value: <i>0</i></dl>
<p> <code>daily</code><br />
 <code>weekly</code><br />
 <code>monthly</code><br />
 <code>yearly</code></p>
<dl>
<dd>The email reports are sent based on the following schedule: </p>
<p> <i>daily</i> reports will be sent every day at 00:00h.<br />
 <i>weekly</i> reports will be sent the first Monday of each week.<br />
 <i>monthly</i> reports will be sent the first day of each month.<br />
 <i>yearly</i> reports will be sent the first day of each year.</dl>
<p> <code>enabled</code></p>
<dl>
<dd>This option enables each report individually. </p>
<p> Default value: <i>n</i></dl>
<p> <code>graphs</code></p>
<dl>
<dd>This is a comma-separated list of graph names you want to appear in the email report. The names are the same as their <i>.rrd</i> files. There is a list of them in the <code>graph_name</code> option in <i>monitorix.conf</i>. </p>
<p> Default value: <i>system, fs</i></dl>
<p> <code>to</code></p>
<dl>
<dd>This is a comma-separated list of recipient email addresses.</dl>
<p> <code>addendum_script</code></p>
<dl>
<dd>This is the full path name of an external script that will be executed during the creation of the report, and its output will be appended to the mail. This is useful for system administrators that want to add extra system information to the reports. </p>
<p> Default value:</dl>
<h3>rigid and limit values</h3>
<p><code>rigid</code></p>
<dl>
<dd>This value defines how the graph must be scaled. Its possible values are: </p>
<p> <i>0</i> No rigid, the graph will be scaled automatically. Only the lower-limit value will be used if it&#8217;s defined.<br />
 <i>1</i> The graph will be scaled by default according the values in <code>limit</code> but without rigidness.<br />
 <i>2</i> The graph will be forced to scale using the contents of <code>limit</code> as its upper-limit and lower-limit values.</dl>
<p> <code>limit</code></p>
<dl>
<dd>This is where you can enter the upper-limit and lower-limit values (separated by a colon) for a graph. The lower-limit value is optional. Some examples would be: </p>
<p> <i>100:0</i> which means <i>100</i> as the upper-limit value and <i>0</i> for the lower-limit value. This is commonly used for percentage values.<br />
 <i>1000</i> which means <i>1000</i> as the upper-limit value and leaving undefined the lower-limit value. This can also be written as <i>1000:</i>.</dl>
<h2>Author</h2>
<p>Monitorix is written by Jordi Sanfeliu &lt;jordi [at] fibranet.cat&gt;</p>
<h2>Copyright</h2>
<p>Copyright &#169; 2005-2016 Jordi Sanfeliu<br />
 Licensed under the GNU General Public License version 2 (GPLv2).</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-monitorix/">monitorix</a></code>(8), <code><a href="/docs/linux/man/1-rrdtool/">rrdtool</a></code>(1) </p>
