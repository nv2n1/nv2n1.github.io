---

title: "globus-url-copy(1)"
name: "globus-url-copy"
section: "1"
letter: "g"
url: "/docs/linux/man/1-globus-url-copy/"
description: "globus-url-copy – globus-url-copy"
---

<p> <code>globus-url-copy</code> [options] SOURCE-URL DESTINATION-URL</p>
<p> The <code>globus-url-copy</code> program is a command line tool for multi-protocol data movement. It supports gsiftp:// (GridFTP), <a href="ftp://,">ftp://,</a> <a rel="nofollow" href="http://,">http://,</a> <a href="https://,">https://,</a> sshftp:// and file:/// protocol specifiers in the URL.</p>
<h2>OPTIONS</h2>
<p> <code>-help, -usage</code></p>
<dl>
<dt>
</dt><dd> Print help.</dd></dl>
<p> <code>-versions</code></p>
<dl>
<dt>
</dt><dd> Print the versions of all modules that this program uses</dd></dl>
<p> <code>-c, -continue-on-error</code></p>
<dl>
<dt>
</dt><dd> Do not die after any errors. By default, program will exit after most errors.</dd></dl>
<p> <code>-a, -ascii</code></p>
<dl>
<dt>
</dt><dd> Convert the file to/from ASCII format to/from local file format</dd></dl>
<p> <code>-b, -binary</code></p>
<dl>
<dt>
</dt><dd> Do not apply any conversion to the files. <code>default</code></dd></dl>
<p> <code>-f FILENAME</code></p>
<dl>
<dt>
</dt><dd> Read a list of URL pairs from filename. Each line should contain sourceURL destURL. Enclose URLs with spaces in double qoutes (&quot;). Blank lines and lines beginning with # will be ignored.</dd></dl>
<p> <code>-cd, -create-dest</code></p>
<dl>
<dt>
</dt><dd> Create destination directory if needed.</dd></dl>
<p> <code>-r</code></p>
<dl>
<dt>
</dt><dd> Copy files in subdirectories</dd></dl>
<p> <code>-fast</code></p>
<dl>
<dt>
</dt><dd> Recommended when using GridFTP servers. Use MODE E for all data transfers, including reusing data channels between list and transfer operations.</dd></dl>
<p> <code>-t SECONDS</code></p>
<dl>
<dt>
</dt><dd> Run the transfer for this number of seconds and then end. Useful for performance testing or forced restart loops.</dd></dl>
<p> <code>-q, -quiet</code></p>
<dl>
<dt>
</dt><dd> Suppress all output for successful operation.</dd></dl>
<p> <code>-v, -verbose</code></p>
<dl>
<dt>
</dt><dd> Display URLs being transferred</dd></dl>
<p> <code>-vb, -verbose-perf</code></p>
<dl>
<dt>
</dt><dd> During the transfer, display the number of bytes transferred and the transfer rate per second. Show URLs being transferred</dd></dl>
<p> <code>-dbg, -debugftp</code></p>
<dl>
<dt>
</dt><dd> Debug ftp connections. Prints control channel communication to stderr</dd></dl>
<p> <code>-rst, -restart</code></p>
<dl>
<dt>
</dt><dd> Restart failed ftp operations.</dd></dl>
<p> <code>-rst-retries RETRIES</code></p>
<dl>
<dt>
</dt><dd> The maximum number of times to retry the operation before giving up on the transfer. Use 0 for infinite. Default is 5.</dd></dl>
<p> <code>-rst-interval SECONDS</code></p>
<dl>
<dt>
</dt><dd> The interval in seconds to wait after a failure before retrying the transfer. Use 0 for an exponential backoff. Default is 0.</dd></dl>
<p> <code>-rst-timeout SECONDS</code></p>
<dl>
<dt>
</dt><dd> Maximum time after a failure to keep retrying. Use 0 for no timeout. Default is 0.</dd></dl>
<p> <code>-stall-timeout SECONDS, -st SECONDS</code></p>
<dl>
<dt>
</dt><dd> How long before cancelling/restarting a transfer with no data movement. Set to 0 to disable. Default is 600 seconds.</dd></dl>
<p> <code>-df FILENAME, -dumpfile FILENAME</code></p>
<dl>
<dt>
</dt><dd> Path to a file where untransferred URLs will be saved for later restarting. Resulting file is the same format as the -f input file. If file exists, it will be read and all other URL input will be ignored.</dd></dl>
<p> <code>-do FILENAME, -dump-only FILENAME</code></p>
<dl>
<dt>
</dt><dd> Perform no write operations on the destination. Instead, all files that would be transferred are enumerated and dumped to the specified file. Resulting file is the same format as the -f input file. Note: if you intend to use this file as input for a future transfer, the -create-dest option will be required if any destination directories do not already exist.</dd></dl>
<p> <code>-rp, -relative-paths</code></p>
<dl>
<dt>
</dt><dd> The path portion of ftp URLs will be interpreted as relative to the user&#8217;s starting directory on the server. By default, all paths are root-relative. When this flag is set, the path portion of the ftp URL must start with %2F if it designates a root-relative path.</dd></dl>
<p> <code>-s SUBJECT, -subject SUBJECT</code></p>
<dl>
<dt>
</dt><dd> Use this subject to match with both the source and dest servers.</dd></dl>
<p> <code>-ss SUBJECT, -source-subject SUBJECT</code></p>
<dl>
<dt>
</dt><dd> Use this subject to match with the source server</dd></dl>
<p> <code>-ds SUBJECT, -dest-subject SUBJECT</code></p>
<dl>
<dt>
</dt><dd> Use this subject to match with the destination server.</dd></dl>
<p> <code>-tcp-bs SIZE, -tcp-buffer-size SIZE</code></p>
<dl>
<dt>
</dt><dd> Specify the size (in bytes) of the buffer to be used by the underlying ftp data channels.</dd></dl>
<p> <code>-bs block SIZE, -block-size block SIZE</code></p>
<dl>
<dt>
</dt><dd> Specify the size (in bytes) of the buffer to be used by the underlying transfer methods.</dd></dl>
<p> <code>-p PARALLELISM, -parallel PARALLELISM</code></p>
<dl>
<dt>
</dt><dd> Specify the number of parallel data connections should be used.</dd></dl>
<p> <code>-notpt, -no-third-party-transfers</code></p>
<dl>
<dt>
</dt><dd> Turn third-party transfers off (on by default).</dd></dl>
<p> <code>-nodcau, -no-data-channel-authentication</code></p>
<dl>
<dt>
</dt><dd> Turn off data channel authentication for ftp transfers.</dd></dl>
<p> <code>-dcsafe, -data-channel-safe</code></p>
<dl>
<dt>
</dt><dd> Set data channel protection mode to SAFE</dd></dl>
<p> <code>-dcpriv, -data-channel-private</code></p>
<dl>
<dt>
</dt><dd> Set data channel protection mode to PRIVATE</dd></dl>
<p> <code>-off, -partial-offset</code></p>
<dl>
<dt>
</dt><dd> Offset for partial ftp file transfers, defaults to 0.</dd></dl>
<p> <code>-len, -partial-length</code></p>
<dl>
<dt>
</dt><dd> Length for partial ftp file transfers, used only for the source url, defaults the full file.</dd></dl>
<p> <code>-list URL</code></p>
<dl>
<dt>
</dt><dd> List the files located at URL.</dd></dl>
<p> <code>-stripe</code></p>
<dl>
<dt>
</dt><dd> Enable striped transfers on supported servers.</dd></dl>
<p> <code>-striped-block-size, -sbs</code></p>
<dl>
<dt>
</dt><dd> Set layout mode and block size for striped transfers. If not set, server defaults will be used. If set to 0, Partitioned mode will be used. If set to &gt; 0, Blocked mode will be used, with this as the block size.</dd></dl>
<p> <code>-ipv6</code></p>
<dl>
<dt>
</dt><dd> Use ipv6 when available (EXPERIMENTAL)</dd></dl>
<p> <code>-udt</code></p>
<dl>
<dt>
</dt><dd> Use UDT, a reliable udp based transport protocol, for data transfers</dd></dl>
<p> <code>-g2, -gridftp2</code></p>
<dl>
<dt>
</dt><dd> Use GridFTP v2 protocol enhancements when possible.</dd></dl>
<p> <code>-dp, -delayed-pasv</code></p>
<dl>
<dt>
</dt><dd> Enable delayed passive.</dd></dl>
<p> <code>-mn NAME, -module-name NAME</code></p>
<dl>
<dt>
</dt><dd> Set the back-end storage module to use for both the source and destination in a GridFTP transfer.</dd></dl>
<p> <code>-mp PARAMETERS, -module-parameters PARAMETERS</code></p>
<dl>
<dt>
</dt><dd> Set the back-end storage module arguments to use for both the source and destination in a GridFTP transfer.</dd></dl>
<p> <code>-smn NAME, -src-module-name NAME</code></p>
<dl>
<dt>
</dt><dd> Set the back-end storage module to use for the source in a GridFTP transfer.</dd></dl>
<p> <code>-smp PARAMETERS, -src-module-parameters PARAMETERS</code></p>
<dl>
<dt>
</dt><dd> Set the back-end storage module arguments to use for the source in a GridFTP transfer.</dd></dl>
<p> <code>-dmn NAME, -dst-module-name NAME</code></p>
<dl>
<dt>
</dt><dd> Set the back-end storage module to use for the destination in a GridFTP transfer.</dd></dl>
<p> <code>-dmp PARAMETERS, -dst-module-parameters PARAMETERS</code></p>
<dl>
<dt>
</dt><dd> Set the back-end storage module arguments to use for the destination in a GridFTP transfer.</dd></dl>
<p> <code>-aa FILE, -authz-assert FILE</code></p>
<dl>
<dt>
</dt><dd> Use the assertions in FILE to authorize the access with both source and destination servers.</dd></dl>
<p> <code>-saa FILE, -src-authz-assert FILE</code></p>
<dl>
<dt>
</dt><dd> Use the assertions in this file to authorize the access with source server.</dd></dl>
<p> <code>-daa FILE, -dst-authz-assert FILE</code></p>
<dl>
<dt>
</dt><dd> Use the assertions in this file to authorize the access with dest server.</dd></dl>
<p> <code>-cache-aa, -cache-authz-assert</code></p>
<dl>
<dt>
</dt><dd> Cache the authz assertion for subsequent transfers.</dd></dl>
<p> <code>-cache-saa, -cache-src-authz-assert</code></p>
<dl>
<dt>
</dt><dd> Cache the src authz assertion for subsequent transfers.</dd></dl>
<p> <code>-cache-daa, -cache-dst-authz-assert</code></p>
<dl>
<dt>
</dt><dd> Cache the dst authz assertion for subsequent transfers.</dd></dl>
<p> <code>-pipeline, -pp</code></p>
<dl>
<dt>
</dt><dd> Enable pipelining support for multi-file ftp transfers. Currently third-party transfers benefit from this. <code>EXPERIMENTAL</code></dd></dl>
<p> <code>-concurrency, -cc</code></p>
<dl>
<dt>
</dt><dd> Number of concurrent ftp connections to use for multiple transfers.</dd></dl>
<p> <code>-nl-bottleneck, -nlb</code></p>
<dl>
<dt>
</dt><dd> Use NetLogger to estimate speeds of disk and network read/write system calls, and attempt to determine the bottleneck component.</dd></dl>
<p> <code>-sp COMMANDS, -src-pipe COMMANDS</code></p>
<dl>
<dt>
</dt><dd> Set the source end of a remote transfer to use piped in input with the given command line. Do not use with -fsstack.</dd></dl>
<p> <code>-DP COMMANDS, -dst-pipe COMMANDS</code></p>
<dl>
<dt>
</dt><dd> Set the destination end of a remote transfer to write data to then standard input of the program run via the given command line. Do not use with -fsstack.</dd></dl>
<p> <code>-pipe COMMANDS</code></p>
<dl>
<dt>
</dt><dd> Sets both -src-pipe and -dst-pipe to the same thing.</dd></dl>
<p> <code>-dcstack STACK, -data-channel-stack STACK</code></p>
<dl>
<dt>
</dt><dd> Set the XIO driver stack for the network on both the source and the destination. Both must be GridFTP servers. The stack should contain all network drivers to use, in the order specified from bottom to top (e.g. -dcstack tcp,gsi). If the gsi driver is not included in the stack and data channel authentication is enabled, it will be inserted above the transport driver in the stack.</dd></dl>
<p> <code>-fsstack STACK, -file-system-stack STACK</code></p>
<dl>
<dt>
</dt><dd> Set the XIO driver stack for the disk on both the source and the destination. Both must be GridFTP servers. The stack should contain all file system drivers to use, in the order specified from bottom to top.</dd></dl>
<p> <code>-src-dcstack STACK, -source-data-channel-stack STACK</code></p>
<dl>
<dt>
</dt><dd> Set the XIO driver stack for the network on the source GridFTP server. See -dcstack above for description of the STACK string.</dd></dl>
<p> <code>-src-fsstack STACK, -source-file-system-stack STACK</code></p>
<dl>
<dt>
</dt><dd> Set the XIO driver stack for the disk on the source GridFTP server. See -fsstack above for description of the STACK string.</dd></dl>
<p> <code>-dst-dcstack STACK, -dest-data-channel-stack STACK</code></p>
<dl>
<dt>
</dt><dd> Set the XIO driver stack for the network on the destination GridFTP server. See -dcstack above for description of the STACK string.</dd></dl>
<p> <code>-dst-fsstack STACK, -dest-file-system-stack STACK</code></p>
<dl>
<dt>
</dt><dd> Set the XIO driver stack for the disk on the destination GridFTP server. See -fsstack above for description of the STACK string.</dd></dl>
<p> <code>-cred PATH</code></p>
<dl>
<dt>
</dt><dd> Set the credentials to use for both ftp connections.</dd></dl>
<p> <code>-src-cred CRED-FILE, -sc CRED-FILE</code></p>
<dl>
<dt>
</dt><dd> Set the credentials to use for source ftp connections.</dd></dl>
<p> <code>-dst-cred CRED-FILE, -dc CRED-FILE</code></p>
<dl>
<dt>
</dt><dd> Set the credentials to use for destination ftp connections.</dd></dl>
<p> <code>-af FILENAME, -alias-file FILENAME</code></p>
<dl>
<dt>
</dt><dd> File with mapping of logical host aliases to lists of physical hosts. When used with multiple concurrent connections, each connection uses the next host in the list. Each line should either be an alias, noted with the @ symbol, or a hostname[:port]. Currently, only the aliases @source and @destination are valid, and they are used for every source or destination URL.</dd></dl>
<p> <code>-sync</code></p>
<dl>
<dt>
</dt><dd> Only transfer files where the destination does not exist or differs from the source. -sync-level controls how to determine if files differ.</dd></dl>
<p> <code>-sync-level number</code></p>
<dl>
<dt>
</dt><dd> Criteria for determining if files differ when performing a sync transfer. The default sync level is 2. The available levels are: </dd>
<dl>
<dt>
</dt><dd> &bull; Level 0 will only transfer if the destination does not exist.</dd></dl>
<dl>
<dt>
</dt><dd> &bull; Level 1 will transfer if the size of the destination does not match the size of the source.</dd></dl>
<dl>
<dt>
</dt><dd> &bull; Level 2 will transfer if the time stamp of the destination is older than the time stamp of the source.</dd></dl>
<dl>
<dt>
</dt><dd> &bull; Level 3 will perform a checksum of the source and destination and transfer if the checksums do not match.</dd></dl>
</dl>
<h2>AUTHOR</h2>
<p> Copyright &#169; 1999-2016 University of Chicago </p>
