---
title: "freshclam(5)"
name: "freshclam"
section: "5"
letter: "f"
url: "/docs/linux/man/5-freshclam/"
description: "freshclam.conf – Configuration file for Clam AntiVirus database update tool"
---

<p><code>freshclam.conf</code> &#8211; Configuration file for Clam AntiVirus database update tool</p>
<h2>Description</h2>
<p>The file freshclam.conf configures the Clam AntiVirus Database Updater, <a href="/docs/linux/man/1-freshclam/">freshclam</a>(1).</p>
<h2>File Format</h2>
<p>The file consists of comments and options with arguments. Each line which starts with a hash (<code>#</code>) symbol is ignored by the parser. Options and arguments are case sensitive and of the form <code>Option Argument</code>. The arguments are of the following types:</p>
<dl>
<dt><code>BOOL</code></p>
<dd>Boolean value (yes/no or true/false or 1/0).</p>
<dt><code>STRING</code></p>
<dd>String without blank characters.</p>
<dt><code>SIZE</code></p>
<dd>Size in bytes. You can use &#8216;M&#8217; or &#8216;m&#8217; modifiers for megabytes and &#8216;K&#8217; or &#8216;k&#8217; for kilobytes.</p>
<dt><code>NUMBER</code></p>
<dd>Unsigned integer.</dl>
<h2>Directives</h2>
<p>When an option is not used (hashed or doesn&#8217;t exist in the configuration file) freshclam takes a default action.</p>
<dl>
<dt><code>Example</code></p>
<dd>If this option is set freshclam will not run.</p>
<dt><code>DatabaseOwner STRING</code></p>
<dd>When started by root, drop privileges to a specified user.<br />
 Default:</p>
<dt><code>AllowSupplementaryGroups BOOL</code></p>
<dd>Initialize supplementary group access (freshclam must be started by root).<br />
 Default: disabled</p>
<dt><code>DatabaseDirectory STRING</code></p>
<dd>Path to a directory containing database files.<br />
 Default: /var/lib/clamav</p>
<dt><code>Checks NUMBER</code></p>
<dd>Number of database checks per day.<br />
 Default: 12</p>
<dt><code>UpdateLogFile STRING</code></p>
<dd>Enable logging to a specified file. Highly recommended.<br />
 Default: disabled.</p>
<dt><code>LogSyslog BOOL</code></p>
<dd>Enable logging to Syslog. May be used in combination with UpdateLogFile.<br />
 Default: disabled.</p>
<dt><code>LogFacility STRING</code></p>
<dd>Specify the type of syslog messages &#8211; please refer to &#8216;man syslog&#8217; for facility names.<br />
 Default: LOG_LOCAL6</p>
<dt><code>PidFile STRING</code></p>
<dd>This option allows you to save the process identifier of the daemon to a file specified in the argument.<br />
 Default: disabled</p>
<dt><code>LogVerbose BOOL</code></p>
<dd>Enable verbose logging.<br />
 Default: disabled</p>
<dt><code>DNSDatabaseInfo STRING</code></p>
<dd>This directive enables database and software version checks through DNS TXT records.<br />
 Default: enabled, pointing to current.cvd.clamav.net</p>
<dt><code>DatabaseMirror STRING</code></p>
<dd>Server name where database updates are downloaded from. In order to download the database from the closest mirror you should configure freshclam to use db.xy.clamav.net where xy represents your country code. If this option is given multiple times, <a href="/docs/linux/man/1-freshclam/">freshclam</a>(1) tries them in the order given. It&#8217;s strongly recommended that you use db.xy.clamav.net as the first mirror and database.clamav.net as the second.<br />
 Default: database.clamav.net</p>
<dt><code>MaxAttempts NUMBER</code></p>
<dd>How many attempts (per mirror) to make before giving up.<br />
 Default: 3 (per mirror)</p>
<dt><code>ScriptedUpdates BOOL</code></p>
<dd>With this option you can control scripted updates. It&#8217;s highly recommended to keep it enabled.<br />
 Default: enabled</p>
<dt><code>CompressLocalDatabase BOOL</code></p>
<dd>By default freshclam will keep the local databases (.cld) uncompressed to make their handling faster. With this option you can enable the compression; the change will take effect with the next database update.<br />
 Default: no</p>
<dt><code>HTTPProxyServer STR</code>, <code>HTTPProxyPort NUMBER</code></p>
<dd>Use given proxy server and TCP port for database downloads.</p>
<dt><code>HTTPProxyUsername STR</code>,<code>HTTPProxyPassword STRING</code></p>
<dd>Proxy usage is authenticated through given username and password.<br />
 Default: no proxy authentication</p>
<dt><code>HTTPUserAgent STRING</code></p>
<dd>If your servers are behind a firewall/proxy which applies User-Agent filtering, you can use this option to force the use of a different User-Agent header.<br />
 Default: clamav/version_number</p>
<dt><code>LocalIPAddress IP</code></p>
<dd>Use <code>IP</code> as client address for downloading databases. Useful for multi homed systems.<br />
 Default: Use OS&#8217;es default outgoing IP address.</p>
<dt><code>NotifyClamd STRING</code></p>
<dd>Notify a running <a href="/docs/linux/man/8-clamd/">clamd</a>(8) to reload its database after a download has occurred. The path for clamd.conf file must be provided.<br />
 Default: The default is to not notify clamd. See <a href="/docs/linux/man/5-clamd-conf/">clamd.conf</a>(5)&#8217;s option SelfCheck for how <a href="/docs/linux/man/8-clamd/">clamd</a>(8) handles database updates in this case.</p>
<dt><code>OnUpdateExecute STRING</code></p>
<dd>Execute this command after the database has been successfully updated.<br />
 Default: disabled</p>
<dt><code>OnOutdatedExecute STRING</code></p>
<dd>Execute this command when freshclam reports outdated version. In the command string %v will be replaced by the new version number.<br />
 Default: disabled</p>
<dt><code>OnErrorExecute STRING</code></p>
<dd>Execute this command after a database update has failed.<br />
 Default: disabled</p>
<dt><code>ConnectTimeout NUMBER</code></p>
<dd>Timeout in seconds when connecting to database server.<br />
 Default: 10</p>
<dt><code>ReceiveTimeout NUMBER</code></p>
<dd>Timeout in seconds when reading from database server.<br />
 Default: 30</p>
<dt><code>SubmitDetectionStats STRING</code></p>
<dd>When enabled freshclam will submit statistics to the ClamAV Project about the latest virus detections in your environment. The ClamAV maintainers will then use this data to determine what types of malware are the most detected in the field and in what geographic area they are. This feature requires LogTime and LogFile to be enabled in clamd.conf. The path for clamd.conf file must be provided.<br />
 Default: disabled</p>
<dt><code>DetectionStatsCountry STRING</code></p>
<dd>Country of origin of malware/detection statistics (for statistical purposes only). The statistics collector at ClamAV.net will look up your IP address to determine the geographical origin of the malware reported by your installation. If this installation is mainly used to scan data which comes from a different location, please enable this option and enter a two-letter code (see <a rel="nofollow" href="http://www.iana.org/domains/root/db/)">http://www.iana.org/domains/root/db/)</a> of the country of origin.<br />
 Default: disabled</dl>
<h2>Files</h2>
<p>/etc/freshclam.conf</p>
<h2>Author</h2>
<p>Thomas Lamy &lt;thomas.lamy [at] netwake.de&gt;, Tomasz Kojm &lt;tkojm [at] clamav.net&gt;</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-freshclam/">freshclam</a>(1), <a href="/docs/linux/man/5-clamd-conf/">clamd.conf</a>(5), <a href="/docs/linux/man/8-clamd/">clamd</a>(8), <a href="/docs/linux/man/8-clamav-milter/">clamav-milter</a>(8), <a href="/docs/linux/man/1-clamscan/">clamscan</a>(1) </p>
