---
title: "pw-cli(1)"
name: "pw-cli"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pw-cli/"
description: "pw-cli – The PipeWire Command Line Interface"
---

<h2 class="name">NAME</h2>
<p> pw-cli &#8211; The PipeWire Command Line Interface </p>
<h2>SYNOPSIS</h2>
<pre>
<code>pw-cli</code> [<i>command</i>]
</pre>
<h2>DESCRIPTION</h2>
<p> Interact with a PipeWire instance. </p>
<p> When a command is given, <code>pw-cli</code> will execute the command and exit </p>
<p> When no command is given, <code>pw-cli</code> starts an interactive session with the default PipeWire instance <i>pipewire-0</i>. </p>
<p> Connections to other, remote instances can be made. The current instance name is displayed at the prompt. Some commands operate on the current instance and some on the local instance. </p>
<p> Use the &#8216;help&#8217; command to list the available commands.</p>
<h2>GENERAL COMMANDS</h2>
<dl>
<dt><code>help</code></p>
<dd> Show a quick help on the commands available.</p>
<dt><code>quit</code></p>
<dd> Exit from <code>pw-cli</code></dl>
<h2>MODULE MANAGEMENT</h2>
<pre>
Modules are loaded and unloaded in the local instance and can add
functionality or objects to the local instance.
</pre>
<dl>
<dt><code>load-module </code><i>name</i> [<i>arguments&#8230;</i>]</p>
<dd> Load a module specified by its name and arguments. For most modules it is OK to be loaded more than once. </p>
<p> This command returns a module variable that can be used to unload the module.</p>
<dt><code>unload-module </code><i>module-var</i></p>
<dd> Unload a module, specified either by its variable.</dl>
<h2>OBJECT INTROSPECTION</h2>
<dl>
<dt><code>list-objects</code></p>
<dd> List the objects of the current instance. </p>
<p> Objects are listed with their <i>id</i>, <i>type</i> and <i>version</i>.</p>
<dt><code>info </code><i>id</i> | <i>all</i></p>
<dd> Get information about a specific object or <i>all</i> objects. </p>
<p> Requesting info about an object will also notify you of changes.</dl>
<h2>WORKING WITH REMOTES</h2>
<dl>
<dt><code>connect [</code><i>remote-name</i>]</p>
<dd> Connect to a remote instance and make this the new current instance. </p>
<p> If no remote name is specified, a connection is made to the default remote instance, usually <i>pipewire-0</i>. </p>
<p> This command returns a remote var that can be used to disconnect or switch remotes.</p>
<dt><code>disconnect [</code><i>remote-var</i>]</p>
<dd> Disconnect from a <i>remote instance</i>. </p>
<p> If no remote name is specified, the current instance is disconnected.</p>
<dt><code>list-remotes</code></p>
<dd> List all <i>remote instances</i>.</p>
<dt><code>switch-remote [</code><i>remote-var</i>]</p>
<dd> Make the specified <i>remote</i> the current instance. </p>
<p> If no remote name is specified, the local instance is made current.</dl>
<h2>NODE MANAGEMENT</h2>
<dl>
<dt><code>create-node </code><i>factory-name</i> [<i>properties&#8230;</i>]</p>
<dd> Create a node from a factory in the current instance. </p>
<p> Properties are key=value pairs separated by whitespace. </p>
<p> This command returns a <i>node variable</i>.</p>
<dt><code>destroy-node </code><i>node-var</i></p>
<dd> Destroy a node.</p>
<dt><code>export-node </code><i>node-id</i> [<i>remote-var</i>]</p>
<dd> Export a node from the local instance to the specified instance. When no instance is specified, the node will be exported to the current instance.</dl>
<h2>LINK MANAGEMENT</h2>
<dl>
<dt><code>create-link </code><i>node-id</i> <i>port-id</i> <i>node-id</i> <i>port-id</i> [<i>properties&#8230;</i>]</p>
<dd> Create a link between 2 nodes and ports. </p>
<p> Port <i>ids</i> can be <i>-1</i> to automatically select an available port. </p>
<p> Properties are key=value pairs separated by whitespace. </p>
<p> This command returns a <i>link variable</i>.</p>
<dt><code>destroy-link </code><i>link-var</i></p>
<dd> Destroy a link.</dl>
<h2>EXAMPLES</h2>
<h2>AUTHORS</h2>
<p> The PipeWire Developers &lt;<i><a rel="nofollow" href="https://gitlab.freedesktop.org/pipewire/pipewire/issues">https://gitlab.freedesktop.org/pipewire/pipewire/issues</a></i>&gt;; PipeWire is available from <i><a rel="nofollow" href="https://pipewire.org">https://pipewire.org</a></i></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pipewire/">pipewire</a>(1)</code>, <code><a href="/docs/linux/man/1-pw-mon/">pw-mon</a>(1)</code>, </p>
<h2>Index</h2>
