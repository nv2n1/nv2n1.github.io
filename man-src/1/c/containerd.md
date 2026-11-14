---
title: "containerd(1)"
name: "containerd"
section: "1"
letter: "c"
url: "/docs/linux/man/1-containerd/"
description: "containerd"
---

<p>containerd is a high performance container runtime whose daemon can be started by using this command. If none of the <i>config</i>, <i>publish</i>, or <i>help</i> commands are specified, the default action of the <code>containerd</code> command is to start the containerd daemon in the foreground. </p>
<p> A default configuration is used if no TOML configuration is specified or located at the default file location. The <i>containerd config</i> command can be used to generate the default configuration for containerd. The output of that command can be used and modified as necessary as a custom configuration. </p>
<h2 class="name">NAME</h2>
<p> containerd </p>
<h2>SYNOPSIS</h2>
<p> containerd </p>
<dl>
<dt>
<dd>
<pre><code>
[--address | -a] = [value]
    [--config | -c] = [value]
        [--log - level | -l] = [value]
            [--root] = [value]
                [--state] = [value]
</code></pre>
</dl>
<p> <code>Usage</code>: </p>
<dl>
<dt>
<dd>
<pre><code>
containerd[GLOBAL OPTIONS] command[COMMAND OPTIONS][ARGUMENTS...]
</code></pre>
</dl>
<h2>GLOBAL OPTIONS</h2>
<p> <code>&#8211;address, -a</code>=&quot;&quot;: address for containerd&#8217;s GRPC server </p>
<p> <code>&#8211;config, -c</code>=&quot;&quot;: path to the configuration file (default: /etc/containerd/config.toml) </p>
<p> <code>&#8211;log-level, -l</code>=&quot;&quot;: set the logging level [trace, debug, info, warn, error, fatal, panic] </p>
<p> <code>&#8211;root</code>=&quot;&quot;: containerd root directory </p>
<p> <code>&#8211;state</code>=&quot;&quot;: containerd state directory </p>
<h2>COMMANDS</h2>
<h2>config</h2>
<p> information on the containerd config </p>
<h3>default</h3>
<p> see the output of the default config </p>
<h3>dump</h3>
<p> see the output of the final main config with imported in subconfig files </p>
<h2>publish</h2>
<p> binary to publish events to containerd </p>
<p> <code>&#8211;namespace</code>=&quot;&quot;: namespace to publish to </p>
<p> <code>&#8211;topic</code>=&quot;&quot;: topic of the event </p>
<h2>oci-hook</h2>
<p> provides a base for OCI runtime hooks to allow arguments to be injected. </p>
<h2>Index</h2>
