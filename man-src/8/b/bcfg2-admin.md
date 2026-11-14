---
title: "bcfg2-admin(8)"
name: "bcfg2-admin"
section: "8"
letter: "b"
url: "/docs/linux/man/8-bcfg2-admin/"
description: "bcfg2-admin – Perform repository administration tasks"
---

<p>bcfg2-admin &#8211; Perform repository administration tasks</p>
<h2>Synopsis</h2>
<p><code>bcfg2-admin</code> <i>[-C config-file]</i> <i>&lt;mode&gt;</i> <i>&lt;mode args&gt;</i> <i>&lt;mode options&gt;</i></p>
<h2>Description</h2>
<p><code>bcfg2-admin</code> Perform bcfg2 repository administration</p>
<h2>Options</h2>
<p><code>-C &lt;config-file&gt;</code></p>
<dl>
<dd>Specify the location of the configuration file (if it is not in /etc/bcfg2.conf)</dl>
<h2>Modes</h2>
<p><code>init</code></p>
<dl>
<dd>Initialize a new repository (interactive)</dl>
<p> <code>client &lt;action&gt; &lt;client&gt; [attribute=value]</code></p>
<dl>
<dd>Add or remove clients from metadata</dl>
<p> <code>query [g=group] [p=profile] [-f output-file] [-n] [-c]</code></p>
<dl>
<dd>Search for clients based on group or profile</dl>
<p> <code>compare &lt;old&gt; &lt;new&gt;</code></p>
<dl>
<dd>Compare two client configurations. Can be used to verify consistent behavior between releases</dl>
<p> <code>minestruct &lt;client&gt; [-f xml-file] [-g groups]</code></p>
<dl>
<dd>Build structure entries based on client statistics extra entries</dl>
<p> <code>pull &lt;client&gt; &lt;entry-type&gt; &lt;entry-name&gt;</code></p>
<dl>
<dd>Install configuration information into repo based on client bad entries</dl>
<p> <code>tidy</code></p>
<dl>
<dd>Remove unused files from repository</dl>
<p> <code>viz [-h] [-b] [-k] [-o png-file] [-r]</code></p>
<dl>
<dd>Create a graphviz diagram of client, group and bundle information</dl>
<h2>Client Options</h2>
<p><code>mode</code></p>
<dl>
<dd>Add a client &#8216;add&#8217; or delete a client &#8216;del&#8217;</dl>
<p> <code>client</code></p>
<dl>
<dd>Specify the client&#8217;s name</dl>
<p> <code>attribute=value</code></p>
<dl>
<dd>Set attribute values when adding a new client</dl>
<h2>Query Options</h2>
<p><code>g=group</code></p>
<dl>
<dd>Specify a group to search within</dl>
<p> <code>p=profile</code></p>
<dl>
<dd>Specify a profile to search within</dl>
<p> <code>-f &lt;output-file&gt;</code></p>
<dl>
<dd>Write the results of the query to a file</dl>
<p> <code>-n</code></p>
<dl>
<dd>Print the results, one on each line</dl>
<p> <code>-c</code></p>
<dl>
<dd>Print the results, separated by commas</dl>
<h2>Compare Options</h2>
<p><code>old</code></p>
<dl>
<dd>Specify the location of the old configuration file</dl>
<p> <code>new</code></p>
<dl>
<dd>Specify the location of the new configuration file</dl>
<h2>Minestruct Options</h2>
<p><code>client</code></p>
<dl>
<dd>Client whose metadata is to be searched for extra entries</dl>
<p> <code>-g &lt;groups&gt;</code></p>
<dl>
<dd>Hierarchy of groups in which to place the extra entries in</dl>
<p> <code>-f &lt;xml-output-file&gt;</code></p>
<dl>
<dd>Specify the xml file in which to write the extra entries</dl>
<h2>Pull Options</h2>
<p><code>client</code></p>
<dl>
<dd>Specify the name of the client to search for</dl>
<p> <code>entry-type</code></p>
<dl>
<dd>Specify the type of the entry to pull</dl>
<p> <code>entry-name</code></p>
<dl>
<dd>Specify the name of the entry to pull</dl>
<h2>Viz Options</h2>
<p><code>-h</code></p>
<dl>
<dd>Include hosts in diagram</dl>
<p> <code>-b</code></p>
<dl>
<dd>Include bundles in diagram</dl>
<p> <code>-o &lt;output file&gt;</code></p>
<dl>
<dd>Write to outfile file instead of stdout</dl>
<p> <code>-r</code></p>
<dl>
<dd>Produce raw graphviz output</dl>
<p> <code>-k</code></p>
<dl>
<dd>Add a shape/color key</dl>
