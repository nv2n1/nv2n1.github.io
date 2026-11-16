---
title: "dnstop(8)"
name: "dnstop"
section: "8"
letter: "d"
url: "/docs/linux/man/8-dnstop/"
description: "dnstop – displays various tables of DNS traffic on your network"
---

<p><code>dnstop</code> &#8211; displays various tables of DNS traffic on your network</p>
<h2>Synopsis</h2>
<p>[-<code>46apsQR</code> ] [-<code>b </code><i>expression</i> ] [-<code>i </code><i>address</i> ] [-<code>f </code><i>filter</i> ] [-<code>r </code><i>interval</i> ] [<i>device</i> ] [<i>savefile</i> ]</p>
<h2>Description</h2>
<p>is a small tool to listen on <i>device</i> or to parse the file <i>savefile</i> and collect and print statistics on the local network&#8217;s DNS traffic. You must have read access to /dev/bpf*</p>
<h2>Command Line Options</h2>
<p>The options are as follows:</p>
<dl>
<dt><code>-4</code></dt>
<dd>count only messages with IPv4 addresses</dd>
<dt><code>-6</code></dt>
<dd>count only messages with IPv6 addresses</dd>
<dt><code>-Q</code></dt>
<dd>count only DNS query messages</dd>
<dt><code>-R</code></dt>
<dd>count only DNS reply messages</dd>
<dt><code>-a</code></dt>
<dd>anonymize addresses</dd>
<dt><code>-b </code><i>expression</i></dt>
<dd>BPF filter expression<br />
 (default: udp port 53)</dd>
<dt><code>-i </code><i>address</i></dt>
<dd>ignore select addresses</dd>
<dt><code>-p</code></dt>
<dd>Do not put the interface into promiscuous mode.</dd>
<dt><code>-r</code></dt>
<dd>Redraw interval (seconds).</dd>
<dt><code>-l </code><i>level</i></dt>
<dd>keep counts on names up to level domain name levels. </dd>
<p> For example, with -l 2 (the default), will keep two tables: one with top-level domain names, and another with second-level domain names. Increasing the level provides more details, but also requires more memory and CPU.</p>
<dt><code>-f</code></dt>
<dd>input filter name </dd>
<p> The &quot;unknown-tlds&quot; filter includes only queries for TLDs that are bogus. Useful for identifying hosts/servers that leak queries for things like &quot;localhost&quot; or &quot;workgroup.&quot; </p>
<p> The &quot;new-gtlds&quot; filter includes only queries for the new gTLD program of 2013/2014. Useful for identifying hosts/servers that use names which may result in future collisions and problems when new gTLDs become active. </p>
<p> The &quot;A-for-A&quot; filter includes only A queries for names that are already IP addresses. Certain Microsoft Windows DNS servers have a known bug that forward these queries. </p>
<p> The &quot;rfc1918-ptr&quot; filter includes only PTR queries for addresses in RFC1918 space. These should never leak from inside an organization. </p>
<p> The &quot;refused&quot; filter, when used with the &#8211;<code>R</code> option, tells to count only replies with rcode REFUSED. </p>
<p> The &quot;qtype-any&quot; filter tells to count only message of type ANY.</p>
<dt><code>-n </code><i>name</i></dt>
<dd>Only count messages within the domain <i>name</i></dd>
<dt><code>-P</code></dt>
<dd>Print &quot;progress&quot; messages on stderr when in non-interactive mode.</dd>
<dt><code>-B </code><i>buckets</i></dt>
<dd>Use buckets hash table buckets.</dd>
<dt><code>-X</code></dt>
<dd>Do not tabulate the sources + query name counters. This can significantly reduce memory usage on busy servers and large savefiles.</dd>
<dt><i>savefile</i></dt>
<dd>a captured network trace in <code>pcap</code> format</dd>
<dt><i>device</i></dt>
<dd>ethernet device (ie fxp0)</dd></dl>
<h2>Run Time Options</h2>
<p>While running, the following options are available to alter the display:</p>
<dl>
<dt><code>s</code></dt>
<dd>display the source address table</dd>
<dt><code>d </code></dt>
<dd>display the destination address table</dd>
<dt><code>t</code></dt>
<dd>display the breakdown of query types seen</dd>
<dt><code>r</code></dt>
<dd>display the breakdown of response codes seen</dd>
<dt><code>o</code></dt>
<dd>display the breakdown of opcodes seen</dd>
<dt><code>1</code></dt>
<dd>show 1st level query names</dd>
<dt><code>2</code></dt>
<dd>show 2nd level query names</dd>
<dt><code>3</code></dt>
<dd>show 3rd level query names</dd>
<dt><code>4</code></dt>
<dd>show 4th level query names</dd>
<dt><code>5</code></dt>
<dd>show 5th level query names</dd>
<dt><code>6</code></dt>
<dd>show 6th level query names</dd>
<dt><code>7</code></dt>
<dd>show 7th level query names</dd>
<dt><code>8</code></dt>
<dd>show 8th level query names</dd>
<dt><code>9</code></dt>
<dd>show 9th level query names</dd>
<dt><code>!</code></dt>
<dd>show sources + 1st level query names</dd>
<dt><code>@</code></dt>
<dd>show sources + 2nd level query names</dd>
<dt><code>#</code></dt>
<dd>show sources + 3rd level query names</dd>
<dt><code>$</code></dt>
<dd>show sources + 4th level query names</dd>
<dt><code>%</code></dt>
<dd>show sources + 5th level query names</dd>
<dt><code>^</code></dt>
<dd>show sources + 6th level query names</dd>
<dt><code>&amp;</code></dt>
<dd>show sources + 7th level query names</dd>
<dt><code>*</code></dt>
<dd>show sources + 8th level query names</dd>
<dt><code>(</code></dt>
<dd>show sources + 9th level query names</dd>
<dt><code>^R</code></dt>
<dd>reset the counters</dd>
<dt><code>^X</code></dt>
<dd>exit the program</dd>
<dt><code>space</code></dt>
<dd>redraw</dd>
<dt><code>?</code></dt>
<dd>help</dd></dl>
<h2>Non-Interactive Mode</h2>
<p>If stdout is not a tty, runs in non-interactive mode. In this case, you must supply a savefile for reading, instead of capturing live packets. After reading the entire savefile, prints the top 50 entries for each table.</p>
<h2>How Messages Are Counted</h2>
<p>By default examines only query messages and ignores replies. In this case the response code table is meaningless and will likely show 100% &quot;Noerror.&quot; </p>
<p> If you supply (only) the &#8211;<code>R</code> command line option, examines replies and ignores queries. This allows you to see meaningful response code values, as well as all the other tables. In this case all the query attributes (such as type and name) are taken from the Question section of the reply. </p>
<p> Note, however, that it is common for a stream of DNS messages to contain more queries than replies. This could happen, for example, if the server is too busy to respond to every single query, or if the server is designed to ignore malformed query messages. Therefore, you might want to examine both queries and replies by giving both &#8211;<code>R</code> and &#8211;<code>Q</code> command line options. In this case, only the response code counts are taken from the replies and all other attributes are taken from the queries.</p>
<h2>Authors</h2>
<dl>
<dt><code>Duane Wessels (wessels [at] measurement-factory.com) </code></dt>
<dd>
</dd><dt><code>Mark Foster (mark [at] foster.cc) </code></dt>
<dd>
</dd><dt><code>Jose Nazario (jose [at] monkey.org) </code></dt>
<dd>
</dd><dt><code>Sam Norris &lt;@ChangeIP.com&gt; </code></dt>
<dd>
</dd><dt><code>Max Horn &lt;@quendi.de&gt; </code></dt>
<dd>
</dd><dt><code>John Morrissey &lt;jwm [at] horde.net&gt; </code></dt>
<dd>
</dd><dt><code>Florian Forster &lt;octo [at] verplant.org&gt; </code></dt>
<dd>
</dd><dt><code>Dave Plonka &lt;plonka [at] cs.wisc.edu&gt; </code></dt>
<dd>
</dd><dt><code><a rel="nofollow" href="http://dnstop.measurement-factory.com/">http://dnstop.measurement-factory.com/</a> </code></dt>
<dd></dd></dl>
<h2>Bugs</h2>
<p>Does not support TCP at this time. </p>
