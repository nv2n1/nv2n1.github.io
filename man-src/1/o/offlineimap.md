---
title: "offlineimap(1)"
name: "offlineimap"
section: "1"
letter: "o"
url: "/docs/linux/man/1-offlineimap/"
description: "offlineimap – Synchronize mailboxes and Maildirs both ways or one either way."
---

<h2 class="name">NAME</h2>
<p> offlineimap &#8211; Synchronize mailboxes and Maildirs both ways or one either way. </p>
<h2>SYNOPSIS</h2>
<pre>
<i>offlineimap</i> (options)
</pre>
<h2>DESCRIPTION</h2>
<p> Synchronize the accounts configured in the configuration file via IMAP. Each account has two sides. One of the side must be an IMAP server. The other side can either be a Maildir or another IMAP server. </p>
<p> Works with Python 2.</p>
<h2>OPTIONS</h2>
<p> -h, &#8211;help</p>
<dl>
<dt>
<dd> Display summary of options.</dl>
<p> &#8211;version</p>
<dl>
<dt>
<dd> Output version.</dl>
<p> -V</p>
<dl>
<dt>
<dd> Output offlineimap version and additional imaplib2 information.</dl>
<p> &#8211;dry-run</p>
<dl>
<dt>
<dd> Run in dry run mode. </p>
<p> Do not actually modify any store but check and print what synchronization actions would be taken if a sync would be performed. It will not precisely give the exact information what will happen. If e.g. we need to create a folder, it merely outputs <i>Would create folder X</i>, but not how many and which mails it would transfer.</dl>
<p> &#8211;info</p>
<dl>
<dt>
<dd> Output information on the configured email repositories. </p>
<p> Useful for debugging and bug reporting. Use in conjunction with the &#8216;-a&#8217; option to limit the output to a single account. This mode will prevent any actual sync to occur and exits after it output the debug information.</dl>
<p> -1</p>
<dl>
<dt>
<dd> Limit multithreading operations and run solely a single-thread sync. </p>
<p> This effectively sets the <i>maxsyncaccounts</i> and all <i>maxconnections</i> configuration file variables to <i>1</i> (the number).</dl>
<p> -P &lt;directory&gt;</p>
<dl>
<dt>
<dd> Set OfflineIMAP into profile mode. </p>
<p> The program will create DIR (it must not already exist). As it runs, Python profiling information about each thread is logged into profiledir. Please note: This option is present for debugging and optimization only, and should NOT be used unless you have a specific reason to do so. It will significantly decrease program performance, may reduce reliability, and can generate huge amounts of data. This option implies the &#8216;-1&#8217; option.</dl>
<p> -a &lt;account1[,account2[,&#8230;]]&gt;</p>
<dl>
<dt>
<dd> Overrides the accounts section in the config file. </p>
<p> Allows one to specify a particular account or set of accounts to sync without having to edit the config file.</dl>
<p> -c &lt;path/to/configuration_file&gt;</p>
<dl>
<dt>
<dd> Specifies a configuration file to use.</dl>
<p> -d &lt;type1[,type2[,&#8230;]]&gt;</p>
<dl>
<dt>
<dd> Enables debugging for OfflineIMAP. </p>
<p> This is useful if you are to track down a malfunction or figure out what is going on under the hood. This option requires one or more debugtypes, separated by commas. These define what exactly will be debugged, and so far include options: &quot;imap&quot;, &quot;thread&quot;, &quot;maildir&quot; or &quot;ALL&quot;. The imap option will enable IMAP protocol stream and parsing debugging. Note that the output may contain passwords, so take care to remove that from the debugging output before sending it to anyone else. The maildir option will enable debugging for certain Maildir operations. The use of any debug option (unless &quot;thread&quot; is included), implies the single-thread option &#8216;-1&#8217;.</dl>
<p> -l &lt;path/to/file.log&gt;</p>
<dl>
<dt>
<dd> Send logs to &lt;file.log&gt;.</dl>
<p> -s</p>
<dl>
<dt>
<dd> Send logs to syslog.</dl>
<p> -f &lt;folder1[,folder1[,&#8230;]]&gt;</p>
<dl>
<dt>
<dd> Only sync the specified folders. </p>
<p> The folder names are the untranslated foldernames of the remote repository. This command-line option overrides any <i>folderfilter</i> and <i>folderincludes</i> options in the configuration file.</dl>
<p> -k &lt;[section:]option=value</p>
<dl>
<dt>
<dd> Override any configuration file option. </p>
<p> If &quot;section&quot; is omitted, it defaults to &quot;general&quot;. Any underscores in the section name are replaced with spaces: for instance, to override option &quot;autorefresh&quot; in the &quot;[Account Personal]&quot; section in the config file one would use &#8216;-k Account_Personal:autorefresh=30&#8217;. Repeat this option as much as necessary to redefine multiple options.</dl>
<p> -o</p>
<dl>
<dt>
<dd> Run only once. </p>
<p> Ignore any autorefresh setting in the configuration file.</dl>
<p> -q</p>
<dl>
<dt>
<dd> Run only quick synchronizations. </p>
<p> Ignore any flag updates on IMAP servers. If a flag on the remote IMAP changes, and we have the message locally, it will be left untouched in a quick run. This option is ignored if maxage is set.</dl>
<p> -u &lt;UI&gt;</p>
<dl>
<dt>
<dd> Specifies an alternative user interface to use. </p>
<p> This overrides the default specified in the configuration file. The UI specified with &#8216;-u&#8217; will be forced to be used, even if checks determine that it is not usable. Possible interface choices are: quiet, basic, syslog, ttyui, blinkenlights, machineui.</dl>
<p> &#8211;delete-folder</p>
<dl>
<dt>
<dd> Delete a folder on the remote repository. </p>
<p> Only one account must be specified/configured for this feature to work or you must provide one account with -a. The folder name must be provided with the remote separators (likely <i>/</i>) in UTF-8 if utf8foldernames is enabled or in IMAP otherwise. E.g.: &quot;Remote/folder/name&quot;.</dl>
<p> &#8211;migrate-fmd5-using-nametrans</p>
<dl>
<dt>
<dd> Migrate FMD5 hashes from versions prior to 6.3.5. </p>
<p> The way that FMD5 hashes are calculated was changed in version 6.3.5 (now using the nametrans folder name) introducing a regression which may lead to re-uploading all messages. Try and fix the above regression by calculating the correct FMD5 values and renaming the corresponding messages.</dl>
<dl>
<dt>
<dd>
 <font SIZE="+1"> <code>Caution</code> </font> </p>
<p> Since the FMD5 part of the filename changes, this may lead to UID conflicts. Ensure to dispose a proper backup of both the cache and the Maildir before running this fix as well as verify the results using the &#8216;&#8211;dry-run&#8217; flag first. </p>
</dl>
<p> &#8211;mbnames-prune</p>
<dl>
<dt>
<dd> Remove dangling entries for removed accounts or if mbnames is not enabled/used anymore. </p>
<p> Internally, offlineimap build intermediate mbnames files. They are added automatically when mbnames is enabled. However, disabling accounts so they are not synced anymore does not necessarily means they should be removed from the file built by mbnames. It is required to start offlineimap with this CLI option each time accounts are removed. When run, any account not in the <i>accounts</i> configuration option are removed in the mbnames file. </p>
<p> It is possible to manually remove intermediate files in <i>&lt;metadata&gt;/mbnames/</i>. </p>
<p> Notice this option honors &#8211;dry-run.</dl>
<h2>CONFIGURATION</h2>
<p> For full details of the available configuration options, please refer to /usr/share/doc/offlineimap/examples/offlineimap.conf.gz.</p>
<h2>SYNCHRONIZATION PERFORMANCE</h2>
<p> By default, we use fairly conservative settings that are safe for syncing but that might not be the best performing one. Once you got everything set up and running, you might want to look into speeding up your synchronization. Here are a couple of hints and tips on how to achieve this. </p>
<dl>
<dt>
<dd> 1. Synchronize more than one account. </p>
<p> By default we only use one connection to an IMAP server. Using 2 or even 3 speeds things up considerably in most cases. In order to synchronize more than one account concurrently, consider starting one instance of offlineimap per account. </p>
<dl>
<dt>
<dd>
 <font SIZE="+1"> <code>Warning</code> </font><br />
 enabling the <i>maxsyncaccounts</i> and <i>maxconnections</i> options is deprecated since it&#8217;s known to have race conditions. </p>
</dl>
</dl>
<dl>
<dt>
<dd> 2. Use folderfilters. </p>
<p> The quickest sync is a sync that can ignore some folders. I sort my inbox into monthly folders, and ignore every folder that is more than 2-3 months old, this lets me only inspect a fraction of my Mails on every sync. If you haven&#8217;t done this yet, do it :). See the <i>folderfilter</i> section in <i>offlineimap.conf</i>.</dl>
<dl>
<dt>
<dd> 3. The sqlite cache. </p>
<p> OfflineImap caches the state of the synchronisation to e.g. be able to determine if a mail has been added or deleted on either side. </p>
<p> The historical status cache was a plain text file that was writing out the complete file for each single new message (or even changed flag) to a temporary file. If there was plenty of files in a folder this was bound to make things slow. The latest status cache is sqlite. This saves plenty of disk activity. </p>
<p> The historical plain status cache is not supported anymore but migrating from a very old installation using the plain text cache is still supported. In this case, you may want to delete the old cache directory in <i>&lt;metadata&gt;/Account-&lt;account&gt;/LocalStatus</i> manually (the sqlite cache stands in the <i>LocalStatus-sqlite</i> folder). First, make sure you have run the new version of offlineimap for all your accounts so that the status cache was migrated.</dl>
<dl>
<dt>
<dd> 4. Use quick sync. </p>
<p> A regular sync will request all flags and all UIDs of all mails in each folder which takes quite some time. A quick sync only compares the number of messages in a folder on the IMAP side (it will detect flag changes on the Maildir side of things though). A quick sync on my smallish account will take 7 seconds rather than 40 seconds. E.g. run a cron script that does a regular sync once a day, and does quick syncs &#8216;-q&#8217; only synchronizing the &#8216;-f INBOX&#8217; in between.</dl>
<dl>
<dt>
<dd> 5. Turn off fsync. </p>
<p> In the <i>[general]</i> section you can set fsync to <i>True</i> or <i>False</i>. If you want to play 110% safe and wait for all operations to hit the disk before continuing, you can set this to True. If you set it to False, you lose some of that safety, trading it for speed.</dl>
<h2>SECURITY AND SSL</h2>
<p> By default, OfflineIMAP will connect using any method that <i>openssl</i> supports, that is SSLv2, SSLv3, or TLSv1. </p>
<p> Do note that SSLv2 is notoriously insecure and deprecated. Unfortunately, python2 does not offer easy ways to disable SSLv2. It is recommended you test your setup and make sure that the mail server does not use an SSLv2 connection. Use e.g. &quot;openssl s_client -host mail.server -port 443&quot; to find out the connection that is used by default. </p>
<dl>
<dt>
<dd> &bull; Certificate checking </p>
<p> Unfortunately, by default we will not verify the certificate of an IMAP TLS/SSL server we connect to, so connecting by SSL is no guarantee against man-in-the-middle attacks. While verifying a server certificate checking the fingerprint is recommended. There is currently only one safe way to ensure that you connect to the correct server in an encrypted manner: you can specify a <i>sslcacertfile</i> setting in your repository section of offlineimap.conf pointing to a file that contains (among others) a CA Certificate in PEM format which validating your server certificate. In this case, we will check that: </p>
<dl>
<dt>
<dd> 1. The server SSL certificate is validated by the CA Certificate.</dl>
<dl>
<dt>
<dd> 2. The server host name matches the SSL certificate.</dl>
<dl>
<dt>
<dd> 3. The server certificate is not past its expiration date.</dl>
</dl>
<p> The FAQ has an entry on how to create your own certificate and CA certificate. </p>
<dl>
<dt>
<dd> &bull; StartTLS </p>
<p> If you have not configured your account to connect via SSL anyway, OfflineImap will still attempt to set up an SSL connection via the STARTTLS function, in case the imap server supports it. </p>
<p> There is no certificate or fingerprint checking involved at all, when using STARTTLS (the underlying imaplib library does not support this yet). This means that you will be protected against passively listening eavesdroppers and they will not be able to see your password or email contents. However, this will not protect you from active attacks, such as Man-In-The-Middle attacks which cause you to connect to the wrong server and pretend to be your mail server. </p>
<p> <code>DO NOT RELY ON STARTTLS AS A SAFE CONNECTION GUARANTEEING THE AUTHENTICITY OF YOUR IMAP SERVER!</code></dl>
<h2>UNIX SIGNALS</h2>
<p> OfflineImap listens to the unix signals SIGUSR1, SIGUSR2, SIGTERM, SIGINT, SIGHUP, SIGQUIT. </p>
<dl>
<dt>
<dd> &bull; If sent a SIGUSR1 it will abort any current (or next future) sleep of all accounts that are configured to <i>autorefresh</i>. In effect, this will trigger a full sync of all accounts to be performed as soon as possible.</dl>
<dl>
<dt>
<dd> &bull; If sent a SIGUSR2 or SIGABRT, it will stop <i>autorefresh</i> mode for all accounts. That is, accounts will abort any current sleep and will exit after a currently running synchronization has finished. This signal can be used to gracefully exit out of a running offlineimap &quot;daemon&quot;.</dl>
<dl>
<dt>
<dd> &bull; SIGTERM, SIGINT, SIGHUP are all treated to gracefully terminate as soon as possible. This means it will finish syncing the current folder in each account, close keep alive connections, remove locks on the accounts and exit. </p>
<p> It may take up to 10 seconds, if autorefresh option is used. </p>
<p> More than one SIGTERM will behave like SIGQUIT.</dl>
<dl>
<dt>
<dd> &bull; If sent SIGQUIT, dumps stack traces for all threads and tries to dump process core.</dl>
<h2>KNOWN ISSUES</h2>
<dl>
<dt>
<dd> &bull; Deletions. </p>
<p> While in usual run the deletions are propagated. To prevent from data loss, removing a folder makes offlineimap re-sync the folder. However, propagating the removal of the whole content of a folder can happen in the two following cases: </p>
<dl>
<dt>
<dd> &bull; The whole content of a folder is deleted but the folder directory still exists.</dl>
<dl>
<dt>
<dd> &bull; The parent directory of the folder was deleted.</dl>
</dl>
<dl>
<dt>
<dd> &bull; SSL3 write pending. </p>
<p> Users enabling SSL may hit a bug about &quot;SSL3 write pending&quot;. If so, the account(s) will stay unsynchronised from the time the bug appeared. Running OfflineIMAP again can help. We are still working on this bug. Patches or detailed bug reports would be appreciated. Please check you&#8217;re running the last stable version and send us a report to the mailing list including the full log.</dl>
<dl>
<dt>
<dd> &bull; IDLE support is incomplete and experimental. Bugs may be encountered. </p>
<dl>
<dt>
<dd> &bull; No hook exists for &quot;run after an IDLE response&quot;. </p>
<p> Email will show up, but may not be processed until the next refresh cycle.</dl>
<dl>
<dt>
<dd> &bull; nametrans may not be supported correctly.</dl>
<dl>
<dt>
<dd> &bull; IMAP IDLE &lt;→ IMAP IDLE doesn&#8217;t work yet.</dl>
<dl>
<dt>
<dd> &bull; IDLE might stop syncing on a system suspend/resume.</dl>
<dl>
<dt>
<dd> &bull; IDLE may only work &quot;once&quot; per refresh. </p>
<p> If you encounter this bug, please send a report to the list!</dl>
</dl>
<dl>
<dt>
<dd> &bull; Maildir support in Windows drive. </p>
<p> Maildir uses colon character (:) in message file names. Colon is however forbidden character in windows drives. There are several workarounds for that situation: </p>
<dl>
<dt>
<dd> 1. Enable file name character translation in windows registry (not tested). </p>
<dl>
<dt>
<dd> &bull; <a rel="nofollow" href="http://support.microsoft.com/kb/289627">http://support.microsoft.com/kb/289627</a></dl>
</dl>
<dl>
<dt>
<dd> 2. Use cygwin managed mount (not tested). </p>
<dl>
<dt>
<dd> &bull; not available anymore since cygwin 1.7</dl>
</dl>
<dl>
<dt>
<dd> 3. Use &quot;maildir-windows-compatible = yes&quot; account OfflineIMAP configuration. </p>
<dl>
<dt>
<dd> &bull; That makes OfflineIMAP to use exclamation mark (!) instead of colon for storing messages. Such files can be written to windows partitions. But you will probably loose compatibility with other programs trying to read the same Maildir.</dl>
<dl>
<dt>
<dd> &bull; Exclamation mark was chosen because of the note in <a rel="nofollow" href="http://docs.python.org/library/mailbox.html">http://docs.python.org/library/mailbox.html</a></dl>
<dl>
<dt>
<dd> &bull; If you have some messages already stored without this option, you will have to re-sync them again</dl>
</dl>
</dl>
<dl>
<dt>
<dd> &bull; OfflineIMAP confused after system suspend. </p>
<p> When resuming a suspended session, OfflineIMAP does not cleanly handles the broken socket(s) if socktimeout option is not set. You should enable this option with a value like 10.</dl>
<dl>
<dt>
<dd> &bull; OfflineIMAP confused when mails change while in a sync. </p>
<p> When OfflineIMAP is syncing, some events happening since the invocation on remote or local side are badly handled. OfflineIMAP won&#8217;t track for changes during the sync.</dl>
<dl>
<dt>
<dd> &bull; Sharing a maildir with multiple IMAP servers. </p>
<p> Generally a word of caution mixing IMAP repositories on the same Maildir root. You have to be careful that you <code>never</code> use the same maildir folder for 2 IMAP servers. In the best case, the folder MD5 will be different, and you will get a loop where it will upload your mails to both servers in turn (infinitely!) as it thinks you have placed new mails in the local Maildir. In the worst case, the MD5 is the same (likely) and mail UIDs overlap (likely too!) and it will fail to sync some mails as it thinks they are already existent. </p>
<p> I would create a new local Maildir Repository for the Personal Gmail and use a different root to be on the safe side here. You could e.g. use </p>
<dl>
<dt>
<dd>
<pre>
`~/mail/Pro' as Maildir root for the ProGmail and
`~/mail/Personal' as root for the personal one.
</pre>
</dl>
<p> If you then point your local mutt, or whatever MUA you use to &#8216;~/mail/&#8217; as root, it should still recognize all folders.</dl>
<dl>
<dt>
<dd> &bull; Edge cases with maxage causing too many messages to be synced. </p>
<p> All messages from at most maxage days ago (+/- a few hours, depending on timezones) are synced, but there are cases in which older messages can also be synced. This happens when a message&#8217;s UID is significantly higher than those of other messages with similar dates, e.g. when messages are added to the local folder behind offlineimap&#8217;s back, causing them to get assigned a new UID, or when offlineimap first syncs a pre-existing Maildir. In the latter case, it could appear as if a noticeable and random subset of old messages are synced.</dl>
<dl>
<dt>
<dd> &bull; Offlineimap hangs. </p>
<p> When having unexpected hangs it&#8217;s advised to set &#8216;singlethreadperfolder&#8217; to <i>yes</i>, especially when in IMAP/IMAP mode (no maildir).</dl>
<dl>
<dt>
<dd> &bull; Passwords in netrc. </p>
<p> Offlineimap doesn&#8217;t know how to retrieve passwords when more than one account is stored in the netrc file. See <a rel="nofollow" href="https://github.com/OfflineIMAP/offlineimap/issues/295.">https://github.com/OfflineIMAP/offlineimap/issues/295.</a></dl>
<dl>
<dt>
<dd> &bull; XOAUTH2 </p>
<p> XOAUTH2 might be a bit tricky to set up. Make sure you&#8217;ve followed the step to step guide in <i>offlineimap.conf</i>. The known bugs about Gmail are tracked at <a rel="nofollow" href="https://github.com/OfflineIMAP/offlineimap/labels/Gmail.">https://github.com/OfflineIMAP/offlineimap/labels/Gmail.</a> </p>
<p> Sometimes, you might hit one of the following error: </p>
<dl>
<dt>
<dd> &bull; [imap]: xoauth2handler: response &quot;{u&#8217;error&#8217;: u&#8217;invalid_grant&#8217;}&quot;</dl>
<dl>
<dt>
<dd> &bull; oauth2handler got: {u&#8217;error&#8217;: u&#8217;invalid_grant&#8217;}</dl>
<p> In such case, we had reports that generating a new refresh token from the same client ID and secret can help. </p>
<p> <code>Google documentation on &quot;invalid_grant&quot;</code>. </p>
<dl>
<dt>
<dd>
<pre>
When you try to use a refresh token, the following returns you an
invalid_grant error:
  - Your server's clock is not in sync with network time protocol - NTP.
  - The refresh token limit has been exceeded.
</pre>
</dl>
<p> <code>Token expiration</code>. </p>
<dl>
<dt>
<dd>
<pre>
It is possible that a granted token might no longer work. A token might stop
working for one of these reasons:
  - The user has revoked access.
  - The token has not been used for six months.
  - The user changed passwords and the token contains Gmail scopes.
  - The user account has exceeded a certain number of token requests.
There is currently a limit of 50 refresh tokens per user account per client. If
the limit is reached, creating a new token automatically invalidates the oldest
token without warning. This limit does not apply to service accounts.
</pre>
</dl>
<p> See <a rel="nofollow" href="https://developers.google.com/analytics/devguides/config/mgmt/v3/authorization">https://developers.google.com/analytics/devguides/config/mgmt/v3/authorization</a> and <a rel="nofollow" href="https://developers.google.com/identity/protocols/OAuth2#expiration">https://developers.google.com/identity/protocols/OAuth2#expiration</a> to know more.</dl>
<dl>
<dt>
<dd> &bull; &quot;does not have message with UID&quot; with Microsoft servers </p>
<dl>
<dt>
<dd>
<pre>
`ERROR: IMAP server 'Server ### Remote' does not have a message with UID 'xxx'`
</pre>
</dl>
<p> Microsoft IMAP servers are not compliant with the RFC. It is currently required to folderfilter some faulting folders. See <a rel="nofollow" href="http://www.offlineimap.org/doc/FAQ.html#exchange-and-office365">http://www.offlineimap.org/doc/FAQ.html#exchange-and-office365</a> for a detailed list.</dl>
<h2>MAIN AUTHORS</h2>
<dl>
<dt>
<dd>
<pre>
John Goerzen, Sebastian Spaetz, Eygene Ryabinkin, Nicolas Sebrecht.
</pre>
</dl>
<h2>SEE ALSO</h2>
<dl>
<dt>
<dd>
<pre>
<a href="//www.systutorials.com/docs/linux/man/7-offlineimapui/">offlineimapui</a>(7), <a href="//www.systutorials.com/docs/linux/man/1-openssl/">openssl</a>(1), <a href="//www.systutorials.com/docs/linux/man/7-signal/">signal</a>(7), <a href="//www.systutorials.com/docs/linux/man/1-sqlite3/">sqlite3</a>(1).
<a rel="nofollow" href="http://www.offlineimap.org">http://www.offlineimap.org</a>
</pre>
</dl>
<h2>Index</h2>
