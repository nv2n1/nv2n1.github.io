---
title: "iptables-xml(1)"
name: "iptables-xml"
section: "1"
letter: "i"
url: "/docs/linux/man/1-iptables-xml/"
description: "iptables-xml — Convert iptables-save format to XML"
---

<h2 class="name">NAME</h2>
<p> iptables-xml &#8212; Convert iptables-save format to XML </p>
<h2>SYNOPSIS</h2>
<p> <code>iptables-xml</code> [<code>-c</code>] [<code>-v</code>]</p>
<h2>DESCRIPTION</h2>
<p> <code>iptables-xml</code> is used to convert the output of iptables-save into an easily manipulatable XML format to STDOUT. Use I/O-redirection provided by your shell to write to a file.</p>
<dl>
<dt><code>-c</code>, <code>&#8211;combine</code></p>
<dd> combine consecutive rules with the same matches but different targets. iptables does not currently support more than one target per match, so this simulates that by collecting the targets from consecutive iptables rules into one action tag, but only when the rule matches are identical. Terminating actions like RETURN, DROP, ACCEPT and QUEUE are not combined with subsequent targets.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd> Output xml comments containing the iptables line from which the XML is derived </p>
</dl>
<p> iptables-xml does a mechanistic conversion to a very expressive xml format; the only semantic considerations are for -g and -j targets in order to discriminate between &lt;call&gt; &lt;goto&gt; and &lt;nane-of-target&gt; as it helps xml processing scripts if they can tell the difference between a target like SNAT and another chain. </p>
<p> Some sample output is: </p>
<p> &lt;iptables-rules&gt;<br />
&nbsp;<wbr>&nbsp;&lt;table name=&quot;mangle&quot;&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&lt;chain name=&quot;PREROUTING&quot;&nbsp;policy=&quot;ACCEPT&quot;&nbsp;packet-count=&quot;63436&quot; byte-count=&quot;7137573&quot;&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&lt;rule&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&lt;conditions&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&lt;match&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&lt;p&gt;tcp&lt;/p&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&lt;/match&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&lt;tcp&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&lt;sport&gt;8443&lt;/sport&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&lt;/tcp&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&lt;/conditions&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&lt;actions&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&lt;call&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&lt;check_ip/&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&lt;/call&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&lt;ACCEPT/&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&lt;/actions&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&lt;/rule&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&lt;/chain&gt;<br />
&nbsp;<wbr>&nbsp;&lt;/table&gt; &lt;/iptables-rules&gt; </p>
<p> Conversion from XML to iptables-save format may be done using the iptables.xslt script and xsltproc, or a custom program using libxsltproc or similar; in this fashion: </p>
<p> xsltproc iptables.xslt my-iptables.xml | iptables-restore </p>
<h2>BUGS</h2>
<p> None known as of iptables-1.3.7 release</p>
<h2>AUTHOR</h2>
<p> Sam Liddicott &lt;azez [at] ufomechanic.net&gt;</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-iptables-save/">iptables-save</a></code>(8), <code><a href="/docs/linux/man/8-iptables-restore/">iptables-restore</a></code>(8), <code><a href="/docs/linux/man/8-iptables/">iptables</a></code>(8) </p>
<h2>Index</h2>
