---
title: "ipset(8)"
name: "ipset"
section: "8"
letter: "i"
url: "/docs/linux/man/8-ipset/"
description: "ipset — administration tool for IP sets"
---

<p>ipset &#8212; administration tool for IP sets</p>
<h2>Synopsis</h2>
<p><code>ipset</code> [ <i>OPTIONS</i> ] <i>COMMAND</i> [ <i>COMMAND-OPTIONS</i> ] </p>
<pre><code>COMMANDS := { create | add | del | test | destroy | list | save | restore | flush | rename | swap | help | version | - }
OPTIONS := { -exist | -output { plain | save | xml } | -quiet | -resolve | -sorted | -name | -terse | -file filename }</code></pre>
<p> <code>ipset</code> <code>create</code> <i>SETNAME</i> <i>TYPENAME</i> [ <i>CREATE-OPTIONS</i> ] <code>ipset</code> <code>add</code> <i>SETNAME</i> <i>ADD-ENTRY</i> [ <i>ADD-OPTIONS</i> ] <code>ipset</code> <code>del</code> <i>SETNAME</i> <i>DEL-ENTRY</i> [ <i>DEL-OPTIONS</i> ] <code>ipset</code> <code>test</code> <i>SETNAME</i> <i>TEST-ENTRY</i> [ <i>TEST-OPTIONS</i> ] <code>ipset</code> <code>destroy</code> [ <i>SETNAME</i> ] <code>ipset</code> <code>list</code> [ <i>SETNAME</i> ] <code>ipset</code> <code>save</code> [ <i>SETNAME</i> ] <code>ipset</code> <code>restore</code> <code>ipset</code> <code>flush</code> [ <i>SETNAME</i> ] <code>ipset</code> <code>rename</code> <i>SETNAME-FROM</i> <i>SETNAME-TO</i> <code>ipset</code> <code>swap</code> <i>SETNAME-FROM</i> <i>SETNAME-TO</i> <code>ipset</code> <code>help</code> [ <i>TYPENAME</i> ] <code>ipset</code> <code>version</code> <code>ipset</code> <code>&#8211;</code></p>
<h2>Description</h2>
<p><code>ipset</code> is used to set up, maintain and inspect so called IP sets in the Linux kernel. Depending on the type of the set, an IP set may store IP(v4/v6) addresses, (TCP/UDP) port numbers, IP and MAC address pairs, IP address and port number pairs, etc. See the set type definitions below. </p>
<p> <code>Iptables</code> matches and targets referring to sets create references, which protect the given sets in the kernel. A set cannot be destroyed while there is a single reference pointing to it.</p>
<h2>Options</h2>
<p>The options that are recognized by <code>ipset</code> can be divided into several different groups.</p>
<h3>Commands</h3>
<p>These options specify the desired action to perform. Only one of them can be specified on the command line unless otherwise specified below. For all the long versions of the command names, you need to use only enough letters to ensure that <code>ipset</code> can differentiate it from all other commands. The <code>ipset</code> parser follows the order here when looking for the shortest match in the long command names.</p>
<dl>
<dt><code>n</code>, <code>create</code> <i>SETNAME</i> <i>TYPENAME</i> [ <i>CREATE-OPTIONS</i> ]</p>
<dd>Create a set identified with setname and specified type. The type may require type specific options. If the <code>-exist</code> option is specified, <code>ipset</code> ignores the error otherwise raised when the same set (setname and create parameters are identical) already exists.</p>
<dt><code>add</code> <i>SETNAME</i> <i>ADD-ENTRY</i> [ <i>ADD-OPTIONS</i> ]</p>
<dd>Add a given entry to the set. If the <code>-exist</code> option is specified, <code>ipset</code> ignores if the entry already added to the set.</p>
<dt><code>del</code> <i>SETNAME</i> <i>DEL-ENTRY</i> [ <i>DEL-OPTIONS</i> ]</p>
<dd>Delete an entry from a set. If the <code>-exist</code> option is specified and the entry is not in the set (maybe already expired), then the command is ignored.</p>
<dt><code>test</code> <i>SETNAME</i> <i>TEST-ENTRY</i> [ <i>TEST-OPTIONS</i> ]</p>
<dd>Test whether an entry is in a set or not. Exit status number is zero if the tested entry is in the set and nonzero if it is missing from the set.</p>
<dt><code>x</code>, <code>destroy</code> [ <i>SETNAME</i> ]</p>
<dd>Destroy the specified set or all the sets if none is given. </p>
<p> If the set has got reference(s), nothing is done and no set destroyed.</p>
<dt><code>list</code> [ <i>SETNAME</i> ] [ <i>OPTIONS</i> ]</p>
<dd>List the header data and the entries for the specified set, or for all sets if none is given. The <code>-resolve</code> option can be used to force name lookups (which may be slow). When the <code>-sorted</code> option is given, the entries are listed sorted (if the given set type supports the operation). The option <code>-output</code> can be used to control the format of the listing: <code>plain</code>, <code>save</code> or <code>xml</code>. (The default is <code>plain</code>.) If the option <code>-name</code> is specified, just the names of the existing sets are listed. If the option <code>-terse</code> is specified, just the set names and headers are listed. The output is printed to stdout, the option <code>-file</code> can be used to specify a filename instead of stdout.</p>
<dt><code>save</code> [ <i>SETNAME</i> ]</p>
<dd>Save the given set, or all sets if none is given to stdout in a format that <code>restore</code> can read. The option <code>-file</code> can be used to specify a filename instead of stdout.</p>
<dt><code>restore</code></p>
<dd>Restore a saved session generated by <code>save</code>. The saved session can be fed from stdin or the option <code>-file</code> can be used to specify a filename instead of stdin. </p>
<p> Please note, existing sets and elements are not erased by <code>restore</code> unless specified so in the restore file. All commands are allowed in restore mode except <code>list</code>, <code>help</code>, <code>version</code>, interactive mode and <code>restore</code> itself.</p>
<dt><code>flush</code> [ <i>SETNAME</i> ]</p>
<dd>Flush all entries from the specified set or flush all sets if none is given.</p>
<dt><code>e</code>, <code>rename</code> <i>SETNAME-FROM</i> <i>SETNAME-TO</i></p>
<dd>Rename a set. Set identified by <i>SETNAME-TO</i> must not exist.</p>
<dt><code>w</code>, <code>swap</code> <i>SETNAME-FROM</i> <i>SETNAME-TO</i></p>
<dd>Swap the content of two sets, or in another words, exchange the name of two sets. The referred sets must exist and compatible type of sets can be swapped only.</p>
<dt><code>help</code> [ <i>TYPENAME</i> ]</p>
<dd>Print help and set type specific help if <i>TYPENAME</i> is specified.</p>
<dt><code>version</code></p>
<dd>Print program version.</p>
<dt><code>&#8211;</code></p>
<dd>If a dash is specified as command, then <code>ipset</code> enters a simple interactive mode and the commands are read from the standard input. The interactive mode can be finished by entering the pseudo-command <code>quit</code>.</dl>
<h3>Other Options</h3>
<p>The following additional options can be specified. The long option names cannot be abbreviated.</p>
<dl>
<dt><code>-!</code>, <code>-exist</code></p>
<dd>Ignore errors when exactly the same set is to be created or already added entry is added or missing entry is deleted.</p>
<dt><code>-o</code>, <code>-output</code> { <code>plain</code> | <code>save</code> | <code>xml</code> }</p>
<dd>Select the output format to the <code>list</code> command.</p>
<dt><code>-q</code>, <code>-quiet</code></p>
<dd>Suppress any output to stdout and stderr. <code>ipset</code> will still exit with error if it cannot continue.</p>
<dt><code>-r</code>, <code>-resolve</code></p>
<dd>When listing sets, enforce name lookup. The program will try to display the IP entries resolved to host names which requires <code>slow</code> DNS lookups.</p>
<dt><code>-s</code>, <code>-sorted</code></p>
<dd>Sorted output. When listing sets entries are listed sorted. Not supported yet.</p>
<dt><code>-n</code>, <code>-name</code></p>
<dd>List just the names of the existing sets, i.e. suppress listing of set headers and members.</p>
<dt><code>-t</code>, <code>-terse</code></p>
<dd>List the set names and headers, i.e. suppress listing of set members.</p>
<dt><code>-f</code>, <code>-file</code> <i>filename</i></p>
<dd>Specify a filename to print into instead of stdout (<code>list</code> or <code>save</code> commands) or read from instead of stdin (<code>restore</code> command).</dl>
<h2>Introduction</h2>
<p>A set type comprises of the storage method by which the data is stored and the data type(s) which are stored in the set. Therefore the <i>TYPENAME</i> parameter of the <code>create</code> command follows the syntax </p>
<p> <i>TYPENAME</i> := <i>method</i><code>:</code><i>datatype</i>[<code>,</code><i>datatype</i>[<code>,</code><i>datatype</i>]] </p>
<p> where the current list of the methods are <code>bitmap</code>, <code>hash</code>, and <code>list</code> and the possible data types are <code>ip</code>, <code>net</code>, <code>mac</code>, <code>port</code> and <code>iface</code>. The dimension of a set is equal to the number of data types in its type name. </p>
<p> When adding, deleting or testing entries in a set, the same comma separated data syntax must be used for the entry parameter of the commands, i.e</p>
<dl>
<dd>ipset add foo ipaddr,portnum,ipaddr</dl>
<p> If host names or service names with dash in the name are used instead of IP addresses or service numbers, then the host name or service name must be enclosed in square brackets. Example:</p>
<dl>
<dd>ipset add foo [test-hostname],[ftp-data]</dl>
<p> In the case of host names the DNS resolver is called internally by <code>ipset</code> but if it returns multiple IP addresses, only the first one is used. </p>
<p> The <code>bitmap</code> and <code>list</code> types use a fixed sized storage. The <code>hash</code> types use a hash to store the elements. In order to avoid clashes in the hash, a limited number of chaining, and if that is exhausted, the doubling of the hash size is performed when adding entries by the <code>ipset</code> command. When entries added by the <code>SET</code> target of <code>iptables/ip6tables</code>, then the hash size is fixed and the set won&#8217;t be duplicated, even if the new entry cannot be added to the set.</p>
<h2>Generic Create And Add Options</h2>
<h3>timeout</h3>
<p>All set types supports the optional <code>timeout</code> parameter when creating a set and adding entries. The value of the <code>timeout</code> parameter for the <code>create</code> command means the default timeout value (in seconds) for new entries. If a set is created with timeout support, then the same <code>timeout</code> option can be used to specify non-default timeout values when adding entries. Zero timeout value means the entry is added permanent to the set. The timeout value of already added elements can be changed by re-adding the element using the <code>-exist</code> option. Example:</p>
<dl>
<dd>ipset create test hash:ip timeout 300</p>
<dd>ipset add test 192.168.0.1 timeout 60</p>
<dd>ipset -exist add test 192.168.0.1 timeout 600</dl>
<p> When listing the set, the number of entries printed in the header might be larger than the listed number of entries for sets with the timeout extensions: the number of entries in the set is updated when elements added/deleted to the set and periodically when the garbage collector evicts the timed out entries.</p>
<h3>counters, packets, bytes</h3>
<p>All set types support the optional <code>counters</code> option when creating a set. If the option is specified then the set is created with packet and byte counters per element support. The packet and byte counters are initialized to zero when the elements are (re-)added to the set, unless the packet and byte counter values are explicitly specified by the <code>packets</code> and <code>bytes</code> options. An example when an element is added to a set with non-zero counter values:</p>
<dl>
<dd>ipset create foo hash:ip counters</p>
<dd>ipset add foo 192.168.1.1 packets 42 bytes 1024</dl>
<h3>comment</h3>
<p>All set types support the optional <code>comment</code> extension. Enabling this extension on an ipset enables you to annotate an ipset entry with an arbitrary string. This string is completely ignored by both the kernel and ipset itself and is purely for providing a convenient means to document the reason for an entry&#8217;s existence. Comments must not contain any quotation marks and the usual escape character (\) has no meaning. For example, the following shell command is illegal:</p>
<dl>
<dd>ipset add foo 1.1.1.1 comment &quot;this comment is \&quot;bad\&quot;&quot;</dl>
<p> In the above, your shell will of course escape the quotation marks and ipset will see the quote marks in the argument for the comment, which will result in a parse error. If you are writing your own system, you should avoid creating comments containing a quotation mark if you do not want to break &quot;ipset save&quot; and &quot;ipset restore&quot;, nonetheless, the kernel will not stop you from doing so. The following is perfectly acceptable:</p>
<dl>
<dd>ipset create foo hash:ip comment</p>
<dd>ipset add foo 192.168.1.1/24 comment &quot;allow access to SMB share on \\fileserv\&quot;</p>
<dd>the above would appear as: &quot;allow access to SMB share on \fileserv\&quot;</dl>
<h3>skbinfo, skbmark, skbprio, skbqueue</h3>
<p>All set types support the optional <code>skbinfo</code> extension. This extension allows you to store the metainfo (firewall mark, tc class and hardware queue) with every entry and map it to packets by usage of SET netfilter target with &#8211;map-set option. <code>skbmark</code> option format: <code>MARK</code> or <code>MARK/MASK</code>, where <code>MARK</code> and <code>MASK</code> are 32bit hex numbers with 0x prefix. If only <code>mark</code> is specified mask 0xffffffff are used. <code>skbprio</code> option has tc class format: <code>MAJOR:MINOR</code>, where <code>major</code> and <code>minor</code> numbers are hex without 0x prefix. <code>skbqueue</code> option is just decimal number.</p>
<dl>
<dd>ipset create foo hash:ip skbinfo</p>
<dd>ipset add foo skbmark 0x1111/0xff00ffff skbprio 1:10 skbqueue 10</dl>
<h3>hashsize</h3>
<p>This parameter is valid for the <code>create</code> command of all <code>hash</code> type sets. It defines the initial hash size for the set, default is 1024. The hash size must be a power of two, the kernel automatically rounds up non power of two hash sizes to the first correct value. Example:</p>
<dl>
<dd>ipset create test hash:ip hashsize 1536</dl>
<h3>maxelem</h3>
<p>This parameter is valid for the <code>create</code> command of all <code>hash</code> type sets. It does define the maximal number of elements which can be stored in the set, default 65536. Example:</p>
<dl>
<dd>ipset create test hash:ip maxelem 2048.</dl>
<h3>family { inet | inet6 }</h3>
<p>This parameter is valid for the <code>create</code> command of all <code>hash</code> type sets except for hash:mac. It defines the protocol family of the IP addresses to be stored in the set. The default is <code>inet</code>, i.e IPv4. For the <code>inet</code> family one can add or delete multiple entries by specifying a range or a network of IPv4 addresses in the IP address part of the entry: </p>
<p> <i>ipaddr</i> := { <i>ip</i> | <i>fromaddr</i>&#8211;<i>toaddr</i> | <i>ip</i>/<i>cidr</i> } </p>
<p> <i>netaddr</i> := { <i>fromaddr</i>&#8211;<i>toaddr</i> | <i>ip</i>/<i>cidr</i> } </p>
<p> Example:</p>
<dl>
<dd>ipset create test hash:ip family inet6</dl>
<h3>nomatch</h3>
<p>The <code>hash</code> set types which can store <code>net</code> type of data (i.e. hash:*net*) support the optional <code>nomatch</code> option when adding entries. When matching elements in the set, entries marked as <code>nomatch</code> are skipped as if those were not added to the set, which makes possible to build up sets with exceptions. See the example at hash type <code>hash:net</code> below. </p>
<p> When elements are tested by <code>ipset</code>, the <code>nomatch</code> flags are taken into account. If one wants to test the existence of an element marked with <code>nomatch</code> in a set, then the flag must be specified too.</p>
<h3>forceadd</h3>
<p>All hash set types support the optional <code>forceadd</code> parameter when creating a set. When sets created with this option become full the next addition to the set may succeed and evict a random entry from the set.</p>
<dl>
<dd>ipset create foo hash:ip forceadd</dl>
<h2>Set Types</h2>
<h3>bitmap:ip</h3>
<p>The <code>bitmap:ip</code> set type uses a memory range to store either IPv4 host (default) or IPv4 network addresses. A <code>bitmap:ip</code> type of set can store up to 65536 entries. </p>
<p> <i>CREATE-OPTIONS</i> := <code>range</code> <i>fromip</i>&#8211;<i>toip</i>|<i>ip</i>/<i>cidr</i> [ <code>netmask</code> <i>cidr</i> ] [ <code>timeout</code> <i>value</i> ] [ <code>counters</code> ] [ <code>comment</code> ] [ <code>skbinfo</code> ] </p>
<p> <i>ADD-ENTRY</i> := { <i>ip</i> | <i>fromip</i>&#8211;<i>toip</i> | <i>ip</i>/<i>cidr</i> } </p>
<p> <i>ADD-OPTIONS</i> := [ <code>timeout</code> <i>value</i> ] [ <code>packets</code> <i>value</i> ] [ <code>bytes</code> <i>value</i> ] [ <code>comment</code> <i>string</i> ] [ <code>skbmark</code> <i>value</i> ] [ <code>skbprio</code> <i>value</i> ] [ <code>skbqueue</code> <i>value</i> ] </p>
<p> <i>DEL-ENTRY</i> := { <i>ip</i> | <i>fromip</i>&#8211;<i>toip</i> | <i>ip</i>/<i>cidr</i> } </p>
<p> <i>TEST-ENTRY</i> := <i>ip</i> </p>
<p> Mandatory <code>create</code> options:</p>
<dl>
<dt><code>range</code> <i>fromip</i>&#8211;<i>toip</i>|<i>ip</i>/<i>cidr</i></p>
<dd>Create the set from the specified inclusive address range expressed in an IPv4 address range or network. The size of the range (in entries) cannot exceed the limit of maximum 65536 elements.</dl>
<p> Optional <code>create</code> options:</p>
<dl>
<dt><code>netmask</code> <i>cidr</i></p>
<dd>When the optional <code>netmask</code> parameter specified, network addresses will be stored in the set instead of IP host addresses. The <i>cidr</i> prefix value must be between 1-32. An IP address will be in the set if the network address, which is resulted by masking the address with the specified netmask, can be found in the set.</dl>
<p> The <code>bitmap:ip</code> type supports adding or deleting multiple entries in one command. </p>
<p> Examples:</p>
<dl>
<dd>ipset create foo bitmap:ip range 192.168.0.0/16</p>
<dd>ipset add foo 192.168.1/24</p>
<dd>ipset test foo 192.168.1.1</dl>
<h3>bitmap:ip,mac</h3>
<p>The <code>bitmap:ip,mac</code> set type uses a memory range to store IPv4 and a MAC address pairs. A <code>bitmap:ip,mac</code> type of set can store up to 65536 entries. </p>
<p> <i>CREATE-OPTIONS</i> := <code>range</code> <i>fromip</i>&#8211;<i>toip</i>|<i>ip</i>/<i>cidr</i> [ <code>timeout</code> <i>value</i> ] [ <code>counters</code> ] [ <code>comment</code> ] [ <code>skbinfo</code> ] </p>
<p> <i>ADD-ENTRY</i> := <i>ip</i>[,<i>macaddr</i>] </p>
<p> <i>ADD-OPTIONS</i> := [ <code>timeout</code> <i>value</i> ] [ <code>packets</code> <i>value</i> ] [ <code>bytes</code> <i>value</i> ] [ <code>comment</code> <i>string</i> ] [ <code>skbmark</code> <i>value</i> ] [ <code>skbprio</code> <i>value</i> ] [ <code>skbqueue</code> <i>value</i> ] </p>
<p> <i>DEL-ENTRY</i> := <i>ip</i>[,<i>macaddr</i>] </p>
<p> <i>TEST-ENTRY</i> := <i>ip</i>[,<i>macaddr</i>] </p>
<p> Mandatory options to use when creating a <code>bitmap:ip,mac</code> type of set:</p>
<dl>
<dt><code>range</code> <i>fromip</i>&#8211;<i>toip</i>|<i>ip</i>/<i>cidr</i></p>
<dd>Create the set from the specified inclusive address range expressed in an IPv4 address range or network. The size of the range cannot exceed the limit of maximum 65536 entries.</dl>
<p> The <code>bitmap:ip,mac</code> type is exceptional in the sense that the MAC part can be left out when adding/deleting/testing entries in the set. If we add an entry without the MAC address specified, then when the first time the entry is matched by the kernel, it will automatically fill out the missing MAC address with the source MAC address from the packet. If the entry was specified with a timeout value, the timer starts off when the IP and MAC address pair is complete. </p>
<p> The <code>bitmap:ip,mac</code> type of sets require two <code>src/dst</code> parameters of the <code>set</code> match and <code>SET</code> target netfilter kernel modules and the second one must be <code>src</code> to match, add or delete entries, because the <code>set</code> match and <code>SET</code> target have access to the source MAC address only. </p>
<p> Examples:</p>
<dl>
<dd>ipset create foo bitmap:ip,mac range 192.168.0.0/16</p>
<dd>ipset add foo 192.168.1.1,12:34:56:78:9A:BC</p>
<dd>ipset test foo 192.168.1.1</dl>
<h3>bitmap:port</h3>
<p>The <code>bitmap:port</code> set type uses a memory range to store port numbers and such a set can store up to 65536 ports. </p>
<p> <i>CREATE-OPTIONS</i> := <code>range</code> <i>fromport</i>&#8211;<i>toport [ </i><code>timeout</code> <i>value</i> ] [ <code>counters</code> ] [ <code>comment</code> ] [ <code>skbinfo</code> ] </p>
<p> <i>ADD-ENTRY</i> := { <i>[proto:]port</i> | <i>[proto:]fromport</i>&#8211;<i>toport</i> } </p>
<p> <i>ADD-OPTIONS</i> := [ <code>timeout</code> <i>value</i> ] [ <code>packets</code> <i>value</i> ] [ <code>bytes</code> <i>value</i> ] [ <code>comment</code> <i>string</i> ] [ <code>skbmark</code> <i>value</i> ] [ <code>skbprio</code> <i>value</i> ] [ <code>skbqueue</code> <i>value</i> ] </p>
<p> <i>DEL-ENTRY</i> := { <i>[proto:]port</i> | <i>[proto:]fromport</i>&#8211;<i>toport</i> } </p>
<p> <i>TEST-ENTRY</i> := <i>[proto:]port</i> </p>
<p> Mandatory options to use when creating a <code>bitmap:port</code> type of set:</p>
<dl>
<dt><code>range</code> <i>[proto:]fromport</i>&#8211;<i>toport</i></p>
<dd>Create the set from the specified inclusive port range.</dl>
<p> The <code>set</code> match and <code>SET</code> target netfilter kernel modules interpret the stored numbers as TCP or UDP port numbers. </p>
<p> <code>proto</code> only needs to be specified if a service name is used, and that name does not exist as a TCP service. </p>
<p> Examples:</p>
<dl>
<dd>ipset create foo bitmap:port range 0-1024</p>
<dd>ipset add foo 80</p>
<dd>ipset test foo 80</p>
<dd>ipset del foo udp:[macon-udp]-[tn-tl-w2]</dl>
<h3>hash:ip</h3>
<p>The <code>hash:ip</code> set type uses a hash to store IP host addresses (default) or network addresses. Zero valued IP address cannot be stored in a <code>hash:ip</code> type of set. </p>
<p> <i>CREATE-OPTIONS</i> := [ <code>family</code> { <code>inet</code> | <code>inet6</code> } ] | [ <code>hashsize</code> <i>value</i> ] [ <code>maxelem</code> <i>value</i> ] [ <code>netmask</code> <i>cidr</i> ] [ <code>timeout</code> <i>value</i> ] [ <code>counters</code> ] [ <code>comment</code> ] [ <code>skbinfo</code> ] </p>
<p> <i>ADD-ENTRY</i> := <i>ipaddr</i> </p>
<p> <i>ADD-OPTIONS</i> := [ <code>timeout</code> <i>value</i> ] [ <code>packets</code> <i>value</i> ] [ <code>bytes</code> <i>value</i> ] [ <code>comment</code> <i>string</i> ] [ <code>skbmark</code> <i>value</i> ] [ <code>skbprio</code> <i>value</i> ] [ <code>skbqueue</code> <i>value</i> ] </p>
<p> <i>DEL-ENTRY</i> := <i>ipaddr</i> </p>
<p> <i>TEST-ENTRY</i> := <i>ipaddr</i> </p>
<p> Optional <code>create</code> options:</p>
<dl>
<dt><code>netmask</code> <i>cidr</i></p>
<dd>When the optional <code>netmask</code> parameter specified, network addresses will be stored in the set instead of IP host addresses. The <i>cidr</i> prefix value must be between 1-32 for IPv4 and between 1-128 for IPv6. An IP address will be in the set if the network address, which is resulted by masking the address with the netmask, can be found in the set. Examples:</p>
<dd>ipset create foo hash:ip netmask 30</p>
<dd>ipset add foo 192.168.1.0/24</p>
<dd>ipset test foo 192.168.1.2</dl>
<h3>hash:mac</h3>
<p>The <code>hash:mac</code> set type uses a hash to store MAC addresses. Zero valued MAC addresses cannot be stored in a <code>hash:mac</code> type of set. </p>
<p> <i>CREATE-OPTIONS</i> := [ <code>hashsize</code> <i>value</i> ] [ <code>maxelem</code> <i>value</i> ] [ <code>timeout</code> <i>value</i> ] [ <code>counters</code> ] [ <code>comment</code> ] [ <code>skbinfo</code> ] </p>
<p> <i>ADD-ENTRY</i> := <i>macaddr</i> </p>
<p> <i>ADD-OPTIONS</i> := [ <code>timeout</code> <i>value</i> ] [ <code>packets</code> <i>value</i> ] [ <code>bytes</code> <i>value</i> ] [ <code>comment</code> <i>string</i> ] [ <code>skbmark</code> <i>value</i> ] [ <code>skbprio</code> <i>value</i> ] [ <code>skbqueue</code> <i>value</i> ] </p>
<p> <i>DEL-ENTRY</i> := <i>macaddr</i> </p>
<p> <i>TEST-ENTRY</i> := <i>macaddr</i> </p>
<p> Examples:</p>
<dl>
<dd>ipset create foo hash:mac</p>
<dd>ipset add foo 01:02:03:04:05:06</p>
<dd>ipset test foo 01:02:03:04:05:06 </p>
</dl>
<h3>hash:net</h3>
<p>The <code>hash:net</code> set type uses a hash to store different sized IP network addresses. Network address with zero prefix size cannot be stored in this type of sets. </p>
<p> <i>CREATE-OPTIONS</i> := [ <code>family</code> { <code>inet</code> | <code>inet6</code> } ] | [ <code>hashsize</code> <i>value</i> ] [ <code>maxelem</code> <i>value</i> ] [ <code>timeout</code> <i>value</i> ] [ <code>counters</code> ] [ <code>comment</code> ] [ <code>skbinfo</code> ] </p>
<p> <i>ADD-ENTRY</i> := <i>netaddr</i> </p>
<p> <i>ADD-OPTIONS</i> := [ <code>timeout</code> <i>value</i> ] [ <code>nomatch</code> ] [ <code>packets</code> <i>value</i> ] [ <code>bytes</code> <i>value</i> ] [ <code>comment</code> <i>string</i> ] [ <code>skbmark</code> <i>value</i> ] [ <code>skbprio</code> <i>value</i> ] [ <code>skbqueue</code> <i>value</i> ] </p>
<p> <i>DEL-ENTRY</i> := <i>netaddr</i> </p>
<p> <i>TEST-ENTRY</i> := <i>netaddr</i> </p>
<p> where <i>netaddr</i> := <i>ip</i>[/<i>cidr</i>] </p>
<p> When adding/deleting/testing entries, if the cidr prefix parameter is not specified, then the host prefix value is assumed. When adding/deleting entries, the exact element is added/deleted and overlapping elements are not checked by the kernel. When testing entries, if a host address is tested, then the kernel tries to match the host address in the networks added to the set and reports the result accordingly. </p>
<p> From the <code>set</code> netfilter match point of view the searching for a match always starts from the smallest size of netblock (most specific prefix) to the largest one (least specific prefix) added to the set. When adding/deleting IP addresses to the set by the <code>SET</code> netfilter target, it will be added/deleted by the most specific prefix which can be found in the set, or by the host prefix value if the set is empty. </p>
<p> The lookup time grows linearly with the number of the different prefix values added to the set. </p>
<p> Example:</p>
<dl>
<dd>ipset create foo hash:net</p>
<dd>ipset add foo 192.168.0.0/24</p>
<dd>ipset add foo 10.1.0.0/16</p>
<dd>ipset add foo 192.168.0/24</p>
<dd>ipset add foo 192.168.0/30 nomatch</dl>
<p> When matching the elements in the set above, all IP addresses will match from the networks 192.168.0.0/24, 10.1.0.0/16 and 192.168.0/24 except the ones from 192.168.0/30.</p>
<h3>hash:net,net</h3>
<p>The <code>hash:net,net</code> set type uses a hash to store pairs of different sized IP network addresses. Bear in mind that the first parameter has precedence over the second, so a nomatch entry could be potentially be ineffective if a more specific first parameter existed with a suitable second parameter. Network address with zero prefix size cannot be stored in this type of set. </p>
<p> <i>CREATE-OPTIONS</i> := [ <code>family</code> { <code>inet</code> | <code>inet6</code> } ] | [ <code>hashsize</code> <i>value</i> ] [ <code>maxelem</code> <i>value</i> ] [ <code>timeout</code> <i>value</i> ] [ <code>counters</code> ] [ <code>comment</code> ] [ <code>skbinfo</code> ] </p>
<p> <i>ADD-ENTRY</i> := <i>netaddr</i>,<i>netaddr</i> </p>
<p> <i>ADD-OPTIONS</i> := [ <code>timeout</code> <i>value</i> ] [ <code>nomatch</code> ] [ <code>packets</code> <i>value</i> ] [ <code>bytes</code> <i>value</i> ] [ <code>comment</code> <i>string</i> ] [ <code>skbmark</code> <i>value</i> ] [ <code>skbprio</code> <i>value</i> ] [ <code>skbqueue</code> <i>value</i> ] </p>
<p> <i>DEL-ENTRY</i> := <i>netaddr</i>,<i>netaddr</i> </p>
<p> <i>TEST-ENTRY</i> := <i>netaddr</i>,<i>netaddr</i> </p>
<p> where <i>netaddr</i> := <i>ip</i>[/<i>cidr</i>] </p>
<p> When adding/deleting/testing entries, if the cidr prefix parameter is not specified, then the host prefix value is assumed. When adding/deleting entries, the exact element is added/deleted and overlapping elements are not checked by the kernel. When testing entries, if a host address is tested, then the kernel tries to match the host address in the networks added to the set and reports the result accordingly. </p>
<p> From the <code>set</code> netfilter match point of view the searching for a match always starts from the smallest size of netblock (most specific prefix) to the largest one (least specific prefix) with the first param having precedence. When adding/deleting IP addresses to the set by the <code>SET</code> netfilter target, it will be added/deleted by the most specific prefix which can be found in the set, or by the host prefix value if the set is empty. </p>
<p> The lookup time grows linearly with the number of the different prefix values added to the first parameter of the set. The number of secondary prefixes further increases this as the list of secondary prefixes is traversed per primary prefix. </p>
<p> Example:</p>
<dl>
<dd>ipset create foo hash:net,net</p>
<dd>ipset add foo 192.168.0.0/24,10.0.1.0/24</p>
<dd>ipset add foo 10.1.0.0/16,10.255.0.0/24</p>
<dd>ipset add foo 192.168.0/24,192.168.54.0-192.168.54.255</p>
<dd>ipset add foo 192.168.0/30,192.168.64/30 nomatch</dl>
<p> When matching the elements in the set above, all IP addresses will match from the networks 192.168.0.0/24&lt;-&gt;10.0.1.0/24, 10.1.0.0/16&lt;-&gt;10.255.0.0/24 and 192.168.0/24&lt;-&gt;192.168.54.0/24 except the ones from 192.168.0/30&lt;-&gt;192.168.64/30.</p>
<h3>hash:ip,port</h3>
<p>The <code>hash:ip,port</code> set type uses a hash to store IP address and port number pairs. The port number is interpreted together with a protocol (default TCP) and zero protocol number cannot be used. </p>
<p> <i>CREATE-OPTIONS</i> := [ <code>family</code> { <code>inet</code> | <code>inet6</code> } ] | [ <code>hashsize</code> <i>value</i> ] [ <code>maxelem</code> <i>value</i> ] [ <code>timeout</code> <i>value</i> ] [ <code>counters</code> ] [ <code>comment</code> ] [ <code>skbinfo</code> ] </p>
<p> <i>ADD-ENTRY</i> := <i>ipaddr</i>,[<i>proto</i>:]<i>port</i> </p>
<p> <i>ADD-OPTIONS</i> := [ <code>timeout</code> <i>value</i> ] [ <code>packets</code> <i>value</i> ] [ <code>bytes</code> <i>value</i> ] [ <code>comment</code> <i>string</i> ] [ <code>skbmark</code> <i>value</i> ] [ <code>skbprio</code> <i>value</i> ] [ <code>skbqueue</code> <i>value</i> ] </p>
<p> <i>DEL-ENTRY</i> := <i>ipaddr</i>,[<i>proto</i>:]<i>port</i> </p>
<p> <i>TEST-ENTRY</i> := <i>ipaddr</i>,[<i>proto</i>:]<i>port</i> </p>
<p> The [<i>proto</i>:]<i>port</i> part of the elements may be expressed in the following forms, where the range variations are valid when adding or deleting entries:</p>
<dl>
<dt><i>portname[-portname]</i></p>
<dd>TCP port or range of ports expressed in TCP portname identifiers from /etc/services</p>
<dt><i>portnumber[-portnumber]</i></p>
<dd>TCP port or range of ports expressed in TCP port numbers</p>
<dt><code>tcp</code>|<code>sctp</code>|<code>udp</code>|<code>udplite</code>:<i>portname</i>|<i>portnumber</i>[-<i>portname</i>|<i>portnumber</i>]</p>
<dd>TCP, SCTP, UDP or UDPLITE port or port range expressed in port name(s) or port number(s)</p>
<dt><code>icmp</code>:<i>codename</i>|<i>type</i>/<i>code</i></p>
<dd>ICMP codename or type/code. The supported ICMP codename identifiers can always be listed by the help command.</p>
<dt><code>icmpv6</code>:<i>codename</i>|<i>type</i>/<i>code</i></p>
<dd>ICMPv6 codename or type/code. The supported ICMPv6 codename identifiers can always be listed by the help command.</p>
<dt><i>proto</i>:0</p>
<dd>All other protocols, as an identifier from /etc/protocols or number. The pseudo port number must be zero.</dl>
<p> The <code>hash:ip,port</code> type of sets require two <code>src</code>/<code>dst</code> parameters of the <code>set</code> match and <code>SET</code> target kernel modules. </p>
<p> Examples:</p>
<dl>
<dd>ipset create foo hash:ip,port</p>
<dd>ipset add foo 192.168.1.0/24,80-82</p>
<dd>ipset add foo 192.168.1.1,udp:53</p>
<dd>ipset add foo 192.168.1.1,vrrp:0</p>
<dd>ipset test foo 192.168.1.1,80</dl>
<h3>hash:net,port</h3>
<p>The <code>hash:net,port</code> set type uses a hash to store different sized IP network address and port pairs. The port number is interpreted together with a protocol (default TCP) and zero protocol number cannot be used. Network address with zero prefix size is not accepted either. </p>
<p> <i>CREATE-OPTIONS</i> := [ <code>family</code> { <code>inet</code> | <code>inet6</code> } ] | [ <code>hashsize</code> <i>value</i> ] [ <code>maxelem</code> <i>value</i> ] [ <code>timeout</code> <i>value</i> ] [ <code>counters</code> ] [ <code>comment</code> ] [ <code>skbinfo</code> ] </p>
<p> <i>ADD-ENTRY</i> := <i>netaddr</i>,[<i>proto</i>:]<i>port</i> </p>
<p> <i>ADD-OPTIONS</i> := [ <code>timeout</code> <i>value</i> ] [ <code>nomatch</code> ] [ <code>packets</code> <i>value</i> ] [ <code>bytes</code> <i>value</i> ] [ <code>comment</code> <i>string</i> ] [ <code>skbmark</code> <i>value</i> ] [ <code>skbprio</code> <i>value</i> ] [ <code>skbqueue</code> <i>value</i> ] </p>
<p> <i>DEL-ENTRY</i> := <i>netaddr</i>,[<i>proto</i>:]<i>port</i> </p>
<p> <i>TEST-ENTRY</i> := <i>netaddr</i>,[<i>proto</i>:]<i>port</i> </p>
<p> where <i>netaddr</i> := <i>ip</i>[/<i>cidr</i>] </p>
<p> For the <i>netaddr</i> part of the elements see the description at the <code>hash:net</code> set type. For the [<i>proto</i>:]<i>port</i> part of the elements see the description at the <code>hash:ip,port</code> set type. </p>
<p> When adding/deleting/testing entries, if the cidr prefix parameter is not specified, then the host prefix value is assumed. When adding/deleting entries, the exact element is added/deleted and overlapping elements are not checked by the kernel. When testing entries, if a host address is tested, then the kernel tries to match the host address in the networks added to the set and reports the result accordingly. </p>
<p> From the <code>set</code> netfilter match point of view the searching for a match always starts from the smallest size of netblock (most specific prefix) to the largest one (least specific prefix) added to the set. When adding/deleting IP addresses to the set by the <code>SET</code> netfilter target, it will be added/deleted by the most specific prefix which can be found in the set, or by the host prefix value if the set is empty. </p>
<p> The lookup time grows linearly with the number of the different prefix values added to the set. </p>
<p> Examples:</p>
<dl>
<dd>ipset create foo hash:net,port</p>
<dd>ipset add foo 192.168.0/24,25</p>
<dd>ipset add foo 10.1.0.0/16,80</p>
<dd>ipset test foo 192.168.0/24,25</dl>
<h3>hash:ip,port,ip</h3>
<p>The <code>hash:ip,port,ip</code> set type uses a hash to store IP address, port number and a second IP address triples. The port number is interpreted together with a protocol (default TCP) and zero protocol number cannot be used. </p>
<p> <i>CREATE-OPTIONS</i> := [ <code>family</code> { <code>inet</code> | <code>inet6</code> } ] | [ <code>hashsize</code> <i>value</i> ] [ <code>maxelem</code> <i>value</i> ] [ <code>timeout</code> <i>value</i> ] [ <code>counters</code> ] [ <code>comment</code> ] [ <code>skbinfo</code> ] </p>
<p> <i>ADD-ENTRY</i> := <i>ipaddr</i>,[<i>proto</i>:]<i>port</i>,<i>ip</i> </p>
<p> <i>ADD-OPTIONS</i> := [ <code>timeout</code> <i>value</i> ] [ <code>packets</code> <i>value</i> ] [ <code>bytes</code> <i>value</i> ] [ <code>comment</code> <i>string</i> ] [ <code>skbmark</code> <i>value</i> ] [ <code>skbprio</code> <i>value</i> ] [ <code>skbqueue</code> <i>value</i> ] </p>
<p> <i>DEL-ENTRY</i> := <i>ipaddr</i>,[<i>proto</i>:]<i>port</i>,<i>ip</i> </p>
<p> <i>TEST-ENTRY</i> := <i>ipaddr</i>,[<i>proto</i>:]<i>port</i>,<i>ip</i> </p>
<p> For the first <i>ipaddr</i> and [<i>proto</i>:]<i>port</i> parts of the elements see the descriptions at the <code>hash:ip,port</code> set type. </p>
<p> The <code>hash:ip,port,ip</code> type of sets require three <code>src</code>/<code>dst</code> parameters of the <code>set</code> match and <code>SET</code> target kernel modules. </p>
<p> Examples:</p>
<dl>
<dd>ipset create foo hash:ip,port,ip</p>
<dd>ipset add foo 192.168.1.1,80,10.0.0.1</p>
<dd>ipset test foo 192.168.1.1,udp:53,10.0.0.1</dl>
<h3>hash:ip,port,net</h3>
<p>The <code>hash:ip,port,net</code> set type uses a hash to store IP address, port number and IP network address triples. The port number is interpreted together with a protocol (default TCP) and zero protocol number cannot be used. Network address with zero prefix size cannot be stored either. </p>
<p> <i>CREATE-OPTIONS</i> := [ <code>family</code> { <code>inet</code> | <code>inet6</code> } ] | [ <code>hashsize</code> <i>value</i> ] [ <code>maxelem</code> <i>value</i> ] [ <code>timeout</code> <i>value</i> ] [ <code>counters</code> ] [ <code>comment</code> ] [ <code>skbinfo</code> ] </p>
<p> <i>ADD-ENTRY</i> := <i>ipaddr</i>,[<i>proto</i>:]<i>port</i>,<i>netaddr</i> </p>
<p> <i>ADD-OPTIONS</i> := [ <code>timeout</code> <i>value</i> ] [ <code>nomatch</code> ] [ <code>packets</code> <i>value</i> ] [ <code>bytes</code> <i>value</i> ] [ <code>comment</code> <i>string</i> ] [ <code>skbmark</code> <i>value</i> ] [ <code>skbprio</code> <i>value</i> ] [ <code>skbqueue</code> <i>value</i> ] </p>
<p> <i>DEL-ENTRY</i> := <i>ipaddr</i>,[<i>proto</i>:]<i>port</i>,<i>netaddr</i> </p>
<p> <i>TEST-ENTRY</i> := <i>ipaddr</i>,[<i>proto</i>:]<i>port</i>,<i>netaddr</i> </p>
<p> where <i>netaddr</i> := <i>ip</i>[/<i>cidr</i>] </p>
<p> For the <i>ipaddr</i> and [<i>proto</i>:]<i>port</i> parts of the elements see the descriptions at the <code>hash:ip,port</code> set type. For the <i>netaddr</i> part of the elements see the description at the <code>hash:net</code> set type. </p>
<p> From the <code>set</code> netfilter match point of view the searching for a match always starts from the smallest size of netblock (most specific cidr) to the largest one (least specific cidr) added to the set. When adding/deleting triples to the set by the <code>SET</code> netfilter target, it will be added/deleted by the most specific cidr which can be found in the set, or by the host cidr value if the set is empty. </p>
<p> The lookup time grows linearly with the number of the different <i>cidr</i> values added to the set. </p>
<p> The <code>hash:ip,port,net</code> type of sets require three <code>src</code>/<code>dst</code> parameters of the <code>set</code> match and <code>SET</code> target kernel modules. </p>
<p> Examples:</p>
<dl>
<dd>ipset create foo hash:ip,port,net</p>
<dd>ipset add foo 192.168.1,80,10.0.0/24</p>
<dd>ipset add foo 192.168.2,25,10.1.0.0/16</p>
<dd>ipset test foo 192.168.1,80.10.0.0/24</dl>
<h3>hash:ip,mark</h3>
<p>The <code>hash:ip,mark</code> set type uses a hash to store IP address and packet mark pairs. </p>
<p> <i>CREATE-OPTIONS</i> := [ <code>family</code> { <code>inet</code> | <code>inet6</code> } ] | [ <code>markmask</code> <i>value</i> ] [ <code>hashsize</code> <i>value</i> ] [ <code>maxelem</code> <i>value</i> ] [ <code>timeout</code> <i>value</i> ] [ <code>counters</code> ] [ <code>comment</code> ] [ <code>skbinfo</code> ] </p>
<p> <i>ADD-ENTRY</i> := <i>ipaddr</i>,<i>mark</i> </p>
<p> <i>ADD-OPTIONS</i> := [ <code>timeout</code> <i>value</i> ] [ <code>packets</code> <i>value</i> ] [ <code>bytes</code> <i>value</i> ] [ <code>comment</code> <i>string</i> ] [ <code>skbmark</code> <i>value</i> ] [ <code>skbprio</code> <i>value</i> ] [ <code>skbqueue</code> <i>value</i> ] </p>
<p> <i>DEL-ENTRY</i> := <i>ipaddr</i>,<i>mark</i> </p>
<p> <i>TEST-ENTRY</i> := <i>ipaddr</i>,<i>mark</i> </p>
<p> Optional <code>create</code> options:</p>
<dl>
<dt><code>markmask</code> <i>value</i></p>
<dd>Allows you to set bits you are interested in the packet mark. This values is then used to perform bitwise AND operation for every mark added. markmask can be any value between 1 and 4294967295, by default all 32 bits are set.</dl>
<p> The <i>mark</i> can be any value between 0 and 4294967295. </p>
<p> The <code>hash:ip,mark</code> type of sets require two <code>src</code>/<code>dst</code> parameters of the <code>set</code> match and <code>SET</code> target kernel modules. </p>
<p> Examples:</p>
<dl>
<dd>ipset create foo hash:ip,mark</p>
<dd>ipset add foo 192.168.1.0/24,555</p>
<dd>ipset add foo 192.168.1.1,0&#215;63</p>
<dd>ipset add foo 192.168.1.1,111236</dl>
<h3>hash:net,port,net</h3>
<p>The <code>hash:net,port,net</code> set type behaves similarly to hash:ip,port,net but accepts a cidr value for both the first and last parameter. Either subnet is permitted to be a /0 should you wish to match port between all destinations. </p>
<p> <i>CREATE-OPTIONS</i> := [ <code>family</code> { <code>inet</code> | <code>inet6</code> } ] | [ <code>hashsize</code> <i>value</i> ] [ <code>maxelem</code> <i>value</i> ] [ <code>timeout</code> <i>value</i> ] [ <code>counters</code> ] [ <code>comment</code> ] [ <code>skbinfo</code> ] </p>
<p> <i>ADD-ENTRY</i> := <i>netaddr</i>,[<i>proto</i>:]<i>port</i>,<i>netaddr</i> </p>
<p> <i>ADD-OPTIONS</i> := [ <code>timeout</code> <i>value</i> ] [ <code>nomatch</code> ] [ <code>packets</code> <i>value</i> ] [ <code>bytes</code> <i>value</i> ] [ <code>comment</code> <i>string</i> ] [ <code>skbmark</code> <i>value</i> ] [ <code>skbprio</code> <i>value</i> ] [ <code>skbqueue</code> <i>value</i> ] </p>
<p> <i>DEL-ENTRY</i> := <i>netaddr</i>,[<i>proto</i>:]<i>port</i>,<i>netaddr</i> </p>
<p> <i>TEST-ENTRY</i> := <i>netaddr</i>,[<i>proto</i>:]<i>port</i>,<i>netaddr</i> </p>
<p> where <i>netaddr</i> := <i>ip</i>[/<i>cidr</i>] </p>
<p> For the [<i>proto</i>:]<i>port</i> part of the elements see the description at the <code>hash:ip,port</code> set type. For the <i>netaddr</i> part of the elements see the description at the <code>hash:net</code> set type. </p>
<p> From the <code>set</code> netfilter match point of view the searching for a match always starts from the smallest size of netblock (most specific cidr) to the largest one (least specific cidr) added to the set. When adding/deleting triples to the set by the <code>SET</code> netfilter target, it will be added/deleted by the most specific cidr which can be found in the set, or by the host cidr value if the set is empty. The first subnet has precedence when performing the most-specific lookup, just as for hash:net,net </p>
<p> The lookup time grows linearly with the number of the different <i>cidr</i> values added to the set and by the number of secondary <i>cidr</i> values per primary. </p>
<p> The <code>hash:net,port,net</code> type of sets require three <code>src</code>/<code>dst</code> parameters of the <code>set</code> match and <code>SET</code> target kernel modules. </p>
<p> Examples:</p>
<dl>
<dd>ipset create foo hash:net,port,net</p>
<dd>ipset add foo 192.168.1.0/24,0,10.0.0/24</p>
<dd>ipset add foo 192.168.2.0/24,25,10.1.0.0/16</p>
<dd>ipset test foo 192.168.1.1,80,10.0.0.1</dl>
<h3>hash:net,iface</h3>
<p>The <code>hash:net,iface</code> set type uses a hash to store different sized IP network address and interface name pairs. </p>
<p> <i>CREATE-OPTIONS</i> := [ <code>family</code> { <code>inet</code> | <code>inet6</code> } ] | [ <code>hashsize</code> <i>value</i> ] [ <code>maxelem</code> <i>value</i> ] [ <code>timeout</code> <i>value</i> ] [ <code>counters</code> ] [ <code>comment</code> ] [ <code>skbinfo</code> ] </p>
<p> <i>ADD-ENTRY</i> := <i>netaddr</i>,[<code>physdev</code>:]<i>iface</i> </p>
<p> <i>ADD-OPTIONS</i> := [ <code>timeout</code> <i>value</i> ] [ <code>nomatch</code> ] [ <code>packets</code> <i>value</i> ] [ <code>bytes</code> <i>value</i> ] [ <code>comment</code> <i>string</i> ] [ <code>skbmark</code> <i>value</i> ] [ <code>skbprio</code> <i>value</i> ] [ <code>skbqueue</code> <i>value</i> ] </p>
<p> <i>DEL-ENTRY</i> := <i>netaddr</i>,[<code>physdev</code>:]<i>iface</i> </p>
<p> <i>TEST-ENTRY</i> := <i>netaddr</i>,[<code>physdev</code>:]<i>iface</i> </p>
<p> where <i>netaddr</i> := <i>ip</i>[/<i>cidr</i>] </p>
<p> For the <i>netaddr</i> part of the elements see the description at the <code>hash:net</code> set type. </p>
<p> When adding/deleting/testing entries, if the cidr prefix parameter is not specified, then the host prefix value is assumed. When adding/deleting entries, the exact element is added/deleted and overlapping elements are not checked by the kernel. When testing entries, if a host address is tested, then the kernel tries to match the host address in the networks added to the set and reports the result accordingly. </p>
<p> From the <code>set</code> netfilter match point of view the searching for a match always starts from the smallest size of netblock (most specific prefix) to the largest one (least specific prefix) added to the set. When adding/deleting IP addresses to the set by the <code>SET</code> netfilter target, it will be added/deleted by the most specific prefix which can be found in the set, or by the host prefix value if the set is empty. </p>
<p> The second direction parameter of the <code>set</code> match and <code>SET</code> target modules corresponds to the incoming/outgoing interface: <code>src</code> to the incoming one (similar to the <code>-i</code> flag of iptables), while <code>dst</code> to the outgoing one (similar to the <code>-o</code> flag of iptables). When the interface is flagged with <code>physdev:</code>, the interface is interpreted as the incoming/outgoing bridge port. </p>
<p> The lookup time grows linearly with the number of the different prefix values added to the set. </p>
<p> The internal restriction of the <code>hash:net,iface</code> set type is that the same network prefix cannot be stored with more than 64 different interfaces in a single set. </p>
<p> Examples:</p>
<dl>
<dd>ipset create foo hash:net,iface</p>
<dd>ipset add foo 192.168.0/24,eth0</p>
<dd>ipset add foo 10.1.0.0/16,eth1</p>
<dd>ipset test foo 192.168.0/24,eth0</dl>
<h3>list:set</h3>
<p>The <code>list:set</code> type uses a simple list in which you can store set names. </p>
<p> <i>CREATE-OPTIONS</i> := [ <code>size</code> <i>value</i> ] [ <code>timeout</code> <i>value</i> ] [ <code>counters</code> ] [ <code>comment</code> ] [ <code>skbinfo</code> ] </p>
<p> <i>ADD-ENTRY</i> := <i>setname</i> [ { <code>before</code> | <code>after</code> } <i>setname</i> ] </p>
<p> <i>ADD-OPTIONS</i> := [ <code>timeout</code> <i>value</i> ] [ <code>packets</code> <i>value</i> ] [ <code>bytes</code> <i>value</i> ] [ <code>comment</code> <i>string</i> ] [ <code>skbmark</code> <i>value</i> ] [ <code>skbprio</code> <i>value</i> ] [ <code>skbqueue</code> <i>value</i> ] </p>
<p> <i>DEL-ENTRY</i> := <i>setname</i> [ { <code>before</code> | <code>after</code> } <i>setname</i> ] </p>
<p> <i>TEST-ENTRY</i> := <i>setname</i> [ { <code>before</code> | <code>after</code> } <i>setname</i> ] </p>
<p> Optional <code>create</code> options:</p>
<dl>
<dt><code>size</code> <i>value</i></p>
<dd>The size of the list, the default is 8.</dl>
<p> By the <code>ipset</code> command you can add, delete and test set names in a <code>list:set</code> type of set. </p>
<p> By the <code>set</code> match or <code>SET</code> target of netfilter you can test, add or delete entries in the sets added to the <code>list:set</code> type of set. The match will try to find a matching entry in the sets and the target will try to add an entry to the first set to which it can be added. The number of direction options of the match and target are important: sets which require more parameters than specified are skipped, while sets with equal or less parameters are checked, elements added/deleted. For example if <i>a</i> and <i>b</i> are <code>list:set</code> type of sets then in the command</p>
<dl>
<dd>iptables -m set &#8211;match-set a src,dst -j SET &#8211;add-set b src,dst</dl>
<p> the match and target will skip any set in <i>a</i> and <i>b</i> which stores data triples, but will match all sets with single or double data storage in <i>a</i> set and stop matching at the first successful set, and add src to the first single or src,dst to the first double data storage set in <i>b</i> to which the entry can be added. You can imagine a <code>list:set</code> type of set as an ordered union of the set elements. </p>
<p> Please note: by the <code>ipset</code> command you can add, delete and <code>test</code> the setnames in a <code>list:set</code> type of set, and <code>not</code> the presence of a set&#8217;s member (such as an IP address).</p>
<h2>General Restrictions</h2>
<p>Zero valued set entries cannot be used with hash methods. Zero protocol value with ports cannot be used.</p>
<h2>Comments</h2>
<p>If you want to store same size subnets from a given network (say /24 blocks from a /8 network), use the <code>bitmap:ip</code> set type. If you want to store random same size networks (say random /24 blocks), use the <code>hash:ip</code> set type. If you have got random size of netblocks, use <code>hash:net</code>. </p>
<p> Backward compatibility is maintained and old <code>ipset</code> syntax is still supported. </p>
<p> The <code>iptree</code> and <code>iptreemap</code> set types are removed: if you refer to them, they are automatically replaced by <code>hash:ip</code> type of sets.</p>
<h2>Diagnostics</h2>
<p>Various error messages are printed to standard error. The exit code is 0 for correct functioning.</p>
<h2>Bugs</h2>
<p>Bugs? No, just funny features. :-) OK, just kidding&#8230;</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-iptables/">iptables</a></code>(8), <code><a href="/docs/linux/man/8-ip6tables/">ip6tables</a></code>(8) <code><a href="/docs/linux/man/8-iptables-extensions/">iptables-extensions</a></code>(8)</p>
<h2>Authors</h2>
<p>Jozsef Kadlecsik wrote ipset, which is based on ippool by Joakim Axelsson, Patrick Schaaf and Martin Josefsson.<br />
 Sven Wegener wrote the iptreemap type.</p>
<h2>Last Remark</h2>
<p><code>I stand on the shoulders of giants.</code></p>
