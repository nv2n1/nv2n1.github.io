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
<p>The protocol used by the KGB collaboration service is based on JSON-RPC (&lt;<a rel="nofollow" href="http://json-rpc.org/">http://json-rpc.org/</a>&gt;). </p>
<p> KGB service helps collaboration by relaying notifications about commits in a version control system to IRC. It consists of client, hooked to the version control system which sends information about changes to the server, and a server, listening for client&#8217;s notifications and relaying them on configured IRC channels.</p>
<h2>Authentication</h2>
<p>Message content is authenticated by using two HTTP headers. The <code>X-KGB-Project</code> header must contain the project ID, as defined in server&#8217;s configuration. The <code>X-KGB-Auth</code> header must contain a SHA1 hash (in hexadecimal notation) calculated over the shared secret, the project ID and the JSON-encoded message. </p>
<p> Upon receiving the HTTP request the server calculates the hash using the supplied project ID, the server copy of the shared secret for that project and the content of the HTTP request. If the hash matches the one provided in the <code>X-KGB-Auth</code> header, the authentication succeeds and the request is processed. Otherwise an error is returned.</p>
<h2>Methods</h2>
<h3>commit_v4 <i>arguments</i></h3>
<p>This method takes information about a single commit and relays it to IRC. <i>arguments</i> is a map with the members described below. Any additional members are ignored.</p>
<dl>
<dt><code>commit_id</code> <i>string</i></dt>
<dd>A string identifying the commit in the version control system. Git (short) hash, Subversion revision number, this kind of thing.</dd>
<dt><code>rev_prefix</code> <i>string</i></dt>
<dd>A string to prepend to the commit ID when displaying on IRC. <tt>&quot;r&quot;</tt> is particularly useful for Subversion repositories.</dd>
<dt><code>author</code> <i>string</i></dt>
<dd>A string representing the commit author.</dd>
<dt><code>branch</code> <i>string</i></dt>
<dd>A string representing the commit branch.</dd>
<dt><code>module</code> <i>string</i></dt>
<dd>A string representing the commit module or sub-project.</dd>
<dt><code>commit_log</code> <i>string</i></dt>
<dd>The commit message.</dd>
<dt><code>changes</code> <i>list of strings</i></dt>
<dd>List of changes files/directories in the commit. Each string is a path, optionaly prepended with <tt>&quot;(A)&quot;</tt> for added paths, <tt>&quot;(M)&quot;</tt> for modified paths and <tt>&quot;(D)&quot;</tt> for deleted paths. If no prefix is given modification is assumed. An additional plus sign flags property changes (Specific to Subversion term), e.g. <tt>&quot;(M+)&quot;</tt>.</dd>
<dt><code>extra</code> <i>map</i></dt>
<dd>A map with additional parameters. Currently supported members are:</dd>
<dl>
<dd>
</dd><dl>
<dt><code>web_link</code></dt>
<dd>A URL with commit details (e.g. gitweb or viewvc).</dd>
<dt><code>use_irc_notices</code></dt>
<dd>A flag whether to use IRC notices instead of regular messages.</dd>
<dt><code>use_color</code></dt>
<dd>A flag whether to use colors when sending commit notifications. Defaults to 1.</dd></dl>
</dl>
<dl>
<dd></dd></dl>
</dl>
<h3>relay_message <i>message</i></h3>
<p>This method takes only one string argument which is the message to relay to IRC. There are no restrictions or requirements to the message content, which is relayed verbatim to project&#8217;s IRC channels.</p>
<h3>ERRORS</h3>
<p><i>Errors reported on </i><i>HTTP</i><i> level</i> </p>
<p> Authentication errors use HTTP code <tt>401</tt>, while other errors &#8212; bad or missing headers and problems with the JSON data use HTTP code <tt>400</tt>. </p>
<p> The error text is in the reason phrase of the HTTP status line (see RFC 2616, section 6.1). </p>
<p> <i>Errors reported on JSON-RPC level</i> </p>
<p> After successful authentication and decoding of the JSON request, all the errors are reported as mandated by the JSON-RPC specification.</p>
<h2>Author</h2>
<dl>
<dt>Damyan Ivanov dmn [at] debian.org</dt>
<dd></dd></dl>
<h2>COPYRIGHT &amp; LICENSE</h2>
<p>Copyright (C) 2012 Damyan Ivanov </p>
<p> This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. </p>
<p> This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details. </p>
<p> You should have received a copy of the GNU General Public License along with this program; if not, write to the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.</p>
