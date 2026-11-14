---
title: "ocf_heartbeat_docker(7)"
name: "ocf_heartbeat_docker"
section: "7"
letter: "o"
url: "/docs/linux/man/7-ocf_heartbeat_docker/"
description: "ocf_heartbeat_docker – Docker container resource agent."
---

<p>ocf_heartbeat_docker &#8211; Docker container resource agent.</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>docker</code> [start | stop | monitor | meta-data | validate-all]</dl>
<h2>Description</h2>
<dd>The docker HA resource agent creates and launches a docker container based off a supplied docker image. Containers managed by this agent are both created and removed upon the agent&#8217;s start and stop actions.</p>
<h2>Supported Parameters</h2>
<p><code>image</code></p>
<dl>
<dd>The docker image to base this container off of. </p>
<p> (required, string, no default)</dl>
<p> <code>name</code></p>
<dl>
<dd>The name to give the created container. By default this will be that resource&#8217;s instance name. </p>
<p> (optional, string, no default)</dl>
<p> <code>allow_pull</code></p>
<dl>
<dd>Allow the image to be pulled from the configured docker registry when the image does not exist locally. NOTE, this can drastically increase the time required to start the container if the image repository is pulled over the network. </p>
<p> (optional, boolean, no default)</dl>
<p> <code>run_opts</code></p>
<dl>
<dd>Add options to be appended to the &#8216;docker run&#8217; command which is used when creating the container during the start action. This option allows users to do things such as setting a custom entry point and injecting environment variables into the newly created container. Note the &#8216;-d&#8217; option is supplied regardless of this value to force containers to run in the background. </p>
<p> NOTE: Do not explicitly specify the &#8211;name argument in the run_opts. This agent will set &#8211;name using either the resource&#8217;s instance or the name provided in the &#8216;name&#8217; argument of this agent. </p>
<p> (optional, string, no default)</dl>
<p> <code>run_cmd</code></p>
<dl>
<dd>Specifiy a command to launch within the container once it has initialized. </p>
<p> (optional, string, no default)</dl>
<p> <code>monitor_cmd</code></p>
<dl>
<dd>Specifiy the full path of a command to launch within the container to check the health of the container. This command must return 0 to indicate that the container is healthy. A non-zero return code will indicate that the container has failed and should be recovered. </p>
<p> The command is executed using nsenter. In the future &#8216;docker exec&#8217; will be used once it is more widely supported. </p>
<p> (optional, string, no default)</dl>
<p> <code>force_kill</code></p>
<dl>
<dd>Kill a container immediately rather than waiting for it to gracefully shutdown </p>
<p> (optional, boolean, no default)</dl>
<p> <code>reuse</code></p>
<dl>
<dd>Allow the container to be reused after stopping the container. By default containers are removed after stop. With the reuse option containers will persist after the container stops. </p>
<p> (optional, boolean, no default)</dl>
<h2>Supported Actions</h2>
<p>This resource agent supports the following actions (operations): </p>
<p> <code>start</code></p>
<dl>
<dd>Starts the resource. Suggested minimum timeout: 90.</dl>
<p> <code>stop</code></p>
<dl>
<dd>Stops the resource. Suggested minimum timeout: 90.</dl>
<p> <code>monitor</code></p>
<dl>
<dd>Performs a detailed status check. Suggested minimum timeout: 30. Suggested interval: 30.</dl>
<p> <code>meta-data</code></p>
<dl>
<dd>Retrieves resource agent metadata (internal use only). Suggested minimum timeout: 5.</dl>
<p> <code>validate-all</code></p>
<dl>
<dd>Performs a validation of the resource configuration. Suggested minimum timeout: 30.</dl>
<h2>Example Crm Shell</h2>
<p>The following is an example configuration for a docker resource using the <code><a href="/docs/linux/man/8-crm/">crm</a></code>(8) shell: </p>
<dl>
<dd>
<pre>primitive p_docker ocf:heartbeat:docker \
 params \
 image=<i>string</i> \
 op monitor timeout=&quot;30&quot; interval=&quot;30&quot; depth=&quot;0&quot; </pre>
</dl>
<h2>Example Pcs</h2>
<p>The following is an example configuration for a docker resource using <code><a href="/docs/linux/man/8-pcs/">pcs</a></code>(8) </p>
<dl>
<dd>
<pre>pcs resource create p_docker ocf:heartbeat:docker \
 image=<i>string</i> \
 op monitor timeout=&quot;30&quot; interval=&quot;30&quot; depth=&quot;0&quot; </pre>
</dl>
<h2>See Also</h2>
<p>m[blue]<code><a rel="nofollow" href="http://www.linux-ha.org/wiki/docker_(resource_agent)">http://www.linux-ha.org/wiki/docker_(resource_agent)</a></code>m[]</p>
<h2>Author</h2>
<p><code>Linux-HA contributors (see the resource agent source for information about individual authors)</code></p>
