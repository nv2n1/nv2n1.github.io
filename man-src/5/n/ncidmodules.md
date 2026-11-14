---
title: "ncidmodules(5)"
name: "ncidmodules"
section: "5"
letter: "n"
url: "/docs/linux/man/5-ncidmodules/"
description: "ncidmodules.conf – ncid module configuration file"
---

<p><code>ncidmodules.conf</code> &#8211; ncid module configuration file</p>
<h2>Description</h2>
<p>The <i>ncidmodules.conf</i> file contains the configuration information for a <i>ncid</i>, output module and its init or rc file. Use <i>ncidmodules.conf</i> to to configure ncid for a particular output module, but use <i>ncid.conf</i> to configure ncid everytime it is started. For example, use <i>ncid.conf</i> to configure ncid for the server address, but use <i>ncidmodules.conf</i> to configure ncid to for ncid-page. </p>
<p> The <i>ncidmodules.conf</i> file is used to set options for:</p>
<dl>
<dd><i>ncid-kpopup</i><br />
 <i>ncid-mythtv</i><br />
 <i>ncid-page</i><br />
 <i>ncid-samba</i><br />
 <i>ncid-speak</i><br />
 <i>ncid-tivo</i><br />
 <i>ncid-yac</i></dl>
<p> The <i>ncidmodules.conf</i> file understands 3 types of lines:</p>
<dl>
<dt><code>blank line</code></p>
<dd>skip it</p>
<dt><code>comment line, beginning with &#8216;#&#8217;</code></p>
<dd>skip it</p>
<dt><code>shell variable set lines.</code></p>
<dd></dl>
<p> See ncidsmodules.conf for more details on the variables that can be set.</p>
<h2>Examples</h2>
<p>ncid command line options to call ncid-page at ring number 4:</p>
<dl>
<dd><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>ncid &#8211;call-prog &#8211;program ncid-page &#8211;ring 4
</dl>
<p> set the email address for ncid-page in ncidmodules.conf:</p>
<dl>
<dd><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>PageTo=cellphone [at] isp.com
</dl>
<h2>See Also</h2>
<p>ncid.1, ncidtools.1, lcdncid.1, out2osd.1, ncidd.8 ncidmodules.1 </p>
