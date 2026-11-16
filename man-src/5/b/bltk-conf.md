---
title: "bltk-conf(5)"
name: "bltk-conf"
section: "5"
letter: "b"
url: "/docs/linux/man/5-bltk-conf/"
description: "bltk.conf – config file for bltk"
---

<p>bltk.conf &#8211; config file for bltk</p>
<h2>Description</h2>
<p>bltk.conf may be used to control particular features of bltk. By default, bltk looks for the file in /etc direcotry.</p>
<h2>Format</h2>
<p>The format of bltk.conf is very simple. Each line is either a comment or a directive. Comment lines start with a # and are ignored. A directive line has the format: </p>
<p> option=value </p>
<p> It is important to note that it is an error to put any space between the option, = and value. </p>
<p> Each setting has a compiled in default which may be modified in the configuration file.</p>
<h2>.Boolean Options</h2>
<p>Below is a list of boolean options. The value for a boolean option may be set to YES or NO.</p>
<dl>
<dt><code>CHK_INSTALLED</code></dt>
<dd>If set to YES, existance of .installed files is checked for.</dd>
<dt><code>WL_DEVELOPER_ENABLED</code></dt>
<dd>Controls whether developer workload is enabled.</dd>
<dt><code>WL_DEVELOPER_EXTERN</code></dt>
<dd>Controls whether external sources are used to build workload application.</dd>
<dt><code>WL_GAME_ENABLED</code></dt>
<dd>Controls whether game workload is enabled.</dd>
<dt><code>WL_GAME_EXTERN</code></dt>
<dd>Controls whether external sources are used to build workload application.</dd>
<dt><code>WL_OFFICE_ENABLED</code></dt>
<dd>Controls whether office workload is enabled.</dd>
<dt><code>WL_OFFICE_EXTERN</code></dt>
<dd>Controls whether external sources are used to build workload application.</dd>
<dt><code>WL_PLAYER_ENABLED</code></dt>
<dd>Controls whether player workload is enabled</dd>
<dt><code>WL_PLAYER_EXTERN</code></dt>
<dd>Controls whether external sources are used to build workload application.</dd>
<dt><code>WL_READER_ENABLED</code></dt>
<dd>Controls whether reader workload is enabled.</dd>
<dt><code>WL_READER_EXTERN</code></dt>
<dd>Controls whether external sources are used to build workload application.</dd></dl>
<h2>.String Options</h2>
<p><code>BLTK_HOME</code> This option specifies the location of BLTK&#8217;s home directory. This directory is used as starting directory for saving results and temporary files.</p>
<dl>
<dt><code>SOFFICE_PROG</code></dt>
<dd>This option specifies an application to be started when office workload is used.</dd>
<dt><code>WL_OFFICE_WORKING_DIR</code></dt>
<dd>The option specifies working directory for office workload.</dd>
<dt><code>BLTK_PLAYER_PROG</code></dt>
<dd>The option replaces default aplication to be used for playing audio/video</dd>
<dt><code>BLTK_PLAYER_FILE</code></dt>
<dd>The option replaces default source to be played.</dd>
<dt><code>BLTK_READER_PROG</code></dt>
<dd>The option replaces default aplication to be used for reading a document.</dd>
<dt><code>BLTK_READER_FILE</code></dt>
<dd>The option replaces default document to be read.</dd></dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-bltk/">bltk</a></code>(1)</p>
<h2>Author</h2>
<p>jskala [at] redhat.com</p>
