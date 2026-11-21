---
title: "derdump(1)"
name: "derdump"
section: "1"
letter: "d"
url: "/docs/linux/man/1-derdump/"
description: "derdump_ – Dumps C-sequence strings from a DER encoded certificate file"
---

<h2 class="name">NAME</h2>
<p> derdump_ &#8211; Dumps C-sequence strings from a DER encoded certificate file </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>derdump</code> [<code>-r</code>] [<code>-i&nbsp;<wbr></code><i>input-file</i>] [<code>-o&nbsp;<wbr></code><i>output-file</i>]</dt></dl>
<h2>STATUS</h2>
<dd>This documentation is still work in progress. Please contribute to the initial review in m[blue]<code>Mozilla NSS bug 836477</code>m[]<font SIZE="-2">[1]</font></dd>
<h2>DESCRIPTION</h2>
<p> <code>derdump </code>dumps C-sequence strings from a DER encode certificate file</p>
<h2>OPTIONS</h2>
<p> <code>-r </code></p>
<dl>
<dt>
</dt><dd> For formatted items, dump raw bytes as well</dd></dl>
<p> <code>-i </code> <i>DER encoded file</i></p>
<dl>
<dt>
</dt><dd> Define an input file to use (default is stdin)</dd></dl>
<p> <code>-o </code> <i>output file</i></p>
<dl>
<dt>
</dt><dd> Define an output file to use (default is stdout).</dd></dl>
<h2>ADDITIONAL RESOURCES</h2>
<p> NSS is maintained in conjunction with PKI and security-related projects through Mozilla dn Fedora. The most closely-related project is Dogtag PKI, with a project wiki at m[blue]<code>PKI Wiki</code>m[]<font SIZE="-2">[2]</font>. </p>
<p> For information specifically about NSS, the NSS project wiki is located at m[blue]<code>Mozilla NSS site</code>m[]<font SIZE="-2">[3]</font>. The NSS site relates directly to NSS code changes and releases. </p>
<p> Mailing lists: pki-devel [at] redhat.com and pki-users [at] redhat.com </p>
<p> IRC: Freenode at #dogtag-pki</p>
<h2>AUTHORS</h2>
<p> The NSS tools were written and maintained by developers with Netscape and now with Red Hat. </p>
<p> Authors: Gerhardus Geldenhuis &lt;gerhardus.geldenhuis [at] gmail.com&gt;. Elio Maldonado &lt;emaldona [at] redhat.com&gt;, Deon Lackey &lt;dlackey [at] redhat.com&gt;</p>
<h2>LICENSE</h2>
<p> Licensed under the Mozilla Public License, version 1.1, and/or the GNU General Public License, version 2 or later, and/or the GNU Lesser General Public License, version 2.1 or later.</p>
<h2>NOTES</h2>
<dl>
<dt> 1.</dt>
<dd> Mozilla NSS bug 836477</dd>
<dl>
<dt>
</dt><dd> <a rel="nofollow" href="https://bugzilla.mozilla.org/show_bug.cgi?id=836477">https://bugzilla.mozilla.org/show_bug.cgi?id=836477</a></dd></dl>
<dt> 2.</dt>
<dd> PKI Wiki</dd>
<dl>
<dt>
</dt><dd> <a rel="nofollow" href="http://pki.fedoraproject.org/wiki/">http://pki.fedoraproject.org/wiki/</a></dd></dl>
<dt> 3.</dt>
<dd> Mozilla NSS site</dd>
<dl>
<dt>
</dt><dd> <a rel="nofollow" href="http://www.mozilla.org/projects/security/pki/nss/">http://www.mozilla.org/projects/security/pki/nss/</a></dd></dl>
</dl>
