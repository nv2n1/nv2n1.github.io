---
title: "kgb-protocol(7)"
name: "kgb-protocol"
section: "7"
letter: "k"
url: "/docs/linux/man/7-kgb-protocol/"
description: "KGB_protocol – specification of the client-server communication protocol"
---

<p>KGB_protocol &#8211; specification of the client-server communication protocol</p>
<h2>Description</h2>
<p>The protocol used by the <font SIZE="-1">KGB</font> collaboration service is based on JSON-RPC (&lt;<a rel="nofollow" href="http://json-rpc.org/">http://json-rpc.org/</a>&gt;). </p>
<p> <font SIZE="-1">KGB</font> service helps collaboration by relaying notifications about commits in a version control system to <font SIZE="-1">IRC.</font> It consists of client, hooked to the version control system which sends information about changes to the server, and a server, listening for client&#8217;s notifications and relaying them on configured <font SIZE="-1">IRC</font> channels.</p>
<h2>Authentication</h2>
<p>Message content is authenticated by using two <font SIZE="-1">HTTP</font> headers. The <code>X-KGB-Project</code> header must contain the project <font SIZE="-1">ID,</font> as defined in server&#8217;s configuration. The <code>X-KGB-Auth</code> header must contain a <font SIZE="-1">SHA1</font> hash (in hexadecimal notation) calculated over the shared secret, the project <font SIZE="-1">ID</font> and the JSON-encoded message. </p>
<p> Upon receiving the <font SIZE="-1">HTTP</font> request the server calculates the hash using the supplied project <font SIZE="-1">ID,</font> the server copy of the shared secret for that project and the content of the <font SIZE="-1">HTTP</font> request. If the hash matches the one provided in the <code>X-KGB-Auth</code> header, the authentication succeeds and the request is processed. Otherwise an error is returned.</p>
<h2>Methods</h2>
<h3>commit_v4 <i>arguments</i></h3>
<p>This method takes information about a single commit and relays it to <font SIZE="-1">IRC. </font><i>arguments</i> is a map with the members described below. Any additional members are ignored.</p>
<dl>
<dt><code>commit_id</code> <i>string</i></p>
<dd>A string identifying the commit in the version control system. Git (short) hash, Subversion revision number, this kind of thing.</p>
<dt><code>rev_prefix</code> <i>string</i></p>
<dd>A string to prepend to the commit <font SIZE="-1">ID</font> when displaying on <font SIZE="-1">IRC. </font><tt>&quot;r&quot;</tt> is particularly useful for Subversion repositories.</p>
<dt><code>author</code> <i>string</i></p>
<dd>A string representing the commit author.</p>
<dt><code>branch</code> <i>string</i></p>
<dd>A string representing the commit branch.</p>
<dt><code>module</code> <i>string</i></p>
<dd>A string representing the commit module or sub-project.</p>
<dt><code>commit_log</code> <i>string</i></p>
<dd>The commit message.</p>
<dt><code>changes</code> <i>list of strings</i></p>
<dd>List of changes files/directories in the commit. Each string is a path, optionaly prepended with <tt>&quot;(A)&quot;</tt> for added paths, <tt>&quot;(M)&quot;</tt> for modified paths and <tt>&quot;(D)&quot;</tt> for deleted paths. If no prefix is given modification is assumed. An additional plus sign flags property changes (Specific to Subversion term), e.g. <tt>&quot;(M+)&quot;</tt>.</p>
<dt><code>extra</code> <i>map</i></p>
<dd>A map with additional parameters. Currently supported members are:</p>
<dl>
<dd>
<dl>
<dt><code>web_link</code></p>
<dd>A <font SIZE="-1">URL</font> with commit details (e.g. gitweb or viewvc).</p>
<dt><code>use_irc_notices</code></p>
<dd>A flag whether to use <font SIZE="-1">IRC</font> notices instead of regular messages.</p>
<dt><code>use_color</code></p>
<dd>A flag whether to use colors when sending commit notifications. Defaults to 1.</dl>
</dl>
<dl>
<dd></dl>
</dl>
<h3>relay_message <i>message</i></h3>
<p>This method takes only one string argument which is the message to relay to <font SIZE="-1">IRC.</font> There are no restrictions or requirements to the message content, which is relayed verbatim to project&#8217;s <font SIZE="-1">IRC</font> channels.</p>
<h3><font SIZE="-1">ERRORS</font></h3>
<p><i>Errors reported on </i><font SIZE="-1"><i>HTTP</i></font><i> level</i> </p>
<p> Authentication errors use <font SIZE="-1">HTTP</font> code <tt>401</tt>, while other errors &#8212; bad or missing headers and problems with the <font SIZE="-1">JSON</font> data use <font SIZE="-1">HTTP</font> code <tt>400</tt>. </p>
<p> The error text is in the reason phrase of the <font SIZE="-1">HTTP</font> status line (see <font SIZE="-1">RFC 2616,</font> section 6.1). </p>
<p> <i>Errors reported on JSON-RPC level</i> </p>
<p> After successful authentication and decoding of the <font SIZE="-1">JSON</font> request, all the errors are reported as mandated by the JSON-RPC specification.</p>
<h2>Author</h2>
<dl>
<dt>Damyan Ivanov dmn [at] debian.org</p>
<dd></dl>
<h2>COPYRIGHT &amp; LICENSE</h2>
<p>Copyright (C) 2012 Damyan Ivanov </p>
<p> This program is free software; you can redistribute it and/or modify it under the terms of the <font SIZE="-1">GNU</font> General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. </p>
<p> This program is distributed in the hope that it will be useful, but <font SIZE="-1">WITHOUT ANY WARRANTY</font>; without even the implied warranty of <font SIZE="-1">MERCHANTABILITY</font> or <font SIZE="-1">FITNESS FOR A PARTICULAR PURPOSE. </font> See the <font SIZE="-1">GNU</font> General Public License for more details. </p>
<p> You should have received a copy of the <font SIZE="-1">GNU</font> General Public License along with this program; if not, write to the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, <font SIZE="-1">MA 02110-1301, USA.</font></p>
