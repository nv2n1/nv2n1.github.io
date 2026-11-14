---
title: "oidentd-conf(5)"
name: "oidentd-conf"
section: "5"
letter: "o"
url: "/docs/linux/man/5-oidentd-conf/"
description: "oidentd.conf – The oidentd configuration file."
---

<p>oidentd.conf &#8211; The oidentd configuration file.</p>
<h2>Description</h2>
<p>The <code>oidentd</code> configuration file is used to specify the amount of control users have over the responses <code>oidentd</code> returns upon successful lookups for connections owned by them. </p>
<p> The <code>$HOME/.oidentd.conf</code> file allows a user to specify what ident response will be returned for specific connections.</p>
<h2>/etc/oidentd.conf SYNTAX</h2>
<dl>
<dt><code>USER DIRECTIVE</code></p>
<dd>The <code>oidentd.conf</code> file consists of 0 or more <i>user</i> directives. The <i>user</i> directive is used to grant capabilities on a per-user basis. </p>
<p> The <i>user</i> directive has the following syntax: </p>
<pre><i>default</i> {
 &lt;<i>range directive</i>&gt;
}
OR
<i>user</i> &lt;username&gt; {
 &lt;<i>range directive</i>&gt;
}</pre>
<p>The <i>default</i> directive matches all users for whom rules are not defined. There should only be one <i>default</i> directive, and it should be the first statement in the file. All entries for users defined after the default definition will inherit the capabilities of the default user. Capabilities can then be allowed, denied, or forced on a per-user basis by way of the <i>user</i> statement followed by the username of the user to whom the properties that follow will apply.</p>
<dt><code>RANGE DIRECTIVE</code></p>
<dd>The body of a <i>user</i> directive consists of 1 or more <i>range</i> directives. </p>
<p> The <i>range</i> directive is used to specify a host/port range for which a set of capabilities is binding. A range directive consists of 1 or more statements of the following form: </p>
<pre>default {
 &lt;capability directive&gt;
}
OR
<i>to</i> &lt;host&gt; <i>lport</i> &lt;lport&gt; <i>from</i> &lt;host&gt; <i>fport</i> &lt;fport&gt; {
 &lt;capability directive&gt;
}</pre>
<p>The <i>default</i> directive matches all host/port pairs for which rules are not defined. There should only be one <i>default</i> directive, and it should be the first statement in the block. </p>
<p> Anywhere from 1 to all 4 of the <i>to</i>, <i>lport</i>, <i>from</i>, and <i>fport</i> parameters may be specified. </p>
<p> The <i>to</i> parameter is used to specify the address to which a connection is made. </p>
<p> The <i>from</i> parameter is used to specify the address from which a connection originates. It may be useful to specify this address when a system has more than 1 IP address. </p>
<p> The <i>to</i> and <i>from</i> parameters take either an IP address or a hostname argument. </p>
<p> The <i>lport</i> parameter is used to specify the local port from which a connection originates. </p>
<p> The <i>fport</i> parameter is used to specify the destination port of a connection. </p>
<p> The <i>lport</i> and <i>fport</i> parameters take either a port or a port range. Ports can be specified numerically (e.g. 113) or by giving a service name (e.g. &quot;auth&quot;). Ranges of ports take the form &lt;starting port&gt;:&lt;ending port&gt;. The ending port is optional. If the ending port is omitted, the range is taken to be any port greater than or equal to the starting port. </p>
<p> The omission of any of the <i>to</i>, <i>lport</i>, <i>from</i> and <i>fport</i> parameters acts like a wildcard for that parameter. For example, the statement &quot;from localhost&quot; matches all connections from localhost on any port to any host on any port.</p>
<dt><code>CAPABILITY DIRECTIVE</code></p>
<dd>The body of a <i>range</i> directive consists of one or more capability directives. </p>
<p> Capabilities are used to assign or deny privileges to specific users. Valid capabilities inside user directives are <i>allow</i>, <i>deny</i>, and<i>force</i>. </p>
<p> The capability directive consists of one or more statements of the form: </p>
<p> <i>allow</i> OR <i>deny</i> OR <i>force</i> &lt;capability&gt;. </p>
<p> The capability argument must be one of the capabilities described in the <code>capability</code> section below. </p>
<p> The force action takes a third argument when the capability is <i>reply</i>. For example, <i>force reply &quot;randomuser&quot;</i>.</dl>
<h2>$HOME/.oidentd.conf SYNTAX</h2>
<p>A user&#8217;s .oidentd.conf configuration file may contain 0 or more of the following statements: </p>
<pre><i>global</i> {
 &lt;capability&gt;
}
OR
&lt;range directive&gt; {
 &lt;capability&gt;
}</pre>
<p>The <i>global</i> directive acts as a wildcard, matching all connections, so if used at all, the global directive should be the first entry in the file and should be used only once. Use is permitted anywhere in the file and infinitely many times, however it doesn&#8217;t make much sense to use it in this manner. </p>
<p> The range directive has the same syntax and semantics as the range directive in the <code>/etc/oidentd.conf</code> file. See above for a description. </p>
<p> Valid capabilities are <i>reply</i>, <i>random</i>, <i>numeric</i>, <i>random_numeric</i>, and <i>hide</i>. Descriptions can be found below.</p>
<h2>Capabilities</h2>
<dl>
<dt><code>spoof</code></p>
<dd>Allow spoofed ident responses; allow the user to specify a string of her choosing as the ident reply. The only restriction on the spoofed response is that it must not be the username of another user. When a user spoofs her ident reply, the login name of the user is recorded along with the forged reply.<br />
 This capability does not apply to the <i>force</i> action.</p>
<dt><code>spoof_all</code></p>
<dd>Allow the usernames of other users to be used as ident responses.<br />
 This capability does not apply to the <i>force</i> action.</p>
<dt><code>spoof_privport</code></p>
<dd>Allow ident replies to be spoofed on privileged ports (ports lower than 1024).<br />
 This capability does not apply to the <i>force</i> action.</p>
<dt><code>reply</code> &lt;string&gt; [&lt;string1&gt; &#8230; &lt;stringN&gt;]</p>
<dd>Reply to successful ident lookups with the ident response specified in &lt;string&gt;. If more than one string parameter is given, one of the strings will be selected randomly. </p>
<p> In a user&#8217;s <code>$HOME/.oidentd.conf</code> file, up to 20 strings may be specified for a <code>reply</code> statement. </p>
<p> In the <code>/etc/oidentd.conf</code> file, there is no limitation on the number of strings that may be specified. </p>
<p> The strings must be quoted strings (e.g. &quot;string&quot;). Strings may contain the following escape characters: </p>
<dl>
<dd>
<dl>
<dt><code>
</code></p>
<dd>new line</p>
<dt><code>	</code></p>
<dd>tab</p>
<dt><code></code></p>
<dd>carriage return</p>
<dt><code></code></p>
<dd>backspace</p>
<dt><code></code></p>
<dd>vertical tab</p>
<dt><code></code></p>
<dd>form feed</p>
<dt><code></code></p>
<dd>alert (bell)</p>
<dt><code></code></p>
<dd>escape</p>
<dt><code>\</code></p>
<dd>backslash</p>
<dt><code>\</code><i>NNN</i></p>
<dd>The character with the ASCII code <i>NNN</i> in the octal base system.</p>
<dt><code>
