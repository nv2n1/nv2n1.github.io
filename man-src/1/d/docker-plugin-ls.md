---
title: "docker-plugin-ls(1)"
name: "docker-plugin-ls"
section: "1"
letter: "d"
url: "/docs/linux/man/1-docker-plugin-ls/"
description: "docker-plugin-ls – List plugins"
---

<h2 class="name">NAME</h2>
<p> docker-plugin-ls &#8211; List plugins </p>
<h2>SYNOPSIS</h2>
<p> <code>docker plugin ls [OPTIONS]</code> </p>
<h2>DESCRIPTION</h2>
<p> Lists all the plugins that are currently installed. You can install plugins using the docker plugin install command. You can also filter using the -f or &#8211;filter flag. </p>
<h2>Filters</h2>
<p> Filter output based on these conditions:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;&#8211; enabled=(true|false)&nbsp;&#8211; plugins that are enabled or not<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;&#8211; capability=&nbsp;&#8211; filters plugins based on capabilities&nbsp;(currently volumedriver, networkdriver, ipamdriver, or authz) </p>
<h2>Format</h2>
<p> Pretty-print plugins using a Go template.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;Valid placeholders:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;.ID &#8211; Plugin ID.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;.Name &#8211; Plugin Name.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;.Description &#8211; Plugin description.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;.Enabled &#8211; Whether plugin is enabled or not. </p>
<h2>EXAMPLES</h2>
<h2>Display all plugins</h2>
<dl>
<dt>
<dd>
<pre>
$ docker plugin ls
ID                  NAME                                    DESCRIPTION                         ENABLED
869080b57404        tiborvass/sample-volume-plugin:latest   A sample volume plugin for Docker   true
141bf6c02ddd        vieux/sshfs:latest                      sshFS plugin for Docker             false
</pre>
</dl>
<h2>Display plugins with their ID and names</h2>
<dl>
<dt>
<dd>
<pre><code>
$ docker plugin ls-- format "&#123;&#123;.ID}}: &#123;&#123;.Name}}" 869080b57404 : tiborvass / sample - volume - plugin : latest
</code></pre>
</dl>
<h2>Display enabled plugins</h2>
<dl>
<dt>
<dd>
<pre>
$ docker plugin ls --filter enabled=true
ID                  NAME                                    DESCRIPTION                         ENABLED
869080b57404        tiborvass/sample-volume-plugin:latest   A sample volume plugin for Docker   true
</pre>
</dl>
<h2>Display plugins with volumedriver capability</h2>
<dl>
<dt>
<dd>
<pre><code>
$ docker plugin ls-- filter capability = volumedriver-- format "table &#123;&#123;.ID}}	&#123;&#123;.Name}}" ID Name 869080b57404 tiborvass / sample - volume - plugin : latest
</code></pre>
</dl>
<h2>OPTIONS</h2>
<p> <code>-f</code>, <code>&#8211;filter</code>= <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Provide filter values (e.g. &#8216;enabled=true&#8217;)</p>
<p> <code>&#8211;format</code>=&quot;&quot; <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Pretty-print plugins using a Go template</p>
<p> <code>-h</code>, <code>&#8211;help</code>[=false] <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>help for ls</p>
<p> <code>&#8211;no-trunc</code>[=false] <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Don&#8217;t truncate output</p>
<p> <code>-q</code>, <code>&#8211;quiet</code>[=false] <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Only display plugin IDs</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-docker-plugin/">docker-plugin</a>(1)</code> </p>
<h2>Index</h2>
