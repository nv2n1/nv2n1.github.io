---
title: "collectd-email(5)"
name: "collectd-email"
section: "5"
letter: "c"
url: "/docs/linux/man/5-collectd-email/"
---

collectd-email - Documentation of collectd's &quot;email plugin&quot;

<h2>Synopsis</h2>

<pre> # See <a HREF="//www.systutorials.com/docs/linux/man/5-collectd.conf/">collectd.conf</a>(5)
 LoadPlugin email
 # ...
 &lt;Plugin email&gt;
 SocketGroup &quot;collectd&quot;
 SocketPerms &quot;0770&quot;
 MaxConns 5
 &lt;/Plugin&gt;</pre>

<h2>Description</h2>

The <tt>&quot;email plugin&quot;</tt> opens an UNIX-socket over which one can submit email statistics, such as the number of ``ham'', ``spam'', ``virus'', etc. mails received/handled, spam scores and matched spam checks. 

 This plugin is intended to be used with the Mail::SpamAssassin::Plugin::Collectd SpamAssassin-plugin which is included in <i>contrib/</i>, but is of course not limited to that use.

<h2>Operation</h2>

This plugin collects data indirectly by providing a UNIX-socket that external programs can connect to. A simple line based protocol is used to communicate with the plugin:
<dl><dt>&bull;
<dd>E-Mail type (e.g. ``ham'', ``spam'', ``virus'', ...) and size (bytes): 

 <pre> e:&lt;type&gt;:&lt;size&gt;</pre>If <tt>&quot;size&quot;</tt> is less than or equal to zero, <tt>&quot;size&quot;</tt> is ignored.
<dt>&bull;
<dd>Spam score: 

 <pre> s:&lt;value&gt;</pre><dt>&bull;
<dd>Successful spam checks (e.g. ``<font SIZE="-1">BAYES_99'', ``SUBJECT_DRUG_GAP_C'', ...</font>): 

 <pre> c:&lt;type1&gt;[,&lt;type2&gt;,...]</pre>Each line is limited to 256 characters (including the newline character). Longer lines will be ignored.</dl>

<h2>See Also</h2>

<i><a HREF="/docs/linux/man/1-collectd/">collectd</a></i>(1), <i><a HREF="/docs/linux/man/5-collectd-conf/">collectd.conf</a></i>(5)

<h2>Author</h2>

The <tt>&quot;email plugin&quot;</tt> has been written by Sebastian Harl &lt;sh at tokkee.org&gt;. 

 The SpamAssassin-plugin has been written by Alexander Wirt &lt;formorer at formorer.de&gt;. 

 This manpage has been written by Florian Forster &lt;octo at collectd.org&gt;.
