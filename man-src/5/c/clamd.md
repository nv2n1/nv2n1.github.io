---
title: "clamd(5)"
name: "clamd"
section: "5"
letter: "c"
url: "/docs/linux/man/5-clamd/"
description: "clamd.conf – Configuration file for Clam AntiVirus Daemon"
---

<p><code>clamd.conf</code> &#8211; Configuration file for Clam AntiVirus Daemon</p>
<h2>Description</h2>
<p>clamd.conf configures the Clam AntiVirus daemon, <a href="/docs/linux/man/8-clamd/">clamd</a>(8).</p>
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
<p>When some option is not used (commented out or not included in the configuration file at all) clamd takes a default action.</p>
<dl>
<dt><code>Example</code></dt>
<dd>If this option is set clamd will not run.</dd>
<dt><code>LogFile STRING</code></dt>
<dd>Enable logging to selected file.<br />
 Default: no</dd>
<dt><code>LogFileUnlock BOOL</code></dt>
<dd>Disable a system lock that protects against running clamd with the same configuration file multiple times.<br />
 Default: no</dd>
<dt><code>LogFileMaxSize SIZE</code></dt>
<dd>Limit the size of the log file. The logger will be automatically disabled if the file is greater than SIZE. Value of 0 disables the limit.<br />
 Default: 1M</dd>
<dt><code>LogTime BOOL</code></dt>
<dd>Log time for each message.<br />
 Default: no</dd>
<dt><code>LogClean BOOL</code></dt>
<dd>Log clean files.<br />
 Default: no</dd>
<dt><code>LogSyslog BOOL</code></dt>
<dd>Use system logger (can work together with LogFile).<br />
 Default: no</dd>
<dt><code>LogFacility STRING</code></dt>
<dd>Specify the type of syslog messages &#8211; please refer to &#8216;man syslog&#8217; for facility names.<br />
 Default: LOG_LOCAL6</dd>
<dt><code>LogVerbose BOOL</code></dt>
<dd>Enable verbose logging.<br />
 Default: no</dd>
<dt><code>PidFile STRING</code></dt>
<dd>Save the process identifier of a listening daemon (main thread) to a specified file.<br />
 Default: no</dd>
<dt><code>TemporaryDirectory STRING</code></dt>
<dd>Optional path to the global temporary directory.<br />
 Default: system specific (usually /tmp or /var/tmp).</dd>
<dt><code>DatabaseDirectory STRING</code></dt>
<dd>Path to a directory containing database files.<br />
 Default: /var/lib/clamav</dd>
<dt><code>LocalSocket STRING</code></dt>
<dd>Path to a local (Unix) socket the daemon will listen on.<br />
 Default: no</dd>
<dt><code>FixStaleSocket BOOL</code></dt>
<dd>Remove stale socket after unclean shutdown.<br />
 Default: yes</dd>
<dt><code>TCPSocket NUMBER</code></dt>
<dd>TCP port number the daemon will listen on.<br />
 Default: no</dd>
<dt><code>TCPAddr STRING</code></dt>
<dd>TCP socket address to bind to. By default clamd binds to INADDR_ANY.<br />
 Default: no</dd>
<dt><code>MaxConnectionQueueLength NUMBER</code></dt>
<dd>Maximum length the queue of pending connections may grow to.<br />
 Default: 15</dd>
<dt><code>MaxThreads NUMBER</code></dt>
<dd>Maximum number of threads running at the same time.<br />
 Default: 10</dd>
<dt><code>ReadTimeout NUMBER</code></dt>
<dd>Waiting for data from a client socket will timeout after this time (seconds).<br />
 Default: 120</dd>
<dt><code>CommandReadTimeout NUMBER</code></dt>
<dd>This option specifies the time (in seconds) after which clamd should timeout if a client doesn&#8217;t provide any initial command after connecting. Note: the timeout for subsequents commands, and/or data chunks is specified by ReadTimeout.<br />
 Default: 5</dd>
<dt><code>SendBufTimeout NUMBER</code></dt>
<dd>This option specifies how long to wait (in miliseconds) if the send buffer is full. Keep this value low to prevent clamd hanging.<br />
 Default: 500</dd>
<dt><code>MaxQueue NUMBER</code></dt>
<dd>Maximum number of queued items (including those being processed by MaxThreads threads). It is recommended to have this value at least twice MaxThreads if possible.<br />
 <code>WARNING: you shouldn&#8217;t increase this too much to avoid running out of file descriptors, the following condition should hold: MaxThreads*MaxRecursion + MaxQueue &#8211; MaxThreads + 6 &lt; RLIMIT_NOFILE.</code> RLIMIT_NOFILE is the maximum number of open file descriptors (usually 1024), set by <code>ulimit -n</code>.<br />
 Default: 100</dd>
<dt><code>IdleTimeout NUMBER</code></dt>
<dd>Waiting for a new job will timeout after this time (seconds).<br />
 Default: 30</dd>
<dt><code>ExcludePath REGEX</code></dt>
<dd>Don&#8217;t scan files and directories matching REGEX. This directive can be used multiple times.<br />
 Default: scan all</dd>
<dt><code>MaxDirectoryRecursion NUMBER</code></dt>
<dd>Maximum depth directories are scanned at.<br />
 Default: 15</dd>
<dt><code>FollowDirectorySymlinks BOOL</code></dt>
<dd>Follow directory symlinks.<br />
 Default: no</dd>
<dt><code>FollowFileSymlinks BOOL</code></dt>
<dd>Follow regular file symlinks.<br />
 Default: no</dd>
<dt><code>SelfCheck NUMBER</code></dt>
<dd>Perform a database check.<br />
 Default: 1800</dd>
<dt><code>VirusEvent COMMAND</code></dt>
<dd>Execute COMMAND when a virus is found. In the command string %v will be replaced with the virus name.<br />
 Default: no</dd>
<dt><code>ExitOnOOM BOOL</code></dt>
<dd>Stop daemon when libclamav reports out of memory condition.<br />
 Default: no</dd>
<dt><code>User STRING</code></dt>
<dd>Run as another user (clamd must be started by root to make this option working).<br />
 Default: no</dd>
<dt><code>AllowSupplementaryGroups BOOL</code></dt>
<dd>Initialize supplementary group access (clamd must be started by root).<br />
 Default: no</dd>
<dt><code>Foreground BOOL</code></dt>
<dd>Don&#8217;t fork into background.<br />
 Default: no</dd>
<dt><code>Debug BOOL</code></dt>
<dd>Enable debug messages from libclamav.</dd>
<dt><code>LeaveTemporaryFiles BOOL</code></dt>
<dd>Do not remove temporary files (for debug purpose).<br />
 Default: no</dd>
<dt><code>StreamMaxLength SIZE</code></dt>
<dd>Clamd uses FTP-like protocol to receive data from remote clients. If you are using clamav-milter to balance load between remote clamd daemons on firewall servers you may need to tune the Stream* options. This option allows you to specify the upper limit for data size that will be transfered to remote daemon when scanning a single file. It should match your MTA&#8217;s limit for a maximum attachment size.<br />
 Default: 10M</dd>
<dt><code>StreamMinPort NUMBER</code></dt>
<dd>Limit data port range.<br />
 Default: 1024</dd>
<dt><code>StreamMaxPort NUMBER</code></dt>
<dd>Limit data port range.<br />
 Default: 2048</dd>
<dt><code>DetectPUA</code></dt>
<dd>Detect Possibly Unwanted Applications.<br />
 Default: No</dd>
<dt><code>ExcludePUA CATEGORY</code></dt>
<dd>Exclude a specific PUA category. This directive can be used multiple times. See <a rel="nofollow" href="http://www.clamav.net/support/pua">http://www.clamav.net/support/pua</a> for the complete list of PUA categories.<br />
 Default: Load all categories (if DetectPUA is activated)</dd>
<dt><code>IncludePUA CATEGORY</code></dt>
<dd>Only include a specific PUA category. This directive can be used multiple times. See <a rel="nofollow" href="http://www.clamav.net/support/pua">http://www.clamav.net/support/pua</a> for the complete list of PUA categories.<br />
 Default: Load all categories (if DetectPUA is activated)</dd>
<dt><code>AlgorithmicDetection BOOL</code></dt>
<dd>In some cases (eg. complex malware, exploits in graphic files, and others), ClamAV uses special algorithms to provide accurate detection. This option controls the algorithmic detection.<br />
 Default: yes</dd>
<dt><code>ScanPE BOOL</code></dt>
<dd>PE stands for Portable Executable &#8211; it&#8217;s an executable file format used in all 32 and 64-bit versions of Windows operating systems. This option allows ClamAV to perform a deeper analysis of executable files and it&#8217;s also required for decompression of popular executable packers such as UPX.<br />
 Default: yes</dd>
<dt><code>ScanELF BOOL</code></dt>
<dd>Executable and Linking Format is a standard format for UN*X executables. This option allows you to control the scanning of ELF files.<br />
 Default: yes</dd>
<dt><code>DetectBrokenExecutables BOOL</code></dt>
<dd>With this option clamd will try to detect broken executables (both PE and ELF) and mark them as Broken.Executable.<br />
 Default: no</dd>
<dt><code>ScanOLE2 BOOL</code></dt>
<dd>This option enables scanning of OLE2 files, such as Microsoft Office documents and .msi files.<br />
 Default: yes</dd>
<dt><code>ScanPDF BOOL</code></dt>
<dd>This option enables scanning within PDF files.<br />
 Default: yes</dd>
<dt><code>ScanHTML BOOL</code></dt>
<dd>Enables HTML detection and normalisation.<br />
 Default: yes</dd>
<dt><code>ScanMail BOOL</code></dt>
<dd>Enable scanning of mail files.<br />
 Default: yes</dd>
<dt><code>MailFollowURLs BOOL</code></dt>
<dd>If an email contains URLs ClamAV can download and scan them. <code>WARNING: This option may open your system to a DoS attack. Never use it on loaded servers.</code><br />
 Default: no</dd>
<dt><code>ScanPartialMessages BOOL</code></dt>
<dd>Scan RFC1341 messages split over many emails. You will need to periodically clean up $TemporaryDirectory/clamav-partial directory. <code>WARNING: This option may open your system to a DoS attack. Never use it on loaded servers.</code><br />
 Default: no</dd>
<dt><code>MailMaxRecursion NUMBER (OBSOLETE)</code></dt>
<dd><code>WARNING:</code> This option is no longer accepted. See <code>MaxRecursion</code>.</dd>
<dt><code>PhishingSignatures BOOL</code></dt>
<dd>With this option enabled ClamAV will try to detect phishing attempts by using signatures.<br />
 Default: yes</dd>
<dt><code>PhishingScanURLs BOOL</code></dt>
<dd>Scan URLs found in mails for phishing attempts using heuristics. This will classify &quot;Possibly Unwanted&quot; phishing emails as Phishing.Heuristics.Email.*<br />
 Default: yes</dd>
<dt><code>PhishingAlwaysBlockSSLMismatch BOOL</code></dt>
<dd>Always block SSL mismatches in URLs, even if the URL isn&#8217;t in the database. This can lead to false positives.<br />
 Default: no</dd>
<dt><code>PhishingAlwaysBlockCloak BOOL</code></dt>
<dd>Always block cloaked URLs, even if URL isn&#8217;t in database. This can lead to false positives.<br />
 Default: no</dd>
<dt><code>HeuristicScanPrecedence BOOL</code></dt>
<dd>Allow heuristic match to take precedence. When enabled, if a heuristic scan (such as phishingScan) detects a possible virus/phishing it will stop scanning immediately. Recommended, saves CPU scan-time. When disabled, virus/phishing detected by heuristic scans will be reported only at the end of a scan. If an archive contains both a heuristically detected virus/phishing, and a real malware, the real malware will be reported. Keep this disabled if you intend to handle &quot;*.Heuristics.*&quot; viruses differently from &quot;real&quot; malware. If a non-heuristically-detected virus (signature-based) is found first, the scan is interrupted immediately, regardless of this config option.<br />
 Default: no</dd>
<dt><code>StructuredDataDetection BOOL</code></dt>
<dd>Enable the DLP module.<br />
 Default: no</dd>
<dt><code>StructuredMinCreditCardCount NUMBER</code></dt>
<dd>This option sets the lowest number of Credit Card numbers found in a file to generate a detect.<br />
 Default: 3</dd>
<dt><code>StructuredMinSSNCount NUMBER</code></dt>
<dd>This option sets the lowest number of Social Security Numbers found in a file to generate a detect.<br />
 Default: 3</dd>
<dt><code>StructuredSSNFormatNormal BOOL</code></dt>
<dd>With this option enabled the DLP module will search for valid SSNs formatted as xxx-yy-zzzz.<br />
 Default: Yes</dd>
<dt><code>StructuredSSNFormatStripped BOOL</code></dt>
<dd>With this option enabled the DLP module will search for valid SSNs formatted as xxxyyzzzz.<br />
 Default: No</dd>
<dt><code>ScanArchive BOOL</code></dt>
<dd>Enable archive scanning.<br />
 Default: yes</dd>
<dt><code>ArchiveMaxFileSize (OBSOLETE)</code></dt>
<dd><code>WARNING:</code> This option is no longer accepted. See <code>MaxFileSize</code> and <code>MaxScanSize</code>.</dd>
<dt><code>ArchiveMaxRecursion (OBSOLETE)</code></dt>
<dd><code>WARNING:</code> This option is no longer accepted. See <code>MaxRecursion</code>.</dd>
<dt><code>ArchiveMaxFiles (OBSOLETE)</code></dt>
<dd><code>WARNING:</code> This option is no longer accepted. See <code>MaxFiles</code>.</dd>
<dt><code>ArchiveMaxCompressionRatio (OBSOLETE)</code></dt>
<dd><code>WARNING:</code> This option is no longer accepted.</dd>
<dt><code>ArchiveBlockMax (OBSOLETE)</code></dt>
<dd><code>WARNING:</code> This option is no longer accepted.</dd>
<dt><code>ArchiveLimitMemoryUsage BOOL</code></dt>
<dd>Use slower decompression algorithm which uses less memory. This option only affects the bzip2 decompressor.<br />
 Default: no</dd>
<dt><code>ArchiveBlockEncrypted BOOL</code></dt>
<dd>Mark encrypted archives as viruses (Encrypted.Zip, Encrypted.RAR).<br />
 Default: no</dd>
<dt><code>MaxScanSize SIZE</code></dt>
<dd>Sets the maximum amount of data to be scanned for each input file. Archives and other containers are recursively extracted and scanned up to this value. <code>Warning: disabling this limit or setting it too high may result in severe damage to the system.</code><br />
 Default: 100M</dd>
<dt><code>MaxFileSize SIZE</code></dt>
<dd>Files larger than this limit won&#8217;t be scanned. Affects the input file itself as well as files contained inside it (when the input file is an archive, a document or some other kind of container). <code>Warning: disabling this limit or setting it too high may result in severe damage to the system.</code><br />
 Default: 25M</dd>
<dt><code>MaxRecursion NUMBER</code></dt>
<dd>Nested archives are scanned recursively, e.g. if a Zip archive contains a RAR file, all files within it will also be scanned. This options specifies how deeply the process should be continued. <code>Warning: disabling this limit or setting it too high may result in severe damage to the system.</code><br />
 Default: 16</dd>
<dt><code>MaxFiles NUMBER</code></dt>
<dd>Number of files to be scanned within an archive, a document, or any other kind of container. <code>Warning: disabling this limit or setting it too high may result in severe damage to the system.</code><br />
 Default: 10000</dd>
<dt><code>ClamukoScanOnAccess BOOL</code></dt>
<dd>Enable Clamuko. Dazuko (/dev/dazuko) must be configured and running.<br />
 Default: no</dd>
<dt><code>ClamukoScanOnOpen BOOL</code></dt>
<dd>Scan files on open.<br />
 Default: no</dd>
<dt><code>ClamukoScanOnClose BOOL</code></dt>
<dd>Scan files on close.<br />
 Default: no.</dd>
<dt><code>ClamukoScanOnExec BOOL</code></dt>
<dd>Scan files on execute.<br />
 Default: no</dd>
<dt><code>ClamukoIncludePath STRING</code></dt>
<dd>Set the include paths (all files and directories inside them will be scanned). You can have multiple ClamukoIncludePath directives but each directory must be added in a separate line).<br />
 Default: no</dd>
<dt><code>ClamukoExcludePath STRING</code></dt>
<dd>Set the exclude paths. All subdirectories will also be excluded.<br />
 Default: no</dd>
<dt><code>ClamukoMaxFileSize SIZE</code></dt>
<dd>Ignore files larger than SIZE.<br />
 Default: 5M</dd></dl>
<h2>Notes</h2>
<p>All options expressing a size are limited to max 4GB. Values in excess will be resetted to the maximum.</p>
<h2>Files</h2>
<p>/etc/clamd.conf</p>
<h2>Author</h2>
<p>Tomasz Kojm &lt;tkojm [at] clamav.net&gt;</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-clamd/">clamd</a>(8), <a href="/docs/linux/man/1-clamdscan/">clamdscan</a>(1), <a href="/docs/linux/man/8-clamav-milter/">clamav-milter</a>(8), <a href="/docs/linux/man/1-clamscan/">clamscan</a>(1), <a href="/docs/linux/man/1-freshclam/">freshclam</a>(1), <a href="/docs/linux/man/1-sigtool/">sigtool</a>(1) </p>
