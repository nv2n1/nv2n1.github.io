---
title: "rpmkeys(8)"
name: "rpmkeys"
section: "8"
letter: "r"
url: "/docs/linux/man/8-rpmkeys/"
description: "rpmkeys – RPM Keyring"
---

<p>rpmkeys &#8211; RPM Keyring</p>
<h2>Synopsis</h2>
<p><code>rpmkeys</code> {<code>&#8211;import|&#8211;checksig</code>} </p>
<h2>Description</h2>
<p>The general forms of rpm digital signature commands are <code>rpmkeys</code> <code>&#8211;import</code> <i>PUBKEY</i><i> &#8230;</i> <code>rpmkeys</code> {<code>-K|&#8211;checksig</code>} <i>PACKAGE_FILE</i><i> &#8230;</i> The <code>&#8211;checksig</code> option checks all the digests and signatures contained in <i>PACKAGE_FILE</i> to ensure the integrity and origin of the package. Note that signatures are now verified whenever a package is read, and <code>&#8211;checksig</code> is useful to verify all of the digests and signatures associated with a package. Digital signatures cannot be verified without a public key. An ASCII armored public key can be added to the <code>rpm</code> database using <code>&#8211;import</code>. An imported public key is carried in a header, and key ring management is performed exactly like package management. For example, all currently imported public keys can be displayed by: <code>rpm -qa gpg-pubkey*</code> Details about a specific public key, when imported, can be displayed by querying. Here&#8217;s information about the Red Hat GPG/DSA key: <code>rpm -qi gpg-pubkey-db42a60e</code> Finally, public keys can be erased after importing just like packages. Here&#8217;s how to remove the Red Hat GPG/DSA key <code>rpm -e gpg-pubkey-db42a60e</code> </p>
<h2>See Also</h2>
<pre><code><a href="//www.systutorials.com/docs/linux/man/3-popt/">popt</a></code>(3),
<code><a href="//www.systutorials.com/docs/linux/man/8-rpm/">rpm</a></code>(8),
<code><a href="//www.systutorials.com/docs/linux/man/8-rpmdb/">rpmdb</a></code>(8),
<code><a href="//www.systutorials.com/docs/linux/man/8-rpmsign/">rpmsign</a></code>(8),
<code><a href="//www.systutorials.com/docs/linux/man/8-rpm2cpio/">rpm2cpio</a></code>(8),
<code><a href="//www.systutorials.com/docs/linux/man/8-rpmbuild/">rpmbuild</a></code>(8),
<code><a href="//www.systutorials.com/docs/linux/man/8-rpmspec/">rpmspec</a></code>(8),</pre>
<p><code>rpmkeys &#8211;help</code> &#8211; as rpm supports customizing the options via popt aliases it&#8217;s impossible to guarantee that what&#8217;s described in the manual matches what&#8217;s available. </p>
<p> <code><a rel="nofollow" href="http://www.rpm.org/">http://www.rpm.org/</a> &lt;URL:<a href="http://www.rpm.org/">http://www.rpm.org/</a>&gt; </code></p>
<h2>Authors</h2>
<pre>Marc Ewing &lt;marc [at] redhat.com&gt;
Jeff Johnson &lt;jbj [at] redhat.com&gt;
Erik Troan &lt;ewt [at] redhat.com&gt;
Panu Matilainen &lt;pmatilai [at] redhat.com&gt;</pre>
