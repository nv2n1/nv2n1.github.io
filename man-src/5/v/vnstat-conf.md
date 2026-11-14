---
title: "vnstat-conf(5)"
name: "vnstat-conf"
section: "5"
letter: "v"
url: "/docs/linux/man/5-vnstat-conf/"
description: "vnstat.conf – vnStat configuration file"
---

<p>vnstat.conf &#8211; vnStat configuration file </p>
<h2>Synopsis</h2>
<p><code>/etc/vnstat.conf</code> </p>
<h2>Description</h2>
<p><code><a href="/docs/linux/man/1-vnstat/">vnstat</a></code>(1), <code><a href="/docs/linux/man/1-vnstati/">vnstati</a></code>(1) and <code><a href="/docs/linux/man/1-vnstatd/">vnstatd</a></code>(1) all use the same configuration file for configuration related settings. Some of the settings are common for all three programs. The file consists of keyword-argument pairs, one per line. Empty lines and lines starting with&nbsp;<wbr>&#8216;#&#8217; are interpreted as comments and not processed. Arguments may optionally be enclosed in double quotes (&quot;) in order to represent arguments containing spaces. Arguments can be padded with spaces or tabulator characters. A hardcoded default value will be used if a keyword can&#8217;t be found from the configuration file. The configuration file is divided into three sections based on the usage of each keyword. The first section contains keywords that are considered generic for all commands, the second section is for daemon related keywords and the last section for image output. </p>
<h2>Common Keywords</h2>
<dl>
<dt><code>BandwidthDetection</code></p>
<dd>Try to automatically detect <code>MaxBandwidth</code> value for each monitored interface. Mostly only ethernet interfaces support this feature. <code>MaxBandwidth</code> or interface specfic <code>MaxBW</code> will be used as fallback value if detection fails. 1 = enabled, 0 = disabled. (vnstat and vnstatd only) </p>
<dt><code>BootVariation</code></p>
<dd>Time in seconds how much the boot time reported by system kernel can variate between updates. Value range: 0..300 </p>
<dt><code>CheckDiskSpace</code></p>
<dd>Enable or disable the availability check of at least some free disk space before a database write. 1 = enabled, 0 = disabled. </p>
<dt><code>DatabaseDir</code></p>
<dd>Specifies the directory where interface databases are to be stored. A full path must be given and a leading &#8216;/&#8217; isn&#8217;t required. </p>
<dt><code>DayFormat, MonthFormat, TopFormat</code></p>
<dd>Formatting of date in available outputs. Uses the same format as <code><a href="/docs/linux/man/1-date/">date</a></code>(1). (vnstat and vnstati only) </p>
<dt><code>Interface</code></p>
<dd>Default interface used when no other interface is specified on the command line. (vnstat and vnstati only) </p>
<dt><code>Locale</code></p>
<dd>Locale setting to be used for prints. This replaces the LC_ALL environment variable. Set to &quot;-&quot; or leave empty in order to use the system default value. (vnstat and vnstati only) </p>
<dt><code>MaxBandwidth</code></p>
<dd>Maximum bandwidth for all interfaces. If the interface specific traffic exceeds the given value then the data is assumed to be invalid and rejected. Set to 0 in order to disable the feature. Value range: 0..50000 (vnstat and vnstatd only) </p>
<dt><code>MaxBW</code></p>
<dd>Same as MaxBandwidth but can be used for setting individual limits for selected interfaces. The name of the interface is specified directly after the MaxBW keyword without spaces. For example MaxBWeth0 for eth0 and MaxBWppp0 for ppp0. Value range: 0..50000 (vnstat and vnstatd only) </p>
<dt><code>MonthRotate</code></p>
<dd>Day of month that months are expected to change. Usually set to 1 but can be set to alternative values for example for tracking monthly billed traffic where the billing period doesn&#8217;t start on the first day. Value range: 1..28 (vnstat and vnstatd only) </p>
<dt><code>OutputStyle</code></p>
<dd>Modify the content and style of text outputs. 0 = minimal and narrow output for terminal with limited width, 1 = normal output with bar column visible, 2 = same as 1 except rate is visible in summary and weekly outputs, 3 = rate column is visible in all outputs where it is supported. (vnstat and vnstati only) </p>
<dt><code>QueryMode</code></p>
<dd>Default query mode when no parameters are given. 0 = normal, 1 = days, 2 = months, 3 = top10, 4 = exportdb, 5 = short, 6 = weeks, 7 = hours and 8 = xml. (vnstat only) </p>
<dt><code>RateUnit</code></p>
<dd>Select which unit is used when traffic rate is visible. 0 = bytes, 1 = bits. (vnstat and vnstati only) </p>
<dt><code>RXCharacter, TXCharacter</code></p>
<dd>Character used for representing the percentual share of received and transmitted traffic in daily output. (vnstat only) </p>
<dt><code>RXHourCharacter, TXHourCharacter</code></p>
<dd>Character used for representing the percentual share of received and transmitted traffic in hourly output. (vnstat only) </p>
<dt><code>Sampletime</code></p>
<dd>Defines how many seconds the -tr option will sample traffic. Value range: 2..600 (vnstat only) </p>
<dt><code>TrafficlessDays</code></p>
<dd>Log days without any traffic to daily list. 1 = enabled, 0 = disabled. (vnstat and vnstatd only) </p>
<dt><code>UnitMode</code></p>
<dd>Select how units are prefixed. This will option changes only the prefix, not how traffic is calculated. 0 = IEC standard prefixes (KiB/MiB/GiB/TiB), 1 = old style binary prefixes (KB/MB/GB/TB). (vnstat and vnstati only) </p>
<dt><code>UseFileLocking</code></p>
<dd>Enable or disable the use of file locking during database access. Disabling file locking may cause database corruption if several processes are trying to write to the file at the same time. </p>
</dl>
<h2>Daemon Related Keywords</h2>
<dl>
<dt><code>BandwidthDetectionInterval</code></p>
<dd>How often in minutes interface specific detection of <code>MaxBandwidth</code> is done for detecting possible changes when <code>BandwidthDetection</code> is enabled. Can be disabled by setting to 0. Value range: 0..30 </p>
<dt><code>CreateDirs</code></p>
<dd>Enable or disable the creation of directories when a configured path doesn&#8217;t exist. This includes <code>DatabaseDir</code> , <code>LogFile</code> and <code>PidFile</code> directories. The <code>LogFile</code> directory will be created only when <code>UseLogging</code> has been set to 1. The <code>PidFile</code> directory will be created only if the daemon is started as a background process. The daemon process will try to create the directory using permissions of the user used to start the process. </p>
<dt><code>DaemonGroup</code></p>
<dd>Specify the user to which the daemon process will switch during startup. The user can either be the name of the group or a numerical group id. Leave empty to disable the group switch. This option can only be used when the process is started as root. </p>
<dt><code>DaemonUser</code></p>
<dd>Specify the user to which the daemon process will switch during startup. The user can either be the login of the user or a numerical user id. Leave empty to disable the user switch. This option can only be used when the process is started as root. </p>
<dt><code>LogFile</code></p>
<dd>Specify log file path and name to be used if UseLogging is set to 1. </p>
<dt><code>OfflineSaveInterval</code></p>
<dd>How often in minutes cached interface data is saved to file when all monitored interfaces are offline. Value range: <code>SaveInterval</code>..60 </p>
<dt><code>PidFile</code></p>
<dd>Specify pid file path and name to be used. </p>
<dt><code>PollInterval</code></p>
<dd>How often in seconds interfaces are checked for status changes. Value range: 2..300 </p>
<dt><code>SaveInterval</code></p>
<dd>How often in minutes cached interface data is saved to file. Value range: ( <code>UpdateInterval</code> / 60 )..60 </p>
<dt><code>SaveOnStatusChange</code></p>
<dd>Enable or disable the additional saving to file of cached interface data when the availability of an interface changes, i.e., when an interface goes offline or comes online. 1 = enabled, 0 = disabled. </p>
<dt><code>UpdateFileOwner</code></p>
<dd>Enable or disable the update of file ownership during daemon process startup. Only database, log and pid files will be modified if the user or group change feature is enabled and the files don&#8217;t match the requested user or group. This option can only be used when the process is started as root. </p>
<dt><code>UpdateInterval</code></p>
<dd>How often in seconds the interface data is updated. Value range: <code>PollInterval</code>..300 </p>
<dt><code>UseLogging</code></p>
<dd>Enable or disable logging. 0 = disabled, 1 = logfile and 2 = syslog. </p>
</dl>
<h2>Image Output Related Keywords</h2>
<dl>
<dt><code>CBackground</code></p>
<dd>Background color. </p>
<dt><code>CEdge</code></p>
<dd>Edge color if visible. </p>
<dt><code>CHeader</code></p>
<dd>Header background color. </p>
<dt><code>CHeaderTitle</code></p>
<dd>Header title text color. </p>
<dt><code>CHeaderDate</code></p>
<dd>Header date text color. </p>
<dt><code>CLine</code></p>
<dd>Line color. </p>
<dt><code>CLineL</code></p>
<dd>Lighter version of line color. Set to &#8216;-&#8216; in order to use a calculated value based on CLine. </p>
<dt><code>CRx</code></p>
<dd>Color for received data. </p>
<dt><code>CRxD</code></p>
<dd>Darker version of received data color. Set to &#8216;-&#8216; in order to use a calculated value based on CRx. </p>
<dt><code>CText</code></p>
<dd>Common text color. </p>
<dt><code>CTx</code></p>
<dd>Color for transmitted data. </p>
<dt><code>CTxD</code></p>
<dd>Darker version of transmitted data color. Set to &#8216;-&#8216; in order to use a calculated value based on CTx. </p>
<dt><code>HeaderFormat</code></p>
<dd>Formatting of date in header. Uses the same format as <code><a href="/docs/linux/man/1-date/">date</a></code>(1). </p>
<dt><code>HourlyRate</code></p>
<dd>Show hours with rate instead of transfered amount. 1 = enabled, 0 = disabled. </p>
<dt><code>SummaryLayout</code></p>
<dd>Select the used layout of the summary output. 1 = layout introduced in version 1.8 with monthly traffic included, 0 = layout used before version 1.8, doesn&#8217;t contain monthly traffic and doesn&#8217;t support average rate. </p>
<dt><code>SummaryRate</code></p>
<dd>Show rate in summary output if available. 1 = enabled, 0 = disabled. </p>
<dt><code>TransparentBg</code></p>
<dd>Set background color as transparent. 1 = enabled, 0 = disabled. </p>
</dl>
<h2>Files</h2>
<dl>
<dt><i>/etc/vnstat.conf</i></p>
<dd>Config file that will be used unless <i>$HOME/.vnstatrc</i> exists or alternative value is given as command line parameter. </p>
</dl>
<h2>Restrictions</h2>
<p>Using long date output formats may cause misalignment in shown columns if the length of the date exceeds the fixed size allocation.</p>
<h2>Author</h2>
<p>Teemu Toivola &lt;tst at iki dot fi&gt;</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-vnstat/">vnstat</a></code>(1), <code><a href="/docs/linux/man/1-vnstati/">vnstati</a></code>(1), <code><a href="/docs/linux/man/1-vnstatd/">vnstatd</a></code>(1), <code><a href="/docs/linux/man/7-units/">units</a></code>(7) </p>
