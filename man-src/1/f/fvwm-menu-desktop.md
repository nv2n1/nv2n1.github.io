---
title: "fvwm-menu-desktop(1)"
name: "fvwm-menu-desktop"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fvwm-menu-desktop/"
description: "fvwm-menu-desktop – Reads XDG menu files and creates Fvwm menus"
---

<h2 class="name">NAME</h2>
<p> fvwm-menu-desktop &#8211; Reads XDG menu files and creates Fvwm menus</p>
<h2>SYNOPSIS</h2>
<p> fvwm-menu-desktop [ <code>&#8211;help</code>|<code>-h</code> ] [ <code>&#8211;version</code>|<code>-v</code> ] [ <code>&#8211;install-prefix</code> <i>DIR</i> ] [ <code>&#8211;desktop</code> <i>NAME</i> ] [ <code>&#8211;menu-type</code> <i>NAME</i> ] [ <code>&#8211;theme</code> <i>NAME</i> ] [ <code>&#8211;with-titles</code>|<code>-w</code> ] [ <code>&#8211;enable-mini-icons</code> ] [ <code>&#8211;size</code>|<code>-s</code> <i>NUM</i> ] [ <code>&#8211;mini-icon-dir</code>|<code>-t</code> <i>DIR</i> ] [ <code>&#8211;title</code>|<code>-t</code> <i>NAME</i> ] [ <code>&#8211;insert-in-menu</code> <i>NAME</i> ] [ <code>&#8211;get-menus</code> <i>all</i>|<i>desktop</i> ] [ <code>&#8211;set-menus</code> <i>menu_paths</i> ] [ <code>&#8211;verbose</code> ] </p>
<h2>DESCRIPTION</h2>
<p> This is a python script which parses XDG menus definitions to build corresponding fvwm menus. </p>
<h2>OPTIONS</h2>
<dl>
<dt>Main Options</p>
<dd>
<dt><code>&#8211;help</code></p>
<dd> Show the help and exit. </p>
<dt><code>&#8211;version</code></p>
<dd> Show the version and exit. </p>
<dt><code>&#8211;install-prefix</code> <i>DIR</i></p>
<dd> Optional parameter to override the standard locations for XDG menu definitions. The standard locations are /etc/xdg/menus (and $HOME/.config/menus if it exists). </p>
<dt><code>&#8211;desktop</code> <i>NAME</i></p>
<dd> Optional parameter to override the <i>NAME</i> of the main desktop environment installed on the system. If a system offers multiple desktop environments $XDG_MENU_PREFIX is typically set and is ignored if &#8211;desktop is denoted. Possible names are: <i>gnome</i>, <i>kde</i>, <i>xfce</i>, <i>lxde</i>, <i>debian</i>, etc. </p>
<dt><code>&#8211;menu-type</code> <i>NAME</i></p>
<dd> Defines which type of menus should be found. Possible <i>NAME</i> types could be: <i>applications</i>, <i>settings</i>, <i>preferences</i>, etc. </p>
<p> Note that if the specified menu type doesn&#8217;t exist the generated menu is empty! </p>
<dt><code>&#8211;theme</code> <i>NAME</i></p>
<dd> Defines the used icon theme. Default is <i>gnome</i> but all others found in /usr/share/icons could be used except the <i>hicolor</i> theme because it&#8217;s the default fallback theme if no icon is found. </p>
<dt><code>&#8211;with-titles</code>|<code>-w</code></p>
<dd> If this option is set menus are generated with titles. Default is no titles. </p>
<dt><code>&#8211;title</code>|<code>-t</code> <i>NAME</i></p>
<dd> Option to define the menu title <i>NAME</i> of the top menu used by Fvwm&#8217;s <code>Popup</code> command. Default is &quot;FvwmMenu&quot;. </p>
<dt><code>&#8211;insert-in-menu</code> <i>NAME</i></p>
<dd> Option to insert generated menu(s) <code>IN</code> a menu <i>NAME</i> (its top title). </p>
<p> Note that this option does not work correctly with the Regnerate Menus menu entry in a normal built menu since items inserted into such a menu cannot be removed (currently). If you use this option there and want to update your menus, you have to restart fvwm. A better way is to use dynamic menus (see the example in the USAGE section). </p>
<dt><code>&#8211;get-menus</code> <i>all</i>|<i>desktop</i></p>
<dd> Prints a space separated list of full menu paths. <i>all</i> is all menus on the system except empty ones. <i>desktop</i> is desktop related menus. No menu generation is done. </p>
<p> This option is meant for use with the configuration tool. </p>
<dt><code>&#8211;set-menus</code> <i>menu_paths</i></p>
<dd> Expects a space separated list of full menu paths to generate user specified menus </p>
<p> This option is meant for use with the configuration tool. </p>
<dt><code>&#8211;verbose</code></p>
<dd> Enables additional information printouts on STDERR. </p>
<dt>Icons Options</p>
<dd>
<p> By default, fvwm-menu-desktop builds menus without mini-icons. To enable mini-icons use: </p>
<dt><code>&#8211;enable-mini-icons</code></p>
<dd> This option enables mini-icons in the menus. If set, 24&#215;24 mini-icons are used. If the specified icon isn&#8217;t that size it will be converted if <code>ImageMagick</code> is installed and saved in $HOME/.fvwm/icons or to the directory specified with &#8211;mini-icon-dir option. Otherwise no icon appears in the menu for that entry. With most distributions, all the menu entries will have mini-icons appropriate to the application. </p>
<dt><code>&#8211;size</code>|<code>-s</code> <i>NUM</i></p>
<dd> If &#8211;enable-mini-icons is used the <i>size</i> of the icons can changed with this parameter. Default is 24. </p>
<dt><code>&#8211;mini-icon-dir</code> <i>DIR</i></p>
<dd> When the right size mini-icon isn&#8217;t available, fvwm-menu-desktop creates icons with the right size in $HOME/.fvwm/icons. If you don&#8217;t want to use the default directory, $HOME/.fvwm/icons, use this option to specify a different folder. </p>
</dl>
<h2>USAGE</h2>
<p> Without any parameters <code>fvwm-menu-desktop</code> creates a menu named &quot;FvwmMenu&quot; with sub menus found for the main desktop environment installed on the system. </p>
<p> To add the default generated menu to the &quot;Root&quot; menu add the following to your fvwm config file (~/.fvwm/config or ~/.fvwm/.fvwm2rc). This generates the menu each time you pop it up: </p>
<dl>
<dt>
<dd>
<pre>
AddToMenu MenuRoot &quot;XDG Menus&quot; Popup FvwmMenu
PipeRead 'fvwm-menu-desktop'
</pre>
</dl>
<p> This is likely to be too slow and is not recommended. </p>
<p> Another possibility is to use <code>DynamicPopupAction</code>, the menu will be built only if you pop up the menu. The following creates a &quot;KDE Menus&quot; menu which contains all Kde menus found on the system which is built only the first time you pop it up: </p>
<dl>
<dt>
<dd>
<pre><code>
AddToMenu MenuRoot "KDE Menus" Popup FvwmKde... AddToMenu FvwmKde + DynamicPopupAction PipeRead 'fvwm-menu-desktop --desktop kde \
                                                 --title FvwmKde \
                                                 --enable-mini-icons \
                                                 [other options]'
</code></pre>
</dl>
<p> The example above generates a menu with the Xdg menus as sub menus. If the sub menus should appear one level higher do this: </p>
<dl>
<dt>
<dd>
<pre>
AddToMenu MenuRoot &quot;Root Menu&quot; Title
+ PipeRead 'fvwm-menu-desktop --insert-in-menu MenuRoot'
</pre>
</dl>
<p> To generate single menus like <i>preferences</i>: </p>
<dl>
<dt>
<dd>
<p>fvwm &#8211; menu &#8211; desktop&#8211; desktop kde&#8211; menu &#8211; type preferences&#8211; title FvwmPref&#8211; enable &#8211; mini &#8211; icons &#8211; size 16 &#8211;with &#8211; titles</p>
</dl>
<p> This generates a single KDE Preferences menu with top title &quot;FvwmPref&quot;, mini icons with a size of 16&#215;16 pixels and titles for each sub menu. But only if a menu with the name <i>preferences</i> exists in the users or system wide Xdg directories. Else it&#8217;s empty! </p>
<p> To add the generated menu to the &quot;Utilities&quot; menu for example put the following to your fvwm config file (~/.fvwm/config or ~/.fvwm/.fvwm2rc): </p>
<dl>
<dt>
<dd>
<p>AddToMenu Utilities &#8220;Preferences Menu&#8221; Popup FvwmPref<br />
    PipeRead &#8216;fvwm-menu-desktop &#8211;desktop kde &#8211;menu-type preferences \<br />
                            &#8211;title FvwmPref [other options]&#8217;</p>
</dl>
<p> If you think that <code>fvwm-menu-desktop</code> slows down your menu startup too much do not use <code>PipeRead</code>. Instead run <code>fvwm-menu-desktop</code> and redirect the menu to a file and read that file in your .fvwm2rc file. </p>
<dl>
<dt>
<dd>
<p>AddToMenu MenuRoot &#8220;XDG Menus&#8221; Popup FvwmMenu&#8230; AddToMenu FvwmMenu + DynamicPopupAction Function FuncRecreateXdgMenus&#8230; DestroyFunc FuncRecreateXdgMenus AddToFunc FuncRecreateXdgMenus + I Test(f $[FVWM_USERDIR] /.menu) Read $[FVWM_USERDIR] /.menu<br />
    + I TestRC(!Match) PipeRead &#8216;fvwm-menu-desktop &gt; $[FVWM_USERDIR]/.menu \<br />
                              &amp;&amp;  echo &#8220;Read $[FVWM_USERDIR]/.menu&#8221;&#8216;</p>
</dl>
<p> or if you want to show the menus directly in a normal &quot;Root&quot; menu use this: </p>
<dl>
<dt>
<dd>
<p>AddToMenu MenuRoot &#8220;Root Menu&#8221; Title + FuncXdgMenusInRoot&#8230; DestroyFunc FuncXdgMenusInRoot AddToFunc FuncXdgMenusInRoot + I Test(f $[FVWM_USERDIR] /.menu) Read $[FVWM_USERDIR] /.menu<br />
    + I TestRC(!Match) PipeRead &#8216;fvwm-menu-desktop &#8211;insert-in-menu MenuRoot \<br />
                              &gt; $[FVWM_USERDIR]/.menu \<br />
                              &amp;&amp; echo &#8220;Read $[FVWM_USERDIR]/.menu&#8221;&#8216;</p>
</dl>
<p> The problem here is, that you have to restart fvwm because items insserted into such a menu cannot be removed. For that BOTH menus must be regenerated: </p>
<dl>
<dt>
<dd>
<pre><code>
AddToMenu MenuRoot DynamicPopupAction FuncMenuRoot
        DestroyFunc FuncMenuRoot
            AddToFunc FuncMenuRoot +
    I DestroyMenu MenuRoot + I AddToMenu MenuRoot DynamicPopupAction FuncMenuRoot + I AddToMenu MenuRoot "Root Menu" Title + I Popup XdgMenus AddToMenu XdgMenus DynamicPopupAction FuncXdgMenusInRoot DestroyFunc FuncXdgMenusInRoot AddToFunc FuncXdgMenusInRoot + I AddToMenu XdgMenus DynamicPopupAction FuncXdgMenusInRoot + I Test(f $[FVWM_USERDIR] /.menu) Read $[FVWM_USERDIR] /.menu
    + I TestRC(!Match) PipeRead 'fvwm-menu-desktop --insert-in-menu MenuRoot \
                              &gt; $[FVWM_USERDIR]/.menu \
                              &amp;&amp; echo "Read $[FVWM_USERDIR]/.menu"'
</code></pre>
</dl>
<h2>GUI</h2>
<p> There&#8217;s a <code>FvwmForm</code> GUI to setup the menu generation manually. It is found in the root of the generated menu called &quot;Regenerate XDG Menu(s)&quot;. </p>
<p> Or it can be started from within <code>FvwmConsole</code> with </p>
<dl>
<dt>
<dd>
<pre>
Module FvwmPerl -l fvwm-menu-desktop-config.fpl
</pre>
</dl>
<h2>BUGS</h2>
<p> The whole process of creating menus from files is slow. Otherwise report bugs to the fvwm-workers mailing list &lt;fvwm-workers [at] fvwm.org&gt;. </p>
<h2>AUTHORS</h2>
<p> This script is based on fvwm-xdg-menu.py written by Piotr Zielinski (<a rel="nofollow" href="http://www.cl.cam.ac.uk/~pz215/)">http://www.cl.cam.ac.uk/~pz215/)</a> who assigned Licence: GPL 2 Date: 03.12.2005. </p>
<p> The script was reworked to replace the existing fvwm-menu-desktop perl script by the fvwm-workers. </p>
<h2>COPYING</h2>
<p> The script is distributed by the same terms as fvwm itself. See GNU General Public License for details. </p>
<h2>Index</h2>
