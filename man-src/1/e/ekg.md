---

title: "ekg(1)"
name: "ekg"
section: "1"
letter: "e"
url: "/docs/linux/man/1-ekg/"
description: "ekg – A Gadu-Gadu compatible client."
---

<p> ekg &#8211; A Gadu-Gadu compatible client.</p>
<h2>SYNOPSIS</h2>
<p> <code>ekg [</code> <code>options</code> <code>]</code> <code>[</code> <code>commands</code> <code>]</code> </p>
<h2>DESCRIPTION</h2>
<p> <code>ekg</code> is an experimental Gadu-Gadu client. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h&nbsp;<wbr>[&#8211;help]</code></dt>
<dd> Shows command line options.</dd>
<dt><code>-u username&nbsp;<wbr>[&#8211;user username]</code></dt>
<dd> Starts ekg with other By default config files are stored in ~/.gg/ (if there is a non-empty $CONFIG_DIR environment variable, ~/$CONFIG_DIR/gg/ is used instead); this option gives ability to create subdirectories structure with other setups.</dd>
<dt><code>-t theme&nbsp;<wbr>[&#8211;theme theme]</code></dt>
<dd> Loads theme from the specified file.</dd>
<dt><code>-c file&nbsp;<wbr>[&#8211;control-pipe file]</code></dt>
<dd> Creates a named pipe that can be used to control the client.</dd>
<dt><code>-n&nbsp;<wbr>[&#8211;no-auto]</code></dt>
<dd> Don&#8217;t connect automagically. After starting program won&#8217;t automatically connect to the gg servers.</dd>
<dt><code>-N&nbsp;<wbr>[&#8211;no-global-config]</code></dt>
<dd> Don&#8217;t load global configuration file (i.e. /etc/ekg.conf) after user&#8217;s one.</dd>
<dt><code>-a&nbsp;<wbr>[&#8211;away[=description]]</code></dt>
<dd> After connecting sets the status to &quot;away&quot;.</dd>
<dt><code>-b&nbsp;<wbr>[&#8211;back[=description]]</code></dt>
<dd> After connecting sets the status to &quot;back&quot;.</dd>
<dt><code>-i&nbsp;<wbr>[&#8211;invisible[=description]]</code></dt>
<dd> After connecting sets the status to &quot;invisible&quot;.</dd>
<dt><code>-p&nbsp;<wbr>[&#8211;private]</code></dt>
<dd> After connecting change to &quot;private mode&quot;.</dd>
<dt><code>-v&nbsp;<wbr>[&#8211;version]</code></dt>
<dd> Prints the client and libgadu library version.</dd>
<dt><code>-f name&nbsp;<wbr>[&#8211;frontend name]</code></dt>
<dd> Selects given user interface. </dd>
</dl>
