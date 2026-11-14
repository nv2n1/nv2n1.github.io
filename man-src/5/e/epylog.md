---
title: "epylog(5)"
name: "epylog"
section: "5"
letter: "e"
url: "/docs/linux/man/5-epylog/"
description: "epylog.conf – epylog configuration"
---

<p><code>epylog.conf</code> &#8211; epylog configuration</p>
<h2>Synopsis</h2>
<p><code>epylog</code> config file is a simple plaintext file in win.ini style format. </p>
<h2>Location</h2>
<p>Epylog will look in /etc/epylog/epylog.conf by default, but you can override that by passing -c switch on the command line.</p>
<h2>[main]</h2>
<dl>
<dt><code>cfgdir</code></p>
<dd>This is where epylog should look for other configuration information, most notably, <code>modules.d</code> directory. See <i><a href="/docs/linux/man/5-epylog-modules/">epylog-modules</a>(5)</i> for more info.</p>
<dt><code>tmpdir</code></p>
<dd>Where to create temporary directories and put temporary files. Note that log files can grow VERY big and epylog might create several copies of them for processing purposes. Make sure there is no danger of filling up that partition. A good place on a designated loghost is /var/tmp, since that is usually a separate partition dedicated entirely for logs.</p>
<dt><code>vardir</code></p>
<dd>Where epylog should save its state data, namely the offsets.xml file. The sanest place for this is /var/lib/epylog.</p>
<dt><code>multimatch</code></p>
<dd>By default, if a line is matched against a module, no other modules will be tried. This helps speed things up tremendously. However, you may have several modules that process the same lines (although this is not a very good setup). In that case you may set this to &quot;yes&quot;. The default value is &quot;no&quot;.</p>
<dt><code>threads</code></p>
<dd>How many processing threads to start. 50 is a good default value, but you may set it to less or more, depending on your system. </p>
</dl>
<h2>[report]</h2>
<dl>
<dt><code>title </code></p>
<dd>What should be the title of the report. For mailed reports, this is the subject of the message. For the ones published on the web, this is the title of the page (as in &lt;title&gt;&lt;/title&gt;).</p>
<dt><code>template</code></p>
<dd>Which html template should be used for the final report. See the source of the default template for the format used.</p>
<dt><code>include_unparsed</code></p>
<dd>Can be either &quot;yes&quot; or &quot;no&quot;. If &quot;no&quot; is specified, strings that didn&#8217;t match any of the modules will not be appended to the report. Not very wise! A good setting is &quot;yes&quot;.</p>
<dt><code>publishers</code></p>
<dd>Lists the publishers to use. The value is the name of the section where to look for the publisher configuration. E.g.:<br />
 <code>publishers = nfspub</code><br />
 will look for a section called &quot;[nfspub]&quot; for publisher initialization. The name of the publisher has nothing to do with the method it uses for publishing. The fact that the default are named [file] and [mail] is only a matter of convenience. List multiple values separated by a comma. </p>
</dl>
<h2>Mail Publisher</h2>
<dl>
<dt><code>method</code></p>
<dd>Method must be set to &quot;mail&quot; for this publisher to be considered a mail publisher.</p>
<dt><code>smtpserv</code></p>
<dd>Can be either a hostname of an SMTP server to use, or the location of a sendmail binary. If the value starts with a &quot;/&quot; it will be considered a path. E.g. valid entries:<br />
 <code>smtpserv = mail.example.com</code><br />
 <code>smtpserv = /usr/sbin/sendmail -t</code></p>
<dt><code>mailto</code></p>
<dd>The list of email addresses where to mail the report. Separate multiple entries by a comma. If ommitted, &quot;root [at] localhost&quot; will be used.</p>
<dt><code>format</code></p>
<dd>Can be one of the following: <code>html</code>, <code>plain</code>, or <code>both</code>. If you use a mail client that doesn&#8217;t support html mail, then you better use &quot;plain&quot; or &quot;both&quot;, though you will miss out on visual cueing that epylog uses to notify of important events.</p>
<dt><code>lynx</code></p>
<dd>This is only useful if you use format other than &quot;html&quot;. Epylog will use a lynx-compliant tool to transform HTML into plain text. The following browsers are known to work: lynx, elinks, w3m.</p>
<dt><code>include_rawlogs</code></p>
<dd>Whether to include the gzipped raw logs with the message. If set to &quot;yes&quot;, it will attach the file with all processed logs with the message. If you use a file publisher in addition to the mail publisher, this may be a tad too paranoid.</p>
<dt><code>rawlogs_limit</code></p>
<dd>If the size of rawlogs.gz is more than this setting (in kilobytes), then raw logs will not be attached. Useful if you have a 50Mb log and check your mail over a slow uplink. </p>
</dl>
<h2>File Publisher</h2>
<dl>
<dt><code>method</code></p>
<dd>Method must be set to &quot;file&quot; for this config to work as a file publisher.</p>
<dt><code>path</code></p>
<dd>Where to place the directories with reports. A sensible location would be in /var/www/html/epylog. Note that the reports may contain sensitive information, so make sure you place a .htaccess in that directory and require a password, or limit by host.</p>
<dt><code>dirmask, filemask</code></p>
<dd>These are the masks to be used for the created directories and files. For format values look at strftime documentation here: <a rel="nofollow" href="http://www.python.org/doc/current/lib/module-time.html">http://www.python.org/doc/current/lib/module-time.html</a></p>
<dt><code>expire_in</code></p>
<dd>A digit specifying the number of days after which the old directories should be removed. Default is 7.</p>
<dt><code>notify</code></p>
<dd>Optionally send notifications to these email addresses when new reports become available. Comment out if no notification is desired. This is definitely redundant if you also use the mail publisher.</p>
<dt><code>smtpserv</code></p>
<dd>Use this smtp server when sending notifications. Can be either a hostname or a path to sendmail. Defaults to &quot;/usr/sbin/sendmail -t&quot;.</p>
<dt><code>pubroot</code></p>
<dd>When generating a notification message, use this as publication root to make a link. E.g.:<br />
 <code>pubroot = <a rel="nofollow" href="http://www.example.com/epylog">http://www.example.com/epylog</a></code><br />
 will make a link: <a rel="nofollow" href="http://www.example.com/epylog/dirname/filename.html">http://www.example.com/epylog/dirname/filename.html</a> </p>
</dl>
<h2>Comments</h2>
<p>Lines starting with &quot;#&quot; will be considered commented out.</p>
<h2>Authors</h2>
<p>Konstantin Ryabitsev &lt;icon [at] linux.duke.edu&gt;</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-epylog/">epylog</a>(3), <a href="/docs/linux/man/8-epylog/">epylog</a>(8), <a href="/docs/linux/man/5-epylog-modules/">epylog-modules</a>(5) </p>
