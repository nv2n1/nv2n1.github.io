---
title: "setup-nsssysinit(1)"
name: "setup-nsssysinit"
section: "1"
letter: "s"
url: "/docs/linux/man/1-setup-nsssysinit/"
description: "setup-nsssysinit – Query or enable the nss-sysinit module"
---

<h2 class="name">NAME</h2>
<p> setup-nsssysinit &#8211; Query or enable the nss-sysinit module </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>setup-nsssysinit</code> [<code>on</code>] [<code>off</code>] [<code>status</code>]</dl>
<h2>DESCRIPTION</h2>
<p> <code>setup-nsssysinit</code></p>
<dd>is a shell script to query the status of the nss-sysinit module and when run with root priviledge it can enable or disable it. </p>
<p> Turns on or off the nss-sysinit module db by editing the global PKCS #11 configuration file. Displays the status. This script can be invoked by the user as super user. It is invoked at nss-sysinit post install time with argument on.</p>
<h2>OPTIONS</h2>
<p> <code>on</code></p>
<dl>
<dt>
<dd> Turn on nss-sysinit.</dl>
<p> <code>off</code></p>
<dl>
<dt>
<dd> Turn on nss-sysinit.</dl>
<p> <code>status</code></p>
<dl>
<dt>
<dd> returns whether nss-syinit is enabled or not.</dl>
<h2>EXAMPLES</h2>
<p> The following example will query for the status of nss-sysinit: </p>
<dl>
<dt>
<dd>
<pre>
        /usr/bin/setup-nsssysinit status
      
</pre>
</dl>
<p> The following example, when run as superuser, will turn on nss-sysinit: </p>
<dl>
<dt>
<dd>
<pre>
        /usr/bin/setup-nsssysinit on
      
</pre>
</dl>
<h2>FILES</h2>
<p> /usr/bin/setup-nsssysinit</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-pkg-config/">pkg-config</a>(1)</p>
<h2>AUTHORS</h2>
<p> The nss libraries were written and maintained by developers with Netscape, Red Hat, Sun, Oracle, Mozilla, and Google. </p>
<p> Authors: Elio Maldonado &lt;emaldona [at] redhat.com&gt;.</p>
<h2>LICENSE</h2>
<p> Licensed under the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, You can obtain one at <a rel="nofollow" href="http://mozilla.org/MPL/2.0/.">http://mozilla.org/MPL/2.0/.</a> </p>
<h2>Index</h2>
