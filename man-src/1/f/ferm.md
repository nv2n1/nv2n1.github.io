---
title: "ferm(1)"
name: "ferm"
section: "1"
letter: "f"
url: "/docs/linux/man/1-ferm/"
description: "ferm – a firewall rule parser for linux"
---

<h2 class="name">NAME</h2>
<p> ferm &#8211; a firewall rule parser for linux </p>
<h2>SYNOPSIS</h2>
<p> <code>ferm</code> <i>options</i> <i>inputfile</i></p>
<h2>DESCRIPTION</h2>
<p> <code>ferm</code> is a frontend for <code>iptables</code>. It reads the rules from a structured configuration file and calls <i><a href="/docs/linux/man/8-iptables/">iptables</a></i>(8) to insert them into the running kernel. </p>
<p> <code>ferm</code>&#8216;s goal is to make firewall rules easy to write and easy to read. It tries to reduce the tedious task of writing down rules, thus enabling the firewall administrator to spend more time on developing good rules than the proper implementation of the rule. </p>
<p> To achieve this, <code>ferm</code> uses a simple but powerful configuration language, which allows variables, functions, arrays, blocks. It also allows you to include other files, allowing you to create libraries of commonly used structures and functions. </p>
<p> <code>ferm</code>, pronounced &#8220;firm&#8221;, stands for &#8220;For Easy Rule Making&#8221;.</p>
<h2>CAUTION</h2>
<p> This manual page does <i>not</i> indend to teach you how firewalling works and how to write good rules. There is already enough documentation on this topic.</p>
<h2>INTRODUCTION</h2>
<p> Let&#8217;s start with a simple example: </p>
<pre>
    chain INPUT {
        proto tcp ACCEPT;
    }
</pre>
<p> This will add a rule to the predefined input chain, matching and accepting all tcp packets. Ok, let&#8217;s make it more complicated: </p>
<pre><code>
chain(INPUT OUTPUT)
{
    proto(udp tcp) ACCEPT;
}
</code></pre>
<p> This will insert 4 rules, namely 2 in chain input, and 2 in chain output, matching and accepting both udp and tcp packets. Normally you would type this: </p>
<pre>
   iptables -A INPUT -p tcp -j ACCEPT
   iptables -A OUTPUT -p tcp -j ACCEPT
   iptables -A INPUT -p udp -j ACCEPT
   iptables -A OUTPUT -p udp -j ACCEPT
</pre>
<p> Note how much less typing we need to do? :-) </p>
<p> Basically, this is all there is to it, although you can make it quite more complex. Something to look at: </p>
<p>chain INPUT<br />
{<br />
    policy ACCEPT;<br />
    daddr 10.0.0.0 / 8 proto tcp dport !ftp jump mychain sport : 1023 TOS 4 settos 8 mark 2;<br />
    daddr 10.0.0.0 / 8 proto tcp dport ftp REJECT;<br />
}</p>
<p> My point here is, that *you* need to make nice rules, keep them readable to you and others, and not make it into a mess. </p>
<p> It would aid the reader if the resulting firewall rules were placed here for reference. Also, you could include the nested version with better readability. </p>
<p> Try using comments to show what you are doing: </p>
<pre>
    # this line enables transparent http-proxying for the internal network:
    proto tcp if eth0 daddr ! 192.168.0.0/255.255.255.0
        dport http REDIRECT to-ports 3128;
</pre>
<p> You will be thankful for it later! </p>
<p>chain INPUT<br />
{<br />
    policy ACCEPT;<br />
    interface(eth0 ppp0)<br />
    {<br />
#deny access to notorius hackers, return here if no match<br />
#was found to resume normal firewalling<br />
        jump badguys;<br />
        protocol tcp jump fw_tcp;<br />
        protocol udp jump fw_udp;<br />
    }<br />
}</p>
<p> The more you nest, the better it looks. Make sure the order you specify is correct, you would not want to do this: </p>
<p>chain FORWARD<br />
{<br />
    proto !udp DROP;<br />
    proto tcp dport ftp ACCEPT;<br />
}</p>
<p> because the second rule will never match. Best way is to specify first everyting that is allowed, and then deny everything else. Look at the examples for more good snapshots. Most people do something like this: </p>
<p>proto tcp<br />
{<br />
    dport(<br />
        ssh http ftp) ACCEPT;<br />
    dport 1024 : 65535 !syn ACCEPT;<br />
    DROP;<br />
}</p>
<h2>STRUCTURE OF A FIREWALL FILE</h2>
<p> The structure of a proper firewall file looks like simplified C-code. Only a few syntactic characters are used in ferm- configuration files. Besides these special caracters, ferm uses &#8216;keys&#8217; and &#8216;values&#8217;, think of them as options and parameters, or as variables and values, whatever. </p>
<p> With these words, you define the characteristics of your firewall. Every firewall consists of two things: First, look if network traffic matches certain conditions, and second, what to do with that traffic. </p>
<p> You may specify conditions that are valid for the kernel interface program you are using, probably <i><a href="/docs/linux/man/8-iptables/">iptables</a></i>(8). For instance, in iptables, when you are trying to match tcp packets, you would say: </p>
<pre>
    iptables --protocol tcp
</pre>
<p> In ferm, this will become: </p>
<pre>
    protocol tcp;
</pre>
<p> Just typing this in ferm doesn&#8217;t do anything, you need to tell ferm (actually, you need to tell <i><a href="/docs/linux/man/8-iptables/">iptables</a></i>(8) and the kernel) what to do with any traffic that matches this condition: </p>
<pre>
    iptables --protocol tcp -j ACCEPT
</pre>
<p> Or, translated to <code>ferm</code>: </p>
<pre>
    protocol tcp ACCEPT;
</pre>
<p> The <code>;</code> character is at the end of every ferm rule. Ferm ignores line breaks, meaning the above example is identical to the following: </p>
<pre>
    protocol tcp
      ACCEPT;
</pre>
<p> Here&#8217;s a list of the special characters:</p>
<dl>
<dt><code>;</code></p>
<dd> This character finalizes a rule. </p>
<p> Separated by semicolons, you may write multiple rules in one line, although this decreases readability: </p>
<pre>
    protocol tcp ACCEPT; protocol udp DROP;
</pre>
<dt><code>{}</code></p>
<dd> The nesting symbol defines a &#8216;block&#8217; of rules. </p>
<p> The curly brackets contain any number of nested rules. All matches before the block are carried forward to these. </p>
<p> The closing curly bracket finalizes the rule set. You should not write a &#8216;;&#8217; after that, because that would be an empty rule. </p>
<p> Example: </p>
<p>chain INPUT proto icmp<br />
{<br />
    icmp &#8211; type echo &#8211; request ACCEPT;<br />
    DROP;<br />
}</p>
<p> This block shows two rules inside a block, which will both be merged with anything in front of it, so you will get two rules: </p>
<pre>
    iptables -A INPUT -p icmp --icmp-type echo-request -j ACCEPT
    iptables -A INPUT -p icmp -j DROP
</pre>
<p> There can be multiple nesting levels: </p>
<p>chain INPUT<br />
{<br />
    proto icmp<br />
    {<br />
        icmp &#8211; type echo &#8211; request ACCEPT;<br />
        DROP;<br />
    }<br />
    daddr 172.16.0.0 / 12 REJECT;<br />
}</p>
<p> Note that the &#8216;<font SIZE="-1">REJECT</font>&#8216; rule is not affected by &#8216;proto icmp&#8217;, although there is no &#8216;;&#8217; after the closing curly brace. Translated to iptables: </p>
<pre>
    iptables -A INPUT -p icmp --icmp-type echo-request -j ACCEPT
    iptables -A INPUT -p icmp -j DROP
    iptables -A INPUT -d 172.16.0.0/12 -j REJECT
</pre>
<dt><code>$</code></p>
<dd> Variable expansion. Replaces &#8216;$FOO&#8217; by the value of the variable. See the section <i></i><font SIZE="-1"><i>VARIABLES</i></font><i></i> for details.</p>
<dt><code>&amp;</code></p>
<dd> Function call. See the section <i></i><font SIZE="-1"><i>FUNCTIONS</i></font><i></i> for details.</p>
<dt><code>()</code></p>
<dd> The array symbol. Using the parentheses, you can define a &#8216;list&#8217; of values that should be applied for the key to the left of it. </p>
<p> Example: </p>
<pre>
    protocol ( tcp udp icmp )
</pre>
<p> this will result in three rules: </p>
<pre>
    ... -p tcp ...
    ... -p udp ...
    ... -p icmp ...
</pre>
<p> Only values can be &#8216;listed&#8217;, so you cannot do something like this: </p>
<pre>
    proto tcp ( ACCEPT LOG );
</pre>
<p> but you can do this: </p>
<pre>
    chain (INPUT OUTPUT FORWARD) proto (icmp udp tcp) DROP;
</pre>
<p> (which will result in nine rules!) </p>
<p> Values are separated by spaces. The array symbol is both left- and right-associative, in contrast with the nesting block, which is left-associative only.</p>
<dt>&quot; # &quot;</p>
<dd> The comment symbol. Anything that follows this symbol up to the end of line is ignored.</p>
<dt>&quot;`command`&quot;</p>
<dd> Execute the command in a shell, and insert the process output. See the section <i>backticks</i> for details.</p>
<dt>&#8216;string&#8217;</p>
<dd> Quote a string which may contain whitespaces, the dollar sign etc. </p>
<pre>
    LOG log-prefix ' hey, this is my log prefix!';
</pre>
<dt>&quot;string&quot;</p>
<dd> Quote a string (see above), but variable references with a dollar sign are evaluated: </p>
<pre>
    DNAT to &quot;$myhost:$myport&quot;;
</pre>
</dl>
<h3>Keywords</h3>
<p> In the previous section, we already introduced some basic keywords like &#8220;chain&#8221;, &#8220;protocol&#8221; and &#8220;<font SIZE="-1">ACCEPT</font>&#8221;. Let&#8217;s explore their nature. </p>
<p> There are three kinds of keywords:</p>
<dl>
<dt>&bull;</p>
<dd> <code>location</code> keywords define where a rule will be created. Example: &#8220;table&#8221;, &#8220;chain&#8221;.</p>
<dt>&bull;</p>
<dd> <code>match</code> keywords perform a test on all passing packets. The current rule is without effect if one (or more) of the matches does not pass. Example: &#8220;proto&#8221;, &#8220;daddr&#8221;. </p>
<p> Most matches are followed by a parameter: &#8220;proto tcp&#8221;, &#8220;daddr 172.16.0.0/12&#8221;.</p>
<dt>&bull;</p>
<dd> <code>target</code> keywords state what to do with a packet. Example: &#8220;<font SIZE="-1">ACCEPT</font>&#8221;, &#8220;<font SIZE="-1">REJECT</font>&#8221;, &#8220;jump&#8221;. </p>
<p> Some targets define more keywords to specify details: &#8220;<font SIZE="-1">REJECT</font> reject-with icmp-net-unreachable&#8221;.</dl>
<p> Every rule consists of a <code>location</code> and a <code>target</code>, plus any number of <code>matches</code>: </p>
<pre>
    table filter                  # location
    proto tcp dport (http https)  # match
    ACCEPT;                       # target
</pre>
<p> Strictly speaking, there is a fourth kind: <code>ferm</code> keywords (which control ferm&#8217;s internal behaviour), but they will be explained later.</p>
<h3>Parameters</h3>
<p> Many keywords take parameters. These can be specified as literals, variable references or lists (arrays): </p>
<p>proto udp<br />
    saddr $TRUSTED_HOSTS;<br />
proto tcp dport(http https ssh);<br />
LOG log &#8211; prefix &#8220;funky wardriver alert: &#8220;;</p>
<p> Some of them can be negated (lists cannot be negated): </p>
<pre>
    proto !esp;
    proto udp dport !domain;
</pre>
<p> Keywords which take no parameters are negated by a prefixed &#8216;!&#8217;: </p>
<pre>
    proto tcp !syn;
</pre>
<p> Read <i><a href="/docs/linux/man/8-iptables/">iptables</a></i>(8) to see where the <code>!</code> can be used.</p>
<h2>BASIC KEYWORDS</h2>
<h3>Location keywords</h3>
<dl>
<dt><code>domain [ip|ip6]</code></p>
<dd> Set the domain. &#8220;ip&#8221; is default and means &#8220;IPv4&#8221; (iptables). &#8220;ip6&#8221; is for IPv6 support, using &#8220;ip6tables&#8221;.</p>
<dt><code>table [filter|nat|mangle]</code></p>
<dd> Specifies which netfilter table this rule will be inserted to: &#8220;filter&#8221; (default), &#8220;nat&#8221; or &#8220;mangle&#8221;.</p>
<dt><code>chain [chain-name]</code></p>
<dd> Specifies the netfilter chain (within the current table) this rule will be inserted to. Common predefined chain names are &#8220;<font SIZE="-1">INPUT</font>&#8221;, &#8220;<font SIZE="-1">OUTPUT</font>&#8221;, &#8220;<font SIZE="-1">FORWARD</font>&#8221;, &#8220;<font SIZE="-1">PREROUTING</font>&#8221;, &#8220;<font SIZE="-1">POSTROUTING</font>&#8221;, depending on the table. See the netfilter documentation for details. </p>
<p> If you specify a non-existing chain here, ferm will add the rule to a custom chain with that name.</p>
<dt><code>policy [ACCEPT|DROP|..]</code></p>
<dd> Specifies the default policy for the current chain (built-in only). Can be one of the built-in targets (<font SIZE="-1">ACCEPT</font>, <font SIZE="-1">DROP</font>, <font SIZE="-1">REJECT</font>, &#8230;). A packet that matches no rules in a chain will be treated as specified by the policy. </p>
<p> To avoid ambiguity, always specify the policies of all predefined chains explicitly.</p>
<dt><code>@subchain [&quot;</code><font SIZE="-1"><code>CHAIN-NAME</code></font><code>&quot;] { &#8230; }</code></p>
<dd> Works like the normal block operators (i.e. without the <i></i>@subchain<i></i> keyword), except that <code>ferm</code> moves rules within the curly braces into a new custom chain. The name for this chain is chosen automatically by ferm. </p>
<p> In many cases, this is faster than just a block, because the kernel may skip a huge block of rules when a precondition is false. Imagine the following example: </p>
<p>table filter chain INPUT<br />
{<br />
    saddr(1.2.3.4 2.3.4.5 3.4.5.6 4.5.6.7 5.6.7.8)<br />
    {<br />
        proto tcp dport(http https ssh) ACCEPT;<br />
        proto udp dport domain ACCEPT;<br />
    }<br />
}</p>
<p> This generates 20 rules. When a packet arrives which does not pass the <code>saddr</code> match, it nonetheless checks all 20 rules. With @subchain, this check is done once, resulting in faster network filtering and less <font SIZE="-1">CPU</font> load: </p>
<p>table filter chain INPUT<br />
{<br />
    saddr(1.2.3.4 2.3.4.5 3.4.5.6 4.5.6.7 5.6.7.8) @subchain<br />
    {<br />
        proto tcp dport(http https ssh) ACCEPT;<br />
        proto udp dport domain ACCEPT;<br />
    }<br />
}</p>
<p> Optionally, you may define the name of the sub chain: </p>
<p>saddr(1.2.3.4 2.3.4.5 3.4.5.6) @subchain &#8220;foobar&#8221;<br />
{<br />
    proto tcp dport(http https ssh) ACCEPT;<br />
    proto udp dport domain ACCEPT;<br />
}</p>
<p> The name can either be a quoted string literal, or an expanded ferm expression such as <tt>@ca</tt>t(&#8220;interface_&#8221;, <tt>$iface</tt>) or <tt>@subst</tt>r($var,0,20). </p>
<p> You can achieve the same by explicitly declaring a custom chain, but you may feel that using @subchain requires less typing.</dl>
<h3>Basic iptables match keywords</h3>
<dl>
<dt><code>interface [interface-name]</code></p>
<dd> Define the interface name, your outside network card, like eth0, or dialup like ppp1, or whatever device you want to match for passing packets. It is equivalent to the <tt>&quot;-i&quot;</tt> switch in <i><a href="/docs/linux/man/8-iptables/">iptables</a></i>(8).</p>
<dt><code>outerface [interface-name]</code></p>
<dd> Same as interface, only for matching the outgoing interface for a packet, as in <i><a href="/docs/linux/man/8-iptables/">iptables</a></i>(8).</p>
<dt><code>protocol [protocol-name|protocol-number]</code></p>
<dd> Currently supported by the kernel are tcp, udp and icmp, or their respective numbers.</p>
<dt><code>saddr|daddr [address-spec]</code></p>
<dd> Matches on packets originating from the specified address (saddr) or targeted at the address (daddr). </p>
<p> Examples: </p>
<pre>
    saddr 192.168/8 ACCEPT; # (identical to the next one:)
    saddr 192.168.0.0/255.255.255.0 ACCEPT;
    daddr my.domain.com ACCEPT;
</pre>
<dt><code>fragment</code></p>
<dd> Specify that only fragmented <font SIZE="-1">IP</font> packets should be matched. When packets are larger that the maximum packet size your system can handle (called Maximum Transmission Unit or <font SIZE="-1">MTU</font>) they will be chopped into bits and sent one by one as single packets. See <i><a href="/docs/linux/man/8-ifconfig/">ifconfig</a></i>(8) if you want to find the <font SIZE="-1">MTU</font> for your system (the default is usually 1500 bytes). </p>
<p> Fragments are frequently used in <font SIZE="-1">DOS</font> attacks, because there is no way of finding out the origin of a fragment packet.</p>
<dt><code>sport|dport [port-spec]</code></p>
<dd> Matches on packets on the specified <font SIZE="-1">TCP</font> or <font SIZE="-1">UDP</font> port. &#8220;sport&#8221; matches the source port, and dport matches the destination port. </p>
<p> This match can be used only after you specified &#8220;protocol tcp&#8221; or &#8220;protocol udp&#8221;, because only these two protocols actually have ports. </p>
<p> And some examples of valid ports/ranges: </p>
<p>dport 80 ACCEPT;<br />
dport http ACCEPT;<br />
dport ssh : http ACCEPT;<br />
dport 0 : 1023 ACCEPT;<br />
#equivalent to : 1023 dport 1023 : 65535 ACCEPT;</p>
<dt><code>syn</code></p>
<dd> Specify that the <font SIZE="-1">SYN</font> flag in a tcp package should be matched, which are used to build new tcp connections. You can identify incoming connections with this, and decide wether you want to allow it or not. Packets that do not have this flag are probably from an already established connection, so it&#8217;s considered reasonably safe to let these through.</p>
<dt><code>module [module-name]</code></p>
<dd> Load an iptables module. Most modules provide more match keywords. We&#8217;ll get to that later.</dl>
<h3>Basic target keywords</h3>
<dl>
<dt><code>jump [custom-chain-name]</code></p>
<dd> Jumps to a custom chain. If no rule in the custom chain matched, netfilter returns to the next rule in the previous chain.</p>
<dt><code>realgoto [custom-chain-name]</code></p>
<dd> Go to a custom chain. Unlike the <code>jump</code> option, <font SIZE="-1"><code>RETURN</code></font> will not continue processing in this chain but instead in the chain that called us via <code>jump</code>. </p>
<p> The keyword <code>realgoto</code> was chosen during the transition period, because <code>goto</code> (already deprecated) used to be an alias for <code>jump</code>.</p>
<dt><font SIZE="-1"><code>ACCEPT</code></font></p>
<dd> Accepts matching packets.</p>
<dt><font SIZE="-1"><code>DROP</code></font></p>
<dd> Drop matching packets without further notice.</p>
<dt><font SIZE="-1"><code>REJECT</code></font></p>
<dd> Rejects matching packets, i.e. send an <font SIZE="-1">ICMP</font> packet to the sender, which is port-unreachable by default. You may specify another <font SIZE="-1">ICMP</font> type. </p>
<pre>
    REJECT; # default to icmp-port-unreachable
    REJECT reject-with icmp-net-unreachable;
</pre>
<p> Type &#8220;iptables -j <font SIZE="-1">REJECT</font> -h&#8221; for details.</p>
<dt><font SIZE="-1"><code>RETURN</code></font></p>
<dd> Finish the current chain and return to the calling chain (if &#8220;jump [custom-chain-name]&#8221; was used).</p>
<dt><font SIZE="-1"><code>NOP</code></font></p>
<dd> No action at all.</dl>
<h2>ADDITIONAL KEYWORDS</h2>
<p> Netfilter is modular. Modules may provide additional targets and match keywords. The list of netfilter modules is constantly growing, and ferm tries to keep up with supporting them all. This chapter describes modules which are currently supported.</p>
<h3>iptables match modules</h3>
<dl>
<dt><code>account</code></p>
<dd> Account traffic for all hosts in defined network/netmask. This is one of the match modules which behave like a target, i.e. you will mostly have to use the <font SIZE="-1"><code>NOP</code></font> target. </p>
<pre>
    mod account aname mynetwork aaddr 192.168.1.0/24 ashort NOP;
</pre>
<dt><code>addrtype</code></p>
<dd> Check the address type; either source address or destination address. </p>
<pre>
    mod addrtype src-type BROADCAST;
    mod addrtype dst-type LOCAL;
</pre>
<p> Type &#8220;iptables -m addrtype -h&#8221; for details.</p>
<dt><code>ah</code></p>
<dd> Checks the <font SIZE="-1">SPI</font> header in an <font SIZE="-1">AH</font> packet. </p>
<pre>
    mod ah ahspi 0x101;
    mod ah ahspi ! 0x200:0x2ff;
</pre>
<p> Additional arguments for IPv6: </p>
<pre>
    mod ah ahlen 32 ACCEPT;
    mod ah ahlen !32 ACCEPT;
    mod ah ahres ACCEPT;
</pre>
<dt><code>comment</code></p>
<dd> Adds a comment of up to 256 characters to a rule, without an effect. Note that unlike ferm comments (&#8216;#&#8217;), this one will show up in &#8220;iptables -L&#8221;. </p>
<pre>
    mod comment comment &quot;This is my comment.&quot; ACCEPT;
</pre>
<dt><code>condition</code></p>
<dd> Matches if a value in /proc/net/ipt_condition/NAME is 1 (path is /proc/net/ip6t_condition/NAME for the ip6 domain). </p>
<pre>
    mod condition condition (abc def) ACCEPT;
    mod condition condition !foo ACCEPT;
</pre>
<dt><code>connbytes</code></p>
<dd> Match by how many bytes or packets a connection (or one of the two flows constituting the connection) have tranferred so far, or by average bytes per packet. </p>
<pre>
    mod connbytes connbytes 65536: connbytes-dir both connbytes-mode bytes ACCEPT;
    mod connbytes connbytes !1024:2048 connbytes-dir reply connbytes-mode packets ACCEPT;
</pre>
<p> Valid values for <i>connbytes-dir</i>: <i>original</i>, <i>reply</i>, <i>both</i>; for <i>connbytes-mode</i>: <i>packets</i>, <i>bytes</i>, <i>avgpkt</i>.</p>
<dt><code>connlimit</code></p>
<dd> Allows you to restrict the number of parallel <font SIZE="-1">TCP</font> connections to a server per client <font SIZE="-1">IP</font> address (or address block). </p>
<pre>
    mod connlimit connlimit-above 4 REJECT;
    mod connlimit connlimit-above !4 ACCEPT;
    mod connlimit connlimit-above 4 connlimit-mask 24 REJECT;
</pre>
<dt><code>connmark</code></p>
<dd> Check the mark field associated with the connection, set by the <font SIZE="-1">CONNMARK</font> target. </p>
<pre>
    mod connmark mark 64;
    mod connmark mark 6/7;
</pre>
<dt><code>conntrack</code></p>
<dd> Check connection tracking information. </p>
<p>mod conntrack ctstate(ESTABLISHED RELATED);<br />
mod conntrack ctproto tcp;<br />
mod conntrack ctorigsrc 192.168.0.2;<br />
mod conntrack ctorigdst 1.2.3.0 / 24;<br />
mod conntrack ctorigsrcport 67;<br />
mod conntrack ctorigdstport 22;<br />
mod conntrack ctreplsrc 2.3.4.5;<br />
mod conntrack ctrepldst !3.4.5.6;<br />
mod conntrack ctstatus ASSURED;<br />
mod conntrack ctexpire 60;<br />
mod conntrack ctexpire 180 : 240;</p>
<p> Type &#8220;iptables -m conntrack -h&#8221; for details.</p>
<dt><code>dccp</code></p>
<dd> Check <font SIZE="-1">DCCP</font> (Datagram Congestion Control Protocol) specific attributes. This module is automatically loaded when you use &#8220;protocol dccp&#8221;. </p>
<p>proto dccp sport 1234 dport 2345 ACCEPT;<br />
proto dccp dccp &#8211; types(SYNCACK ACK) ACCEPT;<br />
proto dccp dccp &#8211; types !REQUEST DROP;<br />
proto dccp dccp &#8211; option 2 ACCEPT;</p>
<dt><code>dscp</code></p>
<dd> Match the 6 bit <font SIZE="-1">DSCP</font> field within the <font SIZE="-1">TOS</font> field. </p>
<pre>
    mod dscp dscp 11;
    mod dscp dscp-class AF41;
</pre>
<dt><code>ecn</code></p>
<dd> Match the <font SIZE="-1">ECN</font> bits of an IPv4 <font SIZE="-1">TCP</font> header. </p>
<pre>
    mod ecn ecn-tcp-cwr;
    mod ecn ecn-tcp-ece;
    mod ecn ecn-ip-ect 2;
</pre>
<p> Type &#8220;iptables -m ecn -h&#8221; for details.</p>
<dt><code>esp</code></p>
<dd> Checks the <font SIZE="-1">SPI</font> header in an <font SIZE="-1">ESP</font> packet. </p>
<pre>
    mod esp espspi 0x101;
    mod esp espspi ! 0x200:0x2ff;
</pre>
<dt><code>eui64</code></p>
<dd> &#8220;This module matches the <font SIZE="-1">EUI-64</font> part of a stateless autoconfigured IPv6 address. It compares the <font SIZE="-1">EUI-64</font> derived from the source <font SIZE="-1">MAC</font> address in Ehternet frame with the lower 64 bits of the IPv6 source address. But &#8221;Universal/Local&#8220; bit is not compared. This module doesn&#8217;t match other link layer frame, and is only valid in the <font SIZE="-1">PREROUTING</font>, <font SIZE="-1">INPUT</font> and <font SIZE="-1">FORWARD</font> chains.&#8221; </p>
<pre>
    mod eui64 ACCEPT;
</pre>
<dt><code>fuzzy</code></p>
<dd> &#8220;This module matches a rate limit based on a fuzzy logic controller [<font SIZE="-1">FLC</font>].&#8221; </p>
<pre>
    mod fuzzy lower-limit 10 upper-limit 20 ACCEPT;
</pre>
<dt><code>hbh</code></p>
<dd> Matches the Hop-by-Hop Options header (ip6). </p>
<p>mod hbh hbh &#8211; len 8 ACCEPT;<br />
mod hbh hbh &#8211; len !8 ACCEPT;<br />
mod hbh hbh &#8211; opts(1 : 4 2 : 8) ACCEPT;</p>
<dt><code>hl</code></p>
<dd> Matches the Hop Limit field (ip6). </p>
<p>mod hl hl &#8211; eq(8 10) ACCEPT;<br />
mod hl hl &#8211; eq !5 ACCEPT;<br />
mod hl hl &#8211; gt 15 ACCEPT;<br />
mod hl hl &#8211; lt 2 ACCEPT;</p>
<dt><code>helper</code></p>
<dd> Checks which conntrack helper module tracks this connection. The port may be specified with &#8220;-portnr&#8221;. </p>
<pre>
    mod helper helper irc ACCEPT;
    mod helper helper ftp-21 ACCEPT;
</pre>
<dt><code>icmp</code></p>
<dd> Check <font SIZE="-1">ICMP</font> specific attributes. This module is automatically loaded when you use &#8220;protocol icmp&#8221;. </p>
<pre>
    proto icmp icmp-type echo-request ACCEPT;
</pre>
<p> This option can also be used in be <i>ip6</i> domain, although this is called <code>icmpv6</code> in <i>ip6tables</i>. </p>
<p> Use &quot;iptables -p icmp <tt>&quot;-h&quot;</tt>&quot; to obtain a list of valid <font SIZE="-1">ICMP</font> types.</p>
<dt><code>iprange</code></p>
<dd> Match a range of IPv4 addresses. </p>
<pre>
    mod iprange src-range 192.168.2.0-192.168.3.255;
    mod iprange dst-range ! 192.168.6.0-192.168.6.255;
</pre>
<dt><code>ipv4options</code></p>
<dd> Match on IPv4 header options like source routing, record route, timestamp and router-alert. </p>
<p>mod ipv4options ssrr ACCEPT;<br />
mod ipv4options lsrr ACCEPT;<br />
mod ipv4options no &#8211; srr ACCEPT;<br />
mod ipv4options !rr ACCEPT;<br />
mod ipv4options !ts ACCEPT;<br />
mod ipv4options !ra ACCEPT;<br />
mod ipv4options !any &#8211; opt ACCEPT;</p>
<dt><code>ipv6header</code></p>
<dd> Matches the IPv6 extension header (ip6). </p>
<p>mod ipv6header header !(hop frag)ACCEPT;<br />
mod ipv6header header(auth dst) ACCEPT;</p>
<dt><code>hashlimit</code></p>
<dd> Similar to &#8216;mod limit&#8217;, but adds the ability to add per-destination or per-port limits managed in a hash table. </p>
<pre>
    mod hashlimit  hashlimit 10/minute  hashlimit-burst 30/minute
      hashlimit-mode dstip  hashlimit-name foobar  ACCEPT;
</pre>
<p> Possible values for hashlimit-mode: dstip dstport srcip srcport (or a list with more than one of these). </p>
<p> There are more possible settings, type &#8220;iptables -m hashlimit -h&#8221; for documentation.</p>
<dt><code>length</code></p>
<dd> Check the package length. </p>
<pre>
    mod length length 128; # exactly 128 bytes
    mod length length 512:768; # range
    mod length length ! 256; # negated
</pre>
<dt><code>limit</code></p>
<dd> Limits the packet rate. </p>
<pre>
    mod limit limit 1/second;
    mod limit limit 15/minute limit-burst 10;
</pre>
<p> Type &#8220;iptables -m limit -h&#8221; for details.</p>
<dt><code>mac</code></p>
<dd> Match the source <font SIZE="-1">MAC</font> address. </p>
<pre>
    mod mac mac-source 01:23:45:67:89;
</pre>
<dt><code>mark</code></p>
<dd> Matches packets based on their netfilter mark field. This may be a 32 bit integer between 0 and 4294967295. </p>
<pre>
    mod mark mark 42;
</pre>
<dt><code>mh</code></p>
<dd> Matches the mobility header (domain <i>ip6</i>). </p>
<pre>
    proto mh mh-type binding-update ACCEPT;
</pre>
<dt><code>multiport</code></p>
<dd> Match a set of source or destination ports (<font SIZE="-1">UDP</font> and <font SIZE="-1">TCP</font> only). </p>
<p>mod multiport source &#8211; ports(https ftp);<br />
mod multiport destination &#8211; ports(mysql domain);</p>
<p> This rule has a big advantage over &#8220;dport&#8221; and &#8220;sport&#8221;: it generates only one rule for up to 15 ports instead of one rule for every port.</p>
<dt><code>nth</code></p>
<dd> Match every &#8216;n&#8217;th packet. </p>
<p>mod nth every 3;<br />
mod nth counter 5 every 2;<br />
mod nth start 2 every 3;<br />
mod nth start 5 packet 2 every 6;</p>
<p> Type &#8220;iptables -m nth -h&#8221; for details.</p>
<dt><code>osf</code></p>
<dd> Match packets depending on the operating system of the sender. </p>
<pre>
    mod osf genre Linux;
    mod osf ! genre FreeBSD ttl 1 log 1;
</pre>
<p> Type &#8220;iptables -m osf -h&#8221; for details.</p>
<dt><code>owner</code></p>
<dd> Check information about the packet creator, namely user id, group id, process id, session id and command name. </p>
<p>mod owner uid &#8211; owner 0;<br />
mod owner gid &#8211; owner 1000;<br />
mod owner pid &#8211; owner 5432;<br />
mod owner sid &#8211; owner 6543;<br />
mod owner cmd &#8211; owner &#8220;sendmail&#8221;;</p>
<p> (&#8220;cmd-owner&#8221;, &#8220;pid-owner&#8221; and &#8220;sid-owner&#8221; require special kernel patches not included in the vanilla Linux kernel)</p>
<dt><code>physdev</code></p>
<dd> Matches the physical device on which a packet entered or is about to leave the machine. This is useful for bridged interfaces. </p>
<p>mod physdev physdev &#8211; in ppp1;<br />
mod physdev physdev &#8211; out eth2;<br />
mod physdev physdev &#8211; is &#8211; in;<br />
mod physdev physdev &#8211; is &#8211; out;<br />
mod physdev physdev &#8211; is &#8211; bridged;</p>
<dt><code>pkttype</code></p>
<dd> Check the link-layer packet type. </p>
<pre>
    mod pkttype pkt-type unicast;
    mod pkttype pkt-type broadcase;
    mod pkttype pkt-type multicast;
</pre>
<dt><code>policy</code></p>
<dd> Matches IPsec policy being applied to this packet. </p>
<p>mod policy dir out pol ipsec ACCEPT;<br />
mod policy strict reqid 23 spi 0x10 proto ah ACCEPT;<br />
mod policy mode tunnel tunnel &#8211; src 192.168.1.2 ACCEPT;<br />
mod policy mode tunnel tunnel &#8211; dst 192.168.2.1 ACCEPT;<br />
mod policy strict next reqid 24 spi 0x11 ACCEPT;</p>
<p> Note that the keyword <i>proto</i> is also used as a shorthand version of <i>protocol</i> (built-in match module). You can fix this conflict by always using the long keyword <i>protocol</i>.</p>
<dt><code>psd</code></p>
<dd> Detect <font SIZE="-1">TCP/UDP</font> port scans. </p>
<pre>
    mod psd psd-weight-threshold 21 psd-delay-threshold 300
      psd-lo-ports-weight 3 psd-hi-ports-weight 1 DROP;
</pre>
<dt><code>quota</code></p>
<dd> Implements network quotas by decrementing a byte counter with each packet. </p>
<pre>
    mod quota quota 65536 ACCEPT;
</pre>
<dt><code>random</code></p>
<dd> Match a random percentage of all packets. </p>
<pre>
    mod random average 70;
</pre>
<dt><code>realm</code></p>
<dd> Match the routing realm. Useful in environments using <font SIZE="-1">BGP</font>. </p>
<pre>
    mod realm realm 3;
</pre>
<dt><code>recent</code></p>
<dd> Temporarily mark source <font SIZE="-1">IP</font> addresses. </p>
<p>mod recent set;<br />
mod recent rcheck seconds 60;<br />
mod recent set rsource name &#8220;badguy&#8221;;<br />
mod recent set rdest;<br />
mod recent rcheck rsource name &#8220;badguy&#8221; seconds 60;<br />
mod recent update seconds 120 hitcount 3 rttl;</p>
<p> This netfilter module has a design flaw: although it is implemented as a match module, it has target-like behaviour when using the &#8220;set&#8221; keyword. </p>
<p> &lt;<a rel="nofollow" href="http://snowman.net/projects/ipt_recent/">http://snowman.net/projects/ipt_recent/</a>&gt;</p>
<dt><code>rt</code></p>
<dd> Match the IPv6 routing header (ip6 only). </p>
<p>mod rt rt &#8211; type 2 rt &#8211; len 20 ACCEPT;<br />
mod rt rt &#8211; type !2 rt &#8211; len !20 ACCEPT;<br />
mod rt rt &#8211; segsleft 2 : 3 ACCEPT;<br />
mod rt rt &#8211; segsleft !4 : 5 ACCEPT;<br />
mod rt rt &#8211; 0 &#8211; res rt &#8211; 0 &#8211; addrs(::1 ::2) rt &#8211; 0 &#8211; not -strict ACCEPT;</p>
<dt><code>sctp</code></p>
<dd> Check <font SIZE="-1">SCTP</font> (Stream Control Transmission Protocol) specific attributes. This module is automatically loaded when you use &#8220;protocol sctp&#8221;. </p>
<p>proto sctp sport 1234 dport 2345 ACCEPT;<br />
proto sctp chunk &#8211; types only DATA : Be ACCEPT;<br />
proto sctp chunk &#8211; types any(INIT INIT_ACK) ACCEPT;<br />
proto sctp chunk &#8211; types !all(HEARTBEAT) ACCEPT;</p>
<p> Use &quot;iptables -p sctp <tt>&quot;-h&quot;</tt>&quot; to obtain a list of valid chunk types.</p>
<dt><code>set</code></p>
<dd> Checks the source or destination IP/Port/MAC against a set. </p>
<pre>
    mod set set badguys src DROP;
</pre>
<p> See &lt;<a rel="nofollow" href="http://ipset.netfilter.org/">http://ipset.netfilter.org/</a>&gt; for more information.</p>
<dt><code>state</code></p>
<dd> Checks the connection tracking state. </p>
<pre>
    mod state state INVALID DROP;
    mod state state (ESTABLISHED RELATED) ACCEPT;
</pre>
<p> Type &#8220;iptables -m state -h&#8221; for details.</p>
<dt><code>statistic</code></p>
<dd> Successor of <code>nth</code> and <code>random</code>, currently undocumented in the <i><a href="/docs/linux/man/8-iptables/">iptables</a></i>(8) man page. </p>
<pre>
    mod statistic mode random probability 0.8 ACCEPT;
    mod statistic mode nth every 5 packet 0 DROP;
</pre>
<dt><code>string</code></p>
<dd> Matches a string. </p>
<pre>
    mod string string &quot;foo bar&quot; ACCEPT;
    mod string algo kmp from 64 to 128 hex-string &quot;deadbeef&quot; ACCEPT;
</pre>
<dt><code>tcp</code></p>
<dd> Checks <font SIZE="-1">TCP</font> specific attributes. This module is automatically loaded when you use &#8220;protocol tcp&#8221;. </p>
<p>proto tcp sport 1234;<br />
proto tcp dport 2345;<br />
proto tcp tcp &#8211; flags(SYN ACK) SYN;<br />
proto tcp tcp &#8211; flags !(SYN ACK)SYN;<br />
proto tcp tcp &#8211; flags ALL(RST ACK);<br />
proto tcp syn;<br />
proto tcp tcp &#8211; option 2;<br />
proto tcp mss 512;</p>
<p> Type &#8220;iptables -p tcp -h&#8221; for details.</p>
<dt><code>tcpmss</code></p>
<dd> Check the <font SIZE="-1">TCP</font> <font SIZE="-1">MSS</font> field of a <font SIZE="-1">SYN</font> or <font SIZE="-1">SYN/ACK</font> packet. </p>
<pre>
    mod tcpmss mss 123 ACCEPT;
    mod tcpmss mss 234:567 ACCEPT;
</pre>
<dt><code>time</code></p>
<dd> Check if the time a packet arrives is in given range. </p>
<p>mod time timestart 12 : 00;<br />
mod time timestop 13 : 30;<br />
mod time days(Mon Wed Fri);<br />
mod time datestart 2005 : 01 : 01;<br />
mod time datestart 2005 : 01 : 01 : 23 : 59 : 59;<br />
mod time datestop 2005 : 04 : 01;<br />
mod time monthday(30 31);<br />
mod time weekdays(Wed Thu);<br />
mod time timestart 12 : 00 utc;<br />
mod time timestart 12 : 00 localtz;</p>
<p> Type &#8220;iptables -m time -h&#8221; for details.</p>
<dt><code>tos</code></p>
<dd> Matches a packet on the specified TOS-value. </p>
<pre>
    mod tos tos Minimize-Cost ACCEPT;
    mod tos tos !Normal-Service ACCEPT;
</pre>
<p> Type &#8220;iptables -m tos -h&#8221; for details.</p>
<dt><code>ttl</code></p>
<dd> Matches the ttl (time to live) field in the <font SIZE="-1">IP</font> header. </p>
<pre>
    mod ttl ttl-eq 12; # ttl equals
    mod ttl ttl-gt 10; # ttl greater than
    mod ttl ttl-lt 16; # ttl less than
</pre>
<dt><code>u32</code></p>
<dd> Compares raw data from the packet. You can specify more than one filter in a ferm list; these are not expanded into multiple rules. </p>
<pre>
    mod u32 u32 '6&amp;0xFF=1' ACCEPT;
    mod u32 u32 ('27&amp;0x8f=7' '31=0x527c4833') DROP;
</pre>
<dt><code>unclean</code></p>
<dd> Matches packets which seem malformed or unusual. This match has no further parameters.</dl>
<h3>iptables target modules</h3>
<p> The following additional targets are available in ferm, provided that you enabled them in your kernel:</p>
<dl>
<dt><font SIZE="-1"><code>CLASSIFY</code></font></p>
<dd> Set the <font SIZE="-1">CBQ</font> class. </p>
<pre>
    CLASSIFY set-class 3:50;
</pre>
<dt><font SIZE="-1"><code>CLUSTERIP</code></font></p>
<dd> Configure a simple cluster of nodes that share a certain <font SIZE="-1">IP</font> and <font SIZE="-1">MAC</font> address. Connections are statically distributed between the nodes. </p>
<pre>
    CLUSTERIP new hashmode sourceip clustermac 00:12:34:45:67:89
      total-nodes 4 local-node 2 hash-init 12345;
</pre>
<dt><font SIZE="-1"><code>CONNMARK</code></font></p>
<dd> Sets the netfilter mark value associated with a connection. </p>
<p>CONNMARK set &#8211; mark 42;<br />
CONNMARK save &#8211; mark;<br />
CONNMARK restore &#8211; mark;<br />
CONNMARK save &#8211; mark mask 0x7fff;<br />
CONNMARK restore &#8211; mark mask 0x8000;</p>
<dt><font SIZE="-1"><code>CONNSECMARK</code></font></p>
<dd> This module copies security markings from packets to connections (if unlabeled), and from connections back to packets (also only if unlabeled). Typically used in conjunction with <font SIZE="-1">SECMARK</font>, it is only valid in the mangle table. </p>
<pre>
    CONNSECMARK save;
    CONNSECMARK restore;
</pre>
<dt><font SIZE="-1"><code>DNAT</code></font><code> to [ip-address|ip-range|ip-port-range]</code></p>
<dd> Change the destination address of the packet. </p>
<p>DNAT to 10.0.0.4;<br />
DNAT to 10.0.0.4 : 80;<br />
DNAT to 10.0.0.4 : 1024 &#8211; 2048;<br />
DNAT to 10.0.1.1 &#8211; 10.0.1.20;</p>
<dt><font SIZE="-1"><code>ECN</code></font></p>
<dd> This target allows to selectively work around known <font SIZE="-1">ECN</font> blackholes. It can only be used in the mangle table. </p>
<pre>
    ECN ecn-tcp-remove;
</pre>
<dt><font SIZE="-1"><code>HL</code></font></p>
<dd> Modify the IPv6 Hop Limit field (ip6/mangle only). </p>
<pre>
    HL hl-set 5;
    HL hl-dec 2;
    HL hl-inc 1;
</pre>
<dt><font SIZE="-1"><code>IPV4OPTSSTRIP</code></font></p>
<dd> Strip all the <font SIZE="-1">IP</font> options from a packet. This module does not take any options. </p>
<pre>
    IPV4OPTSSTRIP;
</pre>
<dt><font SIZE="-1"><code>LOG</code></font></p>
<dd> Log all packets that match this rule in the kernel log. Be carefull with log flooding. Note that this is a &#8220;non-terminating target&#8221;, i.e. rule traversal continues at the next rule. </p>
<pre>
    LOG log-level warning log-prefix &quot;Look at this: &quot;;
    LOG log-tcp-sequence log-tcp-options;
    LOG log-ip-options;
</pre>
<dt><font SIZE="-1"><code>MARK</code></font></p>
<dd> Sets the netfilter mark field for the packet (a 32 bit integer between 0 and 4294967295): </p>
<p>MARK set &#8211; mark 42;<br />
MARK set &#8211; xmark 7 / 3;<br />
MARK and -mark 31;<br />
MARK or -mark 1;<br />
MARK xor -mark 12;</p>
<dt><font SIZE="-1"><code>MASQUERADE</code></font></p>
<dd> Masquerades matching packets. Optionally followed by a port or port-range for iptables. Specify as &#8220;123&#8221;, &#8220;123-456&#8221; or &#8220;123:456&#8221;. The port range parameter specifies what local ports masqueraded connections should originate from. </p>
<pre>
    MASQUERADE;
    MASQUERADE to-ports 1234:2345;
    MASQUERADE to-ports 1234:2345 random;
</pre>
<dt><font SIZE="-1"><code>MIRROR</code></font></p>
<dd> Experimental demonstration target which inverts the source and destination fields in the <font SIZE="-1">IP</font> header. </p>
<pre>
    MIRROR;
</pre>
<dt><font SIZE="-1"><code>NETMAP</code></font></p>
<dd> Map a whole network onto another network in the <code>nat</code> table. </p>
<pre>
    NETMAP to 192.168.2.0/24;
</pre>
<dt><font SIZE="-1"><code>NOTRACK</code></font></p>
<dd> Disable connection tracking for all packets matching that rule. </p>
<pre>
    proto tcp dport (135:139 445) NOTRACK;
</pre>
<dt><font SIZE="-1"><code>NFLOG</code></font></p>
<dd> Log packets over netlink; this is the successor of <i></i><font SIZE="-1"><i>ULOG</i></font><i></i>. </p>
<pre>
    NFLOG nflog-group 5 nflog-prefix &quot;Look at this: &quot;;
    NFLOG nflog-range 256;
    NFLOG nflog-threshold 10;
</pre>
<dt><font SIZE="-1"><code>NFQUEUE</code></font></p>
<dd> Userspace queueing, requires nfnetlink_queue kernel support. </p>
<pre>
    proto tcp dport ftp NFQUEUE queue-num 20;
</pre>
<dt><font SIZE="-1"><code>QUEUE</code></font></p>
<dd> Userspace queueing, the predecessor to <font SIZE="-1"><code>NFQUEUE</code></font>. All packets go to queue 0. </p>
<pre>
    proto tcp dport ftp QUEUE;
</pre>
<dt><font SIZE="-1"><code>REDIRECT</code></font><code> to-ports [ports]</code></p>
<dd> Transparent proxying: alter the destination <font SIZE="-1">IP</font> of the packet to the machine itself. </p>
<pre>
    proto tcp dport http REDIRECT to-ports 3128;
    proto tcp dport http REDIRECT to-ports 3128 random;
</pre>
<dt><font SIZE="-1"><code>SAME</code></font></p>
<dd> Similar to <font SIZE="-1">SNAT</font>, but a client is mapped to the same source <font SIZE="-1">IP</font> for all its connections. </p>
<pre>
    SAME to 1.2.3.4-1.2.3.7;
    SAME to 1.2.3.8-1.2.3.15 nodst;
    SAME to 1.2.3.16-1.2.3.31 random;
</pre>
<dt><font SIZE="-1"><code>SECMARK</code></font></p>
<dd> This is used to set the security mark value associated with the packet for use by security subsystems such as SELinux. It is only valid in the mangle table. </p>
<pre>
    SECMARK selctx &quot;system_u:object_r:httpd_packet_t:s0&quot;;
</pre>
<dt><font SIZE="-1"><code>SET</code></font><code> [add-set|del-set] [setname] [flag(s)]</code></p>
<dd> Add the <font SIZE="-1">IP</font> to the specified set. See &lt;<a rel="nofollow" href="http://ipset.netfilter.org/">http://ipset.netfilter.org/</a>&gt; </p>
<pre>
    proto icmp icmp-type echo-request SET add-set badguys src;
</pre>
<dt><font SIZE="-1"><code>SNAT</code></font><code> to [ip-address|ip-range|ip-port-range]</code></p>
<dd> Change the source address of the packet. </p>
<pre>
    SNAT to 1.2.3.4;
    SNAT to 1.2.3.4:20000-30000;
    SNAT to 1.2.3.4 random;
</pre>
<dt><font SIZE="-1"><code>TCPMSS</code></font></p>
<dd> Alter the <font SIZE="-1">MSS</font> value of <font SIZE="-1">TCP</font> <font SIZE="-1">SYN</font> packets. </p>
<pre>
    TCPMSS set-mss 1400;
    TCPMSS clamp-mss-to-pmtu;
</pre>
<dt><font SIZE="-1"><code>TOS</code></font><code> set-tos [value]</code></p>
<dd> Set the tcp package Type Of Service bit to this value. This will be used by whatever traffic scheduler is willing to, mostly your own linux-machine, but maybe more. The original tos-bits are blanked and overwritten by this value. </p>
<p>TOS set &#8211; tos Maximize &#8211; Throughput;<br />
TOS and -tos 7;<br />
TOS or -tos 1;<br />
TOS xor -tos 4;</p>
<p> Type &#8220;iptables -j <font SIZE="-1">TOS</font> -h&#8221; for details.</p>
<dt><font SIZE="-1"><code>TTL</code></font></p>
<dd> Modify the <font SIZE="-1">TTL</font> header field. </p>
<pre>
    TTL ttl-set 16;
    TTL ttl-dec 1; # decrease by 1
    TTL ttl-inc 4; # increase by 4
</pre>
<dt><font SIZE="-1"><code>ULOG</code></font></p>
<dd> Log packets to a userspace program. </p>
<pre>
    ULOG ulog-nlgroup 5 ulog-prefix &quot;Look at this: &quot;;
    ULOG ulog-cprange 256;
    ULOG ulog-qthreshold 10;
</pre>
</dl>
<h2>OTHER DOMAINS</h2>
<p> Since version 2.0, <code>ferm</code> supports not only <i>ip</i> and <i>ip6</i>, but also <i>arp</i> (<font SIZE="-1">ARP</font> tables) and <i>eb</i> (ethernet bridging tables). The concepts are similar to <i>iptables</i>.</p>
<h3>arptables keywords</h3>
<dl>
<dt><code>source-ip</code>, <code>destination-ip</code></p>
<dd> Matches the source or destination IPv4 address. Same as <code>saddr</code> and <code>daddr</code> in the <i>ip</i> domain.</p>
<dt><code>source-mac</code>, <code>destination-mac</code></p>
<dd> Matches the source or destination <font SIZE="-1">MAC</font> address.</p>
<dt><code>interface</code>, <code>outerface</code></p>
<dd> Input and output interface.</p>
<dt><code>h-length</code></p>
<dd> Hardware length of the packet. </p>
<pre>
    chain INPUT h-length 64 ACCEPT;
</pre>
<dt><code>opcode</code></p>
<dd> Operation code, for details see the <i><a href="/docs/linux/man/8-iptables/">iptables</a></i>(8). </p>
<pre>
    opcode 9 ACCEPT;
</pre>
<dt><code>h-type</code></p>
<dd> Hardware type. </p>
<pre>
    h-type 1 ACCEPT;
</pre>
<dt><code>proto-type</code></p>
<dd> Protocol type. </p>
<pre>
    proto-type 0x800 ACCEPT;
</pre>
<dt><code>Mangling</code></p>
<dd> The keywords <code>mangle-ip-s</code>, <code>mangle-ip-d</code>, <code>mangle-mac-s</code>, <code>mangle-mac-d</code>, <code>mangle-target</code> may be used for <font SIZE="-1">ARP</font> mangling. See <i><a href="/docs/linux/man/8-iptables/">iptables</a></i>(8) for details.</dl>
<h3>ebtables keywords</h3>
<dl>
<dt><code>proto</code></p>
<dd> Matches the protocol which created the frame, e.g. <i>IPv4</i> or <font SIZE="-1"><code>PPP</code></font>. For a list, see <i>/etc/ethertypes</i>.</p>
<dt><code>interface</code>, <code>outerface</code></p>
<dd> Physical input and output interface.</p>
<dt><code>logical-in</code>, <code>logical-out</code></p>
<dd> The logical bridge interface.</p>
<dt><code>saddr</code>, <code>daddr</code></p>
<dd> Matches source or destination <font SIZE="-1">MAC</font> address.</p>
<dt><code>Match modules</code></p>
<dd> The following match modules are supported: 802.3, arp, ip, mark_m, pkttype, stp, vlan, log.</p>
<dt><code>Target extensions</code></p>
<dd> The following target extensions are supported: arpreply, dnat, mark, redirect, snat. </p>
<p> Please note that there is a conflict between <i>&#8211;mark</i> from the <i>mark_m</i> match module and <i>-j mark</i>. Since both would be implemented with the ferm keyword <code>mark</code>, we decided to solve this by writing the target&#8217;s name in uppercase, like in the other domains. The following example rewrites mark 1 to 2: </p>
<pre>
    mark 1 MARK 2;
</pre>
</dl>
<h2>ADVANCED FEATURES</h2>
<h3>Variables</h3>
<p> In complex firewall files, it is helpful to use variables, e.g. to give a network interface a meaningful name. </p>
<p> To set variables, write: </p>
<p>@def $DEV_INTERNET = eth0;<br />
@def $PORTS = (http ftp);<br />
@def $MORE_PORTS = ($PORTS 8080);</p>
<p> In the real ferm code, variables are used like any other keyword parameter: </p>
<pre>
    chain INPUT interface $DEV_INTERNET proto tcp dport $MORE_PORTS ACCEPT;
</pre>
<p> Note that variables can only be used in keyword parameters (&#8220;192.168.1.1&#8221;, &#8220;http&#8221;); they cannot contain ferm keywords like &#8220;proto&#8221; or &#8220;interface&#8221;. </p>
<p> Variables are only valid in the current block: </p>
<p>@def $DEV_INTERNET = eth1;<br />
chain INPUT<br />
{<br />
    proto tcp<br />
    {<br />
        @def $DEV_INTERNET = ppp0;<br />
        interface $DEV_INTERNET dport http ACCEPT;<br />
    }<br />
    interface $DEV_INTERNET DROP;<br />
}</p>
<p> will be expanded to: </p>
<p>chain INPUT<br />
{<br />
    proto tcp<br />
    {<br />
        interface ppp0 dport http ACCEPT;<br />
    }<br />
    interface eth1 DROP;<br />
}</p>
<p> The &#8220;def <tt>$DEV_INTERNET</tt> = ppp0&#8221; is only valid in the &#8220;proto tcp&#8221; block; the parent block still knows &#8220;set <tt>$DEV_INTERNET</tt> = eth1&#8221;. </p>
<p> Include files are special &#8211; variables declared in an included file are still available in the calling block. This is useful when you include a file which only declares variables.</p>
<h3>Automatic variables</h3>
<p> Some variables are set internally by ferm. Ferm scripts can use them just like any other variable.</p>
<dl>
<dt><code>$FILENAME</code></p>
<dd> The name of the configuration file relative to the directory ferm was started in.</p>
<dt><code>$FILEBNAME</code></p>
<dd> The base name of the configuration file.</p>
<dt><code>$DIRNAME</code></p>
<dd> The directory of the configuration file.</p>
<dt><code>$DOMAIN</code></p>
<dd> The current domain. One of <i>ip</i>, <i>ip6</i>, <i>arp</i>, <i>eb</i>.</p>
<dt><code>$TABLE</code></p>
<dd> The current netfilter table.</p>
<dt><code>$CHAIN</code></p>
<dd> The current netfilter chain.</p>
<dt><code>$LINE</code></p>
<dd> The line of the current script. It can be used like this: </p>
<p>@def &amp;log($msg) = {<br />
    LOG log &#8211; prefix &#8220;rule=$msg:$LINE &#8220;;<br />
}<br />
.<br />
    .<br />
    .<br />
        &amp;log(&#8220;log message&#8221;);
</dl>
<h3>Functions</h3>
<p> Functions are similar to variables, except that they may have parameters, and they provide ferm commands, not values. </p>
<p>@def &amp;FOO() = proto(tcp udp) dport domain;<br />
&amp;FOO() ACCEPT;<br />
@def &amp;TCP_TUNNEL($port, $dest) = {<br />
    table filter chain FORWARD interface ppp0 proto tcp dport $port daddr $dest outerface eth0 ACCEPT;<br />
table nat chain PREROUTING interface ppp0 proto tcp dport $port daddr 1.2.3.4 DNAT to $dest;<br />
}<br />
&amp;TCP_TUNNEL(http, 192.168.1.33);<br />
&amp;TCP_TUNNEL(ftp, 192.168.1.30);<br />
&amp;TCP_TUNNEL((ssh smtp), 192.168.1.2);</p>
<p> A function call which contains a block (like &#8216;{&#8230;}&#8217;) must be the last command in a ferm rule, i.e. it must be followed by &#8216;;&#8217;. The &#8216;&amp;<i>FOO()</i>&#8216; example does not contain a block, thus you may write &#8216;<font SIZE="-1">ACCEPT</font>&#8216; after the call. To circumvent this, you can reorder the keywords: </p>
<p>@def &amp;IPSEC() = {proto(esp ah);<br />
proto udp dport 500;<br />
}<br />
chain INPUT ACCEPT &amp;IPSEC();</p>
<h3>Backticks</h3>
<p> With backticks, you may use the output of an external command: </p>
<p>@def $DNSSERVERS = `grep nameserver / etc / resolv.conf | awk &#8216;{print $2}&#8217;`;<br />
chain INPUT proto tcp saddr $DNSSERVERS ACCEPT;</p>
<p> The command is executed with the shell (<i>/bin/sh</i>), just like backticks in perl. ferm does not do any variable expansion here. </p>
<p> The output is then tokenized, and saved as a ferm list (array). Lines beginning with &#8216;#&#8217; are ignored; the other lines may contain any number of values, separated by whitespace.</p>
<h3>Includes</h3>
<p> The @include keyword allows you to include external files: </p>
<pre>
    @include 'vars.ferm';
</pre>
<p> The file name is relative to the calling file, e.g. when including from <i>/etc/ferm/ferm.conf</i>, the above statement includes <i>/etc/ferm/vars.ferm</i>. Variables and functions declared in an included file are still available in the calling file. </p>
<p> <code>include</code> works within a block: </p>
<p>chain INPUT<br />
{<br />
    @include &#8216;input.ferm&#8217;;<br />
}</p>
<p> If you specify a directory (with a trailing &#8216;/&#8217;), all files in this directory are included, sorted alphabetically: </p>
<pre>
    @include 'ferm.d/';
</pre>
<p> With a trailing pipe symbol, <code>ferm</code> executes a shell command and parses its output: </p>
<pre>
    @include '/root/generate_ferm_rules.sh $HOSTNAME|'
</pre>
<h3>Conditionals</h3>
<p> The keyword @if introduces a conditional expression: </p>
<pre>
    @if $condition DROP;
</pre>
<p> A value is evaluated true just like in Perl: zero, empty list, empty string are false, everything else is true. Examples for true values: </p>
<p>(a b);<br />
1;<br />
&#8216;foo&#8217;;<br />
(0 0)</p>
<p> Examples for false values: </p>
<p>();<br />
0;<br />
&#8216;0&#8217;;<br />
&#8221;</p>
<p> There is also @else: </p>
<p>@ if $condition DROP;<br />
@ else REJECT;</p>
<p> Note the semicolon before the @else. </p>
<p> It is possible to use curly braces after either @if or @else: </p>
<p>@ if $condition<br />
{<br />
    MARK set &#8211; mark 2;<br />
    RETURN;<br />
}<br />
@ else<br />
{<br />
    MARK set &#8211; mark 3;<br />
}</p>
<p> Since the closing curly brace also finishes the command, there is no need for semicolon. </p>
<p> There is no @elsif, use @else@if instead. </p>
<p> Example: </p>
<p>@def $have_ipv6 = `test &#8211; f / proc / net / ip6_tables_names &amp;&amp; echo 1 || echo`;<br />
@ if $have_ipv6<br />
{<br />
    domain ip6<br />
    {<br />
#&#8230;.<br />
    }<br />
}</p>
<h3>Hooks</h3>
<p> To run custom commands, you may install hooks: </p>
<pre>
    @hook pre &quot;echo 0 &gt;/proc/sys/net/ipv4/conf/eth0/forwarding&quot;;
    @hook post &quot;echo 1 &gt;/proc/sys/net/ipv4/conf/eth0/forwarding&quot;;
    @hook flush &quot;echo 0 &gt;/proc/sys/net/ipv4/conf/eth0/forwarding&quot;;
</pre>
<p> The specified command is executed using the shell. &#8220;pre&#8221; means run the command before applying the firewall rules, and &#8220;post&#8221; means run the command afterwards. &#8220;flush&#8221; hooks are run after ferm has flushed the firewall rules (option &#8211;flush). You may install any number of hooks.</p>
<h2>BUILT-IN FUNCTIONS</h2>
<p> There are several built-in functions which you might find useful.</p>
<h3>@eq(a,b)</h3>
<p> Tests two values for equality. Example: </p>
<pre>
    @if @eq($DOMAIN, ip6) DROP;
</pre>
<h3>@ne(a,b)</h3>
<p> Similar to <tt>@eq</tt>, this tests for non-equality.</p>
<h3>@not(x)</h3>
<p> Negates a boolean value.</p>
<h3>@resolve((hostname1 hostname2 &#8230;), [type])</h3>
<p> Usually, host names are resolved by iptables. To let ferm resolve host names, use the function <tt>@resolve:</tt> </p>
<p>saddr @resolve(my.host.foo) proto tcp dport ssh ACCEPT;<br />
saddr @resolve((another.host.foo third.host.foo)) proto tcp dport openvpn ACCEPT;<br />
daddr @resolve(ipv6.google.com, AAAA) proto tcp dport http ACCEPT;</p>
<p> Note the double parentheses in the second line: the inner pair for creating a ferm list, and the outer pair as function parameter delimiters. </p>
<p> The second parameter is optional, and specifies the <font SIZE="-1">DNS</font> record type. The default is &#8220;A&#8221;. </p>
<p> Be careful with resolved host names in firewall configuration. <font SIZE="-1">DNS</font> requests may block the firewall configuration for a long time, leaving the machine vulnerable, or they may fail.</p>
<h3>@cat(a, b, &#8230;)</h3>
<p> Concatenate all parameters into one string.</p>
<h3>@substr(expression, offset, length)</h3>
<p> Extracts a substring out of expression and returns it. First character is at offset 0. If <font SIZE="-1">OFFSET</font> is negative, starts that far from the end of the string.</p>
<h3>@length(expression)</h3>
<p> Returns the length in characters of the value of <font SIZE="-1">EXPR</font>.</p>
<h3>@basename(path)</h3>
<p> Return the base name of the file for a given path (File::Spec::splitpath).</p>
<h3>@dirname(path)</h3>
<p> Return the name of the last directory for a given path, assuming the last component is a file name (File::Spec::splitpath).</p>
<h3>@ipfilter(list)</h3>
<p> Filters out the <font SIZE="-1">IP</font> addresses that obviously do not match the current domain. That is useful to create common variables and rules for IPv4 and IPv6: </p>
<p>@def $TRUSTED_HOSTS = (192.168.0.40 2001<br />
                       : abcd<br />
                       : ef::40);<br />
domain(ip ip6) chain INPUT<br />
{<br />
    saddr @ipfilter($TRUSTED_HOSTS) proto tcp dport ssh ACCEPT;<br />
}</p>
<h2>RECIPES</h2>
<p> The <i>./examples/</i> directory contains numerous ferm configuration which can be used to begin a new firewall. This sections contains more samples, recipes and tricks.</p>
<h3>Easy port forwarding</h3>
<p> Ferm function make routine tasks quick and easy: </p>
<pre><code>
@def &amp;FORWARD_TCP($proto, $port, $dest) = {
    table filter chain FORWARD interface $DEV_WORLD outerface $DEV_DMZ daddr $dest proto $proto dport $port ACCEPT;
table nat chain PREROUTING interface $DEV_WORLD daddr $HOST_STATIC proto $proto dport $port DNAT to $dest;
}
&amp;FORWARD_TCP(tcp, http, 192.168.1.2);
&amp;FORWARD_TCP(tcp, smtp, 192.168.1.3);
&amp;FORWARD_TCP((tcp udp), domain, 192.168.1.4);
</code></pre>
<h3>Remote <code>ferm</code></h3>
<p> If the target machine is not able to run <code>ferm</code> for some reason (maybe an embedded device without Perl), you can edit the <code>ferm</code> configuration file on another computer and let <code>ferm</code> generate a shell script there. </p>
<p> Example for OpenWRT: </p>
<pre>
    ferm --remote --shell mywrt/ferm.conf &gt;mywrt/firewall.user
    chmod +x mywrt/firewall.user
    scp mywrt/firewall.user mywrt.local.net:/etc/
    ssh mywrt.local.net /etc/firewall.user
</pre>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;noexec</code></p>
<dd> Do not execute the <i><a href="/docs/linux/man/8-iptables/">iptables</a></i>(8) commands, but skip instead. This way you can parse your data, use <code>&#8211;lines</code> to view the output.</p>
<dt><code>&#8211;flush</code></p>
<dd> Clears the firewall rules and sets the policy of all chains to <font SIZE="-1">ACCEPT</font>. <code>ferm</code> needs a configuration file for that to determine which domains and tables are affected.</p>
<dt><code>&#8211;lines</code></p>
<dd> Show the firewall lines that were generated from the rules. They will be shown just before they are executed, so if you get error messages from <i><a href="/docs/linux/man/8-iptables/">iptables</a></i>(8) etc., you can see which rule caused the error.</p>
<dt><code>&#8211;interactive</code></p>
<dd> Apply the firewall rules and ask the user for confirmation. Reverts to the previous ruleset if there is no valid user response within 30 seconds (see <code>&#8211;timeout</code>). This is useful for remote firewall administration: you can test the rules without fearing to lock yourself out.</p>
<dt><code>&#8211;timeout S</code></p>
<dd> If <code>&#8211;interactive</code> is used, then roll back if there is no valid user response after this number of seconds. The default is 30.</p>
<dt><code>&#8211;help</code></p>
<dd> Show a brief list of available commandline options.</p>
<dt><code>&#8211;version</code></p>
<dd> Shows the version number of the program.</p>
<dt><code>&#8211;fast</code></p>
<dd> Enable fast mode: ferm generates an <i><a href="/docs/linux/man/8-iptables-save/">iptables-save</a></i>(8) file, and installs it with <i><a href="/docs/linux/man/8-iptables-restore/">iptables-restore</a></i>(8). This is much faster, because ferm calls <i><a href="/docs/linux/man/8-iptables/">iptables</a></i>(8) once for every rule by default. </p>
<p> Fast mode is enabled by default since <code>ferm</code> 2.0, deprecating this option.</p>
<dt><code>&#8211;slow</code></p>
<dd> Disable fast mode, i.e. run <i><a href="/docs/linux/man/8-iptables/">iptables</a></i>(8) for every rule, and don&#8217;t use <i><a href="/docs/linux/man/8-iptables-restore/">iptables-restore</a></i>(8).</p>
<dt><code>&#8211;shell</code></p>
<dd> Generate a shell script which calls <i><a href="/docs/linux/man/8-iptables-restore/">iptables-restore</a></i>(8) and prints it. Implies &#8211;fast &#8211;lines.</p>
<dt><code>&#8211;remote</code></p>
<dd> Generate rules for a remote machine. Implies <code>&#8211;noexec</code> and <code>&#8211;lines</code>. Can be combined with <code>&#8211;shell</code>.</p>
<dt><code>&#8211;domain {ip|ip6}</code></p>
<dd> Handle only the specified domain. <code>ferm</code> output may be empty if the domain is not configured in the input file.</p>
<dt><code>&#8211;def &#8216;$name=value&#8217;</code></p>
<dd> Override a variable defined in the configuration file.</dl>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/8-iptables/">iptables</a></i>(8)</p>
<h2>REQUIREMENTS</h2>
<h3>Operating system</h3>
<p> Linux 2.4 or newer, with netfilter support and all netfilter modules used by your firewall script</p>
<h3>Software</h3>
<p> iptables and perl 5.6</p>
<h2>BUGS</h2>
<p> Bugs? What bugs? </p>
<p> If you find a bug, please tell us: ferm [at] foo-projects.org</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2001-2012 Max Kellermann &lt;max [at] foo-projects.org&gt;, Auke Kok &lt;sofar [at] foo-projects.org&gt; </p>
<p> This program is free software; you can redistribute it and/or modify it under the terms of the <font SIZE="-1">GNU</font> General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. </p>
<p> This program is distributed in the hope that it will be useful, but <font SIZE="-1">WITHOUT</font> <font SIZE="-1">ANY</font> <font SIZE="-1">WARRANTY</font>; without even the implied warranty of <font SIZE="-1">MERCHANTABILITY</font> or <font SIZE="-1">FITNESS</font> <font SIZE="-1">FOR</font> A <font SIZE="-1">PARTICULAR</font> <font SIZE="-1">PURPOSE</font>. See the <font SIZE="-1">GNU</font> General Public License for more details. </p>
<p> You should have received a copy of the <font SIZE="-1">GNU</font> General Public License along with this program; if not, write to the Free Software Foundation, Inc., 59 Temple Place, Suite 330, Boston, <font SIZE="-1">MA</font> 02111-1307 <font SIZE="-1">USA</font></p>
<h2>AUTHOR</h2>
<p> Max Kellermann &lt;max [at] foo-projects.org&gt;, Auke Kok &lt;sofar [at] foo-projects.org&gt; </p>
<h2>Index</h2>
<dt><a href="#lbBP">OPTIONS</a></p>
<dd>
<dt><a href="#lbBQ">SEE ALSO</a></p>
<dd>
<dt><a href="#lbBR">REQUIREMENTS</a></p>
<dd>
<dt><a href="#lbBU">BUGS</a></p>
<dd>
<dt><a href="#lbBV">COPYRIGHT</a></p>
<dd>
<dt><a href="#lbBW">AUTHOR</a></p>
<dd></dl>
