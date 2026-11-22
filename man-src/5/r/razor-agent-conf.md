---
title: "razor-agent-conf(5)"
name: "razor-agent-conf"
section: "5"
letter: "r"
url: "/docs/linux/man/5-razor-agent-conf/"
description: "\"razor-agent.conf\" – Configuration file for Razor Agents"
---

<p>&quot;razor-agent.conf&quot; &#8211; Configuration file for Razor Agents</p>
<h2>Description</h2>
<p><tt>&quot;razor-agent.conf&quot;</tt> is a configuration file read by the razor agents, which include <i><a href="/docs/linux/man/1-razor-check/">razor-check</a></i>(1), <i><a href="/docs/linux/man/1-razor-admin/">razor-admin</a></i>(1), <i><a href="/docs/linux/man/1-razor-report/">razor-report</a></i>(1), and <i><a href="/docs/linux/man/1-razor-revoke/">razor-revoke</a></i>(1). The format is &#8220;attribute = value&#8221; pairs, one pair per line. Lines that begin with `#&#8217; are treated as comments.</p>
<h2>Attributes</h2>
<p>Following attributes can be specified:</p>
<dl>
<dt><code>razorhome</code></dt>
<dd>Directory where Razor Agents look for files. All files in <tt>&quot;razor-agent.conf&quot;</tt> without a full path will be relative to <tt>&quot;razorhome&quot;</tt>. The default is <tt>&quot;/etc/razor/&quot;</tt> for root, and <tt>&quot;~/.razor/&quot;</tt> for every other user. If <tt>&quot;razorhome&quot;</tt> does not exist, it will be created.</dd>
<dt><code>logfile</code></dt>
<dd>Log file for the Razor Agents. The default is <tt>&quot;razor-agent.log&quot;</tt>.</dd>
<dt><code>debuglevel</code></dt>
<dd>Controls the amount of messages written to logfile. It is an integer between 0 and 20. For Example, a value of <tt>1</tt> logs only startup and error messages, <tt>5</tt> includes every transaction with the server, and <tt>14</tt> is extremely verbose information intended for debugging use only. NOTE: <tt>15</tt> and higher create debug files on your filesystem &#8212; do not use unless you know what you are doing. The default is <tt>5</tt>.</dd>
<dt><code>identity</code></dt>
<dd>Specify an identify file to use for storing a newly registered identity during <i><a href="/docs/linux/man/1-razor-admin/">razor-admin</a></i>(1). For <i><a href="/docs/linux/man/1-razor-report/">razor-report</a></i>(1) and <i><a href="/docs/linux/man/1-razor-revoke/">razor-revoke</a></i>(1), use this identity when authenticating with Razor Servers. If not specified, <tt>&quot;&lt;razorhome&gt;/identity-&lt;user&gt;&quot;</tt> is used.</dd>
<dt><code>listfile_nomination</code></dt>
<dd>File where Razor Nomination Servers are listed, in order of closest TCP ping time. Nomination Servers are used by <i><a href="/docs/linux/man/1-razor-report/">razor-report</a></i>(1) and <i><a href="/docs/linux/man/1-razor-revoke/">razor-revoke</a></i>(1). This file is created automatically. The default is <tt>&quot;servers.nomination.lst&quot;</tt>.</dd>
<dt><code>listfile_catalogue</code></dt>
<dd>File where Razor Catalogue Servers are listed, in order of closest TCP ping time. Catalogue Servers are used by <i><a href="/docs/linux/man/1-razor-check/">razor-check</a></i>(1). This file is created automatically. The default is <tt>&quot;servers.catalogue.lst&quot;</tt>.</dd>
<dt><code>listfile_discovery</code></dt>
<dd>File where Razor Discovery Servers are listed, in random order. This file is created automatically using DNS. The default is <tt>&quot;servers.discovery.lst&quot;</tt>.</dd>
<dt><code>rediscovery_wait_dns</code></dt>
<dd>Max time in seconds Razor Agents will wait before computing a new <tt>&quot;listfile_discovery&quot;</tt> using DNS. The default is <tt>604800</tt>, which is 7 days.</dd>
<dt><code>rediscovery_wait</code></dt>
<dd>Max time in seconds Razor Agents will wait before computing a new <tt>&quot;listfile_nomination&quot;</tt> and a new <tt>&quot;listfile_catalogue&quot;</tt>. The default is <tt>172800</tt>, which is 2 days.</dd>
<dt><code>turn_off_discovery</code></dt>
<dd>Turns off closest host discovery. When set to 1, <tt>&quot;listfile_catalogue&quot;</tt> and <tt>&quot;listfile_nomination&quot;</tt> will not be updated and <tt>&quot;listfile_discovery&quot;</tt> is not read or updated. The default is <tt>0</tt>.</dd>
<dt><code>ignorelist</code></dt>
<dd>Automatically ignore mailing list posts. If set to <tt>0</tt>, mailing list posts will be handled like all other mail. The default is <tt>0</tt>.</dd>
<dt><code>whitelist</code></dt>
<dd>Name of whitelist file. Razor Agents can consult a whitelist of addresses and SHA1 hashes before checking a mail with Razor Servers. If the address/hash is found on the whitelist, the mail is marked `not spam&#8217;, without checking against the server. The format of the whitelist can be found in <i><a href="/docs/linux/man/5-razor-whitelist/">razor-whitelist</a></i>(5) manpage. The default is <tt>&quot;razor-whitelist&quot;</tt>.</dd>
<dt><code>min_cf</code></dt>
<dd>When checking spam, the server optionally returns a spam confidence value ranging from 0 (not confident) to 100 (absolutely or 100% confident). To be considered spam, the server&#8217;s spam confidence value must be greater than or equal to <tt>&quot;min_cf&quot;</tt>. <tt>&quot;min_cf&quot;</tt> can be a number or an expression containing ac, the average confidence published by a Razor Server. Examples: 0, 60, 100, ac, ac + 10, ac &#8211; 20. If an expression evaluates to less than 0 it becomes 0, likewise those greater than 100 become 100. The default is <tt>&quot;ac&quot;</tt>.</dd>
<dt><code>report_headers</code></dt>
<dd>When reporting spam, the entire email (headers and body) is sent to a Razor Nomination Server. When set to <tt>0</tt>, all the headers are removed except headers beginning with <tt>&quot;Content-&quot;</tt> before sending, and a special header beginning with <tt>&quot;X-Razor2&quot;</tt> is added to note this action. The default is <tt>1</tt>.</dd></dl>
<h2>Authors</h2>
<p>Vipul Ved Prakash, &lt;mail [at] vipul.net&gt; and Chad Norwood &lt;chad [at] samo.org&gt;</p>
<h2>See Also</h2>
<p><i>razor-agents</i>(1), <i><a href="/docs/linux/man/1-razor-check/">razor-check</a></i>(1), <i><a href="/docs/linux/man/1-razor-admin/">razor-admin</a></i>(1), <i><a href="/docs/linux/man/1-razor-report/">razor-report</a></i>(1), <i><a href="/docs/linux/man/1-razor-revoke/">razor-revoke</a></i>(1), <i><a href="/docs/linux/man/5-razor-whitelist/">razor-whitelist</a></i>(5) </p>
