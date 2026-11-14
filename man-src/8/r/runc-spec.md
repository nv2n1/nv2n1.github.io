---
title: "runc-spec(8)"
name: "runc-spec"
section: "8"
letter: "r"
url: "/docs/linux/man/8-runc-spec/"
description: "runc-spec – create a new specification file"
---

<p><code>runc-spec</code> &#8211; create a new specification file </p>
<h2>Synopsis</h2>
<p><code>runc spec</code> [<i>option</i> &#8230;] </p>
<h2>Description</h2>
<p>The <code>spec</code> command creates the new specification file named <i>config.json</i> for the bundle. The spec generated is just a starter file. Editing of the spec is required to achieve desired results. For example, the newly generated spec includes an <code>args</code> parameter that is initially set to call the <code>sh</code> command when the container is started. Calling <code>sh</code> may work for an ubuntu container or busybox, but will not work for containers that do not include the <code>sh</code> binary. </p>
<h2>Options</h2>
<dl>
<dt><code>&#8211;bundle</code>|<code>-b</code> <i>path</i></p>
<dd>Set <i>path</i> to the root of the bundle directory. </p>
<dt><code>&#8211;rootless</code></p>
<dd>Generate a configuration for a rootless container. Note this option is entirely different from the global <code>&#8211;rootless</code> option. </p>
</dl>
<h2>Examples</h2>
<p>To run a simple &quot;hello-world&quot; container, one needs to set the <code>args</code> parameter in the spec to call hello. This can be done using <code><a href="/docs/linux/man/1-sed/">sed</a></code>(1), <code><a href="/docs/linux/man/1-jq/">jq</a></code>(1), or a text editor. The following commands will:<br />
&nbsp;&#8211; create a bundle for hello-world;<br />
&nbsp;&#8211; change the command to run in a container to&nbsp;<code>/hello</code>&nbsp;using&nbsp;<code><a href="/docs/linux/man/1-jq/">jq</a></code>(1);<br />
&nbsp;&#8211; run the&nbsp;<code>hello</code>&nbsp;command in a new hello-world container named&nbsp;<code>container1</code>.  </p>
<pre>mkdir hello
cd hello
docker pull hello-world
docker export $(docker create hello-world) &gt; hello-world.tar
mkdir rootfs
tar -C rootfs -xf hello-world.tar
runc spec
jq '.process.args |= [&quot;/hello&quot;]' &lt; config.json &gt; new.json
mv -f new.json config.json
runc run container1</pre>
</dl>
<p> In the <code>run</code> command above, <code>container1</code> is the name for the instance of the container that you are starting. The name you provide for the container instance must be unique on your host. An alternative for generating a customized spec config is to use <code>oci-runtime-tool</code>; its sub-command <code>oci-runtime-tool generate</code> has lots of options that can be used to do any customizations as you want. See runtime-tools &lt;<a rel="nofollow" href="https://github.com/opencontainers/runtime-tools">https://github.com/opencontainers/runtime-tools</a>&gt; to get more information. When starting a container through <code>runc</code>, the latter usually needs root privileges. If not already running as root, you can use <code><a href="/docs/linux/man/8-sudo/">sudo</a></code>(8), for example:  </p>
<pre>sudo runc start container1</pre>
</dl>
<p> Alternatively, you can start a rootless container, which has the ability to run without root privileges. For this to work, the specification file needs to be adjusted accordingly. You can pass the <code>&#8211;rootless</code> option to this command to generate a proper rootless spec file. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-runc-run/">runc-run</a></code>(8), <code><a href="/docs/linux/man/8-runc/">runc</a></code>(8). </p>
