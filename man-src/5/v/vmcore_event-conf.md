---
title: "vmcore_event-conf(5)"
name: "vmcore_event-conf"
section: "5"
letter: "v"
url: "/docs/linux/man/5-vmcore_event-conf/"
description: "report_event.conf – configuration file for libreport."
---

<p>report_event.conf &#8211; configuration file for libreport.</p>
<h2>Description</h2>
<p>This configuration file specifies which programs should be run when the specified event occurs in problem directory lifetime. </p>
<p> It consists of directives and rules. </p>
<p> Directives start with a reserved word. Currently, there is only one directive, &quot;include&quot;. </p>
<p> include <i>FILE</i></p>
<dl>
<dd>This directive causes files which match FILE to be read and parsed as if they are inserted textually where this directive occurs. FILE can use shell pattern metacharacters (*,?,etc) to specify multiple files. Relative paths are interpreted relative to current file.</dl>
<p> Rule starts with a line with non-space leading character. All subsequent lines which start with space or tab form one rule. Note that separating newline is retained. </p>
<p> Rules may be commented out with #. One # is sufficient to comment out even a multi-line rule (no need to comment out every line). </p>
<p> Rules specify which programs to run on the problem directory. Each rule may have conditions to be checked before the program is run. </p>
<p> Conditions have form VAR=VAL or VAL~=REGEX, where VAR is either word &quot;EVENT&quot; or a name of problem directory element to be checked (for example, &quot;executable&quot;, &quot;package&quot;, hostname&quot; etc). </p>
<p> If all conditions match, the remaining part of the rule (the &quot;program&quot; part) is run in the shell. All shell language constructs are valid. All stdout and stderr output is captured and passed to ABRT and possibly to ABRT&#8217;s frontends and shown to the user. </p>
<p> If the program terminates with nonzero exit code, the event processing is considered unsuccessful and is stopped. Last captured output line, if any, is considered to be the error message indicating the reason of the failure, and may be used by abrt as such. </p>
<p> If the program terminates successfully, next rule is read and processed. This process is repeated until the end of this file.</p>
<h3>Event XML configuration</h3>
<p>These configuration files provides event meta data. </p>
<p> Each file has XML formatting with the following DTD: </p>
<dl>
<dd>
<pre>&lt;!ELEMENT event (name+,description+,requires-items?,exclude-items-by-default?,exclude-items-always?,exclude-binary-items?,include-items-by-default?,minimal-rating?,gui-review-elements?,options?)&gt;
&lt;!ELEMENT name (#PCDATA)&gt;
&lt;!ATTLIST name xml:lang CDATA #IMPLIED&gt;
&lt;!ELEMENT description (#PCDATA)&gt;
&lt;!ATTLIST description xml:lang CDATA #IMPLIED&gt;
&lt;!ELEMENT requires-items (#PCDATA)&gt;
&lt;!ELEMENT exclude-items-by-default (#PCDATA)&gt;
&lt;!ELEMENT include-items-by-default (#PCDATA)&gt;
&lt;!ELEMENT exclude-items-always (#PCDATA)&gt;
&lt;!ELEMENT exclude-binary-items (&quot;yes&quot;|&quot;no&quot;)&gt;
&lt;!ELEMENT minimal-rating (&quot;0&quot;|&quot;1&quot;|&quot;2&quot;|&quot;3&quot;|&quot;4&quot;)&gt;
&lt;!ELEMENT gui-review-elements (&quot;yes&quot;|&quot;no&quot;)&gt;
&lt;!ELEMENT support-restricted-access (&quot;yes&quot;|&quot;no&quot;)&gt;
&lt;!ATTLIST support-restricted-access optionname CDATA #IMPLIED&gt;
&lt;!ELEMENT options (option*,advanced-options)&gt;
&lt;!ELEMENT advanced-options (option)*&gt;
&lt;!ELEMENT option (label+,description+,note-html+,allow-empty?,default-value?)&gt;
&lt;!ATTLIST option type (text|bool|password|number|hint-html) #REQUIRED
 name CDATA #REQUIRED&gt;
&lt;!ELEMENT label (#PCDATA)&gt;
&lt;!ATTLIST label xml:lang CDATA #IMPLIED&gt;
&lt;!ELEMENT note-html (#PCDATA)&gt;
&lt;!ATTLIST note-html xml:lang CDATA #IMPLIED&gt;
&lt;!ELEMENT allow-empty (&quot;yes&quot;|&quot;no&quot;)&gt;
&lt;!ELEMENT default-value (#PCDATA)&gt;</pre>
</dl>
<p> name</p>
<dl>
<dd>User visible name of event</dl>
<p> description</p>
<dl>
<dd>User visible description</dl>
<p> exclude-items-by-default</p>
<dl>
<dd>Comma separated names of excluded problem elements. User can include any of these elements if he wishes it.</dl>
<p> include-items-by-default</p>
<dl>
<dd>Comma separated names of included problem elements. User can exclude any of these elements if he wishes it.</dl>
<p> exclude-items-always</p>
<dl>
<dd>Comma separated names of included problem elements. User cannot include any of these elements.</dl>
<p> exclude-binary-items</p>
<dl>
<dd>If &quot;yes&quot; then all binary problem elements are excluded. User can include them if he wishes it.</dl>
<p> minimal-rating</p>
<dl>
<dd>Minimal backtrace rating required for executing the event. Backtrace rating is a measure of backtrace usability and understandability. With an increasing number of unresolved frames the backtrace rating gets lower values.</dl>
<p> gui-review-elements</p>
<dl>
<dd>If &quot;yes&quot;, user must explicitly approve that all included problem elements can be published. If &quot;no&quot;, the event is executed automatically. If not provided, &quot;yes&quot; is expected.</dl>
<p> support-restricted-access</p>
<dl>
<dd>If &quot;yes&quot;, the UI tools will offer the users to enter the new report with restricted access. If &quot;no&quot;, the UI tools will never offer the users to enter the report with restricted access. &quot;no&quot; is the default value. The element should have one argument named <i>optionname</i> which defines name of an option holding configuration of the restricted access feature. The option must of <i>bool</i> type.</dl>
<p> advanced-options</p>
<dl>
<dd>List of options which are hidden in the default view.</dl>
<p> label</p>
<dl>
<dd>Event option label</dl>
<p> note-html</p>
<dl>
<dd>Event option HTML formatted description</dl>
<p> allow-empty</p>
<dl>
<dd>Determines if user can leave the option empty</dl>
<p> default-value</p>
<dl>
<dd>A value which is used by default</dl>
<p> option:name</p>
<dl>
<dd>Name of exported environment variable name. libreport tools communicate through Environment Variables.</dl>
<h2>Examples</h2>
<dl>
<dd>
<pre>EVENT=post-create analyzer=Python abrt-action-analyze-python
EVENT=post-create
 getent passwd &quot;`cat uid`&quot; | cut -d: -f1 &gt;username</pre>
</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-abrtd/">abrtd</a>(8)</p>
<h2>Author</h2>
<p>Manual page written by Denys Vlasenko &lt;m[blue]<code>dvlasenk [at] redhat.com</code>m[]<font SIZE="-2">[1]</font>&gt;.</p>
<h2>Notes</h2>
<dl>
<dt> 1.</p>
<dd>dvlasenk [at] redhat.com</p>
<dl>
<dd>mailto:dvlasenk [at] redhat.com</dl>
