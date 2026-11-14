---
title: "bltk(5)"
name: "bltk"
section: "5"
letter: "b"
url: "/docs/linux/man/5-bltk/"
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
<dt><code>CHK_INSTALLED</code></p>
<dd>If set to YES, existance of .installed files is checked for.</p>
<dt><code>WL_DEVELOPER_ENABLED</code></p>
<dd>Controls whether developer workload is enabled.</p>
<dt><code>WL_DEVELOPER_EXTERN</code></p>
<dd>Controls whether external sources are used to build workload application.</p>
<dt><code>WL_GAME_ENABLED</code></p>
<dd>Controls whether game workload is enabled.</p>
<dt><code>WL_GAME_EXTERN</code></p>
<dd>Controls whether external sources are used to build workload application.</p>
<dt><code>WL_OFFICE_ENABLED</code></p>
<dd>Controls whether office workload is enabled.</p>
<dt><code>WL_OFFICE_EXTERN</code></p>
<dd>Controls whether external sources are used to build workload application.</p>
<dt><code>WL_PLAYER_ENABLED</code></p>
<dd>Controls whether player workload is enabled</p>
<dt><code>WL_PLAYER_EXTERN</code></p>
<dd>Controls whether external sources are used to build workload application.</p>
<dt><code>WL_READER_ENABLED</code></p>
<dd>Controls whether reader workload is enabled.</p>
<dt><code>WL_READER_EXTERN</code></p>
<dd>Controls whether external sources are used to build workload application.</dl>
<h2>.String Options</h2>
<p><code>BLTK_HOME</code> This option specifies the location of BLTK&#8217;s home directory. This directory is used as starting directory for saving results and temporary files.</p>
<dl>
<dt><code>SOFFICE_PROG</code></p>
<dd>This option specifies an application to be started when office workload is used.</p>
<dt><code>WL_OFFICE_WORKING_DIR</code></p>
<dd>The option specifies working directory for office workload.</p>
<dt><code>BLTK_PLAYER_PROG</code></p>
<dd>The option replaces default aplication to be used for playing audio/video</p>
<dt><code>BLTK_PLAYER_FILE</code></p>
<dd>The option replaces default source to be played.</p>
<dt><code>BLTK_READER_PROG</code></p>
<dd>The option replaces default aplication to be used for reading a document.</p>
<dt><code>BLTK_READER_FILE</code></p>
<dd>The option replaces default document to be read.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-bltk/">bltk</a></code>(1)</p>
<h2>Author</h2>
<p>jskala [at] redhat.com</p>
