---
title: "fvwm-menu-headlines(1)"
name: "fvwm-menu-headlines"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fvwm-menu-headlines/"
description: "fvwm-menu-headlines – builds headlines menu definition for fvwm"
---

<h2 class="name">NAME</h2>
<p> fvwm-menu-headlines &#8211; builds headlines menu definition for fvwm </p>
<h2>SYNOPSIS</h2>
<p> <code>fvwm-menu-headlines</code> [ <code>&#8211;help</code>|<code>-h</code>|<code>-?</code> ] [ <code>&#8211;version</code>|<code>-V</code> ] [ <code>&#8211;info</code> [site] ] [ <code>&#8211;site</code>|<code>-s</code> site ] [ <code>&#8211;name</code>|<code>-n</code> name ] [ <code>&#8211;title</code>|<code>-t</code> title ] [ <code>&#8211;item</code> item ] [ <code>&#8211;exec</code>|<code>-e</code> exec-command ] [ <code>&#8211;command</code>|<code>-e</code> fvwm-command ] [ <code>&#8211;icon-title</code> icon ] [ <code>&#8211;icon-item</code> icon ] [ <code>&#8211;icon-home</code> icon ] [ <code>&#8211;icon-error</code> icon ] [ <code>&#8211;wm-icons</code> ] [ <code>&#8211;frontpage</code> [where] ] [ <code>&#8211;proxy</code>|<code>-p</code> host:port ] [ <code>&#8211;file</code> [file] ] [ <code>&#8211;fake</code> [file] ] [ <code>&#8211;timeout</code> seconds ]</p>
<h2>DESCRIPTION</h2>
<p> This configurable perl script builds an fvwm menu definition for headlines of popular news web sites: FreshMeat, Slashdot, LinuxToday, DaemonNews, GNOME-News, KDE-News, RootPrompt, LinuxFr, ThinkGeek, <font SIZE="-1">CNN</font>, <font SIZE="-1">BBC</font> and more. </p>
<p> It is possible to specify a customized menu item format, change a command (usually launching a browser) and add menu icons (there is a support for the wm-icons package).</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;help</code></p>
<dd> show the help and exit</p>
<dt><code>&#8211;version</code></p>
<dd> show the version and exit</p>
<dt><code>&#8211;info</code> [site]</p>
<dd> if site name is given print the site specific info, otherwise print all site names</p>
<dt><code>&#8211;site</code> site</p>
<dd> defile a web site, headlines of which to show, this option also can be used together with &#8211;help to get new defaults. Default site: freshmeat.</p>
<dt><code>&#8211;name</code> name</p>
<dd> define menu name (default is &#8220;MenuHeadlinesFreshmeat&#8221;)</p>
<dt><code>&#8211;title</code> title</p>
<dd> define menu title (default is &#8220;Freshmeat Headlines&#8221;).</p>
<dt><code>&#8211;item</code> label-format</p>
<dd>
<dt><code>&#8211;exec</code> command-format</p>
<dd> define format for menu item or command (what is shown and what is executed when the item is chosen). Default label is &#8216;%h	%[(%Y-%m-%d <tt>%H:</tt>%M)]&#8217;. <font SIZE="-1">TAB</font> can be specified as &#8216;	&#8217;, but in .fvwm2rc you should specify a double backslash or a real <font SIZE="-1">TAB</font>. </p>
<p> Format specifiers for a headline format: </p>
<pre><code>
% h - headline % u - url % d - date in the native format(that site backend supplied) % [strftime - argument - string] - date / time, see strftime(3)
                                                                                                                                             the date
                                                                                                                                         / time is represented according to the local time;
    date and/or time fields that can't be guessed are stripped
    Example: %[|%d %B %Y| %H:%M %S]
      If site supplied only date - this becomes %[|%d %B %Y|],
      if site supplied no date - this becomes an empty string.
  %{name} - site specific named value, like %{comments}
  %(text) - arbitrary text, good for escaping or aligning
</code></pre>
<p> These specifiers can receive an optional integer size, positive for right adjusted string or negative for left adjusted, example: <tt>%8x</tt>; and optional *num or *-num, which means to leave only the first or last (if minus) num of chars, the num must be greater than 3, since the striped part is replaced with &#8220;&#8230;&#8221;, example: %*30x. Both can be combined: %-10*-20x, this instructs to get only the 20 last characters, but if the length is less then 10 &#8211; to fill with up to 10 spaces on the right. </p>
<p> Example: </p>
<pre>
  --exec &quot;iceweasel -remote 'openURL(%u, new-window)' || iceweasel '%u'&quot;
</pre>
<dt><code>&#8211;command</code> command-format</p>
<dd> like <code>&#8211;exec</code> above, but enables to specify any fvwm command, for example, &#8220;Function FuncFvwmShowURL &#8216;%u&#8221;&#8217; not only Exec. </p>
<p> In fact, &#8211;exec=&#8220;mozilla &#8216;%u&#8221;&#8217; is equivalent to &#8211;command=&#8220;Exec mozilla &#8216;%u&#8221;&#8217;</p>
<dt><code>&#8211;icon-title</code> icon</p>
<dd>
<dt><code>&#8211;icon-item</code> icon</p>
<dd>
<dt><code>&#8211;icon-home</code> icon</p>
<dd>
<dt><code>&#8211;icon-error</code> icon</p>
<dd> define menu icon for title, regular item, frontpage item and error item respectively. Default is no menu icons (equivalent to an empty icon argument).</p>
<dt><code>&#8211;wm-icons</code></p>
<dd> define icon names suitable for use with wm-icons package. Currently this is equivalent to: &#8211;icon-title &#8221; &#8211;icon-item menu/information.xpm &#8211;icon-home menu/home.xpm &#8211;icon-error menu/choice-no.xpm.</p>
<dt><code>&#8211;frontpage</code> [where]</p>
<dd> add the site frontpage item to the menu. Optional value can be used to specify where this item will be placed in the menu &#8211; &#8216;top&#8217; or &#8216;t&#8217;, &#8216;bottom&#8217; or &#8216;b&#8217;.</p>
<dt><code>&#8211;proxy</code> host[:port]</p>
<dd> define a proxy to use. Example: &#8211;proxy proxy.inter.net:3128</p>
<dt><code>&#8211;file</code> [file]</p>
<dd> write the menu output to specified file. If no filename is given with this option (or empty filename), the default filename <font SIZE="-1">WORK_HOME/SITE</font>.menu is used. Without this option or with &#8216;-&#8216; filename, the menu output is written to standard output.</p>
<dt><code>&#8211;fake</code> [file]</p>
<dd> don&#8217;t connect to the host using <font SIZE="-1">HTTP</font> protocol, instead, read from <font SIZE="-1">WORK_HOME/SITE</font>.in file. The following reads input from freshmeat.in (downloaded <a rel="nofollow" href="http://freshmeat.net/backend/recentnews.txt)">http://freshmeat.net/backend/recentnews.txt)</a> and saves output to segfault.menu (both files are in <font SIZE="-1">WORK_HOME</font>): fvwm-menu-headlines &#8211;site freshmeat &#8211;fake &#8211;file</p>
<dt><code>&#8211;timeout</code> seconds</p>
<dd> limit a line reading from a socket to this timeout, the default timeout is 20 seconds.</dl>
<p> <font SIZE="-1">WORK_HOME</font> of this script is ~/.fvwm/.fvwm-menu-headlines. It is created if needed. </p>
<p> Option parameters can be specified either using &#8216;=&#8217; or in the next argument. Short options are ok if not ambiguous: <tt>&quot;-h&quot;</tt>, <tt>&quot;-t&quot;</tt>; but be careful with short options, what is now unambiguous, can become ambiguous in the next versions.</p>
<h2>USAGE</h2>
<p> 1. One of the ways to use this script is to define a crontab entry to run the script every hour or so for every monitored site: </p>
<p>0, 30 * ***fvwm &#8211; menu &#8211; headlines&#8211; file&#8211; site freshmeat 1, 31 * ***fvwm &#8211; menu &#8211; headlines&#8211; file&#8211; site linuxtoday 2, 32 * ***fvwm &#8211; menu &#8211; headlines&#8211; file&#8211; site slashdot</p>
<p> Then add these lines to your fvwm configuration file: </p>
<pre>
  DestroyFunc FuncFvwmMenuHeadlines
  AddToFunc   FuncFvwmMenuHeadlines
  + I Read &quot;$HOME/.fvwm/.fvwm-menu-headlines/$0.menu&quot;
  DestroyMenu MenuHeadlines
  AddToMenu   MenuHeadlines &quot;Headlines&quot; Title
  + MissingSubmenuFunction FuncFvwmMenuHeadlines
  + &quot;FreshMeat&quot;  Popup freshmeat
  + &quot;LinuxToday&quot; Popup linuxtoday
  + &quot;Slashdot&quot;   Popup slashdot
</pre>
<p> 2. Another way to use this script (only if you have fast network/proxy) is to run it every time you want to open your Headlines submenus. (Note, the submenu that is once created is not reloaded, use &#8220;Reset all&#8221;.) </p>
<p> In this case your fvwm configuration lines could be: </p>
<pre>
  DestroyFunc FuncFvwmMenuHeadlines
  AddToFunc   FuncFvwmMenuHeadlines
  + I PipeRead &quot;fvwm-menu-headlines --site $0&quot;
  #+ I Schedule 900000 DestroyMenu $0  # reset generated menu in 15 minutes
  DestroyMenu MenuHeadlines
  AddToMenu   MenuHeadlines &quot;Headlines&quot; Title
  + MissingSubmenuFunction FuncFvwmMenuHeadlines
  + &quot;FreshMeat&quot;  Popup freshmeat
  + &quot;Slashdot&quot;   Popup slashdot
  + &quot;LinuxToday&quot; Popup linuxtoday
  + &quot;GNOME News&quot; Popup gnome-news
  + &quot;KDE News&quot;   Popup kde-news
  + &quot;&quot; Nop
  + &quot;Reset all&quot;  FuncResetHeadlines
  DestroyFunc FuncResetHeadlines
  AddToFunc   FuncResetHeadlines
  + I DestroyMenu freshmeat
  + I DestroyMenu linuxtoday
  + I DestroyMenu slashdot
  + I DestroyMenu gnome-news
  + I DestroyMenu kde-news
</pre>
<p> And finally, add &#8220;Popup MenuHeadlines&#8221; somewhere. </p>
<p> 3. Here is a usual usage. Use FvwmConsole or FvwmCommand to run fvwm commands from a shell script. Every time you want headlines from some site, execute (give any additional options if you want): </p>
<pre>
  PipeRead &quot;fvwm-menu-headlines --site newsforge --name MenuHeadlinesNewsForge&quot;
  # this may take several seconds, you may use: BusyCursor Read true
  Popup MenuHeadlinesNewsForge
</pre>
<h2>HOW TO ADD SITE HEADLINES</h2>
<p> It is possible to add user defined site headlines without touching the script itself. Put your perl extensions to the file WORK_HOME/extension.pl. For each site add something similar to: </p>
<pre><code>
$site_info-&gt;{'myslashdot'} = {
    'name' = &gt; "MySlashdot",
    'host' = &gt; "myslashdot.org",
    'path' = &gt; "/myslashdot.xml",
    'func' = &gt; \&amp;process_my_slashdot,
#the following string is only used in-- info
    'flds' = &gt; 'time, title, department, topic, author, url',
};
sub process_my_slashdot()
{
    return process_xml(
        'story',
#mandatory 'h', 'u' and 'd' aliases or undef
        {'h' = &gt; 'title', 'u' = &gt; 'url', 'd' = &gt; 'time'},
        sub($) {
#convert 'd' string to(y, m, d, H, M, S)
                $_[0] = ~ / (\d +) - (\d +) - (\d +)(\d +) : (\d +) : (\d +) /
                ;
            ($1, ($2 || 0) - 1, $3, $4, $5, $6);
        },
        +0, #timezone offset;
        already in UTC);
}
1;
</code></pre>
<h2>AUTHORS</h2>
<p> This script is inspired by WMHeadlines v1.3 by: </p>
<pre>
  Jeff Meininger &lt;jeffm [at] boxybutgood.com&gt;
  (<a rel="nofollow" href="http://rive.boxybutgood.com/WMHeadlines/">http://rive.boxybutgood.com/WMHeadlines/</a>).
</pre>
<p> Reimplemented for fvwm and heavily enhanced by: </p>
<pre>
  Mikhael Goikhman &lt;migo [at] homemail.com&gt;, 16 Dec 1999.
</pre>
<h2>COPYING</h2>
<p> The script is distributed by the same terms as fvwm itself. See <font SIZE="-1">GNU</font> General Public License for details.</p>
<h2>BUGS</h2>
<p> I try to keep all supported site info up to date, but sites often go down, change their backend formats, change their httpd responses, just stop to post news and so on; the script in the latest cvs may be more up to date. </p>
<p> The headline times may be off by one hour or more, since the time is displayed for your local time zone, and the time zone of the original time in the site backend output is often guessed (sometimes incorrectly); similarly it is guessed whether to apply the daylight saving correction. </p>
<p> Report bugs to fvwm-bug [at] fvwm.org. </p>
<h2>Index</h2>
