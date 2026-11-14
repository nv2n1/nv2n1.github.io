---
title: "ods-ksmutil(1)"
name: "ods-ksmutil"
section: "1"
letter: "o"
url: "/docs/linux/man/1-ods-ksmutil/"
description: "ods-ksmutil – OpenDNSSEC zone and key management"
---

<h2>NAME</h2>
<p> <code>ods-ksmutil</code> &#8211; OpenDNSSEC zone and key management</p>
<h2>SYNOPSIS</h2>
<p> <code>ods-ksmutil setup</code><br />
 <code>ods-ksmutil start|stop|notify</code><br />
 <code>ods-ksmutil update kasp|zonelist|conf|all</code><br />
 <code>ods-ksmutil zone add|delete|list</code> &#8230;<br />
 <code>ods-ksmutil zonelist import|export</code><br />
 <code>ods-ksmutil key generate|import|export|list|purge|rollover|ksk-retire|ds-seen|delete</code> &#8230;<br />
 <code>ods-ksmutil rollover list</code> &#8230;<br />
 <code>ods-ksmutil policy export|import|purge</code> &#8230;<br />
 <code>ods-ksmutil repository list</code> &#8230;<br />
 <code>ods-ksmutil backup list|prepare|commit|rollback|done</code><br />
 <code>ods-ksmutil database backup</code> &#8230;</p>
<h2>DESCRIPTION</h2>
<p> <i>ods-ksmutil</i> manages the operation of the KASP Enforcer, which is the part of OpenDNSSEC that triggers key generation and signing operations on domains based on policies with user-defined timing and security requirements. Since everything beyond this management utility is usually automatic, <i>ods-ksmutil</i> is the primary tool for managing OpenDNSSEC. Among the functions of <i>ods-ksmutil</i> are key management, updates to the zone list and manually rolling keys to recover from exceptional situations like key loss. </p>
<p> To get started, a first invocation of <i>ods-ksmutil setup</i> is needed; see SETUP AND UPDATE COMMANDS below for details. After this is done, the rest of the functionality of <i>ods-ksmutil</i> becomes available. </p>
<p> The following sections discuss the subcommands in logical groups, detailing any options that they support.</p>
<h2>GENERIC OPTIONS</h2>
<dl>
<dt><code>-c </code><i>configfile</i><code>, &#8211;config </code><i>configfile</i></p>
<dd> Change the conf.xml file that is used from the default.</p>
<dt><code>help</code></p>
<dd> This can be used as a subcommand to <i>ods-ksmutil</i> or it can be used after a partial subcommand. In response, <i>ods-ksmutil</i> will give a synopsis of how to continue the command.</p>
<dt><code>-V, &#8211;version</code></p>
<dd> Display version number</dl>
<h2>SETUP AND UPDATE SUBCOMMANDS</h2>
<dl>
<dt><code>setup</code></p>
<dd> Import conf.xml, kasp.xml and zonelist.xml into a database. This deletes any current management information from the database with OpenDNSSEC management information, including any references to keys. Updates to an existing setup should therefore not normally run this subcommand, but <code>update</code> instead.</p>
<dt><code>update kasp</code></p>
<dd>
<dt><code>update zonelist</code></p>
<dd>
<dt><code>update conf</code></p>
<dd>
<dt><code>update all</code></p>
<dd> Update the database with the contents of the respective configuration file, or all those files. The result is comparable to the <code>setup</code> subcommand, except that management information about OpenDNSSEC is not deleted.(Also note that update kasp does not remove any policies from the database, policy purge can be used to remove unused policies).</dl>
<h2>ZONE MANAGEMENT SUBCOMMANDS</h2>
<dl>
<dt><code>zone add &#8211;zone|-z </code><i>zone</i><code> [&#8211;policy|-p </code><i>name</i><code>] [&#8211;in-type|-j </code><i>type</i><code>] [&#8211;out-type|-q </code><i>type</i><code>] [&#8211;input|-i </code><i>input</i><code>] [&#8211;output|-o </code><i>output</i><code>] [&#8211;no-xml]</code></p>
<dd> Add a zone to both zonelist.xml and the database. This is equivalent to manually editing zonelist.xml and then running the <code>update zonelist</code> subcommand. The &#8211;zone option names the zone to add; the &#8211;policy option names the policy to use instead of default; the &#8211;in-type and &#8211;out-type specify the type of input and output adapters (should be DNS or File, default is File); the &#8211;input option specifies a non-standard location for the unsigned zone (default is /var/opendnssec/unsigned/ZONE) or the DNS input file(default is /etc/opendnssec/addns.xml); the &#8211;output option specifies a non-standard location for the signed zone (default is /var/opendnssec/signed/ZONE) or the DNS output file(default is /etc/opendnssec/addns.xml). The &#8211;no-xml flag stops the zonelist.xml file from being updated. This is suitable for a batch mode where you will add multiple zones and then just write zonelist once at the end.</p>
<dt><code>zone delete &#8211;zone|-z </code><i>name</i><code> [&#8211;no-xml]</code></p>
<dd>
<dt><code>zone delete &#8211;all|-a</code></p>
<dd> Delete one zone (or all zones, respectively) from both zonelist.xml and the database. This is equivalent to manually editing zonelist.xml and then running the <code>update zonelist</code> subcommand. The &#8211;no-xml flag stops the zonelist.xml file from being updated. This is suitable for a batch mode where you will delete multiple zones and then just write zonelist once at the end.</p>
<dt><code>zone list</code></p>
<dd> List zones from the zonelist.xml. TODO:Not from the database?</p>
<dt><code>zonelist export</code></p>
<dd> Export list of zones from the database in the same format as zonelist.xml</p>
<dt><code>zonelist import</code></p>
<dd> Synchronise the database with the contents of zonelist.xml; identical to &quot;update zonelist&quot;</dl>
<h2>KEY MANAGEMENT SUBCOMMANDS</h2>
<dl>
<dt><code>key generate &#8211;policy|-p </code><i>name</i><code> &#8211;interval|-n </code><i>interval</i><code> [&#8211;zonetotal|-Z </code><i>zonetotal</i><code>]</code></p>
<dd> Create enough keys for the named policy to last for the period of time given by interval. See INTERVAL FORMAT for the format of timing specifications. </p>
<p> If configured to, OpenDNSSEC will automatically create keys when the need arises. This command can be used to pregenerate keys (maybe for the expected lifetime of an HSM) to help with backup policies. It is also a convenient method of pregenerating a set of keys to allow a disaster recovery site to have a copy of the keys without needed to synchronise keys generated on the fly. </p>
<p> By default the command generates keys for all the zones found on the specified policy. If the optional parameter &#8211;zonetotal is specified then keys will be generated for that total number of zones, regardless of how many are actually currently on the policy.</p>
<dt><code>key import &#8211;algorithm|-g </code><i>algname</i><code> &#8211;bits|-b </code><i>bits</i><code> &#8211;repository|-r </code><i>repo</i><code> &#8211;cka_id|-k </code><i>ckaid</i><code> &#8211;zone|-z </code><i>zone</i><code> &#8211;keytype|-t </code><i>type</i><code> &#8211;keystate|-e </code><i>state</i><code> &#8211;time|-w </code><i>time</i><code> [&#8211;check-repository|-C </code><i>checkrepository</i><code>] [&#8211;retire|-y </code><i>time</i><code>]</code></p>
<dd> Add a key which was created outside of the OpenDNSSEC code into the database. In doing so, the further details involved in key management must be specified in options. </p>
<p> The &#8211;algorithm option names the algorithm used with this key; the &#8211;bits specifies the strength of this algorithm as a key size in bits. </p>
<p> The &#8211;repository option names the repository in which the key should be stored; the &#8211;cka_id option specifies the name that will be used to identify this key in that repository; the &#8211;zone option specifies the zone for which this key is to be used; the &#8211;keytype option specifies whether this key should serve as a KSK or a ZSK. See KEY TYPES below for an introduction to these terms. </p>
<p> The &#8211;keystate option specifies the state in which the key will be after import, and must be one of the options defined in the KEY STATES section below. the &#8211;time option specifies the time that this key was created; the &#8211;check-repository option specified that the key import should fail if no matching key with the specified cka_id exists in the Repository. the &#8211;retire option specifies the time that this key should be retired. These last two options take the formats given in the TIME FORMATS section below.</p>
<dt><code>key export &#8211;zone|-z </code><i>name</i><code> [&#8211;keystate|-e </code><i>state</i><code>] [&#8211;keytype|-t </code><i>type</i><code>] [&#8211;ds]</code></p>
<dd>
<dt><code>key export &#8211;all [&#8211;keystate|-e </code><i>state</i><code>] [&#8211;keytype|-t </code><i>type</i><code>] [&#8211;ds]</code></p>
<dd> Export the keys for a particular zone, or for all zones respectively, from the database. The &#8211;ds option can be used to retrieve DS records for upload to a registry instead of the full key; the &#8211;keystate option can be used to limit the output to keys in a given state; the &#8211;keytype option can be used to limit the output to keys of a given type. See the <i>KEY TYPES and KEY STATES sections below for a specification of possible </i> key types and states.</p>
<dt><code>key list [&#8211;zone name] [&#8211;verbose] [&#8211;keystate|&#8211;all|-e </code><i>state</i><code>|-a] [&#8211;keytype </code><i>type</i><code>|-t </code><i>type</i><code>]</code></p>
<dd> List information about keys in all zones, or in a particular zone. By default keys in the GENERATE and DEAD state are not displayed. </p>
<p> The &#8211;verbose option is used to list additional information about each key. </p>
<p> The &#8211;keystate option can be used to limit the output to keys in a given state. If the &#8211;all option is used then keys in all states (including GENERATE and DEAD) are displayed. The &#8211;keytype option can be used to limit the output to keys of a given type. See the <i>KEY TYPES and KEY STATES sections below for a specification of possible </i> key types and states.</p>
<dt><code>key purge &#8211;zone|-z </code><i>name</i></p>
<dd>
<dt><code>key purge &#8211;policy|-p </code><i>name</i></p>
<dd> Remove any keys in the Dead state from the repository and from the database of the KASP Enforcer. The options &#8211;zone and &#8211;policy are used to limit this operation to a single named zone or policy, respectively.</p>
<dt><code>key rollover &#8211;zone|-z </code><i>name</i><code> &#8211;keytype </code><i>type</i><code>|-t </code><i>type</i></p>
<dd>
<dt><code>key rollover &#8211;zone|-z </code><i>name</i><code> &#8211;all|-a</code></p>
<dd>
<dt><code>key rollover &#8211;policy|-p </code><i>name</i><code> &#8211;keytype </code><i>type</i><code>|-t </code><i>type</i></p>
<dd>
<dt><code>key rollover &#8211;policy|-p </code><i>name</i><code> &#8211;all|-a</code></p>
<dd> Rollover active keys on the named zone or policy, respectively. This command is used to intiate manual rollovers; if it is not given, OpenDNSSEC will automatically rollover keys when the need arises. (Or, in the case of KSKs it will start the rollover process, to finish the KSK rollover see ksk-roll below.) </p>
<p> The &#8211;keytype option specifies the type of key to roll. Alternatively the &#8211;all option can be used which will roll both types of keys. After running, the KASP Enforcer will be woken up so that the signer can be sent the new information. </p>
<p> If the policy that the zone is on specifies that keys are shared then all zones on that policy will be rolled. If appropriate, a backup of the sqlite DB file is made. </p>
<p> If there are no keys ready to take over from the current key then the rollover will not occur immediately, but will be put off until the is a key in the ready state. </p>
<dt><code>key ksk-retire &#8211;zone|-z </code><i>zone</i></p>
<dd>
<dt><code>key ksk-retire &#8211;keytag|-x </code><i>keytag</i></p>
<dd>
<dt><code>key ksk-retire &#8211;cka_id|-k </code><i>ckaid</i></p>
<dd> Indicate to OpenDNSSEC that a currently active key should be retired. If key identifiers are not provided then the oldest key in the zone will be retired. </p>
<p> If only one key is in the active state then this command will exit with an error message, as completing would leave no active keys. </p>
<dt><code>key ds-seen &#8211;zone|-z </code><i>zone</i><code> &#8211;keytag|-x </code><i>keytag</i><code> [&#8211;no-notify|-l] [&#8211;no-retire|-f]</code></p>
<dd>
<dt><code>key ds-seen &#8211;zone|-z </code><i>zone</i><code> &#8211;cka_id|-k </code><i>ckaid</i><code> [&#8211;no-notify|-l] [&#8211;no-retire|-f]</code></p>
<dd> Indicate to OpenDNSSEC that a submitted DS record has appeared in the parent zone, and thereby trigger the completion of a KSK rollover. Note that this action is not yet standardised, and can therefore not be solved in a generic, automatic way. This command was designed for inclusion in any personalised setup that may or may not be automated. </p>
<p> There are several ways to specify which DS is in DNS, and the options reflect these alternatives. The &#8211;keytag option specifies the short integer that serves as a DNSSEC handle to a key; the &#8211;cka_id option refers to a key by way of its long hexadecimal identifier used to identify the key in the repository. </p>
<p> An optional &#8211;no-notify flag can also be passed in, which prevents the enforcer being notified of this change. If this flag is used then the enforcer must be manually notified with the &#8216;ods-enforcerd notify&#8217; command or the changes will not take effect until the next scheduled run of the enforcer. </p>
<p> An optional &#8211;no-retire flag can also be passed in, without this the existing key is moved into the retired state at the same time as making the new key active. If you wish to delay this step then pass in this flag and use the ksk-retire command when needed. </p>
<dt><code>key delete &#8211;cka_id|-k </code><i>ckaid</i><code> [&#8211;no-hsm]</code></p>
<dd> Remove a named key from the system. </p>
<p> Keys in the GENERATE or DEAD state can be safely removed from the system as they are not in use. </p>
<p> The &#8211;no-hsm flag can be provided if you want to leave the key material on the HSM. </p>
<dt><code>rollover list</code></p>
<dd> List the expected dates and times of upcoming rollovers. This can be used to get an idea of upcoming work, such as the non-standardised submission of DS records to a registry.</dl>
<h2>POLICY ADMINISTRATION SUBCOMMANDS</h2>
<dl>
<dt><code>policy export [&#8211;policy|&#8211;all|-p|-a]</code></p>
<dd> Export a policy from the database in the same format as the kasp.xml file.</p>
<dt><code>policy import</code></p>
<dd> Update the database with the contents of kasp.xml; identical to &quot;update kasp&quot;.</p>
<dt><code>policy purge</code></p>
<dd> * Experimental * </p>
<p> Remove any policies which have no zones associated with them. Note that this command has only been tested in a lab environment and so caution is recommended.</dl>
<h2>REPOSITORY AND BACKUP SUBCOMMANDS</h2>
<dl>
<dt><code>repository list</code></p>
<dd> List repositories from the database.</p>
<dt><code>backup list &#8211;repository|-r name</code></p>
<dd> List the backups that have been made on the given repository. The &#8211;repository option specifies what repository to list.</p>
<dt><code>backup prepare &#8211;repository|-r name </code></p>
<dd> Start a two-phase key backup procedure. Prepare the keys generated up to here for backup. Any keys generated automatically by OpenDNSSEC after this command are not guaranteed to be backed up, and will therefore not be taken into account when committing the prepared keys for use by OpenDNSSEC. The next command is usually either <code>backup commit</code> or, in case of failure of the key backup itself, <code>backup rollback</code>. This sequence works reliably if the KASP Enforcer is running. If it is not, the single-phase backup of <code>backup done</code> provides a one-phase backup alternative.</p>
<dt><code>backup commit &#8211;repository|-r name </code></p>
<dd> Successfully end a two-phase key backup procedure. After a key backup has succeeded, release all previously prepared keys for service by OpenDNSSEC. Any keys that were generated since the last issued preparation will not be released as it is uncertain whether these are actually backed up.</p>
<dt><code>backup rollback &#8211;repository|-r name </code></p>
<dd> Safely end a failed two-phase key backup procedure. After a key backup has failed, rollback all previously prepapared keys to the state where they are generated, but not yet available for service by OpenDNSSEC. After fixing this problem, a new attempt to backup the keys can be made.</p>
<dt><code>backup done &#8211;repository|-r name [&#8211;force]</code></p>
<dd> *DEPRECATED* </p>
<p> Indicate that a backup of the given repository has been done, all non-backed up keys will now be marked as backed up. The &#8211;repository option specifies what repository to list. </p>
<p> Note that the KASP Enforcer may take the initiative to generate keys after the backup has started and before the backup is done. This single-phase backup command waives that, which is safe when the KASP Enforcer is not running. If you intend to keep the Enforcer running, you will instead want to use the two-phase <code>backup prepare</code> followed by either <code>backup commit</code> or <code>backup rollback</code>.</p>
<dt><code>database backup [&#8211;output|-o output]</code></p>
<dd> Make a copy of the database of the KASP Enforcer (if using sqlite). This command ensures that the database is in a consistent state by taking a lock out first. The &#8211;output option specifies where the output should go; if not specified, the output goes to the usual enforcer.db.backup file.</dl>
<h2>PROCESS CONTROL SUBCOMMANDS</h2>
<dl>
<dt><code>start|stop|notify</code></p>
<dd> Start, stop or send &quot;SIGHUP&quot; to the ods-enforcerd process.</dl>
<h2>KEY STATES</h2>
<dl>
<dt>GENERATE</p>
<dd> The key has just been generated, but is not ready for use.</p>
<dt>PUBLISH</p>
<dd> The key has been published in the parent zone.</p>
<dt>READY</p>
<dd> The key is ready for use. E.g. according to settings in the policy the key has been published for long enough to have propagated to all resolvers.</p>
<dt>ACTIVE</p>
<dd> The key is actively being used to sign one or more zones.</p>
<dt>RETIRE</p>
<dd> The key has either reached the end of its scheduled life, or it has been rolled prematurely. However, records signed with it may still be cached sp the key is still being published.</p>
<dt>DEAD</p>
<dd> The key has been retired for long enough that its use is no longer cached, so it has been removed from the zone.</dl>
<h2>KEY TYPES</h2>
<p> Keys can be of two types: KSK or ZSK. These terms are explained in more detail in <a href="/docs/linux/man/1-opendnssec/">opendnssec</a>(1). </p>
<p> In DNS records, the KSK can usually be recognised by having its SEP (Secure Entry Point) flag set. But please note that officially this is a mere hint.</p>
<h2>INTERVAL FORMAT</h2>
<p> When specifying an interval for a key generation run the ISO 8601 standard is used, e.g. P2Y6M for 2 years and 6 months; or PT12H30M for 12 hours and 30 minutes. Note that a year is assumed to be 365 days and a month is assumed to be 31 days.</p>
<h2>TIME FORMATS</h2>
<p> When specifying a generation/retire time for a key being imported the following formats are understood:</p>
<dl>
<dt>YYYYMMDD[HH[MM[SS]]]</p>
<dd> (all numeric)</p>
<dt>D-MMM-YYYY[:| ]HH[:MM[:SS]]</p>
<dd>
<dt>DD-MMM-YYYY[:| ]HH[:MM[:SS]]</p>
<dd>
<dt>YYYY-MMM-DD[:| ]HH[:MM[:SS]]</p>
<dd> (alphabetic month)</p>
<dt>D-MM-YYYY[:| ]HH[:MM[:SS]]</p>
<dd>
<dt>DD-MM-YYYY[:| ]HH[:MM[:SS]]</p>
<dd>
<dt>YYYY-MM-DD[:| ]HH[:MM[:SS]]</p>
<dd> (numeric month)</dl>
<h2>FILES</h2>
<dl>
<dt><code>/etc/opendnssec/conf.xml</code></p>
<dd> The main configuration file for OpenDNSSEC.</p>
<dt><code>/etc/opendnssec/zonelist.xml</code></p>
<dd> The list of zones, as defined in conf.xml.</p>
<dt><code>/etc/opendnssec/kasp.xml</code></p>
<dd> The configuration of policies that define timing and security, as defined in conf.xml.</p>
<dt><code>/var/opendnssec/enforcer.db.backup</code></p>
<dd> A backup file of the database used by the KASP Enforcer.Note that this does not include the keys, which are to be extracted from its own repository.</p>
<dt><code>/var/opendnssec/unsigned/</code></p>
<dd> The location that is usually configured in conf.xml to contain unsigned zones.</p>
<dt><code>/var/opendnssec/signed/</code></p>
<dd> The location that is usually configured in conf.xml to contain signed zones.</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/8-ods-control/">ods-control</a>(8), <a href="/docs/linux/man/8-ods-enforcerd/">ods-enforcerd</a>(8), <a href="/docs/linux/man/1-ods-hsmspeed/">ods-hsmspeed</a>(1), <a href="/docs/linux/man/1-ods-hsmutil/">ods-hsmutil</a>(1), <a href="/docs/linux/man/1-ods-kaspcheck/">ods-kaspcheck</a>(1), <a href="/docs/linux/man/8-ods-signer/">ods-signer</a>(8), <a href="/docs/linux/man/8-ods-signerd/">ods-signerd</a>(8), <a href="/docs/linux/man/5-ods-timing/">ods-timing</a>(5), <a href="/docs/linux/man/7-opendnssec/">opendnssec</a>(7), <code><a rel="nofollow" href="http://www.opendnssec.org/">http://www.opendnssec.org/</a></code></p>
<h2>AUTHOR</h2>
<p> <code>ods-ksmutil</code> was written by Sion Lloyd and Nominet as part of the OpenDNSSEC project. </p>
<h2>Index</h2>
