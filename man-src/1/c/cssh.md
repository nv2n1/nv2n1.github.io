---
title: "cssh(1)"
name: "cssh"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cssh/"
description: "cssh, crsh, ctel, ccon – Cluster administration tool"
---

<h2 class="name">NAME</h2>
<p> cssh, crsh, ctel, ccon &#8211; Cluster administration tool </p>
<h2>SYNOPSIS</h2>
<p> cssh&nbsp;<wbr>[options]&nbsp;<wbr>[[user@]&lt;server&gt;[:port]|&lt;tag&gt;]&nbsp;<wbr>[&#8230;] crsh&nbsp;<wbr>[options]&nbsp;<wbr>[[user@]&lt;server&gt;[:port]|&lt;tag&gt;]&nbsp;<wbr>[&#8230;] ctel&nbsp;<wbr>[options]&nbsp;<wbr>[&lt;server&gt;[:port]|&lt;tag&gt;]&nbsp;<wbr>[&#8230;] ccon&nbsp;<wbr>[options]&nbsp;<wbr>[[user@]&lt;server&gt;[:port]|&lt;tag&gt;]&nbsp;<wbr>[&#8230;]</p>
<h2>DESCRIPTION</h2>
<p> The command opens an administration console and an xterm to all specified hosts. Any text typed into the administration console is replicated to all windows. All windows may also be typed into directly. </p>
<p> This tool is intended for (but not limited to) cluster administration where the same configuration or commands must be run on each node within the cluster. Performing these commands all at once via this tool ensures all nodes are kept in sync. </p>
<p> Connections are opened via ssh so a correctly installed and configured ssh installation is required. If, however, the program is called by &#8220;crsh&#8221; then the rsh protocol is used (and the communications channel is insecure), or by &#8220;ctel&#8221; then telnet is used, or by &#8220;ccon&#8221; then console is used. </p>
<p> Extra caution should be taken when editing system files such as /etc/inet/hosts as lines may not necessarily be in the same order. Assuming line 5 is the same across all servers and modifying that is dangerous. Better to search for the specific line to be changed and double-check before changes are committed.</p>
<h3>Further Notes</h3>
<p> Please also see &#8220;<font SIZE="-1">KNOWN BUGS&#8221;</font>.</p>
<dl>
<dt>&bull;</p>
<dd> The dotted line on any sub-menu is a tear-off, i.e. click on it and the sub-menu is turned into its own window.</p>
<dt>&bull;</p>
<dd> Unchecking a hostname on the Hosts sub-menu will unplug the host from the cluster control window, so any text typed into the console is not sent to that host. Re-selecting it will plug it back in.</p>
<dt>&bull;</p>
<dd> If your window manager menu bars are obscured by terminal windows see the <tt>&quot;screen_reserve_XXXXX&quot;</tt> options in the <i></i>$HOME<i>/.clusterssh/config</i> file (see &#8220;<font SIZE="-1">FILES&#8221;</font>).</p>
<dt>&bull;</p>
<dd> If the terminals overlap too much see the <tt>&quot;terminal_reserve_XXXXX&quot;</tt> options in the <i></i>$HOME<i>/.clusterssh/config</i> file (see &#8220;<font SIZE="-1">FILES&#8221;</font>).</p>
<dt>&bull;</p>
<dd> If the code is called as crsh instead of cssh (i.e. a symlink called crsh points to the cssh file or the file is renamed) rsh is used as the communications protocol instead of ssh.</p>
<dt>&bull;</p>
<dd> If the code is called as ctel instead of cssh (i.e. a symlink called ctel points to the cssh file or the file is renamed) telnet is used as the communications protocol instead of ssh.</p>
<dt>&bull;</p>
<dd> If the code is called as ccon instead of cssh (i.e. a symlink called ccon points to the cssh file or the file is renamed) console is used as the communications protocol instead of ssh.</p>
<dt>&bull;</p>
<dd> When using cssh on a large number of systems to connect back to a single system (e.g. you issue a command to the cluster to scp a file from a given location) and when these connections require authentication (i.e. you are going to authenticate with a password), the sshd daemon at that location may refuse connects after the number specified by MaxStartups in sshd_config is exceeded. (If this value is not set, it defaults to 10.) This is expected behavior; sshd uses this mechanism to prevent DoS attacks from unauthenticated sources. Please tune sshd_config and reload the <font SIZE="-1">SSH</font> daemon, or consider using the ~/.ssh/authorized_keys mechanism for authentication if you encounter this problem.</p>
<dt>&bull;</p>
<dd> If client windows fail to open, try running: </p>
<p> <tt>&quot;cssh -e {single host name}&quot;</tt> </p>
<p> This will test the mechanisms used to open windows to hosts. This could be due to either the <tt>&quot;-xrm&quot;</tt> terminal option which enables <tt>&quot;AllowSendEvents&quot;</tt> (some terminal do not require this option, other terminals have another method for enabling it &#8211; see your terminal documention) or the <tt>&quot;ConnectTimeout&quot;</tt> ssh option (see the configuration option <tt>&quot;-o&quot;</tt> or file <tt>&quot;$HOME/.clusterssh/config&quot;</tt> below to resolve this).</dl>
<h2>OPTIONS</h2>
<p> Some of these options may also be defined within the configuration file. Default options are shown as appropriate.</p>
<dl>
<dt>&#8211;action,-a &#8216;&lt;command&gt;&#8217;</p>
<dd> Run the command in each session, i.e. <tt>&quot;-a 'vi /etc/hosts'&quot;</tt> to drop straight into a vi session. <font SIZE="-1">NOTE:</font> not all communications methods support this (ssh and rsh should, telnet and console will not).</p>
<dt>&#8211;autoclose,-A &lt;seconds&gt;</p>
<dd> Number of seconds to wait before closing finished terminal windows.</p>
<dt>&#8211;autoquit,-q|&#8211;no-autoquit,-Q</p>
<dd> Enable|Disable automatically quiting after the last client window has closed (overriding the config file)</p>
<dt>&#8211;cluster-file,-c &lt;file&gt;</p>
<dd> Use supplied file as additional cluster file (see also &#8220;<font SIZE="-1">FILES&#8221;</font>)</p>
<dt>&#8211;config-file,-C &lt;file&gt;</p>
<dd> Use supplied file as additional configuration file (see also &#8220;<font SIZE="-1">FILES&#8221;</font>)</p>
<dt>-d</p>
<dd> <font SIZE="-1">DEPRECATED. </font> See &#8216;&#8211;debug&#8217;.</p>
<dt>-D</p>
<dd> <font SIZE="-1">DEPRECATED. </font> See &#8216;&#8211;debug&#8217;.</p>
<dt>&#8211;debug [number].</p>
<dd> Enable debugging. Either a level can be provided or the option can be repeated multiple times. Maximum level is 4.</p>
<dt>&#8211;evaluate,-e [user@]&lt;hostname&gt;[:port]</p>
<dd> Display and evaluate the terminal and connection arguments so display any potential errors. The &lt;hostname&gt; is required to aid the evaluation.</p>
<dt>&#8211;font,-f &quot;5&#215;8&quot;</p>
<dd> Specify the font to use in the terminal windows. Use standard X font notation.</p>
<dt>&#8211;help,-h|-?</p>
<dd> Show basic help text, and exit</p>
<dt>&#8211;list, -L</p>
<dd> List available cluster tags.</p>
<dt>&#8211;man,-H</p>
<dd> Show full help test (the man page), and exit</p>
<dt>&#8211;master,-M &lt;master&gt;</p>
<dd> The console client program polls master as the primary server, rather than the default set at compile time (typically &#8220;console&#8221;).</p>
<dt>&#8211;options,-o &quot;-x -o ConnectTimeout=10&quot; &#8211; for ssh connections</p>
<dd>
<dt>&#8211;options,-o &quot;&quot; &#8211; for rsh connections</p>
<dd> Specify arguments to be passed to ssh or rsh when making the connection. </p>
<p> <font SIZE="-1"><code>NOTE:</code></font> any &#8220;generic&#8221; change to the method (i.e. specifying the ssh port to use) should be done in the medium&#8217;s own config file (see <tt>&quot;ssh_config&quot;</tt> and <i></i>$HOME<i>/.ssh/config</i>).</p>
<dt>&#8211;output-config,-u</p>
<dd> Output the current configuration in the same format used by the <i></i>$HOME<i>/.clusterssh/config</i> file.</p>
<dt>&#8211;port,-p &lt;port&gt;</p>
<dd> Specify an alternate port for connections.</p>
<dt>&#8211;show-history,-s</p>
<dd> <font SIZE="-1">IN BETA:</font> Show history within console window. This code is still being worked upon, but may help some users.</p>
<dt>&#8211;tag-file,-r &lt;file&gt;</p>
<dd> Use supplied file as additional tag file (see also &#8220;<font SIZE="-1">FILES&#8221;</font>)</p>
<dt>&#8211;term-args,-t &quot;&quot;</p>
<dd> Specify arguments to be passed to terminals being used</p>
<dt>&#8211;tile,-g|&#8211;no-tile,-G</p>
<dd> Enable|Disable window tiling (overriding the config file)</p>
<dt>&#8211;title,-T &quot;<font SIZE="-1">CSSH&quot;</font></p>
<dd> Specify the initial part of the title used in the console and client windows</p>
<dt>&#8211;unique-servers,-m</p>
<dd> Connect to each host only once</p>
<dt>&#8211;use_all_a_records,-A</p>
<dd> If a hostname resolves to multiple <font SIZE="-1">IP</font> addresses, toggle whether or not to connect to all of them, or just the first one (see also config file entry)</p>
<dt>&#8211;username,-l $LOGNAME</p>
<dd> Specify the default username to use for connections (if different from the currently logged in user). <font SIZE="-1"><code>NOTE:</code></font> will be overridden by &lt;user&gt;@&lt;host&gt;</p>
<dt>&#8211;version,-v</p>
<dd> Show version information and exit</dl>
<h2>ARGUMENTS</h2>
<p> The following arguments are support:</p>
<dl>
<dt>[user@]&lt;hostname&gt;[:port] &#8230;</p>
<dd> Open an xterm to the given hostname and connect to the administration console. An optional port number can be used if sshd is not listening on standard port (e.g not listening on port 22) and ssh_config cannot be used.</p>
<dt>&lt;tag&gt; &#8230;</p>
<dd> Open a series of xterms defined by &lt;tag&gt; in one of the suplimentary configuration files (see &#8220;<font SIZE="-1">FILES&#8221;</font>). </p>
<p> Note: specifying a username on a cluster tag will override any usernames defined in the cluster</dl>
<h2>KEY SHORTCUTS</h2>
<p> The following key shortcuts are available within the console window, and all of them may be changed via the configuration files.</p>
<dl>
<dt>Control-q</p>
<dd> Quit the program and close all connections and windows</p>
<dt>Control-+</p>
<dd> Open the &#8216;Add Host(s) or Cluster(s)&#8217; dialogue box. Mutiple host or cluster names can be entered, separated by spaces.</p>
<dt>Alt-n</p>
<dd> Paste in the hostname part of the specific connection string to each client, minus any username or port, i.e. </p>
<p> <tt>&quot;scp /etc/hosts server:files/&lt;Alt-n&gt;.hosts&quot;</tt> </p>
<p> would replace the &lt;Alt-n&gt; with the client&#8217;s name in each window</p>
<dt>Alt-r</p>
<dd> Retile all the client windows</dl>
<h2>EXAMPLES</h2>
<dl>
<dt>Open up a session to 3 servers</p>
<dd> $&nbsp;<wbr>cssh server1 server2 server3</p>
<dt>Open up a session to a cluster of servers identified by the tag &#8216;farm1&#8217; and give the controlling window a specific title, where the cluster is defined in one of the default configuration files</p>
<dd> $&nbsp;<wbr>cssh -T&nbsp;<wbr>&#8216;Web Farm Cluster 1&#8217;&nbsp;<wbr>farm1</p>
<dt>Connect to different servers using different login names. <font SIZE="-1">NOTE:</font> this can also be achieved by setting up appropriate options in the <i>.ssh/config</i> file. Do not close cssh when last terminal exits.</p>
<dd> $&nbsp;<wbr>cssh -Q user1 [at] server1 admin [at] server2</p>
<dt>Open up a cluster defined in a non-default configuration file</p>
<dd> $&nbsp;<wbr>cssh -c&nbsp;<wbr><tt>$HOME</tt>/cssh.config db_cluster</p>
<dt>Use telnet on port 2022 instead of ssh</p>
<dd> $&nbsp;<wbr>ctel -p 2022 server1 server2</p>
<dt>Use rsh instead of ssh</p>
<dd> $&nbsp;<wbr>crsh server1 server2</p>
<dt>Use console with master as the primary server instead of ssh</p>
<dd> $&nbsp;<wbr>ccon -M master server1 server2</dl>
<h2>FILES</h2>
<dl>
<dt><i>/etc/clusters</i>, <i>$HOME/.clusterssh/clusters</i></p>
<dd> These files contain a list of tags to server names mappings. When any name is used on the command line it is checked to see if it is a tag. If it is a tag, then the tag is replaced with the list of servers. The formated is as follows: </p>
<p> &lt;tag&gt;&nbsp;<wbr>[user@]&lt;server&gt;&nbsp;<wbr>[user@]&lt;server&gt;&nbsp;<wbr>[&#8230;] </p>
<pre><code>
i.e.
#List of servers in live
    live admin1[at] server1 admin2[at] server2 server3 server4
</code></pre>
<p> All comments (marked by a #) and blank lines are ignored. Tags may be nested, but be aware of using recursive tags as they are not checked for. </p>
<p> Extra cluster files may also be specified either as an option on the command line (see <tt>&quot;cluster-file&quot;</tt>) or in the users <i></i>$HOME<i>/.clusterssh/config</i> file (see <tt>&quot;extra_cluster_file&quot;</tt> configuration option). </p>
<p> <font SIZE="-1">NOTE:</font> the last tag read overwrites any pre-existing tag of that name </p>
<p> <font SIZE="-1">NOTE:</font> there is a special cluster tag called <tt>&quot;default&quot;</tt> &#8211; any tags or hosts included within this tag will be automatically opened if no other tags are specified on the command line.</p>
<dt><i>/etc/tags</i>, <i>$HOME/.clusterssh/tags</i></p>
<dd> Very similar to <i>cluster</i> files but the definition is reversed. The format is: </p>
<p> &lt;host&gt;&nbsp;<wbr>&lt;tag&gt;&nbsp;<wbr>[&#8230;] </p>
<p> This allows one host to be specified as a member of a number of tags. This format can be clearer than using <i>clusters</i> files. </p>
<p> Extra tag files may be spcieid either an an option (see <tt>&quot;tag-file&quot;</tt>) or within the users <i></i>$HOME<i>/.clusterssh/config</i> file (see <tt>&quot;extra_tag_file&quot;</tt> configuration option). </p>
<p> <font SIZE="-1">NOTE:</font> All tags are added together</p>
<dt><i>/etc/csshrc</i> &amp; <i>$HOME/.clusterssh/config</i></p>
<dd> This file contains configuration overrides &#8211; the defaults are as marked. Default options are overwritten first by the global file, and then by the user file. </p>
<p> <font SIZE="-1"><code>NOTE:</code></font> values for entries do not need to be quoted unless it is required for passing arguments, i.e. </p>
<pre>
  terminal_allow_send_events=&quot;-xrm '*.VT100.allowSendEvents:true'&quot;
</pre>
<p> should be written as </p>
<pre>
  terminal_allow_send_events=-xrm '*.VT100.allowSendEvents:true'
</pre>
<dl>
<dt>
<dd>
<dl>
<dt>auto_close = 5</p>
<dd> Close terminal window after this many seconds. If set to 0 will instead wait on input from the user in each window before closing. Can be overridden by <tt>&quot;-K&quot;</tt> on the command line</p>
<dt>auto_quit = yes</p>
<dd> Automatically quit after the last client window closes. Set to anything other than &#8220;yes&#8221; to disable. Can be overridden by <tt>&quot;-Q&quot;</tt> on the command line.</p>
<dt>clusters = &lt;blank&gt;</p>
<dd> Define a number of cluster tags in addition to (or to replace) tags defined in the <i>/etc/clusters</i> file. The format is: </p>
<pre><code>
clusters = &lt;tag1&gt;&lt;tag2&gt;&lt;tag3&gt;
    &lt;tag1&gt; = host1 host2 host3&lt;tag2&gt; = user[at] host4 user[at] host5 host6&lt;tag3&gt; = &lt;tag1&gt;&lt;tag2&gt;
</code></pre>
<p> As with the <i>/etc/clusters</i> file, be sure not to create recursivly nested tags.</p>
<dt>comms = ssh</p>
<dd> Sets the default communication method (initially taken from the name of program, but can be overridden here).</p>
<dt>console_position = &lt;null&gt;</p>
<dd> Set the initial position of the console &#8211; if empty then let the window manager decide. Format is &#8216;+&lt;x&gt;+&lt;y&gt;&#8217;, i.e. &#8216;+0+0&#8217; is top left hand corner of the screen, &#8216;+0-70&#8217; is bottom left hand side of screen (more or less).</p>
<dt>external_cluster_command = &lt;null&gt;</p>
<dd> Define the full path to an external command that can be used to resolve tags to host names. This command can be written in any language. The script must accept a list of tags to resolve and output a list of hosts on a single line. Any tags that cannot be resolved should be returned unchanged. </p>
<p> A non-0 exit code will be counted as an error, a warning will be printed and output ignored.</p>
<dt>extra_cluster_file = &lt;null&gt;</p>
<dd> Define an extra cluster file in the format of <i>/etc/clusters</i>. Multiple files can be specified, seperated by commas. Both ~ and <tt>$HOME</tt> are acceptable as a to reference the users home directory, i.e. </p>
<pre>
 extra_cluster_file = ~/clusters, $HOME/clus
</pre>
<dt>ignore_host_errors</p>
<dd> <font SIZE="-1">THIS OPTION IS DEPRECATED. </font> It has been left in so current systems continue to function as expected.</p>
<dt>key_addhost = Control-Shift-plus</p>
<dd> Default key sequence to open AddHost menu. See below notes on shortcuts.</p>
<dt>key_clientname = Alt-n</p>
<dd> Default key sequence to send cssh client names to client. See below notes on shortcuts.</p>
<dt>key_localname = Alt-l</p>
<dd> Default key sequence to send hostname of local server to client. See below notes on shortcuts.</p>
<dt>key_paste = Control-v</p>
<dd> Default key sequence to paste text into the console window. See below notes on shortcuts.</p>
<dt>key_quit = Control-q</p>
<dd> Default key sequence to quit the program (will terminate all open windows). See below notes on shortcuts.</p>
<dt>key_retilehosts = Alt-r</p>
<dd> Default key sequence to retile host windows. See below notes on shortcuts.</p>
<dt>key_username = Alt-u</p>
<dd> Default key sequence to send username to client. See below notes on shortcuts.</p>
<dt>macro_servername = %s</p>
<dd>
<dt>macro_hostname = %h</p>
<dd>
<dt>macro_username = %u</p>
<dd>
<dt>macro_newline = %n</p>
<dd>
<dt>macro_version = %v</p>
<dd> Change the replacement macro used when either using a &#8216;Send&#8217; menu item, or when pasting text into the main console.</p>
<dt>macros_enabled = yes</p>
<dd> Enable or disable macro replacement. Note: this affects pasting into the main console, items on the &#8216;Send&#8217; menu and key_clientname, key_localname, key_servername and key_username.</p>
<dt>max_addhost_menu_cluster_items = 6</p>
<dd> Maximum number of entries in the &#8216;Add Host&#8217; menu cluster list before scrollbars are used</p>
<dt>max_host_menu_items = 30</p>
<dd> Maximum number of hosts to put into the host menu before starting a new column</p>
<dt>menu_host_autotearoff = 0</p>
<dd>
<dt>menu_send_autotearoff = 0</p>
<dd> When set to non-0 will automatically tear-off the host or send menu at program start</p>
<dt>mouse_paste = Button-2 (middle mouse button)</p>
<dd> Default key sequence to paste text into the console window using the mouse. See below notes on shortcuts.</p>
<dt>rsh = rsh</p>
<dd>
<dt>ssh = ssh</p>
<dd>
<dt>telnet = telnet</p>
<dd> Set the path to the specific binary to use for the communication method, else uses the first match found in <tt>$PATH</tt></p>
<dt>rsh_args = &lt;blank&gt;</p>
<dd>
<dt>ssh_args = &quot;-x -o ConnectTimeout=10&quot;</p>
<dd>
<dt>telnet_args = &lt;blank&gt;</p>
<dd> Sets any arguments to be used with the communication method (defaults to ssh arguments). </p>
<p> <font SIZE="-1"><code>NOTE:</code></font> The given defaults are based on OpenSSH, not commercial ssh software. </p>
<p> <font SIZE="-1"><code>NOTE:</code></font> Any &#8220;generic&#8221; change to the method (i.e. specifying the ssh port to use) should be done in the medium&#8217;s own config file (see <tt>&quot;ssh_config&quot;</tt> and <i></i>$HOME<i>/.ssh/config</i>).</p>
<dt>screen_reserve_top = 0</p>
<dd>
<dt>screen_reserve_bottom = 60</p>
<dd>
<dt>screen_reserve_left = 0</p>
<dd>
<dt>screen_reserve_right = 0</p>
<dd> Number of pixels from the screen side to reserve when calculating screen geometry for tiling. Setting this to something like 50 will help keep cssh from positioning windows over your window manager&#8217;s menu bar if it draws one at that side of the screen.</p>
<dt>rsh = /path/to/rsh</p>
<dd>
<dt>ssh = /path/to/ssh</p>
<dd> Depending on the value of comms, set the path of the communication binary.</p>
<dt>terminal = /path/to/terminal</p>
<dd> Path to the x-windows terminal used for the client.</p>
<dt>terminal_args = &lt;blank&gt;</p>
<dd> Arguments to use when opening terminal windows. Otherwise takes defaults from <i></i>$HOME<i>/.Xdefaults</i> or $&lt;$HOME/.Xresources&gt; file.</p>
<dt>terminal_font = 6&#215;13</p>
<dd> Font to use in the terminal windows. Use standard X font notation.</p>
<dt>terminal_reserve_top = 5</p>
<dd>
<dt>terminal_reserve_bottom = 0</p>
<dd>
<dt>terminal_reserve_left = 5</p>
<dd>
<dt>terminal_reserve_right = 0</p>
<dd> Number of pixels from the terminal side to reserve when calculating screen geometry for tiling. Setting these will help keep cssh from positioning windows over your scroll and title bars or otherwise overlapping the windows too much.</p>
<dt>terminal_colorize = 1</p>
<dd> If set to 1 (the default), then &#8220;-bg&#8221; and &#8220;-fg&#8221; arguments will be added to the terminal invocation command-line. The terminal will be colored in a pseudo-random way based on the host name; while the color of a terminal is not easily predicted, it will always be the same color for a given host name. After a while, you will recognize hosts by their characteristic terminal color.</p>
<dt>terminal_bg_style = dark</p>
<dd> If set to dark, the the terminal background will be set to black and the foreground to the pseudo-random color. If set to light, then the foreground will be black and the background the pseudo-random color. If terminal_colorize is zero, then this option has no effect.</p>
<dt>terminal_size = 80&#215;24</p>
<dd> Initial size of terminals to use (note: the number of lines (24) will be decreased when resizing terminals for tiling, not the number of characters (80))</p>
<dt>terminal_title_opt = -T</p>
<dd> Option used with <tt>&quot;terminal&quot;</tt> to set the title of the window</p>
<dt>terminal_allow_send_events = -xrm &#8216;*.VT100.allowSendEvents:true&#8217;</p>
<dd> Option required by the terminal to allow XSendEvents to be received</p>
<dt>title = cssh</p>
<dd> Title of windows to use for both the console and terminals.</p>
<dt>unmap_on_redraw = no</p>
<dd> Tell Tk to use the UnmapWindow request before redrawing terminal windows. This defaults to &#8220;no&#8221; as it causes some problems with the <font SIZE="-1">FVWM</font> window manager. If you are experiencing problems with redraws, you can set it to &#8220;yes&#8221; to allow the window to be unmapped before it is repositioned.</p>
<dt>use_all_a_records = no</p>
<dd> If a hostname resolves to multiple <font SIZE="-1">IP</font> addresses, set to <tt>&quot;yes&quot;</tt> to connect to all of them, not just the first one found.</p>
<dt>use_hotkeys = yes</p>
<dd> Setting to anything other than <tt>&quot;yes&quot;</tt> will disable all hotkeys.</p>
<dt>user = $LOGNAME</p>
<dd> Sets the default user for running commands on clients.</p>
<dt>window_tiling = yes</p>
<dd> Perform window tiling (set to <tt>&quot;no&quot;</tt> to disable)</p>
<dt>window_tiling_direction = right</p>
<dd> Direction to tile windows, where &#8220;right&#8221; means starting top left and moving right and then down, and anything else means starting bottom right and moving left and then up</dl>
</dl>
<dl>
<dt>
<dd>
<p> <font SIZE="-1"><code>NOTE:</code></font> The key shortcut modifiers must be in the form &#8220;Control&#8221;, &#8220;Alt&#8221;, or &#8220;Shift&#8221;, i.e. with the first letter capitalised and the rest lower case. Keys may also be disabled individually by setting to the word &#8220;null&#8221;.</dl>
<dt><i>$HOME/.csshrc_send_menu</i></p>
<dd> This (optional) file contains items to populate the send menu. The default entry could be written as: </p>
<pre>
  &lt;send_menu&gt;
    &lt;menu title=&quot;Use Macros&quot;&gt;
        &lt;toggle/&gt;
        &lt;accelerator&gt;ALT-p&lt;/accelerator&gt;
    &lt;/dmenu&gt;
    &lt;menu title=&quot;Remote Hostname&quot;&gt;
        &lt;command&gt;%s&lt;/command&gt;
        &lt;accelerator&gt;ALT-n&lt;/accelerator&gt;
    &lt;/menu&gt;
    &lt;menu title=&quot;Local Hostname&quot;&gt;
        &lt;command&gt;%s&lt;/command&gt;
        &lt;accelerator&gt;ALT-l&lt;/accelerator&gt;
    &lt;/menu&gt;
    &lt;menu title=&quot;Username&quot;&gt;
        &lt;command&gt;%u&lt;/command&gt;
        &lt;accelerator&gt;ALT-u&lt;/accelerator&gt;
    &lt;/menu&gt;
    &lt;menu title=&quot;Test Text&quot;&gt;
        &lt;command&gt;echo &quot;ClusterSSH Version: %v%n&lt;/command&gt;
    &lt;/menu&gt;
  &lt;/send_menu&gt;
</pre>
<p> Submenus can also be specified as follows: </p>
<pre>
  &lt;send_menu&gt;
    &lt;menu title=&quot;Default Entries&quot;&gt;
      &lt;detach&gt;yes&lt;/detach&gt;
      &lt;menu title=&quot;Hostname&quot;&gt;
          &lt;command&gt;%s&lt;/command&gt;
          &lt;accelerator&gt;ALT-n&lt;/accelerator&gt;
      &lt;/menu&gt;
    &lt;/menu&gt;
  &lt;/send_menu&gt;
</pre>
<p> <code>Caveats:</code></p>
<dl>
<dt>
<dd>
<dl>
<dt>There is currently no strict format checking of this file.</p>
<dd>
<dt>The format of the file may change in the future</p>
<dd>
<dt>If the file exists the default entry (Hostname) is not added</p>
<dd></dl>
</dl>
<dl>
<dt>
<dd>
<p> The following replacement macros are available (note: these can be changed in the configuration file):</p>
<dl>
<dt>%s</p>
<dd> Hostname part of the specific connection string to each client, minus any username or port</p>
<dt>%u</p>
<dd> Username part of the connection string to each client</p>
<dt>%h</p>
<dd> Hostname of server where cssh is being run from</p>
<dt>%n</p>
<dd> &lt;<font SIZE="-1">RETURN</font>&gt; code</dl>
</dl>
<dl>
<dt>
<dd>
<p> <font SIZE="-1"><code>NOTE:</code></font> requires XML::Simple to be installed</dl>
</dl>
<h2>KNOWN BUGS</h2>
<dl>
<dt>1.</p>
<dd> Catering for IPv6 addresses is minimal. This is due to a conflict between IPv6 addresses and port numbers within the same server definition since they both use the same seperator, i.e. is the following just an IPv6 address, or an address + port number of 2323? </p>
<pre>
    2001:db8::1428:2323
</pre>
<p> Exactly &#8211; I cannot tell either. the IPv6 address without a port is assumed in those cases where it cannot be determined and a warning is issued. </p>
<p> Possible work arounds include:</p>
<dl>
<dt>
<dd>
<dl>
<dt>a.</p>
<dd> Use square brackets around the IPv6 address, i.e.<br />
&nbsp;<wbr>[2001:db8::1428]:2323 or<br />
&nbsp;<wbr>[2001:db8::1428:2323] as appropriate so there is no ambiguity</p>
<dt>b.</p>
<dd> Use the full IPv6 address if also using a port number &#8211; the 8th colon is assumed to be the port seperator.</p>
<dt>c.</p>
<dd> Define the IPv6 address in your /etc/hosts file, <font SIZE="-1">DNS</font> or other name service lookup mechanism and use the hostname instead of the address.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt>2.</p>
<dd> Swapping virtual desktops can a redraw of all the terminal windows. This is due to a lack of distinction within Tk between switching desktops and minimising/maximising windows. Until Tk can tell the difference between the two events, there is no fix (apart from rewriting everything directly in X)</dl>
<p> Anyone with any good ideas to fix the above bugs is more than welcome to get in touch and/or provide a patch.</p>
<h2>REPORTING BUGS</h2>
<dl>
<dt>&bull;</p>
<dd> If you have issues running cssh, first try: </p>
<p> <tt>&quot;cssh -e [user@]&lt;hostname&gt;[:port]&quot;</tt> </p>
<p> This performs two tests to confirm cssh is able to work properly with the settings provided within the <i></i>$HOME<i>/.clusterssh/config</i> file (or internal defaults). </p>
<pre>
        1. test the terminal window works with the options provided
        2. test ssh works to a host with the configured arguments
</pre>
<p> Configuration options to watch for in ssh are </p>
<pre>
        - Doesnt understand &quot;-o ConnectTimeout=10&quot; - remove the option 
          in the F&lt;$HOME/.clusterssh/config&gt; file
        - OpenSSH-3.8 using untrusted ssh tunnels - use &quot;-Y&quot; instead of &quot;-X&quot;
          or use &quot;ForwardX11Trusted yes' in ssh_config (if you change the
          default ssh options from -x to -X)
</pre>
<dt>&bull;</p>
<dd> If you require support, please run the following commands and post it on the web site in the support/problems forum: </p>
<p> <tt>&quot;perl -V&quot;</tt> </p>
<p> <tt>&quot;perl -MTk -e 'print $Tk::VERSION,$/'&quot;</tt> </p>
<p> <tt>&quot;perl -MX11::Protocol -e 'print $X11::Protocol::VERSION,$/'&quot;</tt> </p>
<p> <tt>&quot;cat /etc/csshrc $HOME/.clusterssh/config&quot;</tt></p>
<dt>&bull;</p>
<dd> Use the debug switches (-d, -D, or -dD) will turn on debugging output. However, please only use this option with one host at a time, i.e. &#8220;cssh -d &lt;host&gt;&#8221; due to the amount of output produced (in both main and child windows).</dl>
<h2>SEE ALSO</h2>
<p> &lt;<a rel="nofollow" href="http://clusterssh.sourceforge.net/">http://clusterssh.sourceforge.net/</a>&gt;, <tt>&quot;ssh&quot;</tt>, Tk::overview, X11::Protocol, <tt>&quot;perl&quot;</tt></p>
<h2>CREDITS</h2>
<p> A web site for comments, requests, bug reports and bug fixes/patches is available at &lt;<a rel="nofollow" href="http://clusterssh.sourceforge.net/">http://clusterssh.sourceforge.net/</a>&gt;</p>
<h2>AUTHOR</h2>
<p> Duncan Ferguson, <tt>&quot;&lt;duncan_j_ferguson at yahoo.co.uk&gt;&quot;</tt></p>
<h2>LICENSE AND COPYRIGHT</h2>
<p> Copyright 1999-2010 Duncan Ferguson. </p>
<p> This program is free software; you can redistribute it and/or modify it under the terms of either: the <font SIZE="-1">GNU</font> General Public License as published by the Free Software Foundation; or the Artistic License. </p>
<p> See <a rel="nofollow" href="http://dev.perl.org/licenses/">http://dev.perl.org/licenses/</a> for more information. </p>
<h2>Index</h2>
