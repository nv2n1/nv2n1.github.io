---
title: "fusesmb(5)"
name: "fusesmb"
section: "5"
letter: "f"
url: "/docs/linux/man/5-fusesmb/"
description: "fusesmb.conf – the configuration file for fusesmb"
---

<p>fusesmb.conf &#8211; the configuration file for <code>fusesmb</code></p>
<h2>File Format</h2>
<p>The file consists of sections and parameters. A section begins with the name of the section in square brackets and continues until the next section begins. Sections contain parameters of the form: <i>name</i> = <i>value</i>. </p>
<p> The file is line-based &#8211; that is, each newline-terminated line represents either a comment, a section name or a parameter. </p>
<p> Section and parameter names are not case sensitive. </p>
<p> Only the first equals sign in a parameter is significant. Whitespace before or after the first equals sign is discarded. Leading, trailing and internal whitespace in section and parameter names is irrelevant. Leading and trailing whitespace in a parameter value is discarded. Internal whitespace within a parameter value is retained verbatim. </p>
<p> Any line beginning with a semicolon (&#8220;<code>;</code>&#8221;) or a hash (&#8220;<code>#</code>&#8221;) character is ignored, as are lines containing only whitespace.</p>
<h2>Special Sections</h2>
<p><code>fusesmb.conf</code> can contain the following sections:</p>
<dl>
<dt>The <code>[global]</code> section</p>
<dd>Section for global parameters.</p>
<dt>The <code>[ignore]</code> section</p>
<dd>Section for specifying servers and/or workgroups that should not be listed.</p>
<dt>The <code>[/</code><i>SERVER</i><code>]</code> section</p>
<dd>Section for server-specific settings. The section name should start with a slash &#8220;<code>/</code>&#8221; and not end with a slash.</p>
<dt>The <code>[/</code><i>SERVER</i><code>/</code><i>SHARE</i><code>]</code></p>
<dd>Section for share-specific settings. The section name should start with a slash followed by the server name followed by a slash ending on the share name. It should not end with a slash. </p>
</dl>
<h2>Explanation Of Each Parameter</h2>
<p>This chapter explains each possible option. The section names &#8211; specified between parentheses after each option &#8211; shows the applicable sections for this option. For example: ( [global] ) specifies that this option is only possible for the section [global].</p>
<dl>
<dt><code>ignore</code> ( [/SERVER] )</p>
<dd>Ignore this server. Possible values are: true, false, 1 and 0. </p>
<p> Example: <i>ignore</i> = <i>true</i></p>
<dt><code>interval</code> ( [global] )</p>
<dd>Interval for scanning the network for shares. Value is a number that specifies the network scanning interval in minutes. If the value is smaller or equal to zero the network is not scanned. </p>
<p> Example: <i>interval</i> = <i>20</i></p>
<dt><code>password</code> ( [global], [/SERVER], [/SERVER/SHARE] )</p>
<dd>Password. Value is string containing the password. </p>
<p> Example: <i>password</i> = <i>secret</i></p>
<dt><code>servers</code> ( [ignore] )</p>
<dd>Servers to ignore. Value is each server to ignore separated by a comma. </p>
<p> Example: <i>servers</i> = <i>SERVER1, SERVER2, SERVER3</i> </p>
<dt><code>showhiddenshares</code> ( [global], [/SERVER] )</p>
<dd>Show hidden shares. Possible values are: true, false, 1 and 0. </p>
<p> Example: <i>showhiddenshares</i> = <i>false</i> </p>
<dt><code>timeout</code> ( [global] )</p>
<dd>Connection timeout in seconds. A server after this timeout is considered offline. Values smaller than 2 seconds are ignored. </p>
<p> Example: <i>timeout</i> = <i>10</i> </p>
<dt><code>username</code> ( [global], [/SERVER], [/SERVER/SHARE] )</p>
<dd>Username. Value is string containing the username. </p>
<p> Example: <i>username</i> = <i>johndoe</i> </p>
<dt><code>workgroups</code> ( [ignore] )</p>
<dd>Workgroups to ignore. Value is each workgroup to ignore separated by a comma. </p>
<p> Example: <i>workgroups</i> = <i>WORKGROUP1, WORKGROUP2</i> </p>
</dl>
<h2>Example</h2>
<pre>; Global settings
<code>[global]</code>
; Default username and password
username=user
password=totallysecret
; List hidden shares
showhiddenshares=true
; Connection timeout in seconds
timeout = 10
;Interval for updating new shares in minutes
interval = 10
; Section for servers and/or workgroups to ignore
<code>[ignore]</code>
servers=SERVER,SERVER2,SERVER3
workgroups=WORKGROUP,WG2
; Share-specific settings
<code>[/SERVER/SHARE]</code>
username=john
password=doe
; Server-specific settings
<code>[/SERVER]</code>
username=jane
password=doe
showhiddenshares=true
ignore=true</pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-fusesmb/">fusesmb</a></code>(1) </p>
<h2>Author</h2>
<p>Vincent Wagelaar &lt;vincent [at] ricardis.tudelft.nl&gt;.</p>
