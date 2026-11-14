---
title: "oscap-docker(8)"
name: "oscap-docker"
section: "8"
letter: "o"
url: "/docs/linux/man/8-oscap-docker/"
description: "oscap-docker – Tool for running oscap within docker container or image"
---

<p>oscap-docker &#8211; Tool for running oscap within docker container or image</p>
<h2>Description</h2>
<p>oscap-docker tool can asses vulnerabilities or security compliance of running Docker containers or cold Docker images. OpenSCAP tool (oscap) is used underneath. Definition of vulnerabilities (CVE stream) is downloaded from product vendor.</p>
<h3>Compliance scan of Docker image</h3>
<p>Usage: oscap-docker image IMAGE_NAME [OSCAP_ARGUMENTS] Run any OpenSCAP (oscap) command within chroot of mounted docker image. Learn more about OSCAP_ARGUMENTS in <a href="/docs/linux/man/8-oscap/">oscap</a>(8) man page.</p>
<h3>Compliance scan of Docker container</h3>
<p>Usage: oscap-docker container CONTAINER_NAME [OSCAP_ARGUMENTS] Run any OpenSCAP (oscap) command within chroot of mounted docker container. Result of this command may differ from scanning just an image due to defined mount points.</p>
<h3>Vulnerability scan of Docker image</h3>
<p>Usage: oscap-docker image-cve IMAGE_NAME [&#8211;results oval-results-file.xml [&#8211;report report.html]] Attach docker image, determine OS variant/version, download CVE stream applicable to the given OS, and finally run vulnerability scan.</p>
<h3>Vulnerability scap of Docker container</h3>
<p>Usage: oscap-docker container-cve CONTAINER_NAME [&#8211;results oval-results-file.xml [&#8211;report report.html]] Chroot to running container, determine OS variant/version, download CVE stream applicable to the given OS and finally run a vulnerability scan. </p>
<h2>Security Policies</h2>
<dl>
<dt><code> SCAP-Security-Guide</code> package contains multiple configuration policies.</p>
<dd>
<dt><code> Red Hat CVE stream can be found online</code> &#8211; <i><a rel="nofollow" href="https://www.redhat.com/security/data/metrics/">https://www.redhat.com/security/data/metrics/</a></i></p>
<dd></dl>
<h2>Reporting Bugs</h2>
<pre>Please report bugs using <a rel="nofollow" href="https://github.com/OpenSCAP/openscap/issues">https://github.com/OpenSCAP/openscap/issues</a></pre>
<h2>Authors</h2>
<pre>Šimon Lukašík &lt;slukasik [at] redhat.com&gt;</pre>
