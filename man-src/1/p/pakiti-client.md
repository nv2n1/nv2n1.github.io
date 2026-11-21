---
title: "pakiti-client(1)"
name: "pakiti-client"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pakiti-client/"
description: "pakiti-client – report the list of installed packages to a collecting server"
---

<h2>SYNOPSIS</h2>
<p> <code>pakiti-client</code> [<i></i><font SIZE="-1"><i>OPTIONS</i></font><i></i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>pakiti-client</code> finds the list of installed packages (i.e. <tt>&quot;rpm -qa&quot;</tt> on an RPM-based system) and formats it in a report that it sends (using a <font SIZE="-1">POST</font> request) to a collecting server (see the <code>&#8211;url</code> option) and/or writes to a file (see the <code>&#8211;output</code> option). </p>
<p> In addition to the list of installed packages, the report also contains information about the submitting machine:</p>
<dl>
<dt>&bull;</dt>
<dd> <tt>&quot;arch&quot;</tt>: the current architecture</dd>
<dt>&bull;</dt>
<dd> <tt>&quot;host&quot;</tt>: the host name (see the <code>&#8211;host</code> option)</dd>
<dt>&bull;</dt>
<dd> <tt>&quot;kernel&quot;</tt>: the current kernel</dd>
<dt>&bull;</dt>
<dd> <tt>&quot;packager&quot;</tt>: the packager (<tt>&quot;rpm&quot;</tt> or <tt>&quot;dpkg&quot;</tt>)</dd>
<dt>&bull;</dt>
<dd> <tt>&quot;site&quot;</tt>: the site name (see the <code>&#8211;site</code> option)</dd>
<dt>&bull;</dt>
<dd> <tt>&quot;system&quot;</tt>: the operating system full name</dd>
<dt>&bull;</dt>
<dd> <tt>&quot;tag&quot;</tt>: a tag used by the collecting server (see the <code>&#8211;tag</code> option)</dd>
<dt>&bull;</dt>
<dd> <tt>&quot;version&quot;</tt>: the report format version (<tt>1</tt>)</dd></dl>
<p> If a certificate (see the <code>&#8211;encrypt</code> option) is given then the report will be S/MIME encrypted before transmission. </p>
<p> The recommended way to use this program is daily via <tt>&quot;cron&quot;</tt>, for instance with (using bash): </p>
<pre>
  # echo &quot;MAILTO=somebody [at] some.where&quot; &gt; /etc/cron.d/pakiti-client
  # echo &quot;$((RANDOM % 60)) $((RANDOM % 24)) * * * nobody pakiti-client \
    --config /etc/pakiti-client.cfg&quot; &gt;&gt; /etc/cron.d/pakiti-client
</pre>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;config</code>, <code>&#8211;conf</code> <i></i><font SIZE="-1"><i>PATH</i></font><i></i></dt>
<dd> use this configuration file before processing the command line parameters</dd>
<dt><code>&#8211;curl</code> <i></i><font SIZE="-1"><i>PATH</i></font><i></i></dt>
<dd> set the path of the <tt>&quot;curl&quot;</tt> command to use</dd>
<dt><code>&#8211;dpkg-query</code> <i></i><font SIZE="-1"><i>PATH</i></font><i></i></dt>
<dd> set the path of the <tt>&quot;dpkg-query&quot;</tt> command to use</dd>
<dt><code>&#8211;encrypt</code> <i></i><font SIZE="-1"><i>PATH</i></font><i></i>|<i></i><font SIZE="-1"><i>STRING</i></font><i></i></dt>
<dd> use this certificate to encrypt the report; the value can either be the path of the file containing the certificate or the certificate itself as multi-line <font SIZE="-1">ASCII</font> armored contents</dd>
<dt><code>&#8211;expect</code> <i></i><font SIZE="-1"><i>STRING</i></font><i></i></dt>
<dd> set the response string to expect from the server in case of success (default: <tt>&quot;OK&quot;</tt>)</dd>
<dt><code>&#8211;help</code>, <code>-h</code>, <code>-?</code></dt>
<dd> show some help</dd>
<dt><code>&#8211;host</code> <i></i><font SIZE="-1"><i>STRING</i></font><i></i></dt>
<dd> set the host name to use in the report</dd>
<dt><code>&#8211;hostname</code> <i></i><font SIZE="-1"><i>PATH</i></font><i></i></dt>
<dd> set the path of the <tt>&quot;hostname&quot;</tt> command to use</dd>
<dt><code>&#8211;input</code>, <code>-i</code> <i></i><font SIZE="-1"><i>PATH</i></font><i></i></dt>
<dd> do not prepare a new report but, instead, read the report from the given file</dd>
<dt><code>&#8211;lsb_release</code> <i></i><font SIZE="-1"><i>PATH</i></font><i></i></dt>
<dd> set the path of the <tt>&quot;lsb_release&quot;</tt> command to use</dd>
<dt><code>&#8211;manual</code>, <code>-m</code></dt>
<dd> show this manual</dd>
<dt><code>&#8211;openssl</code> <i></i><font SIZE="-1"><i>PATH</i></font><i></i></dt>
<dd> set the path of the <tt>&quot;openssl&quot;</tt> command to use</dd>
<dt><code>&#8211;output</code>, <code>-o</code> <i></i><font SIZE="-1"><i>PATH</i></font><i></i></dt>
<dd> write the prepared report to the given file</dd>
<dt><code>&#8211;rndsleep</code>, <code>-r</code> <i></i><font SIZE="-1"><i>NUMBER</i></font><i></i></dt>
<dd> sleep for a random amount of seconds, up to the given number (useful when <code>pakiti-client</code> is invoked by <tt>&quot;cron&quot;</tt>)</dd>
<dt><code>&#8211;rpm</code> <i></i><font SIZE="-1"><i>PATH</i></font><i></i></dt>
<dd> set the path of the <tt>&quot;rpm&quot;</tt> command to use</dd>
<dt><code>&#8211;site</code> <i></i><font SIZE="-1"><i>NAME</i></font><i></i></dt>
<dd> set the site name to use in the report</dd>
<dt><code>&#8211;tag</code> <i></i><font SIZE="-1"><i>STRING</i></font><i></i></dt>
<dd> set the tag used by the collecting server to group reports</dd>
<dt><code>&#8211;uname</code> <i></i><font SIZE="-1"><i>PATH</i></font><i></i></dt>
<dd> set the path of the <tt>&quot;uname&quot;</tt> command to use</dd>
<dt><code>&#8211;url</code> <i></i><font SIZE="-1"><i>URL</i></font><i></i></dt>
<dd> send the prepared report to the collecting server at the given <font SIZE="-1">URL</font></dd>
<dt><code>&#8211;wget</code> <i></i><font SIZE="-1"><i>PATH</i></font><i></i></dt>
<dd> set the path of the <tt>&quot;wget&quot;</tt> command to use</dd></dl>
<h2>CONFIGURATION FILE</h2>
<p> <code>pakiti-client</code> can read its options from a configuration file (see the <code>&#8211;config</code> option). </p>
<p> The file can contain empty lines, comments (lines starting with <tt>&quot;#&quot;</tt>) or option settings either on one line or using the &#8220;heredoc&#8221; syntax. For instance: </p>
<pre><code>
#
#this is my pakiti - client configuration
#
url = http : // some.where.org:8080/some/path
             encrypt =
                 &lt;&lt; EOT-- -- -BEGIN CERTIFICATE-- -- -VR0gBF0wWzBZBgorBgEEAWAKBAsBMEswSQYIKwYBBQUHAgEWPWh0dHA6Ly9jYWZp
                            U2VydmljZXMsQ049U22ydmljZXMsQ049Q29uZmlndXJhdGlvbixEQz1jZXJuLERD... CREUmgapD +
                        aWdxEfeb6qA0OqAFCeHYOWMeeqqtMUE1JPGPoWNkyzqaObr05jm0zd
                            YwYIKwYBBQUHMAKGV2h0dHA6Ly6jYWZpbGVzLmNlcm4uY2gvY2FmaWxlcy9jZXJ =
                        -- -- -END CERTIFICATE-- -- -EOT
</code></pre>
<p> The options specified on the command line have precedence over the ones found in the configuration file.</p>
<h2>AUTHOR</h2>
<p> Lionel Cons &lt;<a rel="nofollow" href="http://cern.ch/lionel.cons">http://cern.ch/lionel.cons</a>&gt;</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) <font SIZE="-1">CERN 2014-2015</font> </p>
<p> Licensed under the Apache License, Version 2.0 (the &#8220;License&#8221;); you may not use this file except in compliance with the License. You may obtain a copy of the License at: &lt;<a rel="nofollow" href="http://www.apache.org/licenses/LICENSE-2.0">http://www.apache.org/licenses/LICENSE-2.0</a>&gt;. </p>
<p> Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an &#8220;<font SIZE="-1">AS IS&#8221; BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,</font> either express or implied. See the License for the specific language governing permissions and limitations under the License. </p>
