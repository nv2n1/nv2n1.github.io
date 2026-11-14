---
title: "nbd-server(5)"
name: "nbd-server"
section: "5"
letter: "n"
url: "/docs/linux/man/5-nbd-server/"
description: "/etc/nbd-server/config – configuration file for nbd-server"
---

<p>/etc/nbd-server/config &#8211; configuration file for nbd-server</p>
<h2>Synopsis</h2>
<p><code>/etc/nbd-server/config </code> </p>
<h2>Description</h2>
<p>This file allows to configure the nbd-server. </p>
<p> While <i>/etc/nbd-server/config</i> is the default configuration file, this can be varied with the <code>-C</code> option to <code><a href="/docs/linux/man/1-nbd-server/">nbd-server</a></code>(1). </p>
<p> The configuration file consists of section header lines, comment lines, and option lines. </p>
<p> A section header is a unique name that is enclosed in square brackets (&quot;[&quot; and &quot;]&quot;). A section header denotes the beginning of a section; a section continues until the next section or the end of the file, whichever is first. The first section in the configuration file must be called <code>generic</code>, and is used for global options that apply to more than one export. This section must always be present, even if it holds no options. Every other section defines one export; the names of these sections are not important, except that you should take care to make sure that each section name is unique. The section name is used as the name for the export in case the client connects with a name rather than a port to specify an export, and must therefore be unique. </p>
<p> A comment line is a line that starts with optional whitespace, followed by a pound sign (&quot;#&quot;), and continues until the end of the line. Comments may <code>not</code> be used on option lines or section header lines. </p>
<p> An option line is a line that starts with an option name, followed by an equals sign (&quot;=&quot;), followed by the option value. An option can be of type string, of type integer, or of type boolean. The value of a boolean option can be denoted with either true or false (so not yes, no, on, off, 1, or 0). All booleans default to false unless specified otherwise. No value may be quoted; always enter it directly. For a string option, leading whitespace is stripped (but trailing whitespace is not).</p>
<h2>Options For Section [Generic]</h2>
<dl>
<dt><code>allowlist</code></p>
<dd>Optional; boolean </p>
<p> Whether to allow the client to fetch a list of exports from this server. If enabled, the client can run <code>nbd-client -l</code> to get a list of exports on this server.</p>
<dt><code>group</code></p>
<dd>Optional; string. </p>
<p> The name of the group this server must run as. If this parameter is not specified, then nbd-server will not attempt to change its GID (so the GID it runs as will be the primary group of the user who starts nbd-server). If it is specified, then nbd-server will change its GID after opening ports, but before accepting connections or opening files.</p>
<dt><code>includedir</code></p>
<dd>Optional; string </p>
<p> The argument should be a directory containing files with the &#8216;.conf&#8217; extension; these files will be parsed as if they were part of the configuration file. Note that these extra configuration files cannot contain a [generic] section; any configuration that should go in the generic section must be placed in the main configuration file. </p>
<p> If this argument is not specified, then no directory will be searched. If it is specified but the directory does not exist, then nbd-server will exit with an appropriate error message; if it is specified but the given directory is empty, nbd-server will continue (unless no exports whatsoever have been configured, in which case it will exit with an appropriate error message)</p>
<dt><code>listenaddr</code></p>
<dd>Optional; string </p>
<p> If this option is set, it should contain a comma-separated lis of the local IP addresses on which we should listen to <code><a href="/docs/linux/man/8-nbd-client/">nbd-client</a></code>(8) connections. If it is not set, <code>nbd-server</code> will listen to &quot;::, 0.0.0.0&quot;, which causes nbd-server to listen to all local IPv4 and IPv6 addresses. To limit to IPv6, specify the address as &quot;::&quot;. To limit to IPv4, specify as &quot;0.0.0.0&quot;.</p>
<dt><code>max_threads</code></p>
<dd>Optional; integer; default 4 </p>
<p> Since NBD 3.12, nbd-server will read requests in a main thread, but do the handling of these requests, and the sending of the reply, in a number of separate worker threads, which are shared among all exports. With this parameter, you can configure the number of these worker threads. </p>
<p> The default should be reasonable for a dual-core single-disk server. You might want to increase it if you have a powerful server that does little else than serving NBD.</p>
<dt><code>oldstyle</code></p>
<dd>Optional; boolean </p>
<p> In versions of nbd-server between 2.9.17 and 3.9.1, when this option was set to true, nbd-server would export all exports on a separate port with the old (pre-2.9.17) handshake protocol. In that case, the &#8216;port&#8217; option for individual exports was mandatory. </p>
<p> Since version 3.10 of nbd-server, however, this option is no longer supported, and any attempt to use it will result in nbd-server exiting with an appropriate error message.</p>
<dt><code>port</code></p>
<dd>Optional; string </p>
<p> The port on which to listen for new-style nbd-client connections. If not specified, the IANA-assigned port of 10809 is used.</p>
<dt><code>user</code></p>
<dd>Optional; string. </p>
<p> The name of the user this server must run as. If this parameter is not specified, then nbd-server will not attempt to change its UID (so the UID it runs as will be the user who starts nbd-server). If it is specified, then nbd-server will change its UID after opening ports, but before accepting connections or opening files.</p>
<dt><code>unixsock</code></p>
<dd>Optional; string </p>
<p> Path for a UNIX domain socket. </p>
<p> If specified, the server will listen on a UNIX domain socket with the specified name. Only newstyle negotiation is supported on UNIX domain sockets.</dl>
<h2>Options For Export Sections</h2>
<dl>
<dt><code>authfile</code></p>
<dd>Optional; string; default empty </p>
<p> The name of the authorization file for this export. This file should contain one line per IP-address, or per network (which must be specified in CIDR-style <i>network</i><code>/</code><i>masklen</i>). Empty lines are skipped, as is any content behind a hashmark (&#8216;#&#8217;) on any line. </p>
<p> If the file does not exist, everyone is allowed to connect. If the file exists but is empty, nobody is allowed to connect. Otherwise, <code>nbd-server</code> will only allow clients to connect whose IP-adres is listed in this file. </p>
<p> Corresponds to the <code>-l</code> option on the command line. However, note that for the command line, the default is <i>/etc/nbd-server/allow</i>.</p>
<dt><code>copyonwrite</code></p>
<dd>Optional; boolean. </p>
<p> Whether this is a copy-on-write export. If it is, then any writes to this export will not be written to the master file, but to a separate file which will be removed upon disconnect. The result of using this option is that nbd-server will be somewhat slower, and that any writes will be lost upon disconnect. </p>
<p> Corresponds to the <code>-c</code> option on the command line</p>
<dt><code>cowdir</code></p>
<dd>Optional; string. </p>
<p> Specifies where to write copy-on-write diff files. If this option is absent, copy-on-write files will be written in the same directory as the base export file. Useful for exporting files in copy-on-write mode from a directory that the user running nbd-server has no write access to. </p>
<p> If the copy-on-write mode is not active, this option has no effect.</p>
<dt><code>exportname</code></p>
<dd>Required; string. </p>
<p> The name of the file (or block device) that will be exported. This must be a fully-qualified path and filename; relative paths are not allowed. If used in conjunction with the <code>temporary</code>, this specifies a template for the temporary file concerned, and thus can be used to control the directory it is created in. If the file does not exist, but <code>filesize</code> is set, then the file will be created. </p>
<p> Note that <code>nbd-server</code> will only try to find and open the exported file when a client actually connects; as a result, <code>nbd-server</code> must be able to open and read this file <code>after</code> changing to the user and group that have been specified by use of the <code>user</code> and <code>group</code> options; also, <code>nbd-server</code> will only detect errors in this option upon connection of a client. </p>
<p> When specified on the command line, this should be the second argument.</p>
<dt><code>filesize</code></p>
<dd>Optional; integer; default autodetected. </p>
<p> Disable autodetection of file or block device size, and forcibly specify a size. Sizes must be specified in bytes. If the <code>multifile</code> option is in effect, this option specifies the size of the <code>entire</code> export, not of individual files. If the file is not present, a single file is created of this size. </p>
<p> When specified on the command line, this should be the third argument.</p>
<dt><code>flush</code></p>
<dd>Optional; boolean. </p>
<p> When this option is enabled, <code>nbd-server</code> will inform the client that it supports and desires to be sent flush requests when the elevator layer receives them. Receipt of a flush request will cause an fdatasync() (or, if the sync option is set, an fsync()) on the backend storage. This increases reliability in the case of an unclean shutdown at the expense of a degradation of performance. This option will have no effect unless supported by the client.</p>
<dt><code>fua</code></p>
<dd>Optional; boolean. </p>
<p> When this option is enabled, <code>nbd-server</code> will inform the client that it supports and desires to be sent fua (force unit access) commands when the elevator layer receives them. Receipt of a force unit access command will cause the specified command to be synced to backend storage using sync_file_range() if supported, or fdatasync() otherwise. This increases reliability in the case of an unclean shutdown at the expense of a degradation of performance. This option will have no effect unless supported by the client.</p>
<dt><code>listenaddr</code></p>
<dd>Optional; string </p>
<p> Ignored, kept for compatibility with the obsolete &#8216;oldstyle&#8217; global parameter.</p>
<dt><code>maxconnections</code></p>
<dd>Optional; integer </p>
<p> If specified, then it limits the number of opened connections for this export.</p>
<dt><code>multifile</code></p>
<dd>Optional; boolean. </p>
<p> If this option is set to true, then <code>nbd-server</code> will search for files of the form <i>exportname</i>.<i>integer</i>, with <i>exportname</i> being the filename that would otherwise have been used (after name transformation for virtualization, if any, has been performed) and <i>integer</i> an integer number, starting with 0 and ending when no more files can be found. </p>
<p> The size of the individual files will be autodetected, <code>even</code> if the <code>filesize</code> option has been specified. </p>
<p> Corresponds to the <code>-m</code> option on the command line.</p>
<dt><code>treefiles</code></p>
<dd>Optional; boolean. </p>
<p> If this option is set to true, then <code>nbd-server</code> will search for files of the form <i>exportname</i>/<i>TREEXXXX</i>/&#8230;/<i>FILEXXXX</i>, with <i>exportname</i> being the filename that would otherwise have been used (after name transformation for virtualization, if any, has been performed) and <i>TREEXXXX</i> and <i>FILEXXXX</i> being autogenerated directory and path names for individual block files. </p>
<p> Files and directories are automatically created. Files will be deleted if the corresponding block gets marked as unused. The size of the individual block files is fixed to 4096 bytes. There will be at most 1024 files/subdirectories per folder. An apropriate nesting level of subdirectories will be created to create a filesystem of <code>filesize</code> bytes in total forming a virtual block device. </p>
<p> This feature is useful to provide a virtual block device on an underlying filesystem that does not handle large files well, for example fuse/ftpfs, davfs or other network filesytems. </p>
<p> This feature is mutually exclusive with the <code>-m</code> and will take precedence if both are given. There is no corresponding command line option, since command line control is considered deprecated. You can however specify a custom config file with the <code>-C</code> option. The <code>filesize</code> option <code>must</code> be specified when using this feature!</p>
<dt><code>postrun</code></p>
<dd>Optional; string </p>
<p> If specified, then it is assumed to be a command that will be ran when a client has disconnected. This can be useful to clean up whatever <code>prerun</code> has set up, to log something, or similar. </p>
<p> If the literal string &#8216;%s&#8217; is present in the command, it will be replaced by the file name that has just been closed. </p>
<p> In contrast to the <code>prerun</code> option, the exit state of <code>postrun</code> is <code>ignored</code>.</p>
<dt><code>prerun</code></p>
<dd>Optional; string </p>
<p> If specified, then this command will be ran after a client has connected to the server (and has been accepted), but before the server starts serving. If the command contains the literal string &#8216;%s&#8217;, then this string will be replaced by the filename of the file which nbd-server wants to export. </p>
<p> This is useful to create export files on the fly, or to verify that a file can be used for export, to write something to a log file, or similar. </p>
<p> If the command runs with a non-zero exit status, then nbd-server will assume the export will fail, and refuse to serve it.</p>
<dt><code>readonly</code></p>
<dd>Optional; boolean. </p>
<p> Disallow writes to the device. If this option is specified, <code>nbd-server</code> will issue an error to any client that tries to write to the device. </p>
<p> Use of this option in conjunction with <code>copyonwrite</code> is possible, but silly. </p>
<p> Corresponds to the <code>-r</code> option on the command line.</p>
<dt><code>rotational</code></p>
<dd>Optional; boolean. </p>
<p> When this option is enabled, <code>nbd-server</code> will inform the client that it would prefer it to send requests in elevator (i.e., optimized) order, perhaps because it has a backing store and no local elevator. By default, the client uses QUEUE_FLAG_NONROT, which effectively restricts the function of the elevator to block merges. By specifying this flag on the server, the client will not use QUEUE_FLAG_NONROT, meaning the client elevator will perform normal elevator ordering of I/O requests. Note that even when the backing store is on rotating media, it is not normally necessary to specify this flag, as the server&#8217;s elevator algorithm will be used. This flag is only required where the server will not be using an elevator algorithm or where the elevator algorithm is effectively neutered (e.g. with the sync option set). This option will have no effect unless supported by the client.</p>
<dt><code>sdp</code></p>
<dd>Optional; boolean. </p>
<p> When this option is enabled, <code>nbd-server</code> will use the Socket Direct Protocol (SDP) to serve the export, rather than just IP. This is faster, but requires special hardware (usually something like InfiniBand) and support in the kernel. </p>
<p> Additionally, support for this option must be enabled at compile time, using the <code>&#8211;enable-sdp</code> option to the <code>configure</code> script. If this option is found in a configuration file and <code>nbd-server</code> does not have support for SDP, then <code>nbd-server</code> will exit with an error message.</p>
<dt><code>sparse_cow</code></p>
<dd>Optional; boolean. </p>
<p> When this option is enabled, <code>nbd-server</code> will use sparse files to implement the copy-on-write option; such files take up less space then they appear to, which allows <code>nbd-server</code> to handle the file as if it was just as large as the block device it&#8217;s for. </p>
<p> If this option is disabled, <code>nbd-server</code> will map every newly written block to the end of the copy-on-write file, which means that <code>nbd-server</code> will have to <a href="/docs/linux/man/2-lseek/">lseek</a>(2) to the right position after every 4096-byte block. </p>
<p> Using this option may be faster when much is being written during a connection.</p>
<dt><code>sync</code></p>
<dd>Optional; boolean. </p>
<p> When this option is enabled, <code>nbd-server</code> will call an fsync() after every write to the backend storage. Calling fsync() increases reliability in case of an unclean shutdown of nbd-server; but, depending on the file system used on the nbd-server side, may degrade performance. The use of this option isn&#8217;t always necessary; e.g., on ext3 filesystems, it is recommended that it is <code>not</code> enabled, since it seriously reduces performance on ext3 filesystems while not importantly impacting reliability.</p>
<dt><code>temporary</code></p>
<dd>Optional; boolean. </p>
<p> Create a temporary export with a name based on exportname (this can be used to set the directory). A unique filename is created, which is unlinked as soon as it is created, and therefore the export will not persist between invocations of <code>nbd-server</code>. Set the size of the file using the <code>filesize</code> option. This option is incompatible with the <code>multifile</code> option. </p>
<p> When specified on the command line, this should be the third argument.</p>
<dt><code>timeout</code></p>
<dd>Optional; integer; default 0 </p>
<p> How many seconds a connection may be idle for this export. When a connection is idle for a longer time, <code>nbd-server</code> will forcibly disconnect the connection. If you specify 0 (the default), then a connection may be idle forever. </p>
<p> Corresponds to the <code>-a</code> option on the command line</p>
<dt><code>transactionlog</code></p>
<dd>Optional; string </p>
<p> If specified, then this pathname is used to generate a transaction log. A transaction log is a binary file consisting of the requests sent to and the replies received by the server, but excluding any data (so, for a write command, it records the offset and length of the write but not the data written). It is therefore relatively safe to distribute to a third party. Note that the transaction log does not include the negotiation sequence. Transaction logs are mainly useful for debugging. The program <code>nbd-tester-client</code> distributed with the source to this program can reply a transaction log against a server and perform a data integrity test. Note that the transaction log is written to for every client opened. If it is necessary to maintain separate transaction logs for each client, the <code>prerun</code> script should rename the transaction log (which will just have been opened in order to avoid transaction logs overwriting eachother. This action should be race-free.</p>
<dt><code>trim</code></p>
<dd>Optional; boolean </p>
<p> When this option is activated, the server announces it supports the NBD_CMD_TRIM command for the export. This command allows the server to discard the data from the disk, but does not require it to.</p>
<dt><code>virtstyle</code></p>
<dd>Optional; string; default &quot;ipliteral&quot; </p>
<p> Defines the style of virtualization. Virtualization allows one to create one export that will serve a different file depending on the IP address that is connecting. When virtualization is active, the <i>exportname</i> parameter needs to contain the string &#8216;%s&#8217;; this will then be replaced by the IP address of the client connecting, in accordance with the option selected here. The result of this transformation is then used as the filename to be opened. </p>
<p> When a client connects over a UNIX domain socket, the literal string &quot;unix&quot; is used in lieu of a client IP address. </p>
<p> There are four types of virtualization that <code>nbd-server</code> supports:</p>
<dl>
<dd>
<dl>
<dt><code>none</code></p>
<dd>No virtualization. Will attempt to open the filename as it was written, even if it contains &#8216;%s&#8217; in the name.</p>
<dt><code>ipliteral</code></p>
<dd>The %s is replaced by the IP address of the connecting host is used as-is. For IPv4, this is done in dotted-quad notation; for IPv6, in hexadecimal form with leading zeros omitted. </p>
<p> As an example, if a client connects from 192.168.1.100 and <code>exportname</code> is specified as <i>/export/%s</i>, then nbd-server will attempt to serve <i>/export/192.168.1.100</i>. For IPv6, with a client connecting from 2001:6f8:32f::39, the filename would be <i>/export/2001:6f8:32f:0:0:0:0:39</i></p>
<dt><code>iphash</code></p>
<dd>Same as above, except that <code>nbd-server</code> will replace the dots in the IP address by forward slashes (&#8216;/&#8217;); in the same example, <code>nbd-server</code> would open <i>/export/192/168/1/100</i> instead. </p>
<p> Since there are no dots in most IPv6 addresses, the effect of using this option when IPv6 is in use is indistinguishable from the ipliteral option. It was thought that having to create an eight-deep directory structure would not be as useful.</p>
<dt><code>cidrhash</code></p>
<dd>This option requires one to add a space and a number after it. <code>nbd-server</code> will use the number as a network mask in CIDR style, and use that as a hash cutoff point. In the above example, if <code>virtstyle</code> has been specified as cidrhash 16, then <code>nbd-server</code> will try to open <i>/export/192.168.0.0/192.168.1.100</i>; if <code>virtstyle</code> were specified as cidrhash 26, then <code>nbd-server</code> will try to open <i>/export/192.168.1.64/192.168.1.100</i>. </p>
<p> For IPv6, in the above example, with cidrhash 42, the filename would be <i>/export/2001:32f:6c0:0:0:0:0:0/2001:32f:6f8:0:0:0:0:39</i>.</dl>
</dl>
</dl>
<h2>See Also</h2>
<p>nbd-server (1), nbd-client (8), nbd-trdump (8)</p>
<h2>Author</h2>
<p>The NBD kernel module and the NBD tools were originally written by Pavel Machek (pavel [at] ucw.cz) </p>
<p> The Linux kernel module is now maintained by Paul Clements (Paul.Clements [at] steeleye.com), while the userland tools are maintained by Wouter Verhelst (&lt;wouter [at] debian.org&gt;) </p>
<p> On The Hurd there is a regular translator available to perform the client side of the protocol, and the use of <code>nbd-client</code> is not required. Please see the relevant documentation for more information. </p>
<p> This manual page was written by Wouter Verhelst (&lt;wouter [at] debian.org&gt;) for the Debian GNU/Linux system (but may be used by others). Permission is granted to copy, distribute and/or modify this document under the terms of the GNU General Public License, version 2, as published by the Free Software Foundation.</p>
<h2>Examples</h2>
<p>A simple <code>nbd-server</code> configuration file would look like this: </p>
<pre> [generic]
 [export]
 exportname = /export/blkdev</pre>
<p>For increased security, one might want to create an authorization file, and set the UID and GID to run as: </p>
<pre> [generic]
 user = nbd
 group = nbd
 [export]
 exportname = /export/blkdev
 authfile = /etc/nbd-server/allow</pre>
<p>With /etc/nbd-server/allow containing the following: </p>
<pre> 127.0.0.1
 192.168.0.0/8
 192.168.1.1</pre>
