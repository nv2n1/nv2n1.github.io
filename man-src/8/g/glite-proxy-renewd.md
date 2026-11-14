---
title: "glite-proxy-renewd(8)"
name: "glite-proxy-renewd"
section: "8"
letter: "g"
url: "/docs/linux/man/8-glite-proxy-renewd/"
description: "glite-proxy-renewd – proxy renewal daemon"
---

<p>glite-proxy-renewd &#8211; proxy renewal daemon</p>
<h2>Synopsis</h2>
<p><code>glite-proxy-renewd</code> [<i>options</i>] </p>
<h2>Description</h2>
<p><code>glite-proxy-renewd</code> registers X.509 proxy certificates and periodicaly renews them using a MyProxy repository. </p>
<h2>Options</h2>
<dl>
<dt><code>-A</code><i> DIR</i>, &#8211;VOMSdir <i>DIR</i></p>
<dd>Renew also VOMS attributes if they are embeded in the renewed proxy. If the option is given, the renewal daemon will retrieve a fresh copy of the VOMS attributes and place it inside the new proxy. </p>
<dt><code>-C</code><i> DIR</i>, &#8211;CAdir <i>DIR</i></p>
<dd>An alternative directory with trusted root anchors. This option overrides the $X509_USER_DIR environment variable. </p>
<dt><code>-c</code><i> NUM</i>, &#8211;condor-limit <i>NUM</i></p>
<dd>Specifies how many <i>NUM</i> seconds before expiration of a proxy should the renewal process be started. It defaults to 1800 seconds. </p>
<dt><code>-d</code><i></i>, &#8211;debug</p>
<dd>Don&#8217;t daemonize and start logging to stdout. Increased level of debugging is enabled, too. </p>
<dt><code>-G</code><i> FILE</i>, &#8211;voms-config <i>FILE</i></p>
<dd>An alternative location of the VOMS configuration. </p>
<dt><code>-h</code><i></i>, &#8211;help</p>
<dd>Display a list of valid options. </p>
<dt><code>-k</code><i> FILE</i>, &#8211;key <i>FILE</i></p>
<dd>Get certificate from <i>FILE</i>. This option overrides the $X509_USER_CERT environment variable. </p>
<dt><code>-O</code><i></i>, &#8211;order-attributes</p>
<dd>Make sure that the order of renewed VOMS attributes is retained. Enabling this option may cause crashes of old VOMS servers (older than 1.8.12). </p>
<dt><code>-r</code><i> DIR</i>, &#8211;repository <i>DIR</i></p>
<dd>All registered proxies and corresponding metadata will be stored in <i>repository</i>. The directory must exist and be writeable by the proxy renewal daemon. </p>
<dt><code>-t</code><i> FILE</i>, &#8211;cert <i>FILE</i></p>
<dd>Get private key from <i>FILE</i>. This option overrides the $X509_USER_KEY environment variable. </p>
<dt><code>-V</code><i> DIR</i>, &#8211;VOMSdir <i>DIR</i></p>
<dd>An alternative directory with trusted VOMS certificates </p>
<dt><code>-v</code><i></i>, &#8211;version</p>
<dd>Display the version of the proxy renewal daemon. </p>
</dl>
<h2>Files</h2>
<dl>
<dt><i>/tmp/dgpr_renew_&lt;uid&gt;</i></p>
<dd>A unix socket used to talk to the daemon. It is created the daemon upon its start </p>
<dt><i>proxy repository</i></p>
<dd>A directory containing all the registered proxy certificates and additional meta-data. </p>
<dt>There is no configuration file used the proxy renewal daemon.</p>
<dd></dl>
<h2>Environment</h2>
<dl>
<dt><code>GLITE_PR_TIMEOUT</code></p>
<dd>Sets the maximum number of seconds that the daemon can spend on serving the client over the unix socket. The default value is 120 seconds. </p>
<dt>Also, standard globus variables are honoured:</p>
<dd>
<dt><code>X509_USER_KEY</code></p>
<dd>If $X509_USER_KEY is set, it is used to locate the private key file. </p>
<dt><code>X509_USER_CERT</code></p>
<dd>If $X509_USER_CERT is set, it is used to locate the certificate file. </p>
<dt><code>X509_CERT_DIR</code></p>
<dd>If $X509_CERT_DIR is set, it is used to locate trusted CA&#8217;s certificates and ca-signing-policy files. </p>
</dl>
<h2>Bugs</h2>
<p>Please report all bugs to CESNET gLite Proxyrenewal issue tracker available at <i><a rel="nofollow" href="https://github.com/CESNET/proxyrenewal/issues">https://github.com/CESNET/proxyrenewal/issues</a></i> </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-glite-proxy-renew/">glite-proxy-renew</a></code>(1) </p>
<h2>Author</h2>
<p>EU EGEE, EU EMI</p>
