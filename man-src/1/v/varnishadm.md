---
title: "varnishadm(1)"
name: "varnishadm"
section: "1"
letter: "v"
url: "/docs/linux/man/1-varnishadm/"
description: "varnishadm – Control a running Varnish instance"
---

<h2>NAME</h2>
<p> varnishadm &#8211; Control a running Varnish instance</p>
<h2>SYNOPSIS</h2>
<p> varnishadm [-t timeout] [-S secret_file] [-T address:port] [-n name] [command [&#8230;]]</p>
<h2>DESCRIPTION</h2>
<p> The varnishadm utility establishes a CLI connection to varnishd either using -n <i>name</i> or using the -T and -S arguments. If -n <i>name</i> is given the location of the secret file and the address:port is looked up in shared memory. If neither is given varnishadm will look for an instance without a given name. </p>
<p> If a command is given, the command and arguments are sent over the CLI connection and the result returned on stdout. </p>
<p> If no command argument is given varnishadm will pass commands and replies between the CLI socket and stdin/stdout.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-t</code><i>&nbsp;<wbr>timeout</i></p>
<dd> Wait no longer than this many seconds for an operation to finish.</p>
<dt><code>-S</code><i>&nbsp;<wbr>secret_file</i></p>
<dd> Specify the authentication secret file. This should be the same -S argument as was given to varnishd. Only processes which can read the contents of this file, will be able to authenticate the CLI connection.</p>
<dt><code>-n</code><i>&nbsp;<wbr>name</i></p>
<dd> Connect to the instance of varnishd with this name.</p>
<dt><code>-T address:port</code></p>
<dd> Connect to the management interface at the specified address and port. </p>
<p> The syntax and operation of the actual CLI interface is described in the <a href="/docs/linux/man/7-varnish-cli/">varnish-cli</a>(7) manual page. Parameteres are described in <a href="/docs/linux/man/1-varnishd/">varnishd</a>(1) manual page. </p>
<p> Additionally, a summary of commands can be obtained by issuing the <i>help</i> command, and a summary of parameters can be obtained by issuing the <i>param.show</i> command.</dl>
<h2>EXIT STATUS</h2>
<p> If a command is given, the exit status of the varnishadm utility is zero if the command succeeded, and non-zero otherwise.</p>
<h2>EXAMPLES</h2>
<p> Some ways you can use varnishadm: </p>
<pre>
varnishadm -T localhost:999 -S /var/db/secret vcl.use foo
echo vcl.use foo | varnishadm -T localhost:999 -S /var/db/secret
echo vcl.use foo | ssh vhost varnishadm -T localhost:999 -S /var/db/secret
</pre>
<h2>SEE ALSO</h2>
<dl>
<dt>&bull;</p>
<dd> <a href="/docs/linux/man/1-varnishd/">varnishd</a>(1)</dl>
<h2>HISTORY</h2>
<p> The varnishadm utility and this manual page were written by Cecilie Fritzvold. Converted to reStructuredText and updated in 2010 by Per Buer.</p>
<h2>COPYRIGHT</h2>
<p> This document is licensed under the same licence as Varnish itself. See LICENCE for details.</p>
<dl>
<dt>&bull;</p>
<dd> Copyright (c) 2007-2014 Varnish Software AS </p>
</dl>
<h2>Index</h2>
