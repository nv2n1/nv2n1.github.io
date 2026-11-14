---
title: "ssh-argv0(1)"
name: "ssh-argv0"
section: "1"
letter: "s"
url: "/docs/linux/man/1-ssh-argv0/"
description: "ssh-argv0 – replaces the old ssh command-name as hostname handling"
---

<p>Debian Project</p>
<h2 class="name">NAME</h2>
<p> <code>ssh-argv0</code> &#8211; replaces the old ssh command-name as hostname handling </p>
<h2>SYNOPSIS</h2>
<p> <i>hostname | user [at] hostname</i> [-<code>l </code><i>login_name</i> ] [<i>command</i> ] </p>
<p> <i>hostname | user [at] hostname</i> [-<code>afgknqstvxACNTX1246</code> ] [-<code>b </code><i>bind_address</i> ] [-<code>c </code><i>cipher_spec</i> ] [-<code>e </code><i>escape_char</i> ] [-<code>i </code><i>identity_file</i> ] [-<code>l </code><i>login_name</i> ] [-<code>m </code><i>mac_spec</i> ] [-<code>o </code><i>option</i> ] [-<code>p </code><i>port</i> ] [-<code>F </code><i>configfile</i> ] [-<code>L </code> <i>port</i> <i>host</i> <i>hostport</i> ] [-<code>R </code> <i>port</i> <i>host</i> <i>hostport</i> ] [-<code>D </code><i>port</i> ] [<i>command</i> ]</p>
<h2>DESCRIPTION</h2>
<p> <code>ssh-argv0</code> replaces the old ssh command-name as hostname handling. If you link to this script with a hostname then executing the link is equivalent to having executed ssh with that hostname as an argument. All other arguments are passed to ssh and will be processed normally.</p>
<h2>OPTIONS</h2>
<p> See <a href="/docs/linux/man/1-ssh/">ssh</a>(1).</p>
<h2>FILES</h2>
<p> See <a href="/docs/linux/man/1-ssh/">ssh</a>(1).</p>
<h2>AUTHORS</h2>
<p> OpenSSH is a derivative of the original and free ssh 1.2.12 release by Tatu Ylonen. Aaron Campbell, Bob Beck, Markus Friedl, Niels Provos, Theo de Raadt and Dug Song removed many bugs, re-added newer features and created OpenSSH. Markus Friedl contributed the support for SSH protocol versions 1.5 and 2.0. Natalie Amery wrote this ssh-argv0 script and the associated documentation.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-ssh/">ssh</a>(1) </p>
<h2>Index</h2>
