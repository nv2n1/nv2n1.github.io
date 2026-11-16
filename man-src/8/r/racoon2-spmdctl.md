---
title: "racoon2-spmdctl(8)"
name: "racoon2-spmdctl"
section: "8"
letter: "r"
url: "/docs/linux/man/8-racoon2-spmdctl/"
description: "spmdctl – Control spmd"
---

<p><code>spmdctl</code> &#8211; Control spmd</p>
<h2>Synopsis</h2>
<p><code>spmdctl</code> [<i>option</i>] <i>COMMAND</i></p>
<h2>Description</h2>
<p><code>spmdctl</code> connects to the spmd interface which is specified in racoon2 configuration file, and requests operation<i></i> to spmd.<br />
 Available operations are:</p>
<dl>
<dd>set, get, and delete DNS server address(es) for spmd DNS proxy function.</dd>
<dd>add IPsec Policy.</dd>
<dd>get spmd statistics.</dd>
<dt>The following options are available:</dt>
<dd>
</dd><dt><code>-d</code></dt>
<dd>Display all messages which exchanged with spmd.</dd>
<dt><code>-f FILE</code></dt>
<dd>Specify racoon2 configuration file name <code>FILE</code>.</dd>
<dt>The following <code>COMMAND</code>s are available:</dt>
<dd>
</dd><dt><code>ns add ADDRESS</code></dt>
<dd>
</dd><dd>Add DNS server address <code>ADDRESS</code> to spmd DNS server list. </dd>
<dt><code>ns delete ADDRESS</code></dt>
<dd>
</dd><dd>Delete DNS server address <code>ADDRESS</code> from spmd DNS server list. </dd>
<dt><code>ns list</code></dt>
<dd>
</dd><dd>Show DNS server address(es) in spmd DNS Server list. Top line is currently used. </dd>
<dt><code>policy add SELECTOR_INDEX LIFETIME {transport|tunnel| SP_SRC_IPADDR SP_DST_IPADDR [SA_SRC_IP_ADDR SA_DST_IPADDR]</code></dt>
<dd>
</dd><dd>Request spmd to add IPsec Security Policy to in-kernel IPsec Security Policy DataBase(SPD).</dd>
<dd><code>SELECTOR_INDEX</code> is a selector index string which described in racoon2 configuration file.</dd>
<dd><code>LIFETIME</code> is the lifetime duration(sec) for this IPsec Security Policy.</dd>
<dd><code>transport|tunnel</code> <code>transport</code> means this IPsec Security Policy is transport mode. <code>tunnel</code> means tunnel mode.</dd>
<dd><code>SP_SRC_IPADDR</code> is the source IP address for this IPsec Security Policy.</dd>
<dd><code>SP_DST_IPADDR</code> is the destination IP address for this IPsec Security Policy.</dd>
<dd><code>SA_SRC_IPADDR</code> is the IPsec SA source IP address associated with this IPsec Security Policy. This is only required in tunnel mode.</dd>
<dd><code>SA_DST_IPADDR</code> is the IPsec SA destination IP address associated with this IPsec Security Policy. This is only required in tunnel mode. </dd>
<dt><code>policy delete SELECTOR_INDEX</code></dt>
<dd>
</dd><dd>Request spmd to delete IPsec Security Policy to in-kernel IPsec Security DataBase(SPD).</dd>
<dd><code>SELECTOR_INDEX</code> is a selector index string which described in racoon2 configuration file. </dd>
<dt><code>policy show</code></dt>
<dd>
</dd><dd>Dump IPsec Security Policies. If &#8216;selector=&#8217; field is empty in a displayed IPsec Security Policy entry, this Policy is out of racoon2 management. </dd>
<dt><code>interactive</code></dt>
<dd>Connect to spmd and just login. You can talk to spmd directly. This command is available when you compiled spmdctl with DEBUG_SPMD. </dd>
<dt><code>status</code></dt>
<dd>Show spmd statistics.</dd></dl>
<h2>Files</h2>
<p><i>racoon2.conf</i></p>
<h2>Authors</h2>
<p>WIDE Project, racoon2 project &lt;<a rel="nofollow" href="http://www.racoon2.wide.ad.jp/">http://www.racoon2.wide.ad.jp/</a>&gt;</p>
<h2>Bugs</h2>
<p><code>policy add</code> command currently doesn&#8217;t support tunnel mode.</p>
<h2>See Also</h2>
<p>spmd(8) racoon2.conf(5) racoon2(7). </p>
