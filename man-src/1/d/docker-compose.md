---
title: "docker-compose(1)"
name: "docker-compose"
section: "1"
letter: "d"
url: "/docs/linux/man/1-docker-compose/"
description: "docker-compose – Define and run multi-container applications with Docker."
---

<h2 class="name">NAME</h2>
<p> docker-compose &#8211; Define and run multi-container applications with Docker. </p>
<h2>SYNOPSIS</h2>
<p> <code>docker-compose </code> [<i>OPTIONS</i>] [<i>COMMAND</i>] [<i>ARGS</i>]&#8230;</p>
<h2>DESCRIPTION</h2>
<p> docker-compose allows you to define a multi-container application with all of its dependencies in a single file, then spin the application up in a single command. The application’s structure and configuration are held in a single place, which makes spinning up applications simple and repeatable everywhere.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-f</code>, <code>&#8211;file</code> FILE</p>
<dd> Specify an alternate compose file (default: docker-compose.yml)</p>
<dt><code>-p</code>, <code>&#8211;project-name</code> NAME</p>
<dd> Specify an alternate project name (default: directory name)</p>
<dt><code>&#8211;verbose</code></p>
<dd> Show more output</p>
<dt><code>-v</code>, <code>&#8211;version</code></p>
<dd> Print version and exit</dl>
<h2>COMMANDS</h2>
<h3>build</h3>
<p> Build or rebuild services</p>
<dl>
<dt><code>&#8211;no-cache</code></p>
<dd> Do not use cache when building the image.</dl>
<h3>help</h3>
<p> Displays help and usage information on a command.</p>
<h3>kill</h3>
<p> Forces running containers to stop by sending a SIGKILL signal.</p>
<dl>
<dt><code>-s</code> SIGNAL</p>
<dd> SIGNAL to send to the container. Default signal is SIGKILL.</dl>
<h3>logs</h3>
<p> View output from containers.</p>
<dl>
<dt><code>&#8211;no-color</code></p>
<dd> Produce a monochrome output.</dl>
<h3>port</h3>
<p> Print the public port for a port binding</p>
<dl>
<dt><code>&#8211;protocol=proto</code></p>
<dd> Choose the 4th layer protocol, tcp or udp. Default is tcp.</p>
<dt><code>&#8211;index=index</code></p>
<dd> Index of the container if there are multiple instances of a service. Default is 1.</dl>
<h3>ps</h3>
<p> List containers.</p>
<dl>
<dt><code>-q</code></p>
<dd> Only display IDs.</dl>
<h3>pull</h3>
<p> Pulls service images from Docker registry.</p>
<dl>
<dt><code>&#8211;allow-insecure-ssl</code></p>
<dd> Allow insecure connections to the Docker registry.</dl>
<h3>restart</h3>
<p> Restart running containers.</p>
<dl>
<dt><code>-t</code>, <code>&#8211;timeout</code> <i>TIMEOUT</i></p>
<dd> Specify a shutdown timeout in seconds. Default is 10.</dl>
<h3>rm</h3>
<p> Remove stopped service containers</p>
<dl>
<dt><code>-f</code>, <code>&#8211;force</code></p>
<dd> Do not ask to confirm removal.</p>
<dt><code>-v</code></p>
<dd> Remove volumes associated with containers.</dl>
<h3>run</h3>
<p> Run a one-off command on a service. By default linked services will be started, unless they are already running.</p>
<dl>
<dt><code>&#8211;allow-insecure-ssl</code></p>
<dd> Allow insecure connections to the Docker registry.</p>
<dt><code>-d</code></p>
<dd> Detached mode. Run container in the background, print new container name.</p>
<dt><code>&#8211;entrypoint</code> <i>CMD</i></p>
<dd> Override the entrypoint of the image with <i>CMD</i>.</p>
<dt><code>-e</code> KEY=VAL</p>
<dd> Set an environment variable. Can be used multiple times.</p>
<dt><code>-u</code>, <code>&#8211;user=</code><i>USER</i></p>
<dd> Run as a specific <i>USER</i>, a username or uid.</p>
<dt><code>&#8211;no-deps</code></p>
<dd> Do not start linked services.</p>
<dt><code>&#8211;rm</code></p>
<dd> Remove container after run. This option is ignored in the detached mode.</p>
<dt><code>&#8211;service-ports</code></p>
<dd> Run command with the service&#8217;s ports enabled and mapped to the host.</p>
<dt><code>-T</code></p>
<dd> Disable pseudo tty allocation. By default a tty is allocated.</dl>
<h3>scale</h3>
<p> Set number of containers to run for a service. Numbers are specified in the form <code>service=num</code> as arguments. </p>
<dl>
<dt>
<dd>
<pre>
# docker-compose scale web=2 worker=3
</dl>
</pre>
<h3>start</h3>
<p> Start existing containers.</p>
<h3>stop</h3>
<p> Stop running containers without removing them.</p>
<dl>
<dt><code>-t</code>, <code>&#8211;timeout</code> <i>TIMEOUT</i></p>
<dd> Specify a shutdown timeout in seconds. Default is 10.</dl>
<h3>up</h3>
<p> Build, (re)create, start and attach to containers. If there are existing containers for a service, `docker-compose up` will stop and recreate them (preserving mounted volumes with volumes-from), so that changes in `docker-compose.yml` are picked up. If you do not want existing containers to be recreated, `docker-compose up &#8211;no-recreate` will re-use existing containers.</p>
<dl>
<dt><code>&#8211;allow-insecure-ssl</code></p>
<dd> Allow insecure connections to the Docker registry.</p>
<dt><code>-d</code></p>
<dd> Detached mode. Run container in the background, print new container name.</p>
<dt><code>&#8211;no-color</code></p>
<dd> Produce a monochrome output.</p>
<dt><code>&#8211;no-deps</code></p>
<dd> Do not start linked services.</p>
<dt><code>&#8211;x-smart-recreate</code></p>
<dd> Only recreate containers whose configuration or image needs to be updated. This feature is experimental.</p>
<dt><code>&#8211;no-recreate</code></p>
<dd> If containers already exist, do not recreate them.</p>
<dt><code>&#8211;no-build</code></p>
<dd> Do not build an image even if it is missing.</p>
<dt><code>-t</code>, <code>&#8211;timeout</code> <i>TIMEOUT</i></p>
<dd> Specify a shutdown timeout in seconds. Default is 10.</dl>
<h3>migrate-to-labels</h3>
<p> Recreate containers to add labels. If docker-compose detects containers that were created without labels, it will refuse to run so that you don&#8217;t end up with two sets of them.</p>
<h2>ENVIRONMENTAL VARIABLES</h2>
<p> Several environmental variables are available to configure docker-compose behavior. </p>
<p> Variables starting with <i>DOCKER_</i> are the same as those used to configure the Docker command-line client. If you&#8217;re using boot2docker, <i>eval &quot;$(boot2docker shellinit)&quot;</i> will set them to their correct values. </p>
<h3>COMPOSE_PROJECT_NAME</h3>
<p> Sets the project name, which is prepended to the name of every container started by docker-compose. Defaults to the <i>basename</i> of the current working directory.</p>
<h3>COMPOSE_FILE</h3>
<p> Specify what file to read configuration from. If not provided, docker-compose will look for <i>docker-compose.yml</i> in the current working directory, and then each parent directory successively, until found.</p>
<h3>DOCKER_HOST</h3>
<p> Sets the URL of the docker daemon. As with the Docker client, defaults to <i><a href="unix:///var/run/docker.sock">unix:///var/run/docker.sock</a></i>.</p>
<h3>DOCKER_TLS_VERIFY</h3>
<p> When set to anything other than an empty string, enables TLS communication with the daemon.</p>
<h3>DOCKER_CERT_PATH</h3>
<p> Configures the path to the <i>ca.pem</i>, <i>cert.pem</i>, and <i>key.pem</i> files used for TLS verification. Defaults to <i>~/.docker</i>. </p>
<h2>SEE ALSO</h2>
<p> Full documentation for docker-compose at: &lt;<a rel="nofollow" href="http://docs.docker.com/compose/">http://docs.docker.com/compose/</a>&gt;</p>
<h2>AUTHOR</h2>
<p> This manual page was written by Dariusz Dwornikowski &lt;dariusz.dwornikowski [at] cs.put.poznan.pl&gt; based on the official docker compose documentation. </p>
<h2>Index</h2>
