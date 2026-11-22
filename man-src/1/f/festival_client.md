---

title: "festival_client(1)"
name: "festival_client"
section: "1"
letter: "f"
url: "/docs/linux/man/1-festival_client/"
description: "festival_client – client access to festiva; text-to-speech server mode"
---

<p> festival_client &#8211; client access to festiva; text-to-speech server mode</p>
<h2>SYNOPSIS</h2>
<p> <code>festival_client</code> <i>[options]</i> <i>[file0]</i> <i>[file1]</i> <i>&#8230;</i> </p>
<h2>DESCRIPTION</h2>
<p> Allows sending commands and/or test to a festival test-to-speech server. Festival may be started in server mode using the option <code>&#8211;server</code> </p>
<p> festival-clinet allows waveforms ot be generated faster as not time is required for start up. See the festival manual for more details on recommended use. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;server </code><i>&lt;string&gt;</i></dt>
<dd> hostname (or IP number) of server</dd>
<dt><code>&#8211;port </code><i>&lt;int&gt;</i><code> {1314}</code></dt>
<dd> port number of server process (1314)</dd>
<dt><code>&#8211;output </code><i>&lt;string&gt;</i></dt>
<dd> file to save output waveform to</dd>
<dt><code>&#8211;otype </code><i>&lt;string&gt;</i><code> {riff}</code></dt>
<dd> output type for waveform</dd>
<dt><code>&#8211;passwd </code><i>&lt;string&gt;</i></dt>
<dd> server passwd in plain text (optional)</dd>
<dt><code>&#8211;prolog </code><i>&lt;string&gt;</i></dt>
<dd> filename containing commands to be sent to the server before standard commands (useful when using &#8211;ttw)</dd>
<dt><code>&#8211;async </code></dt>
<dd> Asynchronous mode, server may send back multiple waveforms per text file</dd>
<dt><code>&#8211;ttw </code></dt>
<dd> Text to waveform: take text from first arg or stdin get server to return waveform(s) stored in output or operated on by aucommand.</dd>
<dt><code>&#8211;withlisp </code></dt>
<dd> Output lisp replies from server.</dd>
<dt><code>&#8211;tts_mode </code><i>&lt;string&gt;</i></dt>
<dd> TTS mode for file (default is fundamental).</dd>
<dt><code>&#8211;aucommand </code><i>&lt;string&gt;</i></dt>
<dd> command to be applied to each waveform retruned from server. Use $FILE in string to refer to waveform file</dd></dl>
<h2>BUGS</h2>
<p> This still isn&#8217;t as general as it should be. It seems to require lots of special little options which suggests the general options aren&#8217;t right. </p>
<h2>AUTHOR</h2>
<p> Alan W Black and Paul Taylor<br/>
 (C) Centre for Speech Technology Research<br/>
 University of Edinburgh<br/>
 80 South Bridge<br/>
 Edinburgh EH1 1HN<br/>
 <a rel="nofollow" href="http://www.cstr.ed.ac.uk/projects/festival.html">http://www.cstr.ed.ac.uk/projects/festival.html</a> </p>
