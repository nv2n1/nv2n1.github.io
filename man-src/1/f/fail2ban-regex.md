---
title: "fail2ban-regex(1)"
name: "fail2ban-regex"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fail2ban-regex/"
description: "fail2ban-regex – test Fail2ban \"failregex\" option"
---

<h2>NAME</h2>
<p> fail2ban-regex &#8211; test Fail2ban &quot;failregex&quot; option</p>
<h2>SYNOPSIS</h2>
<p> <code>fail2ban-regex</code> [<i>,OPTIONS/</i>] <i>,&lt;LOG&gt; &lt;REGEX&gt; /</i>[<i>,IGNOREREGEX/</i>]</p>
<h2>DESCRIPTION</h2>
<p> Fail2Ban reads log file that contains password failure report and bans the corresponding IP addresses using firewall rules. </p>
<p> This tools can test regular expressions for &quot;fail2ban&quot;.</p>
<h3>LOG:</h3>
<dl>
<dt>string</p>
<dd> a string representing a log line</p>
<dt>filename</p>
<dd> path to a log file (<i>,/var/log/auth.log/</i>)</p>
<dt>&quot;systemd-journal&quot;</p>
<dd> search systemd journal (systemd-python required)</dl>
<h3>REGEX:</h3>
<dl>
<dt>string</p>
<dd> a string representing a &#8216;failregex&#8217;</p>
<dt>filename</p>
<dd> path to a filter file (filter.d/sshd.conf)</dl>
<h3>IGNOREREGEX:</h3>
<dl>
<dt>string</p>
<dd> a string representing an &#8216;ignoreregex&#8217;</p>
<dt>filename</p>
<dd> path to a filter file (filter.d/sshd.conf)</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;version</code></p>
<dd> show program&#8217;s version number and exit</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> show this help message and exit</p>
<dt><code>-d</code> DATEPATTERN, <code>&#8211;datepattern</code>=<i>,DATEPATTERN/</i></p>
<dd> set custom pattern used to match date/times</p>
<dt><code>-e</code> ENCODING, <code>&#8211;encoding</code>=<i>,ENCODING/</i></p>
<dd> File encoding. Default: system locale</p>
<dt><code>-r</code>, <code>&#8211;raw</code></p>
<dd> Raw hosts, don&#8217;t resolve dns</p>
<dt><code>-L</code> MAXLINES, <code>&#8211;maxlines</code>=<i>,MAXLINES/</i></p>
<dd> maxlines for multi-line regex</p>
<dt><code>-m</code> JOURNALMATCH, <code>&#8211;journalmatch</code>=<i>,JOURNALMATCH/</i></p>
<dd> journalctl style matches overriding filter file. &quot;systemd-journal&quot; only</p>
<dt><code>-l</code> LOG_LEVEL, <code>&#8211;log-level</code>=<i>,LOG_LEVEL/</i></p>
<dd> Log level for the Fail2Ban logger to use</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd> Be verbose in output</p>
<dt><code>-D</code>, <code>&#8211;debuggex</code></p>
<dd> Produce debuggex.com urls for debugging there</p>
<dt><code>&#8211;print-no-missed</code></p>
<dd> Do not print any missed lines</p>
<dt><code>&#8211;print-no-ignored</code></p>
<dd> Do not print any ignored lines</p>
<dt><code>&#8211;print-all-matched</code></p>
<dd> Print all matched lines</p>
<dt><code>&#8211;print-all-missed</code></p>
<dd> Print all missed lines, no matter how many</p>
<dt><code>&#8211;print-all-ignored</code></p>
<dd> Print all ignored lines, no matter how many</p>
<dt><code>-t</code>, <code>&#8211;log-traceback</code></p>
<dd> Enrich log-messages with compressed tracebacks</p>
<dt><code>&#8211;full-traceback</code></p>
<dd> Either to make the tracebacks full, not compressed (as by default)</dl>
<h2>AUTHOR</h2>
<p> Written by Cyril Jaquier &lt;cyril.jaquier [at] fail2ban.org&gt;. Many contributions by Yaroslav O. Halchenko and Steven Hiscocks.</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to <a rel="nofollow" href="https://github.com/fail2ban/fail2ban/issues">https://github.com/fail2ban/fail2ban/issues</a></p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2004-2008 Cyril Jaquier, 2008- Fail2Ban Contributors<br />
 Copyright of modifications held by their respective authors. Licensed under the GNU General Public License v2 (GPL).</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-fail2ban-client/">fail2ban-client</a>(1) <a href="/docs/linux/man/1-fail2ban-server/">fail2ban-server</a>(1) </p>
<h2>Index</h2>
