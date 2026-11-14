---
title: "digest_file_auth(8)"
name: "digest_file_auth"
section: "8"
letter: "d"
url: "/docs/linux/man/8-digest_file_auth/"
description: "digest_file_auth – File based digest authentication helper for Squid."
---

<p>digest_file_auth &#8211; File based digest authentication helper for Squid. </p>
<p> Version 1.1</p>
<h2>Synopsis</h2>
<p><code>digest_file_auth</code> <code>[-c]</code> file</p>
<h2>Description</h2>
<p><code>digest_file_auth</code> is an installed binary authentication program for Squid. It handles digest authentication protocol and authenticates against a text file backend. This program will automatically detect the existence of a concurrecy channel-ID and adjust appropriately. It may be used with any value 0 or above for the auth_param children concurrency= parameter.</p>
<h2>Options</h2>
<dl>
<dt><code>-c</code></p>
<dd>Accept digest hashed passwords rather than plaintext in the password file</dl>
<h2>Configuration</h2>
<p>Username database file format:</p>
<dl>
<dt>&#8211; comment lines are possible and should start with a &#8216;#&#8217;;</p>
<dd>
<dt>&#8211; empty or blank lines are possible;</p>
<dd>
<dt>&#8211; plaintext entry format is username:password</p>
<dd>
<dt>&#8211; HA1 entry format is username:realm:HA1</p>
<dd></dl>
<p> To build a directory integrated backend, you need to be able to calculate the HA1 returned to squid. To avoid storing a plaintext password you can calculate <code>MD5(username:realm:password) </code> when the user changes their password, and store the tuple <code>username:realm:HA1.</code> then find the matching <code>username:realm </code> when squid asks for the HA1. </p>
<p> This implementation could be improved by using such a triple for the file format. However storing such a triple does little to improve security: If compromised the <code>username:realm:HA1 </code> combination is &quot;plaintext equivalent&quot; &#8211; for the purposes of digest authentication they allow the user access. Password syncronisation is not tackled by digest &#8211; just preventing on the wire compromise.</p>
<h2>Author</h2>
<p>This program was written by <i>Robert Collins &lt;robertc [at] squid-cache.org&gt;</i> </p>
<p> Based on prior work by <i>Arjan de Vet &lt;Arjan.deVet [at] adv.iae.nl&gt;</i> o4a&#8217;hide&#8217; .I Robert Collins &lt;robertc [at] squid-cache.org&gt; <i>Amos Jeffries &lt;amosjeffries [at] squid-cache.org&gt;</i></p>
<h2>Copyright</h2>
<p>&nbsp;<wbr>*&nbsp;<wbr>Copyright&nbsp;<wbr>(C)&nbsp;<wbr>1996-2016 The Squid Software Foundation and contributors<br />
&nbsp;<wbr>*<br />
&nbsp;<wbr>*&nbsp;<wbr>Squid software is distributed under GPLv2+&nbsp;<wbr>license and includes<br />
&nbsp;<wbr>*&nbsp;<wbr>contributions from numerous individuals and organizations.<br />
&nbsp;<wbr>*&nbsp;<wbr>Please see the COPYING and CONTRIBUTORS files for details. </p>
<p> This program and documentation is copyright to the authors named above. </p>
<p> Distributed under the GNU General Public License (GNU GPL) version 2 or later (GPLv2+).</p>
<h2>Questions</h2>
<p>Questions on the usage of this program can be sent to the <i>Squid Users mailing list</i> &lt;squid-users [at] squid-cache.org&gt;</p>
<h2>Reporting Bugs</h2>
<p>Bug reports need to be made in English. See <a rel="nofollow" href="http://wiki.squid-cache.org/SquidFaq/BugReporting">http://wiki.squid-cache.org/SquidFaq/BugReporting</a> for details of what you need to include with your bug report. </p>
<p> Report bugs or bug fixes using <a rel="nofollow" href="http://bugs.squid-cache.org/">http://bugs.squid-cache.org/</a> </p>
<p> Report serious security bugs to <i>Squid Bugs &lt;squid-bugs [at] squid-cache.org&gt;</i> </p>
<p> Report ideas for new improvements to the <i>Squid Developers mailing list</i> &lt;squid-dev [at] squid-cache.org&gt;</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-squid/">squid</a></code>(8), <code><a href="/docs/linux/man/7-gpl/">GPL</a></code>(7),<br />
 The Squid FAQ wiki <a rel="nofollow" href="http://wiki.squid-cache.org/SquidFaq">http://wiki.squid-cache.org/SquidFaq</a><br />
 The Squid Configuration Manual <a rel="nofollow" href="http://www.squid-cache.org/Doc/config/">http://www.squid-cache.org/Doc/config/</a> </p>
