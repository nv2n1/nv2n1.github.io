---
title: "amanda-conf(5)"
name: "amanda-conf"
section: "5"
letter: "a"
url: "/docs/linux/man/5-amanda-conf/"
description: "amanda.conf – Main configuration file for Amanda, the Advanced Maryland Automatic Network Disk Archiver"
---

<p>amanda.conf &#8211; Main configuration file for Amanda, the Advanced Maryland Automatic Network Disk Archiver</p>
<h2>Description</h2>
<p><code><a href="/docs/linux/man/5-amanda-conf/">amanda.conf</a></code>(5) is the main configuration file for Amanda. This manpage lists the relevant sections and parameters of this file for quick reference. </p>
<p> The file <code>&lt;CONFIG_DIR&gt;/&lt;config&gt;/amanda.conf</code> is loaded.</p>
<h2>Syntax</h2>
<p>There are a number of configuration parameters that control the behavior of the Amanda programs. All have default values, so you need not specify the parameter in <code>amanda.conf</code> if the default is suitable.</p>
<h3>Comments</h3>
<p>Lines starting with # are ignored, as are blank lines. Comments may be placed on a line with a directive by starting the comment with a #. The remainder of the line is ignored.</p>
<h3>Keywords And Identifiers</h3>
<p>Keywords are case insensitive, i.e. <code>mailto</code> and <code>MailTo</code> are treated the same. Also, the characters &#8216;<code>&#8211;</code>&#8216; and &#8216;<code>_</code>&#8216; are interchangeable in all predefined Amanda keywords: <code>device_property</code> and <code>device-property</code> have the same meaning. This manpage uses the dashed versions, but the underscored versions will be accepted for backward compatibility </p>
<p> Identifiers are names which are defined in the configuration itself, such as dumptypes or interfaces. Identifiers are are case-insensitive, but sensitive to &#8216;<code>&#8211;</code>&#8216; vs. &#8216;<code>_</code>&#8216;. Identifiers should be quoted in the configuration file, although For historical reasons, the quotes are optional. </p>
<p> Strings are always quoted with double quotes (&quot;), and any double quotes or backslashes within the string are escaped with a backslash: </p>
<pre>tapelist &quot;/path/to/tapelist&quot;
property &quot;escaped-string&quot; &quot;escaping: \ (backslash) and \&quot; (double-quote)&quot;</pre>
<p>To summarize, then: </p>
<pre> # QUOTES CASE -/_
logdir &quot;logs&quot; # required sensitive sensitive
send-amreport-on strange # prohibited insensitive insensitive
tapetype &quot;EXABYTE&quot; # optional insensitive sensitive
define dumptype &quot;dt&quot; { # optional insensitive sensitive
 &quot;dumptype-common&quot; # optional insensitive sensitive
 strategy noinc # prohibited insensitive insensitive
}</pre>
<h3>Value Suffixes</h3>
<p>Integer arguments may have one of the following (case insensitive) suffixes, some of which have a multiplier effect: </p>
<p> <code>b byte bytes</code></p>
<dl>
<dd>Some number of bytes.</dl>
<p> <code>bps</code></p>
<dl>
<dd>Some number of bytes per second.</dl>
<p> <code>k kb kbyte kbytes kilobyte kilobytes</code></p>
<dl>
<dd>Some number of kilobytes (bytes*1024).</dl>
<p> <code>kps kbps</code></p>
<dl>
<dd>Some number of kilobytes per second (bytes*1024). </p>
<p> It is the default multiplier for all size options.</dl>
<p> <code>m mb meg mbyte mbytes megabyte megabytes</code></p>
<dl>
<dd>Some number of megabytes (bytes*1024*1024).</dl>
<p> <code>mps mbps</code></p>
<dl>
<dd>Some number of megabytes per second (bytes*1024*1024).</dl>
<p> <code>g gb gbyte gbytes gigabyte gigabytes</code></p>
<dl>
<dd>Some number of gigabytes (bytes*1024*1024*1024).</dl>
<p> <code>t tb tbyte tbytes terabyte terabytes</code></p>
<dl>
<dd>Some number of terabytes (bytes*1024*1024*1024*1024).</dl>
<p> <code>tape tapes</code></p>
<dl>
<dd>Some number of tapes.</dl>
<p> <code>day days</code></p>
<dl>
<dd>Some number of days.</dl>
<p> <code>week weeks</code></p>
<dl>
<dd>Some number of weeks (days*7). </p>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font><br />
 The value <code>inf</code> may be used in most places where an integer is expected to mean an infinite amount. </p>
<p> Boolean arguments may have any of the values <code>1</code>, <code>y</code>, <code>yes</code>, <code>t</code>, <code>true</code> or <code>on</code> to indicate a true state, or <code>0</code>, <code>n</code>, <code>no</code>, <code>f</code>, <code>false</code> or <code>off</code> to indicate a false state. If no argument is given, <code>true</code> is assumed. </p>
</dl>
</dl>
<h3>Parameter Order</h3>
<p>In general, the order in which parameters occur in the configuration file does not matter, with the exception of subsection inheritance. For example, if dumptype &quot;normal-encrypt&quot; which inherits from dumptype &quot;normal&quot;, then &quot;normal&quot; must appear first in the configuration file.</p>
<h3>Strings</h3>
<p>Quoted strings in Amanda follow a common, C-like syntax. Printable characters and whitespace are kept as-is, except that the backslash character (\) is used as an escape character, and a double-quote ends the string. The allowed escape sequences are </p>
<pre> ESCAPE SEQUENCE BECOMES
 \ \
 \&quot; &quot;
 
 (newline)
 	 (tab)
  (carriage return)
  (form-feed)
 \1 - \7
  - \77
  - \377 (character specified in octal)</pre>
<p>Illegally quoted strings are handled on a &quot;best-effort&quot; basis, which may lead to unexpected results. </p>
<p> Examples: </p>
<pre>finserver &quot;/data/finance/XYZ Corp's \&quot;real\&quot; finances&quot; finance-high eth0 -1
property &quot;syspath&quot; &quot;C:\WINDOWS\SYSTEM&quot;</pre>
<h3>Subsections And Inheritance</h3>
<p>Amanda configuration files may include various <i>subsections</i>, each defining a set of configuration directives. Each type of subsection is described below. Note that all types of subsections can <i>inherit</i> from other subsections of the same type by naming the &quot;parent&quot; section in the &quot;child&quot; subsection. For example: </p>
<pre>define dumptype global {
 record yes
 index yes
}
define dumptype nocomp {
 global # inherit the parameters in dumptype 'global'
 compress none
}</pre>
<p>Note that multiple inheritance is also supported by simply naming multiple parent sections in a child. Parents are implicitly expanded in place in a child, and the last occurrence of each parameter takes precedence. For example, </p>
<pre>define tapetype par1 {
 comment &quot;Parent 1&quot;
 filemark 8k
 speed 300bps
 length 200M
}
define tapetype par2 {
 comment &quot;Parent 2&quot;
 filemark 16k
 speed 400bps
}
define tapetype child {
 par1
 par2
 filemark 32k
}</pre>
<p>In this example, &#8216;child&#8217; will have a filemark of 32k, a speed of 400bps, and a length of 200M.</p>
<h2>Global Parameters</h2>
<p><code>org</code> <i>string</i></p>
<dl>
<dd>Default: <i>&quot;daily&quot;</i>. A descriptive name for the configuration. This string appears in the Subject line of mail reports. Each Amanda configuration should have a different string to keep mail reports distinct.</dl>
<p> <code>mailer</code> <i>string</i></p>
<dl>
<dd>Default found by configure. A mail program that can send mail with &#8216;<i>MAILER -s &quot;subject&quot; user &lt; message_file</i>&#8216;.</dl>
<p> <code>mailto</code> <i>string</i></p>
<dl>
<dd>Default: none. A space separated list of recipients for mail reports. If not specified, amdump will not send any mail.</dl>
<p> <code>send-amreport-on</code> [ <code>all</code> | <code>strange</code> | <code>error</code> | <code>never</code> ]</p>
<dl>
<dd>Default: <code>all</code>. Specify which types of messages will trigger an email from amreport. amreport is used by amdump and amflush. </p>
<p> <code>all</code></p>
<dl>
<dd>Send an email on any message.</dl>
<p> <code>strange</code></p>
<dl>
<dd>Send an email on strange or error message. A strange message occurs when the dump succeeded, but returned one or more errors unknown to Amanda.</dl>
<p> <code>error</code></p>
<dl>
<dd>Send an email only on error messages.</dl>
<p> <code>never</code></p>
<dl>
<dd>Never send an email.</dl>
</dl>
<p> <code>report-use-media</code> <i>boolean</i></p>
<dl>
<dd>Default: <i>True</i> if <code>max-dle-by-volume</code> is not set, <i>False</i> if it is set. If the reporter must print the list of media used in the run.</dl>
<p> <code>report-next-media</code> <i>boolean</i></p>
<dl>
<dd>Default: <i>True</i> if <code>max-dle-by-volume</code> is not set, <i>False</i> if it is set. If the reporter must print the list of media expected for the next run.</dl>
<p> <code>max-dle-by-volume</code> <i>int</i></p>
<dl>
<dd>Default: <i>1000000000</i>. The maximum number of dle written to a single volume.</dl>
<p> <code>dumpcycle</code> <i>int</i></p>
<dl>
<dd>Default: <i>10 days</i>. The number of days in the backup cycle. Each disk will get a full backup at least this often. Setting this to zero tries to do a full backup each run. </p>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font><br />
 This parameter may also be set in a specific <code>dumptype</code> (see below). This value sets the default for all <code>dumptype</code>s so must appear in <code>amanda.conf</code> before any <code>dumptype</code>s are defined. </p>
</dl>
</dl>
<p> <code>runspercycle</code> <i>int</i></p>
<dl>
<dd>Default: <i>same as dumpcycle</i>. The number of amdump runs in <code>dumpcycle</code> days. A value of 0 means the same value as <code>dumpcycle</code>. A value of -1 means guess the number of runs from the <code><a href="/docs/linux/man/5-tapelist/">tapelist</a></code>(5) file, which is the number of tapes used in the last <code>dumpcycle</code> days / <code>runtapes</code>.</dl>
<p> <code>tapecycle</code> <i>int</i></p>
<dl>
<dd>Default: <i>15 tapes</i>. Specifies the number of &quot;active&quot; volumes &#8211; volumes that Amanda will not overwrite. While Amanda is always willing to write to a new volume, it refuses to overwrite a volume unless at least &#8216;<code>tapecycle</code> -1&#8242; volumes have been written since. </p>
<p> It is considered good administrative practice to set the <code>tapecycle</code> parameter slightly lower than the actual number of tapes in use. This allows the administrator to more easily cope with damaged or misplaced tapes or schedule adjustments that call for slight adjustments in the rotation order. </p>
<p> Note: Amanda is commonly misconfigured with <code>tapecycle</code> equal to the number of tapes per <code>dumpcycle</code>. In this misconfiguration, amanda may erase a full dump before a new one is completed. Recovery is then impossible. The <code>tapecycle</code> must be at least one tape larger than the number of tapes per dumpcycle. </p>
<p> The number of tapes per dumpcycle is calculated by multiplying the number of <code>amdump</code> runs per dump cycle <code>runspercycle</code> (the number of <code>amdump</code> runs per dump cycle) and <code>runtapes</code> (the number of tapes used per run). Typically <code>tapecycle</code> is set to two or four times the tapes per dumpcycle.</dl>
<p> <code>usetimestamps</code> <i>bool</i></p>
<dl>
<dd>Default: <code>Yes</code>. This option allows Amanda to track multiple runs per calendar day. The only reason one might disable it is that Amanda versions before 2.5.1 can&#8217;t read logfiles written when this option was enabled.</dl>
<p> <code>label-new-tapes</code> <i>string</i></p>
<dl>
<dd>Deprecated, use <code>autolabel</code> option with options <code>volume-error empty</code> to get equivalent behavior. </p>
<p> Default: not set. When set, this directive will cause Amanda to automatically write an Amanda tape label to any blank tape she encounters.</dl>
<p> <code>autolabel</code> <i>string</i> [<code>any</code>] [<code>other-config</code>] [<code>non-amanda</code>] [<code>volume-error</code>] [<code>empty</code>]</p>
<dl>
<dd>Default: not set. When set, this directive will cause Amanda to automatically write an Amanda tape label to most volume she encounters. This option is DANGEROUS because when set, Amanda may erase near-failing tapes or tapes accidentally loaded in the wrong slot. </p>
<p> When using this directive, specify the template for new tape labels. The template can contains many variables that are substituted by their values: </p>
<pre> $c : config name
 $o : org configuration
 $b : barcode of the volume
 $s : slot number, can specify a minimun number of digit:
 $3s to get '001'
 $m : meta label</pre>
<p>The template can contain some number of contiguous &#8216;%&#8217; characters, which will be replaced with a generated number. Be sure to specify enough &#8216;%&#8217; characters that you do not run out of tape labels. Example: <code>&quot;DailySet1-%%%&quot;</code>, <code>&quot;$c-%%%&quot;</code>, <code>&quot;$m-%%%&quot;</code>, <code>&quot;$m-$b&quot;</code> </p>
<p> The generared label can be used only if it match the <code>labelstr</code> setting. The volume will not be used if the generated label doesn&#8217;t match the <code>labelstr</code> setting. </p>
<p> Note that many devices cannot distinguish an empty tape from an error condition, so it may is often necessary to include <code>volume-error</code> as an autolabel condition. </p>
<p> <code>any</code></p>
<dl>
<dd>equivalent to &#8216;<code>other-config non-amanda volume-error empty</code>&#8216;</dl>
<p> <code>other-config</code></p>
<dl>
<dd>Label volumes with a valid Amanda label that do not match our <code>labelstr</code>. Danger: this may erase volumes from other Amanda configurations without warning!</dl>
<p> <code>non-amanda</code></p>
<dl>
<dd>Label volumes which do not start with data that resembles an Amanda header. Danger: this may erase volumes from other backup applications without warning!</dl>
<p> <code>volume-error</code></p>
<dl>
<dd>Label volumes where an error occurs while trying to read the label. Danger: this may erase arbitrary volumes due to transient errors.</dl>
<p> <code>empty</code></p>
<dl>
<dd>Label volumes where a read returns 0 bytes.</dl>
</dl>
<p> <code>meta-autolabel</code> <i>string</i></p>
<dl>
<dd>Default: not set. When set and if the changer support meta-label, this directive will cause Amanda to automatically add a meta-label to a meta-volume. </p>
<p> A meta-volume is a containers that contains many volumes, eg. a removable hard-disk for use with chg-disk, each hard disk have many slots (volume). The meta-label is the label to put on the meta-volume. </p>
<p> When using this directive, specify the template for new meta labels. The template can contains many variables that are substituted by their values: </p>
<pre> $c : config name
 $o : org configuration</pre>
<p>The template should contain some number of contiguous &#8216;%&#8217; characters, which will be replaced with a generated number. Be sure to specify enough &#8216;%&#8217; characters that you do not run out of meta labels. Example: <code>&quot;DailySet1-%%%&quot;</code>, <code>&quot;$o-%%%&quot;</code>,</dl>
<p> <code>dumpuser</code> <i>string</i></p>
<dl>
<dd>Default: <i>&quot;amanda&quot;</i>. The login name Amanda uses to run the backups. The backup client hosts must allow access from the tape server host as this user via <code>.rhosts</code> or <code>.amandahosts</code>, depending on how the Amanda software was built.</dl>
<p> <code>printer</code> <i>string</i></p>
<dl>
<dd>Printer to use when doing tape labels. See the <code>lbl-templ</code> <code>tapetype</code> option.</dl>
<p> <code>tapedev</code> <i>string</i></p>
<dl>
<dd>Default: <i>&quot;null:&quot;</i>. This parameter can either specify a device (explicitly or by referencing a device definition &#8211; see <code><a href="/docs/linux/man/7-amanda-devices/">amanda-devices</a></code>(7)) or a tape changer (explicitly or by referencing a device definition &#8211; see <code><a href="/docs/linux/man/7-amanda-changers/">amanda-changers</a></code>(7)).</dl>
<p> <code>device-property</code> <i>string</i> <i>string</i></p>
<dl>
<dd>These options can set various device properties. See <code><a href="/docs/linux/man/7-amanda-devices/">amanda-devices</a></code>(7) for more information on device properties and their syntax. Both strings are always quoted; the first string contains the name of the property to set, and the second contains its value. For example, to set a fixed block size of 128k, write: </p>
<pre>device-property &quot;BLOCK_SIZE&quot; &quot;128k&quot;</pre>
</dl>
<p> <code>property</code> [<code>append</code>] <i>string</i> <i>string</i>+</p>
<dl>
<dd>These options can set various properties, they can be used by third party software to store information in the configuration file. Both strings are quoted; the first string contains the name of the property to set, and the others contains its values. <code>append</code> keyword append the values to the list of values for that property.</dl>
<p> <code>tpchanger</code> <i>string</i></p>
<dl>
<dd>Default: not set. The tape changer to use. In most cases, only one of <code>tpchanger</code> or <code>tapedev</code> is specified, although for backward compatibility both may be specified if <code>tpchanger</code> gives the name of an old changer script. See <code><a href="/docs/linux/man/7-amanda-changers/">amanda-changers</a></code>(7) for more information on configuring changers.</dl>
<p> <code>interactivity</code> <i>string</i></p>
<dl>
<dd>Default: not set. The interactivity module Amanda should use to interact with the user. See <code><a href="/docs/linux/man/7-amanda-interactivity/">amanda-interactivity</a></code>(7) for a list of modules.</dl>
<p> <code>taperscan</code> <i>string</i></p>
<dl>
<dd>Default: traditional. The taperscan module amanda should use to find a tape to write to. See <code><a href="/docs/linux/man/7-amanda-taperscan/">amanda-taperscan</a></code>(7) for a list of modules.</dl>
<p> <code>changerdev</code> <i>string</i></p>
<dl>
<dd>Default: <i>&quot;dev/null&quot;</i>. A tape changer configuration parameter. Usage depends on the particular changer defined with the <code>tpchanger</code> option.</dl>
<p> <code>changerfile</code> <i>string</i></p>
<dl>
<dd>Default: <i>&quot;/usr/adm/amanda/log/changer-status&quot;</i>. A tape changer configuration parameter. Usage depends on the particular changer defined with the <code>tpchanger</code> option.</dl>
<p> <code>runtapes</code> <i>int</i></p>
<dl>
<dd>Default: <i>1</i>. The maximum number of tapes used in a single run. If a tape changer is not configured, this option is not used and should be commented out of the configuration file. </p>
<p> If a tape changer is configured, this may be set larger than one to let Amanda write to more than one tape. </p>
<p> Note that this is an upper bound on the number of tapes, and Amanda may use less.</dl>
<p> <code>maxdumpsize</code> <i>int</i></p>
<dl>
<dd>Default: <i></i><code>runtapes</code><i>*</i><i></i><code>tape-length</code>. Maximum number of bytes the planner will schedule for a run. </p>
<p> The default unit is Kbytes if it is not specified.</dl>
<p> <code>taperalgo</code> [ <code>first</code> | <code>firstfit</code> | <code>largest</code> | <code>largestfit</code> | <code>smallest</code> | <code>last</code> ]</p>
<dl>
<dd>Default: <code>first</code>. The algorithm used to choose which dump image to send to the taper. </p>
<p> <code>first</code></p>
<dl>
<dd>First in, first out.</dl>
<p> <code>firstfit</code></p>
<dl>
<dd>The first dump image that will fit on the current tape.</dl>
<p> <code>largest</code></p>
<dl>
<dd>The largest dump image.</dl>
<p> <code>largestfit</code></p>
<dl>
<dd>The largest dump image that will fit on the current tape.</dl>
<p> <code>smallest</code></p>
<dl>
<dd>The smallest dump image.</dl>
<p> <code>last</code></p>
<dl>
<dd>Last in, first out.</dl>
</dl>
<p> <code>taper-parallel-write</code> <i>int</i></p>
<dl>
<dd>Default: <i>1</i>. Amanda can write simultaneously up to that number of volume at any given time. The changer must have as many drives.</dl>
<p> <code>eject-volume</code> <i>int</i></p>
<dl>
<dd>Default: <i>no</i>. Set to <code>yes</code> if you want the volume to be ejected after Amanda wrote data to it. It works only with some changer and device.</dl>
<p> <code>labelstr</code> <i>string</i></p>
<dl>
<dd>Default: <i>&quot;.*&quot;</i>. The tape label constraint regular expression. All tape labels generated (see <code><a href="/docs/linux/man/8-amlabel/">amlabel</a></code>(8)) and used by this configuration must match the regular expression. If multiple configurations are run from the same tape server host, it is helpful to set their labels to different strings (for example, &quot;DAILY[0-9][0-9]*&quot; vs. &quot;ARCHIVE[0-9][0-9]*&quot;) to avoid overwriting each other&#8217;s tapes.</dl>
<p> <code>tapetype</code> <i>string</i></p>
<dl>
<dd>Default: <i>no default</i>. The type of tape drive associated with <code>tapedev</code> or <code>tpchanger</code>. This refers to one of the defined <code>tapetype</code>s in the config file (see below), which specify various tape parameters, like the <code>length</code>, <code>filemark</code> size, and <code>speed</code> of the tape media and device.</dl>
<p> <code>ctimeout</code> <i>int</i></p>
<dl>
<dd>Default: <i>30 seconds</i>. Maximum amount of time that <code>amcheck</code> will wait for each client host.</dl>
<p> <code>dtimeout</code> <i>int</i></p>
<dl>
<dd>Default: <i>1800 seconds</i>. Amount of idle time per disk on a given client that a <code>dumper</code> running from within <code>amdump</code> will wait before it fails with a data timeout error.</dl>
<p> <code>etimeout</code> <i>int</i></p>
<dl>
<dd>Default: <i>300 seconds</i>. Amount of time per estimate on a given client that the <code>planner</code> step of <code>amdump</code> will wait to get the dump size estimates (note: Amanda runs up to 3 estimates for each DLE). For instance, with the default of 300 seconds and four DLE&#8217;s, each estimating level 0 and level 1 on client A, <code>planner</code> will wait up to 40 minutes for that machine. A negative value will be interpreted as a total amount of time to wait per client instead of per disk.</dl>
<p> <code>connect-tries</code> <i>int</i></p>
<dl>
<dd>Default: <i>3</i>. How many times the server will try a connection.</dl>
<p> <code>req-tries</code> <i>int</i></p>
<dl>
<dd>Default: <i>3</i>. How many times the server will resend a REQ packet if it doesn&#8217;t get the ACK packet.</dl>
<p> <code>netusage</code> <i>int</i></p>
<dl>
<dd>Default: <i>80000 Kbps</i>. The maximum network bandwidth allocated to Amanda, in Kbytes per second. See also the <code>interface</code> section.</dl>
<p> <code>inparallel</code> <i>int</i></p>
<dl>
<dd>Default: <i>10</i>. The maximum number of backups that Amanda will attempt to run in parallel. Amanda will stay within the constraints of network bandwidth and holding disk space available, so it doesn&#8217;t hurt to set this number a bit high. Some contention can occur with larger numbers of backups, but this effect is relatively small on most systems.</dl>
<p> <code>displayunit</code> &quot;k|m|g|t&quot;</p>
<dl>
<dd>Default: <i>&quot;k&quot;</i>. The unit used to print many numbers, k=kilo, m=mega, g=giga, t=tera.</dl>
<p> <code>dumporder</code> <i>string</i></p>
<dl>
<dd>Default: <i>&quot;tttTTTTTTT&quot;</i>. The priority order of each dumper: </p>
<pre>s: smallest size
S: largest size
t: smallest time
T: largest time
b: smallest bandwidth
B: largest bandwidth</pre>
</dl>
<p> <code>maxdumps</code> <i>int</i></p>
<dl>
<dd>Default: <i>1</i>. The maximum number of backups from a single host that Amanda will attempt to run in parallel. See also the <code>inparallel</code> option. </p>
<p> Note that this parameter may also be set in a specific <code>dumptype</code> (see below). This value sets the default for all <code>dumptype</code>s so must appear in <code>amanda.conf</code> before any <code>dumptype</code>s are defined.</dl>
<p> <code>bumpsize</code> <i>int</i></p>
<dl>
<dd>Default: <i>10 Mbytes</i>. The minimum savings required to trigger an automatic bump from one incremental level to the next, expressed as size. If Amanda determines that the next higher backup level will be this much smaller than the current level, it will do the next level. The value of this parameter is used only if the parameter <i>bumppercent</i> is set to 0. </p>
<p> The default unit is Kbytes if it is not specified. </p>
<p> The global setting of this parameter can be overwritten inside of a dumptype-definition. </p>
<p> See also the options <code>bumppercent</code>, <code>bumpmult</code> and <code>bumpdays</code>.</dl>
<p> <code>bumppercent</code> <i>int</i></p>
<dl>
<dd>Default: <i>0</i>. The minimum savings required to trigger an automatic bump from one incremental level to the next, expressed as percentage of the current size of the DLE (size of current level 0). If Amanda determines that the next higher backup level will be this much smaller than the current level, it will do the next level. </p>
<p> If this parameter is set to 0, the value of the parameter <i>bumpsize</i> is used to trigger bumping. </p>
<p> The global setting of this parameter can be overwritten inside of a dumptype-definition. </p>
<p> See also the options <code>bumpsize</code>, <code>bumpmult</code> and <code>bumpdays</code>.</dl>
<p> <code>bumpmult</code> <i>float</i></p>
<dl>
<dd>Default: <i>1.5</i>. The bump size multiplier. Amanda multiplies <code>bumpsize</code> by this factor for each level. This prevents active filesystems from bumping too much by making it harder to bump to the next level. For example, with the default <code>bumpsize</code> and <code>bumpmult</code> set to 2.0, the bump threshold will be 10 Mbytes for level one, 20 Mbytes for level two, 40 Mbytes for level three, and so on. </p>
<p> The global setting of this parameter can be overwritten inside of a dumptype-definition.</dl>
<p> <code>bumpdays</code> <i>int</i></p>
<dl>
<dd>Default: <i>2 days</i>. To insure redundancy in the dumps, Amanda keeps filesystems at the same incremental level for at least <code>bumpdays</code> days, even if the other bump threshold criteria are met. </p>
<p> The global setting of this parameter can be overwritten inside of a dumptype-definition.</dl>
<p> <code>diskfile</code> <i>string</i></p>
<dl>
<dd>Default: <i>&quot;disklist&quot;</i>. The file name for the <i>disklist</i> file holding client hosts, disks and other client dumping information.</dl>
<p> <code>infofile</code> <i>string</i></p>
<dl>
<dd>Default: <i>&quot;/usr/adm/amanda/curinfo&quot;</i>. The file or directory name for the historical information database. If Amanda was configured to use DBM databases, this is the base file name for them. If it was configured to use text formated databases (the default), this is the base directory and within here will be a directory per client, then a directory per disk, then a text file of data.</dl>
<p> <code>logdir</code> <i>string</i></p>
<dl>
<dd>Default: <i>&quot;/usr/adm/amanda&quot;</i>. The directory for the <code>amdump</code> and <code>log</code> files.</dl>
<p> <code>indexdir</code> <i>string</i></p>
<dl>
<dd>Default <i>&quot;/usr/adm/amanda/index&quot;</i>. The directory where index files (backup image catalogues) are stored. Index files are only generated for filesystems whose <code>dumptype</code> has the <code>index</code> option enabled.</dl>
<p> <code>tapelist</code> <i>string</i></p>
<dl>
<dd>Default: <i>&quot;tapelist&quot;</i>. The file name for the active <code><a href="/docs/linux/man/5-tapelist/">tapelist</a></code>(5). Amanda maintains this file with information about the active set of tapes.</dl>
<p> <code>device-output-buffer-size</code> <i>int</i></p>
<dl>
<dd>Default: <i>1280k</i>. Controls the amount of memory used by Amanda to hold data as it is read from the network or disk before it is written to the output device. Higher values may be useful on fast tape drives and optical media. </p>
<p> The default unit is bytes if it is not specified.</dl>
<p> <code>tapebufs</code> <i>int</i></p>
<dl>
<dd>Default: <i>20</i>. This option is deprecated; use the <code>device-output-buffer-size</code> directive instead. <code>tapebufs</code> works the same way, but the number specified is multiplied by the device blocksize prior to use.</dl>
<p> <code>reserve</code> <i>int</i></p>
<dl>
<dd>Default: <i>100</i>. The part of holding-disk space that should be reserved for incremental backups if no tape is available, expressed as a percentage of the available holding-disk space (0-100). By default, when there is no tape to write to, degraded mode (incremental) backups will be performed to the holding disk. If full backups should also be allowed in this case, the amount of holding disk space reserved for incrementals should be lowered.</dl>
<p> <code>autoflush</code> <code>no</code>|<code>yes</code>|<code>all</code></p>
<dl>
<dd>Default: <code>no</code>. Whether an amdump run will flush the dumps from holding disk to tape. With <code>yes</code>, only dump matching the command line argument are flushed. With <code>all</code>, all dump are flushed.</dl>
<p> <code>amrecover-do-fsf</code> <i>bool</i></p>
<dl>
<dd>Deprecated; amrecover always uses fsf, and does not invoke amrestore. </p>
<p> Default: <code>on</code>. Amrecover will call amrestore with the -f flag for faster positioning of the tape.</dl>
<p> <code>amrecover-check-label</code> <i>bool</i></p>
<dl>
<dd>Deprecated; amrecover always checks the label, and does not invoke amrestore. </p>
<p> Default: <code>on</code>. Amrecover will call amrestore with the -l flag to check the label.</dl>
<p> <code>amrecover-changer</code> <i>string</i></p>
<dl>
<dd>Default: not set. Amrecover will use the changer if you use &#8216;settape &lt;string&gt;&#8217; and that string is the same as the <code>amrecover-changer</code> setting.</dl>
<p> <code>columnspec</code> <i>string</i></p>
<dl>
<dd>default: &quot;HostName=0:-12:12,Disk=1:-11:11,Level=1:-1:1,OrigKB=1:-7:0,OutKB=1:-7:0,Compress=1:-6:1,DumpTime=1:-7:7,Dumprate=1:-6:1,TapeTime=1:-6:6,TapeRate=1:-6:1&quot; </p>
<p> Defines the width of columns <code>amreport</code> should use. <i>String</i> is a comma (&#8216;,&#8217;) separated list of triples. Each triple consists of three parts which are separated by a equal sign (&#8216;=&#8217;) and a colon (&#8216;:&#8217;) (see the example). These four parts specify: </p>
<dl>
<dd>1. the name of the column, which may be: </p>
<pre> Compress (compression ratio)
 Disk (client disk name)
 DumpRate (dump rate in KBytes/sec)
 DumpTime (total dump time in hours:minutes)
 HostName (client host name)
 Level (dump level)
 OrigKB (original image size in KBytes)
 OutKB (output image size in KBytes)
 TapeRate (tape writing rate in KBytes/sec)
 TapeTime (total tape time in hours:minutes)</pre>
</dl>
<dl>
<dd>2. the amount of space to display before the column (used to get whitespace between columns).</dl>
<dl>
<dd>3. the width of the column itself. If set to a negative value, the width will be calculated on demand to fit the largest entry in this column.</dl>
<dl>
<dd>4. the precision of the column, number of digit after the decimal point for number.</dl>
<p> Here is an example: </p>
<pre>columnspec &quot;Disk=1:18,HostName=0:10,OrigKB=::2,OutKB=1:7&quot;</pre>
<p>The above will display the disk information in 18 characters and put one space before it. The hostname column will be 10 characters wide with no space to the left. The Original KBytes print 2 decimal digit. The output KBytes column is seven characters wide with one space before it.</dl>
<p> <code>includefile</code> <i>string</i></p>
<dl>
<dd>Default: <i>no default</i>. The name of an Amanda configuration file to include within the current file. Useful for sharing dumptypes, tapetypes and interface definitions among several configurations. Relative pathnames are relative to the configuration directory.</dl>
<p> <code>debug-days</code> <i>int</i></p>
<dl>
<dd>Default: <i>3</i>. The number of days the debug files are kept.</dl>
<p> <code>debug-auth</code> <i>int</i></p>
<dl>
<dd>Default: <i>0</i>. Debug level of the auth module</dl>
<p> <code>debug-event</code> <i>int</i></p>
<dl>
<dd>Default: <i>0</i>. Debug level of the event module</dl>
<p> <code>debug-holding</code> <i>int</i></p>
<dl>
<dd>Default: <i>0</i>. Debug level of the holdingdisk module</dl>
<p> <code>debug-protocol</code> <i>int</i></p>
<dl>
<dd>Default: <i>0</i>. Debug level of the protocol module</dl>
<p> <code>debug-planner</code> <i>int</i></p>
<dl>
<dd>Default: <i>0</i>. Debug level of the planner process</dl>
<p> <code>debug-driver</code> <i>int</i></p>
<dl>
<dd>Default: <i>0</i>. Debug level of the driver process</dl>
<p> <code>debug-dumper</code> <i>int</i></p>
<dl>
<dd>Default: <i>0</i>. Debug level of the dumper process</dl>
<p> <code>debug-chunker</code> <i>int</i></p>
<dl>
<dd>Default: <i>0</i>. Debug level of the chunker process</dl>
<p> <code>debug-taper</code> <i>int</i></p>
<dl>
<dd>Default: <i>0</i>. Debug level of the taper process</dl>
<p> <code>debug-recovery</code> <i>int</i></p>
<dl>
<dd>Default: <i>1</i>. Debug level of all recovery process</dl>
<p> <code>flush-threshold-dumped</code> <i>int</i></p>
<dl>
<dd>Default: <i>0</i>. Amanda will not begin writing data to a new volume until the amount of data on the holding disk is at least this percentage of the volume size. In other words, Amanda will not begin until the amount of data on the holding disk is greater than the tape length times this parameter. This parameter may be larger than 100%, for example to keep more recent dumps on the holding disk for faster recovery. </p>
<p> Needless to say, your holding disk must be big enough that this criterion could be satisfied. If the holding disk cannot be used for a particular dump (because, for example, there is no remaining holding space) then Amanda will disregard the constraint specified by this setting and start a new volume anyway. Once writing to a volume has begun, this constraint is not applied unless and until a new volume is needed. </p>
<p> The value of this parameter may not exceed than that of the <code>flush-threshold-scheduled</code> parameter.</dl>
<p> <code>flush-threshold-scheduled</code> <i>int</i></p>
<dl>
<dd>Default: <i>0</i>. Amanda will not begin writing data to a new volume until the sum of the amount of data on the holding disk and the estimated amount of data remaining to be dumped during this run is at least this percentage of the volume size. In other words, Amanda will not begin until the inequality h + s &gt; t &#215; d is satisfied, where h is the amount of data on the holding disk, s is the total amount of data scheduled for this run but not dumped yet, t is the capacity of a volume, and d is this parameter, expressed as a percentage. This parameter may be larger than 100%. </p>
<p> Needless to say, your holding disk must be big enough that this criterion could be satisfied. If the holding disk cannot be used for a particular dump (because, for example, there is no remaining holding space) then Amanda will disregard the constraint specified by this setting and start a new volume anyway. Once writing to a volume has begun, this constraint is not applied unless and until a new volume is needed. </p>
<p> The value of this parameter may not be less than that of the <code>flush-threshold-dumped</code> or <code>taperflush</code> parameters.</dl>
<p> <code>taperflush</code> <i>int</i></p>
<dl>
<dd>Default: <i>0</i>. At the end of a run, Amanda will start a new tape to flush remaining data if there is more data on the holding disk at the end of a run than this setting allows; the amount is specified as a percentage of the capacity of a single volume. In other words, at the end of a run, Amanda will begin a new tape if the inequality h &gt; t &#215; f is satisfied, where h is the amount of data remaining on the holding disk from this or previous runs, t is the capacity of a volume, and f is this parameter, expressed as a percentage. This parameter may be greater than 100%. </p>
<p> The value of this parameter may not exceed that of the <code>flush-threshold-scheduled</code> parameter.; <code>autoflush</code> must be set to &#8216;yes&#8217; if <code>taperflush</code> is greater than 0.</dl>
<p> <code>reserved-udp-port</code> <i>int</i>,<i>int</i></p>
<dl>
<dd>Default: &#8211;with-udpportrange or <i>512,1023</i>. Reserved udp port that will be used (bsd, bsdudp). Range is inclusive.</dl>
<p> <code>reserved-tcp-port</code> <i>int</i>,<i>int</i></p>
<dl>
<dd>Default: &#8211;with-low-tcpportrange or <i>512,1023</i>. Reserved tcp port that will be used (bsdtcp). Range is inclusive.</dl>
<p> <code>unreserved-tcp-port</code> <i>int</i>,<i>int</i></p>
<dl>
<dd>Default: &#8211;with-tcpportrange or <i>1024,65535</i>. Unreserved tcp port that will be used (bsd, bsdudp). Range is inclusive.</dl>
<p> <code>recovery-limit</code> [ <i>string</i> | <code>same-host</code> | <code>server</code>]</p>
<dl>
<dd>Default: none (no limitations). This parameter limits the hosts that may do recoveries. Hosts are identified by their authenticated peer name, as described in <code><a href="/docs/linux/man/7-amanda-auth/">amanda-auth</a></code>(7); if this is not available and the recovery-limit parameter is present, recovery will be denied. The arguments to the parameter are strings giving host match expressions (see <code><a href="/docs/linux/man/7-amanda-match/">amanda-match</a></code>(7)) or the special keywords <code>same-host</code> or <code>server</code>. The <code>same-host</code> keyword requires an exact match to the hostname of the DLE being recovered. The <code>server</code> keyword require the connection come from the fqdn of the server. Specifying no arguments at all will disable all recoveries from any host. </p>
<p> Note that match expressions can be constructed to be forgiving of e.g., fully-qualified vs. unqualified hostnames, but <code>same-host</code> requires an exact match. </p>
<p> The error messages that appear in amrecover are intentionally vague to avoid information leakage. Consult the amindexd debug log for more details on the reasons a recovery was rejected. </p>
<p> Recovery limits can be refined on a per-DLE basis using the dumptype parameter of the same name. Note that the default value will apply to any dumpfiles for disks which no longer appear in the disklist; thus leaving the global parameter at its default value but setting it for all DLEs is not sufficient to maintain secure backups.</dl>
<p> <code>tmpdir</code> <i>string</i></p>
<dl>
<dd>Default: none (system default). Set it to a directory with lots of free space if sort in amindexd fail with &#8216;No space left on device&#8217;.</dl>
<h2>Holdingdisk Section</h2>
<p>The <code>amanda.conf</code> file may define one or more holding disks used as buffers to hold backup images before they are written to tape. The syntax is: </p>
<pre>define holdingdisk <i>name</i> {
 <i>holdingdisk-option</i> <i>holdingdisk-value</i>
 ...
}</pre>
<p>The { must appear at the end of a line, and the } on its own line. </p>
<p> <i>Name</i> is a logical name for this holding disk. </p>
<p> The options and values are: </p>
<p> <code>comment</code> <i>string</i></p>
<dl>
<dd>Default: not set. A comment string describing this holding disk.</dl>
<p> <code>directory</code> <i>string</i></p>
<dl>
<dd>Default: <i>&quot;/dumps/amanda&quot;</i>. The path to this holding area.</dl>
<p> <code>use</code> <i>int</i></p>
<dl>
<dd>Default: <i>0 Gb</i>. Amount of space that can be used in this holding disk area. If the value is zero, all available space on the file system is used. If the value is negative, Amanda will use all available space minus that value.</dl>
<p> <code>chunksize</code> <i>int</i></p>
<dl>
<dd>Default: <i>1 Gb</i>. Holding disk chunk size. Dumps larger than the specified size will be stored in multiple holding disk files. The size of each chunk will not exceed the specified value. However, even though dump images are split in the holding disk, they are concatenated as they are written to tape, so each dump image still corresponds to a single continuous tape section. </p>
<p> The default unit is Kbytes if it is not specified. </p>
<p> If 0 is specified, Amanda will create holding disk chunks as large as ((INT_MAX/1024)-64) Kbytes. </p>
<p> Each holding disk chunk includes a 32 Kbyte header, so the minimum chunk size is 64 Kbytes (but that would be really silly). </p>
<p> Operating systems that are limited to a maximum file size of 2 Gbytes actually cannot handle files that large. They must be at least one byte less than 2 Gbytes. Since Amanda works with 32 Kbyte blocks, and to handle the final read at the end of the chunk, the chunk size should be at least 64 Kbytes (2 * 32 Kbytes) smaller than the maximum file size, e.g. 2047 Mbytes.</dl>
<h2>Dumptype Section</h2>
<p>The <code><a href="/docs/linux/man/5-amanda-conf/">amanda.conf</a></code>(5) file may define multiple sets of backup options and refer to them by name from the <code><a href="/docs/linux/man/5-disklist/">disklist</a></code>(5) file. For instance, one set of options might be defined for file systems that can benefit from high compression, another set that does not compress well, another set for file systems that should always get a full backup and so on. </p>
<p> A set of backup options are entered in a <code>dumptype</code> section, which looks like this: </p>
<pre>define dumptype &quot;<i>name</i>&quot; {
 <i>dumptype-option</i> <i>dumptype-value</i>
 ...
}</pre>
<p>The { must appear at the end of a line, and the } on its own line. </p>
<p> <i>Name</i> is the name of this set of backup options. It is referenced from the <code><a href="/docs/linux/man/5-disklist/">disklist</a></code>(5) file. </p>
<p> Some of the options in a <code>dumptype</code> section are the same as those in the main part of <code><a href="/docs/linux/man/5-amanda-conf/">amanda.conf</a></code>(5). The main option value is used to set the default for all <code>dumptype</code> sections. For instance, setting <code>dumpcycle</code> to 50 in the main part of the config file causes all following <code>dumptype</code> sections to start with that value, but the value may be changed on a section by section basis. Changes to variables in the main part of the config file must be done before (earlier in the file) any <code>dumptype</code>s are defined. </p>
<p> The dumptype options and values are: </p>
<p> <code>auth</code> <i>string</i></p>
<dl>
<dd>Default: <i>&quot;bsdtcp&quot;</i>. Type of authorization to perform between tape server and backup client hosts. See <code><a href="/docs/linux/man/7-amanda-auth/">amanda-auth</a></code>(7) for more detail.</dl>
<p> <code>amandad-path</code> <i>string</i></p>
<dl>
<dd>Default: <i>&quot;$libexec/amandad&quot;</i>. Specify the amandad path of the client, only use with rsh/ssh authentification.</dl>
<p> <code>client-username</code> <i>string</i></p>
<dl>
<dd>Default: <i>CLIENT_LOGIN</i>. Specify the username to connect on the client, only use with rsh/ssh authentification.</dl>
<p> <code>client-port</code> [ <i>int</i> | <i>string</i> ]</p>
<dl>
<dd>Default: <i>&quot;amanda&quot;</i>. Specifies the port to connect to on the client. It can be a service name or a numeric port number.</dl>
<p> <code>bumpsize</code> <i>int</i></p>
<dl>
<dd>Default: <i>10 Mbytes</i>. The minimum savings required to trigger an automatic bump from one incremental level to the next, expressed as size. If Amanda determines that the next higher backup level will be this much smaller than the current level, it will do the next level. The value of this parameter is used only if the parameter <i>bumppercent</i> is set to 0. </p>
<p> The default unit is Kbytes if it is not specified. </p>
<p> See also the options <code>bumppercent</code>, <code>bumpmult</code> and <code>bumpdays</code>.</dl>
<p> <code>bumppercent</code> <i>int</i></p>
<dl>
<dd>Default: <i>0</i>. The minimum savings required to trigger an automatic bump from one incremental level to the next, expressed as percentage of the current size of the DLE (size of current level 0). If Amanda determines that the next higher backup level will be this much smaller than the current level, it will do the next level. </p>
<p> If this parameter is set to 0, the value of the parameter <i>bumpsize</i> is used to trigger bumping. </p>
<p> See also the options <code>bumpsize</code>, <code>bumpmult</code> and <code>bumpdays</code>.</dl>
<p> <code>bumpmult</code> <i>float</i></p>
<dl>
<dd>Default: <i>1.5</i>. The bump size multiplier. Amanda multiplies <code>bumpsize</code> by this factor for each level. This prevents active filesystems from bumping too much by making it harder to bump to the next level. For example, with the default <code>bumpsize</code> and <code>bumpmult</code> set to 2.0, the bump threshold will be 10 Mbytes for level one, 20 Mbytes for level two, 40 Mbytes for level three, and so on.</dl>
<p> <code>bumpdays</code> <i>int</i></p>
<dl>
<dd>Default: <i>2 days</i>. To insure redundancy in the dumps, Amanda keeps filesystems at the same incremental level for at least <code>bumpdays</code> days, even if the other bump threshold criteria are met.</dl>
<p> <code>comment</code> <i>string</i></p>
<dl>
<dd>Default: not set. A comment string describing this set of backup options.</dl>
<p> <code>comprate</code> <i>float</i> [, <i>float</i> ]</p>
<dl>
<dd>Default: <i>0.50, 0.50</i>. The expected full and incremental compression factor for dumps. It is only used if Amanda does not have any history information on compression rates for a filesystem, so should not usually need to be set. However, it may be useful for the first time a very large filesystem that compresses very little is backed up.</dl>
<p> <code>compress</code> [ <code>none</code> | <code>client</code> | <code>server</code> ] [ <code>best</code> | <code>fast</code> | <code>custom</code> ]</p>
<dl>
<dd>Default: <code>client fast</code>. If Amanda does compression of the backup images, it can do so either on the backup client host before it crosses the network or on the tape server host as it goes from the network into the holding disk or to tape. Which place to do compression (if at all) depends on how well the dump image usually compresses, the speed and load on the client or server, network capacity, holding disk capacity, availability of tape hardware compression, etc. </p>
<p> For either type of compression, Amanda also allows the selection of three styles of compression. <code>best</code> is the best compression available, often at the expense of CPU overhead. <code>fast</code> is often not as good a compression as <code>best</code>, but usually less CPU overhead. Or to specify <code>custom</code> to use your own compression method. (See dumptype custom-compress in example/amanda.conf for reference) </p>
<p> So the <code>compress</code> options line may be one of: </p>
<p> compress none</p>
<dl>
<dd></dl>
<p> compress client fast</p>
<dl>
<dd></dl>
<p> compress client best</p>
<dl>
<dd></dl>
<p> compress client custom</p>
<dl>
<dd>Specify <code>client-custom-compress</code> &quot;PROG&quot; </p>
<p> PROG must not contain white space and it must accept -d for uncompress.</dl>
<p> compress server fast</p>
<dl>
<dd></dl>
<p> compress server best</p>
<dl>
<dd></dl>
<p> compress server custom</p>
<dl>
<dd>Specify <code>server-custom-compress</code> &quot;PROG&quot; </p>
<p> PROG must not contain white space and it must accept -d for uncompress.</dl>
<p> Note that some tape devices do compression and this option has nothing to do with whether that is used. If hardware compression is used (usually via a particular tape device name or <code>mt</code> option), Amanda (software) compression should be disabled.</dl>
<p> <code>client-custom-compress</code> <i>string</i></p>
<dl>
<dd>Default: none. The program to use to perform compression/decompression on the client; used with &quot;compress client custom&quot;. Must not contain whitespace. Must accept -d to uncompress.</dl>
<p> <code>server-custom-compress</code> <i>string</i></p>
<dl>
<dd>Default: none. The program to use to perform compression/decompression on the server; used with &quot;compress server custom&quot;. Must not contain whitespace. Must accept -d to uncompress.</dl>
<p> <code>dumpcycle</code> <i>int</i></p>
<dl>
<dd>Default: <i>10 days</i>. The number of days in the backup cycle. Each disk using this set of options will get a full backup at least this of ten. Setting this to zero tries to do a full backup each run.</dl>
<p> <code>encrypt</code> [ <code>none</code> | <code>client</code> | <code>server</code> ]</p>
<dl>
<dd>Default: not set. To encrypt backup images, it can do so either on the backup client host before it crosses the network or on the tape server host as it goes from the network into the holding disk or to tape. </p>
<p> So the <code>encrypt</code> options line may be one of: </p>
<p> encrypt none</p>
<dl>
<dd></dl>
<p> encrypt client</p>
<dl>
<dd>Specify client-encrypt &quot;PROG&quot; </p>
<p> PROG must not contain white space. </p>
<p> Specify client-decrypt-option &quot;decryption-parameter&quot; Default: &quot;-d&quot; </p>
<p> decryption-parameter must not contain white space. </p>
<p> (See dumptype client-encrypt-nocomp in example/amanda.conf for reference)</dl>
<p> encrypt server</p>
<dl>
<dd>Specify server-encrypt &quot;PROG&quot; </p>
<p> PROG must not contain white space. </p>
<p> Specify server-decrypt-option &quot;decryption-parameter&quot; Default: &quot;-d&quot; </p>
<p> decryption-parameter must not contain white space. </p>
<p> (See dumptype server-encrypt-fast in example/amanda.conf for reference)</dl>
<p> Note that current logic assumes compression then encryption during backup(thus decrypt then uncompress during restore). So specifying client-encryption AND server-compression is not supported. <i>amcrypt</i> which is a wrapper of <i>aespipe</i> is provided as a reference symmetric encryption program.</dl>
<p> <code>client-encrypt</code> <i>string</i></p>
<dl>
<dd>Default: none. The program to use to perform encryption/decryption on the client; used with &quot;encrypt client&quot;. Must not contain whitespace.</dl>
<p> <code>client-decrypt-option</code> <i>string</i></p>
<dl>
<dd>Default: -d. The option that can be passed to client-encrypt to make it decrypt instead. Must not contain whitespace.</dl>
<p> <code>server-encrypt</code> <i>string</i></p>
<dl>
<dd>Default: none. The program to use to perform encryption/decryption on the server; used with &quot;encrypt server&quot;. Must not contain whitespace.</dl>
<p> <code>server-decrypt-option</code> <i>string</i></p>
<dl>
<dd>Default: -d. The option that can be passed to server-encrypt to make it decrypt instead. Must not contain whitespace.</dl>
<p> <code>estimate</code> [ <code>client</code> | <code>calcsize</code> | <code>server</code> ]+</p>
<dl>
<dd>Default: <code>client</code>. Determine the way Amanda estimates the size of each DLE before beginning a backup. This is a list of acceptable estimate methods, and Amanda applies the first method supported by the application. The methods are: </p>
<p> client</p>
<dl>
<dd>Use the same program as the dumping program. This is the most accurate method to do estimates, but it can take a long time.</dl>
<p> calcsize</p>
<dl>
<dd>Use a faster program to do estimates, but the result is less accurate.</dl>
<p> server</p>
<dl>
<dd>Use only statistics from the previous few runs to give an estimate. This very quick, but the result is not accurate if your disk usage changes from day to day. If this method is specified, but the server does not have enough data to make an estimate, then the option is internally moved to the end of the list, thereby preferring &#8216;client&#8217; or &#8216;calcsize&#8217; in this case.</dl>
</dl>
<p> <code>exclude</code> [ <code>list</code> | <code>file</code> ][[<code>optional</code>][<code>append</code>][ <i>string</i> ]+]</p>
<dl>
<dd>Default: <code>file</code>. Exclude is the opposite of <code>include</code> and specifies files that will be excluded from the backup. The format of the exclude expressions depends on the application, and some applications do not support excluding files at all. </p>
<p> There are two exclude parameters, <code>exclude</code> <code>file</code> and <code>exclude</code> <code>list.</code> With <code>exclude</code> <code>file</code>, the <i>string</i> is an exclude expression. With <code>exclude</code> <code>list</code> , the <i>string</i> is a file name on the client containing <code>GNU-tar</code> exclude expressions. The path to the specified exclude list file, if present (see description of &#8216;optional&#8217; below), must be readable by the Amanda user. </p>
<p> All exclude expressions are concatenated in one file and passed to the application as an <code>&#8211;exclude-from</code> argument. </p>
<p> For <code>GNU-tar</code>, exclude expressions must always be specified as relative to the top-level directory of the DLE, and must start with &quot;./&quot;. See the manpages for individual applications for more information on supported exclude expressions. </p>
<p> With the <code>append</code> keyword, the <i>string</i> is appended to the current list, without it, the <i>string</i> overwrites the list. </p>
<p> If <code>optional</code> is specified for <code>exclude</code> <code>list</code>, then amcheck will not complain if the file doesn&#8217;t exist or is not readable. </p>
<p> For <code>exclude</code> <code>list</code>, if the file name is relative, the disk name being backed up is prepended. So if this is entered: </p>
<pre> exclude list &quot;.amanda.excludes&quot;</pre>
<p>the actual file used would be /var/.amanda.excludes for a backup of /var, /usr/local/.amanda.excludes for a backup of /usr/local, and so on.</dl>
<p> <code>holdingdisk</code> [ <code>never</code> | <code>auto</code> | <code>required</code> ]</p>
<dl>
<dd>Default: <code>auto</code>. Whether a holding disk should be used for these backups or whether they should go directly to tape. If the holding disk is a portion of another file system that Amanda is backing up, that file system should refer to a dumptype with <code>holdingdisk</code> set to <i>never</i> to avoid backing up the holding disk into itself. </p>
<p> <code>never</code>|no|false|off</p>
<dl>
<dd>Never use a holdingdisk, the dump will always go directly to tape. There will be no dump if you have a tape error.</dl>
<p> <code>auto</code>|yes|true|on</p>
<dl>
<dd>Use the holding disk, unless there is a problem with the holding disk, the dump won&#8217;t fit there or the medium doesn&#8217;t require spooling (e.g., VFS device)</dl>
<p> <code>required</code></p>
<dl>
<dd>Always dump to holdingdisk, never directly to tape. There will be no dump if it doesn&#8217;t fit on holdingdisk</dl>
</dl>
<p> <code>ignore</code> <i>boolean</i></p>
<dl>
<dd>Default: <code>no</code>. Whether disks associated with this backup type should be backed up or not. This option is useful when the <i>disklist</i> file is shared among several configurations, some of which should not back up all the listed file systems.</dl>
<p> <code>include</code> [ <code>list</code> | <code>file</code> ][[<code>optional</code>][<code>append</code>][ <i>string</i> ]+]</p>
<dl>
<dd>Default: <code>file</code> &quot;.&quot;. There are two include lists, <code>include file</code> and <code>include list.</code> With <code>include file</code> , the <i>string</i> is a glob expression. With <code>include list</code> , the <i>string</i> is a file name on the client containing glob expressions. </p>
<p> All include expressions are expanded by Amanda, concatenated in one file and passed to <code>GNU-tar</code> as a <code>&#8211;files-from</code> argument. They must start with &quot;./&quot; and contain no other &quot;/&quot;. </p>
<p> Include expressions must always be specified as relative to the head directory of the DLE. </p>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font><br />
 For globbing to work at all, even the limited single level, the top level directory of the DLE must be readable by the Amanda user. </p>
</dl>
<p> With the <code>append</code> keyword, the <i>string</i> is appended to the current list, without it, the <i>string</i> overwrites the list. </p>
<p> If <code>optional</code> is specified for <code>include list</code>, then amcheck will not complain if the file doesn&#8217;t exist or is not readable. </p>
<p> For <code>include list</code>, If the file name is relative, the disk name being backed up is prepended.</dl>
<p> <code>index</code> <i>boolean</i></p>
<dl>
<dd>Default: <code>no</code>. Whether an index (catalogue) of the backup should be generated and saved in <code>indexdir</code>. These catalogues are used by the <code>amrecover</code> utility.</dl>
<p> <code>kencrypt</code> <i>boolean</i></p>
<dl>
<dd>Default: <code>no</code>. Whether the backup image should be encrypted by Kerberos as it is sent across the network from the backup client host to the tape server host.</dl>
<p> <code>maxdumps</code> <i>int</i></p>
<dl>
<dd>Default: <i>1</i>. The maximum number of backups from a single host that Amanda will attempt to run in parallel. See also the main section parameter <code>inparallel</code>.</dl>
<p> <code>maxpromoteday</code> <i>int</i></p>
<dl>
<dd>Default: <i>10000</i>. The maximum number of day for a promotion, set it 0 if you don&#8217;t want promotion, set it to 1 or 2 if your disks get overpromoted.</dl>
<p> <code>max-warnings</code> <i>int</i></p>
<dl>
<dd>Default: <i>20</i>. The maximum number of error lines in the report for a dle. A value of &#8216;0&#8217; means unlimited. This is useful to reduce the size of the log file and the size of the report. All errors are put in separate files if a dle have more errors.</dl>
<p> <code>priority</code> [ <code>low</code> | <code>medium</code> | <code>high</code> ]</p>
<dl>
<dd>Default: <code>medium</code>. When there is no tape to write to, Amanda will do incremental backups in priority order to the holding disk. The priority may be high (2), medium (1), low (0) or a number of your choice.</dl>
<p> <code>program</code> [ <code>&quot;DUMP&quot;</code> | <code>&quot;GNUTAR&quot;</code> | <code>&quot;APPLICATION&quot;</code> ]</p>
<dl>
<dd>Default: <i>&quot;DUMP&quot;</i>. The type of backup to perform. Valid values are: </p>
<p> <code>&quot;DUMP&quot;</code></p>
<dl>
<dd>The native operating system backup program.</dl>
<p> <code>&quot;GNUTAR&quot;</code></p>
<dl>
<dd>To use GNU-tar or to do PC backups using Samba.</dl>
<p> <code>&quot;APPLICATION&quot;</code></p>
<dl>
<dd>To use an application, see the <i>application</i> option.</dl>
</dl>
<p> <code>application</code> <i>string</i></p>
<dl>
<dd>No default. Must be the name of an application if <i>program</i> is set to <i>APPLICATION</i>. See APPLICATION SECTION below.</dl>
<p> <code>script</code> <i>string</i></p>
<dl>
<dd>No default. Must be the name of a script. You can have many script. See SCRIPT SECTION below.</dl>
<p> <code>property</code> [<code>append</code>] <i>string</i> <i>string</i>+</p>
<dl>
<dd>These options can set various properties, they can be used by third party software to store information in the configuration file. Both strings are quoted; the first string contains the name of the property to set, and the others contains its values. <code>append</code> keyword append the values to the list of values for that property.</dl>
<p> <code>record</code> <i>boolean</i></p>
<dl>
<dd>Default: <code>yes</code>. Whether to ask the backup program to update its database (e.g. /etc/dumpdates for DUMP or /usr/local/var/amanda/gnutar-lists for GNUTAR) of time stamps. This is normally enabled for daily backups and turned off for periodic archival runs.</dl>
<p> <code>skip-full</code> <i>boolean</i></p>
<dl>
<dd>Default: <code>no</code>. If <code>true</code> and <code>planner</code> has scheduled a full backup, these disks will be skipped, and full backups should be run off-line on these days. It was reported that Amanda only schedules level 1 incrementals in this configuration; this is probably a bug.</dl>
<p> <code>skip-incr</code> <i>boolean</i></p>
<dl>
<dd>Default: <code>no</code>. If <code>true</code> and <code>planner</code> has scheduled an incremental backup, these disks will be skipped.</dl>
<p> <code>ssh-keys</code> <i>string</i></p>
<dl>
<dd>Default: not set. The key file the ssh auth will use, it must be the private key. If this parameter is not specified, then the default ssh key will be used.</dl>
<p> <code>starttime</code> <i>int</i></p>
<dl>
<dd>Default: not set. Backup of these disks will not start until after this time of day. The value should be hh*100+mm, e.g. 6:30PM (18:30) would be entered as 1830.</dl>
<p> <code>strategy</code> [ <code>standard</code> | <code>nofull</code> | <code>noinc</code> | <code>skip</code> | <code>incronly</code> ]</p>
<dl>
<dd>Default: <code>standard</code>. Strategy to use when planning what level of backup to run next. Values are: </p>
<p> <code>standard</code></p>
<dl>
<dd>The standard Amanda schedule.</dl>
<p> <code>nofull</code></p>
<dl>
<dd>Never do full backups, only level 1 incrementals.</dl>
<p> <code>noinc</code></p>
<dl>
<dd>Never do incremental backups, only full dumps.</dl>
<p> <code>skip</code></p>
<dl>
<dd>Treat this DLE as if it doesn&#8217;t exist (useful to disable DLEs when sharing the <i>disklist</i> file between multiple configurations). Skipped DLEs will not be checked or dumped, and will not be matched by disklist expressions.</dl>
<p> <code>incronly</code></p>
<dl>
<dd>Only do incremental dumps. <code>amadmin force</code> should be used to tell Amanda that a full dump has been performed off-line, so that it resets to level 1.</dl>
</dl>
<p> <code>allow-split</code> <i>bool</i></p>
<dl>
<dd>Default: true. If true, then dumps with this dumptype can be split on the storage media. If false, then the dump will be written in a single file on the media. See &quot;Dump Splitting Configuration&quot; below.</dl>
<p> <code>tape-splitsize</code> <i>int</i></p>
<dl>
<dd>Deprecated. See &quot;Dump Splitting Configuration&quot; below. </p>
<p> Default: not set. Split dump file on tape into pieces of a specified size. The default unit is Kbytes if it is not specified.</dl>
<p> <code>split-diskbuffer</code> <i>string</i></p>
<dl>
<dd>Deprecated. See &quot;Dump Splitting Configuration&quot; below. Default: not set. When dumping a split dump in PORT-WRITE mode (usually meaning &quot;no holding disk&quot;), buffer the split chunks to a file in the directory specified by this option.</dl>
<p> <code>fallback-splitsize</code> <i>int</i></p>
<dl>
<dd>Deprecated. See &quot;Dump Splitting Configuration&quot; below. </p>
<p> Default: <i>10M</i>. This specifies the part size used when no <code>split-diskbuffer</code> is specified, or when it is too small or does not exist, and thus the maximum amount of memory consumed for in-memory splitting. The default unit is Kbytes if it is not specified.</dl>
<p> <code>recovery-limit</code> [ <code>server</code> | <code>same-host</code> | <i>string</i> ]*</p>
<dl>
<dd>Default: global value. This parameter overrides the global <code>recovery-limit</code> parameter for DLEs of this dumptype.</dl>
<p> <code>dump-limit</code> [ <code>server</code> | <code>same-host</code> ]*</p>
<dl>
<dd>Default: <code>server</code>. Specify which host can initiate a backup of the dle. With <code>server</code>, the server can initiate a backup with the <code>amdump</code> command. With <code>same-host</code>, the client can initiate a backup with the <code>amdump_client</code> command.</dl>
<p> The following <code>dumptype</code> entries are predefined by Amanda: </p>
<pre>define dumptype &quot;no-compress&quot; {
 compress none
}
define dumptype &quot;compress-fast&quot; {
 compress client fast
}
define dumptype &quot;compress-best&quot; {
 compress client best
}
define dumptype &quot;srvcompress&quot; {
 compress server fast
}
define dumptype &quot;bsd-auth&quot; {
 auth &quot;bsd&quot;
}
define dumptype &quot;bsdtcp-auth&quot; {
 auth &quot;bsdtcp&quot;
}
define dumptype &quot;no-record&quot; {
 record no
}
define dumptype &quot;no-hold&quot; {
 holdingdisk no
}
define dumptype &quot;no-full&quot; {
 skip-full yes
} </pre>
<p>In addition to options in a <code>dumptype</code> section, one or more other <code>dumptype</code> names may be supplied as identifiers, which make this <code>dumptype</code> inherit options from other previously defined <code>dumptype</code>s. For instance, two sections might be the same except for the <code>record</code> option: </p>
<pre>define dumptype &quot;normal&quot; {
 comment &quot;Normal backup, no compression, do indexing&quot;
 no-compress
 index yes
 maxdumps 2
}
define dumptype &quot;testing&quot; {
 comment &quot;Test backup, no compression, do indexing, no recording&quot;
 &quot;normal&quot;
 record no
}</pre>
<p>Amanda provides a <code>dumptype</code> named <i>global</i> in the sample <code>amanda.conf</code> file that all <code>dumptype</code>s should reference. This provides an easy place to make changes that will affect every <code>dumptype</code>, although you must be careful that every dumptype explicitly inherits from the <i>global</i> dumptype &#8211; Amanda does not do so automatically.</p>
<h2>Tapetype Section</h2>
<p>The <code>amanda.conf</code> file may define multiple types of tape media and devices. The information is entered in a <code>tapetype</code> section, which looks like this in the config file: </p>
<pre>define tapetype &quot;<i>name</i>&quot; {
 <i>tapetype-option</i> <i>tapetype-value</i>
 ...
}</pre>
<p>The { must appear at the end of a line, and the } on its own line. </p>
<p> <i>Name</i> is the name of this type of tape medium/device. It is referenced from the <code>tapetype</code> option in the main part of the config file. </p>
<p> The tapetype options and values are: </p>
<p> <code>comment</code> <i>string</i></p>
<dl>
<dd>Default: not set. A comment string describing this set of tape information.</dl>
<p> <code>filemark</code> <i>int</i></p>
<dl>
<dd>Default: <i>1 kbytes</i>. How large a file mark (tape mark) is, measured in kbytes. If the size is only known in some linear measurement (e.g. inches), convert it to kbytes using the device density.</dl>
<p> <code>length</code> <i>int</i></p>
<dl>
<dd>Default: <i>2000 kbytes</i>. How much data will fit on a tape, expressed in kbytes. </p>
<p> Note that this value is only used by Amanda to schedule which backups will be run. Once the backups start, Amanda will continue to write to a tape until it gets an error, regardless of what value is entered for <code>length</code> (but see <code><a href="/docs/linux/man/7-amanda-devices/">amanda-devices</a></code>(7) for exceptions).</dl>
<p> <code>blocksize</code> <i>int</i></p>
<dl>
<dd>Default: <i>32 kbytes</i>. How much data will be written in each tape record, expressed in kbytes. This is similar to the <i>BLOCK_SIZE</i> device property, but if the blocksize is not a multiple of 1024 bytes, then this parameter cannot be used to specify it, and the property must be used instead.</dl>
<p> <code>readblocksize</code> <i>int</i></p>
<dl>
<dd>Default: <i>32 kytes</i> How much data will be read in each tape record. This can be used to override a device&#8217;s block size for reads only. This may be useful, for example, in reading a tape written with a 256k block size when Amanda is configured to use 128k blocks. This unusual feature is not supported by all operating systems and tape devices. </p>
<p> The default unit is Kbytes if it is not specified.</dl>
<p> <code>part-size</code> <i>int</i></p>
<dl>
<dd>If this is set to zero (default), then no splitting will take place, and the entire dump will fail, if end-of-medium is encountered before the dump is complete, unless the device property LEOM is true, and the device can detect EOM. See &quot;Dump Splitting Configuration&quot; below.</dl>
<p> <code>part-cache-type</code> [ <code>none</code> | <code>disk</code> | <code>memory</code> ]</p>
<dl>
<dd>Default: none. When part caching is required, this parameter specifies the type of caching that will be used. The options include no caching (<code>none</code>), in which case a failed part will cause the entire dump to fail; on-disk caching (<code>disk</code>), for which <code>part-cache-dir</code> must be set properly; and in-memory caching (<code>memory</code>), which on most systems severely restrains the size of the part that can be written. See &quot;Dump Splitting Configuration&quot; below.</dl>
<p> <code>part-cache-dir</code> <i>string</i></p>
<dl>
<dd>Default: none. The directory in which part-cache files can be written when caching on disk. See &quot;Dump Splitting Configuration&quot; below.</dl>
<p> <code>part-cache-max-size</code> <i>int</i></p>
<dl>
<dd>Default: none. The maximum part size to use when caching is in effect. This is used to limit the part size when disk or memory space for caching is constrained. This value must be greater than zero.</dl>
<p> <code>speed</code> <i>int</i></p>
<dl>
<dd>Default: <i>200 bps</i>. How fast the drive will accept data, in bytes per second. This parameter is NOT currently used by Amanda.</dl>
<p> <code>lbl-templ</code> <i>string</i></p>
<dl>
<dd>Default: not set. A PostScript template file used by <code>amreport</code> to generate labels. Several sample files are provided with the Amanda sources in the <i>example</i> directory. See the <code><a href="/docs/linux/man/8-amreport/">amreport</a></code>(8) man page for more information.</dl>
<p> In addition to options, another <code>tapetype</code> name may be supplied as an identifier, which makes this <code>tapetype</code> inherit options from another <code>tapetype</code>. For instance, the only difference between a DLT4000 tape drive using Compact-III tapes and one using Compact-IV tapes is the length of the tape. So they could be entered as: </p>
<pre>define tapetype &quot;DLT4000-III&quot; {
 comment &quot;DLT4000 tape drives with Compact-III tapes&quot;
 length 12500 mbytes # 10 Gig tapes with some compression
 filemark 2000 kbytes
 speed 1536 kps
}
define tapetype &quot;DLT4000-IV&quot; {
 &quot;DLT4000-III&quot;
 comment &quot;DLT4000 tape drives with Compact-IV tapes&quot;
 length 25000 mbytes # 20 Gig tapes with some compression
}</pre>
<h2>Interface Section</h2>
<p>The <code>amanda.conf</code> file may define multiple types of network interfaces. The information is entered in an <code>interface</code> section, which looks like this: </p>
<pre>define interface &quot;<i>name</i>&quot; {
 <i>interface-option</i> <i>interface-value</i>
 ...
}</pre>
<p>The { must appear at the end of a line, and the } on its own line. </p>
<p> <i>name</i> is the name of this type of network interface. It is referenced from the <i>disklist</i> file. </p>
<p> Note that these sections define network interface characteristics, not the actual interface that will be used. Nor do they impose limits on the bandwidth that will actually be taken up by Amanda. Amanda computes the estimated bandwidth each file system backup will take based on the estimated size and time, then compares that plus any other running backups with the limit as another of the criteria when deciding whether to start the backup. Once a backup starts, Amanda will use as much of the network as it can leaving throttling up to the operating system and network hardware. </p>
<p> The interface options and values are: </p>
<p> <code>comment</code> <i>string</i></p>
<dl>
<dd>Default: not set. A comment string describing this set of network information.</dl>
<p> <code>use</code> <i>int</i></p>
<dl>
<dd>Default: <i>80000 Kbps</i>. The speed of the interface in Kbytes per second.</dl>
<p> In addition to options, another <code>interface</code> name may be supplied as an identifier, which makes this <code>interface</code> inherit options from another <code>interface</code>. At the moment, this is of little use.</p>
<h2>Application Section</h2>
<p>The <code>amanda.conf</code> file may define multiple types of application. The information is entered in a <code>application</code> section, which looks like this: </p>
<pre>define application &quot;<i>name</i>&quot; {
 <i>application-option</i> <i>application-value</i>
 ...
}</pre>
<p>The { must appear at the end of a line, and the } on its own line. </p>
<p> <i>name</i> is the name of this type of application. It is referenced from the <i>dumptype</i> </p>
<p> The application options and values are: </p>
<p> <code>client-name</code> <i>string</i></p>
<dl>
<dd>No default, specifies an application name that is in the amanda-client.conf on the client. The setting from that application will be merged with the current application. If <code>client-name</code> is set then it is an error if that application is not defined on the client. </p>
<p> If <code>client-name</code> is not set then the merge is done with the application that have the name equal to the plugin. eg. if the plugin is &#8216;amgtar&#8217;, then the setting from the application &#8216;amgtar&#8217; is used if it is defined.</dl>
<p> <code>comment</code> <i>string</i></p>
<dl>
<dd>Default: not set. A comment string describing this application.</dl>
<p> <code>plugin</code> <i>string</i></p>
<dl>
<dd>No default. Must be set to the name of the program. This program must be in the <i>$libexecdir/amanda/application</i> directory on the client.</dl>
<p> <code>property</code> [<code>append</code>] [<code>priority</code>] <i>string</i> <i>string</i>+</p>
<dl>
<dd>No default. You can set property for the application, each application have a different set of property. Both strings are quoted; the first string contains the name of the property to set, and the others contains its values. <code>append</code> keyword append the values to the list of values for that property. <code>priority</code> keyword disallow the setting of that property on the client.</dl>
<h2>Script Section</h2>
<p>The <code>amanda.conf</code> file may define multiple types of script. The information is entered in a <code>script</code> section, which looks like this: </p>
<pre>define script &quot;<i>name</i>&quot; {
 <i>script-option</i> <i>script-value</i>
 ...
}</pre>
<p>The { must appear at the end of a line, and the } on its own line. </p>
<p> <i>name</i> is the name of this type of script. It is referenced from the <i>dumptype</i> </p>
<p> The script options and values are: </p>
<p> <code>client-name</code> <i>string</i></p>
<dl>
<dd>No default, specifies a script name that is in the amanda-client.conf on the client. The setting from that script will be merged with the currect script. If <code>client-name</code> is set then it is an error if that script is not defined on the client. </p>
<p> If <code>client-name</code> is not set then the merge is done with the script that have the name equal to the plugin. eg. if the plugin is &#8216;amlog-script&#8217;, then the setting from the script &#8216;amlog-script&#8217; is used.</dl>
<p> <code>comment</code> <i>string</i></p>
<dl>
<dd>Default: not set. A comment string describing this script.</dl>
<p> <code>plugin</code> <i>string</i></p>
<dl>
<dd>No default. Must be set to the name of the program. This program must be in the <i>$libexecdir/amanda/application</i> directory on the client and/or server.</dl>
<p> <code>order</code> <i>int</i></p>
<dl>
<dd>Default: <i>5000</i>. Scripts are executed in that order, it is useful if you have many scripts and they must be executed in a spefific order.</dl>
<p> <code>single-execution</code> <i>boolean</i></p>
<dl>
<dd>Default: <i>no</i>. The script is executed for each dle. If <i>yes</i>, the script is executed one time only.</dl>
<p> <code>execute-where</code> [ <code>client</code> | <code>server</code> ]</p>
<dl>
<dd>Default: <code>client</code>. Where the script must be executed, on the client or server.</dl>
<p> <code>execute-on</code> <i>execute_on</i> [,<i>execute_on</i>]*</p>
<dl>
<dd>No default. When the script must be executed, you can specify many of them: </p>
<p> <code>pre-amcheck</code></p>
<dl>
<dd>Execute before the amcheck command for all dle. Can only be run on server.</dl>
<p> <code>pre-dle-amcheck</code></p>
<dl>
<dd>Execute before the amcheck command for the dle.</dl>
<p> <code>pre-host-amcheck</code></p>
<dl>
<dd>Execute before the amcheck command for all dle for the client.</dl>
<p> <code>post-amcheck</code></p>
<dl>
<dd>Execute after the amcheck command for all dle. Can only be run on server.</dl>
<p> <code>post-dle-amcheck</code></p>
<dl>
<dd>Execute after the amcheck command for the dle.</dl>
<p> <code>post-host-amcheck</code></p>
<dl>
<dd>Execute after the amcheck command for all dle for the client.</dl>
<p> <code>pre-estimate</code></p>
<dl>
<dd>Execute before the estimate command for all dle. Can only be run on server.</dl>
<p> <code>pre-dle-estimate</code></p>
<dl>
<dd>Execute before the estimate command for the dle.</dl>
<p> <code>pre-host-estimate</code></p>
<dl>
<dd>Execute before the estimate command for all dle for the client.</dl>
<p> <code>post-estimate</code></p>
<dl>
<dd>Execute after the estimate command for all dle. Can only be run on server.</dl>
<p> <code>post-dle-estimate</code></p>
<dl>
<dd>Execute after the estimate command for the dle.</dl>
<p> <code>post-host-estimate</code></p>
<dl>
<dd>Execute after the estimate command for all dle for the client.</dl>
<p> <code>pre-backup</code></p>
<dl>
<dd>Execute before the backup command for all dle. Can only be run on server.</dl>
<p> <code>pre-dle-backup</code></p>
<dl>
<dd>Execute before the backup command for the dle.</dl>
<p> <code>pre-host-backup</code></p>
<dl>
<dd>Execute before the backup command for all dle for the client. It can&#8217;t be run on client, it must be run on server</dl>
<p> <code>post-backup</code></p>
<dl>
<dd>Execute after the backup command for all dle. Can only be run on server.</dl>
<p> <code>post-dle-backup</code></p>
<dl>
<dd>Execute after the backup command for the dle.</dl>
<p> <code>post-host-backup</code></p>
<dl>
<dd>Execute after the backup command for all dle for the client. It can&#8217;t be run on client, it must be run on server</dl>
<p> <code>pre-recover</code></p>
<dl>
<dd>Execute before any level is recovered.</dl>
<p> <code>post-recover</code></p>
<dl>
<dd>Execute after all levels are recovered.</dl>
<p> <code>pre-level-recover</code></p>
<dl>
<dd>Execute before each level recovery.</dl>
<p> <code>post-level-recover</code></p>
<dl>
<dd>Execute after each level recovery.</dl>
<p> <code>inter-level-recover</code></p>
<dl>
<dd>Execute between two levels of recovery.</dl>
<p> If you recover level 0 and 2 of the disk /usr with amrecover, it will execute: </p>
<pre>script --pre-recover
script --pre-level-recover --level 0
#recovering level 0
script --post-level-recover --level 0
script --inter-level-recover --level 0 --level 2
script --pre-level-recover --level 2
#recovering level 2
script --post-level-recover --level 2
script --post-recover</pre>
</dl>
<p> <code>property</code> [<code>append</code>] [<code>priority</code>] <i>string</i> <i>string</i>+</p>
<dl>
<dd>No default. You can set property for the script, each script have a different set of property. Both strings are quoted; the first string contains the name of the property to set, and the others contains its values. <code>append</code> keyword append the values to the list of values for that property. <code>priority</code> keyword disallow the setting of that property on the client.</dl>
<h2>Device Section</h2>
<p>Backend storage devices are specified in <code>amanda.conf</code> in the form of &quot;device&quot; sections, which look like this: </p>
<pre>define device <i>name</i> {
 commend &quot;<i>comment (optional)</i>&quot;
 tapedev &quot;<i>device-specifier</i>&quot;
 device-property &quot;<i>prop-name</i>&quot; &quot;<i>prop-value</i>&quot;
 ...
}</pre>
<p>The { must appear at the end of a line, and the } on its own line. </p>
<p> <i>name</i> is the user-specified name of this device. It is referenced from the global <i>tapedev</i> parameter. The <i>device-specifier</i> specifies the device name to use; see <code><a href="/docs/linux/man/7-amanda-devices/">amanda-devices</a></code>(7). As with most sections, the <i>comment</i> parmeter is optional and only for the user&#8217;s convenience. </p>
<p> An arbitrary number of <i>device-property</i> parameters can be specified. Again, see <code><a href="/docs/linux/man/7-amanda-devices/">amanda-devices</a></code>(7) for information on device properties.</p>
<h2>Changer Section</h2>
<p>Changers are described in <code>amanda.conf</code> in the form of &quot;changer&quot; sections, which look like this: </p>
<pre>define changer <i>name</i> {
 comment &quot;<i>comment (optional)</i>&quot;
 tpchanger &quot;<i>changer-spec</i>&quot;
 changerdev &quot;<i>device-name</i>&quot;
 changerfile &quot;<i>state-file</i>&quot;
 ...
}</pre>
<p>The { must appear at the end of a line, and the } on its own line. </p>
<p> <i>name</i> is the user-specified name of this device. The remaining parameters are specific to the changer type selected. </p>
<p> See <code><a href="/docs/linux/man/7-amanda-changers/">amanda-changers</a></code>(7) for more information on configuring changers.</p>
<h2>Interactivity Section</h2>
<p>The <code>amanda.conf</code> file may define multiple interactivyt methods, although only one will be used &#8211; that specified by the <code>interactivity</code> parameter. The information is entered in a <code>interactivity</code> section, which looks like this: </p>
<pre>define interactivity <i>name</i> {
 <i>interactivity-option</i> <i>interactivity-value</i>
 ...
}</pre>
<p>The { must appear at the end of a line, and the } on its own line. </p>
<p> <i>name</i> is the user-specified name of this interactivity. The remaining parameters are specific to the interactivity type selected. </p>
<p> The interactivity options and values are: </p>
<p> <code>comment</code> <i>string</i></p>
<dl>
<dd>Default: not set. A comment string describing this interactivity.</dl>
<p> <code>plugin</code> <i>string</i></p>
<dl>
<dd>No default. Must be set to the name of the interactivity module, as described in <code><a href="/docs/linux/man/7-amanda-interactivity/">amanda-interactivity</a></code>(7).</dl>
<p> <code>property</code> [<code>append</code>] <i>string</i> <i>string</i>+</p>
<dl>
<dd>No default. You can set arbitrary properties for the interactivity. Each interactivity module has a different set of properties. The first string contains the name of the property to set, and the others contains its values. All strings should be quoted. The <code>append</code> keyword appends the given values to an existing list of values for that property.</dl>
<p> See <code><a href="/docs/linux/man/7-amanda-interactivity/">amanda-interactivity</a></code>(7) for more information on configuring interactivity methods.</p>
<h2>Taperscan Section</h2>
<p>The <code>amanda.conf</code> file may define multiple taperscan methods, although only one will be used &#8211; that specified by the <code>taperscan</code> parameter. The information is entered in a <code>taperscan</code> section, which looks like this: </p>
<pre>define taperscan <i>name</i> {
 <i>taperscan-option</i> <i>taperscan-value</i>
 ...
}</pre>
<p>The { must appear at the end of a line, and the } on its own line. </p>
<p> <i>name</i> is the user-specified name of this taperscan. The remaining parameters are specific to the taperscan type selected. </p>
<p> The taperscan options and values are: </p>
<p> <code>comment</code> <i>string</i></p>
<dl>
<dd>Default: not set. A comment string describing this taperscan.</dl>
<p> <code>plugin</code> <i>string</i></p>
<dl>
<dd>No default. Must be set to the name of the taperscan module. See <code><a href="/docs/linux/man/7-amanda-taperscan/">amanda-taperscan</a></code>(7) for a list of defined taperscan modules.</dl>
<p> <code>property</code> [<code>append</code>] <i>string</i> <i>string</i>+</p>
<dl>
<dd>No default. Operates just like properties for interactivity methods, above.</dl>
<p> See <code><a href="/docs/linux/man/7-amanda-taperscan/">amanda-taperscan</a></code>(7) for more information on configuring taperscan.</p>
<h2>Dump Splitting Configuration</h2>
<p>Amanda can &quot;split&quot; dumps into parts while writing them to storage media. This allows Amanda to recover gracefully from a failure while writing a part to a volume, by simply selecting a new volume and re-writing the dump from the beginning of the failed part. Parts also allow Amanda to seek directly to the required data, although this functionality is not yet used. </p>
<p> In order to support re-writing from the beginning of a failed part, Amanda must have access to the contents of the part after it has been partially written. If the dump is being read from holding disk, then the part contents are availble there. Otherwise, the part must be cached, and this can be done memory or on disk. In either of the latter cases, the cache must have enough space to hold an entire part. </p>
<p> Because it is common for a single Amanda configuration to use both holding-disk (FILE-WRITE) and direct (known as PORT-WRITE) dumps, Amanda allows the configuration of different split sizes for the two cases. This allows, for example, for a part size appropriate to large tapes when performing FILE-WRITE dumps, with a part size limited by available disk or memory when performing PORT-WRITE dumps. </p>
<p> Selecting a proper split size is a delicate matter. If the parts are too large, substantial storage space may be wasted in failed parts. If too small, large dumps will be split into innumerable tiny dumpfiles, adding to restoration complexity; furthermore, an excess of filemarks will cause slower tape drive operation and reduce the usable space on tape. A good rule of thumb is 1/10 of the size of a volume of storage media. </p>
<p> In versions of Amanda through 3.1.*, splitting was controlled by the dumptype parameters <code>tape-splitsize</code>, <code>split-diskbuffer</code>, and <code>fallback-splitsize</code>. These keywords had confusing and non-intuitive interactions, and have since been deprecated. </p>
<p> If the deprecated keywords are not present, subsequent versions of Amanda use the dumptype parameter <code>allow-split</code> to control whether a DLE can be split, and the <i>tapetype</i> parameters <code>part-size</code>, <code>part-cache-type</code>, <code>part-cache-dir</code>, and <code>part-cache-max-size</code>. The <code>part-size</code> specifies the &quot;normal&quot; part size, while the <code>part-cache-*</code> parameters describe how to behave when caching is required (on PORT-WRITE). Full details on these parameters are given above.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-amanda/">amanda</a></code>(8), <code><a href="/docs/linux/man/5-amanda-client-conf/">amanda-client.conf</a></code>(5), <code><a href="/docs/linux/man/7-amanda-applications/">amanda-applications</a></code>(7), <code><a href="/docs/linux/man/7-amanda-auth/">amanda-auth</a></code>(7), <code><a href="/docs/linux/man/7-amanda-changers/">amanda-changers</a></code>(7), <code><a href="/docs/linux/man/7-amanda-devices/">amanda-devices</a></code>(7), <code><a href="/docs/linux/man/7-amanda-interactivity/">amanda-interactivity</a></code>(7), <code><a href="/docs/linux/man/7-amanda-scripts/">amanda-scripts</a></code>(7), <code><a href="/docs/linux/man/7-amanda-taperscan/">amanda-taperscan</a></code>(7) </p>
<p> The Amanda Wiki: : <a rel="nofollow" href="http://wiki.zmanda.com/">http://wiki.zmanda.com/</a></p>
<h2>Authors</h2>
<p><code>James da Silva</code> &lt;jds [at] amanda.org&gt; </p>
<p> <code>Stefan G. Weichinger</code> &lt;sgw [at] amanda.org&gt;</p>
