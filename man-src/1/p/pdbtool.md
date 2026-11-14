---
title: "pdbtool(1)"
name: "pdbtool"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pdbtool/"
description: "pdbtool – An application to test and convert syslog-ng pattern database rules"
---

<h2 class="name">NAME</h2>
<p> pdbtool &#8211; An application to test and convert syslog-ng pattern database rules </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>pdbtool</code> [command] [options]</dl>
<h2>DESCRIPTION</h2>
<dd>This manual page is only an abstract; for the complete documentation of syslog-ng and pdbtool, see m[blue]<code>The syslog-ng Administrator Guide</code>m[]<font SIZE="-2">[1]</font>. </p>
<p> The syslog-ng application can match the contents of the log messages to a database of predefined message patterns (also called patterndb). By comparing the messages to the known patterns, syslog-ng is able to identify the exact type of the messages, tag the messages, and sort them into message classes. The message classes can be used to classify the type of the event described in the log message. The functionality of the pattern database is similar to that of the logcheck project, but the syslog-ng approach is faster, scales better, and is much easier to maintain compared to the regular expressions of logcheck. </p>
<p> The <code>pdbtool</code> application is a utility that can be used to: </p>
<dl>
<dt>
<dd> &bull; test message patterns;</dl>
<dl>
<dt>
<dd> &bull; convert an older pattern database to the latest database format;</dl>
<dl>
<dt>
<dd> &bull; merge pattern databases into a single file;</dl>
<dl>
<dt>
<dd> &bull; dump the RADIX tree built from the pattern database (or a part of it) to explore how the pattern matching works.</dl>
<h2>THE DUMP COMMAND</h2>
<dl>
<dt> <code>dump</code> [options]</dl>
<dd>Display the RADIX tree built from the patterns. This shows how are the patterns represented in syslog-ng and it might also help to track down pattern-matching problems. The dump utility can dump the tree used for matching the PROGRAM or the MSG parts. </p>
<p> <code>&#8211;pdb</code> or <code>-p</code></p>
<dl>
<dt>
<dd> Name of the pattern database file to use.</dl>
<p> <code>&#8211;program</code> or <code>-P</code></p>
<dl>
<dt>
<dd> Displays the RADIX tree built from the patterns belonging to the <i>$PROGRAM</i> application.</dl>
<p> <code>&#8211;program-tree</code> or <code>-T</code></p>
<dl>
<dt>
<dd> Display the <i>$PROGRAM</i> tree.</dl>
<p> Example and sample output: </p>
<dl>
<dt>
<dd>
<pre>
pdbtool dump -p patterndb.xml  -P 'sshd'
</pre>
</dl>
<dl>
<dt>
<dd>
<pre>
'p'
   'assword for'
     @QSTRING:@
       'from'
        @QSTRING:@
          'port '
            @NUMBER:@ rule_id='fc49054e-75fd-11dd-9bba-001e6806451b'
              ' ssh' rule_id='fc55cf86-75fd-11dd-9bba-001e6806451b'
                 '2' rule_id='fc4b7982-75fd-11dd-9bba-001e6806451b'
    'ublickey for'
      @QSTRING:@
        'from'
         @QSTRING:@
           'port '
             @NUMBER:@ rule_id='fc4d377c-75fd-11dd-9bba-001e6806451b'
               ' ssh' rule_id='fc5441ac-75fd-11dd-9bba-001e6806451b'
                  '2' rule_id='fc44a9fe-75fd-11dd-9bba-001e6806451b'
              
</pre>
</dl>
<h2>THE MATCH COMMAND</h2>
<dl>
<dt> <code>match</code> [options]</dl>
<dd>Use the <code>match</code> command to test the rules in a pattern database. The command tries to match the specified message against the patterns of the database, evaluates the parsers of the pattern, and also displays which part of the message was parsed successfully. The command returns with a <i>0</i> (success) or <i>1</i> (no match) return code and displays the following information: </p>
<dl>
<dt>
<dd> &bull; the class assigned to the message (that is, system, violation, and so on),</dl>
<dl>
<dt>
<dd> &bull; the ID of the rule that matched the message, and</dl>
<dl>
<dt>
<dd> &bull; the values of the parsers (if there were parsers in the matching pattern).</dl>
<p> The <code>match</code> command has the following options: </p>
<p> <code>&#8211;color-out </code> or <code>-c</code></p>
<dl>
<dt>
<dd> Color the terminal output to highlight the part of the message that was successfully parsed.</dl>
<p> <code>&#8211;debug-csv</code> or <code>-C</code></p>
<dl>
<dt>
<dd> Print the debugging information returned by the <i>&#8211;debug-pattern</i> option as comma-separated values.</dl>
<p> <code>&#8211;debug-pattern</code> or <code>-D</code></p>
<dl>
<dt>
<dd> Print debugging information about the pattern matching. See also the <i>&#8211;debug-csv</i> option.</dl>
<p> <code>&#8211;file=&lt;filename-with-path&gt;</code> or <code>-f</code></p>
<dl>
<dt>
<dd> Process the messages of the specified log file with the pattern database. This option allows to classify messages offline, and to apply the pattern database to already existing logfiles. To read the messages from the standard input (stdin), specify a hyphen (<i>&#8211;</i>) character instead of a filename.</dl>
<p> <code>&#8211;filter=&lt;filter-expression&gt;</code> or <code>-F</code></p>
<dl>
<dt>
<dd> Print only messages matching the specified syslog-ng filter expression.</dl>
<p> <code>&#8211;message</code> or <code>-M</code></p>
<dl>
<dt>
<dd> The text of the log message to match (only the <i>$MESSAGE</i> part without the syslog headers).</dl>
<p> <code>&#8211;pdb</code> or <code>-p</code></p>
<dl>
<dt>
<dd> Name of the pattern database file to use.</dl>
<p> <code>&#8211;program</code> or <code>-P</code></p>
<dl>
<dt>
<dd> Name of the program to use, as contained in the <i>$PROGRAM</i> part of the syslog message.</dl>
<p> <code>&#8211;template=&lt;template-expression&gt;</code> or <code>-T</code></p>
<dl>
<dt>
<dd> A syslog-ng template expression that is used to format the output messages.</dl>
<p> Example: The following command checks if the patterndb.xml file recognizes the <i>Accepted publickey for myuser from 127.0.0.1 port 59357 ssh2</i> message: </p>
<dl>
<dt>
<dd>
<pre>
pdbtool match -p patterndb.xml -P sshd -M &quot;Accepted publickey for myuser from 127.0.0.1 port 59357 ssh2&quot;
</pre>
</dl>
<p> The following example applies the sshd.pdb pattern database file to the log messages stored in the /var/log/messages file, and displays only the messages that received a <i>useracct</i> tag. </p>
<dl>
<dt>
<dd>
<pre>
pdbtool match -p sshd.pdb \
  -file /var/log/messages \
  -filter 'tags("usracct");' 
</pre>
</dl>
<h2>THE MERGE COMMAND</h2>
<dl>
<dt> <code>merge</code> [options]</dl>
<dd>Use the <code>merge</code> command to combine separate pattern database files into a single file (pattern databases are usually stored in separate files per applications to simplify maintenance). If a file uses an older database format, it is automatically updated to the latest format (V3). See the m[blue]<code>The syslog-ng Administrator Guide</code>m[]<font SIZE="-2">[1]</font> for details on the different pattern database versions. </p>
<p> <code>&#8211;directory</code> or <code>-D</code></p>
<dl>
<dt>
<dd> The directory that contains the pattern database XML files to be merged.</dl>
<p> <code>&#8211;glob</code> or <code>-G</code></p>
<dl>
<dt>
<dd> Specify filenames to be merged using a glob pattern, for example, using wildcards. For details on glob patterns, see <code>man glob</code>. This pattern is applied only to the filenames, and not on directory names.</dl>
<p> <code>&#8211;pdb</code> or <code>-p</code></p>
<dl>
<dt>
<dd> Name of the output pattern database file.</dl>
<p> <code>&#8211;recursive</code> or <code>-r</code></p>
<dl>
<dt>
<dd> Merge files from subdirectories as well.</dl>
<p> Example: </p>
<dl>
<dt>
<dd>
<pre>
pdbtool merge --recursive --directory /home/me/mypatterns/  --pdb /var/lib/syslog-ng/patterndb.xml
</pre>
</dl>
<p> Currently it is not possible to convert a file without merging, so if you only want to convert an older pattern database file to the latest format, you have to copy it into an empty directory.</p>
<h2>THE PATTERNIZE COMMAND</h2>
<dl>
<dt> <code>patternize</code> [options]</dl>
<dd>Automatically create a pattern database from a log file containing a large number of log messages. The resulting pattern database is printed to the standard output (stdout). The <code>pdbtool patternize</code> command uses a data clustering technique to find similar log messages and replacing the differing parts with <i>@ESTRING:: @</i> parsers. For details on pattern databases and message parsers, see the m[blue]<code>The syslog-ng Administrator Guide</code>m[]<font SIZE="-2">[1]</font>. The <code>patternize</code> command is available only in syslog-ng OSE version 3.2 and later. </p>
<p> <code>&#8211;file=&lt;path&gt;</code> or <code>-f</code></p>
<dl>
<dt>
<dd> The logfile containing the log messages to create patterns from. To receive the log messages from the standard input (stdin), use <i>&#8211;</i>.</dl>
<p> <code>&#8211;iterate-outliers</code> or <code>-o</code></p>
<dl>
<dt>
<dd> Recursively iterate on the log lines to cover as many log messages with patterns as possible.</dl>
<p> <code>&#8211;named-parsers</code> or <code>-n</code></p>
<dl>
<dt>
<dd> The number of example log messages to include in the pattern database for every pattern. Default value: <i>1</i></dl>
<p> <code>&#8211;samples=&lt;number-of-samples&gt;</code></p>
<dl>
<dt>
<dd> Include a generated name in the parsers, for example, <i>.dict.string1</i>, <i>.dict.string2</i>, and so on.</dl>
<p> <code>&#8211;support=&lt;number&gt;</code> or <code>-S</code></p>
<dl>
<dt>
<dd> A pattern is added to the output pattern database if at least the specified percentage of log messages from the input logfile match the pattern. For example, if the input logfile contains 1000 log messages and the <i>&#8211;support=3.0</i> option is used, a pattern is created only if the pattern matches at least 3 percent of the log messages (that is, 30 log messages). If patternize does not create enough patterns, try to decrease the support value. </p>
<p> Default value: <i>4.0</i></dl>
<p> Example: </p>
<dl>
<dt>
<dd>
<pre>
pdbtool patternize --support=2.5 --file=/var/log/messages
</pre>
</dl>
<h2>THE TEST COMMAND</h2>
<dl>
<dt> <code>test</code> [options]</dl>
<dd>Use the <code>test</code> command to validate a pattern database XML file. Note that you must have the <code>xmllint</code> application installed. The <code>test</code> command is available only in syslog-ng OSE version 3.2 and later. </p>
<p> <code>&#8211;validate</code></p>
<dl>
<dt>
<dd> Validate a pattern database XML file.</dl>
<p> Example: </p>
<dl>
<dt>
<dd>
<pre>
pdbtool test --validate /home/me/mypatterndb.pdb
</pre>
</dl>
<h2>FILES</h2>
<p> /home/algernon/install/syslog-ng/3.5/bin/pdbtool </p>
<p> /home/algernon/install/syslog-ng/3.5/etc/syslog-ng/syslog-ng.conf</p>
<h2>SEE ALSO</h2>
<p> m[blue]<code>The syslog-ng Administrator Guide</code>m[]<font SIZE="-2">[1]</font> </p>
<p> <code><a href="/docs/linux/man/5-syslog-ng-conf/">syslog-ng.conf</a></code>(5) </p>
<p> <code><a href="/docs/linux/man/8-syslog-ng/">syslog-ng</a></code>(8) </p>
<p> m[blue]<code>The syslog-ng OSE 3.3 Administrator Guide</code>m[]<font SIZE="-2">[1]</font> </p>
<p> If you experience any problems or need help with syslog-ng, visit m[blue]<code>visit the syslog-ng wiki</code>m[]<font SIZE="-2">[2]</font> or the m[blue]<code>syslog-ng mailing list</code>m[]<font SIZE="-2">[3]</font>. </p>
<p> For news and notifications about of syslog-ng, visit the m[blue]<code>syslog-ng Insider Blog</code>m[]<font SIZE="-2">[4]</font>.</p>
<h2>AUTHOR</h2>
<p> This manual page was written by the BalaBit Documentation Team &lt;documentation [at] balabit.com&gt;.</p>
<h2>COPYRIGHT</h2>
<h3></h3>
<p> The authors grant permission to copy, distribute and/or modify this manual page under the terms of the GNU General Public License Version 2 or newer (GPL v2+).</p>
<h2>NOTES</h2>
<dl>
<dt> 1.</p>
<dd>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><code>The syslog-ng Administrator Guide</code><br />
&nbsp;<wbr>&nbsp;<wbr></p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://www.balabit.com/support/documentation/">http://www.balabit.com/support/documentation/</a></dl>
<dt> 2.</p>
<dd> visit the syslog-ng wiki</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://www.balabit.com/wiki/syslog-ng-faq">http://www.balabit.com/wiki/syslog-ng-faq</a></dl>
<dt> 3.</p>
<dd> <code>syslog-ng mailing list</code></p>
<dl>
<dt>
<dd> <a rel="nofollow" href="https://lists.balabit.hu/mailman/listinfo/syslog-ng">https://lists.balabit.hu/mailman/listinfo/syslog-ng</a></dl>
<dt> 4.</p>
<dd> <code>syslog-ng Insider Blog</code></p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://insider.blogs.balabit.com">http://insider.blogs.balabit.com</a></dl>
</dl>
<h2>Index</h2>
<dt><a href="#lbAO">NOTES</a></p>
<dd></dl>
