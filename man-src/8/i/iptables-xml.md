---
title: "iptables-xml(8)"
name: "iptables-xml"
section: "8"
letter: "i"
url: "/docs/linux/man/8-iptables-xml/"
description: "iptables-xml — Convert iptables-save format to XML"
---

<p>iptables-xml &#8212; Convert iptables-save format to XML</p>
<h2>Synopsis</h2>
<p><code>iptables-xml</code> [<code>-c</code>] [<code>-v</code>]</p>
<h2>Description</h2>
<p><code>iptables-xml</code> is used to convert the output of iptables-save into an easily manipulatable XML format to STDOUT. Use I/O-redirection provided by your shell to write to a file.</p>
<dl>
<dt><code>-c</code>, <code>&#8211;combine</code></p>
<dd>combine consecutive rules with the same matches but different targets. iptables does not currently support more than one target per match, so this simulates that by collecting the targets from consecutive iptables rules into one action tag, but only when the rule matches are identical. Terminating actions like RETURN, DROP, ACCEPT and QUEUE are not combined with subsequent targets.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd>Output xml comments containing the iptables line from which the XML is derived  iptables-xml does a mechanistic conversion to a very expressive xml format; the only semantic considerations are for -g and -j targets in order to discriminate between &lt;call&gt; &lt;goto&gt; and &lt;nane-of-target&gt; as it helps xml processing scripts if they can tell the difference between a target like SNAT and another chain. Some sample output is: &lt;iptables-rules&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&lt;table name=&quot;mangle&quot;&gt;<br />
&nbsp;<wbr>&lt;chain name=&quot;PREROUTING&quot;&nbsp;<wbr>policy=&quot;ACCEPT&quot;&nbsp;<wbr>packet-count=&quot;63436&quot; byte-count=&quot;7137573&quot;&gt;<br />
&lt;rule&gt;<br />
&nbsp;<wbr>&lt;conditions&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&lt;match&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&lt;p&gt;tcp&lt;/p&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&lt;/match&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&lt;tcp&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&lt;sport&gt;8443&lt;/sport&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&lt;/tcp&gt;<br />
&nbsp;<wbr>&lt;/conditions&gt;<br />
&nbsp;<wbr>&lt;actions&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&lt;call&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&lt;check_ip/&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&lt;/call&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&lt;ACCEPT/&gt;<br />
&nbsp;<wbr>&lt;/actions&gt;<br />
&lt;/rule&gt;<br />
&nbsp;<wbr>&lt;/chain&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&lt;/table&gt; &lt;/iptables-rules&gt; Conversion from XML to iptables-save format may be done using the iptables.xslt script and xsltproc, or a custom program using libxsltproc or similar; in this fashion: xsltproc iptables.xslt my-iptables.xml | iptables-restore </p>
<h2>Bugs</h2>
<p>None known as of iptables-1.3.7 release</p>
<h2>Author</h2>
<p>Sam Liddicott &lt;azez [at] ufomechanic.net&gt;</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-iptables-save/">iptables-save</a></code>(8), <code><a href="/docs/linux/man/8-iptables-restore/">iptables-restore</a></code>(8), <code><a href="/docs/linux/man/8-iptables/">iptables</a></code>(8) </p>
