---
title: "insync-headless(1)"
name: "insync-headless"
section: "1"
letter: "i"
url: "/docs/linux/man/1-insync-headless/"
description: "insync-headless – command line interface for the Insync process"
---

<h2 class="name">NAME</h2>
<p> insync-headless &#8211; command line interface for the Insync process </p>
<h2>SYNOPSIS</h2>
<p> <code>insync-headless [OPTION] [COMMAND] [ARGUMENT]&#8230;</code></p>
<h2>DESCRIPTION</h2>
<p> Command line interface for the Insync process. Insync is an application that syncs your Drive files to your computer. It has more advanced features than Google&#8217;s official client such as multiple account support, Google Doc conversion, symlink support, and built in sharing.</p>
<h2>OPTIONS</h2>
<dl>
<dt><i>-h, &#8211;help </i><code>[COMMAND]</p>
<dd> If COMMAND is given, shows the help message for it; if not, show the basic help message.</p>
<dt></code><i>-v, &#8211;version</i></p>
<dd> Show program&#8217;s version number and exit. </p>
</dl>
<h2>COMMANDS</h2>
<h3><code>Help command</code></h3>
<dl>
<dt><code>insync-headless </code><i>help </i><code>[COMMAND]</p>
<dd> If COMMAND is given, shows the help message for it; if not, show the basic help message.</dl>
<p> </code></p>
<h3><code>Account commands</code></h3>
<dl>
<dt><code>insync-headless </code><i>add_account </i><code>[OPTION]&#8230;</p>
<dd> Add account to Insync. </p>
<p> Arguments:<br />
 -a, &#8211;auth-code AUTH_CODE &#8211; Code to authorize Insync to access your account. To get it, go to <a rel="nofollow" href="https://insynchq.com/auth">https://insynchq.com/auth</a> and follow the prompts. If not given, Insync will open an external browser where you can login.<br />
 -p, &#8211;path PATH &#8211; Path where Insync folder for account will be placed. If not given, will default to ~/&lt;email address&gt;.<br />
 -e, &#8211;export-option EXPORT_OPTION &#8211; Set if account will download Google format files as Open Document formats (.odt), MS Office formats (.docx), or as links (.gddoc). Choices are &quot;open-document&quot;, &quot;ms-office&quot;, and &quot;link&quot;. Defaults to &quot;link&quot;.<br />
 -n, &#8211;no-download &#8211; Set if Insync should not download files when adding account. Files to be synced can be set later with the manage_selective_sync command.</p>
<dt>insync-headless </code><i>get_account_information</p>
<dd> Show information for connected acounts.</p>
<dt></i><code>insync-headless </code><i>move_folder </i><code>PREV_PATH NEW_PATH</p>
<dd> Move folder to a new path.</p>
<dt>insync-headless </code><i>remove_account </i><code>EMAIL</p>
<dd> Remove account from Insync.</p>
<dt>insync-headless </code><i>set_export_option </i><code>EMAIL SETTING</p>
<dd> Set if account will download Google format files as Open Document formats (.odt), MS Office formats (.docx), or as links (.gddoc). Choices are &quot;open-document&quot;, &quot;ms-office&quot;, and &quot;link&quot;.</dl>
<p> </code></p>
<h3><code>Commands for controlling Insync</code></h3>
<dl>
<dt><code>insync-headless </code><i>pause_syncing</p>
<dd> Pause syncing.</p>
<dt></i><code>insync-headless </code><i>quit</p>
<dd> Stop Insync.</p>
<dt></i><code>insync-headless </code><i>resume_syncing</p>
<dd> Resume syncing after Insync is paused.</p>
<dt></i><code>insync-headless </code><i>set_autostart </i><code>AUTOSTART</p>
<dd> Set autostart preference (yes/no).</p>
<dt>insync-headless </code><i>start </i><code>[OPTION]&#8230;</p>
<dd> Start Insync. </p>
<p> Options: </p>
<p> &#8211;no-daemon &#8211; don&#8217;t detach from the terminal, log output to stdout<br />
 &#8212;synchronous-full &#8211; sets synchronous flag of sqlite to FULL instead of the default NORMAL; makes sqlite transactions safer but causes extreme slowdown for others</dl>
<p> </code></p>
<h3><code>File commands</code></h3>
<dl>
<dt><code>insync-headless </code><i>force_sync </i><code>FULL_PATH</p>
<dd> Force sync item.</p>
<dt>insync-headless </code><i>get_domain_link </i><code>FULL_PATH</p>
<dd> Get domain link for file.</p>
<dt>insync-headless </code><i>get_file_status </i><code>FULL_PATH</p>
<dd> Get syncing status of file.</p>
<dt>insync-headless </code><i>get_link </i><code>FULL_PATH</p>
<dd> Get link for file, anyone can access.</p>
<dt>insync-headless </code><i>open_in_gdrive </i><code>FULL_PATH</p>
<dd> Open selected file in Google Drive web interface.</p>
<dt>insync-headless </code><i>remove_from_insync </i><code>FULL_PATH</p>
<dd> Remove linked file/folder from Insync.</p>
<dt>insync-headless </code><i>share </i><code>FULL_PATH</p>
<dd> Share selected file using Insync web interface.</dl>
<p> </code></p>
<h3><code>Ignore list commands</code></h3>
<dl>
<dt><code>insync-headless </code><i>manage_ignore_list </i><code>EMAIL</p>
<dd> Manage ignore list of account through a curses interface. </p>
<p> Adding an extension will NOT remove existing synced files of that type. Removing an extension, however, WILL sync existing ignored files of that type. These extensions will also be checked for folders, e.g., adding .app will ignore app bundles on Mac.</dl>
<p> </code></p>
<h3><code>Proxy commands</code></h3>
<dl>
<dt><code>insync-headless </code><i>get_proxy</p>
<dd> Show proxy configuration.</p>
<dt></i><code>insync-headless </code><i>set_proxy </i><code>MODE [TYPE HOST PORT [USERNAME PASSWORD]]</p>
<dd> Set proxy config. </p>
<p> Arguments: </p>
<p> MODE &#8211; Can be SYSTEM, NONE, or MANUAL. If SYSTEM or NONE, the next items are not required.<br />
 TYPE &#8211; Can be HTTP, SOCKS4, or SOCKS5.<br />
 HOST &#8211; Proxy host.<br />
 PORT &#8211; Proxy port.<br />
 USERNAME &#8211; Username for proxy authentication.<br />
 PASSWORD &#8211; Password for proxy authentication.</dl>
<p> </code></p>
<h3><code>Selective sync commands</code></h3>
<dl>
<dt><code>insync-headless </code><i>get_root_drive_files </i><code>EMAIL</p>
<dd> Get selective sync information for root Drive files and folders of account.</p>
<dt>insync-headless </code><i>manage_selective_sync </i><code>EMAIL</p>
<dd> Manage selective sync settings of account through a curses interface.</p>
<dt>insync-headless </code><i>set_selective_sync </i><code>EMAIL FILE_ID SETTING</p>
<dd> Set selective sync preference (yes/no) of file for given email. file_id can be seen in insync-headless </code><i>get_root_drive_files</dl>
<p> </i></p>
<h3><code>Sharing commands</code></h3>
<dl>
<dt><code>insync-headless </code><i>accept_all_new_shares </i><code>EMAIL</p>
<dd> Accept all new shares file to given account. New shares can be viewed through insync-headless </code><i>get_new_shares</p>
<dt></i><code>insync-headless </code><i>accept_share </i><code>FILENAME EMAIL</p>
<dd> Accept shared file to given account. New shares can be viewed through insync-headless </code><i>get_new_shares</p>
<dt></i><code>insync-headless </code><i>get_new_shares</p>
<dd> Show new shares.</p>
<dt></i><code>insync-headless </code><i>reject_all_new_shares </i><code>EMAIL</p>
<dd> Reject all new shares to given account. New shares can be viewed through insync-headless </code><i>get_new_shares</p>
<dt></i><code>insync-headless </code><i>reject_share </i><code>FILENAME EMAIL</p>
<dd> Reject shared file to given account. New shares can be viewed through insync-headless </code><i>get_new_shares</dl>
<p> </i></p>
<h3><code>Status commands</code></h3>
<dl>
<dt><code>insync-headless </code><i>get_actions_required</p>
<dd> Show required actions.</p>
<dt></i><code>insync-headless </code><i>get_errors</p>
<dd> Show error messages.</p>
<dt></i><code>insync-headless </code><i>get_recent_changes</p>
<dd> Show 20 most recent changes.</p>
<dt></i><code>insync-headless </code><i>get_status</p>
<dd> Show syncing status.</p>
<dt></i><code>insync-headless </code><i>get_sync_progress</p>
<dd> Show progress of files being downloaded/uploaded and how many files are queued.</p>
<dt></i><code>insync-headless </code><i>retry_errors</p>
<dd> Retry all errors.</dl>
<p> </i></p>
<h2>BUGS</h2>
<p> Please report bugs to support [at] insynchq.com.<br />
 How-to guides: &lt;<a rel="nofollow" href="https://help.insynchq.com">https://help.insynchq.com</a>&gt;.<br />
 Support forums: &lt;<a rel="nofollow" href="https://forums.insynchq.com">https://forums.insynchq.com</a>&gt;.</p>
<h2>AUTHOR</h2>
<p> Created by the Insync team.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-insync/">insync</a>(1) </p>
<h2>Index</h2>
<dt><a href="#lbAP">BUGS</a></p>
<dd>
<dt><a href="#lbAQ">AUTHOR</a></p>
<dd>
<dt><a href="#lbAR">SEE ALSO</a></p>
<dd></dl>
