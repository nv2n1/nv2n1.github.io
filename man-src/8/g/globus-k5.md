---
title: "globus-k5(8)"
name: "globus-k5"
section: "8"
letter: "g"
url: "/docs/linux/man/8-globus-k5/"
description: "globus-k5 – Acquire Kerberos Credentials for use with Grid Services"
---

<p>globus-k5 &#8211; Acquire Kerberos Credentials for use with Grid Services</p>
<h2>Synopsis</h2>
<p><code>globus-k5</code> <i>SERVICE-COMMAND</i> <i>SERVICE-ARGS</i>&#8230;</p>
<h2>Description</h2>
<p>The <code>globus-k5</code> program is an authorization module used by the globus-gatekeeper program to acquire Kerberos 5 Credentials prior to executing a Grid Service. This may be accomplished by running <code>kinit</code> with a password stored in the globuskmap file, using the NCSA <code>krb525</code> command, or the <code>sslk5</code> command to use the X509 user proxy. </p>
<p> The arguments passed to <code>globus-k5</code> will not be used by it, but will be passed onto the job manager. The first parameter must be the path to the Grid Service. </p>
<p> It is expected that the environment will contain the variables GLOBUSID and USER for the Grid and local POSIX user identities. This program is normally run as root, and will call seteuid() prior to executing the Grid Service. </p>
<p> The parameters to use and the mapping for the globus to K5 user are located in the globuskmap file.</p>
<h3>Format of the globuskmap file</h3>
<p>The globuskmap file is a line-oriented file which each line containing a command to run to acquire Kerberos 5 credentials for a Grid identity. Each line consists of an optionally-quoted <i>GLOBUSID</i> value followed by a command-line for running a process to acquire a Kerberos credential. For example: </p>
<dl>
<dd>
<pre>&quot;/O=Example/OU=Grid/CN=Joe User&quot; /usr/afsws/bin/klog -principal juser -password mypasswd -cell infn.it</pre>
</dl>
<h2>Environment</h2>
<p>The following variables affect the execution of <code>globus-k5</code>: </p>
<p> <code>GLOBUSKMAP</code></p>
<dl>
<dd>Path to the globuskmap file.</dl>
<p> <code>USER</code></p>
<dl>
<dd>POSIX username that the service will run as.</dl>
<p> <code>KRB5CCNAME</code></p>
<dl>
<dd>Path to a Kerberos credential cache.</dl>
<p> <code>GLOBUS_ID</code></p>
<dl>
<dd>Grid identity to generate Kerberos credentials for.</dl>
<h2>Files</h2>
<p>The following files affect the execution of <code>globus-k5</code>: </p>
<p> <code>/etc/globuskmap</code></p>
<dl>
<dd>Default file mapping Grid identities to Kerberos 5 principals.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-globus-k5/">globus-k5</a></code>(8), <code><a href="/docs/linux/man/8-globus-job-manager/">globus-job-manager</a></code>(8)</p>
<h2>Author</h2>
<p>Copyright &#169; 1999-2016 University of Chicago</p>
