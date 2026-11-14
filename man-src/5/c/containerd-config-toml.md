---
title: "containerd-config-toml(5)"
name: "containerd-config-toml"
section: "5"
letter: "c"
url: "/docs/linux/man/5-containerd-config-toml/"
description: "containerd-config.toml – configuration file for containerd"
---

<p>containerd-config.toml &#8211; configuration file for containerd</p>
<h2>Synopsis</h2>
<p>The <code>config.toml</code> file is a configuration file for the containerd daemon. The file must be placed at <code>/etc/containerd/config.toml</code> or specified with the <code>&#8211;config</code> option of <code>containerd</code> to be used by the daemon. If the file does not exist at the appropriate location or is not provided via the <code>&#8211;config</code> option containerd uses its default configuration settings, which can be displayed with the <code>containerd <a href="/docs/linux/man/1-config/">config</a>(1)</code> command. </p>
<h2>Description</h2>
<p>The TOML file used to configure the containerd daemon settings has a short list of global settings followed by a series of sections for specific areas of daemon configuration. There is also a section for <code>plugins</code> that allows each containerd plugin to have an area for plugin-specific configuration and settings. </p>
<h2>Format</h2>
<dl>
<dt><code>version</code></p>
<dd>The version field in the config file specifies the config’s version. If no version number is specified inside the config file then it is assumed to be a version 1 config and parsed as such. Please use version = 2 to enable version 2 config as version 1 has been deprecated. </p>
<dt><code>root</code></p>
<dd>The root directory for containerd metadata. (Default: &quot;/var/lib/containerd&quot;) </p>
<dt><code>state</code></p>
<dd>The state directory for containerd (Default: &quot;/run/containerd&quot;) </p>
<dt><code>plugin_dir</code></p>
<dd>The directory for dynamic plugins to be stored </p>
<dt><code>[grpc]</code></p>
<dd>Section for gRPC socket listener settings. Contains the following properties: </p>
<dl>
<dd>
<dl>
<dt>&bull;</p>
<dd><code>address</code> (Default: &quot;/run/containerd/containerd.sock&quot;)</p>
<dt>&bull;</p>
<dd><code>tcp_address</code></p>
<dt>&bull;</p>
<dd><code>tcp_tls_cert</code></p>
<dt>&bull;</p>
<dd><code>tcp_tls_key</code></p>
<dt>&bull;</p>
<dd><code>uid</code> (Default: 0)</p>
<dt>&bull;</p>
<dd><code>gid</code> (Default: 0)</p>
<dt>&bull;</p>
<dd><code>max_recv_message_size</code></p>
<dt>&bull;</p>
<dd><code>max_send_message_size</code> </p>
</dl>
</dl>
<dt><code>[ttrpc]</code></p>
<dd>Section for TTRPC settings. Contains properties: </p>
<dl>
<dd>
<dl>
<dt>&bull;</p>
<dd><code>address</code> (Default: &quot;&quot;)</p>
<dt>&bull;</p>
<dd><code>uid</code> (Default: 0)</p>
<dt>&bull;</p>
<dd><code>gid</code> (Default: 0) </p>
</dl>
</dl>
<dt><code>[debug]</code></p>
<dd>Section to enable and configure a debug socket listener. Contains four properties: </p>
<dl>
<dd>
<dl>
<dt>&bull;</p>
<dd><code>address</code> (Default: &quot;/run/containerd/debug.sock&quot;)</p>
<dt>&bull;</p>
<dd><code>uid</code> (Default: 0)</p>
<dt>&bull;</p>
<dd><code>gid</code> (Default: 0)</p>
<dt>&bull;</p>
<dd><code>level</code> (Default: &quot;info&quot;) sets the debug log level </p>
</dl>
</dl>
<dt><code>[metrics]</code></p>
<dd>Section to enable and configure a metrics listener. Contains two properties: </p>
<dl>
<dd>
<dl>
<dt>&bull;</p>
<dd><code>address</code> (Default: &quot;&quot;) Metrics endpoint does not listen by default</p>
<dt>&bull;</p>
<dd><code>grpc_histogram</code> (Default: false) Turn on or off gRPC histogram metrics </p>
</dl>
</dl>
<dt><code>disabled_plugins</code></p>
<dd>Disabled plugins are IDs of plugins to disable. Disabled plugins won&#8217;t be initialized and started. </p>
<dt><code>required_plugins</code></p>
<dd>Required plugins are IDs of required plugins. Containerd exits if any required plugin doesn&#8217;t exist or fails to be initialized or started. </p>
<dt><code>[plugins]</code></p>
<dd>The plugins section contains configuration options exposed from installed plugins. The following plugins are enabled by default and their settings are shown below. Plugins that are not enabled by default will provide their own configuration values documentation. </p>
<dl>
<dd>
<dl>
<dt>&bull;</p>
<dd><code>[plugins.cgroup]</code> has one option <code>no_prometheus</code> (Default: <code>false</code>)</p>
<dt>&bull;</p>
<dd><code>[plugins.diff]</code> has one option <code>default</code>, a list by default set to <code>[&quot;walking&quot;]</code></p>
<dt>&bull;</p>
<dd><code>[plugins.linux]</code> has several options for configuring the runtime, shim, and related options:</p>
<dl>
<dd>
<dl>
<dt>&bull;</p>
<dd><code>shim</code> specifies the shim binary (Default: <code>&quot;containerd-shim&quot;</code>),</p>
<dt>&bull;</p>
<dd><code>runtime</code> is the OCI compliant runtime binary (Default: <code>&quot;runc&quot;</code>),</p>
<dt>&bull;</p>
<dd><code>runtime_root</code> is the root directory used by the runtime (Default: <code>&quot;&quot;</code>),</p>
<dt>&bull;</p>
<dd><code>no_shim</code> specifies whether to use a shim or not (Default: <code>false</code>),</p>
<dt>&bull;</p>
<dd><code>shim_debug</code> turns on debugging for the shim (Default: <code>false</code>) </p>
</dl>
</dl>
<dt>&bull;</p>
<dd><code>[plugins.&quot;io.containerd.gc.v1.scheduler&quot;]</code> has several options that perform advanced tuning for the scheduler:</p>
<dl>
<dd>
<dl>
<dt>&bull;</p>
<dd><code>pause_threshold</code> is the maximum amount of time GC should be scheduled (Default: <code>0.02</code>),</p>
<dt>&bull;</p>
<dd><code>deletion_threshold</code> guarantees GC is scheduled after n number of deletions (Default: <code>0</code> [not triggered]),</p>
<dt>&bull;</p>
<dd><code>mutation_threshold</code> guarantees GC is scheduled after n number of database mutations (Default: <code>100</code>),</p>
<dt>&bull;</p>
<dd><code>schedule_delay</code> defines the delay after trigger event before scheduling a GC (Default <code>&quot;0ms&quot;</code> [immediate]),</p>
<dt>&bull;</p>
<dd><code>startup_delay</code> defines the delay after startup before scheduling a GC (Default <code>&quot;100ms&quot;</code>) </p>
</dl>
</dl>
<dt>&bull;</p>
<dd><code>[plugins.&quot;io.containerd.runtime-shim.v2.shim&quot;]</code> specifies options for configuring the runtime shim:</p>
<dl>
<dd>
<dl>
<dt>&bull;</p>
<dd><code>platforms</code> specifies the list of supported platforms</p>
<dt>&bull;</p>
<dd><code>sched_core</code> Core scheduling is a feature that allows only trusted tasks to run concurrently on cpus sharing compute resources (eg: hyperthreads on a core). (Default: <code>false</code>) </p>
</dl>
</dl>
<dt>&bull;</p>
<dd><code>[plugins.&quot;io.containerd.service.v1.tasks-service&quot;]</code> has one option:</p>
<dl>
<dd>
<dl>
<dt>&bull;</p>
<dd><code>rdt_config_file</code> (Linux only) specifies path to a configuration used for configuring RDT (Default: <code>&quot;&quot;</code>). Enables support for Intel RDT, a technology for cache and memory bandwidth management. See <a rel="nofollow" href="https://github.com/intel/goresctrl/blob/v0.2.0/doc/rdt.md#configuration">https://github.com/intel/goresctrl/blob/v0.2.0/doc/rdt.md#configuration</a> for details of the configuration file format. </p>
</dl>
</dl>
</dl>
</dl>
<dt><code>oom_score</code></p>
<dd>The out of memory (OOM) score applied to the containerd daemon process (Default: 0) </p>
<dt><code>[cgroup]</code></p>
<dd>Section for Linux cgroup specific settings </p>
<dl>
<dd>
<dl>
<dt>&bull;</p>
<dd><code>path</code> (Default: &quot;&quot;) Specify a custom cgroup path for created containers </p>
</dl>
</dl>
<dt><code>[proxy_plugins]</code></p>
<dd>Proxy plugins configures plugins which are communicated to over gRPC </p>
<dl>
<dd>
<dl>
<dt>&bull;</p>
<dd><code>type</code> (Default: &quot;&quot;)</p>
<dt>&bull;</p>
<dd><code>address</code> (Default: &quot;&quot;) </p>
</dl>
</dl>
<dt><code>timeouts</code></p>
<dd>Timeouts specified as a duration </p>
<dt><code>imports</code></p>
<dd>Imports is a list of additional configuration files to include. This allows to split the main configuration file and keep some sections separately (for example vendors may keep a custom runtime configuration in a separate file without modifying the main config.toml). Imported files will overwrite simple fields like int or string (if not empty) and will append array and map fields. Imported files are also versioned, and the version can&#8217;t be higher than the main config. </p>
</dl>
<p> <code>stream_processors</code> </p>
<dl>
<dd>
<dl>
<dt>&bull;</p>
<dd><code>accepts</code> (Default: &quot;[]&quot;) Accepts specific media-types</p>
<dt>&bull;</p>
<dd><code>returns</code> (Default: &quot;&quot;) Returns the media-type</p>
<dt>&bull;</p>
<dd><code>path</code> (Default: &quot;&quot;) Path or name of the binary</p>
<dt>&bull;</p>
<dd><code>args</code> (Default: &quot;[]&quot;) Args to the binary </p>
</dl>
</dl>
<h2>Example</h2>
<p>The following is a complete <code>config.toml</code> default configuration example: </p>
<pre><code>
root = &quot;/var/lib/containerd&quot;
state = &quot;/run/containerd&quot;
oom_score = 0
imports = [&quot;/etc/containerd/runtime_*.toml&quot;, &quot;./debug.toml&quot;]

[grpc]
address = &quot;/run/containerd/containerd.sock&quot;
uid = 0
gid = 0

[debug]
address = &quot;/run/containerd/debug.sock&quot;
uid = 0
gid = 0
level = &quot;info&quot;

[metrics]
address = &quot;&quot;
grpc_histogram = false

[cgroup]
path = &quot;&quot;

[plugins]
[plugins.cgroups]
no_prometheus = false
[plugins.diff]
default = [&quot;walking&quot;]
[plugins.linux]
shim = &quot;containerd-shim&quot;
runtime = &quot;runc&quot;
runtime_root = &quot;&quot;
no_shim = false
shim_debug = false
[plugins.scheduler]
pause_threshold = 0.02
deletion_threshold = 0
mutation_threshold = 100
schedule_delay = 0
startup_delay = &quot;100ms&quot;
[plugins.&quot;io.containerd.runtime-shim.v2.shim&quot;]
platforms = [&quot;linux/amd64&quot;]
sched_core = true
[plugins.&quot;io.containerd.service.v1.tasks-service&quot;]
rdt_config_file = &quot;/etc/rdt-config.yaml&quot;
</code></pre>
<h2>Bugs</h2>
<p>Please file any specific issues that you encounter at <a rel="nofollow" href="https://github.com/containerd/containerd.">https://github.com/containerd/containerd.</a> </p>
<h2>Author</h2>
<p>Phil Estes estesp [at] gmail.com &lt;mailto:estesp [at] gmail.com&gt;</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-ctr/">ctr</a>(8), <a href="/docs/linux/man/8-containerd-config/">containerd-config</a>(8), <a href="/docs/linux/man/8-containerd/">containerd</a>(8) </p>
