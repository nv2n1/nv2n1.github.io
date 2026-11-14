---
title: "rhsm-debug(8)"
name: "rhsm-debug"
section: "8"
letter: "r"
url: "/docs/linux/man/8-rhsm-debug/"
description: "rhsm-debug – Compiles information about system’s entitlements, products, and identity used by Red Hat Subscription Manager."
---

<p>rhsm-debug &#8211; Compiles information about system&#8217;s entitlements, products, and identity used by Red Hat Subscription Manager. </p>
<h2>Synopsis</h2>
<p>rhsm-debug <i>module [options]</i> </p>
<h2>Description</h2>
<p><code>rhsm-debug</code> compiles information about system&#8217;s entitlements, products, and identity used by Red Hat Subscription Manager. </p>
<h2>Commands And Options</h2>
<p><code>rhsm-debug</code> has specific options available for each module, depending on what operation is being performed. The currently supported modules are: </p>
<dl>
<dd>1. system </p>
</dl>
<h3>Common Options</h3>
<dl>
<dt><code>-h, &#8211;help</code></p>
<dd>Prints the specific help information for the given command. </p>
<dt><code>&#8211;proxy=PROXY</code></p>
<dd>Uses an HTTP proxy. The <i>PROXY</i> name has the format <i>hostname:port.</i> </p>
<dt><code>&#8211;proxyuser=PROXYUSERNAME</code></p>
<dd>Gives the username to use to authenticate to the HTTP proxy. </p>
<dt><code>&#8211;proxypassword=PROXYPASSWORD</code></p>
<dd>Gives the password to use to authenticate to the HTTP proxy. </p>
</dl>
<h3>System Options</h3>
<p>The <code>system</code> command pulls in debug information off of the current system </p>
<dl>
<dt><code>&#8211;destination=DESTINATION</code></p>
<dd>The directory to place the resulting debug data. The default is /tmp. </p>
<dt><code>&#8211;no-archive</code></p>
<dd>Generates an uncompressed directory instead of a gzipped file. </p>
<dt><code>&#8211;sos</code></p>
<dd>Excludes data files that are also collected by the sosreport tool. </p>
</dl>
<h2>Bugs</h2>
<p>This tool is part of Red Hat Subscription Manager. To file bugs against this command-line tool, go to &lt;<a rel="nofollow" href="https://bugzilla.redhat.com">https://bugzilla.redhat.com</a>&gt;, and select Red Hat &gt; Red Hat Enterprise Linux &gt; subscription-manager. </p>
<h2>Authors</h2>
<p>William Poteat&lt;wpoteat [at] redhat.com&gt;. The rhsm-debug tool was written by William Poteat.</p>
<h2>Copyright</h2>
<p>Copyright (c) 2012 Red Hat, Inc. This is licensed under the GNU General Public License, version 2 (GPLv2). A copy of this license is available at <a rel="nofollow" href="http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt.">http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt.</a></p>
