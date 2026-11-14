---
title: "ddclient(8)"
name: "ddclient"
section: "8"
letter: "d"
url: "/docs/linux/man/8-ddclient/"
description: "ddclient – Update IP addresses at dynamic DNS services"
---

<p>ddclient &#8211; Update IP addresses at dynamic DNS services</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>ddclient</code> {-help}</p>
<dt> <code>ddclient</code> [-daemon&nbsp;<i>interval</i>] [-proxy&nbsp;<i>host</i>] [-server&nbsp;<i>host</i>] [-protocol&nbsp;<i>type</i>] [-file&nbsp;<i>configfile</i>] [-cache&nbsp;<i>cachefile</i>] [-pid&nbsp;<i>pidfile</i>] [-use&nbsp;<i>mechanism</i>] {-if&nbsp;<i>interface</i> | -ip&nbsp;<i>ipaddress</i> | -web&nbsp;{<i>provider</i>&nbsp;|&nbsp;<i>url</i>} | -fw&nbsp;<i>firewall</i> | -cmd&nbsp;<i>command</i>}</dl>
<h2>Description</h2>
<dd>A perl based client to update your dynamic IP address at DynDNS.com (or other dynamic DNS services such as Hammernode, Zoneedit or EasyDNS), thus allowing you and others to use a fixed hostname (myhost.dyndns.org) to access your machine. This client supports both the dynamic and (near) static services, MX setting, and alternative host. It caches the address, and only attempts the update if the address actually changes. For usage information please run <code>ddclient -help</code> until this manpage is finished. </p>
