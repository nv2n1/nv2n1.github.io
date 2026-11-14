---
title: "atomic(1)"
name: "atomic"
section: "1"
letter: "a"
url: "/docs/linux/man/1-atomic/"
description: "atomic – Atomic Management Tool"
---

<h2 class="name">NAME</h2>
<p> atomic &#8211; Atomic Management Tool </p>
<h2>SYNOPSIS</h2>
<p> <code>atomic</code> [OPTIONS] COMMAND [arg&#8230;]<br />
&nbsp;<wbr>&nbsp;<wbr>{containers,diff,images,install,mount,pull,push,run,scan,sign,stop,storage,migrate,top,trust,uninstall,unmount,umount,update,verify,version} </p>
<p> [<code>-h</code>|<code>&#8211;help</code>] </p>
<h2>DESCRIPTION</h2>
<p> Atomic Management Tool </p>
<h2>OPTIONS</h2>
<p> <code>-h</code> <code>&#8211;help</code><br />
&nbsp;<wbr>&nbsp;<wbr>Print usage statement </p>
<p> <code>-v</code> <code>&#8211;version</code><br />
&nbsp;<wbr>&nbsp;<wbr>Show atomic version </p>
<p> <code>&#8211;debug</code><br />
&nbsp;<wbr>&nbsp;<wbr>Show debug messages </p>
<p> <code>-y</code> <code>&#8211;assumeyes</code><br />
&nbsp;<wbr>&nbsp;<wbr>automatically answer yes for all questions </p>
<h2>ENVIRONMENT VARIABLES</h2>
<p> <code>ATOMIC_CONF</code> The location of the atomic configuration file (normally /etc/atomic.conf) can be overridden with the <i>ATOMIC_CONF</i> environment variable </p>
<p> <code>ATOMIC_CONFD</code> The location of the atomic configuration directory (normally /etc/atomic.d/) can be overridden with the <i>ATOMIC_CONFD</i> environment variable. </p>
<h2>COMMANDS</h2>
<p> <code><a href="/docs/linux/man/1-atomic-containers/">atomic-containers</a>(1)</code> operations on installed containers </p>
<p> <code><a href="/docs/linux/man/1-atomic-diff/">atomic-diff</a>(1)</code> show the differences between two images|containers&#8217; RPMs </p>
<p> <code><a href="/docs/linux/man/1-atomic-host/">atomic-host</a>(1)</code> execute commands to manage an Atomic host. </p>
<p> Note: only available on atomic host platforms. </p>
<p> <code><a href="/docs/linux/man/1-atomic-images/">atomic-images</a>(1)</code> operations on container images </p>
<p> <code><a href="/docs/linux/man/1-atomic-install/">atomic-install</a>(1)</code> execute commands on installed images </p>
<p> <code><a href="/docs/linux/man/1-atomic-mount/">atomic-mount</a>(1)</code> mount image or container to filesystem </p>
<p> <code><a href="/docs/linux/man/1-atomic-pull/">atomic-pull</a>(1)</code> pull latest image from repository </p>
<p> <code><a href="/docs/linux/man/1-atomic-push/">atomic-push</a>(1)</code> push container image to a repository </p>
<p> <code><a href="/docs/linux/man/1-atomic-run/">atomic-run</a>(1)</code> execute image run method (default) </p>
<p> <code><a href="/docs/linux/man/1-atomic-scan/">atomic-scan</a>(1)</code> scan an image or container for CVEs </p>
<p> <code><a href="/docs/linux/man/1-atomic-sign/">atomic-sign</a>(1)</code> sign an image </p>
<p> <code><a href="/docs/linux/man/1-atomic-stop/">atomic-stop</a>(1)</code> execute container image stop method </p>
<p> <code><a href="/docs/linux/man/1-atomic-storage/">atomic-storage</a>(1)</code> manage the container storage on the system </p>
<p> <code><a href="/docs/linux/man/1-atomic-top/">atomic-top</a>(1)</code> display a top-like list of container processes </p>
<p> <code><a href="/docs/linux/man/1-atomic-trust/">atomic-trust</a>(1)</code> manage system container trust policy </p>
<p> <code><a href="/docs/linux/man/1-atomic-uninstall/">atomic-uninstall</a>(1)</code> uninstall container from system </p>
<p> <code><a href="/docs/linux/man/1-atomic-unmount/">atomic-unmount</a>(1)</code> unmount previously mounted image or container </p>
<p> <code><a href="/docs/linux/man/1-atomic-update/">atomic-update</a>(1)</code> Downloads the latest container image. </p>
<h2>CONNECTING TO DOCKER ENGINE</h2>
<p> By default, atomic command connects to docker engine via UNIX domain socket located at /var/run/docker.sock. You can use different connection method via setting several environment variables: </p>
<p> <code>DOCKER_HOST</code> — this variable specifies connection string. If your engine listens on UNIX domain socket, you can specify the path via http+unix://&lt;path&gt;, e.g. http+<a href="unix://var/run/docker2.sock.">unix://var/run/docker2.sock.</a> For TCP the string has this form: tcp://&lt;ip&gt;:&lt;port&gt;, e.g. <a href="tcp://127.0.0.1:2375">tcp://127.0.0.1:2375</a> </p>
<p> <code>DOCKER_TLS_VERIFY</code> — enables TLS verification if it contains any value, otherwise it disables the verification </p>
<p> <code>DOCKER_CERT_PATH</code> — path to directory with TLS certificates, files in the directory need to have specific names: </p>
<p> <code>cert.pem</code> — client certificate </p>
<p> <code>key.pem</code> — client key </p>
<p> <code>ca.pem</code> — CA certificate </p>
<p> For more info, please visit upstream docs: </p>
<p> <code> &lt;<a rel="nofollow" href="https://docs.docker.com/engine/security/https/">https://docs.docker.com/engine/security/https/</a>&gt;</code><br />
 <code> &lt;<a rel="nofollow" href="https://docs.docker.com/machine/reference/env/">https://docs.docker.com/machine/reference/env/</a>&gt;</code> </p>
<h2>HISTORY</h2>
<p> January 2015, Originally compiled by Daniel Walsh (dwalsh at redhat dot com) November, 2015 Addition of scan and diff by Brent Baude (bbaude at dot com) </p>
<h2>Index</h2>
