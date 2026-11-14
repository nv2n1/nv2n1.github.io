---
title: "vendors(5)"
name: "vendors"
section: "5"
letter: "v"
url: "/docs/linux/man/5-vendors/"
description: "vendors.list – Security key configuration for APT"
---

<p>vendors.list &#8211; Security key configuration for APT </p>
<h2>Description</h2>
<p>The package vendor list contains a list of all vendors from whom you wish to<br />
&nbsp;<wbr>authenticate&nbsp;<wbr>&nbsp;<wbr>downloaded&nbsp;<wbr>&nbsp;<wbr>packages.&nbsp;<wbr>&nbsp;<wbr>For each vendor listed, it must contain the corresponding PGP key fingerprint, so that APT can perform signature verification of the release file and subsequent checking of the checksums of each downloaded package. To have authentication enabled, you must add the vendor identification string (see below) enclosed in square braces to the <i><a href="/docs/linux/man/5-sources-list/">sources.list</a></i>(5) line for all sites that mirror the repository provided by that vendor. The format of this file is similar to the one used by <i><a href="/docs/linux/man/5-apt-conf/">apt.conf</a></i>(5). It consists of an arbitrary number of blocks of vendors, where each block starts with a string telling the <code>key_type</code> and the <code>vendor_id</code>. Some vendors may have multiple blocks that define different security policies for their distributions. Debian for instance uses a different signing methodology for stable and unstable releases. <code>key_type</code> is the type of the check required. Currently, there is only one type available which is <i>simple-key</i>. <code>vendor_id</code> is the vendor identification string. It is an arbitrary string you must supply to uniquely identify a vendor that&#8217;s listed in this file. Example:</p>
<dl>
<dd>
<pre>simple-key &quot;joe&quot;
{
 Fingerprint &quot;0987AB4378FSD872343298787ACC&quot;;
 Name &quot;Joe Shmoe &lt;joe [at] shmoe.com&gt;&quot;;
} </pre>
<h2>The Simple-Key Type</h2>
<p>This type of verification is used when the vendor has a single secured key that must be used to sign the Release file. The following items should be present </p>
<dl>
<dt><code>Fingerprint</code></p>
<dd>The PGP fingerprint for the key. The fingerprint should be expressed in the standard notion with or without spaces. The <code>&#8211;fingerprint</code> option for <code><a href="/docs/linux/man/1-gpg/">gpg</a></code>(1) will show the fingerprint for the selected keys(s). </p>
<dt><code>Name</code></p>
<dd>A string containing a description of the owner of the key or vendor. You may put the vendor name and email. The string must be entirely within double-quotes (<code>&quot;</code>). </p>
</dl>
<h2>Files</h2>
<p><i>/etc/apt/vendors.list</i></p>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/5-sources-list/">sources.list</a></i>(5) </p>
<h2>Bugs</h2>
<p>Reporting bugs in APT-RPM is best done in the APT-RPM mailinglist at <a rel="nofollow" href="http://apt-rpm.org/mailinglist.shtml.">http://apt-rpm.org/mailinglist.shtml.</a> </p>
<h2>Author</h2>
<p>Maintainer and contributor information can be found in the credits page <a rel="nofollow" href="http://apt-rpm.org/about.shtml">http://apt-rpm.org/about.shtml</a> of APT-RPM.</p>
