---

title: "abrt-bodhi(1)"
name: "abrt-bodhi"
section: "1"
letter: "a"
url: "/docs/linux/man/1-abrt-bodhi/"
---

abrt-bodhi - The ABRT bodhi client. 

<h2>SYNOPSIS</h2>

 

 <i>abrt-bodhi</i> [-v] [-r[RELEASE]] (-b ID1[,ID2,...] | PKG-NAME) [PKG-NAME]...

<h2>DESCRIPTION</h2>

 

 <i>abrt-bodhi</i> is the command-line tool for listing a new updates. Bodhi can be queried by release, bug id or package name.

<h2>OPTIONS</h2>

 

 -v, --verbose
<dl>
<dt>
</dt><dd> Be verbose</dd></dl>
 

 -r[RELEASE], --release[RELEASE]
<dl>
<dt>
</dt><dd> Specify a release (f16|rawhide)</dd></dl>
 

 -b, --bugs ID1,ID2,.. Specify any number of Bugzilla IDs (--bugs=1234,5678)

<h2>AUTHORS</h2>

 

<dl>
<dt>
</dt><dd> &bull; ABRT team</dd></dl>
