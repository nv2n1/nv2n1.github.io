---
title: "fido-conf(5)"
name: "fido-conf"
section: "5"
letter: "f"
url: "/docs/linux/man/5-fido-conf/"
description: "fido.conf"
---

<p>fido.conf</p>
<h2>Synopsis</h2>
<p>fido.conf </p>
<p> The default file /etc/fido/fido.conf You can override the default file with the <font SIZE="-1">FIDORC</font> <font SIZE="-1">ENV</font> variable or the -f /path/file command line option.</p>
<h2>Description</h2>
<p>fido.conf is the configuration file for <tt>fido</tt>. The file consists of two parts, <font SIZE="-1">GLOBAL</font> settings and <font SIZE="-1">FILE</font> settings. <font SIZE="-1">GLOBAL</font> settings are best defined at the top of the file in key = value format. <font SIZE="-1">FILE</font> settings are distinguished with a filename followed by brackets {}. Key = value pairs inside the brackets apply only to that file. If a value isn&#8217;t set at the <font SIZE="-1">FILE</font> level, then <tt>fido</tt> applies a <font SIZE="-1">GLOBAL</font> setting. Here&#8217;s an example: </p>
<pre> # GLOBAL SETTINGS
 log = syslog
 pid = /var/run/fido.pid</pre>
<pre><code># FILE SETTINGS
/var/log/messages {
    log = /var/log/fido.log
}</code></pre>
<p> In this example, we&#8217;ve set &#8216;log&#8217; twice. Once at the <font SIZE="-1">GLOBAL</font> level and once at the <font SIZE="-1">FILE</font> level. The <font SIZE="-1">FILE</font> level takes precedent. In this case all logged activity for /var/log/messages monitoring will go to /var/log/fido.log If we log activity for other files that don&#8217;t have a &#8216;log&#8217; specified, then it will go to syslog. Here is a list of available settings:<br />
 <code>log</code> Use this setting to direct logging output. Its values can be either &#8216;syslog&#8217; or &#8216;/path/to/file&#8217; This option is available at both the <font SIZE="-1">GLOBAL</font> and <font SIZE="-1">FILE</font> levels. </p>
<pre> log = syslog
 log = /var/log/fido.log</pre>
<p><code>pid</code> Use this setting to assign a file to hold <tt>fido</tt>&#8216;s process <font SIZE="-1">ID</font> (pid). This option is available only at the <font SIZE="-1">GLOBAL</font> level. The default setting is /var/run/fido.pid </p>
<pre> pid = /home/jeff/var/fido.pid</pre>
<p><code>daemon</code> Use this option to run <tt>fido</tt> in the background as a daemon. By default, <tt>fido</tt> will run as a daemon. This setting is available only at the global level. It takes one of two values, true or false. It runs in the foreground when the setting is &#8216;false&#8217;<br />
 <code>rulesdir</code> fido monitors a log file and searches for pattern matches. These patterns are regular expressions that can be stored in a rules file. This directive tells <tt>fido</tt> where to look for its rules. By default, it will look in /etc/fido/rules You can override the default with this setting. This option is available <font SIZE="-1">ONLY</font> at the <font SIZE="-1">GLOBAL</font> level. </p>
<pre> rulesdir = /usr/local/etc/fido/rules</pre>
<p><code>rules</code> This is a <font SIZE="-1">FILES</font> level directive that tells <tt>fido</tt> where to find its pattern matches. It can take one of three different values, a regex, the &#8216;modified&#8217; directive or a file name. If the value is a regex, then <tt>fido</tt> will use that rule as it parses the file it&#8217;s watching. If the value is the &#8216;modified&#8217; directive, then it will trigger an alert each time the file is modified. If the value is a file name, then it will read <tt>$rulesdir</tt>/$rules for all it&#8217;s patterns. The benefit of using a file is that you can set many patterns, one on each line. <tt>fido</tt> will try each line as it looks for a match. </p>
<pre> rules = modified
 rules = .*OutOfMemory.*
 rules = exceeds N seconds|minutes|hours|days
 rules = haha.conf</pre>
<p>In the first example, <tt>fido</tt> will trigger an action if the modification date of the file it&#8217;s monitoring is changed. In the second example, it will tail the file it&#8217;s monitoring and trigger an action each time it matches the &#8216;.*OutOfMemory.*&#8217; pattern. In the third example, it will triggern an action if the file&#8217;s timestamp exceeds a designated time. If the file we&#8217;re monitoring is a directory, then an alert will be triggered if any file in that directory exceeds the designated time. In the final example, it will trigger an action each time it matches a pattern inside <tt>$rulesdir</tt>/haha.conf<br />
 <code>action</code> This is a <font SIZE="-1">FILES</font> level directive that tells <tt>fido</tt> what to do in the event of a pattern match. Generally, you&#8217;ll want to specify a script although you can specify a program with parameters: </p>
<pre> action = echo &quot;action alert!!!!&quot; | /usr/sbin/sendmail -v jeff [at] joedog.org
 action = /home/jeff/bin/haha</pre>
<p><code>throttle</code> This is a <font SIZE="-1">FILES</font> level directive which tells <tt>fido</tt> to delay place a delay between actions. This is useful to avoid flooding inboxes with emails or node managers with <font SIZE="-1">SMTP</font> traps. The trottle format is &#8216;throttle = N denomination&#8217; where &#8216;N&#8217; is a number and &#8216;denomination&#8217; is either &#8216;seconds&#8217;, &#8216;minutes&#8217;, &#8216;hours&#8217; or &#8216;days&#8217;. </p>
<pre> throttle = 15 minutes
 throttle = 1 hour
 throttle = 1 day(s)</pre>
<p><code>exclude</code> This is a <font SIZE="-1">FILES</font> level directive that only works when you monitor directories with the exceeds directive. The format is &#8216;exclude = [pattern]&#8217; where pattern is a regular expression. Consider this: </p>
<pre><code>/export {
    rule    = exceeds 7 days
    exclude = ^\.|CVS|Makefile
}</code></pre>
<p> Given this file block, <tt>fido</tt> will execute an action if any file inside the directory /export is older than 7 days but does <font SIZE="-1">NOT</font> start with &#8216;.&#8217; nor is it named <font SIZE="-1">CVS</font> or Makefile.<br />
 <code>capture</code> This is a <font SIZE="-1">FILES</font> level directive that tells <tt>fido</tt> to log the output from the action directive mentioned above. If you&#8217;re running sendmail -v, then it will log all that verbose output to its selected logging method. Good for debugging it takes one of two values, &#8216;true&#8217; or &#8216;false&#8217; &#8211; if false, it won&#8217;t log output. The default is false </p>
<pre> capture = true
 capture = false</pre>
<p><code>user</code> This is a <font SIZE="-1">GLOBAL</font> setting in which we specify which user <font SIZE="-1">ID</font> <tt>fido</tt> will run under. You&#8217;ll need to select a user that has read permissions to the file it&#8217;s monitoring and write permissions to the directory in which it&#8217;s logging. It is preferred that you select the least privileged user possible. </p>
<pre> user = jboss</pre>
<p><code>group</code> This is a <font SIZE="-1">GLOBAL</font> setting in which we specify with group <font SIZE="-1">ID</font> <tt>fido</tt> will run under. Like &#8216;user&#8217; we recommend you select the least privileged group possible </p>
<pre> group = jboss</pre>
<h2>Sample File</h2>
<pre> #
 # Global values 
 #
 log = syslog
 pid = /var/run/fido.pid
 daemon = true
 rulesdir = /etc/fido/rules
 user = root
 group = daemon</pre>
<pre> /var/log/httpd/access_log {
 rules = .*siege-.*tar.gz.*
 action = /usr/bin/tally
 log = /var/log/fido.log
 }</pre>
<pre> /var/log/maillog {
 rules = maillog.conf
 action = /usr/bin/react
 }</pre>
<pre> /var/log/haha.log {
 rules = ^haha.*
 action = echo &quot;alert!!!!&quot; | /usr/sbin/sendmail -v jeff [at] joedog.org
 capture = true
 }</pre>
