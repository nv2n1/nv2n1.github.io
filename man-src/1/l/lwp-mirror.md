---
title: "lwp-mirror(1)"
name: "lwp-mirror"
section: "1"
letter: "l"
url: "/docs/linux/man/1-lwp-mirror/"
---

<h2 class="name">NAME</h2>
 

 lwp-mirror - Simple mirror utility 

<h2>SYNOPSIS</h2>

 <pre><code>
lwp - mirror[-v][-t timeout]&lt;url&gt;&lt;local file&gt;
</code></pre>

<h2>DESCRIPTION</h2>

 This program can be used to mirror a document from a <font SIZE="-1">WWW</font> server. The document is only transferred if the remote copy is newer than the local copy. If the local copy is newer nothing happens. 

 Use the <tt>&quot;-v&quot;</tt> option to print the version number of this program. 

 The timeout value specified with the <tt>&quot;-t&quot;</tt> option. The timeout value is the time that the program will wait for response from the remote server before it fails. The default unit for the timeout value is seconds. You might append ``m'' or ``h'' to the timeout value to make it minutes or hours, respectively. 

 Because this program is implemented using the <font SIZE="-1">LWP</font> library, it only supports the protocols that <font SIZE="-1">LWP</font> supports.

<h2>SEE ALSO</h2>

 lwp-request, <font SIZE="-1">LWP</font>

<h2>AUTHOR</h2>

 Gisle Aas &lt;gisle [at] aas.no&gt; 

<h2>Index</h2>


