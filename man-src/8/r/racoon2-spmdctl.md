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
<dd>set, get, and delete DNS server address(es) for spmd DNS proxy function.</p>
<dd>add IPsec Policy.</p>
<dd>get spmd statistics.</p>
<dt>The following options are available:</p>
<dd>
<dt><code>-d</code></p>
<dd>Display all messages which exchanged with spmd.</p>
<dt><code>-f FILE</code></p>
<dd>Specify racoon2 configuration file name <code>FILE</code>.</p>
<dt>The following <code>COMMAND</code>s are available:</p>
<dd>
<dt><code>ns add ADDRESS</code></p>
<dd>
<dd>Add DNS server address <code>ADDRESS</code> to spmd DNS server list. </p>
<dt><code>ns delete ADDRESS</code></p>
<dd>
<dd>Delete DNS server address <code>ADDRESS</code> from spmd DNS server list. </p>
<dt><code>ns list</code></p>
<dd>
<dd>Show DNS server address(es) in spmd DNS Server list. Top line is currently used. </p>
<dt><code>policy add SELECTOR_INDEX LIFETIME {transport|tunnel| SP_SRC_IPADDR SP_DST_IPADDR [SA_SRC_IP_ADDR SA_DST_IPADDR]</code></p>
<dd>
<dd>Request spmd to add IPsec Security Policy to in-kernel IPsec Security Policy DataBase(SPD).</p>
<dd><code>SELECTOR_INDEX</code> is a selector index string which described in racoon2 configuration file.</p>
<dd><code>LIFETIME</code> is the lifetime duration(sec) for this IPsec Security Policy.</p>
<dd><code>transport|tunnel</code> <code>transport</code> means this IPsec Security Policy is transport mode. <code>tunnel</code> means tunnel mode.</p>
<dd><code>SP_SRC_IPADDR</code> is the source IP address for this IPsec Security Policy.</p>
<dd><code>SP_DST_IPADDR</code> is the destination IP address for this IPsec Security Policy.</p>
<dd><code>SA_SRC_IPADDR</code> is the IPsec SA source IP address associated with this IPsec Security Policy. This is only required in tunnel mode.</p>
<dd><code>SA_DST_IPADDR</code> is the IPsec SA destination IP address associated with this IPsec Security Policy. This is only required in tunnel mode. </p>
<dt><code>policy delete SELECTOR_INDEX</code></p>
<dd>
<dd>Request spmd to delete IPsec Security Policy to in-kernel IPsec Security DataBase(SPD).</p>
<dd><code>SELECTOR_INDEX</code> is a selector index string which described in racoon2 configuration file. </p>
<dt><code>policy show</code></p>
<dd>
<dd>Dump IPsec Security Policies. If &#8216;selector=&#8217; field is empty in a displayed IPsec Security Policy entry, this Policy is out of racoon2 management. </p>
<dt><code>interactive</code></p>
<dd>Connect to spmd and just login. You can talk to spmd directly. This command is available when you compiled spmdctl with DEBUG_SPMD. </p>
<dt><code>status</code></p>
<dd>Show spmd statistics.</dl>
<h2>Files</h2>
<p><i>racoon2.conf</i></p>
<h2>Authors</h2>
<p>WIDE Project, racoon2 project &lt;<a rel="nofollow" href="http://www.racoon2.wide.ad.jp/">http://www.racoon2.wide.ad.jp/</a>&gt;</p>
<h2>Bugs</h2>
<p><code>policy add</code> command currently doesn&#8217;t support tunnel mode.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-spmd/">spmd</a>(8) <a href="/docs/linux/man/5-racoon2-conf/">racoon2.conf</a>(5) <a href="/docs/linux/man/7-racoon2/">racoon2</a>(7). </p>
