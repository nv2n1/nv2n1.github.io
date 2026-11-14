---
title: "pam_env(7)"
name: "pam_env"
section: "7"
letter: "p"
url: "/docs/linux/man/7-pam_env/"
description: "pam_env – PAM module to set/unset environment variables"
---

<p>pam_env &#8211; PAM module to set/unset environment variables</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>pam_env.so</code> [debug] [conffile=<i>conf-file</i>] [envfile=<i>env-file</i>] [readenv=<i>0|1</i>] [user_envfile=<i>env-file</i>] [user_readenv=<i>0|1</i>]</dl>
<h2>Description</h2>
<dd>The pam_env PAM module allows the (un)setting of environment variables. Supported is the use of previously set environment variables as well as <i>PAM_ITEM</i>s such as <i>PAM_RHOST</i>. </p>
<p> By default rules for (un)setting of variables are taken from the config file /etc/security/pam_env.conf. An alternate file can be specified with the <i>conffile</i> option. </p>
<p> Second a file (/etc/environment by default) with simple <i>KEY=VAL</i> pairs on separate lines will be read. With the <i>envfile</i> option an alternate file can be specified. And with the <i>readenv</i> option this can be completely disabled. </p>
<p> Third it will read a user configuration file ($HOME/.pam_environment by default). The default file can be changed with the <i>user_envfile</i> option and it can be turned on and off with the <i>user_readenv</i> option. </p>
<p> Since setting of PAM environment variables can have side effects to other modules, this module should be the last one on the stack.</p>
<h2>Options</h2>
<p><code>conffile=</code><i>/path/to/pam_env.conf</i></p>
<dl>
<dd>Indicate an alternative pam_env.conf style configuration file to override the default. This can be useful when different services need different environments.</dl>
<p> <code>debug</code></p>
<dl>
<dd>A lot of debug information is printed with <code><a href="/docs/linux/man/3-syslog/">syslog</a></code>(3).</dl>
<p> <code>envfile=</code><i>/path/to/environment</i></p>
<dl>
<dd>Indicate an alternative environment file to override the default. The syntax are simple <i>KEY=VAL</i> pairs on separate lines. The <i>export</i> instruction can be specified for bash compatibility, but will be ignored. This can be useful when different services need different environments.</dl>
<p> <code>readenv=</code><i>0|1</i></p>
<dl>
<dd>Turns on or off the reading of the file specified by envfile (0 is off, 1 is on). By default this option is on.</dl>
<p> <code>user_envfile=</code><i>filename</i></p>
<dl>
<dd>Indicate an alternative .pam_environment file to override the default.The syntax is the same as for <i>/etc/security/pam_env.conf</i>. The filename is relative to the user home directory. This can be useful when different services need different environments.</dl>
<p> <code>user_readenv=</code><i>0|1</i></p>
<dl>
<dd>Turns on or off the reading of the user specific environment file. 0 is off, 1 is on. By default this option is off.</dl>
<h2>Module Types Provided</h2>
<p>The <code>auth</code> and <code>session</code> module types are provided.</p>
<h2>Return Values</h2>
<p>PAM_ABORT</p>
<dl>
<dd>Not all relevant data or options could be gotten.</dl>
<p> PAM_BUF_ERR</p>
<dl>
<dd>Memory buffer error.</dl>
<p> PAM_IGNORE</p>
<dl>
<dd>No pam_env.conf and environment file was found.</dl>
<p> PAM_SUCCESS</p>
<dl>
<dd>Environment variables were set.</dl>
<h2>Files</h2>
<p>/etc/security/pam_env.conf</p>
<dl>
<dd>Default configuration file</dl>
<p> /etc/environment</p>
<dl>
<dd>Default environment file</dl>
<p> $HOME/.pam_environment</p>
<dl>
<dd>User specific environment file</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-pam_env-conf/">pam_env.conf</a></code>(5), <code><a href="/docs/linux/man/5-pam-d/">pam.d</a></code>(5), <code><a href="/docs/linux/man/8-pam/">pam</a></code>(8), <code><a href="/docs/linux/man/7-environ/">environ</a></code>(7).</p>
<h2>Author</h2>
<p>pam_env was written by Dave Kinchlea &lt;kinch [at] kinch.ark.com&gt;.</p>
