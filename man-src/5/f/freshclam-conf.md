---
title: "freshclam-conf(5)"
name: "freshclam-conf"
section: "5"
letter: "f"
url: "/docs/linux/man/5-freshclam-conf/"
description: "freshclam.conf – Configuration file for Clam AntiVirus database update tool"
---

<p><code>freshclam.conf</code> &#8211; Configuration file for Clam AntiVirus database update tool</p>
<h2>Description</h2>
<p>The file freshclam.conf configures the Clam AntiVirus Database Updater, <a href="/docs/linux/man/1-freshclam/">freshclam</a>(1).</p>
<h2>File Format</h2>
<p>The file consists of comments and options with arguments. Each line which starts with a hash (<code>#</code>) symbol is ignored by the parser. Options and arguments are case sensitive and of the form <code>Option Argument</code>. The arguments are of the following types:</p>
<dl>
<dt><code>BOOL</code></dt>
<dd>Boolean value (yes/no or true/false or 1/0).</dd>
<dt><code>STRING</code></dt>
<dd>String without blank characters.</dd>
<dt><code>SIZE</code></dt>
<dd>Size in bytes. You can use &#8216;M&#8217; or &#8216;m&#8217; modifiers for megabytes and &#8216;K&#8217; or &#8216;k&#8217; for kilobytes.</dd>
<dt><code>NUMBER</code></dt>
<dd>Unsigned integer.</dd></dl>
<h2>Directives</h2>
<p>When an option is not used (hashed or doesn&#8217;t exist in the configuration file) freshclam takes a default action.</p>
<dl>
<dt><code>Example</code></dt>
<dd>If this option is set freshclam will not run.</dd>
<dt><code>LogFileMaxSize SIZE</code></dt>
<dd>Limit the size of the log file. The logger will be automatically disabled if the file is greater than SIZE. Value of 0 disables the limit.<br/>
 Default: 1M</dd>
<dt><code>LogTime BOOL</code></dt>
<dd>Log time with each message.<br/>
 Default: no</dd>
<dt><code>LogSyslog BOOL</code></dt>
<dd>Enable logging to Syslog. May be used in combination with UpdateLogFile.<br/>
 Default: disabled.</dd>
<dt><code>LogFacility STRING</code></dt>
<dd>Specify the type of syslog messages &#8211; please refer to &#8216;man syslog&#8217; for facility names.<br/>
 Default: LOG_LOCAL6</dd>
<dt><code>LogVerbose BOOL</code></dt>
<dd>Enable verbose logging.<br/>
 Default: disabled</dd>
<dt><code>LogRotate BOOL</code></dt>
<dd>Rotate log file. Requires LogFileMaxSize option set prior to this option.<br/>
 Default: no</dd>
<dt><code>PidFile STRING</code></dt>
<dd>This option allows you to save the process identifier of the daemon to a file specified in the argument.<br/>
 Default: disabled</dd>
<dt><code>DatabaseDirectory STRING</code></dt>
<dd>Path to a directory containing database files.<br/>
 Default: /var/lib/clamav</dd>
<dt><code>Foreground BOOL</code></dt>
<dd>Don&#8217;t fork into background.<br/>
 Default: no</dd>
<dt><code>Debug BOOL</code></dt>
<dd>Enable debug messages in libclamav.<br/>
 Default: no</dd>
<dt><code>AllowSupplementaryGroups BOOL</code></dt>
<dd>Initialize supplementary group access (freshclam must be started by root).<br/>
 Default: disabled</dd>
<dt><code>UpdateLogFile STRING</code></dt>
<dd>Enable logging to a specified file. Highly recommended.<br/>
 Default: disabled.</dd>
<dt><code>DatabaseOwner STRING</code></dt>
<dd>When started by root, drop privileges to a specified user.<br/>
 Default:</dd>
<dt><code>Checks NUMBER</code></dt>
<dd>Number of database checks per day.<br/>
 Default: 12</dd>
<dt><code>DNSDatabaseInfo STRING</code></dt>
<dd>Use DNS to verify the virus database version. Freshclam uses DNS TXT records to verify the versions of the database and software itself. With this directive you can change the database verification domain.<br/>
 <code>WARNING:</code> Please don&#8217;t change it unless you&#8217;re configuring freshclam to use your own database verification domain.<br/>
 Default: enabled, pointing to current.cvd.clamav.net</dd>
<dt><code>DatabaseMirror STRING</code></dt>
<dd>DatabaseMirror specifies to which mirror(s) freshclam should connect. You should have at least two entries: db.XY.clamav.net (or db.XY.ipv6.clamav.net for IPv6) and database.clamav.net (in this order). Please replace XY with your country code (see <a rel="nofollow" href="http://www.iana.org/cctld/cctld-whois.htm">http://www.iana.org/cctld/cctld-whois.htm</a>). database.clamav.net is a round-robin record which points to our most reliable mirrors. It&#8217;s used as a fall back in case db.XY.clamav.net is not working.<br/>
 Default: database.clamav.net</dd>
<dt><code>PrivateMirror STR</code></dt>
<dd>This option allows you to easily point freshclam to private mirrors. If PrivateMirror is set, freshclam does not attempt to use DNS to determine whether its databases are out-of-date, instead it will use the If-Modified-Since request or directly check the headers of the remote database files. For each database, freshclam first attempts to download the CLD file. If that fails, it tries to download the CVD file. This option overrides DatabaseMirror, DNSDatabaseInfo and ScriptedUpdates. It can be used multiple times to provide fall-back mirrors.<br/>
 Default: disabled</dd>
<dt><code>MaxAttempts NUMBER</code></dt>
<dd>How many attempts (per mirror) to make before giving up.<br/>
 Default: 3 (per mirror)</dd>
<dt><code>ScriptedUpdates BOOL</code></dt>
<dd>With this option you can control scripted updates. It&#8217;s highly recommended to keep it enabled.<br/>
 Default: yes</dd>
<dt><code>TestDatabases BOOL</code></dt>
<dd>With this option enabled, freshclam will attempt to load new databases into memory to make sure they are properly handled by libclamav before replacing the old ones.<br/>
 Default: enabled</dd>
<dt><code>CompressLocalDatabase BOOL</code></dt>
<dd>By default freshclam will keep the local databases (.cld) uncompressed to make their handling faster. With this option you can enable the compression; the change will take effect with the next database update.<br/>
 Default: no</dd>
<dt><code>ExtraDatabase STRING</code></dt>
<dd>Download an additional 3rd party signature database distributed through the ClamAV mirrors. This option can be used multiple times. Here you can find a list of available databases: <a rel="nofollow" href="http://www.clamav.net/download/cvd/3rdparty">http://www.clamav.net/download/cvd/3rdparty</a><br/>
 Default: disabled</dd>
<dt><code>DatabaseCustomURL STRING</code></dt>
<dd>With this option you can provide custom sources (http:// or file://) for database files. This option can be used multiple times.<br/>
 Default: disabled</dd>
<dt><code>HTTPProxyServer STR</code>, <code>HTTPProxyPort NUMBER</code></dt>
<dd>Use given proxy server and TCP port for database downloads. HTTPProxyPort defaults to 8080.</dd>
<dt><code>HTTPProxyUsername STR</code>,<code>HTTPProxyPassword STRING</code></dt>
<dd>Proxy usage is authenticated through given username and password.<br/>
 Default: disabled</dd>
<dt><code>HTTPUserAgent STRING</code></dt>
<dd>If your servers are behind a firewall/proxy which applies User-Agent filtering, you can use this option to force the use of a different User-Agent header.<br/>
 Default: clamav/version_number</dd>
<dt><code>NotifyClamd STRING</code></dt>
<dd>Notify a running <a href="/docs/linux/man/8-clamd/">clamd</a>(8) to reload its database after a download has occurred. The path for clamd.conf file must be provided.<br/>
 Default: The default is to not notify clamd. See <a href="/docs/linux/man/5-clamd-conf/">clamd.conf</a>(5)&#8217;s option SelfCheck for how <a href="/docs/linux/man/8-clamd/">clamd</a>(8) handles database updates in this case.</dd>
<dt><code>OnUpdateExecute STRING</code></dt>
<dd>Execute this command after the database has been successfully updated.<br/>
 Default: disabled</dd>
<dt><code>OnErrorExecute STRING</code></dt>
<dd>Execute this command after a database update has failed.<br/>
 Default: disabled</dd>
<dt><code>OnOutdatedExecute STRING</code></dt>
<dd>Execute this command when freshclam reports outdated version. In the command string %v will be replaced by the new version number.<br/>
 Default: disabled</dd>
<dt><code>LocalIPAddress IP</code></dt>
<dd>Use <code>IP</code> as client address for downloading databases. Useful for multi homed systems.<br/>
 Default: Use OS&#8217;es default outgoing IP address.</dd>
<dt><code>ConnectTimeout NUMBER</code></dt>
<dd>Timeout in seconds when connecting to database server.<br/>
 Default: 10</dd>
<dt><code>ReceiveTimeout NUMBER</code></dt>
<dd>Timeout in seconds when reading from database server.<br/>
 Default: 30</dd>
<dt><code>SubmitDetectionStats STRING</code></dt>
<dd>When enabled freshclam will submit statistics to the ClamAV Project about the latest virus detections in your environment. The ClamAV maintainers will then use this data to determine what types of malware are the most detected in the field and in what geographic area they are. Freshclam will connect to clamd in order to get the recent statistics. The path for clamd.conf file must be provided.<br/>
 Default: disabled</dd>
<dt><code>DetectionStatsCountry STRING</code></dt>
<dd>Country of origin of malware/detection statistics (for statistical purposes only). The statistics collector at ClamAV.net will look up your IP address to determine the geographical origin of the malware reported by your installation. If this installation is mainly used to scan data which comes from a different location, please enable this option and enter a two-letter code (see <a rel="nofollow" href="http://www.iana.org/domains/root/db/)">http://www.iana.org/domains/root/db/)</a> of the country of origin.<br/>
 Default: disabled</dd>
<dt><code>DetectionStatsHostID STRING</code></dt>
<dd>This option enables support for our &quot;Personal Statistics&quot; service. When this option is enabled, the information on malware detected by your clamd installation is made available to you through our website. To get your HostID, log on <a rel="nofollow" href="http://www.stats.clamav.net">http://www.stats.clamav.net</a> and add a new host to your host list. Once you have the HostID, uncomment this option and paste the HostID here. As soon as your freshclam starts submitting information to our stats collecting service, you will be able to view the statistics of this clamd installation by logging into <a href="http://www.stats.clamav.net">http://www.stats.clamav.net</a> with the same credentials you used to generate the HostID. For more information refer to: <a href="http://www.clamav.net/documents/clamav-community-threat-tracking-system/.">http://www.clamav.net/documents/clamav-community-threat-tracking-system/.</a> This feature requires SubmitDetectionStats to be enabled.<br/>
 Default: disabled</dd>
<dt><code>SafeBrowsing BOOL</code></dt>
<dd>This option enables support for Google Safe Browsing. When activated for the first time, freshclam will download a new database file (safebrowsing.cvd) which will be automatically loaded by clamd and clamscan during the next reload, provided that the heuristic phishing detection is turned on. This database includes information about websites that may be phishing sites or possible sources of malware. When using this option, it&#8217;s mandatory to run freshclam at least every 30 minutes. Freshclam uses the ClamAV&#8217;s mirror infrastructure to distribute the database and its updates but all the contents are provided under Google&#8217;s terms of use. See <a rel="nofollow" href="http://code.google.com/support/bin/answer.py?answer=70015">http://code.google.com/support/bin/answer.py?answer=70015</a> and <a href="http://safebrowsing.clamav.net">http://safebrowsing.clamav.net</a> for more information.<br/>
 Default: disabled</dd>
<dt><code>Bytecode BOOL</code></dt>
<dd>This option enables downloading of bytecode.cvd, which includes additional detection mechanisms and improvements to the ClamAV engine.<br/>
 Default: enabled</dd></dl>
<h2>Files</h2>
<p>/etc/freshclam.conf</p>
<h2>Author</h2>
<p>Thomas Lamy &lt;thomas.lamy [at] netwake.de&gt;, Tomasz Kojm &lt;tkojm [at] clamav.net&gt;, Kevin Lin &lt;klin [at] sourcefire.com&gt;</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-freshclam/">freshclam</a>(1), <a href="/docs/linux/man/5-clamd-conf/">clamd.conf</a>(5), <a href="/docs/linux/man/8-clamd/">clamd</a>(8), <a href="/docs/linux/man/1-clamscan/">clamscan</a>(1) </p>
