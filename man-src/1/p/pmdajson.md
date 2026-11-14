---
title: "pmdajson(1)"
name: "pmdajson"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pmdajson/"
description: "pmdajson – JSON PMDA"
---

<h2>NAME</h2>
<p> <code>pmdajson</code> &#8211; JSON PMDA</p>
<h2>DESCRIPTION</h2>
<p> <code>pmdajson</code> is a Performance Metrics Domain Agent (PMDA) which exports metrics from arbitrary sources generating Javascript Object Notation (JSON) syntax, describing metric metadata and values. </p>
<p> Further details on the JSON format can be found at <a rel="nofollow" href="http://www.json.org">http://www.json.org</a></p>
<h2>JSON DATA SOURCES</h2>
<p> <code>pmdajson</code> searches the directories listed in the &quot;directory_list&quot; and &quot;trusted_directory_list&quot; config file options, looking for files called &quot;metadata.json&quot;. These JSON metadata files describe the names, types, etc. of their associated JSON data. For example, let&#8217;s assume the following simple JSON data file: </p>
<pre>
  {
    &quot;string_value&quot;: &quot;testing, 1, 2, 3&quot;,
    &quot;read_count&quot;: 0
  }
</pre>
<p> The associated metadata file would look like the following: </p>
<pre><code>
{
    "metrics" : [
        {
            "name" : "string_value",
            "pointer" : "/string_value",
            "type" : "string",
        },
        {
            "name" : "read_count",
            "pointer" : "/read_count",
            "type" : "integer",
            "description" : "Times values read"
        }
    ]
}
</code></pre>
<p> For more details on the JSON metadata format, see the README file included with <code>pmdajson</code>.</p>
<h2>SECURITY MODEL</h2>
<p> JSON sources that come from &quot;directory_list&quot; config file option aren&#8217;t &quot;trusted&quot;, and any command that needs to be run to get JSON data is run as user &quot;nobody&quot;. </p>
<p> JSON sources that come from &quot;trusted_directory_list&quot; config file option are trusted, and any command that needs to be run to get JSON data is run as user &quot;root&quot;. </p>
<p> For more details on security, see the README file included with <code>pmdajson</code>.</p>
<h2>INSTALLATION</h2>
<p> Install the json PMDA by using the Install script as root: </p>
<p>#&nbsp;<wbr>cd&nbsp;<wbr>$PCP_PMDAS_DIR/json </p>
<p>#&nbsp;<wbr>./Install </p>
<p> To uninstall, do the following as root: </p>
<p>#&nbsp;<wbr>cd&nbsp;<wbr>$PCP_PMDAS_DIR/json </p>
<p>#&nbsp;<wbr>./Remove </p>
<p> <code>pmdajson</code> is launched by <i><a href="/docs/linux/man/1-pmcd/">pmcd</a></i>(1) and should never be executed directly. The Install and Remove scripts notify <i><a href="/docs/linux/man/1-pmcd/">pmcd</a></i>(1) when the agent is installed or removed.</p>
<h2>FILES</h2>
<dl>
<dt><code>$PCP_PMDAS_DIR/json/Install</code></p>
<dd> installation script for the <code>pmdajson</code> agent</p>
<dt><code>$PCP_PMDAS_DIR/json/Remove</code></p>
<dd> undo installation script for the <code>pmdajson</code> agent</p>
<dt><code>$PCP_PMDAS_DIR/json/config.json</code></p>
<dd> configuration file for the <code>pmdajson</code> agent</p>
<dt><code>$PCP_LOG_DIR/pmcd/json.log</code></p>
<dd> default log file for error messages from <code>pmdajson</code></dl>
<h2>PCP ENVIRONMENT</h2>
<p> Environment variables with the prefix <code>PCP_</code> are used to parameterize the file and directory names used by <code>PCP</code>. On each installation, the file <code>/etc/pcp.conf</code> contains the local values for these variables. The <code>$PCP_CONF</code> variable may be used to specify an alternative configuration file, as described in <i><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></i>(5).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1), <code><a href="/docs/linux/man/1-pminfo/">pminfo</a></code>(1) and <code><a href="/docs/linux/man/1-pmprobe/">pmprobe</a></code>(1). </p>
<h2>Index</h2>
