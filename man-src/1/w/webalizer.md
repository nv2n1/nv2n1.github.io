---
title: "webalizer(1)"
name: "webalizer"
section: "1"
letter: "w"
url: "/docs/linux/man/1-webalizer/"
description: "webalizer – A web server log file analysis tool."
---

<h2>NAME</h2>
<p> webalizer &#8211; A web server log file analysis tool.</p>
<h2>SYNOPSIS</h2>
<p> <code>webalizer</code> [<i> option &#8230; </i>] [<i> log-file </i>] </p>
<p> <code>webazolver</code> [<i> option &#8230; </i>] [<i> log-file </i>] </p>
<h2>DESCRIPTION</h2>
<p> The <i>Webalizer</i> is a web server log file analysis program which produces usage statistics in HTML format for viewing with a browser. The results are presented in both columnar and graphical format, which facilitates interpretation. Yearly, monthly, daily and hourly usage statistics are presented, along with the ability to display usage by site, URL, referrer, user agent (browser), username, search strings, entry/exit pages, and country (some information may not be available if not present in the log file being processed). </p>
<p> The <i>Webalizer</i> supports <code>CLF</code> (common log format) log files, as well as <code>Combined</code> log formats as defined by NCSA and others, and variations of these which it attempts to handle intelligently. In addition, the <i>Webalizer</i> supports <code>xferlog</code> formatted (<i>FTP</i>) log files, <code>squid</code> proxy logs and <code>W3C</code> extended format logs. Logs may also be compressed, via <i>gzip</i> (.gz) or, if enabled at compile time, <i>bzip2</i> (.bz2). If a compressed log file is detected, it will be automatically uncompressed while it is read. Compressed logs must have the standard <i>gzip</i> extension of <code>.gz</code> or <i>bzip2</i> extension of <code>.bz2</code>. </p>
<p> <i>webazolver</i> is normally just a symbolic link to the <i>Webalizer</i>. When run as <i>webazolver</i>, only DNS file creation/updates are performed, and the program will exit once complete. All normal options and configuration directives are available, however many will not be used. In addition, a DNS cache file must be specified. If the number of DNS children processes to use are not specified, the <i>webazolver</i> will default to <code>5</code>. </p>
<p> This documentation applies to The Webalizer Version 2.23</p>
<h2>RUNNING THE WEBALIZER</h2>
<p> The <i>Webalizer</i> was designed to be run from a Unix command line prompt or as a <code><a href="/docs/linux/man/8-crond/">crond</a>(8)</code> job. Once executed, the general flow of the program is:</p>
<dl>
<dt><code>o</code></p>
<dd> A default configuration file is scanned for. A file named <i>webalizer.conf</i> is searched for in the current directory, and if found, and is owned by the invoking user, then its configuration data is parsed. If the file is not present in the current directory, the file <i>/etc/webalizer.conf</i> is searched for and, if found, is used instead.</p>
<dt><code>o</code></p>
<dd> Any command line arguments given to the program are parsed. This may include the specification of a configuration file, which is processed at the time it is encountered.</p>
<dt><code>o</code></p>
<dd> If a log file was specified, it is opened and made ready for processing. If no log file was given, <i>STDIN</i> is used for input. If the log filename &#8216;<code>&#8211;</code>&#8216; is specified, <i>STDIN</i> will be forced.</p>
<dt><code>o</code></p>
<dd> If an output directory was specified, the program does a <code><a href="/docs/linux/man/2-chdir/">chdir</a>(2)</code> to that directory in preparation for generating output. If no output directory was given, the current directory is used.</p>
<dt><code>o</code></p>
<dd> If a non-zero number of DNS Children processes were specified, they will be started, and the specified log file will be processed, creating or updating the specified DNS cache file.</p>
<dt><code>o</code></p>
<dd> If no hostname was given, the program attempts to get the hostname using a <code><a href="/docs/linux/man/2-uname/">uname</a>(2)</code> system call. If that fails, <i>localhost</i> is used.</p>
<dt><code>o</code></p>
<dd> A history file is searched for in the current directory (output directory) and read if found. This file keeps totals for previous months, which is used in the main <i>index.html</i> HTML document. <code>Note:</code> The file location can now be specified with the <i>HistoryName</i> configuration option.</p>
<dt><code>o</code></p>
<dd> If incremental processing was specified, a data file is searched for and loaded if found, containing the &#8216;internal state&#8217; data of the program at the end of a previous run. <code>Note:</code> The file location can now be specified with the <i>IncrementalName</i> configuration option.</p>
<dt><code>o</code></p>
<dd> Main processing begins on the log file. If the log spans multiple months, a separate HTML document is created for each month.</p>
<dt><code>o</code></p>
<dd> After main processing, the main <i>index.html</i> page is created, which has totals by month and links to each months HTML document.</p>
<dt><code>o</code></p>
<dd> A new history file is saved to disk, which includes totals generated by The <i>Webalizer</i> during the current run.</p>
<dt><code>o</code></p>
<dd> If incremental processing was specified, a data file is written that contains the &#8216;internal state&#8217; data at the end of this run.</dl>
<h2>INCREMENTAL PROCESSING</h2>
<p> The <i>Webalizer</i> supports incremental run capability. Simply put, this allows processing large log files by breaking them up into smaller pieces, and processing these pieces instead. What this means in real terms is that you can now rotate your log files as often as you want, and still be able to produce monthly usage statistics without the loss of any detail. Basically, The <i>Webalizer</i> saves and restores all internal data in a file named <i>webalizer.current</i>. This allows the program to &#8216;start where it left off&#8217; so to speak, and allows the preservation of detail from one run to the next. The data file is placed in the current output directory, and is a plain ASCII text file that can be viewed with any standard text editor. It&#8217;s location and name may be changed using the <i>IncrementalName</i> configuration keyword. </p>
<p> Some special precautions need to be taken when using the incremental run capability of The <i>Webalizer</i>. Configuration options should not be changed between runs, as that could cause corruption of the internal data stored. For example, changing the <i>MangleAgents</i> level will cause different representations of user agents to be stored, producing invalid results in the user agents section of the report. If you need to change configuration options, do it at the end of the month after normal processing of the previous month and before processing the current month. You may also want to delete the <i>webalizer.current</i> file as well. </p>
<p> The <i>Webalizer</i> also attempts to prevent data duplication by keeping track of the timestamp of the last record processed. This timestamp is then compared to current records being processed, and any records that were logged previous to that timestamp are ignored. This, in theory, should allow you to re-process logs that have already been processed, or process logs that contain a mix of processed/not yet processed records, and not produce duplication of statistics. The only time this may break is if you have duplicate timestamps in two separate log files&#8230; any records in the second log file that do have the same timestamp as the last record in the previous log file processed, will be discarded as if they had already been processed. There are lots of ways to prevent this however, for example, stopping the web server before rotating logs will prevent this situation. This setup also necessitates that you always process logs in chronological order, otherwise data loss will occur as a result of the timestamp compare.</p>
<h2>REVERSE DNS LOOKUPS</h2>
<p> The <i>Webalizer</i> fully supports IPv4 and IPv6 DNS lookups, and maintains a cache of those lookups to reduce processing the same addresses in subsequent runs. The cache file can be created at run-time, or may be created before running the webalizer using either the stand alone &#8216;<i>webazolver</i>&#8216; program, or The Webalizer (DNS) Cache file manager program &#8216;<i>wcmgr</i>&#8216;. In order to perform reverse lookups, a <code>DNSCache</code> file must be specified, either on the command line or in a configuration file. In order to create/update the cache file at run-time, the number of <code>DNSChildren</code> must also be specified, and can be anything between 1 and 100. This specifies the number of child processes to be forked, each of which will perform network DNS queries in order to lookup up the addresses and update the cache. Cached entries that are older than a specified TTL (time to live) will be expired, and if encountered again in a log, will be looked up at that time in order to &#8216;freshen&#8217; them (verify the name is still the same and update its timestamp). The default TTL is 7 days, however may be set to anything between 1 and 100 days. Using the &#8216;<i>wcmgr</i>&#8216; program, entries may also be marked as &#8216;permanent&#8217;, in which case they will persist (with an infinite TTL) in the cache until manually removed. See the file <code>DNS.README</code> for additional information and examples.</p>
<h2>GEOLOCATION LOOKUPS</h2>
<p> The <i>Webalizer</i> has the ability to perform geolocation lookups on IP addresses using either it&#8217;s own internal <i>GeoDB</i> database, or optionally the <i>GeoIP</i> database from MaxMind, Inc. (<a rel="nofollow" href="http://www.maxmind.com">www.maxmind.com</a>). If used, unresolved addresses will be searched for in the database and its country of origin will be returned if found. This actually produces more accurate <i>Country</i> information than DNS lookups, since the DNS address space has additional <i>gcTLDs</i> that do not necessarily map to a specific country (such as <i>.net</i> and <i>.com</i>). It is possible to use both DNS lookups and geolocation lookups at the same time, which will cause any addresses that could not be resolved using DNS lookups to then be looked up in the database, greatly reducing the number of <i>Unknown/Unresolved</i> entries in the generated reports. The native <i>GeoDB</i> geolocation database provided by The <i>Webalizer</i> fully supports both <i>IPv4</i> and <i>IPv6</i> lookups, is updated regularly and is the preferred geolocation method for use with The <i>Webalizer</i>. The most current version of the database can be obtained from our ftp site (<i><a href="ftp://ftp.mrunix.net/">ftp://ftp.mrunix.net/</a></i>).</p>
<h2>COMMAND LINE OPTIONS</h2>
<p> The <i>Webalizer</i> supports many different configuration options that will alter the way the program behaves and generates output. Most of these can be specified on the command line, while some can only be specified in a configuration file. The command line options are listed below, with references to the corresponding configuration file keywords. </p>
<p> <i>General Options</i></p>
<dl>
<dt><code>-h</code></p>
<dd> Display all available command line options and exit program.</p>
<dt><code>-v</code></p>
<dd> Be verbose. Will cause the program to output informational and <i>Debug</i> messages at run-time.</p>
<dt><code>-V</code></p>
<dd> Display the program version and exit. Additional program specific information will be displayed if <i>verbose</i> mode is also used (e.g. &#8216;<i>-vV</i>&#8216;), which can be useful when submitting bug reports.</p>
<dt><code>-d</code></p>
<dd> <code>Debug</code>. Display debugging information for errors and warnings.</p>
<dt><code>-i</code></p>
<dd> <code>IgnoreHist</code>. Ignore history. <code>USE WITH CAUTION</code>. This will cause The <i>Webalizer</i> to ignore any previous monthly history file only. Incremental data (if present) is still processed.</p>
<dt><code>-b</code></p>
<dd> <code>IgnoreState</code>. Ignore incremental data file. <code>USE WITH CAUTION</code>. This will cause The <i>Webalizer</i> to ignore any existing incremental data file. By ignoring the incremental data file, all previous processing for the current month will be lost and those logs must be re-processed.</p>
<dt><code>-p</code></p>
<dd> <code>Incremental</code>. Preserve internal data between runs.</p>
<dt><code>-q</code></p>
<dd> <code>Quiet</code>. Suppress informational messages. Does not suppress warnings or errors.</p>
<dt><code>-Q</code></p>
<dd> <code>ReallyQuiet</code>. Suppress all messages including warnings and errors.</p>
<dt><code>-T</code></p>
<dd> <code>TimeMe</code>. Force display of timing information at end of processing.</p>
<dt><code>-c </code><i>file</i></p>
<dd> Use configuration file <i>file</i>.</p>
<dt><code>-n </code><i>name</i></p>
<dd> <code>HostName</code>. Use the hostname <i>name</i>.</p>
<dt><code>-o </code><i>dir</i></p>
<dd> <code>OutputDir</code>. Use output directory <i>dir</i>.</p>
<dt><code>-t </code><i>name</i></p>
<dd> <code>ReportTitle</code>. Use <i>name</i> for report title.</p>
<dt><code>-F </code>( <code>c</code>lf | <code>f</code>tp | <code>s</code>quid | <code>w</code>3c )</p>
<dd> <code>LogType</code>. Specify log type to be processed. Value can be either <i>c</i>lf, <i>f</i>tp, <i>s</i>quid or <i>w</i>3c format. If not specified, will default to <code>CLF</code> format. <i>FTP</i> logs must be in standard wu-ftpd <i>xferlog</i> format.</p>
<dt><code>-f</code></p>
<dd> <code>FoldSeqErr</code>. Fold out of sequence log records back into analysis, by treating as if they were the same date/time as the last good record. Normally, out of sequence log records are simply ignored.</p>
<dt><code>-Y</code></p>
<dd> <code>CountryGraph</code>. Suppress country graph.</p>
<dt><code>-G</code></p>
<dd> <code>HourlyGraph</code>. Suppress hourly graph.</p>
<dt><code>-x </code><i>name</i></p>
<dd> <code>HTMLExtension</code>. Defines HTML file extension to use. If not specified, defaults to <i>html</i>. Do not include the leading period.</p>
<dt><code>-H</code></p>
<dd> <code>HourlyStats</code>. Suppress hourly statistics.</p>
<dt><code>-K </code><i>num</i></p>
<dd> <code>IndexMonths</code>. Specify how many months should be displayed in the main index (yearly summary) table. Default is 12 months. Can be set to anything between 12 and 120 months (1 to 10 years).</p>
<dt><code>-k </code><i>num</i></p>
<dd> <code>GraphMonths</code>. Specify how many months should be displayed in the main index (yearly summary) graph. Default is 12 months. Can be set to anything between 12 and 72 months (1 to 6 years).</p>
<dt><code>-L</code></p>
<dd> <code>GraphLegend</code>. Suppress color coded graph legends.</p>
<dt><code>-l </code><i>num</i></p>
<dd> <code>GraphLines</code>. Specify number of background lines. Default is 2. Use zero (&#8216;0&#8217;) to disable the lines.</p>
<dt><code>-P </code><i>name</i></p>
<dd> <code>PageType</code>. Specify file extensions that are considered <i>pages</i>. Sometimes referred to as <i>pageviews</i>.</p>
<dt><code>-O </code><i>name</i></p>
<dd> <code>OmitPage</code>. Specify URLs to exclude from being counted as <i>pages</i>.</p>
<dt><code>-m </code><i>num</i></p>
<dd> <code>VisitTimeout</code>. Specify the Visit timeout period. Specified in number of seconds. Default is 1800 seconds (30 minutes).</p>
<dt><code>-I </code><i>name</i></p>
<dd> <code>IndexAlias</code>. Use the filename <i>name</i> as an additional alias for <i>index.</i>.</p>
<dt><code>-M </code><i>num</i></p>
<dd> <code>MangleAgents</code>. Mangle user agent names according to the mangle level specified by <i>num</i>. Mangle levels are:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>5</code></p>
<dd> Browser name and major version.</p>
<dt><code>4</code></p>
<dd> Browser name, major and minor version.</p>
<dt><code>3</code></p>
<dd> Browser name, major version, minor version to two decimal places.</p>
<dt><code>2</code></p>
<dd> Browser name, major and minor versions and sub-version.</p>
<dt><code>1</code></p>
<dd> Browser name, version and machine type if possible.</p>
<dt><code>0</code></p>
<dd> All information (left unchanged).</dl>
</dl>
<dt><code>-g </code><i>num</i></p>
<dd> <code>GroupDomains</code>. Automatically group sites by domain. The grouping level specified by <i>num</i> can be thought of as &#8216;the number of dots&#8217; to display in the grouping. The default value of <code>0</code> disables any domain grouping.</p>
<dt><code>-D </code><i>name</i></p>
<dd> <code>DNSCache</code>. Use the DNS cache file <i>name</i>.</p>
<dt><code>-N </code><i>num</i></p>
<dd> <code>DNSChildren</code>. Use <i>num</i> DNS children processes to perform DNS lookups, either creating or updating the DNS cache file. Specify zero (<code>0</code>) to disable cache file creation/updates. If given, a DNS cache filename must be specified.</p>
<dt><code>-j</code></p>
<dd> Enable <i>GeoDB</i>. This enables the internal GeoDB geolocation services provided by The <i>Webalizer</i>.</p>
<dt><code>-J </code><i>name</i></p>
<dd> <code>GeoDBDatabase</code>. Use the alternate GeoDB database <i>name</i>.</p>
<dt><code>-w</code></p>
<dd> Enable <i>GeoIP</i>. Enables GeoIP (by MaxMind Inc.) geolocation services. If native <i>GeoDB</i> services are also enabled, then this option will have no effect.</p>
<dt><code>-W </code><i>name</i></p>
<dd> <code>GeoIPDatabase</code>. Use the alternate GeoIP database <i>name</i>.</p>
<dt><code>-z </code><i>name</i></p>
<dd> <code>FlagDir</code>. Specify location of the country flag graphics and enable their display in the top country table. The directory <i>name</i> is relative to the output directory being used unless an absolute path is given (ie: starts with a leading &#8216;/&#8217;).</dl>
<p> <i>Hide Options</i></p>
<dl>
<dt><code>-a </code><i>name</i></p>
<dd> <code>HideAgent</code>. Hide user agents matching <i>name</i>.</p>
<dt><code>-r </code><i>name</i></p>
<dd> <code>HideReferrer</code>. Hide referrer matching <i>name</i>.</p>
<dt><code>-s </code><i>name</i></p>
<dd> <code>HideSite</code>. Hide site matching <i>name</i>.</p>
<dt><code>-X</code></p>
<dd> <code>HideAllSites</code>. Hide all individual sites (only display groups).</p>
<dt><code>-u </code><i>name</i></p>
<dd> <code>HideURL</code>. Hide URL matching <i>name</i>.</dl>
<p> <i>Table size options</i></p>
<dl>
<dt><code>-A </code><i>num</i></p>
<dd> <code>TopAgents</code>. Display the top <i>num</i> user agents table.</p>
<dt><code>-R </code><i>num</i></p>
<dd> <code>TopReferrers</code>. Display the top <i>num</i> referrers table.</p>
<dt><code>-S </code><i>num</i></p>
<dd> <code>TopSites</code>. Display the top <i>num</i> sites table.</p>
<dt><code>-U </code><i>num</i></p>
<dd> <code>TopURLs</code>. Display the top <i>num</i> URLs table.</p>
<dt><code>-C </code><i>num</i></p>
<dd> <code>TopCountries</code>. Display the top <i>num</i> countries table.</p>
<dt><code>-e </code><i>num</i></p>
<dd> <code>TopEntry</code>. Display the top <i>num</i> entry pages table.</p>
<dt><code>-E </code><i>num</i></p>
<dd> <code>TopExit</code>. Display the top <i>num</i> exit pages table.</dl>
<h2>CONFIGURATION FILES</h2>
<p> Configuration files are standard <code><a href="/docs/linux/man/7-ascii/">ASCII</a>(7)</code> text files that may be created or edited using any standard editor. Blank lines and lines that begin with a pound sign (&#8216;#&#8217;) are ignored. Any other lines are considered to be configuration lines, and have the form &quot;Keyword Value&quot;, where the &#8216;Keyword&#8217; is one of the currently available configuration keywords defined below, and &#8216;Value&#8217; is the value to assign to that particular option. Any text found after the keyword up to the end of the line is considered the keyword&#8217;s value, so you should not include anything after the actual value on the line that is not actually part of the value being assigned. The file <i>sample.conf</i> provided with the distribution contains lots of useful documentation and examples as well. </p>
<p> <i>General Configuration Keywords</i></p>
<dl>
<dt><code>LogFile </code><i>name</i></p>
<dd> Use log file named <i>name</i>. If none specified, <i>STDIN</i> will be used.</p>
<dt><code>LogType </code><i>name</i></p>
<dd> Specify log file type as <i>name</i>. Values can be either <i>clf</i>, <i>squid</i>, <i>ftp</i> or <i>w3c</i>, with the default being <code>clf</code>.</p>
<dt><code>OutputDir </code><i>dir</i></p>
<dd> Create output in the directory <i>dir</i>. If none specified, the current directory will be used.</p>
<dt><code>HistoryName </code><i>name</i></p>
<dd> Filename to use for history file. Relative to output directory unless absolute name is given (ie: starts with &#8216;/&#8217;). Defaults to &#8216;<code>webalizer.hist</code>&#8216; in the standard output directory.</p>
<dt><code>ReportTitle </code><i>name</i></p>
<dd> Use the title string <i>name</i> for the report title. If none specified, use the default of (in english) &quot;<i>Usage Statistics for </i>&quot;.</p>
<dt><code>HostName </code><i>name</i></p>
<dd> Set the hostname for the report as <i>name</i>. If none specified, an attempt will be made to gather the hostname via a <code><a href="/docs/linux/man/2-uname/">uname</a>(2)</code> system call. If that fails, <i>localhost</i> will be used.</p>
<dt><code>UseHTTPS </code>( yes | <code>no</code> )</p>
<dd> Use <i>https://</i> on links to URLS, instead of the default <i>http://</i>, in the &#8216;<code>Top URLs</code>&#8216; table.</p>
<dt><code>HTAccess </code>( yes | <code>no</code> )</p>
<dd> Enables the creation of a default .htaccess file in the output directory.</p>
<dt><code>Quiet </code>( yes | <code>no</code> )</p>
<dd> Suppress informational messages. Warning and Error messages will not be suppressed.</p>
<dt><code>ReallyQuiet </code>( yes | <code>no</code> )</p>
<dd> Suppress all messages, including Warning and Error messages.</p>
<dt><code>Debug </code>( yes | <code>no</code> )</p>
<dd> Print extra debugging information on Warnings and Errors.</p>
<dt><code>TimeMe </code>( yes | <code>no</code> )</p>
<dd> Force timing information at end of processing.</p>
<dt><code>GMTTime </code>( yes | <code>no</code> )</p>
<dd> Use <i>GMT </i>(<i>UTC</i>) time instead of local timezone for reports.</p>
<dt><code>IgnoreHist </code>( yes | <code>no</code> )</p>
<dd> Ignore previous monthly history file. <code>USE WITH CAUTION</code>. Does not prevent <i>Incremental</i> file processing.</p>
<dt><code>IgnoreState </code>( yes | <code>no</code> )</p>
<dd> Ignore incremental data file. <code>USE WITH CAUTION</code>. By ignoring the incremental data file, all previous processing for the current month will be lost and those logs must be re-processed.</p>
<dt><code>FoldSeqErr </code>( yes | <code>no</code> )</p>
<dd> Fold out of sequence log records back into analysis by treating them as if they had the same date/time as the last good record. Normally, out of sequence log records are ignored.</p>
<dt><code>CountryGraph </code>( <code>yes</code> | no )</p>
<dd> Display Country Usage Graph in output report.</p>
<dt><code>CountryFlags </code>( yes | <code>no</code> )</p>
<dd> Enable or disable the display of flags in the top country table.</p>
<dt><code>FlagDir </code><i>name</i></p>
<dd> Specifies the directory <i>name</i> where the flag graphics are located. If not specified, the default is in the <i>flags</i> directory directly under the output directory being used. If specified, the display of country flags will be enabled by default. Using &#8216;<i>FlagDir flags</i>&#8216; is identical to using &#8216;<i>CountryFlags yes</i>&#8216;.</p>
<dt><code>DailyGraph </code>( <code>yes</code> | no )</p>
<dd> Display Daily Graph in output report.</p>
<dt><code>DailyStats </code>( <code>yes</code> | no )</p>
<dd> Display Daily Statistics in output report.</p>
<dt><code>HourlyGraph </code>( <code>yes</code> | no )</p>
<dd> Display Hourly Graph in output report.</p>
<dt><code>HourlyStats </code>( <code>yes</code> | no )</p>
<dd> Display Hourly Statistics in output report.</p>
<dt><code>PageType </code><i>name</i></p>
<dd> Define the file extensions to consider as a <i>page</i>. If a file is found to have the same extension as <i>name</i>, it will be counted as a <i>page</i> (sometimes called a <i>pageview</i>).</p>
<dt><code>PagePrefix </code><i>name</i></p>
<dd> Allows URLs with the prefix <i>name</i> to be counted as a <i>page</i> type regardless of actual file type. This allows you to treat contents under specified directories as pages no matter what their extension is.</p>
<dt><code>OmitPage </code><i>name</i></p>
<dd> Specifies URLs which should not be counted as pages, regardless of their extension (or lack thereof).</p>
<dt><code>GraphLegend </code>( <code>yes</code> | no )</p>
<dd> Allows the color coded graph legends to be enabled/disabled.</p>
<dt><code>GraphLines </code><i>num</i></p>
<dd> Specify the number of background reference lines displayed on the graphs produced. Disable by using zero (&#8216;<code>0</code>&#8216;), default is <code>2</code>.</p>
<dt><code>IndexMonths </code><i>num</i></p>
<dd> Specify the number of months to display in the main index (yearly summary) table. Default is 12 months. Can be set to anything between 12 and 120 months (1 to 10 years).</p>
<dt><code>YearHeaders </code>( <code>yes</code> | no )</p>
<dd> Enable/disable the display of year headers in the main index (yearly summary) table. If enabled, year headers will be shown when the table is displaying more than 16 months worth of data. Values can be &#8216;yes&#8217; or &#8216;no&#8217;. Default is &#8216;yes&#8217;.</p>
<dt><code>YearTotals </code>( <code>yes</code> | no )</p>
<dd> Enable/disable the display of year totals in the main index (yearly summary) table. If enabled, year totals will be shown when the table is displaying more than 16 months worth of data. Values can be &#8216;yes&#8217; or &#8216;no&#8217;. Default is &#8216;yes&#8217;.</p>
<dt><code>GraphMonths </code><i>num</i></p>
<dd> Specify the number of months to display in the main index (yearly summary) graph. Default is 12 months. Can be set to anything between 12 and 72 months (1 to 6 years).</p>
<dt><code>VisitTimeout </code><i>num</i></p>
<dd> Specifies the visit timeout value. Default is <i>1800 seconds</i> (30 minutes). A visit is determined by looking at the difference in time between the current and last request from a specific site. If the difference is greater or equal to the timeout value, the request is counted as a new visit. Specified in seconds.</p>
<dt><code>IndexAlias </code><i>name</i></p>
<dd> Use <i>name</i> as an additional alias for <i>index.*</i>.</p>
<dt><code>DefaultIndex </code>( <code>yes</code> | no )</p>
<dd> Enables or disables the use of &#8216;<code>index.</code>&#8216; as a default index name to be stripped from the end of URLs. This does not effect any index names that may be defined with the <i>IndexAlias</i> option.</p>
<dt><code>MangleAgents </code><i>num</i></p>
<dd> Mangle user agent names based on mangle level <i>num</i>. See the <i>-M</i> command line switch for mangle levels and their meaning. The default is <code>0</code>, which doesn&#8217;t mangle user agents at all.</p>
<dt><code>StripCGI </code>( <code>yes</code> | no )</p>
<dd> Determines if URL CGI variables should be stripped from the end of URLs. Values may be &#8216;yes&#8217; or &#8216;no&#8217;, with the default being &#8216;yes&#8217;.</p>
<dt><code>TrimSquidURL </code><i>num</i></p>
<dd> Allows squid log URLs to be reduced in granularity by truncating them after <i>num</i> slashes (&#8216;/&#8217;) after the http:// prefix. A setting of one (1) will cause all URLs to be summarized by domain only. The default value is zero (0), which will disable any URL modifications and leave them exactly as found in the log file.</p>
<dt><code>SearchEngine</code> <i>name</i> <i>variable</i></p>
<dd> Allows the specification of search engines and their query strings. The <i>name</i> is the name to match against the referrer string for a given search engine. The <i>variable</i> is the cgi variable that the search engine uses for queries. See the <code>sample.conf</code> file for example usage with common search engines.</p>
<dt><code>SearchCaseI</code> ( <code>yes</code> | no )</p>
<dd> Determines if search strings should be treated case insensitive or not. The default is &#8216;yes&#8217;, which lowercases all search strings (treat as case insensitive).</p>
<dt><code>Incremental </code>( yes | <code>no</code> )</p>
<dd> Enable Incremental mode processing.</p>
<dt><code>IncrementalName </code><i>name</i></p>
<dd> Filename to use for incremental data. Relative to output directory unless an absolute name is given (ie: starts with &#8216;/&#8217;). Defaults to &#8216;<code>webalizer.current</code>&#8216; in the standard output directory.</p>
<dt><code>DNSCache </code><i>name</i></p>
<dd> Filename to use for the DNS cache. Relative to output directory unless an absolute name is given (ie: starts with &#8216;/&#8217;).</p>
<dt><code>DNSChildren </code><i>num</i></p>
<dd> Number of children DNS processes to run in order to create/update the DNS cache file. Specify zero (<code>0</code>) to disable.</p>
<dt><code>CacheIPs </code>( yes | <code>no</code> )</p>
<dd> Cache unresolved IP addresses in the DNS database. Default is &#8216;<code>no</code>&#8216;.</p>
<dt><code>CacheTTL </code><i>num</i></p>
<dd> DNS cache entry time to live (TTL) in days. Default is 7 days. May be any value between 1 and 100.</p>
<dt><code>GeoDB </code>( yes | <code>no</code> )</p>
<dd> Allows native GeoDB geolocation services to be enabled or disabled. Default value is &#8216;<code>no</code>&#8216;.</p>
<dt><code>GeoDBDatabase </code><i>name</i></p>
<dd> Allows the use of an alternate GeoDB database <i>name</i>. If not specified, the default database will be used.</p>
<dt><code>GeoIP </code>( yes | <code>no</code> )</p>
<dd> Allows GeoIP (by MaxMind Inc.) geolocation services to be enabled or disabled. Default is &#8216;<code>no</code>&#8216;. If native <i>GeoDB</i> geolocation services are also enabled, then this option will have no effect (and the native <i>GeoDB</i> services will be used).</p>
<dt><code>GeoIPDatabase </code><i>name</i></p>
<dd> Allows the use of an alternate GeoIP database <i>name</i>. If not specified, the default database will be used.</dl>
<p> <i>Top Table Keywords</i></p>
<dl>
<dt><code>TopAgents </code><i>num</i></p>
<dd> Display the top <i>num</i> User Agents table. Use zero to disable.</p>
<dt><code>AllAgents </code>( yes | <code>no</code> )</p>
<dd> Create separate HTML page with <code>All</code> User Agents.</p>
<dt><code>TopReferrers </code><i>num</i></p>
<dd> Display the top <i>num</i> Referrers table. Use zero to disable.</p>
<dt><code>AllReferrers </code>( yes | <code>no</code> )</p>
<dd> Create separate HTML page with <code>All</code> Referrers.</p>
<dt><code>TopSites </code><i>num</i></p>
<dd> Display the top <i>num</i> Sites table. Use zero to disable.</p>
<dt><code>TopKSites </code><i>num</i></p>
<dd> Display the top <i>num</i> Sites (by KByte) table. Use zero to disable.</p>
<dt><code>AllSites </code>( yes | <code>no</code> )</p>
<dd> Create separate HTML page with <code>All</code> Sites.</p>
<dt><code>TopURLs </code><i>num</i></p>
<dd> Display the top <i>num</i> URLs table. Use zero to disable.</p>
<dt><code>TopKURLs </code><i>num</i></p>
<dd> Display the top <i>num</i> URLs (by KByte) table. Use zero to disable.</p>
<dt><code>AllURLs </code>( yes | <code>no</code> )</p>
<dd> Create separate HTML page with <code>All</code> URLs.</p>
<dt><code>TopCountries </code><i>num</i></p>
<dd> Display the top <i>num</i> Countries in the table. Use zero to disable.</p>
<dt><code>TopEntry </code><i>num</i></p>
<dd> Display the top <i>num</i> Entry Pages in the table. Use zero to disable.</p>
<dt><code>TopExit </code><i>num</i></p>
<dd> Display the top <i>num</i> Exit Pages in the table. Use zero to disable.</p>
<dt><code>TopSearch </code><i>num</i></p>
<dd> Display the top <i>num</i> Search Strings in the table. Use zero to disable.</p>
<dt><code>AllSearchStr </code>( yes | <code>no</code> )</p>
<dd> Create separate HTML page with <code>All</code> Search Strings.</p>
<dt><code>TopUsers </code><i>num</i></p>
<dd> Display the top <i>num</i> Usernames in the table. Use zero to disable. Usernames are only available if using http based authentication.</p>
<dt><code>AllUsers </code>( yes | <code>no</code> )</p>
<dd> Create separate HTML page with <code>All</code> Usernames.</dl>
<p> <i>Hide/Ignore/Group/Include Keywords</i></p>
<dl>
<dt><code>HideAgent </code><i>name</i></p>
<dd> Hide User Agents that match <i>name</i>.</p>
<dt><code>HideReferrer </code><i>name</i></p>
<dd> Hide Referrers that match <i>name</i>.</p>
<dt><code>HideSite </code><i>name</i></p>
<dd> Hide Sites that match <i>name</i>.</p>
<dt><code>HideAllSites </code>( yes | <code>no</code> )</p>
<dd> Hide all individual sites. This causes only grouped sites to be displayed.</p>
<dt><code>HideURL </code><i>name</i></p>
<dd> Hide URLs that match <i>name</i>.</p>
<dt><code>HideUser </code><i>name</i></p>
<dd> Hide Usernames that match <i>name</i>.</p>
<dt><code>IgnoreAgent </code><i>name</i></p>
<dd> Ignore User Agents that match <i>name</i>.</p>
<dt><code>IgnoreReferrer </code><i>name</i></p>
<dd> Ignore Referrers that match <i>name</i>.</p>
<dt><code>IgnoreSite </code><i>name</i></p>
<dd> Ignore Sites that match <i>name</i>.</p>
<dt><code>IgnoreURL </code><i>name</i></p>
<dd> Ignore URLs that match <i>name</i>.</p>
<dt><code>IgnoreUser </code><i>name</i></p>
<dd> Ignore Usernames that match <i>name</i>.</p>
<dt><code>GroupAgent </code><i>name</i> [<i>Label</i>]</p>
<dd> Group User Agents that match <i>name</i>. Display <i>Label</i> in &#8216;Top Agent&#8217; table if given (instead of <i>name</i>). <i>name</i> may be enclosed in quotes.</p>
<dt><code>GroupReferrer </code><i>name</i> [<i>Label</i>]</p>
<dd> Group Referrers that match <i>name</i>. Display <i>Label</i> in &#8216;Top Referrer&#8217; table if given (instead of <i>name</i>). <i>name</i> may be enclosed in quotes.</p>
<dt><code>GroupSite </code><i>name</i> [<i>Label</i>]</p>
<dd> Group Sites that match <i>name</i>. Display <i>Label</i> in &#8216;Top Site&#8217; table if given (instead of <i>name</i>). <i>name</i> may be enclosed in quotes.</p>
<dt><code>GroupDomains </code><i>num</i></p>
<dd> Automatically group sites by domain. The value <i>num</i> specifies the level of grouping, and can be thought of as the &#8216;number of dots&#8217; to be displayed. The default value of <code>0</code> disables domain grouping.</p>
<dt><code>GroupURL </code><i>name</i> [<i>Label</i>]</p>
<dd> Group URLs that match <i>name</i>. Display <i>Label</i> in &#8216;Top URL&#8217; table if given (instead of <i>name</i>). <i>name</i> may be enclosed in quotes.</p>
<dt><code>GroupUser </code><i>name</i> [<i>Label</i>]</p>
<dd> Group Usernames that match <i>name</i>. Display <i>Label</i> in &#8216;Top Usernames&#8217; table if given (instead of <i>name</i>). <i>name</i> may be enclosed in quotes.</p>
<dt><code>IncludeSite </code><i>name</i></p>
<dd> Force inclusion of sites that match <i>name</i>. Takes precedence over <code>Ignore*</code> keywords.</p>
<dt><code>IncludeURL </code><i>name</i></p>
<dd> Force inclusion of URLs that match <i>name</i>. Takes precedence over <code>Ignore*</code> keywords.</p>
<dt><code>IncludeReferrer </code><i>name</i></p>
<dd> Force inclusion of Referrers that match <i>name</i>. Takes precedence over <code>Ignore*</code> keywords.</p>
<dt><code>IncludeAgent </code><i>name</i></p>
<dd> Force inclusion of User Agents that match <i>name</i>. Takes precedence over <code>Ignore*</code> keywords.</p>
<dt><code>IncludeUser </code><i>name</i></p>
<dd> Force inclusion of Usernames that match <i>name</i>. Takes precedence over <code>Ignore*</code> keywords.</dl>
<p> <i>HTML Generation Keywords</i></p>
<dl>
<dt><code>HTMLExtension </code><i>text</i></p>
<dd> Defines the HTML file extension to use. Default is <i>html</i>. Do not include the leading period!</p>
<dt><code>HTMLPre </code><i>text</i></p>
<dd> Insert <i>text</i> at the very beginning of the generated HTML file. Defaults to a standard html 3.2 <i>DOCTYPE</i> record.</p>
<dt><code>HTMLHead </code><i>text</i></p>
<dd> Insert <i>text</i> within the &lt;HEAD&gt;&lt;/HEAD&gt; block of the HTML file.</p>
<dt><code>HTMLBody </code><i>text</i></p>
<dd> Insert <i>text</i> in HTML page, starting with the &lt;BODY&gt; tag. If used, the first line must be a <i>&lt;BODY &#8230;&gt;</i> tag. Multiple lines may be specified.</p>
<dt><code>HTMLPost </code><i>text</i></p>
<dd> Insert <i>text</i> at top (before horiz. rule) of HTML pages. Multiple lines may be specified.</p>
<dt><code>HTMLTail </code><i>text</i></p>
<dd> Insert <i>text</i> at bottom of the HTML page. The <i>text</i> is top and right aligned within a table column at the end of the report.</p>
<dt><code>HTMLEnd </code><i>text</i></p>
<dd> Insert <i>text</i> at the very end of the HTML page. If not specified, the default is to insert the ending &lt;/BODY&gt; and &lt;/HTML&gt; tags. If used, you <i>must</i> supply these tags yourself.</p>
<dt><code>LinkReferrer </code>( yes | <code>no</code> )</p>
<dd> Determines if the referrers listed in the top referrers table should be displayed as plain text, or as a link to the referrer URL.</p>
<dt><code>ColorHit </code>( rrggbb | <code>00805c</code> )</p>
<dd> Sets the graph&#8217;s hit-color to the specified html color (no &#8216;#&#8217;).</p>
<dt><code>ColorFile </code>( rrggbb | <code>0040ff</code> )</p>
<dd> Sets the graph&#8217;s file-color to the specified html color (no &#8216;#&#8217;).</p>
<dt><code>ColorSite </code>( rrggbb | <code>ff8000</code> )</p>
<dd> Sets the graph&#8217;s site-color to the specified html color (no &#8216;#&#8217;).</p>
<dt><code>ColorKbyte </code>( rrggbb | <code>ff0000</code> )</p>
<dd> Sets the graph&#8217;s kilobyte-color to the specified html color (no &#8216;#&#8217;).</p>
<dt><code>ColorPage </code>( rrggbb | <code>00e0ff</code> )</p>
<dd> Sets the graph&#8217;s page-color to the specified html color (no &#8216;#&#8217;).</p>
<dt><code>ColorVisit </code>( rrggbb | <code>ffff00</code> )</p>
<dd> Sets the graph&#8217;s visit-color to the specified html color (no &#8216;#&#8217;).</p>
<dt><code>ColorMisc </code>( rrggbb | <code>00e0ff</code> )</p>
<dd> Sets the &#8216;miscellaneous&#8217; color for table headers (not graphs) to the specified html color (no &#8216;#&#8217;).</p>
<dt><code>PieColor1 </code>( rrggbb | <code>800080</code> )</p>
<dd> Sets the pie&#8217;s first optional color to the specified html color (no &#8216;#&#8217;).</p>
<dt><code>PieColor2 </code>( rrggbb | <code>80ffc0</code> )</p>
<dd> Sets the pie&#8217;s second optional color to the specified html color (no &#8216;#&#8217;).</p>
<dt><code>PieColor3 </code>( rrggbb | <code>ff00ff</code> )</p>
<dd> Sets the pie&#8217;s third optional color to the specified html color (no &#8216;#&#8217;).</p>
<dt><code>PieColor4 </code>( rrggbb | <code>ffc480</code> )</p>
<dd> Sets the pie&#8217;s fourth optional color to the specified html color (no &#8216;#&#8217;).</dl>
<p> <i>Dump Object Keywords</i> </p>
<p> The <i>Webalizer</i> allows you to export processed data to other programs by using <i>tab delimited</i> text files. The <i>Dump*</i> commands specify which files are to be written, and where.</p>
<dl>
<dt><code>DumpPath </code><i>name</i></p>
<dd> Save dump files in directory <i>name</i>. If not specified, the default output directory will be used. Do not specify a trailing slash (&#8216;/&#8217;).</p>
<dt><code>DumpExtension </code><i>name</i></p>
<dd> Use <i>name</i> as the filename extension for dump files. If not given, the default of <code>tab</code> will be used.</p>
<dt><code>DumpHeader </code>( yes | <code>no</code> )</p>
<dd> Print a column header as the first record of the file.</p>
<dt><code>DumpSites </code>( yes | <code>no</code> )</p>
<dd> Dump the sites data to a tab delimited file.</p>
<dt><code>DumpURLs </code>( yes | <code>no</code> )</p>
<dd> Dump the url data to a tab delimited file.</p>
<dt><code>DumpReferrers </code>( yes | <code>no</code> )</p>
<dd> Dump the referrer data to a tab delimited file. This data is only available if using a log that contains referrer information (ie: a combined format web log).</p>
<dt><code>DumpAgents </code>( yes | <code>no</code> )</p>
<dd> Dump the user agent data to a tab delimited file. This data is only available if using a log that contains user agent information (ie: a combined format web log).</p>
<dt><code>DumpUsers </code>( yes | <code>no</code> )</p>
<dd> Dump the username data to a tab delimited file. This data is only available if processing a wu-ftpd xferlog or a web log that contains http authentication information.</p>
<dt><code>DumpSearchStr </code>( yes | <code>no</code> )</p>
<dd> Dump the search string data to a tab delimited file. This data is only available if processing a web log that contains referrer information and had search string information present.</dl>
<h2>FILES</h2>
<dl>
<dt><i>webalizer.conf</i></p>
<dd> Default configuration file. Is searched for in the current directory and if not found, in the <i>/etc/</i> directory.</p>
<dt><i>webalizer.hist</i></p>
<dd> Monthly history file for previous months. (can be changed)</p>
<dt><i>webalizer.current</i></p>
<dd> Current state data file (Incremental processing). (can be changed)</p>
<dt><i>xxxxx_YYYYMM.html</i></p>
<dd> Various monthly <i>HTML</i> output files produced. (extension can be changed)</p>
<dt><i>xxxxx_YYYYMM.png</i></p>
<dd> Various monthly image files used in the reports.</p>
<dt><i>xxxxx_YYYYMM.tab</i></p>
<dd> Monthly tab delimited text files. (extension can be changed)</dl>
<h2>BUGS</h2>
<p> Please report bugs to the author.</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 1997-2013 by Bradford L. Barrett. Distributed under the GNU GPL. See the files &quot;<i>COPYING</i>&quot; and &quot;<i>Copyright</i>&quot;, supplied with all distributions for additional information.</p>
<h2>AUTHOR</h2>
<p> Bradford L. Barrett &lt;<i>brad at mrunix dot net</i>&gt; </p>
<h2>Index</h2>
