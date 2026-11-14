---
title: "nss(5)"
name: "nss"
section: "5"
letter: "n"
url: "/docs/linux/man/5-nss/"
description: "nss – Name Service Switch configuration file"
---

<p>nss &#8211; Name Service Switch configuration file</p>
<h2>Description</h2>
<p>Each call to a function which retrieves data from a system database like the password or group database is handled by the Name Service Switch implementation in the GNU C library. The various services provided are implemented by independent modules, each of which naturally varies widely from the other. </p>
<p> The default implementations coming with the GNU C library are by default conservative and do not use unsafe data. This might be very costly in some situations, especially when the databases are large. Some modules allow the system administrator to request taking shortcuts if these are known to be safe. It is then the system administrator&#8217;s responsibility to ensure the assumption is correct. </p>
<p> There are other modules where the implementation changed over time. If an implementation used to sacrifice speed for memory consumption, it might create problems if the preference is switched. </p>
<p> The <i>/etc/default/nss</i> file contains a number of variable assignments. Each variable controls the behavior of one or more NSS modules. White spaces are ignored. Lines beginning with &#8216;#&#8217; are treated as comments. </p>
<p> The variables currently recognized are:</p>
<dl>
<dt><code>NETID_AUTHORITATIVE =</code> <i>TRUE</i>|<i>FALSE</i></p>
<dd>If set to TRUE, the NIS backend for the <code><a href="/docs/linux/man/3-initgroups/">initgroups</a></code>(3) function will accept the information from the <i>netid.byname</i> NIS map as authoritative. This can speed up the function significantly if the <i>group.byname</i> map is large. The content of the <i>netid.byname</i> map is used <code>as is</code>. The system administrator has to make sure it is correctly generated.</p>
<dt><code>SERVICES_AUTHORITATIVE =</code> <i>TRUE</i>|<i>FALSE</i></p>
<dd>If set to TRUE, the NIS backend for the <code><a href="/docs/linux/man/3-getservbyname/">getservbyname</a></code>(3) and <code><a href="/docs/linux/man/3-getservbyname_r/">getservbyname_r</a></code>(3) functions will assume that the <i>services.byservicename</i> NIS map exists and is authoritative, particularly that it contains both keys with /proto and without /proto for both primary service names and service aliases. The system administrator has to make sure it is correctly generated.</p>
<dt><code>SETENT_BATCH_READ =</code> <i>TRUE</i>|<i>FALSE</i></p>
<dd>If set to TRUE, the NIS backend for the <code><a href="/docs/linux/man/3-setpwent/">setpwent</a></code>(3) and <code><a href="/docs/linux/man/3-setgrent/">setgrent</a></code>(3) functions will read the entire database at once and then hand out the requests one by one from memory with every corresponding <code><a href="/docs/linux/man/3-getpwent/">getpwent</a></code>(3) or <code><a href="/docs/linux/man/3-getgrent/">getgrent</a></code>(3) call respectively. Otherwise, each <code><a href="/docs/linux/man/3-getpwent/">getpwent</a></code>(3) or <code><a href="/docs/linux/man/3-getgrent/">getgrent</a></code>(3) call might result in a network communication with the server to get the next entry.</dl>
<h2>Files</h2>
<p><i>/etc/default/nss</i></p>
<h2>Examples</h2>
<p>The default configuration corresponds to the following configuration file: </p>
<p> NETID_AUTHORITATIVE=FALSE SERVICES_AUTHORITATIVE=FALSE SETENT_BATCH_READ=FALSE</p>
<h2>See Also</h2>
<p><i>nsswitch.conf</i></p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
