---
title: "named(8)"
name: "named"
section: "8"
letter: "n"
url: "/docs/linux/man/8-named/"
description: "named – Internet domain name server"
---

<p>named &#8211; Internet domain name server</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>named</code> [<code>-4</code>] [<code>-6</code>] [<code>-c&nbsp;<wbr></code><i>config-file</i>] [<code>-d&nbsp;<wbr></code><i>debug-level</i>] [<code>-E&nbsp;<wbr></code><i>engine-name</i>] [<code>-f</code>] [<code>-g</code>] [<code>-m&nbsp;<wbr></code><i>flag</i>] [<code>-n&nbsp;<wbr></code><i>#cpus</i>] [<code>-p&nbsp;<wbr></code><i>port</i>] [<code>-s</code>] [<code>-S&nbsp;<wbr></code><i>#max-socks</i>] [<code>-t&nbsp;<wbr></code><i>directory</i>] [<code>-U&nbsp;<wbr></code><i>#listeners</i>] [<code>-u&nbsp;<wbr></code><i>user</i>] [<code>-v</code>] [<code>-V</code>] [<code>-x&nbsp;<wbr></code><i>cache-file</i>]</dl>
<h2>Description</h2>
<p><code>named</code></p>
<dd>is a Domain Name System (DNS) server, part of the BIND 9 distribution from ISC. For more information on the DNS, see RFCs 1033, 1034, and 1035. </p>
<p> When invoked without arguments, <code>named</code> will read the default configuration file <i>/etc/named.conf</i>, read any initial data, and listen for queries.</p>
<h2>Options</h2>
<p>-4</p>
<dl>
<dd>Use IPv4 only even if the host machine is capable of IPv6. <code>-4</code> and <code>-6</code> are mutually exclusive.</dl>
<p> -6</p>
<dl>
<dd>Use IPv6 only even if the host machine is capable of IPv4. <code>-4</code> and <code>-6</code> are mutually exclusive.</dl>
<p> -c <i>config-file</i></p>
<dl>
<dd>Use <i>config-file</i> as the configuration file instead of the default, <i>/etc/named.conf</i>. To ensure that reloading the configuration file continues to work after the server has changed its working directory due to to a possible <code>directory</code> option in the configuration file, <i>config-file</i> should be an absolute pathname.</dl>
<p> -d <i>debug-level</i></p>
<dl>
<dd>Set the daemon&#8217;s debug level to <i>debug-level</i>. Debugging traces from <code>named</code> become more verbose as the debug level increases.</dl>
<p> -E <i>engine-name</i></p>
<dl>
<dd>Use a crypto hardware (OpenSSL engine) for the crypto operations it supports, for instance re-signing with private keys from a secure key store. When compiled with PKCS#11 support <i>engine-name</i> defaults to pkcs11, the empty name resets it to no engine.</dl>
<p> -f</p>
<dl>
<dd>Run the server in the foreground (i.e. do not daemonize).</dl>
<p> -g</p>
<dl>
<dd>Run the server in the foreground and force all logging to <i>stderr</i>.</dl>
<p> -m <i>flag</i></p>
<dl>
<dd>Turn on memory usage debugging flags. Possible flags are <i>usage</i>, <i>trace</i>, <i>record</i>, <i>size</i>, and <i>mctx</i>. These correspond to the ISC_MEM_DEBUGXXXX flags described in <i>&lt;isc/mem.h&gt;</i>.</dl>
<p> -n <i>#cpus</i></p>
<dl>
<dd>Create <i>#cpus</i> worker threads to take advantage of multiple CPUs. If not specified, <code>named</code> will try to determine the number of CPUs present and create one thread per CPU. If it is unable to determine the number of CPUs, a single worker thread will be created.</dl>
<p> -p <i>port</i></p>
<dl>
<dd>Listen for queries on port <i>port</i>. If not specified, the default is port 53.</dl>
<p> -s</p>
<dl>
<dd>Write memory usage statistics to <i>stdout</i> on exit.</p>
<dl>
<dd><code>Note:</code> This option is mainly of interest to BIND 9 developers and may be removed or changed in a future release.</dl>
</dl>
<p> -S <i>#max-socks</i></p>
<dl>
<dd>Allow <code>named</code> to use up to <i>#max-socks</i> sockets.</p>
<dl>
<dd><code>Warning:</code> This option should be unnecessary for the vast majority of users. The use of this option could even be harmful because the specified value may exceed the limitation of the underlying system API. It is therefore set only when the default configuration causes exhaustion of file descriptors and the operational environment is known to support the specified number of sockets. Note also that the actual maximum number is normally a little fewer than the specified value because <code>named</code> reserves some file descriptors for its internal use.</dl>
</dl>
<p> -t <i>directory</i></p>
<dl>
<dd>Chroot to <i>directory</i> after processing the command line arguments, but before reading the configuration file.</p>
<dl>
<dd><code>Warning:</code> This option should be used in conjunction with the <code>-u</code> option, as chrooting a process running as root doesn&#8217;t enhance security on most systems; the way <code><a href="/docs/linux/man/2-chroot/">chroot</a>(2)</code> is defined allows a process with root privileges to escape a chroot jail.</dl>
</dl>
<p> -U <i>#listeners</i></p>
<dl>
<dd>Use <i>#listeners</i> worker threads to listen for incoming UDP packets on each address. If not specified, <code>named</code> will use the number of detected CPUs. If <code>-n</code> has been set to a higher value than the number of CPUs, then <code>-U</code> may be increased as high as that value, but no higher.</dl>
<p> -u <i>user</i></p>
<dl>
<dd>Setuid to <i>user</i> after completing privileged operations, such as creating sockets that listen on privileged ports.</p>
<dl>
<dd><code>Note:</code> On Linux, <code>named</code> uses the kernel&#8217;s capability mechanism to drop all root privileges except the ability to <code><a href="/docs/linux/man/2-bind/">bind</a>(2)</code> to a privileged port and set process resource limits. Unfortunately, this means that the <code>-u</code> option only works when <code>named</code> is run on kernel 2.2.18 or later, or kernel 2.3.99-pre3 or later, since previous kernels did not allow privileges to be retained after <code><a href="/docs/linux/man/2-setuid/">setuid</a>(2)</code>.</dl>
</dl>
<p> -v</p>
<dl>
<dd>Report the version number and exit.</dl>
<p> -V</p>
<dl>
<dd>Report the version number and build options, and exit.</dl>
<p> -x <i>cache-file</i></p>
<dl>
<dd>Load data from <i>cache-file</i> into the cache of the default view.</p>
<dl>
<dd><code>Warning:</code> This option must not be used. It is only of interest to BIND 9 developers and may be removed or changed in a future release.</dl>
</dl>
<h2>Signals</h2>
<p>In routine operation, signals should not be used to control the nameserver; <code>rndc</code> should be used instead. </p>
<p> SIGHUP</p>
<dl>
<dd>Force a reload of the server.</dl>
<p> SIGINT, SIGTERM</p>
<dl>
<dd>Shut down the server.</dl>
<p> The result of sending any other signals to the server is undefined.</p>
<h2>Configuration</h2>
<p>The <code>named</code> configuration file is too complex to describe in detail here. A complete description is provided in the BIND 9 Administrator Reference Manual. </p>
<p> <code>named</code> inherits the <code>umask</code> (file creation mode mask) from the parent process. If files created by <code>named</code>, such as journal files, need to have custom permissions, the <code>umask</code> should be set explicitly in the script used to start the <code>named</code> process.</p>
<h2>Files</h2>
<p><i>/etc/named.conf</i></p>
<dl>
<dd>The default configuration file.</dl>
<p> <i>/var/run/named/named.pid</i></p>
<dl>
<dd>The default process-id file. </p>
</dl>
<h2>Notes</h2>
<dl>
<dt><code>Red Hat SELinux BIND Security Profile:</code></p>
<dd></dl>
<p> By default, Red Hat ships BIND with the most secure SELinux policy that will not prevent normal BIND operation and will prevent exploitation of all known BIND security vulnerabilities . See the <a href="/docs/linux/man/8-selinux/">selinux</a>(8) man page for information about SElinux. It is not necessary to run named in a chroot environment if the Red Hat SELinux policy for named is enabled. When enabled, this policy is far more secure than a chroot environment. Users are recommended to enable SELinux and remove the bind-chroot package. With this extra security comes some restrictions: By default, the SELinux policy does not allow named to write any master zone database files. Only the root user may create files in the $ROOTDIR/var/named zone database file directory (the options { &quot;directory&quot; } option), where $ROOTDIR is set in /etc/sysconfig/named. The &quot;named&quot; group must be granted read privelege to these files in order for named to be enabled to read them. Any file created in the zone database file directory is automatically assigned the SELinux file context named_zone_t . By default, SELinux prevents any role from modifying named_zone_t files; this means that files in the zone database directory cannot be modified by dynamic DNS (DDNS) updates or zone transfers. The Red Hat BIND distribution and SELinux policy creates three directories where named is allowed to create and modify files: /var/named/slaves, /var/named/dynamic /var/named/data. By placing files you want named to modify, such as slave or DDNS updateable zone files and database / statistics dump files in these directories, named will work normally and no further operator action is required. Files in these directories are automatically assigned the &#8216;named_cache_t&#8217; file context, which SELinux allows named to write. <code>Red Hat BIND SDB support:</code> Red Hat ships named with compiled in Simplified Database Backend modules that ISC provides in the &quot;contrib/sdb&quot; directory. Install bind-sdb package if you want use them The SDB modules for LDAP, PostGreSQL, DirDB and SQLite are compiled into named-sdb. See the documentation for the various SDB modules in /usr/share/doc/bind-sdb-*/ . </p>
<h2>See Also</h2>
<p>RFC 1033, RFC 1034, RFC 1035, <code><a href="/docs/linux/man/8-named-checkconf/">named-checkconf</a></code>(8), <code><a href="/docs/linux/man/8-named-checkzone/">named-checkzone</a></code>(8), <code><a href="/docs/linux/man/8-rndc/">rndc</a></code>(8), <code><a href="/docs/linux/man/8-lwresd/">lwresd</a></code>(8), <code><a href="/docs/linux/man/5-named-conf/">named.conf</a></code>(5), BIND 9 Administrator Reference Manual.</p>
<h2>Author</h2>
<p>Internet Systems Consortium</p>
<h2>Copyright</h2>
<p>Copyright &#169; 2004-2009, 2011, 2013 Internet Systems Consortium, Inc. (&quot;ISC&quot;)<br />
 Copyright &#169; 2000, 2001, 2003 Internet Software Consortium.</p>
