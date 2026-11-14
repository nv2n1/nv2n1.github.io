---
title: "rsearch(1)"
name: "rsearch"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rsearch/"
description: "rsearch – Stress test an LDAP server with search operations"
---

<h2 class="name">NAME</h2>
<p> rsearch &#8211; Stress test an LDAP server with search operations </p>
<h2>SYNOPSIS</h2>
<p> <code>rsearch</code> <code>-D</code> binddn <code>-w</code> bindpw <code>-s</code> suffix <code>-f</code> filter [<i>options</i>] </p>
<h2>DESCRIPTION</h2>
<p> Stress tests an LDAP server with search operations. </p>
<h2>OPTIONS</h2>
<p> A summary of options is included below:</p>
<dl>
<dt><code>-H</code></p>
<dd> print Usage (this message)</p>
<dt><code>-h</code> host</p>
<dd> ldap server host (default: localhost)</p>
<dt><code>-p</code> port</p>
<dd> ldap server port (default: 389)</p>
<dt><code>-S</code> scope</p>
<dd> search SCOPE [0,1,or 2] (default: 2)</p>
<dt><code>-b</code></p>
<dd> bind before every operation</p>
<dt><code>-u</code></p>
<dd> don&#8217;t unbind <code>&#8212;</code> just close the connection</p>
<dt><code>-L</code></p>
<dd> set linger <code>&#8212;</code> connection discarded when closed</p>
<dt><code>-N</code></p>
<dd> No operation <code>&#8212;</code> just bind (ignore mdc)</p>
<dt><code>-v</code></p>
<dd> verbose</p>
<dt><code>-y</code></p>
<dd> nodelay</p>
<dt><code>-q</code></p>
<dd> quiet</p>
<dt><code>-l</code></p>
<dd> logging</p>
<dt><code>-m</code></p>
<dd> operaton: modify non-indexed attr (description). <code>-B</code> required</p>
<dt><code>-M</code></p>
<dd> operaton: modify indexed attr (telephonenumber). <code>-B</code> required</p>
<dt><code>-d</code></p>
<dd> operaton: delete. <code>-B</code> required</p>
<dt><code>-c</code></p>
<dd> operaton: compare. <code>-B</code> required</p>
<dt><code>-i</code> file</p>
<dd> name file; used for the search filter</p>
<dt><code>-B</code> file</p>
<dd> [DN and] UID file (use &#8216;-B \?&#8217; to see the format)</p>
<dt><code>-A</code> attrs</p>
<dd> list of attributes for search request</p>
<dt><code>-a</code> file</p>
<dd> list of attributes for search request in a file</p>
<dt> <code>&#8212;</code> (use &#8216;-a \?&#8217; to see the format ; <code>-a</code> &amp; <code>-A</code> are mutually exclusive)</dl>
<dl>
<dt><code>-n</code> number</p>
<dd> (reserved for future use)</p>
<dt><code>-o</code> number</p>
<dd>
<dd>Search time limit, in seconds; (default: 30; no time limit: 0)</p>
<dt><code>-j</code> number</p>
<dd> sample interval, in seconds (default: 10)</p>
<dt><code>-t</code> number</p>
<dd> threads (default: 1)</p>
<dt><code>-T</code> number</p>
<dd> Time limit, in seconds; cmd stops when exceeds &lt;number&gt;</p>
<dt><code>-V</code></p>
<dd> show running average</p>
<dt><code>-C</code> num</p>
<dd> take num samples, then stop</p>
<dt><code>-R</code> num</p>
<dd> drop connection &amp; reconnect every num searches</p>
<dt><code>-x</code></p>
<dd> Use <code>-B</code> file for binding; ignored if <code>-B</code> is not given
</dl>
<h2>AUTHOR</h2>
<p> rsearch was written by the 389 Project.</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to <a rel="nofollow" href="https://fedorahosted.org/389/newticket.">https://fedorahosted.org/389/newticket.</a></p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2001 Sun Microsystems, Inc. Used by permission.<br />
 Copyright &#169; 2008 Red Hat, Inc.<br />
 This manual page was written by Michele Baldessari &lt;michele [at] pupazzo.org&gt;, for the Debian project (but may be used by others).<br />
 This is free software. You may redistribute copies of it under the terms of the Directory Server license found in the LICENSE file of this software distribution. This license is essentially the GNU General Public License version 2 with an exception for plug-in distribution. </p>
<h2>Index</h2>
