---
title: "rbldnsd(8)"
name: "rbldnsd"
section: "8"
letter: "r"
url: "/docs/linux/man/8-rbldnsd/"
description: "rbldnsd – DNS daemon suitable for running DNS-based blocklists"
---

<p>rbldnsd &#8211; DNS daemon suitable for running DNS-based blocklists</p>
<h2>Synopsis</h2>
<p><code>rbldnsd</code> options <i>zone</i>:<i>dataset</i>&#8230; </p>
<h2>Description</h2>
<p><code>rbldnsd</code> is a small DNS-protocol daemon which is designed to handle queries to DNS-based IP-listing or NAME-listing services. Such services are a simple way to share/publish a list of IP addresses or (domain) names which are &quot;listed&quot; for for some reason, for example in order to be able to refuse a service to a client which is &quot;listed&quot; in some blocklist. <code>rbldnsd</code> is not a general-purpose nameserver. It will answer to A and TXT (and SOA and NS if such RRs are specified) queries, and has limited ability to answer to some other types of queries. <code>rbldnsd</code> tries to handle data from two different perspectives: given a set (or several) of &quot;listed entries&quot; (e.g. IP address ranges or domain names), it builds and serves a DNS zone. Note the two are not the same: list of spammer&#8217;s IPs is NOT a DNS zone, but may be represented and used as such, provided that some additional information necessary to build complete DNS zone (e.g. NS and SOA records, maybe A records necessary for http to work) is available. In this context, <code>rbldnsd</code> is very different from other general-purpose nameservers such as BIND or NSD: <code>rbldnsd</code> operates with <i>datasets</i> (sets of entries &#8211; IP addresses or domain names, logically grouped together), while other general-purpose nameservers operates with zones. The way how <code>rbldnsd</code> operates may be somewhat confusing to BIND experts. For <code>rbldnsd</code>, a building block is a dataset: e.g., set of insecure/abuseable hosts (IP addresses), set of network ranges that belongs to various spam operations (IP ranges), domain names that belong to spammers (RHSBL) and so on. Usually, different kind of information is placed into separate file, for easy maintenance. From a number of such datasets, <code>rbldnsd</code> constructs a number of DNS zones as specified on command line. A single dataset may be used for several zones, and a single zone may be constructed from several datasets. <code>rbldnsd</code> will answer queries to DNS zones specified on the command line as a set of zone specifications. Each zone specification consists of zone basename, dataset type and a comma-separated list of files that forms a given dataset: <i>zone</i>:<i>type</i>:<i>file</i>,<i>file</i>,&#8230; Several zones may be specified in command line, so that <code>rbldnsd</code> will answer queries to any of them. Also, a single zone may be specified several times with different datasets, so it is possible to form a zone from a combination of several different dataset. The same dataset may be reused for several zones too (and in this case, it will be read into memory only once). There are several dataset formats available, each is suitable and optimized (in terms of memory, speed and ease of use) for a specific task. Available dataset types may be grouped into the following categories:</p>
<dl>
<dd>lists of IP addresses. When a query is done to a zone with such data, query is interpreted as an IP address in a reverse form (similar to in-addr.arpa zone). If the address is found in dataset data, <code>rbldnsd</code> will return A and TXT records specified in data for that IP. This is a classical IP-based blocklist.</p>
<dd>lists of domain names. Similar to list of IP addresses, but with generic domain names instead of IPs (wildcards allowed). This type of data may be used to form a blocklist of e.g. sender domain names.</p>
<dd>generic list of various types of records, as an auxilary data to form a complete nameserver. This format is similar to bind-style datafiles, but very simplified. One may specify A, TXT, NS and MX records here.</p>
<dd>combined set, different datasets from the list above combined in the single (set of) source files, for easy maintenance.</p>
<dd>acl, or Access Control List. This is a pseudo dataset, that works by overweriting query results based on the requestor (peer) IP address. </p>
<h2>Options</h2>
<p>The following options may be specified: </p>
<dl>
<dt><code>-u</code> <i>user</i>[:<i>group</i>]</p>
<dd><code>rbldnsd</code> will change its userid to the specified <i>user</i>, which defaults to <code>rbldns</code>, and <i>group</i>, which by default is the primary group of a <i>user</i>. <code>rbldnsd</code> will refuse to run as the root user, since this is insecure. </p>
<dt><code>-r</code> <i>rootdir</i></p>
<dd><code>rbldnsd</code> will chroot to <i>rootdir</i> if specified. Data files should be available inside <i>rootdir</i>. </p>
<dt><code>-w</code> <i>workdir</i></p>
<dd><code>rbldnsd</code> will change its working directory to <i>workdir</i> (after chrooting to <i>rootdir</i> if <code>-r</code> option is also specified). May be used to shorten filename paths. </p>
<dt><code>-b</code> <i>address</i>/<i>port</i></p>
<dd>This option is <i>required</i>. <code>rbldnsd</code> will bind to specified <i>address</i> and <i>port</i> (port defaults to port 53, domain). Either numeric IP address or a hostname may be specified, and either port number or service name is accepted. It is possible to specify several addresses to listen on this way, by repeating <code>-b</code> option. Additionally, if there are several addresses listed for a hostname, <code>rbldnsd</code> will listen on all of them. Note that <code>rbldnsd</code> will work slightly faster if only one listening address is specified. Note the delimiter between host and port is a slash (/), not a colon, to be able to correctly handle IPv6 addresses. </p>
<dt><code>-4</code></p>
<dd>Use IPv4 listening socket/transport, do not attempt to use IPv6 (ignored if <code>rbldnsd</code> was built without IPv6 support). </p>
<dt><code>-6</code></p>
<dd>Use IPv6 listening socket/transport, do not attempt to use IPv4 (this option will be reported as error if IPv6 support was not compiled in). </p>
<dt><code>-t</code> <i>defttl</i>:<i>minttl</i>:<i>maxttl</i></p>
<dd>Set default reply time-to-live (TTL) value to be <i>defttl</i>, and set constraints for TTL to <i>minttl</i> and <i>maxttl</i>. Default applies when there&#8217;s no TTL defined in a given scope (in data file), and constraints are applied when such value provided in data. Any of the values may be omitted, including trailing colon (:) characters, e.g. &quot;<code>-t</code>&nbsp;<wbr>30&quot; set default TTL to be 30 secound, and &quot;<code>-t</code>&nbsp;<wbr>::120&quot; or &quot;<code>-t</code>&nbsp;<wbr>::2m&quot; sets maximum allowed TTL to 2 minutes. All 3 values are in time units, with optional suffix: <code>s</code> (secounds, default), <code>m</code> (minutes), <code>h</code> (hours), <code>d</code> (days) or <code>w</code> (weeks). Zero <i>minttl</i> or maxttl means no corresponding constraint will be enforced. Default <i>defttl</i> is 35m. </p>
<dt><code>-c</code> <i>check</i></p>
<dd>Set interval between checking for zone file changes to be <i>check</i>, default is 1m (one minute). <code>rbldnsd</code> will check zone file&#8217;s last modification time every so often, and if it detects a change, zone will be automatically reloaded. Setting this value to 0 disables automatic zone change detection. This procedure may also be triggered by sending a SIGHUP signal to <code>rbldnsd</code> (see SIGNALS section below). </p>
<dt><code>-e</code></p>
<dd>Allow non-network addresses to be used in CIDR ranges. Normally, <code>rbldnsd</code> rejects addresses such as 127.2.3.4/24, where prefix is not within the network mask derived from bit number (in this case, correct form is 127.2.3.0/24, note the trailing zero in prefix). This is done in order to catch possible typos in zones (<code>rbldnsd</code> will warn about a problem and will ignore such entry). This option disables checking whether the CIDR prefix fits within the network mask. </p>
<dt><code>-q</code></p>
<dd>Quick and quiet start. Normally, <code>rbldnsd</code> does socket initialization and zone load in foreground, writing progress and statistic to standard output, and aborts in case of any errors. With this flag, nothing will be printed and first zone load will be done in background (unless <code>-n</code> option is also given), and zone load errors will be non-fatal. </p>
<dt><code>-p</code> <i>pidfile</i></p>
<dd>Write rbldnsd&#8217;s pid to the specified <i>pidfile</i>, so it will be easily findable. This file gets written before entering a chroot jail (if specified) and before changing userid, so it&#8217;s ok to specify e.g. /var/run/rbldnsd.pid here. </p>
<dt><code>-l</code> <i>logfile</i></p>
<dd>Specifies a file to which log all requests made. This file is created after entering a chroot jail and becoming a user. Logfiles may be quite large, esp. on busy sites (<code>rbldnsd</code> will log <i>every</i> recognized request if this option is specified). This option is mainly intended for debugging purposes. Upon receiption of SIGHUP signal, <code>rbldnsd</code> reopens its logfile. If <i>logfile</i> prefixed with a plus sign (+), logging will not be buffered (i.e. each line will be flushed to disk); by default, logging is buffered to reduce system load. Specify a single hyphen (-) as a filename to log to standard output (filedescriptor 1), either buffered by default, or line-buffered if specified as `+-&#8216; (standard output will not be &quot;reopened&quot; upon receiving SIGHUP signal, but will be flushed in case logging is buffered). </p>
<dt><code>-s</code> <i>statsfile</i></p>
<dd>Specifies a file where <code>rbldnsd</code> will write a line with short statistic summary of queries made per zone, every check (<code>-c</code>) interval. Format of each line is: </p>
<pre> <i>timestamp</i> <i>zone</i>:<i>qtot</i>:<i>qok</i>:<i>qnxd</i>:<i>bin</i>:<i>bout</i> <i>zone</i>:...</pre>
<p>where <i>timestamp</i> is unix time (secounds since epoch), <i>zone</i> is the name of the base zone, <i>qtot</i> is the total number of queries received, <i>qok</i> &#8211; number of positive replies, <i>qnxd</i> &#8211; number of NXDOMAIN replies, <i>bin</i> is the total number of bytes read from network (excluding IP/UDP overhead and dropped packets), <i>bout</i> is the total number of bytes written to network. Ther are as many such tuples as there are zones, and one extra, total typle at the end, with <i>zone</i> being &quot;*&quot;, like: </p>
<pre> 1234 bl1.ex:10:5:4:311:432 bl2.ex:24:13:7:248:375 *:98:35:12:820:987</pre>
<p>Note the total values may be larger than the sum of per-zone values, due to queries made against unlisted zones, or bad/broken packets. </p>
<p> <code>Rbldnsd</code> will write bare timestamp to <i>statsfile</i> when it is starting up, shutting down or when statistic counters are being reset after receiving SIGUSR2 signal (see below), to indicate the points where the counters are starting back from zero. </p>
<p> By default, <code>rbldnsd</code> writes absolute counter values into <i>statsfile</i> (number of packets (bytes) since startup or last reset). <i>statsfile</i> may be prefixed with plus sign (+), in which case <code>rbldnsd</code> will write delta values, that is, number of packets or bytes since last write, or number of packets (bytes) per unit of time (&quot;incremental&quot; mode, hence the &quot;+&quot; sign). </p>
<dt><code>-n</code></p>
<dd>Do not become a daemon. Normally, <code>rbldnsd</code> will fork and go to the background after successful initialization. This option disables this behaviour. </p>
<dt><code>-f</code></p>
<dd>Request <code>rbldnsd</code> to continue processing requests during data reloads. <code>Rbldnsd</code> forks a child process to handle requests while parent reloads the data. This ensures smooth operations, but requires more memory, since two copies of data is keept in memory during reload process. </p>
<dt><code>-d</code></p>
<dd>Dump all zones to stdout in BIND format and exit. This may be suitable to convert easily editable rbldnsd-style data into BIND zone. <code>rbldnsd</code> dumps all zones as one stream, so one may want to specify only one zone with <code>-d</code>. Zone file will have appropriate $ORIGIN tags. Note that data generated may be really huge (as BIND format isn&#8217;t appropriate for this sort of things), and some entries may not be really the same in BIND as in <code>rbldnsd</code> (e.g., IP netblocks of large size will be represented as wildcard entries &#8211; 10.0.0.0/8 will become *.10; excluded entries will be represented by a CNAME to `excluded&#8217; name, so such name should not be present in a data set). In this mode, <code>rbldnsd</code> ignores <code>-r</code> (root directory) option. </p>
<dt><code>-v</code></p>
<dd>Do not show exact version information in response to version.bind CH TXT queries (by default <code>rbldnsd</code> responds to such queries since version 0.98). With single <code>-v</code>, <code>rbldnsd</code> will only return &quot;rbldnsd&quot; to the caller, without the version number. Second <code>-v</code> disables providing any information in response to such requests, i.e. <code>rbldnsd</code> will return REFUSE code. </p>
<dt><code>-C</code></p>
<dd>Disable automatic on-the-fly uncompression of data files if this feature is compiled in (see below). </p>
<dt><code>-A</code></p>
<dd>
<dt><code>-a</code></p>
<dd>Controls &quot;laziness&quot; of <code>rbldnsd</code> when constructing replies. With <code>-a</code> specified, <code>rbldnsd</code> does not add AUTH section (containing NS records) to replies unless explicitly asked for NS records. It is equivalent to BIND9 &quot;minimal-answers&quot; configuration setting. While with <code>-A</code> specified, <code>rbldnsd</code> will always fill in AUTH section, increasing size of replies dramatically but allowing (caching) resolver clients to react faster to changes in nameserver lists. Currently (as of 0.998 version), non-lazy (as with <code>-A</code>) mode is the default, but it will change in future release. </p>
<dt><code>-x</code> <i>extension</i></p>
<dd>Load the given <i>extension</i> file (a dynamically-linked library, usually with &quot;.so&quot; suffix). This allows to gather custom statistics or perform other custom tasks. See separate document for details about building and using extensions. This feature is not available on all platforms, and can be disabled at compile time. </p>
<dt><code>-X</code> <i>extarg</i></p>
<dd>Pass the given argument, <i>extarg</i>, to the extension loaded with <code>-x</code>. </p>
</dl>
<h2>Dataset Types And Formats</h2>
<p>Dataset files are text files which are interpreted depending on type specified in command line. Empty lines and lines starting with hash character (#) or semicolon (;) are ignored, except for a special case outlined below in section titled &quot;Special Entries&quot;. </p>
<p> A (comma-separated) list of files in dataset specification (in <i>type</i>:<i>file</i>,<i>file</i>,&#8230;) is interpreted as if all files where logically combined into one single file. </p>
<p> When compiled with zlib support, <code>rbldnsd</code> is able to read gzip-compressed data files. So, every <i>file</i> in dataset specification can be compressed with <code><a href="/docs/linux/man/1-gzip/">gzip</a></code>(1), and <code>rbldnsd</code> will read such a file decompressing it on-the-fly. This feature may be turned off by specifying <code>-C</code> option. </p>
<p> <code>rbldnsd</code> is designed to service a DNSBL, where each entry have single A record and optional TXT record assotiated with it. <code>rbldnsd</code> allows to specify A value and TXT <i>template</i> either for each entry individually, or to use default A value and TXT template pair for a group of entries. See section &quot;Resulting A values and TXT templates&quot; below for a way to specify them.</p>
<h3>Special Entries</h3>
<p>If a line starts with a dollar sign ($), hash character and a dollar sign (#$), semicolon and dollar sign (;#) or colon and a dollar sign (:$), it is interpreted in a special way, regardless of dataset type (this is one exception where a line starting with hash character is not ignored &#8211; to be able to use zone files for both <code>rbldnsd</code> and for DJB&#8217;s rbldns). The following keywords, following a dollar sign, are recognized: </p>
<dl>
<dt><code>$SOA</code> <i>ttl origindn persondn serial refresh retry expire minttl</p>
<dd>Specifies SOA (Start Of Authority) record for all zones using this dataset. Only first SOA record is interpreted. This is the only way to specify SOA &#8211; by default, </i><code>rbldnsd</code> will not add any SOA record into answers, and will REFUSE to answer to certain queries (notably, SOA query to zone&#8217;s base domain name). It is recommended, but not mandatory to specify SOA record for every zone. If no SOA is given, negative replies will not be cacheable by caching nameservers. Only one, first $SOA line is recognized in every dataset (all subsequent $SOA lines encountered in the same dataset are silently ignored). When constructing a zone, SOA will be taken from <i>first</i> dataset where $SOA line is found, in an order as specified in command line, subsequent $SOA lines, if any, are ignored. This way, one may overwrite $SOA found in 3rd party data by <i>prepending</i> small local file to the dataset in question, listing it before any other files.</p>
<dd>If <i>serial</i> value specified is zero, timestamp of most recent modified file will be substituted as <i>serial</i>.</p>
<dd>If <i>ttl</i> field is zero, default ttl (<code>-t</code> option or last <code>$TTL</code> value, see below) will be used.</p>
<dd>All time fields (ttl, refresh, retry, expire, minttl) may be specified in time units. See <code>-t</code> option for details. </p>
<dt><code>$NS</code> <i>ttl</i> <i>nameserverdn</i> <i>nameserverdn&#8230;</p>
<dd>Specifies NS (Name Server) records for all zones using this dataset. Only first $NS line in a dataset is recognized, all subsequent lines are silently ignored. When constructing a zone from several datasets, rbldnsd uses nameservers from $NS line in only first dataset where $NS line is given, in command-line order, just like for $SOA record. Only first 32 namservers are recognized. Individual nameserver(s) may be prefixed with a minus sign (-), which means this single nameserver will be ignored by </i><code>rbldnsd</code>. This is useful to temporary comment out one nameserver entry without removing it from the list. If <i>ttl</i> is zero, default ttl will be used. The list of NS records, just like $SOA value, are taken from the <i>first</i> data file in a dataset where the $NS line is found, subsequent $NS lines, if any, are ignored. </p>
<dt><code>$TTL</code> <i>time-to-live</i></p>
<dd>Specifies TTL (time-to-live) value for all records in current dataset. See also <code>-t</code> option. <code>$TTL</code> special overrides <code>-t</code> value on a per-dataset basis. </p>
<dt><code>$TIMESTAMP</code> <i>dstamp</i> [<i>expires</i>]</p>
<dd>(experimental) Specifies the data timestamp <i>dstamp</i> when the data has been generated, and optionally when it will expire. The timestamps are in form <i>yyyy</i>:<i>mm</i>:<i>dd</i>[:<i>hh</i>[:<i>mi</i>[:<i>ss</i>]]], where <i>yyyy</i> is the year like 2005, <i>mm</i> is the month number (01..12), <i>dd</i> is the month day number (01..31), <i>hh</i> is hour (00..23), <i>mi</i> and <i>ss</i> are minutes and secounds (00.59); hours, minutes and secounds are optional and defaults to 0; the delimiters (either colon or dash may be used) are optional too, but are allowed for readability. Also, single zero (0) or dash (-) may be used as <i>dstamp</i> and/or <i>expires</i>, indicating the value is not given. <i>expires</i> may also be specified as <code>+</code><i>rel</i>, where <i>rel</i> is a time specification (probably with suffix like s, m, h, d) as an offset to <i>dstamp</i>. <code>rbldnsd</code> compares <i>dstamp</i> with current timestamp and refuses to load the file if <i>dstamp</i> specifies time in the future. And if <i>expires</i> is specified, <code>rbldnsd</code> will refuse to service requests for that data if current time is greather than the value specified in <i>expires</i> field.</p>
<dd>Note that <code>rbldnsd</code> will check the data expiry time every time it checks for data file updates (when receiving SIGHUP signal or every <code>-c</code> interval). If automatic data reload timer (<code>-c</code> option) is disabled, zones will not be exipired automatically. </p>
<dt><code>$MAXRANGE4</code> <i>range-size</i></p>
<dd>Specifies maximum size of IPv4 range allowed for IPv4-based datasets. If an entry covers more IP addresses than <i>range-size</i>, it will be ignored (and a warning will be logged). <i>range-size</i> may be specified as a number of hosts, like 256, or as network prefix lenght, like /24 (the two are the same): </p>
<pre> $MAXRANGE4 /24
 $MAXRANGE4 256</pre>
<p>This constraint is active for a dataset it is specified in, and can be owerwritten (by subsequent $MAXRANGE statement) by a smaller value, but can not be increased. </p>
<dt><code>$</code><i>n</i> <i>text</i></p>
<dd>(<i>n</i> is a single digit). Specifies a <i>substitution variable</i> for use as $<i>n</i> placeholders (the <code>$</code><i>n</i> entries are ignored in generic daaset). See section &quot;Resulting A values and TXT templates&quot; below for description and usage examples. </p>
<dt><code>$=</code> <i>text</i></p>
<dd>Set the base template for all individual TXT records. See section &quot;Resulting A values and TXT templates&quot; below for more information. </p>
</dl>
<h3>ip4set Dataset</h3>
<p>A set of IP addresses or CIDR address ranges, together with A and TXT resulting values. IP addresses are specified one per line, by an IP address prefix (initial octets), complete IP address, CIDR range, or IP prefix range (two IP prefixes or complete addresses delimited by a dash, inclusive). Examples, to specify 127.0.0.0/24: </p>
<pre> 127.0.0.0/24
 127.0.0
 127/24
 127-127.0.0
 127.0.0.0-127.0.0.255
 127.0.0.1-255</pre>
<p>to specify 127.16.0.0-127.31.255.255: </p>
<pre> 127.16.0.0-127.31.255.255
 127.16.0-127.31.255
 127.16-127.31
 127.16-31
 127.16.0.0/12
 127.16.0/12
 127.16/12</pre>
<p>Note that in prefix range, last boundary is completed with all-ones (255), not all-zeros line with first boundary and a prefix alone. In prefix ranges, if last boundary is only one octet (127.16-31), it is treated as &quot;suffix&quot;, as value of last <i>specified</i> octet of the first boundary prefix (127.16.0-31 is treated as 127.16.0.0-127.16.31.255, i.e. 127.16.0.0/19). </p>
<p> After an IP address range, A and TXT values for a given entry may be specified. If none given, default values in current scope (see below) applies. If a value starts with a colon, it is interpreted as a pair of A record and TXT template, delimited by colon (:127.0.0.2:This entry is listed). If a value does not start with a colon, it is interpreted as TXT template only, with A record defaulting to the default A value in current scope. </p>
<p> IP address range may be followed by a comment char (either hash character (#) or semicolon (;)), e.g.: </p>
<pre> 127/8 ; loopback network</pre>
<p>In this case all characters up to the end of line are ignored, and default A and TXT values will be used for this IP range. </p>
<p> Every IP address that fits within any of specified ranges is &quot;listed&quot;, and <code>rbldnsd</code> will respond to reverse queries against it within specified zone with positive results. In contrast, if an entry starts with an exclamation sign (!), this is an <i>exclusion</i> entry, i.e. corresponding address range is excluded from being listed (and any value for this record is ignored). This may be used to specify large range except some individual addresses, in a compact form. </p>
<p> If a line starts with a colon (:), this line specifies the default A value and TXT template to return (see below) for all subsequent entries up to end of current file. If no default entry specified, and no value specified for a given record, <code>rbldnsd</code> will return 127.0.0.2 for matching A queries and no record for matching TXT queries. If TXT record template is specified and contains occurences of of dollar sign ($), every such occurence is replaced with an IP address in question, so singe TXT template may be used to e.g. refer to a webpage for an additional information for a specific IP address.</p>
<h3>ip4trie Dataset</h3>
<p>Set of IP4 CIDR ranges with corresponding (A, TXT) values. This dataset is similar to ip4set, but uses a different internal representation. It accepts CIDR ranges only (not a.b.c.d-e.f.g.h), and allows for the specification of A/TXT values on a per CIDR range basis. (If multiple CIDR ranges match a query, the value for longest matching prefix is returned.) Exclusions are supported too. </p>
<p> This dataset is not particularly memory-efficient for storing many single IP addresses &#8212; it uses about 50% more memory than the ip4set dataset in that case. The ip4trie dataset is better adapted, however, for listing CIDR ranges (whose lengths are not a multiple of 8 bits.)</p>
<h3>ip4tset Dataset</h3>
<p>&quot;trivial&quot; ip4set: a set of single IP addresses (one per line), with the same A+TXT template. This dataset type is more efficient than ip4set (in both memory usage and access times), but have obvious limitation. It is intended for DNSBLs like DSBL.org, ORDB.org and similar, where each entry uses the same default A+TXT template. This dataset uses only half a memory for the same list of IP addresses compared to <code>ip4set</code>.</p>
<h3>ip6trie Dataset</h3>
<p>Set of IP6 CIDR ranges. This is the IP6 equivalent of the ip4trie dataset. It allows the sepecification of individual A/TXT values for each CIDR range and supports exclusions. Compressed (&quot;::&quot;) ip6 notation is supported. </p>
<p> Example zone data: </p>
<pre> # Default A and TXT template valuse
 :127.0.1.2: Listed, see <a rel="nofollow" href="http://example.com/lookup?$">http://example.com/lookup?$</a>
 # A listing, note that trailing :0s can be omitted
 2001:21ab:c000/36
 # /64 range with non-default A and TXT values
 2001:21ab:def7:4242 :127.0.1.3: This one smells funny
 # compressed notation
 2605:6001:42::/52
 ::1 # localhost
 !2605:6001:42::bead # exclusion</pre>
<h3>ip6tset Dataset</h3>
<p>&quot;Trivial&quot; ip6 dataset: a set of /64 IP6 CIDR ranges (one per line), all sharing a single A+TXT template. Exclusions of single IP6 (/128) addresses are also supported. This dataset type is quite memory-efficient &#8212; it uses about 40% of the memory that the ip6trie dataset would use &#8212; but has obvious limitations. </p>
<p> This dataset wants the /64s listed as four ip6 words, for example: </p>
<pre> 2001:20fe:23:41ed
 abac:adab:ad00:42f</pre>
<p>Exclusions are denoted with a leading exclamation mark. You may also use compressed &quot;::&quot; notation for excluded addresses. E.g.: </p>
<pre> !abac:adab:ad00:42f:face:0f:a:beef
 !abac:adab:ad00:42f::2</pre>
<h3>dnset Dataset</h3>
<p>Set of (possible wildcarded) domain names with associated A and TXT values. Similar to <code>ip4set</code>, but instead of IP addresses, data consists of domain names (<i>not</i> in reverse form). One domain name per line, possible starting with wildcard (either with star-dot (*.) or just a dot). Entry starting with exclamation sign is exclusion. Default value for all subsequent lines may be specified by a line starting with a colon. </p>
<p> Wildcards are interpreted as follows:</p>
<dl>
<dt>example.com</p>
<dd>only example.com domain is listed, not subdomains thereof. Not a wildcard entry.</p>
<dt>*.example.com</p>
<dd>all subdomains of example.com are listed, but not example.com itself.</p>
<dt>.example.com</p>
<dd>all subdomains of example.com <i>and</i> example.com itself are listed. This is a shortcut: to list a domain name itself and all it&#8217;s subdomains, one may either specify two lines (example.com and *.example.com), or one line (.example.com).</dl>
<p> This dataset type may be used instead of <code>ip4set</code>, provided all CIDR ranges are expanded and reversed (but in this case, TXT template will be expanded differently).</p>
<h3>generic Dataset</h3>
<p>Generic type, simplified bind-style format. Every record should be on one line (line continuations are not supported), and should be specified completely (i.e. all domain names in values should be fully-qualified, entry name may not be omitted). No wildcards are accepted. Only A, TXT, and MX records are recognized. TTL value may be specified before record type. Examples:</p>
<dl>
<dd>
<pre> # bl.ex.com
 # specify some values for current zone
 $NS 0 ns1.ex.com ns2.ex.com
 # record with TTL
 www 3000 A 127.0.0.1
 about TXT &quot;ex.com combined blocklist&quot;</pre>
</dl>
<h3>combined Dataset</h3>
<p>This is a special dataset that stores no data by itself but acts like a container for several other datasets of any type except of combined type itself. The data file contains an optional common section, where various specials are recognized like $NS, $SOA, $TTL (see above), and a series of sections, each of which defines one (nested) dataset and several subzones of the base zone, for which this dataset should be consulted. New (nested) dataset starts with a line </p>
<pre> $DATASET <i>type</i>[:<i>name</i>] <i>subzone</i> <i>subzone</i>...</pre>
<p>and all subsequent lines up to the end of current file or to next $DATASET line are interpreted as a part of dataset of type <i>type</i>, with optional <i>name</i> (name is used for logging purposes only, and the whole &quot;:<i>name</i>&quot; (without quotes or square brackets) part is optional). Note that combined datasets cannot be nested. Every <i>subzone</i> will always be relative to the base zone name specified on command line. If <i>subzone</i> specified as single character &quot;@&quot;, dataset will be connected to the base zone itself. </p>
<p> This dataset type aims to simplify subzone maintenance, in order to be able to include several subzones in one file for easy data transfer, atomic operations and to be able to modify list of subzones on remote secondary nameservers. </p>
<p> Example of a complete dataset that contains subzone `proxies&#8217; with a list of open proxies, subzone `relays&#8217; with a list of open relays, subzone `multihop&#8217; with output IPs of multihop open relays, and the base zone itself includes proxies and relays but not multihops: </p>
<pre> # common section
 $NS 1w ns1.ex.com ns2.ex.com
 $SOA 1w ns1.ex.com admin.ex.com 0 2h 2h 1w 1h
 # list of open proxies,
 # in `proxies' subzone and in base zone
 $DATASET ip4set:proxy proxies @
 :2:Open proxy, see <a rel="nofollow" href="http://bl.ex.com/proxy/$">http://bl.ex.com/proxy/$</a>
 127.0.0.2
 127.0.0.10
 # list of open relays,
 # in `relays' subzone and in base zone
 $DATASET ip4set:relay relays @
 :3:Open relay, see <a rel="nofollow" href="http://bl.ex.com/relay/$">http://bl.ex.com/relay/$</a>
 127.0.0.2
 127.0.2.10
 # list of optputs of multistage relays,
 # in `multihop' subzone only
 $DATASET ip4set:multihop-relay multihop
 :4:Multihop open relay, see <a rel="nofollow" href="http://bl.ex.com/relay/$">http://bl.ex.com/relay/$</a>
 127.0.0.2
 127.0.9.12
 # for the base zone and all subzones,
 # include several additional records
 $DATASET generic:common proxies relays multihop @
 @ A 127.0.0.8
 www A 127.0.0.8
 @ MX 10 mx.ex.com
 # the above results in having the following records
 # (provided that the base zone specified is bl.ex.com):
 # proxies.bl.ex.com A 127.0.0.8
 # <a rel="nofollow" href="http://www.proxies.bl.ex.com">www.proxies.bl.ex.com</a> 127.0.0.8
 # relays.bl.ex.com A 127.0.0.8
 # <a rel="nofollow" href="http://www.relays.bl.ex.com">www.relays.bl.ex.com</a> 127.0.0.8
 # multihop.bl.ex.com A 127.0.0.8
 # <a rel="nofollow" href="http://www.multihop.bl.ex.com">www.multihop.bl.ex.com</a> 127.0.0.8
 # bl.ex.com A 127.0.0.8
 # <a rel="nofollow" href="http://www.bl.ex.com">www.bl.ex.com</a> 127.0.0.8</pre>
<p>Note that $NS and $SOA values applies to the base zone <i>only</i>, regardless of the placement in the file. Unlike the $TTL values and $<i>n</i> substitutions, which may be both global and local for a given (sub-)dataset.</p>
<h3>Resulting A values and TXT templates</h3>
<p>In all zone file types except generic, A values and TXT templates are specified as following: </p>
<pre> :127.0.0.2:Blacklisted: <a rel="nofollow" href="http://example.com/bl?$">http://example.com/bl?$</a></pre>
<p>If a line starts with a colon, it specifies default A and TXT for all subsequent entries in this dataset. Similar format is used to specify values for individual records, with the A value (enclosed by colons) being optional: </p>
<pre> 127.0.0.2 :127.0.0.2:Blacklisted: <a rel="nofollow" href="http://example.com/bl?$">http://example.com/bl?$</a></pre>
<p>or, without specific A value: </p>
<pre> 127.0.0.2 Blacklisted: <a rel="nofollow" href="http://example.com/bl?$">http://example.com/bl?$</a></pre>
<p>Two parts of a line, delimited by second colon, specifies A and TXT record values. Both are optional. By default (either if no default line specified, or no IP address within that line), <code>rbldnsd</code> will return 127.0.0.2 as A record. 127.0.0 prefix for A value may be omitted, so the above example may be simplified to: </p>
<pre> :2:Blacklisted: <a rel="nofollow" href="http://example.com/bl?$">http://example.com/bl?$</a></pre>
<p>There is no default TXT value, so <code>rbldnsd</code> will not return anything for TXT queries it TXT isn&#8217;t specified. </p>
<p> When A value is specified for a given entry, but TXT template is omitted, there may be two cases interpreted differently, namely, whenever there&#8217;s a second semicolon (:) after the A value. If there&#8217;s no second semicolon, default TXT value for this scope will be used. In contrast, when second semicolon is present, no TXT template will be generated at all. All possible cases are outlined in the following example: </p>
<pre> # default A value and TXT template
 :127.0.0.2:IP address $ is listed
 # 127.0.0.4 will use default A and TXT
 127.0.0.4
 # 127.0.0.5 will use specific A and default TXT
 127.0.0.5 :5
 # 127.0.0.6 will use specific a and <i>no</i> TXT
 127.0.0.6 :6:
 # 127.0.0.7 will use default A and specific TXT
 127.0.0.7 IP address $ running an open relay</pre>
<p>In a TXT template, references to substitution variables are replaced with values of that variables. In particular, single dollar sign ($) is replaced by a listed entry (an IP address in question for IP-based datasets and the domain name for domain-based datasets). <code>$</code><i>n</i>-style constructs, where <i>n</i> is a single digit, are replaced by a substitution variable $<i>n</i> defined for this dataset in current scope (see section &quot;Special Entries&quot; above). To specify a dollar sign as-is, use <code>$$</code>. </p>
<p> For example, the following lines: </p>
<pre> $1 See <a rel="nofollow" href="http://www.example.com/bl">http://www.example.com/bl</a>
 $2 for details
 127.0.0.2 $1/spammer/$ $2
 127.0.0.3 $1/relay/$ $2
 127.0.0.4 This spammer wants some $$$$. $1/$</pre>
<p>will result in the following text to be generated: </p>
<pre> See <a rel="nofollow" href="http://www.example.com/bl/spammer/127.0.0.2">http://www.example.com/bl/spammer/127.0.0.2</a> for details
 See <a rel="nofollow" href="http://www.example.com/bl/relay/127.0.0.3">http://www.example.com/bl/relay/127.0.0.3</a> for details
 This spammer wants some $$. See <a rel="nofollow" href="http://www.example.com/bl/127.0.0.4">http://www.example.com/bl/127.0.0.4</a></pre>
<p>If the &quot;base template&quot; (<code>$=</code> variable) is defined, this template is used for expansion, instead of the one specified for an entry being queried. Inside the base template, <code>$=</code> construct is substituted with the text given for individual entries. In order to stop usage of base template <code>$=</code> for a single record, start it with <code>=</code> (which will be omitted from the resulting TXT value). For example, </p>
<pre> $0 See <a rel="nofollow" href="http://www.example.com/bl?$=">http://www.example.com/bl?$=</a> ($) for details
 127.0.0.2 r123
 127.0.0.3
 127.0.0.4 =See other blocklists for details about $</pre>
<p>produces the following TXT records: </p>
<pre> See <a rel="nofollow" href="http://www.example.com/bl?r123">http://www.example.com/bl?r123</a> (127.0.0.2) for details
 See <a rel="nofollow" href="http://www.example.com/bl?127.0.0.3">http://www.example.com/bl?127.0.0.3</a> (127.0.0.3) for details
 See other blocklists for details about 127.0.0.4</pre>
<h3>acl Dataset</h3>
<p>This is not a real dataset, while the syntax and usage is the same as with other datasets. Instead of defining which records exists in a given zone and which do not, the <code>acl</code> dataset specifies which client hosts (peers) are allowed to query the given zone. The dataset specifies a set of IPv4 and/or IPv6 CIDR ranges (with the syntax exactly the same as understood by the <code>ip4trie</code> and <code>ip6trie</code> datasets), together with action specifiers. When a query is made from an IP address listed (not <i>for</i> the IP address), the specified action changes rules used to construct the reply. Possible actions and their meanings are:</p>
<dl>
<dt>:<code>ignore</code></p>
<dd>ignore all queries from this IP address altogether. <code>rbldnsd</code> acts like there was no query received at all. This is the default action.</p>
<dt>:<code>refuse</code></p>
<dd>refuse all queries from the IP in question. <code>rbldnsd</code> will always return REFUSED DNS response code.</p>
<dt>:<code>empty</code></p>
<dd>pretend there&#8217;s no data in all other datasets for the given zone. This means that all the clients in question will always receive reply from <code>rbldnsd</code> telling that the requested IP address or domain name is not listed in a given DNSBL. <code>rbldnsd</code> still replies to metadata queries (SOA and NS records, and to all queries satisfied by generic dataset if specified for the given zone) as usual.</p>
<dt>:<code>pass</code></p>
<dd>process the request as usual. This may be used to add a &quot;whitelisting&quot; entry for a network/host bloked by another (larger) ACL entry.</p>
<dt><i>a_txt_template</i></p>
<dd>usual A+TXT template as used by other datasets. This means that <code>rbldnsd</code> will reply to any valid DNSBL query with &quot;it is listed&quot; answer, so that the client in question will see every IP address or domain name is listed in a given DNSBL. TXT record used in the reply is taken from the acl dataset instead of real datasets. Again, just like with <code>empty</code> case, <code>rbldnsd</code> will continue replying to metadata queries (including generic datasets if any) as usual.</dl>
<p> Only one ACL dataset can be specified for a given zone, and each zone must have at least one non-acl dataset. It is also possible to specify one global ACL dataset, by specifying empty zone name (which is not allowed for other dataset types), like </p>
<pre> <code>rbldnsd</code> ... :<code>acl</code>:<i>filename</i>...</pre>
<p>In this case the ACL defined in <i>filename</i> applies to all zones. If there are both global ACL and local zone-specific ACL specified, both will be consulted and actions taken in the order specified above, ie, if either ACL returns <code>ignore</code> for this IP, the request will be ignored, else if either ACL returns <code>refuse</code>, the query will be refused, and so on. If both ACLs specifies &quot;always listed&quot; A+TXT template, the reply will contain A+TXT from global ACL. </p>
<p> For this dataset type, only a few $-style specials are recognized. In particular, $SOA and $NS keywords are not allowed. When <code>rbldnsd</code> performs <code>$</code> substitution in the TXT template returned from ACL dataset, it will use client IP address to substitute for a single $ character, instead of the IP address or domain name found in the original query.</p>
<h2>Signals</h2>
<p><code>Rbldnsd</code> handles the following signals: </p>
<dl>
<dt><code>SIGHUP</code></p>
<dd>recheck zone files and reload any outdated ones. This is done automatically if enabled, see <code>-c</code> option. Additionally, <code>rbldnsd</code> will reopen logfile upon receiving SIGHUP, if specified (<code>-l</code> option). </p>
<dt><code>SIGTERM</code>, <code>SIGINT</code></p>
<dd>Terminate process. </p>
<dt><code>SIGUSR1</code></p>
<dd>Log current statistic counters into syslog. <code>Rbldnsd</code> collects how many packets it handled, how many bytes was received, sent, how many OK requests/replies (and how many answer records) was received/sent, how many NXDOMAIN answers was sent, and how many errors/refusals/etc was sent, in a period of time. </p>
<dt><code>SIGUSR2</code></p>
<dd>The same as SIGUSR1, but reset all counters and start new sample period. </p>
</dl>
<h2>Notes</h2>
<p>Some unsorted usage notes follows.</p>
<h3>Generating and transferring data files</h3>
<p>When creating a data file for <code>rbldnsd</code> (and for anything else, it is a general advise), it is a good idea to create the data in temporary file and rename the temp file when all is done. <i>Never</i> try to write to the main file directly, it is possible that at the same time, <code>rbldnsd</code> will try to read it and will get incomplete data as the result. The same applies to copying data using <code><a href="/docs/linux/man/1-cp/">cp</a></code>(1) utility and similar (including <code><a href="/docs/linux/man/1-scp/">scp</a></code>(1)), that performs copying over existing data. Even if you&#8217;re sure noone is reading the data while you&#8217;re copying or generating it, imagine what will happen if you will not be able to complete the process for whatever reason (interrupt, filesystem full, endless number of other reasons&#8230;). In most cases is better to keep older but correct data instead of leaving incomplete/corrupt data in place. Right: </p>
<pre> scp remote:data target.tmp &amp;&amp; mv target.tmp target</pre>
<p><i>Wrong</i>: </p>
<pre> scp remote:data target</pre>
<p>Right: </p>
<pre> ./generate.pl &gt; target.tmp &amp;&amp; mv target.tmp target</pre>
<p><i>Wrong</i>: </p>
<pre> ./generate.pl &gt; target</pre>
<p>From this point of view, <code><a href="/docs/linux/man/1-rsync/">rsync</a></code>(1) command seems to be safe, as it <i>always</i> creates temporary file and renames it to the destination only when all is ok (but note the &#8211;partial option, which is good for downloading something but may be wrong to transfer data files &#8212; usually you don&#8217;t want partial files to be loaded). In contrast, <code><a href="/docs/linux/man/1-scp/">scp</a></code>(1) command is <i>not</i> safe, as it performs direct copying. You may still use <code><a href="/docs/linux/man/1-scp/">scp</a></code>(1) in a safe manner, as shown in the example above. Also try to eliminate a case when two (or more) processes performs data copying/generation at the same time to the same destination. When your data is generated by a cron job, use file locking (create separate lock file (which should never be removed) and flock/fcntl it in exclusive mode without waiting, exiting if lock fails) before attempting to do other file manipulation.</p>
<h3>Absolute vs relative domain names</h3>
<p>All <i>keys</i> specified in dataset files are always relative to the zone base DN. In contrast, all the <i>values</i> (NS and SOA records, MX records in generic dataset) are absolute. This is different from BIND behaviour, where trailing dot indicates whenever this is an absolute or relative DN. Trailing dots in domain names are ignored by <code>rbldnsd</code>.</p>
<h3>Aggregating datasets</h3>
<p>Several zones may be served by <code>rbldnsd</code>, every zone may consist of several datasets. There are numerous ways to combine several data files into several zones. For example, suppose you have a list of dialup ranges in file named `dialups&#8217;, and a list of spammer&#8217;s ip addresses in file named `spammers&#8217;, and want to serve 3 zones with <code>rbldnsd</code>: dialups.bl.ex.com, spam.bl.ex.com and bl.ex.com which is a combination of the two. There are two ways to do this: </p>
<pre> rbldnsd <i>options...</i> \
 dialups.bl.ex.com:ip4set:dialups \
 spam.bl.ex.com:ip4set:spammers \
 bl.ex.com:ip4set:dialups,spammers</pre>
<p>or: </p>
<pre> rbldnsd <i>options...</i> \
 dialups.bl.ex.com:ip4set:dialups \
 spam.bl.ex.com:ip4set:spammers \
 bl.ex.com:ip4set:dialups \
 bl.ex.com:ip4set:spammers</pre>
<p>(note you should specify combined bl.ex.com zone <i>after</i> all its subzones in a command line, or else subzones will not be consulted at all). In the first form, there will be 3 independent data sets, and every record will be stored 2 times in memory, but only one search in internal data structures will be needed to resolve queries for aggregate bl.ex.com. In second form, there will be only 2 data sets, every record will be stored only once (both datasets will be reused), but 2 searches will be performed by <code>rbldnsd</code> to answer queries against aggregate zone (but difference in speed is almost unnoticeable). Note that when aggregating several data files into one dataset, an exclusion entry in one file becomes exclusion entry in the whole dataset (which may be a problem when aggregating dialups, where exclusions are common, with open relays/proxies, where exclusions are rare if at all used). Similar effect may be achieved by using <code>combined</code> dataset type, sometimes more easily. <code>combined</code> dataset results in every nested dataset to be used independantly, like in second form above. <code>combined</code> dataset requires <code>rbldnsd</code> to be the authoritative nameserver for the whole base zone. Most important, one may specify SOA and NS records for the base zone <i>only</i>. So, some DNSBLs which does not use a common subzone for the data, cannot use this dataset. An example being DSBL.org DNSBL, where each of list.dsbl.org, multihop.dsbl.org and unconfirmed.dsbl.org zones are separate, independant zones with different set of nameservers. But for DSBL.org, where each dataset is really independant and used only once (there&#8217;s no (sub)zone that is as a combinations of other zones), <code>combined</code> dataset isn&#8217;t necessary. In contrast, SORBS.net zones, where several subzones used and main zone is a combination of several subzones, <code>combined</code> dataset is a way to go.</p>
<h3>All authoritative nameservers should be set up similarily</h3>
<p>When you have several nameservers for your zone, set them all in a similar way. Namely, if one is set up using <code>combined</code> dataset, all the rest should be too, or else DNS meta-data will be broken. This is because metadata (SOA and NS) records returned by nameservers using <code>combined</code> and other datasets will have different origin. With combined dataset, <code>rbldnsd</code> return NS and SOA records for the base zone, not for any subzone defined inside the dataset. Given the above example with dialups.bl.ex.com, spammers.bl.ex.com and aggregate bl.ex.com zones, and two nameservers, first is set up in any ways described above (using individual datasets for every of the 3 zones), and second is set up for the whole bl.ex.com zone using <code>combined</code> dataset. In this case, for queries against dialups.bl.ex.com, first nameserver will return NS records like </p>
<pre> dialups.bl.ex.com. IN NS a.ns.ex.com.</pre>
<p>while second will always use base zone, and NS records will look like </p>
<pre> bl.ex.com. IN NS a.ns.ex.com.</pre>
<p>All authoritative nameservers for a zone must have consistent metadata records. The only way to achieve this is to use similar configuration (combined or not) on all nameservers. Have this in mind when using other software for a nameserver.</p>
<h3>Generic dataset usage</h3>
<p><code>generic</code> dataset type is very rudimentary. It&#8217;s purpose is to complement all the other type to form complete nameserver that may answer to A, TXT and MX queries. This is useful mostly to define A records for HTTP access (relays.bl.example.com A, <a rel="nofollow" href="http://www.bl.example.com">www.bl.example.com</a> A just in case), and maybe descriptive texts as a TXT record. Since <code>rbldnsd</code> only searches <i>one</i>, most closely matching (sub)zone for every request, one cannot specify a single e.g. <code>generic</code> dataset in form </p>
<pre> proxies TXT list of open proxies
 <a rel="nofollow" href="http://www.proxies">www.proxies</a> A 127.0.0.8
 relays TXT list of open relays
 <a rel="nofollow" href="http://www.relays">www.relays</a> A 127.0.0.9</pre>
<p>for several (sub)zones, each of which are represented as a zone too (either in command line or as <code>combined</code> dataset). Instead, several <code>generic</code> datasets should be specified, separate one for every (sub)zone. If the data for every subzone is the same, the same, single dataset may be used, but it should be specified for every zone it should apply to (see <code>combined</code> dataset usage example above). </p>
<h2>Bugs</h2>
<p>Most of the bugs outlined in this section aren&#8217;t really bugs, but present due to non-standartized and thus unknown expected behaviour of a nameserver that serves a DNSBL zone. <code>rbldnsd</code> matches BIND runtime behaviour where appropriate, but not always. <code>rbldnsd</code> lowercases some domain names (the ones that are lookup keys, e.g. in `generic&#8217; and `dnset&#8217; datasets) when loading, to speed up lookup operations. This isn&#8217;t a problem in most cases. There is no TCP mode. If a resource record does not fit in UDP packet (512 bytes), it will be silently ignored. For most usages, this isn&#8217;t a problem, because there should be only a few RRs in an answer, and because one record is usually sufficient to decide whenever a given entry is &quot;listed&quot; or not. <code>rbldnsd</code> isn&#8217;t a full-featured nameserver, after all. <code>rbldnsd</code> will not always return a list of nameserver records in the AUTHORITY section of every positive answer: NS records will be provided (if given) only if there&#8217;s a room for them in single UDP packet. If records does not fit, AUTHORITY section will be empty. <code>rbldnsd</code> does not allow AXFR operations. For DNSBLs, AXFR is the stupidiest yet common thing to do &#8211; use rsync for zone transfers instead. This isn&#8217;t a bug in <code>rbldnsd</code> itself, but in common practice of using AXFR and the like to transfer huge zones in a format which isn&#8217;t suitable for such a task. Perhaps in the future, if there will be some real demand, I&#8217;ll implement AXFR &quot;server&quot; support (so that <code>rbldnsd</code> will be able to act as master for BIND nameservers, but not as secondary), but the note remains: use rsync. <code>rbldnsd</code> truncates all TXT records to be at most 255 bytes. DNS specs allows longer TXTs, but long TXTs is something that should be avoided as much as possible &#8211; TXT record is used as SMTP rejection string. Note that DNS UDP packet is limited to 512 bytes. <code>rbldnsd</code> will log a warning when such truncation occurs. </p>
<h2>Version</h2>
<p>This manpage corresponds to <code>rbldnsd</code> version <code>0.998</code>.</p>
<h2>Author</h2>
<p>The <code>rbldnsd</code> daemon written by Michael Tokarev &lt;mjt+rbldnsd [at] corpit.ru&gt;, based on ideas by Dan Bernstein and his djbdns package, with excellent contributions by Geoffrey T. Dairiki &lt;dairiki [at] dairiki.org&gt;.</p>
<h2>Licence</h2>
<p>Mostly GPL, with some code licensed under 3-clause BSD license.</p>
