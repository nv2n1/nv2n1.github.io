---
title: "nginx-upgrade(8)"
name: "nginx-upgrade"
section: "8"
letter: "n"
url: "/docs/linux/man/8-nginx-upgrade/"
---

nginx-upgrade - tool to upgrade nginx without any downtime

<h2>Synopsis</h2>

<i>nginx-upgrade</i>

<h2>Description</h2>

This downstream shell script updates nginx without any downtime. After upgrading nginx via the package manager, running this script will create a new nginx master. This master takes over all new requests. The old masters and workers are then gracefully shutdown without breaking any existing connections. 

 For further information, see: &lt;<a rel="nofollow" HREF="http://nginx.org/en/docs/control.html">http://nginx.org/en/docs/control.html</a>&gt;

<h2>Bugs</h2>

If you find any bugs, please send an email to the author.

<h2>Author</h2>

Jamie Nguyen &lt;jamielinux [at] fedoraproject.org&gt;
