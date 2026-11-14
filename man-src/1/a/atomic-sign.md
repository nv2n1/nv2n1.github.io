---
title: "atomic-sign(1)"
name: "atomic-sign"
section: "1"
letter: "a"
url: "/docs/linux/man/1-atomic-sign/"
description: "atomic-sign- Create a signature for an image"
---

<h2 class="name">NAME</h2>
<p> atomic-sign- Create a signature for an image </p>
<p> <code>WARNING</code> </p>
<p> Only use <code>atomic sign</code> if you trust the remote registry which contains the image (preferably by being the only administrator of it). </p>
<h2>SYNOPSIS</h2>
<p> <code>atomic sign</code> [<code>-h</code>|<code>&#8211;help</code>] [<code>-d</code>, <code>&#8211;directory</code>] [<code>&#8211;sign-by</code>] [<code>-g</code>, <code>&#8211;gnupghome</code>] [ image &#8230; ] </p>
<h2>DESCRIPTION</h2>
<p> <code>atomic sign</code> will create a local signature for one or more local images that have been pulled from a registry. By default, the signature will be written into a directory derived from the registry configuration files as configured by <code>registry_confdir</code> in /etc/atomic.conf. </p>
<h2>OPTIONS</h2>
<p> <code>-h</code> <code>&#8211;help</code><br />
&nbsp;<wbr>&nbsp;<wbr>Print usage statement. </p>
<p> <code>-d</code> <code>&#8211;directory</code><br />
&nbsp;<wbr>&nbsp;<wbr>Store the signatures in the specified directory.&nbsp;<wbr>&nbsp;<wbr>Default:&nbsp;<wbr>/var/lib/atomic/signature </p>
<p> <code>&#8211;sign-by</code><br />
&nbsp;<wbr>&nbsp;<wbr>Override the default identity of the signature. You can define a default in&nbsp;<wbr>/etc/atomic.conf<br />
&nbsp;<wbr>&nbsp;<wbr>with the key&nbsp;<wbr><code>default_signer</code>. </p>
<p> <code>-g</code> <code>&#8211;gnupghome</code><br />
&nbsp;<wbr>&nbsp;<wbr>Specify the GNUPGHOME directory to use for signing, e.g.&nbsp;<wbr>~/.gnupg. This<br />
&nbsp;<wbr>&nbsp;<wbr>argument will override the value of&nbsp;<wbr><code>gnupg_homedir</code>&nbsp;<wbr>in&nbsp;<wbr>/etc/atomic.conf.<br />
&nbsp;<wbr>&nbsp;<wbr>Defaults to the homedir or the uid defined in&nbsp;<wbr>/proc/self/loginuid if it exists, or<br />
&nbsp;<wbr>&nbsp;<wbr>$SUDO_UID if it is defined, or current UID. </p>
<h2>EXAMPLES</h2>
<p> Sign the foobar image from privateregistry.example.com </p>
<dl>
<dt>
<dd>
<pre>
atomic sign privateregistry.example.com/foobar
</pre>
</dl>
<p> Sign the foobar image and save the signature in /tmp/signatures/. </p>
<dl>
<dt>
<dd>
<pre>
atomic sign -d /tmp/signatures privateregistry.example.com
</pre>
</dl>
<p> Sign the busybox image with the identify of foo [at] bar.com with a user&#8217;s keyring </p>
<p> sudo atomic sign &#8211;sign-by foo [at] bar.com &#8211;gnupghome=~/.gnupg privateregistry.example.com </p>
<h2>RELATED CONFIGURATION</h2>
<p> The write (and read) location for signatures is defined in YAML-based configuration files in /etc/containers/registries.d/. When you sign an image, atomic will use those configuration files to determine where to write the signature based on the the name of the originating registry or a default storage value unless overriden with the -d option. For example, consider the following configuration file. </p>
<p> docker:<br />
&nbsp;<wbr>&nbsp;<wbr>privateregistry.example.com:<br />
&nbsp;<wbr>sigstore: file:///var/lib/atomic/signature </p>
<p> When signing an image preceeded with the registry name &#8216;privateregistry.example.com&#8217;, the signature will be written into subdirectories of /var/lib/atomic/signature/privateregistry.example.com. The use of &#8216;sigstore&#8217; also means the signature will be &#8216;read&#8217; from that same location on a pull-related function. </p>
<p> You can also scope the registry definitions by repository and even name. Consider the following addition to the configuration above. </p>
<p> privateregistry.exaple.com/john:<br />
&nbsp;<wbr>sigstore-staging: file:///mnt/export/signatures<br />
&nbsp;<wbr>sigstore:&nbsp;<wbr> &lt;<a rel="nofollow" href="https://www.example.com/signatures/">https://www.example.com/signatures/</a>&gt; </p>
<p> Now any image from the john repository will use the sigstore-staging location of means that signatures should be written to that location but read should occur from the http URL provided. </p>
<p> The user&#8217;s keyring will be used during signing. When running as root user this may not be desired. Another keyring may be specified using environment variable GNUPGHOME, passed in via argument &#8211;gnupghome or set in configuration file atomic.conf. For example: </p>
<p> gnupg_homedir: /home/USER/.gnupg </p>
<h2>HISTORY</h2>
<p> Initial revision by Brent Baude (bbaude at redhat dot com) August 2016 Updated by Brent Baude (bbaude at redhat dot com) September 2016 Updated by Aaron Weitekamp (aweiteka at redhat dot com) September 2016 </p>
<h2>Index</h2>
