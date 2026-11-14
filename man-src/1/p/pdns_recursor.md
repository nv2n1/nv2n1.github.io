---
title: "pdns_recursor(1)"
name: "pdns_recursor"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pdns_recursor/"
description: "pdns_recursor – high-performance, simple and secure recursing nameserver"
---

<h2>NAME</h2>
<p> pdns_recursor &#8211; high-performance, simple and secure recursing nameserver</p>
<h2>SYNOPSIS</h2>
<p> pdns_recursor [OPTION]&#8230;</p>
<h2>DESCRIPTION</h2>
<p> <a href="/docs/linux/man/1-pdns_recursor/">pdns_recursor</a>(1) is a high performance, simple and secure recursing nameserver. It currently powers over two million internet connections. </p>
<p> The recursor is configured via a configuration file, but each item in that file can be overridden on the command line. </p>
<p> This manpage lists the core set of features needed to get the PowerDNS recursor working, for full and up to date details head to <a rel="nofollow" href="http://doc.powerdns.com/built-in-recursor.html">http://doc.powerdns.com/built-in-recursor.html</a></p>
<h2>EXAMPLES</h2>
<p> To listen on 192.0.2.53 and allow the 192.0.2.0/24 subnet to recurse, and run as a daemon, execute: </p>
<p> #&nbsp;<wbr>pdns_recursor &#8211;local-address=192.0.2.53 &#8211;allow-from=192.0.2.0/24 &#8211;daemon </p>
<p> To stop the recursor by hand, run: </p>
<p> #&nbsp;<wbr>rec_control quit </p>
<p> However, the recommended way of starting and stopping the recursor is to use the init.d script provided.</p>
<h2>OPTIONS</h2>
<p> For authoritative listing of options, consult the online documentation at <a rel="nofollow" href="http://doc.powerdns.com/md/recursor/settings/">http://doc.powerdns.com/md/recursor/settings/</a></p>
<dl>
<dt><code>&#8211;aaaa-additional-processing</code></p>
<dd> Turn on to do AAAA additional processing (slow).</p>
<dl>
<dt>
<dd></dl>
<dt><code>&#8211;allow-from=</code>NETWORK[,NETWORK]&#8230;</p>
<dd> If set, only allow these comma separated NETWORKs, with network mask to recurse. For example: 192.0.2.0/24,203.0.113.128/25.</p>
<dl>
<dt>
<dd></dl>
<dt><code>&#8211;auth-can-lower-ttl</code></p>
<dd> Authoritative zones can transmit a TTL value that is lower than that specified in the parent zone. This is called a &#8216;delegation inconsistency&#8217;. To follow RFC 2181 paragraphs 5.2 and 5.4 to the letter, enable this feature. This will mean a slight deterioration of performance, and it will not solve any problems, but does make the recursor more standards compliant. Not recommended unless you have to tick an &#8216;RFC 2181 compliant&#8217; box. Off by default.</p>
<dl>
<dt>
<dd></dl>
<dt><code>&#8211;auth-zones=</code>ZONENAME=FILENAME[,ZONENAME=FILENAME]&#8230;</p>
<dd> Serve ZONENAME from FILENAME authoritatively. For example: ds9a.nl=/var/zones/ds9a.nl,powerdns.com=/var/zones/powerdns.com.</p>
<dl>
<dt>
<dd></dl>
<dt><code>&#8211;chroot=</code>DIRECTORY</p>
<dd> chroot the process to DIRECTORY.</p>
<dl>
<dt>
<dd></dl>
<dt><code>&#8211;client-tcp-timeout=</code>NUM</p>
<dd> Timeout in seconds when talking to TCP clients.</p>
<dl>
<dt>
<dd></dl>
<dt><code>&#8211;config-dir=</code>DIRECTORY</p>
<dd> Location of configuration directory (recursor.conf), /etc/powerdns by default.</p>
<dl>
<dt>
<dd></dl>
<dt><code>&#8211;daemon</code></p>
<dd> Operate as a daemon.</p>
<dl>
<dt>
<dd></dl>
<dt><code>&#8211;delegation-only</code></p>
<dd> Which domains we only accept delegations from (a Verisign special).</p>
<dl>
<dt>
<dd></dl>
<dt><code>&#8211;entropy-source=</code>FILE</p>
<dd> Read new entropy from FILE, defaults to /dev/urandom.</p>
<dl>
<dt>
<dd></dl>
<dt><code>&#8211;export-etc-hosts</code></p>
<dd> If set, this flag will export the hostnames and IP addresses mentioned in /etc/hosts.</p>
<dl>
<dt>
<dd></dl>
<dt><code>&#8211;fork</code></p>
<dd> If set, fork the daemon for possible double performance.</p>
<dl>
<dt>
<dd></dl>
<dt><code>&#8211;forward-zones=</code>ZONENAME=ADDRESS[,ZONENAME=ADDRESS]&#8230;</p>
<dd> Queries for ZONENAME will be forwarded to ADDRESS. ADDRESS should be an IP address, not a hostname (to prevent chicken and egg problems). Example: forward-zones= ds9a.nl=213.244.168.210, powerdns.com=127.0.0.1.</p>
<dl>
<dt>
<dd></dl>
<dt><code>&#8211;forward-zones-file=</code>FILENAME</p>
<dd> Similar to &#8211;forward-zones, but read the options from FILENAME. FILENAME should contain one zone per line, like: ds9a.nl=213.244.168.210.</p>
<dl>
<dt>
<dd></dl>
<dt><code>&#8211;help</code></p>
<dd> Show a summary of options.</p>
<dl>
<dt>
<dd></dl>
<dt><code>&#8211;hint-file=</code>FILENAME</p>
<dd> Load root hints from this FILENAME</p>
<dl>
<dt>
<dd></dl>
<dt><code>&#8211;local-address=</code>ADDRESS[,ADDRESS]&#8230;</p>
<dd> Listen on ADDRESS, separated by spaces or commas.</p>
<dl>
<dt>
<dd></dl>
<dt><code>&#8211;local-port=</code>PORT</p>
<dd> Listen on PORT.</p>
<dl>
<dt>
<dd></dl>
<dt><code>&#8211;log-common-errors</code></p>
<dd> If we should log rather common errors.</p>
<dl>
<dt>
<dd></dl>
<dt><code>&#8211;max-cache-entries=</code>NUM</p>
<dd> Maximum number of entries in the main cache.</p>
<dl>
<dt>
<dd></dl>
<dt><code>&#8211;max-negative-ttl=</code>NUM</p>
<dd> maximum number of seconds to keep a negative cached entry in memory.</p>
<dl>
<dt>
<dd></dl>
<dt><code>&#8211;max-tcp-clients=</code>NUM</p>
<dd> Maximum number of simultaneous TCP clients.</p>
<dl>
<dt>
<dd></dl>
<dt><code>&#8211;max-tcp-per-client</code></p>
<dd> If set, maximum number of TCP sessions per client (IP address).</p>
<dl>
<dt>
<dd></dl>
<dt><code>&#8211;query-local-address=</code>ADDRESS</p>
<dd> Use ADDRESS as Source IP address when sending queries.</p>
<dl>
<dt>
<dd></dl>
<dt><code>&#8211;query-local-address6=</code>ADDRESS</p>
<dd> Send out local IPv6 queries from ADDRESS. Disabled by default, which also disables outgoing IPv6 support. A useful setting is &#8216;::0&#8217;.</p>
<dl>
<dt>
<dd></dl>
<dt><code>&#8211;quiet</code></p>
<dd> Suppress logging of questions and answers.</p>
<dl>
<dt>
<dd></dl>
<dt><code>&#8211;remotes-ringbuffer-entries=</code>NUM</p>
<dd> maximum number of packets to store statistics for.</p>
<dl>
<dt>
<dd></dl>
<dt><code>&#8211;server-id=</code>TEXT</p>
<dd> Return TEXT when queried for &#8216;server.id&#8217; TXT, defaults to hostname.</p>
<dl>
<dt>
<dd></dl>
<dt><code>&#8211;serve-rfc1918</code></p>
<dd> On by default, this makes the server authoritatively aware of: 10.in-addr.arpa, 168.192.in-addr.arpa and 16-31.172.in-addr.arpa, which saves load on the AS112 servers. Individual parts of these zones can still be loaded or forwarded.</p>
<dl>
<dt>
<dd></dl>
<dt><code>&#8211;setgid=</code>GID</p>
<dd> If set, change group id to GID for more security.</p>
<dl>
<dt>
<dd></dl>
<dt><code>&#8211;setuid=</code>UID</p>
<dd> If set, change user id to UID for more security.</p>
<dl>
<dt>
<dd></dl>
<dt><code>&#8211;single-socket</code></p>
<dd> If set, only use a single socket for outgoing queries.</p>
<dl>
<dt>
<dd></dl>
<dt><code>&#8211;socket-dir=</code>DIRECTORY</p>
<dd> The controlsocket will live in DIRECTORY.</p>
<dl>
<dt>
<dd></dl>
<dt><code>&#8211;spoof-nearmiss-max=</code>NUM</p>
<dd> If non-zero, assume spoofing after this many near misses.</p>
<dl>
<dt>
<dd></dl>
<dt><code>&#8211;trace</code></p>
<dd> if we should output heaps of logging.</p>
<dl>
<dt>
<dd></dl>
<dt><code>&#8211;version-string=</code>TEXT</p>
<dd> TEXT will be reported on version.pdns or version.bind queries.</p>
<dl>
<dt>
<dd></dl>
</dl>
<h2>BUGS</h2>
<p> None known. File new ones at <a rel="nofollow" href="https://github.com/PowerDNS/pdns/issues.">https://github.com/PowerDNS/pdns/issues.</a></p>
<h2>RESOURCES</h2>
<p> Website: <a rel="nofollow" href="http://www.powerdns.com,">http://www.powerdns.com,</a> <a href="https://github.com/PowerDNS/pdns">https://github.com/PowerDNS/pdns</a></p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-rec_control/">rec_control</a>(1)</p>
<h2>AUTHORS</h2>
<p> PowerDNS.COM BV. </p>
<h2>Index</h2>
