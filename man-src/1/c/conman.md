---

title: "conman(1)"
name: "conman"
section: "1"
letter: "c"
url: "/docs/linux/man/1-conman/"
description: "conman – ConMan client"
---

<p> <code>conman</code> [<i>OPTION</i>]&#8230; [<i>CONSOLE</i>]&#8230; </p>
<p> <code>conman</code> is a program for connecting to remote consoles being managed by <code>conmand</code>. Console names can be separated by spaces and/or commas. Globbing is used by default to match console names against the configuration, but regular expression matching can be enabled with the &#8216;<code>-r</code>&#8216; option. </p>
<p> <code>conman</code> supports three modes of console access: monitor (read-only), interactive (read-write), and broadcast (write-only). If neither the &#8216;<code>-m</code>&#8216; (monitor) nor &#8216;<code>-b</code>&#8216; (broadcast) options are specified, the console session is opened in interactive mode. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-b</code></dt>
<dd> Broadcast to multiple consoles (write-only). Data sent by the client will be copied to all specified consoles in parallel, but console output will not be sent back to the client. This option can be used in conjunction with &#8216;<code>-f</code>&#8216; or &#8216;<code>-j</code>&#8216;.</dd>
<dt><code>-d </code><i>destination</i></dt>
<dd> Specify the location of the <code>conmand</code> daemon, overriding the default [127.0.0.1:7890]. This location may contain a hostname or IP address, and be optionally followed by a colon and port number.</dd>
<dt><code>-e </code><i>character</i></dt>
<dd> Specify the client escape character, overriding the default [<code>&amp;</code>].</dd>
<dt><code>-f</code></dt>
<dd> Specify that write-access to the console should be &quot;forced&quot;, thereby stealing the console away from existing clients having write privileges. The original clients are informed by <code>conmand</code> of who perpetrated the theft as their connections are terminated.</dd>
<dt><code>-F </code><i>file</i></dt>
<dd> Read console names/patterns from file. Only one console name may be specified per line. Leading and trailing whitespace, blank lines, and comments (i.e., lines beginning with a &#8216;#&#8217;) are ignored.</dd>
<dt><code>-h</code></dt>
<dd> Display a summary of the command-line options.</dd>
<dt><code>-j</code></dt>
<dd> Specify that write-access to the console should be &quot;joined&quot;, thereby sharing the console with existing clients having write privileges. The original clients are informed by <code>conmand</code> that a new client has been granted write privileges.</dd>
<dt><code>-l </code><i>file</i></dt>
<dd> Log console session output to file.</dd>
<dt><code>-L</code></dt>
<dd> Display license information.</dd>
<dt><code>-m</code></dt>
<dd> Monitor a console (read-only).</dd>
<dt><code>-q</code></dt>
<dd> Query <code>conmand</code> for consoles matching the specified names/patterns. Output from this query can be saved to file for use with the &#8216;<code>-F</code>&#8216; option.</dd>
<dt><code>-Q</code></dt>
<dd> Enable quiet-mode, suppressing informational messages. This mode can be toggled within a console session via the &#8216;<code>&amp;Q</code>&#8216; escape.</dd>
<dt><code>-r</code></dt>
<dd> Match console names via regular expressions instead of globbing.</dd>
<dt><code>-v</code></dt>
<dd> Enable verbose mode.</dd>
<dt><code>-V</code></dt>
<dd> Display version information. </dd>
</dl>
<h2>ESCAPE CHARACTERS</h2>
<p> The following escapes are supported and assume the default escape character [<code>&amp;</code>]:</p>
<dl>
<dt><code>&amp;?</code></dt>
<dd> Display a list of currently available escapes.</dd>
<dt><code>&amp;.</code></dt>
<dd> Terminate the connection.</dd>
<dt><code>&amp;&amp;</code></dt>
<dd> Send a single escape character.</dd>
<dt><code>&amp;B</code></dt>
<dd> Send a &quot;serial-break&quot; to the remote console.</dd>
<dt><code>&amp;E</code></dt>
<dd> Toggle echoing of client input.</dd>
<dt><code>&amp;F</code></dt>
<dd> Switch from read-only to read-write via a &quot;force&quot;.</dd>
<dt><code>&amp;I</code></dt>
<dd> Display information about the connection.</dd>
<dt><code>&amp;J</code></dt>
<dd> Switch from read-only to read-write via a &quot;join&quot;.</dd>
<dt><code>&amp;L</code></dt>
<dd> Replay up the the last 4KB of console output. This escape requires the console device to have logging enabled in the <code>conmand</code> configuration.</dd>
<dt><code>&amp;M</code></dt>
<dd> Switch from read-write to read-only.</dd>
<dt><code>&amp;Q</code></dt>
<dd> Toggle quiet-mode to display/suppress informational messages.</dd>
<dt><code>&amp;R</code></dt>
<dd> Reset the node associated with this console. This escape requires a &quot;resetcmd&quot; to be specified in the <code>conmand</code> configuration.</dd>
<dt><code>&amp;Z</code></dt>
<dd> Suspend the client. </dd>
</dl>
<h2>ENVIRONMENT</h2>
<p> The following environment variables override the default settings.</p>
<dl>
<dt><font SIZE="-1">CONMAN_HOST</font></dt>
<dd> Specifies the hostname or IP address at which to contact <code>conmand</code>, but may be overridden by the &#8216;<code>-d</code>&#8216; command-line option. A port number separated by a colon may follow the hostname (i.e., <i>host:port</i>), although the CONMAN_PORT environment variable takes precedence. If not set, the default host [127.0.0.1] will be used.</dd>
<dt><font SIZE="-1">CONMAN_PORT</font></dt>
<dd> Specifies the port on which to contact <code>conmand</code>, but may be overridden by the &#8216;<code>-d</code>&#8216; command-line option. If not set, the default port [7890] will be used.</dd>
<dt><font SIZE="-1">CONMAN_ESCAPE</font></dt>
<dd> The first character of this variable specifies the escape character, but may be overridden by the &#8216;<code>-e</code>&#8216; command-line option. If not set, the default escape character [<code>&amp;</code>] will be used. </dd>
</dl>
<h2>SECURITY</h2>
<p> The client/server communications are not yet encrypted. </p>
<h2>AUTHOR</h2>
<p> Chris Dunlap &lt;cdunlap [at] llnl.gov&gt; </p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2007-2011 Lawrence Livermore National Security, LLC.<br />
 Copyright (C) 2001-2007 The Regents of the University of California. </p>
<p> ConMan is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/5-conman-conf/">conman.conf</a></code>(5), <code><a href="/docs/linux/man/8-conmand/">conmand</a></code>(8). </p>
<p> <code><a rel="nofollow" href="http://conman.googlecode.com/">http://conman.googlecode.com/</a></code> </p>
