---
title: "clamd-conf(5)"
name: "clamd-conf"
section: "5"
letter: "c"
url: "/docs/linux/man/5-clamd-conf/"
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
<dd>Size in bytes. You can use &#8216;M&#8217; or &#8216;m&#8217; modifiers for megabytes and &#8216;K&#8217; or &#8216;k&#8217; for kilobytes. To specify the size in bytes just don&#8217;t use modifiers.</p>
<dt><code>NUMBER</code></p>
<dd>Unsigned integer.</dl>
<h2>Directives</h2>
<p>When some option is not used (commented out or not included in the configuration file at all) clamd takes a default action.</p>
<dl>
<dt><code>Example</code></p>
<dd>If this option is set clamd will not run.</p>
<dt><code>LogFile STRING</code></p>
<dd>Save all reports to a log file.<br />
 Default: disabled</p>
<dt><code>LogFileUnlock BOOL</code></p>
<dd>By default the log file is locked for writing and only a single daemon process can write to it. This option disables the lock.<br />
 Default: no</p>
<dt><code>LogFileMaxSize SIZE</code></p>
<dd>Maximum size of the log file.<br />
 Value of 0 disables the limit.<br />
 Default: 1048576</p>
<dt><code>LogTime BOOL</code></p>
<dd>Log time for each message.<br />
 Default: no</p>
<dt><code>LogClean BOOL</code></p>
<dd>Log all clean files.<br />
 Useful in debugging but drastically increases the log size.<br />
 Default: no</p>
<dt><code>LogSyslog BOOL</code></p>
<dd>Use the system logger (can work together with LogFile).<br />
 Default: no</p>
<dt><code>LogFacility STRING</code></p>
<dd>Type of syslog messages<br />
 Please refer to &#8216;man syslog&#8217; for facility names.<br />
 Default: LOG_LOCAL6</p>
<dt><code>LogVerbose BOOL</code></p>
<dd>Enable verbose logging.<br />
 Default: no</p>
<dt><code>LogRotate BOOL</code></p>
<dd>Rotate log file. Requires LogFileMaxSize option set prior to this option.<br />
 Default: no</p>
<dt><code>ExtendedDetectionInfo BOOL</code></p>
<dd>Log additional information about the infected file, such as its size and hash, together with the virus name.<br />
 Default: no</p>
<dt><code>PidFile STRING</code></p>
<dd>Save the process identifier of a listening daemon (main thread) to a specified file.<br />
 Default: disabled</p>
<dt><code>TemporaryDirectory STRING</code></p>
<dd>This option allows you to change the default temporary directory.<br />
 Default: system specific (usually /tmp or /var/tmp).</p>
<dt><code>DatabaseDirectory STRING</code></p>
<dd>This option allows you to change the default database directory. If you enable it, please make sure it points to the same directory in both clamd and freshclam.<br />
 Default: defined at configuration (/usr/local/share/clamav)</p>
<dt><code>OfficialDatabaseOnly BOOL</code></p>
<dd>Only load the official signatures published by the ClamAV project.<br />
 Default: no</p>
<dt><code>LocalSocket STRING</code></p>
<dd>Path to a local (Unix) socket the daemon will listen on.<br />
 Default: disabled</p>
<dt><code>LocalSocketGroup STRING</code></p>
<dd>Sets the group ownership on the unix socket.<br />
 Default: the primary group of the user running clamd</p>
<dt><code>LocalSocketMode STRING</code></p>
<dd>Sets the permissions on the unix socket to the specified mode.<br />
 Default: socket is world readable and writable</p>
<dt><code>FixStaleSocket BOOL</code></p>
<dd>Remove stale socket after unclean shutdown.<br />
 Default: yes</p>
<dt><code>TCPSocket NUMBER</code></p>
<dd>TCP port number the daemon will listen on.<br />
 Default: disabled</p>
<dt><code>TCPAddr STRING</code></p>
<dd>By default clamd binds to INADDR_ANY.<br />
 This option allows you to restrict the TCP address and provide some degree of protection from the outside world. This option can be specified multiple times in order to listen on multiple IPs. IPv6 is now supported.<br />
 Default: disabled</p>
<dt><code>MaxConnectionQueueLength NUMBER</code></p>
<dd>Maximum length the queue of pending connections may grow to.<br />
 Default: 200</p>
<dt><code>StreamMaxLength SIZE</code></p>
<dd>Close the STREAM session when the data size limit is exceeded.<br />
 The value should match your MTA&#8217;s limit for the maximum attachment size.<br />
 Default: 25M</p>
<dt><code>StreamMinPort NUMBER</code></p>
<dd>The STREAM command uses an FTP-like protocol.<br />
 This option sets the lower boundary for the port range.<br />
 Default: 1024</p>
<dt><code>StreamMaxPort NUMBER</code></p>
<dd>This option sets the upper boundary for the port range.<br />
 Default: 2048</p>
<dt><code>MaxThreads NUMBER</code></p>
<dd>Maximum number of threads running at the same time.<br />
 Default: 10</p>
<dt><code>ReadTimeout NUMBER</code></p>
<dd>This option specifies the time (in seconds) after which clamd should timeout if a client doesn&#8217;t provide any data.<br />
 Default: 120</p>
<dt><code>CommandReadTimeout NUMBER</code></p>
<dd>This option specifies the time (in seconds) after which clamd should timeout if a client doesn&#8217;t provide any initial command after connecting. Note: the timeout for subsequents commands, and/or data chunks is specified by ReadTimeout.<br />
 Default: 5</p>
<dt><code>SendBufTimeout NUMBER</code></p>
<dd>This option specifies how long to wait (in milliseconds) if the send buffer is full. Keep this value low to prevent clamd hanging.<br />
 Default: 500</p>
<dt><code>MaxQueue NUMBER</code></p>
<dd>Maximum number of queued items (including those being processed by MaxThreads threads). It is recommended to have this value at least twice MaxThreads if possible.<br />
 <code>WARNING: you shouldn&#8217;t increase this too much to avoid running out of file descriptors, the following condition should hold: MaxThreads*MaxRecursion + MaxQueue &#8211; MaxThreads + 6 &lt; RLIMIT_NOFILE.</code> RLIMIT_NOFILE is the maximum number of open file descriptors (usually 1024), set by <code>ulimit -n</code>.<br />
 Default: 100</p>
<dt><code>IdleTimeout NUMBER</code></p>
<dd>This option specifies how long (in seconds) the process should wait for a new job.<br />
 Default: 30</p>
<dt><code>ExcludePath REGEX</code></p>
<dd>Don&#8217;t scan files and directories matching REGEX. This directive can be used multiple times.<br />
 Default: disabled</p>
<dt><code>MaxDirectoryRecursion NUMBER</code></p>
<dd>Maximum depth directories are scanned at.<br />
 Default: 15</p>
<dt><code>FollowDirectorySymlinks BOOL</code></p>
<dd>Follow directory symlinks.<br />
 Default: no</p>
<dt><code>CrossFilesystems BOOL</code></p>
<dd>Scan files and directories on other filesystems.<br />
 Default: yes</p>
<dt><code>FollowFileSymlinks BOOL</code></p>
<dd>Follow regular file symlinks.<br />
 Default: no</p>
<dt><code>SelfCheck NUMBER</code></p>
<dd>This option specifies the time intervals (in seconds) in which clamd should perform a database check.<br />
 Default: 600</p>
<dt><code>VirusEvent COMMAND</code></p>
<dd>Execute a command when a virus is found. In the command string %v will be replaced with the virus name. Additionally, two environment variables will be defined: $CLAM_VIRUSEVENT_FILENAME and $CLAM_VIRUSEVENT_VIRUSNAME.<br />
 Default: disabled</p>
<dt><code>ExitOnOOM BOOL</code></p>
<dd>Stop daemon when libclamav reports out of memory condition.<br />
 Default: no</p>
<dt><code>AllowAllMatchScan BOOL</code></p>
<dd>Permit use of the ALLMATCHSCAN command.<br />
 Default: yes</p>
<dt><code>Foreground BOOL</code></p>
<dd>Don&#8217;t fork into background.<br />
 Default: no</p>
<dt><code>Debug BOOL</code></p>
<dd>Enable debug messages from libclamav.<br />
 Default: no</p>
<dt><code>LeaveTemporaryFiles BOOL</code></p>
<dd>Do not remove temporary files (for debugging purpose).<br />
 Default: no</p>
<dt><code>User STRING</code></p>
<dd>Run the daemon as a specified user (the process must be started by root).<br />
 Default: disabled</p>
<dt><code>AllowSupplementaryGroups BOOL</code></p>
<dd>Initialize a supplementary group access (the process must be started by root).<br />
 Default: no</p>
<dt><code>Bytecode BOOL</code></p>
<dd>With this option enabled ClamAV will load bytecode from the database. It is highly recommended you keep this option turned on, otherwise you may miss detections for many new viruses.<br />
 Default: yes</p>
<dt><code>BytecodeSecurity STRING</code></p>
<dd>Set bytecode security level.</p>
<dl>
<dd>
<dl>
<dd>Possible values:<br />
 <code>TrustSigned</code> &#8211; trust bytecode loaded from signed .c[lv]d files and insert runtime safety checks for bytecode loaded from other sources,<br />
 <code>Paranoid</code> &#8211; don&#8217;t trust any bytecode, insert runtime checks for all.</dl>
</dl>
<dl>
<dd>Recommended: <code>TrustSigned</code>, because bytecode in .cvd files already has these checks.<br />
 Default: TrustSigned</dl>
<dt><code>BytecodeTimeout NUMBER</code></p>
<dd>Set bytecode timeout in milliseconds.<br />
 Default: 5000</p>
<dt><code>BytecodeUnsigned BOOL</code></p>
<dd>Allow loading bytecode from outside digitally signed .c[lv]d files.<br />
 Default: no</p>
<dt><code>BytecodeMode STRING</code></p>
<dd>Set bytecode execution mode.</p>
<dl>
<dd>
<dl>
<dd>Possible values:<br />
 <code>Auto</code> &#8211; automatically choose JIT if possible, fallback to interpreter<br />
 <code>ForceJIT</code> &#8211; always choose JIT, fail if not possible<br />
 <code>ForceInterpreter</code> &#8211; always choose interpreter<br />
 <code>Test</code> &#8211; run with both JIT and interpreter and compare results. Make all failures fatal.</dl>
</dl>
<dl>
<dd>Default: Auto</dl>
<dt><code>DetectPUA BOOL</code></p>
<dd>Detect Possibly Unwanted Applications.<br />
 Default: No</p>
<dt><code>ExcludePUA CATEGORY</code></p>
<dd>Exclude a specific PUA category. This directive can be used multiple times. See <a rel="nofollow" href="http://www.clamav.net/doc/pua.html">http://www.clamav.net/doc/pua.html</a> for the complete list of PUA categories.<br />
 Default: disabled</p>
<dt><code>IncludePUA CATEGORY</code></p>
<dd>Only include a specific PUA category. This directive can be used multiple times. See <a rel="nofollow" href="http://www.clamav.net/doc/pua.html">http://www.clamav.net/doc/pua.html</a> for the complete list of PUA categories.<br />
 Default: disabled</p>
<dt><code>AlgorithmicDetection BOOL</code></p>
<dd>In some cases (eg. complex malware, exploits in graphic files, and others), ClamAV uses special algorithms to provide accurate detection. This option controls the algorithmic detection.<br />
 Default: yes</p>
<dt><code>ScanPE BOOL</code></p>
<dd>PE stands for Portable Executable &#8211; it&#8217;s an executable file format used in all 32 and 64-bit versions of Windows operating systems. This option allows ClamAV to perform a deeper analysis of executable files and it&#8217;s also required for decompression of popular executable packers such as UPX.<br />
 If you turn off this option, the original files will still be scanned, but without additional processing.<br />
 Default: yes</p>
<dt><code>ScanELF BOOL</code></p>
<dd>Executable and Linking Format is a standard format for UN*X executables. This option allows you to control the scanning of ELF files.<br />
 If you turn off this option, the original files will still be scanned, but without additional processing.<br />
 Default: yes</p>
<dt><code>DetectBrokenExecutables BOOL</code></p>
<dd>With this option clamd will try to detect broken executables (both PE and ELF) and mark them as Broken.Executable.<br />
 Default: no</p>
<dt><code>ScanMail BOOL</code></p>
<dd>Enable scanning of mail files.<br />
 If you turn off this option, the original files will still be scanned, but without parsing individual messages/attachments.<br />
 Default: yes</p>
<dt><code>ScanPartialMessages BOOL</code></p>
<dd>Scan RFC1341 messages split over many emails. You will need to periodically clean up $TemporaryDirectory/clamav-partial directory. <code>WARNING: This option may open your system to a DoS attack. Never use it on loaded servers.</code><br />
 Default: no</p>
<dt><code>PhishingSignatures BOOL</code></p>
<dd>With this option enabled ClamAV will try to detect phishing attempts by using signatures.<br />
 Default: yes</p>
<dt><code>PhishingScanURLs BOOL</code></p>
<dd>Scan URLs found in mails for phishing attempts using heuristics. This will classify &quot;Possibly Unwanted&quot; phishing emails as Phishing.Heuristics.Email.*<br />
 Default: yes</p>
<dt><code>PhishingAlwaysBlockCloak BOOL</code></p>
<dd>Always block cloaked URLs, even if URL isn&#8217;t in database. This can lead to false positives.<br />
 Default: no</p>
<dt><code>PhishingAlwaysBlockSSLMismatch BOOL</code></p>
<dd>Always block SSL mismatches in URLs, even if the URL isn&#8217;t in the database. This can lead to false positives.<br />
 Default: no</p>
<dt><code>PartitionIntersection BOOL</code></p>
<dd>Detect partition intersections in raw disk images using heuristics.<br />
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
<dt><code>ScanHTML BOOL</code></p>
<dd>Perform HTML/JavaScript/ScriptEncoder normalisation and decryption.<br />
 If you turn off this option, the original files will still be scanned, but without additional processing.<br />
 Default: yes</p>
<dt><code>ScanOLE2 BOOL</code></p>
<dd>This option enables scanning of OLE2 files, such as Microsoft Office documents and .msi files.<br />
 If you turn off this option, the original files will still be scanned, but without additional processing.<br />
 Default: yes</p>
<dt><code>OLE2BlockMacros BOOL</code></p>
<dd>With this option enabled OLE2 files with VBA macros, which were not detected by signatures will be marked as &quot;Heuristics.OLE2.ContainsMacros&quot;.<br />
 Default: no</p>
<dt><code>ScanPDF BOOL</code></p>
<dd>This option enables scanning within PDF files.<br />
 If you turn off this option, the original files will still be scanned, but without additional processing.<br />
 Default: yes</p>
<dt><code>ScanSWF BOOL</code></p>
<dd>This option enables scanning within SWF files.<br />
 If you turn off this option, the original files will still be scanned, but without decoding and additional processing.<br />
 Default: yes</p>
<dt><code>ScanXMLDOCS BOOL</code></p>
<dd>This option enables scanning xml-based document files supported by libclamav.<br />
 If you turn off this option, the original files will still be scanned, but without additional processing.<br />
 Default: yes</p>
<dt><code>ScanHWP3 BOOL</code></p>
<dd>This option enables scanning HWP3 files.<br />
 If you turn off this option, the original files will still be scanned, but without additional processing.<br />
 Default: yes</p>
<dt><code>ScanArchive BOOL</code></p>
<dd>Scan within archives and compressed files.<br />
 If you turn off this option, the original files will still be scanned, but without unpacking and additional processing.<br />
 Default: yes</p>
<dt><code>ArchiveBlockEncrypted BOOL</code></p>
<dd>Mark encrypted archives as viruses (Encrypted.Zip, Encrypted.RAR).<br />
 Default: no</p>
<dt><code>ForceToDisk</code></p>
<dd>This option causes memory or nested map scans to dump the content to disk.<br />
 If you turn on this option, more data is written to disk and is available when the leave-temps option is enabled at the cost of more disk writes.<br />
 Default: no<br />
 Default: no</p>
<dt><code>MaxScanSize SIZE</code></p>
<dd>Sets the maximum amount of data to be scanned for each input file. Archives and other containers are recursively extracted and scanned up to this value. The size of an archive plus the sum of the sizes of all files within archive count toward the scan size. For example, a 1M uncompressed archive containing a single 1M inner file counts as 2M toward the max scan size. <code>Warning: disabling this limit or setting it too high may result in severe damage to the system.</code><br />
 Default: 100M</p>
<dt><code>MaxFileSize SIZE</code></p>
<dd>Files larger than this limit won&#8217;t be scanned. Affects the input file itself as well as files contained inside it (when the input file is an archive, a document or some other kind of container). <code>Warning: disabling this limit or setting it too high may result in severe damage to the system.</code><br />
 Default: 25M</p>
<dt><code>MaxRecursion NUMBER</code></p>
<dd>Nested archives are scanned recursively, e.g. if a Zip archive contains a RAR file, all files within it will also be scanned. This options specifies how deeply the process should be continued. <code>Warning: setting this limit too high may result in severe damage to the system.</code><br />
 Default: 16</p>
<dt><code>MaxFiles NUMBER</code></p>
<dd>Number of files to be scanned within an archive, a document, or any other kind of container. <code>Warning: disabling this limit or setting it too high may result in severe damage to the system.</code><br />
 Default: 10000</p>
<dt><code>MaxEmbeddedPE SIZE</code></p>
<dd>This option sets the maximum size of a file to check for embedded PE.<br />
 Files larger than this value will skip the additional analysis step.<br />
 Negative values are not allowed.<br />
 Default: 10M</p>
<dt><code>MaxHTMLNormalize SIZE</code></p>
<dd>This option sets the maximum size of a HTML file to normalize.<br />
 HTML files larger than this value will not be normalized or scanned.<br />
 Negative values are not allowed.<br />
 Default: 10M</p>
<dt><code>MaxHTMLNoTags SIZE</code></p>
<dd>This option sets the maximum size of a normalized HTML file to scan.<br />
 HTML files larger than this value after normalization will not be scanned.<br />
 Negative values are not allowed.<br />
 Default: 2M</p>
<dt><code>MaxScriptNormalize SIZE</code></p>
<dd>This option sets the maximum size of a script file to normalize.<br />
 Script content larger than this value will not be normalized or scanned.<br />
 Negative values are not allowed.<br />
 Default: 5M</p>
<dt><code>MaxZipTypeRcg SIZE</code></p>
<dd>This option sets the maximum size of a ZIP file to reanalyze type recognition.<br />
 ZIP files larger than this value will skip the step to potentially reanalyze as PE.<br />
 Negative values are not allowed.<br />
 WARNING: setting this limit too high may result in severe damage or impact performance.<br />
 Default: 1M</p>
<dt><code>MaxPartitions SIZE</code></p>
<dd>This option sets the maximum number of partitions of a raw disk image to be scanned.<br />
 Raw disk images with more partitions than this value will have up to the value partitions scanned.<br />
 Negative values are not allowed.<br />
 WARNING: setting this limit too high may result in severe damage or impact performance.<br />
 Default: 50</p>
<dt><code>MaxIconsPE SIZE</code></p>
<dd>This option sets the maximum number of icons within a PE to be scanned.<br />
 PE files with more icons than this value will have up to the value number icons scanned.<br />
 Negative values are not allowed.<br />
 WARNING: setting this limit too high may result in severe damage or impact performance.<br />
 Default: 100</p>
<dt><code>MaxRecHWP3 NUMBER</code></p>
<dd>This option sets the maximum recursive calls to HWP3 parsing function.<br />
 HWP3 files using more than this limit will be terminated and alert the user.<br />
 Scans will be unable to scan any HWP3 attachments if the recursive limit is reached.<br />
 Negative values are not allowed.<br />
 WARNING: setting this limit too high may result in severe damage or impact performance.<br />
 Default: 16</p>
<dt><code>PCREMatchLimit NUMBER</code></p>
<dd>This option sets the maximum calls to the PCRE match function during an instance of regex matching.<br />
 Instances using more than this limit will be terminated and alert the user but the scan will continue.<br />
 For more information on match_limit, see the PCRE documentation.<br />
 Negative values are not allowed.<br />
 WARNING: setting this limit too high may severely impact performance.<br />
 Default: 10000</p>
<dt><code>PCRERecMatchLimit NUMBER</code></p>
<dd>This option sets the maximum recursive calls to the PCRE match function during an instance of regex matching.<br />
 Instances using more than this limit will be terminated and alert the user but the scan will continue.<br />
 For more information on match_limit_recursion, see the PCRE documentation.<br />
 Negative values are not allowed and values &gt; PCREMatchLimit are superfluous.<br />
 WARNING: setting this limit too high may severely impact performance.<br />
 Default: 5000</p>
<dt><code>PCREMaxFileSize SIZE</code></p>
<dd>This option sets the maximum filesize for which PCRE subsigs will be executed.<br />
 Files exceeding this limit will not have PCRE subsigs executed unless a subsig is encompassed to a smaller buffer.<br />
 Negative values are not allowed.<br />
 Setting this value to zero disables the limit.<br />
 WARNING: setting this limit too high or disabling it may severely impact performance.<br />
 Default: 25M</p>
<dt><code>ScanOnAccess BOOL</code></p>
<dd>This option enables on-access scanning (Linux only)<br />
 Default: disabled</p>
<dt><code>OnAccessIncludePath STRING</code></p>
<dd>This option specifies a directory (including all files and directories inside it), which should be scanned on access. This option can be used multiple times.<br />
 Default: disabled</p>
<dt><code>OnAccessExcludePath STRING</code></p>
<dd>This option allows excluding directories from on-access scanning. It can be used multiple times.<br />
 Default: disabled</p>
<dt><code>OnAccessExcludeUID NUMBER</code></p>
<dd>With this option you can whitelist specific UIDs. Processes with these UIDs will be able to access all files.<br />
 This option can be used multiple times (one per line).<br />
 Default: disabled</p>
<dt><code>OnAccessMaxFileSize SIZE</code></p>
<dd>Files larger than this value will not be scanned in on access.<br />
 Default: 5M</p>
<dt><code>OnAccessMountPath STRING</code></p>
<dd>Specifies a mount point (including all files and directories under it), which should be scanned on access. This option can be used multiple times.<br />
 Default: disabled</p>
<dt><code>OnAccessDisableDDD BOOL</code></p>
<dd>Disables the dynamic directory determination system which allows for recursively watching include paths.<br />
 Default: no</p>
<dt><code>OnAccessPrevention BOOL</code></p>
<dd>Enables fanotify blocking when malicious files are found.<br />
 Default: disabled</p>
<dt><code>DisableCertCheck BOOL</code></p>
<dd>Disable authenticode certificate chain verification in PE files.<br />
 Default: no</p>
<dt><code>StatsEnabled BOOL</code></p>
<dd>Enable submission of statistical data<br />
 Default: no</p>
<dt><code>StatsHostID STRING</code></p>
<dd>HostID in the form of an UUID to use when submitting statistical information.<br />
 Default: auto</p>
<dt><code>StatsPEDisabled BOOL</code></p>
<dd>Disable submission of PE section statistical data.<br />
 Default: no</p>
<dt><code>StatsTimeout NUMBER</code></p>
<dd>Timeout in seconds to timeout communication with the stats server.<br />
 Default: 10</dl>
<h2>Notes</h2>
<p>All options expressing a size are limited to max 4GB. Values in excess will be resetted to the maximum.</p>
<h2>Files</h2>
<p>/etc/clamd.conf</p>
<h2>Authors</h2>
<p>Tomasz Kojm &lt;tkojm [at] clamav.net&gt;, Kevin Lin &lt;klin [at] sourcefire.com&gt;</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-clamd/">clamd</a>(8), <a href="/docs/linux/man/1-clamdscan/">clamdscan</a>(1), <a href="/docs/linux/man/8-clamav-milter/">clamav-milter</a>(8), <a href="/docs/linux/man/1-freshclam/">freshclam</a>(1), <a href="/docs/linux/man/5-freshclam-conf/">freshclam.conf</a>(5) </p>
