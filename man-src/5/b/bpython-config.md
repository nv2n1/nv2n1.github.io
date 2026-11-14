---
title: "bpython-config(5)"
name: "bpython-config"
section: "5"
letter: "b"
url: "/docs/linux/man/5-bpython-config/"
description: "bpython-config – user configuration file for bpython"
---

<p>bpython-config &#8211; user configuration file for bpython</p>
<h2>Synopsis</h2>
<p><code>$XDG_CONFIG_HOME/bpython/config</code></p>
<h2>Description</h2>
<p>The configuration file contains various options controlling the behaviour of <code>bpython</code>.</p>
<h2>General</h2>
<p>This refers to the <code>[general]</code> section in your <i>$XDG_CONFIG_HOME/bpython/config</i> file.</p>
<h3>auto_display_list</h3>
<p>Display the autocomplete list as you type (default: True). When this is off, you can hit tab to see the suggestions.</p>
<h3>autocomplete_mode</h3>
<p>There are three modes for autocomplete. simple, substring, and fuzzy. Simple matches methods with a common prefix, substring matches methods with a common subsequence, and fuzzy matches methods with common characters (default: simple). </p>
<p> New in version 0.12.</p>
<h3>syntax</h3>
<p>Syntax highlighting as you type (default: True).</p>
<h3>arg_spec</h3>
<p>Display the arg spec (list of arguments) for callables, when possible (default: True).</p>
<h3>hist_file</h3>
<p>History file (default: <code>~/.pythonhist</code>).</p>
<h3>paste_time</h3>
<p>The time between lines before pastemode is activated in seconds (default: 0.02).</p>
<h3>hist_length</h3>
<p>Number of lines to store in history (set to 0 to disable) (default: 100)</p>
<h3>tab_length</h3>
<p>Soft tab size (default 4, see pep-8)</p>
<h3>pastebin_url</h3>
<p>The pastebin url to post to (without a trailing slash). This pastebin has to be a pastebin which uses LodgeIt. Examples are: <i><a rel="nofollow" href="http://paste.pocoo.org/xmlrpc/">http://paste.pocoo.org/xmlrpc/</a></i> and <i><a rel="nofollow" href="http://bpaste.net/xmlrpc/">http://bpaste.net/xmlrpc/</a></i> (default: <i><a href="http://bpaste.net/xmlrpc/">http://bpaste.net/xmlrpc/</a></i>)</p>
<h3>pastebin_private</h3>
<p>If the pastebin supports a private option to make a random paste id, use it. Default: True). </p>
<p> New in version 0.12.</p>
<h3>pastebin_show_url</h3>
<p>The url under which the new paste can be reached. <code>$paste_id</code> will be replaced by the ID of the new paste. Examples are: <i><a rel="nofollow" href="http://bpaste.net/show/$paste_id/">http://bpaste.net/show/$paste_id/</a></i> and <i><a rel="nofollow" href="http://paste.pocoo.org/show/$paste_id/">http://paste.pocoo.org/show/$paste_id/</a></i> (default: <i><a href="http://bpaste.net/show/$paste_id/">http://bpaste.net/show/$paste_id/</a></i>)</p>
<h3>pastebin_helper</h3>
<p>The name of a helper executable that should perform pastebin upload on bpython&#8217;s behalf. If set, this overrides <i>pastebin_url</i>. It also overrides <i>pastebin_show_url</i>, as the helper is expected to return the full URL to the pastebin as the first word of its output. The data is supplied to the helper via STDIN. </p>
<p> An example helper program is <code>pastebinit</code>, available for most systems. The following helper program can be used to create <i>gists</i>: </p>
<pre>#!/usr/bin/env python
import sys
import urllib2
import json
def do_gist_json(s):
 &quot;&quot;&quot; Use json to post to github. &quot;&quot;&quot;
 gist_public = False
 gist_url = '<a rel="nofollow" href="https://api.github.com/gists'">https://api.github.com/gists'</a>
 data = {'description': None,
 'public': None,
 'files' : {
 'sample': { 'content': None }
 }}
 data['description'] = 'Gist from BPython'
 data['public'] = gist_public
 data['files']['sample']['content'] = s
 req = urllib2.Request(gist_url, json.dumps(data), {'Content-Type': 'application/json'})
 try:
 res = urllib2.urlopen(req)
 except HTTPError, e:
 return e
 try:
 json_res = json.loads(res.read())
 return json_res['html_url']
 except HTTPError, e:
 return e
if __name__ == &quot;__main__&quot;:
 s = sys.stdin.read()
 print do_gist_json(s)</pre>
<p>New in version 0.12.</p>
<h3>color_scheme</h3>
<p>See <i>themes</i> for more information. </p>
<p> Color schemes should be put in <code>$XDG_CONFIG_HOME/bpython/</code> </p>
<p> e.g to use the theme <code>$XDG_CONFIG_HOME/bpython/foo.theme</code> set <code>color_scheme = foo</code> </p>
<p> If you set the colorscheme to <i>foo</i> this will be translated to <code>$XDG_CONFIG_HOME/bpython/foo.theme</code> so be sure to put the file in that directory. </p>
<p> Leave blank or set to &quot;default&quot; to use the default (builtin) theme.</p>
<h3>flush_output</h3>
<p>Whether to flush all output to stdout on exit (default: True).</p>
<h2>Keyboard</h2>
<p>This section refers to the <code>[keyboard]</code> section in your <code>$XDG_CONFIG_HOME/bpython/config</code>. </p>
<p> You can set various keyboard shortcuts to be used by bpython. However, we have yet to map all keys to their respective control codes. If you configure a key combination which is not yet supported by bpython it will raise an exception telling you the key does not exist in bpython.keys. </p>
<p> Valid keys are:</p>
<dl>
<dt>&bull;</p>
<dd>Control + any alphanumeric character (C-a through A-z, also a few others).</p>
<dt>&bull;</p>
<dd>Any function key ranging from F1 to F12.</dl>
<h3>pastebin</h3>
<p>Default: &lt;F8&gt;</p>
<h3>last_output</h3>
<p>Default: F9 </p>
<p> Shows the last output in the systems $PAGER.</p>
<h3>save</h3>
<p>Default: C-s </p>
<p> Saves the current session to a file (prompts for filename)</p>
<h3>undo</h3>
<p>Default: C-r </p>
<p> Rewinds the last action.</p>
<h3>up_one_line</h3>
<p>Default: C-p </p>
<p> Move the cursor up, by one line.</p>
<h3>down_one_line</h3>
<p>Default: C-n </p>
<p> Move the cursor down, by one line.</p>
<h3>cut_to_buffer</h3>
<p>Default: C-k </p>
<p> Cuts the current line to the buffer.</p>
<h3>search</h3>
<p>Default: C-o </p>
<p> Search up for any lines containing what is on the current line.</p>
<h3>yank_from_buffer</h3>
<p>Default: C-y </p>
<p> Pastes the current line from the buffer (the one you previously cutted)</p>
<h3>clear_word</h3>
<p>Default: C-w </p>
<p> Clear the word the cursor is currently on.</p>
<h3>clear_line</h3>
<p>Default: C-u </p>
<p> Clears to the beginning of the line.</p>
<h3>clear_screen</h3>
<p>Default: C-l </p>
<p> Clears the screen to the top.</p>
<h3>show_source</h3>
<p>Default: F2 </p>
<p> Shows the source of the currently being completed (python) function.</p>
<h3>exit</h3>
<p>Default: C-d </p>
<p> Exits bpython (use on empty line)</p>
<h2>Cli</h2>
<p>This refers to the <code>[cli]</code> section in your config file.</p>
<h3>suggestion_width</h3>
<p>Default: 0.8 </p>
<p> The width of the suggestion window in percent of the terminal width. </p>
<p> New in version 0.9.8.</p>
<h3>trim_prompts</h3>
<p>Default: False </p>
<p> Trims lines starting with &#8216;&gt;&gt;&gt; &#8216; when set to True.</p>
<h2>Gtk</h2>
<p>This refers to the <code>[gtk]</code> section in your <i>$XDG_CONFIG_HOME/bpython/config</i> file.</p>
<h3>font</h3>
<p>Default: Monospace 10 </p>
<p> The font to be used by the GTK version.</p>
<h2>Author</h2>
<p><code>bpython</code> was written by Robert Anthony Farrell &lt;<i>robertanthonyfarrel [at] gmail.com</i>&gt; and his bunch of loyal followers. </p>
<p> This manual page was written by Jørgen Pedersen Tjernø &lt;<i>jorgen [at] devsoft.no</i>&gt;, for the Debian project (but may be used by others).</p>
<h2>Copyright</h2>
<p>2008-2012 Bob Farrell, Andreas Stuehrk et al.</p>
