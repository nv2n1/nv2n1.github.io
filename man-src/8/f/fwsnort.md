---
title: "fwsnort(8)"
name: "fwsnort"
section: "8"
letter: "f"
url: "/docs/linux/man/8-fwsnort/"
description: "fwsnort – Firewall Snort"
---

<p><code>fwsnort</code> &#8211; Firewall Snort</p>
<h2>Synopsis</h2>
<p><code>fwsnort [options]</code></p>
<h2>Description</h2>
<p><code>fwsnort</code> translates Snort rules into iptables rules and generates a shell script that implements the resulting iptables commands. This ruleset allows network traffic that matches Snort signatures (i.e. attacks and other suspicious network behavior) to be logged and/or dropped by iptables directly without putting an interface into promiscuous mode or queuing packets from kernel to user space. Note that fwsnort can also build an iptables policy that combines the string match extension with the NFQUEUE or QUEUE targets to allow the kernel to perform preliminary string matches that are defined within Snort rules before queuing matching packets to userspace. Because the bulk of network communications are not malicious, this should provide a speedup for snort_inline since the majority of packets do not then have to be copied from kernel memory into user memory and subsequently inspected by snort_inline. There is a tradeoff here in terms of signature detection however because snort_inline when deployed in this way does not have the opportunity to see all packets associated with a session, so stream reassembly and signature comparisons against a reassembled buffer do not take place (the stream preprocessor &#8211; stream4, stream5, etc. &#8211; should be disabled). </p>
<p> <code>fwsnort</code> (optionally) uses the IPTables::Parse module to parse the iptables ruleset on the machine to determine which Snort rules are applicable to the specific iptables policy. After all, if iptables is blocking all inbound http traffic from external addresses, it is probably not of much use to try detecting inbound attacks against against tcp/80. By default fwsnort generates iptables rules that log Snort sid&#8217;s within a &#8211;log-prefix to syslog where the messages can be analyzed with a log analyzer such as <code>psad</code> (see <a rel="nofollow" href="http://www.cipherdyne.org/psad/">http://www.cipherdyne.org/psad/</a>). <code>fwsnort</code> relies on the iptables string match module to match Snort content fields in the application portion of ip traffic. Since Snort rules can contain hex data in content fields (specified between pipe &quot;|&quot; characters), fwsnort implements a patch against iptables (which has been accepted by the Netfilter project as of iptables-1.2.7a) which adds a &quot;&#8211;hex-string&quot; option. This allow iptables to accept content fields from Snort rules such as &quot;|0d0a5b52504c5d3030320d0a|&quot; without any modification. <code>fwsnort</code> is able to translate approximately 60% of all rules from the Snort-2.3.3 IDS into equivalent iptables rules. For more information about the translation strategy as well as advantages/disadvantages of the method used by fwsnort to obtain intrusion detection data, see the README included with the fwsnort sources or browse to: <a rel="nofollow" href="http://www.cipherdyne.org/fwsnort/">http://www.cipherdyne.org/fwsnort/</a></p>
<h2>Options</h2>
<dl>
<dt><code>-c</code>, <code>&#8211;config&nbsp;<wbr>&lt;configuration file&gt;</code></p>
<dd>By default fwsnort makes use of the configuration file <code>/etc/fwsnort/fwsnort.conf</code> for almost all configuration parameters. fwsnort can be made to override this path by specifying a different file on the command line with the &#8211;config option.</p>
<dt><code>&#8211;update-rules</code></p>
<dd>Download the latest Emerging Threats rules from <a rel="nofollow" href="http://www.emergingthreats.net">http://www.emergingthreats.net</a> This will overwrite the emerging-all.rules file in the /etc/fwsnort/snort_rules/ directory. Note that the automatic downloading of Snort rules from <a rel="nofollow" href="http://www.snort.org/">http://www.snort.org/</a> as of March, 2005 is only offered as a pay service.</p>
<dt><code>&#8211;include-type&nbsp;<wbr>&nbsp;<wbr>&lt;rules type&gt;</code></p>
<dd>Restrict to processing snort rules of &lt;rules type&gt;. Example rule types would include &quot;ddos&quot;, &quot;backdoor&quot;, and &quot;web-attacks&quot;. This option also supports a comma-separated list of types, e.g. &quot;ddos,backdoor&quot;.</p>
<dt><code>&#8211;exclude-type&nbsp;<wbr>&nbsp;<wbr>&lt;rules type&gt;</code></p>
<dd>Exclude all Snort rules from of type &lt;rules type&gt; from the translation process. For example, if you don&#8217;t want any rules from the file emerging-all.rules to be translated, then use &quot;emerging-all&quot; as the argument to this option. A comma-separated list of types to exclude can be specified.</p>
<dt><code>&#8211;include-regex&nbsp;<wbr>&nbsp;<wbr>&lt;regex&gt;</code></p>
<dd>Only translate Snort rules that match the specified regular expression. This is useful to build <code>fwsnort</code> policies for Snort rules that have a common characteristic (such as a string match on the word &quot;Storm&quot; for the Storm worm for example).</p>
<dt><code>&#8211;exclude-regex&nbsp;<wbr>&nbsp;<wbr>&lt;regex&gt;</code></p>
<dd>Translate all Snort rules except those that match the specified regular expression. This is useful to omit Snort rules from <code>fwsnort</code> policies that have a common characteristic (such as a string match on &quot;HTTP_PORTS&quot; for example).</p>
<dt><code>&#8211;include-re-caseless</code></p>
<dd>Make the rule matchine regular expression specified with <i>&#8211;include-regex</i> match case insensitively.</p>
<dt><code>&#8211;exclude-re-caseless</code></p>
<dd>Make the rule matchine regular expression specified with <i>&#8211;exclude-regex</i> match case insensitively.</p>
<dt><code>&#8211;snort-rdir&nbsp;<wbr>&lt;snort-rules-directory&gt;</code></p>
<dd>Manually specify the directory where the snort rules files are located. The default is <code>/etc/fwsnort/snort_rules.</code> Multiple directories are supported as a comma-separated list.</p>
<dt><code>&#8211;snort-rfile&nbsp;<wbr>&lt;snort-rules-file&gt;</code></p>
<dd>Manually specify a Snort rules file to translated into iptables rules. Multiple files are also supported as a comma-separated list.</p>
<dt><code>&#8211;snort-sid&nbsp;<wbr>&lt;sid&gt;</code></p>
<dd>Generate an iptables ruleset for a single snort rule specified by &lt;sid&gt;. A comma-separated list of sids can be specified, e.g. &quot;2001842,1834&quot;.</p>
<dt><code>&#8211;exclude-sid&nbsp;<wbr>&lt;sid&gt;</code></p>
<dd>Provide a list of Snort ID&#8217;s to be excluded from the translation process.</p>
<dt><code>&#8211;ipt-script&nbsp;<wbr>&lt;script file&gt;</code></p>
<dd>Specify the path to the iptables script generated by fwsnort. The default location is /etc/fwsnort/fwsnort.sh.</p>
<dt><code>&#8211;NFQUEUE</code></p>
<dd>Build an <code>fwsnort</code> policy that sends packets that match Snort <code>content</code> or <code>uricontent</code> fields to userspace via the iptables NFQUEUE target for further analysis. This is a mechanism for reducing the signature inspection load placed on snort_inline. A parallel set of Snort rules that are successfully translated are placed in the /etc/fwsnort/snort_rules_queue directory. This requires CONFIG_NETFILTER_XT_TARGET_NFQUEUE support in the Linux kernel.</p>
<dt><code>&#8211;QUEUE</code></p>
<dd>Same as the <code>&#8211;NFQUEUE</code> command line argument except that the older QUEUE target is used instead of the NFQUEUE target. This requires CONFIG_IP_NF_QUEUE support in the Linux kernel.</p>
<dt><code>&#8211;queue-num&nbsp;<wbr>&lt;num&gt;</code></p>
<dd>Specify a queue number in &#8211;NFQUEUE mode.</p>
<dt><code>&#8211;ipt-apply</code></p>
<dd>Execute the iptables script generated by fwsnort.</p>
<dt><code>&#8211;ipt-flush</code></p>
<dd>Flush all <code>fwsnort</code> currently active iptables rules (flushes the fwsnort chains).</p>
<dt><code>&#8211;ipt-list</code></p>
<dd>List all <code>fwsnort</code> currently active iptables rules (lists the fwsnort chains).</p>
<dt><code>&#8211;ipt-drop</code></p>
<dd>For each logging rule generated by <code>fwsnort</code> add a corresponding DROP rule. Note that for TCP sessions using this option will cause retransmissions as packets that are part of established sessions selectively dropped. Remember that false positives are common occurrences for intrusion detection systems, and so using this or the &#8211;ipt-reject option may break things on your network! You have been warned.</p>
<dt><code>&#8211;ipt-reject</code></p>
<dd>For each logging rule generated by <code>fwsnort</code> add a corresponding REJECT rule. Reset packets will be generated for TCP sessions through the use of the &quot;&#8211;reject-with tcp-reset&quot; option, and ICMP port unreachable messages will be generated for UDP packets through the use of the &quot;&#8211;reject-with icmp-port-unreachable&quot; option.</p>
<dt><code>&#8211;no-ipt-log</code></p>
<dd>By default fwsnort generates an iptables script that implements a logging rule for each successfully translated snort rule. This can be disabled with the &#8211;no-ipt-log option, but &#8211;ipt-drop must also be specified.</p>
<dt><code>&#8211;no-ipt-sync</code></p>
<dd>Do not consult the iptables policy currently running on the machine for applicable snort rules. Unless limited with the &#8211;include-type or &#8211;snort-sid options this can result in a fwsnort.sh script that contains several thousand iptables rules.</p>
<dt><code>&#8211;no-ipt-test</code></p>
<dd>Do not test the iptables build for existence of support for the LOG and REJECT targets, and ascii and hex string matching.</p>
<dt><code>&#8211;no-ipt-jumps</code></p>
<dd>Do not jump packets from the built-in iptables INPUT, OUTPUT, and FORWARD chains to the custom <code>fwsnort</code> chains. This options is mostly useful to make it easy to manually alter the placement of the jump rules in the iptables ruleset.</p>
<dt><code>&#8211;no-ipt-rule-nums</code></p>
<dd>By default <code>fwsnort</code> includes the rule number within the logging prefix for each of the rules it adds to the fwsnort chains. E.g. the logging prefix for rule 34 would look something like &quot;[34] SID1242 ESTAB&quot;. Use this option to not include the rule number.</p>
<dt><code>&#8211;no-ipt-comments</code></p>
<dd>If the iptables &quot;comment&quot; match exists, then <code>fwsnort</code> puts the Snort &quot;msg&quot;, &quot;classtype&quot;, &quot;reference&quot;, &quot;priority&quot;, and &quot;rev&quot; fields within a comment for each iptables rule. Use this option to disable this.</p>
<dt><code>&#8211;no-ipt-INPUT</code></p>
<dd>Do not jump packets from the iptables INPUT chain to the <code>fwsnort</code> chains.</p>
<dt><code>&#8211;no-ipt-OUTPUT</code></p>
<dd>Do not jump packets from the iptables OUTPUT chain to the <code>fwsnort</code> chains.</p>
<dt><code>&#8211;no-ipt-FORWARD</code></p>
<dd>Do not jump packets from the iptables FORWARD chain to the <code>fwsnort</code> chains.</p>
<dt><code>-H</code>, <code>&#8211;Home-net&nbsp;<wbr>&lt;network/mask&gt;</code></p>
<dd>Specify the internal network instead of having <code>fwsnort</code> derive it from the HOME_NET keyword in the fwsnort.conf configuration file.</p>
<dt><code>-E</code>, <code>&#8211;External-net&nbsp;<wbr>&lt;network/mask&gt;</code></p>
<dd>Specify the external network instead of having <code>fwsnort</code> derive it from the EXTERNAL_NET keyword in the fwsnort.conf configuration file.</p>
<dt><code>&#8211;no-addresses</code></p>
<dd>Disable all checks against the output of ifconfig for proper IP addresses. This is useful if <code>fwsnort</code> is running on a bridging firewall.</p>
<dt><code>&#8211;Dump-conf</code></p>
<dd>Print the fwsnort configuration on STDOUT and exit.</p>
<dt><code>&#8211;debug</code></p>
<dd>Run in debug mode. This will cause all parse errors which are normally written to the fwsnort logfile <code>/var/log/fwsnort.log</code> to be written to STDOUT instead.</p>
<dt><code>&#8211;strict</code></p>
<dd>Run fwsnort in &quot;strict&quot; mode. This will prevent fwsnort from translating snort rules that contain the keywords &quot;offset&quot;, &quot;uricontent&quot;, and &quot;depth&quot;.</p>
<dt><code>-U</code>, <code>&#8211;Ulog</code></p>
<dd>Force the usage of the ULOG target for all log messages instead of the default LOG target.</p>
<dt><code>&#8211;ulog-nlgroup</code></p>
<dd>Specify the netlink group for ULOG rules. Such rules are only added for Snort rules that have an action of &quot;log&quot;, or when <code>fwsnort</code> is run in <code>&#8211;Ulog</code> mode.</p>
<dt><code>-l</code>, <code>&#8211;logfile&nbsp;<wbr>&lt;logfile&gt;</code></p>
<dd>By default fwsnort logs all parse errors to the logfile <code>/var/log/fwsnort.log.</code> This path can be manually changed with the &#8211;logfile option.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd>Run fwsnort in verbose mode. This will cause fwsnort to add the original snort rule as a comment to the fwsnort.sh script for each successfully translated rule.</p>
<dt><code>-V</code>, <code>&#8211;Version</code></p>
<dd>Print the fwsnort version and exit.</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd>Print usage information on STDOUT and exit.</dl>
<h2>Files</h2>
<p><code>/etc/fwnort/fwsnort.conf</code></p>
<dl>
<dd>The fwsnort configuration file. The path to this file can be changed on the command line with &#8211;config.</dl>
<p> <code>/etc/fwnort/fwsnort.sh</code></p>
<dl>
<dd>The iptables script generated by fwsnort. The path can be manually specified on the command line with the &#8211;ipt-script option.</dl>
<h2>Fwsnort Configuration Variables</h2>
<p>This section describes what each of the more important fwsnort configuration variables do and how they can be tuned to meet your needs. These variables are located in the fwsnort configuration file <code>/etc/fwsnort/fwsnort.conf</code></p>
<dl>
<dt><code>HOME_NET</code></p>
<dd><code>fwsnort</code> uses the same HOME_NET and EXTERNAL_NET variables as defined in Snort rules, and the same semantics are supported. I.e., individual IP addresses or networks in standard dotted-quad or CIDR notation can be specified, and comma separated lists are also supported.</p>
<dt><code>EXTERNAL_NET</code></p>
<dd>Defines the external network. See the HOME_NET variable for more information.</dl>
<h2>Examples</h2>
<p>The following examples illustrate the command line arguments that could be supplied to fwsnort in a few situations: </p>
<p> Script generation in logging mode, parse errors written to the fwsnort logfile, and iptables policy checking are enabled by default without having to specify any command line arguments: </p>
<p> <code># fwsnort</code> </p>
<p> Generate iptables rules for ddos and backdoor Snort rules only: </p>
<p> <code># fwsnort &#8211;include-type ddos,backdoor</code> </p>
<p> Generate iptables rules for Snort ID&#8217;s 2008475 and 2003268 (from emerging-all.rules): </p>
<p> <code>fwsnort &#8211;snort-sid 2008475,2003268</code> </p>
<p> Generate iptables rules for Snort ID&#8217;s 1834 and 2001842 but queue them to userspace via the NFQUEUE target and restrict exclude the INPUT and OUTPUT chains: </p>
<p> <code>fwsnort &#8211;snort-sid 1834,2001842 &#8211;NFQUEUE &#8211;no-ipt-INPUT &#8211;no-ipt-OUTPUT</code> </p>
<p> Instruct <code>fwsnort</code> to only inspect traffic that traverses the eth0 and eth1 interfaces: </p>
<p> <code># fwsnort &#8211;restrict-intf eth0,eth1</code> </p>
<p> Generate iptables rules for all Snort rules, and write original snort rule to the iptables script as a comment: </p>
<p> <code># fwsnort &#8211;no-ipt-sync &#8211;verbose</code></p>
<h2>Dependencies</h2>
<p><code>fwsnort</code> requires that the iptables string match module be compiled into the kernel (or as a loadable kernel module) in order to be able to match snort signatures that make use of the &quot;content&quot; keyword. Note that the &#8211;no-opt-test option can be specified to have fwsnort generate an iptables script even if the string match module is not compiled in. </p>
<p> <code>fwsnort</code> also requires the IPTables::Parse module in order to parse iptables policies.</p>
<h2>Diagnostics</h2>
<p>The &#8211;debug option can be used to display on STDOUT any errors that are generated as fwsnort parses each snort rule. Normally these errors are written to the fwsnort logfile /var/log/fwsnort.log</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-psad/">psad</a></code>(8), <code><a href="/docs/linux/man/8-iptables/">iptables</a></code>(8), <code><a href="/docs/linux/man/8-snort/">snort</a></code>(8), <code><a href="/docs/linux/man/1-nmap/">nmap</a></code>(1)</p>
<h2>Author</h2>
<p>Michael Rash &lt;mbr [at] cipherdyne.org&gt;</p>
<h2>Contributors</h2>
<p>Many people who are active in the open source community have contributed to fwsnort; see the <code>CREDITS</code> file in the fwsnort sources, or visit <code><a rel="nofollow" href="http://www.cipherdyne.org/fwsnort/docs/contributors.html">http://www.cipherdyne.org/fwsnort/docs/contributors.html</a></code> to view the online list of contributors. </p>
<p> <code>fwsnort</code> is based on the original <code>snort2iptables</code> script written by William Stearns.</p>
<h2>Bugs</h2>
<p>Send bug reports to mbr [at] cipherdyne.org. Suggestions and/or comments are always welcome as well.</p>
<h2>Distribution</h2>
<p><code>fwsnort</code> is distributed under the GNU General Public License (GPL), and the latest version may be downloaded from <code><a rel="nofollow" href="http://www.cipherdyne.org/">http://www.cipherdyne.org/</a></code></p>
