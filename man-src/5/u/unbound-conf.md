---
title: "unbound-conf(5)"
name: "unbound-conf"
section: "5"
letter: "u"
url: "/docs/linux/man/5-unbound-conf/"
description: "unbound.conf – Unbound configuration file."
---

<p><code>unbound.conf</code> &#8211; Unbound configuration file.</p>
<h2>Synopsis</h2>
<p><code>unbound.conf</code></p>
<h2>Description</h2>
<p><code>unbound.conf</code> is used to configure <i><a href="/docs/linux/man/8-unbound/">unbound</a></i>(8). The file format has attributes and values. Some attributes have attributes inside them. The notation is: attribute: value. </p>
<p> Comments start with # and last to the end of line. Empty lines are ignored as is whitespace at the beginning of a line. </p>
<p> The utility <i><a href="/docs/linux/man/8-unbound-checkconf/">unbound-checkconf</a></i>(8) can be used to check unbound.conf prior to usage.</p>
<h2>Example</h2>
<p>An example config file is shown below. Copy this to /etc/unbound/unbound.conf and start the server with: </p>
<pre> $ unbound -c /etc/unbound/unbound.conf </pre>
<p>Most settings are the defaults. Stop the server with: </p>
<pre> $ kill `cat /etc/unbound/unbound.pid`</pre>
<p>Below is a minimal config file. The source distribution contains an extensive example.conf file with all the options. </p>
<pre># <a href="//www.systutorials.com/docs/linux/man/5-unbound.conf/">unbound.conf</a>(5) config file for <a href="//www.systutorials.com/docs/linux/man/8-unbound/">unbound</a>(8).
server:
 directory: &quot;/etc/unbound&quot;
 username: unbound
 # make sure unbound can access entropy from inside the chroot.
 # e.g. on linux the use these commands (on BSD, <a href="//www.systutorials.com/docs/linux/man/8-devfs/">devfs</a>(8) is used):
 # mount --bind -n /dev/random /etc/unbound/dev/random
 # and mount --bind -n /dev/log /etc/unbound/dev/log
 chroot: &quot;/etc/unbound&quot;
 # logfile: &quot;/etc/unbound/unbound.log&quot; #uncomment to use logfile.
 pidfile: &quot;/etc/unbound/unbound.pid&quot;
 # verbosity: 1 # uncomment and increase to get more logging.
 # listen on all interfaces, answer queries from the local subnet.
 interface: 0.0.0.0
 interface: ::0
 access-control: 10.0.0.0/8 allow
 access-control: 2001:DB8::/64 allow</pre>
<h2>File Format</h2>
<p>There must be whitespace between keywords. Attribute keywords end with a colon &#8216;:&#8217;. An attribute is followed by its containing attributes, or a value. </p>
<p> Files can be included using the <code>include:</code> directive. It can appear anywhere, it accepts a single file name as argument. Processing continues as if the text from the included file was copied into the config file at that point. If also using chroot, using full path names for the included files works, relative pathnames for the included names work if the directory where the daemon is started equals its chroot/working directory. Wildcards can be used to include multiple files, see <i><a href="/docs/linux/man/7-glob/">glob</a></i>(7).</p>
<h3>Server Options</h3>
<p>These options are part of the <code>server:</code> clause.</p>
<dl>
<dt><code>verbosity: </code><i>&lt;number&gt;</i></p>
<dd>The verbosity number, level 0 means no verbosity, only errors. Level 1 gives operational information. Level 2 gives detailed operational information. Level 3 gives query level information, output per query. Level 4 gives algorithm level information. Level 5 logs client identification for cache misses. Default is level 1. The verbosity can also be increased from the commandline, see <i><a href="/docs/linux/man/8-unbound/">unbound</a></i>(8).</p>
<dt><code>statistics-interval: </code><i>&lt;seconds&gt;</i></p>
<dd>The number of seconds between printing statistics to the log for every thread. Disable with value 0 or &quot;&quot;. Default is disabled. The histogram statistics are only printed if replies were sent during the statistics interval, requestlist statistics are printed for every interval (but can be 0). This is because the median calculation requires data to be present.</p>
<dt><code>statistics-cumulative: </code><i>&lt;yes or no&gt;</i></p>
<dd>If enabled, statistics are cumulative since starting unbound, without clearing the statistics counters after logging the statistics. Default is no.</p>
<dt><code>extended-statistics: </code><i>&lt;yes or no&gt;</i></p>
<dd>If enabled, extended statistics are printed from <i><a href="/docs/linux/man/8-unbound-control/">unbound-control</a></i>(8). Default is off, because keeping track of more statistics takes time. The counters are listed in <i><a href="/docs/linux/man/8-unbound-control/">unbound-control</a></i>(8).</p>
<dt><code>num-threads: </code><i>&lt;number&gt;</i></p>
<dd>The number of threads to create to serve clients. Use 1 for no threading.</p>
<dt><code>port: </code><i>&lt;port number&gt;</i></p>
<dd>The port number, default 53, on which the server responds to queries.</p>
<dt><code>interface: </code><i>&lt;ip address[@port]&gt;</i></p>
<dd>Interface to use to connect to the network. This interface is listened to for queries from clients, and answers to clients are given from it. Can be given multiple times to work on several interfaces. If none are given the default is to listen to localhost. The interfaces are not changed on a reload (kill -HUP) but only on restart. A port number can be specified with @port (without spaces between interface and port number), if not specified the default port (from <code>port</code>) is used.</p>
<dt><code>interface-automatic: </code><i>&lt;yes or no&gt;</i></p>
<dd>Detect source interface on UDP queries and copy them to replies. This feature is experimental, and needs support in your OS for particular socket options. Default value is no.</p>
<dt><code>outgoing-interface: </code><i>&lt;ip address&gt;</i></p>
<dd>Interface to use to connect to the network. This interface is used to send queries to authoritative servers and receive their replies. Can be given multiple times to work on several interfaces. If none are given the default (all) is used. You can specify the same interfaces in <code>interface:</code> and <code>outgoing-interface:</code> lines, the interfaces are then used for both purposes. Outgoing queries are sent via a random outgoing interface to counter spoofing.</p>
<dt><code>outgoing-range: </code><i>&lt;number&gt;</i></p>
<dd>Number of ports to open. This number of file descriptors can be opened per thread. Must be at least 1. Default depends on compile options. Larger numbers need extra resources from the operating system. For performance a a very large value is best, use libevent to make this possible.</p>
<dt><code>outgoing-port-permit: </code><i>&lt;port number or range&gt;</i></p>
<dd>Permit unbound to open this port or range of ports for use to send queries. A larger number of permitted outgoing ports increases resilience against spoofing attempts. Make sure these ports are not needed by other daemons. By default only ports above 1024 that have not been assigned by IANA are used. Give a port number or a range of the form &quot;low-high&quot;, without spaces.</p>
<dd>The <code>outgoing-port-permit</code> and <code>outgoing-port-avoid</code> statements are processed in the line order of the config file, adding the permitted ports and subtracting the avoided ports from the set of allowed ports. The processing starts with the non IANA allocated ports above 1024 in the set of allowed ports.</p>
<dt><code>outgoing-port-avoid: </code><i>&lt;port number or range&gt;</i></p>
<dd>Do not permit unbound to open this port or range of ports for use to send queries. Use this to make sure unbound does not grab a port that another daemon needs. The port is avoided on all outgoing interfaces, both IP4 and IP6. By default only ports above 1024 that have not been assigned by IANA are used. Give a port number or a range of the form &quot;low-high&quot;, without spaces.</p>
<dt><code>outgoing-num-tcp: </code><i>&lt;number&gt;</i></p>
<dd>Number of outgoing TCP buffers to allocate per thread. Default is 10. If set to 0, or if do_tcp is &quot;no&quot;, no TCP queries to authoritative servers are done.</p>
<dt><code>incoming-num-tcp: </code><i>&lt;number&gt;</i></p>
<dd>Number of incoming TCP buffers to allocate per thread. Default is 10. If set to 0, or if do_tcp is &quot;no&quot;, no TCP queries from clients are accepted.</p>
<dt><code>edns-buffer-size: </code><i>&lt;number&gt;</i></p>
<dd>Number of bytes size to advertise as the EDNS reassembly buffer size. This is the value put into datagrams over UDP towards peers. The actual buffer size is determined by msg-buffer-size (both for TCP and UDP). Do not set higher than that value. Default is 4096 which is RFC recommended. If you have fragmentation reassembly problems, usually seen as timeouts, then a value of 1480 can fix it. Setting to 512 bypasses even the most stringent path MTU problems, but is seen as extreme, since the amount of TCP fallback generated is excessive (probably also for this resolver, consider tuning the outgoing tcp number).</p>
<dt><code>msg-buffer-size: </code><i>&lt;number&gt;</i></p>
<dd>Number of bytes size of the message buffers. Default is 65552 bytes, enough for 64 Kb packets, the maximum DNS message size. No message larger than this can be sent or received. Can be reduced to use less memory, but some requests for DNS data, such as for huge resource records, will result in a SERVFAIL reply to the client.</p>
<dt><code>msg-cache-size: </code><i>&lt;number&gt;</i></p>
<dd>Number of bytes size of the message cache. Default is 4 megabytes. A plain number is in bytes, append &#8216;k&#8217;, &#8216;m&#8217; or &#8216;g&#8217; for kilobytes, megabytes or gigabytes (1024*1024 bytes in a megabyte).</p>
<dt><code>msg-cache-slabs: </code><i>&lt;number&gt;</i></p>
<dd>Number of slabs in the message cache. Slabs reduce lock contention by threads. Must be set to a power of 2. Setting (close) to the number of cpus is a reasonable guess.</p>
<dt><code>num-queries-per-thread: </code><i>&lt;number&gt;</i></p>
<dd>The number of queries that every thread will service simultaneously. If more queries arrive that need servicing, and no queries can be jostled out (see <i>jostle-timeout</i>), then the queries are dropped. This forces the client to resend after a timeout; allowing the server time to work on the existing queries. Default depends on compile options, 512 or 1024.</p>
<dt><code>jostle-timeout: </code><i>&lt;msec&gt;</i></p>
<dd>Timeout used when the server is very busy. Set to a value that usually results in one roundtrip to the authority servers. If too many queries arrive, then 50% of the queries are allowed to run to completion, and the other 50% are replaced with the new incoming query if they have already spent more than their allowed time. This protects against denial of service by slow queries or high query rates. Default 200 milliseconds. The effect is that the qps for long-lasting queries is about (numqueriesperthread / 2) / (average time for such long queries) qps. The qps for short queries can be about (numqueriesperthread / 2) / (jostletimeout in whole seconds) qps per thread, about (1024/2)*5 = 2560 qps by default.</p>
<dt><code>so-rcvbuf: </code><i>&lt;number&gt;</i></p>
<dd>If not 0, then set the SO_RCVBUF socket option to get more buffer space on UDP port 53 incoming queries. So that short spikes on busy servers do not drop packets (see counter in netstat -su). Default is 0 (use system value). Otherwise, the number of bytes to ask for, try &quot;4m&quot; on a busy server. The OS caps it at a maximum, on linux unbound needs root permission to bypass the limit, or the admin can use sysctl net.core.rmem_max. On BSD change kern.ipc.maxsockbuf in /etc/sysctl.conf. On OpenBSD change header and recompile kernel. On Solaris ndd -set /dev/udp udp_max_buf 8388608.</p>
<dt><code>so-sndbuf: </code><i>&lt;number&gt;</i></p>
<dd>If not 0, then set the SO_SNDBUF socket option to get more buffer space on UDP port 53 outgoing queries. This for very busy servers handles spikes in answer traffic, otherwise &#8216;send: resource temporarily unavailable&#8217; can get logged, the buffer overrun is also visible by netstat -su. Default is 0 (use system value). Specify the number of bytes to ask for, try &quot;4m&quot; on a very busy server. The OS caps it at a maximum, on linux unbound needs root permission to bypass the limit, or the admin can use sysctl net.core.wmem_max. On BSD, Solaris changes are similar to so-rcvbuf.</p>
<dt><code>rrset-cache-size: </code><i>&lt;number&gt;</i></p>
<dd>Number of bytes size of the RRset cache. Default is 4 megabytes. A plain number is in bytes, append &#8216;k&#8217;, &#8216;m&#8217; or &#8216;g&#8217; for kilobytes, megabytes or gigabytes (1024*1024 bytes in a megabyte).</p>
<dt><code>rrset-cache-slabs: </code><i>&lt;number&gt;</i></p>
<dd>Number of slabs in the RRset cache. Slabs reduce lock contention by threads. Must be set to a power of 2.</p>
<dt><code>cache-max-ttl: </code><i>&lt;seconds&gt;</i></p>
<dd>Time to live maximum for RRsets and messages in the cache. Default is 86400 seconds (1 day). If the maximum kicks in, responses to clients still get decrementing TTLs based on the original (larger) values. When the internal TTL expires, the cache item has expired. Can be set lower to force the resolver to query for data often, and not trust (very large) TTL values.</p>
<dt><code>cache-min-ttl: </code><i>&lt;seconds&gt;</i></p>
<dd>Time to live minimum for RRsets and messages in the cache. Default is 0. If the the minimum kicks in, the data is cached for longer than the domain owner intended, and thus less queries are made to look up the data. Zero makes sure the data in the cache is as the domain owner intended, higher values, especially more than an hour or so, can lead to trouble as the data in the cache does not match up with the actual data any more.</p>
<dt><code>infra-host-ttl: </code><i>&lt;seconds&gt;</i></p>
<dd>Time to live for entries in the host cache. The host cache contains roundtrip timing, lameness and EDNS support information. Default is 900.</p>
<dt><code>infra-cache-slabs: </code><i>&lt;number&gt;</i></p>
<dd>Number of slabs in the infrastructure cache. Slabs reduce lock contention by threads. Must be set to a power of 2.</p>
<dt><code>infra-cache-numhosts: </code><i>&lt;number&gt;</i></p>
<dd>Number of hosts for which information is cached. Default is 10000.</p>
<dt><code>do-ip4: </code><i>&lt;yes or no&gt;</i></p>
<dd>Enable or disable whether ip4 queries are answered or issued. Default is yes.</p>
<dt><code>do-ip6: </code><i>&lt;yes or no&gt;</i></p>
<dd>Enable or disable whether ip6 queries are answered or issued. Default is yes. If disabled, queries are not answered on IPv6, and queries are not sent on IPv6 to the internet nameservers.</p>
<dt><code>do-udp: </code><i>&lt;yes or no&gt;</i></p>
<dd>Enable or disable whether UDP queries are answered or issued. Default is yes.</p>
<dt><code>do-tcp: </code><i>&lt;yes or no&gt;</i></p>
<dd>Enable or disable whether TCP queries are answered or issued. Default is yes.</p>
<dt><code>tcp-upstream: </code><i>&lt;yes or no&gt;</i></p>
<dd>Enable or disable whether the upstream queries use TCP only for transport. Default is no. Useful in tunneling scenarios.</p>
<dt><code>ssl-upstream: </code><i>&lt;yes or no&gt;</i></p>
<dd>Enabled or disable whether the upstream queries use SSL only for transport. Default is no. Useful in tunneling scenarios. The SSL contains plain DNS in TCP wireformat. The other server must support this (see <code>ssl-service-key</code>).</p>
<dt><code>ssl-service-key: </code><i>&lt;file&gt;</i></p>
<dd>If enabled, the server provider SSL service on its TCP sockets. The clients have to use ssl-upstream: yes. The file is the private key for the TLS session. The public certificate is in the ssl-service-pem file. Default is &quot;&quot;, turned off. Requires a restart (a reload is not enough) if changed, because the private key is read while root permissions are held and before chroot (if any). Normal DNS TCP service is not provided and gives errors, this service is best run with a different <code>port:</code> config or <i>@port</i> suffixes in the <code>interface</code> config.</p>
<dt><code>ssl-service-pem: </code><i>&lt;file&gt;</i></p>
<dd>The public key certificate pem file for the ssl service. Default is &quot;&quot;, turned off.</p>
<dt><code>ssl-port: </code><i>&lt;number&gt;</i></p>
<dd>The port number on which to provide TCP SSL service, default 443, only interfaces configured with that port number as @number get the SSL service.</p>
<dt><code>do-daemonize: </code><i>&lt;yes or no&gt;</i></p>
<dd>Enable or disable whether the unbound server forks into the background as a daemon. Default is yes.</p>
<dt><code>access-control: </code><i>&lt;IP netblock&gt; &lt;action&gt;</i></p>
<dd>The netblock is given as an IP4 or IP6 address with /size appended for a classless network block. The action can be <i>deny</i>, <i>refuse</i>, <i>allow</i> or <i>allow_snoop</i>.</p>
<dd>The action <i>deny</i> stops queries from hosts from that netblock.</p>
<dd>The action <i>refuse</i> stops queries too, but sends a DNS rcode REFUSED error message back.</p>
<dd>The action <i>allow</i> gives access to clients from that netblock. It gives only access for recursion clients (which is what almost all clients need). Nonrecursive queries are refused.</p>
<dd>The <i>allow</i> action does allow nonrecursive queries to access the local-data that is configured. The reason is that this does not involve the unbound server recursive lookup algorithm, and static data is served in the reply. This supports normal operations where nonrecursive queries are made for the authoritative data. For nonrecursive queries any replies from the dynamic cache are refused.</p>
<dd>The action <i>allow_snoop</i> gives nonrecursive access too. This give both recursive and non recursive access. The name <i>allow_snoop</i> refers to cache snooping, a technique to use nonrecursive queries to examine the cache contents (for malicious acts). However, nonrecursive queries can also be a valuable debugging tool (when you want to examine the cache contents). In that case use <i>allow_snoop</i> for your administration host.</p>
<dd>By default only localhost is <i>allow</i>ed, the rest is <i>refuse</i>d. The default is <i>refuse</i>d, because that is protocol-friendly. The DNS protocol is not designed to handle dropped packets due to policy, and dropping may result in (possibly excessive) retried queries.</p>
<dt><code>chroot: </code><i>&lt;directory&gt;</i></p>
<dd>If chroot is enabled, you should pass the configfile (from the commandline) as a full path from the original root. After the chroot has been performed the now defunct portion of the config file path is removed to be able to reread the config after a reload.</p>
<dd>All other file paths (working dir, logfile, roothints, and key files) can be specified in several ways: as an absolute path relative to the new root, as a relative path to the working directory, or as an absolute path relative to the original root. In the last case the path is adjusted to remove the unused portion.</p>
<dd>The pidfile can be either a relative path to the working directory, or an absolute path relative to the original root. It is written just prior to chroot and dropping permissions. This allows the pidfile to be /var/run/unbound.pid and the chroot to be /var/unbound, for example.</p>
<dd>Additionally, unbound may need to access /dev/random (for entropy) from inside the chroot.</p>
<dd>If given a chroot is done to the given directory. The default is &quot;/etc/unbound&quot;. If you give &quot;&quot; no chroot is performed.</p>
<dt><code>username: </code><i>&lt;name&gt;</i></p>
<dd>If given, after binding the port the user privileges are dropped. Default is &quot;unbound&quot;. If you give username: &quot;&quot; no user change is performed.</p>
<dd>If this user is not capable of binding the port, reloads (by signal HUP) will still retain the opened ports. If you change the port number in the config file, and that new port number requires privileges, then a reload will fail; a restart is needed.</p>
<dt><code>directory: </code><i>&lt;directory&gt;</i></p>
<dd>Sets the working directory for the program. Default is &quot;/etc/unbound&quot;.</p>
<dt><code>logfile: </code><i>&lt;filename&gt;</i></p>
<dd>If &quot;&quot; is given, logging goes to stderr, or nowhere once daemonized. The logfile is appended to, in the following format: </p>
<pre>[seconds since 1970] unbound[pid:tid]: type: message. </pre>
<p>If this option is given, the use-syslog is option is set to &quot;no&quot;. The logfile is reopened (for append) when the config file is reread, on SIGHUP.</p>
<dt><code>use-syslog: </code><i>&lt;yes or no&gt;</i></p>
<dd>Sets unbound to send log messages to the syslogd, using <i><a href="/docs/linux/man/3-syslog/">syslog</a></i>(3). The log facility LOG_DAEMON is used, with identity &quot;unbound&quot;. The logfile setting is overridden when use-syslog is turned on. The default is to log to syslog.</p>
<dt><code>log-time-ascii: </code><i>&lt;yes or no&gt;</i></p>
<dd>Sets logfile lines to use a timestamp in UTC ascii. Default is no, which prints the seconds since 1970 in brackets. No effect if using syslog, in that case syslog formats the timestamp printed into the log files.</p>
<dt><code>log-queries: </code><i>&lt;yes or no&gt;</i></p>
<dd>Prints one line per query to the log, with the log timestamp and IP address, name, type and class. Default is no. Note that it takes time to print these lines which makes the server (significantly) slower. Odd (nonprintable) characters in names are printed as &#8216;?&#8217;.</p>
<dt><code>pidfile: </code><i>&lt;filename&gt;</i></p>
<dd>The process id is written to the file. Default is &quot;/var/run/unbound/unbound.pid&quot;. So, </p>
<pre>kill -HUP `cat /var/run/unbound/unbound.pid` </pre>
<p>triggers a reload, </p>
<pre>kill -QUIT `cat /var/run/unbound/unbound.pid` </pre>
<p>gracefully terminates.</p>
<dt><code>root-hints: </code><i>&lt;filename&gt;</i></p>
<dd>Read the root hints from this file. Default is nothing, using builtin hints for the IN class. The file has the format of zone files, with root nameserver names and addresses only. The default may become outdated, when servers change, therefore it is good practice to use a root-hints file.</p>
<dt><code>hide-identity: </code><i>&lt;yes or no&gt;</i></p>
<dd>If enabled id.server and hostname.bind queries are refused.</p>
<dt><code>identity: </code><i>&lt;string&gt;</i></p>
<dd>Set the identity to report. If set to &quot;&quot;, the default, then the hostname of the server is returned.</p>
<dt><code>hide-version: </code><i>&lt;yes or no&gt;</i></p>
<dd>If enabled version.server and version.bind queries are refused.</p>
<dt><code>version: </code><i>&lt;string&gt;</i></p>
<dd>Set the version to report. If set to &quot;&quot;, the default, then the package version is returned.</p>
<dt><code>target-fetch-policy: </code><i>&lt;list of numbers&gt;</i></p>
<dd>Set the target fetch policy used by unbound to determine if it should fetch nameserver target addresses opportunistically. The policy is described per dependency depth.</p>
<dd>The number of values determines the maximum dependency depth that unbound will pursue in answering a query. A value of -1 means to fetch all targets opportunistically for that dependency depth. A value of 0 means to fetch on demand only. A positive value fetches that many targets opportunistically.</p>
<dd>Enclose the list between quotes (&quot;&quot;) and put spaces between numbers. The default is &quot;3 2 1 0 0&quot;. Setting all zeroes, &quot;0 0 0 0 0&quot; gives behaviour closer to that of BIND 9, while setting &quot;-1 -1 -1 -1 -1&quot; gives behaviour rumoured to be closer to that of BIND 8.</p>
<dt><code>harden-short-bufsize: </code><i>&lt;yes or no&gt;</i></p>
<dd>Very small EDNS buffer sizes from queries are ignored. Default is off, since it is legal protocol wise to send these, and unbound tries to give very small answers to these queries, where possible.</p>
<dt><code>harden-large-queries: </code><i>&lt;yes or no&gt;</i></p>
<dd>Very large queries are ignored. Default is off, since it is legal protocol wise to send these, and could be necessary for operation if TSIG or EDNS payload is very large.</p>
<dt><code>harden-glue: </code><i>&lt;yes or no&gt;</i></p>
<dd>Will trust glue only if it is within the servers authority. Default is on.</p>
<dt><code>harden-dnssec-stripped: </code><i>&lt;yes or no&gt;</i></p>
<dd>Require DNSSEC data for trust-anchored zones, if such data is absent, the zone becomes bogus. If turned off, and no DNSSEC data is received (or the DNSKEY data fails to validate), then the zone is made insecure, this behaves like there is no trust anchor. You could turn this off if you are sometimes behind an intrusive firewall (of some sort) that removes DNSSEC data from packets, or a zone changes from signed to unsigned to badly signed often. If turned off you run the risk of a downgrade attack that disables security for a zone. Default is on.</p>
<dt><code>harden-below-nxdomain: </code><i>&lt;yes or no&gt;</i></p>
<dd>From draft-vixie-dnsext-resimprove, returns nxdomain to queries for a name below another name that is already known to be nxdomain. DNSSEC mandates noerror for empty nonterminals, hence this is possible. Very old software might return nxdomain for empty nonterminals (that usually happen for reverse IP address lookups), and thus may be incompatible with this. To try to avoid this only DNSSEC-secure nxdomains are used, because the old software does not have DNSSEC. Default is off.</p>
<dt><code>harden-referral-path: </code><i>&lt;yes or no&gt;</i></p>
<dd>Harden the referral path by performing additional queries for infrastructure data. Validates the replies if trust anchors are configured and the zones are signed. This enforces DNSSEC validation on nameserver NS sets and the nameserver addresses that are encountered on the referral path to the answer. Default off, because it burdens the authority servers, and it is not RFC standard, and could lead to performance problems because of the extra query load that is generated. Experimental option. If you enable it consider adding more numbers after the target-fetch-policy to increase the max depth that is checked to.</p>
<dt><code>use-caps-for-id: </code><i>&lt;yes or no&gt;</i></p>
<dd>Use 0x20-encoded random bits in the query to foil spoof attempts. This perturbs the lowercase and uppercase of query names sent to authority servers and checks if the reply still has the correct casing. Disabled by default. This feature is an experimental implementation of draft dns-0x20.</p>
<dt><code>private-address: </code><i>&lt;IP address or subnet&gt;</i></p>
<dd>Give IPv4 of IPv6 addresses or classless subnets. These are addresses on your private network, and are not allowed to be returned for public internet names. Any occurence of such addresses are removed from DNS answers. Additionally, the DNSSEC validator may mark the answers bogus. This protects against so-called DNS Rebinding, where a user browser is turned into a network proxy, allowing remote access through the browser to other parts of your private network. Some names can be allowed to contain your private addresses, by default all the <code>local-data</code> that you configured is allowed to, and you can specify additional names using <code>private-domain</code>. No private addresses are enabled by default. We consider to enable this for the RFC1918 private IP address space by default in later releases. That would enable private addresses for 10.0.0.0/8 172.16.0.0/12 192.168.0.0/16 169.254.0.0/16 fd00::/8 and fe80::/10, since the RFC standards say these addresses should not be visible on the public internet. Turning on 127.0.0.0/8 would hinder many spamblocklists as they use that.</p>
<dt><code>private-domain: </code><i>&lt;domain name&gt;</i></p>
<dd>Allow this domain, and all its subdomains to contain private addresses. Give multiple times to allow multiple domain names to contain private addresses. Default is none.</p>
<dt><code>unwanted-reply-threshold: </code><i>&lt;number&gt;</i></p>
<dd>If set, a total number of unwanted replies is kept track of in every thread. When it reaches the threshold, a defensive action is taken and a warning is printed to the log. The defensive action is to clear the rrset and message caches, hopefully flushing away any poison. A value of 10 million is suggested. Default is 0 (turned off).</p>
<dt><code>do-not-query-address: </code><i>&lt;IP address&gt;</i></p>
<dd>Do not query the given IP address. Can be IP4 or IP6. Append /num to indicate a classless delegation netblock, for example like 10.2.3.4/24 or 2001::11/64.</p>
<dt><code>do-not-query-localhost: </code><i>&lt;yes or no&gt;</i></p>
<dd>If yes, localhost is added to the do-not-query-address entries, both IP6 ::1 and IP4 127.0.0.1/8. If no, then localhost can be used to send queries to. Default is yes.</p>
<dt><code>prefetch: </code><i>&lt;yes or no&gt;</i></p>
<dd>If yes, message cache elements are prefetched before they expire to keep the cache up to date. Default is no. Turning it on gives about 10 percent more traffic and load on the machine, but popular items do not expire from the cache.</p>
<dt><code>prefetch-key: </code><i>&lt;yes or no&gt;</i></p>
<dd>If yes, fetch the DNSKEYs earlier in the validation process, when a DS record is encountered. This lowers the latency of requests. It does use a little more CPU. Also if the cache is set to 0, it is no use. Default is no.</p>
<dt><code>rrset-roundrobin: </code><i>&lt;yes or no&gt;</i></p>
<dd>If yes, Unbound rotates RRSet order in response (the random number is taken from the query ID, for speed and thread safety). Default is no.</p>
<dt><code>minimal-responses: </code><i>&lt;yes or no&gt;</i></p>
<dd>If yes, Unbound doesn&#8217;t insert authority/additional sections into response messages when those sections are not required. This reduces response size significantly, and may avoid TCP fallback for some responses. This may cause a slight speedup. The default is no, because the DNS protocol RFCs mandate these sections, and the additional content could be of use and save roundtrips for clients.</p>
<dt><code>module-config: </code><i>&lt;module names&gt;</i></p>
<dd>Module configuration, a list of module names separated by spaces, surround the string with quotes (&quot;&quot;). The modules can be validator, iterator. Setting this to &quot;iterator&quot; will result in a non-validating server. Setting this to &quot;validator iterator&quot; will turn on DNSSEC validation. The ordering of the modules is important. You must also set trust-anchors for validation to be useful.</p>
<dt><code>trust-anchor-file: </code><i>&lt;filename&gt;</i></p>
<dd>File with trusted keys for validation. Both DS and DNSKEY entries can appear in the file. The format of the file is the standard DNS Zone file format. Default is &quot;&quot;, or no trust anchor file.</p>
<dt><code>auto-trust-anchor-file: </code><i>&lt;filename&gt;</i></p>
<dd>File with trust anchor for one zone, which is tracked with RFC5011 probes. The probes are several times per month, thus the machine must be online frequently. The initial file can be one with contents as described in <code>trust-anchor-file</code>. The file is written to when the anchor is updated, so the unbound user must have write permission.</p>
<dt><code>trust-anchor: </code><i>&lt;Resource Record&gt;</i></p>
<dd>A DS or DNSKEY RR for a key to use for validation. Multiple entries can be given to specify multiple trusted keys, in addition to the trust-anchor-files. The resource record is entered in the same format as &#8216;dig&#8217; or &#8216;drill&#8217; prints them, the same format as in the zone file. Has to be on a single line, with &quot;&quot; around it. A TTL can be specified for ease of cut and paste, but is ignored. A class can be specified, but class IN is default.</p>
<dt><code>trusted-keys-file: </code><i>&lt;filename&gt;</i></p>
<dd>File with trusted keys for validation. Specify more than one file with several entries, one file per entry. Like <code>trust-anchor-file</code> but has a different file format. Format is BIND-9 style format, the trusted-keys { name flag proto algo &quot;key&quot;; }; clauses are read. It is possible to use wildcards with this statement, the wildcard is expanded on start and on reload.</p>
<dt><code>dlv-anchor-file: </code><i>&lt;filename&gt;</i></p>
<dd>File with trusted keys for DLV (DNSSEC Lookaside Validation). Both DS and DNSKEY entries can be used in the file, in the same format as for <i>trust-anchor-file:</i> statements. Only one DLV can be configured, more would be slow. The DLV configured is used as a root trusted DLV, this means that it is a lookaside for the root. Default is &quot;&quot;, or no dlv anchor file.</p>
<dt><code>dlv-anchor: </code><i>&lt;Resource Record&gt;</i></p>
<dd>Much like trust-anchor, this is a DLV anchor with the DS or DNSKEY inline.</p>
<dt><code>domain-insecure: </code><i>&lt;domain name&gt;</i></p>
<dd>Sets domain name to be insecure, DNSSEC chain of trust is ignored towards the domain name. So a trust anchor above the domain name can not make the domain secure with a DS record, such a DS record is then ignored. Also keys from DLV are ignored for the domain. Can be given multiple times to specify multiple domains that are treated as if unsigned. If you set trust anchors for the domain they override this setting (and the domain is secured).</p>
<dd>This can be useful if you want to make sure a trust anchor for external lookups does not affect an (unsigned) internal domain. A DS record externally can create validation failures for that internal domain.</p>
<dt><code>val-override-date: </code><i>&lt;rrsig-style date spec&gt;</i></p>
<dd>Default is &quot;&quot; or &quot;0&quot;, which disables this debugging feature. If enabled by giving a RRSIG style date, that date is used for verifying RRSIG inception and expiration dates, instead of the current date. Do not set this unless you are debugging signature inception and expiration. The value -1 ignores the date altogether, useful for some special applications.</p>
<dt><code>val-sig-skew-min: </code><i>&lt;seconds&gt;</i></p>
<dd>Minimum number of seconds of clock skew to apply to validated signatures. A value of 10% of the signature lifetime (expiration &#8211; inception) is used, capped by this setting. Default is 3600 (1 hour) which allows for daylight savings differences. Lower this value for more strict checking of short lived signatures.</p>
<dt><code>val-sig-skew-max: </code><i>&lt;seconds&gt;</i></p>
<dd>Maximum number of seconds of clock skew to apply to validated signatures. A value of 10% of the signature lifetime (expiration &#8211; inception) is used, capped by this setting. Default is 86400 (24 hours) which allows for timezone setting problems in stable domains. Setting both min and max very low disables the clock skew allowances. Setting both min and max very high makes the validator check the signature timestamps less strictly.</p>
<dt><code>val-bogus-ttl: </code><i>&lt;number&gt;</i></p>
<dd>The time to live for bogus data. This is data that has failed validation; due to invalid signatures or other checks. The TTL from that data cannot be trusted, and this value is used instead. The value is in seconds, default 60. The time interval prevents repeated revalidation of bogus data.</p>
<dt><code>val-clean-additional: </code><i>&lt;yes or no&gt;</i></p>
<dd>Instruct the validator to remove data from the additional section of secure messages that are not signed properly. Messages that are insecure, bogus, indeterminate or unchecked are not affected. Default is yes. Use this setting to protect the users that rely on this validator for authentication from protentially bad data in the additional section.</p>
<dt><code>val-log-level: </code><i>&lt;number&gt;</i></p>
<dd>Have the validator print validation failures to the log. Regardless of the verbosity setting. Default is 0, off. At 1, for every user query that fails a line is printed to the logs. This way you can monitor what happens with validation. Use a diagnosis tool, such as dig or drill, to find out why validation is failing for these queries. At 2, not only the query that failed is printed but also the reason why unbound thought it was wrong and which server sent the faulty data.</p>
<dt><code>val-permissive-mode: </code><i>&lt;yes or no&gt;</i></p>
<dd>Instruct the validator to mark bogus messages as indeterminate. The security checks are performed, but if the result is bogus (failed security), the reply is not withheld from the client with SERVFAIL as usual. The client receives the bogus data. For messages that are found to be secure the AD bit is set in replies. Also logging is performed as for full validation. The default value is &quot;no&quot;.</p>
<dt><code>ignore-cd-flag: </code><i>&lt;yes or no&gt;</i></p>
<dd>Instruct unbound to ignore the CD flag from clients and refuse to return bogus answers to them. Thus, the CD (Checking Disabled) flag does not disable checking any more. This is useful if legacy (w2008) servers that set the CD flag but cannot validate DNSSEC themselves are the clients, and then unbound provides them with DNSSEC protection. The default value is &quot;no&quot;.</p>
<dt><code>val-nsec3-keysize-iterations: </code><i>&lt;list of values&gt;</i></p>
<dd>List of keysize and iteration count values, separated by spaces, surrounded by quotes. Default is &quot;1024 150 2048 500 4096 2500&quot;. This determines the maximum allowed NSEC3 iteration count before a message is simply marked insecure instead of performing the many hashing iterations. The list must be in ascending order and have at least one entry. If you set it to &quot;1024 65535&quot; there is no restriction to NSEC3 iteration values. This table must be kept short; a very long list could cause slower operation.</p>
<dt><code>add-holddown: </code><i>&lt;seconds&gt;</i></p>
<dd>Instruct the <code>auto-trust-anchor-file</code> probe mechanism for RFC5011 autotrust updates to add new trust anchors only after they have been visible for this time. Default is 30 days as per the RFC.</p>
<dt><code>del-holddown: </code><i>&lt;seconds&gt;</i></p>
<dd>Instruct the <code>auto-trust-anchor-file</code> probe mechanism for RFC5011 autotrust updates to remove revoked trust anchors after they have been kept in the revoked list for this long. Default is 30 days as per the RFC.</p>
<dt><code>keep-missing: </code><i>&lt;seconds&gt;</i></p>
<dd>Instruct the <code>auto-trust-anchor-file</code> probe mechanism for RFC5011 autotrust updates to remove missing trust anchors after they have been unseen for this long. This cleans up the state file if the target zone does not perform trust anchor revocation, so this makes the auto probe mechanism work with zones that perform regular (non-5011) rollovers. The default is 366 days. The value 0 does not remove missing anchors, as per the RFC.</p>
<dt><code>key-cache-size: </code><i>&lt;number&gt;</i></p>
<dd>Number of bytes size of the key cache. Default is 4 megabytes. A plain number is in bytes, append &#8216;k&#8217;, &#8216;m&#8217; or &#8216;g&#8217; for kilobytes, megabytes or gigabytes (1024*1024 bytes in a megabyte).</p>
<dt><code>key-cache-slabs: </code><i>&lt;number&gt;</i></p>
<dd>Number of slabs in the key cache. Slabs reduce lock contention by threads. Must be set to a power of 2. Setting (close) to the number of cpus is a reasonable guess.</p>
<dt><code>neg-cache-size: </code><i>&lt;number&gt;</i></p>
<dd>Number of bytes size of the aggressive negative cache. Default is 1 megabyte. A plain number is in bytes, append &#8216;k&#8217;, &#8216;m&#8217; or &#8216;g&#8217; for kilobytes, megabytes or gigabytes (1024*1024 bytes in a megabyte).</p>
<dt><code>local-zone: </code><i>&lt;zone&gt; &lt;type&gt;</i></p>
<dd>Configure a local zone. The type determines the answer to give if there is no match from local-data. The types are deny, refuse, static, transparent, redirect, nodefault, typetransparent, and are explained below. After that the default settings are listed. Use local-data: to enter data into the local zone. Answers for local zones are authoritative DNS answers. By default the zones are class IN.</p>
<dd>If you need more complicated authoritative data, with referrals, wildcards, CNAME/DNAME support, or DNSSEC authoritative service, setup a stub-zone for it as detailed in the stub zone section below.</p>
<dt><i>deny</i></p>
<dd>Do not send an answer, drop the query. If there is a match from local data, the query is answered.</p>
<dt><i>refuse</i></p>
<dd>Send an error message reply, with rcode REFUSED. If there is a match from local data, the query is answered.</p>
<dt><i>static</i></p>
<dd>If there is a match from local data, the query is answered. Otherwise, the query is answered with nodata or nxdomain. For a negative answer a SOA is included in the answer if present as local-data for the zone apex domain.</p>
<dt><i>transparent</i></p>
<dd>If there is a match from local data, the query is answered. Otherwise if the query has a different name, the query is resolved normally. If the query is for a name given in localdata but no such type of data is given in localdata, then a noerror nodata answer is returned. If no local-zone is given local-data causes a transparent zone to be created by default.</p>
<dt><i>typetransparent</i></p>
<dd>If there is a match from local data, the query is answered. If the query is for a different name, or for the same name but for a different type, the query is resolved normally. So, similar to transparent but types that are not listed in local data are resolved normally, so if an A record is in the local data that does not cause a nodata reply for AAAA queries.</p>
<dt><i>redirect</i></p>
<dd>The query is answered from the local data for the zone name. There may be no local data beneath the zone name. This answers queries for the zone, and all subdomains of the zone with the local data for the zone. It can be used to redirect a domain to return a different address record to the end user, with local-zone: &quot;example.com.&quot; redirect and local-data: &quot;example.com. A 127.0.0.1&quot; queries for <a rel="nofollow" href="http://www.example.com">www.example.com</a> and <a href="http://www.foo.example.com">www.foo.example.com</a> are redirected, so that users with web browsers cannot access sites with suffix example.com.</p>
<dt><i>nodefault</i></p>
<dd>Used to turn off default contents for AS112 zones. The other types also turn off default contents for the zone. The &#8216;nodefault&#8217; option has no other effect than turning off default contents for the given zone.</dl>
<p> The default zones are localhost, reverse 127.0.0.1 and ::1, and the AS112 zones. The AS112 zones are reverse DNS zones for private use and reserved IP addresses for which the servers on the internet cannot provide correct answers. They are configured by default to give nxdomain (no reverse information) answers. The defaults can be turned off by specifying your own local-zone of that name, or using the &#8216;nodefault&#8217; type. Below is a list of the default zone contents.</p>
<dl>
<dt><i>localhost</i></p>
<dd>The IP4 and IP6 localhost information is given. NS and SOA records are provided for completeness and to satisfy some DNS update tools. Default content: </p>
<pre>local-zone: &quot;localhost.&quot; static
local-data: &quot;localhost. 10800 IN NS localhost.&quot;
local-data: &quot;localhost. 10800 IN 
 SOA localhost. nobody.invalid. 1 3600 1200 604800 10800&quot;
local-data: &quot;localhost. 10800 IN A 127.0.0.1&quot;
local-data: &quot;localhost. 10800 IN AAAA ::1&quot;</pre>
<dt><i>reverse IPv4 loopback</i></p>
<dd>Default content: </p>
<pre>local-zone: &quot;127.in-addr.arpa.&quot; static
local-data: &quot;127.in-addr.arpa. 10800 IN NS localhost.&quot;
local-data: &quot;127.in-addr.arpa. 10800 IN 
 SOA localhost. nobody.invalid. 1 3600 1200 604800 10800&quot;
local-data: &quot;1.0.0.127.in-addr.arpa. 10800 IN 
 PTR localhost.&quot;</pre>
<dt><i>reverse IPv6 loopback</i></p>
<dd>Default content: </p>
<pre>local-zone: &quot;1.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.
 0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.ip6.arpa.&quot; static
local-data: &quot;1.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.
 0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.ip6.arpa. 10800 IN 
 NS localhost.&quot;
local-data: &quot;1.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.
 0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.ip6.arpa. 10800 IN 
 SOA localhost. nobody.invalid. 1 3600 1200 604800 10800&quot;
local-data: &quot;1.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.
 0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.ip6.arpa. 10800 IN 
 PTR localhost.&quot;</pre>
<dt><i>reverse RFC1918 local use zones</i></p>
<dd>Reverse data for zones 10.in-addr.arpa, 16.172.in-addr.arpa to 31.172.in-addr.arpa, 168.192.in-addr.arpa. The <code>local-zone:</code> is set static and as <code>local-data:</code> SOA and NS records are provided.</p>
<dt><i>reverse RFC3330 IP4 this, link-local, testnet and broadcast</i></p>
<dd>Reverse data for zones 0.in-addr.arpa, 254.169.in-addr.arpa, 2.0.192.in-addr.arpa (TEST NET 1), 100.51.198.in-addr.arpa (TEST NET 2), 113.0.203.in-addr.arpa (TEST NET 3), 255.255.255.255.in-addr.arpa.</p>
<dt><i>reverse RFC4291 IP6 unspecified</i></p>
<dd>Reverse data for zone </p>
<pre>0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.
0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.ip6.arpa.</pre>
<dt><i>reverse RFC4193 IPv6 Locally Assigned Local Addresses</i></p>
<dd>Reverse data for zone D.F.ip6.arpa.</p>
<dt><i>reverse RFC4291 IPv6 Link Local Addresses</i></p>
<dd>Reverse data for zones 8.E.F.ip6.arpa to B.E.F.ip6.arpa.</p>
<dt><i>reverse IPv6 Example Prefix</i></p>
<dd>Reverse data for zone 8.B.D.0.1.0.0.2.ip6.arpa. This zone is used for tutorials and examples. You can remove the block on this zone with: </p>
<pre> local-zone: 8.B.D.0.1.0.0.2.ip6.arpa. nodefault</pre>
<p>You can also selectively unblock a part of the zone by making that part transparent with a local-zone statement. This also works with the other default zones.</p>
<dt><code>local-data: </code><i>&lt;resource record string&gt;</i></p>
<dd>Configure local data, which is served in reply to queries for it. The query has to match exactly unless you configure the local-zone as redirect. If not matched exactly, the local-zone type determines further processing. If local-data is configured that is not a subdomain of a local-zone, a transparent local-zone is configured. For record types such as TXT, use single quotes, as in local-data: &#8216;example. TXT &quot;text&quot;&#8217;.</p>
<dd>If you need more complicated authoritative data, with referrals, wildcards, CNAME/DNAME support, or DNSSEC authoritative service, setup a stub-zone for it as detailed in the stub zone section below.</p>
<dt><code>local-data-ptr: </code><i>IPaddr name</i></p>
<dd>Configure local data shorthand for a PTR record with the reversed IPv4 or IPv6 address and the host name. For example &quot;192.0.2.4 <a rel="nofollow" href="http://www.example.com">www.example.com</a>&quot;. TTL can be inserted like this: &quot;2001:DB8::4 7200 <a rel="nofollow" href="http://www.example.com">www.example.com</a>&quot;</dl>
<h3>Remote Control Options</h3>
<p>In the <code>remote-control:</code> clause are the declarations for the remote control facility. If this is enabled, the <i><a href="/docs/linux/man/8-unbound-control/">unbound-control</a></i>(8) utility can be used to send commands to the running unbound server. The server uses these clauses to setup SSLv3 / TLSv1 security for the connection. The <i><a href="/docs/linux/man/8-unbound-control/">unbound-control</a></i>(8) utility also reads the <code>remote-control</code> section for options. To setup the correct self-signed certificates use the <i><a href="/docs/linux/man/8-unbound-control-setup/">unbound-control-setup</a></i>(8) utility.</p>
<dl>
<dt><code>control-enable: </code><i>&lt;yes or no&gt;</i></p>
<dd>The option is used to enable remote control, default is &quot;no&quot;. If turned off, the server does not listen for control commands.</p>
<dt><code>control-interface: &lt;ip address&gt;</code></p>
<dd>Give IPv4 or IPv6 addresses to listen on for control commands. By default localhost (127.0.0.1 and ::1) is listened to. Use 0.0.0.0 and ::0 to listen to all interfaces.</p>
<dt><code>control-port: &lt;port number&gt;</code></p>
<dd>The port number to listen on for control commands, default is 8953. If you change this port number, and permissions have been dropped, a reload is not sufficient to open the port again, you must then restart.</p>
<dt><code>server-key-file: &lt;private key file&gt;</code></p>
<dd>Path to the server private key, by default unbound_server.key. This file is generated by the <i>unbound-control-setup</i> utility. This file is used by the unbound server, but not by <i>unbound-control</i>.</p>
<dt><code>server-cert-file: &lt;certificate file.pem&gt;</code></p>
<dd>Path to the server self signed certificate, by default unbound_server.pem. This file is generated by the <i>unbound-control-setup</i> utility. This file is used by the unbound server, and also by <i>unbound-control</i>.</p>
<dt><code>control-key-file: &lt;private key file&gt;</code></p>
<dd>Path to the control client private key, by default unbound_control.key. This file is generated by the <i>unbound-control-setup</i> utility. This file is used by <i>unbound-control</i>.</p>
<dt><code>control-cert-file: &lt;certificate file.pem&gt;</code></p>
<dd>Path to the control client certificate, by default unbound_control.pem. This certificate has to be signed with the server certificate. This file is generated by the <i>unbound-control-setup</i> utility. This file is used by <i>unbound-control</i>.</dl>
<h3>Stub Zone Options</h3>
<p>There may be multiple <code>stub-zone:</code> clauses. Each with a name: and zero or more hostnames or IP addresses. For the stub zone this list of nameservers is used. Class IN is assumed. The servers should be authority servers, not recursors; unbound performs the recursive processing itself for stub zones. </p>
<p> The stub zone can be used to configure authoritative data to be used by the resolver that cannot be accessed using the public internet servers. This is useful for company-local data or private zones. Setup an authoritative server on a different host (or different port). Enter a config entry for unbound with <code>stub-addr:</code> &lt;ip address of host[@port]&gt;. The unbound resolver can then access the data, without referring to the public internet for it. </p>
<p> This setup allows DNSSEC signed zones to be served by that authoritative server, in which case a trusted key entry with the public key can be put in config, so that unbound can validate the data and set the AD bit on replies for the private zone (authoritative servers do not set the AD bit). This setup makes unbound capable of answering queries for the private zone, and can even set the AD bit (&#8216;authentic&#8217;), but the AA (&#8216;authoritative&#8217;) bit is not set on these replies.</p>
<dl>
<dt><code>name: </code><i>&lt;domain name&gt;</i></p>
<dd>Name of the stub zone.</p>
<dt><code>stub-host: </code><i>&lt;domain name&gt;</i></p>
<dd>Name of stub zone nameserver. Is itself resolved before it is used.</p>
<dt><code>stub-addr: </code><i>&lt;IP address&gt;</i></p>
<dd>IP address of stub zone nameserver. Can be IP 4 or IP 6. To use a nondefault port for DNS communication append &#8216;@&#8217; with the port number.</p>
<dt><code>stub-prime: </code><i>&lt;yes or no&gt;</i></p>
<dd>This option is by default off. If enabled it performs NS set priming, which is similar to root hints, where it starts using the list of nameservers currently published by the zone. Thus, if the hint list is slightly outdated, the resolver picks up a correct list online.</p>
<dt><code>stub-first: </code><i>&lt;yes or no&gt;</i></p>
<dd>If enabled, a query is attempted without the stub clause if it fails. The data could not be retrieved and would have caused SERVFAIL because the servers are unreachable, instead it is tried without this clause. The default is no.</dl>
<h3>Forward Zone Options</h3>
<p>There may be multiple <code>forward-zone:</code> clauses. Each with a <code>name:</code> and zero or more hostnames or IP addresses. For the forward zone this list of nameservers is used to forward the queries to. The servers listed as <code>forward-host:</code> and <code>forward-addr:</code> have to handle further recursion for the query. Thus, those servers are not authority servers, but are (just like unbound is) recursive servers too; unbound does not perform recursion itself for the forward zone, it lets the remote server do it. Class IN is assumed. A forward-zone entry with name &quot;.&quot; and a forward-addr target will forward all queries to that other server (unless it can answer from the cache).</p>
<dl>
<dt><code>name: </code><i>&lt;domain name&gt;</i></p>
<dd>Name of the forward zone.</p>
<dt><code>forward-host: </code><i>&lt;domain name&gt;</i></p>
<dd>Name of server to forward to. Is itself resolved before it is used.</p>
<dt><code>forward-addr: </code><i>&lt;IP address&gt;</i></p>
<dd>IP address of server to forward to. Can be IP 4 or IP 6. To use a nondefault port for DNS communication append &#8216;@&#8217; with the port number.</p>
<dt><code>forward-first: </code><i>&lt;yes or no&gt;</i></p>
<dd>If enabled, a query is attempted without the forward clause if it fails. The data could not be retrieved and would have caused SERVFAIL because the servers are unreachable, instead it is tried without this clause. The default is no.</dl>
<h3>Python Module Options</h3>
<p>The <code>python:</code> clause gives the settings for the <i><a href="/docs/linux/man/1-python/">python</a></i>(1) script module. This module acts like the iterator and validator modules do, on queries and answers. To enable the script module it has to be compiled into the daemon, and the word &quot;python&quot; has to be put in the <code>module-config:</code> option (usually first, or between the validator and iterator).</p>
<dl>
<dt><code>python-script: </code><i>&lt;python file&gt;</i></p>
<dd>The script file to load.</dl>
<h2>Memory Control Example</h2>
<p>In the example config settings below memory usage is reduced. Some service levels are lower, notable very large data and a high TCP load are no longer supported. Very large data and high TCP loads are exceptional for the DNS. DNSSEC validation is enabled, just add trust anchors. If you do not have to worry about programs using more than 3 Mb of memory, the below example is not for you. Use the defaults to receive full service, which on BSD-32bit tops out at 30-40 Mb after heavy usage. </p>
<pre># example settings that reduce memory usage
server:
 num-threads: 1
 outgoing-num-tcp: 1 # this limits TCP service, uses less buffers.
 incoming-num-tcp: 1
 outgoing-range: 60 # uses less memory, but less performance.
 msg-buffer-size: 8192 # note this limits service, 'no huge stuff'.
 msg-cache-size: 100k
 msg-cache-slabs: 1
 rrset-cache-size: 100k
 rrset-cache-slabs: 1
 infra-cache-numhosts: 200
 infra-cache-slabs: 1
 key-cache-size: 100k
 key-cache-slabs: 1
 neg-cache-size: 10k
 num-queries-per-thread: 30
 target-fetch-policy: &quot;2 1 0 0 0 0&quot;
 harden-large-queries: &quot;yes&quot;
 harden-short-bufsize: &quot;yes&quot;</pre>
<h2>Files</h2>
<dl>
<dt><i>/etc/unbound</i></p>
<dd>default unbound working directory.</p>
<dt><i>/etc/unbound</i></p>
<dd>default <i><a href="/docs/linux/man/2-chroot/">chroot</a></i>(2) location.</p>
<dt><i>/etc/unbound/unbound.conf</i></p>
<dd>unbound configuration file.</p>
<dt><i>/var/run/unbound/unbound.pid</i></p>
<dd>default unbound pidfile with process ID of the running daemon.</p>
<dt><i>unbound.log</i></p>
<dd>unbound log file. default is to log to <i><a href="/docs/linux/man/3-syslog/">syslog</a></i>(3).</dl>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/8-unbound/">unbound</a></i>(8), <i><a href="/docs/linux/man/8-unbound-checkconf/">unbound-checkconf</a></i>(8).</p>
<h2>Authors</h2>
<p><code>Unbound </code> was written by NLnet Labs. Please see CREDITS file in the distribution for further details.</p>
