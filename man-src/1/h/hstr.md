---
title: "hstr(1)"
name: "hstr"
section: "1"
letter: "h"
url: "/docs/linux/man/1-hstr/"
description: "hh – easily view, navigate, sort and use your command history with shell history suggest box."
---

<h2>NAME</h2>
<p> <code>hh</code> &#8211; easily view, navigate, sort and use your command history with shell history suggest box.</p>
<h2>SYNOPSIS</h2>
<p> <code>hh [option] [arg1] [arg2]&#8230; </code></p>
<dl>
<dt>
<dd> <code>hstr [option] [arg1] [arg2]&#8230;</code></dl>
<h2>DESCRIPTION</h2>
<p> <code>hh</code> uses shell history to provide suggest box like functionality for commands used in the past. By default it parses .bash-history file that is filtered as you type a command substring. Commands are not just filtered, but also ordered by a ranking algorithm that considers number of occurences, length and timestamp. Favorite and frequently used commands can be bookmarked. In addition <code>hh</code> allows removal of commands from history &#8211; for instance with a typo or with a sensitive content.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h &#8211;help</code></p>
<dd> Show help</p>
<dt><code>-n &#8211;non-interactive</code></p>
<dd> Print filtered history on standard output and exit</p>
<dt><code>-f &#8211;favorites</code></p>
<dd> Show favorites view immediately</p>
<dt><code>-s &#8211;show-configuration</code></p>
<dd> Show configuration that can be added to ~/.bashrc</p>
<dt><code>-b &#8211;show-blacklist</code></p>
<dd> Show blacklist of commands to be filtered out before history processing</p>
<dt><code>-V &#8211;version</code></p>
<dd> Show version information</dl>
<h2>KEYS</h2>
<dl>
<dt><code>pattern</code></p>
<dd> Type to filter shell history.</p>
<dt><code>Ctrl-e</code></p>
<dd> Toggle regular expression and substring search.</p>
<dt><code>Ctrl-t</code></p>
<dd> Toggle case sensitive search.</p>
<dt><code>Ctrl-/</code>, <code>Ctrl-7</code></p>
<dd> Rotate view of history as provided by Bash, ranked history ordered by the number of occurences/length/timestamp and favorites.</p>
<dt><code>Ctrl-f</code></p>
<dd> Add currently selected command to favorites.</p>
<dt><code>Ctrl-l</code></p>
<dd> Make search pattern lowercase or uppercase.</p>
<dt><code>Ctrl-r</code>, <code>UP</code> arrow, <code>DOWN</code> arrow, <code>Ctrl-n</code>, <code>Ctrl-p</code></p>
<dd> Navigate in the history list.</p>
<dt><code>TAB</code>, <code>RIGHT</code> arrow</p>
<dd> Choose currently selected item for completion and let user to edit it on the command prompt.</p>
<dt><code>LEFT</code> arrow</p>
<dd> Choose currently selected item for completion and let user to edit it in editor (fix command).</p>
<dt><code>ENTER</code></p>
<dd> Choose currently selected item for completion and execute it.</p>
<dt><code>DEL</code></p>
<dd> Remove currently selected item from the shell history.</p>
<dt><code>BACSKSPACE</code>, <code>Ctrl-h</code></p>
<dd> Delete last pattern character.</p>
<dt><code>Ctrl-u</code>, <code>Ctrl-w</code></p>
<dd> Delete pattern and search again.</p>
<dt><code>Ctrl-x</code></p>
<dd> Write changes to shell history and exit.</p>
<dt><code>Ctrl-g</code></p>
<dd> Exit with empty prompt.</dl>
<h2>ENVIRONMENT VARIABLES</h2>
<p> <code>hh</code> defines the following environment variables:</p>
<dl>
<dt><code>HH_CONFIG</code></p>
<dd> Configuration options: </p>
<p> <i>hicolor</i><br />
&nbsp;<wbr>&nbsp;<wbr>Get more colors with this option&nbsp;<wbr>(default is monochromatic). </p>
<p> <i>monochromatic</i><br />
&nbsp;<wbr>&nbsp;<wbr>Ensure black and white view. </p>
<p> <i>regexp</i><br />
&nbsp;<wbr>&nbsp;<wbr>Filter command history using regular expressions&nbsp;<wbr>(substring match is default)&nbsp;<wbr> </p>
<p> <i>substring</i><br />
&nbsp;<wbr>&nbsp;<wbr>Filter command history using substring. </p>
<p> <i>keywords</i><br />
&nbsp;<wbr>&nbsp;<wbr>Filter command history using keywords &#8211; item matches if contains all keywords in pattern in any order. </p>
<p> <i>casesensitive</i><br />
&nbsp;<wbr>&nbsp;<wbr>Make history filtering case sensitive&nbsp;<wbr>(it&#8217;s case insensitive by default).&nbsp;<wbr> </p>
<p> <i>rawhistory</i><br />
&nbsp;<wbr>&nbsp;<wbr>Show normal history as a default view&nbsp;<wbr>(metric-based view is shown otherwise).&nbsp;<wbr> </p>
<p> <i>favorites</i><br />
&nbsp;<wbr>&nbsp;<wbr>Show favorites as a default view&nbsp;<wbr>(metric-based view is shown otherwise). </p>
<p> <i>blacklist</i><br />
&nbsp;<wbr>&nbsp;<wbr>Load list of commands to skip when processing history from&nbsp;<wbr>~/.hh_blacklist&nbsp;<wbr>(built-in blacklist used otherwise). </p>
<p> <i>bigkeysskip</i><br />
&nbsp;<wbr>&nbsp;<wbr>Skip big history entries i.e. very long lines&nbsp;<wbr>(default). </p>
<p> <i>bigkeysfloor</i><br />
&nbsp;<wbr>&nbsp;<wbr>Use different sorting slot for big keys when building metrics-based view&nbsp;<wbr>(big keys are skipped by default). </p>
<p> <i>bigkeysexit</i><br />
&nbsp;<wbr>&nbsp;<wbr>Exit&nbsp;<wbr>(fail)&nbsp;<wbr>on presence of a big key in history&nbsp;<wbr>(big keys are skipped by default). </p>
<p> <i>warning</i><br />
&nbsp;<wbr>&nbsp;<wbr>Show warning. </p>
<p> <i>debug</i><br />
&nbsp;<wbr>&nbsp;<wbr>Show debug information. </p>
<p> Example:<br />
&nbsp;<wbr>&nbsp;<wbr><code>export HH_CONFIG=hicolor,regexp,rawhistory</code> </p>
<dt><code>HH_PROMPT</code></p>
<dd> Change prompt string which is <code>user [at] host$</code> by default. </p>
<p> Example:<br />
&nbsp;<wbr>&nbsp;<wbr><code>export HH_PROMPT=&quot;$&nbsp;<wbr>&quot;</code> </p>
</dl>
<h2>FILES</h2>
<dl>
<dt><code>~/.hh_favorites</code></p>
<dd>
&nbsp;<wbr>Bookmarked favorite commands.</p>
<dt><code>~/.hh_blacklist</code></p>
<dd>
&nbsp;<wbr>Command blacklist. </p>
</dl>
<h2>BASH CONFIGURATION</h2>
<p> Optionally add the following lines to ~/.bashrc: </p>
<pre><code>
export HH_CONFIG = hicolor #get more colors
                       shopt -
                   s histappend #append new history items to.bash_history export HISTCONTROL = ignorespace #leading space hides commands from history export HISTFILESIZE = 10000 #increase history file size(default is 500) export HISTSIZE = $
{
    HISTFILESIZE
}
#increase history size(default is 500) export PROMPT_COMMAND = "history -a; history -n; ${PROMPT_COMMAND}"
#if this is interactive shell, then bind hh to Ctrl - r(for Vi mode check doc)
    if[[$ - = ~ .*i.*]];
then bind '"\C-r": "\C-a hh \C-j"';
fi
</code></pre>
<p> The prompt command ensures synchronization of the history between BASH memory and history file.</p>
<h2>ZSH CONFIGURATION</h2>
<p> Optionally add the following lines to ~/.zshrc: </p>
<pre>
export HISTFILE=~/.zsh_history   # ensure history file visibility
export HH_CONFIG=hicolor         # get more colors
bindkey -s &quot;\C-r&quot; &quot;qhh
&quot;      # bind hh to Ctrl-r (for Vi mode check doc)
</pre>
<h2>EXAMPLES</h2>
<dl>
<dt><code>hh git</code></p>
<dd>
&nbsp;<wbr>Start&nbsp;<wbr>`hh`&nbsp;<wbr>and show only history items containing&nbsp;<wbr>&#8216;git&#8217;.</p>
<dt><code>hh &#8211;non-interactive git</code></p>
<dd>
&nbsp;<wbr>Print history items containing&nbsp;<wbr>&#8216;git&#8217;&nbsp;<wbr>to standard output and exit.</p>
<dt><code>hh &#8211;show-configuration &gt;&gt; ~/.bashrc</code></p>
<dd>
&nbsp;<wbr>Append default&nbsp;<wbr><code>hh</code>&nbsp;<wbr>configuration to your Bash profile.</p>
<dt><code>hh &#8211;show-blacklist</code></p>
<dd>
&nbsp;<wbr>Show blacklist configured for history processing.</dl>
<h2>AUTHOR</h2>
<p> Written by Martin Dvorak &lt;martin.dvorak [at] mindforger.com&gt;</p>
<h2>BUGS</h2>
<p> Report bugs to <a rel="nofollow" href="https://github.com/dvorka/hstr/issues">https://github.com/dvorka/hstr/issues</a></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-history/">history</a></code>(1), <code><a href="/docs/linux/man/1-bash/">bash</a></code>(1), <code><a href="/docs/linux/man/1-zsh/">zsh</a></code>(1) </p>
<h2>Index</h2>
