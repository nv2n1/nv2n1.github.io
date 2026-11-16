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
<dt><code>BandwidthDetection</code></dt>
<dd>Try to automatically detect <code>MaxBandwidth</code> value for each monitored interface. Mostly only ethernet interfaces support this feature. <code>MaxBandwidth</code> or interface specfic <code>MaxBW</code> will be used as fallback value if detection fails. 1 = enabled, 0 = disabled. (vnstat and vnstatd only) </dd>
<dt><code>BootVariation</code></dt>
<dd>Time in seconds how much the boot time reported by system kernel can variate between updates. Value range: 0..300 </dd>
<dt><code>CheckDiskSpace</code></dt>
<dd>Enable or disable the availability check of at least some free disk space before a database write. 1 = enabled, 0 = disabled. </dd>
<dt><code>DatabaseDir</code></dt>
<dd>Specifies the directory where interface databases are to be stored. A full path must be given and a leading &#8216;/&#8217; isn&#8217;t required. </dd>
<dt><code>DayFormat, MonthFormat, TopFormat</code></dt>
<dd>Formatting of date in available outputs. Uses the same format as <code><a href="/docs/linux/man/1-date/">date</a></code>(1). (vnstat and vnstati only) </dd>
<dt><code>Interface</code></dt>
<dd>Default interface used when no other interface is specified on the command line. (vnstat and vnstati only) </dd>
<dt><code>Locale</code></dt>
<dd>Locale setting to be used for prints. This replaces the LC_ALL environment variable. Set to &quot;-&quot; or leave empty in order to use the system default value. (vnstat and vnstati only) </dd>
<dt><code>MaxBandwidth</code></dt>
<dd>Maximum bandwidth for all interfaces. If the interface specific traffic exceeds the given value then the data is assumed to be invalid and rejected. Set to 0 in order to disable the feature. Value range: 0..50000 (vnstat and vnstatd only) </dd>
<dt><code>MaxBW</code></dt>
<dd>Same as MaxBandwidth but can be used for setting individual limits for selected interfaces. The name of the interface is specified directly after the MaxBW keyword without spaces. For example MaxBWeth0 for eth0 and MaxBWppp0 for ppp0. Value range: 0..50000 (vnstat and vnstatd only) </dd>
<dt><code>MonthRotate</code></dt>
<dd>Day of month that months are expected to change. Usually set to 1 but can be set to alternative values for example for tracking monthly billed traffic where the billing period doesn&#8217;t start on the first day. Value range: 1..28 (vnstat and vnstatd only) </dd>
<dt><code>OutputStyle</code></dt>
<dd>Modify the content and style of text outputs. 0 = minimal and narrow output for terminal with limited width, 1 = normal output with bar column visible, 2 = same as 1 except rate is visible in summary and weekly outputs, 3 = rate column is visible in all outputs where it is supported. (vnstat and vnstati only) </dd>
<dt><code>QueryMode</code></dt>
<dd>Default query mode when no parameters are given. 0 = normal, 1 = days, 2 = months, 3 = top10, 4 = exportdb, 5 = short, 6 = weeks, 7 = hours and 8 = xml. (vnstat only) </dd>
<dt><code>RateUnit</code></dt>
<dd>Select which unit is used when traffic rate is visible. 0 = bytes, 1 = bits. (vnstat and vnstati only) </dd>
<dt><code>RXCharacter, TXCharacter</code></dt>
<dd>Character used for representing the percentual share of received and transmitted traffic in daily output. (vnstat only) </dd>
<dt><code>RXHourCharacter, TXHourCharacter</code></dt>
<dd>Character used for representing the percentual share of received and transmitted traffic in hourly output. (vnstat only) </dd>
<dt><code>Sampletime</code></dt>
<dd>Defines how many seconds the -tr option will sample traffic. Value range: 2..600 (vnstat only) </dd>
<dt><code>TrafficlessDays</code></dt>
<dd>Log days without any traffic to daily list. 1 = enabled, 0 = disabled. (vnstat and vnstatd only) </dd>
<dt><code>UnitMode</code></dt>
<dd>Select how units are prefixed. This will option changes only the prefix, not how traffic is calculated. 0 = IEC standard prefixes (KiB/MiB/GiB/TiB), 1 = old style binary prefixes (KB/MB/GB/TB). (vnstat and vnstati only) </dd>
<dt><code>UseFileLocking</code></dt>
<dd>Enable or disable the use of file locking during database access. Disabling file locking may cause database corruption if several processes are trying to write to the file at the same time. </dd>
</dl>
<h2>Daemon Related Keywords</h2>
<dl>
<dt><code>BandwidthDetectionInterval</code></dt>
<dd>How often in minutes interface specific detection of <code>MaxBandwidth</code> is done for detecting possible changes when <code>BandwidthDetection</code> is enabled. Can be disabled by setting to 0. Value range: 0..30 </dd>
<dt><code>CreateDirs</code></dt>
<dd>Enable or disable the creation of directories when a configured path doesn&#8217;t exist. This includes <code>DatabaseDir</code> , <code>LogFile</code> and <code>PidFile</code> directories. The <code>LogFile</code> directory will be created only when <code>UseLogging</code> has been set to 1. The <code>PidFile</code> directory will be created only if the daemon is started as a background process. The daemon process will try to create the directory using permissions of the user used to start the process. </dd>
<dt><code>DaemonGroup</code></dt>
<dd>Specify the user to which the daemon process will switch during startup. The user can either be the name of the group or a numerical group id. Leave empty to disable the group switch. This option can only be used when the process is started as root. </dd>
<dt><code>DaemonUser</code></dt>
<dd>Specify the user to which the daemon process will switch during startup. The user can either be the login of the user or a numerical user id. Leave empty to disable the user switch. This option can only be used when the process is started as root. </dd>
<dt><code>LogFile</code></dt>
<dd>Specify log file path and name to be used if UseLogging is set to 1. </dd>
<dt><code>OfflineSaveInterval</code></dt>
<dd>How often in minutes cached interface data is saved to file when all monitored interfaces are offline. Value range: <code>SaveInterval</code>..60 </dd>
<dt><code>PidFile</code></dt>
<dd>Specify pid file path and name to be used. </dd>
<dt><code>PollInterval</code></dt>
<dd>How often in seconds interfaces are checked for status changes. Value range: 2..300 </dd>
<dt><code>SaveInterval</code></dt>
<dd>How often in minutes cached interface data is saved to file. Value range: ( <code>UpdateInterval</code> / 60 )..60 </dd>
<dt><code>SaveOnStatusChange</code></dt>
<dd>Enable or disable the additional saving to file of cached interface data when the availability of an interface changes, i.e., when an interface goes offline or comes online. 1 = enabled, 0 = disabled. </dd>
<dt><code>UpdateFileOwner</code></dt>
<dd>Enable or disable the update of file ownership during daemon process startup. Only database, log and pid files will be modified if the user or group change feature is enabled and the files don&#8217;t match the requested user or group. This option can only be used when the process is started as root. </dd>
<dt><code>UpdateInterval</code></dt>
<dd>How often in seconds the interface data is updated. Value range: <code>PollInterval</code>..300 </dd>
<dt><code>UseLogging</code></dt>
<dd>Enable or disable logging. 0 = disabled, 1 = logfile and 2 = syslog. </dd>
</dl>
<h2>Image Output Related Keywords</h2>
<dl>
<dt><code>CBackground</code></dt>
<dd>Background color. </dd>
<dt><code>CEdge</code></dt>
<dd>Edge color if visible. </dd>
<dt><code>CHeader</code></dt>
<dd>Header background color. </dd>
<dt><code>CHeaderTitle</code></dt>
<dd>Header title text color. </dd>
<dt><code>CHeaderDate</code></dt>
<dd>Header date text color. </dd>
<dt><code>CLine</code></dt>
<dd>Line color. </dd>
<dt><code>CLineL</code></dt>
<dd>Lighter version of line color. Set to &#8216;-&#8216; in order to use a calculated value based on CLine. </dd>
<dt><code>CRx</code></dt>
<dd>Color for received data. </dd>
<dt><code>CRxD</code></dt>
<dd>Darker version of received data color. Set to &#8216;-&#8216; in order to use a calculated value based on CRx. </dd>
<dt><code>CText</code></dt>
<dd>Common text color. </dd>
<dt><code>CTx</code></dt>
<dd>Color for transmitted data. </dd>
<dt><code>CTxD</code></dt>
<dd>Darker version of transmitted data color. Set to &#8216;-&#8216; in order to use a calculated value based on CTx. </dd>
<dt><code>HeaderFormat</code></dt>
<dd>Formatting of date in header. Uses the same format as <code><a href="/docs/linux/man/1-date/">date</a></code>(1). </dd>
<dt><code>HourlyRate</code></dt>
<dd>Show hours with rate instead of transfered amount. 1 = enabled, 0 = disabled. </dd>
<dt><code>SummaryLayout</code></dt>
<dd>Select the used layout of the summary output. 1 = layout introduced in version 1.8 with monthly traffic included, 0 = layout used before version 1.8, doesn&#8217;t contain monthly traffic and doesn&#8217;t support average rate. </dd>
<dt><code>SummaryRate</code></dt>
<dd>Show rate in summary output if available. 1 = enabled, 0 = disabled. </dd>
<dt><code>TransparentBg</code></dt>
<dd>Set background color as transparent. 1 = enabled, 0 = disabled. </dd>
</dl>
<h2>Files</h2>
<dl>
<dt><i>/etc/vnstat.conf</i></dt>
<dd>Config file that will be used unless <i>$HOME/.vnstatrc</i> exists or alternative value is given as command line parameter. </dd>
</dl>
<h2>Restrictions</h2>
<p>Using long date output formats may cause misalignment in shown columns if the length of the date exceeds the fixed size allocation.</p>
<h2>Author</h2>
<p>Teemu Toivola &lt;tst at iki dot fi&gt;</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-vnstat/">vnstat</a></code>(1), <code><a href="/docs/linux/man/1-vnstati/">vnstati</a></code>(1), <code><a href="/docs/linux/man/1-vnstatd/">vnstatd</a></code>(1), <code><a href="/docs/linux/man/7-units/">units</a></code>(7) </p>
