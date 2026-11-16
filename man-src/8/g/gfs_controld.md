---
title: "gfs_controld(8)"
name: "gfs_controld"
section: "8"
letter: "g"
url: "/docs/linux/man/8-gfs_controld/"
description: "gfs_controld – daemon that coordinates gfs mounts and recovery"
---

<p>gfs_controld &#8211; daemon that coordinates gfs mounts and recovery</p>
<h2>Synopsis</h2>
<p><code>gfs_controld</code> [OPTIONS]</p>
<h2>Description</h2>
<p>GFS lives in the kernel, and the cluster infrastructure (corosync membership and group management) lives in user space. GFS in the kernel needs to adjust/recover for certain cluster events. It&#8217;s the job of gfs_controld to receive these events and reconfigure gfs as needed. gfs_controld controls and configures gfs through sysfs files that are considered gfs-internal interfaces. Mounting and node failure are the main cluster events that gfs_controld controls. It also manages the assignment of journals to different nodes. <code>mount.gfs2</code>(8) communicates with gfs_controld to join the mount group and receive the necessary options for the kernel mount. The cman init script usually starts the gfs_controld daemon. </p>
<h2>Options</h2>
<p>Command line options override a corresponding setting in cluster.conf. </p>
<dl>
<dt><code>-D</code></dt>
<dd>Enable debugging to stderr and don&#8217;t fork.<br />
 See also <code>gfs_control dump</code> in <code><a href="/docs/linux/man/8-gfs_control/">gfs_control</a></code>(8). </dd>
<dt><code>-L</code></dt>
<dd>Enable debugging to log file.<br />
 See also <code>logging</code> in <code>cluster.conf</code>(5). </dd>
<dt><code>-g</code><i> num</i></dt>
<dd>groupd compatibility mode, 0 off, 1 on.<br />
 Default 0. </dd>
<dt><code>-w</code><i> num</i></dt>
<dd>Enable (1) or disable (0) withdraw.<br />
 Default 1. </dd>
<dt><code>-h</code></dt>
<dd>Print a help message describing available options, then exit. </dd>
<dt><code>-V</code></dt>
<dd>Print program version information, then exit. </dd>
</dl>
<h3>Cluster Upgrading</h3>
<p>When performing a rolling upgrade from cluster2 to cluster3, the gfs_controld daemon runs in cluster2 compatibility mode and processes posix lock (plock) requests from the dlm to remain compatible with cluster2 nodes. Otherwise, <code><a href="/docs/linux/man/8-dlm_controld/">dlm_controld</a></code>(8) handles plocks. </p>
<dl>
<dt><code>-p</code><i> num</i></dt>
<dd>Enable (1) or disable (0) plock code for cluster fs.<br />
 Default 1. </dd>
<dt><code>-l</code><i> num</i></dt>
<dd>Limit the rate of plock operations, 0 for no limit.<br />
 Default 0. </dd>
<dt><code>-o</code><i> num</i></dt>
<dd>Enable (1) or disable (0) plock ownership.<br />
 Default 1. </dd>
<dt><code>-t</code><i> ms</i></dt>
<dd>Plock ownership drop resources time (milliseconds).<br />
 Default 10000. </dd>
<dt><code>-c</code><i> num</i></dt>
<dd>Plock ownership drop resources count.<br />
 Default 10. </dd>
<dt><code>-a</code><i> ms</i></dt>
<dd>Plock ownership drop resources age (milliseconds).<br />
 Default 10000. </dd>
<dt><code>-P</code></dt>
<dd>Enable plock debugging messages (can produce excessive output). </dd>
</dl>
<h2>Files</h2>
<p><code>cluster.conf</code>(5) is usually located at /etc/cluster/cluster.conf. It is not read directly. Other cluster components load the contents into memory, and the values are accessed through the libccs library. </p>
<p> Configuration options are added to the &lt;gfs_controld /&gt; section of cluster.conf, within the top level &lt;cluster&gt; section. </p>
<dl>
<dt><code>enable_withdraw</code></dt>
<dd>Set to 1/0 to enable/disable a response to a withdraw. </dd>
<p> &lt;gfs_controld enable_withdraw=&quot;1&quot;/&gt; </p>
</dl>
<h3>Cluster Upgrading</h3>
<p>See note above about compatibility plock handling during a rolling upgrade. The following options are deprecated, see <code><a href="/docs/linux/man/8-dlm_controld/">dlm_controld</a></code>(8) for the new equivalent options. </p>
<dl>
<dt><code>enable_plock</code></dt>
<dd>See command line description. </dd>
<p> &lt;gfs_controld enable_plock=&quot;1&quot;/&gt; </p>
<dt><code>plock_rate_limit</code></dt>
<dd>See command line description. </dd>
<p> &lt;gfs_controld plock_rate_limit=&quot;0&quot;/&gt; </p>
<dt><code>plock_ownership</code></dt>
<dd>See command line description. </dd>
<p> &lt;gfs_controld plock_ownership=&quot;1&quot;/&gt; </p>
<dt><code>drop_resources_time</code></dt>
<dd>See command line description. </dd>
<p> &lt;gfs_controld drop_resources_time=&quot;10000&quot;/&gt; </p>
<dt><code>drop_resources_count</code></dt>
<dd>See command line description. </dd>
<p> &lt;gfs_controld drop_resources_count=&quot;10&quot;/&gt; </p>
<dt><code>drop_resources_age</code></dt>
<dd>See command line description. </dd>
<p> &lt;gfs_controld drop_resources_age=&quot;10000&quot;/&gt; </p>
<dt><code>plock_debug</code></dt>
<dd>Enable (1) or disable (0) plock debugging messages (can produce excessive output). Default 0. </dd>
<p> &lt;gfs_controld plock_debug=&quot;0&quot;/&gt; </p>
</dl>
<h2>See Also</h2>
<p><code>mount.gfs2</code>(8), <code><a href="/docs/linux/man/8-gfs_control/">gfs_control</a></code>(8), <code><a href="/docs/linux/man/8-dlm_controld/">dlm_controld</a></code>(8), <code><a href="/docs/linux/man/5-cman/">cman</a></code>(5), <code>cluster.conf</code>(5) </p>
