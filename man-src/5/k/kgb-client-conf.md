---
title: "kgb-client-conf(5)"
name: "kgb-client-conf"
section: "5"
letter: "k"
url: "/docs/linux/man/5-kgb-client-conf/"
description: "kgb-client.conf — KGB client configuration file"
---

<p>kgb-client.conf &#8212; KGB client configuration file</p>
<h2>Description</h2>
<p><i><a href="/docs/linux/man/1-kgb-client/">kgb-client</a></i>(1) can be configured via command line options and/or via a configuration file (via the <code>&#8211;conf</code> option). Most of the settings can use either way, with command line options overriding settings from the configuration file. </p>
<p> The file format is <font SIZE="-1">YAML.</font> Elaborate example configuration is at the end of this document.</p>
<h2>Server connection configuration</h2>
<h3>repo-id</h3>
<p>Unique project identifier on the server. <code>Mandatory</code>.</p>
<h3>password</h3>
<p>Pass phrase string. Used together with <code>repo-id</code> to authenticate the request to the servers. Per-server configuration overrides this setting.</p>
<h3>timeout</h3>
<p>Request timeout in seconds. Defaults to <tt>15</tt>.</p>
<h3>servers</h3>
<p>A list of maps, describing the servers to try to send ntifications to. Each server map can have the following members:</p>
<dl>
<dt><code>uri</code></p>
<dd>The <font SIZE="-1">URI</font> of the server. Something like <tt>&quot;<a rel="nofollow" href="http://kgb.server.org:port/">http://kgb.server.org:port/</a>&quot;</tt>.</p>
<dt><code>proxy</code></p>
<dd><font SIZE="-1">SOAP</font> proxy to use. Mandatory if using <font SIZE="-1">SOAP</font> protocol. Defaults to to the value of the <code>uri</code> setting, with <tt>&quot;?session=KGB&quot;</tt> appended.</p>
<dt><code>password</code></p>
<dd>Per-server pass phrase. Defaults to the global <code>password</code> setting.</p>
<dt><code>timeout</code></p>
<dd>Timeout of the request. Defaults to the global <code>timeout</code> setting.</dl>
<h3><code>status_dir</code></h3>
<p>Directory to store information about the last successfuly contacted server. If the request is soon after the last contact, the last server is tried first. This way related notifications tend to come out of the same server.</p>
<h2>Content configuration</h2>
<h3><code>branch-and-module-re</code></h3>
<p>A list of regular expressions. These are matched against the path of the modified files and should have two captures in them &#8212; the first capture is for the branch and the second capture is for the module. </p>
<p> This is useful with Subversion repositories where there is a single repository for the project, with all the modules and branches.</p>
<h3><code>module-and-branch-re</code></h3>
<p>Same as <code>branch-and-module-re</code>, but captures are in reverse order &#8212; module first and branch second.</p>
<h3><code>ignore-branch</code></h3>
<p>A name of a branch to ignore. All changes in that branch are sent without branch info. Useful if most of the branches are made in one branch (e.g. trunk, master).</p>
<h3><code>web-link</code></h3>
<p><font SIZE="-1">URL</font> containing information about the commit (e.g. gitweb, viewvcs). <tt>&quot;${commit}&quot;</tt>, <tt>&quot;${branch}&quot;</tt>, <tt>&quot;${module}&quot;</tt> and <tt>&quot;${project}&quot;</tt> in that string are substituted with the commit <font SIZE="-1">ID,</font> the branch name, the module name and the project <font SIZE="-1">ID</font> respectively. </p>
<p> See App::KGB::Client for examples.</p>
<h3><code>short-url-service</code></h3>
<p>The name of the <font SIZE="-1">URL</font> shortening service to use. If given, the service is used to shorten the result of <code>web-link</code> substitution. </p>
<p> See WWW::Shorten for the list of available services. Note that <code>kgb-client</code> comes with an additional service called <tt>&quot;Debli&quot;</tt>, which is primarily useful for clients running on Debian&#8217;s collaboration server, alioth.</p>
<h3><code>single-line-commits</code></h3>
<p>Send only a single line of the commit message to the channel. Possible values: auto|force|off.</p>
<dl>
<dt><code>auto</code></p>
<dd><code>(default)</code> Uses single line notification if the commit log&#8217;s second line is an empty string. Otherwise uses the whole commit log (as if set to <code>off</code>).</p>
<dt><code>force</code></p>
<dd>Uses only the first line of the commit log, ignoring the rest.</p>
<dt><code>off</code></p>
<dd>Uses the whole commit log, ignoring any empty lines.</dl>
<h3><code>use-irc-notices</code></h3>
<p>If set to a true value will make the <font SIZE="-1">IRC</font> bot use <font SIZE="-1">IRC </font><tt>&quot;notice&quot;</tt> messages instead of the ordinary <tt>&quot;privmsg&quot;</tt> messages.</p>
<h3><code>use-color</code></h3>
<p>If set to a false value will make the <font SIZE="-1">IRC</font> bot use no color in the notifications.</p>
<h2>Example Confguration</h2>
<pre> # vim: filetype=yaml
 ---
 repo-id: 'kgb'
 password: 'notknown'
 timeout: 7
 status-dir: '/home/proj/kgb-client/status'
 module-and-branch-re:
 - '^/([^/]+)/(trunk|tags/(?:[^/]+))/'
 - '^/([^/]+)/branches/([^/]+)/'
 - '^/(website)/()'
 web-link: '<a rel="nofollow" href="http://svn.debian.org/viewvc/${project}?view=revision">http://svn.debian.org/viewvc/${project}?view=revision</a>&amp;revision=${commit}'
 # web-link: '<a rel="nofollow" href="http://anonscm.debian.org/gitweb/?p=${project}/${module}.git;a=commitdiff;h=${commit}'">http://anonscm.debian.org/gitweb/?p=${project}/${module}.git;a=commitdiff;h=${commit}'</a>
 #short-url-service: 'Metamark'
 short-url-service: 'Debli'
 ignore-branch: 'trunk'
 use-irc-notices: 0
 use-color: 1
 servers:
 - uri: '<a rel="nofollow" href="http://kgb.server.org:9418/'">http://kgb.server.org:9418/'</a>
 - uri: '<a rel="nofollow" href="http://another.kgb.server.org:9418/'">http://another.kgb.server.org:9418/'</a>
 timeout: 3
 password: 'notknowneither'</pre>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/1-kgb-client/">kgb-client</a></i>(1), App::KGB::Client, WWW::Shorten, WWW::Shorten::Debli, <i><a href="/docs/linux/man/1-kgb-bot/">kgb-bot</a></i>(1)</p>
<h2>Author</h2>
<dl>
<dt>Damyan Ivanov dmn [at] debian.org</p>
<dd></dl>
<h2>COPYRIGHT &amp; LICENSE</h2>
<p>Copyright (C) 2012, 2013 Damyan Ivanov </p>
<p> This program is free software; you can redistribute it and/or modify it under the terms of the <font SIZE="-1">GNU</font> General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. </p>
<p> This program is distributed in the hope that it will be useful, but <font SIZE="-1">WITHOUT ANY WARRANTY</font>; without even the implied warranty of <font SIZE="-1">MERCHANTABILITY</font> or <font SIZE="-1">FITNESS FOR A PARTICULAR PURPOSE. </font> See the <font SIZE="-1">GNU</font> General Public License for more details. </p>
<p> You should have received a copy of the <font SIZE="-1">GNU</font> General Public License along with this program; if not, write to the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, <font SIZE="-1">MA 02110-1301, USA.</font></p>
