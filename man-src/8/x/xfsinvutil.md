---
title: "xfsinvutil(8)"
name: "xfsinvutil"
section: "8"
letter: "x"
url: "/docs/linux/man/8-xfsinvutil/"
description: "xfsinvutil – xfsdump inventory database checking and pruning utility"
---

<p>xfsinvutil &#8211; xfsdump inventory database checking and pruning utility</p>
<h2>Synopsis</h2>
<pre><code>xfsinvutil</code> [-F|-i] [-m <i>media_label</i>] -M <i>mount_point</i> <i>mm/dd/yyyy</i>
<code>xfsinvutil</code> [-F|-i] [-m <i>media_label</i>] -u <i>UUID</i> <i>mm/dd/yyyy</i>
<code>xfsinvutil</code> [-F] -s <i>SESSION_ID</i>
<code>xfsinvutil</code> -i
<code>xfsinvutil</code> -C</pre>
<h2>Description</h2>
<p><i>xfsdump </i> maintains an online dump inventory in <i>/var/lib/xfsdump/inventory</i>. The <code>-I</code> option of xfsdump displays the inventory contents hierarchically. The levels of the hierarchy are: filesystem, dump session, stream, and media file. </p>
<p> <i>xfsinvutil </i> is a utility to check this inventory database for consistency, to remove entries of dump sessions which may no longer be of relevance, and to browse the contents of the inventory. </p>
<p> The following command line options are available:</p>
<dl>
<dt><code>-F</code></p>
<dd>Don&#8217;t prompt the operator. When <i>xfsinvutil</i> encounters a matching dump session, <i>xfsinvutil</i> will normally ask the operator for permission to delete the entry. With this option the deletion is performed, no questions asked.</p>
<dt><code>-i</code></p>
<dd>Interactive mode. Causes <i>xfsinvutil</i> to run in a mode that will allow the operator to browse and modify the contents of the inventory. Please refer to the <code>Interactive Mode</code> section below for more information.</p>
<dt><code>-M</code> <i>mount_point mm/dd/yyyy</i></p>
<dd>Prunes dump sessions identified by the given mount point which were created prior to the specified date. Optionally <code>-m</code> may be be specified to further limit the matching dump sessions by media label. <i>xfsinvutil</i> will prompt the operator prior to pruning a dump session unless the <code>-F</code> or <code>-i</code> options are given.</p>
<dt><code>-u</code> <i>UUID mm/dd/yyyy</i></p>
<dd>Like <code>-M</code>, except the matching filesystem is specified using its universally unique identifier (UUID) instead of its mount point.</p>
<dt><code>-m</code> <i>media_label</i></p>
<dd>If specified, only sessions with at least one media file whose label matches this value will be eligible for pruning. This restriction is in addition to those imposed by the date and the <code>-M</code> or <code>-u</code> options. This option allows the pruning of all inventory references to media which may have been overwritten or lost. Note that this option does not apply to sessions with no media files.</p>
<dt><code>-s</code> <i>SESSION_ID</i></p>
<dd>Prunes the dump session identified by the given session id. <i>xfsinvutil</i> will prompt the operator prior to pruning a dump session unless the <code>-F</code> option is given.</p>
<dt><code>-C</code></p>
<dd>With this option, <i>xfsinvutil </i> performs consistency checks for all entries in the inventory database. It fixes any problems found. If no consistent entries are found , the corresponding inventory database file is removed.</dl>
<h3>Interactive Mode</h3>
<p>When run with <code>-i</code>, <i>xfsinvutil</i> will present the operator with a hierarchical representation of the <i>xfsdump</i> inventory. In this mode, the operator can use the arrow keys (or the <code>h</code> <code>j</code> <code>k</code> <code>l</code> keys) to navigate the inventory and also use the following keys and functionality:</p>
<dl>
<dt><code>+</code></p>
<dd>Expand a branch of the tree.</p>
<dt><code>&#8211;</code></p>
<dd>Collapse a branch of the tree.</p>
<dt><code>*</code></p>
<dd>Fully expand a branch of the tree.</p>
<dt><code>%</code></p>
<dd>Fully collapse a branch of the tree.</p>
<dt><code>h</code></p>
<dd>Move selection to the parent entry.</p>
<dt><code>l</code></p>
<dd>Move selection to the child entry.</p>
<dt><code>j</code></p>
<dd>Move selection to next entry.</p>
<dt><code>k</code></p>
<dd>Move selection to previous entry.</p>
<dt><code>d</code></p>
<dd>Mark the current record, and all sub-records, to be deleted.</p>
<dt><code>u</code></p>
<dd>Clear the current record and all parent records from being deleted.</p>
<dt><code>i</code></p>
<dd>Import another <i>xfsdump</i> inventory.</p>
<dt><code>?</code></p>
<dd>Show help window.</p>
<dt><code>x</code></p>
<dd>Commit any changes made to the inventory, and exit the program.</p>
<dt><code>q</code></p>
<dd>Exit the program without committing any changes to the inventory.</dl>
<p> Inventories from other hosts can be imported to create a larger common inventory. It is recommended that the contents of <i>/var/lib/xfsdump/inventory</i> on the remote host be copied to a temporary local directory prior to running <i>xfsinvutil</i>. When <i>xfsinvutil</i> is run in interactive mode, and the operator hits <code>i</code>, they will be prompted for the path to the inventory to be imported. <i>xfsinvutil</i> will then add the contents of the imported inventory to the main window, and all entries will be marked as imported. The operator can then delete any of these entries that are not to be imported. When the operator commits the changes, <i>xfsinvutil</i> will import any entries which were not marked as deleted. Deleted entries are not actually deleted from the original imported inventory.</p>
<h2>Notes</h2>
<h3>Inventory</h3>
<p>Each dump session updates an inventory database in <i>/var/lib/xfsdump/inventory</i>. <i>xfsdump</i> uses the inventory to determine the base of incremental and resumed dumps. </p>
<p> This database can be displayed by invoking <i>xfsdump</i> with the <code>-I</code> option. The display uses tabbed indentation to present the inventory hierarchically. The first level is filesystem. The second level is session. The third level is media stream (currently only one stream is supported). The fourth level lists the media files sequentially composing the stream.</p>
<h2>Files</h2>
<dl>
<dt>/var/lib/xfsdump/inventory</p>
<dd>dump inventory database</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-xfsdump/">xfsdump</a>(8), <a href="/docs/linux/man/8-xfsrestore/">xfsrestore</a>(8). </p>
