---
title: "fasd(1)"
name: "fasd"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fasd/"
---

<h2>NAME</h2>

 

 fasd - quick access to files and directories

<h2>SYNOPSIS</h2>

 

 fasd [options] [query ...] 

 [f|a|s|d|z] [options] [query ...] 

 fasd [-A|-D] [paths ...]

<h2>OPTIONS</h2>

<dl>
<dt>
<dd> <pre><code>
- s &amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
list paths with ranks - l &amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
list paths without ranks - i &amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
interactive mode - e &amp;nbsp;
&lt;cmd&gt; &amp;nbsp;
&amp;nbsp;
&amp;nbsp;
set command to execute on the result file - b &amp;nbsp;
&lt;name&gt; &amp;nbsp;
&amp;nbsp;
only use &amp;nbsp;
&lt;name&gt; &amp;nbsp;
backend - B &amp;nbsp;
&lt;name&gt; &amp;nbsp;
&amp;nbsp;
add additional backend &amp;nbsp;
&lt;name&gt; - a &amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
match files and directories - d &amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
match directories only - f &amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
match files only - r &amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
match by rank only - t &amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
match by recent access only - R &amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
reverse listing order - h &amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
show a brief help message - [0 - 9] &amp; nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
select the nth entry
</code></pre></dl>

<h2>DESCRIPTION</h2>

 

 Fasd keeps track of files and directories you access in your shell and gives you quick access to them. You can use fasd to reference files or directories by just a few key identifying characters. You can use fasd to boost your command line productivity by defining your own aliases to launch programs on files or directories. Fasd, by default, provides some basic aliases, including a shell function &quot;z&quot; that resembles the functionality of &quot;z&quot; and &quot;autojump.&quot; 

 The name &quot;fasd&quot; comes from the default suggested aliases f(files), a(files/directories), s(show/search/select), d(directories). 

 Fasd ranks files and directories by &quot;frecency,&quot; that is, by both &quot;frequency&quot; and &quot;recency.&quot; The term &quot;frecency&quot; was first coined by Mozilla and used in Firefox.

<h2>EXAMPLES</h2>

<dl>
<dt>
<dd> <pre>
z bundle
f -e vim nginx conf
f -i rc$
vi&nbsp;<wbr>`f nginx conf`
cp update.html&nbsp;<wbr>`d www`
open&nbsp;<wbr>`sf pdf`
</pre></dl>

<h2>SHELL INITIALIZATION</h2>

 

 To get fasd working in a shell, some initialization code must be run. Put lines below in your POSIX compatible shell rc.
<dl>
<dt>
<dd> <pre>
eval&nbsp;<wbr>&quot;$(fasd --init auto)&quot;
</pre></dl>
 

 This will setup a command hook that executes on every command and advanced tab completion for zsh and bash. 

 If you want more control over what gets into your shell environment, you can pass customized set of arguments to fasd --init.
<dl>
<dt>
<dd> 
zsh - hook &amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
#&amp; nbsp;
define &amp;nbsp;
_fasd_preexec and add it to zsh preexec array
        zsh -
    ccomp &amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
#&amp; nbsp;
zsh command mode completion definitions
        zsh -
    ccomp - install &amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
#&amp; nbsp;setup command mode completion for zsh
zsh-wcomp&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
#&amp; nbsp;
zsh word mode completion definitions
        zsh -
    wcomp - install &amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
#&amp; nbsp;setup word mode completion for zsh
bash-hook&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
#&amp; nbsp;
add hook code to bash &amp;nbsp;
$PROMPT_COMMAND
bash - ccomp &amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
#&amp; nbsp;
bash command mode completion definitions
        bash -
    ccomp - install &amp;nbsp;
&amp;nbsp;
&amp;nbsp;
#&amp; nbsp;setup command mode completion for bash
posix-alias&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
#&amp; nbsp;
define aliases that applies to all posix shells
        posix -
    hook &amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
#&amp; nbsp;
setup &amp;nbsp;$PS1 hook for shells that's posix compatible
tcsh-alias&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
#&amp; nbsp;define aliases for tcsh
tcsh-hook&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
#&amp; nbsp;
setup tcsh precmd alias
</dl>
 

 Example for a minimal zsh setup (no tab completion):
<dl>
<dt>
<dd> <pre>
eval&nbsp;<wbr>&quot;$(fasd --init posix-alias zsh-hook)&quot;
</pre></dl>
 

 Note that this method will slightly increase your shell start-up time, since calling binaries has overhead. You can cache fasd init code if you want minimal overhead. Example code for bash (to be put into .bashrc):
<dl>
<dt>
<dd> 
fasd_cache = "$HOME/.fasd-init-bash" if &amp; nbsp;
[&amp;nbsp; "$(command -v fasd)" &amp; nbsp; - nt &amp; nbsp; "$fasd_cache" &amp; nbsp; - o &amp; nbsp; !&amp;nbsp; - s &amp; nbsp; "$fasd_cache" &amp; nbsp;];
&amp;nbsp;
then
    &amp;nbsp;
&amp;nbsp;
fasd-- init posix - alias bash - hook bash - ccomp bash - ccomp - install &amp;nbsp;
&gt; | &amp;nbsp;
"$fasd_cache" fi
    source &amp;nbsp;
"$fasd_cache" unset fasd_cache
</dl>
 

 Optionally, if you can also source fasd if you want fasd to be a shell function instead of an executable. 

 You can tweak initialization code. For instance, if you want to use &quot;c&quot; instead of &quot;z&quot; to do directory jumping, you can use the alias below:
<dl>
<dt>
<dd> 
alias c = 'fasd_cd -d'
#&amp; nbsp;`- d'&amp;nbsp;option present for bash completion
#&amp; nbsp; function fasd_cd is defined in posix - alias
</dl>

<h2>MATCHING</h2>

 

 Fasd has three matching modes: default, case-insensitive, and fuzzy. 

 For a given set of queries (the set of command-line arguments passed to fasd), a path is a match if and only if:
<dl>
<dt>1.
<dd> Queries match the path in order.
<dt>2.
<dd> The last query matches the last segment of the path.</dl>
 

 If no match is found, fasd will try the same process ignoring case. If still no match is found, fasd will allow extra characters to be placed between query characters for fuzzy matching. 

 Tips:
<dl>
<dt>&bull;
<dd> If you want your last query not to match the last segment of the path, append `/' as the last query.
<dt>&bull;
<dd> If you want your last query to match the end of the filename, append `$' to the last query.</dl>

<h2>COMPATIBILITY</h2>

 

 Fasd's basic functionalities are POSIX compliant, meaning that you should be able to use fasd in all POSIX compliant shells. Your shell need to support command substitution in $PS1 in order for fasd to automatically track your commands and files. This feature is not specified by the POSIX standard, but it's nonetheless present in many POSIX compliant shells. In shells without prompt command or prompt command substitution (tcsh for instance), you can add entries manually with &quot;fasd -A&quot;. You are very welcomed to contribute shell initialization code for not yet supported shells.

<h2>TAB COMPLETION</h2>

 

 Fasd offers two completion modes, command mode completion and word mode completion. Command mode completion works in bash and zsh. Word mode completion only works in zsh. 

 Command mode completion is just like completion for any other commands. It is triggered when you hit tab on a fasd command or its aliases. Under this mode your queries can be separated by a space. Tip: if you find that the completion result overwrites your queries, type an extra space before you hit tab. 

 Word mode completion can be triggered on any command. Word completion is triggered by any command line argument that starts with &quot;,&quot; (all), &quot;f,&quot; (files), or &quot;d,&quot; (directories), or that ends with &quot;,,&quot; (all), &quot;,,f&quot; (files), or &quot;,,d&quot; (directories). Examples:
<dl>
<dt>
<dd> 
$ &amp;nbsp;
vim, rc, lo&lt;Tab&gt; $ &amp;nbsp;
vim &amp;nbsp;
/ etc / rc.local $ &amp;nbsp;
mv index.html d, www&lt;Tab&gt;
                     $ &amp;nbsp;
mv index.html &amp;nbsp;
/ var / www /
</dl>
 

 There are also three zle widgets: &quot;fasd-complete&quot;, &quot;fasd-complete-f&quot;, &quot;fasd-complete-d&quot;. You can bind them to keybindings you like:
<dl>
<dt>
<dd> 
bindkey &amp;nbsp;
'^X^A' &amp; nbsp;
fasd - complete &amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
#&amp; nbsp;
C - x C - a to do fasd - complete &amp;nbsp;
(fils and directories)
    bindkey &amp;nbsp;
'^X^F' &amp; nbsp;
fasd - complete - f &amp;nbsp;
&amp;nbsp;
#&amp; nbsp;
C - x C - f to do fasd - complete - f &amp;nbsp;
(only files)
    bindkey &amp;nbsp;
'^X^D' &amp; nbsp;
fasd - complete - d &amp;nbsp;
&amp;nbsp;
#&amp; nbsp;
C - x C - d to do fasd - complete - d &amp;nbsp;
(only directories)
</dl>

<h2>BACKENDS</h2>

 

 Fasd can take advantage of different sources of recent / frequent files. Most desktop environments (like Gtk) and some editors (like Vim) keep a list of accessed files. Fasd can use them as additional backends if the data can be converted into fasd's native format. As of now, fasd supports Gtk's recently-used.xbel and Vim's viminfo backends. You can define your own backend by declaring a function by that name in your .fasdrc. You set default backend with _FASD_BACKENDS variable in our .fasdrc.

<h2>TWEAKS</h2>

 

 Upon every execution, fasd will source &quot;/etc/fasdrc&quot; and &quot;$HOME/.fasdrc&quot; if they are present. Below are some variables you can set:
<dl>
<dt>
<dd> <pre><code>
$_FASD_DATA
Path to the fasd data file, default &amp;nbsp;
"$HOME/.fasd".$_FASD_BLACKLIST
        List of blacklisted strings.Commands matching them will not be processed.Default is &amp;
    nbsp;
"--help".$_FASD_SHIFT
    List of all commands that needs to be shifted,
    defaults to &amp;nbsp;
"sudo busybox".$_FASD_IGNORE
    List of all commands that will be ignored,
    defaults to &amp;nbsp;
"fasd ls echo".$_FASD_TRACK_PWD
    Fasd defaults to track your &amp;nbsp;
"$PWD".Set this to 0 to disable this behavior.$_FASD_AWK
    Which awk to use.fasd can detect and use a compatible awk.$_FASD_SINK
        File to log all STDERR to,
    defaults to &amp;nbsp;
"/dev/null".$_FASD_MAX
    Max total score &amp;nbsp;
/ &amp;nbsp;
weight, defaults to 2000. $_FASD_SHELL Which shell to execute.Some shells will run faster than others.fasd runs faster with dash and ksh variants.$_FASD_BACKENDS Default backends.$_FASD_RO If set to any non - empty string, fasd will not add or delete entries from database.You can set and export this variable from command line.$_FASD_FUZZY Level of &amp; nbsp;
"fuzziness" &amp; nbsp;when doing fuzzy matching. More precisely, the number of
characters that can be skipped to generate a match. Set to empty or 0 to
disable fuzzy matching. Default value is 2.
$_FASD_VIMINFO
Path to .viminfo file for viminfo backend, defaults to&amp;nbsp;"$HOME/.viminfo"
$_FASD_RECENTLY_USED_XBEL
Path to XDG recently-used.xbel file for recently-used backend, defaults to
"$HOME/.local/share/recently-used.xbel"
</code></pre></dl>

<h2>DEBUGGING</h2>

 

 Fasd is hosted on GitHub: <a rel="nofollow" HREF="https://github.com/clvv/fasd">https://github.com/clvv/fasd</a> 

 If fasd does not work as expected, please file a bug report on GitHub describing the unexpected behavior along with your OS version, shell version, awk version, sed version, and a log file. 

 You can set _FASD_SINK in your .fasdrc to obtain a log.
<dl>
<dt>
<dd> <pre>
_FASD_SINK=&quot;$HOME/.fasd.log&quot;
</pre></dl>

<h2>COPYING</h2>

 

 Fasd is originally written based on code from z (<a rel="nofollow" HREF="https://github.com/rupa/z)">https://github.com/rupa/z)</a> by rupa deadwyler under the WTFPL license. Most if not all of the code has been rewritten. Fasd is licensed under the &quot;MIT/X11&quot; license.

<h2>AUTHORS</h2>

 Wei Dai &lt;x@wei23.net&gt;. 

<h2>Index</h2>


