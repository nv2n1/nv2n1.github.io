---
title: "sshfp(1)"
name: "sshfp"
section: "1"
letter: "s"
url: "/docs/linux/man/1-sshfp/"
description: "sshfp – Generate SSHFP DNS records from knownhosts files or ssh-keyscan"
---

<h2 class="name">NAME</h2>
<p> sshfp &#8211; Generate SSHFP DNS records from knownhosts files or ssh-keyscan </p>
<h2>SYNTAX</h2>
<p> sshfp [<code>-k</code> &lt;<i>knownhosts_file</i>&gt;] [<code>-d</code>] [<code>-a</code>] [<code>&#8211;type</code> &lt;algo&gt;] [<code>&#8211;digest</code> &lt;digest&gt;] [&lt;<i>host1</i>&gt; [<i>host2 &#8230;]</i>] </p>
<p> sshfp <code>-s</code> [<code>-p</code> &lt;<i>port</i>&gt;] [<code>-d</code>] [<code>-a</code>] [<code>&#8211;type</code> &lt;algo&gt;] [<code>&#8211;digest</code> &lt;digest&gt;] [<code>-n &lt;nameserver</code>&gt;<i>] &lt;domain1</i>&gt; [<i>domain2</i>] &lt;<i>host1</i>&gt; [<i>host2 &#8230;</i>] &gt;</p>
<h2>DESCRIPTION</h2>
<p> sshfp generates RFC-4255 SSHFP DNS records based on the public keys stored in a known_hosts file, which implies the user has previously trusted this key, or public keys can be obtained by using ssh-keyscan (1). Using ssh-keyscan (1) implies a secure path to connect to the hosts being scanned. It also implies a trust in the DNS to obtain the IP address of the hostname to be scanned. If the nameserver of the domain allows zone tranfers (AXFR), an entire domain can be processed for all its A records.</p>
<h2>OPTIONS</h2>
<p> <code>-s / &#8211;scan</code> &lt;<i>hostname1</i>&gt; [hostname2 &#8230;]</p>
<dl>
<dt>
<dd> Scan hosts or domain for public SSH keys using ssh-keyscan</dl>
<p> <code>-k / &#8211;knownhosts &lt;</code><i>knownhosts_file</i><i>&gt; &lt;</i><i>hostname1</i><i>&gt; [hostname2 &#8230;]</i></p>
<dl>
<dt>
<dd> Obtain public SSH keys from a known_hosts file. Defaults to using ~/.ssh/known_hosts</dl>
<p> <code>-a / &#8211;all</code></p>
<dl>
<dt>
<dd> Scan all hosts in the known_hosts file when used with -k. When used with -s, it will attempt an zone transfer (AXFR) to obtain all A records in the domain specified.</dl>
<p> <code>-d / &#8211;trailing-dot</code></p>
<dl>
<dt>
<dd> Add a trailing dot to the hostname in the SSHFP records. It is not possible to determine whether a known_hosts or dns query is for a FQDN (eg <a rel="nofollow" href="http://www.redhat.com">www.redhat.com</a>) or not (eg www) or not (unless -d domainname -a is used, in which case a trailing dot is always appended). Non-FQDN get their domainname appended through /etc/resolv.conf These non-FQDN will happen when using a non-FQDN (eg sshfp -k www) or known_hosts entries obtained by running ssh <a href="http://www.sub">www.sub</a> where .domain.com is implied. When -d is used, all hostnames not ending with a dot, that at least contain two parts in their hostname (eg <a href="http://www.sub">www.sub</a> but not www get a trailing dot. Note that the output of sshfp can also just be manually editted for trailing dots.</dl>
<p> <code>-o / &#8211;output</code> &lt;<i>filename</i>&gt;</p>
<dl>
<dt>
<dd> Write to filename instead of stdout</dl>
<p> <code>-p / &#8211;port</code> &lt;<i>portnumber</i>&gt;</p>
<dl>
<dt>
<dd> Use portnumber for scanning. Note that portnumbers do NOT appear in SSHFP records.</dl>
<p> <code>-h / &#8211;help</code></p>
<dl>
<dt>
<dd> Output help information and exit.</dl>
<p> <code>-v / &#8211;version</code></p>
<dl>
<dt>
<dd> Output version information and exit.</dl>
<p> <code>-q / &#8211;quiet</code></p>
<dl>
<dt>
<dd> Output less miscellany to stderr</dl>
<h2>FILES</h2>
<p> ~/.ssh/known_hosts</p>
<h2>REQUIREMENTS</h2>
<p> sshfp requires python-dns (m[blue]<code><a rel="nofollow" href="http://www.pythondns.org">http://www.pythondns.org</a></code>m[]) </p>
<p> Fedora: yum install python-dns </p>
<p> Debian: apt-get install python-dnspython</p>
<h2>BUGS</h2>
<p> if a domain contains non-working glue A records, then ssh-keyscan aborts instead of skipping the single broken entry. </p>
<p> This program can look up hashed hostnames in a known_hosts file if a recent-enough ssh-keygen is present</p>
<h2>EXAMPLES</h2>
<p> typical usage: </p>
<p> sshfp (implies -k -a) </p>
<p> sshfp -a -d (implies -k) </p>
<p> sshfp -k bofh.nohats.ca (from known_hosts) </p>
<p> sshfp -s bofh.nohats.ca (from a scan to the host) </p>
<p> sshfp -k ~paul/.ssh/known_hosts bofh.nohats.ca <a rel="nofollow" href="http://www.openswan.org">www.openswan.org</a> -o /tmp/mysshfp.txt </p>
<p> sshfp -a -d -d nohats.ca -n ns0.nohats.ca &gt;&gt; /var/named/primary/nohats.ca</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ssh-keyscan/">ssh-keyscan</a></code>(1)<code><a href="/docs/linux/man/1-ssh/">ssh</a></code>(1)<code><a href="/docs/linux/man/1-tlsa/">tlsa</a></code>(1) and RFC-4255</p>
<h2>AUTHORS</h2>
<p> Paul Wouters &lt;pwouters [at] redhat.com&gt;, Jacob Appelbaum &lt;jacob [at] appelbaum.net&gt;, James Brown &lt;jbrown [at] yelp.com&gt;</p>
<h2>COPYRIGHT</h2>
<p> Copyright 2006-2010 Xelerance Corporation </p>
<p> Copyright 2012 Paul Wouters </p>
<p> This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. See &lt;m[blue]<code><a rel="nofollow" href="http://www.fsf.org/copyleft/gpl.txt">http://www.fsf.org/copyleft/gpl.txt</a></code>m[]&gt;. </p>
<p> This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License (file COPYING in the distribution) for more details. </p>
<h2>Index</h2>
