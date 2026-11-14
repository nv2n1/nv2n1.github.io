---
title: "omnimapper(8)"
name: "omnimapper"
section: "8"
letter: "o"
url: "/docs/linux/man/8-omnimapper/"
description: "omniMapper – Simple proxy for CORBA naming service from omniORB"
---

<p>omniMapper &#8211; Simple proxy for CORBA naming service from omniORB</p>
<h2>Synopsis</h2>
<p><code>omniMapper</code> [<i>options</i>]</p>
<h2>Description</h2>
<p>This manual page documents briefly the <code>omniMapper</code> command. </p>
<p> <code>omniMapper</code> is a simple daemon which listens on port 2809 (or any other port) and redirects IIOP requets for configured object keys to associated persistent IORs. It can be used to make a naming service (even an old non-INS aware version of omniNames or other ORB&#8217;s naming service) appear on port 2809 with the object key <i>NameService</i>. The same goes for any other service you may wish to specify, such as an interace repository.</p>
<h2>Options</h2>
<p>A summary of options is included below. For a complete description, see the HTML pages included in the omniorb4-doc package.</p>
<dl>
<dt><code>-port</code><i>&nbsp;<wbr>port</i></p>
<dd>This allows you to choose a port other than 2809 to listen on.</p>
<dt><code>-config</code><i>&nbsp;<wbr>config_file</i></p>
<dd>This specifies a location for the configuration file. The default name is <i>/etc/omniMapper.cfg</i>.</p>
<dt><code>-v</code></p>
<dd><code>omniMapper</code> does not normally print anything; this option makes it verbose so it prints configuration information and a record of the redirections it makes to standard output.</dl>
<h2>Configuration File</h2>
<p>The configuration file is very simple. Each line contains a string to be used as an object key, some white space and an IOR (or any valid URI) that it will redirect that object key to. Comments should be prefixed with a <i>#</i> character. For example: </p>
<p>&nbsp;<wbr>#&nbsp;<wbr>Example omniMapper.cfg </p>
<p>&nbsp;<wbr>NameService&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>IOR:000f&#8230; </p>
<p>&nbsp;<wbr>InterfaceRepository IOR:0100&#8230;</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-omninames/">omniNames</a></code>(8).<br />
 The programs are documented fully by the HTML documentation in the omniorb4-doc package.</p>
<h2>Author</h2>
<p>omniMapper was written by Duncan Grisby &lt;duncan [at] grisby.org&gt; </p>
<p> This manual page was written by Floris Bruynooghe &lt;floris.bruynooghe [at] gmail.com&gt;, for the Debian project (but may be used by others).</p>
