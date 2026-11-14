---
title: "rabbitmq-plugins(1)"
name: "rabbitmq-plugins"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rabbitmq-plugins/"
description: "rabbitmq-plugins – command line tool for managing RabbitMQ broker plugins"
---

<h2 class="name">NAME</h2>
<p> rabbitmq-plugins &#8211; command line tool for managing RabbitMQ broker plugins </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>rabbitmq-plugins</code> [-n&nbsp;<wbr><i>node</i>] {<i>command</i>} [<i>command options</i>&#8230;]</dl>
<h2>DESCRIPTION</h2>
<p> <code>rabbitmq-plugins</code></p>
<dd>is a command line tool for managing RabbitMQ broker plugins. It allows one to enable, disable and browse plugins. It must be run by a user with write permissions to the RabbitMQ configuration directory. </p>
<p> Some plugins depend on others to work correctly. <code>rabbitmq-plugins</code> traverses these dependencies and enables all required plugins. Plugins listed on the <code>rabbitmq-plugins</code> command line are marked as explicitly enabled; dependent plugins are marked as implicitly enabled. Implicitly enabled plugins are automatically disabled again when they are no longer required. </p>
<p> The <code>enable</code>, <code>disable</code> and <code>set</code> commands will update the plugins file and then attempt to connect to the broker and ensure it is running all enabled plugins. By default if it is not possible to connect to the running broker (for example if it is stopped) then a warning is displayed. Specify <code>&#8211;online</code> or <code>&#8211;offline</code> to change this behaviour.</p>
<h2>COMMANDS</h2>
<dl>
<dt>
<dl>
<dt>
<dd>
<p> -v</p>
<dl>
<dt>
<dd>
<dd>Show all plugin details (verbose).</dl>
<p> -m</p>
<dl>
<dt>
<dd> Show only plugin names (minimal).</dl>
<p> -E</p>
<dl>
<dt>
<dd> Show only explicitly enabled plugins.</dl>
<p> -e</p>
<dl>
<dt>
<dd> Show only explicitly or implicitly enabled plugins.</dl>
<p> pattern</p>
<dl>
<dt>
<dd> Pattern to filter the plugin names by.</dl>
<p> Lists all plugins, their versions, dependencies and descriptions. Each plugin is prefixed with two status indicator characters inside [ ]. The first indicator can be &quot; &quot; to indicate that the plugin is not enabled, &quot;E&quot; to indicate that it is explicitly enabled, &quot;e&quot; to indicate that it is implicitly enabled, or &quot;!&quot; to indicate that it is enabled but missing and thus not operational. The second indicator can be &quot; &quot; to show that the plugin is not running, or &quot;*&quot; to show that it is. </p>
<p> If the optional pattern is given, only plugins whose name matches <code>pattern</code> are shown. </p>
<p> For example: </p>
<pre>
rabbitmq-plugins list
</pre>
<p> This command lists all plugins, on one line each. </p>
<pre>
rabbitmq-plugins list -v 
</pre>
<p> This command lists all plugins. </p>
<pre>
rabbitmq-plugins list -v management
</pre>
<p> This command lists all plugins whose name contains &quot;management&quot;. </p>
<pre>
rabbitmq-plugins list -e rabbit
</pre>
<p> This command lists all implicitly or explicitly enabled RabbitMQ plugins.</dl>
</dl>
<dl>
<dt>
<dl>
<dt>
<dd>
<p> &#8211;offline</p>
<dl>
<dt>
<dd>
<dd>Just modify the enabled plugins file.</dl>
<p> &#8211;online</p>
<dl>
<dt>
<dd> Treat failure to connect to the running broker as fatal.</dl>
<p> plugin</p>
<dl>
<dt>
<dd> One or more plugins to enable.</dl>
<p> Enables the specified plugins and all their dependencies. </p>
<p> For example: </p>
<pre>
rabbitmq-plugins enable rabbitmq_shovel rabbitmq_management
</pre>
<p> This command enables the <code>shovel</code> and <code>management</code> plugins and all their dependencies.</dl>
</dl>
<dl>
<dt>
<dl>
<dt>
<dd>
<p> &#8211;offline</p>
<dl>
<dt>
<dd>
<dd>Just modify the enabled plugins file.</dl>
<p> &#8211;online</p>
<dl>
<dt>
<dd> Treat failure to connect to the running broker as fatal.</dl>
<p> plugin</p>
<dl>
<dt>
<dd> One or more plugins to disable.</dl>
<p> Disables the specified plugins and all their dependencies. </p>
<p> For example: </p>
<pre>
rabbitmq-plugins disable amqp_client
</pre>
<p> This command disables <code>amqp_client</code> and all plugins that depend on it.</dl>
</dl>
<dl>
<dt>
<dl>
<dt>
<dd>
<p> &#8211;offline</p>
<dl>
<dt>
<dd>
<dd>Just modify the enabled plugins file.</dl>
<p> &#8211;online</p>
<dl>
<dt>
<dd> Treat failure to connect to the running broker as fatal.</dl>
<p> plugin</p>
<dl>
<dt>
<dd> Zero or more plugins to enable.</dl>
<p> Enables the specified plugins and all their dependencies. Unlike <code>rabbitmq-plugins enable</code> this command ignores and overwrites any existing enabled plugins. <code>rabbitmq-plugins set</code> with no plugin arguments is a legal command meaning &quot;disable all plugins&quot;. </p>
<p> For example: </p>
<pre>
rabbitmq-plugins set rabbitmq_management
</pre>
<p> This command enables the <code>management</code> plugin and its dependencies and disables everything else.</dl>
</dl>
<h2>AUTHOR</h2>
<p> <code>The RabbitMQ Team &lt;</code><code>m[blue]&lt;info [at] rabbitmq.com&gt;</code>m[]<code>&gt;</code> </p>
<h2>Index</h2>
