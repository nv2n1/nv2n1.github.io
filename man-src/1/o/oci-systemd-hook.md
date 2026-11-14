---
title: "oci-systemd-hook(1)"
name: "oci-systemd-hook"
section: "1"
letter: "o"
url: "/docs/linux/man/1-oci-systemd-hook/"
---

<h2>SYNOPSIS</h2>

 

 oci-systemd-hook prestart [container.json] 

 

 oci-systemd-hook poststop 

<h2>DESCRIPTION</h2>

 

 Setup environment for systemd to run in docker or a OCI compatible runtime. It is expected to receive the state of the container including the pid and ID over stdin as defined in the OCI specification ( &lt;<a rel="nofollow" HREF="https://github.com/opencontainers/specs">https://github.com/opencontainers/specs</a>&gt;). It mounts tmpfs at /run and /tmp, links journal directory to the host using a bind mount and creates /etc/machine-id for the container systemd. 

<h2>ARGUMENTS.IP step]</h2>

 

 item 

 prestart: Setup the systemd environment in a container item 

 container.json: file which describes the container. oci-systemd-hook will examine the json data for the CMD option and only setup the environment if the CMD is init or systemd. Only available on prestart. item 

 poststop: Teardown and undo the changes on the host done during prestart

<h2>AUTHORS</h2>

 

 Mrunal Patel &lt;mrunalp [at] gmail.com&gt; Dan Walsh &lt;dwalsh [at] redhat.com&gt; 

<h2>Index</h2>


