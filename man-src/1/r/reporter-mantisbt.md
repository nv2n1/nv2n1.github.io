---
title: "reporter-mantisbt(1)"
name: "reporter-mantisbt"
section: "1"
letter: "r"
url: "/docs/linux/man/1-reporter-mantisbt/"
description: "reporter-mantisbt – Reports problem to Mantis Bug Tracker."
---

<h2 class="name">NAME</h2>
<p> reporter-mantisbt &#8211; Reports problem to Mantis Bug Tracker. </p>
<h2>SYNOPSIS</h2>
<p> <i>reporter-mantisbt</i> [-vrf] [-c CONFFILE]&#8230; [-F FMTFILE] [-A FMTFILE2] -d DIR </p>
<p> Or: </p>
<p> <i>reporter-mantisbt</i> [-v] [-c CONFFILE]&#8230; [-d DIR] -t[ID] FILE&#8230; </p>
<p> Or: </p>
<p> <i>reporter-mantisbt</i> [-v] [-c CONFFILE]&#8230; -h DUPHASH</p>
<h2>DESCRIPTION</h2>
<p> The tool reads problem directory DIR. Then it logs in to MantisBT and tries to find an issue with the same duphash HEXSTRING in <i>abrt_hash</i> field. </p>
<p> If such issue is not found, then a new issue is created. Elements of DIR are stored in the issue as part of issue description or as attachments, depending on their type and size. </p>
<p> Otherwise, if such issue is found and it is marked as CLOSED DUPLICATE, the tool follows the chain of duplicates until it finds a non-DUPLICATE issue. The tool adds a new note to found issue. </p>
<p> The URL to new or modified issue is printed to stdout and recorded in <i>reported_to</i> element in DIR. </p>
<p> Option -t uploads FILEs to the already created issue on MantisBT site. The issue ID is retrieved from directory specified by -d DIR. If problem data in DIR was never reported to MantisBT, upload will fail. </p>
<p> Option -tID uploads FILEs to the issue with specified ID on MantisBT site. -d DIR is ignored. </p>
<p> Option -r sets the last url from reporter_to element which is prefixed with TRACKER_NAME to URL field. This option is applied only when a new issue is to be filed. The default value is <i>ABRT Server</i>&quot;</p>
<h3>Configuration file</h3>
<p> If not specified, CONFFILE defaults to /etc/libreport/plugins/mantisbt.conf. Configuration file lines should have <i>PARAM = VALUE</i> format. The parameters are: </p>
<p> <i>Login</i></p>
<dl>
<dt>
<dd> Login to MantisBT account.</dl>
<p> <i>Password</i></p>
<dl>
<dt>
<dd> Password to MantisBT account.</dl>
<p> <i>MantisbtURL</i></p>
<dl>
<dt>
<dd> MantisBT HTTP(S) address. (default: m[blue]<code><a rel="nofollow" href="http://localhost/mantisbt">http://localhost/mantisbt</a></code>m[])</dl>
<p> <i>SSLVerify</i></p>
<dl>
<dt>
<dd> Use yes/true/on/1 to verify server&#8217;s SSL certificate. (default: no)</dl>
<p> <i>Project</i></p>
<dl>
<dt>
<dd> Project issue field value. Useful if you needed different project than specified in /etc/os-release</dl>
<p> <i>ProjectVersion</i></p>
<dl>
<dt>
<dd> Version issue field value. Useful if you needed different project version than specified in /etc/os-release</dl>
<p> <i>CreatePrivate</i></p>
<dl>
<dt>
<dd> Create private MantisBT issue. (default: no)</dl>
<p> Parameters can be overridden via $Mantisbt_PARAM environment variables.</p>
<h3>Formatting configuration files</h3>
<p> Lines starting with # are ignored. </p>
<p> Lines can be continued on the next line using trailing backslash. </p>
<p> Format: </p>
<p> &quot;%summary</p>
<dl>
<dt>
<dd> summary format&quot;</dl>
<p> &quot;section</p>
<dl>
<dt>
<dd> element1[,element2]&#8230;&quot; The literal text line to be added to MantisBT Description or Additional information. Can be empty. (Empty lines are NOT ignored!) </p>
<dl>
<dt>
<dd>
<pre><code>
Summary format is a line of text, where % element % is replaced by text element's content, and [[...%element%...]] block is used only if % element % exists.[[...]] blocks can nest.
</code></pre>
</dl>
<dl>
<dt>
<dd>
<pre>
Sections can be:
- %summary: issue Summary format string.
- %attach: a list of elements to attach.
- %Additional info: issue Additional Information content.
- text, double colon (::) and the list of comma-separated elements.
</pre>
</dl>
<dl>
<dt>
<dd>
<pre>
Description and Additional information MantisBT's fields:
All text, double colons (::) and lists of comma-separated elements which
are placed above the section '%Additional info::' in the configuration file are
stored in the 'Description' field in MantisBT. All text etc. which are placed
under the '%Additional info::' are stored in the 'Additional information' field.
</pre>
</dl>
<dl>
<dt>
<dd>
<pre>
For example:
|:: comment               |  (Description)
|                         |  (Description)
|Package:: package        |  (Description)
|                         |  (Description)
|%Additional_info::       |
|%reporter%               |  (Additional info)
|User:: user_name,uid     |  (Additional info)
|                         |  (Additional info)
|Directories:: root,cwd   |  (Additional info)
</pre>
</dl>
<dl>
<dt>
<dd>
<pre>
Elements can be:
- problem directory element names, which get formatted as
  &lt;element_name&gt;: &lt;contents&gt;
  or
  &lt;element_name&gt;:
  :&lt;contents&gt;
  :&lt;contents&gt;
  :&lt;contents&gt;
- problem directory element names prefixed by &quot;%bare_&quot;,
  which is formatted as-is, without &quot;&lt;element_name&gt;:&quot; and colons
- %oneline, %multiline, %text wildcards, which select all corresponding
  elements for output or attachment
- %binary wildcard, valid only for %attach section, instructs to attach
  binary elements
- problem directory element names prefixed by &quot;-&quot;,
  which excludes given element from all wildcards
</pre>
</dl>
<dl>
<dt>
<dd>
<pre>
Nonexistent elements are silently ignored.
If none of elements exists, the section will not be created.
</pre>
</dl>
</dl>
<h3>Integration with ABRT events</h3>
<p> <i>reporter-mantisbt</i> can be used as an ABRT reporter. Example fragment for /etc/libreport/report_event.conf: </p>
<dl>
<dt>
<dd>
<pre>
# Report Python crashes
EVENT=report_CentOSBugTracker analyzer=Python
      reporter-mantisbt -d . -c /etc/libreport/plugins/mantisbt.conf
</pre>
</dl>
<h2>OPTIONS</h2>
<p> -d DIR</p>
<dl>
<dt>
<dd> Path to problem directory.</dl>
<p> -c CONFFILE</p>
<dl>
<dt>
<dd> Path to configuration file.</dl>
<p> -f</p>
<dl>
<dt>
<dd> Force reporting even if this problem is already reported.</dl>
<p> -F CONF_FORMAT_FILE</p>
<dl>
<dt>
<dd> Formatting file for new issues. Default: /etc/libreport/plugins/mantisbt_format.conf</dl>
<p> -A CONF_FORMAT_FILE</p>
<dl>
<dt>
<dd> Formatting file for duplicates. Default: /etc/libreport/plugins/mantisbt_formatdup.conf</dl>
<p> -t[ID]</p>
<dl>
<dt>
<dd> Upload FILEs to the already created issue on MantisBT site.</dl>
<p> -h, &#8211;duphash DUPHASH</p>
<dl>
<dt>
<dd> Search in MantisBT by abrt&#8217;s DUPHASH and print ISSUE_ID.</dl>
<p> -r TRACKER_NAME</p>
<dl>
<dt>
<dd> Set the last url from reporter_to element which is prefixed with TRACKER_NAME to URL field in MantisBT.</dl>
<h2>ENVIRONMENT VARIABLES</h2>
<p> Environment variables take precedence over values provided in the configuration file. </p>
<p> <i>Mantisbt_Login</i></p>
<dl>
<dt>
<dd> Login to MantisBT account.</dl>
<p> <i>Mantisbt_Password</i></p>
<dl>
<dt>
<dd> Password to MantisBT account.</dl>
<p> <i>Mantisbt_MantisbtURL</i></p>
<dl>
<dt>
<dd> MantisBT HTTP(S) address. (default: m[blue]<code><a rel="nofollow" href="http://localhost/mantisbt">http://localhost/mantisbt</a></code>m[])</dl>
<p> <i>Mantisbt_SSLVerify</i></p>
<dl>
<dt>
<dd> Use yes/true/on/1 to verify server&#8217;s SSL certificate. (default: no)</dl>
<p> <i>Mantisbt_Project</i></p>
<dl>
<dt>
<dd> Project issue field value. Useful if you needed different project than specified in /etc/os-release</dl>
<p> <i>Mantisbt_ProjectVersion</i></p>
<dl>
<dt>
<dd> Version issue field value. Useful if you needed different project version than specified in /etc/os-release</dl>
<p> <i>Mantisbt_CreatePrivate</i></p>
<dl>
<dt>
<dd> Create private MantisBT issue. (default: no)</dl>
<h2>FILES</h2>
<p> /usr/share/libreport/conf.d/plugins/mantisbt.conf</p>
<dl>
<dt>
<dd> Readonly default configuration files.</dl>
<p> /etc/libreport/plugins/mantisbt.conf</p>
<dl>
<dt>
<dd> Configuration file.</dl>
<p> /etc/libreport/plugins/mantisbt_format.conf</p>
<dl>
<dt>
<dd> Configure formating for reporting.</dl>
<p> /etc/libreport/plugins/mantisbt_formatdup.conf</p>
<dl>
<dt>
<dd> Configure formating for reporting duplicates.</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/5-report_event-conf/">report_event.conf</a>(5), <a href="/docs/linux/man/5-mantisbt_format-conf/">mantisbt_format.conf</a>(5), <a href="/docs/linux/man/5-mantisbt_formatdup-conf/">mantisbt_formatdup.conf</a>(5)</p>
<h2>AUTHORS</h2>
<dl>
<dt>
<dd> &bull; ABRT team</dl>
<h2>Index</h2>
