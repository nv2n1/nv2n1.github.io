---
title: "cimauth(8)"
name: "cimauth"
section: "8"
letter: "c"
url: "/docs/linux/man/8-cimauth/"
description: "cimauth – add, modify, remove, or list CIM namespace authorizations of users"
---

<p>cimauth &#8211; add, modify, remove, or list CIM namespace authorizations of users</p>
<h2>Synopsis</h2>
<p><code>cimauth</code> <code>-a</code> <code>-u</code> username <code>-n</code> namespace [ <code>-R</code> ] [ <code>-W</code> ] <code>cimauth</code> <code>-m</code> <code>-u</code> username <code>-n</code> namespace [ <code>-R</code> ] [ <code>-W</code> ] <code>cimauth</code> <code>-r</code> <code>-u</code> username [ <code>-n</code> namespace ] <code>cimauth</code> <code>-l</code> <code>cimauth</code> <code>-h</code> <code>cimauth</code> <code>&#8211;help</code> <code>cimauth</code> <code>&#8211;version</code> </p>
<h2>Description</h2>
<p>The <code>cimauth </code> command manages read and write CIM namespace authorizations of users. The operations are executed on the local host by submitting requests to the CIM Server. If the value of the configuration property <code>enableNamespaceAuthorization</code> is <code>True ,</code> the CIM Server restricts access to namespaces based on user authorizations configured via <code>cimauth . </code> Changes to &quot;Dynamic&quot; authorization parameters does not require the CIM Server to be restarted. &quot;Non Dynamic&quot; configuration properties (E.g. <code>enableNamespaceAuthorization</code> ) can only be set as planned configuration and the CIM Server needs to be restarted to realize the change. (See <code>cimconfig (8) </code> for information on configuring the CIM Server.)</p>
<h3>Options</h3>
<p>The <code>cimauth </code> command recognizes the following options:</p>
<dl>
<dd>
<dl>
<dt><code>-a</code></p>
<dd>Adds read and/or write authorizations to the specified user on the specified namespace. If neither the <code>-R</code> nor the <code>-W </code> option is specified, adds a read authorization by default.</p>
<dt><code>-h, &#8211;help</code></p>
<dd>Display command usage information.</p>
<dt><code>-l</code></p>
<dd>Lists all the authorizations configured in the CIM Server.</p>
<dt><code>-m</code></p>
<dd>Modifies authorizations of the specified user on the specified namespace. If neither the <code>-R </code> nor the <code>-W </code> option is specified, modifies the authorization to be a read authorization by default.</p>
<dt><code>-n</code> namespace</p>
<dd>Specifies the <i>R namespace </i> for the operation.</p>
<dt><code>-r</code></p>
<dd>Removes authorizations of the specified user on the specified namespace. If no namespaces are specified, removes authorizations on all namespaces for the specified user.</p>
<dt><code>-R</code></p>
<dd>Specifies read authorization on the namespace.</p>
<dt><code>-u</code> username</p>
<dd>Specifies the user for the operation. The specified <i>R username </i> must represent a valid user on the local host.</p>
<dt><code>&#8211;version</code></p>
<dd>Display CIM Server version number.</p>
<dt><code>-W</code></p>
<dd>Specifies write authorization on the namespace.</dl>
</dl>
<h2>Exit Status</h2>
<p>When an error occurs, an error message is written to stderr and an error value of 1 is returned. The following return values are returned:</p>
<dl>
<dd>
<dl>
<dt><code>0</code></p>
<dd>Successful completion</p>
<dt><code>1</code></p>
<dd>Error</dl>
</dl>
<h2>Usage Note</h2>
<p>The <code>cimauth </code> command requires that the CIM Server is running.</p>
<h2>Examples</h2>
<p>Add read authorizations to user &quot;guest&quot; on namespace &quot;root/cimv2&quot;.</p>
<dl>
<dd><code>cimauth -a -u guest -n root/cimv2 -R</code></dl>
<p> Add read and write authorizations to user &quot;guest&quot; on namespace &quot;root/system&quot;.</p>
<dl>
<dd><code>cimauth -a -u guest -n root/system -R -W</code></dl>
<p> Modify authorizations of the user &quot;guest&quot; on namespace &quot;root/system&quot; to read only.</p>
<dl>
<dd><code>cimauth -m -u guest -n root/system -R</code></dl>
<p> Remove the authorizations of the user &quot;guest&quot; on namespace &quot;root/system&quot;.</p>
<dl>
<dd><code>cimauth -r -u guest -n root/system</code></dl>
<p> List all the authorizations configured in the CIM Server.</p>
<dl>
<dd><code>cimauth -l</code></dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-cimserver/">cimserver</a>(8), <a href="/docs/linux/man/8-cimconfig/">cimconfig</a>(8). </p>
