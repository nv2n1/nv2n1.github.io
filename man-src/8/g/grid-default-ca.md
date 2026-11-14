---
title: "grid-default-ca(8)"
name: "grid-default-ca"
section: "8"
letter: "g"
url: "/docs/linux/man/8-grid-default-ca/"
description: "grid-default-ca – Select default CA for certificate requests"
---

<p>grid-default-ca &#8211; Select default CA for certificate requests</p>
<h2>Synopsis</h2>
<p><code>grid-default-ca</code> -help | -h | -usage | -u | -version | -versions </p>
<p> <code>grid-default-ca</code> [-ca <i>CA-HASH</i> | -list ] [OPTIONS]</p>
<h2>Description</h2>
<p>The <code>grid-default-ca</code> program sets the default certificate authority to use when the <code>grid-cert-request</code> script is run. The CA&#8217;s certificate, configuration, and signing policy must be installed in the trusted certificate directory to be able to request certificates from that CA. Note that some CAs have different policies and use other tools to handle certificate requests. Please consult your CA&#8217;s support staff if you unsure. The <code>grid-default-ca</code> is designed to work with CAs implemented using the <code>globus_simple_ca</code> package. </p>
<p> By default, the <code>grid-default-ca</code> program displays a list of installed CA certificates and the prompts the user for which one to set as the default. If invoked with the <i>-list</i> command-line option, <code>grid-default-ca</code> will print the list and not prompt nor set the default CA. If invoked with the <i>-ca</i> option, it will not list or prompt, but set the default CA to the one with the hash that matches the <i>CA-HASH</i> argument to that option. If <code>grid-default-ca</code> is used to set the default CA, the caller of this program must have write permissions to the trusted certificate directory. </p>
<p> The <code>grid-default-ca</code> program sets the CA in the one of the grid security directories. It looks in the directory named by the GRID_SECURITY_DIR environment, the X509_CERT_DIR environment, /etc/grid-security and $GLOBUS_LOCATION/share/certificates.</p>
<h2>Options</h2>
<p>The full set of command-line options to <code>grid-default-ca</code> are: </p>
<p> <code>-help, -h, -usage, -u</code></p>
<dl>
<dd>Display the command-line options to <code>grid-default-ca</code> and exit.</dl>
<p> <code>-version, -versions</code></p>
<dl>
<dd>Display the version number of the <code>grid-default-ca</code> command. The second form includes more details.</dl>
<p> <code>-dir </code><i>CA-DIRECTORY</i></p>
<dl>
<dd>Use the trusted certificate directory named by <i>CA-DIRECTORY</i> instead of the default.</dl>
<p> <code>-list</code></p>
<dl>
<dd>Instead of changing the default CA, print out a list of all available CA certificates in the trusted certificate directory.</dl>
<p> <code>-ca </code><i>CA-HASH</i></p>
<dl>
<dd>Set the default CA without displaying the list of choices or prompting. The CA file named by <i>CA-HASH</i> must exist.</dl>
<h2>Examples</h2>
<p>List the contents of the trusted certificate directory that contain the string Example: </p>
<dl>
<dd>
<pre>% grid-default-ca | grep Example
15) cd1186ff - /DC=org/DC=Example/DC=Grid/CN=Example CA</pre>
</dl>
<p> Choose that CA as the default: </p>
<dl>
<dd>
<pre>% grid-default-ca -ca cd1186ff
setting the default CA to: /DC=org/DC=Example/DC=Grid/CN=Example CA
linking /etc/grid-security/certificates/grid-security.conf.cd1186ff to
 /etc/grid-security/certificates/grid-security.conf
linking /etc/grid-security/certificates/grid-host-ssl.conf.cd1186ff to
 /etc/grid-security/certificates/grid-host-ssl.conf
linking /etc/grid-security/certificates/grid-user-ssl.conf.cd1186ff to
 /etc/grid-security/certificates/grid-user-ssl.conf
...done.</pre>
</dl>
<h2>Environment</h2>
<p>The following environment variables affect the execution of <code>grid-default-ca</code>: <code>GRID_SECURITY_DIRECTORY</code>:: Path to the default trusted certificate directory. <code>X509_CERT_DIR</code>:: Path to the default trusted certificate directory. <code>GLOBUS_LOCATION</code>:: Path to the Globus Toolkit installation directory.</p>
<h2>Bugs</h2>
<p>The <code>grid-default-ca</code> program displays CAs from all of the directories in its search list; however, <code>grid-cert-request</code> only uses the first which contains a grid security configuration. </p>
<p> The <code>grid-default-ca</code> program may display the same CA multiple times if it is located in multiple directories in its search path. However, it does not provide any information about which one would actually be used by the <code>grid-cert-request</code> command.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-grid-cert-request/">grid-cert-request</a>(1)</p>
<h2>Author</h2>
<p>Copyright &#169; 1999-2014 University of Chicago</p>
