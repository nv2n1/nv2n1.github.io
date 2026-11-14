---
title: "megarc(5)"
name: "megarc"
section: "5"
letter: "m"
url: "/docs/linux/man/5-megarc/"
description: "megarc – Configuration file for megatools"
---

<p>megarc &#8211; Configuration file for megatools</p>
<h2>Synopsis</h2>
<pre><i>~/.megarc</i>
<i>./.megarc</i></pre>
<h2>Description</h2>
<p>Megatools use INI configuration file to store commonly used login credentials. This makes it less bothersome to use the tools, as you can simply write </p>
<dl>
<dd>
<pre>$ megadf</pre>
</dl>
<p> instead of </p>
<dl>
<dd>
<pre>$ megadf --username my [at] email.com --password mypass</pre>
</dl>
<p> when using the tools. </p>
<p> Configuration file is read either from the current directory or user&#8217;s home directory. Exceptions are when &#8211;ignore-config-file was passed to the tool, or when explicit path to the config file was given via &#8211;config &lt;path&gt;.</p>
<h2>Config File Sections</h2>
<p>All sections are optional.</p>
<h3>[Login] Section</h3>
<p>Username</p>
<dl>
<dd>Your username.</dl>
<p> Password</p>
<dl>
<dd>Your password.</dl>
<h3>[Cache] Section</h3>
<p>Timeout</p>
<dl>
<dd>Cache timeout in seconds (default is 10 minutes).</dl>
<h2>Example</h2>
<p>Create ~/.megarc (on linux) or mega.ini file containing these 3 lines: </p>
<dl>
<dd>
<pre>[Login]
Username = your [at] email
Password = yourpassword</pre>
</dl>
<p> Run <code><a href="/docs/linux/man/1-megadf/">megadf</a></code>(1) to check that megatools are able to login to your account.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-megatools/">megatools</a></code>(7), <code><a href="/docs/linux/man/5-megarc/">megarc</a></code>(5), <code><a href="/docs/linux/man/1-megadf/">megadf</a></code>(1), <code><a href="/docs/linux/man/1-megadl/">megadl</a></code>(1), <code><a href="/docs/linux/man/1-megaget/">megaget</a></code>(1), <code><a href="/docs/linux/man/1-megals/">megals</a></code>(1), <code><a href="/docs/linux/man/1-megamkdir/">megamkdir</a></code>(1), <code><a href="/docs/linux/man/1-megaput/">megaput</a></code>(1), <code><a href="/docs/linux/man/1-megareg/">megareg</a></code>(1), <code><a href="/docs/linux/man/1-megarm/">megarm</a></code>(1), <code><a href="/docs/linux/man/1-megamv/">megamv</a></code>(1), <code><a href="/docs/linux/man/1-megasync/">megasync</a></code>(1), <code><a href="/docs/linux/man/1-megafs/">megafs</a></code>(1).</p>
<h2>Megatools</h2>
<p>Part of the <code><a href="/docs/linux/man/7-megatools/">megatools</a></code>(7) suite.</p>
<h2>Bugs</h2>
<p>Report bugs at <a rel="nofollow" href="https://github.com/megous/megatools">https://github.com/megous/megatools</a> or megous [at] megous.com.</p>
<h2>Author</h2>
<p>Megatools was written by Ondrej Jirman &lt;megous [at] megous.com&gt;, 2013. </p>
<p> Official website is <a rel="nofollow" href="http://megatools.megous.com.">http://megatools.megous.com.</a></p>
