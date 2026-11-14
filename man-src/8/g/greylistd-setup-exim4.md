---
title: "greylistd-setup-exim4(8)"
name: "greylistd-setup-exim4"
section: "8"
letter: "g"
url: "/docs/linux/man/8-greylistd-setup-exim4/"
description: "greylistd-setup-exim4 – add/remove support for greylistd in Exim 4"
---

<p>greylistd-setup-exim4 &#8211; add/remove support for greylistd in Exim 4</p>
<h2>Synopsis</h2>
<p><code>greylistd-setup-exim4</code> {<code>add</code>|<code>remove</code>|<code>test</code>} [<i>file acl_name</i>] [<i>-option</i> &#8230;]</p>
<h2>Description</h2>
<p>This utility configures, deconfigures, or tests for greylistd support in the given Exim 4 configuration file and Access Control List (ACL). </p>
<p> If no file or ACL name is supplied, changes are made to the default configuration files and ACLs for your distribution.</p>
<h2>Usage</h2>
<p>The following commands are available:</p>
<dl>
<dt><code>add</code></p>
<dd>Adds greylistd statement(s).</p>
<dt><code>remove</code></p>
<dd>Removes existing greylistd statement(s).</p>
<dt><code>test</code></p>
<dd>Tests for the presence of greylistd statement(s), without making any changes. A zero exit status indicates that the statement(s) exist(s).</dl>
<p> The following options are available:</p>
<dl>
<dt><code>-quiet</code></p>
<dd>Normally, the result of the operation is printed on standard error; this option inhibits output.</p>
<dt><code>-no-fail</code></p>
<dd>Always exit with a zero status, even on failure. If this option is given, only the result of successful operations are printed.</p>
<dt><code>-no-reload</code></p>
<dd>Normally, if any changes were made to the Exim 4 configuration files, <code>greylistd-setup-exim4</code> invokes the Exim 4 init script, telling Exim to reload its configuration files. This option inhibits this behavior.</p>
<dt><code>-netmask=</code><i>size</i></p>
<dd>In the statement that is inserted in the Exim 4 configuration file, the remote host address is one of the items that is passed on to greylistd. This option causes the host address to be filtered through a netmask of the given size first. Useful values are between 16 and 31 for IPv4.</p>
<dt><code>-acltype=</code>{<code>rcpt</code>|<code>data</code>}</p>
<dd>Used in conjunction with the <code>add</code> command to insert a statement suitable for use in an ACL used to validate the SMTP <code>RCPT TO:</code> command or the message <code>DATA</code>, respectively. This is implicit when the supplied ACL name contains either of the substrings &quot;<code>rcpt</code>&quot; or &quot;<code>data</code>&quot; (such as Debian&#8217;s default &quot;<code>acl_check_rcpt</code>&quot; and &quot;<code>acl_check_data</code>&quot; ACLs). Otherwise, this option has to be present for the <code>add</code> command.</dl>
<h2>Examples</h2>
<dl>
<dt><code>greylistd-setup-exim4 add -netmask=24</code></p>
<dd>Adds greylistd statements to any <code>acl_check_rcpt</code> and <code>acl_check_data</code> ACLs found in any of the following files: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&#8211;&nbsp;<wbr>/etc/exim4/exim4.conf.template<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;&nbsp;<wbr>/etc/exim4/conf.d/acl/30_exim4-config_check_rcpt<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;&nbsp;<wbr>/etc/exim4/conf.d/acl/40_exim4-config_check_data </p>
<p> In these statements, the data passed to greylistd includes the host address filtered through a 24-bit netmask, rather than the host&#8217;s unique IP address. This allows for pools of several Mail Sending Agents (MSAs) within a given network to be treated as a single host. </p>
<p> If successful, Exim 4 is told to reload its configuration files. If a statement already exists, nothing happens &#8211; but the program exits unsuccessfully (non-zero return code).</p>
<dt><code>greylistd-setup-exim4 remove -quiet</code></p>
<dd>Remove greylisting support from the above configuration files and ACLs. If greylistd statements exist in these files and ACLs, they are removed, and Exim 4 will reload its configuration files. The exit code indicates whether the statements were present and are now successfully removed; but no results are printed.</p>
<dt><code>greylistd-setup-exim4 add /etc/exim4/exim4.conf.template acl_check_rcpt -no-reload</code></p>
<dd>If no greylistd statements already exists in the <code>acl_check_rcpt</code> ACL in the file <code>/etc/exim4/exim4.conf.template</code>, one is inserted. In this case, the Exim 4 daemon is then NOT told to reload its configuration files.</dl>
<h2>Bugs</h2>
<p>The statement that is inserted by this utility presumes that the Exim 4 configuration comes from Debian&#8217;s &quot;<code>exim4-config</code>&quot; package. Specifically, it makes use of the <code>+relay_from_hosts</code> host list, the <code>+local_domains</code> and <code>+relay_to_domains</code> domain lists, and the <code>acl_local_deny_exceptions</code> ACL. A more generalized approach is on my, ahem, to-do list.</p>
<h2>Author</h2>
<p>This python script and manual page is written by Tor Slettnes, originally for Debian GNU/Linux.</p>
<h2>Copyright</h2>
<p>Copyright &#169; 2004-2005 Tor Slettnes. </p>
<p> This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. </p>
<p> This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. </p>
<p> On a Debian GNU/Linux system, the full text of the GPL is available in /usr/share/common-licenses/GPL. It is also available at: </p>
<p>&nbsp;<wbr><a rel="nofollow" href="http://www.gnu.org/licenses/gpl.html">http://www.gnu.org/licenses/gpl.html</a></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-greylist/">greylist</a></code>(1), <code><a href="/docs/linux/man/8-greylistd/">greylistd</a></code>(8), <code>/usr/share/doc/exim4/spec.txt.gz</code> </p>
