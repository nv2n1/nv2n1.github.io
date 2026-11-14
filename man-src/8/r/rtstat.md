---
title: "rtstat(8)"
name: "rtstat"
section: "8"
letter: "r"
url: "/docs/linux/man/8-rtstat/"
description: "lnstat – unified linux network statistics"
---

<p>lnstat &#8211; unified linux network statistics</p>
<h2>Synopsis</h2>
<p><code>lnstat</code> [<i>options</i>]</p>
<h2>Description</h2>
<p>This manual page documents briefly the <code>lnstat</code> command. </p>
<p> <code>lnstat</code> is a generalized and more feature-complete replacement for the old rtstat program. It is commonly used to periodically print a selection of statistical values exported by the kernel. In addition to routing cache statistics, it supports any kind of statistics the linux kernel exports via a file in /proc/net/stat/. </p>
<p> Each file in /proc/net/stat/ contains a header line listing the column names. These names are used by <code>lnstat</code> as keys for selecting which statistics to print. For every CPU present in the system, a line follows which lists the actual values for each column of the file. <code>lnstat</code> sums these values up (which in fact are counters) before printing them. After each interval, only the difference to the last value is printed. </p>
<p> Files and columns may be selected by using the <code>-f</code> and <code>-k</code> parameters. By default, all columns of all files are printed.</p>
<h2>Options</h2>
<p>lnstat supports the following options.</p>
<dl>
<dt><code>-h, &#8211;help</code></p>
<dd>Show summary of options.</p>
<dt><code>-V, &#8211;version</code></p>
<dd>Show version of program.</p>
<dt><code>-c, &#8211;count &lt;count&gt;</code></p>
<dd>Print &lt;count&gt; number of intervals.</p>
<dt><code>-d, &#8211;dump</code></p>
<dd>Dump list of available files/keys.</p>
<dt><code>-f, &#8211;file &lt;file&gt;</code></p>
<dd>Statistics file to use, may be specified multiple times. By default all files in /proc/net/stat are scanned.</p>
<dt><code>-i, &#8211;interval &lt;intv&gt;</code></p>
<dd>Set interval to &#8216;intv&#8217; seconds.</p>
<dt><code>-j, &#8211;json</code></p>
<dd>Display results in JSON format</p>
<dt><code>-k, &#8211;keys k,k,k,&#8230;</code></p>
<dd>Display only keys specified. Each key <code>k</code> is of the form <code>[file:]key</code>. If <code>&lt;file&gt;</code> is given, the search for the given key is limited to that file. Otherwise the first file containing the searched key is being used.</p>
<dt><code>-s, &#8211;subject [0-2]</code></p>
<dd>Specify display of subject/header. &#8216;0&#8217; means no header at all, &#8216;1&#8217; prints a header only at start of the program and &#8216;2&#8217; prints a header every 20 lines.</p>
<dt><code>-w, &#8211;width n,n,n,&#8230;</code></p>
<dd>Width for each field.</dl>
<h2>Usage Examples</h2>
<dl>
<dt><code># lnstat -d</code></p>
<dd>Get a list of supported statistics files.</p>
<dt><code># lnstat -k arp_cache:entries,rt_cache:in_hit,arp_cache:destroys</code></p>
<dd>Select the specified files and keys.</p>
<dt><code># lnstat -i 10</code></p>
<dd>Use an interval of 10 seconds.</p>
<dt><code># lnstat -f ip_conntrack</code></p>
<dd>Use only the specified file for statistics.</p>
<dt><code># lnstat -s 0</code></p>
<dd>Do not print a header at all.</p>
<dt><code># lnstat -s 20</code></p>
<dd>Print a header at start and every 20 lines.</p>
<dt><code># lnstat -c -1 -i 1 -f rt_cache -k entries,in_hit,in_slow_tot</code></p>
<dd>Display statistics for keys entries, in_hit and in_slow_tot of field rt_cache every second. </p>
</dl>
<h2>Files</h2>
<dl>
<dt><code>/proc/net/stat/arp_cache, /proc/net/stat/ndisc_cache</code></p>
<dd>Statistics around neighbor cache and ARP. <code>arp_cache</code> is for IPv4, <code>ndisc_cache</code> is the same for IPv6. </p>
<p> <code>entries</code> Number of entries in the neighbor table. </p>
<p> <code>allocs</code> How many neighbor entries have been allocated. </p>
<p> <code>destroys</code> How many neighbor entries have been removed. </p>
<p> <code>hash_grows</code> How often the neighbor (hash) table was increased. </p>
<p> <code>lookups</code> How many lookups were performed. </p>
<p> <code>hits</code> How many <code>lookups</code> were successful. </p>
<p> <code>res_failed</code> How many neighbor lookups failed. </p>
<p> <code>rcv_probes_mcast</code> How many multicast neighbor solicitations were received. (IPv6 only.) </p>
<p> <code>rcv_probes_ucast</code> How many unicast neighbor solicitations were received. (IPv6 only.) </p>
<p> <code>periodic_gc_runs</code> How many garbage collection runs were executed. </p>
<p> <code>forced_gc_runs</code> How many forced garbage collection runs were executed. Happens when adding an entry and the table is too full. </p>
<p> <code>unresolved_discards</code> How many neighbor table entries were discarded due to lookup failure. </p>
<p> <code>table_fulls</code> Number of table overflows. Happens if table is full and forced GC run (see <code>forced_gc_runs</code>) has failed. </p>
<dt><code>/proc/net/stat/ip_conntrack, /proc/net/stat/nf_conntrack</code></p>
<dd>Conntrack related counters. <code>ip_conntrack</code> is for backwards compatibility with older userspace only and shows the same data as <code>nf_conntrack</code>. </p>
<p> <code>entries</code> Number of entries in conntrack table. </p>
<p> <code>searched</code> Number of conntrack table lookups performed. </p>
<p> <code>found</code> Number of <code>searched</code> entries which were successful. </p>
<p> <code>new</code> Number of conntrack entries added which were not expected before. </p>
<p> <code>invalid</code> Number of packets seen which can not be tracked. </p>
<p> <code>ignore</code> Number of packets seen which are already connected to a conntrack entry. </p>
<p> <code>delete</code> Number of conntrack entries which were removed. </p>
<p> <code>delete_list</code> Number of conntrack entries which were put to dying list. </p>
<p> <code>insert</code> Number of entries inserted into the list. </p>
<p> <code>insert_failed</code> Number of entries for which list insertion was attempted but failed (happens if the same entry is already present). </p>
<p> <code>drop</code> Number of packets dropped due to conntrack failure. Either new conntrack entry allocation failed, or protocol helper dropped the packet. </p>
<p> <code>early_drop</code> Number of dropped conntrack entries to make room for new ones, if maximum table size was reached. </p>
<p> <code>icmp_error</code> Number of packets which could not be tracked due to error situation. This is a subset of <code>invalid</code>. </p>
<p> <code>expect_new</code> Number of conntrack entries added after an expectation for them was already present. </p>
<p> <code>expect_create</code> Number of expectations added. </p>
<p> <code>expect_delete</code> Number of expectations deleted. </p>
<p> <code>search_restart</code> Number of conntrack table lookups which had to be restarted due to hashtable resizes. </p>
<dt><code>/proc/net/stat/rt_cache</code></p>
<dd>Routing cache statistics. </p>
<p> <code>entries</code> Number of entries in routing cache. </p>
<p> <code>in_hit</code> Number of route cache hits for incoming packets. Deprecated since IP route cache removal, therefore always zero. </p>
<p> <code>in_slow_tot</code> Number of routing cache entries added for input traffic. </p>
<p> <code>in_slow_mc</code> Number of multicast routing cache entries added for input traffic. </p>
<p> <code>in_no_route</code> Number of input packets for which no routing table entry was found. </p>
<p> <code>in_brd</code> Number of matched input broadcast packets. </p>
<p> <code>in_martian_dst</code> Number of incoming martian destination packets. </p>
<p> <code>in_martian_src</code> Number of incoming martian source packets. </p>
<p> <code>out_hit</code> Number of route cache hits for outgoing packets. Deprecated since IP route cache removal, therefore always zero. </p>
<p> <code>out_slow_tot</code> Number of routing cache entries added for output traffic. </p>
<p> <code>out_slow_mc</code> Number of multicast routing cache entries added for output traffic. </p>
<p> <code>gc_total</code> Total number of garbage collection runs. Deprecated since IP route cache removal, therefore always zero. </p>
<p> <code>gc_ignored</code> Number of ignored garbage collection runs due to minimum GC interval not reached and routing cache not full. Deprecated since IP route cache removal, therefore always zero. </p>
<p> <code>gc_goal_miss</code> Number of garbage collector goal misses. Deprecated since IP route cache removal, therefore always zero. </p>
<p> <code>gc_dst_overflow</code> Number of destination cache overflows. Deprecated since IP route cache removal, therefore always zero. </p>
<p> <code>in_hlist_search</code> Number of hash table list traversals for input traffic. Deprecated since IP route cache removal, therefore always zero. </p>
<p> <code>out_hlist_search</code> Number of hash table list traversals for output traffic. Deprecated since IP route cache removal, therefore always zero. </p>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-ip/">ip</a></code>(8)</p>
<h2>Author</h2>
<p>lnstat was written by Harald Welte &lt;laforge [at] gnumonks.org&gt;. </p>
<p> This manual page was written by Michael Prokop &lt;mika [at] grml.org&gt; for the Debian project (but may be used by others).</p>
