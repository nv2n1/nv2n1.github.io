---
title: "globus-domainname(1)"
name: "globus-domainname"
section: "1"
letter: "g"
url: "/docs/linux/man/1-globus-domainname/"
description: "globus-domainname – Print the local system’s DNS domain name"
---

<h2 class="name">NAME</h2>
<p> globus-domainname &#8211; Print the local system&#8217;s DNS domain name </p>
<h2>SYNOPSIS</h2>
<p> <code>globus-domainname</code> [ -h | -help ] [ -version -versions ]</p>
<h2>DESCRIPTION</h2>
<p> The <code>globus-domainname</code> program prints the domain name of the host it is running on. It uses the same algorithm as the <code>globus-hostname</code> command. Setting the GLOBUS_HOSTNAME environment variable will override values returned from gethostname() and gethostbyname(). </p>
<p> The full set of options to <code>globus-dommainname</code> are </p>
<p> <code>-help</code></p>
<dl>
<dt>
<dd> Show usage information and exit.</dl>
<p> <code>-version</code></p>
<dl>
<dt>
<dd> Show version information and exit.</dl>
<h2>AUTHOR</h2>
<p> Copyright &#169; 1999-2016 University of Chicago </p>
<h2>Index</h2>
