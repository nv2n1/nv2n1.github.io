---
title: "ceph(8)"
name: "ceph"
section: "8"
letter: "c"
url: "/docs/linux/man/8-ceph/"
description: "ceph – ceph administration tool"
---

<p>ceph &#8211; ceph administration tool</p>
<h2>Synopsis</h2>
<pre><code>ceph</code> <code>auth</code> [ <i>add</i> | <i>caps</i> | <i>del</i> | <i>export</i> | <i>get</i> | <i>get-key</i> | <i>get-or-create</i> | <i>get-or-create-key</i> | <i>import</i> | <i>list</i> | <i>print-key</i> | <i>print_key</i> ] ...</pre>
<pre><code>ceph</code> <code>compact</code></pre>
<pre><code>ceph</code> <code>config-key</code> [ <i>del</i> | <i>exists</i> | <i>get</i> | <i>list</i> | <i>put</i> ] ...</pre>
<pre><code>ceph</code> <code>df</code> <i>{detail}</i></pre>
<pre><code>ceph</code> <code>fs</code> [ <i>ls</i> | <i>new</i> | <i>reset</i> | <i>rm</i> ] ...</pre>
<pre><code>ceph</code> <code>fsid</code></pre>
<pre><code>ceph</code> <code>health</code> <i>{detail}</i></pre>
<pre><code>ceph</code> <code>heap</code> [ <i>dump</i> | <i>start_profiler</i> | <i>stop_profiler</i> | <i>release</i> | <i>stats</i> ] ...</pre>
<pre><code>ceph</code> <code>injectargs</code> <i>&lt;injectedargs&gt;</i> [ <i>&lt;injectedargs&gt;</i>... ]</pre>
<pre><code>ceph</code> <code>log</code> <i>&lt;logtext&gt;</i> [ <i>&lt;logtext&gt;</i>... ]</pre>
<pre><code>ceph</code> <code>mds</code> [ <i>add_data_pool</i> | <i>cluster_down</i> | <i>cluster_up</i> | <i>compat</i> | <i>deactivate</i> | <i>dump</i> | <i>fail</i> | <i>getmap</i> | <i>newfs</i> | <i>remove_data_pool</i> | <i>rm</i> | <i>rmfailed</i> | <i>set</i> | <i>set_max_mds</i> | <i>set_state</i> | <i>setmap</i> | <i>stat</i> | <i>stop</i> | <i>tell</i> ] ...</pre>
<pre><code>ceph</code> <code>mon</code> [ <i>add</i> | <i>dump</i> | <i>getmap</i> | <i>remove</i> | <i>stat</i> ] ...</pre>
<pre><code>ceph</code> <code>mon_status</code></pre>
<pre><code>ceph</code> <code>osd</code> [ <i>blacklist</i> | <i>blocked-by</i> | <i>create</i> | <i>deep-scrub</i> | <i>df</i> | <i>down</i> | <i>dump</i> | <i>erasure-code-profile</i> | <i>find</i> | <i>getcrushmap</i> | <i>getmap</i> | <i>getmaxosd</i> | <i>in</i> | <i>lspools</i> | <i>map</i> | <i>metadata</i> | <i>out</i> | <i>pause</i> | <i>perf</i> | <i>pg-temp</i> | <i>primary-affinity</i> | <i>primary-temp</i> | <i>repair</i> | <i>reweight</i> | <i>reweight-by-pg</i> | <i>rm</i> | <i>scrub</i> | <i>set</i> | <i>setcrushmap</i> | <i>setmaxosd</i> | <i>stat</i> | <i>thrash</i> | <i>tree</i> | <i>unpause</i> | <i>unset</i> ] ...</pre>
<pre><code>ceph</code> <code>osd</code> <code>crush</code> [ <i>add</i> | <i>add-bucket</i> | <i>create-or-move</i> | <i>dump</i> | <i>get-tunable</i> | <i>link</i> | <i>move</i> | <i>remove</i> | <i>rename-bucket</i> | <i>reweight</i> | <i>reweight-all</i> | <i>reweight-subtree</i> | <i>rm</i> | <i>rule</i> | <i>set</i> | <i>set-tunable</i> | <i>show-tunables</i> | <i>tunables</i> | <i>unlink</i> ] ...</pre>
<pre><code>ceph</code> <code>osd</code> <code>pool</code> [ <i>create</i> | <i>delete</i> | <i>get</i> | <i>get-quota</i> | <i>ls</i> | <i>mksnap</i> | <i>rename</i> | <i>rmsnap</i> | <i>set</i> | <i>set-quota</i> | <i>stats</i> ] ...</pre>
<pre><code>ceph</code> <code>osd</code> <code>tier</code> [ <i>add</i> | <i>add-cache</i> | <i>cache-mode</i> | <i>remove</i> | <i>remove-overlay</i> | <i>set-overlay</i> ] ...</pre>
<pre><code>ceph</code> <code>pg</code> [ <i>debug</i> | <i>deep-scrub</i> | <i>dump</i> | <i>dump_json</i> | <i>dump_pools_json</i> | <i>dump_stuck</i> | <i>force_create_pg</i> | <i>getmap</i> | <i>ls</i> | <i>ls-by-osd</i> | <i>ls-by-pool</i> | <i>ls-by-primary</i> | <i>map</i> | <i>repair</i> | <i>scrub</i> | <i>send_pg_creates</i> | <i>set_full_ratio</i> | <i>set_nearfull_ratio</i> | <i>stat</i> ] ...</pre>
<pre><code>ceph</code> <code>quorum</code> [ <i>enter</i> | <i>exit</i> ]</pre>
<pre><code>ceph</code> <code>quorum_status</code></pre>
<pre><code>ceph</code> <code>report</code> { <i>&lt;tags&gt;</i> [ <i>&lt;tags&gt;...</i> ] }</pre>
<pre><code>ceph</code> <code>scrub</code></pre>
<pre><code>ceph</code> <code>status</code></pre>
<pre><code>ceph</code> <code>sync</code> <code>force</code> {--yes-i-really-mean-it} {--i-know-what-i-am-doing}</pre>
<pre><code>ceph</code> <code>tell</code> <i>&lt;name (type.id)&gt; &lt;args&gt; [&lt;args&gt;...]</i></pre>
<pre><code>ceph</code> <code>version</code></pre>
<h2>Description</h2>
<p><code>ceph</code> is a control utility which is used for manual deployment and maintenance of a Ceph cluster. It provides a diverse set of commands that allows deployment of monitors, OSDs, placement groups, MDS and overall maintenance, administration of the cluster.</p>
<h2>Commands</h2>
<h3>auth</h3>
<p>Manage authentication keys. It is used for adding, removing, exporting or updating of authentication keys for a particular entity such as a monitor or OSD. It uses some additional subcommands. </p>
<p> Subcommand <code>add</code> adds authentication info for a particular entity from input file, or random key if no input is given and/or any caps specified in the command. </p>
<p> Usage: </p>
<pre>ceph auth add &lt;entity&gt; {&lt;caps&gt; [&lt;caps&gt;...]}</pre>
<p>Subcommand <code>caps</code> updates caps for <code>name</code> from caps specified in the command. </p>
<p> Usage: </p>
<pre>ceph auth caps &lt;entity&gt; &lt;caps&gt; [&lt;caps&gt;...]</pre>
<p>Subcommand <code>del</code> deletes all caps for <code>name</code>. </p>
<p> Usage: </p>
<pre>ceph auth del &lt;entity&gt;</pre>
<p>Subcommand <code>export</code> writes keyring for requested entity, or master keyring if none given. </p>
<p> Usage: </p>
<pre>ceph auth export {&lt;entity&gt;}</pre>
<p>Subcommand <code>get</code> writes keyring file with requested key. </p>
<p> Usage: </p>
<pre>ceph auth get &lt;entity&gt;</pre>
<p>Subcommand <code>get-key</code> displays requested key. </p>
<p> Usage: </p>
<pre>ceph auth get-key &lt;entity&gt;</pre>
<p>Subcommand <code>get-or-create</code> adds authentication info for a particular entity from input file, or random key if no input given and/or any caps specified in the command. </p>
<p> Usage: </p>
<pre>ceph auth get-or-create &lt;entity&gt; {&lt;caps&gt; [&lt;caps&gt;...]}</pre>
<p>Subcommand <code>get-or-create-key</code> gets or adds key for <code>name</code> from system/caps pairs specified in the command. If key already exists, any given caps must match the existing caps for that key. </p>
<p> Usage: </p>
<pre>ceph auth get-or-create-key &lt;entity&gt; {&lt;caps&gt; [&lt;caps&gt;...]}</pre>
<p>Subcommand <code>import</code> reads keyring from input file. </p>
<p> Usage: </p>
<pre>ceph auth import</pre>
<p>Subcommand <code>list</code> lists authentication state. </p>
<p> Usage: </p>
<pre>ceph auth list</pre>
<p>Subcommand <code>print-key</code> displays requested key. </p>
<p> Usage: </p>
<pre>ceph auth print-key &lt;entity&gt;</pre>
<p>Subcommand <code>print_key</code> displays requested key. </p>
<p> Usage: </p>
<pre>ceph auth print_key &lt;entity&gt;</pre>
<h3>compact</h3>
<p>Causes compaction of monitor&#8217;s leveldb storage. </p>
<p> Usage: </p>
<pre>ceph compact</pre>
<h3>config-key</h3>
<p>Manage configuration key. It uses some additional subcommands. </p>
<p> Subcommand <code>del</code> deletes configuration key. </p>
<p> Usage: </p>
<pre>ceph config-key del &lt;key&gt;</pre>
<p>Subcommand <code>exists</code> checks for configuration keys existence. </p>
<p> Usage: </p>
<pre>ceph config-key exists &lt;key&gt;</pre>
<p>Subcommand <code>get</code> gets the configuration key. </p>
<p> Usage: </p>
<pre>ceph config-key get &lt;key&gt;</pre>
<p>Subcommand <code>list</code> lists configuration keys. </p>
<p> Usage: </p>
<pre>ceph config-key list</pre>
<p>Subcommand <code>put</code> puts configuration key and values. </p>
<p> Usage: </p>
<pre>ceph config-key put &lt;key&gt; {&lt;val&gt;}</pre>
<h3>df</h3>
<p>Show cluster&#8217;s free space status. </p>
<p> Usage: </p>
<pre>ceph df {detail}</pre>
<h3>fs</h3>
<p>Manage cephfs filesystems. It uses some additional subcommands. </p>
<p> Subcommand <code>ls</code> to list filesystems </p>
<p> Usage: </p>
<pre>ceph fs ls</pre>
<p>Subcommand <code>new</code> to make a new filesystem using named pools &lt;metadata&gt; and &lt;data&gt; </p>
<p> Usage: </p>
<pre>ceph fs new &lt;fs_name&gt; &lt;metadata&gt; &lt;data&gt;</pre>
<p>Subcommand <code>reset</code> is used for disaster recovery only: reset to a single-MDS map </p>
<p> Usage: </p>
<pre>ceph fs reset &lt;fs_name&gt; {--yes-i-really-mean-it}</pre>
<p>Subcommand <code>rm</code> to disable the named filesystem </p>
<p> Usage: </p>
<pre>ceph fs rm &lt;fs_name&gt; {--yes-i-really-mean-it}</pre>
<h3>fsid</h3>
<p>Show cluster&#8217;s FSID/UUID. </p>
<p> Usage: </p>
<pre>ceph fsid</pre>
<h3>health</h3>
<p>Show cluster&#8217;s health. </p>
<p> Usage: </p>
<pre>ceph health {detail}</pre>
<h3>heap</h3>
<p>Show heap usage info (available only if compiled with tcmalloc) </p>
<p> Usage: </p>
<pre>ceph heap dump|start_profiler|stop_profiler|release|stats</pre>
<h3>injectargs</h3>
<p>Inject configuration arguments into monitor. </p>
<p> Usage: </p>
<pre>ceph injectargs &lt;injected_args&gt; [&lt;injected_args&gt;...]</pre>
<h3>log</h3>
<p>Log supplied text to the monitor log. </p>
<p> Usage: </p>
<pre>ceph log &lt;logtext&gt; [&lt;logtext&gt;...]</pre>
<h3>mds</h3>
<p>Manage metadata server configuration and administration. It uses some additional subcommands. </p>
<p> Subcommand <code>add_data_pool</code> adds data pool. </p>
<p> Usage: </p>
<pre>ceph mds add_data_pool &lt;pool&gt;</pre>
<p>Subcommand <code>cluster_down</code> takes mds cluster down. </p>
<p> Usage: </p>
<pre>ceph mds cluster_down</pre>
<p>Subcommand <code>cluster_up</code> brings mds cluster up. </p>
<p> Usage: </p>
<pre>ceph mds cluster_up</pre>
<p>Subcommand <code>compat</code> manages compatible features. It uses some additional subcommands. </p>
<p> Subcommand <code>rm_compat</code> removes compatible feature. </p>
<p> Usage: </p>
<pre>ceph mds compat rm_compat &lt;int[0-]&gt;</pre>
<p>Subcommand <code>rm_incompat</code> removes incompatible feature. </p>
<p> Usage: </p>
<pre>ceph mds compat rm_incompat &lt;int[0-]&gt;</pre>
<p>Subcommand <code>show</code> shows mds compatibility settings. </p>
<p> Usage: </p>
<pre>ceph mds compat show</pre>
<p>Subcommand <code>deactivate</code> stops mds. </p>
<p> Usage: </p>
<pre>ceph mds deactivate &lt;who&gt;</pre>
<p>Subcommand <code>dump</code> dumps information, optionally from epoch. </p>
<p> Usage: </p>
<pre>ceph mds dump {&lt;int[0-]&gt;}</pre>
<p>Subcommand <code>fail</code> forces mds to status fail. </p>
<p> Usage: </p>
<pre>ceph mds fail &lt;who&gt;</pre>
<p>Subcommand <code>getmap</code> gets MDS map, optionally from epoch. </p>
<p> Usage: </p>
<pre>ceph mds getmap {&lt;int[0-]&gt;}</pre>
<p>Subcommand <code>newfs</code> makes new filesystem using pools &lt;metadata&gt; and &lt;data&gt;. </p>
<p> Usage: </p>
<pre>ceph mds newfs &lt;int[0-]&gt; &lt;int[0-]&gt; {--yes-i-really-mean-it}</pre>
<p>Subcommand <code>remove_data_pool</code> removes data pool. </p>
<p> Usage: </p>
<pre>ceph mds remove_data_pool &lt;pool&gt;</pre>
<p>Subcommand <code>rm</code> removes inactive mds. </p>
<p> Usage: </p>
<pre>ceph mds rm &lt;int[0-]&gt; &lt;name&gt; (type.id)&gt;</pre>
<p>Subcommand <code>rmfailed</code> removes failed mds. </p>
<p> Usage: </p>
<pre>ceph mds rmfailed &lt;int[0-]&gt;</pre>
<p>Subcommand <code>set</code> set mds parameter &lt;var&gt; to &lt;val&gt; </p>
<p> Usage: </p>
<pre>ceph mds set max_mds|max_file_size|allow_new_snaps|inline_data &lt;va&gt; {&lt;confirm&gt;}</pre>
<p>Subcommand <code>set_max_mds</code> sets max MDS index. </p>
<p> Usage: </p>
<pre>ceph mds set_max_mds &lt;int[0-]&gt;</pre>
<p>Subcommand <code>set_state</code> sets mds state of &lt;gid&gt; to &lt;numeric-state&gt;. </p>
<p> Usage: </p>
<pre>ceph mds set_state &lt;int[0-]&gt; &lt;int[0-20]&gt;</pre>
<p>Subcommand <code>setmap</code> sets mds map; must supply correct epoch number. </p>
<p> Usage: </p>
<pre>ceph mds setmap &lt;int[0-]&gt;</pre>
<p>Subcommand <code>stat</code> shows MDS status. </p>
<p> Usage: </p>
<pre>ceph mds stat</pre>
<p>Subcommand <code>stop</code> stops mds. </p>
<p> Usage: </p>
<pre>ceph mds stop &lt;who&gt;</pre>
<p>Subcommand <code>tell</code> sends command to particular mds. </p>
<p> Usage: </p>
<pre>ceph mds tell &lt;who&gt; &lt;args&gt; [&lt;args&gt;...]</pre>
<h3>mon</h3>
<p>Manage monitor configuration and administration. It uses some additional subcommands. </p>
<p> Subcommand <code>add</code> adds new monitor named &lt;name&gt; at &lt;addr&gt;. </p>
<p> Usage: </p>
<pre>ceph mon add &lt;name&gt; &lt;IPaddr[:port]&gt;</pre>
<p>Subcommand <code>dump</code> dumps formatted monmap (optionally from epoch) </p>
<p> Usage: </p>
<pre>ceph mon dump {&lt;int[0-]&gt;}</pre>
<p>Subcommand <code>getmap</code> gets monmap. </p>
<p> Usage: </p>
<pre>ceph mon getmap {&lt;int[0-]&gt;}</pre>
<p>Subcommand <code>remove</code> removes monitor named &lt;name&gt;. </p>
<p> Usage: </p>
<pre>ceph mon remove &lt;name&gt;</pre>
<p>Subcommand <code>stat</code> summarizes monitor status. </p>
<p> Usage: </p>
<pre>ceph mon stat</pre>
<h3>mon_status</h3>
<p>Reports status of monitors. </p>
<p> Usage: </p>
<pre>ceph mon_status</pre>
<h3>osd</h3>
<p>Manage OSD configuration and administration. It uses some additional subcommands. </p>
<p> Subcommand <code>blacklist</code> manage blacklisted clients. It uses some additional subcommands. </p>
<p> Subcommand <code>add</code> add &lt;addr&gt; to blacklist (optionally until &lt;expire&gt; seconds from now) </p>
<p> Usage: </p>
<pre>ceph osd blacklist add &lt;EntityAddr&gt; {&lt;float[0.0-]&gt;}</pre>
<p>Subcommand <code>ls</code> show blacklisted clients </p>
<p> Usage: </p>
<pre>ceph osd blacklist ls</pre>
<p>Subcommand <code>rm</code> remove &lt;addr&gt; from blacklist </p>
<p> Usage: </p>
<pre>ceph osd blacklist rm &lt;EntityAddr&gt;</pre>
<p>Subcommand <code>blocked-by</code> prints a histogram of which OSDs are blocking their peers </p>
<p> Usage: </p>
<pre>ceph osd blocked-by</pre>
<p>Subcommand <code>create</code> creates new osd (with optional UUID). </p>
<p> Usage: </p>
<pre>ceph osd create {&lt;uuid&gt;}</pre>
<p>Subcommand <code>crush</code> is used for CRUSH management. It uses some additional subcommands. </p>
<p> Subcommand <code>add</code> adds or updates crushmap position and weight for &lt;name&gt; with &lt;weight&gt; and location &lt;args&gt;. </p>
<p> Usage: </p>
<pre>ceph osd crush add &lt;osdname (id|osd.id)&gt; &lt;float[0.0-]&gt; &lt;args&gt; [&lt;args&gt;...]</pre>
<p>Subcommand <code>add-bucket</code> adds no-parent (probably root) crush bucket &lt;name&gt; of type &lt;type&gt;. </p>
<p> Usage: </p>
<pre>ceph osd crush add-bucket &lt;name&gt; &lt;type&gt;</pre>
<p>Subcommand <code>create-or-move</code> creates entry or moves existing entry for &lt;name&gt; &lt;weight&gt; at/to location &lt;args&gt;. </p>
<p> Usage: </p>
<pre>ceph osd crush create-or-move &lt;osdname (id|osd.id)&gt; &lt;float[0.0-]&gt; &lt;args&gt;
[&lt;args&gt;...]</pre>
<p>Subcommand <code>dump</code> dumps crush map. </p>
<p> Usage: </p>
<pre>ceph osd crush dump</pre>
<p>Subcommand <code>get-tunable</code> get crush tunable straw_calc_version </p>
<p> Usage: </p>
<pre>ceph osd crush get-tunable straw_calc_version</pre>
<p>Subcommand <code>link</code> links existing entry for &lt;name&gt; under location &lt;args&gt;. </p>
<p> Usage: </p>
<pre>ceph osd crush link &lt;name&gt; &lt;args&gt; [&lt;args&gt;...]</pre>
<p>Subcommand <code>move</code> moves existing entry for &lt;name&gt; to location &lt;args&gt;. </p>
<p> Usage: </p>
<pre>ceph osd crush move &lt;name&gt; &lt;args&gt; [&lt;args&gt;...]</pre>
<p>Subcommand <code>remove</code> removes &lt;name&gt; from crush map (everywhere, or just at &lt;ancestor&gt;). </p>
<p> Usage: </p>
<pre>ceph osd crush remove &lt;name&gt; {&lt;ancestor&gt;}</pre>
<p>Subcommand <code>rename-bucket</code> renames buchket &lt;srcname&gt; to &lt;stname&gt; </p>
<p> Usage: </p>
<pre>ceph osd crush rename-bucket &lt;srcname&gt; &lt;dstname&gt;</pre>
<p>Subcommand <code>reweight</code> change &lt;name&gt;&#8217;s weight to &lt;weight&gt; in crush map. </p>
<p> Usage: </p>
<pre>ceph osd crush reweight &lt;name&gt; &lt;float[0.0-]&gt;</pre>
<p>Subcommand <code>reweight-all</code> recalculate the weights for the tree to ensure they sum correctly </p>
<p> Usage: </p>
<pre>ceph osd crush reweight-all</pre>
<p>Subcommand <code>reweight-subtree</code> changes all leaf items beneath &lt;name&gt; to &lt;weight&gt; in crush map </p>
<p> Usage: </p>
<pre>ceph osd crush reweight-subtree &lt;name&gt; &lt;weight&gt;</pre>
<p>Subcommand <code>rm</code> removes &lt;name&gt; from crush map (everywhere, or just at &lt;ancestor&gt;). </p>
<p> Usage: </p>
<pre>ceph osd crush rm &lt;name&gt; {&lt;ancestor&gt;}</pre>
<p>Subcommand <code>rule</code> is used for creating crush rules. It uses some additional subcommands. </p>
<p> Subcommand <code>create-erasure</code> creates crush rule &lt;name&gt; for erasure coded pool created with &lt;profile&gt; (default default). </p>
<p> Usage: </p>
<pre>ceph osd crush rule create-erasure &lt;name&gt; {&lt;profile&gt;}</pre>
<p>Subcommand <code>create-simple</code> creates crush rule &lt;name&gt; to start from &lt;root&gt;, replicate across buckets of type &lt;type&gt;, using a choose mode of &lt;firstn|indep&gt; (default firstn; indep best for erasure pools). </p>
<p> Usage: </p>
<pre>ceph osd crush rule create-simple &lt;name&gt; &lt;root&gt; &lt;type&gt; {firstn|indep}</pre>
<p>Subcommand <code>dump</code> dumps crush rule &lt;name&gt; (default all). </p>
<p> Usage: </p>
<pre>ceph osd crush rule dump {&lt;name&gt;}</pre>
<p>Subcommand <code>list</code> lists crush rules. </p>
<p> Usage: </p>
<pre>ceph osd crush rule list</pre>
<p>Subcommand <code>ls</code> lists crush rules. </p>
<p> Usage: </p>
<pre>ceph osd crush rule ls</pre>
<p>Subcommand <code>rm</code> removes crush rule &lt;name&gt;. </p>
<p> Usage: </p>
<pre>ceph osd crush rule rm &lt;name&gt;</pre>
<p>Subcommand <code>set</code> used alone, sets crush map from input file. </p>
<p> Usage: </p>
<pre>ceph osd crush set</pre>
<p>Subcommand <code>set</code> with osdname/osd.id update crushmap position and weight for &lt;name&gt; to &lt;weight&gt; with location &lt;args&gt;. </p>
<p> Usage: </p>
<pre>ceph osd crush set &lt;osdname (id|osd.id)&gt; &lt;float[0.0-]&gt; &lt;args&gt; [&lt;args&gt;...]</pre>
<p>Subcommand <code>set-tunable</code> set crush tunable &lt;tunable&gt; to &lt;value&gt;. The only tunable that can be set is straw_calc_version. </p>
<p> Usage: </p>
<pre>ceph osd crush set-tunable straw_calc_version &lt;value&gt;</pre>
<p>Subcommand <code>show-tunables</code> shows current crush tunables. </p>
<p> Usage: </p>
<pre>ceph osd crush show-tunables</pre>
<p>Subcommand <code>tunables</code> sets crush tunables values to &lt;profile&gt;. </p>
<p> Usage: </p>
<pre>ceph osd crush tunables legacy|argonaut|bobtail|firefly|hammer|optimal|default</pre>
<p>Subcommand <code>unlink</code> unlinks &lt;name&gt; from crush map (everywhere, or just at &lt;ancestor&gt;). </p>
<p> Usage: </p>
<pre>ceph osd crush unlink &lt;name&gt; {&lt;ancestor&gt;}</pre>
<p>Subcommand <code>df</code> shows OSD utilization </p>
<p> Usage: </p>
<pre>ceph osd df {plain|tree}</pre>
<p>Subcommand <code>deep-scrub</code> initiates deep scrub on specified osd. </p>
<p> Usage: </p>
<pre>ceph osd deep-scrub &lt;who&gt;</pre>
<p>Subcommand <code>down</code> sets osd(s) &lt;id&gt; [&lt;id&gt;&#8230;] down. </p>
<p> Usage: </p>
<pre>ceph osd down &lt;ids&gt; [&lt;ids&gt;...]</pre>
<p>Subcommand <code>dump</code> prints summary of OSD map. </p>
<p> Usage: </p>
<pre>ceph osd dump {&lt;int[0-]&gt;}</pre>
<p>Subcommand <code>erasure-code-profile</code> is used for managing the erasure code profiles. It uses some additional subcommands. </p>
<p> Subcommand <code>get</code> gets erasure code profile &lt;name&gt;. </p>
<p> Usage: </p>
<pre>ceph osd erasure-code-profile get &lt;name&gt;</pre>
<p>Subcommand <code>ls</code> lists all erasure code profiles. </p>
<p> Usage: </p>
<pre>ceph osd erasure-code-profile ls</pre>
<p>Subcommand <code>rm</code> removes erasure code profile &lt;name&gt;. </p>
<p> Usage: </p>
<pre>ceph osd erasure-code-profile rm &lt;name&gt;</pre>
<p>Subcommand <code>set</code> creates erasure code profile &lt;name&gt; with [&lt;key[=value]&gt; &#8230;] pairs. Add a &#8211;force at the end to override an existing profile (IT IS RISKY). </p>
<p> Usage: </p>
<pre>ceph osd erasure-code-profile set &lt;name&gt; {&lt;profile&gt; [&lt;profile&gt;...]}</pre>
<p>Subcommand <code>find</code> find osd &lt;id&gt; in the CRUSH map and shows its location. </p>
<p> Usage: </p>
<pre>ceph osd find &lt;int[0-]&gt;</pre>
<p>Subcommand <code>getcrushmap</code> gets CRUSH map. </p>
<p> Usage: </p>
<pre>ceph osd getcrushmap {&lt;int[0-]&gt;}</pre>
<p>Subcommand <code>getmap</code> gets OSD map. </p>
<p> Usage: </p>
<pre>ceph osd getmap {&lt;int[0-]&gt;}</pre>
<p>Subcommand <code>getmaxosd</code> shows largest OSD id. </p>
<p> Usage: </p>
<pre>ceph osd getmaxosd</pre>
<p>Subcommand <code>in</code> sets osd(s) &lt;id&gt; [&lt;id&gt;&#8230;] in. </p>
<p> Usage: </p>
<pre>ceph osd in &lt;ids&gt; [&lt;ids&gt;...]</pre>
<p>Subcommand <code>lost</code> marks osd as permanently lost. THIS DESTROYS DATA IF NO MORE REPLICAS EXIST, BE CAREFUL. </p>
<p> Usage: </p>
<pre>ceph osd lost &lt;int[0-]&gt; {--yes-i-really-mean-it}</pre>
<p>Subcommand <code>ls</code> shows all OSD ids. </p>
<p> Usage: </p>
<pre>ceph osd ls {&lt;int[0-]&gt;}</pre>
<p>Subcommand <code>lspools</code> lists pools. </p>
<p> Usage: </p>
<pre>ceph osd lspools {&lt;int&gt;}</pre>
<p>Subcommand <code>map</code> finds pg for &lt;object&gt; in &lt;pool&gt;. </p>
<p> Usage: </p>
<pre>ceph osd map &lt;poolname&gt; &lt;objectname&gt;</pre>
<p>Subcommand <code>metadata</code> fetches metadata for osd &lt;id&gt;. </p>
<p> Usage: </p>
<pre>ceph osd metadata &lt;int[0-]&gt;</pre>
<p>Subcommand <code>out</code> sets osd(s) &lt;id&gt; [&lt;id&gt;&#8230;] out. </p>
<p> Usage: </p>
<pre>ceph osd out &lt;ids&gt; [&lt;ids&gt;...]</pre>
<p>Subcommand <code>pause</code> pauses osd. </p>
<p> Usage: </p>
<pre>ceph osd pause</pre>
<p>Subcommand <code>perf</code> prints dump of OSD perf summary stats. </p>
<p> Usage: </p>
<pre>ceph osd perf</pre>
<p>Subcommand <code>pg-temp</code> set pg_temp mapping pgid:[&lt;id&gt; [&lt;id&gt;&#8230;]] (developers only). </p>
<p> Usage: </p>
<pre>ceph osd pg-temp &lt;pgid&gt; {&lt;id&gt; [&lt;id&gt;...]}</pre>
<p>Subcommand <code>pool</code> is used for managing data pools. It uses some additional subcommands. </p>
<p> Subcommand <code>create</code> creates pool. </p>
<p> Usage: </p>
<pre>ceph osd pool create &lt;poolname&gt; &lt;int[0-]&gt; {&lt;int[0-]&gt;} {replicated|erasure}
{&lt;erasure_code_profile&gt;} {&lt;ruleset&gt;} {&lt;int&gt;}</pre>
<p>Subcommand <code>delete</code> deletes pool. </p>
<p> Usage: </p>
<pre>ceph osd pool delete &lt;poolname&gt; {&lt;poolname&gt;} {--yes-i-really-really-mean-it}</pre>
<p>Subcommand <code>get</code> gets pool parameter &lt;var&gt;. </p>
<p> Usage: </p>
<pre>ceph osd pool get &lt;poolname&gt; size|min_size|crash_replay_interval|pg_num|
pgp_num|crush_ruleset|auid|write_fadvise_dontneed</pre>
<p>Only for tiered pools: </p>
<pre>ceph osd pool get &lt;poolname&gt; hit_set_type|hit_set_period|hit_set_count|hit_set_fpp|
target_max_objects|target_max_bytes|cache_target_dirty_ratio|
cache_target_full_ratio|cache_min_flush_age|cache_min_evict_age|
min_read_recency_for_promote</pre>
<p>Only for erasure coded pools: </p>
<pre>ceph osd pool get &lt;poolname&gt; erasure_code_profile</pre>
<p>Subcommand <code>get-quota</code> obtains object or byte limits for pool. </p>
<p> Usage: </p>
<pre>ceph osd pool get-quota &lt;poolname&gt;</pre>
<p>Subcommand <code>ls</code> list pools </p>
<p> Usage: </p>
<pre>ceph osd pool ls {detail}</pre>
<p>Subcommand <code>mksnap</code> makes snapshot &lt;snap&gt; in &lt;pool&gt;. </p>
<p> Usage: </p>
<pre>ceph osd pool mksnap &lt;poolname&gt; &lt;snap&gt;</pre>
<p>Subcommand <code>rename</code> renames &lt;srcpool&gt; to &lt;destpool&gt;. </p>
<p> Usage: </p>
<pre>ceph osd pool rename &lt;poolname&gt; &lt;poolname&gt;</pre>
<p>Subcommand <code>rmsnap</code> removes snapshot &lt;snap&gt; from &lt;pool&gt;. </p>
<p> Usage: </p>
<pre>ceph osd pool rmsnap &lt;poolname&gt; &lt;snap&gt;</pre>
<p>Subcommand <code>set</code> sets pool parameter &lt;var&gt; to &lt;val&gt;. </p>
<p> Usage: </p>
<pre>ceph osd pool set &lt;poolname&gt; size|min_size|crash_replay_interval|pg_num|
pgp_num|crush_ruleset|hashpspool|nodelete|nopgchange|nosizechange|
hit_set_type|hit_set_period|hit_set_count|hit_set_fpp|debug_fake_ec_pool|
target_max_bytes|target_max_objects|cache_target_dirty_ratio|
cache_target_full_ratio|cache_min_flush_age|cache_min_evict_age|auid|
min_read_recency_for_promote|write_fadvise_dontneed
&lt;val&gt; {--yes-i-really-mean-it}</pre>
<p>Subcommand <code>set-quota</code> sets object or byte limit on pool. </p>
<p> Usage: </p>
<pre>ceph osd pool set-quota &lt;poolname&gt; max_objects|max_bytes &lt;val&gt;</pre>
<p>Subcommand <code>stats</code> obtain stats from all pools, or from specified pool. </p>
<p> Usage: </p>
<pre>ceph osd pool stats {&lt;name&gt;}</pre>
<p>Subcommand <code>primary-affinity</code> adjust osd primary-affinity from 0.0 &lt;=&lt;weight&gt; &lt;= 1.0 </p>
<p> Usage: </p>
<pre>ceph osd primary-affinity &lt;osdname (id|osd.id)&gt; &lt;float[0.0-1.0]&gt;</pre>
<p>Subcommand <code>primary-temp</code> sets primary_temp mapping pgid:&lt;id&gt;|-1 (developers only). </p>
<p> Usage: </p>
<pre>ceph osd primary-temp &lt;pgid&gt; &lt;id&gt;</pre>
<p>Subcommand <code>repair</code> initiates repair on a specified osd. </p>
<p> Usage: </p>
<pre>ceph osd repair &lt;who&gt;</pre>
<p>Subcommand <code>reweight</code> reweights osd to 0.0 &lt; &lt;weight&gt; &lt; 1.0. </p>
<p> Usage: </p>
<pre>osd reweight &lt;int[0-]&gt; &lt;float[0.0-1.0]&gt;</pre>
<p>Subcommand <code>reweight-by-pg</code> reweight OSDs by PG distribution [overload-percentage-for-consideration, default 120]. </p>
<p> Usage: </p>
<pre>ceph osd reweight-by-pg {&lt;int[100-]&gt;} {&lt;poolname&gt; [&lt;poolname...]}</pre>
<p>Subcommand <code>reweight-by-utilization</code> reweight OSDs by utilization [overload-percentage-for-consideration, default 120]. </p>
<p> Usage: </p>
<pre>ceph osd reweight-by-utilization {&lt;int[100-]&gt;}</pre>
<p>Subcommand <code>rm</code> removes osd(s) &lt;id&gt; [&lt;id&gt;&#8230;] in the cluster. </p>
<p> Usage: </p>
<pre>ceph osd rm &lt;ids&gt; [&lt;ids&gt;...]</pre>
<p>Subcommand <code>scrub</code> initiates scrub on specified osd. </p>
<p> Usage: </p>
<pre>ceph osd scrub &lt;who&gt;</pre>
<p>Subcommand <code>set</code> sets &lt;key&gt;. </p>
<p> Usage: </p>
<pre>ceph osd set full|pause|noup|nodown|noout|noin|nobackfill|
norebalance|norecover|noscrub|nodeep-scrub|notieragent</pre>
<p>Subcommand <code>setcrushmap</code> sets crush map from input file. </p>
<p> Usage: </p>
<pre>ceph osd setcrushmap</pre>
<p>Subcommand <code>setmaxosd</code> sets new maximum osd value. </p>
<p> Usage: </p>
<pre>ceph osd setmaxosd &lt;int[0-]&gt;</pre>
<p>Subcommand <code>stat</code> prints summary of OSD map. </p>
<p> Usage: </p>
<pre>ceph osd stat</pre>
<p>Subcommand <code>thrash</code> thrashes OSDs for &lt;num_epochs&gt;. </p>
<p> Usage: </p>
<pre>ceph osd thrash &lt;int[0-]&gt;</pre>
<p>Subcommand <code>tier</code> is used for managing tiers. It uses some additional subcommands. </p>
<p> Subcommand <code>add</code> adds the tier &lt;tierpool&gt; (the second one) to base pool &lt;pool&gt; (the first one). </p>
<p> Usage: </p>
<pre>ceph osd tier add &lt;poolname&gt; &lt;poolname&gt; {--force-nonempty}</pre>
<p>Subcommand <code>add-cache</code> adds a cache &lt;tierpool&gt; (the second one) of size &lt;size&gt; to existing pool &lt;pool&gt; (the first one). </p>
<p> Usage: </p>
<pre>ceph osd tier add-cache &lt;poolname&gt; &lt;poolname&gt; &lt;int[0-]&gt;</pre>
<p>Subcommand <code>cache-mode</code> specifies the caching mode for cache tier &lt;pool&gt;. </p>
<p> Usage: </p>
<pre>ceph osd tier cache-mode &lt;poolname&gt; none|writeback|forward|readonly|
readforward|readproxy</pre>
<p>Subcommand <code>remove</code> removes the tier &lt;tierpool&gt; (the second one) from base pool &lt;pool&gt; (the first one). </p>
<p> Usage: </p>
<pre>ceph osd tier remove &lt;poolname&gt; &lt;poolname&gt;</pre>
<p>Subcommand <code>remove-overlay</code> removes the overlay pool for base pool &lt;pool&gt;. </p>
<p> Usage: </p>
<pre>ceph osd tier remove-overlay &lt;poolname&gt;</pre>
<p>Subcommand <code>set-overlay</code> set the overlay pool for base pool &lt;pool&gt; to be &lt;overlaypool&gt;. </p>
<p> Usage: </p>
<pre>ceph osd tier set-overlay &lt;poolname&gt; &lt;poolname&gt;</pre>
<p>Subcommand <code>tree</code> prints OSD tree. </p>
<p> Usage: </p>
<pre>ceph osd tree {&lt;int[0-]&gt;}</pre>
<p>Subcommand <code>unpause</code> unpauses osd. </p>
<p> Usage: </p>
<pre>ceph osd unpause</pre>
<p>Subcommand <code>unset</code> unsets &lt;key&gt;. </p>
<p> Usage: </p>
<pre>ceph osd unset full|pause|noup|nodown|noout|noin|nobackfill|
norebalance|norecover|noscrub|nodeep-scrub|notieragent</pre>
<h3>pg</h3>
<p>It is used for managing the placement groups in OSDs. It uses some additional subcommands. </p>
<p> Subcommand <code>debug</code> shows debug info about pgs. </p>
<p> Usage: </p>
<pre>ceph pg debug unfound_objects_exist|degraded_pgs_exist</pre>
<p>Subcommand <code>deep-scrub</code> starts deep-scrub on &lt;pgid&gt;. </p>
<p> Usage: </p>
<pre>ceph pg deep-scrub &lt;pgid&gt;</pre>
<p>Subcommand <code>dump</code> shows human-readable versions of pg map (only &#8216;all&#8217; valid with plain). </p>
<p> Usage: </p>
<pre>ceph pg dump {all|summary|sum|delta|pools|osds|pgs|pgs_brief} [{all|summary|sum|delta|pools|osds|pgs|pgs_brief...]}</pre>
<p>Subcommand <code>dump_json</code> shows human-readable version of pg map in json only. </p>
<p> Usage: </p>
<pre>ceph pg dump_json {all|summary|sum|delta|pools|osds|pgs|pgs_brief} [{all|summary|sum|delta|pools|osds|pgs|pgs_brief...]}</pre>
<p>Subcommand <code>dump_pools_json</code> shows pg pools info in json only. </p>
<p> Usage: </p>
<pre>ceph pg dump_pools_json</pre>
<p>Subcommand <code>dump_stuck</code> shows information about stuck pgs. </p>
<p> Usage: </p>
<pre>ceph pg dump_stuck {inactive|unclean|stale|undersized|degraded [inactive|unclean|stale|undersized|degraded...]}
{&lt;int&gt;}</pre>
<p>Subcommand <code>force_create_pg</code> forces creation of pg &lt;pgid&gt;. </p>
<p> Usage: </p>
<pre>ceph pg force_create_pg &lt;pgid&gt;</pre>
<p>Subcommand <code>getmap</code> gets binary pg map to -o/stdout. </p>
<p> Usage: </p>
<pre>ceph pg getmap</pre>
<p>Subcommand <code>ls</code> lists pg with specific pool, osd, state </p>
<p> Usage: </p>
<pre>ceph pg ls {&lt;int&gt;} {active|clean|down|replay|splitting|
scrubbing|scrubq|degraded|inconsistent|peering|repair|
recovery|backfill_wait|incomplete|stale| remapped|
deep_scrub|backfill|backfill_toofull|recovery_wait|
undersized [active|clean|down|replay|splitting|
scrubbing|scrubq|degraded|inconsistent|peering|repair|
recovery|backfill_wait|incomplete|stale|remapped|
deep_scrub|backfill|backfill_toofull|recovery_wait|
undersized...]}</pre>
<p>Subcommand <code>ls-by-osd</code> lists pg on osd [osd] </p>
<p> Usage: </p>
<pre>ceph pg ls-by-osd &lt;osdname (id|osd.id)&gt; {&lt;int&gt;}
{active|clean|down|replay|splitting|
scrubbing|scrubq|degraded|inconsistent|peering|repair|
recovery|backfill_wait|incomplete|stale| remapped|
deep_scrub|backfill|backfill_toofull|recovery_wait|
undersized [active|clean|down|replay|splitting|
scrubbing|scrubq|degraded|inconsistent|peering|repair|
recovery|backfill_wait|incomplete|stale|remapped|
deep_scrub|backfill|backfill_toofull|recovery_wait|
undersized...]}</pre>
<p>Subcommand <code>ls-by-pool</code> lists pg with pool = [poolname | poolid] </p>
<p> Usage: </p>
<pre>ceph pg ls-by-pool &lt;poolstr&gt; {&lt;int&gt;} {active|
clean|down|replay|splitting|
scrubbing|scrubq|degraded|inconsistent|peering|repair|
recovery|backfill_wait|incomplete|stale| remapped|
deep_scrub|backfill|backfill_toofull|recovery_wait|
undersized [active|clean|down|replay|splitting|
scrubbing|scrubq|degraded|inconsistent|peering|repair|
recovery|backfill_wait|incomplete|stale|remapped|
deep_scrub|backfill|backfill_toofull|recovery_wait|
undersized...]}</pre>
<p>Subcommand <code>ls-by-primary</code> lists pg with primary = [osd] </p>
<p> Usage: </p>
<pre>ceph pg ls-by-primary &lt;osdname (id|osd.id)&gt; {&lt;int&gt;}
{active|clean|down|replay|splitting|
scrubbing|scrubq|degraded|inconsistent|peering|repair|
recovery|backfill_wait|incomplete|stale| remapped|
deep_scrub|backfill|backfill_toofull|recovery_wait|
undersized [active|clean|down|replay|splitting|
scrubbing|scrubq|degraded|inconsistent|peering|repair|
recovery|backfill_wait|incomplete|stale|remapped|
deep_scrub|backfill|backfill_toofull|recovery_wait|
undersized...]}</pre>
<p>Subcommand <code>map</code> shows mapping of pg to osds. </p>
<p> Usage: </p>
<pre>ceph pg map &lt;pgid&gt;</pre>
<p>Subcommand <code>repair</code> starts repair on &lt;pgid&gt;. </p>
<p> Usage: </p>
<pre>ceph pg repair &lt;pgid&gt;</pre>
<p>Subcommand <code>scrub</code> starts scrub on &lt;pgid&gt;. </p>
<p> Usage: </p>
<pre>ceph pg scrub &lt;pgid&gt;</pre>
<p>Subcommand <code>send_pg_creates</code> triggers pg creates to be issued. </p>
<p> Usage: </p>
<pre>ceph pg send_pg_creates</pre>
<p>Subcommand <code>set_full_ratio</code> sets ratio at which pgs are considered full. </p>
<p> Usage: </p>
<pre>ceph pg set_full_ratio &lt;float[0.0-1.0]&gt;</pre>
<p>Subcommand <code>set_nearfull_ratio</code> sets ratio at which pgs are considered nearly full. </p>
<p> Usage: </p>
<pre>ceph pg set_nearfull_ratio &lt;float[0.0-1.0]&gt;</pre>
<p>Subcommand <code>stat</code> shows placement group status. </p>
<p> Usage: </p>
<pre>ceph pg stat</pre>
<h3>quorum</h3>
<p>Enter or exit quorum. </p>
<p> Usage: </p>
<pre>ceph quorum enter|exit</pre>
<h3>quorum_status</h3>
<p>Reports status of monitor quorum. </p>
<p> Usage: </p>
<pre>ceph quorum_status</pre>
<h3>report</h3>
<p>Reports full status of cluster, optional title tag strings. </p>
<p> Usage: </p>
<pre>ceph report {&lt;tags&gt; [&lt;tags&gt;...]}</pre>
<h3>scrub</h3>
<p>Scrubs the monitor stores. </p>
<p> Usage: </p>
<pre>ceph scrub</pre>
<h3>status</h3>
<p>Shows cluster status. </p>
<p> Usage: </p>
<pre>ceph status</pre>
<h3>sync force</h3>
<p>Forces sync of and clear monitor store. </p>
<p> Usage: </p>
<pre>ceph sync force {--yes-i-really-mean-it} {--i-know-what-i-am-doing}</pre>
<h3>tell</h3>
<p>Sends a command to a specific daemon. </p>
<p> Usage: </p>
<pre>ceph tell &lt;name (type.id)&gt; &lt;args&gt; [&lt;args&gt;...]</pre>
<h3>version</h3>
<p>Show mon daemon version </p>
<p> Usage: </p>
<pre>ceph version</pre>
<h2>Options</h2>
<dl>
<dt><code>-i infile</code></p>
<dd>will specify an input file to be passed along as a payload with the command to the monitor cluster. This is only used for specific monitor commands.</p>
<dt><code>-o outfile</code></p>
<dd>will write any payload returned by the monitor cluster with its reply to outfile. Only specific monitor commands (e.g. osd getmap) return a payload.</p>
<dt><code>-c ceph.conf, &#8211;conf=ceph.conf</code></p>
<dd>Use ceph.conf configuration file instead of the default <code>/etc/ceph/ceph.conf</code> to determine monitor addresses during startup.</p>
<dt><code>&#8211;id CLIENT_ID, &#8211;user CLIENT_ID</code></p>
<dd>Client id for authentication.</p>
<dt><code>&#8211;name CLIENT_NAME, -n CLIENT_NAME</code></p>
<dd>Client name for authentication.</p>
<dt><code>&#8211;cluster CLUSTER</code></p>
<dd>Name of the Ceph cluster.</p>
<dt><code>&#8211;admin-daemon ADMIN_SOCKET</code></p>
<dd>Submit admin-socket commands.</p>
<dt><code>&#8211;admin-socket ADMIN_SOCKET_NOPE</code></p>
<dd>You probably mean &#8211;admin-daemon</p>
<dt><code>-s, &#8211;status</code></p>
<dd>Show cluster status.</p>
<dt><code>-w, &#8211;watch</code></p>
<dd>Watch live cluster changes.</p>
<dt><code>&#8211;watch-debug</code></p>
<dd>Watch debug events.</p>
<dt><code>&#8211;watch-info</code></p>
<dd>Watch info events.</p>
<dt><code>&#8211;watch-sec</code></p>
<dd>Watch security events.</p>
<dt><code>&#8211;watch-warn</code></p>
<dd>Watch warning events.</p>
<dt><code>&#8211;watch-error</code></p>
<dd>Watch error events.</p>
<dt><code>&#8211;version, -v</code></p>
<dd>Display version.</p>
<dt><code>&#8211;verbose</code></p>
<dd>Make verbose.</p>
<dt><code>&#8211;concise</code></p>
<dd>Make less verbose.</p>
<dt><code>-f {json,json-pretty,xml,xml-pretty,plain}, &#8211;format</code></p>
<dd>Format of output.</p>
<dt><code>&#8211;connect-timeout CLUSTER_TIMEOUT</code></p>
<dd>Set a timeout for connecting to the cluster.</dl>
<h2>Availability</h2>
<p><code>ceph</code> is part of Ceph, a massively scalable, open-source, distributed storage system. Please refer to the Ceph documentation at <i><a rel="nofollow" href="http://ceph.com/docs">http://ceph.com/docs</a></i> for more information.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-ceph-mon/">ceph-mon</a></code>(8), <code><a href="/docs/linux/man/8-ceph-osd/">ceph-osd</a></code>(8), <code><a href="/docs/linux/man/8-ceph-mds/">ceph-mds</a></code>(8)</p>
<h2>Copyright</h2>
<p>2010-2014, Inktank Storage, Inc. and contributors. Licensed under Creative Commons BY-SA</p>
