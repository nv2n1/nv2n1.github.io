---
title: "ctr(1)"
name: "ctr"
section: "1"
letter: "c"
url: "/docs/linux/man/1-ctr/"
description: "ctr"
---

<p>ctr is an unsupported debug and administrative client for interacting with the containerd daemon. Because it is unsupported, the commands, options, and operations are not guaranteed to be backward compatible or stable from release to release of the containerd project. </p>
<h2 class="name">NAME</h2>
<p> ctr </p>
<h2>SYNOPSIS</h2>
<p> ctr </p>
<dl>
<dt>
<dd>
<pre><code>
[--address | -a] = [value]
    [--connect - timeout] = [value]
        [--debug]
        [--namespace | -n] = [value]
            [--timeout] = [value]
</code></pre>
</dl>
<p> <code>Usage</code>: </p>
<dl>
<dt>
<dd>
<pre><code>
ctr[GLOBAL OPTIONS] command[COMMAND OPTIONS][ARGUMENTS...]
</code></pre>
</dl>
<h2>GLOBAL OPTIONS</h2>
<p> <code>&#8211;address, -a</code>=&quot;&quot;: address for containerd&#8217;s GRPC server (default: /run/containerd/containerd.sock) </p>
<p> <code>&#8211;connect-timeout</code>=&quot;&quot;: timeout for connecting to containerd (default: 0s) </p>
<p> <code>&#8211;debug</code>: enable debug output in logs </p>
<p> <code>&#8211;namespace, -n</code>=&quot;&quot;: namespace to use with commands (default: default) </p>
<p> <code>&#8211;timeout</code>=&quot;&quot;: total timeout for ctr commands (default: 0s) </p>
<h2>COMMANDS</h2>
<h2>plugins, plugin</h2>
<p> provides information about containerd plugins </p>
<h3>list, ls</h3>
<p> lists containerd plugins </p>
<p> <code>&#8211;detailed, -d</code>: print detailed information about each plugin </p>
<p> <code>&#8211;quiet, -q</code>: print only the plugin ids </p>
<h2>version</h2>
<p> print the client and server versions </p>
<h2>containers, c, container</h2>
<p> manage containers </p>
<h3>create</h3>
<p> create container </p>
<p> <code>&#8211;allow-new-privs</code>: turn off OCI spec&#8217;s NoNewPrivileges feature flag </p>
<p> <code>&#8211;config, -c</code>=&quot;&quot;: path to the runtime-specific spec config file </p>
<p> <code>&#8211;cwd</code>=&quot;&quot;: specify the working directory of the process </p>
<p> <code>&#8211;device</code>=&quot;&quot;: add a device to a container </p>
<p> <code>&#8211;env</code>=&quot;&quot;: specify additional container environment variables (i.e. FOO=bar) </p>
<p> <code>&#8211;env-file</code>=&quot;&quot;: specify additional container environment variables in a file(i.e. FOO=bar, one per line) </p>
<p> <code>&#8211;gpus</code>=&quot;&quot;: add gpus to the container (default: 0) </p>
<p> <code>&#8211;label</code>=&quot;&quot;: specify additional labels (i.e. foo=bar) </p>
<p> <code>&#8211;memory-limit</code>=&quot;&quot;: memory limit (in bytes) for the container (default: 0) </p>
<p> <code>&#8211;mount</code>=&quot;&quot;: specify additional container mount (ex: type=bind,src=/tmp,dst=/host,options=rbind:ro) </p>
<p> <code>&#8211;net-host</code>: enable host networking for the container </p>
<p> <code>&#8211;no-pivot</code>: disable use of pivot-root (linux only) </p>
<p> <code>&#8211;pid-file</code>=&quot;&quot;: file path to write the task&#8217;s pid </p>
<p> <code>&#8211;privileged</code>: run privileged container </p>
<p> <code>&#8211;read-only</code>: set the containers filesystem as readonly </p>
<p> <code>&#8211;rootfs</code>: use custom rootfs that is not managed by containerd snapshotter </p>
<p> <code>&#8211;runtime</code>=&quot;&quot;: runtime name (default: io.containerd.runc.v2) </p>
<p> <code>&#8211;seccomp</code>: enable the default seccomp profile </p>
<p> <code>&#8211;snapshotter</code>=&quot;&quot;: snapshotter name. Empty value stands for the default value. </p>
<p> <code>&#8211;tty, -t</code>: allocate a TTY for the container </p>
<p> <code>&#8211;with-ns</code>=&quot;&quot;: specify existing Linux namespaces to join at container runtime (format &#8216;&lt;nstype&gt;:&lt;path&gt;&#8217;) </p>
<h3>delete, del, rm</h3>
<p> delete one or more existing containers </p>
<p> <code>&#8211;keep-snapshot</code>: do not clean up snapshot with container </p>
<h3>info</h3>
<p> get info about a container </p>
<h3>list, ls</h3>
<p> list containers </p>
<p> <code>&#8211;quiet, -q</code>: print only the container id </p>
<h3>label</h3>
<p> set and clear labels for a container </p>
<h3>checkpoint</h3>
<p> checkpoint a container </p>
<p> <code>&#8211;image</code>: include the image in the checkpoint </p>
<p> <code>&#8211;rw</code>: include the rw layer in the checkpoint </p>
<p> <code>&#8211;task</code>: checkpoint container task </p>
<h3>restore</h3>
<p> restore a container from checkpoint </p>
<p> <code>&#8211;live</code>: restore the runtime and memory data from the checkpoint </p>
<p> <code>&#8211;rw</code>: restore the rw layer from the checkpoint </p>
<h2>content</h2>
<p> manage content </p>
<h3>active</h3>
<p> display active transfers </p>
<p> <code>&#8211;root</code>=&quot;&quot;: path to content store root (default: /tmp/content) </p>
<p> <code>&#8211;timeout, -t</code>=&quot;&quot;: total timeout for fetch (default: 0s) </p>
<h3>delete, del, remove, rm</h3>
<p> permanently delete one or more blobs </p>
<h3>edit</h3>
<p> edit a blob and return a new digest </p>
<p> <code>&#8211;editor</code>=&quot;&quot;: select editor (vim, emacs, etc.) </p>
<p> <code>&#8211;validate</code>=&quot;&quot;: validate the result against a format (json, mediatype, etc.) </p>
<h3>fetch</h3>
<p> fetch all content for an image into containerd </p>
<p> <code>&#8211;all-metadata</code>: Pull metadata for all platforms </p>
<p> <code>&#8211;all-platforms</code>: pull content from all platforms </p>
<p> <code>&#8211;label</code>=&quot;&quot;: labels to attach to the image </p>
<p> <code>&#8211;metadata-only</code>: Pull all metadata including manifests and configs </p>
<p> <code>&#8211;plain-http</code>: allow connections using plain HTTP </p>
<p> <code>&#8211;platform</code>=&quot;&quot;: Pull content from a specific platform </p>
<p> <code>&#8211;refresh</code>=&quot;&quot;: refresh token for authorization server </p>
<p> <code>&#8211;skip-verify, -k</code>: skip SSL certificate validation </p>
<p> <code>&#8211;user, -u</code>=&quot;&quot;: user[:password] Registry user and password </p>
<h3>fetch-object</h3>
<p> retrieve objects from a remote </p>
<p> <code>&#8211;plain-http</code>: allow connections using plain HTTP </p>
<p> <code>&#8211;refresh</code>=&quot;&quot;: refresh token for authorization server </p>
<p> <code>&#8211;skip-verify, -k</code>: skip SSL certificate validation </p>
<p> <code>&#8211;user, -u</code>=&quot;&quot;: user[:password] Registry user and password </p>
<h3>get</h3>
<p> get the data for an object </p>
<h3>ingest</h3>
<p> accept content into the store </p>
<p> <code>&#8211;expected-digest</code>=&quot;&quot;: verify content against expected digest </p>
<p> <code>&#8211;expected-size</code>=&quot;&quot;: validate against provided size (default: 0) </p>
<h3>list, ls</h3>
<p> list all blobs in the store </p>
<p> <code>&#8211;quiet, -q</code>: print only the blob digest </p>
<h3>push-object</h3>
<p> push an object to a remote </p>
<p> <code>&#8211;plain-http</code>: allow connections using plain HTTP </p>
<p> <code>&#8211;refresh</code>=&quot;&quot;: refresh token for authorization server </p>
<p> <code>&#8211;skip-verify, -k</code>: skip SSL certificate validation </p>
<p> <code>&#8211;user, -u</code>=&quot;&quot;: user[:password] Registry user and password </p>
<h3>label</h3>
<p> add labels to content </p>
<h2>events, event</h2>
<p> display containerd events </p>
<h2>images, image, i</h2>
<p> manage images </p>
<h3>check</h3>
<p> check that an image has all content available locally </p>
<p> <code>&#8211;snapshotter</code>=&quot;&quot;: snapshotter name. Empty value stands for the default value. </p>
<h3>export</h3>
<p> export images </p>
<p> <code>&#8211;all-platforms</code>: exports content from all platforms </p>
<p> <code>&#8211;platform</code>=&quot;&quot;: Pull content from a specific platform (default: []) </p>
<p> <code>&#8211;skip-manifest-json</code>: do not add Docker compatible manifest.json to archive </p>
<h3>import</h3>
<p> import images </p>
<p> <code>&#8211;all-platforms</code>: imports content for all platforms, false by default </p>
<p> <code>&#8211;base-name</code>=&quot;&quot;: base image name for added images, when provided only images with this name prefix are imported </p>
<p> <code>&#8211;compress-blobs</code>: compress uncompressed blobs when creating manifest (Docker format only) </p>
<p> <code>&#8211;digests</code>: whether to create digest images (default: false) </p>
<p> <code>&#8211;index-name</code>=&quot;&quot;: image name to keep index as, by default index is discarded </p>
<p> <code>&#8211;no-unpack</code>: skip unpacking the images, false by default </p>
<p> <code>&#8211;snapshotter</code>=&quot;&quot;: snapshotter name. Empty value stands for the default value. </p>
<h3>list, ls</h3>
<p> list images known to containerd </p>
<p> <code>&#8211;quiet, -q</code>: print only the image refs </p>
<h3>pull</h3>
<p> pull an image from a remote </p>
<p> <code>&#8211;all-metadata</code>: Pull metadata for all platforms </p>
<p> <code>&#8211;all-platforms</code>: pull content and metadata from all platforms </p>
<p> <code>&#8211;label</code>=&quot;&quot;: labels to attach to the image </p>
<p> <code>&#8211;plain-http</code>: allow connections using plain HTTP </p>
<p> <code>&#8211;platform</code>=&quot;&quot;: Pull content from a specific platform (default: []) </p>
<p> <code>&#8211;refresh</code>=&quot;&quot;: refresh token for authorization server </p>
<p> <code>&#8211;skip-verify, -k</code>: skip SSL certificate validation </p>
<p> <code>&#8211;snapshotter</code>=&quot;&quot;: snapshotter name. Empty value stands for the default value. </p>
<p> <code>&#8211;user, -u</code>=&quot;&quot;: user[:password] Registry user and password </p>
<h3>push</h3>
<p> push an image to a remote </p>
<p> <code>&#8211;manifest</code>=&quot;&quot;: digest of manifest </p>
<p> <code>&#8211;manifest-type</code>=&quot;&quot;: media type of manifest digest (default: application/vnd.oci.image.manifest.v1+json) </p>
<p> <code>&#8211;plain-http</code>: allow connections using plain HTTP </p>
<p> <code>&#8211;refresh</code>=&quot;&quot;: refresh token for authorization server </p>
<p> <code>&#8211;skip-verify, -k</code>: skip SSL certificate validation </p>
<p> <code>&#8211;user, -u</code>=&quot;&quot;: user[:password] Registry user and password </p>
<h3>remove, rm</h3>
<p> remove one or more images by reference </p>
<p> <code>&#8211;sync</code>: Synchronously remove image and all associated resources </p>
<h3>tag</h3>
<p> tag an image </p>
<p> <code>&#8211;force</code>: force target_ref to be created, regardless if it already exists </p>
<h3>label</h3>
<p> set and clear labels for an image </p>
<p> <code>&#8211;replace-all, -r</code>: replace all labels </p>
<h2>leases</h2>
<p> manage leases </p>
<h3>list, ls</h3>
<p> list all active leases </p>
<p> <code>&#8211;quiet, -q</code>: print only the blob digest </p>
<h3>create</h3>
<p> create lease </p>
<p> <code>&#8211;expires, -x</code>=&quot;&quot;: expiration of lease (0 value will not expire) (default: 24h0m0s) </p>
<p> <code>&#8211;id</code>=&quot;&quot;: set the id for the lease, will be generated by default </p>
<h3>delete, rm</h3>
<p> delete a lease </p>
<p> <code>&#8211;sync</code>: Synchronously remove leases and all unreferenced resources </p>
<h2>namespaces, namespace, ns</h2>
<p> manage namespaces </p>
<h3>create, c</h3>
<p> create a new namespace </p>
<h3>list, ls</h3>
<p> list namespaces </p>
<p> <code>&#8211;quiet, -q</code>: print only the namespace name </p>
<h3>remove, rm</h3>
<p> remove one or more namespaces </p>
<p> <code>&#8211;cgroup, -c</code>: delete the namespace&#8217;s cgroup </p>
<h3>label</h3>
<p> set and clear labels for a namespace </p>
<h2>pprof</h2>
<p> provide golang pprof outputs for containerd </p>
<p> <code>&#8211;debug-socket, -d</code>=&quot;&quot;: socket path for containerd&#8217;s debug server (default: /run/containerd/debug.sock) </p>
<h3>block</h3>
<p> goroutine blocking profile </p>
<h3>goroutines</h3>
<p> dump goroutine stack dump </p>
<h3>heap</h3>
<p> dump heap profile </p>
<h3>profile</h3>
<p> CPU profile </p>
<p> <code>&#8211;seconds, -s</code>=&quot;&quot;: duration for collection (seconds) (default: 30s) </p>
<h3>threadcreate</h3>
<p> goroutine thread creating profile </p>
<h3>trace</h3>
<p> collect execution trace </p>
<p> <code>&#8211;seconds, -s</code>=&quot;&quot;: trace time (seconds) (default: 5s) </p>
<h2>run</h2>
<p> run a container </p>
<p> <code>&#8211;allow-new-privs</code>: turn off OCI spec&#8217;s NoNewPrivileges feature flag </p>
<p> <code>&#8211;cgroup</code>=&quot;&quot;: cgroup path (To disable use of cgroup, set to &quot;&quot; explicitly) </p>
<p> <code>&#8211;config, -c</code>=&quot;&quot;: path to the runtime-specific spec config file </p>
<p> <code>&#8211;cwd</code>=&quot;&quot;: specify the working directory of the process </p>
<p> <code>&#8211;detach, -d</code>: detach from the task after it has started execution </p>
<p> <code>&#8211;device</code>=&quot;&quot;: add a device to a container </p>
<p> <code>&#8211;env</code>=&quot;&quot;: specify additional container environment variables (i.e. FOO=bar) </p>
<p> <code>&#8211;env-file</code>=&quot;&quot;: specify additional container environment variables in a file(i.e. FOO=bar, one per line) </p>
<p> <code>&#8211;fifo-dir</code>=&quot;&quot;: directory used for storing IO FIFOs </p>
<p> <code>&#8211;gpus</code>=&quot;&quot;: add gpus to the container (default: 0) </p>
<p> <code>&#8211;label</code>=&quot;&quot;: specify additional labels (i.e. foo=bar) </p>
<p> <code>&#8211;log-uri</code>=&quot;&quot;: log uri </p>
<p> <code>&#8211;memory-limit</code>=&quot;&quot;: memory limit (in bytes) for the container (default: 0) </p>
<p> <code>&#8211;mount</code>=&quot;&quot;: specify additional container mount (ex: type=bind,src=/tmp,dst=/host,options=rbind:ro) </p>
<p> <code>&#8211;net-host</code>: enable host networking for the container </p>
<p> <code>&#8211;no-pivot</code>: disable use of pivot-root (linux only) </p>
<p> <code>&#8211;null-io</code>: send all IO to /dev/null </p>
<p> <code>&#8211;pid-file</code>=&quot;&quot;: file path to write the task&#8217;s pid </p>
<p> <code>&#8211;platform</code>=&quot;&quot;: run image for specific platform </p>
<p> <code>&#8211;privileged</code>: run privileged container </p>
<p> <code>&#8211;read-only</code>: set the containers filesystem as readonly </p>
<p> <code>&#8211;rm</code>: remove the container after running </p>
<p> <code>&#8211;rootfs</code>: use custom rootfs that is not managed by containerd snapshotter </p>
<p> <code>&#8211;runtime</code>=&quot;&quot;: runtime name (default: io.containerd.runc.v2) </p>
<p> <code>&#8211;seccomp</code>: enable the default seccomp profile </p>
<p> <code>&#8211;snapshotter</code>=&quot;&quot;: snapshotter name. Empty value stands for the default value. </p>
<p> <code>&#8211;tty, -t</code>: allocate a TTY for the container </p>
<p> <code>&#8211;with-ns</code>=&quot;&quot;: specify existing Linux namespaces to join at container runtime (format &#8216;&lt;nstype&gt;:&lt;path&gt;&#8217;) </p>
<h2>snapshots, snapshot</h2>
<p> manage snapshots </p>
<p> <code>&#8211;snapshotter</code>=&quot;&quot;: snapshotter name. Empty value stands for the default value. </p>
<h3>commit</h3>
<p> commit an active snapshot into the provided name </p>
<h3>diff</h3>
<p> get the diff of two snapshots. the default second snapshot is the first snapshot&#8217;s parent. </p>
<p> <code>&#8211;keep</code>: keep diff content. up to creator to delete it. </p>
<p> <code>&#8211;label</code>=&quot;&quot;: labels to attach to the image </p>
<p> <code>&#8211;media-type</code>=&quot;&quot;: media type to use for creating diff (default: application/vnd.oci.image.layer.v1.tar+gzip) </p>
<p> <code>&#8211;ref</code>=&quot;&quot;: content upload reference to use </p>
<h3>info</h3>
<p> get info about a snapshot </p>
<h3>list, ls</h3>
<p> list snapshots </p>
<h3>mounts, m, mount</h3>
<p> mount gets mount commands for the snapshots </p>
<h3>prepare</h3>
<p> prepare a snapshot from a committed snapshot </p>
<p> <code>&#8211;target, -t</code>=&quot;&quot;: mount target path, will print mount, if provided </p>
<h3>remove, rm</h3>
<p> remove snapshots </p>
<h3>label</h3>
<p> add labels to content </p>
<h3>tree</h3>
<p> display tree view of snapshot branches </p>
<h3>unpack</h3>
<p> unpack applies layers from a manifest to a snapshot </p>
<p> <code>&#8211;snapshotter</code>=&quot;&quot;: snapshotter name. Empty value stands for the default value. </p>
<h3>usage</h3>
<p> usage snapshots </p>
<p> <code>-b</code>: display size in bytes </p>
<h3>view</h3>
<p> create a read-only snapshot from a committed snapshot </p>
<p> <code>&#8211;target, -t</code>=&quot;&quot;: mount target path, will print mount, if provided </p>
<h2>tasks, t, task</h2>
<p> manage tasks </p>
<h3>attach</h3>
<p> attach to the IO of a running container </p>
<h3>checkpoint</h3>
<p> checkpoint a container </p>
<p> <code>&#8211;exit</code>: stop the container after the checkpoint </p>
<p> <code>&#8211;image-path</code>=&quot;&quot;: path to criu image files </p>
<p> <code>&#8211;work-path</code>=&quot;&quot;: path to criu work files and logs </p>
<h3>delete, rm</h3>
<p> delete one or more tasks </p>
<p> <code>&#8211;exec-id</code>=&quot;&quot;: process ID to kill </p>
<p> <code>&#8211;force, -f</code>: force delete task process </p>
<h3>exec</h3>
<p> execute additional processes in an existing container </p>
<p> <code>&#8211;cwd</code>=&quot;&quot;: working directory of the new process </p>
<p> <code>&#8211;detach, -d</code>: detach from the task after it has started execution </p>
<p> <code>&#8211;exec-id</code>=&quot;&quot;: exec specific id for the process </p>
<p> <code>&#8211;fifo-dir</code>=&quot;&quot;: directory used for storing IO FIFOs </p>
<p> <code>&#8211;log-uri</code>=&quot;&quot;: log uri for custom shim logging </p>
<p> <code>&#8211;tty, -t</code>: allocate a TTY for the container </p>
<h3>list, ls</h3>
<p> list tasks </p>
<p> <code>&#8211;quiet, -q</code>: print only the task id </p>
<h3>kill</h3>
<p> signal a container (default: SIGTERM) </p>
<p> <code>&#8211;all, -a</code>: send signal to all processes inside the container </p>
<p> <code>&#8211;exec-id</code>=&quot;&quot;: process ID to kill </p>
<p> <code>&#8211;signal, -s</code>=&quot;&quot;: signal to send to the container </p>
<h3>pause</h3>
<p> pause an existing container </p>
<h3>ps</h3>
<p> list processes for container </p>
<h3>resume</h3>
<p> resume a paused container </p>
<h3>start</h3>
<p> start a container that have been created </p>
<p> <code>&#8211;detach, -d</code>: detach from the task after it has started execution </p>
<p> <code>&#8211;fifo-dir</code>=&quot;&quot;: directory used for storing IO FIFOs </p>
<p> <code>&#8211;log-uri</code>=&quot;&quot;: log uri </p>
<p> <code>&#8211;null-io</code>: send all IO to /dev/null </p>
<p> <code>&#8211;pid-file</code>=&quot;&quot;: file path to write the task&#8217;s pid </p>
<h3>metrics, metric</h3>
<p> get a single data point of metrics for a task with the built-in Linux runtime </p>
<p> <code>&#8211;format</code>=&quot;&quot;: &quot;table&quot; or &quot;json&quot; (default: table) </p>
<h2>install</h2>
<p> install a new package </p>
<p> <code>&#8211;libs, -l</code>: install libs from the image </p>
<p> <code>&#8211;path</code>=&quot;&quot;: set an optional install path other than the managed opt directory </p>
<p> <code>&#8211;replace, -r</code>: replace any binaries or libs in the opt directory </p>
<h2>shim</h2>
<p> interact with a shim directly </p>
<p> <code>&#8211;id</code>=&quot;&quot;: container id </p>
<h3>delete</h3>
<p> delete a container with a task </p>
<h3>exec</h3>
<p> exec a new process in the task&#8217;s container </p>
<p> <code>&#8211;attach, -a</code>: stay attached to the container and open the fifos </p>
<p> <code>&#8211;cwd</code>=&quot;&quot;: current working directory </p>
<p> <code>&#8211;env, -e</code>=&quot;&quot;: add environment vars (default: []) </p>
<p> <code>&#8211;spec</code>=&quot;&quot;: runtime spec </p>
<p> <code>&#8211;stderr</code>=&quot;&quot;: specify the path to the stderr fifo </p>
<p> <code>&#8211;stdin</code>=&quot;&quot;: specify the path to the stdin fifo </p>
<p> <code>&#8211;stdout</code>=&quot;&quot;: specify the path to the stdout fifo </p>
<p> <code>&#8211;tty, -t</code>: enable tty support </p>
<h3>start</h3>
<p> start a container with a task </p>
<h3>state</h3>
<p> get the state of all the processes of the task </p>
<h2>Index</h2>
