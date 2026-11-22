---

title: "rsearch(1)"
name: "rsearch"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rsearch/"
description: "rsearch – Stress test an LDAP server with search operations"
---

<p> rsearch &#8211; Stress test an LDAP server with search operations </p>
<h2>SYNOPSIS</h2>
<p> <code>rsearch</code> <code>-D</code> binddn <code>-w</code> bindpw <code>-s</code> suffix <code>-f</code> filter [<i>options</i>] </p>
<h2>DESCRIPTION</h2>
<p> Stress tests an LDAP server with search operations. </p>
<h2>OPTIONS</h2>
<p> A summary of options is included below:</p>
<dl>
<dt><code>-H</code></dt>
<dd> print Usage (this message)</dd>
<dt><code>-h</code> host</dt>
<dd> ldap server host (default: localhost)</dd>
<dt><code>-p</code> port</dt>
<dd> ldap server port (default: 389)</dd>
<dt><code>-S</code> scope</dt>
<dd> search SCOPE [0,1,or 2] (default: 2)</dd>
<dt><code>-b</code></dt>
<dd> bind before every operation</dd>
<dt><code>-u</code></dt>
<dd> don&#8217;t unbind <code>&#8212;</code> just close the connection</dd>
<dt><code>-L</code></dt>
<dd> set linger <code>&#8212;</code> connection discarded when closed</dd>
<dt><code>-N</code></dt>
<dd> No operation <code>&#8212;</code> just bind (ignore mdc)</dd>
<dt><code>-v</code></dt>
<dd> verbose</dd>
<dt><code>-y</code></dt>
<dd> nodelay</dd>
<dt><code>-q</code></dt>
<dd> quiet</dd>
<dt><code>-l</code></dt>
<dd> logging</dd>
<dt><code>-m</code></dt>
<dd> operaton: modify non-indexed attr (description). <code>-B</code> required</dd>
<dt><code>-M</code></dt>
<dd> operaton: modify indexed attr (telephonenumber). <code>-B</code> required</dd>
<dt><code>-d</code></dt>
<dd> operaton: delete. <code>-B</code> required</dd>
<dt><code>-c</code></dt>
<dd> operaton: compare. <code>-B</code> required</dd>
<dt><code>-i</code> file</dt>
<dd> name file; used for the search filter</dd>
<dt><code>-B</code> file</dt>
<dd> [DN and] UID file (use &#8216;-B \?&#8217; to see the format)</dd>
<dt><code>-A</code> attrs</dt>
<dd> list of attributes for search request</dd>
<dt><code>-a</code> file</dt>
<dd> list of attributes for search request in a file</dd>
<dt> <code>&#8212;</code> (use &#8216;-a \?&#8217; to see the format ; <code>-a</code> &amp; <code>-A</code> are mutually exclusive)</dt></dl>
<dl>
<dt><code>-n</code> number</dt>
<dd> (reserved for future use)</dd>
<dt><code>-o</code> number</dt>
<dd>
</dd><dd>Search time limit, in seconds; (default: 30; no time limit: 0)</dd>
<dt><code>-j</code> number</dt>
<dd> sample interval, in seconds (default: 10)</dd>
<dt><code>-t</code> number</dt>
<dd> threads (default: 1)</dd>
<dt><code>-T</code> number</dt>
<dd> Time limit, in seconds; cmd stops when exceeds &lt;number&gt;</dd>
<dt><code>-V</code></dt>
<dd> show running average</dd>
<dt><code>-C</code> num</dt>
<dd> take num samples, then stop</dd>
<dt><code>-R</code> num</dt>
<dd> drop connection &amp; reconnect every num searches</dd>
<dt><code>-x</code></dt>
<dd> Use <code>-B</code> file for binding; ignored if <code>-B</code> is not given
</dd></dl>
<h2>AUTHOR</h2>
<p> rsearch was written by the 389 Project.</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to <a rel="nofollow" href="https://fedorahosted.org/389/newticket.">https://fedorahosted.org/389/newticket.</a></p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2001 Sun Microsystems, Inc. Used by permission.<br/>
 Copyright &#169; 2008 Red Hat, Inc.<br/>
 This manual page was written by Michele Baldessari &lt;michele [at] pupazzo.org&gt;, for the Debian project (but may be used by others).<br/>
 This is free software. You may redistribute copies of it under the terms of the Directory Server license found in the LICENSE file of this software distribution. This license is essentially the GNU General Public License version 2 with an exception for plug-in distribution. </p>
