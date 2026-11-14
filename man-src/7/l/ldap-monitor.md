---
title: "ldap-monitor(7)"
name: "ldap-monitor"
section: "7"
letter: "l"
url: "/docs/linux/man/7-ldap-monitor/"
description: "ldap-monitor – Real-time NorduGrid monitoring tool"
---

<p>ldap-monitor &#8211; Real-time NorduGrid monitoring tool </p>
<h2>Description</h2>
<p><code>LDAP Grid Monitor</code> is a set of <code>PHP </code> and <code>Java </code> scripts, providing a Web interface to the <code>NorduGrid </code> Information System. Should be working for any similar <code>LDAP </code> based service. </p>
<h2>Requirements</h2>
<dl>
<dt>LDAP library</p>
<dd>e.g., <a rel="nofollow" href="http://www.openldap.org">http://www.openldap.org</a> </p>
<dt>GD library</p>
<dd><a rel="nofollow" href="http://www.boutell.com/gd">http://www.boutell.com/gd</a> </p>
<dt>PHP4 library</p>
<dd><a rel="nofollow" href="http://www.php.net,">http://www.php.net,</a> must be compiled with LDAP and GD extensions </p>
<dt>HTTP server</p>
<dd>must be compiled with PHP4 </p>
<dt>Globus MDS</p>
<dd><a rel="nofollow" href="http://www.globus.org/mds,">http://www.globus.org/mds,</a> or a similar <code>LDAP</code> based service </p>
<dt>Virtual Organisation</p>
<dd>Is optional </p>
</dl>
<h2>Installation</h2>
<p>Copy all the files in a folder, accessible by the HTTP server. </p>
<p> Modify <i>settings.inc</i> according to your MDS structure and liking. </p>
<p> Run the whole stuff by loading <i>loadmon.php</i> into your favorite browser.</p>
<h2>Files</h2>
<p><i>loadmon.php</i></p>
<dl>
<dd>To monitor several servers at once, add hosts and DNs to the <i>$arrhost</i> and, correspondingly, <i>$arrbdn</i> arrays in <i>loadmon.php</i></dl>
<p> <i>isattr.inc </i> <i>cnvname.inc</i> <i>cnvalias.inc</i></p>
<dl>
<dd>Making output more human-readable: modify <i>isattr.inc,</i> <i>cnvname.inc,</i> <i>cnvalias.inc.</i> Otherwise, these files are not needed.</dl>
<p> <i>blacklist.inc</i></p>
<dl>
<dd>To prevent sites from being polled, modify array entries in <i>blacklist.inc.</i> Otherwise, the file is not needed.</dl>
<p> <i>vo-users.php</i></p>
<dl>
<dd>Not needed when working without a Virtual Organisation. In such a case, remove the corresponding link from <i>loadmon.php .</i></dl>
<p> <i>jobstat.php</i></p>
<dl>
<dd>When working without the <code>NorduGrid</code> Information System: to make sure that the job status is defined properly, edit <i>jobstat.php</i> (look for <code>adjustment </code> instructions in the code). </p>
</dl>
<h2>Author</h2>
<p>Oxana Smirnova &lt;oxana dot smirnova at quark dot lu dot se&gt;</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-ngsub/">ngsub</a></code>(1), <code><a href="/docs/linux/man/1-ngstat/">ngstat</a></code>(1), <code><a href="/docs/linux/man/1-ngdel/">ngdel</a></code>(1), <code><a href="/docs/linux/man/1-ngget/">ngget</a></code>(1), <code><a href="/docs/linux/man/1-ngsync/">ngsync</a></code>(1), <code><a href="/docs/linux/man/1-ngcopy/">ngcopy</a></code>(1), <code><a href="/docs/linux/man/1-ngremove/">ngremove</a></code>(1) </p>
