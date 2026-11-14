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
<dt><code>BOOL</code></p>
<dd>Boolean value (yes/no or true/false or 1/0).</p>
<dt><code>STRING</code></p>
<dd>String without blank characters.</p>
<dt><code>SIZE</code></p>
<dd>Size in bytes. You can use &#8216;M&#8217; or &#8216;m&#8217; modifiers for megabytes and &#8216;K&#8217; or &#8216;k&#8217; for kilobytes.</p>
<dt><code>NUMBER</code></p>
<dd>Unsigned integer.</dl>
<h2>Directives</h2>
<p>When some option is not used (commented out or not included in the configuration file at all) clamd takes a default action.</p>
<dl>
<dt><code>Example</code></p>
<dd>If this option is set clamd will not run.</p>
<dt><code>LogFile STRING</code></p>
<dd>Enable logging to selected file.<br />
 Default: no</p>
<dt><code>LogFileUnlock BOOL</code></p>
<dd>Disable a system lock that protects against running clamd with the same configuration file multiple times.<br />
 Default: no</p>
<dt><code>LogFileMaxSize SIZE</code></p>
<dd>Limit the size of the log file. The logger will be automatically disabled if the file is greater than SIZE. Value of 0 disables the limit.<br />
 Default: 1M</p>
<dt><code>LogTime BOOL</code></p>
<dd>Log time for each message.<br />
 Default: no</p>
<dt><code>LogClean BOOL</code></p>
<dd>Log clean files.<br />
 Default: no</p>
<dt><code>LogSyslog BOOL</code></p>
<dd>Use system logger (can work together with LogFile).<br />
 Default: no</p>
<dt><code>LogFacility STRING</code></p>
<dd>Specify the type of syslog messages &#8211; please refer to &#8216;man syslog&#8217; for facility names.<br />
 Default: LOG_LOCAL6</p>
<dt><code>LogVerbose BOOL</code></p>
<dd>Enable verbose logging.<br />
 Default: no</p>
<dt><code>PidFile STRING</code></p>
<dd>Save the process identifier of a listening daemon (main thread) to a specified file.<br />
 Default: no</p>
<dt><code>TemporaryDirectory STRING</code></p>
<dd>Optional path to the global temporary directory.<br />
 Default: system specific (usually /tmp or /var/tmp).</p>
<dt><code>DatabaseDirectory STRING</code></p>
<dd>Path to a directory containing database files.<br />
 Default: /var/lib/clamav</p>
<dt><code>LocalSocket STRING</code></p>
<dd>Path to a local (Unix) socket the daemon will listen on.<br />
 Default: no</p>
<dt><code>FixStaleSocket BOOL</code></p>
<dd>Remove stale socket after unclean shutdown.<br />
 Default: yes</p>
<dt><code>TCPSocket NUMBER</code></p>
<dd>TCP port number the daemon will listen on.<br />
 Default: no</p>
<dt><code>TCPAddr STRING</code></p>
<dd>TCP socket address to bind to. By default clamd binds to INADDR_ANY.<br />
 Default: no</p>
<dt><code>MaxConnectionQueueLength NUMBER</code></p>
<dd>Maximum length the queue of pending connections may grow to.<br />
 Default: 15</p>
<dt><code>MaxThreads NUMBER</code></p>
<dd>Maximum number of threads running at the same time.<br />
 Default: 10</p>
<dt><code>ReadTimeout NUMBER</code></p>
<dd>Waiting for data from a client socket will timeout after this time (seconds).<br />
 Default: 120</p>
<dt><code>CommandReadTimeout NUMBER</code></p>
<dd>This option specifies the time (in seconds) after which clamd should timeout if a client doesn&#8217;t provide any initial command after connecting. Note: the timeout for subsequents commands, and/or data chunks is specified by ReadTimeout.<br />
 Default: 5</p>
<dt><code>SendBufTimeout NUMBER</code></p>
<dd>This option specifies how long to wait (in miliseconds) if the send buffer is full. Keep this value low to prevent clamd hanging.<br />
 Default: 500</p>
<dt><code>MaxQueue NUMBER</code></p>
<dd>Maximum number of queued items (including those being processed by MaxThreads threads). It is recommended to have this value at least twice MaxThreads if possible.<br />
 <code>WARNING: you shouldn&#8217;t increase this too much to avoid running out of file descriptors, the following condition should hold: MaxThreads*MaxRecursion + MaxQueue &#8211; MaxThreads + 6 &lt; RLIMIT_NOFILE.</code> RLIMIT_NOFILE is the maximum number of open file descriptors (usually 1024), set by <code>ulimit -n</code>.<br />
 Default: 100</p>
<dt><code>IdleTimeout NUMBER</code></p>
<dd>Waiting for a new job will timeout after this time (seconds).<br />
 Default: 30</p>
<dt><code>ExcludePath REGEX</code></p>
<dd>Don&#8217;t scan files and directories matching REGEX. This directive can be used multiple times.<br />
 Default: scan all</p>
<dt><code>MaxDirectoryRecursion NUMBER</code></p>
<dd>Maximum depth directories are scanned at.<br />
 Default: 15</p>
<dt><code>FollowDirectorySymlinks BOOL</code></p>
<dd>Follow directory symlinks.<br />
 Default: no</p>
<dt><code>FollowFileSymlinks BOOL</code></p>
<dd>Follow regular file symlinks.<br />
 Default: no</p>
<dt><code>SelfCheck NUMBER</code></p>
<dd>Perform a database check.<br />
 Default: 1800</p>
<dt><code>VirusEvent COMMAND</code></p>
<dd>Execute COMMAND when a virus is found. In the command string %v will be replaced with the virus name.<br />
 Default: no</p>
<dt><code>ExitOnOOM BOOL</code></p>
<dd>Stop daemon when libclamav reports out of memory condition.<br />
 Default: no</p>
<dt><code>User STRING</code></p>
<dd>Run as another user (clamd must be started by root to make this option working).<br />
 Default: no</p>
<dt><code>AllowSupplementaryGroups BOOL</code></p>
<dd>Initialize supplementary group access (clamd must be started by root).<br />
 Default: no</p>
<dt><code>Foreground BOOL</code></p>
<dd>Don&#8217;t fork into background.<br />
 Default: no</p>
<dt><code>Debug BOOL</code></p>
<dd>Enable debug messages from libclamav.</p>
<dt><code>LeaveTemporaryFiles BOOL</code></p>
<dd>Do not remove temporary files (for debug purpose).<br />
 Default: no</p>
<dt><code>StreamMaxLength SIZE</code></p>
<dd>Clamd uses FTP-like protocol to receive data from remote clients. If you are using clamav-milter to balance load between remote clamd daemons on firewall servers you may need to tune the Stream* options. This option allows you to specify the upper limit for data size that will be transfered to remote daemon when scanning a single file. It should match your MTA&#8217;s limit for a maximum attachment size.<br />
 Default: 10M</p>
<dt><code>StreamMinPort NUMBER</code></p>
<dd>Limit data port range.<br />
 Default: 1024</p>
<dt><code>StreamMaxPort NUMBER</code></p>
<dd>Limit data port range.<br />
 Default: 2048</p>
<dt><code>DetectPUA</code></p>
<dd>Detect Possibly Unwanted Applications.<br />
 Default: No</p>
<dt><code>ExcludePUA CATEGORY</code></p>
<dd>Exclude a specific PUA category. This directive can be used multiple times. See <a rel="nofollow" href="http://www.clamav.net/support/pua">http://www.clamav.net/support/pua</a> for the complete list of PUA categories.<br />
 Default: Load all categories (if DetectPUA is activated)</p>
<dt><code>IncludePUA CATEGORY</code></p>
<dd>Only include a specific PUA category. This directive can be used multiple times. See <a rel="nofollow" href="http://www.clamav.net/support/pua">http://www.clamav.net/support/pua</a> for the complete list of PUA categories.<br />
 Default: Load all categories (if DetectPUA is activated)</p>
<dt><code>AlgorithmicDetection BOOL</code></p>
<dd>In some cases (eg. complex malware, exploits in graphic files, and others), ClamAV uses special algorithms to provide accurate detection. This option controls the algorithmic detection.<br />
 Default: yes</p>
<dt><code>ScanPE BOOL</code></p>
<dd>PE stands for Portable Executable &#8211; it&#8217;s an executable file format used in all 32 and 64-bit versions of Windows operating systems. This option allows ClamAV to perform a deeper analysis of executable files and it&#8217;s also required for decompression of popular executable packers such as UPX.<br />
 Default: yes</p>
<dt><code>ScanELF BOOL</code></p>
<dd>Executable and Linking Format is a standard format for UN*X executables. This option allows you to control the scanning of ELF files.<br />
 Default: yes</p>
<dt><code>DetectBrokenExecutables BOOL</code></p>
<dd>With this option clamd will try to detect broken executables (both PE and ELF) and mark them as Broken.Executable.<br />
 Default: no</p>
<dt><code>ScanOLE2 BOOL</code></p>
<dd>This option enables scanning of OLE2 files, such as Microsoft Office documents and .msi files.<br />
 Default: yes</p>
<dt><code>ScanPDF BOOL</code></p>
<dd>This option enables scanning within PDF files.<br />
 Default: yes</p>
<dt><code>ScanHTML BOOL</code></p>
<dd>Enables HTML detection and normalisation.<br />
 Default: yes</p>
<dt><code>ScanMail BOOL</code></p>
<dd>Enable scanning of mail files.<br />
 Default: yes</p>
<dt><code>MailFollowURLs BOOL</code></p>
<dd>If an email contains URLs ClamAV can download and scan them. <code>WARNING: This option may open your system to a DoS attack. Never use it on loaded servers.</code><br />
 Default: no</p>
<dt><code>ScanPartialMessages BOOL</code></p>
<dd>Scan RFC1341 messages split over many emails. You will need to periodically clean up $TemporaryDirectory/clamav-partial directory. <code>WARNING: This option may open your system to a DoS attack. Never use it on loaded servers.</code><br />
 Default: no</p>
<dt><code>MailMaxRecursion NUMBER (OBSOLETE)</code></p>
<dd><code>WARNING:</code> This option is no longer accepted. See <code>MaxRecursion</code>.</p>
<dt><code>PhishingSignatures BOOL</code></p>
<dd>With this option enabled ClamAV will try to detect phishing attempts by using signatures.<br />
 Default: yes</p>
<dt><code>PhishingScanURLs BOOL</code></p>
<dd>Scan URLs found in mails for phishing attempts using heuristics. This will classify &quot;Possibly Unwanted&quot; phishing emails as Phishing.Heuristics.Email.*<br />
 Default: yes</p>
<dt><code>PhishingAlwaysBlockSSLMismatch BOOL</code></p>
<dd>Always block SSL mismatches in URLs, even if the URL isn&#8217;t in the database. This can lead to false positives.<br />
 Default: no</p>
<dt><code>PhishingAlwaysBlockCloak BOOL</code></p>
<dd>Always block cloaked URLs, even if URL isn&#8217;t in database. This can lead to false positives.<br />
 Default: no</p>
<dt><code>HeuristicScanPrecedence BOOL</code></p>
<dd>Allow heuristic match to take precedence. When enabled, if a heuristic scan (such as phishingScan) detects a possible virus/phishing it will stop scanning immediately. Recommended, saves CPU scan-time. When disabled, virus/phishing detected by heuristic scans will be reported only at the end of a scan. If an archive contains both a heuristically detected virus/phishing, and a real malware, the real malware will be reported. Keep this disabled if you intend to handle &quot;*.Heuristics.*&quot; viruses differently from &quot;real&quot; malware. If a non-heuristically-detected virus (signature-based) is found first, the scan is interrupted immediately, regardless of this config option.<br />
 Default: no</p>
<dt><code>StructuredDataDetection BOOL</code></p>
<dd>Enable the DLP module.<br />
 Default: no</p>
<dt><code>StructuredMinCreditCardCount NUMBER</code></p>
<dd>This option sets the lowest number of Credit Card numbers found in a file to generate a detect.<br />
 Default: 3</p>
<dt><code>StructuredMinSSNCount NUMBER</code></p>
<dd>This option sets the lowest number of Social Security Numbers found in a file to generate a detect.<br />
 Default: 3</p>
<dt><code>StructuredSSNFormatNormal BOOL</code></p>
<dd>With this option enabled the DLP module will search for valid SSNs formatted as xxx-yy-zzzz.<br />
 Default: Yes</p>
<dt><code>StructuredSSNFormatStripped BOOL</code></p>
<dd>With this option enabled the DLP module will search for valid SSNs formatted as xxxyyzzzz.<br />
 Default: No</p>
<dt><code>ScanArchive BOOL</code></p>
<dd>Enable archive scanning.<br />
 Default: yes</p>
<dt><code>ArchiveMaxFileSize (OBSOLETE)</code></p>
<dd><code>WARNING:</code> This option is no longer accepted. See <code>MaxFileSize</code> and <code>MaxScanSize</code>.</p>
<dt><code>ArchiveMaxRecursion (OBSOLETE)</code></p>
<dd><code>WARNING:</code> This option is no longer accepted. See <code>MaxRecursion</code>.</p>
<dt><code>ArchiveMaxFiles (OBSOLETE)</code></p>
<dd><code>WARNING:</code> This option is no longer accepted. See <code>MaxFiles</code>.</p>
<dt><code>ArchiveMaxCompressionRatio (OBSOLETE)</code></p>
<dd><code>WARNING:</code> This option is no longer accepted.</p>
<dt><code>ArchiveBlockMax (OBSOLETE)</code></p>
<dd><code>WARNING:</code> This option is no longer accepted.</p>
<dt><code>ArchiveLimitMemoryUsage BOOL</code></p>
<dd>Use slower decompression algorithm which uses less memory. This option only affects the bzip2 decompressor.<br />
 Default: no</p>
<dt><code>ArchiveBlockEncrypted BOOL</code></p>
<dd>Mark encrypted archives as viruses (Encrypted.Zip, Encrypted.RAR).<br />
 Default: no</p>
<dt><code>MaxScanSize SIZE</code></p>
<dd>Sets the maximum amount of data to be scanned for each input file. Archives and other containers are recursively extracted and scanned up to this value. <code>Warning: disabling this limit or setting it too high may result in severe damage to the system.</code><br />
 Default: 100M</p>
<dt><code>MaxFileSize SIZE</code></p>
<dd>Files larger than this limit won&#8217;t be scanned. Affects the input file itself as well as files contained inside it (when the input file is an archive, a document or some other kind of container). <code>Warning: disabling this limit or setting it too high may result in severe damage to the system.</code><br />
 Default: 25M</p>
<dt><code>MaxRecursion NUMBER</code></p>
<dd>Nested archives are scanned recursively, e.g. if a Zip archive contains a RAR file, all files within it will also be scanned. This options specifies how deeply the process should be continued. <code>Warning: disabling this limit or setting it too high may result in severe damage to the system.</code><br />
 Default: 16</p>
<dt><code>MaxFiles NUMBER</code></p>
<dd>Number of files to be scanned within an archive, a document, or any other kind of container. <code>Warning: disabling this limit or setting it too high may result in severe damage to the system.</code><br />
 Default: 10000</p>
<dt><code>ClamukoScanOnAccess BOOL</code></p>
<dd>Enable Clamuko. Dazuko (/dev/dazuko) must be configured and running.<br />
 Default: no</p>
<dt><code>ClamukoScanOnOpen BOOL</code></p>
<dd>Scan files on open.<br />
 Default: no</p>
<dt><code>ClamukoScanOnClose BOOL</code></p>
<dd>Scan files on close.<br />
 Default: no.</p>
<dt><code>ClamukoScanOnExec BOOL</code></p>
<dd>Scan files on execute.<br />
 Default: no</p>
<dt><code>ClamukoIncludePath STRING</code></p>
<dd>Set the include paths (all files and directories inside them will be scanned). You can have multiple ClamukoIncludePath directives but each directory must be added in a separate line).<br />
 Default: no</p>
<dt><code>ClamukoExcludePath STRING</code></p>
<dd>Set the exclude paths. All subdirectories will also be excluded.<br />
 Default: no</p>
<dt><code>ClamukoMaxFileSize SIZE</code></p>
<dd>Ignore files larger than SIZE.<br />
 Default: 5M</dl>
<h2>Notes</h2>
<p>All options expressing a size are limited to max 4GB. Values in excess will be resetted to the maximum.</p>
<h2>Files</h2>
<p>/etc/clamd.conf</p>
<h2>Author</h2>
<p>Tomasz Kojm &lt;tkojm [at] clamav.net&gt;</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-clamd/">clamd</a>(8), <a href="/docs/linux/man/1-clamdscan/">clamdscan</a>(1), <a href="/docs/linux/man/8-clamav-milter/">clamav-milter</a>(8), <a href="/docs/linux/man/1-clamscan/">clamscan</a>(1), <a href="/docs/linux/man/1-freshclam/">freshclam</a>(1), <a href="/docs/linux/man/1-sigtool/">sigtool</a>(1) </p>
