---
title: "ipmidetect-conf(5)"
name: "ipmidetect-conf"
section: "5"
letter: "i"
url: "/docs/linux/man/5-ipmidetect-conf/"
description: "ipmidetect.conf – specify alternate default values for the ipmidetect library"
---

<p>ipmidetect.conf &#8211; specify alternate default values for the ipmidetect library</p>
<h2>Description</h2>
<p>Through a configuration file, system administrators may override the default values used in the <code><a href="/docs/linux/man/3-ipmidetect_load_data/">ipmidetect_load_data</a>(3)</code> API function. </p>
<p> The configuration file is stored at /etc/freeipmi//ipmidetect.conf.</p>
<h2>Configuration Options</h2>
<p>The following are a list of configuration options that can be specified in the configuration file. Each configuration option must be listed on a separate line. Arguments for an option are separated by any amount of whitespace. Multiple arguments are also separated by whitespace. Comments can be marked by using the pound sign (&quot;#&quot;) character, and lines can be continued on the next using backslash (&quot;\&quot;).</p>
<dl>
<dt><i>hostnames host1 host2 host3 &#8230;</i></p>
<dd>Specify the hostname of the server to reach. Multiple hostnames can be listed up to a maximum of 8.</p>
<dt><i>port num</i></p>
<dd>Specify the port.</p>
<dt><i>timeout_len seconds</i></p>
<dd>Specify the timeout length in seconds.</dl>
<h2>Files</h2>
<p>/etc/freeipmi//ipmidetect.conf</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;freeipmi-users [at] gnu.org&gt; or &lt;freeipmi-devel [at] gnu.org&gt;.</p>
<h2>Copyright</h2>
<p>Copyright (C) 2007-2012 Lawrence Livermore National Security, LLC.<br />
 Copyright (C) 2007 The Regents of the University of California.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-libipmidetect/">libipmidetect</a>(3), <a href="/docs/linux/man/8-ipmidetect/">ipmidetect</a>(8) <a rel="nofollow" href="http://www.gnu.org/software/freeipmi/">http://www.gnu.org/software/freeipmi/</a> </p>
