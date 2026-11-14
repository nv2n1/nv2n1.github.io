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
<dd><pre> Initiates database server.</pre><dt>recon
<dd>Initiates reconciliation server.
<dt>cleandb
<dd>Apply filters to all keys in database, fixing some common problems.
<dt>build
<dd>Build key database, including body of keys directly in database.
<dt>fastbuild -n [size] -cache [mbytes]
<dd>Build key database, doesn't include keys directly in database, faster than build. -n specifies the number of keydump files to read per pass when used with build and the multiple of 15,000 keys to be read per pass when used with fastbuild. -cache specifies the database cache to use in megabytes.
<dt>pbuild -cache [mbytes] -ptree_cache [mbytes]
<dd>Build prefix-tree database, used by reconciliation server, from key database. Allows for specification of cache for key database and for ptree database.
<dt>dump numkeys dumpdir &lt;filename-prefix&gt;
<dd>Create a raw dump of the keys in the database. The dump is split into multiple files; the numkeys parameter determines the number of keys dumped in each file. The optional filename-prefix is prepended to the dump file names. Without it the dump files are named 0000.pgp, 0001.pgp,...
<dt>merge
<dd>Adds key from key files to existing database.
<dt>drop
<dd>Drops key from database.
<dt>update_subkeys [-n # of updates / 1000]
<dd>Updates subkey keyid index to include all current keys. Only useful when upgrading versions 1.0.4 or before of <font SIZE="-1">SKS.</font>
<dt>version
<dd>prints <font SIZE="-1">SKS</font> version and linked version of Berkeley <font SIZE="-1">DB</font> to stdout
<dt>help
<dd>Prints the help message.</dl>

<h2>Additional Options</h2>

You won't need most of the options below for normal operation. These options can be given in basedir/sksconf or as command line option for the sks binary.
<dl><dt>-debug
<dd>Debugging mode.
<dt>-debuglevel
<dd>Debugging level --- sets verbosity of logging.
<dt>-q
<dd><pre> Number of bits defining a bin.</pre><dt>-mbar
<dd>Number of errors that can be corrected in one shot.
<dt>-seed
<dd>Seed used by <font SIZE="-1">RNG.</font>
<dt>-hostname
<dd>Current hostname.
<dt>-nodename
<dd>Current nodename.
<dt>-d
<dd><pre> Number of keys to drop at random when synchronizing.</pre><dt>-n
<dd><pre> Number of keydump files to load at once.</pre><dt>-max_internal_matches
<dd>Maximum number of matches for most specific word in a multi-word search.
<dt>-max_matches
<dd>Maximum number of matches that will be returned from a query.
<dt>-max_uid_fetches
<dd>Maximum number of uid fetches performed in a verbose index query.
<dt>-pagesize
<dd>Pagesize in 512 byte chucks for key db.
<dt>-keyid_pagesize
<dd>Pagesize in 512 byte chucks for keyid db.
<dt>-meta_pagesize
<dd>Pagesize in 512 byte chucks for metadata db.
<dt>-subkeyid_pagesize
<dd>Pagesize in 512 byte chucks for subkeyid db.
<dt>-time_pagesize
<dd>Pagesize in 512 byte chucks for time db.
<dt>-tqueue_pagesize
<dd>Pagesize in 512 byte chucks for tqueue db.
<dt>-word_pagesize
<dd>Pagesize in 512 byte chunks for word db.
<dt>-cache
<dd>Cache size in megs for key db.
<dt>-ptree_pagesize
<dd>Pagesize in 512 byte chunks for prefix tree db.
<dt>-ptree_cache
<dd>Cache size in megs for prefix tree db.
<dt>-baseport
<dd>Set base port number.
<dt>-recon_port
<dd>Set recon port number.
<dt>-recon_address
<dd>Set recon binding addresses. Can be a list of whitespace separated <font SIZE="-1">IP</font> addresses or domain names.
<dt>-hkp_port
<dd>Set hkp port number.
<dt>-hkp_address
<dd>Set hkp binding addresses. Can be a list of whitespace separated <font SIZE="-1">IP</font> addresses or domain names.
<dt>-use_port_80
<dd>Have the <font SIZE="-1">HKP</font> interface listen on port 80, as well as the hkp_port.
<dt>-basedir
<dd>Set base directory.
<dt>-stdoutlog
<dd>Send log messages to stdout instead of log file.
<dt>-diskptree
<dd>Use a disk-based ptree implementation. Slower, but requires far less memory.
<dt>-nodiskptree
<dd>Use in-mem ptree.
<dt>-max_ptree_nodes
<dd>Maximum number of allowed ptree nodes. Only meaningful if -diskptree is set.
<dt>-prob
<dd>Set probability. Used for testing code only.
<dt>-recon_sync_interval
<dd>Set sync interval for reconserver.
<dt>-gossip_interval
<dd>Set time between gossips in minutes.
<dt>-dontgossip
<dd>Don't gossip automatically. Host will still respond to requests from other hosts.
<dt>-db_sync_interval
<dd>Set sync interval for dbserver.
<dt>-checkpoint_interval
<dd>Time period between checkpoints.
<dt>-recon_checkpoint_interval
<dd>Time period between checkpoints for reconserver.
<dt>-ptree_thresh_mult
<dd>Multiple of thresh which specifies minimum node size in prefix tree.
<dt>-recon_thresh_mult
<dd>Multiple of thresh which specifies minimum node size that is included in reconciliation.
<dt>-max_recover
<dd>Maximum number of differences to recover in one round.
<dt>-http_fetch_size
<dd>Number of keys for reconserver to fetch from dbserver in one go.
<dt>-wserver_timeout
<dd>Timeout in seconds for webserver requests.
<dt>-reconciliation_timeout
<dd>Timeout for reconciliation runs in minutes.
<dt>-stat_hour
<dd>Hour at which to run database statistics.
<dt>-initial_stat
<dd>Runs database statistics calculation on boot.
<dt>-reconciliation_config_timeout
<dd>Set timeout in seconds for initial exchange of config info in reconciliation.
<dt>-missing_keys_timeout
<dd>Timeout in seconds for get_missing_keys.
<dt>-command_timeout
<dd>Timeout in seconds for commands set over command socket.
<dt>-sendmail_cmd
<dd>Command used for sending mail.
<dt>-from_addr
<dd>From address used in synchronization emails used to communicate with <font SIZE="-1">PKS.</font>
<dt>-dump_new_only
<dd>When doing a database dump, only dump new keys, not keys already contained in a keydump file.
<dt>-max_outstanding_recon_requests
<dd>Maximum number of outstanding requests in reconciliation.
<dt>-membership_reload_interval
<dd>Maximum interval (in hours) at which membership file is reloaded.
<dt>-disable_mailsync
<dd>Disable sending of <font SIZE="-1">PKS</font> mailsync messages. <font SIZE="-1">ONLY FOR STANDALONE SERVERS</font>! <font SIZE="-1">THIS IS THE MECHANIASM FOR SENDING UPDATES TO</font> NON-SKS <font SIZE="-1">SERVERS.</font>
<dt>-disable_log_diffs
<dd>Disable logging of recent hashset diffs.
<dt>-server_contact
<dd>Set OpenPGP KeyID of the server contact
<dt>--help, -help
<dd><dt>-stdin
<dd>Read keyids from stdin (sksclient only) 

 Displays list of options.</dl>

<h2>Files</h2>

Information about important files located in your <font SIZE="-1">SKS</font> basedir.
<dl><dt>bin/sks
<dd>The main <font SIZE="-1">SKS</font> executable.
<dt>bin/sks_add_mail
<dd>The executable responsible for parsing incoming mails from <font SIZE="-1">PKS</font> key servers.
<dt>bin/sks_build.sh
<dd>Script to generate an initial database.
<dt>mailsync
<dd>The mailsync should contains a list of email addresses of <font SIZE="-1">PKS</font> keyservers. This file is important, because it ensures that keys submitted directly to an <font SIZE="-1">SKS</font> keyserver are also forwarded to <font SIZE="-1">PKS</font> keyservers. <font SIZE="-1">IMPORTANT :</font> don't add someone to your mailsync file without getting their permission first!
<dt>membership
<dd>With <font SIZE="-1">SKS,</font> two hosts can efficiently compare their databases then repair whatever differences are found. In order to set up reconciliation, you first need to find other <font SIZE="-1">SKS</font> servers that will agree to gossip with you. The hostname and port of the server that has agreed to do so should be added to this file.
<dt>sksconf
<dd>The configuration file for your <font SIZE="-1">SKS</font> server.</dl>

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
