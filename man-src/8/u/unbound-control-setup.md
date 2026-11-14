---
title: "unbound-control-setup(8)"
name: "unbound-control-setup"
section: "8"
letter: "u"
url: "/docs/linux/man/8-unbound-control-setup/"
description: "unbound-control, unbound-control-setup – Unbound remote server control utility."
---

<p><code>unbound-control,</code> <code>unbound-control-setup</code> &#8211; Unbound remote server control utility.</p>
<h2>Synopsis</h2>
<p><code>unbound-control</code> [<code>-hq</code>] [<code>-c</code> <i>cfgfile</i>] [<code>-s</code> <i>server</i>] <i>command</i></p>
<h2>Description</h2>
<p><code>Unbound-control</code> performs remote administration on the <i><a href="/docs/linux/man/8-unbound/">unbound</a></i>(8) DNS server. It reads the configuration file, contacts the unbound server over SSL sends the command and displays the result. </p>
<p> The available options are:</p>
<dl>
<dt><code>-h</code></p>
<dd>Show the version and commandline option help.</p>
<dt><code>-c </code><i>cfgfile</i></p>
<dd>The config file to read with settings. If not given the default config file /etc/unbound/unbound.conf is used.</p>
<dt><code>-s </code><i>server[@port]</i></p>
<dd>IPv4 or IPv6 address of the server to contact. If not given, the address is read from the config file.</p>
<dt><code>-q</code></p>
<dd>quiet, if the option is given it does not print anything if it works ok.</dl>
<h2>Commands</h2>
<p>There are several commands that the server understands.</p>
<dl>
<dt><code>start</code></p>
<dd>Start the server. Simply execs <i><a href="/docs/linux/man/8-unbound/">unbound</a></i>(8). The unbound executable is searched for in the <code>PATH</code> set in the environment. It is started with the config file specified using <i>-c</i> or the default config file.</p>
<dt><code>stop</code></p>
<dd>Stop the server. The server daemon exits.</p>
<dt><code>reload</code></p>
<dd>Reload the server. This flushes the cache and reads the config file fresh.</p>
<dt><code>verbosity </code><i>number</i></p>
<dd>Change verbosity value for logging. Same values as <code>verbosity</code> keyword in <i><a href="/docs/linux/man/5-unbound-conf/">unbound.conf</a></i>(5). This new setting lasts until the server is issued a reload (taken from config file again), or the next verbosity control command.</p>
<dt><code>log_reopen</code></p>
<dd>Reopen the logfile, close and open it. Useful for logrotation to make the daemon release the file it is logging to. If you are using syslog it will attempt to close and open the syslog (which may not work if chrooted).</p>
<dt><code>stats</code></p>
<dd>Print statistics. Resets the internal counters to zero, this can be controlled using the <code>statistics-cumulative</code> config statement. Statistics are printed with one [name]: [value] per line.</p>
<dt><code>stats_noreset</code></p>
<dd>Peek at statistics. Prints them like the <code>stats</code> command does, but does not reset the internal counters to zero.</p>
<dt><code>status</code></p>
<dd>Display server status. Exit code 3 if not running (the connection to the port is refused), 1 on error, 0 if running.</p>
<dt><code>local_zone </code><i>name</i> <i>type</i></p>
<dd>Add new local zone with name and type. Like <code>local-zone</code> config statement. If the zone already exists, the type is changed to the given argument.</p>
<dt><code>local_zone_remove </code><i>name</i></p>
<dd>Remove the local zone with the given name. Removes all local data inside it. If the zone does not exist, the command succeeds.</p>
<dt><code>local_data </code><i>RR data&#8230;</i></p>
<dd>Add new local data, the given resource record. Like <code>local-data</code> config statement, except for when no covering zone exists. In that case this remote control command creates a transparent zone with the same name as this record. This command is not good at returning detailed syntax errors.</p>
<dt><code>local_data_remove </code><i>name</i></p>
<dd>Remove all RR data from local name. If the name already has no items, nothing happens. Often results in NXDOMAIN for the name (in a static zone), but if the name has become an empty nonterminal (there is still data in domain names below the removed name), NOERROR nodata answers are the result for that name.</p>
<dt><code>dump_cache</code></p>
<dd>The contents of the cache is printed in a text format to stdout. You can redirect it to a file to store the cache in a file.</p>
<dt><code>load_cache</code></p>
<dd>The contents of the cache is loaded from stdin. Uses the same format as dump_cache uses. Loading the cache with old, or wrong data can result in old or wrong data returned to clients. Loading data into the cache in this way is supported in order to aid with debugging.</p>
<dt><code>lookup </code><i>name</i></p>
<dd>Print to stdout the name servers that would be used to look up the name specified.</p>
<dt><code>flush </code><i>name</i></p>
<dd>Remove the name from the cache. Removes the types A, AAAA, NS, SOA, CNAME, DNAME, MX, PTR, SRV and NAPTR. Because that is fast to do. Other record types can be removed using <code>flush_type </code> or <code>flush_zone</code>.</p>
<dt><code>flush_type </code><i>name</i> <i>type</i></p>
<dd>Remove the name, type information from the cache.</p>
<dt><code>flush_zone </code><i>name</i></p>
<dd>Remove all information at or below the name from the cache. The rrsets and key entries are removed so that new lookups will be performed. This needs to walk and inspect the entire cache, and is a slow operation.</p>
<dt><code>flush_bogus</code></p>
<dd>Remove all bogus data from the cache.</p>
<dt><code>flush_stats</code></p>
<dd>Reset statistics to zero.</p>
<dt><code>flush_requestlist</code></p>
<dd>Drop the queries that are worked on. Stops working on the queries that the server is working on now. The cache is unaffected. No reply is sent for those queries, probably making those users request again later. Useful to make the server restart working on queries with new settings, such as a higher verbosity level.</p>
<dt><code>dump_requestlist</code></p>
<dd>Show what is worked on. Prints all queries that the server is currently working on. Prints the time that users have been waiting. For internal requests, no time is printed. And then prints out the module status.</p>
<dt><code>flush_infra </code><i>all|IP</i></p>
<dd>If all then entire infra cache is emptied. If a specific IP address, the entry for that address is removed from the cache. It contains EDNS, ping and lameness data.</p>
<dt><code>dump_infra</code></p>
<dd>Show the contents of the infra cache.</p>
<dt><code>set_option </code><i>opt: val</i></p>
<dd>Set the option to the given value without a reload. The cache is therefore not flushed. The option must end with a &#8216;:&#8217; and whitespace must be between the option and the value. Some values may not have an effect if set this way, the new values are not written to the config file, not all options are supported. This is different from the set_option call in libunbound, where all values work because unbound has not been inited.</p>
<dd>The values that work are: statistics-interval, statistics-cumulative, do-not-query-localhost, harden-short-bufsize, harden-large-queries, harden-glue, harden-dnssec-stripped, harden-below-nxdomain, harden-referral-path, prefetch, prefetch-key, log-queries, hide-identity, hide-version, identity, version, val-log-level, val-log-squelch, ignore-cd-flag, add-holddown, del-holddown, keep-missing, tcp-upstream, ssl-upstream.</p>
<dt><code>get_option </code><i>opt</i></p>
<dd>Get the value of the option. Give the option name without a trailing &#8216;:&#8217;. The value is printed. If the value is &quot;&quot;, nothing is printed and the connection closes. On error &#8216;error &#8230;&#8217; is printed (it gives a syntax error on unknown option). For some options a list of values, one on each line, is printed. The options are shown from the config file as modified with set_option. For some options an override may have been taken that does not show up with this command, not results from e.g. the verbosity and forward control commands. Not all options work, see list_stubs, list_forwards, list_local_zones and list_local_data for those.</p>
<dt><code>list_stubs</code></p>
<dd>List the stub zones in use. These are printed one by one to the output. This includes the root hints in use.</p>
<dt><code>list_forwards</code></p>
<dd>List the forward zones in use. These are printed zone by zone to the output.</p>
<dt><code>list_local_zones</code></p>
<dd>List the local zones in use. These are printed one per line with zone type.</p>
<dt><code>list_local_data</code></p>
<dd>List the local data RRs in use. The resource records are printed.</p>
<dt><code>forward_add </code>[<i>+i</i>] <i>zone addr &#8230;</i></p>
<dd>Add a new forward zone to running unbound. With +i option also adds a <i>domain-insecure</i> for the zone (so it can resolve insecurely if you have a DNSSEC root trust anchor configured for other names). The addr can be IP4, IP6 or nameserver names, like <i>forward-zone</i> config in unbound.conf.</p>
<dt><code>forward_remove </code>[<i>+i</i>] <i>zone</i></p>
<dd>Remove a forward zone from running unbound. The +i also removes a <i>domain-insecure</i> for the zone.</p>
<dt><code>stub_add </code>[<i>+ip</i>] <i>zone addr &#8230;</i></p>
<dd>Add a new stub zone to running unbound. With +i option also adds a <i>domain-insecure</i> for the zone. With +p the stub zone is set to prime, without it it is set to notprime. The addr can be IP4, IP6 or nameserver names, like the <i>stub-zone</i> config in unbound.conf.</p>
<dt><code>stub_remove </code>[<i>+i</i>] <i>zone</i></p>
<dd>Remove a stub zone from running unbound. The +i also removes a <i>domain-insecure</i> for the zone.</p>
<dt><code>forward </code>[<i>off</i> | <i>addr &#8230;</i> ]</p>
<dd>Setup forwarding mode. Configures if the server should ask other upstream nameservers, should go to the internet root nameservers itself, or show the current config. You could pass the nameservers after a DHCP update.</p>
<dd>Without arguments the current list of addresses used to forward all queries to is printed. On startup this is from the forward-zone &quot;.&quot; configuration. Afterwards it shows the status. It prints off when no forwarding is used.</p>
<dd>If <i>off</i> is passed, forwarding is disabled and the root nameservers are used. This can be used to avoid to avoid buggy or non-DNSSEC supporting nameservers returned from DHCP. But may not work in hotels or hotspots.</p>
<dd>If one or more IPv4 or IPv6 addresses are given, those are then used to forward queries to. The addresses must be separated with spaces. With &#8216;@port&#8217; the port number can be set explicitly (default port is 53 (DNS)).</p>
<dd>By default the forwarder information from the config file for the root &quot;.&quot; is used. The config file is not changed, so after a reload these changes are gone. Other forward zones from the config file are not affected by this command.</dl>
<h2>Exit Code</h2>
<p>The unbound-control program exits with status code 1 on error, 0 on success.</p>
<h2>Set Up</h2>
<p>The setup requires a self-signed certificate and private keys for both the server and client. The script <i>unbound-control-setup</i> generates these in the default run directory, or with -d in another directory. If you change the access control permissions on the key files you can decide who can use unbound-control, by default owner and group but not all users. Run the script under the same username as you have configured in unbound.conf or as root, so that the daemon is permitted to read the files, for example with: </p>
<pre> sudo -u unbound unbound-control-setup</pre>
<p>If you have not configured a username in unbound.conf, the keys need read permission for the user credentials under which the daemon is started. The script preserves private keys present in the directory. After running the script as root, turn on <code>control-enable</code> in <i>unbound.conf</i>.</p>
<h2>Statistic Counters</h2>
<p>The <i>stats</i> command shows a number of statistic counters.</p>
<dl>
<dt><i>threadX.num.queries</i></p>
<dd>number of queries received by thread</p>
<dt><i>threadX.num.cachehits</i></p>
<dd>number of queries that were successfully answered using a cache lookup</p>
<dt><i>threadX.num.cachemiss</i></p>
<dd>number of queries that needed recursive processing</p>
<dt><i>threadX.num.prefetch</i></p>
<dd>number of cache prefetches performed. This number is included in cachehits, as the original query had the unprefetched answer from cache, and resulted in recursive processing, taking a slot in the requestlist. Not part of the recursivereplies (or the histogram thereof) or cachemiss, as a cache response was sent.</p>
<dt><i>threadX.num.recursivereplies</i></p>
<dd>The number of replies sent to queries that needed recursive processing. Could be smaller than threadX.num.cachemiss if due to timeouts no replies were sent for some queries.</p>
<dt><i>threadX.requestlist.avg</i></p>
<dd>The average number of requests in the internal recursive processing request list on insert of a new incoming recursive processing query.</p>
<dt><i>threadX.requestlist.max</i></p>
<dd>Maximum size attained by the internal recursive processing request list.</p>
<dt><i>threadX.requestlist.overwritten</i></p>
<dd>Number of requests in the request list that were overwritten by newer entries. This happens if there is a flood of queries that recursive processing and the server has a hard time.</p>
<dt><i>threadX.requestlist.exceeded</i></p>
<dd>Queries that were dropped because the request list was full. This happens if a flood of queries need recursive processing, and the server can not keep up.</p>
<dt><i>threadX.requestlist.current.all</i></p>
<dd>Current size of the request list, includes internally generated queries (such as priming queries and glue lookups).</p>
<dt><i>threadX.requestlist.current.user</i></p>
<dd>Current size of the request list, only the requests from client queries.</p>
<dt><i>threadX.recursion.time.avg</i></p>
<dd>Average time it took to answer queries that needed recursive processing. Note that queries that were answered from the cache are not in this average.</p>
<dt><i>threadX.recursion.time.median</i></p>
<dd>The median of the time it took to answer queries that needed recursive processing. The median means that 50% of the user queries were answered in less than this time. Because of big outliers (usually queries to non responsive servers), the average can be bigger than the median. This median has been calculated by interpolation from a histogram.</p>
<dt><i>total.num.queries</i></p>
<dd>summed over threads.</p>
<dt><i>total.num.cachehits</i></p>
<dd>summed over threads.</p>
<dt><i>total.num.cachemiss</i></p>
<dd>summed over threads.</p>
<dt><i>total.num.prefetch</i></p>
<dd>summed over threads.</p>
<dt><i>total.num.recursivereplies</i></p>
<dd>summed over threads.</p>
<dt><i>total.requestlist.avg</i></p>
<dd>averaged over threads.</p>
<dt><i>total.requestlist.max</i></p>
<dd>the maximum of the thread requestlist.max values.</p>
<dt><i>total.requestlist.overwritten</i></p>
<dd>summed over threads.</p>
<dt><i>total.requestlist.exceeded</i></p>
<dd>summed over threads.</p>
<dt><i>total.requestlist.current.all</i></p>
<dd>summed over threads.</p>
<dt><i>total.recursion.time.median</i></p>
<dd>averaged over threads.</p>
<dt><i>time.now</i></p>
<dd>current time in seconds since 1970.</p>
<dt><i>time.up</i></p>
<dd>uptime since server boot in seconds.</p>
<dt><i>time.elapsed</i></p>
<dd>time since last statistics printout, in seconds.</dl>
<h2>Extended Statistics</h2>
<dl>
<dt><i>mem.total.sbrk</i></p>
<dd>If <a href="/docs/linux/man/2-sbrk/">sbrk</a>(2) is available, an estimate of the heap size of the program in number of bytes. Close to the total memory used by the program, as reported by top and ps. Could be wrong if the OS allocates memory non-contiguously.</p>
<dt><i>mem.cache.rrset</i></p>
<dd>Memory in bytes in use by the RRset cache.</p>
<dt><i>mem.cache.message</i></p>
<dd>Memory in bytes in use by the message cache.</p>
<dt><i>mem.mod.iterator</i></p>
<dd>Memory in bytes in use by the iterator module.</p>
<dt><i>mem.mod.validator</i></p>
<dd>Memory in bytes in use by the validator module. Includes the key cache and negative cache.</p>
<dt><i>histogram.&lt;sec&gt;.&lt;usec&gt;.to.&lt;sec&gt;.&lt;usec&gt;</i></p>
<dd>Shows a histogram, summed over all threads. Every element counts the recursive queries whose reply time fit between the lower and upper bound. Times larger or equal to the lowerbound, and smaller than the upper bound. There are 40 buckets, with bucket sizes doubling.</p>
<dt><i>num.query.type.A</i></p>
<dd>The total number of queries over all threads with query type A. Printed for the other query types as well, but only for the types for which queries were received, thus =0 entries are omitted for brevity.</p>
<dt><i>num.query.type.other</i></p>
<dd>Number of queries with query types 256-65535.</p>
<dt><i>num.query.class.IN</i></p>
<dd>The total number of queries over all threads with query class IN (internet). Also printed for other classes (such as CH (CHAOS) sometimes used for debugging), or NONE, ANY, used by dynamic update. num.query.class.other is printed for classes 256-65535.</p>
<dt><i>num.query.opcode.QUERY</i></p>
<dd>The total number of queries over all threads with query opcode QUERY. Also printed for other opcodes, UPDATE, &#8230;</p>
<dt><i>num.query.tcp</i></p>
<dd>Number of queries that were made using TCP towards the unbound server.</p>
<dt><i>num.query.ipv6</i></p>
<dd>Number of queries that were made using IPv6 towards the unbound server.</p>
<dt><i>num.query.flags.RD</i></p>
<dd>The number of queries that had the RD flag set in the header. Also printed for flags QR, AA, TC, RA, Z, AD, CD. Note that queries with flags QR, AA or TC may have been rejected because of that.</p>
<dt><i>num.query.edns.present</i></p>
<dd>number of queries that had an EDNS OPT record present.</p>
<dt><i>num.query.edns.DO</i></p>
<dd>number of queries that had an EDNS OPT record with the DO (DNSSEC OK) bit set. These queries are also included in the num.query.edns.present number.</p>
<dt><i>num.answer.rcode.NXDOMAIN</i></p>
<dd>The number of answers to queries, from cache or from recursion, that had the return code NXDOMAIN. Also printed for the other return codes.</p>
<dt><i>num.answer.rcode.nodata</i></p>
<dd>The number of answers to queries that had the pseudo return code nodata. This means the actual return code was NOERROR, but additionally, no data was carried in the answer (making what is called a NOERROR/NODATA answer). These queries are also included in the num.answer.rcode.NOERROR number. Common for AAAA lookups when an A record exists, and no AAAA.</p>
<dt><i>num.answer.secure</i></p>
<dd>Number of answers that were secure. The answer validated correctly. The AD bit might have been set in some of these answers, where the client signalled (with DO or AD bit in the query) that they were ready to accept the AD bit in the answer.</p>
<dt><i>num.answer.bogus</i></p>
<dd>Number of answers that were bogus. These answers resulted in SERVFAIL to the client because the answer failed validation.</p>
<dt><i>num.rrset.bogus</i></p>
<dd>The number of rrsets marked bogus by the validator. Increased for every RRset inspection that fails.</p>
<dt><i>unwanted.queries</i></p>
<dd>Number of queries that were refused or dropped because they failed the access control settings.</p>
<dt><i>unwanted.replies</i></p>
<dd>Replies that were unwanted or unsolicited. Could have been random traffic, delayed duplicates, very late answers, or could be spoofing attempts. Some low level of late answers and delayed duplicates are to be expected with the UDP protocol. Very high values could indicate a threat (spoofing).</dl>
<h2>Files</h2>
<dl>
<dt><i>/etc/unbound/unbound.conf</i></p>
<dd>unbound configuration file.</p>
<dt><i>/etc/unbound</i></p>
<dd>directory with private keys (unbound_server.key and unbound_control.key) and self-signed certificates (unbound_server.pem and unbound_control.pem).</dl>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/5-unbound-conf/">unbound.conf</a></i>(5), <i><a href="/docs/linux/man/8-unbound/">unbound</a></i>(8). </p>
