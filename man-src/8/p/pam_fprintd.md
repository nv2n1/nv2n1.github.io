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
<p><code>pam_fprintd.so</code> [debug|debug=[<i>on</i>|<i>off</i>|<i>true</i>|<i>false</i>|<i>1</i>|<i>0</i>]] [max-tries=<i></i><font SIZE="-1"><i>MAX_TRIES</i></font><i></i>] [timeout=<i></i><font SIZE="-1"><i>TIMEOUT</i></font><i></i>]</p>
<h2>Description</h2>
<p>The pam_fprintd module is used to verify a user&#8217;s fingerprints against fingerprints enrolled using fprintd, the fingerprint management daemon.</p>
<h2>Options</h2>
<dl>
<dt><code>debug</code></p>
<dd>
<dt><code>debug=[</code>on<code>|</code>off<code>|</code>true<code>|</code>false<code>|</code>1<code>|</code>0<code>]</code></p>
<dd>Whether debug should be turned on or off. Debug messages will be generated using pam_syslog which means that they will be saved in the systemd journal by default.</p>
<dt><code>max-tries=</code><font SIZE="-1">MAX_TRIES</font></p>
<dd>The number of attempts at fingerprint authentication to try before returning an authentication failure. The minimum, and default, number of tries is 3.</p>
<dt><code>timeout=</code><font SIZE="-1">TIMEOUT</font></p>
<dd>The amount of time before returning an authentication failure. The default timeout is 30 seconds, with 10 seconds being the minimum.</dl>
<h2>Limitations</h2>
<p>The <font SIZE="-1">PAM</font> stack is by design a serialised authentication, so it is not possible for pam_fprintd to allow authentication through passwords and fingerprints at the same time. </p>
<p> It is up to the application using the <font SIZE="-1">PAM</font> services to implement separate <font SIZE="-1">PAM</font> processes and run separate authentication stacks separately. This is the way multiple authentication methods are made available to users of gdm for example.</p>
<h2>Author</h2>
<p><code>fprintd</code> was written by Bastien Nocera.</p>
<h2>See Also</h2>
<dl>
<dt><code>fprintd</code>, <font SIZE="-1"><code>PAM</code></font></p>
<dd>
