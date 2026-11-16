---
title: "sks(8)"
name: "sks"
section: "8"
letter: "s"
url: "/docs/linux/man/8-sks/"
---

SKS - Synchronizing Key Server

<h2>Synopsis</h2>

sks [options] -debug

<h2>Description</h2>

<font SIZE="-1">SKS</font> is a OpenPGP keyserver whose goal is to provide easy to deploy, decentralized, and highly reliable synchronization. That means that a key submitted to one <font SIZE="-1">SKS</font> server will quickly be distributed to all key servers, and even wildly out-of-date servers, or servers that experience spotty connectivity, can fully synchronize with rest of the system. 

 The design of <font SIZE="-1">SKS</font> is deliberately simple. The server consists of two single-threaded processes. The first, ``sks db'', fulfills the normal jobs associated with a public key server, such as answering web requests. The only special functionality of ``sks db'' is that it keeps a log summarizing the changes to the key database. ``sks recon'' does all the work with respect to reconciling hosts databases. ``sks recon'' keeps track of specialized summary information about the database, and can use that information to efficiently determine the differences between its database and that of another host.

<h2>Features</h2>

Highly efficient and reliable reconciliation algorithm 

 Follows <font SIZE="-1">RFC2440</font> and RFC2440bis carefully - unlike <font SIZE="-1">PKS, SKS</font> supports new and old style packets, photoID packets, multiple subkeys, and pretty much everything allowed by the RFCs. 

 Fully compatible with <font SIZE="-1">PKS</font> system - can both send and receive syncs from <font SIZE="-1">PKS</font> servers, ensuring seamless connectivity. 

 Simple configuration: each host just needs a (partial) list of the other participating key servers. Gossip is used to distribute information without putting a heavy load an any one host. 

 Supports HKP/web-based querying, and soon-to-be-standard machine readable indices

<h2>Options</h2>

<font SIZE="-1">SKS</font> binary command options are as follows:
<dl><dt>db
</dt><dd><pre> Initiates database server.</pre></dd><dt>recon
</dt><dd>Initiates reconciliation server.
</dd><dt>cleandb
</dt><dd>Apply filters to all keys in database, fixing some common problems.
</dd><dt>build
</dt><dd>Build key database, including body of keys directly in database.
</dd><dt>fastbuild -n [size] -cache [mbytes]
</dt><dd>Build key database, doesn't include keys directly in database, faster than build. -n specifies the number of keydump files to read per pass when used with build and the multiple of 15,000 keys to be read per pass when used with fastbuild. -cache specifies the database cache to use in megabytes.
</dd><dt>pbuild -cache [mbytes] -ptree_cache [mbytes]
</dt><dd>Build prefix-tree database, used by reconciliation server, from key database. Allows for specification of cache for key database and for ptree database.
</dd><dt>dump numkeys dumpdir &lt;filename-prefix&gt;
</dt><dd>Create a raw dump of the keys in the database. The dump is split into multiple files; the numkeys parameter determines the number of keys dumped in each file. The optional filename-prefix is prepended to the dump file names. Without it the dump files are named 0000.pgp, 0001.pgp,...
</dd><dt>merge
</dt><dd>Adds key from key files to existing database.
</dd><dt>drop
</dt><dd>Drops key from database.
</dd><dt>update_subkeys [-n # of updates / 1000]
</dt><dd>Updates subkey keyid index to include all current keys. Only useful when upgrading versions 1.0.4 or before of <font SIZE="-1">SKS.</font>
</dd><dt>version
</dt><dd>prints <font SIZE="-1">SKS</font> version and linked version of Berkeley <font SIZE="-1">DB</font> to stdout
</dd><dt>help
</dt><dd>Prints the help message.</dd></dl>

<h2>Additional Options</h2>

You won't need most of the options below for normal operation. These options can be given in basedir/sksconf or as command line option for the sks binary.
<dl><dt>-debug
</dt><dd>Debugging mode.
</dd><dt>-debuglevel
</dt><dd>Debugging level --- sets verbosity of logging.
</dd><dt>-q
</dt><dd><pre> Number of bits defining a bin.</pre></dd><dt>-mbar
</dt><dd>Number of errors that can be corrected in one shot.
</dd><dt>-seed
</dt><dd>Seed used by <font SIZE="-1">RNG.</font>
</dd><dt>-hostname
</dt><dd>Current hostname.
</dd><dt>-nodename
</dt><dd>Current nodename.
</dd><dt>-d
</dt><dd><pre> Number of keys to drop at random when synchronizing.</pre></dd><dt>-n
</dt><dd><pre> Number of keydump files to load at once.</pre></dd><dt>-max_internal_matches
</dt><dd>Maximum number of matches for most specific word in a multi-word search.
</dd><dt>-max_matches
</dt><dd>Maximum number of matches that will be returned from a query.
</dd><dt>-max_uid_fetches
</dt><dd>Maximum number of uid fetches performed in a verbose index query.
</dd><dt>-pagesize
</dt><dd>Pagesize in 512 byte chucks for key db.
</dd><dt>-keyid_pagesize
</dt><dd>Pagesize in 512 byte chucks for keyid db.
</dd><dt>-meta_pagesize
</dt><dd>Pagesize in 512 byte chucks for metadata db.
</dd><dt>-subkeyid_pagesize
</dt><dd>Pagesize in 512 byte chucks for subkeyid db.
</dd><dt>-time_pagesize
</dt><dd>Pagesize in 512 byte chucks for time db.
</dd><dt>-tqueue_pagesize
</dt><dd>Pagesize in 512 byte chucks for tqueue db.
</dd><dt>-word_pagesize
</dt><dd>Pagesize in 512 byte chunks for word db.
</dd><dt>-cache
</dt><dd>Cache size in megs for key db.
</dd><dt>-ptree_pagesize
</dt><dd>Pagesize in 512 byte chunks for prefix tree db.
</dd><dt>-ptree_cache
</dt><dd>Cache size in megs for prefix tree db.
</dd><dt>-baseport
</dt><dd>Set base port number.
</dd><dt>-recon_port
</dt><dd>Set recon port number.
</dd><dt>-recon_address
</dt><dd>Set recon binding addresses. Can be a list of whitespace separated <font SIZE="-1">IP</font> addresses or domain names.
</dd><dt>-hkp_port
</dt><dd>Set hkp port number.
</dd><dt>-hkp_address
</dt><dd>Set hkp binding addresses. Can be a list of whitespace separated <font SIZE="-1">IP</font> addresses or domain names.
</dd><dt>-use_port_80
</dt><dd>Have the <font SIZE="-1">HKP</font> interface listen on port 80, as well as the hkp_port.
</dd><dt>-basedir
</dt><dd>Set base directory.
</dd><dt>-stdoutlog
</dt><dd>Send log messages to stdout instead of log file.
</dd><dt>-diskptree
</dt><dd>Use a disk-based ptree implementation. Slower, but requires far less memory.
</dd><dt>-nodiskptree
</dt><dd>Use in-mem ptree.
</dd><dt>-max_ptree_nodes
</dt><dd>Maximum number of allowed ptree nodes. Only meaningful if -diskptree is set.
</dd><dt>-prob
</dt><dd>Set probability. Used for testing code only.
</dd><dt>-recon_sync_interval
</dt><dd>Set sync interval for reconserver.
</dd><dt>-gossip_interval
</dt><dd>Set time between gossips in minutes.
</dd><dt>-dontgossip
</dt><dd>Don't gossip automatically. Host will still respond to requests from other hosts.
</dd><dt>-db_sync_interval
</dt><dd>Set sync interval for dbserver.
</dd><dt>-checkpoint_interval
</dt><dd>Time period between checkpoints.
</dd><dt>-recon_checkpoint_interval
</dt><dd>Time period between checkpoints for reconserver.
</dd><dt>-ptree_thresh_mult
</dt><dd>Multiple of thresh which specifies minimum node size in prefix tree.
</dd><dt>-recon_thresh_mult
</dt><dd>Multiple of thresh which specifies minimum node size that is included in reconciliation.
</dd><dt>-max_recover
</dt><dd>Maximum number of differences to recover in one round.
</dd><dt>-http_fetch_size
</dt><dd>Number of keys for reconserver to fetch from dbserver in one go.
</dd><dt>-wserver_timeout
</dt><dd>Timeout in seconds for webserver requests.
</dd><dt>-reconciliation_timeout
</dt><dd>Timeout for reconciliation runs in minutes.
</dd><dt>-stat_hour
</dt><dd>Hour at which to run database statistics.
</dd><dt>-initial_stat
</dt><dd>Runs database statistics calculation on boot.
</dd><dt>-reconciliation_config_timeout
</dt><dd>Set timeout in seconds for initial exchange of config info in reconciliation.
</dd><dt>-missing_keys_timeout
</dt><dd>Timeout in seconds for get_missing_keys.
</dd><dt>-command_timeout
</dt><dd>Timeout in seconds for commands set over command socket.
</dd><dt>-sendmail_cmd
</dt><dd>Command used for sending mail.
</dd><dt>-from_addr
</dt><dd>From address used in synchronization emails used to communicate with <font SIZE="-1">PKS.</font>
</dd><dt>-dump_new_only
</dt><dd>When doing a database dump, only dump new keys, not keys already contained in a keydump file.
</dd><dt>-max_outstanding_recon_requests
</dt><dd>Maximum number of outstanding requests in reconciliation.
</dd><dt>-membership_reload_interval
</dt><dd>Maximum interval (in hours) at which membership file is reloaded.
</dd><dt>-disable_mailsync
</dt><dd>Disable sending of <font SIZE="-1">PKS</font> mailsync messages. <font SIZE="-1">ONLY FOR STANDALONE SERVERS</font>! <font SIZE="-1">THIS IS THE MECHANIASM FOR SENDING UPDATES TO</font> NON-SKS <font SIZE="-1">SERVERS.</font>
</dd><dt>-disable_log_diffs
</dt><dd>Disable logging of recent hashset diffs.
</dd><dt>-server_contact
</dt><dd>Set OpenPGP KeyID of the server contact
</dd><dt>--help, -help
</dt><dd></dd><dt>-stdin
</dt><dd>Read keyids from stdin (sksclient only) 
 Displays list of options.</dd></dl>

<h2>Files</h2>

Information about important files located in your <font SIZE="-1">SKS</font> basedir.
<dl><dt>bin/sks
</dt><dd>The main <font SIZE="-1">SKS</font> executable.
</dd><dt>bin/sks_add_mail
</dt><dd>The executable responsible for parsing incoming mails from <font SIZE="-1">PKS</font> key servers.
</dd><dt>bin/sks_build.sh
</dt><dd>Script to generate an initial database.
</dd><dt>mailsync
</dt><dd>The mailsync should contains a list of email addresses of <font SIZE="-1">PKS</font> keyservers. This file is important, because it ensures that keys submitted directly to an <font SIZE="-1">SKS</font> keyserver are also forwarded to <font SIZE="-1">PKS</font> keyservers. <font SIZE="-1">IMPORTANT :</font> don't add someone to your mailsync file without getting their permission first!
</dd><dt>membership
</dt><dd>With <font SIZE="-1">SKS,</font> two hosts can efficiently compare their databases then repair whatever differences are found. In order to set up reconciliation, you first need to find other <font SIZE="-1">SKS</font> servers that will agree to gossip with you. The hostname and port of the server that has agreed to do so should be added to this file.
</dd><dt>sksconf
</dt><dd>The configuration file for your <font SIZE="-1">SKS</font> server.</dd></dl>

<h2>Examples</h2>

<pre><code>membership
keyserver.ahost.org 11370 # Comments are allowed
keyserver.foo.org 11370   # Another host with default ports
sksconf
membership_reload_interval: 1
initial_stat:
hostname: keyserver.example.com
from_addr: pgp-public-keys [at] keyserver.example.com
Procmail
PATH=/path/of/sks/exectuables
:0
* ^Subject: incremental
| /path/of/sks_add_mail /path/to/sks/directory
/etc/aliases
pgp-public-keys:      &quot;|/path/of/sks_add_mail /path/to/sks/directory&quot;</code></pre>

<h2>See Also</h2>

<pre> The SKS website is located at <a rel="nofollow" HREF="https://bitbucket.org/skskeyserver/sks-keyserver/.">https://bitbucket.org/skskeyserver/sks-keyserver/.</a></pre>

<h2>Author</h2>

The first draft was written by Thomas Sjogren &lt;thomas [at] northernsecurity.net&gt;.
