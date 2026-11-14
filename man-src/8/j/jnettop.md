---
title: "jnettop(8)"
name: "jnettop"
section: "8"
letter: "j"
url: "/docs/linux/man/8-jnettop/"
description: "jnettop – View hosts/ports taking up the most network traffic"
---

<p>jnettop &#8211; View hosts/ports taking up the most network traffic</p>
<h2>Synopsis</h2>
<p><code>jnettop</code> [options] [-i interface] [-d filename] [-f filename] [-x rule]</p>
<h2>Description</h2>
<p>This manual page documents briefly the <code>jnettop</code> command. This manual page is OBSOLETE. Please use jnettop -h as a main source of information about usage. </p>
<p> <code>jnettop</code> captures traffic coming across the host it is running on and displays streams sorted by bandwidth they use. Result is a nice listing of communication on network by host and port, how many bytes went through this transport and the bandwidth it is consuming.</p>
<h2>Options</h2>
<p>These programs follow the usual GNU command line syntax, with long options starting with two dashes (`-&#8216;). A summary of options is included below.</p>
<dl>
<dt><code>-h, &#8211;help</code></p>
<dd>Show summary of options.</p>
<dt><code>-v, &#8211;version</code></p>
<dd>Show version of program.</p>
<dt><code>-b, &#8211;bit-units</code></p>
<dd>show BPS In bits per second, not bytes per second</p>
<dt><code>-c, &#8211;content-filter</code></p>
<dd>disable content filtering</p>
<dt><code>-d, &#8211;debug filename</code></p>
<dd>write debug information into file</p>
<dt><code>-f, &#8211;config-file filename</code></p>
<dd>reads configuration from filename. defaults to ~/.jnettop. an example can be found at /usr/share/doc/jnettop/dot.jnettop. or in .jnettop file from original distribution package.</p>
<dt><code>-i, &#8211;interface name</code></p>
<dd>capture packets on specified interface</p>
<dt><code>&#8211;local-aggr [none|host|port]</code></p>
<dd>set local aggregation to specified value</p>
<dt><code>-n, &#8211;no-resolver</code></p>
<dd>disable resolving of ip addresses</p>
<dt><code>-p, &#8211;promiscuous</code></p>
<dd>enables promiscuous mode on the sniffed interface</p>
<dt><code>&#8211;remote-aggr [none|host|port]</code></p>
<dd>set remote aggregation to specified value</p>
<dt><code>-s, &#8211;select-rule name</code></p>
<dd>selects one of the rules defined in .jnettop configuration file (by it&#8217;s name)</p>
<dt><code>-x, &#8211;filter rule</code></p>
<dd>allows for specification of custom filtering rule. this allows for <code><a href="/docs/linux/man/1-tcpdump/">tcpdump</a>(1)</code> style syntax. don&#8217;t forget to enclolse the filter into quotes when running from a shell.</dl>
<h2>Configuration</h2>
<p>Program looks for settings in the file specified by parameter <code>-f</code>, which defaults to ~/.jnettop. Configuration file is an ordinary text file with keywords and their arguments. You HAVE to enclose arguments into double quotes. Available keywords are:</p>
<dl>
<dt><code>interface &quot;&lt;interface_name&gt;&quot;</code></p>
<dd>The <code>interface</code> keyword specifies network interface on which to start listening. Example:</p>
<dl>
<dd>interface &quot;eth0&quot;</dl>
<dt><code>local_aggregation [none|host|port]</code></p>
<dd>The <code>local_aggregation</code> keyword specifies initial active local aggregation. Valid values are <code>none</code>, <code>host</code> and <code>port</code>. Example:</p>
<dl>
<dd>local_aggregation host</dl>
<dt><code>promisc [on|off]</code></p>
<dd>The <code>promisc</code> keyword specifies, whether jnettop captures packets in promiscuous mode. Example:</p>
<dl>
<dd>promisc on</dl>
<dt><code>remote_aggregation [none|host|port]</code></p>
<dd>The <code>remote_aggregation</code> keyword specifies initial active remote aggregation. Valid values are <code>none</code>, <code>host</code> and <code>port</code>. Example:</p>
<dl>
<dd>remote_aggregation port</dl>
<dt><code>resolve [on|off]</code></p>
<dd>The <code>resolve</code> keyword specifies, whether resolving is performed on the IP addresses or not.</p>
<dl>
<dd>resolve off</dl>
<dt><code>resolve_rule &quot;&lt;network address&gt;&quot; &quot;&lt;network mask&gt;&quot; [normal|external] (&lt;arguments&gt; &#8230;)</code></p>
<dd>The <code>resolve_rule</code> keyword adds one resolver into list of resolvers for specified address. When resolving, jnettop examines all the rules in the order how they were specified in configuration file. If the network address matches specified range, declared resolver is used. Resolver can be <code>normal</code>, which means the standard DNS lookup or <code>external</code>, which executes specified external program to perform resolving. This can be used with bundled jnettop-lookup-nmb script, which looks up IP addresses using <a href="/docs/linux/man/1-nmblookup/">nmblookup</a>(1) tool. If a tool returns empty string or DNS is not found, next rule is examined. If jnettop runs out of rules, than the standard DNS lookup is executed.</p>
<dl>
<dd>resolve_rule &quot;192.168.0.0&quot; &quot;255.255.255.0&quot; normal<br />
 resolve_rule &quot;192.168.0.0&quot; &quot;255.255.255.0&quot; external &quot;/usr/share/jnettop/jnettop-lookup-nbm&quot;</dl>
<dt><code>rule &quot;&lt;rule_name&gt;&quot; &quot;&lt;rule_definition&gt;&quot;</code></p>
<dd>The <code>rule</code> keyword defines a set of predefined <a href="/docs/linux/man/1-tcpdump/">tcpdump</a>(1)-like filters to apply. You can specify various filters as &quot;show me what 192.168.1.32&quot; sends:</p>
<dl>
<dd>rule &quot;show 192.168.1.32&quot; &quot;src 192.168.1.32&quot;</dl>
<dt><code>select_rule &quot;&lt;rule_name&gt;&quot;</code></p>
<dd>The <code>select_rule</code> keyword specifies initial active predefined rule. The rule must be defined before this keyword is used. Example:</p>
<dl>
<dd>select_rule &quot;show 192.168.1.32&quot;</dl>
<dt><code>variable &quot;&lt;variable_name&gt;&quot; &quot;&lt;variable_contents&gt;&quot;</code></p>
<dd>The <code>variable</code> keyword introduces a string variable for use in future rule definitions. It can be used to shorten rule definitions. Example:</p>
<dl>
<dd>variable &quot;intranet&quot; &quot;net 192.168.0.0/16 or 10.0.0.0/8 or 172.16.0.0/12&quot;</dl>
<dt>For more information, see README file or .jnettop example configuration file included in distribution.</p>
<dd></dl>
<h2>Author</h2>
<p>This manual page was originally written by Ari Pollak &lt;ari [at] debian.org&gt;, for the Debian GNU/Linux system. Small changes were introduced by Jakub Skopal &lt;j@kubs.cz&gt;</p>
