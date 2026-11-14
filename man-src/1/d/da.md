---
title: "da(1)"
name: "da"
section: "1"
letter: "d"
url: "/docs/linux/man/1-da/"
description: "da – setup development environment and create basic projects in various languages"
---

<h2>NAME</h2>
<p> da &#8211; setup development environment and create basic projects in various languages </p>
<h2>SYNOPSIS</h2>
<p> <code>da [&#8211;debug] [&#8211;no-cache] [ ASSISTANT_TYPE ] [ OPTIONS ] [[ SUBASSISTANT ] [OPTIONS] &#8230;] </p>
<p> da [&#8211;debug] [&#8211;no-cache] [ ACTION ] [ OPTIONS ] </p>
<p> </code></p>
<h2>DESCRIPTION</h2>
<p> <code>da</code> is the main command of DevAssistant. It is responsible for dispatching commandline calls to assistants or actions. It accepts some optional flags: </p>
<dl>
<dt><code>&#8211;debug</code></p>
<dd> makes DevAssistant log lots of debugging information</p>
<dt><code>&#8211;no-cache</code></p>
<dd> makes DevAssistant read all individual assistants and completely ignore cache </p>
</dl>
<h2>DESCRIPTION &#8211; ASSISTANT_TYPE</h2>
<p> DevAssistant can help you with various tasks during development. The tasks are carried out by so called &quot;assistants&quot; &#8211; there are four types of assistants: </p>
<p> <code>create</code> &#8211; create new projects, install dependencies and setup environment<br />
 <code>modify</code> &#8211; modify previously created projects (e.g. import them to Eclipse)<br />
 <code>prepare</code> &#8211; prepare development environment for an upstream project<br />
 <code>task</code> &#8211; carry out a custom task not related to a specific project </p>
<p> You can shorten &quot;create&quot; to &quot;crt&quot;, &quot;modify&quot; to &quot;mod&quot; and &quot;prepare&quot; to &quot;prep&quot;. </p>
<p> Each assistant type can have many associated assistants (e.g. python, ruby) and each assistant can have many associated subassistants (e.g. django, flask). You can display these (and also other options) by running e.g. <code>da crt -h</code> and <code>da crt python -h</code>. Once you select the desired assistant (and its subassistants), just run it, e.g. <code>da crt python django -n newproject</code>. </p>
<p> The list of assistants and their functionality may vary depending on your installation &#8211; just run help to see currently available assistants. </p>
<h2>DESCRIPTION &#8211; ACTION</h2>
<p> DevAssistant is designed to also provide custom functionality through so-called actions. Currently, these contain: </p>
<p> <code>help</code> &#8211; display verbose help.<br />
 <code>version</code> &#8211; display devassistant version. </p>
<p> Again, to show options, just use <code>-h</code> with the action, e.g. <code>da version -h</code>. </p>
<h2>COMMON OPTIONS</h2>
<p> There are some commonly used options shared among many assistants. Their usual meaning is explained below:</p>
<dl>
<dt><code>-h &#8211;help</code></p>
<dd> print help for selected assistant.</p>
<dt><code>-n &#8211;name</code></p>
<dd> name of the project (relative or absolute path).</p>
<dt><code>-e &#8211;eclipse</code></p>
<dd> import project into <i>eclipse</i> environment. Uses ~/workspace workspace by default, can be overriden by specifying another path.</p>
<dt><code>-g &#8211;github &lt;username&gt;</code></p>
<dd> create a GitHub repo and push the initial sources there. Uses current system username as GitHub username, unless specified otherwise. The GitHub projectname is taken from the <code>name</code> parameter.</p>
<dt><code>-b &#8211;build</code></p>
<dd> generate a SPEC file, SRPM and mock-build RPM.</p>
<dt><code>-v &#8211;vim</code></p>
<dd> install vim settings specific for this language (backs up your original vim settings) </p>
</dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>DEVASSISTANT_PATH</code></p>
<dd> A colon-separated list of directories in which to search for assistants. Searched in before the standard paths. If multiple assistants with the same name are found only the first of them will be used. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-da-gui/">da-gui</a></code>(1) </p>
<h2>Index</h2>
