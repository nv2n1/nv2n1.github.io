---
title: "tc-ematch(8)"
name: "tc-ematch"
section: "8"
letter: "t"
url: "/docs/linux/man/8-tc-ematch/"
description: "ematch – extended matches for use with \"basic\", \"cgroup\" or \"flow\" filters"
---

<p>ematch &#8211; extended matches for use with &quot;basic&quot;, &quot;cgroup&quot; or &quot;flow&quot; filters</p>
<h2>Synopsis</h2>
<p><code>tc filter add .. basic match</code> EXPR <code>.. flowid ..</code> <i>EXPR</i> := <i>TERM</i> [ { <code>and | or</code> } <i>EXPR</i> ] </p>
<pre><code>TERM := [ not ] { MATCH | '(' EXPR ')' }</code></pre>
<p> <i>MATCH</i> := <i>module</i> &#8216;(&#8216; <i>ARGS</i> &#8216;)&#8217; <i>ARGS</i> := <i>ARG1</i> <i>ARG2</i> .. </p>
<h2>Matches</h2>
<h3>cmp</h3>
<p>Simple comparison ematch: arithmetic compare of packet data to a given value. </p>
<p> <i>cmp</i>( <i>ALIGN</i> at <i>OFFSET</i> [ <i>ATTRS</i> ] { <i>eq</i> | <i>lt</i> | <i>gt</i> } <i>VALUE</i> ) </p>
<p> <i>ALIGN</i> := { <i>u8</i> | <i>u16</i> | <i>u32</i> } </p>
<p> <i>ATTRS</i> := [ layer <i>LAYER</i> ] [ mask <i>MASK</i> ] [ trans ] </p>
<p> <i>LAYER</i> := { <i>link</i> | <i>network</i> | <i>transport</i> | <i>0..2</i> }</p>
<h3>meta</h3>
<p>Metadata ematch </p>
<p> <i>meta</i>( <i>OBJECT</i> { <i>eq</i> | <i>lt</i> |<i>gt</i> } <i>OBJECT</i> ) </p>
<p> <i>OBJECT</i> := { <i>META_ID</i> | <i>VALUE</i> } </p>
<p> <i>META_ID</i> := <i>id</i> [ shift <i>SHIFT</i> ] [ mask <i>MASK</i> ] </p>
<dl>
<dt>meta attributes:</p>
<dd><code>random</code> 32 bit random value </p>
<p> <code>loadavg_1</code> Load average in last 5 minutes </p>
<p> <code>nf_mark</code> Netfilter mark </p>
<p> <code>vlan</code> Vlan tag </p>
<p> <code>sk_rcvbuf</code> Receive buffer size </p>
<p> <code>sk_snd_queue</code> Send queue length </p>
</dl>
<p> A full list of meta attributes can be obtained via </p>
<p> # tc filter add dev eth1 basic match &#8216;meta(list)&#8217;</p>
<h3>nbyte</h3>
<p>match packet data byte sequence </p>
<p> <i>nbyte</i>( <i>NEEDLE</i> at <i>OFFSET</i> [ layer <i>LAYER</i> ] ) </p>
<p> <i>NEEDLE</i> := { <i>string</i> | <i>c-escape-sequence</i> } </p>
<p> <i>OFFSET</i> := <i>int</i> </p>
<p> <i>LAYER</i> := { <i>link</i> | <i>network</i> | <i>transport</i> | <i>0..2</i> }</p>
<h3>u32</h3>
<p>u32 ematch </p>
<p> <i>u32</i>( <i>ALIGN</i> <i>VALUE</i> <i>MASK</i> at [ nexthdr+ ] <i>OFFSET</i> ) </p>
<p> <i>ALIGN</i> := { <i>u8</i> | <i>u16</i> | <i>u32</i> }</p>
<h3>ipset</h3>
<p>test packet against ipset membership </p>
<p> <i>ipset</i>( <i>SETNAME</i> <i>FLAGS</i> ) </p>
<p> <i>SETNAME</i> := <i>string</i> </p>
<p> <i>FLAGS</i> := { <i>FLAG</i> [, <i>FLAGS</i>] } </p>
<p> The flag options are the same as those used by the iptables &quot;set&quot; match. </p>
<p> When using the ipset ematch with the &quot;ip_set_hash:net,iface&quot; set type, the interface can be queried using &quot;src,dst (source ip address, outgoing interface) or &quot;src,src&quot; (source ip address, incoming interface) syntax.</p>
<h3>ipt</h3>
<p>test packet against xtables matches </p>
<p> <i>ipt</i>( <i>[-6]</i> -m<i> </i>MATCH_NAME<i> </i>FLAGS<i> )</i> </p>
<p> <i>MATCH_NAME</i> := <i>string</i> </p>
<p> <i>FLAGS</i> := { <i>FLAG</i> [, <i>FLAGS</i>] } </p>
<p> The flag options are the same as those used by the xtable match used.</p>
<h3>canid</h3>
<p>ematch rule to match CAN frames </p>
<p> <i>canid</i>( <i>IDLIST</i> ) </p>
<p> <i>IDLIST</i> := <i>IDSPEC</i>[<i>IDLIST</i>] </p>
<p> <i>IDSPEC</i> := { ’sff’ <i>CANID</i> | ’eff’ <i>CANID</i> } </p>
<p> <i>CANID</i> := <i>ID</i>[<i>:MASK</i>] </p>
<p> <i>ID</i>, <i>MASK</i> := hexadecimal number (i.e. 0x123)</p>
<h2>Caveats</h2>
<p>The ematch syntax uses &#8216;(&#8216; and &#8216;)&#8217; to group expressions. All braces need to be escaped properly to prevent shell commandline from interpreting these directly. </p>
<p> When using the ipset ematch with the &quot;ifb&quot; device, the outgoing device will be the ifb device itself, e.g. &quot;ifb0&quot;. The original interface (i.e. the device the packet arrived on) is treated as the incoming interface.</p>
<h2>EXAMPLE &amp; USAGE</h2>
<p># tc filter add .. basic match &#8230; </p>
<p> # &#8216;cmp(u16 at 3 layer 2 mask 0xff00 gt 20)&#8217; </p>
<p> # &#8216;meta(nfmark gt 24)&#8217; and &#8216;meta(tcindex mask 0xf0 eq 0xf0)&#8217; </p>
<p> # &#8216;nbyte(&quot;ababa&quot; at 12 layer 1)&#8217; </p>
<p> # &#8216;u32(u16 0x1122 0xffff at nexthdr+4)&#8217; </p>
<p> Check if packet source ip address is member of set named <code>bulk</code>: </p>
<p> # &#8216;ipset(bulk src)&#8217; </p>
<p> Check if packet source ip and the interface the packet arrived on is member of &quot;hash:net,iface&quot; set named <code>interactive</code>: </p>
<p> # &#8216;ipset(interactive src,src)&#8217; </p>
<p> Check if packet matches an IPSec state with reqid 1: </p>
<p> # &#8216;ipt(-m policy &#8211;dir in &#8211;pol ipsec &#8211;reqid 1)&#8217;</p>
<h2>Author</h2>
<p>The extended match infrastructure was added by Thomas Graf.</p>
