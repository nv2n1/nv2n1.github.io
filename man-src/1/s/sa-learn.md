---
title: "sa-learn(1)"
name: "sa-learn"
section: "1"
letter: "s"
url: "/docs/linux/man/1-sa-learn/"
description: "sa-learn – train SpamAssassin’s Bayesian classifier"
---

<h2 class="name">NAME</h2>
<p> sa-learn &#8211; train SpamAssassin&#8217;s Bayesian classifier </p>
<h2>SYNOPSIS</h2>
<p> <code>sa-learn</code> [options] [file]&#8230; </p>
<p> <code>sa-learn</code> [options] &#8211;dump [ all | data | magic ] </p>
<p> Options: </p>
<pre><code>
 --ham                 Learn messages as ham (non-spam)
 --spam                Learn messages as spam
 --forget              Forget a message
 --use-ignores         Use bayes_ignore_from and bayes_ignore_to
 --sync                Synchronize the database and the journal if needed
 --force-expire        Force a database sync and expiry run
 --dbpath &lt;path&gt;       Allows commandline override (in bayes_path form)
                       for where to read the Bayes DB from
 --dump [all|data|magic]  Display the contents of the Bayes database
                       Takes optional argument for what to display
  --regexp &lt;re&gt;        For dump only, specifies which tokens to
                       dump based on a regular expression.
 -f file, --folders=file  Read list of files/directories from file
 --dir                 Ignored;
 historical compatibility-- file Ignored;
 historical compatibility-- mbox Input sources are in mbox format-- mbx Input sources are in mbx format-- max - size&lt;b&gt; Skip messages larger than b bytes;
                       defaults to 256 KiB, 0 implies no limit
 --showdots            Show progress using dots
 --progress            Show progress using progress bar
 --no-sync             Skip synchronizing the database and journal
                       after learning
 -L, --local           Operate locally, no network accesses
 --import              Migrate data from older version/non DB_File
                       based databases
 --clear               Wipe out existing database
 --backup              Backup, to STDOUT, existing database
 --restore &lt;filename&gt;  Restore a database from filename
 -u username, --username=username
                       Override username taken from the runtime
                       environment, used with SQL
 -C path, --configpath=path, --config-file=path
                       Path to standard configuration dir
 -p prefs, --prefspath=file, --prefs-file=file
                       Set user preferences file
 --siteconfigpath=path Path for site configs
                       (default: /etc/mail/spamassassin)
 --cf='config line'    Additional line of configuration
 -D, --debug [area=n,...]  Print debugging messages
 -V, --version         Print version
 -h, --help            Print usage message
</code></pre>
<h2>DESCRIPTION</h2>
<p> Given a typical selection of your incoming mail classified as spam or ham (non-spam), this tool will feed each mail to SpamAssassin, allowing it to &#8216;learn&#8217; what signs are likely to mean spam, and which are likely to mean ham. </p>
<p> Simply run this command once for each of your mail folders, and it will &#8221;learn&#8221; from the mail therein. </p>
<p> Note that csh-style <i>globbing</i> in the mail folder names is supported; in other words, listing a folder name as <tt>&quot;*&quot;</tt> will scan every folder that matches. See <tt>&quot;Mail::SpamAssassin::ArchiveIterator&quot;</tt> for more details. </p>
<p> SpamAssassin remembers which mail messages it has learnt already, and will not re-learn those messages again, unless you use the <code>&#8211;forget</code> option. Messages learnt as spam will have SpamAssassin markup removed, on the fly. </p>
<p> If you make a mistake and scan a mail as ham when it is spam, or vice versa, simply rerun this command with the correct classification, and the mistake will be corrected. SpamAssassin will automatically &#8216;forget&#8217; the previous indications. </p>
<p> Users of <tt>&quot;spamd&quot;</tt> who wish to perform training remotely, over a network, should investigate the <tt>&quot;spamc -L&quot;</tt> switch.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;ham</code></p>
<dd> Learn the input message(s) as ham. If you have previously learnt any of the messages as spam, SpamAssassin will forget them first, then re-learn them as ham. Alternatively, if you have previously learnt them as ham, it&#8217;ll skip them this time around. If the messages have already been filtered through SpamAssassin, the learner will ignore any modifications SpamAssassin may have made.</p>
<dt><code>&#8211;spam</code></p>
<dd> Learn the input message(s) as spam. If you have previously learnt any of the messages as ham, SpamAssassin will forget them first, then re-learn them as spam. Alternatively, if you have previously learnt them as spam, it&#8217;ll skip them this time around. If the messages have already been filtered through SpamAssassin, the learner will ignore any modifications SpamAssassin may have made.</p>
<dt><code>&#8211;folders</code>=<i>filename</i>, <code>-f</code> <i>filename</i></p>
<dd> sa-learn will read in the list of folders from the specified file, one folder per line in the file. If the folder is prefixed with <tt>&quot;ham:type:&quot;</tt> or <tt>&quot;spam:type:&quot;</tt>, sa-learn will learn that folder appropriately, otherwise the folders will be assumed to be of the type specified by <code>&#8211;ham</code> or <code>&#8211;spam</code>. </p>
<p> <tt>&quot;type&quot;</tt> above is optional, but is the same as the standard for ArchiveIterator: mbox, mbx, dir, file, or detect (the default if not specified).</p>
<dt><code>&#8211;mbox</code></p>
<dd> sa-learn will read in the file(s) containing the emails to be learned, and will process them in mbox format (one or more emails per file).</p>
<dt><code>&#8211;mbx</code></p>
<dd> sa-learn will read in the file(s) containing the emails to be learned, and will process them in mbx format (one or more emails per file).</p>
<dt><code>&#8211;use-ignores</code></p>
<dd> Don&#8217;t learn the message if a from address matches configuration file item <tt>&quot;bayes_ignore_from&quot;</tt> or a to address matches <tt>&quot;bayes_ignore_to&quot;</tt>. The option might be used when learning from a large file of messages from which the hammy spam messages or spammy ham messages have not been removed.</p>
<dt><code>&#8211;sync</code></p>
<dd> Synchronize the journal and databases. Upon successfully syncing the database with the entries in the journal, the journal file is removed.</p>
<dt><code>&#8211;force-expire</code></p>
<dd> Forces an expiry attempt, regardless of whether it may be necessary or not. Note: This doesn&#8217;t mean any tokens will actually expire. Please see the <font SIZE="-1">EXPIRATION</font> section below. </p>
<p> Note: <tt>&quot;--force-expire&quot;</tt> also causes the journal data to be synchronized into the Bayes databases.</p>
<dt><code>&#8211;forget</code></p>
<dd> Forget a given message previously learnt.</p>
<dt><code>&#8211;dbpath</code></p>
<dd> Allows a commandline override of the <i>bayes_path</i> configuration option.</p>
<dt><code>&#8211;dump</code> <i>option</i></p>
<dd> Display the contents of the Bayes database. Without an option or with the <i>all</i> option, all magic tokens and data tokens will be displayed. <i>magic</i> will only display magic tokens, and <i>data</i> will only display the data tokens. </p>
<p> Can also use the <code>&#8211;regexp</code> <i></i><font SIZE="-1"><i>RE</i></font><i></i> option to specify which tokens to display based on a regular expression.</p>
<dt><code>&#8211;clear</code></p>
<dd> Clear an existing Bayes database by removing all traces of the database. </p>
<p> <font SIZE="-1">WARNING:</font> This is destructive and should be used with care.</p>
<dt><code>&#8211;backup</code></p>
<dd> Performs a dump of the Bayes database in machine/human readable format. </p>
<p> The dump will include token and seen data. It is suitable for input back into the &#8211;restore command.</p>
<dt><code>&#8211;restore</code>=<i>filename</i></p>
<dd> Performs a restore of the Bayes database defined by <i>filename</i>. </p>
<p> <font SIZE="-1">WARNING:</font> This is a destructive operation, previous Bayes data will be wiped out.</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Print help message and exit.</p>
<dt><code>-u</code> <i>username</i>, <code>&#8211;username</code>=<i>username</i></p>
<dd> If specified this username will override the username taken from the runtime environment. You can use this option to specify users in a virtual user configuration when using <font SIZE="-1">SQL</font> as the Bayes backend. </p>
<p> <font SIZE="-1">NOTE:</font> This option will not change to the given <i>username</i>, it will only attempt to act on behalf of that user. Because of this you will need to have proper permissions to be able to change files owned by <i>username</i>. In the case of <font SIZE="-1">SQL</font> this generally is not a problem.</p>
<dt><code>-C</code> <i>path</i>, <code>&#8211;configpath</code>=<i>path</i>, <code>&#8211;config-file</code>=<i>path</i></p>
<dd> Use the specified path for locating the distributed configuration files. Ignore the default directories (usually <tt>&quot;/usr/share/spamassassin&quot;</tt> or similar).</p>
<dt><code>&#8211;siteconfigpath</code>=<i>path</i></p>
<dd> Use the specified path for locating site-specific configuration files. Ignore the default directories (usually <tt>&quot;/etc/mail/spamassassin&quot;</tt> or similar).</p>
<dt><code>&#8211;cf=&#8217;config line&#8217;</code></p>
<dd> Add additional lines of configuration directly from the command-line, parsed after the configuration files are read. Multiple <code>&#8211;cf</code> arguments can be used, and each will be considered a separate line of configuration.</p>
<dt><code>-p</code> <i>prefs</i>, <code>&#8211;prefspath</code>=<i>prefs</i>, <code>&#8211;prefs-file</code>=<i>prefs</i></p>
<dd> Read user score preferences from <i>prefs</i> (usually <tt>&quot;$HOME/.spamassassin/user_prefs&quot;</tt>).</p>
<dt><code>&#8211;progress</code></p>
<dd> Prints a progress bar (to <font SIZE="-1">STDERR</font>) showing the current progress. In the case where no valid terminal is found this option will behave very much like the &#8211;showdots option.</p>
<dt><code>-D</code> [<i>area,&#8230;</i>], <code>&#8211;debug</code> [<i>area,&#8230;</i>]</p>
<dd> Produce debugging output. If no areas are listed, all debugging information is printed. Diagnostic output can also be enabled for each area individually; <i>area</i> is the area of the code to instrument. For example, to produce diagnostic output on bayes, learn, and dns, use: </p>
<pre>
        spamassassin -D bayes,learn,dns
</pre>
<p> For more information about which areas (also known as channels) are available, please see the documentation at: </p>
<pre>
        C&lt;<a rel="nofollow" href="http://wiki.apache.org/spamassassin/DebugChannels">http://wiki.apache.org/spamassassin/DebugChannels</a>&gt;
</pre>
<p> Higher priority informational messages that are suitable for logging in normal circumstances are available with an area of &#8220;info&#8221;.</p>
<dt><code>&#8211;no-sync</code></p>
<dd> Skip the slow synchronization step which normally takes place after changing database entries. If you plan to learn from many folders in a batch, or to learn many individual messages one-by-one, it is faster to use this switch and run <tt>&quot;sa-learn --sync&quot;</tt> once all the folders have been scanned. </p>
<p> Clarification: The state of <i>&#8211;no-sync</i> overrides the <i>bayes_learn_to_journal</i> configuration option. If not specified, sa-learn will learn to the database directly. If specified, sa-learn will learn to the journal file. </p>
<p> Note: <i>&#8211;sync</i> and <i>&#8211;no-sync</i> can be specified on the same commandline, which is slightly confusing. In this case, the <i>&#8211;no-sync</i> option is ignored since there is no learn operation.</p>
<dt><code>-L</code>, <code>&#8211;local</code></p>
<dd> Do not perform any network accesses while learning details about the mail messages. This will speed up the learning process, but may result in a slightly lower accuracy. </p>
<p> Note that this is currently ignored, as current versions of SpamAssassin will not perform network access while learning; but future versions may.</p>
<dt><code>&#8211;import</code></p>
<dd> If you previously used SpamAssassin&#8217;s Bayesian learner without the <tt>&quot;DB_File&quot;</tt> module installed, it will have created files in other formats, such as <tt>&quot;GDBM_File&quot;</tt>, <tt>&quot;NDBM_File&quot;</tt>, or <tt>&quot;SDBM_File&quot;</tt>. This switch allows you to migrate that old data into the <tt>&quot;DB_File&quot;</tt> format. It will overwrite any data currently in the <tt>&quot;DB_File&quot;</tt>. </p>
<p> Can also be used with the <code>&#8211;dbpath</code> <i>path</i> option to specify the location of the Bayes files to use.</dl>
<h2>MIGRATION</h2>
<p> There are now multiple backend storage modules available for storing user&#8217;s bayesian data. As such you might want to migrate from one backend to another. Here is a simple procedure for migrating from one backend to another. </p>
<p> Note that if you have individual user databases you will have to perform a similar procedure for each one of them.</p>
<dl>
<dt>sa-learn &#8211;sync</p>
<dd> This will sync any outstanding journal entries</p>
<dt>sa-learn &#8211;backup &gt; backup.txt</p>
<dd> This will save all your Bayes data to a plain text file.</p>
<dt>sa-learn &#8211;clear</p>
<dd> This is optional, but good to do to clear out the old database.</p>
<dt>Repeat!</p>
<dd> At this point, if you have multiple databases, you should perform the procedure above for each of them. (i.e. each user&#8217;s database needs to be backed up before continuing.)</p>
<dt>Switch backends</p>
<dd> Once you have backed up all databases you can update your configuration for the new database backend. This will involve at least the bayes_store_module config option and may involve some additional config options depending on what is required by the module. (For example, you may need to configure an <font SIZE="-1">SQL</font> database.)</p>
<dt>sa-learn &#8211;restore backup.txt</p>
<dd> Again, you need to do this for every database.</dl>
<p> If you are migrating to <font SIZE="-1">SQL</font> you can make use of the -u &lt;username&gt; option in sa-learn to populate each user&#8217;s database. Otherwise, you must run sa-learn as the user who database you are restoring.</p>
<h2>INTRODUCTION TO BAYESIAN FILTERING</h2>
<p> (Thanks to Michael Bell for this section!) </p>
<p> For a more lengthy description of how this works, go to <a rel="nofollow" href="http://www.paulgraham.com/">http://www.paulgraham.com/</a> and see &#8220;A Plan for Spam&#8221;. It&#8217;s reasonably readable, even if statistics make me break out in hives. </p>
<p> The short semi-inaccurate version: Given training, a spam heuristics engine can take the most &#8220;spammy&#8221; and &#8220;hammy&#8221; words and apply probabilistic analysis. Furthermore, once given a basis for the analysis, the engine can continue to learn iteratively by applying both the non-Bayesian and Bayesian rulesets together to create evolving &#8220;intelligence&#8221;. </p>
<p> SpamAssassin 2.50 and later supports Bayesian spam analysis, in the form of the <font SIZE="-1">BAYES</font> rules. This is a new feature, quite powerful, and is disabled until enough messages have been learnt. </p>
<p> The pros of Bayesian spam analysis:</p>
<dl>
<dt>Can greatly reduce false positives and false negatives.</p>
<dd> It learns from your mail, so it is tailored to your unique e-mail flow.</p>
<dt>Once it starts learning, it can continue to learn from SpamAssassin and improve over time.</p>
<dd></dl>
<p> And the cons:</p>
<dl>
<dt>A decent number of messages are required before results are useful for ham/spam determination.</p>
<dd>
<dt>It&#8217;s hard to explain why a message is or isn&#8217;t marked as spam.</p>
<dd> i.e.: a straightforward rule, that matches, say, &#8220;<font SIZE="-1">VIAGRA&#8221;</font> is easy to understand. If it generates a false positive or false negative, it is fairly easy to understand why. </p>
<p> With Bayesian analysis, it&#8217;s all probabilities &#8211; &#8220;because the past says it is likely as this falls into a probabilistic distribution common to past spam in your systems&#8221;. Tell that to your users! Tell that to the client when he asks &#8220;what can I do to change this&#8221;. (By the way, the answer in this case is &#8220;use whitelisting&#8221;.)</p>
<dt>It will take disk space and memory.</p>
<dd> The databases it maintains take quite a lot of resources to store and use.</dl>
<h2>GETTING STARTED</h2>
<p> Still interested? Ok, here&#8217;s the guidelines for getting this working. </p>
<p> First a high-level overview:</p>
<dl>
<dt>Build a significant sample of both ham and spam.</p>
<dd> I suggest several thousand of each, placed in <font SIZE="-1">SPAM</font> and <font SIZE="-1">HAM</font> directories or mailboxes. Yes, you <font SIZE="-1">MUST</font> hand-sort this &#8211; otherwise the results won&#8217;t be much better than SpamAssassin on its own. Verify the spamminess/haminess of <font SIZE="-1">EVERY</font> message. You&#8217;re urged to avoid using a publicly available corpus (sample) &#8211; this must be taken from <font SIZE="-1">YOUR</font> mail server, if it is to be statistically useful. Otherwise, the results may be pretty skewed.</p>
<dt>Use this tool to teach SpamAssassin about these samples, like so:</p>
<dd>
<pre>
        sa-learn --spam /path/to/spam/folder
        sa-learn --ham /path/to/ham/folder
        ...
</pre>
<p> Let SpamAssassin proceed, learning stuff. When it finds ham and spam it will add the &#8220;interesting tokens&#8221; to the database.</p>
<dt>If you need SpamAssassin to forget about specific messages, use the <code>&#8211;forget</code> option.</p>
<dd> This can be applied to either ham or spam that has run through the <code>sa-learn</code> processes. It&#8217;s a bit of a hammer, really, lowering the weighting of the specific tokens in that message (only if that message has been processed before).</p>
<dt>Learning from single messages uses a command like this:</p>
<dd>
<pre>
        sa-learn --ham --no-sync mailmessage
</pre>
<p> This is handy for binding to a key in your mail user agent. It&#8217;s very fast, as all the time-consuming stuff is deferred until you run with the <tt>&quot;--sync&quot;</tt> option.</p>
<dt>Autolearning is enabled by default</p>
<dd> If you don&#8217;t have a corpus of mail saved to learn, you can let SpamAssassin automatically learn the mail that you receive. If you are autolearning from scratch, the amount of mail you receive will determine how long until the BAYES_* rules are activated.</dl>
<h2>EFFECTIVE TRAINING</h2>
<p> Learning filters require training to be effective. If you don&#8217;t train them, they won&#8217;t work. In addition, you need to train them with new messages regularly to keep them up-to-date, or their data will become stale and impact accuracy. </p>
<p> You need to train with both spam <i>and</i> ham mails. One type of mail alone will not have any effect. </p>
<p> Note that if your mail folders contain things like forwarded spam, discussions of spam-catching rules, etc., this will cause trouble. You should avoid scanning those messages if possible. (An easy way to do this is to move them aside, into a folder which is not scanned.) </p>
<p> If the messages you are learning from have already been filtered through SpamAssassin, the learner will compensate for this. In effect, it learns what each message would look like if you had run <tt>&quot;spamassassin -d&quot;</tt> over it in advance. </p>
<p> Another thing to be aware of, is that typically you should aim to train with at least 1000 messages of spam, and 1000 ham messages, if possible. More is better, but anything over about 5000 messages does not improve accuracy significantly in our tests. </p>
<p> Be careful that you train from the same source &#8212; for example, if you train on old spam, but new ham mail, then the classifier will think that a mail with an old date stamp is likely to be spam. </p>
<p> It&#8217;s also worth noting that training with a very small quantity of ham, will produce atrocious results. You should aim to train with at least the same amount (or more if possible!) of ham data than spam. </p>
<p> On an on-going basis, it is best to keep training the filter to make sure it has fresh data to work from. There are various ways to do this:</p>
<dl>
<dt>1. Supervised learning</p>
<dd> This means keeping a copy of all or most of your mail, separated into spam and ham piles, and periodically re-training using those. It produces the best results, but requires more work from you, the user. </p>
<p> (An easy way to do this, by the way, is to create a new folder for &#8216;deleted&#8217; messages, and instead of deleting them from other folders, simply move them in there instead. Then keep all spam in a separate folder and never delete it. As long as you remember to move misclassified mails into the correct folder set, it is easy enough to keep up to date.)</p>
<dt>2. Unsupervised learning from Bayesian classification</p>
<dd> Another way to train is to chain the results of the Bayesian classifier back into the training, so it reinforces its own decisions. This is only safe if you then retrain it based on any errors you discover. </p>
<p> SpamAssassin does not support this method, due to experimental results which strongly indicate that it does not work well, and since Bayes is only one part of the resulting score presented to the user (while Bayes may have made the wrong decision about a mail, it may have been overridden by another system).</p>
<dt>3. Unsupervised learning from SpamAssassin rules</p>
<dd> Also called &#8216;auto-learning&#8217; in SpamAssassin. Based on statistical analysis of the SpamAssassin success rates, we can automatically train the Bayesian database with a certain degree of confidence that our training data is accurate. </p>
<p> It should be supplemented with some supervised training in addition, if possible. </p>
<p> This is the default, but can be turned off by setting the SpamAssassin configuration parameter <tt>&quot;bayes_auto_learn&quot;</tt> to 0.</p>
<dt>4. Mistake-based training</p>
<dd> This means training on a small number of mails, then only training on messages that SpamAssassin classifies incorrectly. This works, but it takes longer to get it right than a full training session would.</dl>
<h2>FILES</h2>
<p> <code>sa-learn</code> and the other parts of SpamAssassin&#8217;s Bayesian learner, use a set of persistent database files to store the learnt tokens, as follows.</p>
<dl>
<dt>bayes_toks</p>
<dd> The database of tokens, containing the tokens learnt, their count of occurrences in ham and spam, and the timestamp when the token was last seen in a message. </p>
<p> This database also contains some &#8216;magic&#8217; tokens, as follows: the version number of the database, the number of ham and spam messages learnt, the number of tokens in the database, and timestamps of: the last journal sync, the last expiry run, the last expiry token reduction count, the last expiry timestamp delta, the oldest token timestamp in the database, and the newest token timestamp in the database. </p>
<p> This is a database file, using <tt>&quot;DB_File&quot;</tt>. The database &#8216;version number&#8217; is 0 for databases from 2.5x, 1 for databases from certain 2.6x development releases, 2 for 2.6x, and 3 for 3.0 and later releases.</p>
<dt>bayes_seen</p>
<dd> A map of Message-Id and some data from headers and body to what that message was learnt as. This is used so that SpamAssassin can avoid re-learning a message it has already seen, and so it can reverse the training if you later decide that message was learnt incorrectly. </p>
<p> This is a database file, using <tt>&quot;DB_File&quot;</tt>.</p>
<dt>bayes_journal</p>
<dd> While SpamAssassin is scanning mails, it needs to track which tokens it uses in its calculations. To avoid the contention of having each SpamAssassin process attempting to gain write access to the Bayes <font SIZE="-1">DB,</font> the token timestamps are written to a &#8216;journal&#8217; file which will later (either automatically or via <tt>&quot;sa-learn --sync&quot;</tt>) be used to synchronize the Bayes <font SIZE="-1">DB.</font> </p>
<p> Also, through the use of <tt>&quot;bayes_learn_to_journal&quot;</tt>, or when using the <tt>&quot;--no-sync&quot;</tt> option with sa-learn, the actual learning data will take be placed into the journal for later synchronization. This is typically useful for high-traffic sites to avoid the same contention as stated above.</dl>
<h2>EXPIRATION</h2>
<p> Since SpamAssassin can auto-learn messages, the Bayes database files could increase perpetually until they fill your disk. To control this, SpamAssassin performs journal synchronization and bayes expiration periodically when certain criteria (listed below) are met. </p>
<p> SpamAssassin can sync the journal and expire the <font SIZE="-1">DB</font> tokens either manually or opportunistically. A journal sync is due if <i>&#8211;sync</i> is passed to sa-learn (manual), or if the following is true (opportunistic):</p>
<dl>
<dt>&#8211; bayes_journal_max_size does not equal 0 (means don&#8217;t sync)</p>
<dd>
<dt>&#8211; the journal file exists</p>
<dd></dl>
<p> and either:</p>
<dl>
<dt>&#8211; the journal file has a size greater than bayes_journal_max_size</p>
<dd></dl>
<p> or</p>
<dl>
<dt>&#8211; a journal sync has previously occurred, and at least 1 day has passed since that sync</p>
<dd></dl>
<p> Expiry is due if <i>&#8211;force-expire</i> is passed to sa-learn (manual), or if all of the following are true (opportunistic):</p>
<dl>
<dt>&#8211; the last expire was attempted at least 12hrs ago</p>
<dd>
<dt>&#8211; bayes_auto_expire does not equal 0</p>
<dd>
<dt>&#8211; the number of tokens in the <font SIZE="-1">DB</font> is &gt; 100,000</p>
<dd>
<dt>&#8211; the number of tokens in the <font SIZE="-1">DB</font> is &gt; bayes_expiry_max_db_size</p>
<dd>
<dt>&#8211; there is at least a 12 hr difference between the oldest and newest token atimes</p>
<dd></dl>
<h3><font SIZE="-1">EXPIRE LOGIC</font></h3>
<p> If either the manual or opportunistic method causes an expire run to start, here is the logic that is used:</p>
<dl>
<dt>&#8211; figure out how many tokens to keep. take the larger of either bayes_expiry_max_db_size * 75% or 100,000 tokens. therefore, the goal reduction is number of tokens &#8211; number of tokens to keep.</p>
<dd>
<dt>&#8211; if the reduction number is &lt; 1000 tokens, abort (not worth the effort).</p>
<dd>
<dt>&#8211; if an expire has been done before, guesstimate the new atime delta based on the old atime delta. (new_atime_delta = old_atime_delta * old_reduction_count / goal)</p>
<dd>
<dt>&#8211; if no expire has been done before, or the last expire looks &quot;weird&quot;, do an estimation pass. The definition of &quot;weird&quot; is:</p>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt>&#8211; last expire over 30 days ago</p>
<dd>
<dt>&#8211; last atime delta was &lt; 12 hrs</p>
<dd>
<dt>&#8211; last reduction count was &lt; 1000 tokens</p>
<dd>
<dt>&#8211; estimated new atime delta is &lt; 12 hrs</p>
<dd>
<dt>&#8211; the difference between the last reduction count and the goal reduction count is &gt; 50%</p>
<dd></dl>
</dl>
<dl>
<dt>
<dd></dl>
</dl>
<h3><font SIZE="-1">ESTIMATION PASS LOGIC</font></h3>
<p> Go through each of the <font SIZE="-1">DB</font>&#8216;s tokens. Starting at 12hrs, calculate whether or not the token would be expired (based on the difference between the token&#8217;s atime and the db&#8217;s newest token atime) and keep the count. Work out from 12hrs exponentially by powers of 2. ie: 12hrs * 1, 12hrs * 2, 12hrs * 4, 12hrs * 8, and so on, up to 12hrs * 512 (6144hrs, or 256 days). </p>
<p> The larger the delta, the smaller the number of tokens that will be expired. Conversely, the number of tokens goes up as the delta gets smaller. So starting at the largest atime delta, figure out which delta will expire the most tokens without going above the goal expiration count. Use this to choose the atime delta to use, unless one of the following occurs:</p>
<dl>
<dt>&#8211; the largest atime (smallest reduction count) would expire too many tokens. this means the learned tokens are mostly old and there needs to be new tokens learned before an expire can occur.</p>
<dd>
<dt>&#8211; all of the atime choices result in 0 tokens being removed. this means the tokens are all newer than 12 hours and there needs to be new tokens learned before an expire can occur.</p>
<dd>
<dt>&#8211; the number of tokens that would be removed is &lt; 1000. the benefit isn&#8217;t worth the effort. more tokens need to be learned.</p>
<dd></dl>
<p> If the expire run gets past this point, it will continue to the end. A new <font SIZE="-1">DB</font> is created since the majority of <font SIZE="-1">DB</font> libraries don&#8217;t shrink the <font SIZE="-1">DB</font> file when tokens are removed. So we do the &#8220;create new, migrate old to new, remove old, rename new&#8221; shuffle.</p>
<h3><font SIZE="-1">EXPIRY RELATED CONFIGURATION SETTINGS</font></h3>
<dl>
<dt>&quot;bayes_auto_expire&quot; is used to specify whether or not SpamAssassin ought to opportunistically attempt to expire the Bayes database. The default is 1 (yes).</p>
<dd>
<dt>&quot;bayes_expiry_max_db_size&quot; specifies both the auto-expire token count point, as well as the resulting number of tokens after expiry as described above. The default value is 150,000, which is roughly equivalent to a 6Mb database file if you&#8217;re using DB_File.</p>
<dd>
<dt>&quot;bayes_journal_max_size&quot; specifies how large the Bayes journal will grow before it is opportunistically synced. The default value is 102400.</p>
<dd></dl>
<h2>INSTALLATION</h2>
<p> The <code>sa-learn</code> command is part of the <code>Mail::SpamAssassin</code> Perl module. Install this as a normal Perl module, using <tt>&quot;perl -MCPAN -e shell&quot;</tt>, or by hand.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-spamassassin/">spamassassin</a></i>(1) <i><a href="/docs/linux/man/1-spamc/">spamc</a></i>(1) <i><a href="/docs/linux/man/3-mail--spamassassin/">Mail::SpamAssassin</a></i>(3) <i><a href="/docs/linux/man/3-mail--spamassassin--archiveiterator/">Mail::SpamAssassin::ArchiveIterator</a></i>(3) </p>
<p> &lt;<a rel="nofollow" href="http://www.paulgraham.com/">http://www.paulgraham.com/</a>&gt; Paul Graham&#8217;s &#8220;A Plan For Spam&#8221; paper </p>
<p> &lt;<a rel="nofollow" href="http://www.linuxjournal.com/article/6467">http://www.linuxjournal.com/article/6467</a>&gt; Gary Robinson&#8217;s f(x) and combining algorithms, as used in SpamAssassin </p>
<p> &lt;<a rel="nofollow" href="http://www.bgl.nu/~glouis/bogofilter/">http://www.bgl.nu/~glouis/bogofilter/</a>&gt; &#8216;Training on error&#8217; page. A discussion of various Bayes training regimes, including &#8216;train on error&#8217; and unsupervised training.</p>
<h2>PREREQUISITES</h2>
<p> <tt>&quot;Mail::SpamAssassin&quot;</tt></p>
<h2>AUTHORS</h2>
<p> The SpamAssassin(tm) Project &lt;<a rel="nofollow" href="http://spamassassin.apache.org/">http://spamassassin.apache.org/</a>&gt; </p>
<h2>Index</h2>
<dt><a href="#lbAO">INSTALLATION</a></p>
<dd>
<dt><a href="#lbAP">SEE ALSO</a></p>
<dd>
<dt><a href="#lbAQ">PREREQUISITES</a></p>
<dd>
<dt><a href="#lbAR">AUTHORS</a></p>
<dd></dl>
