---
title: "modifyrepo(1)"
name: "modifyrepo"
section: "1"
letter: "m"
url: "/docs/linux/man/1-modifyrepo/"
description: "modifyrepo – Modify a repomd (xml-rpm-metadata) repository"
---

<h2 class="name">NAME</h2>
<p> modifyrepo &#8211; Modify a repomd (xml-rpm-metadata) repository</p>
<h2>SYNOPSIS</h2>
<p> <code>modifyrepo</code> [options] &lt;input metadata&gt; &lt;output repodata&gt; </p>
<h2>DESCRIPTION</h2>
<p> <code>modifyrepo</code> is a program that allows you to insert arbitrary metadata into a repomd (xml-based rpm metadata) repository. </p>
<h2>EXAMPLES</h2>
<p> $ <code>modifyrepo</code> &#8211;mdtype=newmd metadata.xml /repository/repodata<br />
 Wrote: /repository/repodata/metadata.xml.gz<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>type&nbsp;<wbr>=&nbsp;<wbr>newmd<br />
&nbsp;<wbr>location&nbsp;<wbr>=&nbsp;<wbr>repodata/metadata.xml.gz<br />
&nbsp;<wbr>checksum&nbsp;<wbr>=&nbsp;<wbr>1d7ee93db2964e7f85e07ec19b3204591da1050c<br />
timestamp&nbsp;<wbr>=&nbsp;<wbr>1196716296.0<br />
&nbsp;<wbr>&nbsp;<wbr>open-checksum&nbsp;<wbr>=&nbsp;<wbr>824d936dc7dfff029379797b311af0cc66af4115<br />
 Wrote: /repository/repodata/repomd.xml </p>
<h2>SEE ALSO</h2>
<p> <i>createrepo (8)</i> </p>
<h2>AUTHORS</h2>
<pre><code>
Luke Macken&lt;lmacken[at] redhat.com&gt;
    Seth Vidal&lt;skvidal[at] fedoraproject.org&gt;
</code></pre>
<h2>BUGS</h2>
<p> Any bugs which are found should be emailed to the mailing list: rpm-metadata [at] lists.baseurl.org </p>
<h2>Index</h2>
