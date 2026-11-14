---
title: "systemd-random-seed-service(8)"
name: "systemd-random-seed-service"
section: "8"
letter: "s"
url: "/docs/linux/man/8-systemd-random-seed-service/"
description: "systemd-random-seed.service, systemd-random-seed – Load and save the system random seed at boot and shutdown"
---

<p>systemd-random-seed.service, systemd-random-seed &#8211; Load and save the system random seed at boot and shutdown</p>
<h2>Synopsis</h2>
<p>systemd-random-seed.service </p>
<p> /usr/lib/systemd/random-seed</p>
<h2>Description</h2>
<p>systemd-random-seed.service is a service that loads an on-disk random seed into the kernel entropy pool during boot and saves it at shutdown. See <code><a href="/docs/linux/man/4-random/">random</a></code>(4) for details. By default, no entropy is credited when the random seed is written into the kernel entropy pool, but this may be changed with <i>$SYSTEMD_RANDOM_SEED_CREDIT</i>, see below. On disk the random seed is stored in /var/lib/systemd/random-seed. </p>
<p> Note that this service runs relatively late during the early boot phase, i.e. generally after the initial RAM disk (initrd) completed its work, and the /var/ file system has been mounted writable. Many system services require entropy much earlier than this &#8212; this service is hence of limited use for complex system. It is recommended to use a boot loader that can pass an initial random seed to the kernel to ensure that entropy is available from earliest boot on, for example <code><a href="/docs/linux/man/7-systemd-boot/">systemd-boot</a></code>(7), with its <code>bootctl random-seed</code> functionality. </p>
<p> When loading the random seed from disk, the file is immediately updated with a new seed retrieved from the kernel, in order to ensure no two boots operate with the same random seed. This new seed is retrieved synchronously from the kernel, which means the service will not complete start-up until the random pool is fully initialized. On entropy-starved systems this may take a while. This functionality is intended to be used as synchronization point for ordering services that require an initialized entropy pool to function securely (i.e. services that access /dev/urandom without any further precautions). </p>
<p> Care should be taken when creating OS images that are replicated to multiple systems: if the random seed file is included unmodified each system will initialize its entropy pool with the same data, and thus &#8212; if otherwise entropy-starved &#8212; generate the same or at least guessable random seed streams. As a safety precaution crediting entropy is thus disabled by default. It is recommended to remove the random seed from OS images intended for replication on multiple systems, in which case it is safe to enable entropy crediting, see below. </p>
<p> See m[blue]<code>Random Seeds</code>m[]<font SIZE="-2">[1]</font> for further information.</p>
<h2>Environment</h2>
<p><i>$SYSTEMD_RANDOM_SEED_CREDIT</i></p>
<dl>
<dd>By default, systemd-random-seed.service does not credit any entropy when loading the random seed. With this option this behaviour may be changed: it either takes a boolean parameter or the special string &quot;force&quot;. Defaults to false, in which case no entropy is credited. If true, entropy is credited if the random seed file and system state pass various superficial concisistency checks. If set to &quot;force&quot; entropy is credited, regardless of these checks, as long as the random seed file exists.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/4-random/">random</a></code>(4), <code><a href="/docs/linux/man/7-systemd-boot/">systemd-boot</a></code>(7), <code><a href="/docs/linux/man/4-bootctl/">bootctl</a></code>(4)</p>
<h2>Notes</h2>
<dl>
<dt> 1.</p>
<dd>Random Seeds</p>
<dl>
<dd><a rel="nofollow" href="https://systemd.io/RANDOM_SEEDS">https://systemd.io/RANDOM_SEEDS</a></dl>
