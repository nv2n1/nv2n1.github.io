---
title: "zsh-lovers(1)"
name: "zsh-lovers"
section: "1"
letter: "z"
url: "/docs/linux/man/1-zsh-lovers/"
description: "zsh-lovers – tips, tricks and examples for the Z shell"
---

<h2 class="name">NAME</h2>
<p> zsh-lovers &#8211; tips, tricks and examples for the Z shell </p>
<h2>SYNOPSIS</h2>
<p> Just read it. ;-)</p>
<h2>OVERVIEW</h2>
<p> Whenever we look at the zsh manual we wonder why there are no examples or those simply things in (shell) life. The zsh contains many features, but there was no manpage with some examples (like <a href="/docs/linux/man/5-procmailex/">procmailex</a>(5)). That&#8217;s why we wrote this manpage. </p>
<p> Most of the tricks and oneliner come from the mailinglists zsh-users, zsh-workers, google, newsgroups and from ourself. See section <code>LINKS</code> for details. </p>
<p> Note: This manpage (<a href="/docs/linux/man/1-zsh-lovers/">zsh-lovers</a>(1)) is <code>not</code> an offical part of the Z shell! It&#8217;s just a just for fun &#8211; manpage ;) For comments, bugreports and feedback take a quick look at the section <code>BUGS</code>.</p>
<h2>SHELL-SCRIPTING</h2>
<p> This section provides some examples for often needed shellscript-stuff. Notice that you should not use otherwise most examples won&#8217;t work. Parse options in shellscripts. Example taken from ZWS by Adam Chodorowski (<a rel="nofollow" href="http://www.chodorowski.com/projects/zws/">http://www.chodorowski.com/projects/zws/</a>): </p>
<dl>
<dt>
<dd>
<pre><code>
parse_options()
{
    o_port=(-p 9999)
    o_root=(-r WWW)
    o_log=(-d ZWS.log)
    zparseopts -K -- p:=o_port r:=o_root l:=o_log h=o_help
    if [[ $? != 0 || "$o_help" != "" ]];
    then
        echo Usage : $(basename "$0") "[-p PORT] [-r DIRECTORY]" exit 1 fi
                         port = $o_port[2] root = $o_root[2] log = $o_log[2] if [[$root [1] != '/']];
    then root = "$PWD/$root";
    fi
}
#now use the function:
parse_options $ *
</code></pre>
</dl>
<h2>EXAMPLES</h2>
<p> Available subsections are <code>Aliases</code>, <code>Completion</code>, <code>Unsorted/Misc examples</code>, <code>(Recursive) Globbing &#8211; Examples</code>, <code>Modifiers usage</code>, <code>Redirection-Examples</code>, <code>ZMV-Examples</code> and <code>Module-Examples</code>.</p>
<h3>ALIASES</h3>
<p> Suffix aliases are supported in zsh since version 4.2.0. Some examples: </p>
<dl>
<dt>
<dd>
<pre>
alias -s tex=vim
alias -s html=w3m
alias -s org=w3m
</pre>
</dl>
<p> Now pressing return-key after entering <i>foobar.tex</i> starts vim with foobar.tex. Calling a html-file runs browser w3m. <i><a rel="nofollow" href="http://www.zsh.org">www.zsh.org</a></i> and pressing enter starts w3m with argument <a href="http://www.zsh.org">www.zsh.org</a>. Global aliases can be used anywhere in the command line. Example: </p>
<dl>
<dt>
<dd>
<pre>
$ alias -g C='| wc -l'
$ grep alias ~/.zsh/* C
443
</pre>
</dl>
<p> Some more or less useful global aliases (choose whether they are useful or not for you on your own): </p>
<dl>
<dt>
<dd>
alias &#8211; g&#8230; = &#8216;../..&#8217; alias &#8211; g&#8230;.= &#8216;../../..&#8217; alias &#8211; g&#8230;..= &#8216;../../../..&#8217; alias &#8211; g CA = &#8220;2&gt;&amp;1 | cat -A&#8221; alias &#8211; g C = &#8216;| wc -l&#8217; alias &#8211; g D = &#8220;DISPLAY=:0.0&#8221; alias &#8211; g DN = / dev / null alias &#8211; g ED = &#8220;export DISPLAY=:0.0&#8221; alias &#8211; g EG = &#8216;|&amp; egrep&#8217; alias &#8211; g EH = &#8216;|&amp; head&#8217; alias &#8211; g EL = &#8216;|&amp; less&#8217; alias &#8211; g ELS = &#8216;|&amp; less -S&#8217; alias &#8211; g ETL = &#8216;|&amp; tail -20&#8217; alias &#8211; g ET = &#8216;|&amp; tail&#8217; alias &#8211; g F = &#8216; | fmt -&#8216; alias &#8211; g G = &#8216;| egrep&#8217; alias &#8211; g H = &#8216;| head&#8217; alias &#8211; g HL = &#8216;|&amp; head -20&#8217; alias &#8211; g Sk = &#8220;*~(*.bz2|*.gz|*.tgz|*.zip|*.z)&#8221; alias &#8211; g LL = &#8220;2&gt;&amp;1 | less&#8221; alias &#8211; g L = &#8220;| less&#8221; alias &#8211; g LS = &#8216;| less -S&#8217; alias &#8211; g MM = &#8216;| most&#8217; alias &#8211; g M = &#8216;| more&#8217; alias &#8211; g NE = &#8220;2&gt; /dev/null&#8221; alias &#8211; g NS = &#8216;| sort -n&#8217; alias &#8211; g NUL = &#8220;&gt; /dev/null 2&gt;&amp;1&#8221; alias &#8211; g PIPE = &#8216;|&#8217; alias &#8211; g R = &#8216; &gt; /c/aaa/tee.txt &#8216; alias &#8211; g RNS = &#8216;| sort -nr&#8217; alias &#8211; g S = &#8216;| sort&#8217; alias &#8211; g TL = &#8216;| tail -20&#8217; alias &#8211; g T = &#8216;| tail&#8217; alias &#8211; g US = &#8216;| sort -u&#8217; alias &#8211; g VM = / var / log / messages alias &#8211; g X0G = &#8216;| xargs -0 egrep&#8217; alias &#8211; g X0 = &#8216;| xargs -0&#8217; alias &#8211; g XG = &#8216;| xargs egrep&#8217; alias &#8211; g X = &#8216;| xargs&#8217;
</dl>
<h3>COMPLETION</h3>
<p> See also man 1 zshcompctl zshcompsys zshcompwid. zshcompctl is the old style of zsh programmable completion, zshcompsys is the new completion system, zshcompwid are the zsh completion widgets. </p>
<p> Some functions, like _apt and _dpkg, are very slow. You can use a cache in order to proxy the list of results (like the list of available debian packages) Use a cache: </p>
<dl>
<dt>
<dd>
<pre>
zstyle ':completion:*' use-cache on
zstyle ':completion:*' cache-path ~/.zsh/cache
</pre>
</dl>
<p> Prevent CVS files/directories from being completed: </p>
<dl>
<dt>
<dd>
<pre>
zstyle ':completion:*:(all-|)files' ignored-patterns '(|*/)CVS'
zstyle ':completion:*:cd:*' ignored-patterns '(*/)#CVS'
</pre>
</dl>
<p> Fuzzy matching of completions for when you mistype them: </p>
<dl>
<dt>
<dd>
<pre>
zstyle ':completion:*' completer _complete _match _approximate
zstyle ':completion:*:match:*' original only
zstyle ':completion:*:approximate:*' max-errors 1 numeric
</pre>
</dl>
<p> And if you want the number of errors allowed by _approximate to increase with the length of what you have typed so far: </p>
<dl>
<dt>
<dd>
<pre>
zstyle -e ':completion:*:approximate:*' \
        max-errors 'reply=($((($#PREFIX+$#SUFFIX)/3))numeric)'
</pre>
</dl>
<p> Ignore completion functions for commands you don&#8217;t have: </p>
<dl>
<dt>
<dd>
<pre>
zstyle ':completion:*:functions' ignored-patterns '_*'
</pre>
</dl>
<p> With helper functions like: </p>
<dl>
<dt>
<dd>
xdvi()<br />
{<br />
    command xdvi $<br />
    {<br />
        * : -*.dvi(om[1])<br />
    }<br />
}
</dl>
<p> you can avoid having to complete at all in many cases, but if you do, you might want to fall into menu selection immediately and to have the words sorted by time: </p>
<dl>
<dt>
<dd>
<pre>
zstyle ':completion:*:*:xdvi:*' menu yes select
zstyle ':completion:*:*:xdvi:*' file-sort time
</pre>
</dl>
<p> Completing process IDs with menu selection: </p>
<dl>
<dt>
<dd>
<pre>
zstyle ':completion:*:*:kill:*' menu yes select
zstyle ':completion:*:kill:*'   force-list always
</pre>
</dl>
<p> If you end up using a directory as argument, this will remove the trailing slash (usefull in ln) </p>
<dl>
<dt>
<dd>
<pre>
zstyle ':completion:*' squeeze-slashes true
</pre>
</dl>
<p> cd will never select the parent directory (e.g.: cd ../&lt;TAB&gt;): </p>
<dl>
<dt>
<dd>
<pre>
zstyle ':completion:*:cd:*' ignore-parents parent pwd
</pre>
</dl>
<p> Another method for <i>quick change directories</i>. Add this to your ~/.zshrc, then just enter &#8220;cd &#8230;./dir&#8221; </p>
<dl>
<dt>
<dd>
rationalise &#8211; dot()<br />
{<br />
    if<br />
        [[$LBUFFER = *..]];<br />
    then<br />
        LBUFFER += /..else LBUFFER +=.fi<br />
}<br />
zle &#8211; N rationalise &#8211; dot bindkey.rationalise &#8211; dot
</dl>
<h3>UNSORTED/MISC examples</h3>
<p> Hint: A list of valid glob Qualifiers can be found in <a href="/docs/linux/man/1-zshexpn/">zshexpn</a>(1). See &#8220;man 1 zshexpn | less -p&#8221; Qualifiers for details. </p>
<dl>
<dt>
<dd>
#Get the names of all files that *don&#8217;t* match a pattern *anywhere* on the<br />
#file(and without &#8220;-L&#8221; because its GNUish)<br />
$ print &#8211; rl&#8211; *(.^ e{&#8216;grep -q pattern $REPLY&#8217;})<br />
# or<br />
              $ : *(.e{&#8216;grep -q pattern $REPLY || print -r &#8212; $REPLY&#8217;})<br />
#random numbers<br />
                      $ echo $[${RANDOM} % 1000] #random between 0 &#8211;<br />
                  999 $ echo $[${RANDOM} % 11 + 10] #random between 10 &#8211; 20 $ echo $<br />
{<br />
    (l : 3 ::0<br />
     :) $<br />
    {<br />
        RANDOM<br />
    }<br />
}<br />
#N digits long(3 digits)<br />
#reverse a word<br />
        $ echo &#8220;${(j::)${(@Oa)${(s::):-hello}}}&#8221;<br />
#Show newest directory<br />
    $ ls &#8211;<br />
    ld *(/ om[1])<br />
#random array element<br />
        $ FILES = (&#8230; / files /* )<br />
            $ feh $FILES[$RANDOM%$#FILES+1]<br />
          # cat first line in all files in this dir<br />
            $ for file (*(ND-.)) IFS= read -re &lt; $file<br />
          # test if a parameter is numeric<br />
            $ if [[ $1 == &lt;-&gt; ]] ; then<br />
                   echo numeric<br />
              else<br />
                   echo non-numeric<br />
              fi<br />
          # Show me all the .c files for which there doesn&#8217;t exist a .o file.<br />
            $ print *.c(e_'[[ ! -e $REPLY:r.o ]]&#8217;_)<br />
          # All files in /var/ that are not owned by root<br />
            $ ls -ld /var/*(^u:root)<br />
          # All files for which the owner hat read and execute permissions<br />
            $ echo *(f:u+rx:)<br />
          # The same, but also others dont have execute permissions<br />
            $ echo *(f:u+rx,o-x:)<br />
          # brace expansion &#8211; example<br />
            $ X=(A B C)<br />
            $ Y=(+ -)<br />
            $ print -r &#8212; $^X.$^Y<br />
            A.+ A.- B.+ B.- C.+ C.-<br />
          # Fetch the newest file containing the string &#8216;fgractg*.log&#8217; in the<br />
          # filename and contains the string &#8216;ORA-&#8216; in it<br />
            $ file=(fgractg*.log(Nm0om[1]))<br />
            $ (($#file)) &amp;&amp; grep -l ORA- $file<br />
            # without Zsh<br />
            $ files=$( find . -name . -o -prune -name &#8216;fgractg*&gt;log&#8217; -mtime 0 -print )<br />
            &gt; if [ -n &#8220;$files&#8221; ]; then<br />
            &gt;    IFS=&#8217;<br />
            &gt; &#8216;<br />
            &gt; set -f<br />
            &gt; file=$(ls -td $files | head -1)<br />
            &gt; grep -l ORA- &#8220;$file&#8221;<br />
            &gt; fi<br />
          # keep specified number of child processes running until entire task finished<br />
            $ zsh -c &#8216;sleep 1 &amp; sleep 3 &amp; sleep 2&amp; print -rl &#8212; $jobtexts&#8217;<br />
          # Remove zero length and .bak files in a directory<br />
            $ rm -i *(.L0) *.bak(.)<br />
          # print out files that dont have extensions<br />
            $ printf &#8216;%s
&#8217; ^?*.*<br />
            $ printf &#8216;%s
&#8217; ^?*.[^.]*(D)<br />
            $ ls -d &#8212; ^?*.*(D)<br />
          # Finding files which does not contain a specific string<br />
            $ print -rl file* | comm -2 -3 &#8211; &lt;(grep -l string file*)&#8217;<br />
            $ for f (file*(N)) grep -q string $f || print -r $f&#8217;<br />
          # Show/Check whether a option is set or not. It works both with $options as<br />
          # with $builtins<br />
            $ echo $options[correct]<br />
            off<br />
            $ $options[zle]<br />
            on<br />
          # Count the number of directories on the stack<br />
            $ print $((${${(z)${(f)&#8221;$(dirs -v)&#8221;}[-1]}[1]} + 1)) # or<br />
            $ dirs -v | awk &#8216;{n=$1}END{print n+1}&#8217;<br />
          # Matching all files which do not have a dot in filename<br />
            $ ls *~*.*(.)<br />
          # Show only the ip-address from &#8220;ifconfig device&#8221;<br />
            # ifconfig from net-tools (Linux)<br />
            $ print ${${$(LC_ALL=C /sbin/ifconfig eth0)[7]}:gs/addr://}<br />
            # ifconfig from 4.2BSD {Free,Net,Open}BSD<br />
            $ print ${$(/sbin/ifconfig tun0)[6]}<br />
          # Ping all the IP addresses in a couple of class C&#8217;s or all hosts<br />
          # into /etc/hosts<br />
            $ for i in {1..254}; do ping -c 1 192.168.13.$i; done<br />
            or<br />
            $ I=1<br />
            $ while ( [[ $I -le 255 ]] ) ; do ping -1 2 150.150.150.$I; let I++; done<br />
            or<br />
            $ for i in $(sed &#8216;s/#.*/<br />
                   / &#8216; &gt; /etc/hosts | awk &#8216; { print $2 }&#8217;)<br />
                   : do<br />
                   : echo &#8220;Trying $i &#8230; &#8221;<br />
                   : ping &#8211; c 1 $i;<br />
                   : echo &#8216;=============================&#8217;<br />
                   : done<br />
#load all available modules at startup<br />
                             $ typeset &#8211;<br />
                         U m<br />
                             $ m = ()<br />
                         $ for md($module_path) m = ($m $md /**/ * (*e<br />
                                                                    : &#8216;REPLY=${REPLY#$md/}&#8217; ::r))<br />
                                                        $ zmodload &#8211;<br />
                                                    i $m<br />
#Rename all files within a directory such that their names get a numeral<br />
#prefix in the default sort order.<br />
                                                        $ i = 1;<br />
                   for j in *; do mv $j $i.$j; ((i++)); done<br />
                                                            $ i = 1;<br />
                   for f in *; do mv $f $(echo $i |<br />
                                          awk &#8216;{ printf(&#8220;%03d&#8221;, $0)}&#8217;)<br />
                                   .$f;<br />
                   ((i++)); done<br />
                                $ integer i = 0;<br />
                   for f in *; do mv $f $[i += 1].$f; done<br />
#Find(and print) all symbolic links without a target within the current<br />
#dirtree.<br />
                                                          $ $ file *<br />
                                                      * /*(D@) | fgrep broken<br />
                                             $ for i in **/<br />
                                                      *(D @);<br />
                       [[-f $i || -d $i]] || echo $i<br />
                                                         $ echo *<br />
                                                     * /*(@-^./=%p)<br />
                                              $ print -l **/<br />
                                                     *(-@)<br />
#List all plain files that do not have extensions listed in `fignore&#8217;<br />
                                                         $ ls *<br />
                                                     * /*~*(${~${(j/|/)fignore}})(.)<br />
                                                # see above, but now omit executables<br />
                                                $ ls **/<br />
                                                     *~*(${~${(j / | /) fignore}})(.^ *)<br />
#Print out files that dont have extensions(require *setopt extendedglob *<br />
#and*setopt dotglob *)<br />
                                                         $ printf &#8216;%s
&#8217; ^<br />
                   ? * .*<br />
#List files in reverse order sorted by name<br />
                                 $ print &#8211;<br />
                             rl&#8211; * (On) or<br />
                         $ print &#8211; rl&#8211; * (^on)<br />
#Synonymic to &#8220;ps ax | awk &#8216;{print $1}&#8221;&#8217;<br />
                                              $ print &#8211;<br />
                             l / proc /*/cwd(:h:t:s/self//)<br />
                    # Get the PID of a process (without &#8220;ps&#8221;, &#8220;sed&#8221;, &#8220;pgrep&#8221;, ..<br />
                    # (under Linux)<br />
                      $ pid2 () {<br />
                      &gt;   local i<br />
                      &gt;   for i in /proc/&lt;-&gt;/stat<br />
                      &gt; do<br />
                      &gt;   [[ &#8220;$(&lt; $i)&#8221; = *\((${(j:|:)~@})\)* ]] &amp;&amp; echo $i:h:t<br />
                      &gt; done<br />
                      &gt; }<br />
                    # for X in &#8216;n&#8217; &#8216;o&#8217; &#8216;p&#8217; &#8216;q&#8217; &#8216;r&#8217; &#8216;s&#8217; &#8216;t&#8217; &#8216;u&#8217; &#8216;v&#8217; &#8216;w&#8217; &#8216;x&#8217; &#8216;y&#8217;; do &#8230;<br />
                      $ for (( i = 36#n; i &lt;= 36#y; i++ )); do<br />
                      &gt;   print ${$(([##36]i)):l}<br />
                      &gt; done<br />
                    # or in combination with &#8220;dc&#8221;<br />
                      $ print {$((##n))..$((##y))}P\ 10P | dc<br />
                    # or with &#8220;eval&#8221;<br />
                      $ eval print &#8216;${$(([##36]'{$((36#n))..$((36#y))}&#8217;)):l}&#8217;<br />
                    # foreach in one line of shell<br />
                      $ for f (*) print -r &#8212; $f<br />
                    # copy a directory recursively without data/files<br />
                      $ dirs=(**/ * (/))<br />
                                 $ cd&#8211; $dest_root<br />
                                     $ mkdir &#8211;<br />
                         p&#8211; $dirs<br />
# or without zsh<br />
                             $ find.-<br />
                         type d &#8211; exec env d = &#8220;$dest_root&#8221; sh &#8211; c &#8216; exec mkdir -p &#8212; &#8220;$d/$1&#8243;&#8216; &#8216;{}&#8217; &#8216;{}&#8217; \;<br />
#If `foo = 23&#8221;, then print with 10 digit with leading &#8216;0&#8217;.<br />
  $ foo=23<br />
  $ print ${(r:10::0:)foo}<br />
#find the name of all the files in their home directory that have<br />
#more than 20 characters in their file names<br />
  print -rl $HOME/${(l:20::?:)~:-}*<br />
#Save arrays<br />
  $ print -r &#8212; ${(qq)m} &gt; $nameoffile      # save it<br />
  $ eval &#8220;m=($(cat &#8212; $nameoffile)&#8221;            # or use<br />
  $ m=(&#8220;${(@Q)${(z)&#8221;$(cat &#8212; $nameoffile)&#8221;}}&#8221;) # to restore it<br />
#get a &#8220;ls -l&#8221; on all the files in the tree that are younger than a<br />
#specified age(e.g &#8220;ls -l&#8221; all the files in the tree that where<br />
#modified in the last 2 days)<br />
  $ ls -tld **/*(m-2)<br />
# This will give you a listing 1 file perl line (not à la ls -R).<br />
# Think of an easy way to have a &#8220;ls -R&#8221; style output with<br />
# only files newer than 2 day old.<br />
  $ for d (. ./**/*(/)) {<br />
  &gt;   print -r &#8212; $&#8217;
&#8217;${d}:<br />
  &gt;   cd $d &amp;&amp; {<br />
  &gt;       l=(*(Nm-2))<br />
  &gt;       (($#l)) &amp;&amp; ls -ltd &#8212; $l<br />
  &gt;       cd ~-<br />
  &gt;   }<br />
  &gt; }<br />
#If you also want directories to be included even if their mtime<br />
#is more than 2 days old:<br />
  $ for d (. ./**/*(/)) {<br />
  &gt;   print -r &#8212; $&#8217;
&#8217;${d}:<br />
  &gt;   cd $d &amp;&amp; {<br />
  &gt;      l=(*(N/,m-2))<br />
  &gt;      (($#l)) &amp;&amp; ls -ltd &#8212; $l<br />
  &gt;      cd ~-<br />
  &gt;   }<br />
  &gt; }<br />
#And if you want only the directories with mtime &lt; 2 days to be listed:<br />
  $ for d (. ./**/*(N/m-2)) {<br />
  &gt;   print -r &#8212; $&#8217;
&#8217;${d}:<br />
  &gt;   cd $d &amp;&amp; {<br />
  &gt;      l=(*(Nm-2))<br />
  &gt;      (($#l)) &amp;&amp; ls -ltd &#8212; $l<br />
  &gt;      cd ~-<br />
  &gt;   }<br />
  &gt; }<br />
#print 42 &#8220;-&#8221;<br />
  $ echo ${(l:42::-:)}<br />
# or use &#8220;$COLUMS&#8221;<br />
  $ echo ${(l:$COLUMNS::-:)}<br />
#and now with colors(require autoload colors; colors)<br />
  $ echo &#8220;$bg[red]$fg[black]${(l:42::-:)}&#8221;<br />
#Redirect STDERR to a command like xless without redirecting STDOUT as well.<br />
  $ foo 2&gt;&gt;(xless)<br />
#but this executes the command asynchronously.To do it synchronously:<br />
  $<br />
  {<br />
      {<br />
          foo 1 &gt; &amp;3<br />
      }<br />
      2 &gt; &amp;1 | xless<br />
  } 3&gt;&amp;1<br />
#Rename all MP3 &#8211; Files from name with spaces.mp3 to Name With Spaces.mp3<br />
  $ for i in *.mp3;<br />
  do<br />
  &gt;     mv $i ${${(C)i}:s/Mp3/mp3/}<br />
  &gt; done<br />
#Match file names containing only digits and ending with.xml(require<br />
#* setopt kshglob *)<br />
  $ ls -l [0-9]##.xml<br />
  $ ls -l &lt;0-&gt;.xml<br />
#Remove all &#8220;non txt&#8221; files<br />
  $ rm ./^*.txt<br />
#Move 200 files from a directory into another<br />
  $ mv &#8212; *([1,200]) /another/Dir<br />
#Convert images(foo.gif = &gt; foo.png):<br />
  $ for i in **/*.gif; convert $i $i:r.png<br />
# convert a collection of mp3 files to wave or cdr,<br />
# e.g. file.wav -&gt; file.mp3)<br />
  $ for i (./*.mp3){mpg321 &#8211;w &#8211; $i &gt; ${i:r}.wav}<br />
# Download with LaTeX2HTML  created Files (for example the ZSH-Guide):<br />
  $ for f in http://zsh.sunsite.dk/Guide/zshguide{,{01..08}}.html; do<br />
  &gt;     lynx -source $f &gt;${f:t}<br />
  &gt; done<br />
# Move all files in dir1 and dir2 that have line counts greater than 10 to<br />
# another directory say &#8220;/more10&#8221;<br />
  $ mv dir[12]/**/*.cr(-.e{&#8216;((`wc -l &lt; $REPLY` &gt; 10))&#8217;}) /more10<br />
#Make with dpkg a master &#8211; list of everyfile that it has installed<br />
  $ diff &lt;(find / | sort) &lt;(cat /var/lib/dpkg/info/*.list | sort)<br />
# Replace this fucking Escape-Sequences:<br />
  $ autoload colors ; colors<br />
  $ print &#8220;$bg[cyan]$fg[blue]You are a idiot&#8221; &gt;&gt; /dev/pts/3<br />
# Get ASCII value of a character<br />
  $ char=N ; print $((#char))<br />
# Filename &#8220;Erweiterung&#8221;<br />
# Note: The (N) says to use the nullglob option for this particular<br />
# glob pattern.<br />
  $ for i in *.o(N); do<br />
  &gt;     rm $i<br />
  &gt; done<br />
# Rename files; i. e. FOO to foo and bar to BAR<br />
  $ for i in *(.); mv $i ${i:l} # `FOO&#8217; to `foo&#8217;<br />
  $ for i in *(.); mv $i ${i:u} # `bar to `BAR&#8217;<br />
# Show all suid-files in $PATH<br />
  $ ls -latg ${(s.:.)PATH} | grep &#8216;^&#8230;s&#8217;<br />
# or more complex ;)<br />
  $ print -l ${^path}/*(Ns,S)<br />
# or show only executables with a user given pattern<br />
  $ print -l ${^path}/*vim*(*N)<br />
# gzip files when containing a certain string<br />
  $ gzip ${(ps:
