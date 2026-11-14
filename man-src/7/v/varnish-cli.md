---
title: "varnish-cli(7)"
name: "varnish-cli"
section: "7"
letter: "v"
url: "/docs/linux/man/7-varnish-cli/"
description: "Varnish CLI – Varnish Command Line Interface"
---

<p>Varnish CLI &#8211; Varnish Command Line Interface</p>
<h2>Description</h2>
<p>Varnish as a command line interface (CLI) which can control and change most of the operational parameters and the configuration of Varnish, without interrupting the running service. </p>
<p> The CLI can be used for the following tasks:</p>
<dl>
<dt><code>configuration</code></p>
<dd>You can upload, change and delete VCL files from the CLI.</p>
<dt><code>parameters</code></p>
<dd>You can inspect and change the various parameters Varnish has available through the CLI. The individual parameters are documented in the <a href="/docs/linux/man/1-varnishd/">varnishd</a>(1) man page.</p>
<dt><code>bans</code></p>
<dd>Bans are filters that are applied to keep Varnish from serving stale content. When you issue a ban Varnish will not serve any <i>banned</i> object from cache, but rather re-fetch it from its backend servers.</p>
<dt><code>process management</code></p>
<dd>You can stop and start the cache (child) process though the CLI. You can also retrieve the lastst stack trace if the child process has crashed. </p>
<p> If you invoke <a href="/docs/linux/man/1-varnishd/">varnishd</a>(1) with -T, -M or -d the CLI will be available. In debug mode (-d) the CLI will be in the foreground, with -T you can connect to it with varnishadm or telnet and with -M varnishd will connect back to a listening service <i>pushing</i> the CLI to that service. Please see <a href="/docs/linux/man/1-varnishd/">varnishd</a>(1) for details.</dl>
<h3>Syntax</h3>
<p>Commands are usually terminated with a newline. Long command can be entered using sh style <i>here documents</i>. The format of here-documents is: </p>
<pre>&lt;&lt; word
 here document
word</pre>
<p><i>word</i> can be any continuous string choosen to make sure it doesn&#8217;t appear naturally in the following <i>here document</i>. </p>
<p> When using the here document style of input there are no restrictions on lenght. When using newline-terminated commands maximum lenght is limited by the varnishd parameter <i>cli_buffer</i>. </p>
<p> When commands are newline terminated they get <i>tokenized</i> before parsing so if you have significant spaces enclose your strings in double quotes. Within the quotes you can escape characters with \. The n, r and t get translated to newlines, carrage returns and tabs. Double quotes themselves can be escaped with a backslash. </p>
<p> To enter characters in octals use the 
nn syntax. Hexadecimals can be entered with the 
