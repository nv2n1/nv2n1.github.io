---
title: "basic_radius_auth(8)"
name: "basic_radius_auth"
section: "8"
letter: "b"
url: "/docs/linux/man/8-basic_radius_auth/"
description: "basic_radius_auth – Squid RADIUS authentication helper"
---

<p>basic_radius_auth &#8211; Squid RADIUS authentication helper</p>
<h2>Synopsis</h2>
<p><code>basic_radius_auth</code> <code>-f</code> config file<br />
 <code>basic_radius_auth</code> <code>-h server name</code> <code>port</code> <code>] [-i </code> identifier <code>] -w </code> secret <code>[-t </code> timeout <code>]</code></p>
<h2>Description</h2>
<p><code>basic_radius_auth</code> allows Squid to connect to a RADIUS server to validate the user name and password of Basic HTTP authentication.</p>
<h2>Options</h2>
<dl>
<dt><code>-f configfile</code></p>
<dd>Specifies the path to a configuration file. See the CONFIGURATION section for details on the file content.</p>
<dt><code>-h server</code></p>
<dd>Alternative method of specifying the server to connect to</p>
<dt><code>-p port</code></p>
<dd>Specify another server port where the RADIUS server listens for requests if different from the default RADIUS port. Normally not specified.</p>
<dt><code>-i identifier</code></p>
<dd>Unique identifier identifying this Squid proxy to the RADIUS server. If not specified the IP address is used to identify the proxy.</p>
<dt><code>-w secret</code></p>
<dd>Alternative method of specifying the shared secret. Using the <code>-f</code> option with a configuration file is generally more secure and recommended.</p>
<dt><code>-t timeout</code></p>
<dd>RADIUS request timeout. Default is 10 seconds.</dl>
<h2>Configuration</h2>
<p>The configuration specifies how the helper connects to RADIUS. The file contains a list of directives (one per line). Lines beginning with a <code>#</code> are ignored.</p>
<dl>
<dt><code>server </code><i>radiusserver</i></p>
<dd>specifies the name or address of the RADIUS server to connect to.</p>
<dt><code>secret </code><i>somesecretstring</i></p>
<dd>specifies the shared RADIUS secret.</p>
<dt><code>identifier </code><i>nameofserver</i></p>
<dd>specifies what name the proxy should use to identify itself to the RADIUS server. This directive is optional.</p>
<dt><code>port </code><i>portnumber</i></p>
<dd>Specifies the port number or service name where the helper should connect.</p>
<dt><code>timeout </code><i>seconds</i></p>
<dd>Specifies the RADIUS request timeout.</dl>
<h2>Author</h2>
<p>This program is written by <i>Marc van Selm &lt;selm [at] cistron.nl&gt;</i> <i>Henrik Nordstrom &lt;hno [at] squid-cache.org&gt;</i> </p>
<p> With contributions from many others. </p>
<p> This manual was written by <i>Henrik Nordstrom &lt;hno [at] squid-cache.org&gt;</i></p>
<h2>Copyright</h2>
<p>&nbsp;<wbr>*&nbsp;<wbr>Copyright&nbsp;<wbr>(C)&nbsp;<wbr>1996-2016 The Squid Software Foundation and contributors<br />
&nbsp;<wbr>*<br />
&nbsp;<wbr>*&nbsp;<wbr>Squid software is distributed under GPLv2+&nbsp;<wbr>license and includes<br />
&nbsp;<wbr>*&nbsp;<wbr>contributions from numerous individuals and organizations.<br />
&nbsp;<wbr>*&nbsp;<wbr>Please see the COPYING and CONTRIBUTORS files for details. </p>
<p> This program and documentation is copyright to the authors named above. </p>
<p> Distributed under the GNU General Public License (GNU GPL) version 2 or later (GPLv2+).</p>
<h2>Questions</h2>
<p>Questions on the usage of this program can be sent to the <i>Squid Users mailing list</i> &lt;squid-users [at] squid-cache.org&gt; </p>
<p> Or contact your favorite RADIUS list/friend if the question is more related to RADIUS than Squid.</p>
<h2>Reporting Bugs</h2>
<p>Bug reports need to be made in English. See <a rel="nofollow" href="http://wiki.squid-cache.org/SquidFaq/BugReporting">http://wiki.squid-cache.org/SquidFaq/BugReporting</a> for details of what you need to include with your bug report. </p>
<p> Report bugs or bug fixes using <a rel="nofollow" href="http://bugs.squid-cache.org/">http://bugs.squid-cache.org/</a> </p>
<p> Report serious security bugs to <i>Squid Bugs &lt;squid-bugs [at] squid-cache.org&gt;</i> </p>
<p> Report ideas for new improvements to the <i>Squid Developers mailing list</i> &lt;squid-dev [at] squid-cache.org&gt;</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-squid/">squid</a></code>(8), <code><a href="/docs/linux/man/7-gpl/">GPL</a></code>(7),<br />
 <code>RFC2058</code> &#8211; Remote Authentication Dial In User Service (RADIUS)<br />
 The Squid FAQ wiki <a rel="nofollow" href="http://wiki.squid-cache.org/SquidFaq">http://wiki.squid-cache.org/SquidFaq</a><br />
 The Squid Configuration Manual <a rel="nofollow" href="http://www.squid-cache.org/Doc/config/">http://www.squid-cache.org/Doc/config/</a> </p>
