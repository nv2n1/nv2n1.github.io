---
title: "amanda-compatibility(7)"
name: "amanda-compatibility"
section: "7"
letter: "a"
url: "/docs/linux/man/7-amanda-compatibility/"
description: "amanda-compatibility – Compatibility between Amanda versions"
---

<p>amanda-compatibility &#8211; Compatibility between Amanda versions</p>
<h2>Network Compatibility</h2>
<p>Amanda has used several on-the-wire protocols to communicate between the server and backup clients, and not all of them have been compatible. </p>
<p> Versions of Amanda prior to about 2.3 used a different protocol which is not compatible. 2.3 is very old so this is not of general interest. </p>
<p> The Amanda 2.4 series all use the same protocol. This protocol has support for extensibility. Generally upgrading clients or servers along the 2.4 branch does not cause difficulty. </p>
<p> Amanda 2.5.0 uses the same protocol as 2.4. One can use a 2.5.0 server with 2.4 clients and a 2.4 server with 2.5.0 clients. </p>
<p> Kerberos4 authentication in 2.5 is compatible with 2.4. In 2.5, kerberos4 encryption is broken, at least for the server. </p>
<p> Amanda 2.5.1 introduced a new recover protocol. Backup communication works with any combination of versions, but 2.5.1&#8217;s amrecover cannot communicate with an older server. Use oldamrecover on 2.5.1 and higher clients when communicating with an older server. </p>
<p> Amanda 2.6.0 and later are completely compatible with 2.5.1. </p>
<p> To restore a dump created with the tapesplit_size option using amrecover, you need at least a 2.5 server and late-2.4 client. (Extracting that backup using only shell, mt and dd is also possible.)</p>
<h2>Upgrades</h2>
<p>The recommended course for Amanda upgrades is to upgrade the server first, and test backups and restores before upgrading clients. Consult the changes described below for the relevant span of versions to determine what adjustments, if any, are required. Also see the NEWS file shipped with each Amanda release for more detailed information.</p>
<h3>Amanda 3.2</h3>
<p>The following configuration configration keywords are deprecated. This is currently a warning, but will become an error soon. </p>
<dl>
<dd>&bull; <code>amrecover-do-fsf</code> &#8211; amrecover always seeks to files when recovering</dl>
<dl>
<dd>&bull; <code>amrecover-check-label</code> &#8211; amrecover always checks the volume label when recovering</dl>
<dl>
<dd>&bull; Dumptype parameters <code>tape-splitsize</code>, <code>split-diskbuffer</code>, and <code>fallback-splitsize</code> &#8211; see <code>allow-split</code> and tapetype parameters <code>part-size</code>, <code>part-cache-type</code>, <code>part-cache-dir</code>, and <code>part-cache-max-size</code>. See <code><a href="/docs/linux/man/5-amanda-conf/">amanda.conf</a></code>(5) for more information on these new parameters, noting particularly that all but the first are tapetype parameters, not dumptype parameters. </p>
<p> To convert most cases to the new parameters, set <code>part-size</code> to the old value of <code>tape-splitsize</code> and <code>part-cache-dir</code> to the old value of <code>split-diskbuffer</code>, if present. If <code>split-diskbuffer</code> was set, then set <code>part-cache-type</code> to <code>disk</code>, otherwise <code>memory</code>. Finally, if using memory caching, set <code>part-cache-max-size</code> to the previous value of <code>fallback-splitsize</code>. Be sure to remove all of the old keywords from your configuration.</dl>
<h3>Amanda 3.1</h3>
<p>Although it is a significant rewrite, there are no incompatible changes in this release. </p>
<p> Old-style changer scripts are deprecated in this release. While they remain available, they may be removed in a future release. Consider upgrading to one of the new changer scripts. Users of <i>chg-zd-mtx</i> are particularly encouraged to consider the much more intelligent <i>chg-robot</i>. See <code><a href="/docs/linux/man/7-amanda-changers/">amanda-changers</a></code>(7) for more information. </p>
<p> The following configuration configration keywords are deprecated. This is currently a warning, but will become an error in a future version. </p>
<dl>
<dd>&bull; label_new_tapes &#8211; use autolabel</dl>
<h3>Amanda 2.6.1</h3>
<p>There are no incompatible changes in this release, but consider switching to some of the new applications instead of the old GNUTAR and DUMP programs. </p>
<p> The following configuration configration keywords are deprecated. This is currently a warning, but will become an error soon. </p>
<dl>
<dd>&bull; tapebufs &#8211; use device-output-buffer-size instead</dl>
<dl>
<dd>&bull; rawtapedev &#8211; use tapedev instead</dl>
<dl>
<dd>&bull; file-pad &#8211; this is no longer optional, and all files are padded</dl>
<h3>Amanda 2.6.0</h3>
<p>amverify and amverifyrun are removed and replaced with <code><a href="/docs/linux/man/8-amcheckdump/">amcheckdump</a></code>(8). Both amdd and ammt are removed. </p>
<p> Some Amanda files are now installed in new amanda/ subdirectories: libraries are now installed in $libdir/amanda and internal programs are now installed in $libexecdir/amanda. </p>
<p> The amandates file, previously at /etc/amandates, is now at $localstatedir/amanda/amandates. You may want to move your existing /etc/amandates when you upgrade Amanda. </p>
<p> GLib is now required to build and run Amanda.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-amanda/">amanda</a></code>(8), <code><a href="/docs/linux/man/5-amanda-conf/">amanda.conf</a></code>(5) </p>
<p> The Amanda Wiki: : <a rel="nofollow" href="http://wiki.zmanda.com/">http://wiki.zmanda.com/</a></p>
<h2>Author</h2>
<p><code>Dustin J. Mitchell</code> &lt;dustin [at] zmanda.com&gt;</p>
<dl>
<dd>Zmanda, Inc. (<a rel="nofollow" href="http://www.zmanda.com)">http://www.zmanda.com)</a></dl>
