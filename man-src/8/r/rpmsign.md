---
title: "rpmsign(8)"
name: "rpmsign"
section: "8"
letter: "r"
url: "/docs/linux/man/8-rpmsign/"
description: "rpmsign – RPM Package Signing"
---

<p>rpmsign &#8211; RPM Package Signing</p>
<h2>Synopsis</h2>
<p><code>rpm</code> <code>&#8211;addsign|&#8211;resign</code> <i>PACKAGE_FILE</i><i> &#8230;</i> <code>rpm</code> <code>&#8211;delsign</code> <i>PACKAGE_FILE</i><i> &#8230;</i> </p>
<h2>Description</h2>
<p>Both of the <code>&#8211;addsign</code> and <code>&#8211;resign</code> options generate and insert new signatures for each package <i>PACKAGE_FILE</i> given, replacing any existing signatures. There are two options for historical reasons, there is no difference in behavior currently. <code>rpm</code> <code>&#8211;delsign</code> <i>PACKAGE_FILE</i><i> &#8230;</i> Delete all signatures from each package <i>PACKAGE_FILE</i> given.</p>
<h3>Using Gpg To Sign Packages</h3>
<p>In order to sign packages using GPG, <code>rpm</code> must be configured to run GPG and be able to find a key ring with the appropriate keys. By default, <code>rpm</code> uses the same conventions as GPG to find key rings, namely the <code>$GNUPGHOME</code> environment variable. If your key rings are not located where GPG expects them to be, you will need to configure the macro <code>%_gpg_path</code> to be the location of the GPG key rings to use. If you want to be able to sign packages you create yourself, you also need to create your own public and secret key pair (see the GPG manual). You will also need to configure the <code>rpm</code> macros</p>
<dl>
<dt><code>%_gpg_name</code></p>
<dd>The name of the &quot;user&quot; whose key you wish to use to sign your packages.</dl>
<p> For example, to be able to use GPG to sign packages as the user <i>&quot;John Doe &lt;jdoe [at] foo.com&gt;&quot;</i> from the key rings located in <i>/etc/rpm/.gpg</i> using the executable <i>/usr/bin/gpg</i> you would include </p>
<pre>%_gpg_path /etc/rpm/.gpg
%_gpg_name John Doe &lt;jdoe [at] foo.com&gt;
%__gpg /usr/bin/gpg</pre>
<p>in a macro configuration file. Use <i>/etc/rpm/macros</i> for per-system configuration and <i>~/.rpmmacros</i> for per-user configuration. Typically it&#8217;s sufficient to set just %_gpg_name. </p>
<h2>See Also</h2>
<pre><code><a href="//www.systutorials.com/docs/linux/man/3-popt/">popt</a></code>(3),
<code><a href="//www.systutorials.com/docs/linux/man/8-rpm/">rpm</a></code>(8),
<code><a href="//www.systutorials.com/docs/linux/man/8-rpmdb/">rpmdb</a></code>(8),
<code><a href="//www.systutorials.com/docs/linux/man/8-rpmkeys/">rpmkeys</a></code>(8),
<code><a href="//www.systutorials.com/docs/linux/man/8-rpm2cpio/">rpm2cpio</a></code>(8),
<code><a href="//www.systutorials.com/docs/linux/man/8-rpmbuild/">rpmbuild</a></code>(8),
<code><a href="//www.systutorials.com/docs/linux/man/8-rpmspec/">rpmspec</a></code>(8),</pre>
<p><code>rpmsign &#8211;help</code> &#8211; as rpm supports customizing the options via popt aliases it&#8217;s impossible to guarantee that what&#8217;s described in the manual matches what&#8217;s available. </p>
<p> <code><a rel="nofollow" href="http://www.rpm.org/">http://www.rpm.org/</a> &lt;URL:<a href="http://www.rpm.org/">http://www.rpm.org/</a>&gt; </code></p>
<h2>Authors</h2>
<pre>Marc Ewing &lt;marc [at] redhat.com&gt;
Jeff Johnson &lt;jbj [at] redhat.com&gt;
Erik Troan &lt;ewt [at] redhat.com&gt;
Panu Matilainen &lt;pmatilai [at] redhat.com&gt;</pre>
