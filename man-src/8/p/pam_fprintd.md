---
title: "pam_fprintd(8)"
name: "pam_fprintd"
section: "8"
letter: "p"
url: "/docs/linux/man/8-pam_fprintd/"
description: "pam_fprintd – PAM module to authenticate against fprintd, the fingerprint daemon"
---

<p>pam_fprintd &#8211; PAM module to authenticate against fprintd, the fingerprint daemon</p>
<h2>Synopsis</h2>
<p><code>pam_fprintd.so</code> [debug|debug=[<i>on</i>|<i>off</i>|<i>true</i>|<i>false</i>|<i>1</i>|<i>0</i>]] [max-tries=<i></i><i>MAX_TRIES</i><i></i>] [timeout=<i></i><i>TIMEOUT</i><i></i>]</p>
<h2>Description</h2>
<p>The pam_fprintd module is used to verify a user&#8217;s fingerprints against fingerprints enrolled using fprintd, the fingerprint management daemon.</p>
<h2>Options</h2>
<dl>
<dt><code>debug</code></dt>
<dd>
</dd><dt><code>debug=[</code>on<code>|</code>off<code>|</code>true<code>|</code>false<code>|</code>1<code>|</code>0<code>]</code></dt>
<dd>Whether debug should be turned on or off. Debug messages will be generated using pam_syslog which means that they will be saved in the systemd journal by default.</dd>
<dt><code>max-tries=</code>MAX_TRIES</dt>
<dd>The number of attempts at fingerprint authentication to try before returning an authentication failure. The minimum, and default, number of tries is 3.</dd>
<dt><code>timeout=</code>TIMEOUT</dt>
<dd>The amount of time before returning an authentication failure. The default timeout is 30 seconds, with 10 seconds being the minimum.</dd></dl>
<h2>Limitations</h2>
<p>The PAM stack is by design a serialised authentication, so it is not possible for pam_fprintd to allow authentication through passwords and fingerprints at the same time. </p>
<p> It is up to the application using the PAM services to implement separate PAM processes and run separate authentication stacks separately. This is the way multiple authentication methods are made available to users of gdm for example.</p>
<h2>Author</h2>
<p><code>fprintd</code> was written by Bastien Nocera.</p>
<h2>See Also</h2>
<dl>
<dt><code>fprintd</code>, <code>PAM</code></dt>
<dd>
</dd></dl>