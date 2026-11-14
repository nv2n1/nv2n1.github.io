---
title: "bedup(8)"
name: "bedup"
section: "8"
letter: "b"
url: "/docs/linux/man/8-bedup/"
description: "bedup – program for deduplication program with additional knowledge of burp"
---

<p>bedup &#8211; program for deduplication program with additional knowledge of burp</p>
<h2>Synopsis</h2>
<p><code>bedup</code> [<i>options</i>]<br />
 A file deduplication program with additional knowledge of burp storage directories. This program comes with the burp backup and restore package. </p>
<h2>Options</h2>
<dl>
<dt><code>-c</code> <code>path</code></p>
<dd>Path to config file (default: /etc/burp/burp.conf).</p>
<dt><code>-g</code> <code>&lt;list of group names&gt;</code></p>
<dd>Only run on the directories of clients that are in one of the groups specified. The list is comma-separated. To put a client in a group, use the &#8216;dedup_group&#8217; option in the client configuration file on the server.</p>
<dt><code>-h|-?</code></p>
<dd>Print help text and exit.</p>
<dt><code>-d </code></p>
<dd>Delete any duplicate files found. (non-burp mode only, use with caution!)</p>
<dt><code>-l </code></p>
<dd>Hard link any duplicate files found.</p>
<dt><code>-m </code> <code>&lt;number&gt;</code></p>
<dd>Maximum number of hard links to a single file. (non-burp mode only &#8211; in burp mode, use the max_hardlinks option in the configuration file) The default is 10000. On ext3, the maximum number of links possible is 32000, but space is needed for the normal operation of burp.</p>
<dt><code>-n</code> <code>&lt;list of directories&gt;</code></p>
<dd>Non-burp mode. Deduplicate any (set of) directories.</p>
<dt><code>-v</code></p>
<dd>Print duplicate paths. Useful if you want to double check the files that would be hard linked or deleted before running with one of those options turned on.</p>
<dt><code>-V</code></p>
<dd>Print version and exit.</p>
<dt>By default, bedup will read /etc/burp/burp.conf and deduplicate client storage directories using special knowledge of the structure.</p>
<dd>
<dt>With &#8216;-n&#8217;, this knowledge is turned off and you have to specify the directories to deduplicate on the command line. Running with &#8216;-n&#8217; is therefore dangerous if you are deduplicating burp storage directories.</p>
<dd></dl>
<h2>Bugs</h2>
<p>If you find bugs, please report them to the email list. See the website &lt;<a rel="nofollow" href="http://burp.grke.net/">http://burp.grke.net/</a>&gt; for details. </p>
<h2>Author</h2>
<p>The main author of Burp is Graham Keeling.</p>
<h2>Copyright</h2>
<p>See the LICENCE file included with the source distribution.</p>
