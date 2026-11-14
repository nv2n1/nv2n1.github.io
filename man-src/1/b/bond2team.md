---
title: "bond2team(1)"
name: "bond2team"
section: "1"
letter: "b"
url: "/docs/linux/man/1-bond2team/"
description: "bond2team — Converts bonding configuration to team"
---

<h2>NAME</h2>
<p> bond2team &#8212; Converts bonding configuration to team</p>
<h2>SYNOPSIS</h2>
<p> <code>bond2team</code> [options]</p>
<h2>DESCRIPTION</h2>
<p> bond2team is a tool to convert bonding options to team trying as much as possible to keep the original functionality. </p>
<p> The resulting files are saved in a temporary directory using ifcfg style by default. In the case of converting an ifcfg file, it translates the bonding options to team, preserving all other options. In that case, it converts the respective slave ifcfg files to team port, preserving all their other options too. In case of converting from given bonding options in the command line, the tool can use the specified ports as team ports.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;master &lt;interface&gt;</code></p>
<dd> Specify the interface name or ifcfg file to convert. If the interface name is specified, the tool will look at /etc/sysconfig/network-scripts/ for the respective ifcfg file.</p>
<dt><code>&#8211;rename &lt;interface&gt;</code></p>
<dd> This is a convenient option to replace the original interface name by the specified name. For instance, if &#8211;master specifies bond0, it is possible to use &#8211;rename team0 to change the final interface name to team0.</p>
<dt><code>&#8211;ifcfg</code></p>
<dd> Set the output format to ifcfg config style. [default]</p>
<dt><code>&#8211;json</code></p>
<dd> Set the output format to JSON style. See <code><a href="/docs/linux/man/5-teamd-conf/">teamd.conf</a></code>(5) for further details.</p>
<dt><code>&#8211;bonding_opts &#8216;&lt;bonding options&gt;&#8217;</code></p>
<dd> Specify the bonding options to be converted instead of reading them from the ifcfg file.</p>
<dt><code>&#8211;port &lt;interface&gt;</code></p>
<dd> Set the specified interface as a team port.</p>
<dt><code>&#8211;configdir &lt;directory&gt;</code></p>
<dd> Change the ifcfg configuration path from /etc/sysconfig/network-scripts to the specified &lt;directory&gt;.</p>
<dt><code>&#8211;outputdir &lt;directory&gt;</code></p>
<dd> Set the output directory to &lt;directory&gt;.</p>
<dt><code>&#8211;stdout</code></p>
<dd> Print the result to the screen instead of writing to files.</p>
<dt><code>&#8211;debug</code></p>
<dd> Increase the debugging level.</p>
<dt><code>&#8211;quiet</code></p>
<dd> Disallow any messages to be printed to console.</p>
<dt><code>&#8211;version</code></p>
<dd> Print tool version to console and exit.</p>
<dt><code>&#8211;help</code></p>
<dd> Print help text to console and exit.</p>
<dt><code>&#8211;examples</code></p>
<dd> Print common usage examples to console and exit.</dl>
<h2>EXAMPLES</h2>
<p> To convert the current &#8216;bond0&#8217; ifcfg configuration to team ifcfg:</p>
<dl>
<dt>
<pre>
<dd># bond2team --master bond0
</pre>
</dl>
<p> To convert the current &#8216;bond0&#8217; ifcfg configuration to team ifcfg renaming the interface name to &#8216;team0&#8217;. <code>Caution</code> : firewall rules, alias interfaces, etc., that might be tied to the original interface name can break after the renaming because the tool will only change the ifcfg file, nothing else. </p>
<pre>
# bond2team --master bond0 --rename team0
</pre>
<p> To convert given bonding parameters with ports without any ifcfg: </p>
<pre><code>
#bond2team-- bonding_opts 'mode=1 miimon=500 primary=eth1 primary_reselect=0' --port eth1-- port eth2-- port eth3-- port eth4
</code></pre>
<p> For more examples, see the option <code>&#8211;examples.</code></p>
<h2>CAVEATS</h2>
<p> The tool will not convert any other configuration which might be tied to the current setup. For instance, firewall rules, alias interfaces, bridges, and so on.</p>
<h2>AUTHOR</h2>
<p> Flavio Leitner is the original author of the tool. Jiri Pirko is the original author and current maintainer of libteam.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-teamd/">teamd</a></code>(8), <code><a href="/docs/linux/man/8-teamdctl/">teamdctl</a></code>(8), <code><a href="/docs/linux/man/5-teamd-conf/">teamd.conf</a></code>(5), <code><a href="/docs/linux/man/8-teamnl/">teamnl</a></code>(8) </p>
<h2>Index</h2>
