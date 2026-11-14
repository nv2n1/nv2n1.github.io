---
title: "sa-awl(1)"
name: "sa-awl"
section: "1"
letter: "s"
url: "/docs/linux/man/1-sa-awl/"
description: "sa-awl – examine and manipulate SpamAssassin’s auto-whitelist db"
---

<h2 class="name">NAME</h2>
<p> sa-awl &#8211; examine and manipulate SpamAssassin&#8217;s auto-whitelist db </p>
<h2>SYNOPSIS</h2>
<p> <code>sa-awl</code> [&#8211;clean] [&#8211;min n] [dbfile]</p>
<h2>DESCRIPTION</h2>
<p> Check or clean a SpamAssassin auto-whitelist (<font SIZE="-1">AWL</font>) database file. </p>
<p> The name of the file is specified after any options, as <tt>&quot;dbfile&quot;</tt>. The default is <tt>&quot;$HOME/.spamassassin/auto-whitelist&quot;</tt>.</p>
<h2>OPTIONS</h2>
<dl>
<dt>&#8211;clean</p>
<dd> Clean out infrequently-used <font SIZE="-1">AWL</font> entries. The <tt>&quot;--min&quot;</tt> switch can be used to select the threshold at which entries are kept or deleted.</p>
<dt>&#8211;min n</p>
<dd> Select the threshold at which entries are kept or deleted when <tt>&quot;--clean&quot;</tt> is used. The default is <tt>2</tt>, so entries that have only been seen once are deleted.</dl>
<h2>OUTPUT</h2>
<p> The output looks like this: </p>
<pre>
     AVG  (TOTSCORE/COUNT)  --  EMAIL|ip=IPBASE
</pre>
<p> For example: </p>
<pre><code>
0.0(0.0 / 7)-- dawson[at] example.com | ip = 208.192 21.8(43.7 / 2)-- mcdaniel_2s2000[at] example.com | ip = 200.106
</code></pre>
<p> <tt>&quot;AVG&quot;</tt> is the average score; <tt>&quot;TOTSCORE&quot;</tt> is the total score of all mails seen so far; <tt>&quot;COUNT&quot;</tt> is the number of messages seen from that sender; <tt>&quot;EMAIL&quot;</tt> is the sender&#8217;s email address, and <tt>&quot;IPBASE&quot;</tt> is the <font SIZE="-1"><code>AWL</code></font><code> base </code><font SIZE="-1"><code>IP</code></font><code> address</code>. </p>
<p> <font SIZE="-1"><code>AWL</code></font><code> base </code><font SIZE="-1"><code>IP</code></font><code> address</code> is a way to identify the sender&#8217;s <font SIZE="-1">IP</font> address they frequently send from, in an approximate way, but remaining hard for spammers to spoof. The algorithm is as follows: </p>
<pre>
  - take the last Received header that contains a public IP address -- namely
    one which is not in private, unrouted IP space.
  - chop off the last two octets, assuming that the user may be in an ISP's
    dynamic address pool.
</pre>
<h2>Index</h2>
