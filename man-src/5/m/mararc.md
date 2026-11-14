---
title: "mararc(5)"
name: "mararc"
section: "5"
letter: "m"
url: "/docs/linux/man/5-mararc/"
description: "mararc – Format of the mararc zone file that MaraDNS uses"
---

<p>mararc &#8211; Format of the mararc zone file that MaraDNS uses</p>
<h2>Mararc File Format</h2>
<p>Mararc files use a syntax that is a subset of Python 2.2.3 syntax. In particular, Python 2.2.3 (and possibly other versions of Python) can read a properly formatted mararc file without error. </p>
<p> Unlike Python, however, a mararc file can only use certain variable names, and the variables can only be declared as described below.</p>
<h2>Comments</h2>
<p>Comments (lines ignored by the MaraDNS parser) start with the aq#aq character, like this: </p>
<pre># This is a comment</pre>
<p>The MaraDNS parser also ignores lines which contain only white space.</p>
<h2>Operators</h2>
<p>The MaraRC file supports two operators: = and += </p>
<p> The = operator can be used to assign both numeric and string values </p>
<p> The += operator can only be used on string values, and concatenates the value to the right of the += operator to the string specified to the left of the += operator. </p>
<p> Examples: </p>
<pre>ipv4_bind_addresses = &quot;10.2.19.83&quot;
ipv4_bind_addresses += &quot;,10.2.66.74&quot;
ipv4_bind_addresses += &quot;,10.3.87.13&quot;</pre>
<p>ipv4_bind_addresses now has the value &quot;10.2.19.83,10.2.66.74,10.3.87.13&quot; </p>
<pre>ipv4_alias[&quot;icann&quot;] = &quot;198.41.0.4&quot;
ipv4_alias[&quot;icann&quot;] += &quot;,192.228.79.201&quot;
ipv4_alias[&quot;icann&quot;] += &quot;,192.33.4.12,128.8.10.90&quot;</pre>
<h2>Mararc Variables</h2>
<p>Follows is a listing of variables that can be declared in the mararc file.</p>
<h2>Dictionary Variable Format</h2>
<p>A <code>dictionary variable</code> is an array that can have multiple elements. Unlike a traditional array, these arrays are indexed by strings instead of numbers. These are analogous to associative arrays, or what Perl somewhat inaccurately calls hashes. </p>
<p> The syntax of a dictionary variable is in the following form: </p>
<pre>name[&quot;index&quot;] = &quot;value&quot;</pre>
<p>Where <code>name</code> is the name of the dictionary variable, <code>index</code> is the index of the array, and <code>value</code> is the value stored at that index. </p>
<p> Every time we have a dictionary-type variable (such as csv2), we must first initialize it using a line in the following form: </p>
<pre>csv2 = {}</pre>
<p>Here, csv2 is the name of the &quot;dictionary&quot; variable that we are initializing.</p>
<h2>Dictionary Variables</h2>
<p>Here is a listing of all &quot;dictionary&quot;-style variables that MaraDNS uses: </p>
<p> <code>csv2</code> </p>
<p> The csv2 dictionary variable stores all of the zone names and file names for the zone files that MaraDNS uses. Note that csv2 files are read after MaraDNS is chrooted. Hence the filename is relative to the chroot_dir. Example: </p>
<pre>csv2[&quot;example.net.&quot;] = &quot;db.example.net&quot;</pre>
<p>See <code><a href="/docs/linux/man/5-csv2/">csv2</a>(5)</code> for a description of this fileaqs format. </p>
<p> <code>csv1</code> </p>
<p> csv1: Used to indicate the filename to use for a given zone stored in the legacy csv1 zone file format. This is primarily for compatibility with people who have maradns-1.0 zone files. </p>
<pre>csv1[&quot;zone&quot;] = &quot;filename&quot;</pre>
<p><code>csv1</code>: A pipe-separated-file. See <code><a href="/docs/linux/man/5-csv1/">csv1</a>(5)</code>. </p>
<p> <code>zone</code>: the zone that file in question is authoritative for </p>
<p> <code>filename</code>: the file with the CSV1 zone data </p>
<p> Note that csv1 files are read after MaraDNS is chrooted, and, hence the filename is relative to the chroot_dir. </p>
<p> See the <code><a href="/docs/linux/man/5-csv1/">csv1</a>(5)</code> man page for more information on this file format. </p>
<p> <code>ipv4_alias</code> </p>
<p> ipv4_alias: Used to give nicknames or aliases for ip/netmask pairs for ipv4 (standard 32-bit) IP addresses. </p>
<pre>ipv4_alias[&quot;name&quot;] = &quot;ip1/netmask,ip2/netmask,etc&quot;</pre>
<p><code>name</code>: The name of the alias in question </p>
<p> <code>ip</code>: The ip portion of an ip/netmask pair </p>
<p> <code>netmask</code>: the mask portion of an ip/netmask pair </p>
<p> <code>,</code>: Used to separate ip/netmask pairs. Spaces may be placed before or after this comma. </p>
<p> An ip is in dotted-decimal format, e.g. &quot;10.1.2.3&quot;. </p>
<p> The netmask can be in one of two formats: A single number between 1 and 32, which indicates the number of leading &quot;1&quot; bits in the netmask, or a 4-digit dotted-decimal netmask. </p>
<p> The netmask is used to specify a range of IPs. </p>
<p> <code>ipv4_alias examples</code> </p>
<p> <code>10.1.1.1/24</code> indicates that any ip from 10.1.1.0 to 10.1.1.255 will match. </p>
<p> <code>10.1.1.1/255.255.255.0</code> is identical to 10.1.1.1/24 </p>
<p> <code>10.2.3.4/16</code> indicates that any ip from 10.2.0.0 to 10.2.255.255 will match. </p>
<p> <code>10.2.3.4/255.255.0.0</code> is identical to 10.2.3.4/16 </p>
<p> <code>127.0.0.0/8</code> indicates that any ip with &quot;127&quot; as the first octet (number) will match. </p>
<p> <code>127.0.0.0/255.0.0.0</code> is identical to 127.0.0.0/8 </p>
<p> The netmask is optional, and, if not present, indicates that only a single IP will &quot;match&quot;. e.g: </p>
<p> <code>10.9.9.9/32</code>, <code>10.9.9.9/255.255.255.255</code>, and <code>10.9.9.9</code> are all functionally identical, and indicate that only the ip 10.9.9.9 will match. </p>
<p> The significance of &quot;match&quot; depends on what we use the ipv4 alias for. </p>
<p> ipv4 aliases can nest. E.g: </p>
<pre>ipv4_alias[&quot;susan&quot;] = &quot;10.6.7.8/24&quot; 
ipv4_alias[&quot;office&quot;] = &quot;susan,10.9.9.9&quot;</pre>
<p>Where &quot;susan&quot; in the &quot;office&quot; alias matches the value of the ipv4_alias susan. </p>
<p> Multiple levels of nesting are allowed. Self-referring nests will result in an error. </p>
<p> <code>root_servers</code> </p>
<p> root_servers: This is a special &quot;dictionary&quot; element that can have multiple elements, where a given element points to either an ip, or a pointer to an ipv4 alias. For example: </p>
<pre>root_servers[&quot;.&quot;] = &quot;list_of_servers&quot;</pre>
<p>In this example, &quot;.&quot; indicates that this is a listing of root_servers that will resolve any name not otherwise listed as a root_servers entry. </p>
<p> list_of_servers is a list of root name servers in the exact same format as ipv4_aliases. </p>
<p> The root_servers dictionary array can have multiple elements. Like csv2 elements, the names must be valid domain names that end with the aq.aq character. When there are multiple root_servers elements, the element with the most domain name labels that matches the end of the hostname one is searching for is used. </p>
<p> For exmaple, let us suppose we have the following root_servers entries: </p>
<pre>root_servers[&quot;.&quot;] = &quot;198.41.0.4&quot;
root_servers[&quot;com.&quot;] = &quot;192.5.6.30&quot;
root_servers[&quot;example.net.&quot;] = &quot;10.1.2.3,10.2.3.4&quot;</pre>
<p>In this example, we use use the name server with the IP 10.1.2.3 or 10.2.3.4 to start resolving &quot;<a rel="nofollow" href="http://www.example.net">www.example.net</a>&quot;, the name server with the IP 192.5.6.30 to start resolving &quot;<a rel="nofollow" href="http://www.google.com">www.google.com</a>&quot;, and the name server with the IP 198.41.0.4 to start resolving &quot;<a rel="nofollow" href="http://www.maradns.org">www.maradns.org</a>&quot;. </p>
<p> Note that, while ips in a listing of root name servers can have netmasks, the netmask portion is ignored. </p>
<p> The root_servers should point to root servers. If one wishes to use MaraDNS as a forwarding name server, which forwards DNS requests on to another server, use the upstream_servers variable instead. </p>
<p> <code>upstream_servers</code> </p>
<p> This is identical to the root_servers variable (can have multiple elements, the elements are a list of ipv4_addresses, the variable is a dictionary variable, etc.), but is used when one wishes to use MaraDNS to query other recursive servers, instead of querying the actual root name servers for an answer. </p>
<p> Note that one can not have both root_servers and upstream_servers set in a given mararc file; MaraDNS will return with a fatal error if one attempts to do this. </p>
<p> Like root_servers, this is a dictionary variable that can have multiple elements. For example: </p>
<pre>upstream_servers[&quot;.&quot;] = &quot;10.5.6.7&quot;
upstream_servers[&quot;cl.&quot;] = &quot;10.2.19.83&quot;</pre>
<p>Here, we use 10.2.19.83 to resolve host names that end in &quot;cl&quot;, and 10.5.6.7 to resolve all other host names.</p>
<h2>Normal Variable Format</h2>
<p>Normal variables. These are variables that can only take a single value. </p>
<p> The syntax of a normal variable is in the form </p>
<pre>name = &quot;value&quot;</pre>
<p>Where <code>name</code> is the name of the normal variable, and <code>value</code> is the value of the variable in question.</p>
<h2>Normal Variables</h2>
<p>Here is a listing of normal variables that MaraDNS uses: </p>
<p> <code>ipv4_bind_addresses</code> </p>
<p> ipv4_bind_addresses: The IP addresses to give the MaraDNS server. </p>
<p> This accepts one or more ipv4 IPs in dotted-decimal (e.g. &quot;127.0.0.1&quot;) notation, and specifies what IP addresses the MaraDNS server will listen on. Multiple bind addresses are separated with a comma, like this: &quot;10.1.2.3, 10.1.2.4, 127.0.0.1&quot; </p>
<p> <code>admin_acl</code> </p>
<p> This is a list of ip/netmask pairs that are allowed to get certain administrative information about MaraDNS, including:</p>
<dl>
<dt>*</p>
<dd>The version number of MaraDNS running</p>
<dt>*</p>
<dd>The number of threads MaraDNS has</p>
<dt>*</p>
<dd>MaraDNSaq internal timestamp value</dl>
<p> Note that this information is not available unless the mararc variable debug_msg_level is sufficiently high. See the information on debug_msg_level below for details on this and on the TXT queries sent to get the above information. </p>
<p> <code>bind_address</code> </p>
<p> bind_address: The IP address to give the MaraDNS server. </p>
<p> This accepts a single IP in dotted-decimal (e.g. &quot;127.0.0.1&quot;) notation, and specifies what IP address the MaraDNS server will listen on. Note that ipv4_bind_addresses has the same functionality. This name is included so that MaraDNS 1.0 configuration files will continue to work with MaraDNS 1.2. </p>
<p> <code>bind_star_handling</code> </p>
<p> In the case where there is both a star record for a given name and recordtype, a non-star record with the same name but a different recordtype, and no record for the given name and recordtype, MaraDNS will usually return the star record. BIND, on the other hand, will return a &quot;not there&quot; reply. In other words:</p>
<dl>
<dt>*</p>
<dd>If a non-A record for foo.example.com exists</p>
<dt>*</p>
<dd>An A record for *.example.com exists</p>
<dt>*</p>
<dd>No A record for foo.example.com exists</p>
<dt>*</p>
<dd>And the user asks for the A record for foo.example.com</p>
<dt>*</p>
<dd>MaraDNS will usually return the A record attached to *.example.com</p>
<dt>*</p>
<dd>BIND, on the other hand, returns a &quot;not there&quot; for foo.example.com</dl>
<p> If the BIND behavior is desired, set bind_star_handling to 1. Otherwise, set this to 0. In MaraDNS 1.3, this has a default value of 1. </p>
<p> In addition, if there is a star record that could match any given record type, when bind_star_handling is 1, it makes sure that MaraDNS does not incorrectly return a NXDOMAIN (RFC 4074 section 4.2). </p>
<p> Also, if bind_star_handling has a value of 2, MaraDNS will handle the following case exactly as per section 4.3.3 of RFC1034:</p>
<dl>
<dt>*</p>
<dd>If a record for foo.example.com exists</p>
<dt>*</p>
<dd>An A record for *.example.com exists</p>
<dt>*</p>
<dd>And the user asks for the A record for bar.foo.example.com</p>
<dt>*</p>
<dd>MaraDNS will usually return the A record attached to *.example.com</p>
<dt>*</p>
<dd>RFC1034 section 4.3.3 says one should return a NXDOMAIN.</dl>
<p> MaraDNS will exit with a fatal error if bind_star_handling has any value besides 0, 1, or 2. </p>
<p> <code>chroot_dir</code> </p>
<p> chroot_dir: The directory MaraDNS chroots to </p>
<p> This accepts a single value: The full path to the directory to use as a chroot jail. </p>
<p> Note that csv1 zone files are read after the chroot operation. Hence, the chroot jail needs to have any and all zone files that MaraDNS will load. </p>
<p> <code>csv2_default_zonefile</code> </p>
<p> This is a special zone file that allows there to be stars at the <i>end</i> of hostnames. This file is similar to a normal csv2 zone file, but has the following features and limitations:</p>
<dl>
<dt>*</p>
<dd>Stars are allowed at the end of hostnames</p>
<dt>*</p>
<dd>A SOA record is mandatory</p>
<dt>*</p>
<dd>NS records are mandatory</p>
<dt>*</p>
<dd>Neither CNAME nor FQDN4 records are permitted in the zone file</p>
<dt>*</p>
<dd>Delegation NS records are not permitted in the zone file</p>
<dt>*</p>
<dd>Default zonefiles may not be transferred via zone transfer</p>
<dt>*</p>
<dd>Both recursion and default zonefiles may not be enabled at the same time.</dl>
<p> <code>csv2_synthip_list</code> </p>
<p> Sometimes the IP list of nameservers will be different than the nameservers one is bound to. This allows the synthetic nameserver list to have different IPs. </p>
<p> Note that this may act in an unexpected manner if routable and non-routable (localhost and RFC1918) addresses are combined; in particular, a list with both routable and non-routable addresses will discard the non-routable IP addresses, and a list with rfc1918 and localhost addresses will discard the localhost addresses. </p>
<p> <code>csv2_tilde_handling</code> </p>
<p> How the csv2 zone file parser handles tildes (the ~ character) in csv2 zone files. This is a numeric record, with a possible value between 0 and 3 (four possible values). The way the csv2 parser acts at different csv2_tilde_handling levels:</p>
<dl>
<dt>*</p>
<dd>0) The csv2 parser behaves the same as it does in MaraDNS 1.2: The tilde has no special significance to the parser.</p>
<dt>*</p>
<dd>1) A tilde is not allowed anywhere in a csv2 zone file.</p>
<dt>*</p>
<dd>2) A tilde is only allowed between records in a csv2 zone file. If a tilde is between the first record and the second record, a tilde is required to be between all records. Otherwise, a tilde is not allowed anywhere in a csv2 zone file. The first record can not be a TXT, WKS, or LOC record.</p>
<dt>*</p>
<dd>3) A tilde is required to be between all records in a csv2 zone file.</dl>
<p> The default value for csv2_tilde_handling is 2; this allows compatibility with all 1.2 zone files without tildes while allowing zone files to be updated to use the tilde to separate resource records. </p>
<p> <code>debug_msg_level</code> </p>
<p> This is a number indicating what level of information about a running MaraDNS process should be made public. When set to 0, no information will be made public. </p>
<p> When set to one (the default), or higher, a Tversion.maradns. (TXT query for &quot;version.maradns.&quot;) query will return the version number of MaraDNS. </p>
<p> When set to two or higher, a Tnumthreads.maradns. (TXT query for &quot;numthreads.maradns.&quot;) query will return the number of threads that MaraDNS is currently running, and a Tcache-elements.maradns. query will return the number of elements in MaraDNSaq cache. </p>
<p> If MaraDNS is compiled with debugging information on, a Tmemusage.maradns. query will return the amount of memory MaraDNS has allocated. Note that the overhead for tracking memory usage is considerable and that compiling MaraDNS with &quot;make debug&quot; will greatly slow down MaraDNS. A debug build of MaraDNS is <code>not</code> reccomended for production use. </p>
<p> When set to three or higher, a Ttimestamp.maradns. query will return, in seconds since the UNIX epoch, the timestamp for the system MaraDNS is running on. </p>
<p> <code>default_rrany_set</code> </p>
<p> This variable used to determine what kind of resource records were returned when an ANY query was sent. In MaraDNS 1.2, the data structures have been revised to return any resource record type when an ANY query is sent; this variable does nothing, and is only here so that MaraDNS 1.0 mararc files will continue to work. The only accepted values for this variable were 3 and 15. </p>
<p> <code>dns_port</code> </p>
<p> This is the port that MaraDNS listens on. This is usually 53 (the default value), but certain unusual MaraDNS setups (such as when resolving dangling CNAME records on but a single IP) may need to have a different value for this. </p>
<p> <code>dos_protection_level</code> </p>
<p> If this is set to a non-zero value, certain features of MaraDNS will be disabled in order to speed up MaraDNSaq response time. This is designed for situtations when a MaraDNS server is receiving a large number of queries, such as during a denial of service attack. </p>
<p> This is a numeric variable; its default value is zero, indicating that all of MaraDNSaq normal features are enabled. Higher numeric values disable more features:</p>
<dl>
<dt>*</p>
<dd>A dos_protection_level between 1 and 78 (inclusive) disables getting MaraDNS status information remotely.</p>
<dt>*</p>
<dd>A dos_protection_level of 8 or above disables CNAME lookups.</p>
<dt>*</p>
<dd>A dos_protection_level or 12 or above diables delegation NS records.</p>
<dt>*</p>
<dd>A dos_protection_level of 14 or above disables ANY record processing.</p>
<dt>*</p>
<dd>A dos_protection_level of 18 or above disables star record processing at the beginning of hostnames (default zonefiles still work, however).</p>
<dt>*</p>
<dd>A dos_protection_level of 78 disables all authoritative processing, including default zonefiles; recursive lookups still work.</dl>
<p> The default level of dos_protection_level is 0 when there are one or more zonefiles; 78 when there are no zone files. </p>
<p> <code>ipv6_bind_address</code> </p>
<p> If MaraDNS is compiled with as an authoritative server, then this variable will tell MaraDNS which ipv6 address for the UDP server to; for this variable to be set, MaraDNS must be bound to at least one ipv4 address. </p>
<p> <code>handle_noreply</code> </p>
<p> This is a numeric variable which determines how the recursive resolver informs the client that Mara was unable to contact any remote DNS servers when trying to resolve a given domain. If this is set to 0, no reponse will be sent to the DNS client. If this is set to 1, a &quot;server fail&quot; message will be sent to the DNS client. If this is set to 2, a &quot;this host does not exist&quot; message will be sent to the DNS client. The default value for this is 1. </p>
<p> <code>hide_disclaimer</code> </p>
<p> If this is set to &quot;YES&quot;, MaraDNS will not display the legal disclaimer when starting up. </p>
<p> <code>long_packet_ipv4</code> </p>
<p> This is a list of IPs which we will send UDP packets longer than the 512 bytes RFC1035 permits if necessary. This is designed to allow zoneserver, when used send regular DNS packets over TCP, to receive packets with more data than can fit in a 512-byte DNS packet. </p>
<p> This variable only functions if MaraDNS is compiled as an authoritative only server. </p>
<p> <code>maradns_uid</code> </p>
<p> maradns_uid: The numeric UID that MaraDNS will run as </p>
<p> This accepts a single numerical value: The UID to run MaraDNS as. </p>
<p> MaraDNS, as soon as possible drops root privileges, minimizing the damage a potential attacker can cause should there be a security problem with MaraDNS. This is the UID maradns becomes. </p>
<p> The default UID is 99. </p>
<p> <code>maradns_gid</code> </p>
<p> maradns_gid: The numeric GID that MaraDNS will run as. </p>
<p> This accepts a single numerical value: The GID to run MaraDNS as. </p>
<p> The default GID is 99. </p>
<p> <code>maximum_cache_elements</code> </p>
<p> maximum_cache_elements: The maximum number of elements we can have in the cache of recursive queries. </p>
<p> This cache of recursive queries is used to store entries we have previously obtained from recursive queries. </p>
<p> If we approach this limit, the &quot;custodian&quot; kicks in to effect. The custodian removes elements at random from the cache (8 elements removed per query) until we are at the 99% or so level again. </p>
<p> The default value for this variable is 1024. </p>
<p> <code>maxprocs</code> </p>
<p> maxprocs: The maximum number of threads or processes that MaraDNS is allowed to run at the same time. </p>
<p> This variable is used to minimize the impact on the server when MaraDNS is heavily loaded. When this number is reached, it is impossible for MaraDNS to spawn new threads/processes until the number of threads/processes is reduced. </p>
<p> The default value for this variable is 64. </p>
<p> The maximum value this can have is 500. </p>
<p> <code>max_ar_chain</code> </p>
<p> max_ar_chain: The maximum number of records to display if a record in the additional section (e.g., the IP of a NS server or the ip of a MX exchange) has more than one value. </p>
<p> This is similar to max_chain, but applies to records in the &quot;additional&quot; (or AR) section. </p>
<p> Due to limitations in the internal data structures that MaraDNS uses to store RRs, if this has a value besides one, round robin rotates of records are disabled. </p>
<p> The default value for this variable is 1. </p>
<p> <code>max_chain</code> </p>
<p> max_chain: The maximum number of records to display in a chain of records. </p>
<p> With DNS, it is possible to have more than one RR for a given domain label. For example, &quot;example.com&quot; can have, as the A record, a list of multiple ip addresses. </p>
<p> This sets the maximum number of records MaraDNS will show for a single RR. </p>
<p> MaraDNS normally round-robin rotates records. Hence, all records for a given DNS label (e.g. &quot;example.com.&quot;) will be visible, although not at the same time if there are more records than the value allowed with max_chain </p>
<p> The default value for this variable is 8. </p>
<p> <code>max_tcp_procs</code> </p>
<p> max_tcp_procs: The (optional) maximum number of processes the zone server is allowed to run. </p>
<p> Sometimes, it is desirable to have a different number of maximum allowed tcp processes than maximum allowed threads. If this variable is not set, the maximum number of allowed tcp processes is &quot;maxprocs&quot;. </p>
<p> <code>max_total</code> </p>
<p> max_total: The maximum number of records to show total for a given DNS request. </p>
<p> This is the maximum total number of records that MaraDNS will make available in a DNS reply. </p>
<p> The default value for this variable is 20. </p>
<p> <code>max_mem</code> </p>
<p> max_mem is the maximum amount of memory we allow MaraDNS to allocate, in bytes. </p>
<p> The default value of this is to allocate 1 megabyte for MaraDNSaq general use, and in addition, to allocate 1536 bytes for each element we can have in the cache or DNS record that we are authoritatively serving. </p>
<p> <code>min_ttl</code> </p>
<p> min_ttl: The minimum amount of time a resource record will stay in MaraDNSaq cache, regardless of the TTL the remote server specifies. </p>
<p> Setting this value changes the minimum amount of time MaraDNSaq recursive server will keep a record in the cache. The value is in seconds. </p>
<p> The default value of this is 300 (5 minutes); the minimum value for this is 180 (2 minutes). </p>
<p> <code>min_ttl_cname</code> </p>
<p> min_ttl_cname: The minimum amount of time a resource record will stay in MaraDNSaq cache, regardless of the TTL the remote server specifies. </p>
<p> Setting this value changes the amount of time a CNAME record stays in the cache. The value is in seconds. </p>
<p> The default value for this is the value min_ttl has; the minimum value for this is 180 (2 minutes). </p>
<p> <code>min_visible_ttl</code> </p>
<p> min_visible_ttl: The minimum value that we will will show as the TTL (time to live) value for a resource record to other DNS servers and stub resolvers. In other words, this is the minimum value we will ask other DNS server to cache (keep in their memory) a DNS resource record. </p>
<p> The value is in seconds. The default value for this is 30; the minimum value this can have is 5. People running highly loaded MaraDNS servers may wish to increase this value to 3600 (one hour) in order to reduce the number of queries recursively processed by MaraDNS. </p>
<p> As an aside, RFC1123 section 6.1.2.1 implies that zero-length TTL records should be passed on with a TTL of zero. This, unfortunatly, breaks some stub resolvers (such as Mozillaaqs stub resolver). </p>
<p> <code>random_seed_file</code> </p>
<p> randsom_seed_file: The file from which we read 16 bytes from to get the 128-bit seed for the secure pseudo random number generator. </p>
<p> This localcation of this file is relative to the root of the filesystem, not MaraDNSaq chroot directory. </p>
<p> This is ideally a file which is a good source of random numbers (e.g. /dev/urandom), but can also be a fixed file if your OS does not have a decent random number generator. In that case, make sure the contents of that file is random and with 600 perms, owned by root. We read the file <code>before</code> dropping root privileges. </p>
<p> <code>recurse_delegation</code> </p>
<p> recurse_delegation: Whether to recurse in the case of us finding a NS delegation record, but the user/stub resolver sent a query that desires recursion. Before MaraDNS 1.3, this was the default behavior. </p>
<p> When recurse_delegation has a value of 1, we recurse in this case. Otherwise, we do not. </p>
<p> This parameter has a default value of 0. </p>
<p> <code>recurse_min_bind_port</code> </p>
<p> MaraDNS, by default, binds to a UDP port with a value between 15000 and 19095 when making a recursive query. This variable, and the recurse_number_ports variable, allow this value to be changed. </p>
<p> recurse_min_bind_port is the lowest port number that MaraDNS will bind to when making recursive queries. The default value for this is 15000. </p>
<p> <code>recurse_number_ports</code> </p>
<p> This determines the size of the port range MaraDNS will bind to when making recursive queries. MaraDNS, when making a recursive query, will locally bind to a port number between recurse_min_bin_port and recurse_min_bind_port + recurse_number_ports &#8211; 1. </p>
<p> This number must be a power of 2 between 256 and 32768. In other words, this must have the value 256, 512, 1024, 2048, 4096, 8192, 16384, or 32768. The default value for this is 4096. </p>
<p> The sum of the values for recurse_min_bind_port + recurse_number_ports must fit within the 16-bit value used for UDP ports. In other words, these two parameters, added together, can not be greater than 65534. </p>
<p> <code>recursive_acl</code> </p>
<p> recursive_acl: List of ips allowed to perform recursive queries with the recursive portion of the MaraDNS server </p>
<p> The format of this string is identical to the format of an ipv4_alias entry. </p>
<p> <code>remote_admin</code> </p>
<p> remote_admin: Whether we allow verbose_level to be changed after MaraDNS is started. </p>
<p> If remote_admin is set to 1, and admin_acl is set, any and all IPs listed in admin_acl will be able to reset the value of verbose_level from any value between 0 and 9 via a TXT query in the form of 5.verbose_level.maradns. What this will do is set verbose_query to the value in the first digit of the query. </p>
<p> This is useful when wishing to temporarily increase the verbose_level to find out why a given host name is not resolving, then decreasing verbose_level so as to minimize the size of MaraDNSaq log. </p>
<p> <code>retry_cycles</code> </p>
<p> retry_cycles: The number of times the recursive resolver will try to contact all of the DNS servers to resolve a given name before giving up. This feature was added to MaraDNS 1.2.08, and has a default value of 2. </p>
<p> <code>spammers</code> </p>
<p> spammers: A list of DNS servers which the recursive resolver will not query. </p>
<p> This is mainly used to not allow spam-friendly domains to resolve, since spammers are starting to get in the habit of using spam-friendly DNS servers to resolve their domains, allowing them to hop from ISP to ISP. </p>
<p> The format of this string is identical to the format of an ipv4_alias entry. </p>
<p> <code>synth_soa_origin</code> </p>
<p> When a CSV2 zone file doesnaqt have a SOA record in it, MaraDNS generates a SOA record on the fly. This variable determines the host name for the &quot;SOA origin&quot; (which is called the MNAME in RFC1035); this is the host name of the DNS server which has the &quot;master copy&quot; of a given DNS zoneaqs file. </p>
<p> This host name is in human-readable format without a trailing dot, e.g.: </p>
<pre>synth_soa_origin = &quot;ns1.example.com&quot;</pre>
<p>If this is not set, a synthetic SOA record will use the name of the zone for the SOA origin (MNAME) field. </p>
<p> <code>synth_soa_serial</code> </p>
<p> This determines whether we strictly follow RFC1912 section 2.2 with SOA serial numbers. If this is set to 1 (the default value), we do not strictly follow RFC1912 section 2.2 (the serial is a number, based on the timestamp of the zone file, that is updated every six seconds), but this makes it so that a serial number is guaranteed to be automatically updated every time one edits a zone file. </p>
<p> If this is set to 2, the SOA serial number will be in YYYYMMDDHH format, where YYYY is the 4-digit year, MM is the 2-digit month, DD is the 2-digit day, and HH is the 2-digit hour of the time the zone file was last updated (GMT; localtime doesnaqt work in a chroot() environment). While this format is strictly RFC1912 compliant, the disadvantage is that more than one edit to a zone file in an hour will not update the serial number. </p>
<p> I strongly recommend, unless it is extremely important to have a DNS zone that generates no warnings when tested at dnsreport.com, to have this set to 1 (the default value). Having this set to 2 can result in updated zone files not being seen by slave DNS servers. </p>
<p> Note that synth_soa_serial can only have a value of 1 on the native Windows port. </p>
<p> <code>tcp_convert_acl</code> </p>
<p> This only applies to the zoneserver (general DNS-over-TCP) program. </p>
<p> This is a list of IPs which are allowed to connect to the zoneserver and send normal TCP DNS requests. The zoneserver will convert TCP DNS requests in to UDP DNS requests, and send the UDP request in question to the server specified in <code>tcp_convert_server</code>. Once it gets a reply from the UDP DNS server, it will convert the reply in to a TCP request and send the reply back to the original TCP client. </p>
<p> Whether the RD (recursion desired) flag is set or not when converting a TCP DNS request in to a UDP DNS request is determined by whether the TCP client is on the <code>recursive_acl</code> list. </p>
<p> <code>tcp_convert_server</code> </p>
<p> This only applies to the zoneserver (general DNS-over-TCP) program. </p>
<p> This is the UDP server which we send a query to when converting DNS TCP queries in to DNS UDP servers. Note that, while this value allows multiple IPs, all values except the first one are presently ignored. </p>
<p> <code>timeout_seconds</code> </p>
<p> This only applies when performing recursive lookups. </p>
<p> The amount of time, in seconds, to wait for a reply from a remote DNS server before giving up and trying the next server on this list. The default value is 2 seconds. </p>
<p> This is for setups where a recursive MaraDNS server is on a slow network which takes more than two seconds to send and receive a DNS packet. </p>
<p> Note that, the larger this value is, the slower MaraDNS will process recursive queries when a DNS server is not responding to DNS queries. </p>
<p> <code>timestamp_type</code> </p>
<p> timestamp_type: The type of timestamp to display. The main purpose of this option is to supress the output of timestamps. Since duende uses syslog() to output data, and since syslog() adds its own timestamp, this option should be set to 5 when maradns is invoked with the duende tool. </p>
<p> This option also allows people who do not use the duende tool to view human-readable timestamps. This option only allows timestamps in GMT, due to issues with showing local times in a chroot() environment. </p>
<p> This can have the following values:</p>
<dl>
<dt>0</p>
<dd>The string &quot;Timestamp&quot; followed by a UNIX timestamp</p>
<dt>1</p>
<dd>Just the bare UNIX timestamp</p>
<dt>2</p>
<dd>A GMT timestamp in the Spanish language</p>
<dt>3</p>
<dd>A (hopefully) local timestamp in the Spanish language</p>
<dt>4</p>
<dd>A timestamp using asctime(gmtime()); usually in the English language</p>
<dt>5</p>
<dd>No timestamp whatsoever is shown (this is the best option when maradns is invoked with the duende tool).</p>
<dt>6</p>
<dd>ISO GMT timestamp is shown</p>
<dt>7</p>
<dd>ISO local timestamp is shown</dl>
<p> The default value for this variable is 5. </p>
<p> <code>upstream_port</code> </p>
<p> This is the port that MaraDNSaq recursive resolver uses to contact other DNS servers. This is usually 53 (the default value), but certain unusual MaraDNS setups (such as when resolving dangling CNAME records on but a single IP) may need to have a different valur for this. </p>
<p> <code>verbose_level</code> </p>
<p> verbose_level: The number of messages we log to stdout </p>
<p> This can have five values:</p>
<dl>
<dt>0</p>
<dd>No messages except for the legal disclaimer and fatal parsing errors</p>
<dt>1</p>
<dd>Only startup messages logged (Default level)</p>
<dt>2</p>
<dd>Error queries logged</p>
<dt>3</p>
<dd>All queries logged</p>
<dt>4</p>
<dd>All actions adding and removing records from the cache logged</dl>
<p> The default value for this variable is 1. </p>
<p> <code>verbose_query</code> </p>
<p> verbose_query: Whether to verbosely output all DNS queries that the recursive DNS server receives. If this is set to 1, then all recursive queries sent to MaraDNS will be logged. </p>
<p> This is mainly used for debugging. </p>
<p> <code>zone_transfer_acl</code> </p>
<p> zone_transfer_acl: List of ips allowed to perform zone transfers with the zone server </p>
<p> The format of this string is identical to the format of an ipv4_alias entry.</p>
<h2>Example Mararc File</h2>
<pre># Example mararc file (unabridged version)
# The various zones we support
# We must initialize the csv2 hash, or MaraDNS will be unable to
# load any csv2 zone files
csv2 = {}
# This is just to show the format of the file
#csv2[&quot;example.com.&quot;] = &quot;db.example.com&quot;
# The address this DNS server runs on. If you want to bind 
# to multiple addresses, separate them with a comma like this:
# &quot;10.1.2.3,10.1.2.4,127.0.0.1&quot;
ipv4_bind_addresses = &quot;127.0.0.1&quot;
# The directory with all of the zone files
chroot_dir = &quot;/etc/maradns&quot;
# The numeric UID MaraDNS will run as
maradns_uid = 99
# The (optional) numeric GID MaraDNS will run as
# maradns_gid = 99
# The maximum number of threads (or processes, with the zone server)
# MaraDNS is allowed to run
maxprocs = 96
# It is possible to specify a different maximum number of processes that
# the zone server can run. If this is not set, the maximum number of 
# processes that the zone server can have defaults to the aqmaxprocsaq value
# above
# max_tcp_procs = 64
# Normally, MaraDNS has some MaraDNS-specific features, such as DDIP
# synthesizing, a special DNS query (&quot;erre-con-erre-cigarro.maradns.org.&quot; 
# with a TXT query returns the version of MaraDNS that a server is 
# running), unique handling of multiple QDCOUNTs, etc. Some people 
# might not like these features, so I have added a switch that lets 
# a sys admin disable all these features. Just give &quot;no_fingerprint&quot; 
# a value of one here, and MaraDNS should be more or less 
# indistinguishable from a tinydns server.
no_fingerprint = 0
# Normally, MaraDNS only returns A and MX records when given a
# QTYPE=* (all RR types) query. Changing the value of default_rrany_set
# to 15 causes MaraDNS to also return the NS and SOA records, which
# some registars require. The default value of this is 3
default_rrany_set = 3
# These constants limit the number of records we will display, in order
# to help keep packets 512 bytes or smaller. This, combined with round_robin
# record rotation, help to use DNS as a crude load-balancer.
# The maximum number of records to display in a chain of records (list
# of records) for a given host name
max_chain = 8
# The maximum number of records to display in a list of records in the
# additional section of a query. If this is any value besides one,
# round robin rotation is disabled (due to limitations in the current
# data structure MaraDNS uses)
max_ar_chain = 1
# The maximum number of records to show total for a given question
max_total = 20
# The number of messages we log to stdout
# 0: No messages except for fatal parsing errors and the legal disclaimer
# 1: Only startup messages logged (default)
# 2: Error queries logged
# 3: All queries logged (but not very verbosely right now)
verbose_level = 1
# Initialize the IP aliases, which are used by the list of root name servers,
# the ACL for zone transfers, and the ACL of who gets to perform recursive
# queries
ipv4_alias = {}
# Various sets of root name servers
# Note: Netmasks can exist, but are ignored when specifying root name server
# ICANN: the most common and most controversial root name server
# <a rel="nofollow" href="http://www.icann.org">http://www.icann.org</a>
# This list can be seen at <a rel="nofollow" href="http://www.root-servers.org/">http://www.root-servers.org/</a>
ipv4_alias[&quot;icann&quot;] = &quot;198.41.0.4, 192.228.79.201, 192.33.4.12, 128.8.10.90,&quot;
ipv4_alias[&quot;icann&quot;] += &quot;192.203.230.10, 192.5.5.241, 192.112.36.4,&quot;
ipv4_alias[&quot;icann&quot;] += &quot;128.63.2.53, 192.36.148.17, 192.58.128.30,&quot;
ipv4_alias[&quot;icann&quot;] += &quot;193.0.14.129, 198.32.64.12, 202.12.27.33&quot;
# OpenNIC: <a rel="nofollow" href="http://www.opennic.unrated.net/">http://www.opennic.unrated.net/</a>
# Current as of 2005/11/30; these servers change frequently so please
# look at their web page
ipv4_alias[&quot;opennic&quot;] = &quot;157.238.46.24, 209.104.33.250, 209.104.63.249,&quot;
ipv4_alias[&quot;opennic&quot;] += &quot;130.94.168.216, 209.21.75.53, 64.114.34.119,&quot;
ipv4_alias[&quot;opennic&quot;] += &quot;207.6.128.246, 167.216.255.199, 62.208.181.95,&quot;
ipv4_alias[&quot;opennic&quot;] += &quot;216.87.153.98, 216.178.136.116&quot;
# End of list of root name server lists
# Here is a ACL which restricts who is allowed to perform zone transfer from 
# the zoneserver program
# Simplest form: 10.1.1.1/24 (IP: 10.1.1.1, 24 left bits in IP need to match)
# and 10.100.100.100/255.255.255.224 (IP: 10.100.100.100, netmask
# 255.255.255.224) are allowed to connect to the zone server 
# NOTE: The &quot;maradns&quot; program does not serve zones. Zones are served
# by the &quot;zoneserver&quot; program.
#zone_transfer_acl = &quot;10.1.1.1/24, 10.100.100.100/255.255.255.224&quot;
# More complex: We create two aliases: One called &quot;office&quot; and another
# called &quot;home&quot;. We allow anyone in the office or at home to perform zone
# transfers
#ipv4_alias[&quot;office&quot;] = &quot;10.1.1.1/24&quot;
#ipv4_alias[&quot;home&quot;] = &quot;10.100.100.100/255.255.255.224&quot;
#zone_transfer_acl = &quot;office, home&quot;
# More complex then the last example. We have three employees,
# Susan, Becca, and Mia, whose computers we give zone transfer rights to.
# Susan and Becca are system administrators, and Mia is a developer.
# They are all part of the company. We give the entire company zone
# transfer access
#ipv4_alias[&quot;susan&quot;] = &quot;10.6.7.8/32&quot; # Single IP allowed
#ipv4_alias[&quot;becca&quot;] = &quot;10.7.8.9&quot; # also a single IP
#ipv4_alias[&quot;mia&quot;] = &quot;10.8.9.10/255.255.255.255&quot; # Also a single IP
#ipv4_alias[&quot;sysadmins&quot;] = &quot;susan, becca&quot;
#ipv4_alias[&quot;devel&quot;] = &quot;mia&quot;
#ipv4_alias[&quot;company&quot;] = &quot;sysadmins, devel&quot;
# This is equivalent to the above line
#ipv4_alias[&quot;company&quot;] = &quot;susan, becca, mia&quot;
#zone_transfer_acl = &quot;company&quot;
# If you want to enable recursion on the loopback interface, uncomment
# the relevent lines in the following section
# Recursive ACL: Who is allowd to perform recursive queries. The format
# is identical to that of &quot;zone_transfer_acl&quot;, including ipv4_alias support
#ipv4_alias[&quot;localhost&quot;] = &quot;127.0.0.0/8&quot;
#recursive_acl = &quot;localhost&quot;
# Random seed file: The file from which we read 16 bytes from to get the
# 128-bit random Rijndael key. This is ideally a file which is a good source
# of random numbers, but can also be a fixed file if your OS does not have
# a decent random number generator (make sure the contents of that file is
# random and with 600 perms, owned by root, since we read the file *before*
# dropping root privileges)
#random_seed_file = &quot;/dev/urandom&quot;
# The maximum number of elements we can have in the cache. If we have more 
# elements in the cache than this amount, the &quot;custodian&quot; kicks in to effect,
# removing elements not recently accessed from the cache (8 elements removed 
# per query) until we are at the 99% level or so again.
#maximum_cache_elements = 1024
# It is possible to change the minimul &quot;time to live&quot; for entries in the
# cache; this is the minimum time that an entry will stay in the cache.
# Value is in seconds; default is 300 (5 minutes)
#min_ttl = 300
# CNAME records generally take more effort to resolve in MaraDNS than
# non-CNAME records; it is a good idea to make this higher then min_ttl
# default value is to be the same as min_ttl
#min_ttl_cname = 900
# The root servers which we use when making recursive queries.
# The following line must be uncommented to enable custom root servers 
# for recursive queries
#root_servers = {}
# You can choose which set of root servers to use. Current values (set above)
# are: icann, osrc, alternic, opennic, pacificroot, irsc, tinc, and 
# superroot. 
#root_servers[&quot;.&quot;] = &quot;icann&quot;
# If you prefer to contact other recursive DNS servers instead of the ICANN
# root servers, this is done with the upstream_servers mararc variable:
#upstream_servers[&quot;.&quot;] = &quot;192.168.0.1, 192.168.0.2&quot;
# You can tell MaraDNS to *not* query certain DNS servers when in recursive
# mode. This is mainly used to not allow spam-friendly domains to resolve,
# since spammers are starting to get in the habit of using spam-friendly
# DNS servers to resolve their domains, allowing them to hop from ISP to 
# ISP. The format of this is the same as for zone_transfer_acl and 
# recursive_acl
# For example, at the time of this document (August 12, 2001), azmalink.net
# is a known spam-friendly DNS provider (see doc/detailed/spammers/azmalink.net
# for details.) Note that this is based on IPs, and azmalink.net constantly
# changes IPs (as they constantly have to change ISPs)
# 2002/10/12: Azmalink changed ISP again, this reflect their current ISP
ipv4_alias[&quot;azmalink&quot;] = &quot;12.164.194.0/24&quot;
# As of September 20, 2001, hiddenonline.net is a known spam-friendly
# DNS provider (see doc/detailed/spammers/hiddenonline for details).
ipv4_alias[&quot;hiddenonline&quot;] = &quot;65.107.225.0/24&quot;
spammers = &quot;azmalink,hiddenonline&quot;
# It is also possible to change the maximum number of times MaraDNS will
# follow a CNAME record or a NS record with a glue A record. The default
# value for this is ten.
#max_glueless_level = 10
# In addition, one can change the maximum number of total queries that
# MaraDNS will perform to look up a host name. The default value is 32.
#max_queries_total = 32
# In addition, one can change the amount of time that MaraDNS will wait
# for a DNS server to respond before giving up and trying the next DNS
# server on a list. Note that, the larger this value is, the slower 
# MaraDNS will process recursive queries when a DNS server is not 
# responding to DNS queries. The default value is two seconds.
#timeout_seconds = 2
# And that does it for the caching at this point</pre>
<h2>Bugs</h2>
<p>If one should declare the same the same index twice with a dictionary variable, MaraDNS will exit with a fatal error. This is because earlier versions of MaraDNS acted in a different manner than Python 2.3.3. With Python 2.3.3, the last declaration is used, while MaraDNS used to use the first declaration.</p>
<h2>Legal Disclaimer</h2>
<p>THIS SOFTWARE IS PROVIDED BY THE AUTHORS aqaqAS ISaqaq AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE AUTHORS OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.</p>
