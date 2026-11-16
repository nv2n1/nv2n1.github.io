---
title: "struct_sublog(9)"
name: "struct_sublog"
section: "9"
letter: "s"
url: "/docs/linux/man/9-struct_sublog/"
description: "struct_sublog – subchannel logout area"
---

<p>struct_sublog &#8211; subchannel logout area</p>
<h2>Synopsis</h2>
<pre><code>struct sublog {
    __u32 res0 : 1;
    __u32 esf : 7;
    __u32 lpum : 8;
    __u32 arep : 1;
    __u32 fvf : 5;
    __u32 sacc : 2;
    __u32 termc : 2;
    __u32 devsc : 1;
    __u32 serr : 1;
    __u32 ioerr : 1;
    __u32 seqc : 3;
};</code></pre>
<h2>Members</h2>
<p>res0</p>
<dl>
<dd>reserved</dd></dl>
<p> esf</p>
<dl>
<dd>extended status flags</dd></dl>
<p> lpum</p>
<dl>
<dd>last path used mask</dd></dl>
<p> arep</p>
<dl>
<dd>ancillary report</dd></dl>
<p> fvf</p>
<dl>
<dd>field-validity flags</dd></dl>
<p> sacc</p>
<dl>
<dd>storage access code</dd></dl>
<p> termc</p>
<dl>
<dd>termination code</dd></dl>
<p> devsc</p>
<dl>
<dd>device-status check</dd></dl>
<p> serr</p>
<dl>
<dd>secondary error</dd></dl>
<p> ioerr</p>
<dl>
<dd>i/o-error alert</dd></dl>
<p> seqc</p>
<dl>
<dd>sequence code</dd></dl>
<h2>Author</h2>
<p><code>Cornelia Huck</code> &lt;cornelia.huck [at] de.ibm.com&gt;</p>
<dl>
<dd>Author.</dd></dl>
<h2>Copyright</h2>
