---
title: "clamscan(1)"
name: "clamscan"
section: "1"
letter: "c"
url: "/docs/linux/man/1-clamscan/"
description: "clamscan – scan files and directories for viruses"
---

<h2>NAME</h2>
<p> clamscan &#8211; scan files and directories for viruses</p>
<h2>SYNOPSIS</h2>
<p> clamscan [options] [file/directory/-]</p>
<h2>DESCRIPTION</h2>
<p> clamscan is a command line anti-virus scanner.</p>
<h2>OPTIONS</h2>
<p> Most of the options are simple switches which enable or disable some features. Options marked with [=yes/no(*)] can be optionally followed by =yes/=no; if they get called without the boolean argument the scanner will assume &#8216;yes&#8217;. The asterisk marks the default internal setting for a given option.</p>
<dl>
<dt><code>-h, &#8211;help</code></p>
<dd> Print help information and exit.</p>
<dt><code>-V, &#8211;version</code></p>
<dd> Print version number and exit.</p>
<dt><code>-v, &#8211;verbose</code></p>
<dd> Be verbose.</p>
<dt><code>-a, &#8211;archive-verbose</code></p>
<dd> Show filenames inside scanned archives</p>
<dt><code>&#8211;debug</code></p>
<dd> Display debug messages from libclamav.</p>
<dt><code>&#8211;quiet</code></p>
<dd> Be quiet (only print error messages).</p>
<dt><code>&#8211;stdout</code></p>
<dd> Write all messages (except for libclamav output) to the standard output (stdout).</p>
<dt><code>&#8211;no-summary</code></p>
<dd> Do not display summary at the end of scanning.</p>
<dt><code>-i, &#8211;infected</code></p>
<dd> Only print infected files.</p>
<dt><code>-o, &#8211;suppress-ok-results</code></p>
<dd> Skip printing OK files</p>
<dt><code>&#8211;bell</code></p>
<dd> Sound bell on virus detection.</p>
<dt><code>&#8211;tempdir=DIRECTORY</code></p>
<dd> Create temporary files in DIRECTORY. Directory must be writable for the &#8221; user or unprivileged user running clamscan.</p>
<dt><code>&#8211;leave-temps</code></p>
<dd> Do not remove temporary files.</p>
<dt><code>-d FILE/DIR, &#8211;database=FILE/DIR</code></p>
<dd> Load virus database from FILE or load all virus database files from DIR.</p>
<dt><code>&#8211;official-db-only=[yes/no(*)]</code></p>
<dd> Only load the official signatures published by the ClamAV project.</p>
<dt><code>-l FILE, &#8211;log=FILE</code></p>
<dd> Save scan report to FILE.</p>
<dt><code>-r, &#8211;recursive</code></p>
<dd> Scan directories recursively. All the subdirectories in the given directory will be scanned.</p>
<dt><code>-z, &#8211;allmatch</code></p>
<dd> After a match, continue scanning within the file for additional matches.</p>
<dt><code>&#8211;cross-fs=[yes(*)/no]</code></p>
<dd> Scan files and directories on other filesystems.</p>
<dt><code>&#8211;follow-dir-symlinks=[0/1(*)/2]</code></p>
<dd> Follow directory symlinks. There are 3 options: 0 &#8211; never follow directory symlinks, 1 (default) &#8211; only follow directory symlinks, which are passed as direct arguments to clamscan. 2 &#8211; always follow directory symlinks.</p>
<dt><code>&#8211;follow-file-symlinks=[0/1(*)/2]</code></p>
<dd> Follow file symlinks. There are 3 options: 0 &#8211; never follow file symlinks, 1 (default) &#8211; only follow file symlinks, which are passed as direct arguments to clamscan. 2 &#8211; always follow file symlinks.</p>
<dt><code>-f FILE, &#8211;file-list=FILE</code></p>
<dd> Scan files listed line by line in FILE.</p>
<dt><code>&#8211;remove[=yes/no(*)]</code></p>
<dd> Remove infected files. <code>Be careful!</code></p>
<dt><code>&#8211;move=DIRECTORY</code></p>
<dd> Move infected files into DIRECTORY. Directory must be writable for the &#8221; user or unprivileged user running clamscan.</p>
<dt><code>&#8211;copy=DIRECTORY</code></p>
<dd> Copy infected files into DIRECTORY. Directory must be writable for the &#8221; user or unprivileged user running clamscan.</p>
<dt><code>&#8211;exclude=REGEX, &#8211;exclude-dir=REGEX</code></p>
<dd> Don&#8217;t scan file/directory names matching regular expression. These options can be used multiple times.</p>
<dt><code>&#8211;include=REGEX, &#8211;include-dir=REGEX</code></p>
<dd> Only scan file/directory matching regular expression. These options can be used multiple times.</p>
<dt><code>&#8211;bytecode[=yes(*)/no]</code></p>
<dd> With this option enabled ClamAV will load bytecode from the database. It is highly recommended you keep this option turned on, otherwise you may miss detections for many new viruses.</p>
<dt><code>&#8211;bytecode-unsigned[=yes/no(*)]</code></p>
<dd> Allow loading bytecode from outside digitally signed .c[lv]d files.</p>
<dt><code>&#8211;bytecode-timeout=N</code></p>
<dd> Set bytecode timeout in milliseconds (default: 60000 = 60s)</p>
<dt><code>&#8211;statistics[=none(*)/bytecode/pcre]</code></p>
<dd> Collect and print execution statistics.</p>
<dt><code>&#8211;detect-pua[=yes/no(*)]</code></p>
<dd> Detect Possibly Unwanted Applications.</p>
<dt><code>&#8211;exclude-pua=CATEGORY</code></p>
<dd> Exclude a specific PUA category. This option can be used multiple times. See <a rel="nofollow" href="http://www.clamav.net/doc/pua.html">http://www.clamav.net/doc/pua.html</a> for the complete list of PUA</p>
<dt><code>&#8211;include-pua=CATEGORY</code></p>
<dd> Only include a specific PUA category. This option can be used multiple times. See <a rel="nofollow" href="http://www.clamav.net/doc/pua.html">http://www.clamav.net/doc/pua.html</a> for the complete list of PUA</p>
<dt><code>&#8211;detect-structured[=yes/no(*)]</code></p>
<dd> Use the DLP (Data Loss Prevention) module to detect SSN and Credit Card numbers inside documents/text files.</p>
<dt><code>&#8211;structured-ssn-format=X</code></p>
<dd> X=0: search for valid SSNs formatted as xxx-yy-zzzz (normal); X=1: search for valid SSNs formatted as xxxyyzzzz (stripped); X=2: search for both formats. Default is 0.</p>
<dt><code>&#8211;structured-ssn-count=#n</code></p>
<dd> This option sets the lowest number of Social Security Numbers found in a file to generate a detect (default: 3).</p>
<dt><code>&#8211;structured-cc-count=#n</code></p>
<dd> This option sets the lowest number of Credit Card numbers found in a file to generate a detect (default: 3).</p>
<dt><code>&#8211;scan-mail[=yes(*)/no]</code></p>
<dd> Scan mail files. If you turn off this option, the original files will still be scanned, but without parsing individual messages/attachments.</p>
<dt><code>&#8211;phishing-sigs[=yes(*)/no]</code></p>
<dd> Use the signature-based phishing detection.</p>
<dt><code>&#8211;phishing-scan-urls[=yes(*)/no]</code></p>
<dd> Use the url-based heuristic phishing detection (Phishing.Heuristics.Email.*)</p>
<dt><code>&#8211;heuristic-scan-precedence[=yes/no(*)]</code></p>
<dd> Allow heuristic match to take precedence. When enabled, if a heuristic scan (such as phishingScan) detects a possible virus/phish it will stop scan immediately. Recommended, saves CPU scan-time. When disabled, virus/phish detected by heuristic scans will be reported only at the end of a scan. If an archive contains both a heuristically detected virus/phish, and a real malware, the real malware will be reported Keep this disabled if you intend to handle &quot;*.Heuristics.*&quot; viruses differently from &quot;real&quot; malware. If a non-heuristically-detected virus (signature-based) is found first, the scan is interrupted immediately, regardless of this config option.</p>
<dt><code>&#8211;phishing-ssl[=yes/no(*)]</code></p>
<dd> Block SSL mismatches in URLs (might lead to false positives!).</p>
<dt><code>&#8211;phishing-cloak[=yes/no(*)]</code></p>
<dd> Block cloaked URLs (might lead to some false positives).</p>
<dt><code>&#8211;partition-intersection[=yes/no(*)]</code></p>
<dd> Detect partition intersections in raw disk images using heuristics.</p>
<dt><code>&#8211;algorithmic-detection[=yes(*)/no]</code></p>
<dd> In some cases (eg. complex malware, exploits in graphic files, and others), ClamAV uses special algorithms to provide accurate detection. This option can be used to control the algorithmic detection.</p>
<dt><code>&#8211;scan-pe[=yes(*)/no]</code></p>
<dd> PE stands for Portable Executable &#8211; it&#8217;s an executable file format used in all 32-bit versions of Windows operating systems. By default ClamAV performs deeper analysis of executable files and attempts to decompress popular executable packers such as UPX, Petite, and FSG. If you turn off this option, the original files will still be scanned but without additional processing.</p>
<dt><code>&#8211;scan-elf[=yes(*)/no]</code></p>
<dd> Executable and Linking Format is a standard format for UN*X executables. This option controls the ELF support. If you turn it off, the original files will still be scanned but without additional processing.</p>
<dt><code>&#8211;scan-ole2[=yes(*)/no]</code></p>
<dd> Scan Microsoft Office documents and .msi files. If you turn off this option, the original files will still be scanned but without additional processing.</p>
<dt><code>&#8211;scan-pdf[=yes(*)/no]</code></p>
<dd> Scan within PDF files. If you turn off this option, the original files will still be scanned, but without decoding and additional processing.</p>
<dt><code>&#8211;scan-swf[=yes(*)/no]</code></p>
<dd> Scan SWF files. If you turn off this option, the original files will still be scanned but without additional processing.</p>
<dt><code>&#8211;scan-html[=yes(*)/no]</code></p>
<dd> Detect, normalize/decrypt and scan HTML files and embedded scripts. If you turn off this option, the original files will still be scanned, but without additional processing.</p>
<dt><code>&#8211;scan-xmldocs[=yes(*)/no]</code></p>
<dd> Scan xml-based document files supported by libclamav. If you turn off this option, the original files will still be scanned, but without additional processing.</p>
<dt><code>&#8211;scan-hwp3[=yes(*)/no]</code></p>
<dd> Scan HWP3 files. If you turn off this option, the original files will still be scanned, but without additional processing.</p>
<dt><code>&#8211;scan-archive[=yes(*)/no]</code></p>
<dd> Scan archives supported by libclamav. If you turn off this option, the original files will still be scanned, but without unpacking and additional processing.</p>
<dt><code>&#8211;detect-broken[=yes/no(*)]</code></p>
<dd> Mark broken executables as viruses (Broken.Executable).</p>
<dt><code>&#8211;block-encrypted[=yes/no(*)]</code></p>
<dd> Mark encrypted archives as viruses (Encrypted.Zip, Encrypted.RAR).</p>
<dt><code>&#8211;block-macros[=yes/no(*)]</code></p>
<dd> Mark OLE2 files containing VBA macros as viruses (Heuristics.OLE2.ContainsMacros).</p>
<dt><code>&#8211;max-filesize=#n</code></p>
<dd> Extract and scan at most #n bytes from each archive. You may pass the value in kilobytes in format xK or xk, or megabytes in format xM or xm, where x is a number. This option protects your system against DoS attacks (default: 25 MB, max: &lt;4 GB)</p>
<dt><code>&#8211;max-scansize=#n</code></p>
<dd> Extract and scan at most #n bytes from each archive. The size the archive plus the sum of the sizes of all files within archive count toward the scan size. For example, a 1M uncompressed archive containing a single 1M inner file counts as 2M toward max-scansize. You may pass the value in kilobytes in format xK or xk, or megabytes in format xM or xm, where x is a number. This option protects your system against DoS attacks (default: 100 MB, max: &lt;4 GB)</p>
<dt><code>&#8211;max-files=#n</code></p>
<dd> Extract at most #n files from each scanned file (when this is an archive, a document or another kind of container). This option protects your system against DoS attacks (default: 10000)</p>
<dt><code>&#8211;max-recursion=#n</code></p>
<dd> Set archive recursion level limit. This option protects your system against DoS attacks (default: 16).</p>
<dt><code>&#8211;max-dir-recursion=#n</code></p>
<dd> Maximum depth directories are scanned at (default: 15). </p>
<dt><code>&#8211;max-embeddedpe=#n</code></p>
<dd> Maximum size file to check for embedded PE. You may pass the value in kilobytes in format xK or xk, or megabytes in format xM or xm, where x is a number (default: 10 MB, max: &lt;4 GB).</p>
<dt><code>&#8211;max-htmlnormalize=#n</code></p>
<dd> Maximum size of HTML file to normalize. You may pass the value in kilobytes in format xK or xk, or megabytes in format xM or xm, where x is a number (default: 10 MB, max: &lt;4 GB).</p>
<dt><code>&#8211;max-htmlnotags=#n</code></p>
<dd> Maximum size of normalized HTML file to scan. You may pass the value in kilobytes in format xK or xk, or megabytes in format xM or xm, where x is a number (default: 2 MB, max: &lt;4 GB).</p>
<dt><code>&#8211;max-scriptnormalize=#n</code></p>
<dd> Maximum size of script file to normalize. You may pass the value in kilobytes in format xK or xk, or megabytes in format xM or xm, where x is a number (default: 5 MB, max: &lt;4 GB).</p>
<dt><code>&#8211;max-ziptypercg=#n</code></p>
<dd> Maximum size zip to type reanalyze. You may pass the value in kilobytes in format xK or xk, or megabytes in format xM or xm, where x is a number (default: 1 MB, max: &lt;4 GB).</p>
<dt><code>&#8211;max-partitions=#n</code></p>
<dd> This option sets the maximum number of partitions of a raw disk image to be scanned. This must be a positive integer (default: 50).</p>
<dt><code>&#8211;max-iconspe=#n</code></p>
<dd> This option sets the maximum number of icons within a PE to be scanned. This must be a positive integer (default: 100).</p>
<dt><code>&#8211;max-rechwp3=#n</code></p>
<dd> This option sets the maximum recursive calls to HWP3 parsing function (default: 16).</p>
<dt><code>&#8211;pcre-match-limit=#n</code></p>
<dd> Maximum calls to the PCRE match function (default: 10000).</p>
<dt><code>&#8211;pcre-recmatch-limit=#n</code></p>
<dd> Maximum recursive calls to the PCRE match function (default: 5000).</p>
<dt><code>&#8211;pcre-max-filesize=#n</code></p>
<dd> Maximum size file to perform PCRE subsig matching (default: 25 MB, max: &lt;4 GB).</p>
<dt><code>&#8211;enable-stats</code></p>
<dd> This option enables submission of statistical data. (Default: stats submissions disabled)</p>
<dt><code>&#8211;stats-host-id</code></p>
<dd> This option sets the HostID, in the form of an UUID, to use when submitting statistical information.</p>
<dt><code>&#8211;disable-pe-stats</code></p>
<dd> This option disables the submission of PE section data. (Default: submitting of PE section data enabled if stats submissions as a whole is enabled).</p>
<dt><code>&#8211;stats-timeout=#n</code></p>
<dd> This option sets the timeout in seconds to wait for communication back from the stats server. (Default: 10).</p>
<dt><code>&#8211;disable-cache</code></p>
<dd> Disable caching and cache checks for hash sums of scanned files.</dl>
<h2>EXAMPLES</h2>
<dl>
<dt>(0) Scan a single file:</p>
<dd>
<p> <code>clamscan file</code></p>
<dt>(1) Scan a current working directory:</p>
<dd>
<p> <code>clamscan</code></p>
<dt>(2) Scan all files (and subdirectories) in /home:</p>
<dd>
<p> <code>clamscan -r /home</code></p>
<dt>(3) Load database from a file:</p>
<dd>
<p> <code>clamscan -d /tmp/newclamdb -r /tmp</code></p>
<dt>(4) Scan a data stream:</p>
<dd>
<p> <code>cat testfile | clamscan &#8211;</code></p>
<dt>(5) Scan a mail spool directory:</p>
<dd>
<p> <code>clamscan -r /var/spool/mail</code></dl>
<h2>RETURN CODES</h2>
<p> 0 : No virus found.</p>
<dl>
<dt>1 : Virus(es) found.</p>
<dd>
<dt>2 : Some error(s) occured.</p>
<dd></dl>
<h2>CREDITS</h2>
<p> Please check the full documentation for credits.</p>
<h2>AUTHOR</h2>
<p> Tomasz Kojm &lt;tkojm [at] clamav.net&gt;, Kevin Lin &lt;klin [at] sourcefire.com&gt;</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-clamdscan/">clamdscan</a>(1), <a href="/docs/linux/man/1-freshclam/">freshclam</a>(1), <a href="/docs/linux/man/5-freshclam-conf/">freshclam.conf</a>(5) </p>
<h2>Index</h2>
