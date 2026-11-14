---
title: "archmage(1)"
name: "archmage"
section: "1"
letter: "a"
url: "/docs/linux/man/1-archmage/"
description: "archmage – CHM(Compiled HTML) Decompressor."
---

<h2 class="name">NAME</h2>
<p> archmage &#8211; CHM(Compiled HTML) Decompressor. </p>
<h2>SYNOPSIS</h2>
<p> <code>archmage</code> <i>chmfile directory</i><br />
 <code>archmage</code> -p port <i>chmfile</i></p>
<h2>DESCRIPTION</h2>
<p> This manual page documents briefly the <code>archmage</code> command. This manual page was written for the Debian distribution because the original program does not have a manual page. </p>
<p> <code>arCHMage</code> is an extensible reader and decompiler for files in the CHM format. This is the format used by Microsoft HTML Help, and is also known as Compiled HTML. arCHMage is based on python-chm binding to chmlib from GnoCHM project.</p>
<h2>USAGE</h2>
<p> There is three ways to use arCHMage package now: </p>
<p> 1) Extract .chm to directory (directory will be created): </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>archmage &lt;chmfile&gt; &lt;directory&gt;</p>
<p> 2) Run as http-server, which will publish chm file contents on specified port: </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>archmage -p &lt;port&gt; &lt;chmfile&gt;</p>
<p> 3) Tune your apache to publish chm file contents if there is trailing slash in request to that file (you will need working mod_python for that): </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Add that lines to your httpd.conf:</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt> AddHandler python-program .chm </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt> PythonHandler archmod.mod_chm</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Restart apache.</p>
<p> Let&#8217;s suppose, you have file sample.chm in DocumentRoot of your apache. After that tuning you can receive raw chm file, if you point your browser to </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><a rel="nofollow" href="http://yourserver/sample.chm">http://yourserver/sample.chm</a></p>
<p> or you can view chm file on the fly if you point your browser to </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><a rel="nofollow" href="http://yourserver/sample.chm/">http://yourserver/sample.chm/</a> (note trailing slash)</p>
<h2>FILES</h2>
<dl>
<dt>/etc/archmage/arch.conf</p>
<dd> System-wide configuration file.</dl>
<h2>SEE ALSO</h2>
<p> arCHMage Home Page: <a rel="nofollow" href="http://archmage.sf.net">http://archmage.sf.net</a></p>
<h2>AUTHOR</h2>
<p> arCHMage was written by Eugeny Korekin &lt;az [at] ftc.ru&gt; </p>
<p> This manual page was written by Basil Shubin &lt;bashu [at] users.sourceforge.net&gt;, for the Debian GNU/Linux system (but may be used by others). </p>
<h2>Index</h2>
