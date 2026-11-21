---

title: "globus-domainname(1)"
name: "globus-domainname"
section: "1"
letter: "g"
url: "/docs/linux/man/1-globus-domainname/"
description: "globus-domainname – Print the local system’s DNS domain name"
---

<p> <code>globus-domainname</code> [ -h | -help ] [ -version -versions ]</p>
<p> The <code>globus-domainname</code> program prints the domain name of the host it is running on. It uses the same algorithm as the <code>globus-hostname</code> command. Setting the GLOBUS_HOSTNAME environment variable will override values returned from gethostname() and gethostbyname(). </p>
<p> The full set of options to <code>globus-dommainname</code> are </p>
<p> <code>-help</code></p>
<dl>
<dt>
</dt><dd> Show usage information and exit.</dd></dl>
<p> <code>-version</code></p>
<dl>
<dt>
</dt><dd> Show version information and exit.</dd></dl>
<h2>AUTHOR</h2>
<p> Copyright &#169; 1999-2016 University of Chicago </p>
